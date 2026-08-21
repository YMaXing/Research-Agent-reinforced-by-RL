# How to Choose an AI Agent Framework in 2026

In our last lesson, we introduced the two capstone projects that will guide us through the rest of this course: Nova, an adaptable and interactive research agent, and Brown, a reliable and auditable writing agent. Before we can build them, we face a significant choice: selecting the right framework. This decision is not simple. A poor choice can lead to brittle abstractions that break under real-world load, stall your progress in a fast-moving ecosystem, or reveal hidden gaps in durability only after weeks of investment.

This lesson will equip you with a principled approach to making that choice. We will move beyond hype and brand names to focus on the engineering realities of building production-grade agents. Two core concepts will guide our discussion: the auditable, resumable workflows enabled by **LangGraph's interrupts and checkpoints**, and the universal interoperability provided by the **Model Context Protocol (MCP)**, which keeps your tools portable.

Our capstone projects will serve as a consistent reference point. We will build our research agent, Nova, as a lightweight MCP server that any client can steer. Our writing agent, Brown, will be a durable LangGraph workflow that exposes its capabilities as coarse-grained MCP tools. This lesson focuses on the philosophies, core abstractions, and production trade-offs that justify these architectural decisions, not just API syntax.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down>
Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

With our capstones providing a concrete goal, we can now examine why framework selection so often fails and what layers of the stack—runtime, protocol, and tooling—solve which problems.

## Framework Choice Under Uncertainty

The AI agent ecosystem is new and evolving quickly. No single framework will satisfy every use case. To choose wisely, you must first distinguish between three layers that are often conflated: the **runtime**, the **protocol**, and the **tooling framework**. Each solves a distinct production problem. The runtime, like LangGraph or CrewAI, provides orchestration and state management for durable execution and resumability. The protocol, like the Model Context Protocol (MCP), standardizes how components connect, preventing tool lock-in and the need to rewrite logic for different systems. The tooling framework, like FastMCP, provides the scaffolding for building and deploying these components, handling transports, authentication, and developer experience.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down>
Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

Engineers who select frameworks based on hype cycles or simple "hello, world" demos often run into trouble. One common failure mode is choosing a lightweight framework for a task that requires high reliability. The initial prototype works, but it lacks the primitives for durable execution, checkpointing, or human-in-the-loop interventions, leading to a brittle system that cannot recover from failures in production. Conversely, choosing a complex, graph-based framework for a highly exploratory task can introduce unnecessary overhead, slowing down iteration cycles. Interactive workloads, where the path to a solution is unknown, require different tools than deterministic workloads, which follow a predictable and auditable path.

We learned this firsthand. We initially planned to build our research agent with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was the wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes Instead of Brands

To avoid these traps, you need a way to evaluate frameworks based on stable engineering principles. We have identified four decision axes that can help you analyze any library and determine if it fits your project’s needs.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down>
Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

The first axis is **control-flow explicitness versus LLM-driven autonomy**. Graph-based frameworks like LangGraph require you to explicitly define every node and edge, offering clear control over each state transition. This makes them ideal for deterministic, auditable workflows where you need to know precisely why the system made a particular decision. In contrast, lightweight agent loops, like those in the OpenAI Agents SDK, give the LLM more freedom to direct the workflow, favoring exploration and adaptability. This approach is better for tasks where the path to a solution is not known in advance and the agent needs to react dynamically to its environment. The question to ask is: does your application require repeatable, auditable steps, or does it need to navigate an unpredictable environment?

The second axis is **reliability primitives**. Production systems fail. A good framework provides tools to handle those failures gracefully. Features like checkpointing, which saves the agent's state at various points, allow it to resume after a crash. Time-travel replay enables debugging by letting you revisit and alter past states. Human-in-the-loop (HITL) interrupts pause execution to wait for human approval or input. Durable execution ensures that long-running tasks can survive application restarts. These features are non-negotiable for our writing agent but less critical for the research agent. LangGraph emphasizes interrupts and persistence [[7]](https://docs.langchain.com/oss/python/langgraph/persistence), while PydanticAI integrates with systems like Temporal for durable execution [[31]](https://ai.pydantic.dev/durable_execution/overview/).

The third axis is **abstraction level and developer experience**. Some frameworks, like the OpenAI Agents SDK, provide minimal primitives that require more boilerplate code but offer greater flexibility and control. Others, like CrewAI, use opinionated, high-level constructs that accelerate initial development but can reduce adaptability when dealing with edge cases or custom logic.

The fourth axis is **tooling interoperability**. MCP functions as the USB-C equivalent for AI, providing a standard interface for tools. This lets you write tools once as MCP servers (for example, with FastMCP [[16]](https://github.com/PrefectHQ/fastmcp)) and reuse them across runtimes and IDEs speaking the MCP protocol, including LangGraph or the OpenAI Agents SDK, without rewriting.

Our capstone projects map clearly to these axes. The research agent, Nova, requires high autonomy and interoperable tools for its exploratory nature, making a lightweight loop with MCP a good fit. The writing agent, Brown, demands an explicit, auditable workflow with strong reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks.

**LangGraph** is built on a stateful graph model with native checkpoints and interrupts for auditable workflows, making it ideal for processes that need to be resumable and traceable [[7]](https://docs.langchain.com/oss/python/langgraph/persistence), [[59]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). It offers both a declarative graph API for explicit control and a functional API for easier adoption. It has shown strong, consistent daily download activity, averaging 400K–500K downloads per day over the past three months, indicating a stable and active user base.

<aside>
💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers, etc.), **LangGraph** focuses specifically on **structured**, **stateful workflows**. It introduces graph-based execution with checkpoints and resumability, which are features not native to standard LangChain chains.

In short, LangChain is the toolbox, while LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions [[59]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). You will see LangChain code in the writing agent.
</aside>

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down>
Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.

The **OpenAI Agents SDK** has a minimal surface area consisting of agents, tools, guardrails, handoffs, and sessions, favoring lightweight Python-native loops over compiled state machines [[37]](https://openai.github.io/openai-agents-python/). The library has recorded 90K–120K daily downloads over the past three months, with a slight upward trend suggesting steady adoption.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down>
Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.

**AgentKit** is a modular toolkit for building and deploying agents on the OpenAI platform. It unifies a visual builder, connectors (including MCP), a ChatKit for embedding UIs, and evaluation infrastructure, allowing developers to visually compose multi-agent systems and manage them through a full lifecycle [[17]](https://openai.com/index/introducing-agentkit).

<aside>
💡 OpenAI AgentKit vs. OpenAI Agents SDK

The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration and fine-grained control. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK: it adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**. In short, the SDK is the coding foundation, while AgentKit is the integrated platform for design, deployment, and optimization.
</aside>

**CrewAI** features a dual architecture: role-based autonomous crews for collaborative exploration, and event-driven flows for deterministic control. It also offers a strong developer experience with a CLI and YAML-based configuration. Daily downloads for CrewAI range between 40K and 100K, showing solid interest in its role-based approach.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down>
Image 6: Source: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.

**PydanticAI** emphasizes type safety, schema-driven validation, and durable execution through integrations with tools like Temporal, DBOS, and Prefect. Daily downloads have doubled from ~150k in July to 300-450k by October 2025, showing strong growth momentum driven by its focus on reliability.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down>
Image 7: Source: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.

**AutoGen** has a layered approach, with its Studio GUI intended for exploration, feeding into the AgentChat or core libraries for production hardening [[34]](https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness). It is explicitly positioned as a research prototype, not a production-ready tool.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down>
Image 8: Source: pepy.tech, daily downloads for autogen, accessed October 15, 2025.

The **Claude Agent SDK** is a newer entrant from Anthropic. It offers tight integration with the Claude model family, leveraging its strengths in large context and tool use, but currently has a smaller ecosystem.

**FastMCP** is a tooling layer, not a runtime. It lets you build MCP-compliant servers and clients, making your tools portable across any runtime or IDE. It has shown explosive growth, surging from ~250k daily downloads in July to over 1.2M per day in October 2025, a 5x increase reflecting the growing need for interoperability.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down>
Image 9: Source: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.

Adoption metrics like download trends and GitHub stars can serve as a proxy for maturity, helping you gauge hiring risk, ecosystem health, and long-term maintenance burden. However, it is important to avoid single-framework dogma. Hybrid patterns are common, such as using FastMCP tools inside a LangGraph workflow.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down>
Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026.

We will now examine each framework in detail, using our four axes and capstone needs as constant evaluation lenses.

## A Closer Look at LangGraph

LangGraph uses a graph-based model where nodes are Python functions and edges are explicit transitions. This design makes complex, multi-step logic transparent and auditable, which is exactly what we need for our writing agent, Brown. Its core production primitives include interrupts for human-in-the-loop interaction, persistence and checkpointing for resumability, and time-travel debugging, which lets you replay and branch from any prior state. These features are critical for building reliable systems that can be paused, inspected, and corrected by a human operator.

The framework offers two definition styles: a "graph API" for explicit state machines and a decorator-based "functional API" [[43]](https://www.langchain.com/blog/introducing-the-langgraph-functional-api). The functional API lets developers use standard Python control flow, easing adoption. This presents a trade-off: the functional API has a lower learning curve, but the graph API provides a clearer visual representation of the workflow, which aids debugging and collaboration [[44]](https://docs.langchain.com/oss/python/langgraph/choosing-apis).

LangGraph can be overkill for simple, exploratory scripts where a lighter loop is sufficient. The upfront modeling cost is higher than with a simple agent loop. However, for repeatable and auditable processes like our writing agent, this investment is justified. The built-in safety, observability, and durability it provides are essential for preventing brittle failures in production.

Having examined a graph-centric, reliability-first option, we now turn to a deliberately minimal alternative.

## A Closer Look at OpenAI Agents SDK

The OpenAI Agents SDK is designed with a philosophy of minimal primitives, reducing the conceptual surface area while still enabling powerful agentic applications. Its core concepts are simple and intuitive, making it quick to learn for developers familiar with Python.

-   **Agents**: LLMs with instructions and tools for performing tasks [[38]](https://openai.github.io/openai-agents-python/agents).
-   **Tools**: Python functions agents call to interact with external systems.
-   **Guardrails**: Mechanisms for validating agent inputs and outputs to ensure safety and correctness [[40]](https://openai.github.io/openai-agents-python/guardrails).
-   **Handoffs**: A way for agents to delegate tasks to other, more specialized agents [[38]](https://openai.github.io/openai-agents-python/agents).
-   **Sessions**: Automatically manage conversation history across multiple runs.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down>
Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.

The execution model relies on direct Python control flow with `if/else` statements and loops, rather than a compiled state machine like in graph-based systems. This Python-native approach is a key difference from LangGraph's functional API. While both use decorators, LangGraph compiles your code into an explicit, stateful graph that manages execution, persistence, and interruptions. The OpenAI SDK, in contrast, uses a simpler agent loop that you control directly, offering a more flexible but less constrained environment.

This makes the SDK a strong choice for teams that want a fast path to production and prefer lightweight orchestration with sensible defaults. However, this simplicity comes with a trade-off: reliability features like durable pause, resume, and checkpointing are not provided out of the box and must be implemented by the developer.

The natural extension of this minimal SDK is a full-lifecycle platform built on top of it.

## A Closer Look at AgentKit

AgentKit is a complete lifecycle toolkit layered on top of the OpenAI Agents SDK, designed to cover the entire process of agent development, from design and deployment to optimization and continuous improvement. It extends the SDK by adding a visual workflow designer, UI embedding tools, and a comprehensive evaluation infrastructure.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down>
Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.

Its key components include:

-   **Agent Builder**: A visual canvas for designing and versioning multi-agent workflows with drag-and-drop logic, guardrails, and inline evaluation [[18]](https://www.digitalapplied.com/blog/openai-agentkit-complete-guide).
-   **Connector Registry**: A centralized admin panel for managing data connections like Google Drive and third-party MCPs across workspaces [[17]](https://openai.com/index/introducing-agentkit).
-   **ChatKit**: A toolkit for embedding customizable chat UIs into products, handling streaming and theming.
-   **Evals and Reinforcement Fine-Tuning (RFT)**: A suite for measuring, grading, and improving agent performance, creating a continuous improvement feedback loop.

AgentKit sits one layer above the OpenAI Agents SDK. You still use the SDK for code-first orchestration, but AgentKit provides the surrounding tools for design, deployment, and continuous improvement. This visual approach supports the development of safe multi-agent systems at scale without forcing everything into code. AgentKit adds clear value for teams that need no-code workflow design, versioning, and continuous improvement loops.

We now examine a framework whose duality spans both autonomous crews and structured flows.

## A Closer Look at CrewAI

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcc81dc-f35c-4a6b-95e8-557db10090a9/e0cb631a-91ae-46fc-a332-d5e1afd61c80/w=1920,quality=90,fit=scale-down>
Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`.

CrewAI introduces a powerful duality with its two main concepts: **Crews** and **Flows**. This dual architecture allows you to balance autonomy with control, making it a versatile choice for a range of applications [[22]](https://docs.crewai.com/en/introduction).

**Crews** are designed for role-based, autonomous collaboration. You define agents with specific roles, goals, and tools, and they work together to solve a problem, much like a human team. This is ideal for tasks that benefit from multiple specialized perspectives, such as a researcher agent handing off findings to a writer agent. **Flows**, on the other hand, are for event-driven, deterministic orchestration. They give you fine-grained control over the workflow, allowing you to define precise execution paths, manage state, and integrate with external systems. For example, a "research crew" might autonomously gather information, and then a "writing flow" could deterministically take that information through a series of editing, formatting, and approval steps.

A common development pattern with CrewAI is to start with an autonomous crew for rapid prototyping. Once the requirements solidify, you can introduce a flow to add structure and control. This progression allows you to move from exploration to production within the same framework.

CrewAI also has a strong focus on developer experience, with a CLI for scaffolding projects, YAML-based definitions for agents and tasks, and configurable memory and persistence options. Its sweet spot is in multi-agent handoff scenarios where clear role definitions can accelerate development.

## A Closer Look at PydanticAI

PydanticAI is built on a philosophy similar to FastAPI, where Pydantic models and type hints create compile-time contracts between your code and the LLM's behavior. This focus on type safety ensures that the data flowing through your agent system is always structured and validated.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/0454e524-5d87-4288-82d4-3abd2b78a6f2/image/w=1920,quality=90,fit=scale-down>
Image 14: Diagram illustrating PydanticAI's design philosophy.

One of its standout features is its support for **durable execution** through integrations with platforms like Temporal, DBOS, and Prefect [[31]](https://ai.pydantic.dev/durable_execution/overview/). This allows agents to survive restarts, pause for human input, and resume long-running tasks. It also has built-in **graph support** for creating non-linear workflows.

PydanticAI offers several developer experience wins. It automatically generates schemas from type hints and docstrings, and its structured output feature retries automatically on validation failure, reducing boilerplate and increasing reliability [[27]](https://realpython.com/pydantic-ai). The trade-off is the upfront investment in defining schemas, which provides correctness guarantees but can have a learning curve for teams new to strict typing. PydanticAI is best suited for projects where structured data correctness and long-running, resumable tasks are paramount.

We now look at a layered system that explicitly separates experimentation from production hardening.

## A Closer Look at AutoGen

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down>
Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.

AutoGen is designed with a layered architecture that deliberately separates experimentation from production. This allows for a smooth transition from rapid prototyping to building robust, scalable systems.

-   **AutoGen Studio** is a low-code GUI that lets you prototype agent teams and workflows without writing code [[33]](https://ravichaganti.com/blog/getting-started-with-autogen-framework-for-building-ai-agents-and-applications). You can visually compose agents, configure their tools, and test their interactions in an interactive environment.
-   **AgentChat** is a programming framework for building conversational multi-agent applications. It provides a higher-level, task-driven API built on top of the core layer [[34]](https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness).
-   **Core** provides low-level, event-driven primitives for building scalable, custom agent systems [[32]](https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems).

The typical workflow with AutoGen involves exploring and validating ideas visually inside Studio. Once a pattern proves successful, you can harden it into production-ready code using the lower-level AgentChat and Core APIs. It is important to note the explicit disclaimer that Studio is a research prototype and not intended for production environments.

AutoGen's strength lies in its ability to serve as an R&D laboratory for discovering effective multi-agent conversation patterns and termination conditions. The trade-off is that this flexibility during exploration means that the development team is responsible for re-implementing reliability, security, and observability when moving to production.

A newer entrant focuses on tight model-family integration.

## A Closer Look at Claude Agent SDK

The Claude Agent SDK from Anthropic is built for tight integration with its model family, leveraging Claude's strengths in large context, reasoning, and tool use. It provides an ergonomic tool-calling and orchestration experience tailored to Anthropic's models [[11]](https://www.mindstudio.ai/blog/agent-sdk-vs-framework-claude-pydantic-ai). As a newer framework, it has a smaller community, fewer integrations, and a rapidly evolving API.

This presents a trade-off: early adoption can yield model-optimized performance, but this must be balanced against ecosystem maturity. The clearest use case is for teams already committed to the Anthropic stack who want native performance and accept the smaller community support.

The final examination covers a non-runtime layer that complements every option above.

## A Closer Look at FastMCP

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/745828fd-27e2-4a50-b613-7275a1e1dceb/image/w=1920,quality=90,fit=scale-down>
Image 16: FastMCP Architecture and Interoperability

FastMCP is not a runtime but a tooling framework for building applications using the Model Context Protocol (MCP). It lets you create MCP-compliant servers and clients, making tools and prompts portable across any runtime or IDE that speaks the protocol. Its key benefit is interoperability: write a tool once and reuse it in LangGraph, the OpenAI SDK, or any future compatible system [[14]](https://generect.com/blog/langgraph-mcp). This decoupling ensures your investment in tools is not tied to a single framework's lifecycle.

Beyond the protocol, FastMCP offers production features like authentication, server composition, and cloud deployment. For our capstones, we will implement the research agent, Nova, as a FastMCP server. The writing agent, Brown, will expose its workflows as coarse-grained MCP tools.

The developer experience is simple and Pythonic. A single decorator exposes a function as a tool, while FastMCP handles schema generation and transport.

1.  Here is a quick example from the official documentation [[63]](https://gofastmcp.com/getting-started/quickstart).

    ```python
    from fastmcp import FastMCP
    
    mcp = FastMCP("My MCP Server")
    
    @mcp.tool
    def greet(name: str) -> str:
        return f"Hello, {name}!"
    
    if __name__ == "__main__":
        mcp.run()
    ```

<aside>
💡 **Pattern: tools-as-workflows (Brown)**

For our writing agent (Brown), we wrap each workflow entry point as a **coarse-grained MCP tool** (e.g., `generate_article`, `edit_article`, `edit_selected_text`). The MCP tool handler simply **kicks off the corresponding LangGraph run**, returns progress/messages, and finally yields artifacts and diffs. This gives you MCP portability (Cursor, Claude Code) **without** losing LangGraph’s durability and auditability. You’ll learn more about this in the later lessons.
</aside>

With our examinations complete, we can now synthesize everything into a decision matrix and tentative forecasts.

## Choosing for Your Project: Decision Matrix & Tentative Forecasts

To help you choose the right framework for your project, we have created a decision matrix that maps common project needs to the relative strengths of each framework.

Table 1: Decision matrix comparing AI agent frameworks against common needs

| Feature | LangGraph | PydanticAI | OpenAI SDK | AgentKit | CrewAI | AutoGen | FastMCP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Durability/HITL/Replay** | ✅ | | | | | ✅ | |
| **Typed Contracts + Durable Execution** | | ✅ | | | | | ✅ |
| **Few Primitives + Guardrails/Handoffs** | ✅ | | ✅ | ✅ | | | ✅ |
| **Role-based Teams + Quick Scaffolding** | | | | ✅ | ✅ | ✅ | |
| **Exploration Lab** | | | ✅ | ✅ | ✅ | ✅ | |
| **Tool Portability Across Stacks** | | ✅ | | ✅ | | | ✅ |

It is important to treat this matrix as a snapshot in time. The agent ecosystem is constantly evolving, so you should re-evaluate frameworks against the four decision axes whenever a library releases a major update.

Based on these axes, we can offer some forecasts. LangGraph and PydanticAI are strong choices for reliability-heavy workflows that require auditability and durable execution. The OpenAI Agents SDK is well-suited for applications that need lightweight simplicity, while AgentKit is the right choice when visual design and continuous evaluation loops are required. CrewAI excels at rapid multi-agent prototyping, AutoGen serves as a powerful R&D starting point, and FastMCP is emerging as the universal tooling substrate that connects them all.

In practice, hybrid patterns are common. You might consume FastMCP tools inside a LangGraph workflow, migrate from an AutoGen Studio prototype to a hardened runtime, or expose a complex graph as a single MCP command to gain IDE portability without sacrificing durability.

To make this theory concrete, we now share the actual pivots we made while building the course capstones.

## Our Capstone Pivots

Let’s apply this matrix to our capstone project. Our decision-making process evolved as we built, highlighting the importance of choosing the right tool for the job.

Our initial plan was to use LangGraph for both agents. However, we quickly discovered that the research agent, Nova, required a high degree of interactivity and divergent exploration. A rigid graph structure proved to be too cumbersome for this task. Every new research path or ad-hoc tool call would have required modifying the graph definition, which slowed down the iterative process of exploration. We found that flexible MCP tools were a much better fit, allowing us to pivot and replan on the fly.

The writing agent, Brown, had the opposite requirements. Its process needed to be repeatable and auditable, which made LangGraph’s features like checkpoints, HITL interrupts, and time-travel replay essential. LangGraph's checkpoints allowed us to pause the writing process, get human feedback on a draft, and resume from that exact point, ensuring a fully auditable and collaborative workflow.

The result is a hybrid architecture. Nova is implemented as a FastMCP server that can be steered by any client, including IDEs. Brown is a LangGraph workflow whose entry points are exposed as coarse-grained MCP tools. This gives us an emergent pattern: we can wrap complex internal workflows behind single MCP commands to gain portability without sacrificing durability or auditability. Brown currently exposes three tools: `generate_article`, `edit_article`, and `edit_selected_text`.

We considered the OpenAI Agents SDK, but ultimately deprioritized it because it lacked the first-class persistence and deep MCP integration required for the long-running nature of both capstone tasks. These real-world pivots illustrate the central lesson of the entire module.

## Conclusion

The core takeaway from this lesson is to prioritize stable engineering concepts over transient brand names. When choosing a framework, focus on stateful graphs, typed contracts, durable execution, and standardization through protocols like MCP. These principles will serve you well, even as the landscape of specific libraries continues to change.

Investing time to understand the MCP specification itself is a valuable activity. It is a one-time investment that can yield tool portability across every current and future stack that supports it. A practical selection process should start with applying the four decision axes to your project's needs. Begin with the smallest viable stack that meets your reliability requirements and keep all your tooling portable via MCP. For example, you could begin exploration in AutoGen Studio, extract successful patterns into FastMCP tools, and then anchor your production system in a robust runtime like LangGraph or PydanticAI.

This process is exactly how we arrived at the hybrid FastMCP-plus-LangGraph stack for our capstones. In the next lesson, we will cover system design, including model selection, cost and latency trade-offs, and HITL placement. After that, we will begin the hands-on builds. You will build these systems hands-on: **Nova** with **FastMCP**, implementing the server/client architecture, data ingestion, and Perplexity-driven research loops; and **Brown** with a **LangGraph and FastMCP** hybrid, building the stateful workflow, using context engineering for profiles, implementing evaluator-optimizer cycles, and enabling HITL editing.

## References

- [1] LLM-Driven Autonomy (https://www.emergentmind.com/topics/llm-driven-autonomy)
- [2] ControlFlow 0.9: Take Control of Your Agents (https://www.prefect.io/blog/controlflow-0-9-take-control-of-your-agents)
- [3] General-purpose systems (https://arxiv.org/html/2508.17281v2)
- [4] Agentic UAVs Framework (https://arxiv.org/html/2509.13352v2)
- [5] Agent Frameworks (https://arize.com/ai-agents/agent-frameworks)
- [6] interrupt (https://reference.langchain.com/python/langgraph/types/interrupt)
- [7] Persistence (https://docs.langchain.com/oss/python/langgraph/persistence)
- [8] Interrupts (https://docs.langchain.com/oss/javascript/langgraph/interrupts)
- [9] Claude Agent SDK (https://www.morphllm.com/ai-agent-framework)
- [10] Building Intelligent Agents with Claude Agent SDK (https://www.c-sharpcorner.com/article/building-intelligent-agents-with-claude-agent-sdk-features-comparisons-and-be)
- [11] Agent SDK vs Framework (https://www.mindstudio.ai/blog/agent-sdk-vs-framework-claude-pydantic-ai)
- [12] Inside the Claude Agent SDK (https://buildwithaws.substack.com/p/inside-the-claude-agent-sdk-from)
- [13] Claude Agent SDK: Building Agents That Work (https://aankitroy.com/blog/claude-agent-sdk-building-agents-that-work)
- [14] LangGraph and MCP (https://generect.com/blog/langgraph-mcp)
- [15] Tools (https://gofastmcp.com/servers/tools)
- [16] FastMCP GitHub (https://github.com/PrefectHQ/fastmcp)
- [17] Introducing AgentKit (https://openai.com/index/introducing-agentkit)
- [18] OpenAI AgentKit Complete Guide (https://www.digitalapplied.com/blog/openai-agentkit-complete-guide)
- [19] OpenAI AgentKit and Agent Builder (https://www.nudgesecurity.com/post/openai-agentkit-and-agent-builder-building-secure-ai-agents)
- [20] OpenAI's AgentKit Review (https://medium.com/@leucopsis/openais-agentkit-review-c83bee3c3d02)
- [21] OpenAI Agent Builder Step-by-Step Guide (https://composio.dev/content/openai-agent-builder-step-by-step-guide-to-building-ai-agents-with-mcp)
- [22] Introduction (https://docs.crewai.com/en/introduction)
- [23] What are Crews vs. Flows in CrewAI (https://www.c-sharpcorner.com/article/what-are-crews-vs-flows-in-crewai)
- [24] CrewAI Unique Features (https://vadim.blog/crewai-unique-features)
- [25] CrewAI GitHub (https://github.com/crewaiinc/crewai)
- [26] Flows (https://docs.crewai.com/en/concepts/flows)
- [27] Pydantic AI (https://realpython.com/pydantic-ai)
- [28] Complete Guide to Pydantic for Validating LLM Outputs (https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs)
- [29] Intro to Pydantic (https://education.molssi.org/type-hints-pydantic-tutorial/chapters/IntroToPydantic.html)
- [30] Validators (https://pydantic.dev/docs/validation/latest/concepts/validators)
- [31] Durable Execution (https://ai.pydantic.dev/durable_execution/overview/)
- [32] Microsoft AutoGen: Orchestrating Multi-Agent LLM Systems (https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems)
- [33] Getting Started with AutoGen Framework (https://ravichaganti.com/blog/getting-started-with-autogen-framework-for-building-ai-agents-and-applications)
- [34] AutoGen v0.4 (https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness)
- [35] AutoGen (https://www.ibm.com/think/topics/autogen)
- [36] A Friendly Introduction to the AutoGen (https://newsletter.victordibia.com/p/a-friendly-introduction-to-the-autogen)
- [37] OpenAI Agents SDK (https://openai.github.io/openai-agents-python/)
- [38] Agents (https://openai.github.io/openai-agents-python/agents)
- [39] Migrating from OpenAI Agents SDK (https://platform.claude.com/cookbook/claude-agent-sdk-04-migrating-from-openai-agents-sdk)
- [40] Guardrails (https://openai.github.io/openai-agents-python/guardrails)
- [41] Agents Guide (https://developers.openai.com/api/docs/guides/agents)
- [42] Choosing Between Graph and Functional APIs (https://www.linkedin.com/posts/khalid-husain-3002aa216_choosing-between-graph-and-functional-apis-activity-7396757303217029120-VIK3)
- [43] Introducing the LangGraph Functional API (https://www.langchain.com/blog/introducing-the-langgraph-functional-api)
- [44] Choosing APIs (https://docs.langchain.com/oss/python/langgraph/choosing-apis)
- [45] Functional API for LangGraph (https://changelog.langchain.com/announcements/functional-api-for-langgraph)
- [46] Agent Framework Layers (https://www.linkedin.com/posts/brijpandeyji_most-people-still-lump-everything-into-agent-activity-7409465945489829888-8sk5)
- [47] Agent Runtime Infrastructure Layer (https://www.augmentcode.com/guides/agent-runtime-infrastructure-layer)
- [48] AI Agent Runtime (https://www.guild.ai/glossary/ai-agent-runtime)
- [49] The Emerging AI Agent Stack (https://forum.langchain.com/t/what-does-the-emerging-ai-agent-stack-actually-look-like/3103)
- [50] AI Agent Frameworks (https://www.langchain.com/resources/ai-agent-frameworks)
- [51] How to think about agent frameworks (https://www.langchain.com/blog/how-to-think-about-agent-frameworks)
- [52] A Developer's Guide to Agentic Frameworks in 2026 (https://pub.towardsai.net/a-developers-guide-to-agentic-frameworks-in-2026-3f22a492dc3d)
- [53] The AI Agent Star Race (https://medium.com/@rosgluk/the-ai-agent-star-race-i-pulled-live-github-data-for-20-frameworks-in-may-2026-b4919dfba5e4)
- [54] Top 10 Most Starred AI Agent Frameworks on GitHub 2026 (https://techwithibrahim.medium.com/top-10-most-starred-ai-agent-frameworks-on-github-2026-df6e760a950b)
- [55] Stack Overflow Analysis of Agent Frameworks (https://arxiv.org/html/2510.25423v2)
- [56] AI Agent Frameworks Download Spikes (https://www.youtube.com/watch?v=2Yg-BPFNF5A&vl=en-US)
- [57] LangChain vs. LangGraph (https://www.truefoundry.com/blog/langchain-vs-langgraph)
- [58] LangChain vs. LangGraph (https://duplocloud.com/blog/langchain-vs-langgraph)
- [59] Workflows and agents (https://docs.langchain.com/oss/python/langgraph/workflows-agents)
- [60] LangChain vs. LangGraph (https://www.geeksforgeeks.org/artificial-intelligence/langchain-vs-langgraph)
- [61] LangChain vs. LangGraph (https://milvus.io/blog/langchain-vs-langgraph.md)
- [62] Build your first Flow (https://docs.crewai.com/guides/flows/first-flow)
- [63] Quickstart (https://gofastmcp.com/getting-started/quickstart)
- [64] AutoGen Studio User Guide (https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- [65] AutoGen (https://microsoft.github.io/autogen/stable/)