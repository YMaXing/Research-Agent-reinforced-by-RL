<digest_meta>
  <article_title>Workflows vs. Agents (minimal variant)</article_title>
  <total_sources>13</total_sources>
  <total_artefacts>18</total_artefacts>
  <tavily_saturation>1.0</tavily_saturation>
  <n_orphan_anchors>45</n_orphan_anchors>
  <n_content_sections>6</n_content_sections>
  <external_evidence_policy>forbidden</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
</artefact_registry>

<sources>
<s slug="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age" type="golden_web">The article contrasts workflows (structured LLM pipelines with explicit control flow) against agents (autonomous LLM-driven loops that select tools and decide next steps), drawing definitions from Anthropic’s “Building effective agents.” Workflows follow deterministic patterns such as classify → route → respond → log; agents use recursive reasoning loops for dynamic tool selection, self-correction, and adaptive state management.</s>
<s slug="building-effective-agents" type="golden_web">The source, Anthropic's "Building effective agents" (Dec 19, 2024), distinguishes workflows (LLMs and tools orchestrated via predefined code paths) from agents (LLMs that dynamically direct their own processes and tool use) within broader agentic systems. It advocates starting with the simplest LLM solution and escalating complexity only when needed, as agentic systems trade higher latency and cost for improved performance on suitable tasks.</s>
<s slug="exploring-the-difference-between-agents-and-workflows" type="golden_web">The source contrasts LLM-powered agents with traditional workflows in the context of Agentic RAG. Agents combine an LLM, tools, and memory to reason, retrieve, and act dynamically. The ReAct framework structures this as act (tool calls), observe (tool outputs), and reason (next decision). Workflows follow fixed, predefined sequences for reliability but lack adaptability.</s>
<s slug="what-is-an-ai-agent" type="golden_web">AI agents are software systems using generative AI foundation models for goal pursuit, reasoning, planning, memory, and autonomous decision-making, with multimodal processing of text, voice, video, code, and other inputs. They build on the ReAct Framework for reasoning and acting, with evolved capabilities including observing, collaborating, and self-refining via machine learning and optimization.</s>
<s slug="kQxr-uOxw2o" type="golden_youtube">Most "agents" are API calls to LLMs (OpenAI API examples) or hardcoded processes that reply to users without independent action. The video contrasts these with Anthropic's "Building effective agents" framing: workflows orchestrate LLMs and tools via predefined code paths, while agents dynamically direct their own processes and tool use.</s>
<s slug="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org" type="exploitation">The source is a Google Cloud compilation of 1,302 production generative AI deployments (updated April 2026 from the original 101), the majority using agentic patterns. It organizes cases by 11 industries and six agent types (Customer, Employee, Creative, Code, Data, Security), highlighting the shift from passive assistants to autonomous agents that orchestrate workflows across tools.</s>
<s slug="LCEmiRjPEtQ" type="exploitation">Karpathy's talk frames software evolution as three paradigms: Software 1.0 (explicit code programming computers), Software 2.0 (neural net weights, e.g., AlexNet ~2012, trained on 10k positive/negative examples for sentiment), and Software 3.0 (English prompts programming LLMs ~2019). Prompts are treated as programs; GitHub code increasingly mixes English with code.</s>
<s slug="TRjq7t2Ms5I" type="exploitation">The source is a transcript of Jerry Liu’s (LlamaIndex) AI Engineer Summit talk on production RAG. It contrasts simple retrieval-augmentation pipelines (fixed LLM + data pipeline for context) with fine-tuning, then details the standard RAG stack (data ingestion, vector-database retrieval, LLM synthesis) and its failure modes.</s>
<s slug="gemini-cli-your-open-source-ai-agent" type="exploitation">Gemini CLI is an open-source (Apache 2.0) AI agent that embeds Gemini models directly in the terminal for coding, content generation, problem-solving, research, task management, file manipulation, command execution, and dynamic troubleshooting.</s>
<s slug="google-gemini_gemini-cli" type="exploitation">Gemini CLI is an open-source terminal-based AI agent providing direct access to Gemini models for code understanding, generation, automation, and integration tasks. It positions the tool as supporting both interactive agent sessions and non-interactive scripted workflows via flags such as `--output-format json`.</s>
<s slug="introducing-chatgpt-agent-bridging-research-and-action" type="exploitation">ChatGPT agent unifies Operator’s GUI web interaction, deep research’s synthesis, and ChatGPT conversational ability into a single agentic system that operates on its own virtual computer. The model dynamically selects among a visual browser, text-based browser, terminal, direct API access, and ChatGPT connectors.</s>
<s slug="introducing-perplexity-deep-research" type="exploitation">Perplexity Deep Research is an autonomous research mode that performs iterative search, document reading, and reasoning to produce comprehensive reports on complex queries, taking 2-4 minutes per task. It uses built-in search and coding capabilities to refine a research plan dynamically before synthesizing findings into a final report.</s>
<s slug="stop-building-ai-agents-here-s-what-you-should-build-instead" type="exploitation">The source argues that LLM systems should prioritize structured workflows over agents in most cases, as agents introduce excessive complexity, poor debuggability, and frequent failures from uncontrolled workflow decisions. It defines an agent through four characteristics: Memory, Information Retrieval, Tool Usage, and Workflow Control.</s>
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
<section id="S1::section-1-introduction-the-critical-decision-every-ai-engineer-faces" self_contained="yes" sources="what-is-an-ai-agent,kQxr-uOxw2o,a-developer-s-guide-to-building-scalable-ai-workflows-vs-age" artefacts="">
  <intent>This section introduces the core architectural choice between workflows and agents that every AI engineer must make when starting an application.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age"/>
    <item name="theoretical_foundations" present="yes" evidence="building-effective-agents"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="limitations_failure_modes" present="yes" evidence="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age"/>
    <item name="implementation_tradeoffs" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="yes" evidence="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age"/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="8" n_breadth="3" n_unreachable="0">
    <orphan route="depth" anchor="Begin with a personal story: &quot;As an AI engineer preparing to build your first real AI application, after narrowing down" bullet="motivation">Core motivation for the lesson's opening decision point.</orphan>
    <orphan route="depth" anchor="The Problem: When building AI applications, engineers face a critical architectural decision early in their development" bullet="motivation">Directly states the central problem the section solves.</orphan>
    <orphan route="depth" anchor="Why This Decision Matters: Choose the wrong approach and you might end up with:" bullet="limitations_failure_modes">Lists concrete failure consequences of the architectural choice.</orphan>
    <orphan route="depth" anchor="An overly rigid system that breaks when users deviate from expected patterns or developers try to add new features" bullet="limitations_failure_modes">Specific workflow failure mode.</orphan>
    <orphan route="depth" anchor="An unpredictable agent that works brilliantly 80% of the time but fails catastrophically when it matters most" bullet="limitations_failure_modes">Specific agent failure mode.</orphan>
    <orphan route="depth" anchor="Months of development time wasted rebuilding the entire architecture" bullet="implementation_tradeoffs">Tradeoff consequence of poor choice.</orphan>
    <orphan route="depth" anchor="Frustrated users who can't rely on the AI application" bullet="limitations_failure_modes">Reliability impact on end users.</orphan>
    <orphan route="depth" anchor="Frustrated executives who cannot affort to keep the AI agent running as the costs are too high relative to the profits" bullet="implementation_tradeoffs">Cost-performance tradeoff.</orphan>
    <orphan route="breadth" anchor="Make a quick reference to the real-world where in 2024-2025 billion-dollar AI startups succeed or fail based primarily o" bullet="industry_applications">Connects decision to external industry outcomes.</orphan>
    <orphan route="breadth" anchor="Quick walkthrough of what we'll learn by the end of this lesson: Take the core ideas of what we'll learn in the lesson f" bullet="adjacent_concepts">Links to broader lesson structure outside core mechanism.</orphan>
    <orphan route="breadth" anchor="Must stay brief: Compress the personal story, specific failure modes, and real-world company examples." bullet="adjacent_concepts">Editorial constraint on scope.</orphan>
  </orphan_anchors>
</section>
<section id="S2::section-2-understanding-the-spectrum-from-workflows-to-agents" self_contained="yes" sources="building-effective-agents,stop-building-ai-agents-here-s-what-you-should-build-instead,LCEmiRjPEtQ" artefacts="">
  <intent>This section defines the core properties of workflows versus agents and their shared orchestration layer.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="building-effective-agents"/>
    <item name="theoretical_foundations" present="yes" evidence="building-effective-agents"/>
    <item name="technical_nuances" present="yes" evidence="stop-building-ai-agents-here-s-what-you-should-build-instead"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="stop-building-ai-agents-here-s-what-you-should-build-instead"/>
    <item name="implementation_tradeoffs" present="yes" evidence="building-effective-agents"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="LCEmiRjPEtQ"/>
    <item name="cross_domain_analogies" present="yes" evidence="building-effective-agents"/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="14" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="In this section we want to take a brief look at what LLM workflows and AI agents are. At this point we don't focus on th" bullet="motivation">Sets the definitional goal of the section.</orphan>
    <orphan route="depth" anchor="On LLM workflows we care about:" bullet="theoretical_foundations">Core workflow definition block.</orphan>
    <orphan route="depth" anchor="Definition: A sequence of tasks involving LLM calls or other operations such as reading/writing data to a database or fi" bullet="theoretical_foundations">Exact workflow definition.</orphan>
    <orphan route="depth" anchor="Characteristics: The steps are defined in advance, resulting in deterministic or rule-based paths with predictable execu" bullet="technical_nuances">Workflow determinism property.</orphan>
    <orphan route="depth" anchor="Analogy: A factory assembly line." bullet="cross_domain_analogies">Core analogy for workflows.</orphan>
    <orphan route="depth" anchor="Concepts we will learn in future lessons: chaining, routing, orchestrator-worker patterns" bullet="adjacent_concepts">Future concepts tied to this section's topic.</orphan>
    <orphan route="depth" anchor="Attach an image from the research with a simple LLM Workflow." bullet="technical_nuances">Visual support for workflow mechanism.</orphan>
    <orphan route="depth" anchor="On AI agents we care about:" bullet="theoretical_foundations">Core agent definition block.</orphan>
    <orphan route="depth" anchor="Definition: Systems where an LLM (or multiple LLMs) plays a central role in dynamically deciding (planning) the sequence" bullet="theoretical_foundations">Exact agent definition.</orphan>
    <orphan route="depth" anchor="Characteristics: Adaptive, capable of handling novelty, LLM-driven autonomy in decision-making and execution path." bullet="technical_nuances">Agent autonomy property.</orphan>
    <orphan route="depth" anchor="Analogy: A skilled human expert tackling an unfamiliar problem adapting on the moment after each &quot;Eurika&quot; moment" bullet="cross_domain_analogies">Core analogy for agents.</orphan>
    <orphan route="depth" anchor="Concepts we will learn in future lessons: tools, memory, and ReAct agents" bullet="adjacent_concepts">Future concepts tied to this section's topic.</orphan>
    <orphan route="depth" anchor="Attach an image from the research of how a simple Agentic System looks." bullet="technical_nuances">Visual support for agent mechanism.</orphan>
    <orphan route="depth" anchor="The Role of Orchestration: Explain that both workflows and agents require an orchestration layer, but their nature diffe" bullet="implementation_tradeoffs">Shared orchestration nuance.</orphan>
    <orphan route="breadth" anchor="Must stay brief: Condense definitions, characteristics, and analogies. Briefly mention future concepts without elaborati" bullet="adjacent_concepts">Editorial constraint.</orphan>
  </orphan_anchors>
</section>
<section id="S3::section-3-choosing-your-path" self_contained="yes" sources="TRjq7t2Ms5I,exploring-the-difference-between-agents-and-workflows,introducing-chatgpt-agent-bridging-research-and-action" artefacts="">
  <intent>This section compares developer-defined logic versus LLM-driven autonomy and provides decision criteria plus hybrid guidance.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="theoretical_foundations" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="technical_nuances" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="latest_advancements" present="yes" evidence="introducing-chatgpt-agent-bridging-research-and-action"/>
    <item name="limitations_failure_modes" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="implementation_tradeoffs" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="introducing-chatgpt-agent-bridging-research-and-action"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="14" n_breadth="4" n_unreachable="0">
    <orphan route="depth" anchor="In the previous section we defined the LLM workflows and AI agents independently, now we want to explore their core diff" bullet="motivation">Transitions to comparison of core mechanisms.</orphan>
    <orphan route="depth" anchor="Attach an image from the research showing the gradient between LLM workflows and AI agents." bullet="technical_nuances">Visual of spectrum between the two.</orphan>
    <orphan route="depth" anchor="When to use LLM workflows:" bullet="implementation_tradeoffs">Decision criteria for workflows.</orphan>
    <orphan route="depth" anchor="Examples where the structure is well-defined:" bullet="case_studies_metrics">Use-case examples supporting decision.</orphan>
    <orphan route="depth" anchor="Pipelines for data extraction and transformation from sources such as the web, messaging tools like Slack, video calls f" bullet="industry_applications">Concrete workflow examples.</orphan>
    <orphan route="depth" anchor="Automated report or emails generation from multiple data sources" bullet="industry_applications">Workflow example.</orphan>
    <orphan route="depth" anchor="Understanding project requirements and creating or updating tasks in Notion project management tools" bullet="industry_applications">Workflow example.</orphan>
    <orphan route="depth" anchor="Document summarization followed by translation" bullet="industry_applications">Workflow example.</orphan>
    <orphan route="depth" anchor="Repetitive daily tasks: Sending emails, posting social media updates, responding to messages" bullet="industry_applications">Workflow example.</orphan>
    <orphan route="depth" anchor="Content generation or repurposing, such as transforming articles into social media posts" bullet="industry_applications">Workflow example.</orphan>
    <orphan route="depth" anchor="Strengths: Predictability, reliability for well-defined tasks, easier debugging of fixed paths, potentially lower operat" bullet="implementation_tradeoffs">Workflow strengths.</orphan>
    <orphan route="depth" anchor="Weaknesses: Potentially more development time required as each step is manually engineered. The user experience is rigid" bullet="limitations_failure_modes">Workflow weaknesses.</orphan>
    <orphan route="depth" anchor="Usually preferred in enterprises or regulated fiels as they require predictable programs that work all the time. For exa" bullet="industry_applications">Enterprise preference rationale.</orphan>
    <orphan route="depth" anchor="Ideal for MVPs requiring rapid deployment by hardcoding features" bullet="implementation_tradeoffs">MVP tradeoff.</orphan>
    <orphan route="breadth" anchor="When to use AI agents:" bullet="adjacent_concepts">Complementary decision criteria.</orphan>
    <orphan route="breadth" anchor="Examples: " bullet="adjacent_concepts">Agent use-case examples.</orphan>
    <orphan route="breadth" anchor="Open-ended research and synthesis (e.g., researching about WW2)" bullet="adjacent_concepts">Agent example outside core workflow focus.</orphan>
    <orphan route="breadth" anchor="Dynamic problem-solving (e.g., debugging code, complex customer support)" bullet="adjacent_concepts">Agent example.</orphan>
  </orphan_anchors>
</section>
<section id="S4::section-4-exploring-common-patterns" self_contained="yes" sources="what-is-an-ai-agent,kQxr-uOxw2o,exploring-the-difference-between-agents-and-workflows" artefacts="">
  <intent>This section introduces the most common workflow and agent patterns at an intuitive level for first-time readers.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="theoretical_foundations" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="technical_nuances" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="implementation_tradeoffs" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="1">
    <item name="adjacent_concepts" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S5::section-5-zooming-in-on-our-favorite-examples" self_contained="yes" sources="gemini-cli-your-open-source-ai-agent,introducing-perplexity-deep-research,google-gemini_gemini-cli" artefacts="">
  <intent>This section grounds the spectrum with concrete workflow, agent, and hybrid examples.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="gemini-cli-your-open-source-ai-agent"/>
    <item name="theoretical_foundations" present="yes" evidence="introducing-perplexity-deep-research"/>
    <item name="technical_nuances" present="yes" evidence="google-gemini_gemini-cli"/>
    <item name="latest_advancements" present="yes" evidence="gemini-cli-your-open-source-ai-agent"/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="introducing-perplexity-deep-research"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="google-gemini_gemini-cli"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="yes" evidence="gemini-cli-your-open-source-ai-agent"/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
<section id="S6::section-6-conclusion-the-challenges-of-every-ai-engineer" self_contained="yes" sources="TRjq7t2Ms5I,601-real-world-gen-ai-use-cases-from-the-world-s-leading-org,building-effective-agents" artefacts="">
  <intent>This section summarizes the practical challenges engineers face and points to future lessons.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="building-effective-agents"/>
    <item name="theoretical_foundations" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org"/>
    <item name="limitations_failure_modes" present="yes" evidence="building-effective-agents"/>
    <item name="implementation_tradeoffs" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction-the-critical-decision-every-ai-engineer-faces" need_depth="27" need_breadth="13" target_words="150" mandatory_bullets="6" must_cover_depth="0" must_stay_brief="1"/>
  <section id="S2::section-2-understanding-the-spectrum-from-workflows-to-agents" need_depth="45" need_breadth="7" target_words="200" mandatory_bullets="7" must_cover_depth="0" must_stay_brief="1"/>
  <section id="S3::section-3-choosing-your-path" need_depth="44" need_breadth="16" target_words="250" mandatory_bullets="8" must_cover_depth="0" must_stay_brief="1"/>
  <section id="S4::section-4-exploring-common-patterns" need_depth="3" need_breadth="5" target_words="250" mandatory_bullets="6" must_cover_depth="0" must_stay_brief="1"/>
  <section id="S5::section-5-zooming-in-on-our-favorite-examples" need_depth="3" need_breadth="4" target_words="300" mandatory_bullets="9" must_cover_depth="0" must_stay_brief="1"/>
  <section id="S6::section-6-conclusion-the-challenges-of-every-ai-engineer" need_depth="3" need_breadth="4" target_words="150" mandatory_bullets="5" must_cover_depth="0" must_stay_brief="1"/>
  <overall>
    <weakest_sections>S2::section-2-understanding-the-spectrum-from-workflows-to-agents, S3::section-3-choosing-your-path</weakest_sections>
    <strongest_sections>S5::section-5-zooming-in-on-our-favorite-examples, S6::section-6-conclusion-the-challenges-of-every-ai-engineer</strongest_sections>
    <dominant_gap_type>depth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>