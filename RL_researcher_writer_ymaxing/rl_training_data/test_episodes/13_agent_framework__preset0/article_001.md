# How to Choose an AI Agent Framework: A Guide for Engineers

In our last lesson, we introduced the two capstone projects that will be central to our work: Nova, an adaptable and interactive research agent, and Brown, a reliable and auditable writing agent. The design of these systems forces us to confront one of the most critical decisions in AI engineering: choosing the right framework.

This choice is not trivial. A poor decision made early can lead to brittle abstractions that break under real-world load, stalled progress in a fast-moving ecosystem, or hidden gaps in durability that only surface after weeks of investment. The landscape is crowded and noisy, making it easy to pick a framework based on hype rather than engineering principles.

This lesson will give you a structured way to navigate this uncertainty. We will focus on two core concepts that anchor our capstone designs: using LangGraph's interrupts and checkpoints for resumable auditability in our writing agent, and leveraging the Model Context Protocol (MCP) as a universal interoperability layer to keep our research agent's tools portable. Our high-level architecture, shown in Image 1, reflects this hybrid approach. The research agent is a lightweight MCP server that any client can steer, while the writing agent is a durable workflow that exposes its capabilities as coarse-grained MCP tools. We will not focus on API syntax or "hello world" tutorials. Instead, we will examine the philosophies, core abstractions, and production trade-offs that matter.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down> 
Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

With our capstones as a concrete reference, let's examine why framework selection so often fails and what layers—runtime, protocol, and tooling—actually solve which problems.

## Framework Choice Under Uncertainty

The AI agent ecosystem is new and evolving at a breakneck pace. No single framework will satisfy every use case, and what seems popular today may be obsolete tomorrow. To make a durable choice, you must first understand that "agent framework" is an overloaded term that conflates three distinct layers: the runtime, the protocol, and the tooling framework.

The **runtime** is the orchestration engine that manages state and execution. Frameworks like LangGraph, CrewAI, and the OpenAI Agents SDK fall into this category. They provide the machinery for durable execution and resumability, handling the complex logic of keeping an agent running, recoverable, and stateful [[48]](https://www.augmentcode.com/guides/agent-runtime-infrastructure-layer). The **protocol**, such as the Model Context Protocol (MCP), is a standardization layer. It defines a common language for agents and tools to communicate, preventing vendor lock-in and eliminating the need to rewrite tools for every new runtime [[47]](https://www.linkedin.com/posts/brijpandeyji_most-people-still-lump-everything-into-agent-activity-7409465945489829888-8sk5). Finally, the **tooling framework**, like FastMCP, provides the scaffolding for implementing the protocol. It supplies ready-to-deploy servers, clients, and authentication, improving the developer experience.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down> 
Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

When engineers choose a framework based on hype or simple demos, they often select a runtime that is a poor fit for their production needs. An overly simple framework may lack the reliability primitives for a durable workload, such as built-in state management for long conversations, leading to data loss on restart. Conversely, an overly complex one introduces unnecessary overhead, forcing a rigid graph structure on a simple, linear task. This distinction between interactive and deterministic workloads is a good initial lens for assessing fit.

We learned this firsthand. We initially planned to build our research agent with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was a wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes Instead of Brands

To avoid these traps, you need a way to evaluate frameworks based on principles, not brands. We have identified four decision axes that can help you analyze any library and determine its fit for your project.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down> 
Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

The first axis is **control-flow explicitness versus LLM-driven autonomy**. Graph-based frameworks like LangGraph offer explicit nodes and edges, providing determinism and auditability. This is ideal for workflows where you need to trace every state transition. In contrast, lightweight agent loops, like the one in the OpenAI Agents SDK, favor autonomy and adaptability, which is better for exploratory tasks where the solution path is unknown. The question to ask is: does your application require repeatable, auditable steps, or does it need to navigate an unpredictable environment?

The second axis is **reliability primitives**. Production systems fail. A good framework provides tools to handle those failures gracefully. Look for features like checkpointing, time-travel replay, human-in-the-loop (HITL) interrupts, and durable execution across restarts. LangGraph emphasizes interrupts and persistence [[1]](https://docs.langchain.com/oss/python/langgraph/persistence), while PydanticAI integrates with systems like Temporal and DBOS for durable execution [[2]](https://ai.pydantic.dev/durable_execution/overview/). These features are non-negotiable for our writing agent but less critical for the research agent.

The third axis is **abstraction level and developer experience**. Some frameworks, like the OpenAI Agents SDK, provide minimal primitives that require more boilerplate but offer greater flexibility. Others, like CrewAI, have opinionated constructs that accelerate initial development but can reduce adaptability when dealing with edge cases.

The fourth axis is **tooling interoperability**. MCP functions as the USB-C equivalent for AI, providing a standard interface for tools. It lets you write tools once as MCP servers (for example, with FastMCP [[3]](https://gofastmcp.com/)) and reuse them across different runtimes and IDEs that speak the protocol, including LangGraph and the OpenAI Agents SDK [[3]](https://gofastmcp.com/).

Our capstone projects map clearly to these axes. The research agent requires high autonomy and interoperable tools for its exploratory nature, making a lightweight loop with MCP a good fit. The writing agent demands an explicit, auditable workflow with strong reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks.

**LangGraph**'s philosophy is built on a stateful graph model with native checkpoints and interrupts for auditable workflows [[1]](https://docs.langchain.com/oss/python/langgraph/persistence). It is ideal for processes that need to be resumable and traceable, as we saw in our review of common workflow patterns [[4]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). The library shows strong, consistent adoption, with daily downloads averaging 400,000–500,000 over the past three months.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down> 
Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.

<aside>
💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers), **LangGraph** focuses specifically on **structured**, **stateful workflows**. It introduces graph-based execution with checkpoints and resumability, features not native to standard LangChain chains. In short, LangChain is the toolbox, while LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions [[4]](https://docs.langchain.com/oss/python/langgraph/workflows-agents).
</aside>

The **OpenAI Agents SDK** offers a minimal API surface consisting of agents, tools, guardrails, handoffs, and sessions [[5]](https://openai.github.io/openai-agents-python/). It favors lightweight, Python-native loops over compiled state machines. Daily downloads have been steady at 90,000–120,000 over the past three months, with a slight upward trend.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down> 
Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.

**AgentKit** is a modular toolkit for building, deploying, and optimizing agents across the OpenAI platform. It unifies a visual builder, connectors (including MCP), a ChatKit for embedding UIs, and evaluation infrastructure. This allows developers to visually compose multi-agent systems and manage the entire lifecycle from design to deployment.

<aside>
💡 OpenAI AgentKit vs. OpenAI Agents SDK

The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK. It adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**. In short, the SDK is the coding foundation, while AgentKit is the integrated platform for design, deployment, and optimization.
</aside>

**CrewAI** features a dual architecture of role-based autonomous crews for collaborative exploration versus event-driven flows for deterministic control. It also provides a strong developer experience with its CLI and YAML-based definitions. Daily downloads for CrewAI range between 40,000 and 100,000.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down> 
Image 6: Source: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.

**PydanticAI** emphasizes type safety, schema-driven validation, and durable execution through integrations with platforms like Temporal, DBOS, and Prefect. It also has built-in graph support. Its daily downloads have doubled from ~150,000 in July to 300,000-450,000 by October 2025, showing strong growth momentum.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-c0f83f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down> 
Image 7: Source: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.

**AutoGen** from Microsoft takes a layered approach, with a Studio GUI for exploration, AgentChat for conversational apps, and a Core library for custom primitives. It is explicitly positioned for R&D, with the idea that successful prototypes are hardened into production code.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down> 
Image 8: Source: pepy.tech, daily downloads for autogen, accessed October 15, 2025.

The **Claude Agent SDK** is a newer entrant from Anthropic. It offers tight integration with the Claude family of models, leveraging their strengths in large context and tool use, but it has a smaller ecosystem.

Finally, **FastMCP** is a non-runtime tooling layer for building MCP-compliant servers and clients, making tools portable across any runtime or IDE. It has seen explosive growth, with daily downloads surging from ~250,000 in July to over 1.2 million per day in October 2025.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down> 
Image 9: Source: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.

Adoption metrics like download trends and GitHub stars can serve as a proxy for maturity, ecosystem health, and hiring risk. However, it is important to avoid single-framework dogma. Hybrid patterns are common, such as consuming FastMCP tools inside a LangGraph workflow or migrating from an AutoGen prototype to a more hardened runtime.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down> 
Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026.

Now, we will examine each framework in more detail, using our four axes and capstone needs as constant evaluation lenses.

## Framework Deep Dive: LangGraph

LangGraph’s approach is centered on graph-based modeling, where nodes are Python functions and edges represent explicit transitions. This design makes complex, multi-step logic transparent and auditable, a key requirement for our writing agent, Brown.

Its core production primitives are what set it apart for reliability. It offers interrupts for human-in-the-loop validation, allowing a workflow to pause and wait for external approval before continuing [[6]](https://reference.langchain.com/python/langgraph/types/interrupt). Persistence and checkpointing enable resumability, ensuring that a long-running process can recover from a crash without losing its state [[7]](https://docs.langchain.com/oss/python/langgraph/persistence). Furthermore, its time-travel debugging lets you replay and branch from any prior state, which is invaluable for debugging complex agentic behavior. These features are critical for building systems that can recover from failures and allow for human oversight.

LangGraph provides two distinct definition styles: a "graph API" for fully explicit graphs and a "functional API" that uses decorators [[19]](https://www.langchain.com/blog/introducing-the-langgraph-functional-api). This creates a trade-off between the learning curve and the determinism you gain. The explicit graph API requires more upfront modeling but delivers complete control and better visualization capabilities. The functional API feels more like standard Python, making it easier to adopt, but it offers less granular checkpoints and no visualization since the execution flow is dynamic [[44]](https://blog.langchain.com/introducing-the-langgraph-functional-api).

However, LangGraph can be overkill for simple, exploratory scripts where a lighter loop would suffice. The investment in modeling is justified only when you need repeatable, auditable processes, as is the case with our writing agent. This steeper upfront cost pays off in production with built-in safety, observability, and durability that prevent the brittle failures common in less structured agentic systems.

Having examined a graph-centric, reliability-first option, we now turn to a deliberately minimal alternative.

## Framework Deep Dive: OpenAI Agents SDK

The philosophy behind the OpenAI Agents SDK is one of minimal primitives [[20]](https://www.langchain.com/resources/ai-agent-frameworks). It deliberately reduces the conceptual surface area to make building agentic applications more approachable. Its core concepts are simple but powerful.

- **Agents** are LLMs equipped with instructions and tools.
- **Tools** are Python functions that agents can call to interact with the outside world.
- **Guardrails** are mechanisms for validating agent inputs and outputs to ensure safety and correctness [[21]](https://openai.github.io/openai-agents-python/guardrails).
- **Handoffs** provide a way for agents to delegate tasks to other, more specialized agents [[22]](https://openai.github.io/openai-agents-python/agents).
- **Sessions** automatically manage conversation history across multiple runs.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down> 
Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.

The execution model is fundamentally different from that of graph-based systems. Instead of a compiled state machine, orchestration is handled with standard Python control flow, such as `if/else` statements and loops. This Python-native approach feels intuitive and flexible. Even when compared to LangGraph's decorator-based functional API, which also looks like standard Python, the underlying execution model differs. LangGraph compiles your code into an explicit, stateful graph that manages execution, persistence, and interruptions. The SDK, in contrast, uses a simple agent loop that you control directly.

This makes the SDK a strong choice for teams that want a fast path to production where lightweight orchestration and sensible defaults are sufficient. However, this simplicity comes with a trade-off: reliability primitives like durable pause, resume, and checkpointing are not provided out of the box and must be implemented by the developer.

The natural extension of this minimal SDK is a full-lifecycle platform built on top of it.

## Framework Deep Dive: AgentKit

AgentKit is a complete lifecycle toolkit layered on top of the OpenAI Agents SDK [[6]](https://openai.com/index/introducing-agentkit). It extends the SDK by adding visual workflow design, UI embedding, and a comprehensive evaluation infrastructure, covering the entire process from design and deployment to optimization and continuous improvement.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down> 
Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.

Its key components provide an end-to-end solution for building and managing agents.

- **Agent Builder** is a drag-and-drop canvas for designing and versioning multi-agent workflows. It allows for visual composition of logic, inline evaluation, and full version control [[7]](https://www.digitalapplied.com/blog/openai-agentkit-complete-guide).
- **Connector Registry** is a centralized interface for managing data connections, including Dropbox, Google Drive, and third-party MCPs, across an organization [[8]](https://medium.com/@leucopsis/openais-agentkit-review-c83bee3c3d02).
- **ChatKit** is a toolkit for embedding agentic chat UIs directly into products, handling streaming, conversation threads, and custom theming [[7]](https://www.digitalapplied.com/blog/openai-agentkit-complete-guide).
- **Evals and Reinforcement Fine-Tuning (RFT)** offer expanded capabilities for measuring, grading, and improving agent performance through datasets, automated prompt optimization, and custom graders [[7]](https://www.digitalapplied.com/blog/openai-agentkit-complete-guide).

AgentKit sits one layer above the SDK. You still use the SDK for code-first orchestration, but AgentKit provides the surrounding tools for design, deployment, and continuous improvement. This visual composition and built-in evaluation support the development of safe, multi-agent systems at scale without forcing everything into code. The main trade-off is its optimization for the OpenAI ecosystem, although its growing support for MCP connectors is improving interoperability. AgentKit adds clear value for teams that need no-code workflow design, versioning, and continuous improvement loops.

Next, we will examine a framework whose duality spans both autonomous crews and structured flows.

## Framework Deep Dive: CrewAI

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcc81dc-f35c-4a6b-95e8-557db10090a9/e0cb631a-91ae-46fc-a332-d5e1afd61c80/w=1920,quality=90,fit=scale-down> 
Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`.

CrewAI introduces a powerful duality with its two main concepts: **Crews** and **Flows** [[9]](https://docs.crewai.com/en/introduction). This dual architecture is designed to balance autonomy with control, allowing developers to choose the right level of abstraction for their needs.

**Crews** are for role-based, autonomous collaboration. You define agents with specific roles, goals, and tools, and they work together to solve a problem, much like a human team. This is ideal for tasks that benefit from a division of labor and collaborative problem-solving, where the exact steps are not known in advance. For example, a research crew might have a "Researcher" agent to find information and a "Synthesizer" agent to compile it into a report.

**Flows** are for event-driven, deterministic orchestration. They give you fine-grained control over the workflow, allowing you to define precise execution paths, manage state, and implement conditional logic. This is better for structured processes where reliability and predictability are key. For instance, a content publishing flow could manage the steps of drafting, reviewing, and scheduling an article.

This architecture supports a common development pattern: you can start with an autonomous crew for rapid prototyping and then introduce a flow to add structure and control as your requirements become more defined [[9]](https://docs.crewai.com/en/introduction).

CrewAI also has a strong focus on developer experience, with a CLI for scaffolding projects, YAML-based definitions for agents and tasks, and configurable options for memory and persistence. Its sweet spot is in multi-agent handoff scenarios, like a researcher-to-writer workflow, where role clarity accelerates development. The main trade-off is that its opinionated constructs, while speeding up initial development, can lead to configuration overhead and reduced flexibility when dealing with edge cases.

Another framework approaches the problem through the lens of type safety and compile-time contracts.

## Framework Deep Dive: PydanticAI

PydanticAI's philosophy is heavily inspired by FastAPI, where Pydantic models and type hints create compile-time contracts between your code and the LLM's behavior [[10]](https://realpython.com/pydantic-ai). This focus on type safety ensures that the data flowing through your agentic system is always structured and validated.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/0454e524-5d87-4288-82d4-3abd2b78a6f2/image/w=1920,quality=90,fit=scale-down> 
Image 14: Diagram illustrating PydanticAI's design philosophy.

Its production-oriented features are a key strength. It offers **durable execution integrations** with platforms like Temporal, DBOS, and Prefect, which allow agents to survive restarts, pause for human input, and resume long-running tasks [[2]](https://ai.pydantic.dev/durable_execution/overview/). It also has built-in **graph support** for defining non-linear workflows.

The developer experience is enhanced by several ergonomic features, including automatic schema generation from type hints and docstrings, and structured output with automatic retries on validation failure. However, this comes with the cost of an up-front investment in defining schemas, which can be a learning curve for teams new to strict typing.

PydanticAI's best-fit scenario is for projects where structured data correctness and resumable, long-running tasks are paramount. This aligns well with the auditability and reliability needs of our writing agent, Brown.

We will now look at a layered system that explicitly separates experimentation from production hardening.

## Framework Deep Dive: AutoGen

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down> 
Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.

AutoGen from Microsoft is designed with a layered architecture that deliberately separates experimentation from production [[11]](https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness).

- **AutoGen Studio** is a low-code GUI that lets you prototype agent teams and workflows without writing code. You can visually compose agents, configure their tools, and test their interactions [[12]](https://ravichaganti.com/blog/getting-started-with-autogen-framework-for-building-ai-agents-and-applications).
- **AgentChat** is a programming framework for building conversational multi-agent applications [[13]](https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems).
- **Core** provides low-level, event-driven primitives for building scalable, custom agent systems [[14]](https://www.ibm.com/think/topics/autogen).

The typical workflow involves exploring and validating ideas visually inside Studio, then hardening the successful patterns into code using the lower-level `AgentChat` and `Core` libraries. Microsoft explicitly states that Studio is a research prototype and not intended for production environments [[15]](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html).

AutoGen's strength lies in its use as an R&D laboratory for discovering effective multi-agent conversation patterns and termination conditions. However, this flexibility during exploration comes with a trade-off. When moving to production, the development team is responsible for re-implementing reliability, security, and observability, as these are not core features of the prototyping environment.

A newer entrant in the framework space focuses on tight integration with a specific model family.

## Framework Deep Dive: Claude Agent SDK

The Claude Agent SDK from Anthropic is built on a philosophy of tight integration with the Claude family of models [[16]](https://www.mindstudio.ai/blog/agent-sdk-vs-framework-claude-pydantic-ai). It is designed to use their specific strengths, such as large context windows, strong reasoning capabilities, and fine-grained control over tool use.

The SDK provides ergonomic tool-calling and orchestration features tailored specifically to the Anthropic model family. However, as a newer entrant, it comes with the trade-offs of a smaller community, fewer third-party integrations, and a rapidly evolving API surface.

This presents both an opportunity and a risk. Early adoption can yield model-optimized performance, but teams must balance this against the maturity of the ecosystem. The clearest use case for the Claude Agent SDK is for teams that are already committed to the Anthropic stack and want to maximize native performance, while being willing to accept smaller community support.

The final deep dive examines a non-runtime layer that complements every option discussed so far.

## Framework Deep Dive: FastMCP

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/745828fd-27e2-4a50-b613-7275a1e1dceb/image/w=1920,quality=90,fit=scale-down> 
Image 16: FastMCP Architecture and Interoperability

FastMCP plays a unique role in the agent ecosystem. It is not a runtime; instead, it is a tooling framework that lets you build MCP-compliant servers and clients so that tools, resources, and prompts become portable across any runtime or IDE that speaks the protocol [[17]](https://github.com/PrefectHQ/fastmcp).

The primary benefit is interoperability. You can write a tool once and reuse it inside LangGraph, the OpenAI SDK, Cursor, Claude Code, or any future compatible system. This decouples your tool development from your choice of orchestration engine. FastMCP also offers production-oriented extensions beyond the protocol itself, including authentication, server composition, and cloud deployment features.

Our capstone projects leverage this portability. The research agent, Nova, is implemented as a FastMCP server that any client can steer. The writing agent, Brown, exposes its complex workflows as coarse-grained MCP tools.

<aside>
💡 Pattern: tools-as-workflows (Brown)

For our writing agent (Brown), we wrap each workflow entry point as a **coarse-grained MCP tool** (e.g., `generate_article`, `edit_article`, `edit_selected_text`). The MCP tool handler simply **kicks off the corresponding LangGraph run**, returns progress and messages, and finally yields artifacts and diffs. This gives you MCP portability (Cursor, Claude Code) **without** losing LangGraph’s durability and auditability. You’ll learn more about this in later lessons.
</aside>

The developer experience of FastMCP is designed to be simple and Pythonic. You can expose a function as a tool with a single decorator, and FastMCP handles the schema generation and transport details automatically.

Here is a quick example from the official documentation [[18]](https://gofastmcp.com/getting-started/quickstart):

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
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Durability/HITL/Replay** | ✅ | | | | | ✅ | |
| **Typed Contracts + Durable Execution** | | ✅ | | | | | ✅ |
| **Few Primitives + Guardrails/Handoffs** | ✅ | | ✅ | ✅ | | | ✅ |
| **Role-based Teams + Quick Scaffolding** | | | | ✅ | ✅ | ✅ | |
| **Exploration Lab** | | | ✅ | ✅ | ✅ | ✅ | |
| **Tool Portability Across Stacks** | | ✅ | | ✅ | | | ✅ |

It is important to treat this matrix as a snapshot in time. The agent ecosystem is evolving rapidly, and you should re-evaluate frameworks against the four decision axes whenever libraries release major updates.

Based on these axes, we can make some forecasts. LangGraph and PydanticAI are well-suited for reliability-heavy workflows. The OpenAI SDK offers lightweight simplicity, while AgentKit is ideal when visual design and continuous evaluation loops are required. CrewAI excels at rapid multi-agent prototyping, AutoGen serves as a strong R&D starting point, and FastMCP is emerging as the universal tooling substrate.

In practice, hybrid patterns are common. You might consume FastMCP tools inside a LangGraph workflow, migrate from an AutoGen Studio prototype to a hardened runtime, or expose a complex graph as a single MCP command to gain IDE portability without sacrificing durability.

To make this theory concrete, we will now share the actual pivots we made while building the course capstones.

## Our Capstone Pivots

Let’s apply this matrix to our capstone project. Our decision-making process evolved as we built, highlighting the importance of choosing the right tool for the job.

We initially planned to use LangGraph for both agents. However, we quickly discovered that the research agent’s need for high interactivity and divergent exploration made rigid graphs cumbersome. For Nova, flexible MCP tools proved to be a superior approach, allowing us to adapt on the fly without being constrained by a predefined structure.

The writing agent, Brown, had the opposite requirements. Its repeatable, auditable process demanded the features that LangGraph excels at: checkpoints, HITL interrupts, and time-travel replay capabilities. This ensured that every step of the writing process was traceable and recoverable.

The result is a hybrid architecture. Nova is implemented as a FastMCP server that any client, including IDEs, can steer. Brown is implemented as a LangGraph workflow whose entry points are exposed as deliberately coarse-grained MCP tools. Currently, Brown exposes three such tools: `generate_article`, `edit_article`, and `edit_selected_text`. This pattern of wrapping complex internal workflows behind single MCP commands allows us to gain portability without sacrificing durability or auditability.

We considered the OpenAI Agents SDK, but it was ultimately deprioritized for our capstones. It lacked the first-class persistence and deep MCP integration required for the long-running, stateful nature of both our research and writing tasks. For example, a research session with Nova could span hours and involve multiple interruptions; without native persistence, the agent's state would be lost on any server restart or connection drop, forcing the user to start over. This was an unacceptable risk for our production-oriented design.

These real-world pivots illustrate the central lesson of this module.

## Conclusion

The core takeaway from our exploration of the agent framework landscape is to prioritize stable concepts over transient brand names. Technologies like stateful graphs, typed contracts, durable execution, and MCP standardization provide lasting value, while specific library implementations will continue to evolve. Understanding these foundational principles allows you to make choices that are resilient to the hype cycle.

Reading the MCP specification itself is a high-leverage activity. A one-time investment in understanding the protocol can yield tool portability across every current and future stack that supports it, future-proofing a critical part of your system.

A practical selection process for your own projects should follow a similar path to ours. First, apply the four decision axes to your requirements to clarify your needs. Then, start with the smallest viable stack that meets your reliability needs, avoiding unnecessary complexity. Finally, keep all your tooling portable via MCP to maintain flexibility. A common migration path might start with exploration in AutoGen Studio, followed by extracting successful patterns into FastMCP tools, and finally anchoring the production system in a robust runtime like LangGraph or PydanticAI.

In the next lesson, we will move on to system design, covering model selection, cost and latency trade-offs, and the strategic placement of human-in-the-loop gates. After that, we will begin the hands-on capstone builds, implementing the hybrid FastMCP-plus-LangGraph stack we have chosen through this exact process. You will build **Nova** with **FastMCP** for research and **Brown** with **LangGraph + FastMCP** for writing, putting these principles into practice.

## References

- [1] [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [2] [Durable Execution](https://ai.pydantic.dev/durable_execution/overview/)
- [3] [FastMCP](https://gofastmcp.com/)
- [4] [Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
- [5] [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [6] [Introducing AgentKit](https://openai.com/index/introducing-agentkit)
- [7] [OpenAI AgentKit: The Complete Guide for Developers](https://www.digitalapplied.com/blog/openai-agentkit-complete-guide)
- [8] [OpenAI’s AgentKit Review](https://medium.com/@leucopsis/openais-agentkit-review-c83bee3c3d02)
- [9] [Introduction](https://docs.crewai.com/en/introduction)
- [10] [Pydantic AI: Build Type-Safe LLM Agents in Python](https://realpython.com/pydantic-ai)
- [11] [AutoGen v0.4: Reimagining the foundation of agentic AI for scale, extensibility, and robustness](https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness)
- [12] [Getting Started with AutoGen Framework for Building AI Agents and Applications](https://ravichaganti.com/blog/getting-started-with-autogen-framework-for-building-ai-agents-and-applications)
- [13] [Microsoft AutoGen: Orchestrating Multi-Agent LLM Systems](https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems)
- [14] [What is AutoGen?](https://www.ibm.com/think/topics/autogen)
- [15] [AutoGen Studio User Guide](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- [16] [Agent SDK vs Framework: Claude, Pydantic, and the Future of AI](https://www.mindstudio.ai/blog/agent-sdk-vs-framework-claude-pydantic-ai)
- [17] [fastmcp](https://github.com/PrefectHQ/fastmcp)
- [18] [Quickstart](https://gofastmcp.com/getting-started/quickstart)
- [19] [Introducing the LangGraph Functional API](https://www.langchain.com/blog/introducing-the-langgraph-functional-api)
- [20] [How to Choose an AI Agent Framework](https://www.langchain.com/resources/ai-agent-frameworks)
- [21] [Guardrails](https://openai.github.io/openai-agents-python/guardrails)
- [22] [Agents](https://openai.github.io/openai-agents-python/agents)
- [23] [Interrupt](https://reference.langchain.com/python/langgraph/types/interrupt)
- [24] [The Agent Execution Runtime: A Missing Layer in the AI Stack](https://www.augmentcode.com/guides/agent-runtime-infrastructure-layer)
- [25] [Most people still lump everything into “agent frameworks”...](https://www.linkedin.com/posts/brijpandeyji_most-people-still-lump-everything-into-agent-activity-7409465945489829888-8sk5)
- [26] [Introducing the LangGraph Functional API](https://blog.langchain.com/introducing-the-langgraph-functional-api)