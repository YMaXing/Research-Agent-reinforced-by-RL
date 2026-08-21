<digest_meta>
  <article_title>Retrieval-Augmented Generation (standard variant)</article_title>
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
| A12 | what-is-agentic-rag | table | vanilla,agentic | 6 | \| \| Vanilla LLM RAG \| Agentic RAG \| |
</artefact_registry>

<sources>
<s slug="a-complete-guide-to-rag" type="golden_web">Retrieval-Augmented Generation (RAG) augments a base LLM (e.g., OpenAI) with external retrieval over proprietary documents, rules, and data instead of retraining. The architecture splits into a Retriever that returns relevant passages from a vector store and a Generator (LLM) that synthesizes an answer from those passages. The source presents a minimal Python implementation using LangChain: BSHTMLLoader loads Tolstoy’s “War and Peace,” OpenAIEmbeddings produce vectors, Qdrant.from_documents stores them in-memory, and RetrievalQA (chain_type="stuff") performs retrieval-augmented answering in a loop. Query preprocessing converts arbitrary user input into searchable form via LLM reformulation; RAG Fusion extends this by generating multiple query variants, retrieving from each, and re-ranking the union with a Cross-Encoder. The guide contrasts Bi-Encoders with Cross-Encoders that score pairwise relevance more accurately and are applied only at re-ranking time. Data search relies on vector databases: Qdrant, Pinecone, Chroma, Weaviate, Milvus, FAISS, plus pgvector and MongoDB Atlas. EnsembleRetriever combines sparse (BM25Retriever, TF-IDF) and dense retrievers with Reciprocal Rank Fusion. RELP variant uses retrieved passages as few-shot examples rather than direct context. Additional techniques include classification of query type and AutoRAG. Ranking and evaluation sections detail Cross-Encoder re-ranking, RRF, and LLM-based ranking. Retrieval quality is measured with P@K, AP@K, MAP@K, and NDCG@K. Response evaluation inspects token-level logits to detect low-confidence hallucinations. Fine-tuning via LoRA is noted but out of scope. FLARE is described at high level.</s>
<s slug="advanced-rag-blueprint-optimize-llm-retrieval-systems" type="golden_web">The source addresses limitations of vanilla RAG and details optimization techniques under the label advanced RAG, organized into pre-retrieval, retrieval, and post-retrieval stages. Vanilla RAG fails to ensure relevance of retrieved documents, sufficiency of context, absence of noise, acceptable latency, or fallback behavior. Pre-retrieval optimizations cover data indexing and query optimization. Data indexing methods include sliding window, enhancing data granularity, metadata tagging, optimizing index structures, and small-to-big. Query optimization techniques comprise query routing, query rewriting, Hypothetical Document Embeddings (HyDE), query expansion, and self-query. Retrieval optimizations target embedding models and database search. Embedding improvements include domain-specific fine-tuning or instructor models. Database techniques are hybrid search and filtered vector search. Post-retrieval optimizations consist of prompt compression and re-ranking. The source notes that re-ranking is applied after initial vector retrieval because of its higher cost. No quantitative benchmarks are reported.</s>
<s slug="from-local-to-global-a-graphrag-approach-to-query-focused-su" type="golden_web">Retrieval-Augmented Generation (standard variant), termed vector RAG in the source, retrieves a fixed number of text records semantically similar to a user query via text embeddings and vector-space similarity, then populates a prompt template with the query plus those records for an LLM to generate a response. It is designed for cases where the external corpus exceeds the LLM context window and performs well only on localized fact-retrieval queries. The source contrasts it explicitly with global sensemaking queries that require corpus-wide understanding of entity connections. Vector RAG cannot support these because retrieval is limited to individually relevant records rather than holistic structure. It is implemented in the evaluation as condition SS. Key supporting data include two ~1 M–1.7 M token corpora. Across 125 LLM-generated global sensemaking questions per corpus, vector RAG was outperformed by all global methods on comprehensiveness and diversity. Exact techniques named: text embeddings, semantic similarity retrieval, map-reduce summarization. Limitations stated: evaluation confined to two ~1 M-token English corpora and sensemaking questions.</s>
<s slug="rag-fundamentals-first-by-paul-iusztin-decoding-ml" type="golden_web">Retrieval-Augmented Generation (RAG) enhances LLM outputs by retrieving external data, augmenting the prompt, and generating responses. The source explains that LLMs rely on parameterized knowledge which fails on post-cutoff events and leads to hallucinations. RAG addresses hallucinations by forcing answers based solely on retrieved context as the single source of truth and solves access to old, private, or rapidly changing data without retraining. The vanilla RAG framework comprises three independent modules: the ingestion pipeline, the retrieval pipeline, and the generation pipeline. The source includes a diagram of the vanilla RAG architecture and the cosine distance formula. Coverage is limited to the naive variant.</s>
<s slug="what-is-retrieval-augmented-generation-aka-rag" type="golden_web">Retrieval-Augmented Generation (RAG) is a technique that augments LLMs with external knowledge retrieval to improve accuracy, grounding, and citation of sources. The term originated in the 2020 paper “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks”. Core workflow: an embedding model converts the user query into a vector, compares it against a vector database of a knowledge base, retrieves matching passages, and supplies them to the LLM. RAG supports use cases such as medical assistants, financial market-data tools, customer support. Adopters include AWS, IBM, Glean, Google, Microsoft, NVIDIA, Oracle, and Pinecone. Historical precursors include 1970s NLP-based question-answering systems, the mid-1990s Ask Jeeves service, and IBM Watson’s 2011 Jeopardy! demonstration.</s>
<s slug="build-advanced-retrieval-augmented-generation-systems" type="exploitation">The source details construction of production-ready retrieval-augmented generation (RAG) systems, contrasting naive RAG with advanced RAG that adds preprocessing and post-processing stages. It organizes work into three phases—ingestion, inference pipeline, and evaluation. Ingestion covers content preprocessing and extraction, chunking strategy, chunking organization, alignment optimization, and update strategies. Inference pipeline addresses query preprocessing, subqueries, query router, post-retrieval steps, and post-completion steps. Evaluation discusses user-feedback capture, assessment pipelines, golden datasets, harms modeling, and red-teaming. The source references four pipeline diagrams and links to Azure samples.</s>
<s slug="introducing-contextual-retrieval" type="exploitation">Contextual Retrieval improves standard RAG retrieval accuracy for large knowledge bases by prepending concise, chunk-specific explanatory context to each chunk before embedding and BM25 indexing. Standard RAG is described as chunking a corpus, generating embeddings plus TF-IDF/BM25 representations, retrieving via semantic similarity and lexical matching, fusing results, and appending top-K chunks to prompts. The method uses two techniques—Contextual Embeddings and Contextual BM25—plus optional reranking. Experiments across codebases, fiction, ArXiv, and science papers report: Contextual Embeddings alone cut top-20 failure rate by 35%; combined Contextual Embeddings + Contextual BM25 by 49%; adding Cohere reranker by 67%.</s>
<s slug="rag-is-dead-long-live-agentic-retrieval" type="exploitation">RAG has evolved from naive top-k chunk retrieval in vector databases to agentic strategies. The source covers terminology including hybrid search, CRAG, Self-RAG, HyDE, deep research, reranking, multi-modal embeddings, and RAPTOR. Core retrieval modes in LlamaParseIndex are chunk, files_via_metadata, files_via_content, and auto_routed. For multiple knowledge bases, LlamaParseCompositeRetriever with CompositeRetrievalMode.ROUTED accepts per-index name and description strings. The full agentic system stacks LLM-based index selection at the composite layer with auto_routed mode at each sub-index.</s>
<s slug="the-rise-of-rag" type="exploitation">RAG (Retrieval-Augmented Generation) was introduced in the 2020 Meta paper. It augments LLM generation by retrieving external information to mitigate knowledge cutoffs and hallucinations. The system comprises retrieval of relevant data from documents, databases, or multimedia followed by generation that conditions the LLM on the retrieved content plus the user prompt. Retrieval is performed via chunk-based semantic similarity on unstructured data. Enhancements include hierarchical chunking, metadata filtering, hybrid search, Anthropic's Contextual Retrieval, custom-trained embedding models with rerankers, and GraphRAG. RAG is contrasted with long-context models such as Gemini 1.5. Future directions include agentic systems that decompose queries, launch parallel or sequential retrievals, and detect missing information before generation.</s>
<s slug="what-is-agentic-rag-1" type="exploitation">Standard RAG connects a generative AI model to an external knowledge base so that retrieved context augments user queries before LLM generation. The pipeline uses two models: an embedding model paired with a vector database for retrieval, and an LLM for response generation. The source contrasts standard RAG with agentic RAG to highlight baseline limits. Standard systems connect to a single external dataset, remain reactive, require extensive prompt engineering, and perform no self-validation or iterative optimization. They cannot route across multiple sources, plan multistep workflows, or call external tools.</s>
<s slug="what-is-agentic-rag" type="exploitation">Retrieval-Augmented Generation (RAG) is a technique that augments an LLM with an external knowledge source at inference time. A naive pipeline consists of a retrieval component—typically an embedding model paired with a vector database—and a generative component. At inference time the user query triggers a similarity search over indexed documents; the most similar passages are returned and concatenated into the LLM prompt. The source explicitly states two limitations of this one-shot architecture: it accesses only a single external knowledge source and performs retrieval once without reasoning or validation of result quality. It contrasts this with ReAct-style agents that add planning, tool use, memory, and iterative loops.</s>
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
  <intent>Introduce the core problem of static LLM knowledge and position standard RAG as the open-book solution within Context Engineering.</intent>
  <depth_checklist depth_score="3">
    <item name="motivation" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="theoretical_foundations" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="4">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="historical_context" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="enabling_technologies" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="industry_applications" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="5" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="Quick reference to what we've learned in previous lessons: Take the core ideas of what we've learned in previous lessons" bullet="motivation">Directly supports motivation for Context Engineering recall.</orphan>
    <orphan route="depth" anchor="Transition to what we'll learn in this lesson: After presenting what we learned in the past, make a transition to what w" bullet="motivation">Sets up lesson motivation.</orphan>
    <orphan route="depth" anchor="Additional guidance:" bullet="motivation">Frames core problem definition.</orphan>
    <orphan route="depth" anchor="Start by informing readers of a core problem: LLMs are trained on a fixed dataset, making their knowledge static and pro" bullet="motivation">Matches explicit motivation item.</orphan>
    <orphan route="depth" anchor="Introduce RAG as a reliable solution to this problem, we can insert new knowledge using the context window" bullet="theoretical_foundations">Direct theoretical foundation for RAG.</orphan>
    <orphan route="breadth" anchor="With RAG, we are giving the LLM an "open-book exam" by connecting it to external, real-time knowledge sources. Like huma" bullet="cross_domain_analogies">Explicit human analogy from outside core mechanism.</orphan>
    <orphan route="breadth" anchor="We'll contrast retrieval with agent memory in Lesson 10 (next one), where we discuss short- and long-term memory stores" bullet="adjacent_concepts">Connects to adjacent future topic.</orphan>
    <orphan route="breadth" anchor="Clarify that RAG is a tool/method, AI Engineers use/implement in the process of "Context Engineering" taught in lesson 0" bullet="enabling_technologies">Links to broader enabling process.</orphan>
    <orphan route="unreachable" anchor="Briefly outline the lesson's journey: from the "what" and "how" of basic RAG to the advanced and agentic patterns." bullet="motivation">Pure structural outline not present in sources.</orphan>
  </orphan_anchors>
</section>
<section id="S2::section-2-the-rag-system-core-components" self_contained="yes" sources="advanced-rag-blueprint-optimize-llm-retrieval-systems,a-complete-guide-to-rag,build-advanced-retrieval-augmented-generation-systems" artefacts="">
  <intent>Decompose standard RAG into the three conceptual pillars of retrieval, augmentation, and generation.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="theoretical_foundations" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="technical_nuances" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="1">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="6" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Understanding these components is the first step in the Context Engineering process (Lesson 03) of designing effective R" bullet="motivation">Direct motivation tie-in.</orphan>
    <orphan route="depth" anchor="Break down RAG into three conceptual pillars:" bullet="theoretical_foundations">Core theoretical decomposition.</orphan>
    <orphan route="depth" anchor="Retrieval: The engine/system for finding relevant information. Semantic similarity or keyword-based search (BM25) is oft" bullet="technical_nuances">Technical detail on retrieval pillar.</orphan>
    <orphan route="depth" anchor="Augmentation: The process of taking the retrieved information and formatting it into the context of a prompt for the LLM" bullet="technical_nuances">Technical detail on augmentation pillar.</orphan>
    <orphan route="depth" anchor="Generation: The final step where the LLM uses the augmented input to generate an answer grounded in the provided data." bullet="technical_nuances">Technical detail on generation pillar.</orphan>
    <orphan route="depth" anchor="Include a Mermaid diagram that illustrates the flow between the user's query, the Retriever, the Augmentation step, and" bullet="technical_nuances">Diagram supports technical flow nuance.</orphan>
  </orphan_anchors>
</section>
<section id="S3::section-3-the-rag-pipeline-ingestion-and-retrieval" self_contained="yes" sources="introducing-contextual-retrieval,from-local-to-global-a-graphrag-approach-to-query-focused-su,rag-fundamentals-first-by-paul-iusztin-decoding-ml" artefacts="">
  <intent>Detail the two-phase offline ingestion and online retrieval workflow of standard RAG.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="theoretical_foundations" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="technical_nuances" present="yes" evidence="introducing-contextual-retrieval"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="1">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="12" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Detail the end-to-end RAG workflow, splitting it into its two distinct phases." bullet="technical_nuances">Core technical workflow detail.</orphan>
    <orphan route="depth" anchor="Phase 1: Offline Ingestion & Indexing" bullet="technical_nuances">Technical phase detail.</orphan>
    <orphan route="depth" anchor="Load: Reading documents from various sources (PDFs, websites, APIs). Example tools: Unstructured, LangChain document loa" bullet="technical_nuances">Implementation nuance for load step.</orphan>
    <orphan route="depth" anchor="Split: Breaking content into smaller, meaningful pieces with rule-based or semantic chunkers (avoid cutting mid-idea). E" bullet="technical_nuances">Implementation nuance for split step.</orphan>
    <orphan route="depth" anchor="Embed: Using an embedding model to convert each chunk into a vector embedding. Example models: OpenAI text-embedding-3-l" bullet="technical_nuances">Implementation nuance for embed step.</orphan>
    <orphan route="depth" anchor="Store: Loading the embeddings and their corresponding text into a vector database or search index for fast similarity lo" bullet="technical_nuances">Implementation nuance for store step.</orphan>
    <orphan route="depth" anchor="Phase 2: Online Retrieval & Generation" bullet="technical_nuances">Technical phase detail.</orphan>
    <orphan route="depth" anchor="Query: A user asks a question; optionally normalize or expand it. Example: LangChain `Runnable` chain or LlamaIndex `Que" bullet="technical_nuances">Implementation nuance for query step.</orphan>
    <orphan route="depth" anchor="Embed: Turn the query into a vector with the same embedding model as indexing." bullet="technical_nuances">Technical nuance for query embed.</orphan>
    <orphan route="depth" anchor="Search: The query vector is used to find the top-k most similar document chunks in the vector database. Example: vector" bullet="technical_nuances">Technical nuance for search step.</orphan>
    <orphan route="depth" anchor="Generate: Build a prompt that includes the user query, instructions, and retrieved chunks; call the LLM to produce a gro" bullet="technical_nuances">Technical nuance for generate step.</orphan>
    <orphan route="depth" anchor="Include a more detailed Mermaid diagram showing both offline and online paths, tools (generic, not vendor-specific)." bullet="technical_nuances">Diagram supports technical pipeline nuance.</orphan>
  </orphan_anchors>
</section>
<section id="S4::section-4-advanced-rag-techniques" self_contained="yes" sources="what-is-agentic-rag-1,rag-is-dead-long-live-agentic-retrieval,advanced-rag-blueprint-optimize-llm-retrieval-systems" artefacts="">
  <intent>Explore advanced retrieval techniques that improve standard RAG quality on real-world data.</intent>
  <depth_checklist depth_score="7">
    <item name="motivation" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="theoretical_foundations" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="technical_nuances" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="latest_advancements" present="yes" evidence="introducing-contextual-retrieval"/>
    <item name="limitations_failure_modes" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="implementation_tradeoffs" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="case_studies_metrics" present="yes" evidence="introducing-contextual-retrieval"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="rag-is-dead-long-live-agentic-retrieval"/>
  </breadth_checklist>
  <orphan_anchors n_depth="10" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="Dedicate this section to exploring methods that significantly improve retrieval performance." bullet="motivation">Direct motivation for advanced techniques.</orphan>
    <orphan route="depth" anchor="Hybrid Search: Combining keyword-based search (like BM25) for precision with vector search for capturing semantic meanin" bullet="technical_nuances">Technical nuance of hybrid search.</orphan>
    <orphan route="depth" anchor="What/Why: Pair BM25 precision on exact terms with vector search to capture paraphrases." bullet="theoretical_foundations">Theoretical rationale for hybrid.</orphan>
    <orphan route="depth" anchor="Re-ranking: Using a second "re-ranker" model (e.g., a cross-encoder, Cohere Rerank) to re-order the initial retrieved do" bullet="technical_nuances">Technical nuance of re-ranking.</orphan>
    <orphan route="depth" anchor="What/Why: A second model scores (query, candidate) pairs for relevance, improving ordering." bullet="theoretical_foundations">Theoretical rationale for re-ranking.</orphan>
    <orphan route="depth" anchor="Query Transformations:" bullet="technical_nuances">Technical category of transformations.</orphan>
    <orphan route="depth" anchor="Decomposition: Break a complex query into sub-questions, retrieve per sub-question, then merge." bullet="technical_nuances">Technical nuance of decomposition.</orphan>
    <orphan route="depth" anchor="HyDE (Hypothetical Document Expansion): Generate a short, ideal answer draft, embed it, then search." bullet="technical_nuances">Technical nuance of HyDE.</orphan>
    <orphan route="depth" anchor="Advanced Chunking Strategies: Moving beyond fixed-size chunks to methods that preserve more context, such as semantic ch" bullet="technical_nuances">Technical nuance of chunking.</orphan>
    <orphan route="depth" anchor="Fixed chunks: Splitting a 20-page handbook every 500 words might cut the "Reimbursements" section in half, so you get a" bullet="limitations_failure_modes">Failure mode of fixed chunks.</orphan>
    <orphan route="depth" anchor="Semantic chunks: Splitting by headings keeps the whole "Reimbursements" section together, so the exact numbers and excep" bullet="technical_nuances">Technical benefit of semantic chunks.</orphan>
    <orphan route="depth" anchor="Layout-aware (tables and forms):" bullet="technical_nuances">Technical nuance of layout-aware chunking.</orphan>
    <orphan route="depth" anchor="GraphRAG: Introducing retrieval from knowledge graphs. Explain that this technique excels at answering questions about c" bullet="technical_nuances">Technical nuance of GraphRAG.</orphan>
    <orphan route="depth" anchor="Fixed chunks: Splitting a 20-page handbook every 500 words might cut the "Reimbursements" section in half, so you get a" bullet="limitations_failure_modes">Repeated failure-mode example.</orphan>
    <orphan route="depth" anchor="Semantic chunks: Splitting by headings keeps the whole "Reimbursements" section together, so the exact numbers and excep" bullet="technical_nuances">Repeated technical benefit.</orphan>
    <orphan route="breadth" anchor="GraphRAG: Introducing retrieval from knowledge graphs. Explain that this technique excels at answering questions about c" bullet="adjacent_trends">Connects to emerging GraphRAG trend outside core vector RAG.</orphan>
  </orphan_anchors>
</section>
<section id="S5::section-5-agentic-rag" self_contained="yes" sources="what-is-agentic-rag,what-is-retrieval-augmented-generation-aka-rag,what-is-agentic-rag-1" artefacts="">
  <intent>Contrast standard linear RAG with adaptive agentic RAG that treats retrieval as one tool inside a ReAct loop.</intent>
  <depth_checklist depth_score="6">
    <item name="motivation" present="yes" evidence="what-is-agentic-rag"/>
    <item name="theoretical_foundations" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="technical_nuances" present="yes" evidence="what-is-agentic-rag"/>
    <item name="latest_advancements" present="yes" evidence="what-is-agentic-rag"/>
    <item name="limitations_failure_modes" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="yes" evidence="A12"/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="what-is-agentic-rag"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="what-is-agentic-rag"/>
  </breadth_checklist>
  <orphan_anchors n_depth="7" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Tie directly to Lessons 7–8 (ReAct). Emphasize: Agentic RAG is essentially a ReAct-style agent equipped with a retrieval tool. The agent reasons (Thought), decides an Action (e.g., retrieve), observes results, and iterates." bullet="theoretical_foundations">Core theoretical distinction.</orphan>
    <orphan route="depth" anchor="Clarify: agents typically use many tools (web search, code execution, databases). Labeling a whole system “agentic RAG” can be too narrow—the retrieval tool is just one of several." bullet="limitations_failure_modes">Limitation of narrow labeling.</orphan>
    <orphan route="depth" anchor="First, define the core distinction (the theoretical part):" bullet="theoretical_foundations">Theoretical distinction item.</orphan>
    <orphan route="depth" anchor="Standard RAG: A linear, pre-determined workflow. It's powerful but rigid. Every query follows the same Path: Retrieve -> Augment -> Generate." bullet="technical_nuances">Technical contrast detail.</orphan>
    <orphan route="depth" anchor="Agentic RAG: Adaptive and iterative. The agent decides when to retrieve, how to reformulate, which source to search, and whether to chain multiple retrieval and reasoning steps." bullet="technical_nuances">Technical contrast detail.</orphan>
    <orphan route="depth" anchor="Explain the capabilities of an agentic approach:" bullet="technical_nuances">Technical capabilities detail.</orphan>
    <orphan route="depth" anchor="Then, show (conceptually) it in action:" bullet="technical_nuances">Action illustration detail.</orphan>
  </orphan_anchors>
</section>
<section id="S6::section-6-conclusion" self_contained="yes" sources="from-local-to-global-a-graphrag-approach-to-query-focused-su,the-rise-of-rag,a-complete-guide-to-rag" artefacts="">
  <intent>Summarize RAG benefits, position it as foundational Context Engineering skill, and preview next lessons.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="the-rise-of-rag"/>
    <item name="theoretical_foundations" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="yes" evidence="the-rise-of-rag"/>
    <item name="limitations_failure_modes" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="5">
    <item name="adjacent_concepts" present="yes" evidence="the-rise-of-rag"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="the-rise-of-rag"/>
    <item name="enabling_technologies" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="industry_applications" present="yes" evidence="the-rise-of-rag"/>
    <item name="adjacent_trends" present="yes" evidence="the-rise-of-rag"/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction-giving-llms-an-open-book-exam" need_depth="20" need_breadth="5" target_words="565" mandatory_bullets="8" must_cover_depth="0" must_stay_brief="2"/>
  <section id="S2::section-2-the-rag-system-core-components" need_depth="22" need_breadth="5" target_words="465" mandatory_bullets="5" must_cover_depth="0" must_stay_brief="1"/>
  <section id="S3::section-3-the-rag-pipeline-ingestion-and-retrieval" need_depth="40" need_breadth="5" target_words="625" mandatory_bullets="10" must_cover_depth="8" must_stay_brief="0"/>
  <section id="S4::section-4-advanced-rag-techniques" need_depth="31" need_breadth="7" target_words="910" mandatory_bullets="7" must_cover_depth="5" must_stay_brief="0"/>
  <section id="S5::section-5-agentic-rag" need_depth="23" need_breadth="3" target_words="395" mandatory_bullets="9" must_cover_depth="3" must_stay_brief="1"/>
  <section id="S6::section-6-conclusion" need_depth="4" need_breadth="1" target_words="210" mandatory_bullets="4" must_cover_depth="0" must_stay_brief="1"/>
  <overall>
    <weakest_sections>S4::section-4-advanced-rag-techniques, S3::section-3-the-rag-pipeline-ingestion-and-retrieval</weakest_sections>
    <strongest_sections>S6::section-6-conclusion, S1::section-1-introduction-giving-llms-an-open-book-exam</strongest_sections>
    <dominant_gap_type>depth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>