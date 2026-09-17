# How to Choose an AI Agent Framework

In the last lesson, we introduced the scope and design of our two capstone projects: Nova, an adaptable and interactive research agent, and Brown, a reliable and auditable writing agent. These projects serve as our concrete anchors for the engineering decisions we will make throughout this course. One of the first and most critical decisions is choosing the right framework.

Making this choice late, or making the wrong one, can lead to significant problems. You might build on brittle abstractions that break under real-world load, stall your progress in a fast-moving ecosystem, or discover hidden gaps in durability only after weeks of investment. This lesson is about avoiding those traps.

We will focus on two core concepts that will recur throughout our builds. First, we will explore LangGraph’s interrupts and checkpoints, which provide the resumable auditability that our writing agent, Brown, requires. Second, we will look at the Model Context Protocol (MCP) as a universal interoperability layer that keeps our tools portable, a key requirement for our research agent, Nova.

Our high-level architecture, shown in Image 1, will be our consistent reference point. Nova is built as a lightweight MCP server that any client can steer, while Brown is a durable workflow that exposes its capabilities as coarse-grained MCP tools. This lesson will focus on the philosophies, core abstractions, and production trade-offs of various frameworks to help you understand these design choices, rather than providing simple API tutorials.![High-level architecture diagram illustrating the two capstone builds](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down)
Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

With our capstone projects as a concrete reference, we can now examine why framework selection under uncertainty so often fails in production. We will also explore the distinct problems that the runtime, protocol, and tooling layers are designed to solve.

## Framework Choice Under Uncertainty

The AI agent ecosystem is new and evolving quickly. No single framework will satisfy every use case. To choose wisely, you must distinguish between three layers that are often conflated: the runtime, the protocol, and the tooling.

The **runtime** is the orchestration and state management layer. Frameworks like LangGraph, CrewAI, and the OpenAI Agents SDK fall into this category. They are responsible for durable execution and resumability, ensuring your agent can recover from crashes and manage long-running tasks. The **protocol**, like MCP, provides a standardized interface for tools. This prevents you from being locked into a single runtime, as your tools can be reused across any compatible system. Finally, the **tooling** framework, such as FastMCP, provides ready-to-deploy components like transports and authentication, improving the developer experience.![Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down)
Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

Engineers often select frameworks based on hype or simple "hello world" demos. This can lead to common failure modes. You might choose a framework that is too simple and lacks the reliability primitives needed for production, or one that is overly complex and adds unnecessary overhead. This gap between prototype and production is where many projects fail. Without a dedicated runtime layer, production agents are vulnerable to several issues. **Shared memory store poisoning** can occur when agents without namespace-level isolation corrupt a shared backend. **Container escape** is a risk when agents share a host kernel. A single **runaway agent can exhaust host resources** without kernel-level limits. Finally, **cascading failures** can propagate across agents through shared dependencies, turning a local fault into a system-wide failure. A quick initial lens for assessing a framework's fit is to consider whether your workload is interactive and exploratory or deterministic and repeatable.

We learned this firsthand. We initially planned to build our research agent with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was a wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes Instead of Brands

To avoid these traps, you need a way to evaluate frameworks based on principles. We use four decision axes to analyze any new library and determine if it fits a project’s needs.![A diagram illustrating the four key decision axes for evaluating AI agent frameworks.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down)
Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

The first axis is **control-flow explicitness versus LLM-driven autonomy**. This choice reflects a fundamental trade-off between predictable, symbolic systems and adaptable, generative ones. This is a classic architectural choice. Symbolic designs externalize planning into deterministic modules, while neural designs use the LLM for planning, gaining adaptability but sacrificing predictability. Production systems often adopt hybrid patterns, using LLMs for high-level decomposition while enforcing symbolic constraints on tool execution to balance safety and adaptability [[11]](https://arxiv.org/html/2602.10479v1). Graph-based frameworks like LangGraph use explicit nodes and edges, functioning like state machines that enforce valid data flow [[12]](https://arxiv.org/html/2603.03655v1). This is ideal for deterministic workflows where reproducibility is essential, as the inherent non-determinism of LLMs makes them challenging for regulated environments [[13]](https://pmc.ncbi.nlm.nih.gov/articles/PMC13079118). On the other hand, lightweight agent loops, like those in the OpenAI Agents SDK, favor exploration and adaptability. The question to ask is: does your application require repeatable, auditable steps, or does it need to navigate an unpredictable environment?

The second axis is **reliability primitives**. A good framework provides tools to handle failures gracefully, borrowing lessons from safety-critical systems where isolation and deterministic execution ensure stability [[14]](https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime). Features like checkpointing, time-travel replay, human-in-the-loop (HITL) interrupts, and durable execution are non-negotiable for our writing agent but less critical for the research agent. LangGraph emphasizes interrupts and persistence [[1]](https://docs.langchain.com/oss/python/langgraph/persistence), while PydanticAI integrates with systems like Temporal and DBOS for durable execution [[2]](https://ai.pydantic.dev/durable_execution/overview/).

The third axis is **abstraction level and developer experience**. Some frameworks, like the OpenAI Agents SDK, provide minimal primitives such as Agents, Tools, and Guardrails. This requires more boilerplate code but offers greater flexibility. Others, like CrewAI, provide opinionated constructs that accelerate initial development but may reduce adaptability later.

The fourth axis is **tooling interoperability**. MCP functions as the USB-C of AI, offering a standard interface for tools. This lets you write tools once as MCP servers using a library like FastMCP [[3]](https://gofastmcp.com/) and reuse them across different runtimes, including LangGraph and the OpenAI Agents SDK.

Our capstone projects map clearly to these axes. The research agent requires autonomy and interoperable tools for its exploratory nature, making a lightweight loop with MCP a good fit. The writing agent demands an explicit, auditable workflow with strong reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks.

**LangGraph** is built on a stateful graph model with native checkpoints and interrupts for auditable workflows [[1]](https://docs.langchain.com/oss/python/langgraph/persistence). This makes it ideal for processes that need to be resumable and traceable, like our writing agent [[4]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). Its graph-based architecture is better suited for stateful applications and complex decision-making than the linear model of its predecessor, LangChain [[19]](https://milvus.io/blog/langchain-vs-langgraph.md). The framework shows strong, consistent adoption, with daily downloads averaging between 400,000 and 500,000.

<aside>
💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers, etc.), **LangGraph** focuses specifically on **structured**, **stateful workflows**. It introduces graph-based execution with checkpoints and resumability, which are features not native to standard LangChain chains.

In short, LangChain is the toolbox, while LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions [[4]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). You will see LangChain code in the writing agent.
</aside>![Daily downloads for LangGraph](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down)
Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.

The **OpenAI Agents SDK** offers a minimal API surface consisting of agents, tools, guardrails, handoffs, and sessions [[5]](https://openai.github.io/openai-agents-python/). It favors lightweight, Python-native loops over compiled state machines. Its design philosophy favors a minimal API surface over comprehensive abstractions, making it faster to understand what an agent is doing [[20]](https://www.langchain.com/resources/ai-agent-frameworks). The library has recorded between 90,000 and 120,000 daily downloads over the past three months.![Daily downloads for OpenAI Agents SDK](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down)
Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.

**AgentKit** is a modular toolkit for building, deploying, and optimizing agents across the OpenAI platform. It unifies a visual builder, connectors (including MCP), a ChatKit for embedding UIs, and evaluation infrastructure [[21]](https://openai.com/index/introducing-agentkit). Developers can visually compose multi-agent systems, manage connectors, and embed chat-based experiences directly in their products—all backed by versioning, guardrails, and evaluation tools for safe, reliable deployment.

<aside>
💡 OpenAI AgentKit vs. OpenAI Agents SDK

The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration and fine-grained control. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK: it adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**. In short, the SDK is the coding foundation, while AgentKit is the integrated platform for design, deployment, and optimization.
</aside>

**CrewAI** features a dual architecture of role-based autonomous crews for collaborative exploration and event-driven flows for deterministic control [[6]](https://docs.crewai.com/introduction). It has a strong developer experience with a command-line interface (CLI) and YAML definitions. Its daily downloads range between 40,000 and 100,000.![Daily downloads for Crewai](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down)
Image 6: Source: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.

**PydanticAI** emphasizes type safety, schema-driven validation, and durable execution through integrations with systems like Temporal, DBOS, or Prefect [[2]](https://ai.pydantic.dev/durable_execution/overview/). It uses Pydantic models to instruct the language model to return data that matches a provided schema, ensuring type-safe objects with automatic validation [[22]](https://realpython.com/pydantic-ai). Daily downloads have grown strongly, from around 150,000 in July to between 300,000 and 450,000 by October 2025.![Daily downloads for PydanticAI](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down)
Image 7: Source: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.

**AutoGen** from Microsoft takes a layered approach, with a Studio GUI for exploration, AgentChat for building conversational apps, and a core library for hardening prototypes into production systems [[7]](https://microsoft.github.io/autogen/stable/). This modular design allows developers to work at different levels of abstraction depending on their needs [[23]](https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems).![Daily downloads for autogen](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down)
Image 8: Source: pepy.tech, daily downloads for autogen, accessed October 15, 2025.

The **Claude Agent SDK** is a newer entrant from Anthropic. It offers tight integration with the Claude family of models, leveraging their strengths in large context and tool use, but it has a smaller ecosystem. It exposes the full Anthropic Messages API, allowing developers to build their own orchestration logic on top of the client library [[24]](https://www.mindstudio.ai/blog/agent-sdk-vs-framework-claude-pydantic-ai).

**FastMCP** is a tooling layer, not a runtime. It lets you build MCP-compliant servers and clients, making your tools portable across any runtime or IDE. It has shown explosive growth, with daily downloads surging from around 250,000 in July to over 1.2 million per day in October 2025.![Daily downloads for FastMCP](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down)
Image 9: Source: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.

We use adoption metrics like download trends and GitHub stars as a proxy for maturity, ecosystem health, and long-term maintenance burden. However, you should avoid committing to a single framework. Hybrid patterns are common, such as consuming FastMCP tools inside a LangGraph workflow or migrating from an AutoGen prototype to a more hardened runtime.![Bar chart showing GitHub star counts for AI agent frameworks](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down)
Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026.

We will now deep-dive into each framework, starting with LangGraph, using our four axes and capstone needs as constant evaluation lenses.

## Framework Deep Dive: LangGraph

LangGraph uses a graph-based modeling approach where nodes are Python functions and edges are explicit transitions. This design makes complex, multi-step logic transparent and auditable. Its core production primitives are what set it apart for reliability-focused applications. It offers interrupts for human-in-the-loop validation, persistence and checkpointing for resumability, and a time-travel feature that lets you replay and branch from any prior state.

However, this checkpointing introduces latency and storage overhead. Each step in the graph can generate a new snapshot, and for long-running agents with many steps, this can lead to significant storage growth [[15]](https://aerospike.com/blog/langgraph-production-latency-replay-scale). To mitigate this, LangGraph offers optimizations like `DeltaChannel`, which stores only incremental state changes, and asynchronous persistence modes that trade a small amount of recovery risk for better performance [[1]](https://docs.langchain.com/oss/python/langgraph/persistence). These features are crucial for managing the operational costs of stateful agents in production.

The framework provides two main definition styles: a "graph API" for fully explicit graphs and a "functional API" that uses decorators. This creates a trade-off between the learning curve and the level of determinism you achieve. For simple, exploratory scripts, LangGraph can be overkill, as a lighter loop might be more appropriate.

However, for repeatable and auditable processes like our writing agent, the initial modeling investment is justified. The built-in safety, observability, and durability prevent the kind of brittle failures that are common in less structured production systems. This contrasts sharply with lighter, more autonomous loops, which offer flexibility at the cost of predictability.

Having examined a graph-centric, reliability-first option, we now turn to a deliberately minimal alternative.

## Framework Deep Dive: OpenAI Agents SDK

The OpenAI Agents SDK is built on a philosophy of minimal primitives. It deliberately reduces the conceptual surface area to make it quick to learn while still enabling powerful agentic applications. The core concepts are agents, tools, guardrails, handoffs, and sessions.

**Agents** are LLMs with instructions and tools. **Tools** are Python functions agents can call to interact with the world. **Guardrails** provide a mechanism for validating agent inputs and outputs to ensure safety. **Handoffs** allow agents to delegate tasks to other, more specialized agents. Finally, **Sessions** automatically manage conversation history across multiple runs.![Diagram illustrating the core primitives of the OpenAI Agents SDK](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down)
Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.

Its execution model relies on direct Python control flow with `if/else` statements and loops, rather than a compiled state machine like in graph-based systems. The fundamental difference between the OpenAI Agents SDK and LangGraph’s functional API lies in this execution model. The OpenAI SDK uses a simple, Python-native agent loop that you control directly. In contrast, even with its decorator-based functional API, LangGraph compiles your code into an explicit, stateful graph. This underlying state machine manages execution and persistence, providing a more robust but also more constrained environment.

The SDK is a strong choice for teams that want a fast path to production and prefer lightweight orchestration with sensible defaults. However, it comes with a reliability trade-off: features like durable pause, resume, and checkpointing are not provided out of the box and must be implemented by the team.

The natural extension of this minimal SDK is a full-lifecycle platform built on top of it.

## Framework Deep Dive: AgentKit

AgentKit is a complete lifecycle toolkit layered on top of the OpenAI Agents SDK, covering design, deployment, and optimization. It extends the SDK by adding visual workflow design, UI embedding, and evaluation infrastructure, turning the code-first framework into an integrated platform.![The Homework Helper workflow in AgentKit](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down)
Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.

Its key components include:
-   **Agent Builder**: A drag-and-drop canvas for designing and versioning multi-agent workflows. Builders can compose logic visually, add guardrails, and run preview tests with inline evaluation and version control.
-   **Connector Registry**: A centralized interface for managing data connections (Dropbox, Google Drive, SharePoint, Teams, and third-party MCPs) across workspaces and organizations.
-   **ChatKit**: A toolkit for embedding agentic chat UIs directly into web or mobile products, handling streaming responses, conversation threads, and custom theming.
-   **Evals and Reinforcement Fine-Tuning (RFT)**: Expanded capabilities for measuring, grading, and improving agent performance, including datasets, automated prompt optimization, and custom graders.

AgentKit sits one layer above the OpenAI Agents SDK. You still use the SDK for code-first orchestration, but AgentKit provides the surrounding tools for design, deployment, and continuous improvement. This visual composition and built-in evaluation support safe multi-agent systems at scale. While it is optimized for the OpenAI ecosystem, its growing support for MCP connectors improves interoperability. AgentKit adds clear value for teams that need no-code workflow design, versioning, and continuous improvement loops.

We now examine a framework whose duality spans both autonomous crews and structured flows.

## Framework Deep Dive: CrewAI

CrewAI introduces a powerful duality with its two main concepts: **Crews** and **Flows**. This dual architecture allows you to balance autonomous collaboration with deterministic control.![Setting up an autonomous agent in CrewAI Studio](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcc81dc-f35c-4a6b-95e8-557db10090a9/e0cb631a-91ae-46fc-a332-d5e1afd61c80/w=1920,quality=90,fit=scale-down)
Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`.

**Crews** are designed for role-based, autonomous collaboration. You define agents with specific roles, goals, and tools, and they work together to solve a problem, much like a human team. This is ideal for tasks requiring creative problem-solving and dynamic interaction. **Flows**, on the other hand, are for event-driven, deterministic orchestration. They give you fine-grained control over the workflow, allowing you to define precise execution paths, manage state, and handle events.

A common development pattern is to start with an autonomous crew for rapid prototyping. Once the requirements become more defined, you can introduce a flow to add structure and control. The developer experience is a key focus, with features like CLI scaffolding, YAML definitions for agents and tasks, and configurable memory and persistence options.

The framework's design also reflects patterns seen in game AI, where multi-agent systems have long been used for complex coordination. For example, the Critic-Refiner pattern, where one AI agent produces an output and another critiques it, is a common technique in both game AI and frameworks like CrewAI that model team collaboration [[25]](https://www.truefoundry.com/blog/multi-agent-architecture). This allows for a feedback loop that improves the quality and accuracy of the final result.

CrewAI finds its sweet spot in multi-agent handoff scenarios, such as a researcher-to-writer workflow, where clear role definitions accelerate development. The trade-off is that its opinionated constructs can be brittle. The auto-generated hierarchical manager, for example, is known to be unreliable, often failing to delegate tasks intelligently and instead running them sequentially [[16]](https://vadim.blog/crewai-unique-features). This reveals a gap between the framework’s organizational metaphor and its technical implementation, often requiring custom manager prompts for production use.

Another framework approaches the problem through the lens of type safety and compile-time contracts.

## Framework Deep Dive: PydanticAI

PydanticAI adopts a philosophy similar to FastAPI, where Pydantic models and type hints create compile-time contracts between your code and the LLM's behavior. This focus on type safety ensures that the data flowing through your agent system is always valid and structured.![Diagram illustrating PydanticAI's design philosophy.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/0454e524-5d87-4288-82d4-3abd2b78a6f2/image/w=1920,quality=90,fit=scale-down)
Image 14: Diagram illustrating PydanticAI's design philosophy.

It comes with strong production features, most notably **durable execution integrations** with systems like Temporal, DBOS, and Prefect. This allows agents to survive restarts, pause for human input, and resume long-running tasks. It also has built-in **graph support** for creating non-linear workflows. The developer experience is enhanced by automatic schema generation from type hints and docstrings, along with structured output that includes automatic retries on validation failure.

The main trade-off is the upfront investment in defining schemas. While this provides correctness guarantees, it can present a learning curve for teams new to strict typing. PydanticAI is best suited for projects where structured data correctness and resumable tasks are paramount, which aligns well with the auditability needs of our writing agent.

We now look at a layered system explicitly separating experimentation from production hardening.

## Framework Deep Dive: AutoGen

AutoGen from Microsoft is designed with a layered architecture that deliberately separates experimentation from production. This allows for a smooth transition from rapid prototyping to building hardened, scalable agent systems.![Visualizing a multi-agent workflow in AutoGen Studio](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down)
Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.

The framework consists of three main layers:
-   **AutoGen Studio** is a low-code GUI that lets you prototype agent teams and workflows without writing code. You can visually compose agents, configure their tools, and test their interactions.
-   **AgentChat** is a programming framework for building conversational multi-agent applications.
-   **Core** provides low-level, event-driven primitives for building scalable, custom agent systems.

The typical workflow involves exploring and validating ideas visually inside Studio, then hardening the successful patterns into code using the lower layers. It is important to note the explicit disclaimer that Studio is a research prototype and not intended for production use [[8]](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html).

AutoGen's strength lies in its use as an R&D laboratory for discovering effective multi-agent conversation patterns and termination conditions. The trade-off is that this flexibility during exploration requires the team to re-implement reliability, security, and observability when moving to production.

A newer entrant focuses on tight model-family integration.

## Framework Deep Dive: Claude Agent SDK

The Claude Agent SDK from Anthropic is built on a philosophy of tight integration with its family of models. It is designed to use the specific strengths of Claude models, such as their large context windows, strong reasoning capabilities, and fine-grained control over tool use.

The framework provides ergonomic tool calling and orchestration tailored to the Anthropic model family. As a newer entrant to the agent framework landscape, it comes with certain trade-offs. The community is smaller, there are fewer third-party integrations, and the API surface is still evolving.

This presents both an opportunity and a risk. Early adoption can yield performance benefits optimized for Claude models, but teams must weigh this against the maturity of the ecosystem. The clearest use case for the Claude Agent SDK is for teams already committed to the Anthropic stack who want native performance and are willing to accept smaller community support.

The final deep dive examines a non-runtime layer that complements every option above.

## Framework Deep Dive: FastMCP

FastMCP is not a runtime; it is a tooling layer that lets you build MCP-compliant servers and clients. This makes your tools, resources, and prompts portable across any runtime or IDE that speaks the MCP protocol.![FastMCP Architecture and Interoperability](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/745828fd-27e2-4a50-b613-7275a1e1dceb/image/w=1920,quality=90,fit=scale-down)
Image 16: FastMCP Architecture and Interoperability

The primary benefit is interoperability. You can write a tool once and reuse it inside LangGraph, the OpenAI SDK, or any other compatible system. MCP complements agent frameworks by standardizing the "hands" of an AI system—how it interacts with the world—while the framework provides the "brain" or high-level orchestration [[17]](https://www.backslash.security/blog/what-is-mcp-model-context-protocol). FastMCP also provides production extensions like authentication and server composition.

Our capstone projects use this pattern. The research agent, Nova, is implemented as a FastMCP server that any client can steer. The writing agent, Brown, exposes its complex workflows as coarse-grained MCP tools. The developer experience is simple and Pythonic; you can expose a function as a tool with a single decorator, and FastMCP handles the schema generation and transport details automatically [[9]](https://gofastmcp.com/getting-started/quickstart).

```python
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
```

<aside>
💡 **Pattern: tools-as-workflows (Brown)**
For our writing agent (Brown), we wrap each workflow entry point as a **coarse-grained MCP tool** (e.g., `generate_article`, `edit_article`, `edit_selected_text`). The MCP tool handler simply **kicks off the corresponding LangGraph run** , returns progress/messages, and finally yields artifacts and diffs. This gives you MCP portability (Cursor, Claude Code) **without** losing LangGraph’s durability and auditability.
You’ll learn more about this in the later lessons.
</aside>

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

This matrix is a snapshot in time. The ecosystem is evolving, so you should always re-evaluate frameworks against the four decision axes when major updates are released.

Another way to frame the choice is by the mental model each framework encourages: CrewAI is for "building a team," LangGraph for "building a graph," and AutoGen for "building a conversation." Choosing the framework that best maps to how you conceptualize the problem can be more effective than comparing feature lists [[16]](https://vadim.blog/crewai-unique-features).

Based on these axes, we can offer some forecasts. LangGraph and PydanticAI are strong for reliability-heavy workflows, and the OpenAI SDK for lightweight simplicity. AgentKit is ideal when visual design and evaluation loops are needed. CrewAI excels at rapid multi-agent prototyping, AutoGen is a powerful R&D starting point, and FastMCP is the universal tooling substrate.

In practice, hybrid patterns are common. You might consume FastMCP tools inside LangGraph workflows, migrate from AutoGen Studio prototypes to more hardened runtimes, or expose complex graphs as single MCP commands to gain IDE portability without sacrificing durability.

To make this theory concrete, we will now share the actual pivots we made while building our course capstones.

## Our Capstone Pivots

Let’s apply this matrix to our capstone project. Our decision-making process evolved as we built, highlighting the importance of choosing the right tool for the job.

We initially planned to use LangGraph for both agents. However, we quickly found that the research agent, Nova, required high interactivity and divergent exploration, which made a rigid graph structure cumbersome. In this case, flexible MCP tools proved to be a better fit. The writing agent, Brown, had the opposite requirement. Its process needed to be repeatable and auditable, which made LangGraph’s checkpoints, HITL interrupts, and time-travel replay capabilities essential.

This led to our final hybrid architecture. Nova is implemented as a FastMCP server that any client can steer, including IDEs. Brown is a LangGraph workflow whose entry points are exposed as coarse-grained MCP tools. This pattern of wrapping complex internal workflows behind single MCP commands allows us to gain portability without sacrificing durability or auditability.

We considered the OpenAI Agents SDK, but it was ultimately deprioritized because it lacked the first-class persistence and deep MCP integration required for the long-running nature of both capstone tasks. For example, Brown exposes three main tools: `generate_article`, `edit_article`, and `edit_selected_text`. Each of these can be long-running and require a durable, resumable execution environment.

These real pivots illustrate the central lesson of this entire module.

## Conclusion

The core takeaway from this lesson is to prioritize stable concepts over transient brand names. Stateful graphs, typed contracts, durable execution, and MCP standardization are principles that will outlast any single framework. The MCP specification, in particular, is a high-leverage investment. Understanding it once gives you tool portability across every current and future stack. As an open standard, its ecosystem continues to evolve, with active research into areas like streaming extensions for real-time workflows and enhanced security frameworks [[18]](https://www.databricks.com/blog/what-is-model-context-protocol).

A practical selection process for your own projects should start with applying the four decision axes to your requirements. Begin with the smallest viable stack that meets your reliability needs, and keep your tooling portable by using MCP. A common migration path is to start exploration in a tool like AutoGen Studio, extract successful patterns into FastMCP tools, and then anchor your production system in a reliability-focused framework like LangGraph or PydanticAI. This approach allows you to move from a flexible, experimental environment to a hardened, production-ready system without rewriting your core tool logic.

Looking ahead, the next lesson will provide a system design framework covering model selection, cost and latency trade-offs, and the strategic placement of human-in-the-loop gates. Following that, we will dive into the hands-on implementation of our capstone projects. You will see the hybrid FastMCP-plus-LangGraph stack in action as we build Nova with FastMCP to handle its research loops and Brown with LangGraph to manage its auditable writing and editing cycles. This will provide a concrete demonstration of how the principles discussed in this lesson translate into real-world engineering decisions.

## References

- [1] Persistence (n.d.). LangChain. https://docs.langchain.com/oss/python/langgraph/persistence
- [2] Durable Execution (n.d.). Pydantic. https://ai.pydantic.dev/durable_execution/overview/
- [3] FastMCP (n.d.). FastMCP. https://gofastmcp.com/
- [4] Workflows and agents (n.d.). LangChain. https://docs.langchain.com/oss/python/langgraph/workflows-agents
- [5] OpenAI Agents SDK (n.d.). OpenAI. https://openai.github.io/openai-agents-python/
- [6] Introduction (n.d.). CrewAI. https://docs.crewai.com/introduction
- [7] AutoGen (n.d.). Microsoft. https://microsoft.github.io/autogen/stable/
- [8] AutoGen Studio User Guide (n.d.). Microsoft. https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html
- [9] Quickstart (n.d.). FastMCP. https://gofastmcp.com/getting-started/quickstart
- [10] Build your first Flow (n.d.). CrewAI. https://docs.crewai.com/guides/flows/first-flow
- [11] The Convergence of Large Language Models and Classical AI (2026). Arxiv. https://arxiv.org/html/2602.10479v1
- [12] Mozi: A Modular Agent for Drug Discovery (2026). Arxiv. https://arxiv.org/html/2603.03655v1
- [13] Reproducibility of large language models in medicine (n.d.). National Center for Biotechnology Information. https://pmc.ncbi.nlm.nih.gov/articles/PMC13079118
- [14] Hidden Technical Debt in the Agent Runtime (2026). https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime
- [15] LangGraph in Production: Latency, Replay, and Scale (n.d.). Aerospike. https://aerospike.com/blog/langgraph-production-latency-replay-scale
- [16] CrewAI's Genuinely Unique Features (n.d.). https://vadim.blog/crewai-unique-features
- [17] What is MCP (Model Context Protocol)? (n.d.). Backslash Security. https://www.backslash.security/blog/what-is-mcp-model-context-protocol
- [18] What is the Model Context Protocol? (n.d.). Databricks. https://www.databricks.com/blog/what-is-model-context-protocol
- [19] LangChain vs. LangGraph: A Detailed Comparison (n.d.). Milvus. https://milvus.io/blog/langchain-vs-langgraph.md
- [20] AI Agent Frameworks (n.d.). LangChain. https://www.langchain.com/resources/ai-agent-frameworks
- [21] Introducing AgentKit (2025). OpenAI. https://openai.com/index/introducing-agentkit
- [22] Build AI Agents With Pydantic (n.d.). Real Python. https://realpython.com/pydantic-ai
- [23] Microsoft AutoGen: Orchestrating Multi-Agent LLM Systems (n.d.). Tribe AI. https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems
- [24] Agent SDK vs. Framework: Claude, Pydantic AI, and the Future of AI Development (n.d.). MindStudio. https://www.mindstudio.ai/blog/agent-sdk-vs-framework-claude-pydantic-ai
- [25] Multi-Agent Architecture: A Deep Dive (n.d.). TrueFoundry. https://www.truefoundry.com/blog/multi-agent-architecture