# How to Choose an AI Agent Framework

In our last lesson, we introduced the scope and design of our central project: a system of two specialized agents, Nova and Brown. Nova is an adaptable research agent, and Brown is a reliable, auditable writing agent. This lesson provides the scaffolding for choosing the right frameworks to build them.

The choice of an agent framework can make or break a project. A poor selection can lead to brittle abstractions that fail under real-world load, creating systems that are difficult to debug and maintain. It can stall progress in a fast-moving ecosystem or reveal hidden gaps in durability that only appear after weeks of investment, forcing costly rewrites. This lesson provides the scaffolding for choosing the right frameworks to build our agents, ensuring they are both powerful and production-ready.

Throughout this lesson, we will use two core concepts as our guide: LangGraph's interrupts and checkpoints for resumable auditability in our writing agent, and the Model Context Protocol (MCP) as a universal layer that keeps our research agent's tools portable. Our high-level architecture, shown in Image 1, will be our reference point. The research agent is built as a lightweight MCP server that any client can steer, while the writing agent is a durable workflow that exposes its capabilities as coarse-grained MCP tools. This lesson focuses on the philosophies, core abstractions, and production trade-offs of various frameworks, providing you with decision principles rather than just API syntax.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down>
Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

With our capstone projects as a concrete reference, let's examine why framework selection so often fails in production and understand the distinct layers—runtime, protocol, and tooling—that solve different problems.

## Framework Choice Under Uncertainty

The AI agent ecosystem is new and evolving quickly, and no single framework will satisfy every use case. It is important to distinguish between three layers that are often conflated: the runtime, the protocol, and the tooling framework. Each layer solves a distinct set of production problems.

The **runtime** (e.g., LangGraph, CrewAI) is the infrastructure layer that handles orchestration and state management. It provides durable execution, ensuring that an agent can recover from crashes, pause for human input, and manage its memory across long-running tasks. The **protocol**, like the MCP, provides a standard for interoperability. It acts as a universal language for tools, preventing vendor lock-in and allowing you to reuse tools across different runtimes. Finally, the **tooling framework** (e.g., FastMCP) offers ready-to-deploy components like transports, authentication, and server scaffolding, which improve the developer experience and accelerate development.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down>
Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

Engineers who select frameworks based on hype or simple "hello, world" demos often encounter failure modes in production. A framework might be too simple, lacking the reliability primitives needed for durable, long-running workflows. Conversely, a framework might be overly complex, introducing unnecessary overhead for what should be a simple, exploratory task.

Our capstone projects illustrate this perfectly. An initial plan to use a static graph for our research agent failed because research is an interactive and divergent process. The agent needed to pivot, add tools, and replan on the fly, which a rigid structure could not accommodate. However, that same static graph structure proved ideal for our writing agent, which required a repeatable and auditable process with clear checkpoints. This highlights the importance of matching the framework to the workload, which is why assessing a task as either interactive or deterministic is a good first step.

We learned this firsthand. We initially planned to build our research agent with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was a wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes Instead of Brands

To avoid common pitfalls, you need a way to evaluate frameworks based on principles. We have identified four decision axes that can help you analyze any library and determine if it fits your project’s needs.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down>
Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

The first axis is **control-flow explicitness versus LLM-driven autonomy**. This trade-off is rooted in the non-deterministic nature of LLMs; factors like temperature settings make pure LLM-driven control a challenge for regulated environments requiring reproducible results [[1]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13079118). Graph-based frameworks like LangGraph offer determinism, with explicit nodes and edges that make every state transition auditable. This is ideal for workflows where you need to know precisely why the system made a decision. In contrast, lightweight agent loops, like those in the OpenAI Agents SDK, favor exploration and adaptability, which is better for tasks where the path to a solution is not known in advance. The question to ask is: does your application require repeatable, auditable steps, or does it need to navigate an unpredictable environment?

The second axis is **reliability primitives**. A good framework provides tools to handle failures gracefully, drawing lessons from safety-critical systems where consistency and predictable failure modes are paramount [[2]](https://www.linkedin.com/posts/baraktur_towards-a-science-of-ai-agent-reliability-activity-7434268792404267008-W8nW). Look for features like checkpointing, time-travel replay, and durable execution across restarts. It is also important to consider support for human-in-the-loop, or HITL, which allows for human intervention in a workflow—a topic we will explore in detail in Lesson 14. LangGraph, for example, emphasizes interrupts and persistence [[3]](https://docs.langchain.com/oss/python/langgraph/persistence), while PydanticAI integrates with systems like Temporal and DBOS for durable execution [[4]](https://ai.pydantic.dev/durable_execution/overview/). These features are non-negotiable for our writing agent but less critical for the research agent.

The third axis is **abstraction level and developer experience**. Some frameworks, like the OpenAI Agents SDK, provide minimal primitives that require more boilerplate but offer greater flexibility. Others, like CrewAI, use opinionated constructs that accelerate initial development but may reduce adaptability later on.

The fourth axis is **tooling interoperability**. MCP acts as the USB-C of AI, providing a standard interface for tools. This lets you write tools once as MCP servers, for example, with FastMCP [[5]](https://gofastmcp.com/), and reuse them across different runtimes and IDEs like Cursor without rewriting them.

Our capstone projects map clearly to these axes. The research agent requires autonomy and interoperable tools, making a lightweight loop with MCP a good fit. The writing agent demands an explicit, auditable workflow with strong reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks.

### LangGraph

LangGraph’s philosophy is built on a stateful graph model with native checkpoints and interrupts for auditable workflows [[3]](https://docs.langchain.com/oss/python/langgraph/persistence). This makes it ideal for processes that need to be resumable and traceable [[6]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). Its graph-based architecture provides explicit control over state transitions, which is essential for building reliable, production-grade systems where every decision must be traceable. LangGraph has shown strong, consistent daily download activity, averaging around 400K–500K downloads per day over the past three months, indicating a healthy and active user base.

<aside>
💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers, etc.), **LangGraph** focuses specifically on **structured**, **stateful workflows**. It introduces graph-based execution with checkpoints and resumability, which are features not native to standard LangChain chains.

In short, LangChain is the toolbox, while LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions [[6]](https://docs.langchain.com/oss/python/langgraph/workflows-agents).
</aside>

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down>
Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.

### OpenAI Agents SDK

The OpenAI Agents SDK features a minimal surface area consisting of agents, tools, guardrails, handoffs, and sessions [[7]](https://openai.github.io/openai-agents-python/). It favors lightweight, Python-native loops over compiled state machines. This approach gives developers more direct control over the execution flow, using familiar Python constructs rather than learning a new graph-based syntax. The library has recorded 90K–120K daily downloads over the past three months, with a slight upward trend, suggesting steady adoption.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down>
Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.

### AgentKit

AgentKit is a modular toolkit for building, deploying, and optimizing agents across the OpenAI platform. It unifies a visual builder, connectors (including MCP), a ChatKit for embedding, and evaluation infrastructure. This end-to-end environment is designed to accelerate the entire agent development lifecycle, from initial design to long-term maintenance and improvement. Developers can visually compose multi-agent systems, manage connectors, and embed chat-based experiences directly in their products, all backed by versioning, guardrails, and evaluation tools for safe, reliable deployment.

<aside>
💡 OpenAI AgentKit vs. OpenAI Agents SDK

The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration and fine-grained control. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK: it adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**. In short, the SDK is the coding foundation, while AgentKit is the integrated platform for design, deployment, and optimization.
</aside>

### CrewAI

CrewAI is known for its duality: role-based autonomous crews for collaborative exploration versus event-driven flows for deterministic control [[8]](https://docs.crewai.com/introduction). This unique architecture allows developers to prototype quickly with autonomous agents for tasks like research and then add the deterministic structure of flows as the application matures into a production system. It also provides a strong developer experience with its CLI and YAML configurations. The library's daily downloads range between 40K and 100K.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down>
Image 6: Source: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.

### PydanticAI

PydanticAI emphasizes type safety, schema-driven validation, and durable execution through integrations with systems like Temporal, DBOS, or Prefect, along with built-in graph support. This focus on data integrity, enforced at runtime, makes it a strong choice for enterprise applications where correctness and reliability are non-negotiable. Daily downloads of Pydantic-AI doubled from ~150k in July to 300-450k by October 2025, demonstrating strong growth.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down>
Image 7: Source: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.

### AutoGen

AutoGen takes a layered approach, with its Studio GUI positioned for exploration and prototyping, feeding ideas into its AgentChat or core libraries for production hardening [[9]](https://microsoft.github.io/autogen/stable/). This allows for rapid, low-commitment experimentation in a visual environment while providing a clear path to building robust, production-ready applications using the underlying code libraries.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down>
Image 8: Source: pepy.tech, daily downloads for autogen, accessed October 15, 2025.

### Claude Agent SDK

The Claude Agent SDK is a newer entrant from Anthropic. It offers tight integration with the Claude model family. It is designed to take full advantage of Claude's specific capabilities, such as its large context window for complex reasoning and its fine-grained tool use control, but it has a smaller ecosystem.

### FastMCP

FastMCP is a non-runtime tooling layer that allows you to build MCP-compliant servers and clients, making your tools portable across any runtime or IDE. This focus on interoperability is a significant advantage in a rapidly evolving ecosystem, as it decouples your tool implementations from any single framework, ensuring they remain useful even if you switch runtimes. It has shown explosive growth, with daily downloads surging from ~250k in July to over 1.2M per day in October 2025, a 5x increase, highlighting the growing importance of interoperability.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down>
Image 9: Source: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.

We use adoption metrics like download trends and GitHub stars as a proxy for maturity, which helps gauge hiring risk, ecosystem health, and long-term maintenance. It is also important to avoid single-framework dogma; hybrid patterns, such as using FastMCP tools within LangGraph, are common and effective.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down>
Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026.

We will now examine each framework in detail, using the four axes and capstone needs as constant evaluation lenses.

## Framework Deep Dive: LangGraph

LangGraph uses a graph-based modeling approach where nodes are Python functions and edges are explicit transitions. This makes complex, multi-step logic transparent and auditable. Its core production primitives include interrupts for human-in-the-loop interaction, persistence and checkpointing for resumability, and time-travel debugging, which lets you replay and branch from any prior state.

However, this durability comes with a scaling challenge. By default, LangGraph writes the full state at every step, which can lead to significant storage growth in long-running conversations. To mitigate this, the framework offers optimizations like `DeltaChannel`, which stores only the incremental changes, and configurable persistence modes that trade-off between performance and recoverability [[17]](https://docs.langchain.com/oss/python/langgraph/persistence).

LangGraph offers two definition styles: a "graph API" for fully explicit graphs and a "functional API" that is decorator-based. This presents a trade-off between the learning curve and the payoff in determinism. This upfront modeling cost is a key differentiator from lighter, more autonomous loops. While those loops are easier to start with, they often lack the built-in safety, observability, and durability needed for production. For repeatable, auditable processes like our writing agent, the initial investment in a graph-based model is justified by the long-term reliability it provides.

Having examined a graph-centric, reliability-first option, we now turn to a deliberately minimal alternative.

## Framework Deep Dive: OpenAI Agents SDK

The OpenAI Agents SDK is built on a philosophy of minimal primitives, which reduces the conceptual surface area while still enabling powerful agentic applications. Its core concepts—agents, tools, guardrails, handoffs, and sessions—provide a minimal yet powerful set of primitives for building agentic applications [[7]](https://openai.github.io/openai-agents-python/).

**Agents** are LLMs equipped with instructions and tools. They form the core of the application, responsible for reasoning and decision-making.

**Tools** are Python functions that agents can call to interact with the outside world, such as fetching data from an API or querying a database.

**Guardrails** are mechanisms for validating agent inputs and outputs to ensure safety and correctness, preventing unintended or harmful actions.

**Handoffs** provide a way for agents to delegate tasks to other, more specialized agents, enabling a modular and scalable architecture.

**Sessions** automatically manage conversation history across multiple runs, allowing agents to maintain context and have more coherent interactions.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down>
Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.

The fundamental difference between the OpenAI Agents SDK and LangGraph’s functional API lies in the execution model. The OpenAI SDK uses a simple, Python-native agent loop that you control directly with standard code like `if/else` statements and `for` loops. In contrast, even with its decorator-based functional API, LangGraph compiles your code into an explicit, stateful graph. This underlying state machine manages execution, persistence, and interruptions, providing a more robust but also more constrained environment.

The SDK is a strong choice for teams that want a fast path to production with lightweight orchestration. However, it comes with a reliability trade-off: features like durable pause, resume, and checkpointing are not provided out of the box and must be implemented by the team.

The natural extension of this minimal SDK is a full-lifecycle platform built on top of it.

## Framework Deep Dive: AgentKit

AgentKit is a complete lifecycle toolkit layered on top of the OpenAI Agents SDK, covering design, deployment, and optimization. It extends the SDK by adding visual workflow design, UI embedding, and evaluation infrastructure, providing an end-to-end environment for building and managing agents.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down>
Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.

**Agent Builder** is a drag-and-drop canvas for designing and versioning multi-agent workflows. Builders can compose logic visually, add guardrails, and run preview tests with inline evaluation and version control.

**Connector Registry** is a centralized interface for managing data connections (Dropbox, Google Drive, SharePoint, Teams, and third-party MCPs) across workspaces and organizations.

**ChatKit** is a toolkit for embedding agentic chat UIs directly into web or mobile products, handling streaming responses, conversation threads, and custom theming.

**Evals and Reinforcement Fine-Tuning (RFT)** provide expanded capabilities for measuring, grading, and improving agent performance, including datasets, automated prompt optimization, and custom graders. Reinforcement Fine-Tuning, or RFT, is a technique for customizing reasoning models, which we will cover in a future lesson.

AgentKit sits one layer above the OpenAI Agents SDK. You use the SDK for code-first orchestration, while AgentKit provides the surrounding tools for design, deployment, and continuous improvement. This allows for safe multi-agent systems at scale without forcing everything into code. While it is strongest within the OpenAI stack, its growing MCP connector support improves interoperability. This is particularly valuable in a visual builder, as MCP allows the platform to dynamically discover tool capabilities without requiring developers to write and maintain custom integration code for each new service [[10]](https://www.scalekit.com/blog/mcp-vs-apis-how-are-they-different). AgentKit adds clear value for teams that need no-code workflow design, versioning, and continuous improvement loops.

We now examine a framework whose duality spans both autonomous crews and structured flows.

## Framework Deep Dive: CrewAI

CrewAI’s core philosophy is to model problems as building a team of people, rather than a graph of nodes (LangGraph) or a conversation (AutoGen) [[11]](https://vadim.blog/crewai-unique-features). This is expressed through its dual architecture: **Crews** for autonomous collaboration and **Flows** for deterministic control [[8]](https://docs.crewai.com/introduction).

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcc81dc-f35c-4a6b-95e8-557db10090a9/e0cb631a-91ae-46fc-a332-d5e1afd61c80/w=1920,quality=90,fit=scale-down>
Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`.

**Crews** are for role-based, autonomous collaboration. You define agents with specific roles (e.g., "researcher," "writer"), goals, and tools, and they work together to solve a problem. **Flows**, by contrast, are for event-driven, deterministic orchestration, giving you fine-grained control over the workflow's execution path [[12]](https://docs.crewai.com/guides/flows/first-flow). This dual architecture lets you prototype with an autonomous crew, then wrap it in a flow to add production-grade structure and control [[11]](https://vadim.blog/crewai-unique-features).

The framework provides a strong developer experience with CLI scaffolding and YAML definitions for agents and tasks. Its sweet spot is in multi-agent handoff scenarios, such as researcher-to-writer workflows, where role clarity accelerates development. However, its opinionated constructs come with trade-offs. The `Process.hierarchical` mode, which auto-generates a manager agent, is conceptually appealing but has been shown to be unreliable in practice, often failing to delegate tasks intelligently and simply executing them sequentially [[11]](https://vadim.blog/crewai-unique-features). This highlights a key limitation: while the "team" metaphor is intuitive, it can break down when the underlying LLM lacks the reasoning capacity for true management.

Another framework approaches the problem through the lens of type safety and compile-time contracts.

## Framework Deep Dive: PydanticAI

PydanticAI follows a philosophy similar to FastAPI, where Pydantic models and type hints create compile-time contracts between your code and the LLM's behavior. This focus on type safety ensures data integrity and predictability.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/0454e524-5d87-4288-82d4-3abd2b78a6f2/image/w=1920,quality=90,fit=scale-down>
Image 14: Diagram illustrating PydanticAI's design philosophy.

Its production-ready features include **durable execution integrations** with platforms like Temporal, DBOS, or Prefect, allowing agents to survive restarts and handle long-running tasks [[4]](https://ai.pydantic.dev/durable_execution/overview/). It also has built-in **graph support** for non-linear flows. The developer experience is enhanced by automatic schema generation from type hints and structured output with automatic retries on validation failure.

The main trade-off is the up-front investment in defining schemas, which can be a learning curve for teams new to strict typing. However, this investment pays off in correctness guarantees. PydanticAI is best suited for projects where structured data correctness and resumable tasks are paramount, which aligns well with our writing agent’s need for auditability.

We now look at a layered system explicitly separating experimentation from production hardening.

## Framework Deep Dive: AutoGen

AutoGen features a layered design that deliberately separates experimentation from production [[9]](https://microsoft.github.io/autogen/stable/). This architecture allows for a smooth transition from rapid prototyping to building robust, production-ready applications.

**AutoGen Studio** is a low-code GUI that lets you prototype agent teams and workflows without writing code. You can visually compose agents, configure their tools, and test their interactions.

**AgentChat** is a programming framework for building conversational multi-agent applications.

**Core** provides low-level, event-driven primitives for building scalable, custom agent systems.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down>
Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.

The typical workflow involves exploring and validating ideas visually in Studio, then hardening the successful patterns into code using the lower layers. It is important to note the explicit disclaimer that Studio is a research prototype and not intended for production environments [[13]](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html).

AutoGen's strength lies in its use as an R&D laboratory for discovering multi-agent conversation patterns. However, this flexibility during exploration comes with a trade-off: the team must re-implement reliability, security, and observability when moving to production.

A newer entrant focuses on tight model-family integration.

## Framework Deep Dive: Claude Agent SDK

The Claude Agent SDK is built on a philosophy of tight integration with the Claude model family, taking advantage of its strengths in large context windows, strong reasoning, and fine-grained control over tool use. It focuses on providing an ergonomic tool-calling and orchestration experience tailored specifically to Anthropic models.

As a newer entrant, it has a smaller community and fewer third-party integrations, and its API is still evolving. This presents a trade-off between opportunity and risk. Early adoption can yield model-optimized performance, but teams must balance this against the maturity of the ecosystem. The clearest use case is for teams already committed to the Anthropic stack who want native performance and are willing to accept smaller community support.

The final deep dive examines a non-runtime layer that complements every option above.

## Framework Deep Dive: FastMCP

FastMCP is not a runtime; it is a tooling layer that lets you build MCP-compliant servers and clients. This makes your tools, resources, and prompts portable across any runtime or IDE that speaks the protocol [[5]](https://gofastmcp.com/). The key benefit is interoperability: you can write a tool once and reuse it in LangGraph, the OpenAI SDK, Cursor, or any other compatible system. This portability is a significant advantage in a rapidly evolving ecosystem, as it decouples your tool implementations from any single framework.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/745828fd-27e2-4a50-b613-7275a1e1dceb/image/w=1920,quality=90,fit=scale-down>
Image 16: FastMCP Architecture and Interoperability

The developer experience is designed to be simple and Pythonic. You can expose a function as a tool with a single decorator, and FastMCP handles the schema generation and transport details [[14]](https://gofastmcp.com/getting-started/quickstart). This removes significant boilerplate, allowing developers to focus on the tool's logic rather than the complexities of the MCP protocol, schema validation, or transport negotiation [[18]](https://generect.com/blog/langgraph-mcp).

```python
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

FastMCP also provides production extensions like authentication, server composition, and cloud deployment features. Our capstone projects use this pattern extensively: the research agent, Nova, is implemented as a FastMCP server whose tools for searching and scraping can be steered by any client. Meanwhile, the writing agent, Brown, exposes its complex LangGraph workflows as coarse-grained MCP tools, making its durable, auditable processes available to other systems in a standardized way.

<aside>
💡 Pattern: tools-as-workflows (Brown)

For our writing agent (Brown), we wrap each workflow entry point as a **coarse-grained MCP tool** (e.g., `generate_article`, `edit_article`, `edit_selected_text`). The MCP tool handler simply **kicks off the corresponding LangGraph run**, returns progress/messages, and finally yields artifacts and diffs. This gives you MCP portability (Cursor, Claude Code) **without** losing LangGraph’s durability and auditability.
You’ll learn more about this in the later lessons.
</aside>

With our detailed examinations complete, we can now synthesize everything into a decision matrix.

## Choosing for Your Project: Decision Matrix & Tentative Forecasts

To help you choose the right framework, we have created a decision matrix that maps common project needs to the relative strengths of each framework. This matrix serves as a practical guide for navigating the complex landscape of agent frameworks and making an informed decision based on your specific requirements.

Table 1: Decision matrix comparing AI agent frameworks against common needs

| Feature | LangGraph | PydanticAI | OpenAI SDK | AgentKit | CrewAI | AutoGen | FastMCP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Durability/HITL/Replay** | ✅ | | | | | ✅ | |
| **Typed Contracts + Durable Execution** | | ✅ | | | | | ✅ |
| **Few Primitives + Guardrails/Handoffs** | ✅ | | ✅ | ✅ | | | ✅ |
| **Role-based Teams + Quick Scaffolding**| | | | ✅ | ✅ | ✅ | |
| **Exploration Lab** | | | ✅ | ✅ | ✅ | ✅ | |
| **Tool Portability Across Stacks** | | ✅ | | ✅ | | | ✅ |

Treat this matrix as a snapshot in time. The ecosystem is evolving, so always re-evaluate new releases against the four decision axes.

Based on this, we can make some tentative forecasts. LangGraph and PydanticAI are well-suited for reliability-heavy workflows. The OpenAI SDK is a good choice for lightweight simplicity, while AgentKit is ideal when visual design and continuous evaluation are required. CrewAI is excellent for rapid multi-agent prototyping, FastMCP serves as a universal tooling substrate, and AutoGen is a strong starting point for R&D.

In practice, hybrid patterns are common. You might consume FastMCP tools inside LangGraph workflows, migrate from AutoGen prototypes to hardened runtimes, or expose complex graphs as single MCP commands to gain IDE portability without sacrificing durability.

To make this theory concrete, let's share the actual pivots we made while building the course capstones.

## Our Capstone Pivots

Let’s apply this matrix to our capstone project. Our decision-making process evolved as we built, highlighting the importance of choosing the right tool for the job and being willing to pivot when a framework does not meet the project's needs.

Our initial plan was to use LangGraph for both agents. However, we quickly found that the research agent’s need for high interactivity and divergent exploration made rigid graphs cumbersome. The structured, stateful nature of LangGraph, while powerful, introduced unnecessary overhead for a task that required flexibility and rapid iteration. Flexible MCP tools proved to be a better fit, allowing us to build a lightweight, adaptable agent that could easily be steered by any client.

For the writing agent, the requirements were the opposite. Its repeatable, auditable process demanded LangGraph’s checkpoints, HITL interrupts, and time-travel replay capabilities. These features were essential for ensuring the reliability and traceability of the writing process, allowing for human oversight and intervention at critical points.

The result is a hybrid architecture. Nova, our research agent, is implemented as a FastMCP server that any client, including IDEs, can steer. Brown, our writing agent, is a LangGraph workflow whose entry points are exposed as coarse-grained MCP tools. This approach gives us portability without sacrificing durability or auditability. Brown currently exposes three tools: `generate_article`, `edit_article`, and `edit_selected_text`.

We considered the OpenAI Agents SDK but ultimately deprioritized it because it lacked the first-class persistence and deep MCP integration required for the long-running nature of our capstone tasks. These real-world pivots illustrate the central lesson of this module.

## Conclusion

The core takeaway from this lesson is to prioritize stable concepts—stateful graphs, typed contracts, durable execution, and MCP standardization—over transient brand names. Frameworks will come and go, but these underlying principles will remain relevant. The MCP specification itself is a valuable read; a one-time investment yields portability across every current and future stack. As an open standard, its evolution will be shaped by ongoing research into areas like enhanced security for multi-tenant deployments and streaming extensions for real-time workflows [[15]](https://www.databricks.com/blog/what-is-model-context-protocol), [[16]](https://project-rachel.4open.science/Rachel.So.MCP.Servers.for.Scientific.Workflows.pdf).

A practical selection process is to apply the four decision axes to your project, start with the smallest viable stack that meets your reliability needs, and keep all your tooling portable via MCP. A common migration path is to begin exploration in AutoGen Studio, extract successful patterns into FastMCP tools, and then anchor the production system in a framework like LangGraph or PydanticAI. This approach allows for rapid prototyping while ensuring a clear path to a robust, production-ready application.

In our next lesson, we will cover system design, including model selection, cost/latency trade-offs, and HITL placement. After that, we will begin the hands-on capstone builds, using the hybrid FastMCP-plus-LangGraph stack we have chosen through this exact process: **Nova** with **FastMCP** for research and **Brown** with **LangGraph + FastMCP** for writing and editing. This will provide a concrete demonstration of how to apply the principles discussed in this lesson to build real-world, production-grade agentic systems.

## References

- [1]  [LLMs lack reproducibility](https://pmc.ncbi.nlm.nih.gov/articles/PMC13079118)
- [2]  [Towards a Science of AI Agent Reliability](https://www.linkedin.com/posts/baraktur_towards-a-science-of-ai-agent-reliability-activity-7434268792404267008-W8nW)
- [3]  [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [4]  [Durable Execution](https://ai.pydantic.dev/durable_execution/overview/)
- [5]  [FastMCP](https://gofastmcp.com/)
- [6]  [Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
- [7]  [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [8]  [Introduction](https://docs.crewai.com/introduction)
- [9]  [AutoGen](https://microsoft.github.io/autogen/stable/)
- [10]  [MCP vs APIs: How are they different?](https://www.scalekit.com/blog/mcp-vs-apis-how-are-they-different)
- [11]  [CrewAI's Genuinely Unique Features: An Honest Technical Deep-Dive](https://vadim.blog/crewai-unique-features)
- [12]  [Build your first Flow](https://docs.crewai.com/guides/flows/first-flow)
- [13]  [AutoGen Studio User Guide](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- [14]  [Quickstart](https://gofastmcp.com/getting-started/quickstart)
- [15]  [What is the Model Context Protocol (MCP)?](https://www.databricks.com/blog/what-is-model-context-protocol)
- [16]  [MCP Servers for Scientific Workflows](https://project-rachel.4open.science/Rachel.So.MCP.Servers.for.Scientific.Workflows.pdf)
- [17]  [LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [18]  [LangGraph MCP Client Setup Made Easy](https://generect.com/blog/langgraph-mcp)