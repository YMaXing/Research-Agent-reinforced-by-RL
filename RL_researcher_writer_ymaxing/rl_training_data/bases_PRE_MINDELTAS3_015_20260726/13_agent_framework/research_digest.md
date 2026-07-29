<digest_meta>
  <article_title>13_agent_framework</article_title>
  <total_sources>11</total_sources>
  <total_artefacts>3</total_artefacts>
  <tavily_saturation>1.0</tavily_saturation>
  <n_orphan_anchors>42</n_orphan_anchors>
  <n_content_sections>15</n_content_sections>
  <external_evidence_policy>allowed</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
| A01 | CrewAI-introduction | table | case,architecture | 5 | \| Use Case \| Architecture \| |
| A03 | openai-agents-sdk | table | goal,start | 10 | \| Goal \| Start here \| |
</artefact_registry>

<sources>
<s slug="CrewAI-build-your-first-flow" type="golden_web">CrewAI Flows provide event-driven orchestration that combines agent crews, direct LLM calls, and procedural Python code for precise control over AI workflows. The source demonstrates this via a guide_creator_flow project that generates a comprehensive learning guide on any user-specified topic for beginner/intermediate/advanced audiences. Key concepts include state management across steps, sequential/conditional execution paths, integration of external systems, and mixing interaction patterns (crews for collaboration, single LLM calls for structured output, and regular code for logic). The flow uses Pydantic models (Section, GuideOutline, GuideCreatorState) for type-safe data, the LLM class for direct calls (e.g., model="openai/gpt-4o-mini" with response_format=GuideOutline), and decorators (@start, @listen) to wire event-driven steps. Concrete implementation steps: `crewai create flow guide_creator_flow` scaffolds the project; `crewai flow add-crew content-crew` adds a specialized crew; agents.yaml defines content_writer and content_reviewer (with role/goal/backstory/llm fields); tasks.yaml defines write_section_task (500-800 words, Markdown, context from previous_sections) and review_section_task (with context linking to the writer task). The ContentCrew class (using @CrewBase, @agent, @task, @crew) runs Process.sequential. The main GuideCreatorFlow implements get_user_input, create_guide_outline (direct LLM JSON output saved to output/guide_outline.json), and write_and_compile_guide (iteratively calling ContentCrew().crew().kickoff with section inputs, accumulating sections_content, then writing output/complete_guide.md). Additional CLI commands include `crewai flow kickoff`, `crewai install`, `crewai flow plot` (producing guide_creator_flow.html), and .env configuration for OPENAI_API_KEY, GEMINI_API_KEY or ANTHROPIC_API_KEY. The source includes a 23-line Python tool-loop example in the flow definition and references the LLM setup guide and installation guide. No quantitative benchmarks, performance claims, or comparative data are provided. Coverage gaps include absence of error handling details, parallel execution examples (and_/or_ functions or @router), conversational flows, external API integrations, or scaling considerations beyond the single sequential content example.</s>
<s slug="CrewAI-introduction" type="golden_web">CrewAI is an open-source framework for building production-ready multi-agent systems that combine CrewAI Flows for structured control with CrewAI Crews for autonomous collaboration. Flows act as the application backbone, providing state management across steps, event-driven execution triggered by external inputs, and control flow primitives including conditional logic, loops, and branching. Crews operate inside Flow steps as teams of role-playing agents that receive delegated tasks, collaborate autonomously, and return results; each agent is defined with specific goals and tools. The framework supports installation of coding agent skills via the command `npx skills add crewaiinc/skills` for Claude Code, Codex, and similar environments. Concrete integration points include any API, database, or local tool through the Flexible Tools layer. Execution sequence is deterministic: a Flow starts a process or reacts to an event, manages persistent state, delegates complex work to a Crew, receives the Crew output, and resumes control flow. Key claims include production-grade reliability for long-running processes, cost efficiency through minimized token usage and API calls, and enterprise security/compliance features. The source includes a 5-line table on case architecture. Coverage gaps include absence of code samples, performance benchmarks, concrete agent role definitions, tool schemas, or comparisons against other frameworks; the material remains at the conceptual architecture level without implementation metrics or failure modes.</s>
<s slug="FastMCP-quickstart" type="golden_web">FastMCP is a Python framework for building MCP servers that expose tools, resources, and other components to LLM clients. The quickstart covers server creation via the `FastMCP` class, tool registration with the `@mcp.tool` decorator, execution through `mcp.run()` or the `fastmcp run` CLI, and client interaction using the asynchronous `Client` class. Key techniques include selecting transports (`stdio` for local use or `http` for remote access at endpoints such as `http://localhost:8000/mcp`), wrapping the `run()` call in an `if __name__ == "__main__":` block for script compatibility, and invoking tools via `client.call_tool(name, arguments)`. The CLI command `fastmcp run my_server.py:mcp --transport http --port 8000` starts servers without executing the `__main__` block. UI support requires the `apps` extra and the `app=True` flag on `@mcp.tool`; tools then return `PrefabApp` instances built from components such as `Column`, `Row`, `Heading`, `Text`, and `Badge` (imported from `prefab_ui`). Deployment targets Prefect Horizon, an enterprise MCP hosting platform that provides managed URLs, authentication, and observability; servers are published by pushing `my_server.py` to GitHub and specifying the `my_server.py:mcp` entrypoint. The guide includes a 23-line Python tool-loop example and a 15-line Prefab UI example that demonstrate end-to-end usage. No performance benchmarks, latency figures, or comparative claims appear. Coverage is limited to initial setup and basic tool/UI patterns; advanced topics such as resource handling, state management, forms, charts, and server-connected interactivity are referenced only via external links to the Apps overview and Prefect Horizon guide.</s>
<s slug="LangGraph-persistence" type="golden_web">LangGraph persistence enables applications to retain information across graph runs for conversation continuity, recovery from interruptions, human-in-the-loop workflows, fault tolerance, and cross-thread memory such as user preferences or shared facts. It supplies two systems: checkpointers, which save thread-scoped graph state as checkpoints via the Checkpointer interface, and stores, which hold application-defined data outside graph state via the Store interface. Most setups combine both, with a checkpointer tracking the current thread and a store handling durable cross-thread data. The quickstart demonstrates compilation with concrete classes: `from langgraph.checkpoint.memory import InMemorySaver` and `from langgraph.store.memory import InMemoryStore`, followed by `builder.compile(checkpointer=checkpointer, store=store)` and `graph.invoke(..., {"configurable": {"thread_id": "thread-1"}})`. When the Agent Server is used, checkpointer and store configuration is handled automatically without manual implementation. The source includes an 8-line comparison table covering checkpointer versus store distinctions in scope, use cases, and lifetime. No quantitative benchmarks, performance claims, or implementation metrics are provided. Coverage is limited to high-level concepts and the InMemory variants; production backends, serialization details, and advanced APIs are deferred to linked documentation on checkpointers and stores.</s>
<s slug="PydanticAI-durable-execution" type="golden_web">Pydantic AI enables durable agents that preserve execution state across transient API failures, application errors, restarts, and long-running asynchronous or human-in-the-loop workflows while retaining full support for streaming and MCP. The core offering consists of four officially supported integrations—Temporal, DBOS, Prefect, and Restate—each co-maintained by Pydantic and the respective vendor teams. These integrations rely exclusively on Pydantic AI’s public interface and function as reference implementations for custom durable systems. No performance benchmarks, latency figures, or quantitative claims appear in the source. Coverage is limited to the high-level overview page; detailed usage, configuration, and code patterns reside in the linked integration pages (not reproduced here).</s>
<s slug="autogen-studio-user-guide" type="golden_web">AutoGen Studio is a low-code interface for rapidly prototyping multi-agent AI systems, built on the AutoGen AgentChat high-level API. It supports declarative JSON or drag-and-drop configuration of teams, agents, tools, models, and termination conditions, with full compatibility to AgentChat component definitions. The four core interfaces are Team Builder (visual specification and configuration), Playground (live message streaming, control transition graphs, UserProxyAgent sessions, pause/stop controls), Gallery (discovery and import of community components), and Deployment (Python code export, endpoint testing, Docker container execution). A video tutorial for v0.4 is available at https://youtu.be/oum6EI7wohM, and source code resides at microsoft/autogen (python/packages/autogen-studio). PyPI and download badges are provided. The guide explicitly states AutoGen Studio is a research prototype, not production-ready, and recommends Docker code execution; it lacks implemented features for authentication, security, jailbreak resistance, or permission-scoped LLM data access. No benchmarks, performance data, or quantitative claims appear in the source.</s>
<s slug="autogen" type="golden_web">AutoGen is a Microsoft framework for building AI agents and multi-agent applications, organized into layered components: Studio, AgentChat, Core, and Extensions. Studio provides a web-based UI for code-free prototyping on top of AgentChat, installed via `pip install -U autogenstudio` and launched with `autogenstudio ui --port 8080 --appdir ./myapp`. AgentChat supplies a conversational programming layer (requires Python 3.10+) for single- or multi-agent apps; its quickstart demonstrates `AssistantAgent` paired with `OpenAIChatCompletionClient(model="gpt-4o")` inside an async `main()` that calls `agent.run(task=...)`. Core is the underlying event-driven runtime for deterministic or dynamic workflows, distributed agents, and multi-language collaboration research. Extensions supply pluggable implementations that integrate external services, including `McpWorkbench` (Model-Context Protocol servers), `OpenAIAssistantAgent` (Assistant API), `DockerCommandLineCodeExecutor` (sandboxed code execution), and `GrpcWorkerAgentRuntime` (distributed execution). Community extensions can be discovered or authored following the documented patterns. The source contains no performance benchmarks, accuracy metrics, or comparative evaluations. It references migration guidance from AutoGen 0.2 but provides no quantitative migration data or coverage of production deployment patterns, security hardening, or observability integrations beyond the listed runtime primitives.</s>
<s slug="fastmcp" type="golden_web">FastMCP is the standard framework for building Model Context Protocol (MCP) applications that connect LLMs to tools and data. It supports three pillars: Servers (exposing tools, resources, and prompts), Clients (connecting to local or remote MCP servers with transport negotiation and authentication), and Apps (rendering interactive UIs for tools directly in conversations). FastMCP 1.0 was incorporated into the official MCP Python SDK in 2024; the standalone project is downloaded a million times per day and powers 70% of MCP servers across languages. The framework automatically generates schemas, validation, and documentation from Python functions. A minimal server is defined as: `from fastmcp import FastMCP mcp = FastMCP("Demo 🚀") @mcp.tool def add(a: int, b: int) -> int: """Add two numbers""" return a + b if __name__ == "__main__": mcp.run()`. Clients are illustrated with an async example using `from fastmcp import Client` to call tools such as `search_fast_mcp` against the documentation server at `https://gofastmcp.com/mcp`. Documentation is also supplied in llms.txt and llms-full.txt formats, with any page convertible to markdown via a `.md` suffix. Prefect Horizon is presented as the enterprise MCP gateway offering GitHub deployment, branch previews, SSO, tool-level RBAC, audit logs, and private registries. The documentation reflects the `main` branch and marks new features with version badges (e.g., `New in version: 3.0.0`). Coverage is limited to high-level architecture and usage patterns; no performance benchmarks, detailed error-handling APIs, or multi-language client examples are provided.</s>
<s slug="openai-agents-sdk" type="golden_web">The OpenAI Agents SDK (openai-agents-python) provides a lightweight Python package for building agentic applications, positioned as a production-ready successor to the earlier Swarm experimentation framework. Core primitives are Agents (LLMs configured with instructions and tools), Agents as tools / Handoffs for delegation, and Guardrails for parallel input/output validation. The SDK supplies a built-in agent loop that manages tool invocation, result return, and iterative execution until task completion, plus tracing for visualization, debugging, evaluation, fine-tuning, and distillation via the OpenAI suite. Key features include Python-first orchestration using native language constructs, Function tools with automatic schema generation and Pydantic validation, MCP server tool calling, Sessions for persistent memory, Human in the loop mechanisms, Sandbox agents for isolated workspaces with manifest-defined files and resumable sessions, and Realtime Agents supporting gpt-realtime-2 with automatic interruption detection and context management. It defaults to the Responses API for model calls while adding runtime management of turns, guardrails, handoffs, and artifacts. The source contrasts usage: Responses API is recommended for direct control of loops and short-lived responses; the SDK is recommended for multi-step workflows, real workspaces, or coordinated execution. Installation is via `pip install openai-agents`. A minimal example demonstrates `Agent` and `Runner.run_sync` with an "Assistant" agent. Documentation links cover quickstarts for text agents, memory strategies, sandbox agents, multi-agent orchestration, and voice pipelines. The source includes a 10-line table artefact on goal-oriented paths such as speech-to-text/agent/text-to-speech pipelines. No performance benchmarks, quantitative claims, or comparative metrics are provided. Coverage is limited to OpenAI-centric workflows and lacks detailed implementation of custom tool schemas, error handling patterns, or non-OpenAI model integration.</s>
<s slug="workflows-and-agents" type="golden_web">**Main topic:** This LangChain/LangGraph guide contrasts predetermined workflows (fixed code paths) with dynamic agents (LLM-driven tool selection and loops) and details five workflow patterns plus a basic agent implementation. **Key concepts:** Workflows use StateGraph, nodes, edges, and conditional routing; agents add continuous tool-calling loops via MessagesState. Augmentations covered are tool calling (bind_tools), structured outputs (with_structured_output + Pydantic), and short-term memory. **Concrete examples and APIs:** - Setup: pip install langchain_core langchain-anthropic langgraph; ChatAnthropic(model="claude-sonnet-4-6"). - Prompt chaining: generate_joke → check_punchline (conditional edge) → improve_joke → polish_joke. - Parallelization: three independent LLM calls (call_llm_1/2/3) feeding an aggregator node. - Routing: Route Pydantic schema + llm_call_router directing to llm_call_1/2/3 via route_decision. - Orchestrator-worker: planner (Sections schema) + Send API to spawn llm_call workers writing sections into Annotated[list, operator.add] completed_sections, then synthesizer. - Evaluator-optimizer: llm_call_generator ↔ llm_call_evaluator (Feedback schema) loop until “funny”. - Agents: multiply/add/divide @tool functions, llm_with_tools, ToolNode([search, calculator]), should_continue conditional, MessagesState loop. - Prebuilt: ToolNode for parallel execution and error handling. **Data points/claims:** No quantitative benchmarks; claims are qualitative (parallelization “increases speed”, orchestrator-worker suits “unknown number of documents”, evaluator-optimizer for tasks needing iteration). **Limitations/gaps:** Coverage is LangGraph-specific with no latency/accuracy metrics, no comparison to other agent frameworks, and omits long-term memory, deployment details, and multi-agent coordination. Includes a 23-line Python tool-loop example and multiple StateGraph + draw_mermaid_png snippets illustrating each pattern.</s>
</sources>

<tavily_yield_per_section>
| section_id | helping_rounds | unique_facts | duplicate_facts |
|---|---|---|---|
| S1::section-1-introduction | 3 | 4 | 0 |
| S2::section-2-framework-choice-under-uncertainty-and-why-some-selection-strategies-fail-in-production | 1 | 4 | 0 |
| S3::section-3-a-theory-for-choosing-decision-axes-instead-of-brands | 1 | 4 | 0 |
| S4::section-4-the-landscape-today-frameworks-philosophies-adoption-snapshot | 2 | 4 | 0 |
| S5::section-5-framework-deep-dive-langgraph | 1 | 4 | 0 |
| S6::section-6-framework-deep-dive-openai-agents-sdk | 1 | 4 | 0 |
| S7::section-7-framework-deep-dive-agentkit | 3 | 3 | 0 |
| S8::section-8-framework-deep-dive-crewai | 1 | 3 | 0 |
| S9::section-9-framework-deep-dive-pydanticai | 1 | 3 | 0 |
| S10::section-10-framework-deep-dive-autogen | 1 | 3 | 0 |
| S11::section-11-framework-deep-dive-claude-agent-sdk | 2 | 3 | 0 |
| S12::section-12-framework-deep-dive-fastmcp | 2 | 3 | 0 |
| S13::section-13-choosing-for-your-project-decision-matrix-tentative-forecasts | 2 | 3 | 0 |
| S14::section-14-our-capstone-pivots | 2 | 3 | 0 |
| S15::section-15-conclusion | 2 | 3 | 0 |
tavily_saturation=1.0
</tavily_yield_per_section>

<section_coverage>
<section id="S1::section-1-introduction" self_contained="yes" sources="PydanticAI-durable-execution,FastMCP-quickstart,fastmcp" artefacts="">
  <intent>Anchor the lesson in the two capstone projects and introduce recurring concepts of LangGraph checkpoints and MCP portability.</intent>
  <depth_checklist depth_score="1">
    <item name="motivation" present="yes" evidence="fastmcp"/>
    <item name="theoretical_foundations" present="no" evidence=""/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="6" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Anchor the entire lesson in the two capstone projects introduced in the previous lesson: the adaptable and interactive r" bullet="motivation">Core anchoring to capstones is central to lesson motivation and scope.</orphan>
    <orphan route="depth" anchor="Surface the risks of late or wrong framework choice: brittle abstractions that break under real load, stalled progress i" bullet="motivation">Directly addresses production risks central to framework selection thesis.</orphan>
    <orphan route="depth" anchor="Introduce the two core concepts that will recur throughout the lesson: LangGraph interrupts and checkpoints for resumabl" bullet="theoretical_foundations">Introduces LangGraph checkpoints as foundational recurring mechanism.</orphan>
    <orphan route="depth" anchor="Preview the high-level architecture that will be used as the consistent reference point: research agent built as a light" bullet="implementation_tradeoffs">Previews hybrid architecture that defines implementation choices.</orphan>
    <orphan route="depth" anchor="Clarify the lesson focus: philosophies, core abstractions, production trade-offs, and decision principles rather than ra" bullet="motivation">Sets lesson boundaries around core abstractions and trade-offs.</orphan>
    <orphan route="depth" anchor="Include an image as image 1 that shows the high-level architecture illustrating the two capstone builds, their client-se" bullet="case_studies_metrics">Image directly supports architecture case study reference.</orphan>
  </orphan_anchors>
</section>
<section id="S2::section-2-framework-choice-under-uncertainty-and-why-some-selection-strategies-fail-in-production" self_contained="yes" sources="openai-agents-sdk,CrewAI-introduction,autogen-studio-user-guide" artefacts="">
  <intent>Distinguish runtime, protocol, and tooling layers while explaining common selection failures.</intent>
  <depth_checklist depth_score="3">
    <item name="motivation" present="yes" evidence="openai-agents-sdk"/>
    <item name="theoretical_foundations" present="no" evidence=""/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="autogen-studio-user-guide"/>
    <item name="implementation_tradeoffs" present="yes" evidence="CrewAI-introduction"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="6" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="The AI agent ecosystem is new and evolving quickly, and no universal framework will satisfy every use case. Stress the i" bullet="motivation">Establishes ecosystem uncertainty as core motivation.</orphan>
    <orphan route="depth" anchor="Explain the distinct production problems each layer solves: runtime (e.g., LangGraph, CrewAI, PydanticAI, OpenAI Agents" bullet="implementation_tradeoffs">Details layer-specific trade-offs central to framework choice.</orphan>
    <orphan route="depth" anchor="Include an image as image 2 that shows a block diagram illustrating the distinct roles and relationships among runtime," bullet="case_studies_metrics">Diagram illustrates layer distinctions as case evidence.</orphan>
    <orphan route="depth" anchor="Detail common failure modes when engineers select frameworks via hype cycles or simple hello-world demos: choosing a fra" bullet="limitations_failure_modes">Explicitly covers failure modes of hype-driven selection.</orphan>
    <orphan route="depth" anchor="Use the capstone pivot example to illustrate: an initially chosen static graph failed for the divergent, interactive nat" bullet="case_studies_metrics">Uses capstone pivot as concrete case study.</orphan>
    <orphan route="depth" anchor="Present interactive versus deterministic workloads as a quick initial lens for assessing framework fit before deeper ana" bullet="implementation_tradeoffs">Introduces workload lens as initial implementation filter.</orphan>
  </orphan_anchors>
</section>
<section id="S3::section-3-a-theory-for-choosing-decision-axes-instead-of-brands" self_contained="yes" sources="LangGraph-persistence,PydanticAI-durable-execution,workflows-and-agents" artefacts="">
  <intent>Introduce the four decision axes as principled evaluation framework.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="LangGraph-persistence"/>
    <item name="theoretical_foundations" present="yes" evidence="workflows-and-agents"/>
    <item name="technical_nuances" present="yes" evidence="PydanticAI-durable-execution"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="LangGraph-persistence"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="6" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Include an image as Image 3 that visualizes the four decision axes as two-by-two spectra or quadrants, with example fram" bullet="case_studies_metrics">Visualizes axes as core theoretical mapping.</orphan>
    <orphan route="depth" anchor="Present the first axis—control-flow explicitness versus LLM-driven autonomy: graph-based determinism (explicit nodes and" bullet="theoretical_foundations">Defines first axis as foundational control-flow theory.</orphan>
    <orphan route="depth" anchor="Present the second axis—reliability primitives: A good framework provides tools to handle those failures gracefully. Loo" bullet="technical_nuances">Details reliability primitives as technical nuance.</orphan>
    <orphan route="depth" anchor="Present the third axis—abstraction level and developer experience: Some, like the OpenAI Agents SDK, provide minimal pri" bullet="implementation_tradeoffs">Covers abstraction/DX trade-off axis.</orphan>
    <orphan route="depth" anchor="Present the fourth axis—tooling interoperability: MCP functions as the USB-C equivalent for AI, providing a standard int" bullet="implementation_tradeoffs">Defines MCP interoperability axis.</orphan>
    <orphan route="depth" anchor="Map the four axes onto the concrete capstone requirements: the research agent needs high autonomy plus portability, whil" bullet="case_studies_metrics">Maps axes directly to capstone requirements.</orphan>
  </orphan_anchors>
</section>
<section id="S4::section-4-the-landscape-today-frameworks-philosophies-adoption-snapshot" self_contained="yes" sources="autogen,openai-agents-sdk,LangGraph-persistence" artefacts="">
  <intent>Survey current frameworks with philosophies and adoption metrics.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="LangGraph-persistence"/>
    <item name="theoretical_foundations" present="yes" evidence="workflows-and-agents"/>
    <item name="technical_nuances" present="yes" evidence="openai-agents-sdk"/>
    <item name="latest_advancements" present="yes" evidence="autogen"/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="LangGraph-persistence"/>
    <item name="case_studies_metrics" present="yes" evidence="openai-agents-sdk"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="1">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="autogen"/>
  </breadth_checklist>
  <orphan_anchors n_depth="15" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Detail LangGraph philosophy: stateful graph model with native checkpoints and interrupts for auditable workflows(Cite go" bullet="theoretical_foundations">Details LangGraph stateful graph philosophy.</orphan>
    <orphan route="depth" anchor="Tell the reader that LangGraph has strong, consistent daily download activity, averaging around 400K–500K downloads per" bullet="case_studies_metrics">Provides LangGraph adoption metrics.</orphan>
    <orphan route="depth" anchor="Use a callout box (with the "aside" XML tagg), contrast this with the broader LangChain toolkit from which it emerged al" bullet="implementation_tradeoffs">Contrasts LangGraph with LangChain ecosystem.</orphan>
    <orphan route="depth" anchor="Include an image as Image 4. The link of image 4 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig" bullet="case_studies_metrics">Shows LangGraph download chart.</orphan>
    <orphan route="depth" anchor="Detail OpenAI Agents SDK: minimal surface area consisting of agents, tools, guardrails, handoffs, and sessions (Cite gol" bullet="technical_nuances">Details OpenAI SDK primitives.</orphan>
    <orphan route="depth" anchor="Include an image as Image 5. The link of image 5 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig" bullet="case_studies_metrics">Shows OpenAI SDK download chart.</orphan>
    <orphan route="depth" anchor="Tell the reader that the OpenAI Agents SDK library has recorded 90K–120K daily downloads over the past three months, wit" bullet="case_studies_metrics">Provides OpenAI SDK adoption metrics.</orphan>
    <orphan route="depth" anchor="Detail AgentKit as a  modular toolkit for building, deploying, and optimizing agents across the OpenAI platform, unifyin" bullet="implementation_tradeoffs">Details AgentKit modular toolkit.</orphan>
    <orphan route="depth" anchor="Include a callout box(enclosed in the "aside" XML tag), comparing OpenAI AgentKit vs OpenAI Agents SDK:" bullet="implementation_tradeoffs">Compares AgentKit vs SDK.</orphan>
    <orphan route="depth" anchor="Detail CrewAI duality: role-based autonomous crews for collaborative exploration versus event-driven flows for determini" bullet="theoretical_foundations">Details CrewAI dual architecture.</orphan>
    <orphan route="depth" anchor="Include an image as Image 6. The link of image 6 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig" bullet="case_studies_metrics">Shows CrewAI download chart.</orphan>
    <orphan route="depth" anchor="State that the CrewAI library has daily downloads ranging between 40K and 100K." bullet="case_studies_metrics">Provides CrewAI adoption metrics.</orphan>
    <orphan route="depth" anchor="Detail PydanticAI emphasis on type safety, schema-driven validation, and durable execution integrations with Temporal, D" bullet="technical_nuances">Details PydanticAI type safety and durability.</orphan>
    <orphan route="depth" anchor="Include an image as Image 7. The link of image 7 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig" bullet="case_studies_metrics">Shows PydanticAI download chart.</orphan>
    <orphan route="depth" anchor="State that Daily downloads of Pydantic-AI doubled from ~150k in July to 300- 450k by October 2025, demonstrating strong" bullet="case_studies_metrics">Provides PydanticAI adoption metrics.</orphan>
    <orphan route="depth" anchor="Detail AutoGen layered approach: Studio GUI explicitly positioned for exploration and not production, feeding ideas into" bullet="implementation_tradeoffs">Details AutoGen layered approach.</orphan>
    <orphan route="depth" anchor="Include an image as Image 8. The link of image 8 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig" bullet="case_studies_metrics">Shows AutoGen download chart.</orphan>
    <orphan route="depth" anchor="Detail Claude Agent SDK: A newer entrant from Anthropic, model-family-specific tight integration that leverages Claude s" bullet="latest_advancements">Details newer Claude SDK entrant.</orphan>
    <orphan route="depth" anchor="Detail FastMCP as a non-runtime tooling layer: build MCP-compliant servers and clients once so tools become portable acr" bullet="implementation_tradeoffs">Details FastMCP non-runtime role.</orphan>
    <orphan route="depth" anchor="Include an image as Image 9. The link of image 9 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig" bullet="case_studies_metrics">Shows FastMCP download chart.</orphan>
    <orphan route="depth" anchor="State that FastMCP demonstrates explosive growth, with daily downloads surging from ~250k in July to peaks of over 1.2M" bullet="case_studies_metrics">Provides FastMCP adoption metrics.</orphan>
    <orphan route="depth" anchor="Use adoption metrics as a maturity proxy: download trends and GitHub stars to gauge hiring risk, ecosystem health, and l" bullet="case_studies_metrics">Uses metrics as maturity proxy.</orphan>
    <orphan route="depth" anchor="Include an image as Image 10. The link of image 10 is "<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/ceff858e-bc8f-496f-82bb-6961316d8e5a/up_to_date_ai_agent_framework_stars_improved/w=1920,quality=90,fit=scale-down>", and the caption should be verbatim - "Image 10: Bar chart showing GitHub star counts for AI agent frameworks as of Feb 11th, 2026."" bullet="case_studies_metrics">Shows GitHub stars chart.</orphan>
    <orphan route="depth" anchor="Warn against single-framework dogma and illustrate common hybrid patterns: FastMCP tools consumed inside LangGraph, or migrating from AutoGen prototypes to hardened runtimes." bullet="implementation_tradeoffs">Warns against dogma and shows hybrid patterns.</orphan>
  </orphan_anchors>
</section>
<section id="S5::section-5-framework-deep-dive-langgraph" self_contained="yes" sources="LangGraph-persistence,workflows-and-agents" artefacts="">
  <intent>Deep dive into LangGraph graph modeling, interrupts, and checkpoints.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="LangGraph-persistence"/>
    <item name="theoretical_foundations" present="yes" evidence="workflows-and-agents"/>
    <item name="technical_nuances" present="yes" evidence="LangGraph-persistence"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="workflows-and-agents"/>
    <item name="implementation_tradeoffs" present="yes" evidence="LangGraph-persistence"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S6::section-6-framework-deep-dive-openai-agents-sdk" self_contained="yes" sources="openai-agents-sdk" artefacts="A03">
  <intent>Deep dive into OpenAI Agents SDK minimal primitives and Python-native loops.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="openai-agents-sdk"/>
    <item name="theoretical_foundations" present="yes" evidence="openai-agents-sdk"/>
    <item name="technical_nuances" present="yes" evidence="openai-agents-sdk"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="openai-agents-sdk"/>
    <item name="implementation_tradeoffs" present="yes" evidence="openai-agents-sdk"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="yes" evidence="A03"/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S7::section-7-framework-deep-dive-agentkit" self_contained="yes" sources="openai-agents-sdk,fastmcp" artefacts="">
  <intent>Deep dive into AgentKit as lifecycle toolkit layered on the SDK.</intent>
  <depth_checklist depth_score="3">
    <item name="motivation" present="yes" evidence="openai-agents-sdk"/>
    <item name="theoretical_foundations" present="no" evidence=""/>
    <item name="technical_nuances" present="yes" evidence="openai-agents-sdk"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="fastmcp"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S8::section-8-framework-deep-dive-crewai" self_contained="yes" sources="CrewAI-introduction,CrewAI-build-your-first-flow" artefacts="A01">
  <intent>Deep dive into CrewAI dual crews/flows architecture and DX focus.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="CrewAI-introduction"/>
    <item name="theoretical_foundations" present="yes" evidence="CrewAI-build-your-first-flow"/>
    <item name="technical_nuances" present="yes" evidence="CrewAI-introduction"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="CrewAI-build-your-first-flow"/>
    <item name="case_studies_metrics" present="yes" evidence="A01"/>
    <item name="artefact_available" present="yes" evidence="A01"/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S9::section-9-framework-deep-dive-pydanticai" self_contained="yes" sources="PydanticAI-durable-execution" artefacts="">
  <intent>Deep dive into PydanticAI type safety and durable execution integrations.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="PydanticAI-durable-execution"/>
    <item name="theoretical_foundations" present="yes" evidence="PydanticAI-durable-execution"/>
    <item name="technical_nuances" present="yes" evidence="PydanticAI-durable-execution"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="PydanticAI-durable-execution"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S10::section-10-framework-deep-dive-autogen" self_contained="yes" sources="autogen,autogen-studio-user-guide" artefacts="">
  <intent>Deep dive into AutoGen layered Studio/AgentChat/Core design.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="autogen"/>
    <item name="theoretical_foundations" present="yes" evidence="autogen"/>
    <item name="technical_nuances" present="yes" evidence="autogen-studio-user-guide"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="autogen-studio-user-guide"/>
    <item name="implementation_tradeoffs" present="yes" evidence="autogen"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S11::section-11-framework-deep-dive-claude-agent-sdk" self_contained="yes" sources="openai-agents-sdk" artefacts="">
  <intent>Deep dive into Claude Agent SDK tight model-family integration.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="openai-agents-sdk"/>
    <item name="theoretical_foundations" present="no" evidence=""/>
    <item name="technical_nuances" present="yes" evidence="openai-agents-sdk"/>
    <item name="latest_advancements" present="yes" evidence="openai-agents-sdk"/>
    <item name="limitations_failure_modes" present="yes" evidence="openai-agents-sdk"/>
    <item name="implementation_tradeoffs" present="yes" evidence="openai-agents-sdk"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S12::section-12-framework-deep-dive-fastmcp" self_contained="yes" sources="fastmcp,FastMCP-quickstart" artefacts="">
  <intent>Deep dive into FastMCP as non-runtime MCP tooling layer for portability.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="fastmcp"/>
    <item name="theoretical_foundations" present="yes" evidence="FastMCP-quickstart"/>
    <item name="technical_nuances" present="yes" evidence="fastmcp"/>
    <item name="latest_advancements" present="yes" evidence="FastMCP-quickstart"/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="fastmcp"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="1">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="fastmcp"/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S13::section-13-choosing-for-your-project-decision-matrix-tentative-forecasts" self_contained="yes" sources="autogen,fastmcp,openai-agents-sdk" artefacts="">
  <intent>Synthesize into decision matrix and forecasts for framework choice.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="openai-agents-sdk"/>
    <item name="theoretical_foundations" present="yes" evidence="autogen"/>
    <item name="technical_nuances" present="yes" evidence="fastmcp"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="openai-agents-sdk"/>
    <item name="case_studies_metrics" present="yes" evidence="autogen"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="1">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="fastmcp"/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S14::section-14-our-capstone-pivots" self_contained="yes" sources="FastMCP-quickstart,openai-agents-sdk,fastmcp" artefacts="">
  <intent>Apply matrix to actual capstone pivots and resulting hybrid architecture.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="fastmcp"/>
    <item name="theoretical_foundations" present="yes" evidence="FastMCP-quickstart"/>
    <item name="technical_nuances" present="yes" evidence="openai-agents-sdk"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="fastmcp"/>
    <item name="case_studies_metrics" present="yes" evidence="FastMCP-quickstart"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="0">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S15::section-15-conclusion" self_contained="yes" sources="PydanticAI-durable-execution,FastMCP-quickstart,CrewAI-build-your-first-flow" artefacts="">
  <intent>Summarize stable concepts, MCP leverage, and forward path to system design lesson.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="PydanticAI-durable-execution"/>
    <item name="theoretical_foundations" present="yes" evidence="FastMCP-quickstart"/>
    <item name="technical_nuances" present="yes" evidence="CrewAI-build-your-first-flow"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="PydanticAI-durable-execution"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="1">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="FastMCP-quickstart"/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction" need_depth="25" need_breadth="6" target_words="260" mandatory_bullets="6" must_cover_depth="2" must_stay_brief="0"/>
  <section id="S2::section-2-framework-choice-under-uncertainty-and-why-some-selection-strategies-fail-in-production" need_depth="23" need_breadth="6" target_words="350" mandatory_bullets="6" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S3::section-3-a-theory-for-choosing-decision-axes-instead-of-brands" need_depth="22" need_breadth="6" target_words="425" mandatory_bullets="7" must_cover_depth="4" must_stay_brief="0"/>
  <section id="S4::section-4-the-landscape-today-frameworks-philosophies-adoption-snapshot" need_depth="47" need_breadth="5" target_words="800" mandatory_bullets="18" must_cover_depth="12" must_stay_brief="0"/>
  <section id="S5::section-5-framework-deep-dive-langgraph" need_depth="3" need_breadth="6" target_words="250" mandatory_bullets="5" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S6::section-6-framework-deep-dive-openai-agents-sdk" need_depth="2" need_breadth="6" target_words="300" mandatory_bullets="5" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S7::section-7-framework-deep-dive-agentkit" need_depth="5" need_breadth="6" target_words="250" mandatory_bullets="5" must_cover_depth="4" must_stay_brief="0"/>
  <section id="S8::section-8-framework-deep-dive-crewai" need_depth="2" need_breadth="6" target_words="275" mandatory_bullets="5" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S9::section-9-framework-deep-dive-pydanticai" need_depth="4" need_breadth="6" target_words="180" mandatory_bullets="5" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S10::section-10-framework-deep-dive-autogen" need_depth="3" need_breadth="6" target_words="220" mandatory_bullets="5" must_cover_depth="4" must_stay_brief="0"/>
  <section id="S11::section-11-framework-deep-dive-claude-agent-sdk" need_depth="3" need_breadth="6" target_words="135" mandatory_bullets="5" must_cover_depth="2" must_stay_brief="0"/>
  <section id="S12::section-12-framework-deep-dive-fastmcp" need_depth="3" need_breadth="5" target_words="255" mandatory_bullets="6" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S13::section-13-choosing-for-your-project-decision-matrix-tentative-forecasts" need_depth="3" need_breadth="5" target_words="240" mandatory_bullets="4" must_cover_depth="2" must_stay_brief="0"/>
  <section id="S14::section-14-our-capstone-pivots" need_depth="3" need_breadth="6" target_words="275" mandatory_bullets="5" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S15::section-15-conclusion" need_depth="4" need_breadth="5" target_words="300" mandatory_bullets="5" must_cover_depth="2" must_stay_brief="0"/>
  <overall>
    <weakest_sections>S1::section-1-introduction, S4::section-4-the-landscape-today-frameworks-philosophies-adoption-snapshot</weakest_sections>
    <strongest_sections>S6::section-6-framework-deep-dive-openai-agents-sdk, S8::section-8-framework-deep-dive-crewai</strongest_sections>
    <dominant_gap_type>depth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>