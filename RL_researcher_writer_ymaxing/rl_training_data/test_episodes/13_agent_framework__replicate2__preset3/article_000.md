# Lesson 13: Choosing Your AI Agent Framework

In our last lesson, we introduced the scope and design of our two capstone projects: Nova, an adaptable and interactive research agent, and Brown, a reliable and auditable writing agent. Now, we face a critical engineering decision: which frameworks will we use to build them? Choosing incorrectly can lead to brittle abstractions that break under real load, stalled progress in a fast-moving ecosystem, or hidden gaps in durability that only appear after weeks of investment.

This lesson is about making that choice with confidence. We will anchor our discussion in the concrete needs of our capstones, focusing on two core concepts that will recur throughout: LangGraph's interrupts and checkpoints for Brown's resumable auditability, and the Model Context Protocol (MCP) as a universal interoperability layer that keeps Nova's tools portable.

Our reference architecture, shown in Image 1, reflects this split. The research agent is a lightweight MCP server that any client can steer, while the writing agent is a durable workflow that exposes its capabilities as coarse-grained MCP tools. This lesson will explore the philosophies, core abstractions, and production trade-offs that led us to this design. We will focus on decision principles, not just API syntax, to give you a mental model for evaluating any framework.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down>
Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

With the capstones as our concrete reference, we can now examine why framework selection under uncertainty so often fails and what layers—runtime, protocol, and tooling—actually solve which problems.

## Framework Choice Under Uncertainty

The AI agent ecosystem is new and evolving quickly; no single framework will satisfy every use case. To choose wisely, you must distinguish between three layers that are often conflated: the runtime, the protocol, and the tooling framework. Each layer solves a distinct production problem. The **runtime** (e.g., LangGraph, CrewAI) delivers durable execution and state management. The **protocol**, like MCP, prevents tool lock-in by standardizing how agents and tools communicate—a lesson learned from the ad-hoc nature of early function-calling integrations [[75]](https://arxiv.org/html/2505.02279v1). The **tooling framework** (e.g., FastMCP) provides the scaffolding—transports, authentication, and developer experience—to implement that protocol.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down>
Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

Engineers who select frameworks based on hype or simple demos often run into trouble. A framework might lack the reliability primitives for a production workload, or it might introduce unnecessary complexity for an exploratory task. This distinction between interactive and deterministic workloads is a crucial first lens for assessing fit.

We learned this firsthand. We initially planned to build our research agent, Nova, with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was the wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, Brown, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes Instead of Brands

To avoid these traps, you need to evaluate frameworks based on principles, not brands. We use four decision axes to analyze any library and determine its fit for a project.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down>
Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

### Control-Flow Explicitness vs. LLM-Driven Autonomy

This axis measures the trade-off between deterministic control and flexible autonomy. Graph-based frameworks like LangGraph offer explicit nodes and edges, providing clear auditability and control over every state transition. This is ideal for repeatable workflows where you need to know precisely why the system made a decision. In contrast, lightweight agent loops, like those in the OpenAI Agents SDK, favor exploration and adaptability, which is better for tasks where the path to a solution is not known in advance. Does your application require auditable steps, or does it need to navigate an unpredictable environment?

### Reliability Primitives

Production systems fail. A good framework provides tools to handle those failures gracefully. These are not just technical features but governance necessities. Regulatory frameworks like the EU AI Act demand auditable trails and human oversight, making features like checkpointing, time-travel replay, and HITL interrupts critical for compliance [[76]](https://www.nice.com/agentic-ai/agentic-ai-governance-frameworks). LangGraph, for instance, emphasizes interrupts and persistence for building resumable workflows [[7]](https://docs.langchain.com/oss/python/langgraph/persistence). PydanticAI integrates with systems like Temporal and DBOS for durable execution [[31]](https://ai.pydantic.dev/durable_execution/overview/). These features are non-negotiable for our writing agent but less critical for the more ephemeral research agent.

### Abstraction Level and Developer Experience

Frameworks exist on a spectrum of abstraction. Some, like the OpenAI Agents SDK, provide minimal primitives and require more boilerplate but deliver greater flexibility. Others, like CrewAI, offer opinionated constructs that accelerate initial development but can reduce adaptability when edge cases arise. The right choice depends on whether your team values granular control or rapid, structured scaffolding.

### Tooling Interoperability

This is where protocols become essential. MCP functions as the USB-C of AI, providing a standard interface for tools. This lets you write tools once as MCP servers—for example, with FastMCP [[14]](https://gofastmcp.com/)—and reuse them across any runtime that speaks the protocol, including LangGraph, the OpenAI Agents SDK, or even IDEs like Cursor. This portability prevents vendor lock-in and ensures your tools can outlive any single framework.

Our capstone projects map clearly to these axes. The research agent requires autonomy and interoperable tools for its exploratory nature, making a lightweight loop with MCP a good fit. The writing agent demands an explicit, auditable workflow with strong reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks.

**LangGraph** is built on a stateful graph model with native checkpoints and interrupts for auditable workflows [[7]](https://docs.langchain.com/oss/python/langgraph/persistence). This makes it ideal for processes that need to be resumable and traceable, like our writing agent [[61]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). It shows strong, consistent adoption, with daily downloads averaging 400K–500K.

<aside>
💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers), **LangGraph** focuses specifically on **structured, stateful workflows**. It introduces graph-based execution with checkpoints and resumability, features not native to standard LangChain chains. In short, LangChain is the toolbox; LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions [[61]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). You will see LangChain code in the writing agent.
</aside>

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down>
Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.

The **OpenAI Agents SDK** takes a different approach, favoring a minimal surface area of agents, tools, guardrails, handoffs, and sessions [[15]](https://openai.github.io/openai-agents-python/). It uses lightweight, Python-native loops instead of compiled state machines. The library has seen 90K–120K daily downloads recently.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down>
Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.

**AgentKit** is a modular toolkit for building and deploying agents on the OpenAI platform. It unifies a visual builder, connectors (including MCP), a ChatKit for embedding UIs, and evaluation infrastructure. This allows developers to visually compose multi-agent systems and manage them through a full lifecycle.

<aside>
💡 OpenAI AgentKit vs. OpenAI Agents SDK

The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK: it adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**. In short, the SDK is the coding foundation; AgentKit is the integrated platform for design, deployment, and optimization.
</aside>

**CrewAI** features a dual architecture: role-based autonomous crews for collaborative exploration and event-driven flows for deterministic control. It emphasizes a strong developer experience with a CLI and YAML-based definitions. Its daily downloads range between 40K and 100K.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down>
Image 6: Source: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.

**PydanticAI** prioritizes type safety and schema-driven validation. It offers durable execution through integrations with systems like Temporal, DBOS, and Prefect, along with built-in graph support. Its adoption is growing rapidly, with daily downloads doubling to 300K-450K in the last quarter.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down>
Image 7: Source: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.

**AutoGen** from Microsoft uses a layered approach. Its Studio GUI is positioned for exploration, with ideas hardened into code using the AgentChat or core libraries [[12]](https://microsoft.github.io/autogen/stable/).

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down>
Image 8: Source: pepy.tech, daily downloads for autogen, accessed October 15, 2025.

The **Claude Agent SDK** is a newer entrant from Anthropic. It offers tight integration with the Claude model family, leveraging its strengths in large context and tool use, but currently has a smaller ecosystem.

Finally, **FastMCP** is a non-runtime tooling layer for building MCP-compliant servers and clients. It makes tools portable across any runtime or IDE. Its growth has been explosive, surging to over 1.2M daily downloads.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down>
Image 9: Source: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.

Adoption metrics like download trends and GitHub stars can serve as a proxy for maturity, ecosystem health, and hiring risk.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down>
Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026.

No single framework is a silver bullet. In practice, hybrid patterns are common, such as consuming FastMCP tools inside a LangGraph workflow. We will now deep-dive into each framework, using our four axes and capstone needs as constant evaluation lenses.

## Framework Deep Dive: LangGraph

LangGraph uses a graph-based model where nodes are Python functions and edges are explicit transitions. This design makes complex, multi-step logic transparent and auditable, which is essential for our writing agent, Brown. Its core production primitives are what set it apart for reliable systems: interrupts for human-in-the-loop validation, persistence and checkpointing for resumability, and time-travel debugging that lets you replay and branch from any prior state, effectively turning the workflow into a deterministic and replayable state machine [[7]](https://docs.langchain.com/oss/python/langgraph/persistence), [[77]](https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171).

The framework offers two definition styles: a "graph API" for fully explicit graphs and a decorator-based "functional API." This creates a trade-off between a steeper learning curve and the payoff of deterministic, observable behavior. While LangGraph can be overkill for simple, exploratory scripts where lighter loops are more efficient, its modeling investment is justified for repeatable, auditable processes like Brown's.

Compared to lighter, more autonomous loops, LangGraph's steeper upfront modeling cost buys you built-in safety, observability, and durability. These features are critical for preventing the kind of brittle failures that plague many agentic systems in production. Having examined this graph-centric, reliability-first option, we now turn to a deliberately minimal alternative.

## Framework Deep Dive: OpenAI Agents SDK

The OpenAI Agents SDK embodies a philosophy of minimal primitives, reducing the conceptual surface area to a few core components while enabling powerful agentic applications [[15]](https://openai.github.io/openai-agents-python/).

Its core concepts interrelate to form a simple but effective system:
-   **Agents** are the central actors—LLMs equipped with instructions and tools.
-   **Tools** are Python functions that agents call to interact with the outside world.
-   **Guardrails** provide a mechanism for validating agent inputs and outputs to ensure safety and correctness.
-   **Handoffs** allow one agent to delegate a task to another, more specialized agent.
-   **Sessions** automatically manage conversation history across multiple turns, providing a simple memory layer.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down>
Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.

The fundamental difference between the OpenAI Agents SDK and LangGraph’s functional API lies in the execution model. The OpenAI SDK uses a simple, Python-native agent loop that you control directly. Orchestration is handled with standard Python code like `if/else` statements and `for` loops. In contrast, even with its decorator-based functional API, LangGraph compiles your code into an explicit, stateful graph. This underlying state machine manages execution, persistence, and interruptions, providing a more robust but also more constrained environment.

The SDK is a strong choice for teams who want a fast path to production with lightweight orchestration and sensible defaults. However, it comes with a reliability trade-off. This trade-off has concrete consequences in production. An agent that crashes mid-task loses all progress, as there is no built-in failure recovery. In concurrent setups, this can also lead to duplicate work [[78]](https://www.diagrid.io/solutions/openai-agents-production). Features like durable pause, resume, and checkpointing are not provided out of the box and must be implemented by the team. The natural extension of this minimal SDK is a full-lifecycle platform built on top of it.

## Framework Deep Dive: AgentKit

AgentKit is a complete lifecycle toolkit layered on the OpenAI Agents SDK, covering design, deployment, and optimization [[17]](https://openai.com/index/introducing-agentkit). It extends the SDK by adding a visual workflow designer, UI embedding tools, and a comprehensive evaluation infrastructure.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down>
Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.

Its key components provide an end-to-end development experience:
-   **Agent Builder**: A drag-and-drop canvas for designing and versioning multi-agent workflows. It supports preview runs, inline evaluation, and guardrails.
-   **Connector Registry**: A centralized interface for managing data connections, including Dropbox, Google Drive, and third-party MCPs.
-   **ChatKit**: A toolkit for embedding agentic chat UIs directly into your products, handling streaming, threads, and custom theming.
-   **Evals and Reinforcement Fine-Tuning (RFT)**: A suite of tools for measuring, grading, and improving agent performance through datasets, automated prompt optimization, and custom graders.

AgentKit sits one layer above the OpenAI Agents SDK. You still use the SDK for code-first orchestration, but AgentKit provides the surrounding tools for design, deployment, and continuous improvement. This visual composition, combined with built-in evaluation, supports the development of safe, multi-agent systems at scale without forcing everything into code. The trade-off is its optimization for the OpenAI ecosystem. While its growing MCP connector support improves interoperability, it also introduces security risks like data leakage from untrusted third-party servers [[79]](https://labs.zenity.io/p/analyzing-the-security-risks-of-openai-s-agentkit). AgentKit adds clear value for teams that need no-code workflow design, versioning, and continuous improvement loops.

We now examine a framework whose duality spans both autonomous crews and structured flows.

## Framework Deep Dive: CrewAI

CrewAI introduces a powerful duality with its two main concepts: **Crews** and **Flows** [[2]](https://docs.crewai.com/introduction). This dual architecture allows you to balance autonomy with control.

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

Its production-oriented features are a key differentiator. It offers **durable execution integrations** with platforms like Temporal, DBOS, and Prefect, allowing agents to survive restarts, pause for human input, and resume long-running tasks with a full audit history managed by the external runtime [[31]](https://ai.pydantic.dev/durable_execution/overview/), [[81]](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal). It also has built-in **graph support** for defining non-linear workflows. The developer experience is enhanced by automatic schema generation from type hints and docstrings, along with structured output that includes automatic retries on validation failure.

While the upfront investment in defining schemas can present a learning curve for teams new to strict typing, it pays off in correctness guarantees. PydanticAI is best suited for projects where structured data integrity and long-running, resumable tasks are paramount, aligning well with the auditability needs of our writing agent, Brown.

We now look at a layered system that explicitly separates experimentation from production.

## Framework Deep Dive: AutoGen

AutoGen, from Microsoft, is designed with a layered architecture that deliberately separates experimentation from production hardening [[12]](https://microsoft.github.io/autogen/stable/).

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down>
Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.

The framework consists of three primary layers:
-   **AutoGen Studio** is a low-code GUI that lets you prototype multi-agent workflows without writing code. You can visually compose agents, configure their tools, and test their interactions in a playground environment [[13]](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html).
-   **AgentChat** is a programming framework for building conversational multi-agent applications. It provides higher-level abstractions for common patterns.
-   **Core** provides low-level, event-driven primitives for building scalable, custom agent systems from the ground up.

The typical workflow involves exploring and validating ideas visually inside Studio, then hardening the successful patterns into production-ready code using the AgentChat and Core layers. Microsoft is explicit that Studio is a research prototype and not intended for production use.

AutoGen's strength lies in its use as an R&D laboratory for discovering effective multi-agent conversation patterns, drawing on coordination strategies from fields like robotics [[82]](https://xue-guang.com/post/llm-marl). The trade-off is that this flexibility during exploration requires the development team to re-implement reliability, security, and observability when moving from prototype to production.

A newer entrant to the field focuses on tight integration with its specific model family.

## Framework Deep Dive: Claude Agent SDK

The Claude Agent SDK is a newer entrant from Anthropic that is built on a philosophy of tight integration with its model family. It is designed to leverage the specific strengths of Claude models, such as their large context windows, strong reasoning capabilities, and fine-grained control over tool use.

The SDK focuses on providing an ergonomic tool-calling and orchestration experience tailored specifically to the Anthropic stack. However, as a newer framework, it comes with the trade-offs of a smaller community, fewer third-party integrations, and a rapidly evolving API surface.

This presents a choice between opportunity and risk. Early adoption can yield performance benefits that are highly optimized for Claude models. Teams must balance this against the maturity of the surrounding ecosystem. The clearest use case is for teams already committed to the Anthropic stack who want native performance and are willing to accept smaller community support in exchange.

The final deep dive examines a non-runtime layer that complements every option above.

## Framework Deep Dive: FastMCP

FastMCP is not a runtime; it is a tooling framework for building applications based on the Model Context Protocol (MCP) [[14]](https://gofastmcp.com/). Its role is to make tools, resources, and prompts portable across any runtime or IDE that speaks the protocol.

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

Based on this, we can make some forecasts. LangGraph and PydanticAI are strong contenders for reliability-heavy workflows. The OpenAI SDK is well-suited for lightweight simplicity, while AgentKit excels when visual design and continuous evaluation are required. CrewAI is a great choice for rapid multi-agent prototyping, and AutoGen remains a powerful R&D starting point. FastMCP serves as the universal tooling substrate that can connect them all.

In practice, hybrid patterns are common. You might consume FastMCP tools inside a LangGraph workflow, migrate from an AutoGen prototype to a hardened runtime, or expose a complex graph as a single MCP command to gain IDE portability without sacrificing durability. To make this theory concrete, we will now share the actual pivots we made while building our capstones.

## Our Capstone Pivots

Let’s apply this matrix to our capstone projects. Our decision-making process evolved as we built, highlighting the importance of choosing the right tool for the job.

We initially planned to use LangGraph for both agents. However, we quickly found that the research agent, Nova, needed a high degree of interactivity and divergent exploration. A rigid graph was too cumbersome. Flexible MCP tools, which allowed us to change direction on the fly, proved to be a much better fit.

The writing agent, Brown, had the opposite requirements. Its process needed to be repeatable and auditable. Here, LangGraph's features were essential. Its checkpoints, HITL interrupts, and time-travel replay capabilities gave us the control and observability we needed to ensure a reliable workflow.

This led to our hybrid architecture: Nova is implemented as a FastMCP server that any client can steer, while Brown is a LangGraph workflow whose entry points are exposed as coarse-grained MCP tools. This pattern of wrapping complex internal workflows behind single MCP commands is powerful; it gives you portability without sacrificing durability or auditability, which can be measured by throughput and latency metrics under load [[84]](https://mcp-server-langgraph.mintlify.app/comparisons/benchmarks). Brown currently exposes three tools: `generate_article`, `edit_article`, and `edit_selected_text`.

We considered the OpenAI Agents SDK but ultimately deprioritized it because it lacked the first-class persistence and deep MCP integration required for the long-running nature of both capstone tasks. These real-world pivots illustrate the central lesson of this module.

## Conclusion

The AI agent framework landscape is noisy and fast-moving. The key to navigating it is to prioritize stable concepts over transient brand names. Focus on stateful graphs, typed contracts, durable execution, and MCP standardization. These are the principles that will endure.

Investing time to understand the MCP specification itself is a high-leverage activity. It is a one-time investment that yields tool portability across every current and future stack that supports it.

Our practical selection process is this: apply the four decision axes to your project, start with the smallest viable stack that meets your reliability needs, and keep all your tooling portable via MCP. A common migration path might start with exploration in AutoGen Studio, then extract successful patterns into FastMCP tools, and finally anchor the production system in a durable runtime like LangGraph or PydanticAI.

In our next lesson, we will cover system design, including model selection, cost-latency trade-offs, and HITL placement. Afterward, we will begin the hands-on builds of our capstones—Nova with FastMCP and Brown with our hybrid LangGraph-plus-FastMCP stack—using the exact principles we have established here.

## References

- [1] [Build your first Flow](https://docs.crewai.com/guides/flows/first-flow)
- [2] [Introduction](https://docs.crewai.com/introduction)
- [3] [Quickstart](https://docs.crewai.com/quickstart)
- [4] [Durable Execution](https://ai.pydantic.dev/durable_execution/overview/)
- [5] [AutoGen](https://microsoft.github.io/autogen/stable/)
- [6] [AutoGen Studio User Guide](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- [7] [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [8] [What is control-flow explicitness versus LLM-driven autonomy in agent frameworks?](https://www.emergentmind.com/topics/llm-driven-autonomy)
- [9] [What is control-flow explicitness versus LLM-driven autonomy in agent frameworks?](https://www.prefect.io/blog/controlflow-0-9-take-control-of-your-agents)
- [10] [What is control-flow explicitness versus LLM-driven autonomy in agent frameworks?](https://arxiv.org/html/2508.17281v2)
- [11] [What is control-flow explicitness versus LLM-driven autonomy in agent frameworks?](https://arize.com/ai-agents/agent-frameworks)
- [12] [What is AutoGen layered design with Studio AgentChat Core?](https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness)
- [13] [What is AutoGen layered design with Studio AgentChat Core?](https://www.ibm.com/think/topics/autogen)
- [14] [FastMCP](https://gofastmcp.com/)
- [15] [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [16] [Quickstart](https://gofastmcp.com/getting-started/quickstart)
- [17] [Introducing AgentKit](https://openai.com/index/introducing-agentkit)
- [18] [What are the main components of OpenAI AgentKit including visual builder and MCP connectors?](https://www.digitalapplied.com/blog/openai-agentkit-complete-guide)
- [19] [What are the main components of OpenAI AgentKit including visual builder and MCP connectors?](https://www.nudgesecurity.com/post/openai-agentkit-and-agent-builder-building-secure-ai-agents)
- [20] [What are the main components of OpenAI AgentKit including visual builder and MCP connectors?](https://medium.com/@leucopsis/openais-agentkit-review-c83bee3c3d02)
- [21] [What are the main components of OpenAI AgentKit including visual builder and MCP connectors?](https://composio.dev/content/openai-agent-builder-step-by-step-guide-to-building-ai-agents-with-mcp)
- [22] [How does FastMCP enable tool portability across runtimes like LangGraph?](https://generect.com/blog/langgraph-mcp)
- [23] [How does FastMCP enable tool portability across runtimes like LangGraph?](https://gofastmcp.com/servers/tools)
- [24] [How does FastMCP enable tool portability across runtimes like LangGraph?](https://github.com/PrefectHQ/fastmcp)
- [25] [How does PydanticAI use type hints for schema-driven validation?](https://realpython.com/pydantic-ai)
- [26] [How does PydanticAI use type hints for schema-driven validation?](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs)
- [27] [How does PydanticAI use type hints for schema-driven validation?](https://education.molssi.org/type-hints-pydantic-tutorial/chapters/IntroToPydantic.html)
- [28] [How does PydanticAI use type hints for schema-driven validation?](https://pydantic.dev/docs/validation/latest/concepts/validators)
- [29] [How does PydanticAI use type hints for schema-driven validation?](https://pub.towardsai.net/pydantic-a-data-engineers-guide-to-data-validation-ca88a8d9bb2f)
- [30] [What reliability primitives like checkpointing and interrupts does LangGraph offer?](https://docs.langchain.com/oss/javascript/langgraph/interrupts)
- [31] [What reliability primitives like checkpointing and interrupts does LangGraph offer?](https://reference.langchain.com/python/langgraph/types/interrupt)
- [32] [What reliability primitives like checkpointing and interrupts does LangGraph offer?](https://docs.langchain.com/oss/python/langgraph/persistence)
- [33] [What are runtime protocol and tooling layers in AI agent frameworks?](https://www.linkedin.com/posts/brijpandeyji_most-people-still-lump-everything-into-agent-activity-7409465945489829888-8sk5)
- [34] [What are runtime protocol and tooling layers in AI agent frameworks?](https://www.augmentcode.com/guides/agent-runtime-infrastructure-layer)
- [35] [What are runtime protocol and tooling layers in AI agent frameworks?](https://www.guild.ai/glossary/ai-agent-runtime)
- [36] [What are runtime protocol and tooling layers in AI agent frameworks?](https://arize.com/ai-agents/agent-frameworks)
- [37] [What are runtime protocol and tooling layers in AI agent frameworks?](https://forum.langchain.com/t/what-does-the-emerging-ai-agent-stack-actually-look-like/3103)
- [38] [What is abstraction level versus developer experience axis for agent frameworks?](https://www.langchain.com/resources/ai-agent-frameworks)
- [39] [What is abstraction level versus developer experience axis for agent frameworks?](https://www.langchain.com/blog/how-to-think-about-agent-frameworks)
- [40] [What is abstraction level versus developer experience axis for agent frameworks?](https://pub.towardsai.net/a-developers-guide-to-agentic-frameworks-in-2026-3f22a492dc3d)
- [41] [What primitives like guardrails handoffs sessions does OpenAI Agents SDK use?](https://cohorte.co/blog/mastering-the-openai-agents-sdk-a-field-guide-for-busy-developers-ai-vps)
- [42] [What primitives like guardrails handoffs sessions does OpenAI Agents SDK use?](https://openai.github.io/openai-agents-python/agents)
- [43] [What primitives like guardrails handoffs sessions does OpenAI Agents SDK use?](https://platform.claude.com/cookbook/claude-agent-sdk-04-migrating-from-openai-agents-sdk)
- [44] [What primitives like guardrails handoffs sessions does OpenAI Agents SDK use?](https://openai.github.io/openai-agents-python/guardrails)
- [45] [What primitives like guardrails handoffs sessions does OpenAI Agents SDK use?](https://developers.openai.com/api/docs/guides/agents)
- [46] [What is the core philosophy of the Claude Agent SDK?](https://www.morphllm.com/ai-agent-framework)
- [47] [What is the core philosophy of the Claude Agent SDK?](https://www.c-sharpcorner.com/article/building-intelligent-agents-with-claude-agent-sdk-features-comparisons-and-be)
- [48] [What is the core philosophy of the Claude Agent SDK?](https://www.mindstudio.ai/blog/agent-sdk-vs-framework-claude-pydantic-ai)
- [49] [What is the core philosophy of the Claude Agent SDK?](https://buildwithaws.substack.com/p/inside-the-claude-agent-sdk-from)
- [50] [What is the core philosophy of the Claude Agent SDK?](https://aankitroy.com/blog/claude-agent-sdk-building-agents-that-work)
- [51] [What is CrewAI dual architecture of crews versus flows?](https://www.c-sharpcorner.com/article/what-are-crews-vs-flows-in-crewai)
- [52] [What is CrewAI dual architecture of crews versus flows?](https://vadim.blog/crewai-unique-features)
- [53] [What is CrewAI dual architecture of crews versus flows?](https://github.com/crewaiinc/crewai)
- [54] [What is CrewAI dual architecture of crews versus flows?](https://docs.crewai.com/en/concepts/flows)
- [55] [What are LangGraph graph API versus functional API styles?](https://www.linkedin.com/posts/khalid-husain-3002aa216_choosing-between-graph-and-functional-apis-activity-7396757303217029120-VIK3)
- [56] [What are LangGraph graph API versus functional API styles?](https://www.langchain.com/blog/introducing-the-langgraph-functional-api)
- [57] [What are LangGraph graph API versus functional API styles?](https://blog.langchain.com/introducing-the-langgraph-functional-api)
- [58] [What are LangGraph graph API versus functional API styles?](https://docs.langchain.com/oss/python/langgraph/choosing-apis)
- [59] [What are LangGraph graph API versus functional API styles?](https://changelog.langchain.com/announcements/functional-api-for-langgraph)
- [60] [How does LangGraph differ from LangChain in the ecosystem?](https://www.truefoundry.com/blog/langchain-vs-langgraph)
- [61] [Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
- [62] [How does LangGraph differ from LangChain in the ecosystem?](https://duplocloud.com/blog/langchain-vs-langgraph)
- [63] [How does LangGraph differ from LangChain in the ecosystem?](https://www.datacamp.com/tutorial/langchain-vs-langgraph-vs-langsmith-vs-langflow)
- [64] [How does LangGraph differ from LangChain in the ecosystem?](https://www.geeksforgeeks.org/artificial-intelligence/langchain-vs-langgraph)
- [65] [How does LangGraph differ from LangChain in the ecosystem?](https://milvus.io/blog/langchain-vs-langgraph.md)
- [66] [How do GitHub stars and download trends measure agent framework maturity?](https://medium.com/@rosgluk/the-ai-agent-star-race-i-pulled-live-github-data-for-20-frameworks-in-may-2026-b4919dfba5e4)
- [67] [How do GitHub stars and download trends measure agent framework maturity?](https://techwithibrahim.medium.com/top-10-most-starred-ai-agent-frameworks-on-github-2026-df6e760a950b)
- [68] [How do GitHub stars and download trends measure agent framework maturity?](https://arxiv.org/html/2510.25423v2)
- [69] [How do GitHub stars and download trends measure agent framework maturity?](https://www.youtube.com/watch?v=2Yg-BPFNF5A&vl=en-US)
- [70] [What is control-flow explicitness versus LLM-driven autonomy in agent frameworks?](https://arxiv.org/html/2509.13352v2)
- [71] [What is control-flow explicitness versus LLM-driven autonomy in agent frameworks?](https://arize.com/ai-agents/agent-frameworks)
- [72] [What is AutoGen layered design with Studio AgentChat Core?](https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems)
- [73] [What is AutoGen layered design with Studio AgentChat Core?](https://ravichaganti.com/blog/getting-started-with-autogen-framework-for-building-ai-agents-and-applications)
- [74] [What is AutoGen layered design with Studio AgentChat Core?](https://newsletter.victordibia.com/p/a-friendly-introduction-to-the-autogen)
- [75] [A Survey of Agent Interoperability Protocols](https://arxiv.org/html/2505.02279v1)
- [76] [Agentic AI Governance Frameworks](https://www.nice.com/agentic-ai/agentic-ai-governance-frameworks)
- [77] [Checkpoint-based State Replay with LangGraph](https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171)
- [78] [OpenAI Agents in Production](https://www.diagrid.io/solutions/openai-agents-production)
- [79] [Analyzing the Security Risks of OpenAI's AgentKit](https://labs.zenity.io/p/analyzing-the-security-risks-of-openai-s-agentkit)
- [80] [Multi-Agent Systems for Robotic Autonomy with LLMs](https://arxiv.org/html/2502.14743v2)
- [81] [Orchestrating ambient agents with Temporal](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal)
- [82] [LLM-based Multi-Agent Cooperation](https://xue-guang.com/post/llm-marl)
- [83] [MCP Agent Observability](https://www.fiddler.ai/blog/mcp-agent-observability)
- [84] [Hybrid MCP-plus-LangGraph Benchmarks](https://mcp-server-langgraph.mintlify.app/comparisons/benchmarks)