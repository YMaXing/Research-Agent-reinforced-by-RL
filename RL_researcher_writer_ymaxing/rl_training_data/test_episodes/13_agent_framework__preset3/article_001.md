# How to Choose an AI Agent Framework: A Principled Approach

In our last lesson, we introduced the scope and design of our two capstone projects: Nova, an adaptable and interactive research agent, and Brown, a reliable and auditable writing agent. These projects are not just academic exercises; they represent the kind of complex, production-grade systems AI engineers are building today. But before we write a single line of code for them, we face a critical decision: which framework should we use?

Choosing the right framework is one of the most consequential decisions you will make. The wrong choice can lead to brittle abstractions that break under real-world load, stalled progress in a fast-moving ecosystem, or hidden gaps in durability that only appear after weeks of investment. To build our agents, we will rely on two core concepts: LangGraph's interrupts and checkpoints for Brown's resumable auditability, and the Model Context Protocol (MCP) as a universal interoperability layer to keep Nova's tools portable.

This lesson focuses on the philosophies, core abstractions, and production trade-offs of the agent framework landscape. We will not be writing "hello world" tutorials. Instead, we will arm you with a set of decision principles to help you navigate this complex space. Our reference architecture will be the one we use for our capstones: the research agent built as a lightweight MCP server that any client can steer, and the writing agent built as a durable workflow that exposes its capabilities as coarse-grained MCP tools.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down
Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

With the capstones as our concrete reference, we can now examine why framework selection under uncertainty so often fails in production and what layers actually solve which problems.

## Framework Choice Under Uncertainty

The AI agent ecosystem is new and evolving quickly. No single framework will satisfy every use case. To choose wisely, you must first distinguish between three layers that are often conflated: the runtime, the protocol, and the tooling framework. Each layer solves a distinct set of production problems. The **runtime** (e.g., LangGraph, CrewAI) provides the infrastructure for durable execution, state management, and orchestration [[49]](https://www.guild.ai/glossary/ai-agent-runtime). The **protocol** (e.g., MCP) prevents tool lock-in by standardizing how agents and tools communicate, ensuring portability [[47]](https://www.linkedin.com/posts/brijpandeyji_most-people-still-lump-everything-into-agent-activity-7409465945489829888-8sk5). The **tooling framework** (e.g., FastMCP) provides the scaffolding for building and deploying these tools with a good developer experience.

While MCP is our focus, it is part of a broader landscape of emerging standards. Other protocols like the Agent Communication Protocol (ACP) and Agent-to-Agent (A2A) protocol are also working to solve interoperability. ACP focuses on REST-native messaging, and A2A enables peer-to-peer task delegation. This illustrates that the protocol layer itself is an active area of innovation aimed at preventing a fragmented ecosystem. [[73]](https://arxiv.org/html/2505.02279v1)

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down
Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

Engineers often select frameworks based on hype cycles or simple "hello-world" demos. This leads to common failure modes. You might choose a framework that is too simple and lacks the reliability primitives for production, or one that is overly complex and introduces unnecessary overhead for exploratory work. For example, a framework might excel at prototyping but lack features for durable execution, process isolation, or multi-tenant security, which are essential for production environments [[48]](https://www.augmentcode.com/guides/agent-runtime-infrastructure-layer). The initial choice between interactive and deterministic workloads is a good starting point for assessing a framework's fit.

We learned this firsthand. We initially planned to build our research agent with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was the wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes Instead of Brands

To avoid these traps, you need a way to evaluate frameworks based on stable principles rather than transient brand names. We have found four decision axes that help analyze any new library and determine if it fits your project’s needs.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down
Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

The first axis is **control-flow explicitness versus LLM-driven autonomy**. Graph-based frameworks like LangGraph offer determinism through explicit nodes and edges, providing auditability for every state transition. This is ideal for workflows where you need to know precisely why the system made a decision. In contrast, lightweight agent loops, like those in the OpenAI Agents SDK, favor exploration and adaptability, which is better for tasks where the path to a solution is unknown. This choice is increasingly influenced by external factors; regulations like the EU AI Act, which emphasize human control for high-risk systems, are pushing enterprises toward auditable workflows over unbounded autonomy. [[74]](https://www.nice.com/agentic-ai/agentic-ai-governance-frameworks)

The second axis is **reliability primitives**. Production systems fail. A good framework provides tools to handle those failures gracefully. Look for features like checkpointing, time-travel replay, human-in-the-loop (HITL) interrupts, and durable execution across restarts. These are non-negotiable for our writing agent but less important for the research agent. LangGraph emphasizes interrupts and persistence, while PydanticAI integrates with systems like Temporal and DBOS for durable execution. [[7]](https://docs.langchain.com/oss/python/langgraph/persistence), [[67]](https://ai.pydantic.dev/durable_execution/overview/) These features enable a strategy of **risk-based autonomy**, where an agent’s freedom is scaled according to its task's importance, ensuring tighter controls for high-stakes actions. [[74]](https://www.nice.com/agentic-ai/agentic-ai-governance-frameworks)

The third axis is **abstraction level and developer experience (DX)**. Some frameworks, like the OpenAI Agents SDK, provide minimal primitives that require more boilerplate but deliver greater flexibility. Others, like CrewAI, offer opinionated constructs that accelerate initial development but may reduce adaptability later on.

The final axis is **tooling interoperability**. MCP functions as the USB-C of AI, providing a standard interface for tools. It lets you write tools once as MCP servers using a framework like FastMCP and reuse them across different runtimes and IDEs, including LangGraph or the OpenAI Agents SDK, without rewriting them. [[70]](https://gofastmcp.com/)

Our capstone projects map clearly to these axes. The research agent requires autonomy and interoperable tools for its exploratory nature, making a lightweight loop with MCP a good fit. The writing agent demands an explicit, auditable workflow with reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks.

**LangGraph**'s philosophy is built on a stateful graph model with native checkpoints and interrupts for auditable workflows. This makes it ideal for processes that need to be resumable and traceable. [[7]](https://docs.langchain.com/oss/python/langgraph/persistence), [[72]](https://docs.langchain.com/oss/python/langgraph/workflows-agents) The library shows strong, consistent daily download activity, averaging around 400K–500K downloads per day.

<aside>
💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers), **LangGraph** focuses specifically on **structured, stateful workflows**. It introduces graph-based execution with checkpoints and resumability, features not native to standard LangChain chains. In short, LangChain is the toolbox, while LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions. [[72]](https://docs.langchain.com/oss/python/langgraph/workflows-agents) You will see LangChain code in the writing agent.
</aside>

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down
Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.

The **OpenAI Agents SDK** offers a minimal API surface consisting of agents, tools, guardrails, handoffs, and sessions. It favors lightweight, Python-native loops over compiled state machines. [[71]](https://openai.github.io/openai-agents-python/) The library has recorded 90K–120K daily downloads over the past three months, with a slight upward trend.

<aside>
💡 OpenAI AgentKit vs OpenAI Agents SDK

The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration and fine-grained control. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK: it adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**. In short, the SDK is the coding foundation, while AgentKit is the integrated platform for design, deployment, and optimization. [[18]](https://www.digitalapplied.com/blog/openai-agentkit-complete-guide)
</aside>

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down
Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.

**AgentKit** is a modular toolkit for building, deploying, and optimizing agents across the OpenAI platform. It unifies a visual builder, connectors (including MCP), ChatKit for embedding UIs, and evaluation infrastructure. [[17]](https://openai.com/index/introducing-agentkit) Developers can visually compose multi-agent systems, manage data sources, and embed chat experiences directly in their products, all backed by versioning and guardrails.

**CrewAI** features a dual architecture: role-based autonomous crews for collaborative exploration versus event-driven flows for deterministic control. It also provides a strong developer experience through its CLI and YAML configurations. [[22]](https://docs.crewai.com/en/introduction) The library has daily downloads ranging between 40K and 100K.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down
Image 6: Source: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.

**PydanticAI** emphasizes type safety, schema-driven validation, and durable execution through integrations with systems like Temporal, DBOS, or Prefect. [[27]](https://realpython.com/pydantic-ai) Daily downloads have doubled from ~150k in July to 300-450k by October 2025, demonstrating strong growth.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down
Image 7: Source: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.

**AutoGen** from Microsoft takes a layered approach. Its Studio GUI is explicitly positioned for exploration and not production, with the idea that successful patterns are later hardened using its AgentChat or core libraries. [[32]](https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems)

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down
Image 8: Source: pepy.tech, daily downloads for autogen, accessed October 15, 2025.

The **Claude Agent SDK** is a newer entrant from Anthropic. It offers tight integration with the Claude model family, using its strengths in large context and tool use, but currently has a smaller ecosystem. [[9]](https://www.morphllm.com/ai-agent-framework) Its design philosophy emphasizes giving agents access to the same real-world tools that humans use, such as the terminal and file system, rather than abstract API wrappers. [[13]](https://aankitroy.com/blog/claude-agent-sdk-building-agents-that-work)

**FastMCP** is a tooling layer, not a runtime. It lets you build MCP-compliant servers and clients, making your tools portable across any runtime or IDE. [[16]](https://github.com/PrefectHQ/fastmcp) It has shown explosive growth, with daily downloads surging from ~250k in July to over 1.2M per day in October 2025.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down
Image 9: Source: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.

We use adoption metrics like download trends and GitHub stars as a proxy for a framework's maturity, ecosystem health, and long-term maintenance burden. While stars measure curiosity, download counts and release velocity can indicate a committed user base solving real problems. For example, some frameworks with high star counts have low release cadences, while others with fewer stars ship frequently, suggesting a smaller but more active community. [[55]](https://medium.com/@rosgluk/the-ai-agent-star-race-i-pulled-live-github-data-for-20-frameworks-in-may-2026-b4919dfba5e4)

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down
Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026.

It is important to avoid single-framework dogma. Hybrid patterns are common and powerful. For example, you can consume FastMCP tools inside a LangGraph workflow or migrate from an AutoGen prototype to a more hardened runtime. We will now deep-dive into each framework, using our four axes and capstone needs as constant evaluation lenses.

## Framework Deep Dive: LangGraph

### Graph-Based Modeling and Primitives
LangGraph uses a graph-based modeling approach where nodes are Python functions and edges are explicit transitions. This design makes complex, multi-step logic transparent and auditable. Its core production primitives include interrupts for human-in-the-loop workflows, persistence and checkpointing for resumability, and time-travel debugging that lets you replay and branch from any prior state. [[6]](https://reference.langchain.com/python/langgraph/types/interrupt), [[7]](https://docs.langchain.com/oss/python/langgraph/persistence) By capturing each state transition, this transforms a transient execution into a replayable state machine, allowing engineers to trace failures back to specific nodes and inspect intermediate states. [[75]](https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171)

### API Styles and Use Cases
The framework offers two definition styles: a "graph API" for fully explicit graphs and a "functional API" that uses decorators. [[43]](https://www.langchain.com/blog/introducing-the-langgraph-functional-api) This creates a trade-off between a steeper learning curve and the payoff of a deterministic, observable system. LangGraph's functional API offers less boilerplate for rapid prototyping, while the graph API provides explicit control for complex branching and collaboration. [[42]](https://www.linkedin.com/posts/khalid-husain-3002aa216_choosing-between-graph-and-functional-apis-activity-7396757303217029120-VIK3) However, LangGraph can be overkill for simple, exploratory scripts where lighter loops are more efficient. Its strength lies in repeatable, auditable processes like our writing agent, where the upfront modeling investment is justified by the built-in safety, observability, and durability. This contrasts sharply with lighter, autonomous loops that prioritize flexibility over structured control.

Having examined a graph-centric, reliability-first option, we now turn to a deliberately minimal alternative.

## Framework Deep Dive: OpenAI Agents SDK

### Philosophy and Core Primitives
The OpenAI Agents SDK embodies a philosophy of minimal primitives, deliberately reducing the conceptual surface area while still enabling powerful agentic applications. [[52]](https://www.langchain.com/resources/ai-agent-frameworks) Its core concepts are simple and interrelated. **Agents** are LLMs equipped with instructions and **Tools**. **Guardrails** provide validation for agent inputs and outputs. **Handoffs** allow agents to delegate tasks to other, more specialized agents, and **Sessions** automatically manage conversation history across multiple runs. [[37]](https://cohorte.co/blog/mastering-the-openai-agents-sdk-a-field-guide-for-busy-developers-ai-vps)

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down
Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.

### Execution Model and Trade-offs
The execution model is one of its key differentiators. Unlike the compiled state machines in graph systems, the SDK uses direct Python control flow. Orchestration is handled with standard constructs like `if/else` statements and loops. [[53]](https://www.langchain.com/blog/how-to-think-about-agent-frameworks) This Python-native approach provides a familiar development experience and a fast path to production for teams that prefer lightweight orchestration and sensible defaults.

However, this simplicity comes with a significant reliability trade-off. Features like durable pause, resume, and checkpointing are not provided out of the box and must be implemented by the development team. [[54]](https://pub.towardsai.net/a-developers-guide-to-agentic-frameworks-in-2026-3f22a492dc3d) This creates critical failure modes in production. When an agent crashes mid-task, all progress is lost. Without a distributed locking mechanism, concurrent agents can pick up the same task and produce duplicate work. [[76]](https://www.diagrid.io/solutions/openai-agents-production) This makes the SDK a strong choice for stateless or short-lived tasks but requires substantial engineering effort to build the durability layer needed for long-running, stateful applications.

The natural extension of this minimal SDK is a full-lifecycle platform built on top of it.

## Framework Deep Dive: AgentKit

### A Full Lifecycle Toolkit
AgentKit is a complete lifecycle toolkit layered on top of the OpenAI Agents SDK, covering design, deployment, and optimization. It extends the SDK by adding visual workflow design, UI embedding, and a robust evaluation infrastructure, providing an end-to-end environment for building and managing agents. [[17]](https://openai.com/index/introducing-agentkit)

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down
Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.

### Components and Value Proposition
Its key components provide a comprehensive platform. The **Agent Builder** is a drag-and-drop canvas for designing and versioning multi-agent workflows. [[19]](https://www.nudgesecurity.com/post/openai-agentkit-and-agent-builder-building-secure-ai-agents) The **Connector Registry** centralizes data connections, including third-party MCPs. [[20]](https://medium.com/@leucopsis/openais-agentkit-review-c83bee3c3d02) **ChatKit** is a toolkit for embedding agentic UIs directly into your products. [[17]](https://openai.com/index/introducing-agentkit) Finally, its **Evals and Reinforcement Fine-Tuning (RFT)** capabilities allow you to measure, grade, and improve agent performance over time. [[18]](https://www.digitalapplied.com/blog/openai-agentkit-complete-guide)

AgentKit adds clear value over the raw SDK for teams that need no-code workflow design, versioning, and continuous improvement loops. While it is strongest when staying inside the OpenAI stack, its growing support for MCP connectors improves its interoperability. However, integrating third-party MCP servers can introduce security risks like data leakage or tool poisoning if not properly managed, creating new challenges for visual, no-code environments. [[77]](https://labs.zenity.io/p/analyzing-the-security-risks-of-openai-s-agentkit)

We now examine a framework whose duality spans both autonomous crews and structured flows.

## Framework Deep Dive: CrewAI

### The Duality of Crews and Flows
CrewAI is built around a powerful duality: **Crews** and **Flows**. This dual architecture allows you to combine the collaborative intelligence of autonomous agents with the precise control of deterministic workflows. [[22]](https://docs.crewai.com/en/introduction)

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcc81dc-f35c-4a6b-95e8-557db10090a9/e0cb631a-91ae-46fc-a332-d5e1afd61c80/w=1920,quality=90,fit=scale-down
Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`.

**Crews** are designed for role-based, autonomous collaboration. You define agents with specific roles, goals, and tools, and they work together to solve a problem, much like a human team. This is ideal for tasks that benefit from a division of labor and collaborative problem-solving. [[23]](https://www.c-sharpcorner.com/article/what-are-crews-vs-flows-in-crewai) **Flows**, on the other hand, are for event-driven, deterministic orchestration. They give you fine-grained control over the execution path, allowing you to manage state and define how different components interact. [[26]](https://docs.crewai.com/en/concepts/flows) This role-based design mirrors coordination patterns from multi-agent systems (MAS) research in fields like robotics, which often use centralized supervisors or decentralized peer-to-peer communication to manage collaboration. [[78]](https://xue-guang.com/post/llm-marl)

### Developer Experience and Use Cases
The typical development pattern is to start with an autonomous crew for rapid prototyping and then introduce a flow to add structure and control as your requirements become more defined. This approach is supported by a strong developer experience, with CLI scaffolding and YAML definitions for agents and tasks, as well as performance optimizations like lazy-loading dependencies to reduce cold-start latency. [[79]](https://github.com/crewaiinc/crewai) CrewAI finds its sweet spot in multi-agent handoff scenarios, like researcher-to-writer workflows, where role clarity accelerates development. However, its opinionated constructs can lead to configuration overhead and reduced flexibility when edge cases appear. [[24]](https://vadim.blog/crewai-unique-features)

Another framework approaches the problem through the lens of type safety and compile-time contracts.

## Framework Deep Dive: PydanticAI

### A Philosophy of Type Safety
PydanticAI brings a FastAPI-like philosophy to agent development, where Pydantic models and type hints create compile-time contracts between your code and the LLM's behavior. [[27]](https://realpython.com/pydantic-ai) This schema-driven approach ensures data integrity and makes your application more reliable by providing runtime validation.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/0454e524-5d87-4288-82d4-3abd2b78a6f2/image/w=1920,quality=90,fit=scale-down
Image 14: Diagram illustrating PydanticAI's design philosophy.

### Production Features and Trade-offs
Its production-oriented features are a key strength. It offers **durable execution integrations** with systems like Temporal, DBOS, or Prefect, allowing agents to survive restarts and handle long-running tasks. It also has built-in **graph support** for non-linear workflows. [[27]](https://realpython.com/pydantic-ai) These integrations draw on principles from data pipeline orchestration, where durable state management and automatic retries are essential for reliability. Some advanced patterns even implement agent tools as durable workflows, ensuring every action is auditable and fault-tolerant. [[80]](https://temporal.io/blog/orchestrating-ambient-agents-with-temporal) The developer experience is enhanced by automatic schema generation from type hints and docstrings, as well as structured output with automatic retries on validation failure.

This approach requires an up-front investment in defining schemas, which can be a learning curve for teams new to strict typing. However, the payoff is correctness guarantees. PydanticAI is best suited for projects where structured data correctness and resumable tasks are paramount, aligning well with our writing agent’s auditability needs.

We now look at a layered system that explicitly separates experimentation from production.

## Framework Deep Dive: AutoGen

### A Layered Approach to Development
AutoGen from Microsoft is designed with a layered architecture that deliberately separates experimentation from production hardening. This allows for a flexible development process, moving from rapid prototyping to robust implementation. [[32]](https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems)

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down
Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.

The framework consists of three main layers. **AutoGen Studio** is a low-code GUI that lets you prototype agent teams and workflows without writing code. **AgentChat** is a higher-level programming framework for building conversational multi-agent applications. Finally, the **Core** layer provides low-level, event-driven primitives for building scalable, custom agent systems. [[34]](https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness)

### From Exploration to Production
The typical workflow involves exploring and validating ideas visually in Studio, then hardening the successful patterns into code using the lower-level AgentChat or Core libraries. It is important to note the explicit disclaimer that Studio is a research prototype and not intended for production environments. AutoGen's strength lies in its use as an R&D laboratory for discovering multi-agent conversation patterns. Its supervisor-worker architecture is a classic example of the centralized coordination pattern found in multi-agent systems research. [[78]](https://xue-guang.com/post/llm-marl) However, this flexibility comes with a trade-off: the team must re-implement reliability, security, and observability when moving to production.

A newer entrant focuses on tight model-family integration.

## Framework Deep Dive: Claude Agent SDK

### Tight Model Integration
The Claude Agent SDK is a newer entrant from Anthropic that is built on a philosophy of tight integration with its model family. [[11]](https://www.mindstudio.ai/blog/agent-sdk-vs-framework-claude-pydantic-ai) This approach is designed to take advantage of the specific strengths of Claude models, such as their large context windows, strong reasoning capabilities, and fine-grained control over tool use. The SDK provides ergonomic tool calling and orchestration tailored to the Anthropic ecosystem, aiming to deliver model-optimized performance. [[12]](https://buildwithaws.substack.com/p/inside-the-claude-agent-sdk-from)

### Opportunity vs. Risk
However, as a newer framework, it comes with trade-offs. The community is smaller, there are fewer third-party integrations, and the API surface is still evolving. Teams considering the Claude Agent SDK must balance the potential for high performance against the risks associated with a less mature ecosystem. It is the clearest choice for teams already committed to the Anthropic stack who want native performance and are willing to accept smaller community support.

The final deep dive examines a non-runtime layer that complements every option above.

## Framework Deep Dive: FastMCP

### The Universal Tooling Layer
FastMCP is not a runtime; it is a tooling framework that lets you build MCP-compliant servers and clients. [[16]](https://github.com/PrefectHQ/fastmcp) This makes your tools, resources, and prompts portable across any runtime or IDE that speaks the protocol. The core benefit is interoperability. You can write a tool once and reuse it inside LangGraph, the OpenAI SDK, or any other compatible system.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/745828fd-27e2-4a50-b613-7275a1e1dceb/image/w=1920,quality=90,fit=scale-down
Image 16: FastMCP Architecture and Interoperability

### Production Patterns and Developer Experience
Beyond the protocol itself, FastMCP provides production-ready extensions for authentication, server composition, and cloud deployment. However, as tool catalogs grow, new scalability failure modes can emerge, such as "tool-space interference," where the presence of many otherwise reasonable tools can degrade end-to-end task performance. [[81]](https://www.microsoft.com/en-us/research/blog/tool-space-interference-in-the-mcp-era-designing-for-agent-compatibility-at-scale) This is reflected in our capstone architecture: the research agent (Nova) is implemented as a FastMCP server that any client can steer, while the writing agent (Brown) exposes its complex workflows as coarse-grained MCP tools.

<aside>
💡 Pattern: tools-as-workflows (Brown)

For our writing agent (Brown), we wrap each workflow entry point as a **coarse-grained MCP tool** (e.g., `generate_article`, `edit_article`, `edit_selected_text`). The MCP tool handler simply **kicks off the corresponding LangGraph run**, returns progress messages, and finally yields artifacts and diffs. This gives you MCP portability (e.g., usage in Cursor or Claude Code) **without** losing LangGraph’s durability and auditability. You’ll learn more about this in later lessons.
</aside>

The developer experience is designed to be simple and Pythonic. You can expose a function as a tool with a single decorator, and FastMCP handles the schema generation and transport details automatically.

1. Here is a quick example from the official documentation.
    ```python
    from fastmcp import FastMCP
    
    mcp = FastMCP("My MCP Server")
    
    @mcp.tool
    def greet(name: str) -> str:
        return f"Hello, {name}!"
    
    if __name__ == "__main__":
        mcp.run()
    ```

With our deep dives complete, we can now synthesize everything into a decision matrix and make some tentative forecasts.

## Choosing for Your Project: Decision Matrix & Tentative Forecasts

To help you choose the right framework for your project, we have created a decision matrix that maps common project needs to the relative strengths of each framework.

Table 1: Decision matrix comparing AI agent frameworks against common needs
| Feature | LangGraph | PydanticAI | OpenAI SDK | AgentKit | CrewAI | AutoGen | FastMCP |
|---|---|---|---|---|---|---|---|
| **Durability/HITL/Replay** | ✅ | | | | | ✅ | |
| **Typed Contracts + Durable Execution** | | ✅ | | | | | ✅ |
| **Few Primitives + Guardrails/Handoffs** | ✅ | | ✅ | ✅ | | | ✅ |
| **Role-based Teams + Quick Scaffolding** | | | | ✅ | ✅ | ✅ | |
| **Exploration Lab** | | | ✅ | ✅ | ✅ | ✅ | |
| **Tool Portability Across Stacks** | | ✅ | | ✅ | | | ✅ |

This matrix should be treated as a snapshot in time. The agent framework ecosystem is constantly evolving, so you should always re-evaluate your choices against our four decision axes whenever libraries release major updates.

Based on these axes, we can offer some forecasts. LangGraph and PydanticAI are strong choices for reliability-heavy workflows. The OpenAI SDK is well-suited for lightweight simplicity, while AgentKit is a good fit when visual design and continuous evaluation loops are required. CrewAI excels at rapid multi-agent prototyping, AutoGen serves as a strong R&D starting point, and FastMCP is emerging as the universal tooling substrate.

In practice, hybrid patterns are common. You might consume FastMCP tools inside a LangGraph workflow, migrate from an AutoGen Studio prototype to a hardened runtime, or expose a complex graph as a single MCP command to gain IDE portability without sacrificing durability. To make this theory concrete, we will now share the actual pivots we made while building the course capstones.

## Our Capstone Pivots

Let’s apply this matrix to our capstone project. Our decision-making process evolved as we built, highlighting the importance of choosing the right tool for the job.

Our initial plan was to use LangGraph for both agents. However, we quickly discovered that the research agent’s need for high interactivity and divergent exploration made a rigid graph cumbersome. The predefined structure of a graph was too restrictive for a task that required constant replanning and the dynamic addition of new tools. Flexible MCP tools, which could be developed and exposed independently, proved to be a superior choice for Nova.

The writing agent, on the other hand, had the opposite requirements. Its repeatable, auditable process demanded the features that LangGraph excels at: checkpoints for saving state, HITL interrupts for human review, and time-travel replay capabilities for debugging and verification. These reliability primitives were non-negotiable for a system intended to produce high-quality, consistent output.

The result is a hybrid architecture. Nova is implemented as a FastMCP server that any client, including IDEs, can steer. Brown is implemented as a LangGraph workflow whose entry points are exposed as coarse-grained MCP tools. This pattern of wrapping complex internal workflows behind single MCP commands allows us to gain portability without sacrificing durability or auditability. Benchmarks of similar hybrid systems show they can achieve high throughput (over 400 requests/second) with fault tolerance and state persistence via Redis checkpointing, validating the robustness of this approach. [[82]](https://mcp-server-langgraph.mintlify.app/comparisons/benchmarks) Brown currently exposes three tools: `generate_article`, `edit_article`, and `edit_selected_text`.

We considered the OpenAI Agents SDK but ultimately deprioritized it because it lacked the first-class persistence and deep MCP integration required for the long-running nature of both capstone tasks. These real-world pivots illustrate the central lesson of this module.

## Conclusion

The core takeaway from this lesson is to prioritize stable concepts over transient brand names. Stateful graphs, typed contracts, durable execution, and MCP standardization are the foundational ideas that will outlast any single framework. These principles provide a durable mental model for evaluating technology in a rapidly changing field. The MCP specification, in particular, is a high-leverage investment. Understanding it once gives you tool portability across every current and future stack that supports it, decoupling your application's core logic from the underlying runtime.

Our recommended selection process is simple: apply the four decision axes to your project, start with the smallest viable stack that meets your reliability needs, and keep all your tooling portable via MCP. This approach allows for flexibility and future-proofing. For example, a common migration path might be to begin exploration in AutoGen Studio, extract successful patterns into FastMCP tools, and then anchor your production system in a robust runtime like LangGraph or PydanticAI. This allows you to move from a low-code, experimental environment to a hardened, production-ready system without rewriting your core tool logic.

In our next lesson, we will cover system design, including model selection, cost and latency trade-offs, and HITL placement. After that, we will begin the hands-on capstone builds, where you will see this hybrid FastMCP-plus-LangGraph stack in action. We will build Nova with FastMCP, focusing on its server/client architecture, data ingestion, and research loops. Then, we will build Brown with LangGraph and FastMCP, implementing its auditable workflow, context engineering for profiles, and evaluator-optimizer cycles with human-in-the-loop editing. This will bring the principles we have discussed today into concrete practice.

## References

- [1] LLM-Driven Autonomy. (n.d.). Emergent Mind. https://www.emergentmind.com/topics/llm-driven-autonomy
- [2] ControlFlow 0.9: Take control of your agents. (n.d.). Prefect.io. https://www.prefect.io/blog/controlflow-0-9-take-control-of-your-agents
- [3] General-purpose systems. (n.d.). arXiv. https://arxiv.org/html/2508.17281v2
- [4] Agentic UAVs Framework. (n.d.). arXiv. https://arxiv.org/html/2509.13352v2
- [5] Agent Frameworks. (n.d.). Arize. https://arize.com/ai-agents/agent-frameworks
- [6] langgraph.types.interrupt. (n.d.). LangChain. https://reference.langchain.com/python/langgraph/types/interrupt
- [7] Persistence. (n.d.). LangChain. https://docs.langchain.com/oss/python/langgraph/persistence
- [8] Interrupts. (n.d.). LangChain. https://docs.langchain.com/oss/javascript/langgraph/interrupts
- [9] AI Agent Framework. (n.d.). MorphL. https://www.morphllm.com/ai-agent-framework
- [10] Building Intelligent Agents With Claude Agent SDK. (n.d.). C-sharpcorner. https://www.c-sharpcorner.com/article/building-intelligent-agents-with-claude-agent-sdk-features-comparisons-and-be
- [11] Agent SDK vs Framework. (n.d.). MindStudio. https://www.mindstudio.ai/blog/agent-sdk-vs-framework-claude-pydantic-ai
- [12] Inside the Claude Agent SDK. (n.d.). Build with AWS. https://buildwithaws.substack.com/p/inside-the-claude-agent-sdk-from
- [13] Claude Agent SDK: Building Agents That Work. (n.d.). Ankit Roy. https://aankitroy.com/blog/claude-agent-sdk-building-agents-that-work
- [14] LangGraph MCP. (n.d.). Generect. https://generect.com/blog/langgraph-mcp
- [15] Servers Tools. (n.d.). FastMCP. https://gofastmcp.com/servers/tools
- [16] FastMCP GitHub. (n.d.). GitHub. https://github.com/PrefectHQ/fastmcp
- [17] Introducing AgentKit. (n.d.). OpenAI. https://openai.com/index/introducing-agentkit
- [18] OpenAI AgentKit Complete Guide. (n.d.). Digital Applied. https://www.digitalapplied.com/blog/openai-agentkit-complete-guide
- [19] OpenAI AgentKit and Agent Builder. (n.d.). Nudge Security. https://www.nudgesecurity.com/post/openai-agentkit-and-agent-builder-building-secure-ai-agents
- [20] OpenAI’s AgentKit Review. (n.d.). Medium. https://medium.com/@leucopsis/openais-agentkit-review-c83bee3c3d02
- [21] OpenAI Agent Builder Step-by-Step Guide. (n.d.). Composio. https://composio.dev/content/openai-agent-builder-step-by-step-guide-to-building-ai-agents-with-mcp
- [22] Introduction. (n.d.). CrewAI. https://docs.crewai.com/en/introduction
- [23] What Are Crews vs. Flows in CrewAI?. (n.d.). C-sharpcorner. https://www.c-sharpcorner.com/article/what-are-crews-vs-flows-in-crewai
- [24] CrewAI Unique Features. (n.d.). Vadim.blog. https://vadim.blog/crewai-unique-features
- [25] CrewAI GitHub. (n.d.). GitHub. https://github.com/crewaiinc/crewai
- [26] Flows. (n.d.). CrewAI. https://docs.crewai.com/en/concepts/flows
- [27] Pydantic AI. (n.d.). Real Python. https://realpython.com/pydantic-ai
- [28] The Complete Guide to Using Pydantic for Validating LLM Outputs. (n.d.). Machine Learning Mastery. https://machinelearningmastery.com/the-complete-guide-to-using-pydantic-for-validating-llm-outputs
- [29] Intro to Pydantic. (n.d.). MolSSI. https://education.molssi.org/type-hints-pydantic-tutorial/chapters/IntroToPydantic.html
- [30] Validators. (n.d.). Pydantic. https://pydantic.dev/docs/validation/latest/concepts/validators
- [31] Pydantic: A Data Engineer’s Guide to Data Validation. (n.d.). Towards AI. https://pub.towardsai.net/pydantic-a-data-engineers-guide-to-data-validation-ca88a8d9bb2f
- [32] Microsoft AutoGen: Orchestrating Multi-Agent LLM Systems. (n.d.). Tribe.ai. https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems
- [33] Getting Started with AutoGen Framework. (n.d.). Ravichaganti.com. https://ravichaganti.com/blog/getting-started-with-autogen-framework-for-building-ai-agents-and-applications
- [34] AutoGen v0.4: Reimagining the foundation of agentic AI. (n.d.). Microsoft Research. https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness
- [35] AutoGen. (n.d.). IBM. https://www.ibm.com/think/topics/autogen
- [36] A Friendly Introduction to the AutoGen. (n.d.). Victor Dibia. https://newsletter.victordibia.com/p/a-friendly-introduction-to-the-autogen
- [37] Mastering the OpenAI Agents SDK. (n.d.). Cohorte. https://cohorte.co/blog/mastering-the-openai-agents-sdk-a-field-guide-for-busy-developers-ai-vps
- [38] Agents. (n.d.). OpenAI. https://openai.github.io/openai-agents-python/agents
- [39] Migrating from OpenAI Agents SDK to Claude Agent SDK. (n.d.). Claude Platform. https://platform.claude.com/cookbook/claude-agent-sdk-04-migrating-from-openai-agents-sdk
- [40] Guardrails. (n.d.). OpenAI. https://openai.github.io/openai-agents-python/guardrails
- [41] Agents Guide. (n.d.). OpenAI. https://developers.openai.com/api/docs/guides/agents
- [42] Choosing between Graph and Functional APIs. (n.d.). LinkedIn. https://www.linkedin.com/posts/khalid-husain-3002aa216_choosing-between-graph-and-functional-apis-activity-7396757303217029120-VIK3
- [43] Introducing the LangGraph Functional API. (n.d.). LangChain Blog. https://www.langchain.com/blog/introducing-the-langgraph-functional-api
- [44] Introducing the LangGraph Functional API. (n.d.). LangChain Blog. https://blog.langchain.com/introducing-the-langgraph-functional-api
- [45] Choosing APIs. (n.d.). LangChain. https://docs.langchain.com/oss/python/langgraph/choosing-apis
- [46] Functional API for LangGraph. (n.d.). LangChain Changelog. https://changelog.langchain.com/announcements/functional-api-for-langgraph
- [47] Runtime protocols vs. tooling layers. (n.d.). LinkedIn. https://www.linkedin.com/posts/brijpandeyji_most-people-still-lump-everything-into-agent-activity-7409465945489829888-8sk5
- [48] Agent Runtime Infrastructure Layer. (n.d.). AugmentCode. https://www.augmentcode.com/guides/agent-runtime-infrastructure-layer
- [49] AI Agent Runtime. (n.d.). Guild.ai. https://www.guild.ai/glossary/ai-agent-runtime
- [50] Agent Frameworks. (n.d.). Arize. https://arize.com/ai-agents/agent-frameworks
- [51] What does the emerging AI agent stack actually look like?. (n.d.). LangChain Forum. https://forum.langchain.com/t/what-does-the-emerging-ai-agent-stack-actually-look-like/3103
- [52] AI Agent Frameworks. (n.d.). LangChain. https://www.langchain.com/resources/ai-agent-frameworks
- [53] How to think about agent frameworks. (n.d.). LangChain Blog. https://www.langchain.com/blog/how-to-think-about-agent-frameworks
- [54] A Developer’s Guide to Agentic Frameworks in 2026. (n.d.). Towards AI. https://pub.towardsai.net/a-developers-guide-to-agentic-frameworks-in-2026-3f22a492dc3d
- [55] The AI Agent Star Race. (n.d.). Medium. https://medium.com/@rosgluk/the-ai-agent-star-race-i-pulled-live-github-data-for-20-frameworks-in-may-2026-b4919dfba5e4
- [56] Top 10 Most Starred AI Agent Frameworks on GitHub 2026. (n.d.). Medium. https://techwithibrahim.medium.com/top-10-most-starred-ai-agent-frameworks-on-github-2026-df6e760a950b
- [57] Stack Overflow Analysis of Agent Frameworks. (n.d.). arXiv. https://arxiv.org/html/2510.25423v2
- [58] AI Agent Frameworks Download Spikes. (n.d.). YouTube. https://www.youtube.com/watch?v=2Yg-BPFNF5A&vl=en-US
- [59] LangChain vs. LangGraph. (n.d.). TrueFoundry. https://www.truefoundry.com/blog/langchain-vs-langgraph
- [60] LangChain vs. LangGraph. (n.d.). DuploCloud. https://duplocloud.com/blog/langchain-vs-langgraph
- [61] LangChain vs. LangGraph vs. LangSmith vs. LangFlow. (n.d.). DataCamp. https://www.datacamp.com/tutorial/langchain-vs-langgraph-vs-langsmith-vs-langflow
- [62] LangChain vs. LangGraph. (n.d.). GeeksforGeeks. https://www.geeksforgeeks.org/artificial-intelligence/langchain-vs-langgraph
- [63] LangChain vs. LangGraph. (n.d.). Milvus. https://milvus.io/blog/langchain-vs-langgraph.md
- [64] Build your first Flow. (n.d.). CrewAI. https://docs.crewai.com/guides/flows/first-flow
- [65] Introduction. (n.d.). CrewAI. https://docs.crewai.com/introduction
- [66] Quickstart. (n.d.). FastMCP. https://gofastmcp.com/getting-started/quickstart
- [67] Durable Execution. (n.d.). Pydantic AI. https://ai.pydantic.dev/durable_execution/overview/
- [68] AutoGen Studio User Guide. (n.d.). Microsoft. https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html
- [69] AutoGen. (n.d.). Microsoft. https://microsoft.github.io/autogen/stable/
- [70] FastMCP. (n.d.). FastMCP. https://gofastmcp.com/
- [71] OpenAI Agents SDK. (n.d.). OpenAI. https://openai.github.io/openai-agents-python/
- [72] Workflows and agents. (n.d.). LangChain. https://docs.langchain.com/oss/python/langgraph/workflows-agents
- [73] A Survey of Agent Interoperability Protocols. (n.d.). arXiv. https://arxiv.org/html/2505.02279v1
- [74] Agentic AI Governance Frameworks. (n.d.). NICE. https://www.nice.com/agentic-ai/agentic-ai-governance-frameworks
- [75] Debugging Non-Deterministic LLM Agents. (n.d.). dev.to. https://dev.to/sreeni5018/debugging-non-deterministic-llm-agents-implementing-checkpoint-based-state-replay-with-langgraph-5171
- [76] Running OpenAI Agents reliably in production. (n.d.). Diagrid. https://www.diagrid.io/solutions/openai-agents-production
- [77] Analyzing the Security Risks of OpenAI’s AgentKit. (n.d.). Zenity. https://labs.zenity.io/p/analyzing-the-security-risks-of-openai-s-agentkit
- [78] LLM-based Multi-Agent Cooperation: A Survey and Roadmap. (n.d.). xue-guang.com. https://xue-guang.com/post/llm-marl
- [79] CrewAI GitHub Repository. (n.d.). GitHub. https://github.com/crewaiinc/crewai
- [80] Orchestrating ambient agents with Temporal. (n.d.). Temporal.io. https://temporal.io/blog/orchestrating-ambient-agents-with-temporal
- [81] Tool-Space Interference in the MCP Era. (n.d.). Microsoft Research. https://www.microsoft.com/en-us/research/blog/tool-space-interference-in-the-mcp-era-designing-for-agent-compatibility-at-scale
- [82] Benchmarks: MCP Server with LangGraph. (n.d.). Mintlify. https://mcp-server-langgraph.mintlify.app/comparisons/benchmarks