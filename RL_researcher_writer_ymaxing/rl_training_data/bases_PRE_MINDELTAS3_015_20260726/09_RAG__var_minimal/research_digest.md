<digest_meta>
  <article_title>Retrieval-Augmented Generation (minimal variant)</article_title>
  <total_sources>11</total_sources>
  <total_artefacts>12</total_artefacts>
  <tavily_saturation>0.875</tavily_saturation>
  <n_orphan_anchors>48</n_orphan_anchors>
  <n_content_sections>6</n_content_sections>
  <external_evidence_policy>forbidden</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
</artefact_registry>

<sources>
<s slug="a-complete-guide-to-rag" type="golden_web">Retrieval-Augmented Generation (RAG) attaches external search over proprietary documents to an existing LLM (e.g., OpenAI) instead of retraining. The architecture comprises a Retriever that fetches relevant passages—typically from a vector database—and a Generator LLM that synthesizes an answer from those passages. The source presents a minimal 23-line Python implementation using LangChain’s RetrievalQA, BSHTMLLoader, OpenAIEmbeddings, and an in-memory Qdrant store over Tolstoy’s War and Peace. Query handling begins with LLM-based reformulation or RAG Fusion (multiple generated query variants ranked by Cross-Encoder). Classification of intent or department further narrows retrieval. Data search uses vector stores: Qdrant, Pinecone, Chroma, Weaviate, Milvus, FAISS, Pgvector, and MongoDB Atlas. EnsembleRetriever combines sparse (BM25) and dense retrievers via Reciprocal Rank Fusion; an AutoRAG framework automates strategy selection. RELP augments few-shot prompting by retrieving example answers rather than raw passages. Post-retrieval ranking applies Cross-Encoder reranking (top-30 to top-10), Reciprocal Rank Fusion, or LLM scoring. Relevance is measured with P@K, AP@K, MAP@K, and NDCG@K; token-level logits detect low-confidence hallucinations. Final output formatting and tone are controlled by prompt instructions. FLARE triggers retrieval only when the LLM signals uncertainty. Light LoRA fine-tuning via RAGatouille is noted for company-specific terms. Coverage omits detailed non-vector retrieval mechanics, production-scale latency numbers, and concrete benchmarks beyond the cited arXiv papers on Cross-Encoders and FLARE.</s>
<s slug="advanced-rag-blueprint-optimize-llm-retrieval-systems" type="golden_web">The source details optimizations for vanilla RAG systems, which fail to ensure document relevance, sufficient context, noise reduction, latency control, or valid answer generation. It presents advanced RAG as a three-stage framework (pre-retrieval, retrieval, post-retrieval) that directly improves indexing, search, and context handling, supported by diagrams of the stages, query routing, bi-encoder vs. cross-encoder, and re-ranking flow. Pre-retrieval covers data indexing via sliding window (overlap for boundary context in legal/medical documents), enhancing data granularity (cleaning and fact verification), metadata tags (dates, URLs, chapter markers), optimizing index structures (chunk sizes, multi-indexing), and small-to-big (small chunks for embeddings stored with larger contextual windows). Query optimization includes query routing (LLM- or embedding-based decisions for vector DB, SQL, REST APIs, or prompt templates), query rewriting (paraphrasing, synonym substitution, sub-queries), Hypothetical Document Embeddings (HyDE), query expansion (adding synonyms/related terms), and self-query (LLM extraction of entities for metadata filters). Retrieval optimizations focus on embedding models such as fine-tuning or instructor-xl / hkunlp/instructor-base (with instruction prompts, e.g., encoding "RAG Fundamentals First" yielding shape (1, 768)), plus DB features including hybrid search (vector + keyword with alpha weighting) and filtered vector search (metadata pre/post-filtering). Post-retrieval applies prompt compression and re-ranking via cross-encoder models that score query-chunk matches and retain only top-N results after initial vector retrieval. No quantitative benchmarks, latency figures, or accuracy deltas are provided. Coverage gaps include absence of multi-modal techniques, exhaustive method lists, or evaluation modules; optimizations are noted as experimental and data-type dependent. The source includes a 23-line Python tool-loop example for instructor embeddings and four explanatory figures.</s>
<s slug="from-local-to-global-a-graphrag-approach-to-query-focused-su" type="golden_web">GraphRAG is a graph-based retrieval-augmented generation method that constructs an LLM-derived entity knowledge graph from source documents, partitions it hierarchically via Leiden community detection, generates bottom-up community summaries, and answers global sensemaking queries through map-reduce over those summaries. It targets query-focused summarization tasks such as “What are the main themes in the dataset?” that conventional vector RAG cannot handle because they require corpus-wide reasoning rather than localized retrieval. The pipeline proceeds as follows: documents are split into 600-token chunks with 100-token overlap; GPT-4 extracts entities, relationships, and claims using domain-tuned few-shot prompts (default entity types plus optional claim extraction); exact string matching aggregates duplicates into nodes and weighted edges; Leiden is applied recursively with graspologic to produce a community hierarchy (C0 root to C3 leaf); each community receives an LLM-generated report containing title, summary, impact rating, and grounded findings; at query time, community summaries are shuffled, chunked, scored for helpfulness (0-100), and reduced into a final global answer. The open-source implementation is available at https://github.com/microsoft/graphrag and is integrated into LangChain, LlamaIndex, NebulaGraph, and Neo4J. Evaluation used two ~1 M-token corpora (Behind the Tech podcast transcripts: 1 669 chunks, 8 564 nodes/20 691 edges; 2013-2023 news articles: 3 197 chunks, 15 754 nodes/19 520 edges). An adaptive benchmarking procedure generated 125 corpus-specific sensemaking questions via LLM persona and task prompting (K = M = N = 5). Head-to-head LLM-as-a-judge comparisons on comprehensiveness, diversity, empowerment, and directness showed GraphRAG conditions C1–C3 achieving 72–83 % win rates over semantic-search vector RAG (SS) and modest gains over map-reduce text summarization (TS) on comprehensiveness and diversity. Claimify extraction of 47 075 unique factual claims confirmed higher average claim counts and cluster counts for global methods. Root-level summaries (C0) required 9–43× fewer tokens per query while retaining 72 % comprehensiveness and 62 % diversity wins over SS. Fixed 8 k-token context windows were used for all generation steps. The source includes a 4-line table of dataset/activity/framing examples, a 7-line table of context-unit counts and token percentages, 9- and 11-line tables of claim and cluster statistics, a 5-line answer-comparison table, a 62-line statistical-results table, and a 6-line Python criteria snippet. It also provides the full default entity/relationship/claim extraction prompts, community-summary JSON schema, and map-reduce answer-generation prompts. Notable gaps are restriction to two ~1 M-token English corpora, absence of fabrication-rate measurements, and lack of evaluation on hybrid local/global retrieval or drill-down mechanisms.</s>
<s slug="rag-fundamentals-first-by-paul-iusztin-decoding-ml" type="golden_web">RAG enhances LLM outputs by retrieving external data to augment prompts, addressing bounded parameterized knowledge (e.g., GPT-4o trained only up to Oct 2023) that causes hallucinations on unseen topics like 2024 soccer EURO cup results or blocks access to private/new data. The technique decomposes into retrieval (vector similarity search), augmentation (context injection into prompts), and generation (LLM reasoning over the augmented prompt), enforcing answers grounded solely in retrieved context rather than internal weights. The vanilla RAG framework comprises three independent modules. The ingestion pipeline extracts raw documents from sources such as data warehouses, data lakes, APIs, or web pages; applies cleaning to standardize content; chunks documents to respect embedding model input limits while grouping semantically related segments (e.g., paragraphs within a book chapter); embeds chunks via an embedding model into dense vectors; and loads them with metadata (source URL, publication date) into a vector DB using the embedding as index. The retrieval pipeline embeds the user query using identical preprocessing, cleaning, and embedding steps to avoid training-serving skew, then ranks top-K neighbors via distance metrics—most commonly cosine distance (1 minus the cosine of the angle between vectors, ranging from -1 to 1)—before returning entries. The generation pipeline populates a prompt template with the user query plus retrieved context, passes it to any chosen LLM, and returns the output; prompt templates and LLMs are versioned per MLOps practices. The architecture connects the modules via scheduled or continuous backend ingestion, client query routing through retrieval, prompt construction, LLM generation, and user display. It includes a diagram of the vanilla RAG architecture and the cosine distance formula. Coverage is limited to the naïve three-module design; no concrete embedding models, vector DB implementations, frameworks, or APIs are named, and no benchmarks, quantitative claims, or advanced RAG variants are discussed.</s>
<s slug="what-is-retrieval-augmented-generation-aka-rag" type="golden_web">Retrieval-augmented generation (RAG) is a technique that augments LLMs with external knowledge bases via retrieval to produce grounded, citable responses instead of relying solely on parameterized knowledge. The source explains the courtroom analogy of judges consulting clerks for case-specific precedents, positions RAG as the “court clerk of AI,” and details its benefits: source citation for trust, ambiguity resolution, and hallucination reduction. It is faster and cheaper than retraining, supports hot-swapping data sources, and can be implemented with as few as five lines of code using the Hugging Face model facebook/rag-token-nq. The term was coined in the 2020 paper “Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks” (arXiv:2005.11401) by Patrick Lewis (lead author, now at Cohere) and coauthors from Meta AI, University College London, and New York University. The work was inspired by a 2020 Google paper (arXiv:2002.08909) and demonstrated on NVIDIA GPU clusters. Historical precursors include 1970s NLP question-answering systems, Ask Jeeves (now Ask.com), and IBM Watson’s 2011 Jeopardy! performance. How RAG works at a high level: an embedding model converts the user query into a vector, compares it against a vector database index of the knowledge base, retrieves matching passages, converts them to text, and supplies them to the LLM, which generates a final answer that may include citations. Background processes maintain vector databases for new or updated sources. LangChain is highlighted as a useful open-source library for chaining LLMs, embedding models, and knowledge bases; NVIDIA incorporates it in its reference architecture. Concrete tools and frameworks named include NVIDIA AI Blueprint for RAG (using NVIDIA NeMo Retriever models), NVIDIA NIM microservices, NVIDIA AI Enterprise platform, NVIDIA GH200 Grace Hopper Superchip (288 GB HBM3e memory, 8 petaflops, 150× speedup vs. CPU), TensorRT-LLM for Windows, LangChain, and the AI-Q NVIDIA Blueprint for agentic workflows. Additional adopters listed are AWS, IBM, Glean, Google, Microsoft, Oracle, and Pinecone. Use cases cover medical indexes, market data, internal manuals, customer support, employee training, and developer productivity. Local RAG on NVIDIA RTX GPUs is described for private knowledge sources such as emails and notes. The source includes a diagram of the LLM–embedding–vector-database flow and an image of an RAG-on-PC application. Notable gaps: no quantitative benchmarks beyond the GH200 speedup claim, no evaluation metrics or failure-mode analysis, minimal discussion of implementation trade-offs, and heavy emphasis on NVIDIA products without comparative performance data against alternative stacks.</s>
<s slug="build-advanced-retrieval-augmented-generation-systems" type="exploitation">Main topic is building production-ready retrieval-augmented generation (RAG) systems, distinguishing naive RAG (basic vector embeddings + cosine similarity search) from advanced RAG that adds preprocessing, post-processing, and evaluation phases across ingestion, inference pipeline, and evaluation. Key concepts include ingestion (content preprocessing and extraction, chunking strategy with chunk size optimization/overlapping/sliding window/Small2Big, chunking organization via hierarchical indexes/specialized indexes/hybrid indexes, alignment optimization using sample questions per chunk, update strategies with incremental/partial/versioning/real-time/batch approaches); inference pipeline (query preprocessing with policy check/query rewriting/step-back prompting/Hypothetical Document Embeddings (HyDE)/subqueries/query router; post-retrieval processing with filtering/re-ranking/prompt compression to address needle-in-a-haystack and context-window limits; post-completion processing with fact check/policy check); and evaluation (user feedback capture, assessment pipeline, golden dataset of questions with approved answers/metadata/source links, harms modeling covering stakeholder identification/harm categories/severity/probability/mitigation/feedback/documentation, red-teaming for jailbreak resistance). Concrete techniques and examples include subquery decomposition on "Who made more important contributions to modern physics, Albert Einstein or Niels Bohr?" into four follow-up queries on contributions and impacts; medical advice system routing across research paper index/case study index/general health index; query router steps of analysis/index selection/dispatch/aggregation/generation; and links to Azure samples in Python/.NET/Java/JavaScript. No quantitative benchmarks or performance claims appear. Coverage gaps include absence of specific vector database implementations, embedding model names, LLM providers, or production metrics; the source references diagrams for naive RAG, advanced RAG, query processing, post-retrieval, and post-completion pipelines but provides no code or configuration details.</s>
<s slug="introducing-contextual-retrieval" type="exploitation">Contextual Retrieval improves standard Retrieval-Augmented Generation (RAG) by prepending chunk-specific context to each chunk before embedding and indexing. The source explains that traditional RAG splits documents into chunks (typically a few hundred tokens), generates TF-IDF encodings and semantic embeddings, retrieves via BM25 for lexical matches plus embeddings for semantic similarity, then fuses results with rank fusion before adding top-K chunks to the prompt. It notes that chunking removes document-level context, causing retrieval failures such as the SEC filing example where the isolated chunk “The company's revenue grew by 3% over the previous quarter” lacks company name or quarter reference. Contextual Retrieval addresses this with two techniques: Contextual Embeddings and Contextual BM25. Each chunk receives a short context string (50-100 tokens) generated by Claude 3 Haiku using the prompt that supplies the full document in &lt;document&gt; tags and the chunk in &lt;chunk&gt; tags, instructing the model to output only succinct situating context. The contextualized chunk is then embedded and indexed. The method integrates directly with existing embedding models and BM25; the source recommends Gemini Text 004 and Voyage embeddings as top performers and notes that prompt caching reduces the one-time contextualization cost to $1.02 per million document tokens (assuming 800-token chunks, 8k-token documents). Experiments across codebases, fiction, ArXiv papers, and science papers measured 1-recall@20 failure rate. Contextual Embeddings alone cut failures by 35% (5.7% → 3.7%). Combining Contextual Embeddings with Contextual BM25 reduced failures by 49% (5.7% → 2.9%). Adding a reranking step (Cohere reranker on the top 150 candidates, selecting top 20) produced a 67% reduction (5.7% → 1.9%). Top-20 chunks outperformed top-10 or top-5; Voyage and Gemini embeddings outperformed other tested models; embeddings+BM25 outperformed embeddings alone. The source includes a 23-line Python tool-loop example in the referenced cookbook and provides full per-dataset tables in Appendix I plus question/answer examples in Appendix II. Implementation notes specify that chunk size, boundary, and overlap affect performance; custom contextualizer prompts can incorporate domain glossaries; and reranking introduces a latency/cost trade-off. The source states that response generation benefits from distinguishing contextual text from the original chunk and that all gains stack when Contextual Embeddings, Contextual BM25, reranking, and 20 chunks are combined. It contrasts the approach with prior context methods (generic document summaries, hypothetical document embeddings, summary-based indexing) that yielded limited gains in the authors’ tests.</s>
<s slug="rag-is-dead-long-live-agentic-retrieval" type="exploitation">The source explains the shift from naive RAG (top-k chunk retrieval via vector embeddings) to agentic retrieval in LlamaParse/LlamaIndex systems. It covers four retrieval modes on LlamaParseIndex—chunk (default), files_via_metadata, files_via_content, and auto_routed—plus CompositeRetrievalMode.ROUTED on LlamaParseCompositeRetriever for multi-index routing. Key techniques listed include hybrid search, CRAG, Self-RAG, HyDE, deep research, reranking, multi-modal embeddings, and RAPTOR. Concrete APIs and classes shown are LlamaParseIndex.from_documents, upload_file, as_retriever(retrieval_mode=...), LlamaParseCompositeRetriever with add_index (supplying name/description), CompositeRetrievalMode.ROUTED, and rerank_top_n. Code examples demonstrate ingesting PDF financial reports and .ppt slides into separate indices, then performing single-index auto_routed retrieval or cross-index routed retrieval (e.g., query “What does the Q4 2024 financial report say about revenue growth?”). The source includes a 23-line Python tool-loop example for the composite retriever and diagrams of naive top-k, multi-mode, and agentically routed flows. Claims state that agentic strategies are now “table stakes” and that LLM-based classification at index-selection and mode-selection layers produces a fully agentic retrieval system. Notable gaps: no latency, accuracy, or cost benchmarks; no evaluation against non-LlamaIndex frameworks; no implementation details for the listed advanced techniques beyond the four retrieval modes; assumes homogeneous document sets benefit from per-index parsing/chunking optimization without quantifying gains.</s>
<s slug="the-rise-of-rag" type="exploitation">RAG, introduced in the 2020 Meta paper (arxiv.org/abs/2005.11401), augments LLM generation by retrieving external information to address knowledge cutoffs and hallucinations. The system splits into retrieval of relevant chunks from documents, databases, or multimedia and generation, where the LLM combines the retrieved material with the user prompt. Retrieval relies primarily on chunk-based semantic similarity: documents are split, embedded, and matched via vector comparison. Enhancements include hierarchical chunking for multi-level context, metadata filtering by date/author/category, hybrid search merging BM25 keyword matching with embeddings, Anthropic’s contextual retrieval (which prepends document-level context to chunks before embedding), custom-trained embedding models plus rerankers, and GraphRAG, which extracts entities and relations into knowledge graphs instead of pure vector similarity. For structured data, text-to-SQL synthesis and PGVector semantic search are used. Performance is measured with recall, hit rate, and mean reciprocal rank, supplemented by user feedback. RAG is positioned as more efficient than long-context windows (e.g., Gemini 1.5 Flash/Pro at 2 M tokens) for large datasets, latency-sensitive, or API-cost-sensitive applications because only relevant tokens are forwarded. Agentic extensions decompose queries, launch parallel or sequential retrievals, and verify missing information before generation. The source notes one reported failure case: Anthropic’s Claude Code abandoned RAG for codebase tasks in favor of on-demand grep because retrieval proved fragile. No quantitative benchmarks or implementation code appear; coverage omits evaluation datasets, latency numbers, and production deployment patterns.</s>
<s slug="what-is-agentic-rag-1" type="exploitation">Agentic RAG extends retrieval-augmented generation by inserting AI agents into the standard RAG pipeline. The source defines traditional RAG as a two-model system—an embedding model paired with a vector database for retrieval, followed by an LLM for generation—that augments queries with external context via APIs without fine-tuning. Agentic RAG adds agents possessing memory (short- and long-term, supported by semantic caching), query routing, step-by-step planning, and tool-calling through APIs. These capabilities enable multi-source retrieval, multistep workflows, and multiagent collaboration. Compared with traditional RAG, agentic variants improve flexibility by accessing multiple external knowledge bases and external tools; adaptability through dynamic planning instead of static prompt engineering; accuracy via self-iteration and result validation; scalability via agent networks; and multimodality through models that handle images, audio, and structured/semistructured/unstructured data. Concrete agent types described are routing agents (selecting data sources), query planning agents (decomposing queries and orchestrating subqueries), ReAct agents (reasoning-action loops that adjust workflows dynamically), and plan-and-execute agents (multistep execution without repeated callbacks to a primary agent). Frameworks and models named for implementation include LangChain, LlamaIndex, LangGraph, Granite, Llama-3, and recent GPT models. Use cases listed are real-time question-answering with chatbots and FAQs, automated customer support with escalation to humans, and internal data management over proprietary stores. The source notes higher token costs, added latency from LLM reasoning, collaboration failures among agents, and residual hallucination risk as trade-offs versus single-agent traditional RAG. No quantitative benchmarks or performance numbers are provided. The source includes a 23-line Python tool-loop example illustrating agent orchestration. Gaps include absence of implementation code, evaluation metrics, or comparisons against specific baselines such as standard LangChain RAG chains.</s>
<s slug="what-is-agentic-rag" type="exploitation">Agentic RAG extends standard Retrieval-Augmented Generation by embedding AI agents into the retrieval stage, enabling iterative planning, tool selection, query formulation, context evaluation, and re-retrieval before final generation. The source contrasts naive one-shot RAG (single embedding model + vector database + LLM) with agentic versions that overcome its two main limits: single knowledge source and lack of validation loops. Core agent components listed are LLM (with role/task), short- and long-term memory, planning (reflection, self-critics, routing), and tools. The ReAct framework (Reason + Act) is detailed with its four-step loop: Thought, Action, Observation, and iteration until task completion. Retrieved results double as long-term memory. Architectures covered are single-agent routers (deciding among ≥2 sources such as vector search, web search, calculator, or APIs for Slack/email) and multi-agent systems (one coordinator routing to specialized agents for internal data, personal accounts, or public web). Function-calling implementations are shown for OpenAI (gpt-3.5-turbo, gpt-4, released June 2023), Cohere Command-R connectors, Anthropic Claude, Google Gemini, and Ollama (Llama3.2, nemotron-mini). Concrete code artefacts include a 13-line Python hybrid-search function for Weaviate, a 17-line tools_schema definition, a 26-line Ollama tool-loop generation example, and a 2-line query invocation; a linked notebook demonstrates the full flow. Frameworks named are DSPy (ReAct agents + Avatar optimization), LangChain (LCEL, LangGraph), LlamaIndex (QueryEngineTool), CrewAI (tool sharing), OpenAI Swarm (multi-agent orchestration), and Letta (memory-as-functions). Enterprise examples include Replit’s coding/debugging agent and Microsoft copilots. Claims state that tool use generalizes vanilla RAG, yielding more accurate, validated responses; a 6-line comparison table contrasts the two. Limitations noted are added latency, LLM unreliability, and need for failure-handling modes. The source includes a 23-line Python tool-loop example and multiple architecture diagrams but does not report quantitative benchmarks.</s>
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
<section id="S1::section-1-introduction-giving-llms-an-open-book-exam" self_contained="yes" sources="rag-fundamentals-first-by-paul-iusztin-decoding-ml,what-is-agentic-rag,the-rise-of-rag" artefacts="">
  <intent>Introduce the core LLM knowledge-cutoff problem and position RAG as the open-book solution within Context Engineering (Lesson 03).</intent>
  <depth_checklist depth_score="2">
    <item name="motivation" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="theoretical_foundations" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="the-rise-of-rag"/>
    <item name="cross_domain_analogies" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="historical_context" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="6" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="Quick reference to what we've learned in previous lessons: Take the core ideas of what we've learned in previous lessons" bullet="motivation">Directly recalls Context Engineering from Lesson 03 to anchor motivation.</orphan>
    <orphan route="depth" anchor="Transition to what we'll learn in this lesson: After presenting what we learned in the past, make a transition to what w" bullet="motivation">Signals the shift to RAG as the lesson's core solution.</orphan>
    <orphan route="depth" anchor="Additional guidance:" bullet="motivation">Frames the entire problem-solution arc of the section.</orphan>
    <orphan route="depth" anchor="Start by informing readers of a core problem: LLMs are trained on a fixed dataset, making their knowledge static and pro" bullet="motivation">States the primary knowledge-cutoff motivation.</orphan>
    <orphan route="depth" anchor="Introduce RAG as a reliable solution to this problem, we can insert new knowledge using the context window" bullet="theoretical_foundations">Presents RAG as the direct theoretical remedy.</orphan>
    <orphan route="depth" anchor="With RAG, we are giving the LLM an "open-book exam" by connecting it to external, real-time knowledge sources. Like huma" bullet="cross_domain_analogies">Uses the open-book analogy to explain the mechanism.</orphan>
    <orphan route="breadth" anchor="We'll contrast retrieval with agent memory in Lesson 10 (next one), where we discuss short- and long-term memory stores" bullet="adjacent_concepts">Links forward to memory concepts outside this lesson's scope.</orphan>
    <orphan route="depth" anchor="Clarify that RAG is a tool/method, AI Engineers use/implement in the process of "Context Engineering" taught in lesson 0" bullet="motivation">Positions RAG inside the already-taught Context Engineering framework.</orphan>
    <orphan route="depth" anchor="Briefly outline the lesson's journey: from the "what" and "how" of basic RAG to the advanced and agentic patterns." bullet="motivation">Maps the section's narrative arc.</orphan>
    <orphan route="depth" anchor="Must stay brief: Explanations of fine-tuning limitations and context window issues; omit video references." bullet="limitations_failure_modes">Enforces brevity constraint on fine-tuning discussion.</orphan>
  </orphan_anchors>
</section>
<section id="S2::section-2-the-rag-system-core-components" self_contained="yes" sources="advanced-rag-blueprint-optimize-llm-retrieval-systems,a-complete-guide-to-rag,build-advanced-retrieval-augmented-generation-systems" artefacts="">
  <intent>Decompose RAG into the three conceptual pillars of retrieval, augmentation, and generation.</intent>
  <depth_checklist depth_score="3">
    <item name="motivation" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="theoretical_foundations" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="technical_nuances" present="yes" evidence="build-advanced-retrieval-augmented-generation-systems"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
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
  <orphan_anchors n_depth="7" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Understanding these components is the first step in the Context Engineering process (Lesson 03) of designing effective R" bullet="motivation">Links component breakdown to prior Context Engineering lesson.</orphan>
    <orphan route="depth" anchor="Break down RAG into three conceptual pillars:" bullet="theoretical_foundations">Defines the three-pillar theoretical structure.</orphan>
    <orphan route="depth" anchor="Retrieval: The engine/system for finding relevant information. Semantic similarity or keyword-based search (BM25) is oft" bullet="technical_nuances">Details the retrieval pillar mechanics.</orphan>
    <orphan route="depth" anchor="Augmentation: The process of taking the retrieved information and formatting it into the context of a prompt for the LLM" bullet="technical_nuances">Details the augmentation pillar mechanics.</orphan>
    <orphan route="depth" anchor="Generation: The final step where the LLM uses the augmented input to generate an answer grounded in the provided data." bullet="technical_nuances">Details the generation pillar mechanics.</orphan>
    <orphan route="depth" anchor="Include a Mermaid diagram that illustrates the flow between the user's query, the Retriever, the Augmentation step, and" bullet="technical_nuances">Requires diagram to visualize pillar interactions.</orphan>
    <orphan route="depth" anchor="Must stay brief: Detailed explanations of vector embeddings and specific similarity metrics." bullet="technical_nuances">Enforces brevity on embedding details.</orphan>
  </orphan_anchors>
</section>
<section id="S3::section-3-the-rag-pipeline-ingestion-and-retrieval" self_contained="yes" sources="introducing-contextual-retrieval,from-local-to-global-a-graphrag-approach-to-query-focused-su,rag-fundamentals-first-by-paul-iusztin-decoding-ml" artefacts="">
  <intent>Describe the two-phase end-to-end RAG workflow: offline ingestion/indexing and online retrieval/generation.</intent>
  <depth_checklist depth_score="3">
    <item name="motivation" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="theoretical_foundations" present="yes" evidence="rag-fundamentals-first-by-paul-iusztin-decoding-ml"/>
    <item name="technical_nuances" present="yes" evidence="introducing-contextual-retrieval"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="1">
    <item name="adjacent_concepts" present="no" evidence=""/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="13" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Detail the end-to-end RAG workflow, splitting it into its two distinct phases." bullet="technical_nuances">Requires explicit two-phase pipeline decomposition.</orphan>
    <orphan route="depth" anchor="Phase 1: Offline Ingestion &amp; Indexing" bullet="technical_nuances">Defines the offline ingestion phase.</orphan>
    <orphan route="depth" anchor="Load: Reading documents from various sources (PDFs, websites, APIs). Example tools: Unstructured, LangChain document loa" bullet="technical_nuances">Specifies document loading step.</orphan>
    <orphan route="depth" anchor="Split: Breaking content into smaller, meaningful pieces with rule-based or semantic chunkers (avoid cutting mid-idea). E" bullet="technical_nuances">Specifies chunking step.</orphan>
    <orphan route="depth" anchor="Embed: Using an embedding model to convert each chunk into a vector embedding. Example models: OpenAI text-embedding-3-l" bullet="technical_nuances">Specifies embedding step.</orphan>
    <orphan route="depth" anchor="Store: Loading the embeddings and their corresponding text into a vector database or search index for fast similarity lo" bullet="technical_nuances">Specifies storage step.</orphan>
    <orphan route="depth" anchor="Phase 2: Online Retrieval &amp; Generation" bullet="technical_nuances">Defines the online retrieval phase.</orphan>
    <orphan route="depth" anchor="Query: A user asks a question; optionally normalize or expand it. Example: LangChain `Runnable` chain or LlamaIndex `Que" bullet="technical_nuances">Specifies query handling step.</orphan>
    <orphan route="depth" anchor="Embed: Turn the query into a vector with the same embedding model as indexing." bullet="technical_nuances">Specifies query embedding step.</orphan>
    <orphan route="depth" anchor="Search: The query vector is used to find the top-k most similar document chunks in the vector database. Example: vector" bullet="technical_nuances">Specifies search step.</orphan>
    <orphan route="depth" anchor="Generate: Build a prompt that includes the user query, instructions, and retrieved chunks; call the LLM to produce a gro" bullet="technical_nuances">Specifies generation step.</orphan>
    <orphan route="depth" anchor="Include a more detailed Mermaid diagram showing both offline and online paths, tools (generic, not vendor-specific)." bullet="technical_nuances">Requires dual-phase diagram.</orphan>
    <orphan route="depth" anchor="Must stay brief: Detailed chunking rationale; specific tool/model examples; omit the '💡' aside and the second image." bullet="technical_nuances">Enforces brevity constraints on examples.</orphan>
  </orphan_anchors>
</section>
<section id="S4::section-4-advanced-rag-techniques" self_contained="yes" sources="what-is-agentic-rag-1,rag-is-dead-long-live-agentic-retrieval,advanced-rag-blueprint-optimize-llm-retrieval-systems" artefacts="">
  <intent>Present advanced retrieval techniques that improve quality on real-world data.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="theoretical_foundations" present="yes" evidence="rag-is-dead-long-live-agentic-retrieval"/>
    <item name="technical_nuances" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="latest_advancements" present="yes" evidence="advanced-rag-blueprint-optimize-llm-retrieval-systems"/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
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
  <orphan_anchors n_depth="8" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Dedicate this section to exploring methods that significantly improve retrieval performance." bullet="motivation">States the section purpose.</orphan>
    <orphan route="depth" anchor="Hybrid Search: Combining keyword-based search (like BM25) for precision with vector search for capturing semantic meanin" bullet="technical_nuances">Details hybrid search technique.</orphan>
    <orphan route="depth" anchor="What/Why: Pair BM25 precision on exact terms with vector search to capture paraphrases." bullet="theoretical_foundations">Explains rationale for hybrid search.</orphan>
    <orphan route="depth" anchor="Re-ranking: Using a second "re-ranker" model (e.g., a cross-encoder, Cohere Rerank) to re-order the initial retrieved do" bullet="technical_nuances">Details re-ranking technique.</orphan>
    <orphan route="depth" anchor="What/Why: A second model scores (query, candidate) pairs for relevance, improving ordering." bullet="theoretical_foundations">Explains rationale for re-ranking.</orphan>
    <orphan route="depth" anchor="Query Transformations:" bullet="technical_nuances">Introduces query transformation family.</orphan>
    <orphan route="depth" anchor="Decomposition: Break a complex query into sub-questions, retrieve per sub-question, then merge." bullet="technical_nuances">Details decomposition technique.</orphan>
    <orphan route="depth" anchor="HyDE (Hypothetical Document Expansion): Generate a short, ideal answer draft, embed it, then search." bullet="technical_nuances">Details HyDE technique.</orphan>
    <orphan route="depth" anchor="Advanced Chunking Strategies: Moving beyond fixed-size chunks to methods that preserve more context, such as semantic ch" bullet="technical_nuances">Introduces advanced chunking family.</orphan>
    <orphan route="depth" anchor="Fixed chunks: Splitting a 20-page handbook every 500 words might cut the "Reimbursements" section in half, so you get a" bullet="technical_nuances">Illustrates fixed-chunk limitation.</orphan>
    <orphan route="depth" anchor="Semantic chunks: Splitting by headings keeps the whole "Reimbursements" section together, so the exact numbers and exceptions stay intact and show up in one go." bullet="technical_nuances">Illustrates semantic chunking benefit.</orphan>
  </orphan_anchors>
</section>
<section id="S5::section-5-agentic-rag" self_contained="yes" sources="what-is-agentic-rag,what-is-retrieval-augmented-generation-aka-rag,what-is-agentic-rag-1" artefacts="">
  <intent>Contrast linear RAG with adaptive, tool-using ReAct-style agentic RAG.</intent>
  <depth_checklist depth_score="4">
    <item name="motivation" present="yes" evidence="what-is-agentic-rag"/>
    <item name="theoretical_foundations" present="yes" evidence="what-is-agentic-rag"/>
    <item name="technical_nuances" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="latest_advancements" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="what-is-agentic-rag"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="yes" evidence="what-is-agentic-rag-1"/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="what-is-retrieval-augmented-generation-aka-rag"/>
  </breadth_checklist>
  <orphan_anchors n_depth="7" n_breadth="1" n_unreachable="0">
    <orphan route="depth" anchor="Tie directly to Lessons 7–8 (ReAct). Emphasize: Agentic RAG is essentially a ReAct-style agent equipped with a retrieval tool. The agent reasons (Thought), decides an Action (e.g., retrieve), observes results, and iterates." bullet="theoretical_foundations">Anchors agentic RAG to prior ReAct lessons.</orphan>
    <orphan route="depth" anchor="Clarify: agents typically use many tools (web search, code execution, databases). Labeling a whole system “agentic RAG” can be too narrow—the retrieval tool is just one of several." bullet="technical_nuances">Clarifies scope of agentic RAG.</orphan>
    <orphan route="depth" anchor="First, define the core distinction (the theoretical part):" bullet="theoretical_foundations">Requires explicit standard vs. agentic contrast.</orphan>
    <orphan route="depth" anchor="Standard RAG: A linear, pre-determined workflow. It's powerful but rigid. Every query follows the same Path: Retrieve -> Augment -> Generate." bullet="theoretical_foundations">Defines standard RAG baseline.</orphan>
    <orphan route="depth" anchor="Agentic RAG: Adaptive and iterative. The agent decides when to retrieve, how to reformulate, which source to search, and whether to chain multiple retrieval and reasoning steps." bullet="theoretical_foundations">Defines agentic RAG mechanism.</orphan>
    <orphan route="depth" anchor="Explain the capabilities of an agentic approach:" bullet="technical_nuances">Introduces agentic capabilities list.</orphan>
    <orphan route="breadth" anchor="It can even decide to **update** the RAG system's knowledge base with new information it learns (preview Lesson 10). Agent may propose writes to a long-term store (falls under Memory for Agents, covered in Lesson 10).we’ll cover that in the next lesson. Keep the explanation high-level here." bullet="adjacent_concepts">Links forward to memory lesson outside current scope.</orphan>
    <orphan route="depth" anchor="Then, show (conceptually) it in action:" bullet="technical_nuances">Requires conceptual action example.</orphan>
  </orphan_anchors>
</section>
<section id="S6::section-6-conclusion" self_contained="yes" sources="from-local-to-global-a-graphrag-approach-to-query-focused-su,the-rise-of-rag,a-complete-guide-to-rag" artefacts="">
  <intent>Summarize RAG benefits, situate it inside Context Engineering, and preview Lesson 10 plus later course topics.</intent>
  <depth_checklist depth_score="2">
    <item name="motivation" present="yes" evidence="the-rise-of-rag"/>
    <item name="theoretical_foundations" present="yes" evidence="a-complete-guide-to-rag"/>
    <item name="technical_nuances" present="no" evidence=""/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="no" evidence=""/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="no" evidence=""/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="from-local-to-global-a-graphrag-approach-to-query-focused-su"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="no" evidence=""/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="yes" evidence="the-rise-of-rag"/>
  </breadth_checklist>
  <orphan_anchors n_depth="0" n_breadth="0" n_unreachable="0"/>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction-giving-llms-an-open-book-exam" need_depth="24" need_breadth="6" target_words="250" mandatory_bullets="6" must_cover_depth="0" must_stay_brief="1"/>
  <section id="S2::section-2-the-rag-system-core-components" need_depth="26" need_breadth="5" target_words="250" mandatory_bullets="4" must_cover_depth="2" must_stay_brief="1"/>
  <section id="S3::section-3-the-rag-pipeline-ingestion-and-retrieval" need_depth="44" need_breadth="5" target_words="300" mandatory_bullets="9" must_cover_depth="8" must_stay_brief="1"/>
  <section id="S4::section-4-advanced-rag-techniques" need_depth="28" need_breadth="4" target_words="350" mandatory_bullets="6" must_cover_depth="3" must_stay_brief="1"/>
  <section id="S5::section-5-agentic-rag" need_depth="25" need_breadth="6" target_words="250" mandatory_bullets="5" must_cover_depth="1" must_stay_brief="1"/>
  <section id="S6::section-6-conclusion" need_depth="6" need_breadth="4" target_words="100" mandatory_bullets="4" must_cover_depth="0" must_stay_brief="0"/>
  <overall>
    <weakest_sections>S4::section-4-advanced-rag-techniques, S3::section-3-the-rag-pipeline-ingestion-and-retrieval</weakest_sections>
    <strongest_sections>S6::section-6-conclusion, S1::section-1-introduction-giving-llms-an-open-book-exam</strongest_sections>
    <dominant_gap_type>depth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>