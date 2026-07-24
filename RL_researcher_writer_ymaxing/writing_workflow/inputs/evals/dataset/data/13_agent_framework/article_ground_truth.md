# Lesson 13: Agen    Frameworks Overview & Comparison

In the previous lesson, we introduced the two capstone projects we will build: an adaptable research agent and a reliable writing agent.

That leaves us with a critical decision: which framework should we use to build these projects? The ecosystem is new, evolving quickly, and crowded with options. Choosing for the wrong reasons can lock you into brittle abstractions; choosing too late can stall a project. This lesson is a guide to making that decision. We will compare the most popular libraries: LangGraph, OpenAI Agents SDK, AgentKit, CrewAI, PydanticAI, AutoGen, Claude Agent SDK, and FastMCP by focusing on their philosophies, abstractions, and trade-offs, not just their APIs.

We will anchor this comparison in our capstone architecture. You will learn how we evaluated the options, why we changed direction mid-build, and how to reason about framework choice under uncertainty. As you read, keep two concepts in mind: LangGraph’s interrupts and checkpoints, which enable auditable, resumable workflows[[2]](<https://docs.langchain.com/oss/python/langgraph/persistence>), and the Model Context Protocol (MCP) as your interoperability layer[[10]](<https://gofastmcp.com/>) (think “USB-C for AI,” so tools you build today can plug into multiple runtimes tomorrow).

We will show how this plays out in practice: our research agent ships as a FastMCP server, while our writing system uses a LangGraph workflow that calls MCP tools.

![Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down)

Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

## Framework Choice Under Uncertainty and Why Some Selection Strategies Fail in Production

The AI agent ecosystem is new and evolving quickly, and no universal framework will satisfy every use case. This landscape is often confusing because different types of tools are frequently lumped together. To make an informed choice, you must first understand the distinct roles these tools play.

A runtime (e.g., LangGraph, CrewAI, PydanticAI, OpenAI Agents SDK, AgentKit, AutoGen) orchestrates an agent’s behavior, managing its state and control flow. A protocol (e.g., Model Context Protocol, MCP) standardizes how agents access tools and resources, ensuring that a tool built for one runtime can be used by another. Finally, a tooling framework (e.g., FastMCP) helps you implement that protocol, making it easier to build and deploy these interoperable tools.

![Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Frameworks.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down)

Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

These components solve different production problems. A runtime like LangGraph provides reliability features like checkpoints and interrupts for durable, auditable execution[[2]](<https://docs.langchain.com/oss/python/langgraph/persistence>). A protocol like MCP provides tool portability, freeing you from vendor lock-in[[10]](<https://gofastmcp.com/>). A tooling framework like FastMCP provides the servers, clients, and transports needed to make that protocol production-ready[[10]](<https://gofastmcp.com/>).

A common mistake is choosing a framework based on hype or a simple “Hello, World” example without considering the real demands of a production system. This often leads to one of two traps: either you pick a framework that is too simple and lacks the reliability primitives for your use case, or you choose one that is too complex and imposes unnecessary overhead.

We learned this firsthand. We initially planned to build our research agent with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was a wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes Instead of Brands

To avoid these traps, you need a way to evaluate frameworks based on principles. Here are four decision axes that can help you analyze any new library and determine if it fits your project’s needs.

![Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down)

Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

1. **Control-Flow Explicitness vs. LLM-Driven Autonomy:** Frameworks exist on a spectrum of control. At one end, graph-based systems like LangGraph give you explicit control over every state transition. This is ideal for deterministic, auditable workflows where you need to know precisely why the system made a particular decision. At the other end, agent loops with minimal primitives, like the OpenAI Agents SDK, favor LLM-driven autonomy. This is better for exploratory tasks where the path to a solution is not known in advance. The question to ask is: Does your application require repeatable, auditable steps, or does it need to navigate an unpredictable environment?

2. **Reliability Primitives: Production systems fail.** A good framework provides tools to handle those failures gracefully. Look for features like checkpointing (saving the agent’s state), time-travel/replay (re-running a process from a saved state), human-in-the-loop (HITL) interrupts (pausing for human approval), and durable execution (surviving restarts). LangGraph emphasizes interrupts and persistence[[2]](<https://docs.langchain.com/oss/python/langgraph/persistence>), while PydanticAI integrates with systems like Temporal and DBOS for durable execution[[7]](<https://ai.pydantic.dev/durable_execution/overview/>).

3. **Abstraction Level and Developer Experience (DX):** Frameworks offer different levels of abstraction. Some, like the OpenAI Agents SDK, provide a minimal set of primitives (Agents, Tools, Guardrails), giving you flexibility at the cost of more boilerplate. Others, like CrewAI, offer opinionated constructs (Crews, Flows) that speed up development but may be less flexible. High-level abstractions are great for building quickly, but the ability to drop to a lower level for fine-grained control is critical when you encounter edge cases.

4. **Tooling Interoperability (MCP):** To avoid rewriting your integrations every time you switch runtimes, treat your tools as standalone components. The Model Context Protocol (MCP) acts like a “USB-C for AI,” providing a standard interface for tools. By building your tools as MCP servers (for example, with FastMCP[[10]](<https://gofastmcp.com/>)), you can plug them into any framework that speaks the protocol, including LangGraph, the OpenAI Agents SDK, or even IDEs like Cursor.

Our capstone projects clearly map to these axes. The research agent requires autonomy and interoperable tools for its exploratory nature, making a lightweight loop with MCP a good fit. The writing agent demands an explicit, auditable workflow with reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks.

- **LangGraph**: Best for stateful, auditable workflows. It uses a graph-based model with built-in support for checkpoints and interrupts[[2]](<https://docs.langchain.com/oss/python/langgraph/persistence>), making it ideal for processes that need to be resumable and traceable[[1]](<https://docs.langchain.com/oss/python/langgraph/workflows-agents>).

![Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down)

Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.

LangGraph has strong, consistent daily download activity, averaging around 400K–500K downloads per day over the past three months.

<aside>
💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers, etc.), **LangGraph** focuses specifically on **structured**, **stateful workflows**. It introduces graph-based execution with checkpoints and resumability, which are features not native to standard LangChain chains.

In short, LangChain is the toolbox, while LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions[[1]](<https://docs.langchain.com/oss/python/langgraph/workflows-agents>).

You will see LangChain code in the writing agent.

</aside>

- **OpenAI Agents SDK**: A lightweight, production-ready framework with a small surface area: Agents, Tools, Guardrails, Handoffs, and Sessions[[3]](<https://openai.github.io/openai-agents-python/>). It is a fast path to production if you prefer minimal abstractions and letting the LLM drive the planning.

![Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down)

Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.

The OpenAI Agents SDK library has recorded 90K–120K daily downloads over the past three months, with a slight upward trend.

- **OpenAI’s AgentKit**: A modular toolkit for building, deploying, and optimizing agents across the OpenAI platform. It unifies visual design (**Agent Builder**), frontend integration (**ChatKit**), and performance optimization (**Evals**) into one workflow. Developers can visually compose multi-agent systems, manage connectors, and embed chat-based experiences directly in their products—all backed by versioning, guardrails, and evaluation tools for safe, reliable deployment.

<aside>
💡
OpenAI AgentKit vs. OpenAI Agents SDK

The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration and fine-grained control. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK: it adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**.

In short, the SDK is the coding foundation, while AgentKit is the integrated platform for design, deployment, and optimization.

</aside>

- **CrewAI**: Designed for multi-agent collaboration. It uses “Crews” for role-based autonomous work[[4]](<https://docs.crewai.com/introduction>) and “Flows” for deterministic orchestration[[4]](<https://docs.crewai.com/introduction>)[[6]](<https://docs.crewai.com/guides/flows/first-flow>), with a strong emphasis on developer experience through its CLI and YAML configurations[[5]](<https://docs.crewai.com/quickstart>).

![Image 6: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down)

Image 6: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.

The CrewAI library has **daily downloads ranging between 40K and 100K**.

- **PydanticAI**: The “FastAPI for agents.” It prioritizes type safety, data validation, and durable execution through integrations with Temporal and DBOS[[7]](<https://ai.pydantic.dev/durable_execution/overview/>). It shines when correctness and structured data are critical.

![Image 7: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down)

Image 7: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.

Daily downloads of Pydantic-AI doubled from ~150k in July to **300- 450k** by October 2025, demonstrating strong growth momentum.

- **AutoGen**: A flexible framework with a layered design. AutoGen Studio provides a GUI for no-code prototyping, making it an excellent exploration lab[[9]](<https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html>). However, Studio is explicitly not for production[[9]](<https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html>); for that, you would use the underlying AgentChat or core libraries[[8]](<https://microsoft.github.io/autogen/stable/>).

![Image 8: pepy.tech, daily downloads for autogen, accessed October 15, 2025.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down)

Image 8: pepy.tech, daily downloads for autogen, accessed October 15, 2025.

AutoGen had about **10k** daily downloads recently.

- **Claude Agent SDK**: A newer entrant from Anthropic, designed to integrate tightly with Claude models. It focuses on providing robust tool use and orchestration capabilities tailored to the strengths of their model family.

- **FastMCP**: Not a runtime, but a framework for building MCP servers and clients[[10]](<https://gofastmcp.com/>). It provides the “USB-C ports” for your tools, ensuring they are portable across different runtimes and stacks[[10]](<https://gofastmcp.com/>). It also includes production-ready features like authentication and cloud deployment[[10]](<https://gofastmcp.com/>).

![Image 9: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down)

Image 9: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.

FastMCP demonstrates explosive growth, with daily downloads surging from ~250k in July to peaks of over **1.2M per day** in October 2025, a 5x increase over three months.

To get a further sense of community energy, you can look at GitHub stars as of September 17, 2025. While stars do not equal quality, they can be a useful proxy for ecosystem maturity and hiring risk.

![Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down)

Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026.

## Framework Deep Dive: LangGraph

LangGraph is designed for building stateful, auditable applications[[1]](<https://docs.langchain.com/oss/python/langgraph/workflows-agents>). Its core philosophy is that you model your logic as a graph, where each node is a function and edges represent the transitions between them[[1]](<https://docs.langchain.com/oss/python/langgraph/workflows-agents>). This structure allows you to create complex, multi-step workflows that can be paused, inspected, and resumed at any point[[2]](<https://docs.langchain.com/oss/python/langgraph/persistence>).

The key production features are interrupts and persistence[[2]](<https://docs.langchain.com/oss/python/langgraph/persistence>). With **interrupts**, you can pause the graph to wait for human approval before proceeding. With **persistence** (or checkpointing), the state of the graph is saved at each step[[2]](<https://docs.langchain.com/oss/python/langgraph/persistence>). This enables not only long-running work but also **time-travel debugging**, where you can replay a workflow from any previous checkpoint to understand how it reached a particular state[[2]](<https://docs.langchain.com/oss/python/langgraph/persistence>).

LangGraph offers two ways to define these graphs: a “graph API” and a “functional API”[[1]](<https://docs.langchain.com/oss/python/langgraph/workflows-agents>). The graph API is more explicit, requiring you to define a `StateGraph` object and then add nodes and edges step-by-step (e.g., `workflow.add_node(...)`, `workflow.add_edge(...)`)[[1]](<https://docs.langchain.com/oss/python/langgraph/workflows-agents>). The functional API is a more recent, concise alternative that uses decorators to define the graph, making the code look more like a standard Python application while still compiling down to the same stateful graph[[1]](<https://docs.langchain.com/oss/python/langgraph/workflows-agents>).

However, this power comes at a cost. Modeling control flow as an explicit graph is more work than simply letting an LLM plan its own steps. The learning curve is steeper, but the payoff is determinism and safety. For simple scripts or one-off flows, LangGraph may be overkill, but for the repeatable and auditable process of our writing agent, it is the right tool.

## Framework Deep Dive: OpenAI Agents SDK

In contrast to LangGraph’s explicit graph model, the OpenAI Agents SDK offers a minimal set of primitives, designed to be lightweight and easy to learn. Its philosophy is to provide just enough structure to build powerful applications without a steep learning curve.

The SDK is built around five core concepts[[3]](<https://openai.github.io/openai-agents-python/>):

- **Agents**: LLMs equipped with instructions and tools.
- **Tools**: Python functions that agents can call to interact with the outside world.
- **Guardrails**: Mechanisms for validating agent inputs and outputs to ensure safety and correctness.
- **Handoffs**: A way for agents to delegate tasks to other, more specialized agents.
- **Sessions**: Automatically manage conversation history across multiple runs.

![Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down)

Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.

The fundamental difference between the OpenAI Agents SDK and LangGraph’s functional API lies in the execution model[[3]](<https://openai.github.io/openai-agents-python/>). The OpenAI SDK uses a simple, Python-native agent loop that you control directly. Orchestration is handled with standard Python code (e.g., `if/else` statements, `for` loops)[[3]](<https://openai.github.io/openai-agents-python/>). In contrast, even with the decorator-based functional API, LangGraph compiles your code into an explicit, stateful graph. This underlying state machine manages execution, persistence, and interruptions, providing a more robust but also more constrained environment than the SDK’s straightforward loop.

The SDK keeps orchestration lightweight, allowing you to either let the LLM plan its actions or route logic with your own Python code. This makes it a fast path to production for teams that value a small conceptual surface and good defaults. The trade-off is that you will have to build some reliability features yourself, like durable pause and resume, that come out-of-the-box in more opinionated frameworks.

## Framework Deep Dive: AgentKit

AgentKit is OpenAI’s complete toolkit for building, deploying, and optimizing agents across the API and ChatGPT ecosystem. It extends the OpenAI Agents SDK by adding visual workflow design, UI embedding, and evaluation infrastructure.

![Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down)

Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.

AgentKit introduces several core components:

- **Agent Builder**: A drag-and-drop canvas for designing and versioning multi-agent workflows. Builders can compose logic visually, add guardrails, and run preview tests with inline evaluation and version control.
- **Connector Registry**: A centralized interface for managing data connections (Dropbox, Google Drive, SharePoint, Teams, and third-party MCPs) across workspaces and organizations.
- **ChatKit**: A toolkit for embedding agentic chat UIs directly into web or mobile products, handling streaming responses, conversation threads, and custom theming.
- **Evals and Reinforcement Fine-Tuning (RFT)**: Expanded capabilities for measuring, grading, and improving agent performance, including datasets, automated prompt optimization, and custom graders.
- **AgentKit sits one layer above the OpenAI Agents SDK**: you still use the SDK for code-first orchestration, but AgentKit provides the surrounding tools for design, deployment, and continuous improvement.

The trade-off is that AgentKit is currently most optimized for OpenAI’s ecosystem and assumes use of the OpenAI stack. However, its inclusion of MCP connectors suggests growing interoperability with external tools and protocols.

## Framework Deep Dive: CrewAI

![Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcc81dc-f35c-4a6b-95e8-557db10090a9/e0cb631a-91ae-46fc-a332-d5e1afd61c80/w=1920,quality=90,fit=scale-down)

Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`.

CrewAI is a framework designed for orchestrating teams of autonomous AI agents[[4]](<https://docs.crewai.com/introduction>). It introduces a powerful duality with its two main concepts: **Crews** and **Flows**.

- **Crews** are for role-based, autonomous collaboration[[4]](<https://docs.crewai.com/introduction>). You define agents with specific roles, goals, and tools, and they work together to solve a problem, much like a human team.
- **Flows** are for event-driven, deterministic orchestration[[6]](<https://docs.crewai.com/guides/flows/first-flow>). They give you fine-grained control over the workflow, allowing you to define precise execution paths[[6]](<https://docs.crewai.com/guides/flows/first-flow>).
This dual architecture lets you start with an autonomous crew for rapid prototyping, then introduce a flow to add structure and control as your requirements become more defined.

The developer experience is a major focus for CrewAI. It offers a command-line interface (CLI) for scaffolding projects[[5]](<https://docs.crewai.com/quickstart>) and uses YAML files to define agents and tasks[[5]](<https://docs.crewai.com/quickstart>), making configuration fast and readable. It excels in multi-agent automations where role clarity is crucial, such as when a research agent hands off findings to a writer agent for drafting.

The trade-off for this speed and high-level abstraction is the configuration overhead. To build robust systems, you need to work within CrewAI’s constructs, which involves defining Crews, writing Flows, configuring memory (short-term, long-term, and entity-based), choosing a persistence mechanism, and specifying state schemas. For very simple tasks, this might feel like more setup than a minimal SDK requires.

## Framework Deep Dive: PydanticAI

PydanticAI brings the developer experience of FastAPI to agent development. Its philosophy is built on type safety and data validation, using Pydantic models to define the inputs and outputs of every component. This creates a strong contract between your code and the LLM, moving many potential runtime errors to compile-time.

![Image 14: Diagram illustrating PydanticAI's design philosophy.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/0454e524-5d87-4288-82d4-3abd2b78a6f2/image/w=1920,quality=90,fit=scale-down)

Image 14: Diagram illustrating PydanticAI's design philosophy.

The framework has two key features for production systems. First, it supports **durable execution** via integrations with workflow engines such as Temporal, Prefect and DBOS[[7]](<https://ai.pydantic.dev/durable_execution/overview/>). This allows agents to survive restarts, pause for human input, and resume long-running tasks. Second, it has built-in **graph support** for modeling complex, non-linear control flow.

PydanticAI’s ergonomics are excellent for developers who value explicit schemas. Type hints automatically define tool schemas, docstrings become tool descriptions, and structured outputs guide automatic retries if the LLM’s output fails validation. The trade-off is that you must define these schemas up front, which can feel like additional initial setup. Teams unfamiliar with dependency injection or durable workflows will have a steep learning curve.

## Framework Deep Dive: AutoGen

![Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down)

Image 15: Visualizing a multi-agent workflow in **AutoGen Studio**. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.

AutoGen, from Microsoft Research, is a powerful framework with a layered design[[8]](<https://microsoft.github.io/autogen/stable/>), making it an excellent laboratory for exploring multi-agent patterns.

- **AutoGen Studio** is a low-code GUI that lets you prototype agent teams and workflows without writing code[[9]](<https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html>). You can visually compose agents, configure their tools, and test their interactions.

- **AgentChat** is a programming framework for building conversational multi-agent applications[[8]](<https://microsoft.github.io/autogen/stable/>).

- **Core** provides low-level, event-driven primitives for building scalable, custom agent systems[[8]](<https://microsoft.github.io/autogen/stable/>).

The typical journey with AutoGen involves using Studio to quickly explore and validate an idea, then exporting the configuration and hardening the architecture in code using AgentChat or Core[[9]](<https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html>). It is critical to understand that **Studio is a research prototype and is not intended for production**[[9]](<https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html>).

The trade-off with AutoGen is its focus on experimentation. While it is incredibly flexible for research and development, you will need to re-implement many production necessities like reliability, security, and observability yourself when you move to a production environment.

## Framework Deep Dive: Claude Agent SDK

As a newer entrant from Anthropic, the Claude Agent SDK is designed for tight integration with the Claude family of models. While the ecosystem is still maturing compared to more established frameworks, its philosophy centers on leveraging Claude’s strengths, including large context windows, strong reasoning capabilities, and low-level tool use control.

The SDK aims to provide an ergonomic way to build agents that can reliably call tools and orchestrate complex tasks. For teams already committed to the Anthropic ecosystem, this framework offers the promise of a more optimized and native development experience. The trade-off is a smaller community and fewer third-party integrations at this stage. As with any new framework, early adoption means navigating a rapidly evolving API, but it also offers the opportunity to build applications that are finely tuned to the underlying models.

## Framework Deep Dive: FastMCP

![Image 16: FastMCP Architecture and Interoperability](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/745828fd-27e2-4a50-b613-7275a1e1dceb/image/w=1920,quality=90,fit=scale-down)
Image 16: FastMCP Architecture and Interoperability

You use FastMCP to build an MCP client or server that exposes your tools, resources, and prompts[[10]](<https://gofastmcp.com/>). This server can then be called by any MCP-compliant client, whether a LangGraph agent, an IDE plugin, or a simple script[[10]](<https://gofastmcp.com/>). This interoperability is its key strength. You write your tools once and can reuse them across your entire stack, drastically reducing lock-in and duplicate work[[10]](<https://gofastmcp.com/>).

FastMCP also provides production-grade features beyond the basic protocol, including authentication, server composition, and a cloud platform for easy deployment[[10]](<https://gofastmcp.com/>). For our capstone project, we adopted FastMCP to ensure our tools were portable. Our research agent is a FastMCP server, and its tools can be called from any MCP client[[10]](<https://gofastmcp.com/>).

<aside>

💡 **Pattern: tools-as-workflows (Brown)** 
For our writing agent (Brown), we wrap each workflow entry point as a **coarse-grained MCP tool** (e.g., `generate_article`, `edit_article`, `edit_selected_text`). The MCP tool handler simply **kicks off the corresponding LangGraph run** , returns progress/messages, and finally yields artifacts and diffs. This gives you MCP portability (Cursor, Claude Code) **without** losing LangGraph’s durability and auditability.
You’ll learn more about this in the later lessons.

</aside>

The developer experience is designed to be simple and Pythonic[[11]](<https://gofastmcp.com/getting-started/quickstart>). You can expose a function as a tool with a single decorator, and FastMCP handles schema generation and transport[[11]](<https://gofastmcp.com/getting-started/quickstart>). Here is a quick example from the official docs [[11]](<https://gofastmcp.com/getting-started/quickstart>).

    from fastmcp import FastMCP

    mcp = FastMCP("My MCP Server")

    @mcp.tool
    def greet(name: str) -> str:
        return f"Hello, {name}!"

    if __name__ == "__main__":
        mcp.run()

## Choosing for Your Project: Decision Matrix & Tentative Forecasts

To turn these principles into practical guidance, we can use a decision matrix to map common project needs to the frameworks that are a natural fit.

Table 1: Decision matrix comparing AI agent frameworks against common needs

| Feature | LangGraph | PydanticAI | OpenAI SDK | AgentKit | CrewAI | AutoGen | FastMCP |
|---------|---|---|---|---|---|---|---|
| **Durability/HITL/Replay** | ✅ | | | | | ✅ | |
| **Typed Contracts + Durable Execution** | | ✅ | | | | | ✅ |
| **Few Primitives + Guardrails/Handoffs** | ✅ | | ✅ | ✅ | | | ✅ |
| **Role-based Teams + Quick Scaffolding** | | | | ✅ | ✅ | ✅ | |
| **Exploration Lab** | | | ✅ | ✅ | ✅ | ✅ | |
| **Tool Portability Across Stacks** | | ✅ | | ✅ | | | ✅ |

Please keep in mind that these libraries and frameworks are evolving rapidly, so the features from the table above may become outdated in the next months.

Based on the table above, we can make a tentative forecast. LangGraph and PydanticAI are strong candidates for production workflows where reliability, auditability, and correctness are the primary concerns. The OpenAI Agents SDK will appeal to a broad developer base that values simple agents, while AgentKit is primarily for teams that need visual workflow design, chat embedding, and evaluation infrastructure. CrewAI is well-suited for rapid multi-agent prototyping with a clear path to more structured control. FastMCP will remain the durable tooling substrate that connects these different runtimes, and AutoGen will continue to serve as the R&D lab for exploring new multi-agent patterns.

Remember to combine these axes. It is common to use FastMCP tools inside a LangGraph workflow or to start in AutoGen Studio before migrating to a more production-hardened framework. If you want an IDE-native user experience for a long-running workflow, you can keep LangGraph for orchestration but front it with FastMCP by exposing each workflow as an MCP command. This provides MCP portability for an enhanced user experience, combined with LangGraph’s durability for reliability.

## Our Capstone Pivots

Let’s apply this matrix to our capstone project. Our decision-making process evolved as we built, highlighting the importance of choosing the right tool for the job.

We began by planning to use LangGraph for both the research and writing agents. However, early experiments showed that research is an interactive and divergent process. We needed to add tools, change our approach mid-run, and replan frequently. A rigid workflow was not the right fit. To maximize portability and flexibility, we moved the research workload into MCP tools and implemented our research agent, Nova, as a **FastMCP server**[[10]](<https://gofastmcp.com/>). Any MCP client can now steer it.

The writing agent, Brown, took the opposite path. The writing process was repeatable and required auditability. We required checkpoints for long drafts, HITL interrupts for editing, and the ability to replay the process for debugging. We kept Brown as a **LangGraph workflow**[[2]](<https://docs.langchain.com/oss/python/langgraph/persistence>), but its tools are also served by FastMCP[[10]](<https://gofastmcp.com/>). In short: **LangGraph for orchestration; FastMCP for tools**.

To provide a seamless developer experience, we also expose Brown’s core workflows as coarse-grained MCP tools. This allows an MCP client like Cursor to trigger an entire writing or editing process with a single command, while LangGraph manages the durable, auditable execution behind the scenes. Brown currently exposes three tools: `generate_article`, `edit_article`, and `edit_selected_text`.

We also considered alternatives. The OpenAI Agents SDK was a solid contender for its lightweight primitives, and it remains a great option for projects that value a minimal surface area. However, we ultimately centered the capstone on LangGraph and FastMCP to leverage their first-class support for persistence, HITL, and MCP-backed portability, which are critical for our complex, long-running tasks.

## Conclusion

The key lesson is to prioritize concepts over brands. The general concepts: stateful graphs[[1]](<https://docs.langchain.com/oss/python/langgraph/workflows-agents>)[[2]](<https://docs.langchain.com/oss/python/langgraph/persistence>), typed contracts, durable execution[[7]](<https://ai.pydantic.dev/durable_execution/overview/>), and tool standardization (MCP)[[10]](<https://gofastmcp.com/>) will allow you to adapt as frameworks rise and fall. The agent landscape will continue to evolve, but a solid understanding of these core principles will enable you to make informed decisions. The MCP specification is short and worth skimming; understanding it once pays dividends across every agent stack[[10]](<https://gofastmcp.com/>).

Prototype, measure, and iterate. Begin by selecting the decision axes, then choose the smallest stack that meets your current needs, and finally keep your tooling interface portable with MCP to avoid lock-in. It is common to start a pattern in AutoGen Studio for speed[[9]](<https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html>), migrate your tools to FastMCP for portability[[10]](<https://gofastmcp.com/>), and anchor your long-running flows in LangGraph or PydanticAI as your requirements solidify[[2]](<https://docs.langchain.com/oss/python/langgraph/persistence>)[[7]](<https://ai.pydantic.dev/durable_execution/overview/>).

In the next lesson (14), you’ll formalize the **system‑design decision framework** —how to choose models, balance cost/latency, and place human‑in‑the‑loop gates. Later in Part 2 (Lessons 16–24), you’ll build both agents end‑to‑end: **Nova** with **FastMCP** (server/client, ingestion, Perplexity loops, filtering, `research.md`) and **Brown** with **LangGraph + FastMCP** (workflow + MCP tools, profiles via context engineering, evaluator‑optimizer review‑edit cycles, HITL editing).

### References

  1. LangChain. (n.d.). _Workflows and agents_. LangChain Documentation. <https://docs.langchain.com/oss/python/langgraph/workflows-agents>
  2. LangChain. (n.d.). _Persistence_. LangChain Documentation. <https://docs.langchain.com/oss/python/langgraph/persistence>
  3. OpenAI. (n.d.). _OpenAI Agents SDK_. OpenAI. <https://openai.github.io/openai-agents-python/>
  4. CrewAI. (n.d.). _Introduction_. CrewAI Documentation. <https://docs.crewai.com/introduction>
  5. CrewAI. (n.d.). _Quickstart_. CrewAI Documentation. <https://docs.crewai.com/quickstart>
  6. CrewAI. (n.d.). _Build your first Flow_. CrewAI Documentation. <https://docs.crewai.com/guides/flows/first-flow>
  7. Pydantic. (n.d.). _Durable Execution_. Pydantic AI Documentation. <https://ai.pydantic.dev/durable_execution/overview/>
  8. Microsoft. (n.d.). _AutoGen_. Microsoft. <https://microsoft.github.io/autogen/stable/>
  9. Microsoft. (n.d.). _AutoGen Studio User Guide_. AutoGen Documentation. <https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html>
  10. Prefect Technologies, Inc. (n.d.). _FastMCP_. FastMCP. <https://gofastmcp.com/>
  11. Prefect Technologies, Inc. (n.d.). _Quickstart_. FastMCP Documentation. <https://gofastmcp.com/getting-started/quickstart>