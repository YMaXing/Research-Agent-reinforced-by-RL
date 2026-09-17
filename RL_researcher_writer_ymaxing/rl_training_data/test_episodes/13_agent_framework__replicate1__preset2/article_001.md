# Lesson 13: Choosing Your AI Agent Framework

In our last lesson, we introduced the scope and design of our central project: a system of two specialized agents, Nova and Brown. Nova is an adaptable research agent designed for interactive exploration, while Brown is a reliable writing agent focused on auditable content generation. This lesson provides the scaffolding for building them by tackling one of the most critical decisions in AI engineering: choosing the right framework.

The choice of an agent framework is not just a technical detail; it defines the production viability of your entire system. A poor selection can lead to brittle abstractions that break under real-world load, stalled progress in a rapidly changing ecosystem, or hidden gaps in durability that only appear after weeks of investment.

Throughout this lesson, we will use our capstone projects as a concrete anchor. We will explore two core concepts that are central to their design: LangGraph's interrupts and checkpoints, which provide the resumable auditability needed for our writing agent, and the Model Context Protocol (MCP), a universal interoperability layer that keeps our research agent's tools portable. This leads to a high-level architecture where our research agent is a lightweight MCP server that any client can steer, while our writing agent is a durable workflow that exposes its capabilities as coarse-grained MCP tools.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down
Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions.

This lesson focuses on the philosophies, core abstractions, and production trade-offs of leading frameworks, not just API syntax. With our capstone projects as a concrete reference, we can now examine why framework selection so often fails in production and what layers, runtime, protocol, and tooling, actually solve which problems.

## Framework Choice Under Uncertainty

The AI agent ecosystem is new and evolving quickly. No single framework will satisfy every use case. To make an informed choice, you must distinguish between three layers that are often conflated: runtime, protocol, and tooling. Each layer solves a distinct set of production problems.

The **runtime** is the orchestration and state management layer, encompassing frameworks like LangGraph, CrewAI, and the OpenAI Agents SDK. It is the machinery that keeps an agent running, recoverable, and isolated. This layer handles durable execution across crashes, manages short-term and long-term memory, and provides process isolation to prevent one agent from affecting another. It is everything underneath the agent's reasoning loop that ensures it can run reliably in a shared production environment.

The **protocol** layer provides standardization and portability. The Model Context Protocol (MCP) is the key example here. It defines a standard way for agents and tools to communicate, much like a universal adapter. This prevents vendor lock-in by decoupling your tools from any specific runtime, allowing them to be reused across different frameworks and even IDEs.

Finally, the **tooling** layer offers implementation details and server scaffolding. FastMCP, for instance, provides ready-to-deploy transports, authentication, and a better developer experience for building MCP-compliant tools. It handles the boilerplate, letting you focus on the logic of your tools.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down
Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework.

When engineers select frameworks based on hype or simple demos, they risk common failure modes. Choosing a framework that is too simple means you will lack the reliability primitives needed for production workloads. Conversely, choosing one that is overly complex introduces unneeded overhead for exploratory work. The initial distinction between interactive and deterministic workloads is a good starting point for assessing which framework fits your needs.

We learned this firsthand. We initially planned to build our research agent with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was a wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

## A Theory for Choosing: Decision Axes Instead of Brands

To avoid these traps, you need a way to evaluate frameworks based on principles, not just brand names. We use four decision axes to analyze any library and determine if it fits a project’s needs.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down
Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks.

### Control-Flow Explicitness vs. LLM-Driven Autonomy

This axis balances deterministic control against LLM-driven autonomy. Graph-based systems like LangGraph offer explicit, auditable state transitions, ideal for repeatable processes. In contrast, lightweight loops like the OpenAI Agents SDK favor adaptability for exploratory tasks where the path is unknown.

This trade-off reflects a classic design choice between *Symbolic* systems, which externalize logic into deterministic state machines for verifiability, and *Neural* systems, which use the LLM's generative capabilities for planning, gaining adaptability at the cost of predictability [[9]](https://arxiv.org/html/2602.10479v1). The question is: does your application require auditable steps or must it navigate unpredictability?

### Reliability Primitives

Production systems fail, so frameworks must provide tools to handle failures gracefully. Lessons from safety-critical embedded systems apply here: production agent runtimes require strong isolation, reproducibility, and bounded failure modes to be trustworthy [[10]](https://uxmag.com/articles/ai-agent-runtimes-in-dedicated-lanes-lessons-from-chinas-ev-roads), [[11]](https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime). Look for checkpointing, time-travel replay, HITL interrupts, and durable execution across restarts. LangGraph emphasizes interrupts and persistence [[1]](https://docs.langchain.com/oss/python/langgraph/persistence), while PydanticAI integrates with systems like Temporal for durability [[2]](https://ai.pydantic.dev/durable_execution/overview/). These are non-negotiable for our writing agent but less critical for the research agent.

### Abstraction Level and Developer Experience

Frameworks exist on a spectrum of abstraction. Some, like the OpenAI Agents SDK, provide minimal primitives, requiring more boilerplate but offering greater flexibility. Others, like CrewAI, offer opinionated constructs that accelerate initial development but can reduce adaptability when dealing with edge cases. The right choice depends on whether you prefer to build from low-level components or assemble pre-built modules.

### Tooling Interoperability

In a rapidly changing ecosystem, tool portability is key. MCP functions as the USB-C of AI, providing a standard interface for tools. It enables dynamic discovery, allowing an agent to find and use new tools at runtime without being redeployed, which future-proofs the architecture against changing services [[12]](https://www.scalekit.com/blog/mcp-vs-apis-how-are-they-different). This lets you write tools once as MCP servers, for example, with FastMCP [[3]](https://gofastmcp.com/), and reuse them across any runtime that speaks the protocol, including LangGraph or the OpenAI Agents SDK. This prevents tool lock-in and ensures your work remains valuable even if you switch runtimes.

Our capstone projects map clearly to these axes. The research agent requires autonomy and interoperable tools for its exploratory nature, making a lightweight loop with MCP a good fit. The writing agent demands an explicit, auditable workflow with strong reliability primitives, making LangGraph the better choice.

## The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks.

### LangGraph

LangGraph’s philosophy is built around a stateful graph model with native checkpoints and interrupts for auditable workflows [[1]](https://docs.langchain.com/oss/python/langgraph/persistence). This makes it ideal for processes that need to be resumable and traceable, as we covered in Lesson 5 on workflow ingredients [[4]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). Its graph-based architecture is well-suited for stateful applications, complex decision-making, and multi-agent coordination, providing a robust foundation for building reliable systems [[16]](https://milvus.io/blog/langchain-vs-langgraph.md). The framework has shown strong, consistent adoption, averaging around 400,000–500,000 downloads per day over the past three months.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down
Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025.

<aside>
💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers, etc.), **LangGraph** focuses specifically on **structured**, **stateful workflows**. It introduces graph-based execution with checkpoints and resumability, which are features not native to standard LangChain chains.

In short, LangChain is the toolbox, while LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions [[4]](https://docs.langchain.com/oss/python/langgraph/workflows-agents). You will see LangChain code in the writing agent.
</aside>

### OpenAI Agents SDK

The OpenAI Agents SDK favors a minimal surface area consisting of agents, tools, guardrails, handoffs, and sessions [[5]](https://openai.github.io/openai-agents-python/). It uses lightweight, Python-native loops over compiled state machines, giving developers direct control over the orchestration logic. This approach is designed for quick learning and easy integration into existing Python applications. The library has recorded 90,000–120,000 daily downloads over the past three months, with a slight upward trend.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down
Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025.

### AgentKit

AgentKit is a modular toolkit for building, deploying, and optimizing agents across the OpenAI platform. It unifies a visual builder, connectors (including MCP), a ChatKit for embedding UIs, and evaluation infrastructure [[17]](https://openai.com/index/introducing-agentkit). Developers can visually compose multi-agent systems, manage connectors, and embed chat-based experiences directly in their products, all backed by versioning and guardrails. It provides a comprehensive environment for creating agents that can act autonomously [[18]](https://www.nudgesecurity.com/post/openai-agentkit-and-agent-builder-building-secure-ai-agents).

<aside>
💡 OpenAI AgentKit vs. OpenAI Agents SDK

The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration and fine-grained control. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK: it adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**. In short, the SDK is the coding foundation, while AgentKit is the integrated platform for design, deployment, and optimization.
</aside>

### CrewAI

CrewAI features a dual architecture: role-based autonomous crews for collaborative exploration versus event-driven flows for deterministic control [[19]](https://docs.crewai.com/introduction). Its core mental model is "build a team of people," contrasting with LangGraph's "build a graph" or AutoGen's "build a conversation" [[13]](https://vadim.blog/crewai-unique-features). This separation of deterministic orchestration from autonomous reasoning is a key architectural insight [[13]](https://vadim.blog/crewai-unique-features). It also offers a strong developer experience with CLI scaffolding and YAML definitions. Daily downloads for the library range between 40,000 and 100,000.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down
Image 6: Source: pepy.tech, daily downloads for Crewai, accessed October 15, 2025.

### PydanticAI

PydanticAI emphasizes type safety, schema-driven validation, and durable execution through integrations with systems like Temporal and DBOS [[2]](https://ai.pydantic.dev/durable_execution/overview/). By leveraging Pydantic models, it ensures that LLM outputs conform to a predefined schema, providing a reliable bridge between the probabilistic nature of LLMs and the deterministic requirements of application code [[20]](https://realpython.com/pydantic-ai). Daily downloads doubled from ~150,000 in July to 300,000–450,000 by October 2025, demonstrating strong growth.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down
Image 7: Source: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025.

### AutoGen

AutoGen takes a layered approach, with its Studio GUI positioned for exploration and not production [[7]](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html). This allows ideas to be hardened into its AgentChat or core libraries. The framework is designed for building multi-agent conversational systems with customizable behaviors, making it a flexible playground for research and prototyping [[21]](https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems).

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down
Image 8: Source: pepy.tech, daily downloads for autogen, accessed October 15, 2025.

### Claude Agent SDK

A newer entrant from Anthropic, this SDK offers tight integration with the Claude model family, leveraging its strengths in large context and low-level tool use. It is designed to solve the architectural problem of maintaining control over agent logic while Anthropic manages the runtime, with native support for tools as first-class citizens [[22]](https://buildwithaws.substack.com/p/inside-the-claude-agent-sdk-from).

### FastMCP

FastMCP is a tooling layer, not a runtime. It lets you build MCP-compliant servers and clients once, so your tools become portable across any runtime or IDE [[3]](https://gofastmcp.com/). It has shown explosive growth, with daily downloads surging from ~250,000 in July to over 1.2 million per day in October 2025.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down
Image 9: Source: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025.

Adoption metrics like download trends and GitHub stars can serve as a proxy for a framework's maturity, ecosystem health, and long-term maintenance burden.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down
Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026.

It is important to avoid single-framework dogma. Hybrid patterns are common in practice, such as consuming FastMCP tools inside a LangGraph workflow or migrating from AutoGen prototypes to hardened runtimes. We will now deep-dive into each framework, starting with LangGraph, using our four axes and capstone needs as constant evaluation lenses.

## Framework Deep Dive: LangGraph

LangGraph uses a graph-based modeling approach where nodes are Python functions and edges are explicit transitions. This makes complex, multi-step logic transparent and auditable. Its core production primitives include interrupts for human-in-the-loop interaction, persistence and checkpointing for resumability, and time-travel debugging that lets you replay and branch from any prior state [[1]](https://docs.langchain.com/oss/python/langgraph/persistence). To manage storage growth in long-running workflows, LangGraph offers optimizations like `DeltaChannel`, which stores only incremental state changes instead of full snapshots at every step. It also provides different persistence modes, such as writing checkpoints asynchronously to balance performance and durability against process crashes [[1]](https://docs.langchain.com/oss/python/langgraph/persistence).

The framework offers two definition styles: a "graph API" for fully explicit graphs and a "functional API" that is decorator-based. This presents a trade-off between a steeper learning curve and the payoff of full determinism. The functional API allows developers to define workflows using standard Python functions with decorators, making it easier to integrate LangGraph's features into existing applications without a complete code restructure [[23]](https://www.langchain.com/blog/introducing-the-langgraph-functional-api).

While LangGraph provides built-in safety, observability, and durability, it can be overkill for simple exploratory scripts, which might benefit from lighter loops. However, for repeatable and auditable processes like our writing agent, the upfront modeling investment is justified. This contrasts with lighter, more autonomous loops, which are easier to start with but can lead to brittle production failures without these built-in safety nets.

Having examined a graph-centric, reliability-first option, we now turn to a deliberately minimal alternative.

## Framework Deep Dive: OpenAI Agents SDK

The OpenAI Agents SDK is built on a philosophy of minimal primitives, which deliberately reduces the conceptual surface area while still enabling powerful agentic applications [[5]](https://openai.github.io/openai-agents-python/).

Its core concepts are:
-   **Agents**: LLMs equipped with instructions and tools, forming the core building block of your application.
-   **Tools**: Python functions that agents can call to interact with the outside world, with automatic schema generation.
-   **Guardrails**: Mechanisms for validating agent inputs and outputs to ensure safety and correctness, running in parallel with execution.
-   **Handoffs**: A way for agents to delegate tasks to other, more specialized agents, enabling modular and focused designs.
-   **Sessions**: A persistence layer that automatically manages conversation history and tool results across multiple runs.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down
Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships.

The fundamental difference between the OpenAI Agents SDK and LangGraph’s functional API lies in the execution model. The OpenAI SDK uses a simple, Python-native agent loop that you control directly. Orchestration is handled with standard Python code, such as `if/else` statements and `for` loops.

In contrast, even with its decorator-based functional API, LangGraph compiles your code into an explicit, stateful graph. This underlying state machine manages execution, persistence, and interruptions, providing a more robust but also more constrained environment.

The SDK is a strong choice for teams that want a fast production path where lightweight orchestration and sensible defaults are preferred. However, it comes with a reliability trade-off: durable pause, resume, and checkpointing features are not provided out of the box and must be implemented by the team. The natural extension of this minimal SDK is a full-lifecycle platform built on top of it.

## Framework Deep Dive: AgentKit

AgentKit is a complete lifecycle toolkit layered on the OpenAI Agents SDK, covering design, deployment, optimization, and continuous improvement. It extends the SDK by adding visual workflow design, UI embedding, and evaluation infrastructure.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down
Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents.

Its key components include:
-   **Agent Builder**: A drag-and-drop canvas for designing and versioning multi-agent workflows. It supports preview runs, inline evaluation, and full versioning, making it ideal for rapid iteration [[17]](https://openai.com/index/introducing-agentkit).
-   **Connector Registry**: A centralized interface for managing data connections like Dropbox, Google Drive, and third-party MCPs across workspaces [[17]](https://openai.com/index/introducing-agentkit).
-   **ChatKit**: A toolkit for embedding agentic chat UIs directly into web or mobile products, handling streaming responses and custom theming [[17]](https://openai.com/index/introducing-agentkit).
-   **Evals and Reinforcement Fine-Tuning (RFT)**: Expanded capabilities for measuring, grading, and improving agent performance, including datasets and automated prompt optimization [[17]](https://openai.com/index/introducing-agentkit).

AgentKit sits one layer above the OpenAI Agents SDK. You still use the SDK for code-first orchestration, but AgentKit provides the surrounding tools for design, deployment, and continuous improvement. This visual composition and built-in evaluation support safe multi-agent systems at scale without forcing everything into code.

The main trade-off is its optimization for the OpenAI ecosystem, although growing MCP connector support improves broader interoperability. AgentKit adds clear value over the raw SDK for teams that need no-code workflow design, versioning, and continuous improvement loops. We now examine a framework whose duality spans both autonomous crews and structured flows.

## Framework Deep Dive: CrewAI

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcc81dc-f35c-4a6b-95e8-557db10090a9/e0cb631a-91ae-46fc-a332-d5e1afd61c80/w=1920,quality=90,fit=scale-down
Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`.

CrewAI introduces a powerful duality with its two main concepts: **Crews** and **Flows**.
-   **Crews** are for role-based, autonomous collaboration. You define agents with specific roles, goals, and tools, and they work together to solve a problem, much like a human team.
-   **Flows** are for event-driven, deterministic orchestration. They give you fine-grained control over the workflow, allowing you to define precise execution paths.

This dual architecture lets you start with an autonomous crew for rapid prototyping, then introduce a flow to add structure and control as your requirements become more defined. It also features a `hierarchical` process mode that auto-generates a manager agent to coordinate the team. However, this feature is known to be unreliable in practice; the manager often executes tasks sequentially instead of delegating intelligently, making it more of a demo feature than a production-ready one [[13]](https://vadim.blog/crewai-unique-features).

The framework has a strong focus on developer experience, with CLI scaffolding, YAML definitions for agents and tasks, and configurable memory and persistence options. Its sweet spot is in multi-agent handoff scenarios, such as researcher-to-writer flows, where role clarity accelerates development. However, its opinionated constructs, while enabling rapid initial velocity, can lead to configuration overhead and reduced flexibility when edge cases appear.

Next, another framework approaches the problem through the lens of type safety and compile-time contracts.

## Framework Deep Dive: PydanticAI

PydanticAI’s philosophy is similar to FastAPI, where Pydantic models and type hints create compile-time contracts between your code and the LLM's behavior.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/0454e524-5d87-4288-82d4-3abd2b78a6f2/image/w=1920,quality=90,fit=scale-down
Image 14: Diagram illustrating PydanticAI's design philosophy.

It offers strong production features, including **durable execution integrations** with systems like Temporal, DBOS, or Prefect, which allow agents to survive restarts and handle long-running tasks [[2]](https://ai.pydantic.dev/durable_execution/overview/). It also has built-in **graph support** for non-linear flows. The developer experience is enhanced by automatic schema generation from type hints and structured output with automatic retries on validation failure.

The main trade-off is the up-front investment in defining schemas, which is a strength for ensuring correctness but can be a learning curve for teams new to strict typing. PydanticAI is best suited for projects where structured data correctness and long-running resumable tasks are essential, aligning well with our writing agent’s auditability needs.

We now look at a layered system that explicitly separates experimentation from production hardening.

## Framework Deep Dive: AutoGen

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down
Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team.

AutoGen features a layered design that deliberately separates experimentation from production [[6]](https://microsoft.github.io/autogen/stable/).
-   **AutoGen Studio** is a low-code GUI that lets you prototype agent teams and workflows without writing code. It provides a visual interface for creating agent teams and an interactive playground for testing them [[7]](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html).
-   **AgentChat** is a programming framework for building conversational multi-agent applications. It builds on the core layer to provide a task-driven API for common patterns like group chat and code execution [[24]](https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness).
-   **Core** provides low-level, event-driven primitives for building scalable, custom agent systems, handling foundational capabilities like message passing between agents [[21]](https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems).

The typical workflow involves exploring and validating ideas visually inside Studio, then hardening the successful patterns into code using the lower-level libraries. However, it is important to note the explicit disclaimer that Studio is a research prototype and not meant for production environments [[7]](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html).

AutoGen's strength lies in its use as an R&D laboratory for discovering multi-agent conversation patterns and effective termination conditions. The trade-off is that this flexibility during exploration requires the team to re-implement reliability, security, and observability when moving to production. A newer entrant focuses on tight model-family integration.

## Framework Deep Dive: Claude Agent SDK

The Claude Agent SDK is built on a philosophy of tight integration with the Claude model family, leveraging its strengths in large context windows, strong reasoning, and fine-grained control over tool use. It provides ergonomic tool calling and orchestration tailored specifically to Anthropic models. A core feature is its native support for permissions and hooks, such as the `canUseTool` callback and declarative allow/deny rules, which distinguish it from more general-purpose frameworks [[22]](https://buildwithaws.substack.com/p/inside-the-claude-agent-sdk-from).

As a newer entrant, its trade-offs include a smaller community, fewer third-party integrations, and a rapidly evolving API surface. This presents both an opportunity and a risk: early adoption can yield model-optimized performance, but teams must balance this against the maturity of the ecosystem. The clearest use case is for teams already committed to the Anthropic stack who want native performance and are willing to accept smaller community support.

The final deep dive examines a non-runtime layer that complements every option above.

## Framework Deep Dive: FastMCP

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/745828fd-27e2-4a50-b613-7275a1e1dceb/image/w=1920,quality=90,fit=scale-down
Image 16: FastMCP Architecture and Interoperability

FastMCP is not a runtime; it is a tooling layer that lets you build MCP-compliant servers and clients [[3]](https://gofastmcp.com/). This makes your tools, resources, and prompts portable across any runtime or IDE that speaks the protocol. MCP represents a strategic shift, enabling agents to dynamically discover and use tools at runtime. This allows an AI system to adapt to new capabilities without needing to be hardcoded for every API, making the architecture more future-proof [[12]](https://www.scalekit.com/blog/mcp-vs-apis-how-are-they-different). The key benefit is interoperability: you can write a tool once and reuse it inside LangGraph, the OpenAI SDK, or any future compatible system.

FastMCP also provides production extensions beyond the protocol itself, including authentication, server composition, and cloud deployment features. In our capstone project, the research agent is implemented as a FastMCP server that any client can steer, while the writing agent exposes its complex workflows as coarse-grained MCP tools.

<aside>
💡 Pattern: tools-as-workflows (Brown)

For our writing agent (Brown), we wrap each workflow entry point as a **coarse-grained MCP tool** (e.g., `generate_article`, `edit_article`, `edit_selected_text`). The MCP tool handler simply **kicks off the corresponding LangGraph run**, returns progress/messages, and finally yields artifacts and diffs. This gives you MCP portability (Cursor, Claude Code) **without** losing LangGraph’s durability and auditability. You’ll learn more about this in the later lessons.
</aside>

The developer experience of FastMCP is designed to be simple and Pythonic. You can expose a function as a tool with a single decorator, and FastMCP handles the schema generation and transport details automatically [[8]](https://gofastmcp.com/getting-started/quickstart).

```python
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

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

It is important to treat this matrix as a snapshot. The AI agent ecosystem is constantly evolving, so you should re-evaluate frameworks against the four decision axes whenever libraries release major updates.

Based on the current landscape, we can offer some tentative forecasts. LangGraph and PydanticAI are strong choices for reliability-heavy workflows that require explicit state management and durability. The OpenAI SDK offers lightweight simplicity for teams prioritizing speed and minimal abstractions, while AgentKit is the right choice when visual design and continuous evaluation loops are required.

CrewAI is well-suited for rapid multi-agent prototyping where role-based collaboration is a natural fit. FastMCP stands out as the universal tooling substrate, ensuring tool portability across any stack. AutoGen remains a strong starting point for R&D and exploring complex conversational patterns. In practice, hybrid patterns are common, such as consuming FastMCP tools inside LangGraph workflows or migrating from AutoGen prototypes to hardened runtimes.

To make the theory concrete, we now share the actual pivots we made while building the course capstones.

## Our Capstone Pivots

Let’s apply this matrix to our capstone project. Our decision-making process evolved as we built, highlighting the importance of choosing the right tool for the job.

Our initial plan was to use LangGraph for both agents. However, we soon realized that the research agent’s need for high interactivity and divergent exploration made rigid graphs cumbersome. For Nova, flexible MCP tools proved superior. In contrast, the writing agent, Brown, required a repeatable, auditable process, which made LangGraph’s checkpoints, HITL interrupts, and time-travel replay capabilities the ideal choice.

This led to a hybrid outcome: Nova is implemented as a FastMCP server that any client, including IDEs, can steer. Brown is implemented as a LangGraph workflow whose entry points are deliberately exposed as coarse MCP tools. This pattern of wrapping complex internal workflows behind single MCP commands allows us to gain portability without sacrificing durability or auditability.

We considered the OpenAI Agents SDK but ultimately deprioritized it because it lacked the first-class persistence and deep MCP integration required for the long-running nature of both capstone tasks. For Brown, we currently expose three tools: `generate_article`, `edit_article`, and `edit_selected_text`. These real pivots illustrate the central lesson of this entire module.

## Conclusion

The core takeaway from this lesson is to prioritize stable concepts over transient brand names. Focus on stateful graphs, typed contracts, durable execution, and MCP standardization. These principles provide a durable mental model for evaluating any framework, new or old. The MCP specification itself is a high-leverage investment; understanding it once gives you tool portability across every current and future stack. Open research directions for the protocol include developing streaming extensions for real-time data, enhancing security for multi-tenant deployments, and creating standardized libraries for more programming languages [[14]](https://www.databricks.com/blog/what-is-model-context-protocol), [[15]](https://project-rachel.4open.science/Rachel.So.MCP.Servers.for.Scientific.Workflows.pdf).

A practical selection process should start by applying the four decision axes to your project. Begin with the smallest viable stack that meets your reliability needs, and keep all your tooling portable via MCP. A common migration path might start with exploration in AutoGen Studio, followed by extracting successful patterns into FastMCP tools, and finally anchoring the production system in a robust runtime like LangGraph or PydanticAI. This layered approach allows you to move from idea to production with confidence, choosing the right level of abstraction and control at each stage.

In our next lesson, we will cover system design, including model selection, cost and latency trade-offs, and HITL placement. After that, we will move on to the hands-on capstone builds, where we will use the hybrid FastMCP-plus-LangGraph stack we have chosen through this exact process.

We will build Nova with FastMCP to handle research and ingestion, and Brown with LangGraph and MCP tools to create a durable and auditable writing workflow. This will provide a concrete demonstration of how to apply these principles to build production-ready agentic systems.

## References

- [1] Persistence. (n.d.). LangChain. https://docs.langchain.com/oss/python/langgraph/persistence
- [2] Durable Execution. (n.d.). Pydantic. https://ai.pydantic.dev/durable_execution/overview/
- [3] FastMCP. (n.d.). FastMCP. https://gofastmcp.com/
- [4] Workflows and agents. (n.d.). LangChain. https://docs.langchain.com/oss/python/langgraph/workflows-agents
- [5] OpenAI Agents SDK. (n.d.). OpenAI. https://openai.github.io/openai-agents-python/
- [6] AutoGen. (n.d.). Microsoft. https://microsoft.github.io/autogen/stable/
- [7] AutoGen Studio User Guide. (n.d.). Microsoft. https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html
- [8] Quickstart. (n.d.). FastMCP. https://gofastmcp.com/getting-started/quickstart
- [9] The Evolution of Agentic AI Architectures. (2026). arXiv. https://arxiv.org/html/2602.10479v1
- [10] AI Agent Runtimes in Dedicated Lanes: Lessons from China’s EV Roads. (n.d.). UX Magazine. https://uxmag.com/articles/ai-agent-runtimes-in-dedicated-lanes-lessons-from-chinas-ev-roads
- [11] The Hidden Technical Debt in your AI Agent's Runtime. (2026). leehanchung.github.io. https://leehanchung.github.io/blogs/2026/04/24/hidden-technical-debt-agent-runtime
- [12] MCP vs. APIs: How Are They Different? (n.d.). ScaleKit. https://www.scalekit.com/blog/mcp-vs-apis-how-are-they-different
- [13] CrewAI's Genuinely Unique Features: An Honest Technical Deep-Dive. (n.d.). vadim.blog. https://vadim.blog/crewai-unique-features
- [14] What is the Model Context Protocol (MCP)? (n.d.). Databricks. https://www.databricks.com/blog/what-is-model-context-protocol
- [15] MCP Servers for Scientific Workflows. (n.d.). 4open.science. https://project-rachel.4open.science/Rachel.So.MCP.Servers.for.Scientific.Workflows.pdf
- [16] LangChain vs. LangGraph: Choosing the Right Framework for Your LLM Application. (n.d.). Milvus. https://milvus.io/blog/langchain-vs-langgraph.md
- [17] Introducing AgentKit. (2025). OpenAI. https://openai.com/index/introducing-agentkit
- [18] OpenAI AgentKit and Agent Builder: Building Secure AI Agents. (n.d.). Nudge Security. https://www.nudgesecurity.com/post/openai-agentkit-and-agent-builder-building-secure-ai-agents
- [19] Introduction. (n.d.). CrewAI. https://docs.crewai.com/introduction
- [20] Build LLM Agents with Validated, Structured Outputs Using Pydantic AI. (n.d.). Real Python. https://realpython.com/pydantic-ai
- [21] Microsoft AutoGen: A Deep Dive into Orchestrating Multi-Agent LLM Systems. (n.d.). Tribe AI. https://www.tribe.ai/applied-ai/microsoft-autogen-orchestrating-multi-agent-llm-systems
- [22] Inside the Claude Agent SDK, from Anthropic. (n.d.). Build With AWS. https://buildwithaws.substack.com/p/inside-the-claude-agent-sdk-from
- [23] Introducing the LangGraph Functional API. (2025). LangChain Blog. https://www.langchain.com/blog/introducing-the-langgraph-functional-api
- [24] AutoGen v0.4: Reimagining the foundation of agentic AI for scale, extensibility, and robustness. (2024). Microsoft Research. https://www.microsoft.com/en-us/research/blog/autogen-v0-4-reimagining-the-foundation-of-agentic-ai-for-scale-extensibility-and-robustness