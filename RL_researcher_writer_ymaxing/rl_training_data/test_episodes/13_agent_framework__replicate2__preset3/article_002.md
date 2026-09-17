# Lesson 13: Choosing Your AI Agent Framework

In our last lesson, we introduced the scope and design of our two capstone projects: Nova, an adaptable and interactive research agent, and Brown, a reliable and auditable writing agent. Now, we face a critical engineering decision: which frameworks will we use to build them? Choosing incorrectly can lead to brittle abstractions that break under real load, stalled progress in an ecosystem that evolves quickly, or hidden gaps in durability that only appear after weeks of investment. A poor choice can mean the difference between a successful product and a failed prototype.

This lesson provides the principles to make that choice. We will anchor our discussion in the concrete needs of our capstones, focusing on two core concepts that will recur throughout: LangGraph's interrupts and checkpoints for Brown's resumable auditability, and the Model Context Protocol (MCP) as a universal interoperability layer that keeps Nova's tools portable.

Our reference architecture, shown in Image 1, reflects this split. The research agent is a lightweight MCP server that any client can steer, while the writing agent is a durable workflow that exposes its capabilities as coarse-grained MCP tools. This lesson will explore the philosophies, core abstractions, and production trade-offs that led us to this design. We will focus on decision principles, not just API syntax, to give you a mental model for evaluating any framework.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down>
Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

With the capstones as our concrete reference, we can now examine why framework selection under uncertainty so often fails and what layers—runtime, protocol, and tooling—actually solve which problems.

## Framework Choice Under Uncertainty

The AI agent ecosystem is new and changing rapidly; no single framework will satisfy every use case. To choose wisely, you must distinguish between three layers that are often conflated: the runtime, the protocol, and the tooling framework. Each layer solves a distinct production problem.

The **runtime** (e.g., LangGraph, CrewAI) delivers durable execution and state management, handling orchestration, security, and integration [[35]](https://www.guild.ai/glossary/ai-agent-runtime). It is the engine that keeps an agent running, recoverable, and isolated from other agents in a shared production environment [[34]](https://www.augmentcode.com/guides/agent-runtime-infrastructure-layer). The **protocol**, like MCP, prevents tool lock-in by standardizing how agents and tools communicate. This is a lesson learned from the ad-hoc nature of early function-calling integrations, which created fragmented and difficult-to-maintain systems [[75]](https://arxiv.org/html/2505.02279v1). Finally, the **tooling framework** (e.g., FastMCP) provides the scaffolding to implement that protocol, supplying ready-to-deploy transports, authentication, and a smooth developer experience.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down>
Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

Engineers who select frameworks based on hype or simple demos often run into trouble. A framework might lack the reliability primitives for a production workload, or it might introduce unnecessary complexity for an exploratory task. This mismatch leads to common failure modes. For example, choosing a lightweight framework for a financial compliance agent might result in a system that cannot be audited or recovered after a crash. Conversely, using a heavy, graph-based framework for a simple chatbot adds needless overhead. This distinction between interactive and deterministic workloads is a crucial first lens for assessing fit.

We learned this firsthand. We initially planned to build our research agent, Nova, with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was the wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, Brown, which required a repeatable, auditable process, we did the opposite. We used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes Instead of Brands

To avoid these traps, you need to evaluate frameworks based on principles, not brands. We use four decision axes to analyze any library and determine its fit for a project.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down>
Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

### Control-Flow Explicitness vs. LLM-Driven Autonomy

This axis measures the trade-off between deterministic control and flexible autonomy. Graph-based frameworks like LangGraph offer explicit nodes and edges, providing clear auditability and control over every state transition. This is ideal for repeatable workflows where you need to know precisely why the system made a decision. In contrast, lightweight agent loops, like those in the OpenAI Agents SDK, favor exploration and adaptability. This is better for tasks where the path to a solution is not known in advance. The key question is whether your application requires auditable, repeatable steps or needs to navigate an unpredictable environment. For our capstones, Brown needs explicitness, while Nova needs autonomy.

### Reliability Primitives

Production systems fail. A good framework provides tools to handle those failures gracefully. These are not just technical features but governance necessities. Regulatory frameworks like the EU AI Act demand auditable trails and human oversight, making features like checkpointing, time-travel replay, and Human-in-the-Loop (HITL) interrupts critical for compliance [[76]](https://www.nice.com/agentic-ai/agentic-ai-governance-frameworks). LangGraph, for instance, emphasizes interrupts and persistence for building resumable workflows [[32]](https://docs.langchain.com/oss/python/langgraph/persistence). PydanticAI integrates with systems like Temporal and DBOS for durable execution, ensuring that long-running tasks can survive restarts [[4]](https://ai.pydantic.dev/durable_execution/overview/). These features are non-negotiable for our writing agent but less critical for the more ephemeral research agent.

### Abstraction Level and Developer Experience

Frameworks exist on a spectrum of abstraction. Some, like the OpenAI Agents SDK, provide minimal primitives and require more boilerplate but deliver greater flexibility and control. This approach is powerful if you understand the underlying mechanics and want to own the logic. Others, like CrewAI, offer opinionated constructs such as "Crews" and "Flows" that accelerate initial development but can reduce adaptability when edge cases arise. The right choice depends on whether your team values granular control over the agent's reasoning loop or prefers a more structured, scaffolded approach to get started quickly.

### Tooling Interoperability

Protocols are essential for this purpose. MCP functions as the USB-C of AI, providing a standard interface for tools. This lets you write tools once as MCP servers. For example, with FastMCP, you can create tools that can be reused across any runtime that speaks the protocol, including LangGraph, the OpenAI Agents SDK, or even IDEs like Cursor [[14]](https://gofastmcp.com/). This portability prevents vendor lock-in and ensures your tools can outlive any single framework. It decouples the "what" (the tool's capability) from the "how" (the runtime that orchestrates it).

Our capstone projects map clearly to these axes. The research agent requires autonomy and interoperable tools for its exploratory nature, making a lightweight loop with MCP a good fit. The writing agent demands an explicit, auditable workflow with strong reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks.

**LangGraph** is built on a stateful graph model with native checkpoints and interrupts for auditable workflows [[32]](https://docs.langchain.com/oss/python/langgraph/persistence). This makes it ideal for processes that need to be resumable and traceable, like our writing agent [[61]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). Its design philosophy centers on providing explicit control over state transitions, which is critical for building reliable, production-grade systems. This focus on durability and observability has resonated with developers, as reflected in its strong and consistent adoption, with daily downloads averaging between 400,000 and 500,000.

<aside>
💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers), **LangGraph** focuses specifically on **structured, stateful workflows**. It introduces graph-based execution with checkpoints and resumability, features not native to standard LangChain chains. In short, LangChain is the toolbox; LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions [[61]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). You will see LangChain code in the writing agent.
</aside>

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down>
Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.

The **OpenAI Agents SDK** takes a different approach, favoring a minimal surface area of agents, tools, guardrails, handoffs, and sessions [[15]](https://openai.github.io/openai-agents-python/). It uses lightweight, Python-native loops instead of compiled state machines, giving developers direct control over the execution flow. This philosophy appeals to those who prefer to build orchestration logic with familiar programming constructs. The library has seen steady adoption, with 90,000 to 120,000 daily downloads recently.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down>
Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.

**AgentKit** is a modular toolkit for building and deploying agents on the OpenAI platform. It unifies a visual builder, connectors (including MCP), a ChatKit for embedding UIs, and evaluation infrastructure, allowing developers to visually compose multi-agent systems and manage them through a full lifecycle [[17]](https://openai.com/index/introducing-agentkit).

<aside>
💡 OpenAI AgentKit vs. OpenAI Agents SDK

The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK. It adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**. In short, the SDK is the coding foundation; AgentKit is the integrated platform for design, deployment, and optimization.
</aside>

**CrewAI** features a dual architecture: role-based autonomous crews for collaborative exploration and event-driven flows for deterministic control [[2]](https://docs.crewai.com/introduction), [[1]](https://docs.crewai.com/guides/flows/first-flow). It emphasizes a strong developer experience with a CLI and YAML-based definitions. Its daily downloads range between 40,000 and 100,000, indicating a solid user base interested in its multi-agent coordination patterns.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down>
Image 6: Source: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.

**PydanticAI** prioritizes type safety and schema-driven validation. It offers durable execution through integrations with systems like Temporal, DBOS, and Prefect, along with built-in graph support. Its adoption is growing rapidly, with daily downloads doubling to 300,000-450,000 in the last quarter, suggesting a strong demand for its reliability-focused features.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down>
Image 7: Source: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.

**AutoGen** from Microsoft uses a layered approach. Its Studio GUI is positioned for exploration, with ideas hardened into code using the AgentChat or core libraries [[5]](https://microsoft.github.io/autogen/stable/). This allows for a smooth transition from no-code prototyping to production-grade systems.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down>
Image 8: Source: pepy.tech, daily downloads for autogen, accessed October 15, 2025.

The **Claude Agent SDK** is a newer entrant from Anthropic. It offers tight integration with the Claude model family, leveraging its strengths in large context and tool use, but currently has a smaller ecosystem.

Finally, **FastMCP** is a non-runtime tooling layer for building MCP-compliant servers and clients. It makes tools portable across any runtime or IDE. Its growth has been explosive, surging to over 1.2 million daily downloads, highlighting the critical need for interoperability.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down>
Image 9: Source: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.

Adoption metrics like download trends and GitHub stars can serve as a proxy for maturity, ecosystem health, and hiring risk. However, stars often measure initial curiosity more than sustained production use [[66]](https://medium.com/@rosgluk/the-ai-agent-star-race-i-pulled-live-github-data-for-20-frameworks-in-may-2026-b4919dfba5e4).

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down>
Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026. (Source: [The AI Agent Star Race](https://medium.com/@rosgluk/the-ai-agent-star-race-i-pulled-live-github-data-for-20-frameworks-in-may-2026-b4919dfba5e4))

No single framework is a silver bullet. In practice, hybrid patterns are common, such as consuming FastMCP tools inside a LangGraph workflow. We will now deep-dive into each framework, using our four axes and capstone needs as constant evaluation lenses.

## Framework Deep Dive: LangGraph

LangGraph uses a graph-based model where nodes are Python functions and edges are explicit transitions. This design makes complex, multi-step logic transparent and auditable, which is essential for our writing agent, Brown. Its core production primitives are what set it apart for reliable systems. These include interrupts for human-in-the-loop validation, persistence and checkpointing for resumability, and time-travel debugging that lets you replay and branch from any prior state. This effectively turns the workflow into a deterministic and replayable state machine [[32]](https://docs.langchain.com/oss/python/langgraph/persistence), [[77]](https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171).

The framework offers two definition styles: a "graph API" for fully explicit graphs and a decorator-based "functional API" [[56]](https://www.langchain.com/blog/introducing-the-langgraph-functional-api). The graph API provides maximum control and visibility, making it ideal for complex, auditable systems. The functional API offers a lower-friction entry point by allowing you to define workflows using standard Python functions and control flow. However, both styles compile to the same underlying durable runtime, providing a smooth path from simple scripts to robust, stateful graphs.

While LangGraph can be overkill for simple, exploratory scripts where lighter loops are more efficient, its modeling investment is justified for repeatable, auditable processes like Brown's. Compared to lighter, more autonomous loops, LangGraph's steeper upfront modeling cost buys you built-in safety, observability, and durability. These features are critical for preventing the kind of brittle failures that plague many agentic systems in production. Having examined this graph-centric, reliability-first option, we now turn to a deliberately minimal alternative.

## Framework Deep Dive: OpenAI Agents SDK

The OpenAI Agents SDK embodies a philosophy of minimal primitives, reducing the conceptual surface area to a few core components while enabling powerful agentic applications [[15]](https://openai.github.io/openai-agents-python/). Its design favors a lightweight, Python-first approach that gives developers fine-grained control without imposing a heavy orchestration stack.

Its core concepts interrelate to form a simple but effective system:
-   **Agents** are the central actors. They are LLMs equipped with instructions and tools.
-   **Tools** are Python functions that agents call to interact with the outside world.
-   **Guardrails** provide a mechanism for validating agent inputs and outputs to ensure safety and correctness.
-   **Handoffs** allow one agent to delegate a task to another, more specialized agent.
-   **Sessions** automatically manage conversation history across multiple turns, providing a simple memory layer.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down>
Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.

The fundamental difference between the OpenAI Agents SDK and LangGraph’s functional API lies in the execution model. The OpenAI SDK uses a simple, Python-native agent loop that you control directly. Orchestration is handled with standard Python code like `if/else` statements and `for` loops. In contrast, even with its decorator-based functional API, LangGraph compiles your code into an explicit, stateful graph. This underlying state machine manages execution, persistence, and interruptions, providing a more robust but also more constrained environment.

The SDK is a strong choice for teams who want a fast path to production with lightweight orchestration and sensible defaults. However, it comes with a reliability trade-off. This trade-off has concrete consequences in production. An agent that crashes mid-task loses all progress, as there is no built-in failure recovery. In concurrent setups, this can also lead to duplicate work [[78]](https://www.diagrid.io/solutions/openai-agents-production). Features like durable pause, resume, and checkpointing are not provided out of the box and must be implemented by the team. The natural extension of this minimal SDK is a full-lifecycle platform built on top of it.

## Framework Deep Dive: AgentKit

AgentKit is a complete lifecycle toolkit layered on the OpenAI Agents SDK, covering design, deployment, and optimization [[17]](https://openai.com/index/introducing-agentkit). It extends the SDK by adding a visual workflow designer, UI embedding tools, and a comprehensive evaluation infrastructure, transforming it from a code-first library into an end-to-end platform for building and managing agents.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down>
Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.

Its key components provide an end-to-end development experience:
-   **Agent Builder**: A drag-and-drop canvas for designing and versioning multi-agent workflows. It supports preview runs, inline evaluation, and guardrails, allowing for rapid iteration.
-   **Connector Registry**: A centralized interface for managing data connections, including Dropbox, Google Drive, and third-party MCPs, which simplifies data governance.
-   **ChatKit**: A toolkit for embedding agentic chat UIs directly into your products, handling streaming, threads, and custom theming.
-   **Evals and Reinforcement Fine-Tuning**: A suite of tools for measuring, grading, and improving agent performance through datasets, automated prompt optimization, and custom graders.

AgentKit sits one layer above the OpenAI Agents SDK. You still use the SDK for code-first orchestration, but AgentKit provides the surrounding tools for design, deployment, and continuous improvement. This visual composition, combined with built-in evaluation, supports the development of safe, multi-agent systems at scale without forcing everything into code. The trade-off is its optimization for the OpenAI ecosystem. While its growing MCP connector support improves interoperability, it also introduces security risks like data leakage from untrusted third-party servers [[79]](https://labs.zenity.io/p/analyzing-the-security-risks-of-openai-s-agentkit). AgentKit adds clear value for teams that need no-code workflow design, versioning, and continuous improvement loops.

We now examine a framework whose duality spans both autonomous crews and structured flows.

## Framework Deep Dive: CrewAI

CrewAI introduces a powerful duality with its two main concepts: **Crews** and **Flows** [[2]](https://docs.crewai.com/introduction). This dual architecture allows you to balance autonomy with control, making it a flexible choice for a range of applications.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcc81dc-f35c-4a6b-95e8-557db10090a9/e0cb631a-91ae-46fc-a332-d5e1afd61c80/w=1920,quality=90,fit=scale-down>
Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`.

-   **Crews** are for role-based, autonomous collaboration. You define agents with specific roles (e.g., "researcher," "writer"), goals, and tools, and they work together to solve a problem, much like a human team. This model has roots in multi-agent systems from robotics, where agents with distinct roles coordinate on complex tasks [[80]](https://arxiv.org/html/2502.14743v2). This is ideal for tasks requiring emergent, collaborative problem-solving.
-   **Flows** are for event-driven, deterministic orchestration [[1]](https://docs.crewai.com/guides/flows/first-flow). They give you fine-grained control over the workflow, allowing you to define precise execution paths with standard Python code, manage state, and integrate with external systems.

A typical development pattern is to start with an autonomous crew for rapid prototyping and then introduce a flow to add structure and control as requirements become more defined. CrewAI emphasizes developer experience with CLI scaffolding, YAML definitions for agents and tasks, and configurable memory options. It shines in multi-agent handoff scenarios, like a researcher-to-writer pipeline, where role clarity accelerates development. The trade-off is that its opinionated constructs, while speeding up initial work, can introduce configuration overhead and reduce flexibility when dealing with edge cases.

Next, we will look at a framework that approaches the problem through the lens of type safety.

## Framework Deep Dive: PydanticAI

PydanticAI brings a FastAPI-like philosophy to agent development, where Pydantic models and type hints create compile-time contracts between your code and the LLM's behavior. This focus on type safety ensures that data flowing through your agent system is always valid and well-structured.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/0454e524-5d87-4288-82d4-3abd2b78a6f2/image/w=1920,quality=90,fit=scale-down>
Image 14: Diagram illustrating PydanticAI's design philosophy.

Its production-oriented features are a key differentiator. It offers **durable execution integrations** with platforms like Temporal, DBOS, and Prefect. This allows agents to survive restarts, pause for human input, and resume long-running tasks with a full audit history managed by the external runtime [[4]](https://ai.pydantic.dev/durable_execution/overview/), [[81]](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal). It also has built-in **graph support** for defining non-linear workflows. The developer experience is enhanced by automatic schema generation from type hints and docstrings, along with structured output that includes automatic retries on validation failure.

While the upfront investment in defining schemas can present a learning curve for teams new to strict typing, it pays off in correctness guarantees. PydanticAI is best suited for projects where structured data integrity and long-running, resumable tasks are paramount, aligning well with the auditability needs of our writing agent, Brown.

We now look at a layered system that explicitly separates experimentation from production.

## Framework Deep Dive: AutoGen

AutoGen, from Microsoft, is designed with a layered architecture that deliberately separates experimentation from production hardening [[5]](https://microsoft.github.io/autogen/stable/). This structure allows teams to move from rapid, no-code prototyping to robust, production-grade implementations within a single ecosystem.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down>
Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.

The framework consists of three primary layers:
-   **AutoGen Studio** is a low-code GUI that lets you prototype multi-agent workflows without writing code. You can visually compose agents, configure their tools, and test their interactions in a playground environment [[6]](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html).
-   **AgentChat** is a programming framework for building conversational multi-agent applications. It provides higher-level abstractions for common patterns, making it easier to get started with code.
-   **Core** provides low-level, event-driven primitives for building scalable, custom agent systems from the ground up, offering maximum control and flexibility.

The typical workflow involves exploring and validating ideas visually inside Studio, then hardening the successful patterns into production-ready code using the AgentChat and Core layers. Microsoft is explicit that Studio is a research prototype and not intended for production use.

AutoGen's strength lies in its use as an R&D laboratory for discovering effective multi-agent conversation patterns, drawing on coordination strategies from fields like robotics [[82]](https://xue-guang.com/post/llm-marl). The trade-off is that this flexibility during exploration requires the development team to re-implement reliability, security, and observability when moving from prototype to production.

A newer entrant to the field focuses on tight integration with its specific model family.

## Framework Deep Dive: Claude Agent SDK

The Claude Agent SDK is a newer entrant from Anthropic that is built on a philosophy of tight integration with its model family. It is designed to leverage the specific strengths of Claude models, such as their large context windows, strong reasoning capabilities, and fine-grained control over tool use.

The SDK focuses on providing an ergonomic tool-calling and orchestration experience tailored specifically to the Anthropic stack. However, as a newer framework, it comes with the trade-offs of a smaller community, fewer third-party integrations, and a rapidly evolving API surface.

This presents a choice between opportunity and risk. Early adoption can yield performance benefits that are highly optimized for Claude models, but teams must balance this against the maturity of the surrounding ecosystem. The clearest use case is for teams already committed to the Anthropic stack who want native performance and are willing to accept smaller community support in exchange.

The final deep dive examines a non-runtime layer that complements every option above.

## Framework Deep Dive: FastMCP

FastMCP is not a runtime; it is a tooling framework for building applications based on the Model Context Protocol (MCP) [[14]](https://gofastmcp.com/). Its role is to make tools, resources, and prompts portable across any runtime or IDE that speaks the protocol. This separation of concerns is a powerful architectural pattern that promotes modularity and reusability.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/745828fd-27e2-4a50-b613-7275a1e1dceb/image/w=1920,quality=90,fit=scale-down>
Image 16: FastMCP Architecture and Interoperability

The primary benefit of this approach is interoperability. You can write a tool once as an MCP server and reuse it inside LangGraph, the OpenAI SDK, Cursor, or any future compatible system without rewriting it. At scale, however, MCP servers can face challenges like connection timeouts or stalls from oversized responses, requiring monitoring in production [[83]](https://www.fiddler.ai/blog/mcp-agent-observability). Beyond the protocol itself, FastMCP also provides production-oriented extensions for authentication, server composition, and cloud deployment.

Our capstone projects use this pattern. The research agent, Nova, is implemented as a FastMCP server that any client can steer. The writing agent, Brown, exposes its complex LangGraph workflows as coarse-grained MCP tools.

<aside>
💡 Pattern: tools-as-workflows (Brown)

For our writing agent (Brown), we wrap each workflow entry point as a **coarse-grained MCP tool** (e.g., `generate_article`, `edit_article`, `edit_selected_text`). The MCP tool handler simply **kicks off the corresponding LangGraph run**, returns progress/messages, and finally yields artifacts and diffs. This gives you MCP portability (Cursor, Claude Code) **without** losing LangGraph’s durability and auditability. You’ll learn more about this in later lessons.
</aside>

The developer experience is designed to be simple and Pythonic. You can expose a function as a tool with a single decorator, and FastMCP handles the schema generation and transport details automatically [[16]](https://gofastmcp.com/getting-started/quickstart).

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

With our deep dives complete, we can now synthesize everything into a decision matrix and offer some tentative forecasts.

## Choosing for Your Project: Decision Matrix & Tentative Forecasts

To help you choose, the following matrix maps common project needs to the relative strengths of each framework.

Table 1: Decision matrix comparing AI agent frameworks against common needs
| Feature | LangGraph | PydanticAI | OpenAI SDK | AgentKit | CrewAI | AutoGen | FastMCP |
|---|---|---|---|---|---|---|---|
| **Durability/HITL/Replay** | ✅ | | | | | ✅ | |
| **Typed Contracts + Durable Execution** | | ✅ | | | | | ✅ |
| **Few Primitives + Guardrails/Handoffs** | ✅ | | ✅ | ✅ | | | ✅ |
| **Role-based Teams + Quick Scaffolding** | | | | ✅ | ✅ | ✅ | |
| **Exploration Lab** | | | ✅ | ✅ | ✅ | ✅ | |
| **Tool Portability Across Stacks** | | ✅ | | ✅ | | | ✅ |

Treat this matrix as a snapshot. The ecosystem is evolving, so you should always re-evaluate new releases against the four decision axes.

Based on this, we can make some forecasts. We expect that frameworks with strong reliability primitives, like LangGraph and PydanticAI, will become dominant for enterprise-critical workflows where auditability and durability are non-negotiable. The OpenAI SDK will likely remain popular for its lightweight simplicity, especially for projects tightly integrated with the OpenAI ecosystem, while AgentKit will appeal to teams needing visual design and continuous evaluation loops.

CrewAI is well-positioned for rapid multi-agent prototyping, and AutoGen will continue to be a strong starting point for R&D. FastMCP is set to become the universal tooling substrate that connects them all. In practice, hybrid patterns are becoming standard. For example, a team might use AutoGen for initial discovery, build the discovered tools with FastMCP, and orchestrate the final production workflow with LangGraph. This modular approach allows you to leverage the strengths of each framework while mitigating their weaknesses.

To make this theory concrete, we will now share the actual pivots we made while building our capstones.

## Our Capstone Pivots

Let’s apply this matrix to our capstone projects. Our decision-making process evolved as we built, highlighting the importance of choosing the right tool for the job.

We initially planned to use LangGraph for both agents. However, we quickly found that the research agent, Nova, needed a high degree of interactivity and divergent exploration. A rigid graph was too cumbersome. For Nova, the "LLM-driven autonomy" axis was paramount. The initial LangGraph choice was too far on the "control-flow explicitness" side. Flexible MCP tools, which allowed us to change direction on the fly, proved to be a much better fit. The pivot to a lightweight loop with MCP tools moved it to the correct point on the spectrum.

The writing agent, Brown, had the opposite requirements. Its process needed to be repeatable and auditable. Here, the "reliability primitives" axis was the deciding factor. LangGraph's features were essential. Its checkpoints, HITL interrupts, and time-travel replay capabilities gave us the control and observability we needed to ensure a reliable workflow.

We considered the OpenAI Agents SDK for both projects but ultimately deprioritized it. For Brown, the lack of first-class persistence was a dealbreaker. The SDK has no built-in durability layer, meaning a crash during a long-running writing task would lose all progress [[78]](https://www.diagrid.io/solutions/openai-agents-production). For a system that requires auditability and resumability, building this layer from scratch would have been a significant engineering effort. For Nova, while the lightweight loop was appealing, the SDK's MCP integration was not as deep as what we could achieve with FastMCP, which was critical for our goal of tool portability.

This led to our hybrid architecture: Nova is implemented as a FastMCP server that any client can steer, while Brown is a LangGraph workflow whose entry points are exposed as coarse-grained MCP tools. This pattern of wrapping complex internal workflows behind single MCP commands is powerful. It gives you portability without sacrificing durability or auditability, which can be measured by throughput and latency metrics under load [[84]](https://mcp-server-langgraph.mintlify.app/comparisons/benchmarks). Brown currently exposes three tools: `generate_article`, `edit_article`, and `edit_selected_text`.

These real-world pivots illustrate the central lesson of this module.

## Conclusion

The AI agent framework landscape is noisy and rapidly changing. The key to navigating it is to prioritize stable concepts over transient brand names. Focus on stateful graphs, typed contracts, durable execution, and MCP standardization. These are the principles that will endure and provide a solid foundation for your work, regardless of which new framework appears next week.

Investing time to understand the MCP specification itself is a high-leverage activity. It is a one-time investment that yields tool portability across every current and future stack that supports it. This allows you to build a library of reusable, interoperable tools that are decoupled from any single runtime, future-proofing your agentic systems.

Our practical selection process is this: apply the four decision axes to your project, start with the smallest viable stack that meets your reliability needs, and keep all your tooling portable via MCP. A common migration path might start with exploration in AutoGen Studio, then extract successful patterns into FastMCP tools, and finally anchor the production system in a durable runtime like LangGraph or PydanticAI. This phased approach allows for rapid iteration while ensuring a clear path to a robust, production-ready system. It transforms framework selection from a gamble on a brand into a deliberate engineering decision based on first principles.

In our next lesson, we will cover system design, including model selection, cost-latency trade-offs, and HITL placement. Afterward, we will begin the hands-on builds of our capstones. We will build Nova with FastMCP, covering the server/client implementation, data ingestion, Perplexity-driven research loops, filtering, and artifact generation into `research.md`. We will then build Brown using our hybrid LangGraph and FastMCP stack, implementing the full workflow with MCP tools, context engineering for profiles, evaluator-optimizer review cycles, and HITL editing.

## References

- [1] Build your first Flow (https://docs.crewai.com/guides/flows/first-flow)
- [2] Introduction (https://docs.crewai.com/introduction)
- [3] Quickstart (https://docs.crewai.com/quickstart)
- [4] Durable Execution (https://ai.pydantic.dev/durable_execution/overview/)
- [5] AutoGen (https://microsoft.github.io/autogen/stable/)
- [6] AutoGen Studio User Guide (https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- [7] Persistence (https://docs.langchain.com/oss/python/langgraph/persistence)
- [8] LLM-Driven Autonomy (https://www.emergentmind.com/topics/llm-driven-autonomy)
- [9] ControlFlow 0.9: Take control of your agents (https://www.prefect.io/blog/controlflow-0-9-take-control-of-your-agents)
- [10] A Survey on Large Language Model Based Autonomous Agents (https://arxiv.org/html/2508.17281v2)
- [11] Agent Frameworks (https://arize.com/ai-agents/agent-frameworks)
- [12] AutoGen v0.4: Reimagining the foundation of agentic AI for scale, extensibility, and robustness (https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness)
- [13] AutoGen (https://www.ibm.com/think/topics/autogen)
- [14] FastMCP (https://gofastmcp.com/)
- [15] OpenAI Agents SDK (https://openai.github.io/openai-agents-python/)
- [16] Quickstart (https://gofastmcp.com/getting-started/quickstart)
- [17] Introducing AgentKit (https://openai.com/index/introducing-agentkit)
- [18] OpenAI AgentKit: The Complete Guide for Developers (https://www.digitalapplied.com/blog/openai-agentkit-complete-guide)
- [19] OpenAI AgentKit and Agent Builder: Building Secure AI Agents (https://www.nudgesecurity.com/post/openai-agentkit-and-agent-builder-building-secure-ai-agents)
- [20] OpenAI’s AgentKit Review (https://medium.com/@leucopsis/openais-agentkit-review-c83bee3c3d02)
- [21] OpenAI Agent Builder: Step-by-step guide to building AI agents with MCP (https://composio.dev/content/openai-agent-builder-step-by-step-guide-to-building-ai-agents-with-mcp)
- [22] How does FastMCP enable tool portability across runtimes like LangGraph? (https://generect.com/blog/langgraph-mcp)
- [23] Tools (https://gofastmcp.com/servers/tools)
- [24] fastmcp (https://github.com/PrefectHQ/fastmcp)
- [25] Pydantic AI (https://realpython.com/pydantic-ai)
- [26] The Complete Guide to Using Pydantic for Validating LLM Outputs (https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs)
- [27] Introduction to Pydantic (https://education.molssi.org/type-hints-pydantic-tutorial/chapters/IntroToPydantic.html)
- [28] Validators (https://pydantic.dev/docs/validation/latest/concepts/validators)
- [29] Pydantic: A Data Engineer’s Guide to Data Validation (https://pub.towardsai.net/pydantic-a-data-engineers-guide-to-data-validation-ca88a8d9bb2f)
- [30] Interrupts (https://docs.langchain.com/oss/javascript/langgraph/interrupts)
- [31] interrupt (https://reference.langchain.com/python/langgraph/types/interrupt)
- [32] Persistence (https://docs.langchain.com/oss/python/langgraph/persistence)
- [33] Most people still lump everything into “agent frameworks”... (https://www.linkedin.com/posts/brijpandeyji_most-people-still-lump-everything-into-agent-activity-7409465945489829888-8sk5)
- [34] The Missing Layer: Agent Execution Runtimes (https://www.augmentcode.com/guides/agent-runtime-infrastructure-layer)
- [35] AI Agent Runtime (https://www.guild.ai/glossary/ai-agent-runtime)
- [36] Agent Frameworks (https://arize.com/ai-agents/agent-frameworks)
- [37] What does the emerging AI agent stack actually look like? (https://forum.langchain.com/t/what-does-the-emerging-ai-agent-stack-actually-look-like/3103)
- [38] AI Agent Frameworks (https://www.langchain.com/resources/ai-agent-frameworks)
- [39] How to think about agent frameworks (https://www.langchain.com/blog/how-to-think-about-agent-frameworks)
- [40] A Developer’s Guide to Agentic Frameworks in 2026 (https://pub.towardsai.net/a-developers-guide-to-agentic-frameworks-in-2026-3f22a492dc3d)
- [41] Mastering the OpenAI Agents SDK: A Field Guide for Busy Developers & AI VPs (https://cohorte.co/blog/mastering-the-openai-agents-sdk-a-field-guide-for-busy-developers-ai-vps)
- [42] Agents (https://openai.github.io/openai-agents-python/agents)
- [43] Migrating from OpenAI Agents SDK (https://platform.claude.com/cookbook/claude-agent-sdk-04-migrating-from-openai-agents-sdk)
- [44] Guardrails (https://openai.github.io/openai-agents-python/guardrails)
- [45] Agents (https://developers.openai.com/api/docs/guides/agents)
- [46] The Ultimate Guide to AI Agent Frameworks (https://www.morphllm.com/ai-agent-framework)
- [47] Building Intelligent Agents with Claude Agent SDK (https://www.c-sharpcorner.com/article/building-intelligent-agents-with-claude-agent-sdk-features-comparisons-and-be)
- [48] Agent SDK vs. Framework: Claude, Pydantic AI, and the Future of Agentic Development (https://www.mindstudio.ai/blog/agent-sdk-vs-framework-claude-pydantic-ai)
- [49] Inside the Claude Agent SDK (https://buildwithaws.substack.com/p/inside-the-claude-agent-sdk-from)
- [50] Claude Agent SDK: Building Agents That Work (https://aankitroy.com/blog/claude-agent-sdk-building-agents-that-work)
- [51] What are Crews vs. Flows in CrewAI? (https://www.c-sharpcorner.com/article/what-are-crews-vs-flows-in-crewai)
- [52] CrewAI's Unique Features (https://vadim.blog/crewai-unique-features)
- [53] crewai (https://github.com/crewaiinc/crewai)
- [54] Flows (https://docs.crewai.com/en/concepts/flows)
- [55] Choosing between Graph and Functional APIs in LangGraph (https://www.linkedin.com/posts/khalid-husain-3002aa216_choosing-between-graph-and-functional-apis-activity-7396757303217029120-VIK3)
- [56] Introducing the LangGraph Functional API (https://www.langchain.com/blog/introducing-the-langgraph-functional-api)
- [57] Introducing the LangGraph Functional API (https://blog.langchain.com/introducing-the-langgraph-functional-api)
- [58] Choosing APIs (https://docs.langchain.com/oss/python/langgraph/choosing-apis)
- [59] Functional API for LangGraph (https://changelog.langchain.com/announcements/functional-api-for-langgraph)
- [60] LangChain vs. LangGraph: Which One to Choose? (https://www.truefoundry.com/blog/langchain-vs-langgraph)
- [61] Workflows and agents (https://docs.langchain.com/oss/python/langgraph/workflows-agents)
- [62] LangChain vs. LangGraph: A Deep Dive into AI Application Frameworks (https://duplocloud.com/blog/langchain-vs-langgraph)
- [63] LangChain vs. LangGraph vs. LangSmith vs. LangFlow: A Complete Guide (https://www.datacamp.com/tutorial/langchain-vs-langgraph-vs-langsmith-vs-langflow)
- [64] LangChain vs LangGraph (https://www.geeksforgeeks.org/artificial-intelligence/langchain-vs-langgraph)
- [65] LangChain vs. LangGraph: Which Framework to Choose for Your LLM Application (https://milvus.io/blog/langchain-vs-langgraph.md)
- [66] The AI Agent Star Race: I Pulled Live GitHub Data for 20 Frameworks in May 2026 (https://medium.com/@rosgluk/the-ai-agent-star-race-i-pulled-live-github-data-for-20-frameworks-in-may-2026-b4919dfba5e4)
- [67] Top 10 Most Starred AI Agent Frameworks on GitHub (2026) (https://techwithibrahim.medium.com/top-10-most-starred-ai-agent-frameworks-on-github-2026-df6e760a950b)
- [68] A Comprehensive Study of GitHub Issues in Python-based Agent Frameworks (https://arxiv.org/html/2510.25423v2)
- [69] AI Agent Frameworks Download Spikes (https://www.youtube.com/watch?v=2Yg-BPFNF5A&vl=en-US)
- [70] Agentic UAVs: An LLM-driven Framework for Autonomous Drone Operations (https://arxiv.org/html/2509.13352v2)
- [71] Agent Frameworks (https://arize.com/ai-agents/agent-frameworks)
- [72] Microsoft AutoGen: Orchestrating Multi-Agent LLM Systems (https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems)
- [73] Getting Started with AutoGen Framework for Building AI Agents and Applications (https://ravichaganti.com/blog/getting-started-with-autogen-framework-for-building-ai-agents-and-applications)
- [74] A Friendly Introduction to the AutoGen Framework (https://newsletter.victordibia.com/p/a-friendly-introduction-to-the-autogen)
- [75] A Survey of Agent Interoperability Protocols: Model Context Protocol (MCP), Agent Communication Protocol (ACP), Agent-to-Agent Protocol (A2A), and Agent Network Protocol (ANP) (https://arxiv.org/html/2505.02279v1)
- [76] Agentic AI Governance Frameworks (https://www.nice.com/agentic-ai/agentic-ai-governance-frameworks)
- [77] Debugging Non-Deterministic LLM Agents: Implementing Checkpoint-Based State Replay with LangGraph (https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171)
- [78] Running OpenAI Agents in Production (https://www.diagrid.io/solutions/openai-agents-production)
- [79] Analyzing the Security Risks of OpenAI’s AgentKit (https://labs.zenity.io/p/analyzing-the-security-risks-of-openai-s-agentkit)
- [80] Large Language Model based Multi-Agents: A Survey of Progress and Challenges (https://arxiv.org/html/2502.14743v2)
- [81] Orchestrating ambient agents with Temporal (https://temporal.io/blog/orchestrating-ambient-agents-with-temporal)
- [82] LLM-based Multi-Agent Cooperation: A Survey (https://xue-guang.com/post/llm-marl)
- [83] MCP Agent Observability (https://www.fiddler.ai/blog/mcp-agent-observability)
- [84] Benchmarks (https://mcp-server-langgraph.mintlify.app/comparisons/benchmarks)