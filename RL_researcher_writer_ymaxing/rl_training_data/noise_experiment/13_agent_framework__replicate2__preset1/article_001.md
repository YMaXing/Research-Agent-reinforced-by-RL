# How to Choose an AI Agent Framework

In our last lesson, we introduced the two capstone projects that will be central to this course: Nova, an adaptable and interactive research agent, and Brown, a reliable and auditable writing agent. The design of these systems forces us to confront a critical engineering decision: which framework should we build on? This choice is not trivial. A poor selection can lead to brittle abstractions that break under real load. It can also cause stalled progress in a fast-moving ecosystem or hidden gaps in durability that only appear after weeks of investment.

Throughout this lesson, we will explore two core concepts that anchor our capstone designs. For Brown, the writing agent, we need auditable and resumable workflows, which we will achieve using LangGraph's interrupts and checkpoints. For Nova, the research agent, we need tool portability, which we will achieve using the Model Context Protocol (MCP) as a universal interoperability layer.

This leads us to a hybrid architecture. Our research agent will be a lightweight MCP server that any client can steer, while our writing agent will be a durable workflow that exposes its capabilities as coarse-grained MCP tools. This lesson focuses on the philosophies, core abstractions, and production trade-offs that justify these architectural choices, rather than on API syntax or "hello, world" tutorials.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down
Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

With our capstones as a concrete reference, we can now examine why framework selection under uncertainty so often fails in production. We will break down the distinct layers of an agentic system—runtime, protocol, and tooling—to understand which problems each layer actually solves.

## Framework Choice Under Uncertainty

The AI agent ecosystem is new and evolving quickly. No single framework will satisfy every use case. To choose effectively, you must distinguish between three layers that are frequently conflated: the runtime, the protocol, and the tooling framework.

Each layer solves a distinct production problem. The **runtime** (e.g., LangGraph, CrewAI, PydanticAI) provides the orchestration and state management needed for durable execution and resumability. The **protocol** (e.g., Model Context Protocol, or MCP) offers a standardized interface that prevents tool lock-in and eliminates the need to rewrite tools for different runtimes. Finally, the **tooling framework** (e.g., FastMCP) supplies ready-to-deploy components like transports and authentication, improving the developer experience.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down
Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

Engineers who select frameworks based on hype cycles or simple demos often run into trouble. A framework that seems easy for a prototype may lack the reliability primitives needed for production workloads. Conversely, a complex framework might introduce unnecessary overhead for exploratory work. Research on multi-agent systems highlights a critical decoupling: a workflow’s execution path can diverge significantly from the ideal yet still produce a correct answer ("behavioral detours"), while another can follow the expected path perfectly yet produce a wrong answer ("silent semantic corruption"). The key is to match the framework's characteristics to your workload's needs, distinguishing between interactive and deterministic tasks [[13]](https://arxiv.org/html/2604.27586v1).

We learned this firsthand. We initially planned to build our research agent with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was a wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes Instead of Brands

To avoid these traps, you need a way to evaluate frameworks based on principles, not brands. We use four decision axes to analyze any library and determine its fit for a given project.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down
Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

The first axis is **control-flow explicitness versus LLM-driven autonomy**. Frameworks with graph-based determinism, like LangGraph, provide explicit nodes and edges that make every state transition auditable. This is ideal for deterministic workflows where you need to know precisely why the system made a particular decision. In contrast, lightweight agent loops, like those in the OpenAI Agents SDK, favor exploration and adaptability, which is better for tasks where the path to a solution is not known in advance. The question to ask is: does your application require repeatable, auditable steps, or does it need to navigate an unpredictable environment?

The second axis is **reliability primitives**. Production systems fail. A good framework provides tools to handle those failures gracefully. Look for features like checkpointing, time-travel replay, human-in-the-loop (HITL) interrupts, and durable execution across restarts. This is analogous to the shift from simple scripts to robust orchestration in cloud computing; AI agents are stateful, long-running workloads, not stateless functions, and require primitives that reflect this reality. LangGraph emphasizes interrupts and persistence, while PydanticAI integrates with systems like Temporal and DBOS for durable execution. These features are non-negotiable for our writing agent but less critical for the more ephemeral research agent [[1]](https://docs.langchain.com/oss/python/langgraph/persistence), [[2]](https://ai.pydantic.dev/durable_execution/overview/), [[14]](https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox).

The third axis is **abstraction level and developer experience**. Some frameworks, like the OpenAI Agents SDK, provide minimal primitives (Agents, Tools, Guardrails), requiring more boilerplate but delivering greater flexibility. Others, like CrewAI, offer opinionated constructs that accelerate initial development but may reduce adaptability when dealing with edge cases.

The fourth axis is **tooling interoperability**. MCP functions as the USB-C equivalent for AI. It provides a standard interface for tools, letting you write them once as MCP servers using a framework like FastMCP and reuse them across different runtimes, including LangGraph, the OpenAI Agents SDK, or even IDEs like Cursor, without rewriting [[3]](https://gofastmcp.com/).

Our capstone projects map clearly to these axes. The research agent requires autonomy and interoperable tools for its exploratory nature, making a lightweight loop with MCP a good fit. The writing agent demands an explicit, auditable workflow with strong reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks. We will use adoption metrics like download trends and GitHub stars as a proxy for maturity, ecosystem health, and long-term maintenance burden.

### LangGraph

LangGraph’s philosophy centers on a stateful graph model with native checkpoints and interrupts for auditable workflows. This makes it ideal for processes that need to be resumable and traceable, a perfect fit for our writing agent. The library shows strong, consistent activity, with daily downloads averaging between 400K and 500K over the past three months [[1]](https://docs.langchain.com/oss/python/langgraph/persistence), [[4]](https://docs.langchain.com/oss/python/langgraph/workflows-agents).

<aside>
💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers, etc.), **LangGraph** focuses specifically on **structured**, **stateful workflows**. It introduces graph-based execution with checkpoints and resumability, which are features not native to standard LangChain chains.

In short, LangChain is the toolbox, while LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions [[4]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). You will see LangChain code in the writing agent.
</aside>

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down
Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.

### OpenAI Agents SDK

The OpenAI Agents SDK embodies a philosophy of minimal API surface area, composed of agents, tools, guardrails, handoffs, and sessions. It favors lightweight, Python-native loops over compiled state machines. Over the past three months, the library has recorded 90K–120K daily downloads, with a slight upward trend [[5]](https://openai.github.io/openai-agents-python/).

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down
Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.

### AgentKit

AgentKit is a modular toolkit for building, deploying, and optimizing agents across the OpenAI platform. It unifies a visual builder, connectors (including MCP), ChatKit for UI embedding, and evaluation infrastructure. This allows developers to visually compose multi-agent systems, manage data sources, and embed chat-based experiences directly into their products, all backed by versioning, guardrails, and evaluation tools for safe, reliable deployment.

<aside>
💡 OpenAI AgentKit vs. OpenAI Agents SDK

The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration and fine-grained control. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK: it adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**. In short, the SDK is the coding foundation, while AgentKit is the integrated platform for design, deployment, and optimization.
</aside>

### CrewAI

CrewAI features a dual architecture: role-based autonomous crews for collaborative exploration, and event-driven flows for deterministic control. It also provides a strong developer experience with CLI scaffolding and YAML-based definitions for agents and tasks. Daily downloads for CrewAI have ranged between 40K and 100K.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down
Image 6: Source: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.

### PydanticAI

PydanticAI emphasizes type safety and schema-driven validation. It offers durable execution through integrations with platforms like Temporal, DBOS, and Prefect, along with built-in graph support. Daily downloads of Pydantic-AI doubled from ~150K in July to 300-450K by October 2025, demonstrating strong growth.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down
Image 7: Source: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.

### AutoGen

AutoGen takes a layered approach, with its Studio GUI explicitly positioned for exploration and prototyping, not production. Successful patterns discovered in the Studio can then be hardened into code using the AgentChat or core libraries [[6]](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html), [[7]](https://microsoft.github.io/autogen/stable/).

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down
Image 8: Source: pepy.tech, daily downloads for autogen, accessed October 15, 2025.

### Claude Agent SDK

A newer entrant from Anthropic, this SDK offers tight integration with the Claude model family, leveraging its strengths in large context and low-level tool use. However, its ecosystem is smaller and still evolving.

### FastMCP

FastMCP is not a runtime but a tooling layer for building MCP-compliant servers and clients. This makes tools portable across any runtime or IDE that supports the protocol. FastMCP has shown explosive growth, with daily downloads surging from ~250K in July to over 1.2M per day in October 2025.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down
Image 9: Source: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.

GitHub stars offer another view of community adoption and trust.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down
Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026.

It is important to avoid a single-framework dogma. Hybrid patterns are common and effective. For example, you can consume FastMCP tools inside a LangGraph workflow or migrate from an AutoGen prototype to a more hardened runtime. We will now deep-dive into each framework, starting with LangGraph, using our four axes and capstone needs as constant evaluation lenses.

## Framework Deep Dive: LangGraph

LangGraph uses a graph-based model where nodes are Python functions and edges are explicit transitions. This design makes complex, multi-step logic transparent and auditable. Its core value is in making an inherently non-deterministic process—LLM interactions—traceable and repeatable. The LLM remains probabilistic, but the workflow becomes deterministic, debuggable, and auditable [[15]](https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171).

Its core production primitives include interrupts for human-in-the-loop validation, persistence for resumability, and time-travel debugging that lets you replay and branch from any prior state. For high-stakes applications, this is critical. A financial trading agent, for example, can be paused before executing a trade, allowing a human to inspect the state, approve the action, or even modify the plan before resuming execution [[16]](https://www.comet.com/site/blog/multi-agent-systems).

The framework offers two definition styles: a "graph API" for fully explicit graphs and a "functional API" that uses decorators. This creates a trade-off between the learning curve and the payoff in determinism. The functional API is easier to adopt, but the graph API provides clearer visualization and more granular control [[8]](https://www.langchain.com/blog/introducing-the-langgraph-functional-api).

LangGraph is overkill for simple, exploratory scripts. However, for repeatable processes like our writing agent, the modeling investment is justified by the built-in safety. This contrasts with lighter loops, which can suffer from costly "behavioral detours" like rerouting or looping when encountering unexpected inputs [[13]](https://arxiv.org/html/2604.27586v1).

Having examined a graph-centric, reliability-first option, we now turn to a deliberately minimal alternative.

## Framework Deep Dive: OpenAI Agents SDK

The OpenAI Agents SDK is designed with a philosophy of minimal primitives to reduce the conceptual surface area while still enabling powerful agentic applications. Its core concepts are simple and interrelated.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down
Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.

Here is how the main components work together:
- **Agents**: These are LLMs equipped with instructions and a set of tools they can use.
- **Tools**: These are simply Python functions that agents can call to interact with the outside world.
- **Guardrails**: These are mechanisms for validating agent inputs and outputs to ensure safety and correctness.
- **Handoffs**: This is a pattern for agents to delegate tasks to other, more specialized agents.
- **Sessions**: This component automatically manages conversation history across multiple runs, providing a simple form of memory.

The execution model is based on direct Python control flow, using standard `if/else` statements and loops, rather than a compiled state machine like in graph-based systems. The fundamental difference between the OpenAI Agents SDK and LangGraph’s functional API lies in this execution model. The OpenAI SDK uses a simple, Python-native agent loop that you control directly. In contrast, even with its decorator-based functional API, LangGraph compiles your code into an explicit, stateful graph. This underlying state machine manages execution, persistence, and interruptions, providing a more robust but also more constrained environment.

The SDK is a strong choice for teams that want a fast path to production and prefer lightweight orchestration with sensible defaults. However, it comes with a reliability trade-off: features like durable pause, resume, and checkpointing are not provided out of the box and must be implemented by the developer. The natural extension of this minimal SDK is a full-lifecycle platform built on top of it.

## Framework Deep Dive: AgentKit

AgentKit is a complete lifecycle toolkit layered on top of the OpenAI Agents SDK, covering design, deployment, optimization, and continuous improvement. It extends the SDK by adding a visual workflow designer, UI embedding tools, and a comprehensive evaluation infrastructure [[9]](https://openai.com/index/introducing-agentkit).

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down
Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.

Its key components include:
- **Agent Builder**: A drag-and-drop canvas for designing and versioning multi-agent workflows. It allows for visual composition of logic, the addition of guardrails, and preview testing with inline evaluation.
- **Connector Registry**: A centralized interface for managing data connections, including Dropbox, Google Drive, SharePoint, Teams, and third-party MCPs.
- **ChatKit**: A toolkit for embedding agentic chat UIs directly into web or mobile products.
- **Evals and Reinforcement Fine-Tuning (RFT)**: Capabilities for measuring, grading, and improving agent performance.

AgentKit sits one layer above the OpenAI Agents SDK. You still use the SDK for code-first orchestration, but AgentKit provides the surrounding tools for design, deployment, and continuous improvement. This visual composition and built-in evaluation support safe multi-agent systems at scale without forcing everything into code. The trade-off is its optimization for the OpenAI ecosystem, though growing MCP connector support is improving its interoperability. AgentKit adds clear value over the raw SDK for teams that need no-code workflow design, versioning, and continuous improvement loops.

We now examine a framework whose duality spans both autonomous crews and structured flows.

## Framework Deep Dive: CrewAI

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcc81dc-f35c-4a6b-95e8-557db10090a9/e0cb631a-91ae-46fc-a332-d5e1afd61c80/w=1920,quality=90,fit=scale-down
Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`.

CrewAI introduces a powerful duality with its two main concepts: **Crews** and **Flows**. This dual architecture allows you to balance autonomy with control [[10]](https://docs.crewai.com/introduction).

**Crews** are for role-based, autonomous collaboration. You define agents with specific roles, goals, and tools, and they work together to solve a problem, much like a human team. This is ideal for tasks requiring flexibility and emergent behavior. **Flows**, on the other hand, are for event-driven, deterministic orchestration. They give you fine-grained control over the workflow, allowing you to define precise execution paths with conditional logic and state management [[11]](https://docs.crewai.com/guides/flows/first-flow).

A typical development pattern is to start with an autonomous crew for rapid prototyping to explore a problem space. Once the requirements solidify, you can introduce a flow to add structure, reliability, and control to the process.

CrewAI also has a strong focus on developer experience, with features like CLI scaffolding for quick project setup, YAML-based definitions for agents and tasks, and configurable memory and persistence options. It finds its sweet spot in multi-agent handoff scenarios, such as a researcher-to-writer workflow, where role clarity accelerates development. The trade-off of its opinionated constructs is a rapid initial velocity at the cost of some flexibility when edge cases arise.

Another framework approaches the problem through the lens of type safety and compile-time contracts.

## Framework Deep Dive: PydanticAI

PydanticAI’s philosophy is similar to that of FastAPI, where Pydantic models and type hints create compile-time contracts between your code and the LLM's behavior. This focus on type safety ensures data integrity and makes your application more robust.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/0454e524-5d87-4288-82d4-3abd2b78a6f2/image/w=1920,quality=90,fit=scale-down
Image 14: Diagram illustrating PydanticAI's design philosophy.

It comes with strong production features, including **durable execution integrations** with systems like Temporal, DBOS, or Prefect. This allows agents to survive restarts, pause for human input, and resume long-running tasks. Workflow engines like Temporal provide "durable virtual memory," making workflows "fault-oblivious" so they can resume exactly where they left off after a crash. PydanticAI also has built-in **graph support** for non-linear flows [[17]](https://intuitionlabs.ai/articles/agentic-ai-temporal-orchestration).

The developer experience is enhanced by automatic schema generation from type hints and docstrings, as well as structured output with automatic retries on validation failure. The main trade-off is the up-front investment in defining schemas. PydanticAI is best suited for projects where structured data correctness and long-running, resumable tasks are paramount.

We now look at a layered system that explicitly separates experimentation from production hardening.

## Framework Deep Dive: AutoGen

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down
Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.

AutoGen features a layered design that deliberately separates experimentation from production. It is composed of three main layers:
- **AutoGen Studio** is a low-code GUI that allows you to prototype agent teams and workflows without writing code. You can visually compose agents, configure their tools, and test their interactions.
- **AgentChat** is a programming framework for building conversational multi-agent applications.
- **Core** provides low-level, event-driven primitives for building scalable, custom agent systems.

The typical workflow involves exploring and validating ideas visually inside Studio, then hardening the successful patterns into code using the lower-level AgentChat and Core libraries. It is important to note the official disclaimer that Studio is a research prototype and not intended for production environments [[6]](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html).

AutoGen’s strength lies in its use as an R&D laboratory for discovering effective multi-agent conversation patterns. The trade-off is that its flexibility requires the team to re-implement reliability when moving to production, addressing failure modes like memory degradation across long-horizon tasks or implementation drift under execution pressure [[18]](https://huggingface.co/papers?q=failure-mode-targeted+generation).

A newer entrant to the field focuses on tight integration with a specific model family.

## Framework Deep Dive: Claude Agent SDK

The Claude Agent SDK is built with a philosophy of tight integration to leverage the specific strengths of Anthropic's Claude models, such as their large context windows, strong reasoning capabilities, and fine-grained control over tool use. It offers ergonomic tool calling and orchestration tailored to the Anthropic model family.

As a newer entrant, its trade-offs include a smaller community, fewer third-party integrations, and a rapidly evolving API surface. This presents both an opportunity and a risk. Early adoption can yield model-optimized performance, but teams must balance this against the maturity of the ecosystem. The clearest use case for the Claude Agent SDK is for teams already committed to the Anthropic stack who want native performance and are willing to accept smaller community support.

The final deep dive examines a non-runtime layer that complements every option we have discussed.

## Framework Deep Dive: FastMCP

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/745828fd-27e2-4a50-b613-7275a1e1dceb/image/w=1920,quality=90,fit=scale-down
Image 16: FastMCP Architecture and Interoperability

FastMCP is not a runtime; it is a tooling framework that lets you build MCP-compliant servers and clients. This makes tools, resources, and prompts portable across any runtime or IDE that speaks the protocol. Much like the Language Server Protocol (LSP) standardized how IDEs interact with language compilers, MCP aims to standardize how agents interact with tools. You can write a tool once and reuse it inside LangGraph, Cursor, or any future compatible system [[19]](https://medium.com/@laowang_journey/model-context-protocol-mcp-real-world-use-cases-adoptions-and-comparison-to-functional-calling-9320b775845c).

This approach enhances security and efficiency. Instead of stuffing large documents into a prompt and hitting token limits, an agent can call MCP endpoints to fetch only the necessary context, with the server enforcing permissions [[20]](https://arxiv.org/html/2510.10819v1). Beyond the protocol itself, FastMCP provides production-ready extensions for authentication, server composition, and cloud deployment.

<aside>
💡 **Pattern: tools-as-workflows (Brown)**

For our writing agent (Brown), we wrap each workflow entry point as a **coarse-grained MCP tool** (e.g., `generate_article`, `edit_article`, `edit_selected_text`). The MCP tool handler simply **kicks off the corresponding LangGraph run**, returns progress/messages, and finally yields artifacts and diffs. This gives you MCP portability (Cursor, Claude Code) **without** losing LangGraph’s durability and auditability. You’ll learn more about this in the later lessons.
</aside>

The developer experience of FastMCP is designed to be simple and Pythonic. You can expose a function as a tool with a single decorator, and FastMCP handles the schema generation and transport details automatically [[12]](https://gofastmcp.com/getting-started/quickstart).

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

With these deep dives complete, we can now synthesize everything into a decision matrix and offer some tentative forecasts.

## Choosing for Your Project: Decision Matrix & Tentative Forecasts

To help you choose the right framework for your project, we have compiled a decision matrix that maps common project needs to the relative strengths of each framework.

Table 1: Decision matrix comparing AI agent frameworks against common needs
| Feature | LangGraph | PydanticAI | OpenAI SDK | AgentKit | CrewAI | AutoGen | FastMCP |
|---|---|---|---|---|---|---|---|
| **Durability/HITL/Replay** | ✅ | | | | | ✅ | |
| **Typed Contracts + Durable Execution** | | ✅ | | | | | ✅ |
| **Few Primitives + Guardrails/Handoffs** | ✅ | | ✅ | ✅ | | | ✅ |
| **Role-based Teams + Quick Scaffolding** | | | | ✅ | ✅ | ✅ | |
| **Exploration Lab** | | | ✅ | ✅ | ✅ | ✅ | |
| **Tool Portability Across Stacks** | | ✅ | | ✅ | | | ✅ |

It is important to treat this matrix as a snapshot in time. The ecosystem is evolving rapidly, so you should always re-evaluate frameworks against the four decision axes whenever libraries release major updates.

Based on our analysis, we can offer some forecasts. LangGraph and PydanticAI are well-suited for reliability-heavy workflows. The OpenAI SDK is a good choice for lightweight simplicity, while AgentKit is ideal when visual design and continuous evaluation loops are required. CrewAI excels at rapid multi-agent prototyping, AutoGen serves as a strong R&D starting point, and FastMCP is emerging as the universal tooling substrate.

In practice, hybrid patterns are common and often provide the best of both worlds. For example, you can consume portable FastMCP tools inside a durable LangGraph workflow, combining interoperability with reliability. Another effective pattern is to migrate from an AutoGen Studio prototype to a more hardened runtime once the agent's logic is validated. You can also expose a complex graph as a single MCP command to gain IDE portability without sacrificing durability.

To make this theory concrete, we will now share the actual pivots we made while building our course capstones.

## Our Capstone Pivots

Let’s apply this matrix to our capstone project. Our decision-making process evolved as we built, highlighting the importance of matching the tool to the job.

Our initial plan was to use LangGraph for both the research agent (Nova) and the writing agent (Brown). However, a one-size-fits-all approach quickly proved inadequate. Nova's need for high interactivity and divergent exploration meant a rigid graph was susceptible to costly "behavioral detours"—constant rerouting and extended execution in response to new information. Flexible, portable MCP tools were a much better fit for this exploratory work.

The writing agent had opposite requirements. Its process needed to be repeatable and auditable, which made LangGraph’s features like checkpoints, HITL interrupts, and time-travel replay capabilities essential.

This led to our final hybrid architecture. Nova is implemented as a FastMCP server, allowing any client to steer its research process. Brown is a LangGraph workflow, but its entry points are exposed as coarse-grained MCP tools. This creates an emergent pattern of wrapping complex workflows behind single MCP commands, gaining portability without sacrificing durability. Brown currently exposes three tools: `generate_article`, `edit_article`, and `edit_selected_text`.

We considered the OpenAI Agents SDK, but deprioritized it because it lacked the first-class persistence and deep MCP integration required for the long-running nature of both capstone tasks. These real-world pivots illustrate the central lesson of this module.

## Conclusion

The key takeaway from this lesson is to prioritize stable concepts over transient brand names. Focus on stateful graphs, typed contracts, durable execution, and MCP for standardization. These principles will serve you well as the framework landscape continues to evolve.

We highly recommend reading the MCP specification itself. It is a one-time investment that will yield tool portability across every current and future stack. This allows you to decouple your tools from any specific runtime, a crucial advantage in this fast-moving field.

Our practical selection process is straightforward: apply the four decision axes to your project, start with the smallest viable stack that meets your reliability needs, and keep all your tooling portable via MCP. A common migration path might be to begin exploration in AutoGen Studio, extract successful patterns into FastMCP tools, and then anchor your production system in a robust runtime like LangGraph or PydanticAI.

In our next lesson, we will cover system design, including model selection, cost and latency trade-offs, and HITL placement. After that, we will move on to the hands-on capstone builds, where you will see the hybrid FastMCP-plus-LangGraph stack we have chosen through this exact process in action. We will build out Nova with FastMCP for ingestion and research loops, and Brown with LangGraph and MCP tools for a durable, auditable writing workflow.

## References

- [1] Persistence. (n.d.). LangChain. https://docs.langchain.com/oss/python/langgraph/persistence
- [2] Durable Execution. (n.d.). Pydantic AI. https://ai.pydantic.dev/durable_execution/overview/
- [3] FastMCP. (n.d.). gofastmcp.com. https://gofastmcp.com/
- [4] Workflows and agents. (n.d.). LangChain. https://docs.langchain.com/oss/python/langgraph/workflows-agents
- [5] OpenAI Agents SDK. (n.d.). OpenAI. https://openai.github.io/openai-agents-python/
- [6] AutoGen Studio User Guide. (n.d.). Microsoft. https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html
- [7] AutoGen. (n.d.). Microsoft. https://microsoft.github.io/autogen/stable/
- [8] Introducing the LangGraph Functional API. (2025, January 29). LangChain. https://www.langchain.com/blog/introducing-the-langgraph-functional-api
- [9] Introducing AgentKit. (2025, October 6). OpenAI. https://openai.com/index/introducing-agentkit
- [10] Introduction. (n.d.). CrewAI. https://docs.crewai.com/introduction
- [11] Build your first Flow. (n.d.). CrewAI. https://docs.crewai.com/guides/flows/first-flow
- [12] Quickstart. (n.d.). gofastmcp.com. https://gofastmcp.com/getting-started/quickstart
- [13] Trace-Level Analysis of Information Contamination in Multi-Agent Systems. (2026). arXiv. https://arxiv.org/html/2604.27586v1
- [14] Running AI Agents on Kubernetes with the Agent Sandbox. (2026, March 20). Kubernetes. https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox
- [15] Debugging Non-Deterministic LLM Agents. (n.d.). Dev.to. https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171
- [16] A Developer’s Guide to Multi-Agent Systems. (n.d.). Comet. https://www.comet.com/site/blog/multi-agent-systems
- [17] Agentic AI Needs Temporal for Orchestration. (n.d.). Intuition Labs. https://intuitionlabs.ai/articles/agentic-ai-temporal-orchestration
- [18] Failure-mode-targeted generation. (n.d.). Hugging Face. https://huggingface.co/papers?q=failure-mode-targeted+generation
- [19] Model Context Protocol (MCP): Real-World Use Cases. (n.d.). Medium. https://medium.com/@laowang_journey/model-context-protocol-mcp-real-world-use-cases-adoptions-and-comparison-to-functional-calling-9320b775845c
- [20] The Model Context Protocol (MCP) as a Standardized Interface. (2025). arXiv. https://arxiv.org/html/2510.10819v1