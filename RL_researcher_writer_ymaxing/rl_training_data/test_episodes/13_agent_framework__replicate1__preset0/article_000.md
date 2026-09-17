# Choosing Your AI Agent Framework: A Guide for Engineers

In our last lesson, we introduced the two capstone projects that will anchor our journey: Nova, an adaptable and interactive research agent, and Brown, a reliable and auditable writing agent. The design of these systems immediately raises a critical question: what framework should we build them on? This choice is not trivial. A poor decision can lead to brittle abstractions that break under real-world load, stalled progress in a fast-moving ecosystem, or hidden gaps in durability that only appear after weeks of investment.

Throughout this lesson, we will explore two core concepts that guided our decisions. First, LangGraph’s interrupts and checkpoints, which provide the resumable auditability essential for our writing agent. Second, the Model Context Protocol (MCP), a universal interoperability layer that keeps our research agent's tools portable and independent of any single runtime.

Our final architecture, shown in Image 1, reflects this thinking. The research agent is a lightweight MCP server that any client can steer, while the writing agent is a durable workflow that exposes its capabilities as coarse-grained MCP tools. This lesson focuses on the philosophies, core abstractions, and production trade-offs that led us to this design, providing you with a set of principles for making your own framework decisions.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down> 
Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

With our capstone projects as a concrete reference, we can now examine why framework selection so often fails and what layers—runtime, protocol, and tooling—actually solve which problems.

## Framework Choice Under Uncertainty

The AI agent ecosystem is new and evolving quickly. No single framework will satisfy every use case. To choose wisely, you must distinguish between three layers that are often conflated: runtime, protocol, and tooling.

Each layer solves a distinct production problem. The **runtime** (e.g., LangGraph, CrewAI, OpenAI Agents SDK) provides the engine for orchestration and state management, delivering features like durable execution and resumability. The **protocol** (e.g., MCP) is a standardization layer that prevents tool lock-in by defining a common interface, ensuring portability. Finally, the **tooling framework** (e.g., FastMCP) provides the scaffolding for implementation, offering ready-to-deploy servers, transports, and authentication that improve the developer experience.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down> 
Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

Engineers often select frameworks based on hype or simple "hello-world" demos. This leads to common failure modes, like choosing a framework that is too simple and lacks reliability primitives for production, or one that is overly complex and introduces unnecessary overhead for exploratory work. Interactive workloads, like our research agent, demand flexibility, while deterministic workloads, like our writing agent, require auditability.

We learned this firsthand. We initially planned to build our research agent with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was the wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes Instead of Brands

To avoid these traps, you need to evaluate frameworks based on principles, not just brand names. We use four decision axes to analyze any library and determine its fit for a given project.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down> 
Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

The first axis is **control-flow explicitness versus LLM-driven autonomy**. Graph-based frameworks like LangGraph offer explicit nodes and edges, providing clear auditability and control over every state transition. This is ideal for deterministic workflows where you need to know precisely why the system made a decision. In contrast, lightweight agent loops, like those in the OpenAI Agents SDK, favor exploration and adaptability, which is better for tasks where the path to a solution is not known in advance. The question to ask is: does your application require repeatable, auditable steps, or does it need to navigate an unpredictable environment?

The second axis is **reliability primitives**. Production systems fail. A good framework provides tools to handle those failures gracefully. Features like checkpointing, time-travel replay, human-in-the-loop (HITL) interrupts, and durable execution are non-negotiable for our writing agent. LangGraph emphasizes interrupts and persistence, while frameworks like PydanticAI integrate with systems like Temporal and DBOS for durable execution [[1]](https://docs.langchain.com/oss/python/langgraph/persistence), [[2]](https://ai.pydantic.dev/durable_execution/overview/).

The third axis is **abstraction level and developer experience**. Some frameworks, like the OpenAI Agents SDK, provide minimal primitives (Agents, Tools, Guardrails) that require more boilerplate but deliver flexibility. Others, like CrewAI, offer opinionated constructs that accelerate initial development but may reduce adaptability later on.

The fourth axis is **tooling interoperability**. MCP acts as the USB-C of AI, providing a standard interface for tools [[3]](https://gofastmcp.com/). This lets you write tools once as MCP servers (for example, with FastMCP) and reuse them across different runtimes like LangGraph or the OpenAI Agents SDK, and even in IDEs like Cursor, without rewriting them.

Our capstone projects map clearly to these axes. The research agent requires high autonomy and interoperable tools, making a lightweight loop with MCP a good fit. The writing agent demands an explicit, auditable workflow with strong reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape.

**LangGraph** is built on a stateful graph model with native checkpoints and interrupts, making it ideal for auditable and resumable workflows like our writing agent [[1]](https://docs.langchain.com/oss/python/langgraph/persistence), [[4]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). It has shown strong, consistent adoption, with 400K–500K daily downloads over the past three months.

<aside>
💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers), **LangGraph** focuses specifically on **structured, stateful workflows**. It introduces graph-based execution with checkpoints and resumability, which are features not native to standard LangChain chains. In short, LangChain is the toolbox, while LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions [[4]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). You will see LangChain code in the writing agent.
</aside>

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down> 
Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.

The **OpenAI Agents SDK** offers a minimal API surface with core primitives like agents, tools, guardrails, handoffs, and sessions [[5]](https://openai.github.io/openai-agents-python/). It favors lightweight, Python-native loops over compiled state machines. The library has recorded 90K–120K daily downloads over the past three months, with a slight upward trend.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down> 
Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.

**AgentKit** is a modular toolkit for building, deploying, and optimizing agents on the OpenAI platform. It unifies a visual builder, connectors (including MCP), a ChatKit for UI embedding, and evaluation infrastructure. This allows developers to visually compose multi-agent systems and manage them through a full lifecycle.

<aside>
💡 OpenAI AgentKit vs. OpenAI Agents SDK

The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration and fine-grained control. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK: it adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**. In short, the SDK is the coding foundation, while AgentKit is the integrated platform for design, deployment, and optimization.
</aside>

**CrewAI** features a dual architecture: role-based autonomous "crews" for collaborative exploration and event-driven "flows" for deterministic control. It also provides a strong developer experience with its CLI and YAML-based definitions. Daily downloads for CrewAI range between 40K and 100K.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down> 
Image 6: Source: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.

**PydanticAI** emphasizes type safety and schema-driven validation. It offers durable execution through integrations with platforms like Temporal, DBOS, and Prefect, along with built-in graph support. Its daily downloads have doubled from ~150K in July to 300-450K by October 2025.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down> 
Image 7: Source: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.

**AutoGen** from Microsoft takes a layered approach, with its Studio GUI positioned for exploration, feeding ideas into the AgentChat or core libraries for production hardening [[6]](https://microsoft.github.io/autogen/stable/).

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down> 
Image 8: Source: pepy.tech, daily downloads for autogen, accessed October 15, 2025.

The **Claude Agent SDK** is a newer entrant from Anthropic. It focuses on tight integration with the Claude model family, leveraging its strengths in large context and tool use, but currently has a smaller ecosystem.

**FastMCP** is not a runtime but a tooling layer for building MCP-compliant servers and clients [[3]](https://gofastmcp.com/). This makes tools portable across any runtime or IDE. It has shown explosive growth, with daily downloads surging from ~250K in July to over 1.2M per day in October 2025.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down> 
Image 9: Source: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.

Adoption metrics like download trends and GitHub stars can serve as a proxy for a framework's maturity, ecosystem health, and long-term maintenance burden. However, it is important to avoid single-framework dogma. Hybrid patterns are common in practice, such as consuming FastMCP tools inside a LangGraph workflow or migrating from an AutoGen prototype to a hardened runtime.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down> 
Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026.

Now, we will take a deeper look at each framework, using our four axes and capstone needs as constant evaluation lenses.

## Framework Deep Dive: LangGraph

LangGraph models workflows as graphs where nodes are Python functions and edges are explicit transitions. This makes complex, multi-step logic transparent and auditable. Its core production primitives include interrupts for human-in-the-loop, persistence and checkpointing for resumability, and time-travel debugging that lets you replay and branch from any prior state.

The framework offers two definition styles: a "graph API" for fully explicit graphs and a "functional API" that uses decorators [[7]](https://blog.langchain.com/introducing-the-langgraph-functional-api). This creates a trade-off between the learning curve and the payoff in determinism. The functional API is easier to adopt for existing procedural code, but the graph API provides more granular control and better visualization for debugging complex flows.

LangGraph can be overkill for simple exploratory scripts, where lighter loops are more efficient. However, for repeatable, auditable processes like our writing agent, the upfront modeling investment is justified by the built-in safety, observability, and durability it provides. This contrasts with lighter, more autonomous loops that offer less structure but greater flexibility for unpredictable tasks.

Having examined a graph-centric, reliability-first option, we now turn to a deliberately minimal alternative.

## Framework Deep Dive: OpenAI Agents SDK

The OpenAI Agents SDK is designed with a philosophy of minimal primitives, reducing the conceptual surface area while still enabling powerful agentic applications. Its core concepts—agents, tools, guardrails, handoffs, and sessions—provide a lightweight yet comprehensive toolkit [[5]](https://openai.github.io/openai-agents-python/).

-   **Agents** are LLMs equipped with instructions and tools.
-   **Tools** are Python functions that agents can call to interact with the outside world.
-   **Guardrails** are mechanisms for validating agent inputs and outputs to ensure safety and correctness.
-   **Handoffs** provide a way for agents to delegate tasks to other, more specialized agents.
-   **Sessions** automatically manage conversation history across multiple runs.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down> 
Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.

The execution model is based on direct Python control flow with `if/else` statements and loops, rather than compiled state machines like those in graph-based systems. This Python-native agent loop gives you direct control over orchestration. In contrast, even with its decorator-based functional API, LangGraph compiles your code into an explicit, stateful graph that manages execution, persistence, and interruptions. This provides a more robust but also more constrained environment.

The SDK is a strong choice for teams that want a fast path to production and prefer lightweight orchestration with sensible defaults. However, this simplicity comes with a trade-off: reliability features like durable pause, resume, and checkpointing are not provided out of the box and must be implemented by the team.

The natural extension of this minimal SDK is a full-lifecycle platform built on top of it.

## Framework Deep Dive: AgentKit

AgentKit is a complete lifecycle toolkit layered on top of the OpenAI Agents SDK, covering design, deployment, optimization, and continuous improvement [[8]](https://openai.com/index/introducing-agentkit). It extends the SDK by adding visual workflow design, UI embedding, and evaluation infrastructure.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down> 
Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.

Its key components include:

-   **Agent Builder**: A drag-and-drop canvas for designing and versioning multi-agent workflows.
-   **Connector Registry**: A centralized interface for managing data connections, including third-party MCPs.
-   **ChatKit**: A toolkit for embedding agentic chat UIs directly into your products.
-   **Evals and Reinforcement Fine-Tuning (RFT)**: Capabilities for measuring, grading, and improving agent performance.

AgentKit sits one layer above the OpenAI Agents SDK. You still use the SDK for code-first orchestration, but AgentKit provides the surrounding tools for design, deployment, and continuous improvement. Its visual composition and built-in evaluation tools support the development of safe, multi-agent systems at scale without forcing everything into code. The trade-off is that it is most powerful when used within the OpenAI ecosystem, though its growing support for MCP connectors is improving interoperability. AgentKit adds clear value over the raw SDK for teams that need no-code workflow design, versioning, and continuous improvement loops.

We now examine a framework whose duality spans both autonomous crews and structured flows.

## Framework Deep Dive: CrewAI

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcc81dc-f35c-4a6b-95e8-557db10090a9/e0cb631a-91ae-46fc-a332-d5e1afd61c80/w=1920,quality=90,fit=scale-down> 
Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`.

CrewAI introduces a powerful duality with its two main concepts: **Crews** and **Flows** [[9]](https://docs.crewai.com/introduction). **Crews** are for role-based, autonomous collaboration. You define agents with specific roles, goals, and tools, and they work together to solve a problem, much like a human team. **Flows**, on the other hand, are for event-driven, deterministic orchestration, giving you fine-grained control over the workflow [[10]](https://docs.crewai.com/guides/flows/first-flow).

This dual architecture lets you start with an autonomous crew for rapid prototyping, then introduce a flow to add structure and control as your requirements become more defined. CrewAI also has a strong focus on developer experience, with CLI scaffolding, YAML definitions for agents and tasks, and configurable memory and persistence options.

The framework's sweet spot is in multi-agent handoff scenarios, such as researcher-to-writer workflows, where role clarity accelerates development. The trade-off is that its opinionated constructs, while speeding up initial development, can lead to configuration overhead and reduced flexibility when edge cases arise.

Another framework approaches the problem through the lens of type safety and compile-time contracts.

## Framework Deep Dive: PydanticAI

PydanticAI brings a FastAPI-like philosophy to agent development, where Pydantic models and type hints create compile-time contracts between your code and the LLM's behavior [[11]](https://realpython.com/pydantic-ai). This focus on type safety ensures that the data flowing through your system is always structured and validated.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/0454e524-5d87-4288-82d4-3abd2b78a6f2/image/w=1920,quality=90,fit=scale-down> 
Image 14: Diagram illustrating PydanticAI's design philosophy.

It includes production-ready features like **durable execution integrations** with systems such as Temporal, DBOS, or Prefect, which allow agents to survive restarts and handle long-running tasks [[2]](https://ai.pydantic.dev/durable_execution/overview/). It also has built-in **graph support** for non-linear flows. The developer experience is enhanced by automatic schema generation from type hints and docstrings, and structured outputs with automatic retries on validation failure.

The main trade-off is the upfront investment in defining schemas. While this guarantees data correctness, it can present a learning curve for teams new to strict typing. PydanticAI is best suited for projects where structured data correctness and resumable tasks are paramount, which aligns well with the auditability needs of our writing agent.

We now look at a layered system that explicitly separates experimentation from production hardening.

## Framework Deep Dive: AutoGen

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down> 
Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.

AutoGen from Microsoft features a layered design that deliberately separates experimentation from production [[6]](https://microsoft.github.io/autogen/stable/), [[12]](https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness).

-   **AutoGen Studio** is a low-code GUI that lets you prototype agent teams and workflows without writing code [[13]](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html).
-   **AgentChat** is a programming framework for building conversational multi-agent applications.
-   **Core** provides low-level, event-driven primitives for building scalable, custom agent systems.

The typical workflow involves exploring and validating ideas visually inside Studio, then hardening the successful patterns into code using the lower-level layers. It is important to note the explicit disclaimer that Studio is a research prototype and is not intended for production environments.

AutoGen's strength lies in its use as an R&D laboratory for discovering multi-agent conversation patterns and effective termination conditions. The trade-off is that while it offers high flexibility during exploration, the team is responsible for re-implementing reliability, security, and observability when moving to production.

A newer entrant focuses on tight model-family integration.

## Framework Deep Dive: Claude Agent SDK

The Claude Agent SDK is built on a philosophy of tight integration with the Claude model family, leveraging its strengths in large context windows, strong reasoning, and fine-grained control over tool use [[14]](https://www.mindstudio.ai/blog/agent-sdk-vs-framework-claude-pydantic-ai). It provides ergonomic tool calling and orchestration tailored specifically to Anthropic's models.

As a newer entrant, its trade-offs include a smaller community, fewer third-party integrations, and a rapidly evolving API. This presents both an opportunity and a risk. Early adoption can yield model-optimized performance, but teams must balance this against the maturity of the ecosystem. The clearest use case is for teams already committed to the Anthropic stack who want native performance and are willing to accept smaller community support.

The final deep dive examines a non-runtime layer that complements every option above.

## Framework Deep Dive: FastMCP

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/745828fd-27e2-4a50-b613-7275a1e1dceb/image/w=1920,quality=90,fit=scale-down> 
Image 16: FastMCP Architecture and Interoperability

FastMCP is not a runtime; it is a tooling framework for building MCP-compliant servers and clients [[3]](https://gofastmcp.com/). This allows you to make your tools, resources, and prompts portable across any runtime or IDE that speaks the protocol. The key benefit is interoperability: you can write a tool once and reuse it inside LangGraph, the OpenAI SDK, Cursor, or any other compatible system.

Beyond the protocol itself, FastMCP offers production-oriented features like authentication, server composition, and cloud deployment options. Our capstone projects use this pattern: the research agent is implemented as a FastMCP server that any client can steer, while the writing agent exposes its complex workflows as coarse-grained MCP tools.

<aside>
💡 **Pattern: tools-as-workflows (Brown)**

For our writing agent (Brown), we wrap each workflow entry point as a **coarse-grained MCP tool** (e.g., `generate_article`, `edit_article`, `edit_selected_text`). The MCP tool handler simply **kicks off the corresponding LangGraph run**, returns progress and messages, and finally yields artifacts and diffs. This gives you MCP portability (Cursor, Claude Code) **without** losing LangGraph’s durability and auditability. You’ll learn more about this in the later lessons.
</aside>

The developer experience of FastMCP is designed to be simple and Pythonic. You can expose a function as a tool with a single decorator, and FastMCP handles the schema generation and transport details for you [[15]](https://gofastmcp.com/getting-started/quickstart).

1. Here is a quick example from the official docs.
    ```python
    from fastmcp import FastMCP
    
    mcp = FastMCP("My MCP Server")
    
    @mcp.tool
    def greet(name: str) -> str:
        return f"Hello, {name}!"
    
    if __name__ == "__main__":
        mcp.run()
    ```

With our deep dives complete, we can now synthesize everything into a decision matrix and some tentative forecasts.

## Choosing for Your Project: Decision Matrix & Tentative Forecasts

To help you choose the right framework, we have created a decision matrix that maps common project needs to the relative strengths of each library.

Table 1: Decision matrix comparing AI agent frameworks against common needs
| Feature | LangGraph | PydanticAI | OpenAI SDK | AgentKit | CrewAI | AutoGen | FastMCP |
|---|---|---|---|---|---|---|---|
| **Durability/HITL/Replay** | ✅ | | | | | ✅ | |
| **Typed Contracts + Durable Execution** | | ✅ | | | | | ✅ |
| **Few Primitives + Guardrails/Handoffs** | ✅ | | ✅ | ✅ | | | ✅ |
| **Role-based Teams + Quick Scaffolding** | | | | ✅ | ✅ | ✅ | |
| **Exploration Lab** | | | ✅ | ✅ | ✅ | ✅ | |
| **Tool Portability Across Stacks** | | ✅ | | ✅ | | | ✅ |

It is important to treat this matrix as a snapshot. The ecosystem is evolving, so you should always re-evaluate frameworks against the four decision axes when major updates are released.

Based on these axes, we can offer some forecasts. LangGraph and PydanticAI are strong choices for reliability-heavy workflows. The OpenAI SDK is well-suited for applications that require lightweight simplicity, while AgentKit is ideal when visual design and continuous evaluation are needed. CrewAI excels at rapid multi-agent prototyping, AutoGen serves as a powerful R&D starting point, and FastMCP is emerging as the universal tooling substrate.

In practice, hybrid patterns are common. You might consume FastMCP tools inside LangGraph workflows, migrate from AutoGen Studio prototypes to hardened runtimes, or expose complex graphs as single MCP commands to gain IDE portability without sacrificing durability.

To make this theory concrete, we will now share the actual pivots we made while building our course capstones.

## Our Capstone Pivots

Let’s apply this matrix to our capstone project. Our decision-making process evolved as we built, highlighting the importance of choosing the right tool for the job.

We initially planned to use LangGraph for both agents. However, we quickly found that the research agent’s need for high interactivity and divergent exploration made a rigid graph structure cumbersome. Flexible MCP tools proved to be a better fit, allowing us to adapt on the fly.

The writing agent had the opposite requirements. Its repeatable, auditable process demanded the features that LangGraph excels at: checkpoints, HITL interrupts, and time-travel replay capabilities. This led to our final hybrid architecture: Nova is implemented as a FastMCP server that any client can steer, while Brown is a LangGraph workflow whose entry points are exposed as coarse-grained MCP tools.

This approach revealed an emergent pattern: wrapping complex internal workflows behind single MCP commands. This gives you the portability of MCP without sacrificing the durability and auditability of a stateful framework like LangGraph. For our writing agent, Brown, we exposed three main tools: `generate_article`, `edit_article`, and `edit_selected_text`.

We considered the OpenAI Agents SDK, but ultimately deprioritized it because it lacked the first-class persistence and deep MCP integration required for the long-running nature of both capstone tasks. These real-world pivots illustrate the central lesson of this module.

## Conclusion

The core takeaway from this lesson is to prioritize stable concepts over transient brand names. Stateful graphs, typed contracts, durable execution, and MCP standardization are principles that will outlast any single framework. The MCP specification, in particular, is a high-leverage area of study; a one-time investment in understanding it can yield tool portability across every current and future stack.

Our recommended selection process is to first apply the four decision axes to your project's needs. Start with the smallest viable stack that meets your reliability requirements and keep all your tooling portable via MCP. A practical migration path could be to begin exploration in AutoGen Studio, extract successful patterns into FastMCP tools, and then anchor your production system in a robust framework like LangGraph or PydanticAI.

In our next lesson, we will cover system design, including model selection, cost and latency trade-offs, and HITL placement. After that, we will begin the hands-on capstone builds, using the hybrid FastMCP-plus-LangGraph stack we chose through this exact process. You will see how we build **Nova** with **FastMCP** for its server/client architecture and research capabilities, and **Brown** with **LangGraph + FastMCP** for its durable workflow and human-in-the-loop editing cycles.

## References

- [1] Persistence. (n.d.). LangChain. https://docs.langchain.com/oss/python/langgraph/persistence
- [2] Durable Execution. (n.d.). Pydantic. https://ai.pydantic.dev/durable_execution/overview/
- [3] FastMCP. (n.d.). gofastmcp.com. https://gofastmcp.com/
- [4] Workflows and agents. (n.d.). LangChain. https://docs.langchain.com/oss/python/langgraph/workflows-agents
- [5] OpenAI Agents SDK. (n.d.). OpenAI. https://openai.github.io/openai-agents-python/
- [6] AutoGen. (n.d.). Microsoft. https://microsoft.github.io/autogen/stable/
- [7] Introducing the LangGraph Functional API. (2025, January 29). LangChain Blog. https://blog.langchain.com/introducing-the-langgraph-functional-api
- [8] Introducing AgentKit. (2025, October 6). OpenAI. https://openai.com/index/introducing-agentkit
- [9] Introduction. (n.d.). CrewAI. https://docs.crewai.com/introduction
- [10] Build your first Flow. (n.d.). CrewAI. https://docs.crewai.com/guides/flows/first-flow
- [11] Pydantic AI: Build Type-Safe LLM Agents in Python. (2026, March 11). Real Python. https://realpython.com/pydantic-ai
- [12] AutoGen v0.4: Reimagining the foundation of agentic AI for scale, extensibility, and robustness. (n.d.). Microsoft Research. https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness
- [13] AutoGen Studio User Guide. (n.d.). Microsoft. https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html
- [14] What is the core philosophy of the Claude Agent SDK?. (n.d.). MindStudio. https://www.mindstudio.ai/blog/agent-sdk-vs-framework-claude-pydantic-ai
- [15] Quickstart. (n.d.). gofastmcp.com. https://gofastmcp.com/getting-started/quickstart