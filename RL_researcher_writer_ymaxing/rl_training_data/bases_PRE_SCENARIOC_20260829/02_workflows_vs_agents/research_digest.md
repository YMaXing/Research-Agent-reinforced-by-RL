<digest_meta>
  <article_title>Workflows vs. Agents</article_title>
  <total_sources>13</total_sources>
  <total_artefacts>18</total_artefacts>
  <tavily_saturation>1.0</tavily_saturation>
  <n_orphan_anchors>35</n_orphan_anchors>
  <n_content_sections>6</n_content_sections>
  <external_evidence_policy>allowed</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
| A08 | google-gemini_gemini-cli | code:bash | installation,required | 2 | # Using npx (no installation required) |
</artefact_registry>

<sources>
<s slug="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age" type="golden_web">The source examines architectural trade-offs between orchestrated AI workflows and autonomous agents for scalable production systems, drawing on the author’s experience with CrewAI and LangGraph. It defines a workflow as a structured LLM pipeline where developers explicitly define control flow while an agent is a loop-based system in which the LLM autonomously selects tools, reasons, self-corrects, and decides completion. Key concepts include deterministic execution versus dynamic tool selection and adaptive reasoning; hybrid systems that layer reactive workflows for predictable tasks with deliberative agents for ambiguous decisions; and operational requirements such as observability, cost controls, and failure handling.</s>
<s slug="building-effective-agents" type="golden_web">Anthropic’s “Building effective agents” (Dec 19, 2024) distinguishes workflows from agents inside broader agentic systems. Workflows orchestrate LLMs and tools via fixed code paths; agents let LLMs dynamically plan, select tools, and control execution while receiving environmental feedback. The post advises starting with the simplest viable approach—often a single augmented LLM call with retrieval, tools, and memory—before adding multi-step patterns. It presents the augmented LLM as the core building block and recommends the Model Context Protocol for standardized third-party tool integration.</s>
<s slug="exploring-the-difference-between-agents-and-workflows" type="golden_web">LLM-powered agents integrate a language model, tools, and memory to reason, retrieve data, and act via external systems such as APIs or databases. The source contrasts them with workflows and details an Agentic RAG implementation called the Second Brain agent. Agents follow the ReAct loop (act by calling tools, observe outputs, reason about next steps). Workflows execute a fixed predefined sequence of steps, offering reliability but rigidity similar to classic programming.</s>
<s slug="what-is-an-ai-agent" type="golden_web">AI agents are autonomous software systems that leverage generative AI and foundation models to pursue goals, complete tasks, and handle complex workflows through reasoning, planning, memory, and adaptation. They process multimodal inputs and can collaborate with other agents. Key concepts include the ReAct Framework for reasoning and acting, plus evolved capabilities: reasoning via logic and inference; acting on decisions through digital or physical steps; observing via perception, NLP, or sensors.</s>
<s slug="kQxr-uOxw2o" type="golden_youtube">Most "agents" are API calls to an LLM that reply to users without independent action or decisions. The video distinguishes these from Anthropic's definition in "Building effective agents": workflows are systems where LLMs and tools are orchestrated through predefined code paths, while agents are systems where LLMs dynamically direct their own processes and tool usage. Workflows include LLM call routers that select among tools or prompts, orchestrators that assign subtasks to specialized models, parallel execution, memory retrieval, and iteration via multiple LLM calls.</s>
<s slug="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org" type="exploitation">The source is a Google Cloud promotional compilation of 1,302 real-world generative AI deployments across industries, emphasizing the transition to agentic systems. Main topic is production deployment of specialized agents that autonomously orchestrate multi-step workflows, replacing passive assistants; key concepts include agentic teams, natural-language interfaces over legacy systems, multimodal physical-world digitization, and Security Command Center-style agentic auto-remediation.</s>
<s slug="LCEmiRjPEtQ" type="exploitation">Karpathy's talk frames software evolution as three paradigms—Software 1.0, Software 2.0, and Software 3.0—with LLMs now eating prior stacks. LLMs are positioned as utilities and early operating systems circa 1960s time-sharing: LLM as CPU, context window as RAM, tool use and embeddings as file system. Opportunities center on partial-autonomy LLM apps rather than full agents: Cursor and Perplexity package state, orchestrate embedding/chat/diff models, supply application-specific GUIs for verification, and expose an autonomy slider.</s>
<s slug="TRjq7t2Ms5I" type="exploitation">Jerry Liu's talk at the AI Engineer Summit details production-ready RAG systems built with LlamaIndex, contrasting retrieval augmentation against fine-tuning. The core RAG stack comprises data ingestion plus querying with retrieval and synthesis. Evaluation requires benchmarks before optimization: isolated retrieval metrics and end-to-end metrics on generated responses using label-free or with-label LLM evaluators on full pipelines.</s>
<s slug="gemini-cli-your-open-source-ai-agent" type="exploitation">Gemini CLI is an open-source AI agent that embeds Gemini models directly into the developer terminal for coding, file manipulation, command execution, dynamic troubleshooting, content generation, problem-solving, deep research, and task management. Key concepts include agent capabilities such as multi-step planning, auto-recovery from failed paths, and relentless execution on behalf of the user, contrasted implicitly with simpler single-turn command-response patterns.</s>
<s slug="google-gemini_gemini-cli" type="exploitation">Gemini CLI is an open-source terminal-based AI agent that provides direct access to Gemini models for code understanding, generation, automation, and task execution. It is positioned as an agentic tool with built-in capabilities for file operations, shell commands, web fetching, and real-time grounding via Google Search, alongside extensibility through MCP servers for custom integrations.</s>
<s slug="introducing-chatgpt-agent-bridging-research-and-action" type="exploitation">ChatGPT agent unifies Operator’s web interaction capabilities with deep research’s synthesis strengths inside a single conversational model that operates on its own virtual computer. The agent fluidly switches among a visual browser, a text-based browser, a terminal for code execution and file manipulation, direct API calls, and ChatGPT connectors for Gmail and GitHub.</s>
<s slug="introducing-perplexity-deep-research" type="exploitation">Perplexity Deep Research is an autonomous research mode launched on February 14, 2025, that conducts multi-step web searches, document analysis, and iterative reasoning to produce synthesized reports. It extends Perplexity’s core question-answering system by running 2–4 minutes of agent-style loops that refine a research plan after each search and read step, then generate a final report exportable as PDF, document, or Perplexity Page.</s>
<s slug="stop-building-ai-agents-here-s-what-you-should-build-instead" type="exploitation">The source examines why most LLM-powered applications should prioritize structured workflows over autonomous agents. It defines an agent via four characteristics—memory, information retrieval via RAG, tool usage, and workflow control—then argues that handing over the final control step usually adds brittleness unless tasks are highly dynamic and unstable. The source contrasts this with five explicit workflow patterns.</s>
</sources>

<tavily_yield_per_section>
| section_id | helping_rounds | unique_facts | duplicate_facts |
|---|---|---|---|
| S1::section-1-introduction-the-critical-decision-every-ai-engineer-faces | 3 | 8 | 0 |
| S2::section-2-understanding-the-spectrum-from-workflows-to-agents | 3 | 8 | 0 |
| S3::section-3-choosing-your-path | 3 | 7 | 0 |
| S4::section-4-exploring-common-patterns | 4 | 7 | 0 |
| S5::section-5-zooming-in-on-our-favorite-examples | 1 | 6 | 0 |
| S6::section-6-conclusion-the-challenges-of-every-ai-engineer | 1 | 6 | 0 |
tavily_saturation=1.0
</tavily_yield_per_section>

<section_coverage>
<section id="S1::section-1-introduction-the-critical-decision-every-ai-engineer-faces" self_contained="yes" sources="what-is-an-ai-agent,a-developer-s-guide-to-building-scalable-ai-workflows-vs-age,kQxr-uOxw2o" artefacts="">
  <intent>This section introduces the core architectural decision between workflows and agents that every AI engineer must make early in building applications, establishing why the choice matters for success or failure.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age"/>
    <item name="theoretical_foundations" present="yes" evidence="building-effective-agents"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="limitations_failure_modes" present="yes" evidence="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age"/>
    <item name="implementation_tradeoffs" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="case_studies_metrics" present="yes" evidence="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="5">
    <item name="adjacent_concepts" present="yes" evidence="LCEmiRjPEtQ"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="enabling_technologies" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="industry_applications" present="yes" evidence="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age"/>
    <item name="adjacent_trends" present="yes" evidence="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org"/>
  </breadth_checklist>
  <orphan_anchors n_depth="3" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Begin with a personal story: &quot;As an AI engineer preparing to build your first real AI application, after narrowing down" bullet="motivation">Personal narrative directly supports the motivation checklist item for why the decision matters.</orphan>
    <orphan route="depth" anchor="The Problem: When building AI applications, engineers face a critical architectural decision early in their development" bullet="motivation">Explicitly frames the core problem driving the section.</orphan>
    <orphan route="depth" anchor="Why This Decision Matters: Choose the wrong approach and you might end up with:" bullet="limitations_failure_modes">Lists concrete failure consequences that fit limitations item.</orphan>
  </orphan_anchors>
</section>

<section id="S2::section-2-understanding-the-spectrum-from-workflows-to-agents" self_contained="yes" sources="building-effective-agents,stop-building-ai-agents-here-s-what-you-should-build-instead,LCEmiRjPEtQ" artefacts="">
  <intent>This section defines the core properties of LLM workflows and AI agents at a conceptual level and explains the shared role of orchestration.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="building-effective-agents"/>
    <item name="theoretical_foundations" present="yes" evidence="stop-building-ai-agents-here-s-what-you-should-build-instead"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="LCEmiRjPEtQ"/>
    <item name="limitations_failure_modes" present="yes" evidence="building-effective-agents"/>
    <item name="implementation_tradeoffs" present="yes" evidence="stop-building-ai-agents-here-s-what-you-should-build-instead"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="5">
    <item name="adjacent_concepts" present="yes" evidence="building-effective-agents"/>
    <item name="cross_domain_analogies" present="yes" evidence="stop-building-ai-agents-here-s-what-you-should-build-instead"/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="LCEmiRjPEtQ"/>
    <item name="industry_applications" present="yes" evidence="building-effective-agents"/>
    <item name="adjacent_trends" present="yes" evidence="LCEmiRjPEtQ"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="On LLM workflows we care about:" bullet="theoretical_foundations">Directly supplies definition and characteristics for the theoretical foundations item.</orphan>
    <orphan route="breadth" anchor="Analogy: A factory assembly line." bullet="cross_domain_analogies">Provides explicit cross-domain analogy requested by the breadth checklist.</orphan>
  </orphan_anchors>
</section>

<section id="S3::section-3-choosing-your-path" self_contained="yes" sources="TRjq7t2Ms5I,exploring-the-difference-between-agents-and-workflows,introducing-chatgpt-agent-bridging-research-and-action" artefacts="">
  <intent>This section compares workflows and agents on the developer-defined versus LLM-driven autonomy axis and supplies decision guidance plus hybrid examples.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="theoretical_foundations" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="introducing-chatgpt-agent-bridging-research-and-action"/>
    <item name="limitations_failure_modes" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="implementation_tradeoffs" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="case_studies_metrics" present="yes" evidence="introducing-chatgpt-agent-bridging-research-and-action"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="4">
    <item name="adjacent_concepts" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="industry_applications" present="yes" evidence="introducing-chatgpt-agent-bridging-research-and-action"/>
    <item name="adjacent_trends" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
  </breadth_checklist>
  <orphan_anchors n_depth="2" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="When to use LLM workflows:" bullet="implementation_tradeoffs">Lists strengths, weaknesses and use-cases that map to tradeoffs item.</orphan>
    <orphan route="depth" anchor="Hybrid Approaches: Most real-world systems blend elements of both approaches." bullet="theoretical_foundations">Supports hybrid gradient discussion in foundations.</orphan>
  </orphan_anchors>
</section>

<section id="S4::section-4-exploring-common-patterns" self_contained="yes" sources="what-is-an-ai-agent,kQxr-uOxw2o,exploring-the-difference-between-agents-and-workflows" artefacts="">
  <intent>This section introduces the most common workflow and agent patterns to build reader intuition before deeper lessons.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="theoretical_foundations" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="limitations_failure_modes" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="implementation_tradeoffs" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="5">
    <item name="adjacent_concepts" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="cross_domain_analogies" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="industry_applications" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="adjacent_trends" present="yes" evidence="kQxr-uOxw2o"/>
  </breadth_checklist>
  <orphan_anchors n_depth="2" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="LLM workflows:" bullet="theoretical_foundations">Introduces chaining, routing and orchestrator-worker patterns for foundations.</orphan>
    <orphan route="depth" anchor="Core components of a ReAct AI agent:" bullet="implementation_tradeoffs">High-level ReAct description maps to tradeoffs discussion.</orphan>
  </orphan_anchors>
</section>

<section id="S5::section-5-zooming-in-on-our-favorite-examples" self_contained="yes" sources="gemini-cli-your-open-source-ai-agent,introducing-perplexity-deep-research,google-gemini_gemini-cli" artefacts="">
  <intent>This section grounds the concepts with concrete high-level examples ranging from simple workflow to hybrid agent system.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="gemini-cli-your-open-source-ai-agent"/>
    <item name="theoretical_foundations" present="yes" evidence="introducing-perplexity-deep-research"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="google-gemini_gemini-cli"/>
    <item name="limitations_failure_modes" present="yes" evidence="gemini-cli-your-open-source-ai-agent"/>
    <item name="implementation_tradeoffs" present="yes" evidence="introducing-perplexity-deep-research"/>
    <item name="case_studies_metrics" present="yes" evidence="google-gemini_gemini-cli"/>
    <item name="artefact_available" present="yes" evidence="A08"/>
  </depth_checklist>
  <breadth_checklist breadth_score="4">
    <item name="adjacent_concepts" present="yes" evidence="gemini-cli-your-open-source-ai-agent"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="google-gemini_gemini-cli"/>
    <item name="industry_applications" present="yes" evidence="introducing-perplexity-deep-research"/>
    <item name="adjacent_trends" present="yes" evidence="gemini-cli-your-open-source-ai-agent"/>
  </breadth_checklist>
  <orphan_anchors n_depth="2" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Document summarization and analysis workflow by Gemini in Google Workspace" bullet="case_studies_metrics">Provides concrete workflow case study matching metrics item.</orphan>
    <orphan route="depth" anchor="Gemini CLI coding assistant:" bullet="implementation_tradeoffs">Detailed high-level implementation supports tradeoffs discussion.</orphan>
  </orphan_anchors>
</section>

<section id="S6::section-6-conclusion-the-challenges-of-every-ai-engineer" self_contained="yes" sources="TRjq7t2Ms5I,601-real-world-gen-ai-use-cases-from-the-world-s-leading-org,building-effective-agents" artefacts="">
  <intent>This concluding section summarizes the real-world challenges AI engineers face and sets up future lessons on reliable hybrid systems.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="building-effective-agents"/>
    <item name="theoretical_foundations" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org"/>
    <item name="limitations_failure_modes" present="yes" evidence="building-effective-agents"/>
    <item name="implementation_tradeoffs" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="case_studies_metrics" present="yes" evidence="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="4">
    <item name="adjacent_concepts" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="building-effective-agents"/>
    <item name="industry_applications" present="yes" evidence="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org"/>
    <item name="adjacent_trends" present="yes" evidence="TRjq7t2Ms5I"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="The Reality of AI Engineering: Now that you understand the spectrum from LLM workflows to AI agents" bullet="motivation">Ties challenges back to spectrum understanding for motivation.</orphan>
    <orphan route="breadth" anchor="The Good News: These challenges are solvable." bullet="adjacent_trends">Points to future adjacent practices and trends.</orphan>
  </orphan_anchors>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction-the-critical-decision-every-ai-engineer-faces" need_depth="11" need_breadth="1" target_words="400" mandatory_bullets="5" must_cover_depth="0" must_stay_brief="2"/>
  <section id="S2::section-2-understanding-the-spectrum-from-workflows-to-agents" need_depth="6" need_breadth="4" target_words="500" mandatory_bullets="4" must_cover_depth="0" must_stay_brief="1"/>
  <section id="S3::section-3-choosing-your-path" need_depth="8" need_breadth="2" target_words="650" mandatory_bullets="7" must_cover_depth="0" must_stay_brief="0"/>
  <section id="S4::section-4-exploring-common-patterns" need_depth="9" need_breadth="1" target_words="700" mandatory_bullets="8" must_cover_depth="2" must_stay_brief="1"/>
  <section id="S5::section-5-zooming-in-on-our-favorite-examples" need_depth="7" need_breadth="2" target_words="1150" mandatory_bullets="6" must_cover_depth="0" must_stay_brief="0"/>
  <section id="S6::section-6-conclusion-the-challenges-of-every-ai-engineer" need_depth="5" need_breadth="5" target_words="450" mandatory_bullets="6" must_cover_depth="0" must_stay_brief="0"/>
  <overall>
    <weakest_sections>S6::section-6-conclusion-the-challenges-of-every-ai-engineer, S1::section-1-introduction-the-critical-decision-every-ai-engineer-faces</weakest_sections>
    <strongest_sections>S5::section-5-zooming-in-on-our-favorite-examples, S2::section-2-understanding-the-spectrum-from-workflows-to-agents</strongest_sections>
    <dominant_gap_type>depth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>