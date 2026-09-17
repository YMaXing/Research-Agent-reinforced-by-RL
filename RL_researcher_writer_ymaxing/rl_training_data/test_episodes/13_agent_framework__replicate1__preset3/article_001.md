# Lesson 13: How to Choose an AI Agent Framework

In our last lesson, we introduced the scope and design of our central project: a system of two specialized agents. Nova, an adaptable and interactive research agent, and Brown, a reliable and auditable writing agent. This lesson tackles the next critical decision: choosing the right framework to build them.

The wrong choice can lead to brittle abstractions that break under real-world load, stalled progress in a fast-moving ecosystem, or hidden gaps in durability that only appear after weeks of investment. To navigate this, we will focus on two core concepts that recur throughout this lesson. The first is LangGraph's interrupts and checkpoints, which provide the resumable auditability needed for our writing agent. The second is the Model Context Protocol (MCP), a universal interoperability layer that keeps our tools portable, a key requirement for our research agent.

Our high-level architecture, shown in Image 1, will serve as a consistent reference point. The research agent, Nova, is built as a lightweight MCP server that any client can steer, while the writing agent, Brown, is a durable workflow that exposes its capabilities as coarse-grained MCP tools. This lesson will focus on the philosophies, core abstractions, and production trade-offs that led us to this design, providing you with the principles to make your own informed decisions.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down>
Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

With our capstones as a concrete reference, let's examine why framework selection under uncertainty so often fails in production and what layers—runtime, protocol, and tooling—actually solve which problems.

## Framework Choice Under Uncertainty

The AI agent ecosystem is new and evolving quickly, and no universal framework will satisfy every use case. To make a sound choice, you must distinguish between three layers that are frequently conflated: the runtime, the protocol, and the tooling framework.

Each layer solves a distinct production problem. The **runtime** (e.g., LangGraph, CrewAI, PydanticAI) provides the orchestration and state management needed for durable execution and resumability. The **protocol**, like MCP, is a standard that prevents tool lock-in by ensuring your tools are portable across different runtimes. Finally, the **tooling framework** (e.g., FastMCP) provides the scaffolding for implementing the protocol, offering ready-to-deploy transports, authentication, and a better developer experience. While MCP is the most adopted standard for tool use, it is part of a broader landscape of emerging interoperability protocols, including Agent-to-Agent (A2A) and Agent Communication (ACP) protocols, which standardize how agents discover and delegate tasks [[11]](https://arxiv.org/html/2505.02279v1).

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down>
Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

Engineers often select frameworks based on hype or simple demos, which leads to common failures. A framework that seems easy for a "hello world" example may lack the reliability primitives needed for production workloads, leading to data loss or unrecoverable states when an agent crashes. Conversely, a complex framework can introduce unnecessary overhead and latency for exploratory work where speed of iteration is more important than perfect durability. This distinction between interactive and deterministic workloads is a good initial lens for assessing a framework's fit.

We learned this firsthand. We initially planned to build our research agent with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was a wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes Instead of Brands

To avoid these traps, you need a way to evaluate frameworks based on principles. We use four decision axes to analyze any library and determine if it fits a project’s needs.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down>
Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

**Control-flow explicitness versus LLM-driven autonomy** is the first axis. Graph-based frameworks like LangGraph offer determinism through explicit nodes and edges, delivering auditability and control over every state transition. This is ideal for workflows where you need to know precisely why the system made a particular decision. In contrast, lightweight agent loops, like those in the OpenAI Agents SDK, favor exploration and adaptability, which is better for tasks where the path to a solution is not known in advance. The question to ask is: does your application require repeatable, auditable steps, or does it need to navigate an unpredictable environment? This is not just a technical trade-off. Emerging regulations like the EU AI Act and enterprise governance frameworks increasingly require auditable decision chains for high-risk use cases, making explicit workflows a prerequisite for safe deployment in many industries [[12]](https://www.nice.com/agentic-ai/agentic-ai-governance-frameworks), [[13]](https://vegavid.com/ai-agents-for-compliance-and-risk-management).

**Reliability primitives** form the second axis. A good framework provides tools to handle failures gracefully. Features like checkpointing, time-travel replay, human-in-the-loop (HITL) interrupts, and durable execution across restarts are essential for our writing agent but less critical for the research agent. LangGraph emphasizes interrupts and persistence, while PydanticAI integrates with systems like Temporal and DBOS for durable execution [[1]](https://docs.langchain.com/oss/python/langgraph/persistence), [[2]](https://ai.pydantic.dev/durable_execution/overview/).

**Abstraction level and developer experience** is the third axis. Some frameworks, like the OpenAI Agents SDK, provide minimal primitives, requiring more boilerplate but delivering flexibility. Others, like CrewAI, offer opinionated constructs that accelerate initial development but may reduce adaptability later on.

**Tooling interoperability** is the final axis. MCP functions as the USB-C of AI, providing a standard interface for tools. It lets you write tools once as MCP servers, for example, with FastMCP, and reuse them across runtimes like LangGraph, the OpenAI Agents SDK, or even IDEs like Cursor, without rewriting them [[3]](https://gofastmcp.com/).

Our capstone projects map clearly to these axes. The research agent requires autonomy and interoperable tools for its exploratory nature, making a lightweight loop with MCP a good fit. The writing agent demands an explicit, auditable workflow with reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks.

**LangGraph** is built on a stateful graph model with native checkpoints and interrupts, making it ideal for auditable and resumable workflows. Its design is particularly suited for processes that need to be traceable and recoverable, which is why we chose it for our writing agent. Its daily download activity is strong and consistent, averaging around 400K–500K downloads per day over the past three months, indicating a healthy and active user base [[1]](https://docs.langchain.com/oss/python/langgraph/persistence), [[4]](https://docs.langchain.com/oss/python/langgraph/workflows-agents).

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down>
Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.

<aside>
💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers, etc.), **LangGraph** focuses specifically on **structured**, **stateful workflows**. It introduces graph-based execution with checkpoints and resumability, which are features not native to standard LangChain chains.

In short, LangChain is the toolbox, while LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions. You will see LangChain code in the writing agent [[4]](https://docs.langchain.com/oss/python/langgraph/workflows-agents).
</aside>

The **OpenAI Agents SDK** has a minimal surface area consisting of agents, tools, guardrails, handoffs, and sessions, favoring lightweight Python-native loops over compiled state machines. This makes it quick to learn and easy to integrate into existing Python applications. The library has recorded 90K–120K daily downloads over the past three months, with a slight upward trend, suggesting steady adoption for projects that align with its philosophy [[5]](https://openai.github.io/openai-agents-python/).

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down>
Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.

**AgentKit** is a modular toolkit for building, deploying, and optimizing agents across the OpenAI platform. It unifies a visual builder, connectors (including MCP), ChatKit for embedding, and evaluation infrastructure. Developers can visually compose multi-agent systems, manage connectors, and embed chat-based experiences directly in their products, all backed by versioning, guardrails, and evaluation tools for safe, reliable deployment.

<aside>
💡 OpenAI AgentKit vs. OpenAI Agents SDK

The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration and fine-grained control. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK: it adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**. In short, the SDK is the coding foundation, while AgentKit is the integrated platform for design, deployment, and optimization.
</aside>

**CrewAI** features a dual architecture: role-based autonomous crews for collaborative exploration versus event-driven flows for deterministic control. This allows developers to start with flexible, autonomous agents and gradually add structure as the application matures. Its daily downloads range between 40K and 100K, reflecting its popularity for multi-agent systems [[6]](https://docs.crewai.com/introduction).

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down>
Image 6: Source: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.

**PydanticAI** emphasizes type safety, schema-driven validation, and durable execution through integrations with platforms like Temporal, DBOS, and Prefect, along with built-in graph support. This focus on reliability and correctness has driven strong adoption. Daily downloads of Pydantic-AI doubled from ~150k in July to 300-450k by October 2025.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down>
Image 7: Source: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.

**AutoGen** uses a layered approach, with its Studio GUI positioned for exploration and not production, feeding ideas into its AgentChat or core libraries for hardening. This makes it a powerful tool for research and prototyping multi-agent conversational patterns [[7]](https://microsoft.github.io/autogen/stable/).

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down>
Image 8: Source: pepy.tech, daily downloads for autogen, accessed October 15, 2025.

The **Claude Agent SDK** is a newer entrant from Anthropic, offering tight integration that leverages the Claude model family's strengths in large context and low-level tool use, but with a smaller ecosystem.

**FastMCP** is a non-runtime tooling layer that lets you build MCP-compliant servers and clients, making tools portable across any runtime or IDE. It has shown rapid growth, with daily downloads surging from ~250k in July to over 1.2M per day in October 2025.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down>
Image 9: Source: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.

Adoption metrics like download trends and GitHub stars can be a proxy for maturity, helping you gauge hiring risk, ecosystem health, and long-term maintenance burden. However, it's important to avoid single-framework dogma. Hybrid patterns are common, such as consuming FastMCP tools inside LangGraph or migrating from AutoGen prototypes to hardened runtimes.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down>
Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026.

We will now deep-dive into each framework, using our four axes and capstone needs as constant evaluation lenses.

## Framework Deep Dive: LangGraph

LangGraph uses a graph-based model where nodes are Python functions and edges are explicit transitions, making complex, multi-step logic transparent and auditable. Its core production primitives include interrupts for human-in-the-loop, persistence and checkpointing for resumability, and time-travel debugging that lets you replay and branch from any prior state. This time-travel capability transforms a transient execution into a replayable state machine. By capturing each state transition, LangGraph creates a complete, deterministic audit trail. This allows you to trace failures to specific nodes, inspect intermediate state, and re-execute a workflow from any previous checkpoint without rerunning the entire process [[14]](https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171).

The framework offers two definition styles: a "graph API" for fully explicit graphs and a "functional API" that is decorator-based. This presents a trade-off between the learning curve and the payoff in determinism. The functional API is easier to adopt for existing procedural code, as it allows you to use standard loops and conditionals, but the graph API provides clearer visualization and more granular control over state and time-travel checkpoints [[22]](https://blog.langchain.com/introducing-the-langgraph-functional-api).

LangGraph is overkill for simple, exploratory scripts where lighter loops are more efficient. However, for repeatable, auditable processes like our writing agent, the investment in modeling is justified. Compared to lighter, autonomous loops, LangGraph has a steeper upfront modeling cost but provides built-in safety, observability, and durability that prevent brittle production failures. This makes it a strong choice for enterprise-grade applications where reliability is a primary concern.

Having examined a graph-centric, reliability-first option, we now turn to a deliberately minimal alternative.

## Framework Deep Dive: OpenAI Agents SDK

The OpenAI Agents SDK is designed with a philosophy of minimal primitives, reducing the conceptual surface area while still enabling powerful agentic applications. Its core concepts are simple and interrelated.

-   **Agents**: LLMs equipped with instructions and tools.
-   **Tools**: Python functions that agents can call to interact with the outside world.
-   **Guardrails**: Mechanisms for validating agent inputs and outputs to ensure safety and correctness.
-   **Handoffs**: A way for agents to delegate tasks to other, more specialized agents.
-   **Sessions**: Automatically manage conversation history across multiple runs.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down>
Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.

The execution model is based on direct Python control flow with `if/else` statements and loops, contrasting with the compiled state machines of graph systems. The key difference between the OpenAI Agents SDK and LangGraph’s functional API lies in this execution model. The OpenAI SDK uses a simple, Python-native agent loop that you control directly. Orchestration is handled with standard Python code. In contrast, even with its decorator-based functional API, LangGraph compiles your code into an explicit, stateful graph. This underlying state machine manages execution, persistence, and interruptions, providing a more robust but also more constrained environment.

The SDK is a strong choice for teams that want a fast path to production when lightweight orchestration and sensible defaults are preferred. However, this comes with a reliability trade-off. Without a native durability layer, if an agent crashes mid-task, all progress is lost. Features like durable pause, resume, and checkpointing are not provided out of the box and must be implemented by the team, often by integrating an external runtime [[15]](https://www.diagrid.io/solutions/openai-agents-production), [[16]](https://www.zenml.io/blog/openai-agents-sdk-durable-runtime).

The natural extension of this minimal SDK is a full-lifecycle platform built on top of it.

## Framework Deep Dive: AgentKit

AgentKit is a complete lifecycle toolkit layered on the OpenAI Agents SDK, covering design, deployment, optimization, and continuous improvement. It extends the SDK by adding visual workflow design, UI embedding, and evaluation infrastructure.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down>
Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.

Its key components provide an end-to-end solution for agent development:

-   **Agent Builder**: A drag-and-drop canvas for designing and versioning multi-agent workflows. It allows builders to compose logic visually, add guardrails, and run preview tests with inline evaluation and version control.
-   **Connector Registry**: A centralized interface for managing data connections like Dropbox, Google Drive, and third-party MCPs across workspaces.
-   **ChatKit**: A toolkit for embedding agentic chat UIs directly into web or mobile products, handling streaming, conversation threads, and custom theming.
-   **Evals and Reinforcement Fine-Tuning (RFT)**: Expanded capabilities for measuring, grading, and improving agent performance, including datasets, automated prompt optimization, and custom graders.

AgentKit sits one layer above the OpenAI Agents SDK. You still use the SDK for code-first orchestration, but AgentKit provides the surrounding tools for design, deployment, and continuous improvement. This visual composition and built-in evaluation support safe multi-agent systems at scale without forcing everything into code. The trade-off is that it is strongest when staying inside the OpenAI stack. While its growing MCP connector support improves interoperability, it also introduces security risks, as third-party MCP servers can be a vector for tool poisoning or data leakage if not properly vetted [[17]](https://labs.zenity.io/p/analyzing-the-security-risks-of-openai-s-agentkit). AgentKit adds clear value over the raw SDK for teams that need no-code workflow design, versioning, and continuous improvement loops.

We now examine a framework whose duality spans both autonomous crews and structured flows.

## Framework Deep Dive: CrewAI

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcc81dc-f35c-4a6b-95e8-557db10090a9/e0cb631a-91ae-46fc-a332-d5e1afd61c80/w=1920,quality=90,fit=scale-down>
Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`.

CrewAI introduces a powerful duality with its two main concepts: **Crews** and **Flows**. This dual architecture lets you start with an autonomous crew for rapid prototyping, then introduce a flow to add structure and control as your requirements become more defined [[8]](https://docs.crewai.com/guides/flows/first-flow).

-   **Crews** are for role-based, autonomous collaboration. You define agents with specific roles, goals, and tools, and they work together to solve a problem, much like a human team. This role-based, collaborative model is heavily influenced by research in multi-agent systems (MAS) for robotics, where distinct agents are assigned to specific functional modules (e.g., one per robotic arm) and coordinate through communication to achieve a collective goal [[18]](https://openaccess.thecvf.com/content/CVPR2025W/MEIS/papers/Chen_Multi-Agent_Systems_for_Robotic_Autonomy_with_LLMs_CVPRW_2025_paper.pdf).
-   **Flows** are for event-driven, deterministic orchestration. They give you fine-grained control over the workflow, allowing you to define precise execution paths.

This approach often follows a natural progression: you can begin with autonomous crews for rapid prototyping and then layer on flows for structure once the requirements solidify. CrewAI has a strong focus on developer experience, with CLI scaffolding, YAML definitions for agents and tasks, and configurable memory and persistence options. It shines in multi-agent handoff scenarios, like a researcher-to-writer workflow, where role clarity accelerates development. The trade-off is that its opinionated constructs, while speeding up initial velocity, can lead to configuration overhead and reduced flexibility when edge cases appear.

Another framework approaches the problem through the lens of type safety and compile-time contracts.

## Framework Deep Dive: PydanticAI

PydanticAI’s philosophy is similar to FastAPI, where Pydantic models and type hints create compile-time contracts between your code and the LLM's behavior. This focus on type safety ensures that data flowing through your agentic system is always valid and predictable.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/0454e524-5d87-4288-82d4-3abd2b78a6f2/image/w=1920,quality=90,fit=scale-down>
Image 14: Diagram illustrating PydanticAI's design philosophy.

It comes with strong production features, including **durable execution integrations** with platforms like Temporal, DBOS, or Prefect. This allows agents to survive restarts, pause for human input, and resume long-running tasks, with each tool call potentially backed by a fault-tolerant workflow that provides retries and a full audit history [[19]](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal). It also has built-in **graph support** for non-linear flows. The developer experience is enhanced by automatic schema generation from type hints and docstrings, and structured output with automatic retries on validation failure.

The main trade-off is the up-front investment in defining schemas. While this can be a learning curve for teams new to strict typing, it provides strong correctness guarantees. PydanticAI is best suited for projects where structured data correctness and long-running, resumable tasks are paramount, which aligns well with our writing agent’s auditability needs.

We now look at a layered system explicitly separating experimentation from production hardening.

## Framework Deep Dive: AutoGen

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down>
Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.

AutoGen features a layered design that deliberately separates experimentation from production. It offers multiple entry points depending on your needs, allowing for a gradual increase in complexity and control [[7]](https://microsoft.github.io/autogen/stable/):

-   **AutoGen Studio** is a low-code GUI that lets you prototype agent teams and workflows without writing code. You can visually compose agents, configure their tools, and test their interactions.
-   **AgentChat** is a programming framework for building conversational multi-agent applications. Its use of a supervisor to direct specialized workers reflects centralized coordination patterns from multi-agent systems research in fields like robotics [[20]](https://xue-guang.com/post/llm-marl).
-   **Core** provides low-level, event-driven primitives for building scalable, custom agent systems.

The typical workflow involves exploring and validating ideas visually inside Studio, then hardening the successful patterns into code using the lower layers. It is important to note the official disclaimer that Studio is a research prototype and not intended for production use [[9]](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html).

AutoGen's strength lies in its use as an R&D laboratory for discovering multi-agent conversation patterns and effective termination conditions. The trade-off is that its high flexibility during exploration requires the team to re-implement reliability, security, and observability when moving to production.

A newer entrant focuses on tight model-family integration.

## Framework Deep Dive: Claude Agent SDK

The Claude Agent SDK is built on a philosophy of tight integration that leverages the strengths of the Claude model family: large context windows, strong reasoning, and fine-grained control over tool use. It focuses on providing an ergonomic tool-calling and orchestration experience tailored specifically to Anthropic models.

As a newer entrant, its trade-offs include a smaller community, fewer third-party integrations, and a rapidly evolving API surface. This presents both an opportunity and a risk. Early adoption can yield model-optimized performance, but teams must balance this against the maturity of the ecosystem. The clearest use case is for teams already committed to the Anthropic stack who want native performance and are willing to accept smaller community support.

The final deep dive examines a non-runtime layer that complements every option above.

## Framework Deep Dive: FastMCP

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/745828fd-27e2-4a50-b613-7275a1e1dceb/image/w=1920,quality=90,fit=scale-down>
Image 16: FastMCP Architecture and Interoperability

FastMCP is not a runtime; it is a tooling framework that lets you build MCP-compliant servers and clients. This makes your tools, resources, and prompts portable across any runtime or IDE that speaks the protocol. The key interoperability benefit is that you can write a tool once and reuse it inside LangGraph, the OpenAI SDK, Cursor, Claude Code, or any future compatible system.

Beyond the protocol itself, FastMCP offers production extensions for authentication, server composition, and cloud deployment. These extensions are critical for addressing common MCP failure modes at scale, such as concurrency hangs, large tool responses overflowing context windows, and timeouts under heavy load [[21]](https://arxiv.org/html/2603.05637v1). Our capstone projects use this pattern: the research agent, Nova, is implemented as a FastMCP server that any client can steer, while the writing agent, Brown, exposes its complex workflows as coarse-grained MCP tools.

<aside>
💡 **Pattern: tools-as-workflows (Brown)**

For our writing agent (Brown), we wrap each workflow entry point as a **coarse-grained MCP tool** (e.g., `generate_article`, `edit_article`, `edit_selected_text`). The MCP tool handler simply **kicks off the corresponding LangGraph run**, returns progress and messages, and finally yields artifacts and diffs. This gives you MCP portability (Cursor, Claude Code) **without** losing LangGraph’s durability and auditability. You’ll learn more about this in later lessons.
</aside>

FastMCP offers a simple, Pythonic developer experience. You can expose a function as a tool with a single decorator, and FastMCP handles the schema generation and transport details for you [[10]](https://gofastmcp.com/getting-started/quickstart).

1.  Here is a quick example from the official docs.
    ```python
    from fastmcp import FastMCP
    
    mcp = FastMCP("My MCP Server")
    
    @mcp.tool
    def greet(name: str) -> str:
        return f"Hello, {name}!"
    
    if __name__ == "__main__":
        mcp.run()
    ```

With our deep dives complete, we can now synthesize everything into a decision matrix and tentative forecasts.

## Choosing for Your Project: Decision Matrix & Tentative Forecasts

The following decision matrix maps common project needs to the relative strengths of each framework.

Table 1: Decision matrix comparing AI agent frameworks against common needs

| Feature | LangGraph | PydanticAI | OpenAI SDK | AgentKit | CrewAI | AutoGen | FastMCP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Durability/HITL/Replay** | ✅ | | | | | ✅ | |
| **Typed Contracts + Durable Execution** | | ✅ | | | | | ✅ |
| **Few Primitives + Guardrails/Handoffs** | ✅ | | ✅ | ✅ | | | ✅ |
| **Role-based Teams + Quick Scaffolding** | | | | ✅ | ✅ | ✅ | |
| **Exploration Lab** | | | ✅ | ✅ | ✅ | ✅ | |
| **Tool Portability Across Stacks** | | ✅ | | ✅ | | | ✅ |

Treat this matrix as a snapshot. The ecosystem is evolving, so you should always re-evaluate new libraries against the four decision axes.

Based on these axes, we can make some tentative forecasts. LangGraph and PydanticAI are well-suited for reliability-heavy workflows where auditability and durable execution are key. The OpenAI Agents SDK is a good choice for lightweight simplicity, while AgentKit is better when visual design and continuous evaluation loops are required. CrewAI is ideal for rapid multi-agent prototyping, AutoGen is a strong starting point for R&D, and FastMCP serves as the universal tooling substrate.

In practice, hybrid patterns are common. You might consume FastMCP tools inside LangGraph workflows, migrate from AutoGen Studio prototypes to hardened runtimes, or expose complex graphs as single MCP commands to gain IDE portability without sacrificing durability. For example, a production system might use LangGraph for its core, auditable business logic, but expose certain entry points as MCP tools built with FastMCP, allowing other services or even human-in-the-loop IDEs to interact with the workflow in a standardized way.

To make this theory concrete, we will now share the actual pivots we made while building the course capstones.

## Our Capstone Pivots

Let’s apply this matrix to our capstone project. Our decision-making process evolved as we built, highlighting the importance of choosing the right tool for the job.

Our initial plan was to use LangGraph for both agents. However, we quickly found that the research agent’s need for high interactivity and divergent exploration made rigid graphs cumbersome. The process of research is not linear; it involves frequent changes in direction, adding new tools on the fly, and adapting to unexpected findings. A pre-defined graph structure created too much friction. Flexible MCP tools, which could be called independently by a lightweight client, proved to be a much better fit for Nova.

In contrast, the writing agent had the opposite requirements. Its process is repeatable and needs to be auditable. We needed to track every step, from drafting to editing to final review, and be able to pause for human input. This demanded the checkpoints, HITL interrupts, and time-travel replay capabilities that LangGraph provides.

This led to our hybrid outcome: Nova is implemented as a FastMCP server that any client, including IDEs, can steer, while Brown is a LangGraph workflow whose entry points are deliberately coarse MCP tools. This pattern of wrapping complex internal workflows behind single MCP commands allows us to gain portability without sacrificing durability or auditability. Brown currently exposes three tools: `generate_article`, `edit_article`, and `edit_selected_text`.

We considered the OpenAI Agents SDK but ultimately deprioritized it. For the long-running nature of both capstone tasks, it lacked the first-class persistence and deep MCP integration we required. These real-world pivots illustrate the central lesson of this module.

## Conclusion

The core takeaway from this lesson is to prioritize stable concepts over transient brand names. Stateful graphs, typed contracts, durable execution, and MCP standardization are the principles that will outlast any single framework. Investing time to understand the MCP specification is particularly high-leverage, as it provides portability across every current and future stack. This ensures that the tools and services you build today will remain valuable even as the runtimes and orchestration layers evolve.

A practical selection process should start by applying the four decision axes to your project. Begin with the smallest viable stack that meets your reliability needs and ensure all your tooling is portable via MCP. A common migration path might start with exploration in AutoGen Studio to validate multi-agent patterns, followed by extracting successful logic into portable FastMCP tools. Finally, you can anchor the production system in a robust runtime like LangGraph or PydanticAI to ensure durability and auditability. This phased approach allows you to move quickly during the experimental phase while building a solid foundation for a production-grade application.

In our next lesson, we will cover system design, including model selection, cost and latency trade-offs, and the strategic placement of human-in-the-loop gates. After that, we will begin the hands-on capstone builds, using the hybrid FastMCP-plus-LangGraph stack we chose through this exact process. Nova will be built with FastMCP to support its client-server architecture and iterative research loops, while Brown will use LangGraph and FastMCP to create a durable workflow with review-edit cycles and HITL editing.

## References

- [1] Persistence. (n.d.). LangChain. https://docs.langchain.com/oss/python/langgraph/persistence
- [2] Durable Execution. (n.d.). Pydantic. https://ai.pydantic.dev/durable_execution/overview/
- [3] FastMCP. (n.d.). gofastmcp.com. https://gofastmcp.com/
- [4] Workflows and agents. (n.d.). LangChain. https://docs.langchain.com/oss/python/langgraph/workflows-agents
- [5] OpenAI Agents SDK. (n.d.). OpenAI. https://openai.github.io/openai-agents-python/
- [6] Introduction. (n.d.). CrewAI. https://docs.crewai.com/introduction
- [7] AutoGen. (n.d.). Microsoft. https://microsoft.github.io/autogen/stable/
- [8] Build your first Flow. (n.d.). CrewAI. https://docs.crewai.com/guides/flows/first-flow
- [9] AutoGen Studio User Guide. (n.d.). Microsoft. https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html
- [10] Quickstart. (n.d.). FastMCP. https://gofastmcp.com/getting-started/quickstart
- [11] A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP). (2025). arXiv. https://arxiv.org/html/2505.02279v1
- [12] Agentic AI Governance Frameworks. (n.d.). NICE. https://www.nice.com/agentic-ai/agentic-ai-governance-frameworks
- [13] AI Agents for Compliance and Risk Management. (n.d.). Vegavid. https://vegavid.com/ai-agents-for-compliance-and-risk-management
- [14] Debugging Non-Deterministic LLM Agents: Implementing Checkpoint-Based State Replay with LangGraph. (2024). DEV Community. https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171
- [15] How to run your OpenAI agents in production. (n.d.). Diagrid. https://www.diagrid.io/solutions/openai-agents-production
- [16] Building a Durable Runtime for the OpenAI Agents SDK. (n.d.). ZenML. https://www.zenml.io/blog/openai-agents-sdk-durable-runtime
- [17] Analyzing the Security Risks of OpenAI's AgentKit. (n.d.). Zenity. https://labs.zenity.io/p/analyzing-the-security-risks-of-openai-s-agentkit
- [18] Multi-Agent Systems for Robotic Autonomy with LLMs. (2025). The Computer Vision Foundation. https://openaccess.thecvf.com/content/CVPR2025W/MEIS/papers/Chen_Multi-Agent_Systems_for_Robotic_Autonomy_with_LLMs_CVPRW_2025_paper.pdf
- [19] Orchestrating ambient agents with Temporal. (2025). Temporal. https://temporal.io/blog/orchestrating-ambient-agents-with-temporal
- [20] LLM-based Multi-Agent Cooperation: A Survey and Roadmap. (2025). xue-guang.com. https://xue-guang.com/post/llm-marl
- [21] Stability, Concurrency, & Performance. (2026). arXiv. https://arxiv.org/html/2603.05637v1
- [22] Introducing the LangGraph Functional API. (2025). LangChain Blog. https://blog.langchain.com/introducing-the-langgraph-functional-api