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