# Lesson 13: Agent Frameworks Overview & Comparison

In the previous lesson, we introduced the two capstone projects we will build: an adaptable research agent and a reliable writing agent.

That leaves us with a critical decision: which framework should we use to build these projects? The ecosystem is new, evolving quickly, and crowded with options. Choosing for the wrong reasons can lock you into brittle abstractions; choosing too late can stall a project. This lesson is a guide to making that decision. We will compare the most popular libraries: LangGraph, OpenAI Agents SDK, AgentKit, CrewAI, PydanticAI, AutoGen, Claude Agent SDK, and FastMCP by focusing on their philosophies, abstractions, and trade-offs, not just their APIs.

We will anchor this comparison in our capstone architecture. You will learn how we evaluated the options, why we changed direction mid-build, and how to reason about framework choice under uncertainty. As you read, keep two concepts in mind: LangGraph’s interrupts and checkpoints, which enable auditable, resumable workflows, and the Model Context Protocol (MCP) as your interoperability layer (think “USB-C for AI,” so tools you build today can plug into multiple runtimes tomorrow).

We will show how this plays out in practice: our research agent ships as a FastMCP server, while our writing system uses a LangGraph workflow that calls MCP tools.

![Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions”.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down)

Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

## Framework Choice Under Uncertainty and Why Some Selection Strategies Fail in Production

The AI agent ecosystem is new and evolving quickly, and no universal framework will satisfy every use case. This landscape is often confusing because different types of tools are frequently lumped together. To make an informed choice, you must first understand the distinct roles these tools play.

A runtime (e.g., LangGraph, CrewAI, PydanticAI, OpenAI Agents SDK, AgentKit, AutoGen) orchestrates an agent’s behavior, managing its state and control flow. A protocol (e.g., Model Context Protocol, MCP) standardizes how agents access tools and resources, ensuring that a tool built for one runtime can be used by another. Finally, a tooling framework (e.g., FastMCP) helps you implement that protocol, making it easier to build and deploy these interoperable tools.

![Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.s”.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down)

Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

These components solve different production problems. A runtime like LangGraph provides reliability features like checkpoints and interrupts for durable, auditable execution. A protocol like MCP provides tool portability, freeing you from vendor lock-in. A tooling framework like FastMCP provides the servers, clients, and transports needed to make that protocol production-ready.

A common mistake is choosing a framework based on hype or a simple “Hello, World” example without considering the real demands of a production system. This often leads to one of two traps: either you pick a framework that is too simple and lacks the reliability primitives for your use case, or you choose one that is too complex and imposes unnecessary overhead.

We learned this firsthand. We initially planned to build our research agent with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was a wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes Instead of Brands

To avoid these traps, you need a way to evaluate frameworks based on principles. Here are four decision axes that can help you analyze any new library and determine if it fits your project’s needs.

![Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks”.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down)

Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

1. **Control-Flow Explicitness vs. LLM-Driven Autonomy:** Frameworks exist on a spectrum of control. At one end, graph-based systems like LangGraph give you explicit control over every state transition. This is ideal for deterministic, auditable workflows where you need to know precisely why the system made a particular decision. At the other end, agent loops with minimal primitives, like the OpenAI Agents SDK, favor LLM-driven autonomy. This is better for exploratory tasks where the path to a solution is not known in advance. The question to ask is: Does your application require repeatable, auditable steps, or does it need to navigate an unpredictable environment?

2. **Reliability Primitives: Production systems fail.** A good framework provides tools to handle those failures gracefully. Look for features like checkpointing (saving the agent’s state), time-travel/replay (re-running a process from a saved state), human-in-the-loop (HITL) interrupts (pausing for human approval), and durable execution (surviving restarts). LangGraph emphasizes interrupts and persistence, while PydanticAI integrates with systems like Temporal and DBOS for durable execution.

3. **Abstraction Level and Developer Experience (DX):** Frameworks offer different levels of abstraction. Some, like the OpenAI Agents SDK, provide a minimal set of primitives (Agents, Tools, Guardrails), giving you flexibility at the cost of more boilerplate. Others, like CrewAI, offer opinionated constructs (Crews, Flows) that speed up development but may be less flexible. High-level abstractions are great for building quickly, but the ability to drop to a lower level for fine-grained control is critical when you encounter edge cases.

4. **Tooling Interoperability (MCP):** To avoid rewriting your integrations every time you switch runtimes, treat your tools as standalone components. The Model Context Protocol (MCP) acts like a “USB-C for AI,” providing a standard interface for tools. By building your tools as MCP servers (for example, with FastMCP), you can plug them into any framework that speaks the protocol, including LangGraph, the OpenAI Agents SDK, or even IDEs like Cursor.

Our capstone projects clearly map to these axes. The research agent requires autonomy and interoperable tools for its exploratory nature, making a lightweight loop with MCP a good fit. The writing agent demands an explicit, auditable workflow with reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks.

- **LangGraph**: Best for stateful, auditable workflows. It uses a graph-based model with built-in support for checkpoints and interrupts, making it ideal for processes that need to be resumable and traceable.

![Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.”.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down)

LangGraph has strong, consistent daily download activity, averaging around 400K–500K downloads per day over the past three months.

<aside>
💡
**LangGraph vs. LangChain**

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers, etc.), **LangGraph** focuses specifically on **structured**, **stateful workflows**. It introduces graph-based execution with checkpoints and resumability, which are features not native to standard LangChain chains.

In short, LangChain is the toolbox, while LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions.

You will see LangChain code in the writing agent.

</aside>

- **OpenAI Agents SDK**: A lightweight, production-ready framework with a small surface area: Agents, Tools, Guardrails, Handoffs, and Sessions. It is a fast path to production if you prefer minimal abstractions and letting the LLM drive the planning.

![Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025”.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down)

The OpenAI Agents SDK library has recorded 90K–120K daily downloads over the past three months, with a slight upward trend.

- **OpenAI’s AgentKit**: A modular toolkit for building, deploying, and optimizing agents across the OpenAI platform. It unifies visual design (**Agent Builder**), frontend integration (**ChatKit**), and performance optimization (**Evals**) into one workflow. Developers can visually compose multi-agent systems, manage connectors, and embed chat-based experiences directly in their products—all backed by versioning, guardrails, and evaluation tools for safe, reliable deployment.

<aside>
💡
**OpenAI AgentKit vs. OpenAI Agents SDK**

The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration and fine-grained control. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK: it adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**.

In short, the SDK is the coding foundation, while AgentKit is the integrated platform for design, deployment, and optimization.

</aside>

- **CrewAI**: Designed for multi-agent collaboration. It uses “Crews” for role-based autonomous work and “Flows” for deterministic orchestration, with a strong emphasis on developer experience through its CLI and YAML configurations.

![Image 6: pepy.tech, daily downloads for Crewai, accessed October 15, 2025”.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down)

The CrewAI library has **daily downloads ranging between 40K and 100K**.

- **PydanticAI**: The “FastAPI for agents.” It prioritizes type safety, data validation, and durable execution through integrations with Temporal and DBOS. It shines when correctness and structured data are critical.

![Image 7: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025”.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down)

Daily downloads of Pydantic-AI doubled from ~150k in July to **300- 450k** by October 2025, demonstrating strong growth momentum.

- **AutoGen**: A flexible framework with a layered design. AutoGen Studio provides a GUI for no-code prototyping, making it an excellent exploration lab. However, Studio is explicitly not for production; for that, you would use the underlying AgentChat or core libraries.

![Image 8: pepy.tech, daily downloads for autogen, accessed October 15, 2025”.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down)

AutoGen had about **10k** daily downloads recently.

- **Claude Agent SDK**: A newer entrant from Anthropic, designed to integrate tightly with Claude models. It focuses on providing robust tool use and orchestration capabilities tailored to the strengths of their model family.

- **FastMCP**: Not a runtime, but a framework for building MCP servers and clients. It provides the “USB-C ports” for your tools, ensuring they are portable across different runtimes and stacks. It also includes production-ready features like authentication and cloud deployment.

![Image 9: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025”.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down)

FastMCP demonstrates explosive growth, with daily downloads surging from ~250k in July to peaks of over **1.2M per day** in October 2025, a 5x increase over three months.

To get a further sense of community energy, you can look at GitHub stars as of September 17, 2025. While stars do not equal quality, they can be a useful proxy for ecosystem maturity and hiring risk.

![Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026”.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down)

## Framework Deep Dive: LangGraph
