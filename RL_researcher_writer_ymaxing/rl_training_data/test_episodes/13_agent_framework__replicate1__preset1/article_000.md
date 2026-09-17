# Choosing Your AI Agent Framework: A Guide for Production

In our last lesson, we introduced the scope and design of our two capstone projects: Nova, an adaptable and interactive research agent, and Brown, a reliable and auditable writing agent. These projects serve as our concrete anchors for navigating one of the most critical decisions in AI engineering: choosing the right framework.

Making the wrong choice, or making it too late, can lead to brittle abstractions that break under real-world load, stalled progress in a fast-moving ecosystem, or hidden gaps in durability that only appear after weeks of investment. This lesson is about avoiding those traps.

We will focus on two core concepts that define our capstone architectures. For our writing agent, we will use LangGraph's interrupts and checkpoints to build a resumable, auditable workflow. For our research agent, we will leverage the Model Context Protocol (MCP) as a universal interoperability layer to keep our tools portable and adaptable.

The high-level architecture we will build is a hybrid system. The research agent, Nova, will be a lightweight MCP server that any client can steer. The writing agent, Brown, will be a durable LangGraph workflow that exposes its capabilities as coarse-grained MCP tools. This lesson focuses on the philosophies, core abstractions, and production trade-offs that led us to this design, providing you with a set of principles to guide your own decisions.![High-level architecture diagram for the capstone projects](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down)
Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

With our capstones as a concrete reference, we can now examine why framework selection under uncertainty so often fails and what layers—runtime, protocol, and tooling—actually solve which problems.

## Framework Choice Under Uncertainty

The AI agent ecosystem is new and evolving quickly. No single framework will satisfy every use case. To choose wisely, you must distinguish between three layers that are often conflated: the runtime, the protocol, and the tooling framework.

Each layer solves a distinct production problem. The **runtime** (e.g., LangGraph, CrewAI, PydanticAI) provides the engine for orchestration and state management, delivering features like durable execution and resumability. The **protocol** (e.g., MCP) creates a standard for communication, preventing tool lock-in and allowing your tools to outlive any single runtime. Finally, the **tooling framework** (e.g., FastMCP) supplies ready-to-deploy components like transports and authentication, improving the developer experience.![Diagram of Runtime, Protocol, and Tooling Framework relationships](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down)
Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

Engineers often select frameworks based on hype cycles or "hello, world" demos. This leads to common failure modes. You might choose a framework that is too simple and lacks the reliability primitives for production, or one that is overly complex and introduces unnecessary overhead for exploratory work. Research into multi-agent systems formalizes this challenge. Workflows can undergo significant *structural divergence*—changing their execution path—yet still recover the correct answer. Conversely, they can suffer *silent semantic corruption*, where the process looks correct but corrupted data leads to a wrong result, making simple success metrics misleading [[77]](https://arxiv.org/html/2604.27586v1). Interactive workloads, like research, require flexibility, while deterministic workloads, like generating a report, demand auditability.

We learned this firsthand. We initially planned to build our research agent with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was the wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes Instead of Brands

To avoid these traps, you need to evaluate frameworks based on principles, not brands. We use four decision axes to analyze any library and determine its fit for a project.![Diagram of the four key decision axes for evaluating AI agent frameworks](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down)
Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

The first axis is **control-flow explicitness versus LLM-driven autonomy**. Graph-based frameworks like LangGraph offer determinism through explicit nodes and edges. This provides clear auditability, making it ideal for workflows where you need to trace every state transition. In contrast, lightweight agent loops, like those in the OpenAI Agents SDK, favor exploration and adaptability, which is better for tasks where the solution path is unknown. The question to ask is: does your application require repeatable, auditable steps, or does it need to navigate an unpredictable environment?

The second axis is **reliability primitives**. Production systems fail. A good framework provides tools to handle those failures gracefully. Look for features like checkpointing, time-travel replay, Human-in-the-Loop (HITL) interrupts, and durable execution across restarts. LangGraph emphasizes interrupts and persistence [[7]](https://docs.langchain.com/oss/python/langgraph/persistence), while PydanticAI integrates with systems like Temporal and DBOS for durable execution [[6]](https://ai.pydantic.dev/durable_execution/overview/). These are non-negotiable for our writing agent but less critical for the research agent.

The third axis is **abstraction level and developer experience**. Some frameworks, like the OpenAI Agents SDK, provide minimal primitives, requiring more boilerplate but offering greater flexibility. Others, like CrewAI, offer opinionated constructs that accelerate initial development but may reduce adaptability later.

The fourth axis is **tooling interoperability**. MCP functions as the USB-C of AI, providing a standard interface for tools. It lets you write tools once as MCP servers, for example, with FastMCP [[10]](https://gofastmcp.com/), and reuse them across different runtimes and IDEs without rewriting them.

Our capstone projects map clearly to these axes. The research agent requires autonomy and interoperable tools for its exploratory nature, making a lightweight loop with MCP a good fit. The writing agent demands an explicit, auditable workflow with reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks.

**LangGraph** is built on a stateful graph model with native checkpoints and interrupts for auditable workflows [[7]](https://docs.langchain.com/oss/python/langgraph/persistence). It is ideal for processes that need to be resumable and traceable [[62]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). It has shown strong, consistent daily download activity, averaging around 400K–500K downloads per day over the past three months.

<aside>
💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers), **LangGraph** focuses specifically on **structured**, **stateful workflows**. It introduces graph-based execution with checkpoints and resumability, features not native to standard LangChain chains.

In short, LangChain is the toolbox, while LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions [[62]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). You will see LangChain code in the writing agent.
</aside>![Daily downloads for LangGraph](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down)
Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.

The **OpenAI Agents SDK** offers a minimal API surface consisting of agents, tools, guardrails, handoffs, and sessions [[1]](https://openai.github.io/openai-agents-python/). It favors lightweight, Python-native loops over compiled state machines. The library has recorded 90K–120K daily downloads over the past three months, with a slight upward trend.![Daily downloads for OpenAI Agents SDK](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down)
Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.

**AgentKit** is a modular toolkit for building, deploying, and optimizing agents on the OpenAI platform. It unifies a visual builder, connectors (including MCP), a ChatKit for embedding UIs, and evaluation infrastructure. Developers can visually compose multi-agent systems, manage connectors, and embed chat-based experiences directly in their products, all backed by versioning and guardrails for safe deployment [[17]](https://openai.com/index/introducing-agentkit).

<aside>
💡 OpenAI AgentKit vs. OpenAI Agents SDK

The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration and fine-grained control. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK: it adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**. In short, the SDK is the coding foundation, while AgentKit is the integrated platform for design, deployment, and optimization.
</aside>

**CrewAI** features a dual architecture of role-based autonomous crews for collaborative exploration versus event-driven flows for deterministic control [[22]](https://docs.crewai.com/en/introduction). Its daily downloads range between 40K and 100K.![Daily downloads for CrewAI](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down)
Image 6: Source: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.

**PydanticAI** emphasizes type safety and schema-driven validation. It integrates with durable execution systems like Temporal, DBOS, or Prefect [[6]](https://ai.pydantic.dev/durable_execution/overview/). Daily downloads of Pydantic-AI doubled from ~150k in July to 300-450k by October 2025, showing strong growth.![Daily downloads for PydanticAI](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down)
Image 7: Source: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.

**AutoGen** uses a layered approach, with a Studio GUI for exploration and AgentChat or core libraries for production hardening [[33]](https://ravichaganti.com/blog/getting-started-with-autogen-framework-for-building-ai-agents-and-applications).![Daily downloads for AutoGen](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down)
Image 8: Source: pepy.tech, daily downloads for autogen, accessed October 15, 2025.

The **Claude Agent SDK** is a newer entrant from Anthropic. It offers tight integration with the Claude model family, leveraging its strengths in large context and tool use, but it has a smaller ecosystem.

**FastMCP** is a non-runtime tooling layer for building MCP-compliant servers and clients, making tools portable across any runtime or IDE. It has shown explosive growth, with daily downloads surging from ~250k in July to over 1.2M per day in October 2025.![Daily downloads for FastMCP](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down)
Image 9: Source: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.

We use adoption metrics like download trends and GitHub stars to gauge maturity, ecosystem health, and long-term maintenance burden [[56]](https://techwithibrahim.medium.com/top-10-most-starred-ai-agent-frameworks-on-github-2026-df6e760a950b).![Bar chart of GitHub stars for AI agent frameworks](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down)
Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026.

It is important to avoid single-framework dogma. Hybrid patterns are common in practice, such as consuming FastMCP tools inside LangGraph or migrating from AutoGen prototypes to hardened runtimes. We will now deep-dive into each framework, using our four axes and capstone needs as constant evaluation lenses.

## Framework Deep Dive: LangGraph

LangGraph uses a graph-based modeling approach where nodes are Python functions and edges are explicit transitions. This design makes complex, multi-step logic transparent and auditable. By capturing each state transition, it transforms an otherwise non-deterministic execution into a replayable and inspectable state machine, which is essential for production debugging [[78]](https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171). Its core production primitives include interrupts for HITL, persistence and checkpointing for resumability, and time-travel debugging that lets you load the exact checkpoint from a failed run, rewind to the step before the failure, modify the logic, and replay execution from that point [[79]](https://www.comet.com/site/blog/multi-agent-systems), [[7]](https://docs.langchain.com/oss/python/langgraph/persistence).

The framework offers two definition styles: a "graph API" for fully explicit graphs and a "functional API" that uses decorators [[43]](https://www.langchain.com/blog/introducing-the-langgraph-functional-api). This creates a trade-off between the learning curve and the payoff in determinism. The graph API offers more granular control and better support for time-travel, while the functional API is easier to adopt in existing codebases [[44]](https://blog.langchain.com/introducing-the-langgraph-functional-api).

LangGraph can be overkill for simple, exploratory scripts where lighter loops are more efficient. However, for repeatable, auditable processes like our writing agent, the upfront modeling investment is justified. It provides built-in safety, observability, and durability that prevent brittle failures in production. Having examined a graph-centric, reliability-first option, we now turn to a deliberately minimal alternative.

## Framework Deep Dive: OpenAI Agents SDK

The OpenAI Agents SDK is designed with a philosophy of minimal primitives, reducing the conceptual surface area while still enabling powerful agentic applications [[1]](https://openai.github.io/openai-agents-python/).

Its core concepts are simple and interrelated. **Agents** are LLMs equipped with instructions and **Tools**, which are Python functions they can call. **Guardrails** provide a mechanism for validating agent inputs and outputs to ensure safety. **Handoffs** allow one agent to delegate tasks to another, more specialized agent. Finally, **Sessions** automatically manage conversation history across multiple runs [[37]](https://cohorte.co/blog/mastering-the-openai-agents-sdk-a-field-guide-for-busy-developers-ai-vps).![Diagram of OpenAI Agents SDK core primitives](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down)
Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.

The execution model is based on direct Python control flow with `if/else` statements and loops, rather than a compiled state machine like in graph-based systems. This Python-native agent loop offers a straightforward development experience. While LangGraph's functional API also uses decorators, it compiles your code into an explicit, stateful graph that manages execution, persistence, and interruptions. This provides a more robust but also more constrained environment than the SDK’s simple loop.

The SDK is a strong choice for teams that want a fast path to production and prefer lightweight orchestration with sensible defaults. However, it comes with a reliability trade-off: features like durable pause, resume, and checkpointing are not provided out of the box and must be implemented by the team. The natural extension of this minimal SDK is a full-lifecycle platform built on top of it.

## Framework Deep Dive: AgentKit

AgentKit is a complete lifecycle toolkit layered on top of the OpenAI Agents SDK, covering design, deployment, and optimization [[17]](https://openai.com/index/introducing-agentkit). It extends the SDK by adding a visual workflow designer, UI embedding tools, and a comprehensive evaluation infrastructure.![AgentKit Homework Helper workflow example](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down)
Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.

Its key components include the **Agent Builder**, a drag-and-drop canvas for designing and versioning multi-agent workflows; the **Connector Registry**, which centralizes data connections like Dropbox, Google Drive, and third-party MCPs; **ChatKit**, a toolkit for embedding agentic chat UIs into your products; and a suite of tools for **Evals and Reinforcement Fine-Tuning (RFT)** that help measure, grade, and improve agent performance.

AgentKit sits one layer above the OpenAI Agents SDK. You still use the SDK for code-first orchestration, but AgentKit provides the surrounding tools for design, deployment, and continuous improvement. This visual composition, combined with built-in evaluation tools, supports the development of safe, multi-agent systems at scale without forcing everything into code. It is strongest when used within the OpenAI stack, though its growing support for MCP connectors is improving interoperability. AgentKit adds clear value over the raw SDK for teams that need no-code workflow design, versioning, and continuous improvement loops. We now examine a framework whose duality spans both autonomous crews and structured flows.

## Framework Deep Dive: CrewAI![CrewAI Studio visual editor](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcc81dc-f35c-4a6b-95e8-557db10090a9/e0cb631a-91ae-46fc-a332-d5e1afd61c80/w=1920,quality=90,fit=scale-down)
Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`.

CrewAI introduces a powerful duality with its two main concepts: **Crews** and **Flows**. **Crews** are designed for role-based, autonomous collaboration. You define agents with specific roles, goals, and tools, and they work together to solve a problem, much like a human team. **Flows**, on the other hand, are for event-driven, deterministic orchestration, giving you fine-grained control over the execution path [[22]](https://docs.crewai.com/en/introduction).

This dual architecture allows for a natural development progression. You can start with an autonomous crew for rapid prototyping and then introduce a flow to add structure and control as your requirements become more defined. The developer experience is a key focus, with features like CLI scaffolding, YAML definitions for agents and tasks, and configurable memory and persistence options.

CrewAI finds its sweet spot in multi-agent handoff scenarios, such as a researcher-to-writer workflow, where clear role definitions can accelerate development. However, this reliance on opinionated constructs comes with a trade-off. While it provides a rapid start, it can also lead to configuration overhead and reduced flexibility when dealing with edge cases. Another framework approaches the problem through the lens of type safety and compile-time contracts.

## Framework Deep Dive: PydanticAI

PydanticAI adopts a philosophy similar to FastAPI, where Pydantic models and type hints create compile-time contracts between your code and the LLM's behavior [[27]](https://realpython.com/pydantic-ai). This focus on type safety ensures data integrity and predictability.![Diagram of PydanticAI's design philosophy](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/0454e524-5d87-4288-82d4-3abd2b78a6f2/image/w=1920,quality=90,fit=scale-down)
Image 14: Diagram illustrating PydanticAI's design philosophy.

It offers strong production features, including **durable execution integrations** with systems like Temporal, DBOS, or Prefect, which allow agents to survive restarts and handle long-running tasks [[6]](https://ai.pydantic.dev/durable_execution/overview/). This makes workflows "fault-oblivious," meaning they can resume exactly where they left off after an outage without losing state [[80]](https://intuitionlabs.ai/articles/agentic-ai-temporal-orchestration). It also has built-in **graph support** for non-linear workflows. The developer experience is enhanced by automatic schema generation from type hints and structured outputs with automatic retries on validation failure.

The main trade-off is the upfront investment in defining schemas. While this provides correctness guarantees, it can present a learning curve for teams new to strict typing. PydanticAI is best suited for projects where structured data correctness and resumable tasks are paramount, aligning well with our writing agent’s need for auditability. We now look at a layered system that explicitly separates experimentation from production hardening.

## Framework Deep Dive: AutoGen![AutoGen Studio multi-agent workflow visualization](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down)
Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.

AutoGen features a layered design that deliberately separates experimentation from production [[32]](https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems). At the top is **AutoGen Studio**, a low-code GUI for prototyping agent teams without writing code. Below that is **AgentChat**, a programming framework for building conversational multi-agent applications. At the foundation is the **Core**, which provides low-level, event-driven primitives for building scalable, custom agent systems.

The typical workflow involves exploring and validating ideas visually in Studio, then hardening the successful patterns into code using the lower-level libraries [[34]](https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness). It is important to note the explicit disclaimer that Studio is a research prototype and not intended for production environments [[9]](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html).

AutoGen's strength lies in its use as an R&D laboratory for discovering multi-agent conversation patterns and effective termination conditions. However, this flexibility during exploration comes at a cost: the team must re-implement reliability, security, and observability when moving to production. A newer entrant focuses on tight model-family integration.

## Framework Deep Dive: Claude Agent SDK

The Claude Agent SDK is built on a philosophy of tight integration that leverages the specific strengths of the Claude model family, such as large context windows, strong reasoning capabilities, and fine-grained control over tool use. It offers ergonomic tool calling and orchestration tailored specifically to Anthropic's models.

As a newer entrant to the agent framework landscape, it comes with the trade-offs of a smaller community, fewer third-party integrations, and a rapidly evolving API. Teams considering this SDK must balance the opportunity for model-optimized performance against the risks associated with a less mature ecosystem.

The clearest use case for the Claude Agent SDK is for teams already committed to the Anthropic stack who want to achieve native performance and are willing to accept a smaller level of community support. The final deep dive examines a non-runtime layer that complements every option above.

## Framework Deep Dive: FastMCP![FastMCP architecture and interoperability diagram](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/745828fd-27e2-4a50-b613-7275a1e1dceb/image/w=1920,quality=90,fit=scale-down)
Image 16: FastMCP Architecture and Interoperability

FastMCP plays a unique role in the agent ecosystem. It is not a runtime; instead, it is a tooling layer that lets you build MCP-compliant servers and clients [[16]](https://github.com/PrefectHQ/fastmcp). This makes your tools, resources, and prompts portable across any runtime or IDE that speaks the MCP protocol.

The primary benefit is interoperability. You can write a tool once and reuse it in LangGraph, the OpenAI SDK, or even IDEs like Cursor. Adoption has been rapid across the developer tool ecosystem, with integrations in VS Code, JetBrains, Zed, and by coding assistants like Sourcegraph Cody and Codeium [[81]](https://arxiv.org/html/2503.23278v2), [[82]](https://www.descope.com/learn/post/mcp). FastMCP also provides production-ready features beyond the protocol itself, such as authentication, server composition, and cloud deployment options.

Our capstone projects use this pattern. The research agent, Nova, is implemented as a FastMCP server that any client can steer. The writing agent, Brown, exposes its complex LangGraph workflows as coarse-grained MCP tools.

<aside>
💡 **Pattern: tools-as-workflows (Brown)**
For our writing agent (Brown), we wrap each workflow entry point as a **coarse-grained MCP tool** (e.g., `generate_article`, `edit_article`, `edit_selected_text`). The MCP tool handler simply **kicks off the corresponding LangGraph run**, returns progress and messages, and finally yields artifacts and diffs. This gives you MCP portability (Cursor, Claude Code) **without** losing LangGraph’s durability and auditability.
You’ll learn more about this in the later lessons.
</aside>

The developer experience of FastMCP is designed to be simple and Pythonic. You can expose a function as a tool with a single decorator, and FastMCP handles the schema generation and transport details for you [[11]](https://gofastmcp.com/getting-started/quickstart).

1.  Here is a quick example from the official docs.
    ```python
    from fastmcp import FastMCP
    
    mcp = FastMCP("Demo 🚀")
    
    @mcp.tool
    def add(a: int, b: int) -> int:
        """Add two numbers"""
        return a + b
    
    if __name__ == "__main__":
        mcp.run()
    ```

With our deep dives complete, we can now synthesize everything into a decision matrix and tentative forecasts.

## Choosing for Your Project: Decision Matrix & Tentative Forecasts

To help you choose the right framework, we have created a decision matrix that maps common project needs to the relative strengths of each framework.

Table 1: Decision matrix comparing AI agent frameworks against common needs
| Feature | LangGraph | PydanticAI | OpenAI SDK | AgentKit | CrewAI | AutoGen | FastMCP |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Durability/HITL/Replay** | ✅ | | | | | ✅ | |
| **Typed Contracts + Durable Execution** | | ✅ | | | | | ✅ |
| **Few Primitives + Guardrails/Handoffs** | ✅ | | ✅ | ✅ | | | ✅ |
| **Role-based Teams + Quick Scaffolding** | | | | ✅ | ✅ | ✅ | |
| **Exploration Lab** | | | ✅ | ✅ | ✅ | ✅ | |
| **Tool Portability Across Stacks** | | ✅ | | ✅ | | | ✅ |

This matrix should be treated as a snapshot in time. The ecosystem is constantly evolving, so it is important to re-evaluate frameworks against the four decision axes whenever libraries release major updates.

Based on our analysis, we can offer some tentative forecasts. LangGraph and PydanticAI are well-suited for reliability-heavy workflows. The OpenAI SDK is a good choice for lightweight simplicity, while AgentKit is ideal when visual design and continuous evaluation are required. CrewAI excels at rapid multi-agent prototyping, AutoGen serves as a strong R&D starting point, and FastMCP is becoming the universal tooling substrate.

In practice, hybrid patterns are common. You might consume FastMCP tools inside a LangGraph workflow, migrate from an AutoGen Studio prototype to a hardened runtime, or expose a complex graph as a single MCP command to gain IDE portability without sacrificing durability. To make this theory concrete, we now share the actual pivots we made while building our course capstones.

## Our Capstone Pivots

Let’s apply this matrix to our capstone project. Our decision-making process evolved as we built, highlighting the importance of choosing the right tool for the job.

Our initial plan was to use LangGraph for both agents. However, we quickly found that the research agent’s need for high interactivity and divergent exploration made a rigid graph structure cumbersome. In this case, flexible MCP tools proved to be a superior approach. Attempts to build autonomous research agents often document recurring failure modes, such as implementation drift under pressure, memory degradation on long tasks, and a bias toward training data defaults that limits novel discovery [[83]](https://huggingface.co/papers?q=failure-mode-targeted+generation).

The writing agent had the opposite requirements. Its repeatable, auditable process demanded the features that LangGraph excels at: checkpoints, HITL interrupts, and time-travel replay capabilities.

This led to our final hybrid architecture. Nova, the research agent, is implemented as a FastMCP server that any client, including IDEs, can steer. Brown, the writing agent, is a LangGraph workflow whose entry points are exposed as coarse-grained MCP tools. This pattern of wrapping complex internal workflows behind single MCP commands allows us to gain portability without sacrificing durability or auditability. Brown currently exposes three tools: `generate_article`, `edit_article`, and `edit_selected_text`.

We considered the OpenAI Agents SDK but ultimately deprioritized it because it lacked the first-class persistence and deep MCP integration required for the long-running nature of both capstone tasks. These real-world pivots illustrate the central lesson of this module.

## Conclusion

The core takeaway from this lesson is to prioritize stable concepts over transient brand names. Stateful graphs, typed contracts, durable execution, and MCP standardization are principles that will outlast any single framework.

The MCP specification, in particular, is a high-leverage investment. Understanding it once gives you tool portability across every current and future stack that supports it. A practical selection process should begin by applying the four decision axes to your project. Start with the smallest viable stack that meets your reliability needs, and keep your tooling portable via MCP.

A common migration path might look like this: begin exploration in AutoGen Studio, extract successful patterns into FastMCP tools, and then anchor your production system in a robust framework like LangGraph or PydanticAI.

In our next lesson, we will cover system design, including model selection, cost and latency trade-offs, and HITL placement. Following that, we will begin the hands-on builds of our capstone projects, using the hybrid FastMCP-plus-LangGraph stack we have chosen through this exact process. We will build **Nova** with **FastMCP** for its server/client architecture and research loops, and **Brown** with **LangGraph + FastMCP** to combine a durable workflow with portable MCP tools for review-edit cycles and HITL editing.

## References

- [1] OpenAI Agents SDK. (n.d.). OpenAI. [https://openai.github.io/openai-agents-python/](https://openai.github.io/openai-agents-python/)
- [2] ControlFlow is an open-source framework for taming the complexity of AI workflows. (n.d.). Prefect. [https://www.prefect.io/blog/controlflow-0-9-take-control-of-your-agents](https://www.prefect.io/blog/controlflow-0-9-take-control-of-your-agents)
- [3] General-purpose systems. (n.d.). arXiv. [https://arxiv.org/html/2508.17281v2](https://arxiv.org/html/2508.17281v2)
- [4] Agent Frameworks. (n.d.). Arize. [https://arize.com/ai-agents/agent-frameworks](https://arize.com/ai-agents/agent-frameworks)
- [5] Agent Frameworks. (n.d.). Arize. [https://arize.com/ai-agents/agent-frameworks](https://arize.com/ai-agents/agent-frameworks)
- [6] Durable Execution. (n.d.). Pydantic. [https://ai.pydantic.dev/durable_execution/overview/](https://ai.pydantic.dev/durable_execution/overview/)
- [7] Persistence. (n.d.). LangChain. [https://docs.langchain.com/oss/python/langgraph/persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [8] Interrupts. (n.d.). LangChain. [https://docs.langchain.com/oss/javascript/langgraph/interrupts](https://docs.langchain.com/oss/javascript/langgraph/interrupts)
- [9] AutoGen Studio User Guide. (n.d.). Microsoft. [https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- [10] FastMCP. (n.d.). gofastmcp.com. [https://gofastmcp.com/](https://gofastmcp.com/)
- [11] Quickstart. (n.d.). gofastmcp.com. [https://gofastmcp.com/getting-started/quickstart](https://gofastmcp.com/getting-started/quickstart)
- [12] LangGraph MCP Client Setup Made Easy. (2026). Generect. [https://generect.com/blog/langgraph-mcp](https://generect.com/blog/langgraph-mcp)
- [13] Tools. (n.d.). gofastmcp.com. [https://gofastmcp.com/servers/tools](https://gofastmcp.com/servers/tools)
- [14] FastMCP has three pillars. (n.d.). GitHub. [https://github.com/PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)
- [15] Introducing AgentKit. (2025). OpenAI. [https://openai.com/index/introducing-agentkit](https://openai.com/index/introducing-agentkit)
- [16] Introducing AgentKit. (2025). OpenAI. [https://openai.com/index/introducing-agentkit](https://openai.com/index/introducing-agentkit)
- [17] Introducing AgentKit. (2025). OpenAI. [https://openai.com/index/introducing-agentkit](https://openai.com/index/introducing-agentkit)
- [18] Introduction. (n.d.). CrewAI. [https://docs.crewai.com/introduction](https://docs.crewai.com/introduction)
- [19] Introduction. (n.d.). CrewAI. [https://docs.crewai.com/introduction](https://docs.crewai.com/introduction)
- [20] Build your first Flow. (n.d.). CrewAI. [https://docs.crewai.com/guides/flows/first-flow](https://docs.crewai.com/guides/flows/first-flow)
- [21] Q: What makes Crews different from Flows? (n.d.). GitHub. [https://github.com/crewaiinc/crewai](https://github.com/crewaiinc/crewai)
- [22] Introduction. (n.d.). CrewAI. [https://docs.crewai.com/en/introduction](https://docs.crewai.com/en/introduction)
- [23] Pydantic AI is a Python framework for building LLM agents. (n.d.). Real Python. [https://realpython.com/pydantic-ai](https://realpython.com/pydantic-ai)
- [24] The Complete Guide to Using Pydantic for Validating LLM Outputs. (n.d.). Machine Learning Mastery. [https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs](https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs)
- [25] Intro to Pydantic. (n.d.). MolSSI. [https://education.molssi.org/type-hints-pydantic-tutorial/chapters/IntroToPydantic.html](https://education.molssi.org/type-hints-pydantic-tutorial/chapters/IntroToPydantic.html)
- [26] Validators. (n.d.). Pydantic. [https://pydantic.dev/docs/validation/latest/concepts/validators](https://pydantic.dev/docs/validation/latest/concepts/validators)
- [27] Pydantic: A Data Engineer’s Guide to Data Validation. (n.d.). Towards AI. [https://pub.towardsai.net/pydantic-a-data-engineers-guide-to-data-validation-ca88a8d9bb2f](https://pub.towardsai.net/pydantic-a-data-engineers-guide-to-data-validation-ca88a8d9bb2f)
- [28] Microsoft AutoGen: Orchestrating Multi-Agent LLM Systems. (n.d.). Tribe.ai. [https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems](https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems)
- [29] Getting Started with AutoGen Framework. (n.d.). ravichaganti.com. [https://ravichaganti.com/blog/getting-started-with-autogen-framework-for-building-ai-agents-and-applications](https://ravichaganti.com/blog/getting-started-with-autogen-framework-for-building-ai-agents-and-applications)
- [30] AutoGen v0.4. (n.d.). Microsoft Research. [https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness](https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness)
- [31] AutoGen. (n.d.). IBM. [https://www.ibm.com/think/topics/autogen](https://www.ibm.com/think/topics/autogen)
- [32] A Friendly Introduction to the AutoGen. (n.d.). Victor Dibia. [https://newsletter.victordibia.com/p/a-friendly-introduction-to-the-autogen](https://newsletter.victordibia.com/p/a-friendly-introduction-to-the-autogen)
- [33] Getting Started with AutoGen Framework. (n.d.). ravichaganti.com. [https://ravichaganti.com/blog/getting-started-with-autogen-framework-for-building-ai-agents-and-applications](https://ravichaganti.com/blog/getting-started-with-autogen-framework-for-building-ai-agents-and-applications)
- [34] AutoGen v0.4. (n.d.). Microsoft Research. [https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness](https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness)
- [35] OpenAI Agents SDK primitives. (n.d.). Cohorte. [https://cohorte.co/blog/mastering-the-openai-agents-sdk-a-field-guide-for-busy-developers-ai-vps](https://cohorte.co/blog/mastering-the-openai-agents-sdk-a-field-guide-for-busy-developers-ai-vps)
- [36] Agents. (n.d.). OpenAI. [https://openai.github.io/openai-agents-python/agents](https://openai.github.io/openai-agents-python/agents)
- [37] Mastering the OpenAI Agents SDK. (n.d.). Cohorte. [https://cohorte.co/blog/mastering-the-openai-agents-sdk-a-field-guide-for-busy-developers-ai-vps](https://cohorte.co/blog/mastering-the-openai-agents-sdk-a-field-guide-for-busy-developers-ai-vps)
- [38] Guardrails. (n.d.). OpenAI. [https://openai.github.io/openai-agents-python/guardrails](https://openai.github.io/openai-agents-python/guardrails)
- [39] Agents Guide. (n.d.). OpenAI. [https://developers.openai.com/api/docs/guides/agents](https://developers.openai.com/api/docs/guides/agents)
- [40] Choosing between graph and functional APIs. (n.d.). LinkedIn. [https://www.linkedin.com/posts/khalid-husain-3002aa216_choosing-between-graph-and-functional-apis-activity-7396757303217029120-VIK3](https://www.linkedin.com/posts/khalid-husain-3002aa216_choosing-between-graph-and-functional-apis-activity-7396757303217029120-VIK3)
- [41] Introducing the LangGraph Functional API. (n.d.). LangChain Blog. [https://www.langchain.com/blog/introducing-the-langgraph-functional-api](https://www.langchain.com/blog/introducing-the-langgraph-functional-api)
- [42] Introducing the LangGraph Functional API. (n.d.). LangChain Blog. [https://blog.langchain.com/introducing-the-langgraph-functional-api](https://blog.langchain.com/introducing-the-langgraph-functional-api)
- [43] Introducing the LangGraph Functional API. (n.d.). LangChain Blog. [https://www.langchain.com/blog/introducing-the-langgraph-functional-api](https://www.langchain.com/blog/introducing-the-langgraph-functional-api)
- [44] Introducing the LangGraph Functional API. (n.d.). LangChain Blog. [https://blog.langchain.com/introducing-the-langgraph-functional-api](https://blog.langchain.com/introducing-the-langgraph-functional-api)
- [45] Functional API for LangGraph. (n.d.). LangChain Changelog. [https://changelog.langchain.com/announcements/functional-api-for-langgraph](https://changelog.langchain.com/announcements/functional-api-for-langgraph)
- [46] Agent Runtime Infrastructure Layer. (n.d.). AugmentCode. [https://www.augmentcode.com/guides/agent-runtime-infrastructure-layer](https://www.augmentcode.com/guides/agent-runtime-infrastructure-layer)
- [47] AI Agent Runtime. (n.d.). Guild.ai. [https://www.guild.ai/glossary/ai-agent-runtime](https://www.guild.ai/glossary/ai-agent-runtime)
- [48] AWS Bedrock AgentCore. (n.d.). Arize. [https://arize.com/ai-agents/agent-frameworks](https://arize.com/ai-agents/agent-frameworks)
- [49] AI Agent Frameworks. (n.d.). LangChain Resources. [https://www.langchain.com/resources/ai-agent-frameworks](https://www.langchain.com/resources/ai-agent-frameworks)
- [50] How to think about agent frameworks. (n.d.). LangChain Blog. [https://www.langchain.com/blog/how-to-think-about-agent-frameworks](https://www.langchain.com/blog/how-to-think-about-agent-frameworks)
- [51] A Developer’s Guide to Agentic Frameworks in 2026. (n.d.). Towards AI. [https://pub.towardsai.net/a-developers-guide-to-agentic-frameworks-in-2026-3f22a492dc3d](https://pub.towardsai.net/a-developers-guide-to-agentic-frameworks-in-2026-3f22a492dc3d)
- [52] Top 10 Most Starred AI Agent Frameworks on GitHub (2026). (n.d.). TechWithIbrahim. [https://techwithibrahim.medium.com/top-10-most-starred-ai-agent-frameworks-on-github-2026-df6e760a950b](https://techwithibrahim.medium.com/top-10-most-starred-ai-agent-frameworks-on-github-2026-df6e760a950b)
- [53] Stack Overflow Analysis of Agent Frameworks. (n.d.). arXiv. [https://arxiv.org/html/2510.25423v2](https://arxiv.org/html/2510.25423v2)
- [54] LangChain vs. LangGraph. (n.d.). TrueFoundry. [https://www.truefoundry.com/blog/langchain-vs-langgraph](https://www.truefoundry.com/blog/langchain-vs-langgraph)
- [55] LangChain vs. LangGraph. (n.d.). DuploCloud. [https://duplocloud.com/blog/langchain-vs-langgraph](https://duplocloud.com/blog/langchain-vs-langgraph)
- [56] Top 10 Most Starred AI Agent Frameworks on GitHub (2026). (n.d.). TechWithIbrahim. [https://techwithibrahim.medium.com/top-10-most-starred-ai-agent-frameworks-on-github-2026-df6e760a950b](https://techwithibrahim.medium.com/top-10-most-starred-ai-agent-frameworks-on-github-2026-df6e760a950b)
- [57] LangChain vs. LangGraph vs. LangSmith vs. LangFlow. (n.d.). DataCamp. [https://www.datacamp.com/tutorial/langchain-vs-langgraph-vs-langsmith-vs-langflow](https://www.datacamp.com/tutorial/langchain-vs-langgraph-vs-langsmith-vs-langflow)
- [58] LangChain vs. LangGraph. (n.d.). GeeksforGeeks. [https://www.geeksforgeeks.org/artificial-intelligence/langchain-vs-langgraph](https://www.geeksforgeeks.org/artificial-intelligence/langchain-vs-langgraph)
- [59] LangChain vs. LangGraph. (n.d.). Milvus. [https://milvus.io/blog/langchain-vs-langgraph.md](https://milvus.io/blog/langchain-vs-langgraph.md)
- [60] interrupt function in LangGraph. (n.d.). LangChain Reference. [https://reference.langchain.com/python/langgraph/types/interrupt](https://reference.langchain.com/python/langgraph/types/interrupt)
- [61] Migrating from OpenAI Agents SDK to Claude Agent SDK. (n.d.). Claude Platform. [https://platform.claude.com/cookbook/claude-agent-sdk-04-migrating-from-openai-agents-sdk](https://platform.claude.com/cookbook/claude-agent-sdk-04-migrating-from-openai-agents-sdk)
- [62] Workflows and agents. (n.d.). LangChain. [https://docs.langchain.com/oss/python/langgraph/workflows-agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
- [63] How to think about agent frameworks. (n.d.). LangChain Blog. [https://www.langchain.com/blog/how-to-think-about-agent-frameworks](https://www.langchain.com/blog/how-to-think-about-agent-frameworks)
- [64] AutoGen. (n.d.). Microsoft. [https://microsoft.github.io/autogen/stable/](https://microsoft.github.io/autogen/stable/)
- [65] LangChain vs. LangGraph. (n.d.). TrueFoundry. [https://www.truefoundry.com/blog/langchain-vs-langgraph](https://www.truefoundry.com/blog/langchain-vs-langgraph)
- [66] LangChain vs. LangGraph. (n.d.). DuploCloud. [https://duplocloud.com/blog/langchain-vs-langgraph](https://duplocloud.com/blog/langchain-vs-langgraph)
- [67] LangChain vs. LangGraph vs. LangSmith vs. LangFlow. (n.d.). DataCamp. [https://www.datacamp.com/tutorial/langchain-vs-langgraph-vs-langsmith-vs-langflow](https://www.datacamp.com/tutorial/langchain-vs-langgraph-vs-langsmith-vs-langflow)
- [68] LangChain vs. LangGraph. (n.d.). GeeksforGeeks. [https://www.geeksforgeeks.org/artificial-intelligence/langchain-vs-langgraph](https://www.geeksforgeeks.org/artificial-intelligence/langchain-vs-langgraph)
- [69] LangChain vs. LangGraph. (n.d.). Milvus. [https://milvus.io/blog/langchain-vs-langgraph.md](https://milvus.io/blog/langchain-vs-langgraph.md)
- [70] Choosing APIs. (n.d.). LangChain. [https://docs.langchain.com/oss/python/langgraph/choosing-apis](https://docs.langchain.com/oss/python/langgraph/choosing-apis)
- [71] Functional API for LangGraph. (n.d.). LangChain Changelog. [https://changelog.langchain.com/announcements/functional-api-for-langgraph](https://changelog.langchain.com/announcements/functional-api-for-langgraph)
- [72] We started with seven core Agent frameworks. (n.d.). arXiv. [https://arxiv.org/html/2510.25423v2](https://arxiv.org/html/2510.25423v2)
- [73] Flow State Management. (n.d.). CrewAI. [https://docs.crewai.com/en/concepts/flows](https://docs.crewai.com/en/concepts/flows)
- [74] Microsoft AutoGen: Orchestrating Multi-Agent LLM Systems. (n.d.). Tribe.ai. [https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems](https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems)
- [75] A Friendly Introduction to the AutoGen. (n.d.). Victor Dibia. [https://newsletter.victordibia.com/p/a-friendly-introduction-to-the-autogen](https://newsletter.victordibia.com/p/a-friendly-introduction-to-the-autogen)
- [76] AutoGen. (n.d.). IBM. [https://www.ibm.com/think/topics/autogen](https://www.ibm.com/think/topics/autogen)
- [77] Trace-Level Analysis of Information Contamination in Multi-Agent Systems. (2026). arXiv. [https://arxiv.org/html/2604.27586v1](https://arxiv.org/html/2604.27586v1)
- [78] Debugging Non-Deterministic LLM Agents. (n.d.). Dev.to. [https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171](https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171)
- [79] Multi-Agent Systems. (n.d.). Comet. [https://www.comet.com/site/blog/multi-agent-systems](https://www.comet.com/site/blog/multi-agent-systems)
- [80] Agentic AI and Temporal Orchestration. (n.d.). Intuition Labs. [https://intuitionlabs.ai/articles/agentic-ai-temporal-orchestration](https://intuitionlabs.ai/articles/agentic-ai-temporal-orchestration)
- [81] Overview of Agent Frameworks. (2025). arXiv. [https://arxiv.org/html/2503.23278v2](https://arxiv.org/html/2503.23278v2)
- [82] Model Context Protocol (MCP). (n.d.). Descope. [https://www.descope.com/learn/post/mcp](https://www.descope.com/learn/post/mcp)
- [83] Failure-Mode-Targeted Generation. (n.d.). Hugging Face. [https://huggingface.co/papers?q=failure-mode-targeted+generation](https://huggingface.co/papers?q=failure-mode-targeted+generation)