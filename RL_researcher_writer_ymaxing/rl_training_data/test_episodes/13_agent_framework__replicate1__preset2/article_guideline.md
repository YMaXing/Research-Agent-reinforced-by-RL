## Global Context of the Lesson

### What We Are Planning to Share

We will write a lesson that guides AI engineers in choosing agent frameworks under uncertainty by first distinguishing runtimes, the MCP protocol, and tooling layers. We will introduce four decision axes—control-flow explicitness versus autonomy, reliability primitives, abstraction and DX level, and tooling interoperability—to replace hype-driven or brand-based selection. We will survey the current landscape with adoption metrics, then deep-dive into the philosophies, core abstractions, strengths, and trade-offs of LangGraph, OpenAI Agents SDK, AgentKit, CrewAI, PydanticAI, AutoGen, Claude Agent SDK, and FastMCP. We will anchor every comparison in the concrete needs of the two capstone projects (the adaptable MCP-driven research agent and the auditable LangGraph-driven writing agent), supplying a decision matrix, hybrid patterns, and real pivots as illustration. Ultimately we connect framework selection to production viability and the broader AI engineering practice while highlighting MCP as a portability layer.

### Why We Think It's Valuable

Framework choice directly impacts production viability—poor selections create brittleness, missing durability features, vendor lock-in, or excessive overhead. This lesson equips you with principle-based axes instead of transient brands and highlights MCP as a portability layer, allowing tools to outlive specific runtimes in a fast-changing ecosystem. Mastering these concepts prevents stalled progress on complex projects such as the capstones and gives you a reusable mental model for evaluating any new framework that appears.

### Expected Length of the Lesson
**4,500 words**

### Theory / Practice Ratio

100% theory - 0% practice

## Anchoring the Lesson in the Course

### Details About the Course

This piece is part of a broader course on AI agents and LLM workflows. The course consists of 4 parts, each with multiple lessons. 

Thus, it's essential to always anchor this piece into the broader course, understanding where the reader is in its journey. You will be careful to consider the following:
- The points of view.
- To not reintroduce concepts already thought in the previous lesson.
- To be careful when talking about concepts introduced only in future lessons.
- To always reference previous and future lessons when discussing topics outside the piece's scope.

### Lesson Scope

This is lesson 13 of the Agentic AI Engineering course. It follows lesson 12’s introduction of the scope and design of the central project - a system of two specialized agents - and precedes lesson 14’s system-design framework for models, cost, latency, and HITL placement. It supplies the conceptual scaffolding used in lessons 15-26 when the capstones are built end-to-end.

### Point of View

The course is created by a team writing for a single reader, also known as the student. Thus, for voice consistency across the course, we will always use 'we,' 'our,' and 'us' to refer to the team who creates the course, and 'you' or 'your' to address the reader. Avoid singular first person and don't use 'we' to refer to the student.

Examples of correct point of view:
- Instead of "Before we can choose between workflows and agents, we need a clear understanding of what they are." word it as "To choose between workflows and agents, you need a clear understanding of what they are."

### Who Is the Intended Audience

AI engineers who have built basic LLM tool-calling loops and been introduced to the course capstones but need structured principles for evaluating production frameworks amid a crowded, evolving landscape.

### Concepts Introduced in Previous Lessons

In previous lessons of the course, we introduced the following concepts:

**Part 1:**

- **Lesson 1 - AI Engineering & Agent Landscape**: Understanding the role, the stack, and why agents matter now
- **Lesson 2 - Workflows vs. Agents**: Grasping the crucial difference between predefined logic and LLM-driven autonomy
- **Lesson 3 - Context Engineering**: The art of managing information flow to LLMs
- **Lesson 4 - Structured Outputs**: Ensuring reliable data extraction from LLM responses
- **Lesson 5 - Basic Workflow Ingredients**: Implementing chaining, routing, parallel and the orchestrator-worker patterns
- **Lesson 6 - Agent Tools & Function Calling**: Giving your LLM the ability to take action
- **Lesson 7 - Planning & Reasoning**: Understanding patterns like ReAct (Reason + Act)
- **Lesson 8 - Implementing ReAct**: Building a reasoning agent from scratch
- **Lesson 9 - Agent Memory & Knowledge**: Short-term vs. long-term memory (procedural, episodic, semantic)
- **Lesson 10 - RAG Deep Dive**: Advanced retrieval techniques for knowledge-augmented agents
- **Lesson 11 - Multimodal Data**: Foundations and Implementations of Multimodal LLMs

**Part 2:**

- **Lesson 12 - Central Project: Scope & Design**: Introducing the scope and design of the central project

As this is the second lesson in Part 2 - Building Agentic Systems, after we introduced the scope and design of the central project of our course, we will introduce agent frameworks, compare them and teach students how to evaluate across various dimensions to justify the design choices we made for our agents in last lesson.

### Concepts That Will Be Introduced in Future Lessons

In future lessons of the course, we will introduce the following concepts:
- System-design decision framework covering model selection, cost/latency trade-offs, and HITL gate placement
- End-to-end Nova implementation as FastMCP server with Perplexity loops and research artifacts
- End-to-end Brown implementation as LangGraph workflow exposing coarse MCP tools
- Tools-as-workflows pattern combining durability with IDE-native portability

If you must mention these, keep explanations high-level and intuitive and explicitly note that they will be covered in their respective future lessons.

### Anchoring the Reader in the Educational Journey

Within the course we are teaching the reader multiple topics and concepts. Thus, understanding where the reader is in its educational journey it's critical for this piece. You have to use only previous introduced concepts, while being reluctant about using concepts that haven't been introduced yet.

When discussing the **concepts introduced in previous lessons** listed in the `Concepts Introduced in Previous Lessons` section, avoid reintroducing them to the reader. Especially don't reintroduce the acronyms. Use them as if the reader already knows what they are. 

Avoid using all the **concepts that haven't been introduced in previous lessons** listed in the `Concepts That Will Be Introduced in Future Lessons` subsection. Whenever another concept requires references to these banned concepts, instead of directly using it, use other intuitive and grounded explanations as you would explain them to a 7-year-old. For example:
- If the "tools" concept wasn't introduced yet and you have to talk about agents, refer them to as "actions".
- If the "routing" concept wasn't introduced yet and you have to talk about it, refer it to as "guiding the workflow between multiple decisions".
You can use the concepts that haven't been introduced in previous lessons listed in the `Concepts That Will Be Introduced in Future Lessons` subsection, only if we explicitly specify them. Still, even in that case, as the reader doesn't know how that concept works, you are just allowed to use the term, while keeping the explanation extremely high-level and intuitive, as if you were explaining it to a 7-year-old.
Whenever you use a concept from the `Concepts That Will Be Introduced in Future Lessons` subsection explicitly specify that it will be explained in more detail in future lessons.

In all use cases avoid using acronyms that aren't explicitly stated in the guidelines. Rather use other more accessible synonyms or descriptions that are easier to understand by non-experts.

## Narrative Flow of the Lesson

Follow the next narrative flow when writing the end-to-end lesson:

- What problem are we solving? Why is it essential to solve it?
	- Start with a personal story where we encountered the problem
- Why other solutions are not working and what's wrong with them.
- At a theoretical level, explain our solution or transformation. Highlight:
    - The theoretical foundations.
    - Why is it better than other solutions?
    - What tools or algorithms can we use?
- Provide some hands-on examples.
- Go deeper into the advanced theory.
- Provide a more complex example supporting the advanced theory.
- Connect our solution to the bigger picture and next steps.

## Lesson Outline 

1. Introduction: Capstone projects as concrete anchor
2. Framework Choice Under Uncertainty and Why Some Selection Strategies Fail in Production
3. A Theory for Choosing: Decision Axes Instead of Brands
4. The Landscape Today: Frameworks, Philosophies & Adoption Snapshot
5. Framework Deep Dive: LangGraph
6. Framework Deep Dive: OpenAI Agents SDK
7. Framework Deep Dive: AgentKit
8. Framework Deep Dive: CrewAI
9. Framework Deep Dive: PydanticAI
10. Framework Deep Dive: AutoGen
11. Framework Deep Dive: Claude Agent SDK
12. Framework Deep Dive: FastMCP
13. Choosing for Your Project: Decision Matrix & Tentative Forecasts
14. Our Capstone Pivots
15. Conclusion

## Section 1 - Introduction

- Anchor the entire lesson in the two capstone projects introduced in the previous lesson: the adaptable and interactive research agent (Nova) and the reliable, auditable writing agent (Brown).
- Surface the risks of late or wrong framework choice: brittle abstractions that break under real load, stalled progress in a fast-moving ecosystem, or hidden gaps in durability that only appear after weeks of investment.
- Introduce the two core concepts that will recur throughout the lesson: LangGraph interrupts and checkpoints for resumable auditability in the writing agent versus MCP as a universal interoperability layer that keeps tools portable.
- Preview the high-level architecture that will be used as the consistent reference point: research agent built as a lightweight MCP server that any client can steer, writing agent built as a durable workflow that exposes coarse-grained MCP tools.
- Clarify the lesson focus: philosophies, core abstractions, production trade-offs, and decision principles rather than raw API syntax or hello-world tutorials.
- Include an image as image 1 that shows the high-level architecture illustrating the two capstone builds, their client-server interactions via MCP, and hybrid MCP-plus-LangGraph usage (research side lightweight and exploratory, writing side stateful and auditable). The link of image 1 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e167f50b-ae33-459e-8365-53f204ffa781/image/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 1: High-level architecture diagram illustrating the two capstone builds: an adaptable research agent and a reliable writing hybrid agent, showing their client-server interactions."
- Transition to Section 2: With the capstones as our concrete reference, we can now examine why framework selection under uncertainty so often fails in production and what layers (runtime, protocol, tooling) actually solve which problems.

- **Section length:** 260 words

## Section 2 - Framework Choice Under Uncertainty and Why Some Selection Strategies Fail in Production

- The AI agent ecosystem is new and evolving quickly, and no universal framework will satisfy every use case. Stress the importance of clearly distinguishing the three layers that are frequently conflated: runtime (orchestration and state management), protocol (standardization and portability such as MCP), and tooling framework (implementation details and server scaffolding).
- Explain the distinct production problems each layer solves: runtime (e.g., LangGraph, CrewAI, PydanticAI, OpenAI Agents SDK, AgentKit, AutoGen) delivers durable execution and resumability; protocol (e.g., Model Context Protocol, MCP) prevents tool lock-in and rewriting; tooling (e.g., FastMCP) supplies ready-to-deploy transports, authentication, and developer experience.
- Include an image as image 2 that shows a block diagram illustrating the distinct roles and relationships among runtime, protocol (MCP), and tooling framework layers, with arrows showing how MCP decouples tools from any particular runtime. The link of image 2 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b7c59478-b2c1-45b1-956b-b9b6b213bf9a/image/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 2: Diagram illustrating the relationships and functionalities of Runtime, Protocol, and Tooling Framework."
- Detail common failure modes when engineers select frameworks via hype cycles or simple hello-world demos: choosing a framework that is too simple and therefore lacks reliability primitives for production workloads, or choosing one that is overly complex and introduces unneeded overhead for exploratory work.  
- Use the capstone pivot example to illustrate: an initially chosen static graph failed for the divergent, interactive nature of the research agent but succeeded for the repeatable, auditable writing agent.
- Present interactive versus deterministic workloads as a quick initial lens for assessing framework fit before deeper analysis.
- Transition to Section 3: Use the following personal story to conclude section 2.
We learned this firsthand. We initially planned to build our research agent with a static LangGraph workflow. However, we quickly realized that research is an interactive and divergent process. We needed to add tools, pivot strategy, and replan on the fly. A rigid graph was a wrong fit. Instead, we moved the “work” into portable MCP tools and kept the orchestration light. For the writing agent, which required a repeatable, auditable process, we did the opposite: we used LangGraph for its explicit state management and checkpoints, ensuring a durable and observable workflow.

- **Section length:** 350 words

## Section 3 - A Theory for Choosing: Decision Axes Instead of Brands

To avoid these traps, you need a way to evaluate frameworks based on principles. Introduce the following four decision axes that can help analyze any new library and determine if it fits any project’s needs.

- Include an image as Image 3 that visualizes the four decision axes as two-by-two spectra or quadrants, with example framework placements and capstone project markers on each axis. The link of image 2 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/fb91871d-9101-48fb-80df-7200f8e0db66/image/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 3: A diagram illustrating the four key decision axes for evaluating AI agent frameworks."
- Present the first axis—control-flow explicitness versus LLM-driven autonomy: graph-based determinism (explicit nodes and edges) like LangGraph delivers auditability - control over every state transition. It is ideal for deterministic, auditable workflows where you need to know precisely why the system made a particular decision. Meanwhile, lightweight agent loops, like the OpenAI Agents SDK, favor exploration and adaptability. This is better for exploratory tasks where the path to a solution is not known in advance. The question to ask is: Does your application require repeatable, auditable steps, or does it need to navigate an unpredictable environment?
- Present the second axis—reliability primitives: A good framework provides tools to handle those failures gracefully. Look for features like checkpointing, time-travel replay, HITL interrupts, and durable execution across restarts; these are non-negotiable for the writing agent but less critical for the research agent. Cite the golden source [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence) to show that LangGraph emphasizes interrupts and persistence, meanwhile cite the golden source [Durable Execution](https://ai.pydantic.dev/durable_execution/overview/) to show that PydanticAI integrates with systems like Temporal and DBOS for durable execution.
- Present the third axis—abstraction level and developer experience: Some, like the OpenAI Agents SDK, provide minimal primitives (Agents, Tools, Guardrails) like the OpenAI Agents SDK require more boilerplate but deliver flexibility; others like CrewAI opinionated constructs accelerate initial velocity yet reduce adaptability at the edges.
- Present the fourth axis—tooling interoperability: MCP functions as the USB-C equivalent for AI, providing a standard interface for tools, letting you write tools once as MCP servers (for example, with FastMCP, please cite golden source. [FastMCP](https://gofastmcp.com/)) and reuse them across runtimes and IDEs speaking the MCP protocol,including LangGraph, the OpenAI Agents SDK, or even IDEs like Cursor, without rewriting.
- Map the four axes onto the concrete capstone requirements: the research agent needs high autonomy plus portability, while the writing agent needs explicit control plus strong reliability primitives.
- Transition to Section 4: Emphasize that our capstone projects map to the four decision axes. The research agent requires autonomy and interoperable tools for its exploratory nature, making a lightweight loop with MCP a good fit. The writing agent demands an explicit, auditable workflow with reliability primitives, making LangGraph the better choice.

-  **Section length:** 425 words

## Section 4 - The Landscape Today: Frameworks, Philosophies & Adoption Snapshot

With these decision axes in mind, let’s survey the current landscape of agent frameworks.

- Detail LangGraph philosophy: stateful graph model with native checkpoints and interrupts for auditable workflows(Cite golden source [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)), ideal for processes that need to be resumable and traceable(Cite golden source [Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)); 

- Tell the reader that LangGraph has strong, consistent daily download activity, averaging around 400K–500K downloads per day over the past three months.

- Use a callout box (with the "aside" XML tagg), contrast this with the broader LangChain toolkit from which it emerged along the line of the text below:

💡 LangGraph vs. LangChain

LangGraph is part of the LangChain ecosystem but serves a distinct purpose. While **LangChain** provides the broad toolkit for building LLM applications (chains, memory, tools, retrievers, etc.), **LangGraph** focuses specifically on **structured**, **stateful workflows**. It introduces graph-based execution with checkpoints and resumability, which are features not native to standard LangChain chains.

In short, LangChain is the toolbox, while LangGraph is the workflow engine that brings determinism and recovery to complex agent interactions (You can cite golden source 1[Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)).

You will see LangChain code in the writing agent.

- Include an image as Image 4. The link of image 4 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/73d4d93b-c058-4979-89bc-c94fc44fbb1c/Screenshot_2025-10-16_175628/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 4: Source: pepy.tech, daily downloads for LangGraph, accessed October 15, 2025."

- Detail OpenAI Agents SDK: minimal surface area consisting of agents, tools, guardrails, handoffs, and sessions (Cite golden source [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)); favors lightweight Python-native loops over compiled state machines.

- Include an image as Image 5. The link of image 5 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/6da7731a-daf0-4b2d-84b2-c2ab75951be2/Screenshot_2025-10-16_175409/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 5: Source: pepy.tech, daily downloads for OpenAI Agents SDK, accessed October 15, 2025."

- Tell the reader that the OpenAI Agents SDK library has recorded 90K–120K daily downloads over the past three months, with a slight upward trend.

- Detail AgentKit as a  modular toolkit for building, deploying, and optimizing agents across the OpenAI platform, unifying visual builder, connectors (including MCP), ChatKit embedding, and evaluation infrastructure. Developers can visually compose multi-agent systems, manage connectors, and embed chat-based experiences directly in their products—all backed by versioning, guardrails, and evaluation tools for safe, reliable deployment.

- Include a callout box(enclosed in the "aside" XML tag), comparing OpenAI AgentKit vs OpenAI Agents SDK:
    The **Agents SDK** is a lightweight developer framework for code-first agent creation, ideal for direct API orchestration and fine-grained control. **AgentKit**, by contrast, is a **complete lifecycle toolkit** that layers on top of the SDK: it adds a **visual builder, UI embedding tools**, and **evaluation infrastructure**. In short, the SDK is the coding foundation, while AgentKit is the integrated platform for design, deployment, and optimization.

- Detail CrewAI duality: role-based autonomous crews for collaborative exploration versus event-driven flows for deterministic control, plus strong CLI and YAML developer experience.

- Include an image as Image 6. The link of image 6 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/97392864-1995-4e2f-b31a-ff01325ee0e7/Screenshot_2025-10-16_181034/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 6: Source: pepy.tech, daily downloads for Crewai, accessed October 15, 2025."

- State that the CrewAI library has **daily downloads ranging between 40K and 100K**.

- Detail PydanticAI emphasis on type safety, schema-driven validation, and durable execution integrations with Temporal, DBOS, or Prefect plus built-in graph support.

- Include an image as Image 7. The link of image 7 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/7b1f1d0a-f1f8-45b8-95de-0f832f0c9712/Screenshot_2025-10-16_182609/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 7: Source: pepy.tech, daily downloads for PydanticAI, accessed October 15, 2025."

- State that Daily downloads of Pydantic-AI doubled from ~150k in July to **300- 450k** by October 2025, demonstrating strong growth momentum.

- Detail AutoGen layered approach: Studio GUI explicitly positioned for exploration and not production, feeding ideas into AgentChat or core libraries for hardening.

- Include an image as Image 8. The link of image 8 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/b2998c69-ca90-4f1d-a60f-e090f4705715/Screenshot_2025-10-16_181515/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 8: Source: pepy.tech, daily downloads for autogen, accessed October 15, 2025."

- Detail Claude Agent SDK: A newer entrant from Anthropic, model-family-specific tight integration that leverages Claude strengths in large context and low-level tool use, but with a smaller ecosystem.

- Detail FastMCP as a non-runtime tooling layer: build MCP-compliant servers and clients once so tools become portable across any runtime or IDE.

- Include an image as Image 9. The link of image 9 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e0e1b539-2a2c-4226-b70e-b93596e382a4/Screenshot_2025-10-16_182130/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 9: Source: pepy.tech, daily downloads for FastMCP, accessed October 15, 2025."

- State that FastMCP demonstrates explosive growth, with daily downloads surging from ~250k in July to peaks of over **1.2M per day** in October 2025, a 5x increase over three months.

- Use adoption metrics as a maturity proxy: download trends and GitHub stars to gauge hiring risk, ecosystem health, and long-term maintenance burden.

- Include an image as Image 10. The link of image 10 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026."

- Warn against single-framework dogma and illustrate common hybrid patterns: FastMCP tools consumed inside LangGraph, or migrating from AutoGen prototypes to hardened runtimes.

- Transition to Section 5: We now deep-dive into each framework, starting with LangGraph, using the four axes and capstone needs as constant evaluation lenses.

-  **Section length:** 800 words

## Section 5 - Framework Deep Dive: LangGraph

- Describe the graph-based modeling approach in which nodes are Python functions and edges are explicit transitions, making complex multi-step logic transparent and auditable.
- Highlight core production primitives: interrupts for human-in-the-loop, persistence and checkpointing for resumability, and time-travel debugging that lets you replay and branch from any prior state.
- Contrast the two definition styles (“graph API” - fully explicit graphs - versus “functional API” - decorator-based) and the resulting trade-off between learning curve and determinism payoff.
- Explain when LangGraph is overkill: simple exploratory scripts benefit from lighter loops, whereas repeatable auditable processes such as the writing agent justify the modeling investment.
- Contrast with lighter autonomous loops: steeper upfront modeling cost but built-in safety, observability, and durability that prevent brittle production failures.
- Transition to Section 6: Having examined a graph-centric, reliability-first option, we now turn to a deliberately minimal alternative.

-  **Section length:** 250 words

## Section 6 - Framework Deep Dive: OpenAI Agents SDK

- Articulate the philosophy of minimal primitives that deliberately reduces conceptual surface area while still enabling powerful agentic applications.
- Map the core concepts—agents with instructions and tools, guardrails for safety, handoffs between agents, sessions for history—and show how they interrelate:
    - **Agents**: LLMs equipped with instructions and tools.
    - **Tools**: Python functions that agents can call to interact with the outside world.
    - **Guardrails**: Mechanisms for validating agent inputs and outputs to ensure safety and   correctness.
    - **Handoffs**: A way for agents to delegate tasks to other, more specialized agents.
    - **Sessions**: Automatically manage conversation history across multiple runs.

- Include an image as Image 11. The link of image 11 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/f5434281-c286-43ad-b086-9ee3b6ceec0d/image/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 11: Diagram illustrating the core primitives of the OpenAI Agents SDK and their relationships."

- Contrast the execution model (direct Python control flow with if/else and loops) against compiled state machines in graph systems. The fundamental difference between OpenAI Agents SDK and LangGraph’s functional API lies in the execution model. The OpenAI SDK uses a simple, Python-native agent loop that you control directly. Orchestration is handled with standard Python code (e.g., `if/else` statements, `for` loops). In contrast, even with the decorator-based functional API, LangGraph compiles your code into an explicit, stateful graph. This underlying state machine manages execution, persistence, and interruptions, providing a more robust but also more constrained environment than the SDK’s straightforward loop.
- Highlight the strength for teams that want a fast production path when lightweight orchestration and sensible defaults are preferred.
- Surface the reliability trade-off: durable pause, resume, and checkpointing features must be implemented by the team because they are not provided out of the box.
- Transition to Section 7: The natural extension of the minimal SDK is a full-lifecycle platform built on top of it.

-  **Section length:** 300 words

## Section 7 - Framework Deep Dive: AgentKit

- Position AgentKit as a complete lifecycle toolkit layered on the OpenAI Agents SDK, covering design, deployment, optimization, and continuous improvement.It extends the OpenAI Agents SDK by adding visual workflow design, UI embedding, and evaluation infrastructure.

- Include an image as Image 12. The link of image 12 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ca9dc7f7-c280-4434-8a53-e0322ef1f660/image/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 12: The Homework Helper workflow in AgentKit shows how agents collaborate to rewrite queries, classify intent, and route requests to specialized agents."

- Enumerate key components: visual Agent Builder canvas with versioning, Connector Registry (including MCP connectors), ChatKit for UI embedding, and evaluation plus reinforcement-from-traces infrastructure:
    - **Agent Builder**: A drag-and-drop canvas for designing and versioning multi-agent workflows. Builders can compose logic visually, add guardrails, and run preview tests with inline evaluation and version control.
    - **Connector Registry**: A centralized interface for managing data connections (Dropbox, Google Drive, SharePoint, Teams, and third-party MCPs) across workspaces and organizations.
    - **ChatKit**: A toolkit for embedding agentic chat UIs directly into web or mobile products, handling streaming responses, conversation threads, and custom theming.
    - **Evals and Reinforcement Fine-Tuning (RFT)**: Expanded capabilities for measuring, grading, and improving agent performance, including datasets, automated prompt optimization, and custom graders.
    - **AgentKit sits one layer above the OpenAI Agents SDK**: you still use the SDK for code-first orchestration, but AgentKit provides the surrounding tools for design, deployment, and continuous improvement.
- Explain how visual composition and built-in evaluation tools support safe multi-agent systems at scale without forcing everything into code.
- Discuss the ecosystem optimization trade-off: strongest when staying inside the OpenAI stack, yet growing MCP connector support improves broader interoperability.
- Clarify when AgentKit adds clear value over the raw SDK: teams that need no-code workflow design, versioning, and continuous improvement loops.
- Transition to Section 8: We now examine a framework whose duality spans both autonomous crews and structured flows.

-  **Section length:** 250 words

## Section 8 - Framework Deep Dive: CrewAI

- Include an image as Image 13. The link of image 13 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3bcc81dc-f35c-4a6b-95e8-557db10090a9/e0cb631a-91ae-46fc-a332-d5e1afd61c80/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 13: Setting up an autonomous agent in CrewAI Studio using the visual editor. Each agent is assigned a role, goal, and model here, powered by `gpt-4o-mini`."

- Describe the dual architecture: role-based autonomous crews optimized for collaborative exploration versus flows for event-driven deterministic orchestration.I t introduces a powerful duality with its two main concepts: **Crews** and **Flows**.
- Outline the typical progression pattern: begin with autonomous crews for rapid prototyping, then layer flows for structure once requirements solidify:
    - **Crews** are for role-based, autonomous collaboration. You define agents with specific roles, goals, and tools, and they work together to solve a problem, much like a human team.
    - **Flows** are for event-driven, deterministic orchestration. They give you fine-grained control over the workflow, allowing you to define precise execution paths.
    This dual architecture lets you start with an autonomous crew for rapid prototyping, then introduce a flow to add structure and control as your requirements become more defined.

- Emphasize the DX focus: CLI scaffolding, YAML definitions for agents and tasks, and configurable memory and persistence options.
- Identify the sweet spot in multi-agent handoff scenarios (for example researcher-to-writer flows) where role clarity accelerates development.
- Surface the trade-off of opinionated constructs: rapid initial velocity but configuration overhead and reduced flexibility when edge cases appear.
- Transition to Section 9: Another framework approaches the problem through the lens of type safety and compile-time contracts.

-  **Section length:** 275 words

## Section 9 - Framework Deep Dive: PydanticAI

- Articulate the FastAPI-like philosophy in which Pydantic models and type hints create compile-time contracts between code and LLM behavior.

- Include an image as Image 14. The link of image 14 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/0454e524-5d87-4288-82d4-3abd2b78a6f2/image/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 14: Diagram illustrating PydanticAI's design philosophy."

- Highlight production features: **durable execution integrations** with Temporal, DBOS, or Prefect, which allows agents to survive restarts, pause for human input, and resume long-running tasks, plus built-in **graph support** for non-linear flows.
- Detail ergonomics wins: automatic schema generation from type hints and docstrings, structured output with automatic retries on validation failure.
- Acknowledge the up-front schema investment as both a strength (correctness guarantees) and a potential learning-curve cost for teams new to strict typing.
- State the best-fit scenario: projects where structured data correctness and long-running resumable tasks are paramount, aligning well with the writing agent’s auditability needs.
- Transition to Section 10: We now look at a layered system explicitly separating experimentation from production hardening.

-  **Section length:** 180 words

## Section 10 - Framework Deep Dive: AutoGen

- Include an image as Image 15. The link of image 15 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/14fc33bd-0c3c-48e1-a49f-ac4166fa0a5c/image/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 15: Visualizing a multi-agent workflow in AutoGen Studio. Each block represents an agent, model, or termination condition, showing how conversations and actions flow within an experimental agent team."

- Describe the layered design that deliberately separates experimentation from production: Studio GUI for no-code prototyping, AgentChat for conversational applications, and Core for custom primitives:
    - **AutoGen Studio** is a low-code GUI that lets you prototype agent teams and workflows without writing code. You can visually compose agents, configure their tools, and test their interactions.

    - **AgentChat** is a programming framework for building conversational multi-agent applications.

    - **Core** provides low-level, event-driven primitives for building scalable, custom agent systems.

- Outline the typical workflow: explore and validate ideas visually inside Studio, then harden the successful patterns into code using the lower layers.
- Include the explicit disclaimer that Studio remains a research prototype and is not production-ready.
- Highlight its strength as an R&D laboratory for discovering multi-agent conversation patterns and effective termination conditions.
- Surface the trade-off: high flexibility during exploration requires the team to re-implement reliability, security, and observability when moving to production.
- Transition to Section 11: A newer entrant focuses on tight model-family integration.

-  **Section length:** 220 words

## Section 11 - Framework Deep Dive: Claude Agent SDK

- Articulate the tight integration philosophy that leverages Claude model strengths: large context windows, strong reasoning, and fine-grained control over tool use.
- Focus on ergonomic tool calling and orchestration tailored specifically to the Anthropic model family.
- Detail the trade-offs of a newer entrant: smaller community, fewer third-party integrations, and a rapidly evolving API surface.
- Frame the opportunity versus risk: early adoption can yield model-optimized performance, but teams must balance this against ecosystem maturity.
- State the clearest use case: teams already committed to the Anthropic stack who want native performance and are willing to accept smaller community support.
- Transition to Section 12: The final deep dive examines a non-runtime layer that complements every option above.

-  **Section length:** 135 words

## Section 12 - Framework Deep Dive: FastMCP

- Include an image as Image 16. The link of image 16 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/745828fd-27e2-4a50-b613-7275a1e1dceb/image/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 16: FastMCP Architecture and Interoperability"

- Clarify FastMCP’s non-runtime role: it lets you build MCP-compliant servers and clients so that tools, resources, and prompts become portable across any runtime or IDE that speaks the protocol.
- Emphasize the interoperability benefit: write a tool once and reuse it inside LangGraph, the OpenAI SDK, Cursor, Claude Code, or any future compatible system.
- Cover production extensions beyond the protocol itself: authentication, server composition, and cloud deployment features.
- Illustrate the capstone usage pattern: the research agent implemented as a FastMCP server that any client can steer, while the writing agent exposes its complex workflows as coarse-grained MCP tools.
- Use a callout box (enclosed in "aside" XML tag) to highlight the simple Pythonic developer experience achieved through decorators that handle schema generation and transport details automatically:
💡 **Pattern: tools-as-workflows (Brown)** 
For our writing agent (Brown), we wrap each workflow entry point as a **coarse-grained MCP tool** (e.g., `generate_article`, `edit_article`, `edit_selected_text`). The MCP tool handler simply **kicks off the corresponding LangGraph run** , returns progress/messages, and finally yields artifacts and diffs. This gives you MCP portability (Cursor, Claude Code) **without** losing LangGraph’s durability and auditability.
You’ll learn more about this in the later lessons.

- State that the eveloper experience of FastMCP is designed to be simple and Pythonic, and users can expose a function as tool with a single decorator, and FastMCP handles schema generation and transport. To prove this, include a code snippet as a quick example from the official docs in golden source [Quickstart](https://gofastmcp.com/getting-started/quickstart).

- Transition to Section 13: With deep dives complete, we can now synthesize everything into a decision matrix and tentative forecasts.

-  **Section length:** 255 words

## Section 13 - Choosing for Your Project: Decision Matrix & Tentative Forecasts

- Present a decision matrix as a table that maps common project needs (durability and HITL requirements, typed contracts, minimal primitives, role-based teams, exploration laboratory needs, tool portability) to the relative strengths of each framework, the title of the table should be "Table 1: Decision matrix comparing AI agent frameworks against common needs" verbatim:

| Feature | LangGraph | PydanticAI | OpenAI SDK | AgentKit | CrewAI | AutoGen | FastMCP |
|---------|---|---|---|---|---|---|---|
| **Durability/HITL/Replay** | ✅ | | | | | ✅ | |
| **Typed Contracts + Durable Execution** | | ✅ | | | | | ✅ |
| **Few Primitives + Guardrails/Handoffs** | ✅ | | ✅ | ✅ | | | ✅ |
| **Role-based Teams + Quick Scaffolding** | | | | ✅ | ✅ | ✅ | |
| **Exploration Lab** | | | ✅ | ✅ | ✅ | ✅ | |
| **Tool Portability Across Stacks** | | ✅ | | ✅ | | | ✅ |

- Include the evolving-nature caveat: treat the matrix as a snapshot and re-evaluate against the four decision axes whenever libraries release major updates.

- Offer forecasts grounded in the axes: LangGraph and PydanticAI for reliability-heavy workflows, OpenAI SDK for lightweight simplicity, AgentKit when visual design and continuous evaluation loops are required.
- Note CrewAI’s suitability for rapid multi-agent prototyping, FastMCP as the universal tooling substrate, and AutoGen as a strong R&D starting point.
- Illustrate common hybrid patterns that appear in practice: FastMCP tools consumed inside LangGraph workflows, migration from AutoGen Studio prototypes to hardened runtimes, and exposing complex graphs as single MCP commands to gain IDE portability without sacrificing durability.

- Transition to Section 14: To make the theory concrete, we now share the actual pivots we made while building the course capstones.

-  **Section length:** 240 words

## Section 14 - Our Capstone Pivots

Let’s apply this matrix to our capstone project. Our decision-making process evolved as we built, highlighting the importance of choosing the right tool for the job.

- Contrast the initial plan (LangGraph for both agents) with reality: the research agent’s need for high interactivity and divergent exploration made rigid graphs cumbersome, while flexible MCP tools proved superior.
- Show the opposite requirements for the writing agent: its repeatable, auditable process demanded LangGraph’s checkpoints, HITL interrupts, and time-travel replay capabilities.
- Describe the resulting hybrid outcome: Nova implemented as a FastMCP server that any client (including IDEs) can steer, Brown implemented as a LangGraph workflow whose entry points are deliberately coarse MCP tools.
- Explain the emergent pattern of wrapping complex internal workflows behind single MCP commands so that portability is gained without sacrificing durability or auditability.
- Detail why the OpenAI Agents SDK was considered but ultimately deprioritized: it lacked first-class persistence and deep MCP integration required for the long-running nature of both capstone tasks. Brown currently exposes three tools: `generate_article`, `edit_article`, and `edit_selected_text`.
- Transition to Section 15: These real pivots illustrate the central lesson of the entire module.

-  **Section length:** 275 words

## Section 15 - Conclusion

- Summarize the core takeaway: prioritize stable concepts (stateful graphs, typed contracts, durable execution, MCP standardization) over transient brand names.
- Position the MCP specification itself as high-leverage reading: a one-time investment yields portability across every current and future stack.
- Outline a practical selection process: apply the four decision axes to your project, start with the smallest viable stack that meets reliability needs, and keep all tooling portable via MCP.
- Provide a migration path example: begin exploration in AutoGen Studio, extract successful patterns into FastMCP tools, then anchor production in LangGraph or PydanticAI.
- Look forward to the next lesson on system design (model selection, cost/latency trade-offs, HITL placement) and the subsequent hands-on capstone builds that use the hybrid FastMCP-plus-LangGraph stack chosen through this exact process: *Nova** with **FastMCP** (server/client, ingestion, Perplexity loops, filtering, `research.md`) and **Brown** with **LangGraph + FastMCP** (workflow + MCP tools, profiles via context engineering, evaluator‑optimizer review‑edit cycles, HITL editing).
-  **Section length:** 300 words

## Golden Sources

- [Workflows and agents](https://docs.langchain.com/oss/python/langgraph/workflows-agents)
- [Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [Introduction](https://docs.crewai.com/introduction)
- [Quickstart](https://docs.crewai.com/quickstart)
- [Build your first Flow](https://docs.crewai.com/guides/flows/first-flow)
- [Durable Execution](https://ai.pydantic.dev/durable_execution/overview/)
- [AutoGen](https://microsoft.github.io/autogen/stable/)
- [AutoGen Studio User Guide](https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/index.html)
- [FastMCP](https://gofastmcp.com/)
- [Quickstart](https://gofastmcp.com/getting-started/quickstart)