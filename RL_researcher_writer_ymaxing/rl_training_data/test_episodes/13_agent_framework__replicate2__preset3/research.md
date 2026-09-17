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

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What mathematical foundations underpin LangGraph checkpointing for auditability?</summary>

Phase: [EXPLORATION]

### Source [64]: https://reference.langchain.com/python/langgraph/checkpoints

Query: What mathematical foundations underpin LangGraph checkpointing for auditability?

Answer: LangGraph checkpointing uses UUIDs for unique identifiers, JSON serialization for data persistence, and database storage for state snapshots. It ensures auditability through time-travel debugging and state replay.

-----

Phase: [EXPLORATION]

### Source [65]: https://reference.langchain.com/python/langgraph/checkpoints

Query: What mathematical foundations underpin LangGraph checkpointing for auditability?

Answer: Checkpoints allow LangGraph agents to persist their state within and across multiple interactions. A checkpoint is a snapshot of the graph state at a given point in time, identified by a unique, monotonically increasing ID. Core concepts include Checkpoint as snapshot of graph state including channel values, channel versions, and version tracking per node; Thread as sequence of checkpoints identified by unique thread_id; Serde as serialization protocol defaulting to JsonPlusSerializer; Pending writes preserved when nodes fail.

-----

Phase: [EXPLORATION]

### Source [66]: https://reference.langchain.com/python/langgraph.checkpoint

Query: What mathematical foundations underpin LangGraph checkpointing for auditability?

Answer: Checkpoint is a snapshot of the graph state at a given point in time. Checkpoint tuple refers to an object containing checkpoint and the associated config, metadata and pending writes. BaseCheckpointSaver interface requires implementing put, put_writes, get_tuple, list, delete_thread, get_next_version. Pending writes stored when node fails mid-execution at superstep so resumption doesn't re-run successful nodes. Uses UUID draft version objects.

-----

Phase: [EXPLORATION]

### Source [67]: https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171

Query: What mathematical foundations underpin LangGraph checkpointing for auditability?

Answer: LangGraph Time Travel feature records every decision creating complete replayable audit trail. Captures each state transition transforming transient execution into replayable state machine. Engineers can trace failures to specific nodes, inspect intermediate state, re-execute from any checkpoint without rerunning entire workflow. Shifts to state driven engineering where workflow becomes deterministic, debuggable, and auditable.

-----

</details>

<details>
<summary>What scalability failure modes limit MCP in high-throughput research agents?</summary>

Phase: [EXPLORATION]

### Source [70]: https://arxiv.org/html/2603.05637v1

Query: What scalability failure modes limit MCP in high-throughput research agents?

Answer: Stability, Concurrency, & Performance (8 issues): Issues that affect the responsiveness or reliability of MCP servers and tools, and may manifest as CPU hangs, stalled or slow operations, connection reuse problems, and timeouts under heavy or concurrent workloads. These faults are primarily attributed to Scalability Limitations (37.5%), Algorithmic Non-Convergence (25%), Concurrency Handling (25%), and Memory Management (12.5%). Tool Interface & Argument Parsing (7 issues): Issues arising from mismatched or outdated tool interfaces, including incorrect function signatures, inconsistent parameter parsing, and discrepancies between expected and actual argument structures across MCP tools, FastAPI endpoints, and Command-Line Interface (CLI) wrappers. The most frequent dependency-related problems are: Missing Dependency (18.4%), Backward Incompatibility/Breaking Change (16.3%), Executable Missing/Not on PATH (14.3%), Version Pin Used as Regression Workaround (12.2%), and Version Mismatch/Conflict (8.2%). A typical case involved a dependency conflict preventing installation of the MCP server, where the user reported that ‘When trying to install the dicom-mcp with pip, the pynetdicom has a conflicting dependencies.’, resulting in a ResolutionImpossible error during environment setup. Response Size and Continuation Control (7 issues): Issues caused by tool responses that are excessively large, unbounded, or not properly segmented, including oversized JSON payloads, high-volume data objects, or long text outputs. These responses can exceed model context limits, trigger repeated continuation requests, or lead to degraded performance or stalls. Such faults arise from insufficient control over response size, streaming, or continuation boundaries.

-----

Phase: [EXPLORATION]

### Source [71]: https://www.microsoft.com/en-us/research/blog/tool-space-interference-in-the-mcp-era-designing-for-agent-compatibility-at-scale

Query: What scalability failure modes limit MCP in high-throughput research agents?

Answer: So, what does MCP have to say about horizontal integration? As catalogs grow, we expect some new failure modes to surface. This blog post introduces these as tool-space interference, and sketches both early observations and some pragmatic interventions to keep the society we’re building from stepping on its own feet. Tool-space interference describes situations where otherwise reasonable tools or agents, when co-present, reduce end-to-end effectiveness. This can look like longer action sequences, higher token cost, brittle recovery from errors, or, in some cases, task failure. While our survey provides informative initial results, it also faces significant limitations, the most obvious of which is authorization: many of the most popular MCP servers provide access to services that require authorization to use, hindering automated analysis. We are often still able to collect static features from these servers but are limited in the functional testing that can be done. One-size fits all (but some more than others). change the branch in the terminal, and an authorized MCP tool does not imply authorization in the browser. Thus, while any single agent might complete the task efficiently, the larger set of agents might misunderstand or interfere with one another, leading to additional rounds of debugging, or even complete task failure.

-----

Phase: [EXPLORATION]

### Source [72]: https://www.fiddler.ai/blog/mcp-agent-observability

Query: What scalability failure modes limit MCP in high-throughput research agents?

Answer: Issue Type | Detection Method | Root Cause Indicator | Resolution. Tool timeout | Span duration exceeds threshold | Incomplete tool spans in trace | Add retry logic or increase timeout. Context overflow | Token count metrics spike | Long tool responses in trace | Implement response summarization. Wrong tool selection | Semantic evaluation of tool choice | Shift in tool selection distribution | Adjust prompt engineering. Cascading failure | Error propagation across spans | Child span failures after parent error | Add circuit breakers between tools. MCP Agent Failure Modes That Don't Show Up in Standard Logs. Three outcomes drive the business case for MCP agent observability: 1. SLO Enforcement: Detect tool timeouts and fallback failures before they impact users, maintaining 99.9% uptime targets. 2. Cost Control: Attribute token spend to specific tools and workflows to optimize the most expensive paths. 3. Compliance: Generate audit trails that trace decisions through reasoning chains for regulatory review under GDPR, HIPAA, and SR 11-7. The Four MCP Agent Observability Signals You Actually Need. Four observability signals form the minimum viable telemetry for MCP agent operations. Each addresses a distinct failure mode you encounter when debugging production agents. End-to-End Tracing Across LLM and Tool Calls. Severity policies must be versioned and auditable because they constitute part of your governance framework. When regulators ask why a specific transaction was approved, you need to show not just the decision but the policy that governed it. Test and Qualify MCP Servers Before Adoption. Verify that each MCP server handles malformed requests, timeout scenarios, and rate limiting gracefully before production use. Profile p50, p95, and p99 latencies under realistic load to ensure the server meets your SLO requirements.

-----

</details>

<details>
<summary>What engineering challenges arise integrating AgentKit visual builder with MCP?</summary>

Phase: [EXPLORATION]

### Source [73]: https://mcp-server-langgraph.mintlify.app/comparisons/vs-openai-agentkit

Query: What engineering challenges arise integrating AgentKit visual builder with MCP?

Answer: Integrating AgentKit visual builder with MCP faces challenges in code customization, security risks, and data leakage. Migration complexity and workflow logic redesign are also significant hurdles. Limitations include limited to visual builder capabilities, code customization difficult, still in beta, less control over agent logic. Ideal strategy: Prototype with OpenAI AgentKit visual builder or MCP Server with LangGraph quick-start, then production with MCP Server with LangGraph for scale, security, and cost optimization. When NOT to use MCP Server with LangGraph: non-technical team, need visual workflow builder NOW (MCP is code-first only), OpenAI models sufficient, zero DevOps capacity, low volume. Recreate in LangGraph: Map Agent Builder nodes to LangGraph graph = StateGraph(AgentState), add nodes (agents/tools from AgentKit), add edges (connections from visual builder). Integrate Tools: Replace OpenAI connectors with MCP tools, Add LiteLLM for multi-provider support, Configure authentication (JWT).

-----

Phase: [EXPLORATION]

### Source [74]: https://labs.zenity.io/p/analyzing-the-security-risks-of-openai-s-agentkit

Query: What engineering challenges arise integrating AgentKit visual builder with MCP?

Answer: 3rd-party MCP servers not under the user’s control can have numerous security issues that can affect the clients connected to them such as Rug Pulls and Tool Poisoning. Publish - an agent can be made available to the outside world by clicking on the “Publish button”. It can then be integrated into ChatKit, and users can start interacting with it. If any private data is left unintentionally in the RAG, it can be made available to outside users interacting with the agent. Data leakage and data alteration possible. If a MCP server has a tool that can insert or edit the data store it’s connected to, a prompt injection can have hazardous effects. AgentKit components: Agent Builder (visual agent workflow builder with drag-and-drop, pre-built templates, versioning), Connector Registry (collection of MCP connectors), ChatKit. Private data leakage and/or corruption: Agent Builder allows connecting with File Search (vector database) and MCP Connectors (Gmail, DropBox, Stripe). Data leaked in several ways.

-----

Phase: [EXPLORATION]

### Source [75]: https://community.openai.com/t/how-to-get-started-with-agent-builder/1361280

Query: What engineering challenges arise integrating AgentKit visual builder with MCP?

Answer: For such MCP failures: unauth-ed remote MCPs will fail if a Transform is in front (Agent node → Transform → open MCP node), tool listing works, but tool calling fails. All testing in Preview mode chat. Same issue here. MCP server working perfectly fine in OpenAI Dashboard → Chat area. MCP server can be added to workflow area and its tools show, but instant generic error when trying to use the server. Getting errors trying to run preview on any models from 4o+. Fix your MCP connectors first. Its anything to do with MCP nodes. I am also getting errors from MCP Nodes. Specifically testing remote MCPs that require token authorization. Getting generic error toast. I have a agent setup of agent → if → transform → mcp, but it does not get past mcp step - it fails with the tool call. I see it call the list function of the MCP when building the agent, I see the logs on my server, but when running the agent in preview mode, never calls the MCP. I get this when it tries to run the tool, and never see my server hit. MCP: We experienced an error while running the workflow.

-----

</details>

<details>
<summary>How has robotics multi-agent coordination influenced current LLM agent framework designs?</summary>

Phase: [EXPLORATION]

### Source [77]: https://openaccess.thecvf.com/content/CVPR2025W/MEIS/papers/Chen_Multi-Agent_Systems_for_Robotic_Autonomy_with_LLMs_CVPRW_2025_paper.pdf

Query: How has robotics multi-agent coordination influenced current LLM agent framework designs?

Answer: In MAS-based robotics, each functional module is assigned to a distinct agent, facilitating information processing of different levels and agent-agent communication. By employing a multi-agent framework, robotic systems now walking into a future from a step over single-function demonstrations to fully autonomous systems capable of decision-making, task planning, and execution. For instance, robots guided by high-level instructions can autonomously determine task execution strategies. The RoCo framework, developed by Mandi, assigns individual robotic agents to each robotic arm in a multi-arm system, enabling coordination through agent interaction. Similarly, multi-agent robots are applicable in multi-robot collaboration systems, where inter-agent communication enhances efficiency and flexibility. MAS improves the adaptability of robotic applications across various subfields and allows them to be seamlessly blended. The proposed multi-agent framework can effectively design feasible robot configurations and produce corresponding control solutions when the task requirements are provided through natural language prompts with proper details.

-----

Phase: [EXPLORATION]

### Source [78]: https://arxiv.org/html/2502.14743v2

Query: How has robotics multi-agent coordination influenced current LLM agent framework designs?

Answer: RoCo (Mandi et al., 2024) develops a framework for multi-robot collaboration, which uses LLMs for both high-level communication and low-level motion planning, achieving better coordination in a variety of multi-robot tasks. ReAd (Zhang et al., 2024b) further improves coordination efficiency by using principled credit assignment of multiple agents. Chen et al. (2023) develops an LLM-based consensus-seeking method that can be applied as a high-level planner for multi-robot coordination tasks. For scientific research, Zheng et al. (2023) automates chemical experiments using multiple LLM agents, each tasked with specific experimental and analytic tasks, including making plans, literature retrieval, experiment execution, and result summary. The core idea behind using LLM-based MAS for decision-making is to harness the collective capabilities of multiple agents with diverse expertise. These agents, each acting as an expert, collaborate to address complex tasks efficiently, such as software development, embodied intelligence, and scientific research. Li et al. (2023b) introduces a novel communicative agent framework called CAMEL, which enables autonomous cooperation among agents through role-playing and inception prompting, aiming to achieve autonomously collaborative programming according to only users’ text instructions. A concurrent work (Qian et al., 2023) shares the same spirit with (Li et al., 2023b). Within the field of embodied intelligence, RoCo (Mandi et al., 2024) develops a framework for multi-robot collaboration, which uses LLMs for both high-level communication and low-level motion planning.

-----

Phase: [EXPLORATION]

### Source [79]: https://arxiv.org/html/2505.05762v1

Query: How has robotics multi-agent coordination influenced current LLM agent framework designs?

Answer: Unlike the single robotic module, MAS offers a more human-like and flexible approach to global robotic system design. In MAS-based robotics, each functional module is assigned to a distinct agent, facilitating information processing of different levels and agent-agent communication. By employing a multi-agent framework, robotic systems now walking into a future from a step over single-function demonstrations to fully autonomous systems capable of decision-making, task planning, and execution. Since the advent of Large Language Models (LLMs), various research based on such models have maintained significant academic attention and impact, especially in AI and robotics. In this paper, we propose a multi-agent framework with LLMs to construct an integrated system for robotic task analysis, mechanical design, and path generation. The framework includes three core agents: Task Analyst, Robot Designer, and Reinforcement Learning Designer. Outputs are formatted as multimodal results, such as code files or technical reports, for stronger understandability and usability. To evaluate generalizability comparatively, we conducted experiments with models from both GPT and DeepSeek. Results demonstrate that the proposed system can design feasible robots with control strategies when task requirements are provided through natural language prompts with proper details.

-----

Phase: [EXPLORATION]

### Source [80]: https://xue-guang.com/post/llm-marl

Query: How has robotics multi-agent coordination influenced current LLM agent framework designs?

Answer: The emergence of Large Language Models (LLMs) has catalyzed a paradigm shift in artificial intelligence, particularly in how we approach complex problem-solving through multi-agent systems. As we stand in May 2025, the field of LLM-based multi-agent cooperation has evolved from theoretical curiosity to practical reality, with implementations spanning software development, financial trading, robotics, and enterprise operations. The field has converged on several dominant architectural patterns. Centralized coordination employs a supervisor agent that manages and directs specialized worker agents, exemplified by AutoGen’s supervisor architecture and LangGraph’s supervisor tool-calling pattern (Analytics Vidhya, 2024). This approach provides clear control and coordination but can create bottlenecks. Decentralized systems enable peer-to-peer communication without central authority, as seen in CAMEL’s role-playing framework, offering greater resilience but increased coordination complexity. Hierarchical architectures implement multi-level supervision where supervisors manage other supervisors, supported by frameworks like LangGraph’s hierarchical teams and MegaAgent’s system-level parallelism.

-----

Phase: [EXPLORATION]

### Source [81]: https://arxiv.org/html/2402.01680v2

Query: How has robotics multi-agent coordination influenced current LLM agent framework designs?

Answer: Chen et al. (2023d) investigates communication challenges in scenarios involving a large number of robots, as assigning each robot an LLM will be costly and unpractical due to the long context. The study compares four communication frameworks, centralized, decentralized, and two hybrid models, to evaluate their effectiveness in coordinating complex multi-agent tasks. Yu et al. (2023) proposes Co-NavGPT for multi-robot cooperative visual target navigation, integrating LLM as a global planner to assign frontier goals to each robot. Chen et al. (2023b) proposes an LLM-based consensus-seeking framework, which can be applied as a cooperative planner to a multi-robot aggregation task. Li et al. (2023b) first proposes a simple role-play agent framework, which utilizes the interplay of two roles to realize autonomous programming based on one-sentence user instruction. It provides insights into the “cognitive” processes of communicative agents. Dong et al. (2023b) makes LLMs work as distinct “experts” for sub-tasks in software development, autonomously collaborating to generate code. Moreover, Qian et al. (2023) presents an end-to-end framework for software development, utilizing multiple agents for software development without incorporating advanced human teamwork experience. Hong et al. (2023) first incorporates human workflow insights for more controlled and validated performance. It encodes SOPs into prompts to enhance structured coordination. Dasgupta et al. (2023) first explores the potential to use LLM as an action planner for embedded agents. Mandi et al. (2023) introduces RoCo, a novel approach for multi-robot collaboration that uses LLMs for high-level communication and low-level path planning. Each robotic arm is equipped with an LLM, cooperating with inverse kinematics and collision checking. Experimental results demonstrate the adaptability and success of RoCo in collaborative tasks. Zhang et al. (2023c) presents CoELA, a Cooperative Embodied Language Agent, managing discussions and task planning in an LLM-MA setting. This challenging setting is featured with decentralized control, complex partial observation, costly communication, and multi-objective long-horizon tasks.

-----

</details>

<details>
<summary>What role are regulatory frameworks playing in enterprise choices between auditable and autonomous agent systems?</summary>

Phase: [EXPLORATION]

### Source [82]: https://vegavid.com/ai-agents-for-compliance-and-risk-management

Query: What role are regulatory frameworks playing in enterprise choices between auditable and autonomous agent systems?

Answer: Regulatory frameworks guide enterprises to choose auditable AI systems over autonomous ones to ensure compliance, traceability, and risk management. Audit trails and human oversight are essential for regulatory adherence. Autonomous agents introduce new risks that require specific governance frameworks. Vegavid designs AI agents around real regulatory frameworks, audit requirements, and operational constraints. Their agents help organizations manage regulatory obligations, identify potential risks early, and maintain audit-ready operations across regulated and high-risk environments. AI agents for compliance and risk management automate monitoring of regulations, assess risks, and enforce internal controls. They continuously analyze data, detect anomalies, and support compliance workflows. Benefits include early risk identification, reduced manual effort, improved audit readiness through automated evidence collection and traceability, and scalable risk management across systems, regions, and regulatory frameworks.

-----

Phase: [EXPLORATION]

### Source [83]: https://www.nice.com/agentic-ai/agentic-ai-governance-frameworks

Query: What role are regulatory frameworks playing in enterprise choices between auditable and autonomous agent systems?

Answer: Regulatory frameworks create tension between autonomy and oversight. The EU AI Act emphasizes meaningful human control, while business cases favor end-to-end automation. SOX controls require demonstrable access controls, and GDPR’s data minimization expects systems access only what’s necessary. Making agent permissions auditable satisfies security and compliance. Human-on-the-loop approaches suit medium-risk scenarios; human-in-the-loop for high-risk actions like loan approvals. Continuous oversight with anomaly detection, behavioral baselines, and kill-switches replaces static approvals. Organizations extend model risk management practices to agentic systems via AI ethics boards and compliance committees. Every action is logged for human-readable audit trails.

-----

Phase: [EXPLORATION]

### Source [84]: https://galileo.ai/blog/ai-agent-compliance-governance-audit-trails-risk-management

Query: What role are regulatory frameworks playing in enterprise choices between auditable and autonomous agent systems?

Answer: Regulatory compliance drives preference for auditable systems. NIST AI Risk Management Framework and ISO/IEC 42001 provide core vocabulary and auditable systems. Financial regulators treat missing traces as books-and-records violations, requiring logs of every autonomous decision. Penalties scale across jurisdictions; US companies prioritize federal frameworks while preparing for state-level rules. Regulators are pivoting from guidance to audits, with SEC and OCC examining AI governance. Risk escalates with sensitive data access and traceability gaps, with data breaches costing $4.3 million on average. Human verification is essential for high-stakes decisions. Proactive risk controls and established frameworks accelerate safe delivery.

-----

Phase: [EXPLORATION]

### Source [85]: https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/03/governance-nist-ai-agent-standards-agentic-governance-v1-csa-styled.pdf

Query: What role are regulatory frameworks playing in enterprise choices between auditable and autonomous agent systems?

Answer: NIST AI RMF provides risk-based analytical model for identifying, assessing, and managing AI risks, while ISO 42001 provides management system infrastructure for operationalizing decisions. ISO 42001 certification appears in enterprise procurement and regulatory positioning for EU AI Act conformity. NIST standards are voluntary, reflecting its role in U.S. standards development without compliance burden. No U.S. federal regulation mandates AI RMF adoption, though agencies reference it in guidance. The framework maps to ISO 42001 controls for integrated implementation. It situates agentic AI governance within international regulatory context, providing roadmap for aligning programs to 2026 requirements.

-----

Phase: [EXPLORATION]

### Source [86]: https://witness.ai/blog/agentic-ai-governance-framework

Query: What role are regulatory frameworks playing in enterprise choices between auditable and autonomous agent systems?

Answer: Traditional AI governance frameworks fall short for autonomous systems, assuming non-autonomous behavior. Agentic AI governance requires continuous monitoring, explainability, attribution, and auditability for regulatory compliance and trust. It spans the entire AI lifecycle to ensure autonomous systems align with organizational objectives, regulatory compliance, and responsible AI principles. Key components include governance models, controls, and safeguards purpose-built for autonomy. This is critical in healthcare, cybersecurity, and enterprise deployments where static compliance checks are insufficient.

-----

</details>

<details>
<summary>How do data pipeline orchestration tools like Temporal inform reliability primitives in agent runtimes?</summary>

Phase: [EXPLORATION]

### Source [87]: https://temporal.io/blog/orchestrating-ambient-agents-with-temporal

Query: How do data pipeline orchestration tools like Temporal inform reliability primitives in agent runtimes?

Answer: Temporal informs reliability primitives in agent runtimes through built-in retries, timeouts, and durable state management. It ensures workflows complete successfully or not at all, providing automatic retries and full audit history. This enhances the reliability and observability of AI agents. One of the most powerful patterns implemented was using Temporal primitives (Workflows, Signals, Queries) as the “tools” that the AI agents call to interact with the world. In the Model Context Protocol (MCP) framework, agents invoke tools like get_historical_ticks, place_order, get_portfolio_status to gather data or execute trades. Instead of these tools being simple functions or external APIs, each one is a Temporal primitive under the hood. This marriage of MCP tools with Temporal brought significant reliability, observability, and scalability benefits. Every time the agent “places an order,” it’s invoking this Workflow. The use of Temporal here means the action is durable, and if the underlying Activity fails (say the exchange API is down), Temporal can retry or timeout gracefully. In fact, every @mcp.tool() in the system is backed by a deterministic Temporal Workflow, which gives automatic retries and full replay for audit/compliance out of the box. The AI agents’ tools became durable operations. Inconsistent state if an agent’s tool call crashed midway is avoided — Temporal ensures either the whole Workflow completes or it doesn’t happen at all, and inspection of what happened from the history is always possible. The architecture consists of three primary agents: a broker agent (user interface Workflow), an execution agent (trading decisions Workflow), and a judge agent (LLM-as-judge evaluator Workflow), plus supporting Workflows for market data streaming, order execution, and an execution ledger. Temporal allowed these to be broken into modular Workflows that each handle their domain.

-----

Phase: [EXPLORATION]

### Source [88]: https://www.langchain.com/resources/langgraph-vs-temporal

Query: How do data pipeline orchestration tools like Temporal inform reliability primitives in agent runtimes?

Answer: Temporal is a general-purpose runtime that can run AI workloads. Temporal is a durable execution engine built for generic workflows: financial transactions, job pipelines, background processing. Temporal executes your workflows. Temporal requires deterministic workflow code, so non-deterministic LLM behavior needs workarounds like Worker Versioning or patching to handle code changes safely. Temporal's tooling is developer-centric. It requires understanding of activities, workflows, replay, and determinism primitives.

-----

Phase: [EXPLORATION]

### Source [89]: https://danmccarey.net/blog/complex-data-pipelines-with-temporal

Query: How do data pipeline orchestration tools like Temporal inform reliability primitives in agent runtimes?

Answer: Temporal is a workflow orchestration platform that addresses pain points head-on. Built with reliability and scalability at its core, Temporal allows you to define workflows as code while abstracting away much of the complexity of managing states, retries, and concurrency. Its model is particularly suited for scenarios involving long-running processes and high reliability requirements—making it perfect for data pipelines. Key features: 1. Code-First Workflows: Temporal lets you define workflows and activities in code. This approach makes workflows easy to read, debug, and version, unlike traditional graphical interfaces or configuration-driven orchestration tools. 2. Built-In Reliability: With Temporal, retries, timeouts, and failure handling are built into the framework. You don’t have to worry about writing custom logic for transient failures or crafting idempotent steps—Temporal handles it for you. 3. Stateful and Durable: Temporal’s ability to maintain state ensures that workflows can pause and resume without losing progress. This feature is especially useful in long-running pipelines or workflows that rely on external user input or system events.

-----

Phase: [EXPLORATION]

### Source [90]: https://temporal.io/blog/ai-ml-and-data-engineering-workflows-with-temporal

Query: How do data pipeline orchestration tools like Temporal inform reliability primitives in agent runtimes?

Answer: With Temporal, you can focus more on the logic of your application and less on the boilerplate around job management, retries, and failure handling. Temporal handles the heavy lifting, making your processes more reliable and easier to manage. Temporal isn't just for procedural Workflows. It can handle long-running jobs, complex nested Workflows, and interact with other systems through signals for multistep processes. You can also build entity lifecycle workflows that represent a digital twin of a ML model, a data pipeline, or a dataset. This flexibility is invaluable whether you're automating data pipelines, coordinating microservices, or anything in between. Temporal provides a code-first approach to tackle these orchestration challenges head-on. It allows you to not only build more reliable services, but also to build them faster, which is probably why we see Temporal being used by so many AI companies today. As of this writing, we have over 90 companies with a .ai domain using Temporal Cloud.

-----

</details>

<details>
<summary>What historical shifts in AI agent research explain the current rise of MCP as an interoperability standard?</summary>

Phase: [EXPLORATION]

### Source [92]: https://arxiv.org/html/2504.21030v1

Query: What historical shifts in AI agent research explain the current rise of MCP as an interoperability standard?

Answer: The Model Context Protocol (MCP) emerged in response to a growing recognition of the limitations of existing approaches to context management in AI systems. As large language models became increasingly capable, their integration into agent architectures revealed a fundamental disconnect between the sophisticated reasoning capabilities of these models and their ability to maintain coherent context across interactions. The development of MCP can be traced through several key milestones: Late 2023 - Early 2024: Initial research and conceptualization at Anthropic, driven by challenges encountered in developing Claude and related agent systems. Internal prototypes demonstrated the potential benefits of standardized context management. Recent advancements in context management approaches, particularly the development of the Model Context Protocol (MCP), offer promising solutions to these challenges. MCP provides a standardized framework for connecting AI models with external data sources and tools, enabling more effective context retention and sharing across agent interactions. This protocol represents a significant advancement in agent architecture, addressing one of the fundamental limitations identified in previous research.

-----

Phase: [EXPLORATION]

### Source [93]: https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp

Query: What historical shifts in AI agent research explain the current rise of MCP as an interoperability standard?

Answer: Developers have embraced MCP as a standard for connecting generative AI agents with external systems. While the initial focus was on tool integration, MCP’s architecture also enables agents to interact with other agents because it already offers fundamental capabilities needed for these interactions. Not surprisingly, we are seeing the MCP community organically contribute to evolve the protocol to provide additional inter-agent capabilities and abstractions. “At CrewAI, we’ve long championed open standards as the foundation for scalable, secure agent ecosystems. We’re seeing multiple patterns emerge around agent interoperability, and it’s still early days—but it’s clear that MCP is gaining real traction and we expect it to meaningfully shape whatever the final version of this layer looks like. A unified MCP is an important step toward agent interoperability and we’re glad to see AWS helping push that forward in the MCP community. As agentic systems mature, collaboration across vendors and systems will be key. We’re committed to contributing to that future, with flexibility and openness at the core of everything we build.” – João Moura, Founder & CEO, CrewAI. This blog post is the first in a series diving into the technical details of these advances. We explore how MCP can be used to enable agent-to-agent communication, and highlight AWS’s efforts to simplify this pattern. While this post focuses on evolving MCP, we believe more work is needed in the broader agentic AI space with code-first SDKs, inter-agent communication and open observability standards. Stay tuned as we continue exploring the evolving agentic AI landscape.

-----

Phase: [EXPLORATION]

### Source [94]: https://cxfoundation.com/blog/ai-interoperability

Query: What historical shifts in AI agent research explain the current rise of MCP as an interoperability standard?

Answer: Model Context Protocol (MCP) is an open-source framework from Anthropic that standardizes how AI systems, including LLMs, integrate and share data with external data sources and tools. Commonly referred to as the “USB-C for LLMs and AI agents,” MCP enables popular tools like Claude, ChatGPT, and Perplexity (to name a few) to communicate with your internal tools (think Salesforce, Slack, your CCaaS platform, etc.) Currently, MCP is the most commonly-used standard. AI interoperability is the ability for different AI Agents, models, and systems to autonomously collaborate and take collective action to achieve desired outcomes, even if those AI agents are from different vendors, platforms, or domains. The goal is to provide interoperable agentic AI orchestration without vendor lock-in: to connect AI agents from different systems, providers, and frameworks into one unified, governed system with shared language and standards. Interoperability signals the end of single-purpose AI applications and the beginning of interconnected multi-agent systems (MAS) that autonomously execute multi-step, cross-functional workflows.

-----

Phase: [EXPLORATION]

### Source [95]: https://www.kore.ai/blog/what-is-ai-agent-interoperability

Query: What historical shifts in AI agent research explain the current rise of MCP as an interoperability standard?

Answer: Within a single platform, this mostly works. The problem is that real enterprises do not run on a single platform. An orchestrator on one vendor's infrastructure needs to delegate to a specialist agent on another vendor's framework, retrieve data from a third system, and return results to a fourth. That is the real-world complexity, and it is exactly where the absence of shared standards creates a bottleneck. MCP, A2A, and ACP are each addressing a piece of this stack. None of them addresses it completely yet. But enterprises that architect their multi-agent systems with these protocols in mind will scale significantly faster than those that do not. These are the three emerging agent protocols working to standardize how AI agents communicate across boundaries. MCP, from Anthropic, standardizes how agents connect to external tools and data sources. A2A, from Google, enables agents on different frameworks to discover each other and hand off tasks. ACP, from IBM, focuses on structured agent communication with governance and auditability built in. None is a dominant standard yet, but all three represent where the industry is heading.

-----

Phase: [EXPLORATION]

### Source [96]: https://arxiv.org/html/2505.02279v1

Query: What historical shifts in AI agent research explain the current rise of MCP as an interoperability standard?

Answer: Protocol-Oriented Interoperability (2024–2025): The current phase emphasizes lightweight, standardized protocols such as MCP, ACP, ANP, and A2A. These protocols address previous limitations by enabling dynamic discovery, secure communication, and decentralized collaboration across heterogeneous agent systems, promoting scalability and robust interoperability. An AI agent is defined as any autonomous software entity that perceives its environment through inputs (e.g., user queries, sensor data) and acts upon it via outputs (e.g., API calls, messages) to achieve designated goals. Agents operate within environments characterized along dimensions such as observability, determinism, episodicity, and dynamicity, and may employ sensors and actuators to interact with physical or virtual world models. The evolution of agent interoperability is illustrated through a visual timeline (Figure 2, Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)) and a detailed table (Table 2, Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)). The timeline captures high-level milestones, while the table offers technical detail, describing each development alongside key contributions. Together, these representations outline the trajectory of interoperability standards and protocols over time.

-----

</details>

<details>
<summary>What failure modes emerge when OpenAI Agents SDK lacks native checkpointing?</summary>

Phase: [EXPLORATION]

### Source [97]: https://www.diagrid.io/solutions/openai-agents-production

Query: What failure modes emerge when OpenAI Agents SDK lacks native checkpointing?

Answer: The OpenAI Agents SDK has no durability layer, checkpointing, state persistence, or failure recovery. When an agent crashes mid-conversation or mid-tool-call, all progress is lost. No mechanism detects that an agent has stopped running; a crashed process goes unnoticed until someone checks. Production agent workflows can sit in a failed state for hours before anyone reacts. Running multiple agent instances has no built-in coordination; without distributed locking, concurrent runners can pick up the same task and produce duplicate work with no deduplication. Tracing provides debugging info after the fact but does not prevent data loss, recover failed runs, or persist state across crashes. Diagrid adds durable execution so agents survive crashes and recover automatically.

-----

Phase: [EXPLORATION]

### Source [98]: https://www.zenml.io/blog/openai-agents-sdk-durable-runtime

Query: What failure modes emerge when OpenAI Agents SDK lacks native checkpointing?

Answer: Without checkpointing, long-running approval flows risk losing work: a support run that has already looked up an order, checked policy, and drafted an answer reaches a sensitive action needing human approval. If the reviewer is unavailable, a Kubernetes pod may sit idle for hours, or the run is thrown away and restarted, risking redo of work or duplicate side effects. The SDK exposes approval interruptions and resumable RunState, but without an external durable runtime, these primitives alone do not prevent loss of progress during extended waits.

-----

</details>

<details>
<summary>What latency tradeoffs arise from CrewAI opinionated role constructs at scale?</summary>

Phase: [EXPLORATION]

### Source [101]: https://github.com/crewaiinc/crewai

Query: What latency tradeoffs arise from CrewAI opinionated role constructs at scale?

Answer: Performance optimizations include lazy-loading MCP SDK and event types to reduce cold start by ~29%. Defer MCP SDK import by fixing import path in agent/core.py to avoid triggering full mcp SDK (~300-400ms). Move MCPToolResolver import into get_mcp_tools() method body. Lazy-load heavy MCP imports in mcp/__init__.py using __getattr__. Saves ~200ms on 'import crewai' cold start. Lazy-load all event type modules in events/__init__.py using __getattr__ pattern, saving ~550ms on 'import crewai' cold start. CrewAI is highly scalable, supporting simple automations and large-scale enterprise workflows involving numerous agents and complex tasks simultaneously.

-----

Phase: [EXPLORATION]

### Source [102]: https://docs.crewai.com/en/concepts/agents

Query: What latency tradeoffs arise from CrewAI opinionated role constructs at scale?

Answer: Agents support settings like memory=True, respect_context_window=True, max_rpm=10 to limit API calls, function_calling_llm for cheaper models. respect_context_window=True (default) for processing large documents that might exceed limits, long-running conversations, research tasks. respect_context_window=False for precision-critical tasks like legal/medical, code review, financial analysis. max_execution_time=300 (5-minute timeout), max_retry_limit=3. Use RAG tools for very large datasets. max_iter=50 for complex analysis.

-----

Phase: [EXPLORATION]

### Source [103]: https://docs.crewai.com/en/guides/concepts/evaluating-use-cases

Query: What latency tradeoffs arise from CrewAI opinionated role constructs at scale?

Answer: Choosing between Crews and Flows: Crews for specialized agents in research/analysis pipelines (e.g., Market Research Specialist, Market Analyst). Low complexity/high precision, high complexity/low precision, high complexity/high precision use cases. Crews suitable when role-based delegation and sequential/parallel processes fit the workflow.

-----

</details>

<details>
<summary>What metrics validate hybrid MCP-plus-LangGraph durability in capstone workloads?</summary>

Phase: [EXPLORATION]

### Source [104]: https://mcp-server-langgraph.mintlify.app/comparisons/benchmarks

Query: What metrics validate hybrid MCP-plus-LangGraph durability in capstone workloads?

Answer: Metrics validating hybrid MCP-plus-LangGraph durability include max throughput, latency percentiles, error rate, and state persistence. Auto-scaling and fault tolerance also confirm robustness. In Kubernetes with HPA: Max Throughput 425 req/s (auto-scaling to 10 pods), Latency p50 320 ms, p95 1,200 ms, p99 2,400 ms, Error Rate 0.25%. For complex workflow with conditionals: Throughput 32 req/s, Latency p50 2,800 ms, p95 6,500 ms, p99 9,200 ms, Error Rate 0.15%, State Persistence via Redis checkpointing, Fault Tolerance with automatic retry. Recovery Time 45 seconds from spike to steady state.

-----

Phase: [EXPLORATION]

### Source [105]: https://aerospike.com/blog/langgraph-production-latency-replay-scale

Query: What metrics validate hybrid MCP-plus-LangGraph durability in capstone workloads?

Answer: MLPerf Inference benchmarks highlight interactive latency metrics like TTFT under a second and TPOT in tens of milliseconds. For durable execution, systems handling 2,000 requests per second with 12 steps require storage for 24,000 writes per second. LangGraph persists state for workflow resumption after delays, ensures safe restarts via predictable replay, separates external actions to prevent duplication, and supports interrupts that persist state indefinitely until resumption.

-----

Phase: [EXPLORATION]

### Source [106]: https://dev.to/manjunathgovindaraju/building-a-reliable-langgraph-workflow-plan-execute-validate-pev-automated-retries-and-mcp-1pik

Query: What metrics validate hybrid MCP-plus-LangGraph durability in capstone workloads?

Answer: Template parameters include pass_threshold 0.80, max_retries 2, max_replans 1. Features for reliability: Validation with confidence score 0.0-1.0, per-step retry with feedback, automatic replanning on exhausted retries, full audit trail via operator.add accumulator preserving every attempt in step_results, structured outputs with Pydantic models. MCP integration provides standardized secure access to enterprise data, allowing tool updates without redeploying core logic. PEV acts as brain for reasoning/planning/validation, MCP as hands for data access.

-----

Phase: [EXPLORATION]

### Source [107]: https://medium.com/@karthikbhuvanagiri_22581/solving-hybrid-workflow-challenges-in-langgraph-with-mcp-integration-2603d5a02477

Query: What metrics validate hybrid MCP-plus-LangGraph durability in capstone workloads?

Answer: Hybrid approach preserves business-defined sequences while using MCP for dynamic tool invocation. Best practices: Modularize MCP server tool definitions, validate tool availability at runtime for graceful degradation, log and monitor tool interactions for debugging and optimization, design for extensibility. Workflow stages include Data Ingestion (Ingestion Agent, rule-based no LLM), Data Transformation & Loading (Data Agent, rule-based), AI-Powered Analysis & Reporting. Use helper methods for reliable tool invocation with error handling and context-sensitive fallback logic.

-----

Phase: [EXPLORATION]

### Source [108]: https://www.dailydoseofds.com/model-context-protocol-crash-course-part-9

Query: What metrics validate hybrid MCP-plus-LangGraph durability in capstone workloads?

Answer: MCP servers act as swappable capability providers exposing tools, prompts, resources independently for horizontal scaling across domains. LangGraph provides structured memory, conditional branching, and reintegration of tool outputs. Deep Research Assistant uses stateful LangGraph agent with dual-server MCP client and StateGraph for message flow, tool usage, and state evolution with conditional logic for flexible transitions based on tool needs or user meta-commands.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="a-survey-of-agent-interoperability-protocols-model-context-p.md">
<details>
<summary>A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)</summary>

Phase: [EXPLORATION]

**Source URL:** <https://arxiv.org/html/2505.02279v1>

# A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)

###### Abstract

Large language model (LLM)-powered autonomous agents demand robust, standardized protocols to integrate tools, share contextual data, and coordinate tasks across heterogeneous systems. Ad-hoc integrations are difficult to scale, secure, and generalize across domains. This survey examines four emerging agent communication protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP), each addressing interoperability in distinct deployment contexts. MCP provides a JSON-RPC client-server interface for secure tool invocation and typed data exchange. ACP introduces REST-native messaging via multi-part messages and asynchronous streaming to support multimodal agent responses. A2A enables peer-to-peer task outsourcing through capability-based Agent Cards, facilitating enterprise-scale workflows. ANP supports open-network agent discovery and secure collaboration using decentralized identifiers (DIDs) and JSON-LD graphs. The protocols are compared across multiple dimensions, including interaction modes, discovery mechanisms, communication patterns, and security models. Based on the comparative analysis, a phased adoption roadmap is proposed: beginning with MCP for tool access, followed by ACP for multimodal messaging, A2A for collaborative task execution, and extending to ANP for decentralized agent marketplaces. This work provides a comprehensive foundation for designing secure, interoperable, and scalable ecosystems of LLM-powered agents.

## 1 Introduction

Large Language Models (LLMs) have become central to modern artificial intelligence, powering autonomous agents that operate across cloud, edge, and desktop environments \[ [1](https://arxiv.org/html/2505.02279v1#bib.bib1 ""), [2](https://arxiv.org/html/2505.02279v1#bib.bib2 "")\]. These agents \[ [3](https://arxiv.org/html/2505.02279v1#bib.bib3 "")\] ingest contextual information, execute tasks, and interact with external services or tools. However, inconsistent and fragmented interoperability practices make it difficult to integrate, secure, and scale communication among LLM-driven agents \[ [4](https://arxiv.org/html/2505.02279v1#bib.bib4 "")\].

Interoperability (the ability of distinct agents and systems to discover capabilities, exchange context, and coordinate actions seamlessly) is essential for modular, reusable, and resilient multi-agent \[ [5](https://arxiv.org/html/2505.02279v1#bib.bib5 "")\] workflows. Standardized protocols reduce development overhead, improve security, and enable cross-platform collaboration. Clear, universally adopted standards remain nascent.

This survey examines four emerging agent communication protocols, each targeting a different interoperability tier:

- •


Model Context Protocol (MCP): a JSON-RPC client–server interface for secure context ingestion and structured tool invocation \[ [6](https://arxiv.org/html/2505.02279v1#bib.bib6 ""), [7](https://arxiv.org/html/2505.02279v1#bib.bib7 ""), [8](https://arxiv.org/html/2505.02279v1#bib.bib8 "")\].

- •


Agent-to-Agent Protocol (A2A): a peer-to-peer framework using capability-based Agent Cards over HTTP and Server-Sent Events for enterprise-scale task orchestration \[ [9](https://arxiv.org/html/2505.02279v1#bib.bib9 "")\].

- •


Agent Communication Protocol (ACP): a REST-native performative messaging layer with multi-part messages, asynchronous streaming, and observability features for local multi-agent systems \[ [10](https://arxiv.org/html/2505.02279v1#bib.bib10 "")\].

- •


Agent Network Protocol (ANP): a decentralized discovery and collaboration protocol built on decentralized identifiers (DIDs) and JSON-LD graphs for open-internet agent marketplaces  \[ [11](https://arxiv.org/html/2505.02279v1#bib.bib11 ""), [12](https://arxiv.org/html/2505.02279v1#bib.bib12 "")\].


Architectural details, integration approaches, communication patterns, and security considerations are reviewed for each protocol. A comparison highlights trade-offs in interaction modes, discovery mechanisms, communication models, and security frameworks. A phased adoption roadmap sequences MCP, A2A, ACP, and ANP to guide progressive deployment in real-world agent ecosystems.

The remainder of the paper is organized as follows. Section 2 discusses challenges in agent interoperability. Section 3 reviews background and related work. Sections 4–7 describe the architectures of MCP, A2A, ACP, and ANP, respectively. Section 8 presents the comparative evaluation. Section 9 outlines the phased adoption roadmap. Section 10 concludes and suggests future research directions.

## 2 Challenges and Solutions in Agent Protocol Interoperability

Despite the emergence of multiple open protocols like MCP, ACP, A2A, and ANP, achieving seamless agent interoperability in real-world AI systems remains a non-trivial task. This section identifies key challenges encountered in agent-based architectures and highlights how each protocol addresses them with purpose-built design principles.

Lack of Context Standardization for LLMs:
Large Language Models (LLMs) require contextual grounding to produce accurate outputs. However, existing application architectures provide no unified mechanism to deliver structured context to LLMs, leading to ad hoc tool integrations and unreliable behavior.
Solution: The Model Context Protocol (MCP) addresses this by standardizing how applications deliver tools, datasets, and sampling instructions to LLMs, akin to a USB-C for AI. It supports flexible plug-and-play tools, safe infrastructure integration, and compatibility across LLM vendors.

https://arxiv.org/html/2505.02279v1/security_challenges.pngFigure 1: Protocol-aligned solution to challenges in agent communication

Communication Barriers Between Heterogeneous Agents:
Enterprise systems often consist of agents built using different stacks and frameworks, resulting in isolated behavior and poor collaboration.
Solution: The Agent Communication Protocol (ACP) offers a RESTful, SDK-optional interface with open governance under the Linux Foundation. It enables asynchronous-first interactions, offline discovery, and vendor-neutral execution, bridging interoperability gaps at scale.

Absence of Unified Agent Collaboration Standards:
Even when agents communicate, there’s no shared framework for dynamic negotiation, capability sharing, and coordination.
Solution: The Agent2Agent (A2A) protocol introduces a multimodal communication standard to unlock dynamic interaction between opaque, autonomous agents—regardless of framework. It simplifies enterprise integration and supports shared task management and user experience negotiation.

Internet-Agnostic Agent Communication:
The modern internet is optimized for human interaction but suboptimal for autonomous agents, which require low-latency, API-native communication and decentralized identity validation.
Solution: The Agent Network Protocol (ANP) provides a layered protocol architecture incorporating decentralized identity (W3C DID), semantic web principles, and encrypted communication to facilitate cross-platform agent collaboration over the open internet.

Together, these protocols aim to transform fragmented AI ecosystems into robust, secure, and interoperable agent networks—scalable across organizational and vendor boundaries. See Table [7](https://arxiv.org/html/2505.02279v1#S7.T7 "Table 7 ‣ 7.4 Security Considerations Across the ANP Lifecycle ‣ 7 ANP Architecture ‣ A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)") for a detailed comparative overview.

## 3 Background and Related Work

Autonomous agents powered by large language models (LLMs) are rapidly being adopted across industries to automate complex tasks, yet disparate frameworks and ad-hoc integrations hinder robust interoperability, security, and scalability \[ [2](https://arxiv.org/html/2505.02279v1#bib.bib2 ""), [4](https://arxiv.org/html/2505.02279v1#bib.bib4 "")\]. Recent surveys have begun to characterize the landscape of LLM-based multi-agent systems, categorizing collaboration patterns, memory architectures, and orchestration strategies \[ [13](https://arxiv.org/html/2505.02279v1#bib.bib13 ""), [14](https://arxiv.org/html/2505.02279v1#bib.bib14 ""), [15](https://arxiv.org/html/2505.02279v1#bib.bib15 "")\]. However, these works largely focus on high-level workflows and neglect the underlying protocols necessary for dynamic peer discovery, capability negotiation, and secure tool invocation.

Effective interoperability—enabling agents to discover capabilities, share context, and coordinate actions—is critical for building modular, reusable, and resilient multi-agent systems. Early efforts in dynamic discovery have introduced metadata manifests and capability descriptors to allow runtime agent registration and lookup \[ [16](https://arxiv.org/html/2505.02279v1#bib.bib16 "")\], while recent work on automated tool testing frameworks (e.g., TOOLFUZZ) highlights the challenges of ensuring compatibility across evolving API surfaces \[ [17](https://arxiv.org/html/2505.02279v1#bib.bib17 "")\]. Yet, no unified protocol has emerged that specifies how agents should announce their interfaces, authenticate peers, or negotiate context sharing across heterogeneous LLM frameworks.

In response to this gap, recent proposals such as the Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent2Agent Protocol (A2A) and Agent Network Protocol (ANP) aim to define lightweight, formal interfaces for context ingestion, performative messaging, and peer discovery using JSON-RPC schemas \[ [6](https://arxiv.org/html/2505.02279v1#bib.bib6 ""), [10](https://arxiv.org/html/2505.02279v1#bib.bib10 ""), [9](https://arxiv.org/html/2505.02279v1#bib.bib9 ""), [11](https://arxiv.org/html/2505.02279v1#bib.bib11 ""), [12](https://arxiv.org/html/2505.02279v1#bib.bib12 "")\]. Each protocol is examined in detail, followed by a comparative analysis and a roadmap for their integration within emerging multi-agent ecosystems.

### 3.1 AI Agents: Definition and Scope

An _AI agent_ is defined as any autonomous software entity that perceives its environment through inputs (e.g., user queries, sensor data) and acts upon it via outputs (e.g., API calls, messages) to achieve designated goals \[ [18](https://arxiv.org/html/2505.02279v1#bib.bib18 "")\]. Agents operate within environments characterized along dimensions such as observability, determinism, episodicity, and dynamicity, and may employ sensors and actuators to interact with physical or virtual world models \[ [18](https://arxiv.org/html/2505.02279v1#bib.bib18 ""), [19](https://arxiv.org/html/2505.02279v1#bib.bib19 "")\].

According to Franklin and Graesser’s taxonomy, agents can be categorized based on attributes like autonomy, sociability, reactivity, and adaptability, reflecting their ability to function in open, multi-agent settings \[ [20](https://arxiv.org/html/2505.02279v1#bib.bib20 "")\]. Jennings emphasizes proactive goal generation, complex planning, and robust recovery capabilities under uncertainty as key distinguishing features from simple reactive programs \[ [21](https://arxiv.org/html/2505.02279v1#bib.bib21 "")\]. Wooldridge further identifies four core properties— _autonomy_, _social ability_, _reactivity_, and _pro‐activeness_, that enables agents to operate without direct human intervention, collaborate with peers, and pursue long‐term objectives \[ [19](https://arxiv.org/html/2505.02279v1#bib.bib19 "")\].

Agent architectures span from simple rule‐based reactive models, where actions are direct responses to percepts, to rich deliberative frameworks such as Belief‐Desire‐Intention (BDI) systems that support symbolic reasoning, dynamic plan execution, and intention reconsideration. In multi-agent systems, coordination is achieved through communication protocols, negotiation strategies, and organizational structures, laying the groundwork for LLM‐powered ecosystems that require robust interoperability, security, and scalability. This broad yet precise definition underpins our subsequent review of communication standards, orchestration frameworks, and protocol designs.

### 3.2 Early Symbolic Agent Languages—Evolution of Agent Communication Standards

The first formal agent messaging languages emerged in the early 1990s with the goal of providing a standardized “envelope” and performative vocabulary for knowledge‐based systems. The Knowledge Query and Manipulation Language (KQML) introduced by Genesereth and Ketchpel defined a set of speech‐act performatives (e.g., ask‐if, tell, reply) along with a flexible message envelope supporting parameters such as :content, :language, :ontology, :receiver, and :reply‐with. KQML also specified content‐language bindings (commonly KIF) to express propositions in a machine‐interpretable form \[ [22](https://arxiv.org/html/2505.02279v1#bib.bib22 ""), [23](https://arxiv.org/html/2505.02279v1#bib.bib23 "")\]. Although widely used in DARPA’s Open Knowledge Base and Agent projects, KQML’s lack of formal semantics for performatives and heavyweight XML‐style encodings hindered large‐scale deployments.

Building on KQML, the FIPA Agent Communication Language (FIPA‐ACL)—ratified by the Foundation for Intelligent Physical Agents in 2000—refined the notion of communicative acts by prescribing precise pre‐ and post‐condition semantics grounded in agents’ mental states (beliefs, desires, intentions). FIPA‐ACL defined a richer set of performatives (e.g., agree, refuse, request), standardized content languages (e.g., SL0, SL1), and outlined interaction protocols for common patterns such as _contract net_, _iterated contract net_, and _subscribe/notify_\[ [24](https://arxiv.org/html/2505.02279v1#bib.bib24 "")\]. Reference implementations in platforms like JADE and JACK offered Java‐based agent containers and message‐handling APIs, yet the complexity of FIPA’s ontology management, coupled with verbose XML encodings, limited its uptake to academic and defense use cases rather than lightweight, industry‐grade systems.

### 3.3 Service-Oriented Integrations and Retrieval-Augmented Generation

The early 2000s witnessed the rise of service-oriented architectures (SOA), in which enterprise systems exposed functionality as web services (SOAP, WSDL, WS-\* standards) and registered endpoints in UDDI repositories \[ [25](https://arxiv.org/html/2505.02279v1#bib.bib25 "")\]. Message-oriented middleware and enterprise service buses (ESBs) such as Apache Camel and Mule ESB facilitated protocol bridging, message routing, and payload transformation, leveraging patterns like content-based routing, message splitting, and aggregation \[ [26](https://arxiv.org/html/2505.02279v1#bib.bib26 "")\]. While SOA and ESBs decoupled service producers from consumers, they often incurred high operational complexity, brittle adapters, and configuration sprawl as APIs evolved and security requirements tightened.

With the advent of large language models, Retrieval-Augmented Generation (RAG) emerged in 2020 to integrate external knowledge into generation pipelines by coupling dense vector retrieval with autoregressive decoding \[ [27](https://arxiv.org/html/2505.02279v1#bib.bib27 "")\]. RAG systems encode queries and documents in a shared embedding space (e.g., DPR) to fetch top-kk relevant passages, then condition LLM outputs on retrieved context to reduce hallucinations and enable dynamic knowledge updates \[ [28](https://arxiv.org/html/2505.02279v1#bib.bib28 "")\]. Despite improving factuality and flexibility, RAG frameworks treat retrieval and generation as separate batch processes and do not prescribe how LLMs should translate grounded content into executable actions or orchestrate multi-step workflows—highlighting a need for protocol-level standards that unify knowledge grounding with action invocation.

### 3.4 LLM Agents and Function Calling

The rapid evolution of large language models (LLMs) such as GPT-3.5, GPT-4, Claude, and Gemini has fundamentally transformed agent design by enabling zero- and few-shot understanding of complex natural language instructions without bespoke rule engines \[ [2](https://arxiv.org/html/2505.02279v1#bib.bib2 "")\]. These foundation models can parse user intent, plan multi-step workflows, and maintain dialogue coherence across diverse domains, opening the door to “LLM agents” that combine linguistic reasoning with external tool execution.

To operationalize tool use, OpenAI introduced function calling in 2023, a lightweight protocol whereby an LLM can output a JSON-formatted signature corresponding to a predefined API endpoint \[ [29](https://arxiv.org/html/2505.02279v1#bib.bib29 "")\]. Under this paradigm, developers supply the model with a catalog of function definitions—each described by a name, JSON schema for arguments, and descriptive help text—and the model decides at generation time whether to invoke a function, emitting well-formed JSON that can be parsed and executed by downstream systems. This approach unifies natural language understanding and action invocation, enabling real-time data fetches, database queries, and transactional operations from within a single LLM response.

Building on this core capability, several frameworks have emerged to simplify agent development:

- •


LangChain provides abstractions for chaining LLM calls, memory buffers, and function invocation in modular workflows, with built-in support for retrievers, vector stores, and agent loops \[ [30](https://arxiv.org/html/2505.02279v1#bib.bib30 "")\].

- •


LlamaIndex (formerly GPT Index) focuses on integrating LLMs with custom knowledge bases, offering document loaders, index wrappers, and a “tool registry” that maps user queries to API calls \[ [31](https://arxiv.org/html/2505.02279v1#bib.bib31 "")\].

- •


The OpenAI Plugin Store enables third-party tool providers to register plugins that expose RESTful interfaces, metadata, and authentication flows, which can be discovered and invoked by any model with plugin access \[ [32](https://arxiv.org/html/2505.02279v1#bib.bib32 "")\].


Despite these advances, current function-calling ecosystems suffer from several limitations. Tool definitions are typically static: agents must be re-initialized whenever new APIs are added or schemas change, preventing truly dynamic discovery. Security boundaries—such as authentication tokens, rate limits, and access control—are ad-hoc and framework-specific, increasing the risk of unauthorized calls. Moreover, each framework employs its own metadata conventions, hindering cross-framework reuse of tools and requiring bespoke adapters for interoperability \[ [33](https://arxiv.org/html/2505.02279v1#bib.bib33 "")\]. Addressing these challenges requires protocol-level standards that prescribe a common schema for function metadata, dynamic capability negotiation, and end-to-end security guarantees across heterogeneous LLM agent platforms.

### 3.5 Orchestration and Lightweight Agent Frameworks

Recent advances have extended the capabilities of LLMs beyond reasoning to include orchestration of external tool invocation. Toolformer employs a self-supervised masking strategy that exposes potential API calls during pretraining, enabling the model to learn when and how to invoke functions as part of its text generation \[ [34](https://arxiv.org/html/2505.02279v1#bib.bib34 "")\]. ReAct interleaves chain-of-thought reasoning with explicit action calls, allowing models to alternate between “thinking” steps and tool invocations based on intermediate observations \[ [35](https://arxiv.org/html/2505.02279v1#bib.bib35 "")\]. These approaches unify reasoning and action at the single-agent level but do not address peer discovery or multi-agent coordination.

Complementing these algorithmic techniques, several lightweight frameworks have emerged to suppprt multi-agent orchestration with minimal boilerplate (Table [1](https://arxiv.org/html/2505.02279v1#S3.T1 "Table 1 ‣ 3.5 Orchestration and Lightweight Agent Frameworks ‣ 3 Background and Related Work ‣ A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)")). Additional orchestration systems, such as AutoGPT’s autonomous loops \[ [36](https://arxiv.org/html/2505.02279v1#bib.bib36 "")\] and Reflexion’s iterative self-improvement mechanism \[ [37](https://arxiv.org/html/2505.02279v1#bib.bib37 "")\], highlight the value of feedback and adaptation in agent workflows, However, these frameworks continue to rely on static tool registries and bespoke communication layers. Across these approaches, the lack of a standardized protocol for capability advertisement, peer authentication, and cross-framework composition contributes to fragmentation-hindering the emergence of a cohesive, interoperable agent ecosystem.

Table 1: Lightweight LLM Agent Frameworks

| Framework | Core Feature | Reference |
| --- | --- | --- |
| CrewAI | High-level “crew” abstractions for role assignment, subtask delegation, and message routing among agents | \[ [38](https://arxiv.org/html/2505.02279v1#bib.bib38 "")\] |
| SmolAgents | Single-file Python library combining retrieval, vision, and agent loop primitives for rapid prototyping | \[ [39](https://arxiv.org/html/2505.02279v1#bib.bib39 "")\] |
| AG2 (AutoGen) | Open-source AgentOS with human-in-the-loop checkpoints, policy enforcement hooks, and lifecycle management | \[ [40](https://arxiv.org/html/2505.02279v1#bib.bib40 "")\] |
| Semantic Kernel | Enterprise-grade SDK unifying memory stores, planning modules, and plugin orchestration across sessions | \[ [41](https://arxiv.org/html/2505.02279v1#bib.bib41 "")\] |
| Swarm | Stateless multi-agent coordination via JSON-RPC routines, spawning and aggregating parallel agent tasks | \[ [42](https://arxiv.org/html/2505.02279v1#bib.bib42 "")\] |

### 3.6 Protocol Evolution Timeline

The evolution of agent interoperability is illustrated through a visual timeline (Figure [2](https://arxiv.org/html/2505.02279v1#S3.F2 "Figure 2 ‣ 3.6 Protocol Evolution Timeline ‣ 3 Background and Related Work ‣ A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)")) and a detailed table (Table [2](https://arxiv.org/html/2505.02279v1#S3.T2 "Table 2 ‣ 3.6 Protocol Evolution Timeline ‣ 3 Background and Related Work ‣ A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)")). The timeline captures high-level milestones, while the table offers technical detail, describing each development alongside key contributions. Together, these representations outline the trajectory of interoperability standards and protocols over time.

Table 2: Timeline of Key Agent Interoperability Milestones

| Year | Milestone | Key Contribution |
| --- | --- | --- |
| 1993 | KQML | Introduced speech-act primitives and a flexible message envelope for knowledge-based agents \[ [22](https://arxiv.org/html/2505.02279v1#bib.bib22 "")\]. |
| 1998 | MASIF | Defined basic service registration and discovery mechanisms for agent environments \[ [43](https://arxiv.org/html/2505.02279v1#bib.bib43 "")\]. |
| 2000 | FIPA-ACL | Standardized performative semantics, content languages, and interaction protocols with formal pre-/post-conditions \[ [24](https://arxiv.org/html/2505.02279v1#bib.bib24 "")\]. |
| 2002 | Web Services (SOAP/WSDL) | Enabled service-oriented agent integration via UDDI, XML messaging, and contract definitions \[ [25](https://arxiv.org/html/2505.02279v1#bib.bib25 "")\]. |
| 2006 | ESB Patterns | Codified enterprise integration patterns (routing, transformation) in ESBs like Apache Camel and Mule \[ [26](https://arxiv.org/html/2505.02279v1#bib.bib26 "")\]. |
| 2020 | RAG | Coupled dense vector retrieval with LLM decoding to ground outputs in external corpora \[ [27](https://arxiv.org/html/2505.02279v1#bib.bib27 "")\]. |
| 2023 | Function Calling | Allowed LLMs to emit JSON-formatted API calls against a catalog of function schemas \[ [29](https://arxiv.org/html/2505.02279v1#bib.bib29 "")\]. |
| 2023 | Toolformer | Trained LLMs via self-supervised masking to predict API call placement in text \[ [34](https://arxiv.org/html/2505.02279v1#bib.bib34 "")\]. |
| 2023 | ReAct | Interleaved chain-of-thought reasoning and explicit action calls for dynamic workflows \[ [35](https://arxiv.org/html/2505.02279v1#bib.bib35 "")\]. |
| 2024 | MCP | Proposed a JSON-RPC protocol for standardized context ingestion and tool invocation \[ [6](https://arxiv.org/html/2505.02279v1#bib.bib6 "")\]. |
| 2024 | ANP | Peer-to-peer protocol enabling cross-platform and cross-organization agent communication over the open internet. \[ [11](https://arxiv.org/html/2505.02279v1#bib.bib11 "")\]. |
| 2024 | ACP | Defined performative messaging primitives with formal types and security layers \[ [10](https://arxiv.org/html/2505.02279v1#bib.bib10 "")\]. |
| 2025 | A2A | Introduced peer discovery, capability exchange, and decentralized agent dialogues \[ [9](https://arxiv.org/html/2505.02279v1#bib.bib9 "")\]. |
https://arxiv.org/html/2505.02279v1/timeline_agent.pngFigure 2: Timeline of Interoperability

Three distinct evolutionary phases emerge:

1. 1.


Symbolic and SOA Foundations (1993–2006): Early interoperability standards such as KQML and FIPA-ACL set formal semantic foundations. Subsequent developments in Web Services and Enterprise Service Bus (ESB) frameworks streamlined enterprise integration but introduced complexity and limited flexibility.

2. 2.


Retrieval and In-Model Action (2020–2023): Marked by the introduction of Retrieval-Augmented Generation (RAG), this phase leveraged vector-based retrieval to enhance the grounding of language model outputs. Innovations like Function Calling, Toolformer, and ReAct enabled LLMs to directly translate reasoning into executable API calls, significantly advancing agent autonomy and flexibility.

3. 3.


Protocol-Oriented Interoperability (2024–2025): The current phase emphasizes lightweight, standardized protocols such as MCP, ACP, ANP, and A2A. These protocols address previous limitations by enabling dynamic discovery, secure communication, and decentralized collaboration across heterogeneous agent systems, promoting scalability and robust interoperability.

## 4 MCP

### 4.1 Client Application (Host)

The Client Application (Host) serves as the initiator of interactions in the MCP ecosystem. It is responsible for managing connections to one or more MCP Servers and orchestrating communication workflows in accordance with protocol specifications. In practice, the client initializes sessions, requests and processes the four core primitives Resources, Tools, Prompts, and Sampling, and handles asynchronous notifications related to server-side events. The client must also implement robust error-handling routines to gracefully manage communication failures or timeout conditions, ensuring reliable coordination with remote MCP Servers.

https://arxiv.org/html/2505.02279v1/mcp.pngFigure 3: An overview of MCP \[ [7](https://arxiv.org/html/2505.02279v1#bib.bib7 "")\]

### 4.2 MCP Server (Providing Context & Capabilities)

The MCP Server functions as the provider of data, services, and interaction templates that the client can utilize to enrich LLM-based workflows. It exposes and manages contextual Resources, executes external operations via Tools, defines reusable Prompts for consistent interaction patterns, and optionally delegates text-generation tasks through Sampling. Beyond serving requests, the server is responsible for enforcing access control policies, maintaining operational security, and emitting notifications that reflect changes in its available capabilities. This provider-side architecture complements the client’s orchestration logic by modularizing access to complex or dynamic resources.

### 4.3 Core Components

The Model Context Protocol is composed of several layered abstractions that govern the structure and semantics of communication. At the foundation lies the Protocol Layer, which defines the semantics of message exchange using the JSON-RPC 2.0 specification. It ensures that each request is linked to a corresponding response and that all interactions conform to predictable patterns. Above this, the Transport Layer handles the physical transmission of messages between the client and server, supporting both local communication via Stdio and network-based channels such as HTTP with optional Server-Sent Events (SSE). At the highest abstraction, MCP organizes messages into four types: Requests, which are calls expecting replies; Results, which are successful responses to earlier requests; and Errors, which indicate failures or invalid invocations. A fourth type, Notifications, is used for asynchronous updates that do not require a client acknowledgment.

### 4.4 MCP Server Core Capabilities

The MCP Server offers four core capabilities Tools, Resources, Prompts, and Sampling each mapped to a distinct control model that governs the interaction between the client, the server, and the LLM.

Tools are model-controlled capabilities that allow the LLM to invoke external APIs or services, often automatically and sometimes with user approval. This facilitates seamless integration with third-party systems and streamlines access to real-world data and operations.

Resources are application-controlled elements, such as structured documents or contextual datasets, that are selected and managed by the client application. They provide the LLM with tailored, task-specific inputs and enable context-aware completions.

Prompts are user-controlled templates defined by the server but selected by end-users through the client interface. These reusable prompts promote consistency, reduce redundancy, and support repeatable interaction patterns.

Sampling is server-controlled and allows the MCP Server to delegate the task of generating LLM completions to the client. This supports sophisticated agentic workflows and enables fine-grained oversight over the model’s generative process, including the ability to adjust temperature, length, and other sampling parameters dynamically.

### 4.5 MCP Connection Lifecycle

The Model Context Protocol (MCP) defines a three-phase lifecycle for client–server interactions, designed to ensure robust session management, secure capability negotiation, and clean termination. These phases Initialization, Operation, and Shutdown correspond to the temporal sequence of communication between the Client Application and MCP Server.

Initialization begins by establishing protocol compatibility and exchanging supported capabilities. During version negotiation, the client and server agree on the highest mutually supported protocol version. This is followed by a capability exchange, in which both sides advertise optional features—such as sampling, prompts, tools, and logging—that can be used during the session. The phase concludes with a notifications/initialized message sent by the client after receiving the server’s initialize response, signaling readiness to proceed to operational communication.

Operation represents the core active phase, during which the client and server exchange JSON-RPC method calls and notifications in accordance with the negotiated capabilities. Both parties are expected to adhere strictly to the features agreed upon during initialization, ensuring compatibility and predictability. Each task invocation may include a configurable timeout, and if a response is not received within that window, the client may issue a cancellation notification to prevent resource exhaustion or stale execution threads.

Shutdown ensures a clean and predictable end to the session. Either party may initiate termination by closing the transport layer typically HTTP or stdio which signals the end of communication. Upon shutdown, both client and server are responsible for resource cleanup, including the removal of active timeouts, cancellation of subscriptions, and deallocation of any spawned child processes. After this point, no new protocol messages should be sent, with the exception of essential diagnostics like ping or log flush events.

### 4.6 Security Challenges and Mitigations Across the MCP Lifecycle

As MCP adoption increases in enterprise and developer ecosystems, its lifecycle introduces multiple security vulnerabilities spanning initialization, operation, and update phases. These risks include tool poisoning, privilege persistence, and command injection, among others, many of which are amplified by LLMs’ susceptibility to prompt manipulation and opaque execution traces.

Table [3](https://arxiv.org/html/2505.02279v1#S4.T3 "Table 3 ‣ 4.6 Security Challenges and Mitigations Across the MCP Lifecycle ‣ 4 MCP ‣ A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)") summarizes the most critical security threats identified across each lifecycle phase of MCP deployments, alongside their corresponding mitigation strategies and authoritative references. This synthesis reflects both current attack disclosures and best-practice defenses from recent audits and protocol reviews.

Table 3: Threats and Mitigation Strategies Across the MCP Lifecycle

| Phase | Threat | Description | Mitigation Strategy |
| --- | --- | --- | --- |
| Creation | Installer Spoofing | Malicious packages introduced during build or install pipelines. | Enforce SBOMs, digital signatures, and reproducible builds. |
| | Supply-Chain Backdoors | Persistent malware via CI/CD artifacts. | Harden CI/CD, validate manifests, and verify artifact integrity. |
| | Name Collision | Impersonation of trusted MCP agents using similar names. | Use Sigstore and DIDs to ensure unique, verifiable identities. |
| | No Auth Handshake | Clients connect to unauthenticated or rogue servers. | Enforce mutual authentication and TLS-based validation. |
| Operation | Tool Poisoning | Malicious prompts or metadata influencing LLM behavior. | Validate schemas, use filtering (YARA/RegEx), and apply semantic guards. |
| | Credential Theft | Secrets leaked via completions or tool output. | Use OAuth 2.1 + PKCE, restrict token scopes, and enforce mTLS. |
| | Sandbox Escape | Tools access host OS or bypass isolation. | Use syscall filters, AppArmor, and container hardening. |
| | Remote Access Control | LLMs inject SSH keys or create backdoor shells. | Monitor with EDR/HIDS and restrict outbound behavior. |
| | Command Injection / RCE | Unsafe inputs trigger system execution. | Sanitize inputs, disable shell access, and disallow evals. |
| | Tool Redefinition | Tools turn malicious after validation ("rug pull"). | Use signed, versioned manifests and monitor for mutation. |
| | Cross-Server Shadowing | One server overrides another’s tool references. | Enforce scoped namespaces and validate routing origins. |
| | Lack of Visibility | Clients cannot inspect tool instructions or payloads. | Enable debug mode, metadata introspection, and logging. |
| Update | Version Drift | Older vulnerable MCP versions remain in use. | Use GitOps for drift detection and enforce auto-remediation. |
| | Privilege Persistence | Retained elevated roles or old token scopes. | Audit roles after updates and rotate credentials. |
| | Configuration Drift | Misconfigurations introduced post-update. | Validate against CVEs and apply hardened defaults. |
| | Unsigned Tool Manifests | Manifests altered or injected post-deployment. | Enforce signature checks and block unsigned tools. |

## 5 A2A Architecture

The Agent-to-Agent (A2A) architecture facilitates communication and collaboration between distinct agentic systems to accomplish tasks. It comprises three primary actors—User, Client Agent, and Remote Agent (Server), that interact via a well-defined protocol, enabling secure and interoperable execution.

https://arxiv.org/html/2505.02279v1/a2a.pngFigure 4: An overview of A2A

### 5.1 Core Components

The User initiates a task or request, typically without needing to understand or directly interact with the underlying agentic systems. The Client Agent receives this request, analyzes its intent, and identifies a suitable Remote Agent (Server) by inspecting the advertised capabilities through its Agent Card. Once selected, the Client Agent engages the Remote Agent to execute the task, coordinating message exchanges and retrieving results—termed Artifacts—which are then delivered back to the User.

#### 5.1.1 User

The User acts as the originator of any A2A interaction, embodying the intent or need that sets the agentic process in motion. While frequently a human end-user, the User can also be a system, service, or another agent in hierarchical workflows. Regardless of its form, the User does not directly interact with Remote Agents; instead, it relies on the Client Agent to translate its requests into actionable tasks and to mediate all responses.

A2A supports diverse User interaction models. A Direct End-User may engage with the Client Agent through interfaces such as chatbots or voice assistants, providing task input and receiving results in real time. An Indirect End-User interacts with higher-level systems that transparently utilize A2A agents behind the scenes, such as enterprise dashboards or orchestration tools. Systems or Services may also act as Users, invoking A2A agents autonomously for workflows like data transformation or monitoring. In multi-agent hierarchies, an Agent as User scenario occurs when one agent triggers downstream actions by another agent to fulfill complex tasks. These various User paradigms underscore the protocol’s agnosticism toward User identity and emphasize its focus on standardizing communication between Client and Remote Agents.

#### 5.1.2 Client Agent

The Client Agent serves as an intermediary that represents the User’s intent and coordinates with Remote Agents to fulfill it. Its responsibilities span multiple stages of the task lifecycle. It begins by performing Agent Discovery, retrieving and evaluating Agent Cards that describe each Remote Agent’s skills, capabilities, input/output specifications, and authentication requirements. Based on this discovery, the Client selects a Remote Agent aligned with the User’s task. Next, the Client Agent is responsible for Task Initiation. It constructs a structured Task object, encapsulating the User’s intent, relevant metadata, and formatted inputs. It then sends this task to the selected Remote Agent using a well-formed Message. During execution, the Client Agent manages the Message and Artifact Exchange. It communicates bi-directionally with the Remote Agent, sending new instructions or follow-ups, and receiving outputs—termed Artifacts—along with any intermediate updates. For long-running or stateful interactions, it maintains Session Context, using identifiers to group related exchanges under a unified workflow.

The Client Agent also oversees Error Handling, parsing any failure responses returned by the Remote Agent, and executing appropriate recovery strategies such as retries, fallback agent selection, or User notifications. After execution, the Result Presentation step involves transforming Artifacts into a user-consumable format and integrating them into the surrounding application or user interface.

Where supported, the Client Agent may handle Asynchronous Communication through mechanisms such as Server-Sent Events (SSE) or push notifications. For SSE, it establishes a persistent HTTP connection and streams updates in real time. If push notification support is available, the Client Agent registers with a notification service to receive task updates delivered out-of-band. Altogether, the Client Agent acts as the execution orchestrator, data translator, and communication bridge within the A2A protocol, enabling intelligent, context-aware interactions on behalf of the User.

#### 5.1.3 Remote Agent (Server)

The Remote Agent (Server) is the service endpoint that executes tasks delegated by the Client Agent. It provides one or more Skills, which represent discrete operations it can perform ranging from simple data retrieval to complex computations or orchestrations involving external APIs or databases. Each skill is formally defined by its input and output schema, enabling consistent invocation across clients.

To make these capabilities discoverable, the Remote Agent publishes an Agent Card—a structured metadata document that includes a list of available skills, usage instructions, input/output formats, supported protocols, and authentication requirements. This Agent Card acts as both an advertisement and an interface contract for interacting agents.

The Remote Agent must also manage its internal Resource Usage, ensuring fair allocation of compute, memory, network, and storage resources during task execution. Alongside execution, it is responsible for enforcing Security and Access Control mechanisms. This includes authenticating Clients, verifying message integrity, and authorizing access to specific skills based on access policies or token scopes. By abstracting service capabilities into modular, independently managed components, the Remote Agent supports composability, reliability, and interoperability within agentic ecosystems.

### 5.2 A2A Main Components

An A2A agent is structured around several core components that define its behavior, capabilities, and interactions. These components serve as the operational and semantic building blocks for any agent to function within an agent-to-agent ecosystem.

Agent Card acts as a self-description and discovery mechanism. It is a JSON-formatted document that publicly declares the agent’s metadata, including its name, version, description, supported skills, and authentication requirements. Client Agents rely on Agent Cards to discover and evaluate Remote Agents that can fulfill specific task criteria. As the primary entry point for coordination, an agent without an Agent Card is effectively invisible within the A2A system.

Skills represent the actionable capabilities offered by an agent. Each skill is described by a name, purpose, expected input parameters, and output format. Skills are invoked via Tasks and encapsulate the core utility the agent provides. An agent’s relevance and specialization are directly tied to the breadth and precision of its published skills.

Task is the atomic unit of work delegation. It specifies the skill to be executed, along with input parameters and contextual metadata. Tasks are issued by Client Agents and processed by Remote Agents, enabling asynchronous or synchronous collaboration. By structuring intention and invocation in a standardized format, Tasks allow A2A agents to operate interoperably across diverse systems.

Messages serve as the primary communication channel between agents. These encapsulate data exchange and coordination activities such as task submission, intermediate status updates, or artifact delivery—and can be composed of multiple typed parts including plain text, structured data, or file references. Without Messages, inter-agent interaction would not be possible, making them foundational to the A2A protocol.
Artifacts are the tangible outputs of skill execution. Once a Remote Agent completes a task, it generates Artifacts that may contain structured responses, computed results, documents, or linked data. These outputs are transmitted back to the Client Agent, which may render them to the User or incorporate them into downstream processes. Artifacts represent the materialized knowledge or value created through agentic collaboration.

### 5.3 A2A Transport Layer and Communication

The A2A protocol supports multiple transport mechanisms to enable communication between Client and Remote Agents, tailored to support both synchronous and asynchronous workflows. When real-time streaming is required and supported by both parties, Server-Sent Events (SSE) can be employed. SSE establishes a persistent HTTP connection over which the Remote Agent can send live status updates or partial Artifacts to the Client Agent, facilitating continuous feedback during long-running tasks.

In scenarios where persistent connections are impractical such as mobile or distributed deployments—the protocol accommodates Push Notifications. These are implemented through a PushNotificationService interface that allows the Remote Agent to notify the Client about task progress or completion via out-of-band channels. This model is particularly suited for latency-tolerant workflows and background task orchestration.

All core task communications in A2A adhere to the JSON-RPC 2.0 specification. This ensures a standardized format for method invocation, parameter passing, and result encapsulation. Additionally, Remote Agent discovery is bootstrapped via HTTP GET requests directed at the Agent’s endpoint, specifically retrieving its Agent Card as a structured representation of supported capabilities. Together, these mechanisms enable flexible, interoperable, and extensible communication across diverse runtime environments.

### 5.4 A2A Remote Agent (Server) Lifecycle

The lifecycle of a Remote Agent in the A2A protocol follows a structured progression through four key phases: Creation, Operation, Update, and Termination. Each phase reflects a distinct set of responsibilities critical to ensuring secure, discoverable, and reliable agent behavior.

Creation begins with the publication of the Agent Card, a JSON-formatted document served at /.well-known/agent.json, which declares metadata such as the agent’s name, version, supported skills, and authentication schemes. Once the Agent Card is made available, the agent service is deployed at a designated endpoint and configured to handle JSON-RPC 2.0 requests over HTTP. To complete the creation phase, the Remote Agent must implement the declared authentication mechanisms, enabling secure client verification and access control.

During Operation, the Remote Agent processes Tasks submitted by Client Agents in accordance with its advertised skills. This includes receiving structured Task payloads, executing the associated skill logic, and managing ongoing communication through JSON-RPC status messages and Artifact delivery. If supported, the agent may also stream asynchronous updates using Server-Sent Events (SSE) or deliver them through a registered PushNotificationService. The agent is responsible for maintaining internal task state throughout execution to ensure consistency and traceability across interactions.

In the Update phase, the Remote Agent refreshes its capabilities or configurations. This includes incrementing the version field in the Agent Card, adding new skills or authentication modes, and applying security patches to maintain compliance. The agent may also deprecate outdated features or legacy interfaces, ideally signaling these changes to clients through updated documentation or explicit lifecycle status fields.

Finally, during Termination, the Remote Agent gracefully winds down its operations. In-flight Tasks are driven to completion or transitioned to a terminal state, and any open SSE streams are closed. The service then deregisters its Agent Card—by removing or archiving the published metadata and releases allocated system resources, ensuring a clean shutdown with no residual exposure or stale endpoints. A well-defined Remote Agent lifecycle enhances discoverability, promotes interoperability, and ensures that agent-based collaboration remains secure, consistent, and predictable within the broader A2A ecosystem.

### 5.5 Security Challenges and Mitigations Across the A2A Lifecycle

A secure A2A deployment requires addressing threats across all lifecycle phases creation, operation, update, and termination. Table [4](https://arxiv.org/html/2505.02279v1#S5.T4 "Table 4 ‣ 5.5 Security Challenges and Mitigations Across the A2A Lifecycle ‣ 5 A2A Architecture ‣ A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)") consolidates principal vulnerabilities and corresponding mitigation strategies, drawn from official A2A protocol references and recent security analyses.

Table 4: A2A Lifecycle Security Challenges and Mitigation Strategies

| Phase | Security Challenge | Threat Description | Mitigation Strategy |
| --- | --- | --- | --- |
| Creation | Agent Card & Manifest Spoofing | Adversaries may tamper with the Agent Card at /.well-known/agent.json, impersonating a trusted Remote Agent. | Digitally sign Agent Cards, verify checksums during retrieval, and harden CI/CD pipelines to prevent injection \[ [9](https://arxiv.org/html/2505.02279v1#bib.bib9 "")\]. |
| --- | --- | --- | --- |
| Operation | Task Injection & Command Forgery | Malicious tasks/send or tasks/sendSubscribe calls may manipulate JSON-RPC to trigger unauthorized execution. | Enforce TLS, use JSON Web Signatures (JWS), validate schemas, and issue scoped capability tokens \[ [44](https://arxiv.org/html/2505.02279v1#bib.bib44 "")\]. |
| | Push Notification Hijacking | Attackers may spoof SSE endpoints or intercept notifications, leading to fake updates or leakage. | Authenticate notification channels, isolate streams per session, and sign pushed events \[ [45](https://arxiv.org/html/2505.02279v1#bib.bib45 "")\]. |
| Update | Unauthorized Capability Injection & Version Drift | Unauthorized actors may add hidden skills to Agent Cards, or clients may operate on outdated configurations. | Use immutable, versioned manifests, detect drift with GitOps, and require signed manifest diffs \[ [46](https://arxiv.org/html/2505.02279v1#bib.bib46 "")\]. |
| Termination | Orphaned Resources & Audit Gaps | Tokens, SSE streams, or agent registrations may persist after use, complicating security audits. | Implement shutdown hooks, revoke credentials, and centralize audit logging with enforced retention \[ [47](https://arxiv.org/html/2505.02279v1#bib.bib47 "")\]. |

## 6 ACP Core Architecture

The Agent Communication Protocol (ACP) defines a layered, REST-native framework for interoperable AI agents. Its static architecture comprises distinct actors and protocol layers, each responsible for a well-defined set of functions.

https://arxiv.org/html/2505.02279v1/ACP.pngFigure 5: An overview of ACP

### 6.1 ACP Architecture Overview

The Agent Communication Protocol (ACP) defines a streamlined three-role architecture designed to standardize discovery, invocation, and interaction among AI agents. This architecture ensures that clients can seamlessly locate agents, initiate structured task requests, and receive multimodal responses without requiring bespoke integrations.

At the entry point of this architecture is the Agent Client, which initiates communication by discovering agents through a published registry and composing structured requests in ACP compliant format. It encapsulates user intent into multi-part messages, manages session-level context if needed, and processes ordered response parts ranging from plain text to rich artifacts and binary data returned by agents.

At the center of the ACP system is the ACP Server, which acts as a protocol broker. It maintains the Agent Registry, a metadata catalog defined by the Agent Detail Schema, and enforces system-wide policies including authentication, authorization, and rate limiting. Upon receiving a client request, the ACP Server performs agent lookup and routing, ensures compliance with registered capabilities, and facilitates secure transport of response parts back to the client in the prescribed order.

The ACP Agent represents the execution endpoint, where domain-specific logic resides. It may operate as a stateless microservice or maintain session context to support multi-turn interactions. The agent ingests structured requests composed of ordered message parts each tagged with semantic metadata and processes them in accordance with the registered skill definitions. Upon task completion, the agent emits response parts that conform to ACP’s Message Structure specification, enabling a uniform and interpretable response pipeline.

Together, these three components establish a modular and interoperable framework for agent communication, promoting scalable deployment, loose coupling, and clear separation of discovery, orchestration, and execution logic.

### 6.2 ACP Main Components

ACP interactions are governed by a set of core components that define agent behavior, enable runtime interoperability, and standardize task communication. Central to this architecture is the Agent Detail, a self-descriptive JSON or YAML document that serves as the agent’s public identity and capability profile. It provides essential metadata, including the agent’s name, available operations, supported content types, authentication schemes, and runtime diagnostics. Clients rely on Agent Detail as a precondition for invocation, enabling trust and selection without bespoke integration.

Complementing this, Discovery Mechanisms allow clients to locate agents dynamically at runtime. These mechanisms may be centralized—such as registry APIs—or decentralized, including manifest files hosted under well-known URLs (e.g., /.well-known/agent.yml) or embedded within deployment metadata like container labels. This discoverability layer decouples client logic from fixed configurations and supports scalable agent networks.

Once an agent is located, clients issue a Task Request, a structured unit of delegated work. Task Requests are composed of ordered message parts that specify the target operation and include textual inputs, binary payloads, or references to externally hosted data. This design accommodates both synchronous calls and long-running, asynchronous tasks.

All requests and responses conform to ACP’s Message Structure, which standardizes the communication envelope. Each message is an ordered list of parts, with explicit MIME content\_type annotations and either embedded content or dereferenceable content\_url values. Optional name attributes enable the use of semantically tagged Artifacts, facilitating downstream interpretation.

Finally, the result of agent execution is encapsulated in one or more Artifacts. These may consist of structured JSON outputs, plain text completions, binary files, or even nested message references. Artifacts are delivered as part of the Message Structure response and are subsequently rendered, stored, or chained into additional agent workflows, ensuring extensibility and composability across ACP-enabled systems.

### 6.3 ACP Agent Lifecycle

The lifecycle of an ACP agent closely mirrors the A2A framework’s four canonical phases: Creation, Operation, Update, and Termination. Each stage ensures that agent behavior remains discoverable, interoperable, and secure throughout its active deployment.

Creation begins with the configuration and deployment of the agent. This involves declaring the agent’s capabilities and metadata through an Agent Detail manifest, which is made accessible via an ACP-compliant server, such as an ASGI-based or built-in implementation. The agent is initialized with authentication mechanisms and routing logic that collectively secure both service discovery and downstream task execution.

During Operation, agents process structured sendTask requests submitted by clients. These requests contain encoded parameters required for task execution. The ACP runtime supports synchronous execution as well as incremental streaming of intermediate results. Each task progresses through well-defined states—such as created, in\_progress, or awaiting that are managed by the ACP execution engine. For multi-turn workflows, session-level persistence ensures continuity of context across multiple interactions.

In the Update phase, the Agent Detail manifest is refreshed to reflect changes in the agent’s behavior or capabilities. These updates may include new operations, supported MIME types, or version increments. Importantly, the discovery process is resilient to such changes: clients querying the agent registry retrieve the latest manifest without requiring direct API modification, thereby preserving backward compatibility.

Termination involves the graceful decommissioning of the agent. All active tasks are driven to completion, ongoing streams are closed, and the agent’s manifest is deregistered or marked as inactive to prevent future discovery. Any allocated resources are released, and session data is finalized to ensure a clean and auditable shutdown.

### 6.4 Security Considerations Across the ACP Lifecycle

ACP-based systems face distinct security challenges as they progress through their lifecycle phases—from agent registration to shutdown. Table [5](https://arxiv.org/html/2505.02279v1#S6.T5 "Table 5 ‣ 6.4 Security Considerations Across the ACP Lifecycle ‣ 6 ACP Core Architecture ‣ A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)") summarizes key threats and their corresponding mitigation strategies, grounded in recent red-teaming, protocol, and platform-level research.

Table 5: ACP Lifecycle Security Challenges and Mitigation Strategies

| Phase | Security Challenge | Threat Description | Mitigation Strategy |
| --- | --- | --- | --- |
| Creation | Metadata Spoofing & Supply Chain Attacks | Attackers may publish forged Agent Detail manifests (e.g., /.well-known/agent.yml) to impersonate agents or inject malicious skills. | Digitally sign all manifests, verify at discovery, and enforce CI/CD signature checks and artifact validation \[ [10](https://arxiv.org/html/2505.02279v1#bib.bib10 "")\]. |
| --- | --- | --- | --- |
| Operation | Message Tampering & MITM | Adversaries can intercept or alter sendTask or getTask RPC calls, leading to payload injection or message corruption. | Use TLS for transport security and sign each message part with JWS \[ [44](https://arxiv.org/html/2505.02279v1#bib.bib44 "")\]. |
| | Auth Flaws & Unauthorized Access | Weak bearer token enforcement may allow unauthorized execution or task disruption. | Apply capability-scoped, short-lived tokens; enforce mutual TLS with identity revocation \[ [46](https://arxiv.org/html/2505.02279v1#bib.bib46 "")\]. |
| Persistence | Session Hijacking & Privacy Leaks | Replay attacks or token theft may occur in long-lived sessions without proper binding or encryption. | Rotate session IDs, encrypt persisted context, and minimize token lifetimes \[ [45](https://arxiv.org/html/2505.02279v1#bib.bib45 "")\]. |
| Update | Version Rollback & Config Drift | Stale manifests or software may reintroduce patched vulnerabilities post-update. | Enforce immutable, versioned manifests and use GitOps to detect drift \[ [48](https://arxiv.org/html/2505.02279v1#bib.bib48 "")\]. |
| Termination | Orphaned Resources & Audit Gaps | Failing to revoke tokens or close SSE streams complicates cleanup and forensics. | Drain active tasks, revoke credentials, and centralize audit logging with retention policies \[ [48](https://arxiv.org/html/2505.02279v1#bib.bib48 "")\]. |

## 7 ANP Architecture

Agent Network Protocol (ANP) is a decentralized, peer-to-peer communication standard designed for cross-platform agent interoperability on the open internet. ANP enables agents to autonomously discover, authenticate, and interact using structured metadata and AI-native data exchange. The following sections align ANP’s architecture with a standardized lifecycle and modular framework, modeled consistently with MCP, A2A, and ACP.

https://arxiv.org/html/2505.02279v1/anp-architecture.pngFigure 6: An overview of ANP \[ [12](https://arxiv.org/html/2505.02279v1#bib.bib12 ""), [11](https://arxiv.org/html/2505.02279v1#bib.bib11 "")\]

### 7.1 Core Components

The Agent Network Protocol (ANP) is underpinned by a set of foundational components that collectively support decentralized identity, semantic self-description, discovery, and adaptive interaction. At the core is the Agent Identity, which employs Decentralized Identifiers (DIDs) to uniquely identify agents across platforms. Specifically, ANP adopts the did:wba method, where each identifier corresponds to an HTTPS-hosted DID document, thereby leveraging existing Web infrastructure for decentralized identity resolution.

Building upon this identity layer is the Agent Description, implemented through the Agent Description Protocol (ADP). These JSON-LD formatted documents contain structured metadata about the agent, including its name, capabilities, supported protocols, authentication schemes, and service endpoints. They serve as the agent’s publicly accessible profile, facilitating interoperability and semantic understanding.

Agents expose their presence and capabilities through a Discovery Directory, typically located at the standardized .well-known/agent-descriptions endpoint. This directory enables both human users and automated systems to retrieve a list of available agents under a given domain, forming the basis for scalable agent indexing and search.

To support interaction, ANP accommodates two categories of communication interfaces: Structured Interfaces, such as JSON-RPC and OpenAPI, and Natural Language Interfaces, defined via YAML or equivalent schema files. Both interface types are declared within the agent’s description and enable flexible interaction patterns suited to varying complexity and use cases.

Finally, the Meta-Protocol Negotiator facilitates dynamic protocol alignment between agents. This mechanism allows agents to exchange natural language descriptions of their communication requirements and capabilities, from which compatible interaction protocols can be negotiated and instantiated. By supporting runtime adaptability and negotiation, this layer ensures seamless interoperability even among heterogeneous agent ecosystems.

### 7.2 ANP Agent Lifecycle

The ANP agent lifecycle adheres to the canonical phases of Creation, Operation, Update, and Termination, reflecting the decentralized design principles of the Agent Network Protocol. Each phase ensures that agents remain discoverable, verifiable, and interoperable within a globally distributed agent ecosystem.

Creation initiates with the generation of a decentralized identifier (DID) using the did:wba method. This identifier is associated with a publicly resolvable HTTPS endpoint hosting the agent’s DID document. In parallel, the agent prepares a self-descriptive Agent Description (ADP) document in JSON-LD format, detailing its services, supported protocols, and authentication mechanisms. The ADP is then published under a standardized path such as /.well-known/agent-descriptions, enabling web-based discovery or optional registration with search agents.

During the Operation phase, agents authenticate and interact via cryptographic credentials defined in their DID documents. All communications follow structured interaction models declared in the ADP—such as JSON-RPC for precise invocation or YAML-based interfaces for natural language negotiation. Secure transport is established using HTTPS and, where applicable, real-time communication is supported through mechanisms such as Server-Sent Events (SSE) or long polling. Agents act autonomously or cooperatively by invoking external services, interpreting requests, and returning results in a standardized format.

The Update phase allows agents to revise their ADP documents and associated DID metadata to reflect evolving capabilities or interface changes. These updates are automatically propagated through recurring crawls by indexing services or explicitly refreshed via active discovery endpoints. Because agent identity and service descriptions are independently versioned and published, clients can dynamically adapt to updates without breaking existing integrations.

Termination involves the intentional deactivation of an agent. This includes the removal or archival of its DID document and the depublication of its ADP endpoint from discovery directories. Any issued authentication tokens, access credentials, or associated metadata must be revoked to ensure security. A clean shutdown preserves the integrity of the agent ecosystem by preventing stale or orphaned entries from persisting in discovery indexes or trusted registries.

### 7.3 Transport and Format

ANP relies on HTTP(S) for transport and JSON-LD for data formatting. Schema.org vocabularies and contexts like ‘ad:‘ are used for semantic clarity. Structured interfaces such as JSON-RPC and OpenAPI are compatible and embedded via ADP.

### 7.4 Security Considerations Across the ANP Lifecycle

Table [6](https://arxiv.org/html/2505.02279v1#S7.T6 "Table 6 ‣ 7.4 Security Considerations Across the ANP Lifecycle ‣ 7 ANP Architecture ‣ A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)") summarizes major threats and corresponding mitigations across the ANP lifecycle.

Table 6: ANP Lifecycle Security Challenges and Mitigation Strategies

| Phase | Security Challenge | Threat Description | Mitigation Strategy |
| --- | --- | --- | --- |
| Creation | Identity Spoofing | DID documents may be spoofed or hosted insecurely, leading to agent misidentification. | Enforce HTTPS-hosted DIDs, verify with DNS records, and require DID signature validation. |
| Operation | Unverified Agents | Malicious actors may bypass DID checks or use spoofed credentials. | Authenticate via DID public keys and validate humanAuthorization for sensitive actions. |
| | Interface Tampering | Agents may alter structured interfaces or inject into natural language endpoints. | Require cryptographic signing of interfaces and log access events with source metadata. |
| Update | Stale Descriptions | Outdated or manipulated agent metadata may deceive clients. | Automate crawling of agent descriptions and validate against known-good hashes. |
| Termination | Orphaned Identifiers | Expired DIDs or agent declarations (ADPs) may persist in registries or caches. | Use expiration timestamps and require revocation signaling during deregistration. |
Table 7: Comparison of MCP, ACP, A2A, and ANP Protocols

| Aspect | MCP (Model Context Protocol) | ACP (Agent Communication Protocol) | A2A (Agent-to-Agent Protocol) | ANP (Agent Network Protocol) |
| --- | --- | --- | --- | --- |
| Architecture Model | Client–Server with JSON-RPC primitives | Brokered Client–Server (Registry + Task Routing) | Peer-like Client ↔\leftrightarrow Remote Agent | Decentralized Peer-to-Peer |
| Agent Discovery | Manual registration or static URL lookup | Registry-based | Agent Card retrieval via HTTP | Search Engine Discovery |
| Identity & Auth | Token-based auth; supports DIDs optionally | Bearer tokens, mutual TLS, JWS | DID-based handshake or out-of-band headers | Decentralized Identifiers (DID), especially did:wba |
| Message Format | JSON-RPC 2.0 with Prompts, Tools, Resources | Structured multipart messages with MIME-typed parts | Task + Artifact messaging over JSON | JSON-LD with Schema.org and ADP/Meta-Protocol negotiation |
| Core Components | Tools, Prompts, Resources, Sampling | Agent Detail, Message, Task Request, Artifact | Agent Card, Task, Message, Artifact | DID Document, Agent Description, Meta-Protocol, Structured Interface |
| Transport Layer | HTTP, Stdio, Server-Sent Events (SSE) | HTTP with incremental streams | HTTP with optional SSE + Push Notifications | HTTP with JSON-LD over TLS |
| Session Support | Stateless + optional persistent tool context | Session-aware with run state tracking | Session-aware or stateless; client-managed IDs | Stateless; DID-authenticated tokens used across connections |
| Target Scope | LLM ↔\leftrightarrow External Tool/Service integration | Model-Agnostic, Infrastructure-level agents | Trusted enterprise task delegation | Open Internet agent interconnectivity |
| Primary Use Case | Augment LLMs with external capabilities (e.g., code, search) | Secure, typed message exchange for diverse agents | Multi-agent workflows within organizational trust boundaries | Cross-platform agent discovery, secure P2P execution |
| Strengths | Tight LLM integration; resource injection | Multimodal messaging; brokered registry; tool modularity | Inter-agent negotiation; artifact-driven delegation | DID-based trustless identity; AI-native protocol negotiation |
| Limitations | Centralized server assumption; prompt injection risks | Registry required; strong assumptions on server control | Enterprise-centric; assumes agent catalog | High negotiation overhead; evolving adoption ecosystem |

## 8 Comparison of Agent Protocols

To facilitate a clearer understanding of how major agent interoperability protocols differ, Table [7](https://arxiv.org/html/2505.02279v1#S7.T7 "Table 7 ‣ 7.4 Security Considerations Across the ANP Lifecycle ‣ 7 ANP Architecture ‣ A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP)") presents a side-by-side comparison of four widely discussed frameworks: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP). This structured analysis highlights their architectural choices, messaging formats, discovery methods, session models, and intended use cases, offering insights into their suitability across diverse deployment scenarios.

## 9 Phased Adoption Roadmap for Agent Interoperability

This section presents a practical, multi-stage deployment strategy for agent interoperability based on protocol maturity, integration complexity, and domain-specific use cases. The roadmap helps organizations gradually adopt the most suitable agent communication standards while ensuring scalability, composability, and security.

### 9.1 Stage 1 – MCP for Tool Invocation

The initial phase involves adopting the Model Context Protocol (MCP) to enable secure and structured interaction between large language models (LLMs) and external tools or resources. MCP leverages a JSON-RPC-based client-server model, making it ideal for early agent integration where tool invocation, deterministic execution, and typed inputs/outputs are critical.

### 9.2 Stage 2 – ACP for Rich Interaction

Once foundational tool capabilities are in place, the Agent Communication Protocol (ACP) can be layered to support asynchronous, multimodal, and REST-native messaging. ACP introduces ordered message parts, flexible task schemas, and streaming support—features that enable richer agent conversations and integration with broader RESTful ecosystems.

### 9.3 Stage 3 – A2A for Enterprise Collaboration

In more complex enterprise environments, the Agent-to-Agent (A2A) protocol enables multi-agent workflows and task orchestration through structured capability cards and artifact exchanges. A2A supports dynamic discovery via Agent Cards and secure intra-organizational collaboration in trusted contexts.

### 9.4 Stage 4 – ANP for Open Agent Markets

The final phase involves extending interoperability to the open internet using the Agent Network Protocol (ANP). ANP facilitates decentralized agent discovery, DID-based identity verification, and peer-to-peer communication using JSON-LD graphs. It provides the foundation for scalable, cross-platform agent marketplaces and AI-native web interaction. This phased approach enables organizations to adopt agent communication protocols progressively, maximizing interoperability while minimizing integration complexity at each stage.

## 10 Conclusion

As autonomous agents powered by large language models proliferate across domains, the demand for secure, modular, and interoperable communication grows increasingly urgent. This survey presented a structured analysis of four emerging protocols—MCP, ACP, A2A, and ANP—that each address distinct layers of agent interoperability. By unifying tool invocation, multimodal messaging, task coordination, and decentralized discovery, these protocols collectively form the foundation for scalable multi-agent systems. The comparative evaluation demonstrates that no single protocol suffices across all contexts; instead, a phased, complementary adoption strategy—beginning with MCP and progressing through ACP and A2A to ANP—offers a practical pathway for deploying agent ecosystems. Future research should explore protocol interoperability bridges, trust frameworks for agent collaboration, and standardized evaluation benchmarks to accelerate adoption and ensure resilience in real-world deployments. These foundational efforts will be critical for advancing the next generation of intelligent, networked agents.

## References

- \[1\]↑
Tom B Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla
Dhariwal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell,
et al.

Language models are few-shot learners.

Advances in neural information processing systems,
33:1877–1901, 2020.

- \[2\]↑
Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney
von Arx, et al.

On the opportunities and risks of foundation models.

arXiv preprint arXiv:2108.07258, 2021.

- \[3\]↑
Lei Wang, Chen Ma, Xueyang Feng, Zeyu Zhang, Hao Yang, Jingsen Zhang, Zhiyuan
Chen, Jiakai Tang, Xu Chen, Yankai Lin, Wayne Xin Zhao, Zhewei Wei, and
Jirong Wen.

A survey on large language model based autonomous agents.

Frontiers of Computer Science, 18(6), Mar. 2024.

- \[4\]↑
Grégoire Mialon, Roberto Dessì, Maria Lomeli, Christoforos Nalmpantis, Ram
Pasunuru, Roberta Raileanu, Baptiste Rozière, Timo Schick, Jane Dwivedi-Yu,
Asli Celikyilmaz, Edouard Grave, Yann LeCun, and Thomas Scialom.

Augmented language models: A survey.

arXiv preprint arXiv:2302.07842, 2023.

- \[5\]↑
Taicheng Guo, Xiuying Chen, Yaqi Wang, Ruidi Chang, Shichao Pei, Nitesh V.
Chawla, Olaf Wiest, and Xiangliang Zhang.

Large language model based multi-agents: A survey of progress and
challenges.

arXiv preprint arXiv:2402.01680, 2024.

Accessed: Apr. 30, 2025.

- \[6\]↑
Model Context Protocol.

Introduction to model context protocol (mcp).

[https://modelcontextprotocol.io/introduction](https://modelcontextprotocol.io/introduction ""), 2024.

Accessed: Apr. 2025.

- \[7\]↑
Aditi Singh, Abul Ehtesham, Saket Kumar, and Tala Talaei Khoei.

A survey of the model context protocol (mcp): Standardizing context
to enhance large language models (llms).

Preprints, Apr. 2025.

- \[8\]↑
Partha Pratim Ray.

A survey on model context protocol: Architecture, state-of-the-art,
challenges and future directions.

TechRxiv, Apr. 2025.

Accessed: Apr. 30, 2025.

- \[9\]↑
Google.

Agent2agent (a2a) protocol documentation.

[https://google.github.io/A2A/](https://google.github.io/A2A/ ""), 2024.

Accessed: Apr. 2025.

- \[10\]↑
IBM BeeAI.

Introduction to agent communication protocol (acp).

[https://docs.beeai.dev/acp/alpha/introduction](https://docs.beeai.dev/acp/alpha/introduction ""), 2024.

Accessed: Apr. 2025.

- \[11\]↑
Agent Network Protocol Contributors.

Agent network protocol (anp).

[https://github.com/agent-network-protocol/AgentNetworkProtocol](https://github.com/agent-network-protocol/AgentNetworkProtocol ""),
2024.

Accessed: Apr. 30, 2025.

- \[12\]↑
Agent Network Protocol Contributors.

Agent network protocol official website.

[https://agent-network-protocol.com/](https://agent-network-protocol.com/ ""), 2024.

Accessed: Apr. 30, 2025.

- \[13\]↑
Khanh-Tung Tran, Dung Dao, Minh-Duong Nguyen, Quoc-Viet Pham, Barry O’Sullivan,
and Hoang D. Nguyen.

Multi-agent collaboration mechanisms: A survey of llms.

CoRR, abs/2501.06322, 2025.

- \[14\]↑
Taicheng Guo, Xiuying Chen, Yaqi Wang, Ruidi Chang, Shichao Pei, Nitesh V.
Chawla, Olaf Wiest, and Xiangliang Zhang.

Large language model based multi-agents: A survey of progress and
challenges.

CoRR, abs/2402.01680, 2024.

- \[15\]↑
Bingyu Yan, Xiaoming Zhang, Litian Zhang, Lian Zhang, Ziyi Zhou, Dezhuang Miao,
and Chaozhuo Li.

Beyond self-talk: A communication-centric survey of llm-based
multi-agent systems.

CoRR, abs/2502.14321, 2025.

- \[16\]↑
Akram Sheriff.

Dynamic llm agent metadata manifest-based discovery of agents in an
llm agentic application platform.

Technical Report 7522, Technical Disclosure Commons, 2024.

- \[17\]↑
Ivan Milev, Mislav Balunovic, Maximilian Baader, and Martin Vechev.

Toolfuzz: Automated agent tool testing.

CoRR, abs/2503.04479, 2024.

- \[18\]↑
Stuart J. Russell and Peter Norvig.

Artificial Intelligence: A Modern Approach.

Prentice Hall, 3rd edition, 2010.

- \[19\]↑
Michael Wooldridge.

An Introduction to MultiAgent Systems.

John Wiley & Sons, 2009.

- \[20\]↑
Stan Franklin and Art Graesser.

Is it an agent, or just a program? a taxonomy for autonomous agents.

International Journal of Cognitive Science, 6(1–2):29–36,
1997.

- \[21\]↑
Nicholas R. Jennings.

On agent-based software engineering.

Artificial Intelligence, 117(2):277–296, 2000.

- \[22\]↑
Michael R. Genesereth and Scott P. Ketchpel.

The kqml protocol: A specification of language and communication.

In Proceedings of the Third International Conference on
Information and Knowledge Management (CIKM), pages 1–10. ACM, 1993.

- \[23\]↑
Tim Finin, Rich Fritzson, Donald McKay, and Robin McEntire.

Kqml as an agent communication language.

In Proceedings of the third international conference on
Information and knowledge management, pages 456–463, 1994.

- \[24\]↑
Foundation for Intelligent Physical Agents.

Fipa communicative act library specification.

[https://www.fipa.org/specs/fipa00037/SC00037J.html](https://www.fipa.org/specs/fipa00037/SC00037J.html ""), 2000.

- \[25\]↑
Francisco Curbera, Marc Duftler, Rania Khalaf, William Nagy, Nirmal Mukhi, and
Sanjiva Weerawarana.

Web services: Why and how.

IBM Systems Journal, 41(2):170–177, 2002.

- \[26\]↑
Gregor Hohpe and Bobby Woolf.

Enterprise Integration Patterns: Designing, Building, and
Deploying Messaging Solutions.

Addison-Wesley Signature Series (Fowler). Addison-Wesley
Professional, 2006.

- \[27\]↑
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio Petroni, Vladimir
Karpukhin, Naman Goyal, Mike Lewis, William Yih, Tim Rocktäschel, and
Sebastian Riedel.

Retrieval-augmented generation for knowledge-intensive nlp tasks.

In Advances in Neural Information Processing Systems,
volume 33, pages 9459–9474, 2020.

- \[28\]↑
Gautier Izacard and Edouard Grave.

Towards an efficient pipeline for knowledge-intensive nlp tasks.

arXiv preprint arXiv:2112.04426, 2021.

- \[29\]↑
OpenAI.

Function calling in openai models.

[https://platform.openai.com/docs/guides/functions](https://platform.openai.com/docs/guides/functions ""), 2023.

Accessed: Apr. 2025.

- \[30\]↑
Harrison Chase.

Langchain: Build applications with llms through composability.

[https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain ""), 2022.

Accessed: Apr. 2025.

- \[31\]↑
Jerry Wu et al.

Llamaindex: Connecting llms to your knowledge.

[https://github.com/jerryjliu/llama\_index](https://github.com/jerryjliu/llama_index ""), 2023.

Accessed: Apr. 2025.

- \[32\]↑
OpenAI.

Openai plugin store.

[https://platform.openai.com/docs/plugins](https://platform.openai.com/docs/plugins ""), 2023.

- \[33\]↑
Fangzhou Liu, Xinyu Li, Zihan Wu, Yang Song, Wayne Xin Zhao, and Ji-Rong Wen.

Autotool: Building general-purpose llm agents with self-extendable
toolsets.

arXiv preprint arXiv:2403.02659, 2024.

- \[34\]↑
Timo Schick and Hinrich Schütze.

Toolformer: Language models can teach themselves to use tools.

In Proceedings of the 61st Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers), pages 8213–8229. ACL,
2023.

- \[35\]↑
Sheng Yao, Eric Urbach, and Dale Schuurmans.

React: Synergizing reasoning and acting in language models.

In Proceedings of the 2023 Conference on Empirical Methods in
Natural Language Processing (EMNLP), pages 2659–2671. ACL, 2023.

- \[36\]↑
AutoGen Community.

Autogpt: An experimental open-source autonomous agent using gpt-4.

[https://github.com/Significant-Gravitas/Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT ""), 2023.

Accessed: Apr. 2025.

- \[37\]↑
Thomas Shinn and Regina Barzilay.

Reflexion: Language model self-improvement through iterative learning
from failures.

arXiv preprint arXiv:2310.02493, 2023.

Available at [https://arxiv.org/abs/2310.02493](https://arxiv.org/abs/2310.02493 "").

- \[38\]↑
CrewAI Project.

CrewAI: High-level crew abstractions for collaborative llm agents.

[https://github.com/crew-ai/crewai](https://github.com/crew-ai/crewai ""), 2024.

Accessed: Apr. 2025.

- \[39\]↑
SmolAgents Project.

Smolagents: A single-file python library for multi-modal llm agent
prototyping.

[https://github.com/smolagents/smolagents](https://github.org/smolagents/smolagents ""), 2024.

Accessed: Apr. 2025.

- \[40\]↑
AutoGen Community.

Ag2 (autogen): An open-source agentos with human-in-the-loop
workflows.

[https://github.com/Significant-Gravitas/Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT ""), 2025.

Accessed: Apr. 2025.

- \[41\]↑
Microsoft.

Semantic kernel: Sdk for llm orchestration and memory.

[https://github.com/microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel ""), 2024.

Accessed: Apr. 2025.

- \[42\]↑
OpenAI.

Swarm: Stateless multi-agent coordination via json-rpc routines.

[https://platform.openai.com/docs/models/swarm](https://platform.openai.com/docs/models/swarm ""), 2024.

Accessed: Apr. 2025.

- \[43\]↑
Dejan S. Milojicic, Markus Breugst, Ingo Busse, John Campbell, Stefan Covaci,
Barry Friedman, Kazuya Kosaka, Danny B. Lange, Kouichi Ono, Mitsuru Oshima,
Cynthia Tham, Sankar Virdhagriswaran, and Jim White.

Masif: The omg mobile agent system interoperability facility.

In Proceedings of the Second International Workshop on Mobile
Agents, MA ’98, page 50–67, Berlin, Heidelberg, 1998. Springer-Verlag.

- \[44\]↑
Pengfei He, Yupin Lin, Shen Dong, Han Xu, Yue Xing, and Hui Liu.

Red-teaming llm multi-agent systems via communication attacks.

arXiv preprint arXiv:2502.14847, 2025.

- \[45\]↑
Sahar Abdelnabi, Amr Gomaa, Eugene Bagdasarian, Per Ola Kristensson, and Reza
Shokri.

Firewalls to secure dynamic llm agentic networks.

arXiv preprint arXiv:2502.01822, 2025.

- \[46\]↑
Carol Doe.

A2a protocol: An in‐depth guide. the need for agent
interoperability.

[https://medium.com/@author/a2a-protocol-guide](https://medium.com/@author/a2a-protocol-guide ""), 2025.

\[Online; accessed 2025-04-24\].

- \[47\]↑
Google Developers Blog.

Announcing the agent2agent protocol (a2a).

[https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/ ""),
2025.

\[Online; accessed 2025-04-24\].

- \[48\]↑
Fiona Zhang and George Kumar.

Ai agents under threat: A survey of key security challenges and
mitigations.

In Proceedings of the ACM Conference on Security in AI Systems,
pages 1–12, 2025.

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

<research_source type="scraped_from_research" phase="exploration" file="essential-guide-to-agentic-ai-governance-frameworks-for-futu.md">
<details>
<summary>Agentic AI Governance Frameworks</summary>

Phase: [EXPLORATION]

**Source URL:** <https://www.nice.com/agentic-ai/agentic-ai-governance-frameworks>

# Agentic AI Governance Frameworks

_What does a comprehensive governance framework for enterprise agentic AI look like — and how do policy definition, model oversight, audit logging, escalation protocols, and ongoing compliance monitoring work together to keep autonomous AI operating within acceptable boundaries?_

### Key Takeaway

Provides a comprehensive governance framework for enterprise agentic AI deployment — covering policy definition, model oversight, audit logging, escalation protocols, and ongoing compliance monitoring. NiCE's governance layer within CXone is presented as the industry's most complete framework for responsible autonomous AI in customer service.

In 2024, something shifted in how enterprises deploy artificial intelligence. A financial services firm in Singapore automated 40% of its loan pre-qualification process using autonomous agents that could gather documents, verify income, check credit policies, and draft preliminary decisions—all without a human touching the workflow until final approval. A major health insurer deployed agents that monitor claims patterns, flag anomalies, and initiate fraud investigations across multiple systems. Contact centers began rolling out agents that don’t just answer questions but actively manage entire customer journeys: adjusting routing, scheduling callbacks, triggering retention offers, and updating CRM records in real time through advanced [conversational AI and chatbots](https://www.nice.com/products/conversational-ai-and-chatbots).

These aren’t the chatbots of 2022. Agentic AI refers to systems that can set their own sub-goals, plan multi-step actions, and call external tools or APIs without waiting for human prompts at every turn. They persist across sessions, remember context, and take actions that have real consequences in the world. When a customer calls about a disputed charge, an agentic system might simultaneously pull transaction records, check policy exceptions, draft a resolution letter, and schedule a follow-up—coordinating across billing, CRM, and communication platforms in seconds.

This shift amplifies every AI governance concern enterprises already had. Bias doesn’t just affect a single prediction; it can cascade through a chain of autonomous decisions. Privacy isn’t just about what data a model sees; it’s about what an agent can access, combine, and act upon across multiple systems. Safety isn’t just about model outputs; it’s about agents that can modify records, process payments, or trigger workflows with minimal human intervention. The challenge isn’t whether to govern these intelligent systems—it’s how to govern them without strangling the very speed and autonomy that makes them valuable.

For large contact centers, financial institutions, and public agencies, this is urgent. These organizations are already deploying autonomous agents for customer service, back-office processing, and risk monitoring. They face regulators asking pointed questions about accountability. They manage sensitive data across complex, interconnected systems. And they need governance approaches that work at the speed of agentic systems—not the speed of quarterly compliance reviews.

Agentic AI governance is not a technical control exercise. It’s a strategic business capability that enables safe innovation, regulatory confidence, and trustworthy customer experiences. Organizations that get this right can move faster than competitors because they can demonstrate control to regulators, customers, and boards. Those that treat governance as an afterthought will find themselves slowing down later—or facing consequences when autonomous agents make decisions they can’t explain or defend.

NiCE provides AI-powered CX platform— [NiCE CXone](https://www.nice.com/products/cxone) and [CXone](https://www.nice.com/solutions/call-center-software)—where agentic AI is already orchestrating customer journeys, managing workforce engagement, and enabling real-time compliance. For NiCE, governance isn’t a feature bolted on after deployment. It’s a core design principle embedded into how autonomous agents operate across every customer touchpoint.

https://www.nice.com/_next/image?url=https%3A%2F%2Fresources.nice.com%2Fwp-content%2Fuploads%2F2026%2F04%2Fcontact-center-with-multiple-screens.jpg&w=3840&q=80

## What makes agentic AI different—and why governance must adapt

Traditional AI systems operate in a fundamentally different mode than agentic systems. A predictive model scores a loan application. [A chatbot responds to a customer question](https://www.nice.com/products). A recommendation engine suggests products. In each case, the AI provides an output, and a human (or a deterministic system) decides what to do with it. The governance model is straightforward: control the inputs, validate the model, review the outputs.

Agentic AI breaks this pattern. These systems don’t just produce outputs—they take actions. An agentic system in a contact center might open support tickets, modify CRM records, re-route calls based on real-time sentiment analysis, adjust IVR flows for specific customer segments, trigger refunds within approved limits, or schedule callbacks across multiple systems. The system sets goals, plans steps to achieve them, executes those steps by calling tools and APIs, and adapts based on results. It operates with autonomous decision making rather than waiting for human direction at each step.

Three characteristics fundamentally change what governance must address. First, autonomy: agentic systems act without immediate human prompts, making decisions in real time based on their goals and current context. Second, persistence: they maintain state over long-running workflows, remembering context across sessions and transactions. Third, environment coupling: they act across APIs, legacy applications, cloud platforms, and data sources, affecting multiple systems with each decision chain.

Consider the governance assumptions that worked for traditional AI systems:

- Static workflows with predictable decision points

- Centralized control where humans approve each significant action

- Pre-approved use cases with well-defined boundaries

- Periodic review cycles for model performance and compliance


Agentic systems demand different assumptions:

- Dynamic planning where agents determine their own workflows

- Distributed decision points across tools, systems, and time

- Continuous risk evaluation as agents encounter novel situations

- Real-time intervention capabilities when behavior deviates from policy


A concrete example makes this tangible. Imagine an AI agent monitoring real-time customer sentiment during service interactions using [AI interaction analytics](https://www.nice.com/products/interaction-analytics). When it detects escalating frustration, it automatically adjusts routing to prioritize the call, proposes a remediation offer within pre-set parameters, and flags the interaction for human review if certain thresholds are crossed. The oversight model can’t just evaluate the agent’s predictions—it must follow the entire journey, understanding why the agent chose specific actions and ensuring those actions stayed within policy at each step.

For organizations using platforms like NiCE CXone, this means governance must be embedded where the work happens. It’s not enough to document the model. Governance controls must operate within routing logic, workforce engagement rules, knowledge access permissions, and compliance recording. The policy layer must be as real-time as the agents themselves.

## Why existing AI governance frameworks fall short for autonomous agents

Many enterprises in 2023 and 2024 built governance around generative AI pilots. They created policy documents, prompt guidelines, model risk inventories, and [interaction analytics for monitoring model outputs](https://www.nice.com/products/interaction-analytics). These frameworks assumed a human operator for each meaningful action—someone reviewing outputs, approving decisions, and taking responsibility for consequences. That assumption breaks down with agentic systems.

Legacy governance frameworks typically assume human-in-the-loop at every transaction. They focus on model outputs rather than end-to-end action chains. They rely on static approvals—a sign-off at deployment—instead of continuous risk signals during operation. They treat AI as a tool that humans wield, not as an autonomous actor in enterprise systems.

Specific pain points emerge quickly when organizations try to apply these frameworks to agentic AI. Agents bypass manual checkpoints by chaining tools—an action that looks routine at each step might produce problematic outcomes across the full sequence. Multi-step workflows make attribution difficult; when something goes wrong, it’s unclear which decision in the chain caused the harm. Conventional audit logs capture API calls but not the reasoning that connected them. Security teams find themselves reviewing logs that show what happened without explaining why the agent made those choices.

The contrast is stark:

- Legacy governance operates through periodic reviews, policy PDFs, and manual sign-offs that occur on quarterly or annual cycles

- Effective agentic governance requires real-time policy enforcement, continuous monitoring, and automatic containment when agents approach policy boundaries


Consider a compliance-relevant example in CX. Suppose an agentic system adjusts compliance recording based on conversation topics—triggering enhanced recording when financial advice is discussed, or pausing recording when a customer requests privacy for sensitive personal information. An older governance framework assumed static recording rules: record everything, or record based on simple triggers. It can’t handle an agent that makes real-time decisions about when and how to record based on conversation context. The governance framework needs to be as dynamic as the agent behavior it’s meant to control.

## Core principles of an agentic AI governance framework

Designing governance for agentic AI requires starting from different assumptions than traditional AI governance. The framework must explicitly assume that agents are autonomous, tool-using, and capable of taking consequential actions without human prompts. What follows are the core principles that should shape any agentic AI governance framework.

Identity-first governance treats every agent as a distinct non-human identity. Just as human employees have credentials, permissions, and accountability trails, autonomous agents need the same. Each agent—whether it’s a collections assistant, a routing optimizer, or a QA summarization tool—should have unique agent identities in the enterprise identity and access management system. This makes it possible to track what each agent did, enforce appropriate access controls, and revoke permissions when needed. Without identity-first governance, organizations can’t answer basic questions: which agent accessed this data? Which agent triggered this workflow?

Data-centric protection shifts focus from governing models to governing data. Agentic systems derive their power from combining data sources—CRM records, billing history, interaction transcripts, knowledge bases. Governance must specify which data each agent can see, transform, and move. Data protection isn’t just about the model architecture; it’s about ensuring agents can only access information appropriate to their purpose and can’t exfiltrate or misuse sensitive data.

Lifecycle orientation means managing agents from design through retirement. An agent governance approach must cover initial design and risk assessment, testing in sandbox environments, deployment with appropriate controls, continuous monitoring during operation, updates and retraining, and eventual retirement when the agent is replaced or decommissioned. Each stage has distinct governance requirements; treating deployment as the only governance moment creates security gaps.

Risk-based autonomy scales an agent’s freedom according to task criticality, customer impact, and regulatory risk. A summarization agent with read-only access to transcripts presents different risks than a payment adjustment agent that can modify account balances. Governance models should grant autonomy proportional to risk—more freedom for lower-risk tasks, tighter constraints and more human oversight for high-risk actions.

Continuous oversight replaces static, one-time approvals with always-on monitoring. Effective agentic AI governance requires anomaly detection, behavioral baselines, and kill-switches that can intervene in real time. The approval to deploy an agent isn’t a one-time gate; it’s the beginning of an ongoing oversight relationship where the agent is continuously monitored against policy expectations.

These principles should integrate with existing enterprise governance structures. Organizations with mature model risk management practices can extend those frameworks to cover agentic systems. AI ethics boards, compliance committees, and risk management functions all have roles to play. Creating an entirely separate governance track for agentic AI fragments oversight and creates gaps.

For platform like [CXone contact center solutions](https://www.nice.com/solutions), these principles translate into concrete capabilities: identity management for AI agents, data access policies that restrict what agents can see, lifecycle controls from development through production, and monitoring dashboards that show agent behavior in real time alongside human agent performance.

https://www.nice.com/_next/image?url=https%3A%2F%2Fresources.nice.com%2Fwp-content%2Fuploads%2F2026%2F04%2Fvisualization-of-interconnected-nodes.jpg&w=3840&q=80

## Agentic AI governance architecture: from policy to runtime control

Governance architecture is the plumbing that turns principles and policies into real-time constraints on what agents can do. It’s where abstract commitments to responsible agentic AI adoption become operational realities that prevent harm and enable accountability. The architecture must address three interconnected domains: how agents prove who they are and what they can access, what data and context they can operate within, and how their behavior is monitored and corrected.

### Identity and access for AI agents

Every agent operating in an enterprise environment needs a unique identity in the organization’s IAM system. This applies whether the agent is a customer service agent assistant, a fraud detection monitor, or a workforce scheduling optimizer. The identity should be as distinct and traceable as any human employee’s credentials.

Role-based or attribute-based permissions enforce least privilege. A collections agent might be permitted to view account balances and payment history but prohibited from changing credit limits or closing accounts. A workforce scheduling agent might read performance metrics but require explicit approval to export raw call recordings. These permissions should be specific to the agent’s purpose, not inherited from a generic service account with broad access.

Zero Trust principles apply directly to agentic systems. No implicit trust should be granted based on network location or initial authentication. Every action should be verified against current context—the time of day, the type of task, the sensitivity of the data being accessed. A scheduling agent that typically operates during business hours should trigger alerts if it suddenly makes requests at 3 AM.

Authentication should use strong, short-lived credentials through secure brokers rather than long-lived API keys or super tokens. When agents inherit full customer or admin privilege access, they create massive attack surfaces. Scoped tokens tied to well-defined action sets limit blast radius if credentials are compromised.

This approach aligns with regulatory expectations. SOX controls for financial systems require demonstrable access controls. GDPR’s data minimization principle expects that systems access only what’s necessary for their purpose. Making agent permissions auditable and reviewable satisfies both security teams and compliance requirements.

Consider a practical contact center example. An outbound collections agent operates with permissions to view customer contact information, account balances, and payment history. It cannot modify credit limits, close accounts, or access unrelated customer records. Every action it takes is logged against its unique identity within an [AI customer service automation platform](https://www.nice.com/), creating human readable audit trails for compliance and forensic purposes.

### Data and context boundaries

Agentic AI derives its power from synthesizing information across data sources. A [customer service interaction](https://www.nice.com/glossary/what-is-call-center-call-recording) might require context from CRM, billing, interaction history, [product knowledge bases](https://www.nice.com/products/knowledge-management), and policy documents. This integration creates governance challenges: more data access means more potential for privacy violations, more risk of data combination that reveals information the agent shouldn’t infer, and more complexity in controlling what agents do with what they know.

Classification by sensitivity provides the foundation. Organizations should categorize data as PII, PCI, health information, behavioral data, intellectual property, and other relevant classifications. Each classification carries different handling requirements, and agents should only access classifications appropriate to their function.

Purpose limitation constrains how agents use data. An agent designed for call summarization shouldn’t use those transcripts to build marketing propensity models without explicit consent and governance approval. The agent’s access should be bounded by its intended purpose, with technical guardrails preventing secondary uses.

Practical implementation includes policy-based controls that redact or mask sensitive fields in context windows. A service agent can read the last three customer interactions and current account balance but sees only tokenized credit card data. A journey analytics agent can analyze patterns across aggregated, anonymized data but cannot access identifiable recordings.

Architectural tools make these boundaries enforceable. Secure data gateways can intercept agent requests and apply access policies. Attribute-based access control evaluates each request against the agent’s identity, the data’s classification, and the current context. On-the-fly redaction in transcription and summarization pipelines removes sensitive data before agents see it.

For organizations handling sensitive data across customer interactions, these boundaries are essential. The compliance burden increases significantly if agents can access data without purpose limitation or if sensitive information flows through agentic systems without appropriate protections.

### Monitoring, explainability, and intervention

For agentic systems, governance must operate at runtime. The question isn’t just whether an agent was approved to deploy—it’s whether the agent is currently behaving within its policy envelope. This requires capabilities that traditional AI governance never needed.

Decision-chain logging captures not just API calls but the reasoning that connected them. When an agent sets a goal, plans steps, calls tools, and evaluates results, each stage should be logged in a way that auditors can reconstruct later. This addresses one of the hardest problems in agentic governance: understanding why an agent took a particular action, not just that it did.

Behavioral baselining establishes normal patterns for each agent. An agent that typically processes 200 transactions per hour but suddenly attempts 2,000 should trigger alerts. Unusual tool usage sequences, unexpected data access patterns, or actions outside normal operating hours all warrant investigation. Anomaly detection systems should monitor for emergent behaviors that might indicate the agent is operating outside intended parameters.

Human-readable summaries translate agent behavior into language that supervisors, auditors, and regulators can understand. A compliance officer shouldn’t need to parse raw API logs to understand what happened. Dashboards should show when an AI disputes-resolution agent offered credits above threshold, triggered escalations, or deviated from negotiation guidelines.

Intervention tools provide the ability to override agent decisions when necessary. Soft stops throttle agent actions or require human confirmation for certain steps—slowing the agent down without halting it entirely. Hard stops disable an agent immediately or revoke its credentials when something has gone wrong. Policy auto-adjustment can lower agent autonomy automatically during incidents, overnight, or when monitoring signals indicate elevated risk.

Real-time alerts are essential for effective human oversight. When an agent repeatedly accesses high-risk data objects outside normal patterns, human operators should know immediately—not during a quarterly review. The ability to intervene in real time is what distinguishes effective agentic governance from documentation exercises, especially when coupled with [AI quality management for contact centers](https://www.nice.com/products/quality-management) that surfaces risky interactions automatically.

These monitoring capabilities should integrate with broader operational oversight. When NiCE platforms show agent behaviors alongside human agent performance, supervisors can maintain consistent oversight across both. The goal is unified visibility into customer experience delivery, whether the work is done by humans or AI agents.

## Aligning agentic AI governance with global regulations (EU AI Act and beyond)

The regulatory landscape for AI is evolving rapidly. In 2024 and beyond, regulations increasingly assume that AI systems require documented risk management, effective human oversight, transparency and explainability, and data protection by design. Agentic AI makes compliance both more challenging and more important.

The EU AI Act specifically classifies AI systems by risk level. High risk AI systems include those used in credit decisions, employment eligibility, access to essential services, and law enforcement. Many agentic AI use cases—credit decision assistance, eligibility assessments, customer service in regulated industries—may fall into these categories. Organizations deploying agentic AI in the EU must understand where their agents sit in this classification and what obligations follow.

A tension exists between autonomy and oversight in the regulatory framework. The EU AI Act emphasizes meaningful human control, but the business case for agentic AI often centers on end-to-end automation. Resolving this tension requires practical patterns. “Human-on-the-loop” approaches work for medium-risk scenarios: humans monitor agent behavior and can intervene but don’t approve each action. “Human-in-the-loop” patterns apply to high-risk actions: agent decisions about loan approvals, debt restructuring, or high-value refunds require explicit human approval before execution.

Concrete alignment steps help organizations navigate regulatory compliance:

- Map each AI agent and use case to its likely regulatory risk class, considering customer harm potential, regulatory sector, and operational criticality

- Maintain documentation of intended purpose, data flows, controls, and oversight mechanisms for each agent

- Adopt emerging standards like ISO/IEC 42001 for AI management systems to structure policies and audits

- Ensure audit trails are sufficiently detailed to demonstrate compliance to supervisory authorities


Consider a collections agent operating in the EU. Debt restructuring offers above a defined threshold require human review before presentation to the customer. The agent can draft proposals and check policy limits autonomously, but a human authorizes the final offer. Logs capture the agent’s reasoning, the human’s decision, and the customer’s response—providing the evidence regulators expect.

Strong governance doesn’t slow enterprises down in regulated sectors. Organizations that can demonstrate control move faster because they don’t face regulatory pushback, customer distrust, or board concerns about uncontrolled AI. Responsible AI isn’t about avoiding automation—it’s about automating responsibly.

## A practical, risk-based playbook for deploying agentic AI in the enterprise

Moving from agentic AI experiments to scaled deployment requires a structured approach. The following playbook outlines four stages that help large organizations adopt autonomous agents responsibly, balancing innovation with appropriate controls.

### Step 1: Assess organizational readiness and risk posture

Before deploying agentic AI at scale, organizations need a clear picture of where they stand. This begins with an inventory of current and planned AI agents—including shadow AI where teams may have connected tools informally without central oversight. The inventory should map agents to business processes, customer touchpoints, and systems accessed.

Existing governance should be evaluated against the needs of agentic systems. Many organizations have policies and committees designed for predictive models or generative AI pilots. A gap analysis will reveal what’s missing: identity management for non-human actors, continuous monitoring capabilities, data access controls appropriate for autonomous agents, intervention mechanisms for real-time correction.

Cross functional involvement is essential. Operations understands where agents can deliver value. IT and security teams manage access and monitor for threats. Legal and compliance interpret regulatory requirements. Data teams control information flows. CX leadership defines customer experience standards. An AI governance council or center of excellence that brings these perspectives together prevents siloed decisions that create risk.

Classification by risk dimensions helps prioritize. Consider customer harm potential—financial loss, emotional distress, discrimination. Evaluate regulatory impact—credit, employment, healthcare, public sector touchpoints. Assess operational criticality—business continuity, fraud exposure, reputational damage. Use cases vary dramatically in their risk profiles, and governance intensity should match.

The output of this assessment should be a concise readiness report that identifies which agent use cases can proceed with minimal governance changes and which require significant uplift before deployment.

https://www.nice.com/_next/image?url=https%3A%2F%2Fresources.nice.com%2Fwp-content%2Fuploads%2F2026%2F04%2Fprofessional-team-collaborating.jpg&w=3840&q=80

### Step 2: Design guardrails tailored to each use case

Guardrails must be contextual. The controls appropriate for a call summarization agent differ substantially from those for a payment adjustment agent. A one-size-fits-all approach either over-constrains low-risk agents or under-protects high-risk ones.

A three-tier guardrail model provides structure:

Tier 1 covers low-risk, informational agents like knowledge retrieval and summarization tools. These agents operate with broad autonomy but restricted data access and read-only permissions. They can plan tasks and execute them independently because their actions don’t modify systems or affect customer outcomes directly.

Tier 2 addresses medium-risk process assistants that draft responses, propose schedule changes, or recommend actions. Humans approve final actions before execution. The agent does preparatory work; the human makes the consequential decision.

Tier 3 applies to high-risk agents that change financial status, access sensitive health or financial data, or make eligibility recommendations. These operate under strict human-in-the-loop requirements with enhanced logging and narrow autonomy bounds.

Each agent should have explicit “rules of engagement” that specify what it may do autonomously, what always requires human approval, and what it must never do. Hard constraints—never delete records, never change customer identifiers, never access data outside the defined scope—provide boundaries that can’t be crossed regardless of the agent’s goals.

A bank’s contact center might deploy agents across all three tiers. Tier 1: summarization of calls for quality assurance, operating independently with access only to transcripts. Tier 2: drafting hardship letters that customers review and approve before sending. Tier 3: modifying repayment plans, requiring supervisor sign-off before any changes take effect.

### Step 3: Pilot in sandboxes and controlled production slices

Sandbox environments allow organizations to test agentic systems without real-world consequences. Using synthetic or anonymized data, sandboxes should mirror production complexity—multiple tools, real routing logic, actual integration patterns—so that behaviors observed in testing predict behaviors in production.

Piloting in production should start with limited scope: low-risk but operationally relevant tasks, specific customer segments or channels, defined time windows. Clear rollback plans ensure that if problems emerge, the organization can revert quickly without customer impact.

Measurement during pilots should cover multiple dimensions. Error rates and near-miss incidents reveal where agents struggle. Human override frequency and the reasons behind overrides show where autonomy bounds may be inappropriate. Customer effort, resolution time, and satisfaction metrics indicate whether the agentic approach actually improves experience. Compliance signals—adherence to scripts, proper disclosures, recording policy compliance—validate regulatory readiness.

Transparent communication matters both internally and externally. Human workers need to understand how pilots work and how to intervene when necessary. Customers interacting with AI agents should know they’re doing so, consistent with regulatory expectations and trust-building principles. Hiding AI involvement from either group undermines the trust that responsible agentic AI adoption requires.

### Step 4: Scale with continuous monitoring and governance evolution

Once pilots demonstrate stability, organizations can expand scope gradually. More queues, additional languages, broader geographic coverage—each expansion should be incremental, with monitoring confirming that performance and compliance remain acceptable at larger scale. Autonomy can increase where evidence supports it, with agents taking on more complex tasks as they prove reliable.

Ongoing performance and risk dashboards should track AI agent behavior continuously. Monthly or quarterly governance reviews by the AI governance council assess whether policies remain appropriate, whether new risks have emerged, and whether controls need adjustment. The regulatory landscape continues to evolve; governance frameworks must evolve with it.

Feedback loops from multiple sources keep governance grounded in operational reality. Frontline employees report issues or unexpected behaviors they observe. Customers provide signals through survey feedback and complaints. These inputs should flow back into governance decisions, informing policy updates and control refinements.

Governance for agentic AI is iterative. Frameworks should be treated as living systems refined with operational data, not one-time compliance projects completed and filed away. The goal is continuous improvement—governance that becomes more effective over time as the organization learns how its autonomous agents behave in real conditions.

This connects to a broader CX vision: autonomous agents orchestrating customer journeys while human workers focus on complex, empathetic work that requires human judgment. Governance keeps trust and regulatory compliance intact while enabling that future.

## The future of agentic AI governance in customer experience and beyond

Agentic AI represents a fundamental shift from AI that answers to AI that acts. Governance must evolve accordingly, becoming identity-aware, data-centric, lifecycle-driven, and risk-based. The frameworks that worked for traditional AI systems—static approvals, periodic reviews, human-in-the-loop at every step—cannot keep pace with autonomous systems that operate across multiple systems, combine data sources, and make decisions in real time for global CX leaders like [NiCE](https://www.nice.com/company/about-us).

In customer experience specifically, the implications are profound. Agents will increasingly orchestrate omnichannel journeys, adjusting routing, workforce deployment, and personalization at scale. They’ll handle complex tasks that previously required multiple human touchpoints, resolving issues faster and with less customer effort. Whether these capabilities increase trust and satisfaction—or create new forms of risk and ethical dilemmas—depends largely on governance.

The next three to five years will likely see convergence across disciplines that have historically operated separately. AI governance, cybersecurity, and operational risk management will merge into integrated frameworks that address autonomous systems holistically. Standardization around frameworks like ISO/IEC 42001 and sector-specific AI guidelines will provide common language and expectations. Governance itself may become more automated, with governance agents monitoring operational agents—meta-oversight that scales with AI deployment and showcases why [NiCE’s AI leadership stories](https://www.nice.com/resources/why-nice-the-room-where-it-happened-video-series) focus on both innovation and control.

Organizations that treat agentic AI governance as core infrastructure position themselves for competitive advantage. They can innovate faster because they can demonstrate control to regulators, customers, and boards. They can adopt new capabilities confidently because they have the frameworks to manage associated risks. They deliver customer experiences that are not just efficient but trustworthy—experiences where AI operates with transparency and accountability.

NiCE remains committed to embedding these governance principles into its platforms. CXone provide the foundation for enterprises to deploy autonomous agents with appropriate identity, data, and lifecycle controls. The goal isn’t to constrain AI but to enable it responsibly—delivering faster, calmer, and more human customer experiences while maintaining the trust that enterprise relationships require.

### Frequently Asked Questions (FAQs)

What is an agentic AI governance framework?

An agentic AI governance framework is a set of policies, controls, and operational mechanisms designed to oversee autonomous AI systems that can plan, decide, and act across enterprise workflows. Unlike traditional AI governance, which focuses on model outputs, agentic AI governance manages end-to-end decision chains, real-time actions, data access, and accountability to ensure autonomous agents operate safely, transparently, and within regulatory and ethical boundaries.

Why do traditional AI governance models fall short for agentic AI?

Traditional AI governance assumes humans approve or execute each meaningful action, with periodic reviews of model performance. Agentic AI systems act autonomously across multiple systems, persist across sessions, and adapt in real time. This requires continuous monitoring, runtime policy enforcement, identity-based controls, and real-time intervention capabilities rather than static approvals and quarterly reviews.

What are the core principles of effective agentic AI governance?

Effective agentic AI governance is built on several foundational principles:

- **Identity-first governance**, where each AI agent has a unique, auditable identity
- **Data-centric protection**, restricting what data each agent can access and how it can be used
- **Risk-based autonomy**, scaling freedom based on task criticality and regulatory exposure
- **Lifecycle governance**, managing agents from design through retirement
- **Continuous oversight**, with real-time monitoring, explainability, and intervention mechanisms

Together, these principles allow enterprises to balance autonomy with control.

How does agentic AI governance support regulatory compliance such as the EU AI Act?

Agentic AI governance aligns with emerging regulations by enforcing purpose limitation, meaningful human oversight, transparency, and auditability. High-risk use cases require human-in-the-loop approval, detailed decision logging, and explainable outcomes. Runtime monitoring and clear audit trails enable organizations to demonstrate compliance to regulators while still benefiting from autonomous execution in lower-risk scenarios.

How should enterprises start implementing agentic AI governance in practice?

Enterprises should begin with a risk-based approach:

- Inventory existing and planned AI agents and map them to business processes
- Classify use cases by customer impact, regulatory exposure, and operational risk
- Define tiered guardrails that specify what agents can do autonomously and when human approval is required
- Pilot in sandbox and limited production environments with clear rollback plans
- Scale gradually with continuous monitoring, governance reviews, and feedback loops

This approach enables safe innovation without slowing down AI-driven transformation.

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

<research_source type="scraped_from_research" phase="exploration" file="orchestrating-ambient-agents-with-temporal-temporal.md">
<details>
<summary>Orchestrating ambient agents with Temporal</summary>

Phase: [EXPLORATION]

**Source URL:** <https://temporal.io/blog/orchestrating-ambient-agents-with-temporal>

# Orchestrating ambient agents with Temporal

AUTHORS

Kevin Martin

DATE

Sep 18, 2025

CATEGORY

[How-To](https://temporal.io/blog/categories/how-to)

DURATION

14 MIN

- AI/ML
- Code Samples
- Finance
- Python
- Temporal Primitives

TABLE OF CONTENTS

1. [Temporal Schedules: Enabling proactive agents](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal#temporal-schedules-enabling-proactive-agents)
2. [Signals & Queries: The language of inter-agent communication](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal#signals--queries-the-language-of-inter-agent-communication)
3. [Observability with Temporal UI: Watching agents in action](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal#observability-with-temporal-ui-watching-agents-in-action)
4. [Orchestrating multiple agents with Temporal Workflows](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal#orchestrating-multiple-agents-with-temporal-workflows)
5. [Temporal primitives as MCP tools: Durable actions for AI Agents](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal#temporal-primitives-as-mcp-tools-durable-actions-for-ai-agents)
6. [Real-time feedback routing](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal#real-time-feedback-routing)
7. [Conclusion](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal#conclusion)

Orchestrating Ambient Agents with Temporal \| AI + Crypto Trading Demo - YouTube

Tap to unmute

[Orchestrating Ambient Agents with Temporal \| AI + Crypto Trading Demo](https://www.youtube.com/watch?v=4mSbMEguGJs) [Temporal](https://www.youtube.com/channel/UCGovZyy8OfFPNlNV0i1fI1g)

Temporal14.7K subscribers

[Watch on](https://www.youtube.com/watch?v=4mSbMEguGJs)

Building a proactive, 24×7 [crypto trading platform](https://github.com/Aslan11/crypto-trading-agents) with multiple AI agents has been both challenging and enlightening. Using **Temporal** for orchestration and the **Model Context Protocol (MCP)** for tool interfaces, I designed a system around three core agents: a **broker agent** (the user-facing entry point that manages intents and orchestrates Workflows), an **execution agent** (responsible for making and executing trading decisions), and a **judge agent** (that continuously evaluates performance and updates the execution agent’s system prompt and strategy). Surrounding these are supporting Workflows for market data, order placement, and ledgering.

The inspiration came this past June at the **AI Engineers World’s Fair in San Francisco**, where I first encountered the concepts of _ambient intelligence_ and _proactive AI_ at a breakout hosted by AWS and Anthropic. The idea of agents that run continuously — quietly nudging the system forward without waiting for explicit prompts — sparked this project. Then in July, at IBM’s **AI Agent Meetup**, Claire Longo’s talk introduced the idea of an **LLM as judge**. It was such a compelling concept that I quickly extended my architecture with a judge agent, turning the system into one that is not only proactive but also self-refining over time.

Along the way, I discovered several key advantages of using Temporal in such an AI-driven system. In this post, I’ll dive into what I learned about five crucial features of Temporal and how they benefited my multi-agent architecture: **Schedules**, **Signals & Queries**, **Temporal’s UI**, **workflow orchestration**, and **Temporal primitives as MCP tools**.

https://images.ctfassets.net/0uuz8ydxyd9p/7ytPvbWiNfUyO1Mew6im1R/e924f13a5673a5fb85a3e8b6af3ae1bd/Screenshot_2025-09-17_at_12.01.37%C3%A2__PM.png

## Temporal Schedules: Enabling proactive agents [\#](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal#temporal-schedules-enabling-proactive-agents)

One of the first challenges was ensuring the trading agents act **proactively** at regular intervals without a user having to take action. Crypto markets never sleep, so my trading agent needed to wake up periodically, analyze data, and make decisions continuously. Temporal’s **Schedules** feature turned out to be perfect for this. Instead of writing custom cron jobs or sleep loops, I defined a Temporal Schedule that triggers a “nudge” Workflow every few seconds to prompt the execution agent to analyze the portfolio status and market data. This made the agent truly ambient — always running on a schedule managed durably by Temporal’s Server, not by ad-hoc timers in my code. This led to a powerful realization for me: LLM providers, like OpenAI & Anthropic, will provide the “brain” for ambient agents, but Temporal will provide the ever-beating heart that keeps the system running durably.

For example, I created a schedule called `"ensemble-nudge"` to run a Workflow every 25 seconds. In code it looks like this:

```
schedule = Schedule(
    action=ScheduleActionStartWorkflow(
        workflow=EnsembleNudgeWorkflow.run,
        id="ensemble-nudge-wf",
        task_queue="mcp-tools",
    ),
    spec=ScheduleSpec(intervals=[ScheduleIntervalSpec(every=timedelta(seconds=25))]),
)
await client.create_schedule("ensemble-nudge", schedule)
```

With a few lines, Temporal ensures a Workflow (`EnsembleNudgeWorkflow`) is started on that interval. This **built-in scheduling** freed me from managing threads or external cron services. If the Worker or process restarts, the schedule is still tracked by Temporal and will fire the next Workflow on time. Temporal Schedules thus made it easy to implement an **always-on agent** that reacts regularly **without** human intervention.

## Signals & Queries: The language of inter-agent communication [\#](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal#signals--queries-the-language-of-inter-agent-communication)

In a multi-agent system, the agents need to talk to each other. Temporal’s **Signals** and **Queries** became the backbone of communication between my agents’ Workflows. Each AI agent (broker, execution, judge) is implemented as a long-running Workflow that maintains state and waits for Signals. This is similar to an actor model: agents are always alive (durably so, thanks to Temporal) and react to incoming Signals/Events, and they expose Queries to fetch their internal state. I found this far cleaner and more reliable than building custom messaging or polling mechanisms.

```
@workflow.signal
def update_system_prompt(self, prompt: str) -> None:
    """Update the system prompt for the execution agent."""
    self.system_prompt = prompt
    workflow.logger.info(f"System prompt updated (length: {len(prompt)} chars)")

@workflow.query
def get_system_prompt(self) -> str:
    """Get the current system prompt."""
    return self.system_prompt
```

With these in place, the LLM-as-judge agent can dynamically tune the execution agent’s behavior. After each performance evaluation, the judge uses Temporal’s client API to get a handle to the execution agent’s Workflow (by ID) and send it a Signal with a new prompt.

For example, the judge agent code calls:

```
await handle.signal("update_system_prompt", improved_prompt)
```

This is done whenever it determines a prompt update is needed. This Signal delivery is **asynchronous and reliable** — Temporal ensures the Signal is delivered to the Workflow instance, even if the target Workflow is running on a different Worker or the process restarts. In my case, I could see the `ExecutionAgentWorkflow` received the prompt update and logged the change (`"System prompt updated..."` appears in the Workflow logs).

I also used Signals for other interactions: a **“nudge” Signal** triggers the execution agent Workflow to begin its analysis, and logging Signals are used to record decisions and actions in each agent’s log Workflow. Queries complement this by allowing an agent to **pull data** from another agent. For example, the judge agent queries the execution agent for its current system prompt, and the broker agent queries the ledger Workflow for recent portfolio status & transaction history. Signals and Queries gave me a simple, strongly ordered way for inter-agent communication without needing an external message bus. This decoupling via Temporal constructs kept each agent Workflow isolated yet cooperative.

## Observability with Temporal UI: Watching agents in action [\#](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal#observability-with-temporal-ui-watching-agents-in-action)

When orchestrating multiple intelligent agents, understanding _what_ happened _when_ is crucial. Temporal’s Web UI became an invaluable tool for observing the system’s behavior in real time. Every agent and tool in my system runs as a Temporal Workflow, which means I have a timeline of each Workflow’s execution and Events accessible in the UI. This proved extremely helpful for debugging and trustworthiness: I could literally watch the agents’ interactions step by step.

https://images.ctfassets.net/0uuz8ydxyd9p/4NjIM6lnBAnpF1p3SADxam/85e10212d252087cada987344f198bfb/Screenshot_2025-09-17_at_12.02.56%C3%A2__PM.png
For example, whenever the judge agent updated the execution agent’s prompt via a Signal, I could open the `ExecutionAgentWorkflow` in Temporal’s UI and see the **Signal Event** recorded at that timestamp. Right next to it, I’d see the log entry confirming the prompt change. Similarly, the schedule-triggered Workflows (the “nudges”) showed up as runs of the `EnsembleNudgeWorkflow` every 25 seconds, visible in the history. Having this chronological view made it easy to answer questions like: _Did the execution agent receive the nudge on time? Did the judge agent run its evaluation cycle after 10 minutes as expected?_ I could trace all these events in one place.

The Temporal UI also gave me confidence in the system’s **auditability**. Each Workflow’s history is stored, so I have an exact record of every decision and action the agents took (with timestamps and inputs) — a critical requirement in financial systems. Instead of logging to scattered files, I relied on Temporal’s histories (and some custom Workflow logs) to inspect what the agents were doing. This observability was especially useful when the agents’ behavior became complex; being able to visualize their coordination in the UI helped me fine-tune the Schedules and Signal handling. In short, Temporal’s UI turned the black-box nature of AI agents into a glass box, where I could see and debug the internals of the multi-agent orchestration easily.

## Orchestrating multiple agents with Temporal Workflows [\#](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal#orchestrating-multiple-agents-with-temporal-workflows)

Coordinating several agents and services — ticker feeds, a trading agent, a performance judge, and more — can get complicated fast. Temporal simplified this by acting as the **central orchestrator** for all agent workflows. In my design, each major component is a separate Workflow (or set of Workflows) and Temporal manages their lifecycles and interactions. This yielded a system where agents can run truly 24×7 with resilience and clarity in how they interact.

As I mentioned above, the architecture consists of three primary agents: a **broker agent** (user interface Workflow), an **execution agent** (trading decisions Workflow), and a **judge agent** (LLM-as-judge evaluator Workflow), plus supporting Workflows for market data streaming, order execution, and an execution ledger. Temporal allowed these to be broken into **modular Workflows** that each handle their domain. The broker starts a market data subscription Workflow which streams data from Coinbase. The execution agent Workflow listens for “nudge” Signals (from the Schedule) and uses MCP tools as Workflows/Queries/Signals to fetch data and place orders. The judge Workflow wakes up periodically (or on demand) to analyze performance and then signals the execution agent with adjustments. All of this is orchestrated by Temporal in a single connected system.

The benefit was huge: **continuous orchestration without downtime**, and guaranteed state tracking. Temporal’s fault tolerance means if one agent Workflow or Activity fails, it can be retried or continued without bringing down the whole system. This was critical because crypto trading must not stop; Temporal gave me the building blocks to ensure the agents coordinate reliably _around the clock_. Additionally, because Temporal Workflows are **deterministic and replayable**, I gained deterministic audit trails of the agents’ decision processes — an important factor if I ever need to explain a trade or comply with regulations.

Orchestrating with Temporal also simplified the design: rather than writing complex multi-threaded code or managing distributed state, I let Temporal Workflows handle concurrency and state isolation. Each agent had its own Workflow “instance” (for example, an `ExecutionAgentWorkflow` with a well-known ID) and could maintain internal variables (like the current prompt or recent actions) in memory safely. Temporal’s single-responsibility Workflows made the multi-agent system **easier to extend** too. I can add another agent or tool by just creating a new Workflow and perhaps scheduling or signaling it, without touching the core loop of other agents. This modular orchestration on Temporal proved to be a robust way to manage a complex ensemble of AI components.

## Temporal primitives as MCP tools: Durable actions for AI Agents [\#](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal#temporal-primitives-as-mcp-tools-durable-actions-for-ai-agents)

One of the most powerful patterns I implemented was using Temporal primitives (Workflows, Signals, Queries) as the **“tools”** that the AI agents call to interact with the world. In the Model Context Protocol (MCP) framework I used, agents invoke tools like `get_historical_ticks`, `place_order`, `get_portfolio_status`, etc., to gather data or execute trades. Instead of these tools being simple functions or external APIs, I made each one a **Temporal primitive** under the hood. This marriage of MCP tools with Temporal brought significant reliability, observability, and scalability benefits.

For example, when the execution agent wants to execute a trade, it calls a `place_mock_order` tool. That tool is actually implemented as a Temporal Workflow (`PlaceMockOrder`) which wraps an Activity to simulate the trade fill. Here’s a glimpse of that Workflow code:

```
@workflow.defn
class PlaceMockOrder:
    @workflow.run
    async def run(self, intent: OrderIntent) -> Dict:
        logger.info("Placing mock order: %s", intent)
        result: Dict = await workflow.execute_activity(
            mock_fill,
            intent,
            schedule_to_close_timeout=timedelta(seconds=5),
            retry_policy=RetryPolicy(maximum_attempts=1),
        )
        return result
```

Every time the agent “places an order,” it’s invoking this Workflow. The use of Temporal here means the action is durable, and if the underlying Activity fails (say the exchange API is down, in a real scenario), Temporal can retry or timeout gracefully. In fact, **every `@mcp.tool()` in the system is backed by a deterministic Temporal Workflow**, which gives us _automatic retries_ and _full replay for audit/compliance_ out of the box. The AI agents’ tools became **durable operations**. I didn’t have to worry about inconsistent state if an agent’s tool call crashed midway — Temporal ensures either the whole Workflow completes or it doesn’t happen at all, and we can always inspect what happened from the history.

Using Temporal for tool implementations also kept the agent’s reasoning loop deterministic. The agent (an LLM) would decide on an action, call a tool, and receive the result — all that heavy lifting (fetching market data, logging a trade, etc.) was done inside a Temporal Workflow which is isolated from the agent’s prompt and handled by a Temporal Worker, keeping the MCP server’s load low. This maintains a clear separation: the MCP server shows what can be done, the LLM decides what to do, and Temporal Workflows handle how it’s done reliably. The result is an AI trading system that marries the flexibility of LLM-driven decision-making with the robustness of Temporal’s Workflow execution.

## Real-time feedback routing [\#](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal#real-time-feedback-routing)

In this multi-agent crypto trading system, the **broker agent** acts as a coordinator that relays human feedback to the appropriate specialist agent (either the execution or judge agent) without needing to interrupt their operation. The broker leverages an MCP tool called `send_user_feedback` for this purpose. When the broker receives a user’s feedback, it invokes this tool with a target parameter indicating **which agent** should get the message. Internally, the tool uses the target to fetch the corresponding Temporal Workflow handle and sends an asynchronous **Signal** to that agent’s Workflow. For example, if `target_agent="execution"`, it grabs the execution agent’s Workflow (`"execution-agent"`) and signals its `add_user_feedback` method with the feedback payload; if targeting the judge, it does the analogous call on the judge agent’s Workflow:

```
# Broker routes feedback by signaling the target agent's workflow
if target_agent.lower() == "execution":
    handle = client.get_workflow_handle("execution-agent")
    await handle.signal("add_user_feedback", feedback_data)
    # ... feedback sent to execution agent ...
elif target_agent.lower() == "judge":
    handle = client.get_workflow_handle("judge-agent")
    await handle.signal("add_user_feedback", feedback_data)
    # ... feedback sent to judge agent ...
```

This simple routing logic ensures the right agent receives the user’s note in real time. Because the broker uses Temporal Signals, the feedback delivery is fire-and-forget — it does not interrupt the agent’s ongoing Workflow. The broker agent merely acts as a messenger, letting the specialized agents handle the feedback when they are ready.

On the receiving end, both the execution and judge agents’ Workflows define an `add_user_feedback` Signal handler to record these incoming messages. In the `ExecutionAgentWorkflow`, for instance, `add_user_feedback` simply timestamps the feedback, assigns a unique ID, marks it unprocessed, and appends it to an internal list of feedback messages:

```
@workflow.signal
def add_user_feedback(self, feedback_data: Dict[str, Any]) -> None:
    """Add user feedback to be incorporated into the agent's conversation."""
    feedback_entry = {
        **self._get_timestamp(),
        "feedback_id": f"feedback_{len(self.user_feedback) + 1}",
        "message": feedback_data.get("message", ""),
        "source": feedback_data.get("source", "user"),
        "processed": False
    }
    self.user_feedback.append(feedback_entry)
    workflow.logger.info(f"User feedback received: {feedback_data.get('message', '')[:100]}...")
```

The `JudgeAgentWorkflow` implements the same pattern for its own feedback list ( [GitHub](https://github.com/Aslan11/crypto-trading-agents/blob/5e81edb0a076310c6040800652338748f499ad64/agents/workflows/judge_agent_workflow.py#L294-L303)). Storing feedback in a queue with a `processed=False` flag allows the agent to **defer processing** until a convenient moment. The running agent (e.g., the execution agent’s loop) can periodically query its Workflow for any pending feedback (via a `get_pending_feedback` query) and incorporate those messages into its context. For example, the execution agent’s client checks for new feedback and injects it into the conversation as a special user message (e.g., [prefixing](https://github.com/Aslan11/crypto-trading-agents/blob/5e81edb0a076310c6040800652338748f499ad64/agents/utils.py#L169-L177) with “\[USER FEEDBACK\]”), then marks it as processed. This design lets a human trader “nudge” or guide the agents on the fly — the feedback is delivered instantly and queued, to be digested by the agent without halting its autonomous flow. In short, the Broker’s feedback relay and the agents’ Signal handlers work together to enable real-time human guidance of the trading agents without any interruption to their Workflows.

## Conclusion [\#](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal#conclusion)

Building an always-on, multi-agent trading system with an AI and a human-in-the-loop taught me just how much a platform like Temporal can simplify complex automation. Here are the key takeaways from this project:

- **Proactive orchestration with Schedules** — Agents can operate continuously without custom schedulers or external cron jobs.
- **Real-time communication with Signals and Queries** — Agents can coordinate, share state, and accept human feedback seamlessly without pausing their loops.
- **Visibility with the Temporal UI** — Every agent action, Signal, and update is captured in Workflow history, making the system transparent, debuggable, and auditable.
- **Reliability from Temporal’s core guarantees** — Durable Execution, retries, and durable state tracking ensure the system runs 24×7 without drift or data loss.
- **Durability by implementing tools as Workflows** — Every agent action is executed as a Temporal Workflow, giving audit trails and fault tolerance “for free.”
- **Extendability** — Adding a new agent or tool is as simple as creating another Workflow. The modular architecture makes it straightforward to experiment, iterate, and grow the system.
- **Team-friendly design** — Temporal enforces a clean separation of concerns: one engineer can focus on a single Workflow, develop and test it locally, and deploy it independently. This makes collaboration easy, even on a multi-agent system.

In the end, Temporal handled the timing, communication, reliability, and observability, freeing me to focus on the higher-level logic of the agents. That’s what made it possible to turn a set of experimental AI agents into a robust, proactive trading system — a pattern I expect to reuse in future projects where complex agents need dependable orchestration.

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