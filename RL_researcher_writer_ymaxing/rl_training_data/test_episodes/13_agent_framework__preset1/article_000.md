# How to Choose an AI Agent Framework

In our previous lesson, we introduced the scope and design of our two capstone projects: Nova, an adaptable and interactive research agent, and Brown, a reliable and auditable writing agent. These projects serve as our concrete anchors for exploring one of the most critical decisions in AI engineering: choosing the right agent framework.

The choice of framework can determine whether a project succeeds or fails. A poor selection can lead to brittle abstractions that break under real-world load, stalled progress in a fast-moving ecosystem, or hidden gaps in durability that only appear after weeks of investment. This lesson is about moving beyond hype and making principled decisions.

We will focus on two core concepts that are central to our capstone designs. For Brown, the writing agent, we need auditable and resumable workflows, which we will achieve using **LangGraph's interrupts and checkpoints**. For Nova, the research agent, we need tool portability and adaptability, which we will solve with the **Model Context Protocol (MCP)**, a universal interoperability layer.

Our final architecture will reflect these needs: Nova will be built as a lightweight MCP server that any client can steer, while Brown will be a durable LangGraph workflow that exposes its capabilities as coarse-grained MCP tools. This lesson will unpack the philosophies, core abstractions, and production trade-offs of the leading frameworks to show you how we arrived at this design. We will focus on decision principles, not just API syntax, to give you a mental model for evaluating any framework you encounter.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down
Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

With our capstones as a concrete reference, let's examine why framework selection under uncertainty so often fails and what layers—runtime, protocol, and tooling—actually solve which problems.

## Framework Choice Under Uncertainty

The AI agent ecosystem is new and evolving quickly. No single framework will satisfy every use case. To make sense of the options, you must distinguish between three layers that are often conflated: the runtime, the protocol, and the tooling.

The **runtime** is the orchestration engine that manages state and execution. Frameworks like LangGraph, CrewAI, and the OpenAI Agents SDK fall into this category. They provide the machinery for durable execution, state management, and resumability. The **protocol**, like MCP, provides a standardized interface that ensures portability. It prevents you from being locked into a single runtime by allowing your tools to communicate with any compatible system. Finally, the **tooling framework**, like FastMCP, provides the scaffolding to build on top of a protocol, offering ready-to-deploy transports, authentication, and a better developer experience.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down
Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

Engineers often select frameworks based on hype cycles or simple "hello, world" demos. This leads to common failure modes. A framework that looks easy in a tutorial might lack the reliability primitives needed for a production workload. Conversely, a complex framework might introduce unnecessary overhead for an exploratory, interactive task.

Our capstone projects illustrate this perfectly. An interactive workload like Nova’s research process requires flexibility, while a deterministic one like Brown’s writing process demands auditability. Choosing the wrong framework for either would have led to a dead end.

We learned this firsthand. We initially planned to build our research agent with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. This mismatch creates "structural divergence," where the execution path deviates from the predefined graph, forcing the system into costly "rerouting" patterns to handle unexpected states [[8]](https://arxiv.org/html/2604.27586v1). A rigid graph was a wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes

To avoid these traps, you need a way to evaluate frameworks based on first principles, not brand names. We use four decision axes to analyze any library and determine if it fits a project’s needs.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down
Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

### Control-Flow Explicitness vs. LLM-Driven Autonomy

This axis measures the trade-off between deterministic control and flexible autonomy. Graph-based frameworks like LangGraph offer **explicit control**, with defined nodes and edges that make every state transition auditable. This is ideal for repeatable workflows where you need to know precisely why the system made a particular decision. On the other end, lightweight agent loops, like those in the OpenAI Agents SDK, favor **autonomy**. They are better for exploratory tasks where the path to a solution is unknown. The question to ask is: does your application require repeatable, auditable steps, or does it need to navigate an unpredictable environment?

### Reliability Primitives

Production systems fail. A good framework provides tools to handle those failures gracefully. This is why specialized agent runtimes exist; traditional orchestrators like Kubernetes are designed for stateless, scalable services, not the stateful, singleton, and often idle-then-bursty lifecycle of an AI agent [[9]](https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox). Look for features like **checkpointing**, **time-travel replay**, **human-in-the-loop (HITL) interrupts**, and **durable execution** across restarts. LangGraph, for example, emphasizes interrupts and persistence for building human-in-the-loop workflows [[1]](https://docs.langchain.com/oss/python/langgraph/persistence). PydanticAI integrates with durable execution systems like Temporal and DBOS [[2]](https://ai.pydantic.dev/durable_execution/overview/). These features are non-negotiable for our writing agent, Brown, but less critical for the more exploratory research agent, Nova.

### Abstraction Level and Developer Experience

Frameworks exist on a spectrum of abstraction. Some, like the OpenAI Agents SDK, provide minimal primitives like Agents, Tools, and Guardrails. This requires more boilerplate code but offers greater flexibility. Others, like CrewAI, offer opinionated, high-level constructs that accelerate initial development but can reduce adaptability when dealing with edge cases. The choice depends on whether you prefer to build from first principles or leverage a more structured, pre-packaged solution.

### Tooling Interoperability

In a rapidly changing ecosystem, tool lock-in is a real risk. This is where a standardized protocol like MCP becomes invaluable. MCP functions as the USB-C of AI, providing a standard interface for tools. You can write your tools once as MCP servers using a library like FastMCP [[3]](https://gofastmcp.com/) and reuse them across any runtime that speaks the protocol. This ensures your tools remain portable even if you switch runtimes. Its value is proven by rapid adoption in major IDEs like Cursor, VS Code, and JetBrains, which now act as native MCP clients [[10]](https://medium.com/@laowang_journey/model-context-protocol-mcp-real-world-use-cases-adoptions-and-comparison-to-functional-calling-9320b775845c).

Our capstone projects map clearly to these axes. The research agent, Nova, requires autonomy and interoperable tools for its exploratory nature, making a lightweight loop with MCP a good fit. The writing agent, Brown, demands an explicit, auditable workflow with strong reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks.

### LangGraph

LangGraph’s philosophy centers on a stateful, graph-based model. It uses native checkpoints and interrupts to create auditable and resumable workflows, making it ideal for processes that need to be traceable and recoverable [[1]](https://docs.langchain.com/oss/python/langgraph/persistence), [[4]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). The framework has shown strong and consistent adoption, with daily downloads averaging between 400K and 500K over the past three months.

<aside>
💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides a broad toolkit for building LLM applications—including chains, memory, and tools—**LangGraph** focuses specifically on **structured, stateful workflows**. It introduces graph-based execution with checkpoints and resumability, features not native to standard LangChain chains. In short, LangChain is the toolbox, while LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions [[4]](https://docs.langchain.com/oss/python/langgraph/workflows-agents).
</aside>

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down
Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.

### OpenAI Agents SDK

The OpenAI Agents SDK takes a different approach, favoring a minimal API surface with just a few core primitives: agents, tools, guardrails, handoffs, and sessions [[5]](https://openai.github.io/openai-agents-python/). It encourages building agentic loops using native Python control flow rather than compiled state machines. The library has seen steady adoption, with 90K to 120K daily downloads over the past three months.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down
Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.

### AgentKit

AgentKit is a complete toolkit for building, deploying, and optimizing agents on the OpenAI platform. It unifies a visual builder, a connector registry (including MCP), a `ChatKit` for embedding UIs, and evaluation infrastructure. This allows developers to visually compose multi-agent systems and embed them directly into products, all backed by versioning and guardrails for safe deployment.

<aside>
💡 OpenAI AgentKit vs. OpenAI Agents SDK

The **Agents SDK** is a lightweight, code-first framework for orchestrating agents via an API. In contrast, **AgentKit** is a complete lifecycle toolkit layered on top of the SDK. It adds a **visual builder**, **UI embedding tools**, and **evaluation infrastructure**. The SDK is the coding foundation; AgentKit is the integrated platform for design, deployment, and optimization.
</aside>

### CrewAI

CrewAI is built on a dual architecture of role-based autonomous **crews** for collaborative exploration and event-driven **flows** for deterministic control. It offers a strong developer experience with CLI scaffolding and YAML-based definitions. Daily downloads for the library range between 40K and 100K.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down
Image 6: Source: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.

### PydanticAI

PydanticAI emphasizes type safety and schema-driven validation. It also provides durable execution through integrations with systems like Temporal, DBOS, and Prefect, along with built-in graph support. Its adoption has grown strongly, with daily downloads doubling from ~150K in July to between 300K and 450K by October 2025.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down
Image 7: Source: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.

### AutoGen

AutoGen from Microsoft offers a layered approach, with a Studio GUI for exploration and AgentChat and Core libraries for production hardening. It is explicitly positioned as a tool for prototyping, not for building production-ready applications directly from the UI.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down
Image 8: Source: pepy.tech, daily downloads for autogen, accessed October 15, 2025.

### Claude Agent SDK

A newer entrant from Anthropic, this SDK offers tight integration with the Claude family of models. It leverages Claude's strengths, such as large context windows, but comes with a smaller ecosystem compared to more established frameworks.

### FastMCP

FastMCP is not a runtime but a tooling layer for building MCP-compliant servers and clients. It allows you to write tools once and make them portable across any runtime or IDE. It has shown explosive growth, with daily downloads surging from ~250K in July to over 1.2M per day in October 2025.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down
Image 9: Source: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.

We can use adoption metrics like download trends and GitHub stars as a proxy for a framework's maturity, ecosystem health, and long-term maintenance burden. However, it is important to avoid single-framework dogma. Hybrid patterns are common and often necessary. For instance, you might consume FastMCP tools inside a LangGraph workflow or migrate a prototype from AutoGen to a more hardened runtime for production.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down
Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026.

Now that we have surveyed the landscape, we will take a deeper dive into each framework, using our four axes and capstone needs as constant evaluation lenses, starting with LangGraph.

## Framework Deep Dive: LangGraph

LangGraph is built around a graph-based modeling approach where nodes are Python functions and edges represent explicit transitions. This design makes complex, multi-step logic transparent and auditable, which is critical for production systems where you need to understand why a decision was made.

Its core production primitives are what set it apart for reliability-focused applications. It offers **interrupts** for human-in-the-loop validation, **persistence** and **checkpointing** for resumability after failures, and **time-travel debugging** that lets you replay and branch from any prior state. The checkpointer saves serialized `MessagesState` snapshots to a database like PostgreSQL or SQLite, capturing the complete state at every step [[11]](https://arxiv.org/pdf/2603.21692).

LangGraph provides two distinct styles for defining workflows. The "graph API" requires you to explicitly define every node and edge, offering maximum control and determinism. The "functional API" uses decorators to define workflows in a more traditional, imperative style. This creates a trade-off: the graph API has a steeper learning curve but provides unparalleled transparency, while the functional API is easier to adopt but abstracts away some of the underlying state machine.

This level of control is not always necessary. For simple, exploratory scripts, a lighter agent loop might be more appropriate. However, for repeatable processes like our writing agent, the investment is justified. It transforms a transient, non-deterministic process into a replayable and inspectable state machine, making the workflow deterministic and auditable even if the LLM remains probabilistic [[12]](https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171).

Having examined a graph-centric, reliability-first option, we now turn to a deliberately minimal alternative.

## Framework Deep Dive: OpenAI Agents SDK

The OpenAI Agents SDK is designed around a philosophy of minimal primitives, deliberately reducing the conceptual surface area to make it quick to learn and easy to use. It provides a small set of core concepts that are powerful enough to build complex agentic applications.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down
Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.

These core primitives include:
*   **Agents:** LLMs equipped with instructions and tools.
*   **Tools:** Python functions that agents can call to interact with the outside world.
*   **Guardrails:** Mechanisms for validating agent inputs and outputs to ensure safety and correctness.
*   **Handoffs:** A way for agents to delegate tasks to other, more specialized agents.
*   **Sessions:** A system to automatically manage conversation history across multiple runs.

The execution model is fundamentally different from graph-based systems. Instead of compiling your logic into a state machine, the SDK uses direct Python control flow. You orchestrate your agents using standard `if/else` statements and `for` loops. This Python-native approach feels familiar and offers a great deal of flexibility.

This makes the SDK a strong choice for teams that want a fast path to production and prefer lightweight orchestration with sensible defaults. However, this simplicity comes with a trade-off. Reliability primitives like durable pause, resume, and checkpointing are not provided out of the box. If your application requires these features, you will need to implement them yourself.

The natural extension of this minimal SDK is a full-lifecycle platform built on top of it, which is exactly what AgentKit provides.

## Framework Deep Dive: AgentKit

AgentKit is a complete lifecycle toolkit layered on top of the OpenAI Agents SDK, designed to cover the entire process of building, deploying, and optimizing agents. It extends the SDK by adding a visual workflow designer, UI embedding tools, and a robust evaluation infrastructure.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down
Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.

Its key components include:
*   **Agent Builder:** A drag-and-drop canvas for designing and versioning multi-agent workflows. It allows for visual composition of logic, inline evaluation, and version control.
*   **Connector Registry:** A centralized interface for managing data connections, including Dropbox, Google Drive, and third-party MCPs.
*   **ChatKit:** A toolkit for embedding agentic chat UIs directly into your products, handling streaming, threading, and custom themes.
*   **Evals and Reinforcement Fine-Tuning (RFT):** A suite of tools for measuring, grading, and improving agent performance through datasets, automated prompt optimization, and custom graders.

AgentKit sits one layer above the SDK. You still use the SDK for code-first orchestration, but AgentKit provides the surrounding tools for design, deployment, and continuous improvement. This visual composition and built-in evaluation support make it easier to build and manage safe, multi-agent systems at scale without forcing everything into code. The trade-off is that it is most powerful when you stay within the OpenAI ecosystem, although its growing support for MCP connectors is improving interoperability.

For teams that need no-code workflow design, versioning, and a continuous improvement loop, AgentKit adds clear value over the raw SDK. We now examine a framework whose duality spans both autonomous crews and structured flows.

## Framework Deep Dive: CrewAI

CrewAI introduces a powerful duality with its two main architectural concepts: **Crews** and **Flows**. This dual architecture allows you to balance autonomous collaboration with deterministic control, making it a flexible choice for a wide range of applications.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcc81dc-f35c-4a6b-95e8-557db10090a9/e0cb631a-91ae-46fc-a332-d5e1afd61c80/w=1920,quality=90,fit=scale-down
Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`.

**Crews** are designed for role-based, autonomous collaboration. You define agents with specific roles, goals, and tools, and they work together to solve a problem, much like a human team. This is ideal for tasks that require creative problem-solving and flexible decision-making.

**Flows**, on the other hand, are for event-driven, deterministic orchestration. They give you fine-grained control over the workflow, allowing you to define precise execution paths with conditional logic and state management.

A typical development pattern with CrewAI is to start with an autonomous crew for rapid prototyping. Once the requirements solidify, you can introduce a flow to add structure and control. The framework also has a strong focus on developer experience, with CLI scaffolding, YAML-based definitions for agents and tasks, and configurable memory and persistence options.

CrewAI finds its sweet spot in multi-agent handoff scenarios, like a researcher passing findings to a writer, where role clarity accelerates development. The trade-off is that its opinionated constructs, while speeding up initial work, can introduce configuration overhead and reduce flexibility when dealing with edge cases.

Next, we will look at a framework that approaches the problem through the lens of type safety and compile-time contracts.

## Framework Deep Dive: PydanticAI

PydanticAI brings the philosophy of FastAPI to the world of AI agents, where Pydantic models and type hints create compile-time contracts between your code and the LLM's behavior. This focus on type safety ensures that the data flowing through your system is always structured and valid.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/0454e524-5d87-4288-82d4-3abd2b78a6f2/image/w=1920,quality=90,fit=scale-down
Image 14: Diagram illustrating PydanticAI's design philosophy.

It comes with several production-ready features. Its **durable execution integrations** with systems like Temporal, DBOS, or Prefect allow agents to survive restarts, pause for human input, and resume long-running tasks. These integrations provide what is effectively "durable virtual memory," making workflows "fault-oblivious" so they can resume exactly where they left off after a crash [[13]](https://intuitionlabs.ai/articles/agentic-ai-temporal-orchestration). It also has built-in **graph support** for creating non-linear workflows.

From an ergonomics perspective, PydanticAI shines. It automatically generates schemas from type hints and docstrings and provides structured output with automatic retries on validation failure. The main trade-off is the up-front investment in defining schemas. While this guarantees data correctness, it can present a learning curve for teams new to strict typing.

PydanticAI is best suited for projects where structured data correctness and long-running, resumable tasks are paramount. This aligns well with the auditability requirements of our writing agent, Brown.

We now look at a layered system that explicitly separates experimentation from production hardening.

## Framework Deep Dive: AutoGen

AutoGen is designed with a layered architecture that deliberately separates experimentation from production. This allows for rapid, flexible prototyping while providing a clear path to harden successful patterns into robust, production-ready code.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down
Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.

The framework consists of three main layers:
*   **AutoGen Studio:** A low-code GUI that lets you prototype agent teams and workflows without writing code. You can visually compose agents, configure their tools, and test their interactions.
*   **AgentChat:** A programming framework for building conversational multi-agent applications.
*   **Core:** A set of low-level, event-driven primitives for building scalable, custom agent systems.

The typical workflow involves exploring and validating ideas visually inside Studio, then translating the successful patterns into code using the lower-level AgentChat and Core libraries. It is important to note the explicit disclaimer that Studio is a research prototype and is not meant for production environments [[6]](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html).

AutoGen's strength lies in its use as an R&D laboratory for discovering effective multi-agent conversation patterns and termination conditions. The trade-off is that this high degree of flexibility during exploration means that the team is responsible for re-implementing reliability, security, and observability when moving a prototype to production.

Next, we will examine a newer entrant that focuses on tight model-family integration.

## Framework Deep Dive: Claude Agent SDK

The Claude Agent SDK is a newer framework from Anthropic that is built around a philosophy of tight integration with the Claude family of models. It is designed to leverage Claude's specific strengths, such as its large context windows, strong reasoning capabilities, and fine-grained control over tool use.

The SDK focuses on providing an ergonomic tool-calling and orchestration experience that is tailored specifically to the Anthropic model family. This can lead to highly optimized performance for teams that are already committed to using Claude.

However, as a newer entrant, it comes with certain trade-offs. The community is smaller, there are fewer third-party integrations available, and the API surface is still evolving. This creates a classic opportunity-versus-risk scenario. Early adoption can yield model-optimized performance, but teams must balance this against the maturity of the ecosystem. The clearest use case is for teams already standardized on the Anthropic stack who want native performance and are willing to accept smaller community support.

The final deep dive examines a non-runtime layer that complements every option we have discussed.

## Framework Deep Dive: FastMCP

FastMCP is not a runtime; it is a tooling framework that allows you to build MCP-compliant servers and clients. Its role is to make your tools, resources, and prompts portable across any runtime or IDE that speaks the Model Context Protocol.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/745828fd-27e2-4a50-b613-7275a1e1dceb/image/w=1920,quality=90,fit=scale-down
Image 16: FastMCP Architecture and Interoperability

The primary benefit of this approach is interoperability. You can write a tool once and reuse it inside LangGraph, the OpenAI SDK, or any future system that supports MCP. This is especially powerful given the protocol's wide adoption in developer tools like Cursor, VS Code, and JetBrains [[10]](https://medium.com/@laowang_journey/model-context-protocol-mcp-real-world-use-cases-adoptions-and-comparison-to-functional-calling-9320b775845c). This decouples your tooling from your orchestration layer, which is a powerful pattern in a rapidly evolving ecosystem.

FastMCP also provides production-oriented features that extend beyond the protocol itself, such as authentication, server composition, and cloud deployment options. Our capstone projects make extensive use of this pattern. Nova, the research agent, is implemented as a FastMCP server that any client can steer. Brown, the writing agent, exposes its complex LangGraph workflows as coarse-grained MCP tools.

<aside>
💡 **Pattern: tools-as-workflows (Brown)**
For our writing agent (Brown), we wrap each workflow entry point as a **coarse-grained MCP tool** (e.g., `generate_article`, `edit_article`, `edit_selected_text`). The MCP tool handler simply **kicks off the corresponding LangGraph run** , returns progress/messages, and finally yields artifacts and diffs. This gives you MCP portability (Cursor, Claude Code) **without** losing LangGraph’s durability and auditability. You’ll learn more about this in the later lessons.
</aside>
<aside>
💡 The developer experience of FastMCP is designed to be simple and Pythonic. You can expose a function as a tool with a single decorator, and FastMCP handles the schema generation and transport details automatically. Here is a quick example from the official documentation [[7]](https://gofastmcp.com/getting-started/quickstart):
</aside>

```python
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
```

With our deep dives complete, we can now synthesize everything into a decision matrix and offer some tentative forecasts.

## Choosing for Your Project: Decision Matrix & Tentative Forecasts

To help you choose the right framework, we have created a decision matrix that maps common project needs to the relative strengths of each library.

Table 1: Decision matrix comparing AI agent frameworks against common needs
| Feature | LangGraph | PydanticAI | OpenAI SDK | AgentKit | CrewAI | AutoGen | FastMCP |
|---|---|---|---|---|---|---|---|
| **Durability/HITL/Replay** | ✅ | | | | ✅ | | |
| **Typed Contracts + Durable Execution** | | ✅ | | | | | ✅ |
| **Few Primitives + Guardrails/Handoffs** | ✅ | | ✅ | ✅ | | | ✅ |
| **Role-based Teams + Quick Scaffolding** | | | | ✅ | ✅ | ✅ | |
| **Exploration Lab** | | ✅ | ✅ | ✅ | ✅ | | |
| **Tool Portability Across Stacks** | | ✅ | | ✅ | | | ✅ |

It is important to remember that the agent framework ecosystem is constantly evolving. Treat this matrix as a snapshot in time and re-evaluate frameworks against the four decision axes whenever a library releases a major update.

Based on these axes, we can offer some forecasts. For reliability-heavy workflows, LangGraph and PydanticAI are strong contenders. For lightweight simplicity, the OpenAI Agents SDK is a good choice, while AgentKit is ideal when visual design and continuous evaluation are required. CrewAI excels at rapid multi-agent prototyping, AutoGen serves as a powerful R&D starting point, and FastMCP is emerging as the universal tooling substrate.

In practice, hybrid patterns are common. You might consume FastMCP tools inside a LangGraph workflow, migrate a prototype from AutoGen Studio to a hardened runtime, or expose a complex graph as a single MCP command to gain IDE portability without sacrificing durability.

To make this theory concrete, we will now share the actual pivots we made while building our course capstones.

## Our Capstone Pivots

Let’s apply this matrix to our capstone project. Our decision-making process evolved as we built, highlighting the importance of choosing the right tool for the job.

Initially, we planned to use LangGraph for both agents. However, we quickly discovered that the research agent, Nova, required a high degree of interactivity and divergent exploration. A rigid, predefined graph was too cumbersome. Research has shown that this kind of task triggers "structural divergence" from a fixed plan, forcing costly "rerouting" and "extended execution" that a static graph handles poorly [[8]](https://arxiv.org/html/2604.27586v1). We found that flexible MCP tools were a much better fit for this exploratory work.

The writing agent, Brown, had the opposite requirements. Its process needed to be repeatable, auditable, and resilient to failure. Here, LangGraph’s strengths shone. Its built-in checkpoints, HITL interrupts, and time-travel replay capabilities were exactly what we needed to ensure a durable and observable workflow.

This led to our final hybrid architecture. Nova is implemented as a FastMCP server, making its research capabilities available to any client, including IDEs. Brown is implemented as a LangGraph workflow, but its entry points are exposed as coarse-grained MCP tools. This gives us the best of both worlds: we gain the portability of MCP without sacrificing the durability and auditability of LangGraph.

We considered the OpenAI Agents SDK, but ultimately deprioritized it because it lacked the first-class persistence and deep MCP integration required for the long-running nature of both capstone tasks. For Brown, we currently expose three coarse-grained tools: `generate_article`, `edit_article`, and `edit_selected_text`.

These real-world pivots illustrate the central lesson of this module.

## Conclusion

The AI agent framework landscape is noisy and fast-moving, but the underlying principles are stable. Instead of chasing transient brand names, you should prioritize stable concepts: stateful graphs for auditability, typed contracts for correctness, durable execution for reliability, and MCP for portability.

Investing time to understand the MCP specification itself is a high-leverage activity. It is a one-time investment that will yield portability across every current and future stack that supports it. A practical selection process should start by applying the four decision axes to your project. Begin with the smallest viable stack that meets your reliability needs, and keep all your tooling portable via MCP.

You can even define a clear migration path for your projects. For example, you might begin exploration in AutoGen Studio, extract successful patterns into FastMCP tools, and then anchor your production system in a reliability-focused framework like LangGraph or PydanticAI.

In our next lesson, we will cover system design, including model selection, cost and latency trade-offs, and HITL placement. Afterward, we will begin the hands-on capstone builds, using the hybrid FastMCP-plus-LangGraph stack we chose through this exact process. You will build Nova with FastMCP and Brown with LangGraph, putting these principles into practice.

## References

*   [1] [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
*   [2] [Durable Execution](https://ai.pydantic.dev/durable_execution/overview/)
*   [3] [FastMCP](https://gofastmcp.com/)
*   [4] [Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
*   [5] [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
*   [6] [AutoGen Studio User Guide](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
*   [7] [Quickstart](https://gofastmcp.com/getting-started/quickstart)
*   [8] [Trace-Level Analysis of Information Contamination in Multi-Agent Systems](https://arxiv.org/html/2604.27586v1)
*   [9] [Running agents on Kubernetes with Agent Sandbox](https://kubernetes.io/blog/2026/03/20/running-agents-on-kubernetes-with-agent-sandbox)
*   [10] [Model Context Protocol (MCP): Real-World Use Cases, Adoptions, and Comparison to Functional Calling](https://medium.com/@laowang_journey/model-context-protocol-mcp-real-world-use-cases-adoptions-and-comparison-to-functional-calling-9320b775845c)
*   [11] [LangGraph Checkpoint Formal Models](https://arxiv.org/pdf/2603.21692)
*   [12] [Debugging Non-Deterministic LLM Agents: Implementing Checkpoint-Based State Replay with LangGraph](https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171)
*   [13] [Agentic AI Needs Temporal for Orchestration](https://intuitionlabs.ai/articles/agentic-ai-temporal-orchestration)