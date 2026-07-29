<digest_meta>
  <article_title>Retrieval-Augmented Generation</article_title>
  <total_sources>11</total_sources>
  <total_artefacts>12</total_artefacts>
  <tavily_saturation>0.875</tavily_saturation>
  <n_orphan_anchors>28</n_orphan_anchors>
  <n_content_sections>6</n_content_sections>
  <external_evidence_policy>allowed</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
| A01 | from-local-to-global-a-graphrag-approach-to-query-focused-su | code:python | criteria | 6 | CRITERIA = { |
| A12 | what-is-agentic-rag | table | vanilla,agentic | 6 | \| \| Vanilla LLM RAG \| Agentic RAG \| |
</artefact_registry>

<sources>
<s slug="a-complete-guide-to-rag" type="golden_web">Main topic: comprehensive guide to Retrieval-Augmented Generation (RAG), contrasting it with model retraining and detailing the full pipeline for grounding LLMs in private company data. Key concepts: Retriever and Generator; query preprocessing via LLM reformulation or RAG Fusion; vector databases; ensembling of dense and sparse retrievers; result ranking, evaluation, and stylistic formatting. Concrete tools: LangChain, Qdrant, OpenAIEmbeddings, BM25Retriever, EnsembleRetriever; vector stores Qdrant, Pinecone, Chroma, FAISS; metrics P@K, MAP@K, NDCG@K. Specific claims: Cross-Encoder accuracy superior to Bi-Encoders.</s>
<s slug="advanced-rag-blueprint-optimize-llm-retrieval-systems" type="golden_web">Optimizations for vanilla RAG across pre-retrieval, retrieval, and post-retrieval. Pre-retrieval: sliding window overlap, metadata tags, multi-indexing, small-to-big decoupling, query rewriting, HyDE, self-query. Retrieval: hybrid search, filtered vector search, instructor models. Post-retrieval: prompt compression, re-ranking via cross-encoder. No quantitative benchmarks provided.</s>
<s slug="from-local-to-global-a-graphrag-approach-to-query-focused-su" type="golden_web">GraphRAG pipeline: chunking, LLM entity/relationship extraction, knowledge graph construction with Leiden clustering, hierarchical community summaries. Evaluations on two 1M-token corpora show 72–83% win rates on comprehensiveness vs vector RAG. Open-source at microsoft/graphrag. Limitations: fixed 8k context, two English corpora only.</s>
<s slug="rag-fundamentals-first-by-paul-iusztin-decoding-ml" type="golden_web">Defines RAG via Retrieval, Augmentation, Generation modules. Ingestion: load-clean-chunk-embed-store. Retrieval: embed query, cosine similarity top-K. Generation: prompt + context to LLM. Addresses hallucinations and knowledge cutoffs without retraining.</s>
<s slug="what-is-retrieval-augmented-generation-aka-rag" type="golden_web">NVIDIA overview: RAG as open-book exam for LLMs using external sources. Reduces hallucinations, enables citations. Roots in 1970s QA systems. Tools: LangChain, NVIDIA NeMo Retriever, Pinecone. 5-line implementation possible; integrates with agentic AI.</s>
<s slug="build-advanced-retrieval-augmented-generation-systems" type="exploitation">Microsoft guide: advanced RAG adds preprocessing, post-processing, evaluation. Covers chunking strategies, query routers, re-ranking, harms modeling, red-teaming. Diagrams for naive vs advanced pipelines.</s>
<s slug="introducing-contextual-retrieval" type="exploitation">Contextual Retrieval prepends 50-100 token situating context to chunks. Reduces retrieval failure from 5.7% to 1.9% with rerank. Uses Claude 3 Haiku + prompt caching; tested on codebases, fiction, arXiv.</s>
<s slug="rag-is-dead-long-live-agentic-retrieval" type="exploitation">Agentic retrieval via LlamaParse: auto_routed mode, composite retrievers for multi-index. Routes queries across retrieval modes and knowledge bases.</s>
<s slug="the-rise-of-rag" type="exploitation">RAG evolution: chunk-based, hierarchical, hybrid, contextual, GraphRAG, text-to-SQL. Advantages over long-context models: lower latency, traceability. Agentic systems decompose queries.</s>
<s slug="what-is-agentic-rag-1" type="exploitation">Agentic RAG adds routing, planning, ReAct/plan-and-execute agents, multi-agent coordination. Contrasts reactive vs proactive behavior. Frameworks: LangGraph, CrewAI, OpenAI Swarm.</s>
<s slug="what-is-agentic-rag" type="exploitation">ReAct loop (Thought-Action-Observation) for iterative retrieval. Agents access multiple tools including vector search, web search. 6-line vanilla vs agentic comparison table. Code examples for hybrid search and tool loops.</s>
</sources>

<tavily_yield_per_section>
| section_id | helping_rounds | unique_facts | duplicate_facts |
|---|---|---|---|
| S1::section-1-introduction-giving-llms-an-open-book-exam | 3 | 9 | 0 |
| S2::section-2-the-rag-system-core-components | 4 | 8 | 0 |
| S3::section-3-the-rag-pipeline-ingestion-and-retrieval | 2 | 8 | 0 |
| S4::section-4-advanced-rag-techniques | 4 | 7 | 0 |
| S5::section-5-agentic-rag | 1 | 7 | 0 |
| S6::section-6-conclusion | 2 | 6 | 0 |
tavily_saturation=0.875
</tavily_yield_per_section>

<section_coverage>
<section id="S1::section-1-introduction-giving-llms-an-open-book-exam" self_contained="yes" sources="what-is-retrieval-augmented-generation-aka-rag,rag-fundamentals-first-by-paul-iusztin-decoding-ml,the-rise-of-rag" artefacts="">
  <intent>This section introduces the core problem of static LLM knowledge and positions RAG as the solution within the course's context engineering framework.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="theoretical_foundations" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="technical_nuances" present="yes" evidence="the-rise-of-rag"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="5">
    <item name="adjacent_concepts" present="yes" evidence="the-rise-of-rag"/>
    <item name="cross_domain_analogies" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="historical_context" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="enabling_technologies" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="the-rise-of-rag"/>
  </breadth_checklist>
  <orphan_anchors n_depth="2" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="Quick reference to what we've learned in previous lessons: Take the core ideas of what we've learned in previous lessons" bullet="motivation">Directly addresses course context engineering recall needed for motivation.</orphan>
    <orphan route="depth" anchor="Start by informing readers of a core problem: LLMs are trained on a fixed dataset, making their knowledge static and pro" bullet="motivation">Matches exact motivation bullet on knowledge cutoffs.</orphan>
    <orphan route="breadth" anchor="We'll contrast retrieval with agent memory in Lesson 10 (next one), where we discuss short- and long-term memory stores" bullet="adjacent_concepts">Touches future memory topic as adjacent concept.</orphan>
  </orphan_anchors>
</section>
<section id="S2::section-2-the-rag-system-core-components" self_contained="yes" sources="advanced-rag-blueprint-optimize-llm-retrieval-systems,a-complete-guide-to-rag,build-advanced-retrieval-augmented-generation-systems" artefacts="">
  <intent>This section decomposes RAG into the three conceptual pillars of retrieval, augmentation, and generation with a supporting diagram.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="theoretical_foundations" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="technical_nuances" present="yes" evidence="build-advanced-retrieval-augmented-generation-systems"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="implementation_tradeoffs" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="build-advanced-retrieval-augmented-generation-systems"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Understanding these components is the first step in the Context Engineering process (Lesson 03) of designing effective R" bullet="motivation">Links components directly to prior context engineering lesson.</orphan>
  </orphan_anchors>
</section>
<section id="S3::section-3-the-rag-pipeline-ingestion-and-retrieval" self_contained="yes" sources="introducing-contextual-retrieval,from-local-to-global-a-graphrag-approach-to-query-focused-su,rag-fundamentals-first-by-paul-iusztin-decoding-ml" artefacts="">
  <intent>This section details the offline ingestion/indexing and online retrieval/generation phases of a complete RAG pipeline.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="theoretical_foundations" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="technical_nuances" present="yes" evidence="introducing-contextual-retrieval"/>
    <item name="latest_advancements" present="yes" evidence="introducing-contextual-retrieval"/>
    <item name="limitations_failure_modes" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="implementation_tradeoffs" present="yes" evidence="introducing-contextual-retrieval"/>
    <item name="case_studies_metrics" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="introducing-contextual-retrieval"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Phase 1: Offline Ingestion &amp; Indexing" bullet="technical_nuances">Covers concrete load-split-embed-store steps with examples.</orphan>
  </orphan_anchors>
</section>
<section id="S4::section-4-advanced-rag-techniques" self_contained="yes" sources="what-is-agentic-rag-1,rag-is-dead-long-live-agentic-retrieval,advanced-rag-blueprint-optimize-llm-retrieval-systems" artefacts="">
  <intent>This section explores advanced techniques including hybrid search, re-ranking, query transformations, and GraphRAG to improve retrieval quality.</intent>
  <depth_checklist depth_score="8">
    <item name="motivation" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="theoretical_foundations" present="yes" evidence="rag-is-dead-long-live-agentic-retrieval"/>
    <item name="technical_nuances" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="latest_advancements" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="limitations_failure_modes" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="implementation_tradeoffs" present="yes" evidence="rag-is-dead-long-live-agentic-retrieval"/>
    <item name="case_studies_metrics" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="artefact_available" present="yes" evidence="A01"/>
  </depth_checklist>
  <breadth_checklist breadth_score="5">
    <item name="adjacent_concepts" present="yes" evidence="rag-is-dead-long-live-agentic-retrieval"/>
    <item name="cross_domain_analogies" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="industry_applications" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="adjacent_trends" present="yes" evidence="rag-is-dead-long-live-agentic-retrieval"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="Hybrid Search: Combining keyword-based search (like BM25) for precision with vector search for capturing semantic meanin" bullet="technical_nuances">Matches hybrid search technical nuance directly.</orphan>
    <orphan route="breadth" anchor="GraphRAG: Introducing retrieval from knowledge graphs. **Explain that this technique excels at answering questions about complex relationships and interconnected entities, which are often lost in standard document chunks.**" bullet="cross_domain_analogies">Draws explicit graph vs chunk comparison across domains.</orphan>
  </orphan_anchors>
</section>
<section id="S5::section-5-agentic-rag" self_contained="yes" sources="what-is-agentic-rag,what-is-retrieval-augmented-generation-aka-rag,what-is-agentic-rag-1" artefacts="">
  <intent>This section contrasts standard linear RAG with adaptive agentic RAG using ReAct-style reasoning and tool use.</intent>
  <depth_checklist depth_score="8">
    <item name="motivation" present="yes" evidence="what-is-agentic-rag"/>
    <item name="theoretical_foundations" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="technical_nuances" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="latest_advancements" present="yes" evidence="what-is-agentic-rag"/>
    <item name="limitations_failure_modes" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="implementation_tradeoffs" present="yes" evidence="what-is-agentic-rag"/>
    <item name="case_studies_metrics" present="yes" evidence="what-is-agentic-rag"/>
    <item name="artefact_available" present="yes" evidence="A12"/>
  </depth_checklist>
  <breadth_checklist breadth_score="5">
    <item name="adjacent_concepts" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="cross_domain_analogies" present="yes" evidence="what-is-agentic-rag"/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="industry_applications" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="adjacent_trends" present="yes" evidence="what-is-agentic-rag"/>
  </breadth_checklist>
  <orphan_anchors n_depth="1" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Tie directly to Lessons 7–8 (ReAct). Emphasize: Agentic RAG is essentially a ReAct-style agent equipped with a retrieval tool." bullet="theoretical_foundations">Links directly to prior ReAct lessons for theoretical grounding.</orphan>
  </orphan_anchors>
</section>
<section id="S6::section-6-conclusion" self_contained="yes" sources="from-local-to-global-a-graphrag-approach-to-query-focused-su,the-rise-of-rag,a-complete-guide-to-rag" artefacts="">
  <intent>This section summarizes RAG benefits, positions it as foundational for AI engineering, and previews future lessons on memory and evaluations.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="the-rise-of-rag"/>
    <item name="theoretical_foundations" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="limitations_failure_modes" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="5">
    <item name="adjacent_concepts" present="yes" evidence="the-rise-of-rag"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="enabling_technologies" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="industry_applications" present="yes" evidence="the-rise-of-rag"/>
    <item name="adjacent_trends" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="1" n_unreachable="0">
    <orphan route="breadth" anchor="To transition from this lesson to the next, specify what we will learn in future lessons. First mention what we will learn in next lesson, which is Lesson 10." bullet="adjacent_concepts">Previews adjacent memory concept in next lesson.</orphan>
  </orphan_anchors>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction-giving-llms-an-open-book-exam" need_depth="10" need_breadth="4" target_words="565" mandatory_bullets="8" must_cover_depth="2" must_stay_brief="3"/>
  <section id="S2::section-2-the-rag-system-core-components" need_depth="6" need_breadth="3" target_words="465" mandatory_bullets="5" must_cover_depth="4" must_stay_brief="1"/>
  <section id="S3::section-3-the-rag-pipeline-ingestion-and-retrieval" need_depth="4" need_breadth="3" target_words="625" mandatory_bullets="10" must_cover_depth="12" must_stay_brief="1"/>
  <section id="S4::section-4-advanced-rag-techniques" need_depth="3" need_breadth="4" target_words="910" mandatory_bullets="9" must_cover_depth="8" must_stay_brief="0"/>
  <section id="S5::section-5-agentic-rag" need_depth="3" need_breadth="1" target_words="395" mandatory_bullets="10" must_cover_depth="5" must_stay_brief="1"/>
  <section id="S6::section-6-conclusion" need_depth="3" need_breadth="4" target_words="210" mandatory_bullets="4" must_cover_depth="2" must_stay_brief="1"/>
  <overall>
    <weakest_sections>S2::section-2-the-rag-system-core-components, S1::section-1-introduction-giving-llms-an-open-book-exam</weakest_sections>
    <strongest_sections>S5::section-5-agentic-rag, S3::section-3-the-rag-pipeline-ingestion-and-retrieval</strongest_sections>
    <dominant_gap_type>depth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>