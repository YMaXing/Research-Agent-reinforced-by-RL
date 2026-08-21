<digest_meta>
  <article_title>Retrieval-Augmented Generation (demanding variant)</article_title>
  <total_sources>11</total_sources>
  <total_artefacts>12</total_artefacts>
  <tavily_saturation>0.875</tavily_saturation>
  <n_orphan_anchors>42</n_orphan_anchors>
  <n_content_sections>6</n_content_sections>
  <external_evidence_policy>allowed</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
| A08 | what-is-agentic-rag | code:python | search,results,query | 13 | def get_search_results(query: str) -> st |
| A09 | what-is-agentic-rag | code:python | tools,schema | 17 | tools_schema=[{\ |
| A10 | what-is-agentic-rag | code:python | ollama,generation,tools,user,message | 26 | def ollama_generation_with_tools(user_me |
| A11 | what-is-agentic-rag | code:python | ollama,generation,tools,hnsw,different | 2 | ollama_generation_with_tools("How is HNS |
| A12 | what-is-agentic-rag | table | vanilla,agentic | 6 | \| \| Vanilla LLM RAG \| Agentic RAG \| |
</artefact_registry>

<sources>
<s slug="a-complete-guide-to-rag" type="golden_web">A Complete Guide to RAG explains Retrieval-Augmented Generation as an alternative to model retraining for injecting proprietary company data (documents, rules, wikis, CRM) into LLMs such as OpenAI models. The core architecture separates a Retriever (vector store or other index returning relevant passages) from a Generator (LLM that synthesizes an answer from retrieved context). The guide stresses that answer quality depends on retrieval precision because source documents are typically unstructured, contradictory, or context-dependent.</s>
<s slug="advanced-rag-blueprint-optimize-llm-retrieval-systems" type="golden_web">The source details optimizations for RAG systems to address vanilla RAG limitations in document relevance, context sufficiency, noise, latency, and answer validity. It frames advanced RAG as improvements applied across three stages—pre-retrieval, retrieval, and post-retrieval—while noting the need for separate evaluation modules.</s>
<s slug="from-local-to-global-a-graphrag-approach-to-query-focused-su" type="golden_web">GraphRAG is a graph-based retrieval-augmented generation method that addresses the failure of vector RAG on global sensemaking queries over entire corpora (e.g., “What are the main themes in the dataset?”). It first splits source documents into fixed-size text chunks (default 600 tokens with 100-token overlap), then uses an LLM to extract entities, relationships, and claims via domain-tailored prompts that support in-context learning and optional self-reflection passes.</s>
<s slug="rag-fundamentals-first-by-paul-iusztin-decoding-ml" type="golden_web">Retrieval-Augmented Generation (RAG) enhances LLM outputs by fetching external data to address bounded parameterized knowledge, hallucinations, and outdated or private information. The source defines RAG as Retrieval (search external data), Augmented (inject into prompt), and Generation (LLM response). GPT-4o (OpenAI, cutoff October 2023) is cited to illustrate: it accurately recalls 2020 pandemic events via training data but hallucinates on 2024 soccer EURO results or private/new data.</s>
<s slug="what-is-retrieval-augmented-generation-aka-rag" type="golden_web">Retrieval-augmented generation (RAG) is a technique that augments LLMs by retrieving relevant information from external or internal knowledge bases before generation, improving accuracy, grounding answers in sources, enabling citations, resolving query ambiguity, and reducing hallucinations. It was introduced in the 2020 paper “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks” by Patrick Lewis.</s>
<s slug="build-advanced-retrieval-augmented-generation-systems" type="exploitation">This source details the construction of production-ready advanced retrieval-augmented generation (RAG) systems, contrasting naive RAG (basic vector embedding + cosine similarity retrieval followed by LLM generation) with advanced RAG pipelines that incorporate extensive preprocessing, post-processing, and evaluation.</s>
<s slug="introducing-contextual-retrieval" type="exploitation">Contextual Retrieval improves standard RAG for large knowledge bases by prepending chunk-specific explanatory context before embedding and indexing. Traditional RAG splits documents into chunks of a few hundred tokens, generates semantic embeddings, and optionally applies BM25 (built on TF-IDF with length normalization and term-frequency saturation) for lexical matching, then fuses results via rank fusion before appending top-K chunks to prompts.</s>
<s slug="rag-is-dead-long-live-agentic-retrieval" type="exploitation">RAG has evolved from naive top-k chunk retrieval in vector databases to agentic strategies that incorporate hybrid search, CRAG, Self-RAG, HyDE, deep research, reranking, multi-modal embeddings, and RAPTOR. The source demonstrates this progression through LlamaParse services, abstracting techniques behind a small set of top-level hyperparameters while exposing retrieval modes for flexible query handling.</s>
<s slug="the-rise-of-rag" type="exploitation">RAG improves LLM reliability by retrieving external information to address knowledge cutoffs and hallucinations, as introduced in the 2020 Meta paper. The system splits into retrieval (identifying relevant data from documents, databases, or multimedia via user prompt analysis) and generation (LLM response synthesis using retrieved content plus the prompt).</s>
<s slug="what-is-agentic-rag-1" type="exploitation">Agentic RAG extends retrieval-augmented generation by embedding AI agents into the pipeline for multi-source retrieval, adaptive workflows, and improved accuracy. The source defines traditional RAG as a two-model system consisting of an embedding model paired with a vector database for information retrieval, followed by an LLM for context-augmented generation.</s>
<s slug="what-is-agentic-rag" type="exploitation">Agentic RAG extends standard Retrieval-Augmented Generation by embedding AI agents into the retrieval stage, enabling iterative planning, tool selection, query formulation, context evaluation, and validation loops. The source contrasts naive one-shot RAG (single vector search plus LLM generation) with agentic variants that overcome single-source and non-reasoning limits via ReAct-style cycles (Thought → Action → Observation) that maintain short- and long-term memory.</s>
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
<section id="S1::section-1-introduction-giving-llms-an-open-book-exam" self_contained="yes" sources="what-is-agentic-rag,rag-fundamentals-first-by-paul-iusztin-decoding-ml,the-rise-of-rag" artefacts="">
  <intent>Introduce the core problem of static LLM knowledge and position RAG as the open-book solution within Context Engineering.</intent>
  <depth_checklist depth_score="3">
    <item name="motivation" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="theoretical_foundations" present="yes" evidence="the-rise-of-rag"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="what-is-agentic-rag"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="the-rise-of-rag"/>
    <item name="cross_domain_analogies" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="6" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="Quick reference to what we've learned in previous lessons: Take the core ideas of what we've learned in previous lessons" bullet="motivation">Directly recalls Context Engineering from Lesson 03 as foundation for RAG.</orphan>
    <orphan route="depth" anchor="Transition to what we'll learn in this lesson: After presenting what we learned in the past, make a transition to what w" bullet="motivation">Sets up RAG as the lesson's core method for dynamic knowledge.</orphan>
    <orphan route="depth" anchor="Additional guidance:" bullet="limitations_failure_modes">Covers fine-tuning limits and context-window constraints in depth.</orphan>
    <orphan route="depth" anchor="Start by informing readers of a core problem: LLMs are trained on a fixed dataset, making their knowledge static and pro" bullet="motivation">Opens with static knowledge and hallucination problem.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Fine-tuning limitations (resource-heavy, slow, catastrophic forgetting risks, dataset curation, mul" bullet="limitations_failure_modes">Explicitly requires detailed coverage of fine-tuning drawbacks.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Context window limitations (finite nature, cost implications, "lost in the middle" phenomenon with" bullet="limitations_failure_modes">Requires explicit treatment of context-window issues.</orphan>
    <orphan route="depth" anchor="Introduce RAG as a reliable solution to this problem, we can insert new knowledge using the context window" bullet="theoretical_foundations">Positions RAG as the practical insertion mechanism.</orphan>
    <orphan route="depth" anchor="With RAG, we are giving the LLM an "open-book exam" by connecting it to external, real-time knowledge sources. Like huma" bullet="cross_domain_analogies">Uses human open-book analogy for motivation.</orphan>
    <orphan route="breadth" anchor="We'll contrast retrieval with agent memory in Lesson 10 (next one), where we discuss short- and long-term memory stores" bullet="adjacent_concepts">Links forward to memory concepts outside current scope.</orphan>
    <orphan route="breadth" anchor="Clarify that RAG is a tool/method, AI Engineers use/implement in the process of "Context Engineering" taught in lesson 0" bullet="adjacent_concepts">Anchors RAG inside previously taught Context Engineering.</orphan>
    <orphan route="breadth" anchor="Briefly outline the lesson's journey: from the "what" and "how" of basic RAG to the advanced and agentic patterns." bullet="adjacent_trends">Previews progression to agentic patterns taught later.</orphan>
  </orphan_anchors>
</section>
<section id="S2::section-2-the-rag-system-core-components" self_contained="yes" sources="advanced-rag-blueprint-optimize-llm-retrieval-systems,build-advanced-retrieval-augmented-generation-systems,a-complete-guide-to-rag" artefacts="">
  <intent>Decompose RAG into the three pillars of retrieval, augmentation, and generation with vector-embedding mechanics.</intent>
  <depth_checklist depth_score="3">
    <item name="motivation" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="theoretical_foundations" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="technical_nuances" present="yes" evidence="build-advanced-retrieval-augmented-generation-systems"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="9" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Understanding these components is the first step in the Context Engineering process (Lesson 03) of designing effective R" bullet="motivation">Frames components as Context Engineering step.</orphan>
    <orphan route="depth" anchor="Break down RAG into three conceptual pillars:" bullet="theoretical_foundations">Requires explicit three-pillar decomposition.</orphan>
    <orphan route="depth" anchor="Retrieval: The engine/system for finding relevant information. Semantic similarity or keyword-based search (BM25) is oft" bullet="technical_nuances">Demands semantic-search and vector-embedding depth.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Semantic search, detailed explanation of vector embeddings (creation process, properties, and stora" bullet="technical_nuances">Explicit depth requirement on embeddings and vector DBs.</orphan>
    <orphan route="depth" anchor="Augmentation: The process of taking the retrieved information and formatting it into the context of a prompt for the LLM" bullet="technical_nuances">Requires detailed augmentation formatting steps.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Augmentation process, detailed steps for formatting retrieved information into the LLM's context, a" bullet="technical_nuances">Explicit depth requirement on prompt construction.</orphan>
    <orphan route="depth" anchor="Generation: The final step where the LLM uses the augmented input to generate an answer grounded in the provided data." bullet="theoretical_foundations">Requires generation-phase grounding explanation.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Generation phase, how the LLM synthesizes information and produces a factually grounded answer." bullet="technical_nuances">Explicit depth requirement on synthesis mechanics.</orphan>
    <orphan route="depth" anchor="Include a Mermaid diagram that illustrates the flow between the user's query, the Retriever, the Augmentation step, and" bullet="implementation_tradeoffs">Diagram is a technical implementation artefact.</orphan>
  </orphan_anchors>
</section>
<section id="S3::section-3-the-rag-pipeline-ingestion-and-retrieval" self_contained="yes" sources="introducing-contextual-retrieval,from-local-to-global-a-graphrag-approach-to-query-focused-su,rag-fundamentals-first-by-paul-iusztin-decoding-ml" artefacts="">
  <intent>Detail the two-phase pipeline (offline ingestion + online retrieval) with concrete loading, chunking, embedding, and search steps.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="theoretical_foundations" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="technical_nuances" present="yes" evidence="introducing-contextual-retrieval"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="introducing-contextual-retrieval"/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="introducing-contextual-retrieval"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="18" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Detail the end-to-end RAG workflow, splitting it into its two distinct phases." bullet="technical_nuances">Requires explicit two-phase split.</orphan>
    <orphan route="depth" anchor="Phase 1: Offline Ingestion & Indexing" bullet="technical_nuances">Core ingestion mechanics demanded.</orphan>
    <orphan route="depth" anchor="Load: Reading documents from various sources (PDFs, websites, APIs). Example tools: Unstructured, LangChain document loa" bullet="implementation_tradeoffs">Document loading challenges and tools required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Document loading from various sources (PDFs, websites, APIs, databases) and challenges associated w" bullet="technical_nuances">Explicit depth on loading formats and challenges.</orphan>
    <orphan route="depth" anchor="Split: Breaking content into smaller, meaningful pieces with rule-based or semantic chunkers (avoid cutting mid-idea). E" bullet="technical_nuances">Chunking strategies required.</orphan>
    <orphan route="depth" anchor="Embed: Using an embedding model to convert each chunk into a vector embedding. Example models: OpenAI text-embedding-3-l" bullet="technical_nuances">Embedding model choices required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Embedding process, specific embedding models (e.g., OpenAI, Google, Cohere, Hugging Face variants), " bullet="technical_nuances">Explicit depth on embedding models and selection.</orphan>
    <orphan route="depth" anchor="Store: Loading the embeddings and their corresponding text into a vector database or search index for fast similarity lo" bullet="technical_nuances">Vector DB storage required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Storage mechanisms, detailed overview of vector databases (e.g., FAISS, Milvus, Qdrant, Pinecone, E" bullet="technical_nuances">Explicit depth on vector DB options and use cases.</orphan>
    <orphan route="depth" anchor="Phase 2: Online Retrieval & Generation" bullet="technical_nuances">Online phase mechanics required.</orphan>
    <orphan route="depth" anchor="Query: A user asks a question; optionally normalize or expand it. Example: LangChain `Runnable` chain or LlamaIndex `Que" bullet="implementation_tradeoffs">Query processing required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Query processing (normalization, expansion, and initial parsing)." bullet="technical_nuances">Explicit depth on query handling.</orphan>
    <orphan route="depth" anchor="Embed: Turn the query into a vector with the same embedding model as indexing." bullet="technical_nuances">Query embedding step required.</orphan>
    <orphan route="depth" anchor="Search: The query vector is used to find the top-k most similar document chunks in the vector database. Example: vector" bullet="technical_nuances">Search mechanisms required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Search mechanisms (top-k retrieval, similarity metrics like cosine similarity, and filtering capabi" bullet="technical_nuances">Explicit depth on top-k, metrics, and filtering.</orphan>
    <orphan route="depth" anchor="Generate: Build a prompt that includes the user query, instructions, and retrieved chunks; call the LLM to produce a gro" bullet="technical_nuances">Generation with citations required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Generation with structured outputs, ensuring citations and specific formatting as discussed in Less" bullet="technical_nuances">Explicit depth on structured outputs and citations.</orphan>
    <orphan route="depth" anchor="Include a more detailed Mermaid diagram showing both offline and online paths, tools (generic, not vendor-specific)." bullet="implementation_tradeoffs">Pipeline diagram is technical artefact.</orphan>
  </orphan_anchors>
</section>
<section id="S4::section-4-advanced-rag-techniques" self_contained="yes" sources="what-is-agentic-rag-1,rag-is-dead-long-live-agentic-retrieval,advanced-rag-blueprint-optimize-llm-retrieval-systems" artefacts="">
  <intent>Present production-grade retrieval improvements including hybrid search, re-ranking, query transformations, advanced chunking, GraphRAG, and metadata filtering.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="theoretical_foundations" present="yes" evidence="rag-is-dead-long-live-agentic-retrieval"/>
    <item name="technical_nuances" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="latest_advancements" present="yes" evidence="rag-is-dead-long-live-agentic-retrieval"/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="case_studies_metrics" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="4">
    <item name="adjacent_concepts" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="industry_applications" present="yes" evidence="rag-is-dead-long-live-agentic-retrieval"/>
    <item name="adjacent_trends" present="yes" evidence="what-is-agentic-rag-1"/>
  </breadth_checklist>
  <orphan_anchors n_depth="8" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Dedicate this section to exploring methods that significantly improve retrieval performance." bullet="motivation">Section purpose is performance improvement techniques.</orphan>
    <orphan route="depth" anchor="Hybrid Search: Combining keyword-based search (like BM25) for precision with vector search for capturing semantic meanin" bullet="technical_nuances">Hybrid search mechanics required.</orphan>
    <orphan route="depth" anchor="Re-ranking: Using a second "re-ranker" model (e.g., a cross-encoder, Cohere Rerank) to re-order the initial retrieved documents for improved relevance. They take the query and one candidate document together and output a relevance score." bullet="technical_nuances">Re-ranking required.</orphan>
    <orphan route="depth" anchor="Query Transformations:" bullet="technical_nuances">Decomposition and HyDE required.</orphan>
    <orphan route="depth" anchor="Advanced Chunking Strategies: Moving beyond fixed-size chunks to methods that preserve more context, such as semantic chunking, layout-aware chunking for complex documents or context enriched chunking (contextual retrieval)." bullet="technical_nuances">Advanced chunking depth required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Advanced chunking strategies (semantic chunking, layout-aware chunking for complex documents like tables/forms, context-enriched chunking, and their impact on retrieval)." bullet="technical_nuances">Explicit depth on chunking variants.</orphan>
    <orphan route="depth" anchor="GraphRAG: Introducing retrieval from knowledge graphs. **Explain that this technique excels at answering questions about complex relationships and interconnected entities, which are often lost in standard document chunks.** It solves problems where understanding the "how" and "why" between data points is as important as the data itself." bullet="theoretical_foundations">GraphRAG relationship reasoning required.</orphan>
    <orphan route="depth" anchor="Metadata Filtering: One of the most effective levers in production is metadata filtering. If each chunk carries fields like `source`, `department`, `country`, `language`, `policy_version`, or `effective_date`, you can filter the search space before scoring. This is especially important when documents are similar but scoped differently." bullet="implementation_tradeoffs">Metadata filtering production lever required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Metadata filtering (importance of metadata fields like source, department, language, policy version, temporal filters, and bitemporal logic for dynamic data)." bullet="technical_nuances">Explicit depth on metadata and temporal filters.</orphan>
    <orphan route="depth" anchor="add a mermaid diagram: Show hybrid retrieval flow: BM25 results + vector results → union → re-rank → final context." bullet="implementation_tradeoffs">Hybrid flow diagram required.</orphan>
  </orphan_anchors>
</section>
<section id="S5::section-5-agentic-rag" self_contained="yes" sources="what-is-agentic-rag,what-is-retrieval-augmented-generation-aka-rag,what-is-agentic-rag-1" artefacts="A08,A09,A10,A11,A12">
  <intent>Contrast linear RAG with adaptive, ReAct-style agentic RAG that treats retrieval as one controllable tool among many.</intent>
  <depth_checklist depth_score="8">
    <item name="motivation" present="yes" evidence="what-is-agentic-rag"/>
    <item name="theoretical_foundations" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="technical_nuances" present="yes" evidence="what-is-agentic-rag"/>
    <item name="latest_advancements" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="limitations_failure_modes" present="yes" evidence="what-is-agentic-rag"/>
    <item name="implementation_tradeoffs" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="case_studies_metrics" present="yes" evidence="what-is-agentic-rag"/>
    <item name="artefact_available" present="yes" evidence="A08"/>
  </depth_checklist>
  <breadth_checklist breadth_score="4">
    <item name="adjacent_concepts" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="what-is-agentic-rag"/>
    <item name="industry_applications" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="adjacent_trends" present="yes" evidence="what-is-agentic-rag"/>
  </breadth_checklist>
  <orphan_anchors n_depth="11" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Tie directly to Lessons 7–8 (ReAct). Emphasize: Agentic RAG is essentially a ReAct-style agent equipped with a retrieval tool. The agent reasons (Thought), decides an Action (e.g., retrieve), observes results, and iterates." bullet="theoretical_foundations">ReAct linkage required.</orphan>
    <orphan route="depth" anchor="Clarify: agents typically use many tools (web search, code execution, databases). Labeling a whole system “agentic RAG” can be too narrow—the retrieval tool is just one of several." bullet="technical_nuances">Tool breadth clarification required.</orphan>
    <orphan route="depth" anchor="First, define the core distinction (the theoretical part):" bullet="theoretical_foundations">Standard vs agentic distinction required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Core distinction between standard RAG (linear, rigid) and agentic RAG (adaptive, iterative, agent-controlled)." bullet="theoretical_foundations">Explicit depth on linear vs adaptive distinction.</orphan>
    <orphan route="depth" anchor="Explain the capabilities of an agentic approach:" bullet="technical_nuances">Iterative, choice, fusion, and update capabilities required.</orphan>
    <orphan route="depth" anchor="Then, show (conceptually) it in action:" bullet="case_studies_metrics">Conceptual mini thought-process example required.</orphan>
    <orphan route="depth" anchor="Discuss the shift from viewing RAG as an isolated process to a core tool in an agent's toolkit" bullet="theoretical_foundations">Shift to toolkit view required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: The conceptual shift from RAG as an isolated process to a core tool within an agent's versatile toolkit." bullet="theoretical_foundations">Explicit depth on toolkit shift.</orphan>
    <orphan route="depth" anchor="Use a conceptual Mermaid diagram to show an agent's main loop, where it can choose between tools like `web_search`, `code_interpreter`, and `internal_knowledge_base` (our RAG tool)." bullet="implementation_tradeoffs">Agent loop diagram required.</orphan>
    <orphan route="depth" anchor="Mini “thought process” example (no code):" bullet="case_studies_metrics">Thought-Action-Observation trace required.</orphan>
    <orphan route="depth" anchor="Frame this as the difference between a simple database lookup and a conversation with a knowledgeable research assistant." bullet="cross_domain_analogies">Research-assistant analogy required.</orphan>
  </orphan_anchors>
</section>
<section id="S6::section-6-conclusion" self_contained="yes" sources="the-rise-of-rag,from-local-to-global-a-graphrag-approach-to-query-focused-su,a-complete-guide-to-rag" artefacts="">
  <intent>Summarize RAG benefits, position it as foundational Context Engineering skill, and preview Lesson 10 memory and later production topics.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="the-rise-of-rag"/>
    <item name="theoretical_foundations" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="the-rise-of-rag"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="adjacent_trends" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
  </breadth_checklist>
  <orphan_anchors n_depth="10" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Summarize the key takeaways: RAG is the most used solution to the LLM knowledge problem, advanced techniques are important for production-grade quality, and the future of knowledge retrieval is agentic." bullet="motivation">Key takeaways summary required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Summarize key takeaways: RAG as the primary solution for LLM knowledge limitations, the necessity of advanced techniques for production quality, and the strategic importance of agentic RAG." bullet="theoretical_foundations">Explicit depth on takeaways.</orphan>
    <orphan route="depth" anchor="Reiterate the core benefits: reducing hallucinations, enabling customization with proprietary data, and building user trust through verifiable, source-backed answers." bullet="motivation">Core benefits reiteration required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Reiterate core benefits: reduction of hallucinations, enabling customization with proprietary data, and building user trust through verifiable, source-backed answers." bullet="theoretical_foundations">Explicit depth on benefits.</orphan>
    <orphan route="depth" anchor="Conclude by positioning RAG not as a niche skill but as a foundational competency for the modern AI Engineer, as a subset of Context Engineering." bullet="theoretical_foundations">Foundational competency positioning required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Positioning RAG as a foundational competency for AI Engineers and its integration within Context Engineering." bullet="theoretical_foundations">Explicit depth on positioning.</orphan>
    <orphan route="depth" anchor="To transition from this lesson to the next, specify what we will learn in future lessons. First mention what we will learn in next lesson, which is Lesson 10." bullet="adjacent_trends">Lesson 10 memory transition required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Detailed transition to Lesson 10 on Memory for Agents, explaining how short-term and long-term memory systems complement RAG's on-demand retrieval." bullet="adjacent_concepts">Explicit depth on memory complement.</orphan>
    <orphan route="depth" anchor="Lightly preview other relevant future topics touched here (e.g., evaluations for retrieval quality and monitoring in production) and note they’ll be covered later in the course." bullet="adjacent_trends">Production monitoring preview required.</orphan>
    <orphan route="depth" anchor="Must cover in depth: Light preview of future topics like retrieval quality evaluations and production monitoring, highlighting their importance for maintaining high-performing RAG systems." bullet="adjacent_trends">Explicit depth on evaluations and monitoring.</orphan>
  </orphan_anchors>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction-giving-llms-an-open-book-exam" need_depth="23" need_breadth="7" target_words="650" mandatory_bullets="9" must_cover_depth="2" must_stay_brief="2"/>
  <section id="S2::section-2-the-rag-system-core-components" need_depth="32" need_breadth="4" target_words="600" mandatory_bullets="4" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S3::section-3-the-rag-pipeline-ingestion-and-retrieval" need_depth="58" need_breadth="4" target_words="800" mandatory_bullets="8" must_cover_depth="6" must_stay_brief="0"/>
  <section id="S4::section-4-advanced-rag-techniques" need_depth="26" need_breadth="2" target_words="1100" mandatory_bullets="7" must_cover_depth="2" must_stay_brief="0"/>
  <section id="S5::section-5-agentic-rag" need_depth="33" need_breadth="2" target_words="700" mandatory_bullets="6" must_cover_depth="2" must_stay_brief="1"/>
  <section id="S6::section-6-conclusion" need_depth="34" need_breadth="3" target_words="350" mandatory_bullets="5" must_cover_depth="4" must_stay_brief="0"/>
  <overall>
    <weakest_sections>S6::section-6-conclusion, S3::section-3-the-rag-pipeline-ingestion-and-retrieval</weakest_sections>
    <strongest_sections>S4::section-4-advanced-rag-techniques, S1::section-1-introduction-giving-llms-an-open-book-exam</strongest_sections>
    <dominant_gap_type>depth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>