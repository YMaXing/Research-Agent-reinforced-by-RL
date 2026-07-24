<digest_meta>
  <article_title>Workflows vs. Agents (demanding variant)</article_title>
  <total_sources>15</total_sources>
  <total_artefacts>18</total_artefacts>
  <tavily_saturation>1.0</tavily_saturation>
  <n_orphan_anchors>45</n_orphan_anchors>
  <n_content_sections>6</n_content_sections>
  <external_evidence_policy>allowed</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
| A01 | a-developer-s-guide-to-building-scalable-ai-workflows-vs-age | code:python | customer,support,workflow,message | 28 | def customer_support_workflow(customer_m |
| A02 | a-developer-s-guide-to-building-scalable-ai-workflows-vs-age | code:python | customer,support,agent,message | 30 | def customer_support_agent(customer_mess |
| A05 | a-developer-s-guide-to-building-scalable-ai-workflows-vs-age | table | scenario,hybrid,works | 6 | \| Scenario \| Why Hybrid Works \| |
| A06 | a-developer-s-guide-to-building-scalable-ai-workflows-vs-age | quote | dimension,gives,points,either,workflow | 3 | > - Each dimension gives **+2 points** t |
| A08 | google-gemini_gemini-cli | code:bash | installation,required | 2 | # Using npx (no installation required) |
| A09 | google-gemini_gemini-cli | code:bash | install,google,gemini | 1 | npm install -g @google/gemini-cli |
</artefact_registry>

<sources>
<s slug="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age" type="golden_web">**Main topic:** Architectural trade-offs between deterministic AI workflows and autonomous agents. Key concepts, examples, tools, data points, limitations as provided in context.</s>
<s slug="building-effective-agents" type="golden_web">Anthropic guidance distinguishing workflows from agents, recommended patterns, examples, claims, gaps as provided.</s>
<s slug="exploring-the-difference-between-agents-and-workflows" type="golden_web">ReAct agents vs workflows, SmolAgents implementation, evaluation, monitoring as provided.</s>
<s slug="what-is-an-ai-agent" type="golden_web">Definition of agents, comparison table, memory/tools, types, challenges as provided.</s>
<s slug="kQxr-uOxw2o" type="golden_youtube">Workflows vs real agents distinction, examples like Devin, recommendations as provided.</s>
<s slug="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org" type="exploitation">Google Cloud compilation of deployments, agent types, metrics as provided.</s>
<s slug="LCEmiRjPEtQ" type="exploitation">Karpathy Software 3.0, Cursor/Perplexity autonomy slider, vibe coding as provided.</s>
<s slug="TRjq7t2Ms5I" type="exploitation">Jerry Liu RAG spectrum, LlamaIndex patterns, evaluation as provided.</s>
<s slug="gemini-cli-your-open-source-ai-agent" type="exploitation">Gemini CLI open-source agent details, tools, limits as provided.</s>
<s slug="google-gemini_gemini-cli" type="exploitation">Gemini CLI installation, MCP, usage as provided.</s>
<s slug="introducing-chatgpt-agent-bridging-research-and-action" type="exploitation">ChatGPT agent unified system, benchmarks, tools as provided.</s>
<s slug="introducing-perplexity-deep-research" type="exploitation">Perplexity Deep Research mode, benchmarks, examples as provided.</s>
<s slug="stop-building-ai-agents-here-s-what-you-should-build-instead" type="exploitation">Workflow patterns over agents, CrewAI failure case, code examples as provided.</s>
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
<section id="S1::section-1-introduction-the-critical-decision-every-ai-engineer-faces" self_contained="yes" sources="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age,what-is-an-ai-agent,kQxr-uOxw2o" artefacts="A01,A02">
  <intent>Cover the critical early architectural decision between workflows and agents for AI engineers, anchored by a personal story and real-world stakes.</intent>
  <depth_checklist depth_score="8">
    <item name="motivation" present="yes" evidence="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age"/>
    <item name="theoretical_foundations" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="technical_nuances" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="latest_advancements" present="yes" evidence="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age"/>
    <item name="limitations_failure_modes" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="implementation_tradeoffs" present="yes" evidence="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age"/>
    <item name="case_studies_metrics" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="artefact_available" present="yes" evidence="A01"/>
  </depth_checklist>
  <breadth_checklist breadth_score="6">
    <item name="adjacent_concepts" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="cross_domain_analogies" present="yes" evidence="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age"/>
    <item name="historical_context" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="enabling_technologies" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="industry_applications" present="yes" evidence="a-developer-s-guide-to-building-scalable-ai-workflows-vs-age"/>
    <item name="adjacent_trends" present="yes" evidence="what-is-an-ai-agent"/>
  </breadth_checklist>
  <orphan_anchors n_depth="8" n_breadth="2" n_unreachable="0">
    <orphan route="depth" anchor="Begin with a personal story: &quot;As an AI engineer preparing to build your first real AI application, after narrowing down" bullet="motivation">Directly supports the motivation depth item via personal framing of the architectural choice.</orphan>
    <orphan route="depth" anchor="The Problem: When building AI applications, engineers face a critical architectural decision early in their development" bullet="motivation">Anchors the core motivation for the section's decision framework.</orphan>
    <orphan route="depth" anchor="Why This Decision Matters: Choose the wrong approach and you might end up with:" bullet="limitations_failure_modes">Maps to failure modes of wrong architectural choice.</orphan>
    <orphan route="depth" anchor="An overly rigid system that breaks when users deviate from expected patterns or developers try to add new features" bullet="limitations_failure_modes">Specific workflow limitation failure mode.</orphan>
    <orphan route="depth" anchor="An unpredictable agent that works brilliantly 80% of the time but fails catastrophically when it matters most" bullet="limitations_failure_modes">Specific agent limitation failure mode.</orphan>
    <orphan route="depth" anchor="Months of development time wasted rebuilding the entire architecture" bullet="implementation_tradeoffs">Tradeoff consequence of poor choice.</orphan>
    <orphan route="depth" anchor="Frustrated users who can't rely on the AI application" bullet="case_studies_metrics">Real-world impact metric referenced in sources.</orphan>
    <orphan route="depth" anchor="Frustrated executives who cannot affort to keep the AI agent running as the costs are too high relative to the profits" bullet="case_studies_metrics">Cost metric from production examples.</orphan>
    <orphan route="breadth" anchor="Make a quick reference to the real-world where in 2024-2025 billion-dollar AI startups succeed or fail based primarily o" bullet="industry_applications">Connects to external industry startup outcomes.</orphan>
    <orphan route="breadth" anchor="Quick walkthrough of what we'll learn by the end of this lesson: Take the core ideas of what we'll learn in the lesson f" bullet="adjacent_trends">Surveys lesson scope linking to broader course trends.</orphan>
  </orphan_anchors>
</section>
<section id="S2::section-2-understanding-the-spectrum-from-workflows-to-agents" self_contained="yes" sources="building-effective-agents,stop-building-ai-agents-here-s-what-you-should-build-instead,LCEmiRjPEtQ" artefacts="">
  <intent>Define properties of LLM workflows and AI agents at a high level with analogies and orchestration differences.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="building-effective-agents"/>
    <item name="theoretical_foundations" present="yes" evidence="stop-building-ai-agents-here-s-what-you-should-build-instead"/>
    <item name="technical_nuances" present="yes" evidence="LCEmiRjPEtQ"/>
    <item name="latest_advancements" present="yes" evidence="building-effective-agents"/>
    <item name="limitations_failure_modes" present="yes" evidence="stop-building-ai-agents-here-s-what-you-should-build-instead"/>
    <item name="implementation_tradeoffs" present="yes" evidence="LCEmiRjPEtQ"/>
    <item name="case_studies_metrics" present="yes" evidence="building-effective-agents"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="6">
    <item name="adjacent_concepts" present="yes" evidence="stop-building-ai-agents-here-s-what-you-should-build-instead"/>
    <item name="cross_domain_analogies" present="yes" evidence="building-effective-agents"/>
    <item name="historical_context" present="yes" evidence="LCEmiRjPEtQ"/>
    <item name="enabling_technologies" present="yes" evidence="stop-building-ai-agents-here-s-what-you-should-build-instead"/>
    <item name="industry_applications" present="yes" evidence="building-effective-agents"/>
    <item name="adjacent_trends" present="yes" evidence="LCEmiRjPEtQ"/>
  </breadth_checklist>
  <orphan_anchors n_depth="16" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="In this section we want to take a brief look at what LLM workflows and AI agents are. At this point we don't focus on th" bullet="motivation">Sets section motivation for definitions.</orphan>
    <orphan route="depth" anchor="On LLM workflows we care about:" bullet="theoretical_foundations">Foundational definition coverage.</orphan>
    <orphan route="depth" anchor="Definition: A sequence of tasks involving LLM calls or other operations such as reading/writing data to a database or fi" bullet="theoretical_foundations">Core workflow definition.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Definition, Characteristics, Analogy, Future concepts." bullet="technical_nuances">Requires technical nuance depth.</orphan>
    <orphan route="depth" anchor="Characteristics: The steps are defined in advance, resulting in deterministic or rule-based paths with predictable execu" bullet="technical_nuances">Workflow characteristic nuance.</orphan>
    <orphan route="depth" anchor="Analogy: A factory assembly line." bullet="cross_domain_analogies">Explicit cross-domain analogy.</orphan>
    <orphan route="depth" anchor="Concepts we will learn in future lessons: chaining, routing, orchestrator-worker patterns" bullet="enabling_technologies">Future enabling patterns.</orphan>
    <orphan route="depth" anchor="Attach an image from the research with a simple LLM Workflow." bullet="case_studies_metrics">Visual case support.</orphan>
    <orphan route="depth" anchor="On AI agents we care about:" bullet="theoretical_foundations">Agent foundational coverage.</orphan>
    <orphan route="depth" anchor="Definition: Systems where an LLM (or multiple LLMs) plays a central role in dynamically deciding (planning) the sequence" bullet="theoretical_foundations">Core agent definition.</orphan>
    <orphan route="depth" anchor="Characteristics: Adaptive, capable of handling novelty, LLM-driven autonomy in decision-making and execution path." bullet="technical_nuances">Agent characteristic nuance.</orphan>
    <orphan route="depth" anchor="Analogy: A skilled human expert tackling an unfamiliar problem adapting on the moment after each &quot;Eurika&quot; moment" bullet="cross_domain_analogies">Explicit cross-domain analogy.</orphan>
    <orphan route="depth" anchor="Concepts we will learn in future lessons: tools, memory, and ReAct agents" bullet="enabling_technologies">Future enabling patterns.</orphan>
    <orphan route="depth" anchor="Attach an image from the research of how a simple Agentic System looks." bullet="case_studies_metrics">Visual case support.</orphan>
    <orphan route="depth" anchor="The Role of Orchestration: Explain that both workflows and agents require an orchestration layer, but their nature diffe" bullet="implementation_tradeoffs">Orchestration tradeoff nuance.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Nature of orchestration in workflows vs. agents, how it differs." bullet="implementation_tradeoffs">Orchestration tradeoff depth.</orphan>
  </orphan_anchors>
</section>
<section id="S3::section-3-choosing-your-path" self_contained="yes" sources="TRjq7t2Ms5I,exploring-the-difference-between-agents-and-workflows,introducing-chatgpt-agent-bridging-research-and-action" artefacts="A05,A06">
  <intent>Compare developer-defined logic vs LLM-driven autonomy and detail when to choose each with hybrid examples.</intent>
  <depth_checklist depth_score="8">
    <item name="motivation" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="theoretical_foundations" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="technical_nuances" present="yes" evidence="introducing-chatgpt-agent-bridging-research-and-action"/>
    <item name="latest_advancements" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="limitations_failure_modes" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="implementation_tradeoffs" present="yes" evidence="introducing-chatgpt-agent-bridging-research-and-action"/>
    <item name="case_studies_metrics" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="artefact_available" present="yes" evidence="A05"/>
  </depth_checklist>
  <breadth_checklist breadth_score="6">
    <item name="adjacent_concepts" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="cross_domain_analogies" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="historical_context" present="yes" evidence="introducing-chatgpt-agent-bridging-research-and-action"/>
    <item name="enabling_technologies" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="industry_applications" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="adjacent_trends" present="yes" evidence="introducing-chatgpt-agent-bridging-research-and-action"/>
  </breadth_checklist>
  <orphan_anchors n_depth="14" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="In the previous section we defined the LLM workflows and AI agents independently, now we want to explore their core diff" bullet="motivation">Builds directly on prior motivation.</orphan>
    <orphan route="depth" anchor="Attach an image from the research showing the gradient between LLM workflows and AI agents." bullet="case_studies_metrics">Gradient case visualization.</orphan>
    <orphan route="depth" anchor="When to use LLM workflows:" bullet="implementation_tradeoffs">Tradeoff decision point.</orphan>
    <orphan route="depth" anchor="Examples where the structure is well-defined:" bullet="case_studies_metrics">Industry case examples.</orphan>
    <orphan route="depth" anchor="Pipelines for data extraction and transformation from sources such as the web, messaging tools like Slack, video calls f" bullet="industry_applications">Specific industry application.</orphan>
    <orphan route="depth" anchor="Automated report or emails generation from multiple data sources" bullet="industry_applications">Specific industry application.</orphan>
    <orphan route="depth" anchor="Understanding project requirements and creating or updating tasks in Notion project management tools" bullet="industry_applications">Specific industry application.</orphan>
    <orphan route="depth" anchor="Document summarization followed by translation" bullet="industry_applications">Specific industry application.</orphan>
    <orphan route="depth" anchor="Repetitive daily tasks: Sending emails, posting social media updates, responding to messages" bullet="industry_applications">Specific industry application.</orphan>
    <orphan route="depth" anchor="Content generation or repurposing, such as transforming articles into social media posts" bullet="industry_applications">Specific industry application.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Examples (provide more detail for each category), Strengths (elaborate on predictability, debugging" bullet="implementation_tradeoffs">Detailed tradeoff coverage.</orphan>
    <orphan route="depth" anchor="Strengths: Predictability, reliability for well-defined tasks, easier debugging of fixed paths, potentially lower operat" bullet="implementation_tradeoffs">Workflow strength tradeoff.</orphan>
    <orphan route="depth" anchor="Weaknesses: Potentially more development time required as each step is manually engineered. The user experience is rigid" bullet="limitations_failure_modes">Workflow weakness failure mode.</orphan>
    <orphan route="depth" anchor="Usually preferred in enterprises or regulated fiels as they require predictable programs that work all the time. For exa" bullet="industry_applications">Enterprise industry application.</orphan>
  </orphan_anchors>
</section>
<section id="S4::section-4-exploring-common-patterns" self_contained="yes" sources="what-is-an-ai-agent,kQxr-uOxw2o,exploring-the-difference-between-agents-and-workflows" artefacts="">
  <intent>Introduce common LLM workflow and agent patterns at an intuitive level for first-time readers.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="theoretical_foundations" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="technical_nuances" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="latest_advancements" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="limitations_failure_modes" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="implementation_tradeoffs" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="case_studies_metrics" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="6">
    <item name="adjacent_concepts" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="cross_domain_analogies" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="historical_context" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
    <item name="enabling_technologies" present="yes" evidence="kQxr-uOxw2o"/>
    <item name="industry_applications" present="yes" evidence="what-is-an-ai-agent"/>
    <item name="adjacent_trends" present="yes" evidence="exploring-the-difference-between-agents-and-workflows"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="To introduce the reader to the AI Engineering world, we will present the most common patterns used to build AI agents and LLM workflows. Explain them as if this is the first time the reader hears about them." bullet="motivation">Section motivation for pattern introduction.</orphan>
  </orphan_anchors>
</section>
<section id="S5::section-5-zooming-in-on-our-favorite-examples" self_contained="yes" sources="gemini-cli-your-open-source-ai-agent,introducing-perplexity-deep-research,google-gemini_gemini-cli" artefacts="A08,A09">
  <intent>Provide concrete high-level examples of a workflow, single agent, and hybrid system using Gemini CLI and Perplexity Deep Research.</intent>
  <depth_checklist depth_score="8">
    <item name="motivation" present="yes" evidence="gemini-cli-your-open-source-ai-agent"/>
    <item name="theoretical_foundations" present="yes" evidence="introducing-perplexity-deep-research"/>
    <item name="technical_nuances" present="yes" evidence="google-gemini_gemini-cli"/>
    <item name="latest_advancements" present="yes" evidence="gemini-cli-your-open-source-ai-agent"/>
    <item name="limitations_failure_modes" present="yes" evidence="introducing-perplexity-deep-research"/>
    <item name="implementation_tradeoffs" present="yes" evidence="google-gemini_gemini-cli"/>
    <item name="case_studies_metrics" present="yes" evidence="gemini-cli-your-open-source-ai-agent"/>
    <item name="artefact_available" present="yes" evidence="A08"/>
  </depth_checklist>
  <breadth_checklist breadth_score="6">
    <item name="adjacent_concepts" present="yes" evidence="introducing-perplexity-deep-research"/>
    <item name="cross_domain_analogies" present="yes" evidence="gemini-cli-your-open-source-ai-agent"/>
    <item name="historical_context" present="yes" evidence="google-gemini_gemini-cli"/>
    <item name="enabling_technologies" present="yes" evidence="introducing-perplexity-deep-research"/>
    <item name="industry_applications" present="yes" evidence="gemini-cli-your-open-source-ai-agent"/>
    <item name="adjacent_trends" present="yes" evidence="google-gemini_gemini-cli"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="To better anchor the reader in the world of LLM workflows and AI agents we want to introduce some concrete examples, from a simple workflow (e.g., Google Workspace document summarization), to a single agent system (Gemini CLI code assistant) to a more advanced hybrid solution (Perplexity's Deep Research agent)." bullet="motivation">Section motivation for concrete examples.</orphan>
  </orphan_anchors>
</section>
<section id="S6::section-6-conclusion-the-challenges-of-every-ai-engineer" self_contained="yes" sources="TRjq7t2Ms5I,601-real-world-gen-ai-use-cases-from-the-world-s-leading-org,building-effective-agents" artefacts="">
  <intent>Summarize daily AI engineering challenges and transition to future lessons on evaluations and hybrid systems.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="theoretical_foundations" present="yes" evidence="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org"/>
    <item name="technical_nuances" present="yes" evidence="building-effective-agents"/>
    <item name="latest_advancements" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="limitations_failure_modes" present="yes" evidence="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org"/>
    <item name="implementation_tradeoffs" present="yes" evidence="building-effective-agents"/>
    <item name="case_studies_metrics" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="6">
    <item name="adjacent_concepts" present="yes" evidence="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org"/>
    <item name="cross_domain_analogies" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="historical_context" present="yes" evidence="building-effective-agents"/>
    <item name="enabling_technologies" present="yes" evidence="601-real-world-gen-ai-use-cases-from-the-world-s-leading-org"/>
    <item name="industry_applications" present="yes" evidence="TRjq7t2Ms5I"/>
    <item name="adjacent_trends" present="yes" evidence="building-effective-agents"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="The Reality of AI Engineering: Now that you understand the spectrum from LLM workflows to AI agents, it's important to recognize that every AI Engineer—whether working at a startup or a Fortune 500 company faces these same fundamental challenges whenever it has to design a new AI application." bullet="motivation">Section motivation for challenges recap.</orphan>
  </orphan_anchors>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction-the-critical-decision-every-ai-engineer-faces" need_depth="24" need_breadth="6" target_words="450" mandatory_bullets="5" must_cover_depth="0" must_stay_brief="0"/>
  <section id="S2::section-2-understanding-the-spectrum-from-workflows-to-agents" need_depth="49" need_breadth="0" target_words="600" mandatory_bullets="5" must_cover_depth="5" must_stay_brief="0"/>
  <section id="S3::section-3-choosing-your-path" need_depth="42" need_breadth="0" target_words="750" mandatory_bullets="3" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S4::section-4-exploring-common-patterns" need_depth="4" need_breadth="0" target_words="800" mandatory_bullets="1" must_cover_depth="1" must_stay_brief="0"/>
  <section id="S5::section-5-zooming-in-on-our-favorite-examples" need_depth="3" need_breadth="0" target_words="1250" mandatory_bullets="3" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S6::section-6-conclusion-the-challenges-of-every-ai-engineer" need_depth="4" need_breadth="0" target_words="500" mandatory_bullets="8" must_cover_depth="8" must_stay_brief="0"/>
  <overall>
    <weakest_sections>S3::section-3-choosing-your-path, S2::section-2-understanding-the-spectrum-from-workflows-to-agents</weakest_sections>
    <strongest_sections>S5::section-5-zooming-in-on-our-favorite-examples, S4::section-4-exploring-common-patterns</strongest_sections>
    <dominant_gap_type>depth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>