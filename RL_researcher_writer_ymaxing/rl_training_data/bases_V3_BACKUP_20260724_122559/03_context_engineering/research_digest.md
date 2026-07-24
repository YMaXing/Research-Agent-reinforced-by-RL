<digest_meta>
  <article_title>Context Engineering</article_title>
  <total_sources>10</total_sources>
  <total_artefacts>20</total_artefacts>
  <tavily_saturation>1.0</tavily_saturation>
  <n_orphan_anchors>42</n_orphan_anchors>
  <n_content_sections>8</n_content_sections>
  <external_evidence_policy>forbidden</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
| A01 | a-survey-of-context-engineering-for-large-language-models | table | dimension,prompt,engineering,context | 9 | \| Dimension \| Prompt Engineering \| Conte |
| A19 | humanlayer_12-factor-agents | code:xml | slack,message | 5 | <slack_message> |
</artefact_registry>

<sources>
<s slug="a-survey-of-context-engineering-for-large-language-models" type="golden_web">Context Engineering is a formal discipline optimizing dynamic, structured information payloads for LLMs during inference. Defines context C = A(c1,…,cn) assembling components such as cinstr, cknow, ctools, cmem, cstate, cquery. Frames task as maximizing expected reward under length constraints. Covers foundational components: retrieval/generation, processing, management. Techniques include CLEAR, CoT, ToT, GoT, RAG variants, long-context models, self-refinement, memory architectures, compression. Benchmarks show gains like MultiArith 17.7%→78.7%, Game of 24 4%→74%. Limitations: lost-in-the-middle, quadratic costs, context collapse.</s>
<s slug="context-engineering-a-guide-with-examples" type="golden_web">Context engineering designs systems that select, organize, and manage information in the context window. Contrasts with prompt engineering. Techniques: RAG, dynamic tool use, multi-agent sharing. Applications: customer-service bots, AI coding assistants. Failures: context poisoning, distraction, confusion, clash with mitigations like validation, summarization, tool-loadout management, pruning. Notes million-token windows do not eliminate issues.</s>
<s slug="context-engineering-what-it-is-and-techniques-to-consider" type="golden_web">Context engineering curates and fills LLM context window with precisely the right information. Extends RAG. Context comprises system prompt, user input, short/long-term memory, retrieved knowledge, tools, structured outputs, global state. Techniques: knowledge/tool selection, context ordering/compression, long-term memory blocks. Uses LlamaIndex Workflows for event-driven sequences.</s>
<s slug="context-engineering" type="golden_web">Context engineering curates information in LLM context window at each agent step. Treats context as limited RAM. Strategies: write, select, compress, isolate. Manages instructions, knowledge, tools. Failure modes: poisoning, distraction, confusion, clash. LangGraph supplies checkpointing, memory stores, tool search, summarization, multi-agent patterns.</s>
<s slug="the-rise-of-context-engineering" type="golden_web">Context engineering builds dynamic systems supplying LLMs right information, tools, formatting. Supersedes prompt engineering. Components: multi-source system, dynamic construction, selection, tools, formatting, verification. Failures stem from inadequate context. Techniques: tool formatting, short/long-term memory, RAG. Frameworks: LangGraph, LangSmith.</s>
<s slug="1-for-context-engineering-over-prompt-engineering" type="exploitation">Context engineering assembles information inside context window including task descriptions, few-shot, RAG, tools, state, history. Contrasts with prompt engineering. Frames practice as science and art. Part of broader software layer for control flows, routing, guardrails, evals.</s>
<s slug="context-engineering-101-cheat-sheet" type="exploitation">Context engineering is core skill for reliable LLM applications, evolution beyond prompt engineering. Aggregates resources on patterns, 12-factor agents, long-context failures, context ownership.</s>
<s slug="context-engineering-guide" type="exploitation">Context engineering designs and optimizes instructions plus relevant context. Covers prompt chains, RAG, tools, memory, structured outputs. Multi-agent workflow example with system prompts, date handling, vector caching.</s>
<s slug="humanlayer_12-factor-agents" type="exploitation">AI engineering reduces to context engineering. Patterns for reliable agents: own context window, deterministic pre-fetching, micro-agents, unified thread state. Tools as structured outputs. Supports triggers from Slack etc. Context engineering recognized after publication.</s>
<s slug="what-is-context-engineering" type="exploitation">Context engineering assembles inputs in finite LLM window. Higher abstraction over prompt engineering for RAG. Categories: tool use, prompt engineering, retrieval, memory, agentic architectures. Example evolves customer-support RAG into full agent with memory, tools, compaction.</s>
</sources>

<tavily_yield_per_section>
| section_id | helping_rounds | unique_facts | duplicate_facts |
|---|---|---|---|
| S1::section-1-introduction-when-prompt-engineering-breaks | 2 | 7 | 0 |
| S2::section-2-from-prompt-to-context-engineering | 3 | 7 | 0 |
| S3::section-3-understanding-context-engineering | 2 | 6 | 0 |
| S4::section-4-what-makes-up-the-context | 1 | 6 | 0 |
| S5::section-5-production-implementation-challenges | 2 | 6 | 0 |
| S6::section-6-key-strategies-for-context-optimization | 3 | 6 | 0 |
| S7::section-7-here-is-an-example | 2 | 5 | 0 |
| S8::section-8-conclusion-wrap-up-connecting-context-engineering-to-ai-engineering | 2 | 5 | 0 |
tavily_saturation=1.0
</tavily_yield_per_section>

<section_coverage>
<section id="S1::section-1-introduction-when-prompt-engineering-breaks" self_contained="yes" sources="the-rise-of-context-engineering,context-engineering-what-it-is-and-techniques-to-consider,1-for-context-engineering-over-prompt-engineering" artefacts="">
  <intent>Introduces evolution of AI applications from simple chatbots to memory-enabled agents and explains why prompt engineering alone fails at scale, motivating the shift to context engineering.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="the-rise-of-context-engineering"/>
    <item name="theoretical_foundations" present="yes" evidence="context-engineering-what-it-is-and-techniques-to-consider"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="1-for-context-engineering-over-prompt-engineering"/>
    <item name="limitations_failure_modes" present="yes" evidence="the-rise-of-context-engineering"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="context-engineering-what-it-is-and-techniques-to-consider"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="the-rise-of-context-engineering"/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="1-for-context-engineering-over-prompt-engineering"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="Start the lesson with a short story on the evolution of AI applications:" bullet="motivation">Story directly supports motivation for why prompt engineering breaks.</orphan>
    <orphan route="breadth" anchor="Chatbots (2022): Simple question-and-answer interfaces" bullet="historical_context">Provides historical timeline of AI application growth.</orphan>
  </orphan_anchors>
</section>

<section id="S2::section-2-from-prompt-to-context-engineering" self_contained="yes" sources="context-engineering-101-cheat-sheet,context-engineering-guide,context-engineering-a-guide-with-examples" artefacts="">
  <intent>Details concrete limitations of prompt engineering and shows how context engineering addresses exponential data growth and multi-turn state.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="context-engineering-a-guide-with-examples"/>
    <item name="theoretical_foundations" present="yes" evidence="context-engineering-guide"/>
    <item name="technical_nuances" present="yes" evidence="context-engineering-101-cheat-sheet"/>
    <item name="latest_advancements" present="yes" evidence="context-engineering-a-guide-with-examples"/>
    <item name="limitations_failure_modes" present="yes" evidence="context-engineering-guide"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="4">
    <item name="adjacent_concepts" present="yes" evidence="context-engineering-101-cheat-sheet"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="context-engineering-guide"/>
    <item name="industry_applications" present="yes" evidence="context-engineering-a-guide-with-examples"/>
    <item name="adjacent_trends" present="yes" evidence="context-engineering-101-cheat-sheet"/>
  </breadth_checklist>
  <orphan_anchors n_depth="2" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Issues with prompt engineering:" bullet="limitations_failure_modes">Lists specific failure modes of prompt engineering.</orphan>
    <orphan route="depth" anchor="Real-world example: In one of our previous projects, we tried to add everything into the context window of the LLM. As it supported windows up to 2 million tokens, we thought, &quot;What could go wrong?&quot;" bullet="case_studies_metrics">Provides concrete project anecdote.</orphan>
  </orphan_anchors>
</section>

<section id="S3::section-3-understanding-context-engineering" self_contained="yes" sources="what-is-context-engineering,a-survey-of-context-engineering-for-large-language-models,the-rise-of-context-engineering" artefacts="A01">
  <intent>Defines context engineering, contrasts it with prompt engineering and fine-tuning, and positions it as the primary skill for modern AI systems.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="the-rise-of-context-engineering"/>
    <item name="theoretical_foundations" present="yes" evidence="a-survey-of-context-engineering-for-large-language-models"/>
    <item name="technical_nuances" present="yes" evidence="what-is-context-engineering"/>
    <item name="latest_advancements" present="yes" evidence="the-rise-of-context-engineering"/>
    <item name="limitations_failure_modes" present="yes" evidence="a-survey-of-context-engineering-for-large-language-models"/>
    <item name="implementation_tradeoffs" present="yes" evidence="what-is-context-engineering"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="yes" evidence="A01"/>
  </depth_checklist>
  <breadth_checklist breadth_score="5">
    <item name="adjacent_concepts" present="yes" evidence="what-is-context-engineering"/>
    <item name="cross_domain_analogies" present="yes" evidence="a-survey-of-context-engineering-for-large-language-models"/>
    <item name="historical_context" present="yes" evidence="the-rise-of-context-engineering"/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="yes" evidence="what-is-context-engineering"/>
    <item name="adjacent_trends" present="yes" evidence="the-rise-of-context-engineering"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="Definition: Context engineering is about finding the best way to arrange parts of your memory into the context that's passed to the LLM to squeeze out the best results out of it." bullet="theoretical_foundations">Core definition anchors theoretical explanation.</orphan>
    <orphan route="breadth" anchor="Analogy: `Context as the AI's &quot;RAM&quot;`:" bullet="cross_domain_analogies">Uses operating-system RAM analogy.</orphan>
  </orphan_anchors>
</section>

<section id="S4::section-4-what-makes-up-the-context" self_contained="yes" sources="context-engineering-what-it-is-and-techniques-to-consider,context-engineering,context-engineering-101-cheat-sheet" artefacts="">
  <intent>Breaks down the concrete elements that constitute context, mapping short-term and long-term memory components to the prompt construction workflow.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="no" evidence=""/>
    <item name="theoretical_foundations" present="yes" evidence="context-engineering-what-it-is-and-techniques-to-consider"/>
    <item name="technical_nuances" present="yes" evidence="context-engineering"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="context-engineering-101-cheat-sheet"/>
    <item name="implementation_tradeoffs" present="yes" evidence="context-engineering-what-it-is-and-techniques-to-consider"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="4">
    <item name="adjacent_concepts" present="yes" evidence="context-engineering"/>
    <item name="cross_domain_analogies" present="yes" evidence="context-engineering-what-it-is-and-techniques-to-consider"/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="context-engineering-101-cheat-sheet"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="context-engineering"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="To better understand what contenxt engineering is, let's look at the core elements that built up the context." bullet="technical_nuances">Directly leads into component breakdown.</orphan>
    <orphan route="breadth" anchor="Short-term working memory, which is often referred to as the state of the agent or workflow, which can contain:" bullet="adjacent_concepts">Introduces adjacent memory concepts.</orphan>
  </orphan_anchors>
</section>

<section id="S5::section-5-production-implementation-challenges" self_contained="yes" sources="1-for-context-engineering-over-prompt-engineering,humanlayer_12-factor-agents,context-engineering-guide" artefacts="">
  <intent>Enumerates four primary production challenges that arise when scaling context management inside real agent and workflow systems.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="humanlayer_12-factor-agents"/>
    <item name="theoretical_foundations" present="no" evidence=""/>
    <item name="technical_nuances" present="yes" evidence="context-engineering-guide"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="1-for-context-engineering-over-prompt-engineering"/>
    <item name="implementation_tradeoffs" present="yes" evidence="humanlayer_12-factor-agents"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="4">
    <item name="adjacent_concepts" present="yes" evidence="context-engineering-guide"/>
    <item name="cross_domain_analogies" present="yes" evidence="humanlayer_12-factor-agents"/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="1-for-context-engineering-over-prompt-engineering"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="context-engineering-guide"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="The context window challenge:" bullet="limitations_failure_modes">Details core technical limitation.</orphan>
    <orphan route="breadth" anchor="Tool confusion:" bullet="adjacent_concepts">Connects to tool-selection patterns.</orphan>
  </orphan_anchors>
</section>

<section id="S6::section-6-key-strategies-for-context-optimization" self_contained="yes" sources="context-engineering-a-guide-with-examples,what-is-context-engineering,the-rise-of-context-engineering" artefacts="">
  <intent>Presents four practical optimization strategies (select, compress, isolate, format) used in production to keep context minimal yet sufficient.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="context-engineering-a-guide-with-examples"/>
    <item name="theoretical_foundations" present="yes" evidence="the-rise-of-context-engineering"/>
    <item name="technical_nuances" present="yes" evidence="what-is-context-engineering"/>
    <item name="latest_advancements" present="yes" evidence="context-engineering-a-guide-with-examples"/>
    <item name="limitations_failure_modes" present="yes" evidence="what-is-context-engineering"/>
    <item name="implementation_tradeoffs" present="yes" evidence="the-rise-of-context-engineering"/>
    <item name="case_studies_metrics" present="yes" evidence="context-engineering-a-guide-with-examples"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="5">
    <item name="adjacent_concepts" present="yes" evidence="what-is-context-engineering"/>
    <item name="cross_domain_analogies" present="yes" evidence="context-engineering-a-guide-with-examples"/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="the-rise-of-context-engineering"/>
    <item name="industry_applications" present="yes" evidence="context-engineering-a-guide-with-examples"/>
    <item name="adjacent_trends" present="yes" evidence="what-is-context-engineering"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="Selecting the right context:" bullet="technical_nuances">Core selection technique with concrete steps.</orphan>
    <orphan route="breadth" anchor="Isolating Context:" bullet="adjacent_concepts">Links to multi-agent isolation patterns.</orphan>
  </orphan_anchors>
</section>

<section id="S7::section-7-here-is-an-example" self_contained="yes" sources="a-survey-of-context-engineering-for-large-language-models,context-engineering-what-it-is-and-techniques-to-consider,context-engineering-guide" artefacts="A19">
  <intent>Illustrates the full context-engineering pipeline through healthcare and enterprise use-cases, including a concrete XML-formatted prompt example.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="context-engineering-guide"/>
    <item name="theoretical_foundations" present="no" evidence=""/>
    <item name="technical_nuances" present="yes" evidence="context-engineering-what-it-is-and-techniques-to-consider"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="a-survey-of-context-engineering-for-large-language-models"/>
    <item name="implementation_tradeoffs" present="yes" evidence="context-engineering-guide"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="yes" evidence="A19"/>
  </depth_checklist>
  <breadth_checklist breadth_score="4">
    <item name="adjacent_concepts" present="yes" evidence="context-engineering-what-it-is-and-techniques-to-consider"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="context-engineering-guide"/>
    <item name="industry_applications" present="yes" evidence="a-survey-of-context-engineering-for-large-language-models"/>
    <item name="adjacent_trends" present="yes" evidence="context-engineering-what-it-is-and-techniques-to-consider"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="Example Query: `I have a headache. What can I do to stop it? I would prefer not to take any medicine.`" bullet="case_studies_metrics">Walks through concrete query handling.</orphan>
    <orphan route="breadth" anchor="Healthcare: AI systems that have access to patient data, patient history, current symptoms, and medical literature" bullet="industry_applications">Shows healthcare domain application.</orphan>
  </orphan_anchors>
</section>

<section id="S8::section-8-conclusion-wrap-up-connecting-context-engineering-to-ai-engineering" self_contained="yes" sources="1-for-context-engineering-over-prompt-engineering,context-engineering-101-cheat-sheet,what-is-context-engineering" artefacts="">
  <intent>Positions context engineering as the integrative discipline combining AI engineering, software engineering, data engineering and operations, and previews upcoming lessons.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="1-for-context-engineering-over-prompt-engineering"/>
    <item name="theoretical_foundations" present="yes" evidence="what-is-context-engineering"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="context-engineering-101-cheat-sheet"/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="1-for-context-engineering-over-prompt-engineering"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="5">
    <item name="adjacent_concepts" present="yes" evidence="what-is-context-engineering"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="context-engineering-101-cheat-sheet"/>
    <item name="enabling_technologies" present="yes" evidence="1-for-context-engineering-over-prompt-engineering"/>
    <item name="industry_applications" present="yes" evidence="what-is-context-engineering"/>
    <item name="adjacent_trends" present="yes" evidence="context-engineering-101-cheat-sheet"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="Context engineering is more of an art than a science." bullet="theoretical_foundations">Summarizes integrative view.</orphan>
    <orphan route="breadth" anchor="Our goal with this course is to teach you how to combine these skills to build production-ready AI products." bullet="industry_applications">Connects to broader AI engineering practice.</orphan>
  </orphan_anchors>
</section>

</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction-when-prompt-engineering-breaks" need_depth="7" need_breadth="6" target_words="220" mandatory_bullets="5" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S2::section-2-from-prompt-to-context-engineering" need_depth="9" need_breadth="2" target_words="275" mandatory_bullets="6" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S3::section-3-understanding-context-engineering" need_depth="4" need_breadth="4" target_words="500" mandatory_bullets="9" must_cover_depth="5" must_stay_brief="0"/>
  <section id="S4::section-4-what-makes-up-the-context" need_depth="7" need_breadth="5" target_words="500" mandatory_bullets="8" must_cover_depth="4" must_stay_brief="0"/>
  <section id="S5::section-5-production-implementation-challenges" need_depth="7" need_breadth="5" target_words="400" mandatory_bullets="5" must_cover_depth="2" must_stay_brief="0"/>
  <section id="S6::section-6-key-strategies-for-context-optimization" need_depth="4" need_breadth="4" target_words="650" mandatory_bullets="10" must_cover_depth="6" must_stay_brief="0"/>
  <section id="S7::section-7-here-is-an-example" need_depth="6" need_breadth="5" target_words="500" mandatory_bullets="6" must_cover_depth="4" must_stay_brief="0"/>
  <section id="S8::section-8-conclusion-wrap-up-connecting-context-engineering-to-ai-engineering" need_depth="7" need_breadth="4" target_words="275" mandatory_bullets="5" must_cover_depth="2" must_stay_brief="0"/>
  <overall>
    <weakest_sections>S5::section-5-production-implementation-challenges, S1::section-1-introduction-when-prompt-engineering-breaks</weakest_sections>
    <strongest_sections>S3::section-3-understanding-context-engineering, S6::section-6-key-strategies-for-context-optimization</strongest_sections>
    <dominant_gap_type>balanced</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>