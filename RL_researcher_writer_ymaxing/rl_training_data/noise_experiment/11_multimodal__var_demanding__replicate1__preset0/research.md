# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>What are the documented error rates, failure modes, and performance statistics of traditional OCR and layout detection systems when handling complex documents with diagrams, nested tables, handwritten text, or poor scan quality?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://www.llamaindex.ai/blog/ocr-accuracy

Query: What are the documented error rates, failure modes, and performance statistics of traditional OCR and layout detection systems when handling complex documents with diagrams, nested tables, handwritten text, or poor scan quality?

Answer: Traditional OCR engines like Tesseract and PaddleOCR achieve 88–94% accuracy on high-volume, simple layouts but top out there on complex layouts, mixed content types, or degraded scans. They treat pages as flat text grids, struggling with multi-column formats, nested tables, overlapping text layers, faded watermarks, and embedded graphics, introducing recognition errors. For handwriting, CER is 3–5%, considered good but requiring human-in-the-loop for high accuracy. Poor scan quality below 300 DPI causes 20%+ drops in accuracy; 5-degree tilts increase WER by 15%+. Enterprise APIs (Google Document AI, Azure Form Recognizer, AWS Textract) reach 96–98% on standard forms but accuracy drops on irregular layouts, heavy tables, embedded charts, mixed handwriting/print. Benchmarks: CER <1% printed, 3–5% handwriting; WER <2% standard docs. Document condition like fold lines, shadows, ink bleed degrade performance. Hardware constraints cause tiling errors.

-----

-----

Phase: [EXPLOITATION]

### Source [2]: https://conexiom.com/blog/the-6-biggest-ocr-problems-and-how-to-overcome-them

Query: What are the documented error rates, failure modes, and performance statistics of traditional OCR and layout detection systems when handling complex documents with diagrams, nested tables, handwritten text, or poor scan quality?

Answer: Traditional OCR struggles with poor image quality from blurry/low-resolution scans (<300 DPI) or handwritten text, resulting in misinterpreted/unreadable text and significantly reduced accuracy. Variable document formats with varying structures/layouts are processed incorrectly due to reliance on pre-defined rules. Complex/non-textual elements like tables, graphs, logos cause significant difficulty in accurate recognition/digitization. Text distortion/skew from non-horizontal/vertical text or physical distortions leads to inaccurate recognition. No specific numerical error rates provided, but these issues frequently cause OCR errors in real-world use.

-----

-----

Phase: [EXPLOITATION]

### Source [3]: https://jiffy.ai/overcoming-ocr-errors-and-limitations-with-intelligent-document-processing/

Query: What are the documented error rates, failure modes, and performance statistics of traditional OCR and layout detection systems when handling complex documents with diagrams, nested tables, handwritten text, or poor scan quality?

Answer: OCR-based solutions deliver maximum accuracy of only 60% even with best-quality scanners, requiring more manual corrections than time saved. They fail on semi-structured, unstructured, and handwritten documents due to template-based processing requiring specific formats/rules. Cannot deliver straight-through processing (STP) accurately on complex/varied documents. Lacks context extraction, e.g., numbers without units. Works on simple printed docs like invoices but unsuitable for enterprise-scale with large volume/variety including complex tables, handwritten text.

-----

-----

Phase: [EXPLOITATION]

### Source [4]: https://unstructured.io/blog/unstructured-leads-in-document-parsing-quality-benchmarks-tell-the-full-story

Query: What are the documented error rates, failure modes, and performance statistics of traditional OCR and layout detection systems when handling complex documents with diagrams, nested tables, handwritten text, or poor scan quality?

Answer: Traditional OCR-era metrics fail on modern documents like scanned invoices, multi-column layouts, nested tables, handwritten annotations. Legacy systems assume single correct output, penalizing semantic equivalents. No specific rates for traditional OCR, but implies poor performance on real-world messy enterprise docs from healthcare/finance/manufacturing with these elements, as modern tools are benchmarked against them.

-----

-----

Phase: [EXPLOITATION]

### Source [5]: https://netfira.com/why-ocr-technology-fails-on-real-world-documents-and-how-intelligent-document-processing-can-help/

Query: What are the documented error rates, failure modes, and performance statistics of traditional OCR and layout detection systems when handling complex documents with diagrams, nested tables, handwritten text, or poor scan quality?

Answer: OCR fails on real-world B2B docs with skewed/poorly scanned pages, low contrast/faded text, multiple columns/nested tables, mixed languages, logos/stamps/watermarks, handwritten notes/signatures, inconsistent spacing. Outputs unreliable text with misread/merged/separated characters, lost context. Relies on templates/fixed coordinates, fragile to layout changes. Does not understand data relationships (e.g., line items to headers, totals). Confidence scores don't solve contextual errors. Scales poorly, shifting work to manual fixes. Performs well only on clean, high-res, standard fonts/layouts.

-----

</details>

<details>
<summary>What are prominent real-world enterprise use cases and limitations of text-only AI approaches in fields like financial report analysis with charts, medical imaging diagnostics, and technical documentation with sketches?</summary>

Phase: [EXPLOITATION]

### Source [6]: https://konfuzio.com/en/chatgpt-financial-analysis/

Query: What are prominent real-world enterprise use cases and limitations of text-only AI approaches in fields like financial report analysis with charts, medical imaging diagnostics, and technical documentation with sketches?

Answer: Prominent enterprise use cases of text-only AI like ChatGPT in financial analysis include: automated creation of financial reports from key metrics (e.g., generating narrative reports on sales, costs, and trends); scenario analysis for cash flows (e.g., simulating inflation or cost changes); peer-group analysis from public reports (e.g., comparing gross margins); and risk modeling for budgeting (e.g., impact of interest rate hikes). A University of Chicago study showed GPT-4 outperforming human analysts in earnings prediction from balance sheets (60% accuracy vs. 53-57%), using chain-of-thought prompts. Limitations of text-only approaches: limited industry-specific understanding (e.g., misses nuances in investment banking, risk management); data quality issues leading to errors; lacks deep grasp of regulatory or legal details; datenschutz risks with sensitive data; black-box opacity hindering auditability; cannot handle charts/images directly, requiring manual input of tabular data which may introduce bias or incompleteness. Specialized enterprise AI is recommended for precision and security.

-----

-----

Phase: [EXPLOITATION]

### Source [7]: https://techtoday.lenovo.com/sites/default/files/2025-05/Medical%20Imaging%20White%20Paper%20NVIDIA%20and%20Lenovo.pdf

Query: What are prominent real-world enterprise use cases and limitations of text-only AI approaches in fields like financial report analysis with charts, medical imaging diagnostics, and technical documentation with sketches?

Answer: In medical imaging diagnostics, AI excels in segmentation (outlining tumors/organs), detection (identifying abnormalities), classification (e.g., malignant vs. benign tumors), registration (aligning multi-modal images), and reconstruction (building images from signals like MRI/CT). Enterprise examples: SUNY Upstate uses MONAI for prostate segmentation accelerating cancer diagnosis; ACR/OSU collaborations improve breast density classification for cancer risk. Text-only AI limitations implied: relies on vision-based deep learning/computer vision for image analysis; manual/semi-automatic methods are time-consuming/error-prone; text-only cannot process raw images, needing image-specific AI for accuracy, scalability, regulatory compliance. Challenges include adoption readiness, data privacy in collaborative training, need for foundational models and clinician involvement—areas where pure text models fall short without multimodal integration.

-----

-----

Phase: [EXPLOITATION]

### Source [8]: https://www.ijcai.org/proceedings/2023/0581.pdf

Query: What are prominent real-world enterprise use cases and limitations of text-only AI approaches in fields like financial report analysis with charts, medical imaging diagnostics, and technical documentation with sketches?

Answer: Financial reports contain textual and tabular data (charts/tables); text-only summarization invalidates existing approaches as they ignore tables. Proposed USTT model summarizes both, detecting salient coupled content via gates between row/column/sentence embeddings, using external KB to reduce selective bias. Dataset: 13,897 triplets from reports. Experiments show text-only baselines (BART/T5/PEGASUS) underperform on table+text (e.g., ROUGE-1: 30.13 vs. USTT 32.28; FactScore 6.37 vs. 9.73). Limitations of text-only: poor factual consistency with tables (e.g., hallucinations, misses data); lower salience/coverage; cannot preserve tabular facts without integration, leading to biased summaries from selective human text.

-----

-----

Phase: [EXPLOITATION]

### Source [9]: https://arxiv.org/html/2503.22035v1

Query: What are prominent real-world enterprise use cases and limitations of text-only AI approaches in fields like financial report analysis with charts, medical imaging diagnostics, and technical documentation with sketches?

Answer: AI (universal approximators like LLMs) limitations in financial services: struggles with small datasets, extrapolation, subjective probabilities, relationships/ethics. EPOCH framework: irreplaceable human Empathy/Presence/Opinion/Creativity/Hope for trust, inclusion, innovation. Use cases where text-only AI aids: liquidity prediction, risk management, robo-advisors, algorithmic trading, compliance (fraud/ML detection). But cannot build trust (process over answer), ensure financial inclusion (biased on sparse data), drive true innovation (extrapolation chaos), or provide human connection in consumer experience. Example: AI suggests medical action but users seek human verification—parallels financial decisions needing judgment beyond data.

-----

-----

Phase: [EXPLOITATION]

### Source [10]: https://www.philips.com/a-w/about/news/archive/features/2022/20221124-10-real-world-examples-of-ai-in-healthcare.html

Query: What are prominent real-world enterprise use cases and limitations of text-only AI approaches in fields like financial report analysis with charts, medical imaging diagnostics, and technical documentation with sketches?

Answer: AI use cases in medical imaging: precise CT positioning/reconstruction; fast MR acquisition; auto ultrasound measurements; faster/accurate radiology reads (e.g., MS lesions, lung nodules); stroke detection/planning; predictive patient deterioration. Enterprise: reduces dose/noise, speeds workflows, improves accuracy (e.g., 44% better MS diagnosis). Text-only limitations implicit: all require image processing (segmentation/detection); ultrasound/CT/MR rely on visual data AI can't handle text-only; manual methods error-prone/time-intensive, highlighting need for vision AI over text models for diagnostics.

-----

</details>

<details>
<summary>What are the practical advantages, trade-offs, and implementation best practices for feeding multimodal data to LLMs like Gemini using raw bytes, Base64 encoding, versus URLs from data lakes or public sources?</summary>

Phase: [EXPLOITATION]

### Source [11]: https://cloud.google.com/blog/products/data-analytics/how-to-use-an-llm-to-create-data-schemas-in-bigquery

Query: What are the practical advantages, trade-offs, and implementation best practices for feeding multimodal data to LLMs like Gemini using raw bytes, Base64 encoding, versus URLs from data lakes or public sources?

Answer: Multimodal large language models (LLMs) like Gemini can analyze examples of data in the data lake, including text descriptions, code, and even images of existing databases. By understanding this data and its relationships, LLMs can suggest or even automatically generate schema layouts, simplifying the laborious process of implementing the data model within the database. The blog demonstrates using Gemini Pro 1.0 Vision model in BigQuery to create a database schema from an entity relationship (ER) diagram image. Step 1: Create an ER diagram using a modeling tool or screenshot. Step 2: Craft a prompt with the ER image as input, including detailed rules for BigQuery DDL generation and examples. Step 3: Call the Gemini model via Colab notebooks or BigQuery ML integration with Vertex AI. The prompt uses multimodal input (image + text) to generate DDL statements. This approach streamlines data modeling by passing multi-modal input directly to Gemini, focusing on images of ER diagrams to produce executable schemas. No explicit discussion of raw bytes vs Base64 vs URLs, but implies image handling via URLs or direct upload in BigQuery ML context. Advantages: Reduces manual effort, handles complex hierarchical structures from diverse sources. Trade-offs: Relies on prompt quality and iteration; potential inaccuracies in generated schemas requiring validation. Best practices: Parameterize prompts for scale, use examples, iterate based on outputs.

-----

-----

Phase: [EXPLOITATION]

### Source [12]: https://towardsdatascience.com/integrating-multimodal-data-into-a-large-language-model-d1965b8ab00c/

Query: What are the practical advantages, trade-offs, and implementation best practices for feeding multimodal data to LLMs like Gemini using raw bytes, Base64 encoding, versus URLs from data lakes or public sources?

Answer: The article discusses multimodal RAG using LlamaParse for parsing documents into markdown with images. LlamaParse premium mode extracts text, tables, and images into structured markdown. Images are downloaded as JPG files (screenshots of pages) and stored locally with paths added to node metadata (e.g., 'image_path'). During query retrieval, image nodes are created from these local paths and passed to multimodal LLM (gpt-4o-mini) alongside text context. Code shows: image_nodes.append(NodeWithScore(node=ImageNode(image_path=n.metadata["image_path"]))) and llm_response = self.multi_modal_llm.complete(prompt=fmt_prompt, image_documents=[image_node.node for image_node in image_nodes]). No mention of raw bytes, Base64, or URLs specifically for Gemini, but uses local file paths for images in OpenAI multimodal API calls. Advantages of local paths: Avoids network latency, full control. Trade-offs: Memory intensive for large images, requires local storage/download. Best practices: Parse with multimodal model (gpt-4o), store image screenshots per page, link via metadata, pass ImageNode objects to LLM.complete() with max_tokens limit. For larger docs, uses prompt caching to reduce cost. Compares gpt-4o-mini (cheaper, faster) vs Claude for context assignment.

-----

-----

Phase: [EXPLOITATION]

### Source [13]: https://arxiv.org/html/2505.18458v1

Query: What are the practical advantages, trade-offs, and implementation best practices for feeding multimodal data to LLMs like Gemini using raw bytes, Base64 encoding, versus URLs from data lakes or public sources?

Answer: The survey covers data management for multimodal LLMs across stages like pre-training (TB-scale interleaved image-text corpora in JSON/WebDataset), continual pre-training, SFT (image+task description pairs), RAG (domain-specific like MIMIC-IV), evaluation (MMMU benchmark with images). Data formats: TFRecord/MindRecord for multimodal (images+labels in single file), tf.data.Dataset for tensor input. Acquisition: Layout analysis (PaddleOCR, MinerU pipelines; end-to-end multimodal LLMs like GOT2.0, Fox). Deduplication: SemDeDup for text+image via embeddings. Filtering: Content-level for improper images/videos (CogVideoX motion filters, HunyuanVideo pipelines). Storage: Distributed (JuiceFS, 3FS SSDs), heterogeneous (ZeRO-Offload GPU/CPU/NVMe). No specific raw bytes/Base64/URLs comparison for Gemini, but implies local tensor formats for training avoid network; RAG uses organized vectors/graphs. Advantages of efficient formats: High I/O throughput, fault tolerance. Trade-offs: Large multimodal datasets need scalable storage/movement (caching, offloading). Best practices: Pipeline parsing (OCR+layout), embedding clustering dedup, hierarchical storage/checkpointing.

-----

</details>

<details>
<summary>How can multimodal RAG retrieval tools be integrated as actions within ReAct-style reasoning agents to enable processing of images, PDFs, and visual documents in enterprise workflows?</summary>

Phase: [EXPLOITATION]

### Source [14]: https://www.linkedin.com/posts/sayandey01_generativeai-llm-rag-activity-7412381316106760192-nFx3

Query: How can multimodal RAG retrieval tools be integrated as actions within ReAct-style reasoning agents to enable processing of images, PDFs, and visual documents in enterprise workflows?

Answer: The source describes a Multimodal RAG architecture for handling complex PDFs with tables, charts, and images using the unstructured library and Multi-Vector retrieval strategy. ETL Pipeline: Uses unstructured library with hi_res strategy to partition elements into images, tables, and narrative text; by_title chunking groups relevant elements. Multimodal Summarization: Images extracted as Base64 and summarized by multimodal model (GPT-4o mini); tables converted to HTML and summarized; text summarized via LLM. Storage Strategy: Embeds text summaries in Vector Store for semantic search; stores raw objects (Base64 images, HTML tables) in separate Doc Store linked by unique Document ID. Retrieval Flow: Semantic search on summaries retrieves Document ID to fetch raw image/table; LLM generates answer with original context. This enables specific questions about data in tables or diagrams. Mentions Agentic RAG where AI agents orchestrate tools, retrieval, reasoning, and external APIs using ReAct, CoT planning, best for real workflows like querying DB, getting reports, verifying with API, summarizing results, multi-source research automation – directly relevant to integrating multimodal retrieval as actions in ReAct-style agents for enterprise processing of visual documents.

-----

-----

Phase: [EXPLOITATION]

### Source [15]: https://www.snowflake.com/en/engineering-blog/arctic-agentic-rag-multimodal-pdf-retrieval/

Query: How can multimodal RAG retrieval tools be integrated as actions within ReAct-style reasoning agents to enable processing of images, PDFs, and visual documents in enterprise workflows?

Answer: The source details Arctic Agentic RAG series for enterprise AI, focusing on multimodal PDF retrieval with Snowflake Cortex. Treats PDFs as images for multimodal embeddings (no OCR), embedding pages into shared vector space with queries for unified text-visual search. Advantages: preserves layout/charts/tables, efficient single embeddings. Evaluated models: Voyage Multimodal 3, GME-Qwen2-VL, Nomic-Embed-Multimodal vs text-OCR baseline. Custom benchmark on tech manuals (charts/text), SEC filings, SlideVQA shows multimodal excels on visual-heavy docs, text on structured. Hybrid retrieval: multimodal + keyword + text reranking improves Recall@5. Part of agentic RAG for enterprise workflows, with open-source notebook for PDF processing, Cortex Search indexing/searching, RAG prompting. Series emphasizes agentic query clarification and innovations for reliable enterprise AI, implying integration as retrieval actions in reasoning agents like ReAct for processing complex visual PDFs.

-----

-----

Phase: [EXPLOITATION]

### Source [16]: https://pathway.com/developers/templates/rag/multimodal-rag

Query: How can multimodal RAG retrieval tools be integrated as actions within ReAct-style reasoning agents to enable processing of images, PDFs, and visual documents in enterprise workflows?

Answer: Describes Multimodal RAG template for PDFs with text, images, charts using Pathway and GPT-4o. Uses BaseRAGQuestionAnswerer integrating data ingestion, LLM, vector store. Parser: DoclingParser with llm strategy for tables/images using GPT-4o to explain content, stored with chunks in index. Embedder: OpenAIEmbedder. Real-time indexing with Pathway Vector Store. Architecture for production: handles finance PDFs with complex tables/charts as images, extracts/explains via GPT-4o, searchable. Serves as endpoint for queries. Mentions combining with adaptive RAG, rerankers; agentic aspects via LLM-driven parsing/retrieval. Enables enterprise workflows by keeping apps in sync with visual docs, privacy, scalability. Code setup reads binary files, builds server on port 8000 for list_documents/answer endpoints – integrable as tool actions in ReAct agents.

-----

-----

Phase: [EXPLOITATION]

### Source [17]: https://www.linkedin.com/posts/gauravagg_mmctagent-enables-multimodal-reasoning-over-activity-7413983881181339648--PyD

Query: How can multimodal RAG retrieval tools be integrated as actions within ReAct-style reasoning agents to enable processing of images, PDFs, and visual documents in enterprise workflows?

Answer: Discusses MMCTAgent, a multimodal agent for reasoning over large video/image collections using Planner (decomposes queries, invokes tools/modalities), Critic (vets logic), modular for custom tools like OCR/object detectors. Handles screenshots, PDFs, diagrams, UI flows for enterprise automation. Structured reasoning with chain-of-thought across visual data, scalable for hours-long videos. Agentic design plugs tools into loops, enabling purposeful cognition beyond perception – aligns with ReAct-style (observe-plan-act-critique). For enterprise: medical imaging, manufacturing QA, security analytics; implies multimodal retrieval (e.g., visual search) as actions in reasoning agents processing images/PDFs/visual docs in workflows.

-----

-----

Phase: [EXPLOITATION]

### Source [18]: https://www.usaii.org/ai-insights/multimodal-rag-explained-from-text-to-images-and-beyond

Query: How can multimodal RAG retrieval tools be integrated as actions within ReAct-style reasoning agents to enable processing of images, PDFs, and visual documents in enterprise workflows?

Answer: Explains multimodal RAG integrating text/images/audio via shared embeddings (transformers/CNNs/wav2vec, contrastive alignment). Stages: knowledge prep (embed modalities), query retrieval (vector DB), context fusion (early/late), multimodal LLM generation. Approaches: text retrieval+multimodal gen, true multi-modal retrieval, Agentic RAG (autonomously decides retrieval/generation). Enterprise apps: search engines retrieving docs/presentations/diagrams, healthcare (images/records). Strategies: LangChain/LlamaIndex pipelines, fine-tune multimodal LLMs, agentic RAG for autonomous reasoning. Integrable via APIs into workflows; agentic variant directly supports ReAct-style agents calling retrieval actions for visual docs/PDFs/images.

-----

</details>

<details>
<summary>How do multimodal LLMs for image and document understanding differ architecturally and functionally from diffusion-based models like Stable Diffusion, and in what agentic scenarios can they be combined as tools?</summary>

Phase: [EXPLOITATION]

### Source [19]: https://arxiv.org/html/2409.14993v3

Query: How do multimodal LLMs for image and document understanding differ architecturally and functionally from diffusion-based models like Stable Diffusion, and in what agentic scenarios can they be combined as tools?

Answer: Multimodal LLMs demonstrate impressive ability for multi-modal understanding via autoregressive probabilistic modeling, using architectures like alignment (vision encoder + projector + LLM) or early-fusion (visual tokenizer + autoregressive LLM). They process text and visual inputs to output text descriptions or reasoning. Diffusion models excel in multi-modal generation, particularly visual generation, using diffusion denoising modeling with forward noise addition and reverse denoising processes, often in latent space (LDM) with U-Net or Transformer (DiT) backbones like Stable Diffusion for text-to-image/video. Architecturally, multimodal LLMs are transformer decoder-based for understanding (e.g., GPT-4V autoregressive), while diffusions are iterative denoising networks for generation. Functionally, LLMs focus on understanding (captioning, QA), diffusions on generation (high-quality images/videos). They can be combined in agentic scenarios as connector-based joint models where pretrained multimodal LLM acts as controller and diffusion as tool for visual generation (e.g., LLM generates prompts/conditions for diffusion), enabling multi-modal generation tasks like image editing from descriptions. Challenges include generation failure in complex conditions, addressed by learnable connectors aligning embeddings.

-----

-----

Phase: [EXPLOITATION]

### Source [20]: https://docs.anyscale.com/llm

Query: How do multimodal LLMs for image and document understanding differ architecturally and functionally from diffusion-based models like Stable Diffusion, and in what agentic scenarios can they be combined as tools?

Answer: Anyscale supports multimodal pipelines combining models like Whisper for audio transcription with LLMs for analysis, and vision-language models (VLMs) for batch processing text+images, focusing on understanding tasks. Separately, it supports fine-tuning/pre-training diffusion models like Stable Diffusion for image generation. Multimodal LLMs/VLMs handle text+image understanding (e.g., Ray Data LLM for datasets with text/images), while diffusion models focus on generation workloads requiring GPU power. In agentic scenarios, they combine in complex agent orchestration via Ray's framework: LLMs as reasoning engines interact with tools/environments, including diffusion models as scalable microservices via Ray Serve for image generation in workflows (e.g., LLM plans, diffusion generates visuals). Supports agentic tuning for tool use like APIs/code execution.

-----

-----

Phase: [EXPLOITATION]

### Source [21]: https://magazine.sebastianraschka.com/p/understanding-multimodal-llms

Query: How do multimodal LLMs for image and document understanding differ architecturally and functionally from diffusion-based models like Stable Diffusion, and in what agentic scenarios can they be combined as tools?

Answer: Multimodal LLMs use unified embedding-decoder (image encoder/projector + LLM concatenation) or cross-modality attention architectures for image+text understanding (e.g., captioning, PDF table extraction). Focus on autoregressive next-token prediction for reasoning/QA. Diffusion models like Stable Diffusion use latent diffusion (VAE compression + U-Net/DiT denoising) for image generation from noise/text. Architecturally, multimodal LLMs extend text LLMs with vision encoders/projectors; diffusions are specialized generative models. Functionally, LLMs for understanding (e.g., Llama 3.2-Vision), diffusions for creation. Combined in agentic setups as tools: LLM reasons/plans, invokes diffusion for generation (e.g., in NVLM hybrid or connector models).

-----

</details>

<details>
<summary>What are the key capabilities and architectural innovations of leading 2025 multimodal LLMs including Llama 4, Gemma 2, Qwen3, DeepSeek R1/V3, GPT-5, Gemini 2.5, and Claude for native image and document processing?</summary>

Phase: [EXPLOITATION]

### Source [22]: https://medium.com/data-science-in-your-pocket/2025-the-year-ai-reasoning-models-took-over-a-month-by-month-review-of-frontier-breakthroughs-6ea2163f854f

Query: What are the key capabilities and architectural innovations of leading 2025 multimodal LLMs including Llama 4, Gemma 2, Qwen3, DeepSeek R1/V3, GPT-5, Gemini 2.5, and Claude for native image and document processing?

Answer: The article reviews 2025 AI reasoning models, highlighting architectural innovations and capabilities relevant to multimodal processing. Key points include: Gemini 2.5 Pro features 1M-token context with strong video/audio input and native multimodal support, enabling deep thinking mode for multimodal reasoning (AIME 88%, GPQA 84%). GPT-5 offers 400k context and unified multi-tier family with thinking depth for complex multimodal tasks. Llama 4 (Scout/Maverick) supports multi-modal reasoning, viable for tasks requiring GPT-class closed models, with multi-million token contexts redefining document-scale workflows. Qwen 3 excels in multi-modal reasoning with strong multilingual performance. DeepSeek R1 uses reinforcement learning for reasoning, with V3.1 pushing sparse MoE for efficiency. Claude Opus 4.1 and Sonnet 4.5 sustain complex workflows, strong on complex text reasoning. General innovations: long context and multimodality (1M+ tokens with native image/audio/video), Mixture-of-Experts (DeepSeek V3.1, Qwen3, Llama 4), deliberate thinking modes across GPT-5, Gemini 2.5/3, Claude 4.x, DeepSeek R1. Llama 4 and Qwen 3 make open-weight models viable for high-level coding and multi-modal reasoning. Gemini 3 Pro and Llama 4 Scout enable multi-million token contexts for document processing.

-----

-----

Phase: [EXPLOITATION]

### Source [23]: https://codedesign.ai/blog/the-ultimate-guide-to-the-top-large-language-models-in-2025/

Query: What are the key capabilities and architectural innovations of leading 2025 multimodal LLMs including Llama 4, Gemma 2, Qwen3, DeepSeek R1/V3, GPT-5, Gemini 2.5, and Claude for native image and document processing?

Answer: The guide compares top 2025 LLMs with a Multimodal Capability Matrix: GPT-5 supports Text, Image, Audio, Video; Gemini 2.5 Pro supports Text, Image, Audio, Video with 2M token context for deep multimodal understanding, ideal for video analysis and large-scale document intelligence; Llama 4 supports Text, Image with up to 10M tokens (Scout model), pinnacle of open-weight AI with Mixture-of-Experts (MoE) architecture for frontier performance and efficiency; Claude 4 Opus supports Text, Image (no Audio/Video). GPT-5 excels in complex reasoning and agentic workflows with multimodal inputs. Gemini 2.5 Pro unrivaled for massive context and multimodal fluency. Llama 4 offers control and customizability with multimodal text/image support.

-----

-----

Phase: [EXPLOITATION]

### Source [24]: https://www.linkedin.com/posts/progressivethinker_this-is-the-most-essential-breakdown-of-2025-activity-7376654335319117825-a5aD

Query: What are the key capabilities and architectural innovations of leading 2025 multimodal LLMs including Llama 4, Gemma 2, Qwen3, DeepSeek R1/V3, GPT-5, Gemini 2.5, and Claude for native image and document processing?

Answer: The post summarizes 2025 flagship LLM architectures: DeepSeek V3 uses Multi-Head Latent Attention (MLA) for KV cache compression and 256-expert MoE with shared expert; Llama 4 adopts MoE with fewer, larger experts and alternating MoE/dense layers; Gemma 3 employs sliding window attention to cut KV cache memory, Gemma 3n adds Per-Layer Embedding (PLE) and MatFormer for on-device efficiency; Qwen3 features deep/narrow dense models and MoE without shared expert, Qwen3-Next adds many small experts, shared expert, Gated DeltaNet + Gated Attention hybrid for long context, Multi-Token Prediction (MTP). Mentions DeepSeek-OCR for document processing: compresses pages into vision tokens (7x-20x reduction), DeepEncoder + MoE-based decoder, 97-98% precision at 10x compression for ultra-long context LLMs and document understanding.

-----

-----

Phase: [EXPLOITATION]

### Source [25]: https://www.preprints.org/manuscript/202508.1904

Query: What are the key capabilities and architectural innovations of leading 2025 multimodal LLMs including Llama 4, Gemma 2, Qwen3, DeepSeek R1/V3, GPT-5, Gemini 2.5, and Claude for native image and document processing?

Answer: The preprint compares coding LLMs: Qwen3-Coder uses 480B MoE (35B active), 256K→1M token context; DeepSeek R1 is open-weight with GRPO training; Gemini 2.5 has multimodal fusion, 1M token context; Claude 3.7 uses dense transformer with hybrid reasoning. Focuses on coding but notes long-context for document processing (Qwen superior at 1M tokens). Qwen excels in agentic tasks supporting document-scale workflows.

-----

-----

Phase: [EXPLOITATION]

### Source [26]: https://www.promptitude.io/post/ultimate-2025-ai-language-models-comparison-gpt5-gpt-4-claude-gemini-sonar-more

Query: What are the key capabilities and architectural innovations of leading 2025 multimodal LLMs including Llama 4, Gemma 2, Qwen3, DeepSeek R1/V3, GPT-5, Gemini 2.5, and Claude for native image and document processing?

Answer: The comparison covers 2025 LLMs: GPT-5 multimodal (text/image/audio/video), 400k tokens; Gemini 2.5 multimodal (text/image/audio/video), 2M tokens for large-scale document intelligence; LLaMA 4 Scout multimodal (text/image/video), up to 10M tokens for extensive research/documents; Claude 4.0 Sonnet/Opus multimodal text/image; DeepSeek R1 strong in scientific reasoning with long-form content; Claude Opus 4.1 for multi-step reasoning and coding.

-----

</details>

<details>
<summary>How can different encoder architectures be integrated into multimodal LLMs to natively support additional modalities like PDFs, audio, and video beyond basic text-image handling?</summary>

Phase: [EXPLOITATION]

### Source [27]: https://sparkco.ai/blog/exploring-multimodal-llms-text-image-and-video-integration

Query: How can different encoder architectures be integrated into multimodal LLMs to natively support additional modalities like PDFs, audio, and video beyond basic text-image handling?

Answer: Deploy specialized encoders for each modality. For instance, use BERT-based models for text, Convolutional Neural Networks (CNNs) for images, and Video Transformers for video data. This specialized approach enhances the model's ability to process diverse data types efficiently. Incorporate cross-attention layers to enable effective fusion of multimodal information. These layers help the model align and reason across different modalities, crucial for tasks like visual analytics and real-time data integration. Adopt modular memory architectures to store and retrieve multimodal information dynamically. These architectures are vital for tasks requiring integrated understanding, such as scientific reasoning and time series analysis. Specialized modality encoders efficiently process various data types—crucial for complex tasks like vision-language tasks and real-time data integration. Cross-attention mechanisms facilitate the fusion of multimodal information, enriching the model's proficiency in aligning and reasoning across different data types. Modular memory systems allow LLMs to effectively store and retrieve multimodal context, supporting more complex reasoning processes.

-----

-----

Phase: [EXPLOITATION]

### Source [28]: https://www.emergentmind.com/topics/multimodal-llms

Query: How can different encoder architectures be integrated into multimodal LLMs to natively support additional modalities like PDFs, audio, and video beyond basic text-image handling?

Answer: Multimodal LLM architectures are typically structured with three to five interacting components: Modality Encoders: Each supported modality (e.g., vision, audio, text, video) is passed through a dedicated encoder (such as CLIP-ViT for images, Whisper for audio, 1D-ResNet for time series, or BERT for tabular data) to produce a learned feature representation. Input Projection/Alignment Module: To reconcile differing latent spaces, encoders' outputs are transformed (e.g., with linear layers, 1D convolutions, cross-attention blocks, or projectors) so they align with the token embedding space used by the LLM backbone. LLM Backbone (Cognitive Module): The central LLM incorporates both text and aligned modality soft tokens into an integrated input sequence. Specialized Memory/Expert Modules: Some advanced models augment or replace standard LLM blocks with modular visual memory or mixtures-of-multimodal-experts structures. Integration strategies range from simple token concatenation, to cross-attention layers, to plug-and-play temporal modules for video, and to composite attention mechanisms for compute efficiency.

-----

-----

Phase: [EXPLOITATION]

### Source [29]: https://towardsai.net/p/l/enhancing-llm-capabilities-the-power-of-multimodal-llms-and-rag

Query: How can different encoder architectures be integrated into multimodal LLMs to natively support additional modalities like PDFs, audio, and video beyond basic text-image handling?

Answer: A typical Multimodal LLM (MLLM) architecture can be abstracted into the following key components: Modality Encoders: These are specialized neural networks responsible for processing raw data from different modalities (like images, audio, video) and converting them into embeddings. Vision Encoder: For image inputs, models like CLIP’s Vision Transformer (ViT) or OpenCLIP are commonly used. Audio Encoder: For audio inputs, models like HuBERT or Whisper can be employed. Video Encoder: Video encoders often involve a combination of visual and temporal processing. Pre-trained LLM: This is the core of the MLLM, a powerful Transformer-based language model. Modality Interface (Connector): This bridges the gap between the representations from the modality encoders and the input format expected by the pre-trained LLM. Projection Layer: A simple yet effective interface can be one or more linear layers (MLPs) that project the output embeddings from the vision, audio, or video encoders into the same dimensional space as the word embeddings of the LLM. Q-Former (Querying Transformer): As used in BLIP-2, this involves a set of learnable query tokens that interact with the visual features through cross-attention.

-----

-----

Phase: [EXPLOITATION]

### Source [30]: https://arxiv.org/html/2411.06284v3

Query: How can different encoder architectures be integrated into multimodal LLMs to natively support additional modalities like PDFs, audio, and video beyond basic text-image handling?

Answer: Encoder-Decoder Frameworks: These architectures, used in models like DALL-E, allow for mapping between text and image domains. The encoder processes the input (e.g., text), while the decoder generates the output (e.g., an image). Cross-Modal Transformers: These use separate transformers for each modality, with cross-modal attention layers to fuse information. This allows the model to process text and images separately at first, then combine the information. The evolution from LLMs to MLLMs involved integrating visual data with textual data, enabling models to process and understand multiple modalities. Techniques like VisualBERT and VL-BERT extended the BERT architecture to handle both text and images, pre-training on large-scale multimodal datasets to learn joint representations. Cross-modal attention mechanisms allowed models to align and integrate information from different modalities, enhancing their ability to perform tasks like image captioning and visual question answering. Unified Representation: MLLMs achieve integrated representations of multimodal data through unified codebooks and joint embedding spaces, enabling seamless processing across different modalities.

-----

</details>

<details>
<summary>What are recommended multimodal embedding models like Voyage AI, Cohere, and SigLIP for direct image and document retrieval in RAG systems, including their integration approaches and performance characteristics?</summary>

Phase: [EXPLOITATION]

### Source [31]: https://milvus.io/blog/choose-embedding-model-rag-2026.md

Query: What are recommended multimodal embedding models like Voyage AI, Cohere, and SigLIP for direct image and document retrieval in RAG systems, including their integration approaches and performance characteristics?

Answer: Voyage Multimodal 3.5 (Voyage AI, undisclosed parameters, 1024 dimensions, text/image/video modalities) is balanced across tasks for multimodal RAG. In cross-modal retrieval (text-to-image with hard negatives), it scores 0.900 R@1 (third after Qwen3-VL-2B at 0.945 and Gemini at 0.928), with modality gap of 0.59. Cross-lingual retrieval: 0.982 R@1 (Easy:1.000, Medium:1.000, Hard:0.938). Key information retrieval (needle-in-haystack up to 4K chars): 1.000 accuracy, 0% degradation. MRL dimension compression: leads with ρ 0.880 full dim to 0.874 at 256 dim (0.7% decay), ideal for storage savings in vector DBs like Milvus. Cohere Embed v4 (undisclosed params, fixed dims, text modality) excels in enterprise retrieval. Cross-lingual: 0.955 R@1 (Easy:1.000, Medium:0.980, Hard:0.875). Key info up to 8K: 1.000, 0% degradation. SigLIP not directly tested; Jina CLIP v2 (~1B params, 1024 dims, text/image) as similar: cross-modal 0.873 R@1, modality gap 0.87; key info 1.000 up to 4K. Integration: Generate embeddings via model SDKs, store in Milvus vector DB (supports MRL truncation, mixed multimodal collections, cosine/L2/IP search). For multimodal RAG, small modality gap enables direct text-image search in same collection without re-ranking. All output standard float vectors for direct insert/search in Milvus/PyMilvus. Use for image/document retrieval in RAG: embed queries/images/docs, retrieve top-k via ANN, feed to LLM.

-----

-----

Phase: [EXPLOITATION]

### Source [32]: https://www.reddit.com/r/Rag/comments/1rcba6y/whats_the_best_embedding_model_for_rag_in_2026_my/

Query: What are recommended multimodal embedding models like Voyage AI, Cohere, and SigLIP for direct image and document retrieval in RAG systems, including their integration approaches and performance characteristics?

Answer: Users recommend Cohere embed-v4, Voyage AI for RAG on legal documents (better than OpenAI text-embedding-3-large at 78% precision). Focus on production benchmarks for domain-specific text retrieval at 10M+ docs scale, latency, cost per 1M tokens. No specific multimodal or SigLIP mentions; implies text-focused but enterprise retrieval strengths.

-----

-----

Phase: [EXPLOITATION]

### Source [33]: https://greennode.ai/blog/best-embedding-models-for-rag

Query: What are recommended multimodal embedding models like Voyage AI, Cohere, and SigLIP for direct image and document retrieval in RAG systems, including their integration approaches and performance characteristics?

Answer: Cohere Embed v3 (proprietary API) best for enterprise RAG with long text inputs (up to 8192 tokens), document retrieval/knowledge search. Strong on MTEB/BEIR, optimized for semantic search/hybrid RAG. Easy integration with vector DBs like Pinecone/Qdrant/Weaviate. Balances quality/latency for production. No Voyage AI, SigLIP, or multimodal specifics; focuses text embeddings for RAG scalability.

-----

-----

Phase: [EXPLOITATION]

### Source [34]: https://eagerworks.com/blog/best-embedding-model-for-rag

Query: What are recommended multimodal embedding models like Voyage AI, Cohere, and SigLIP for direct image and document retrieval in RAG systems, including their integration approaches and performance characteristics?

Answer: eager-embed-v1 (open-source, 2560 dims, text/image, single-vector multimodal) for scalable RAG on visually rich docs (PDFs/slides/charts). Beats SigLIP (56.4 vs 31.4 avg multilingual score, 80% higher), OpenAI CLIP (674% better). Top-10 ViDoRe2 benchmark. Enables direct image/document retrieval without multi-vector complexity. Integration: HuggingFace Transformers/Qwen3-VL, normalize embeddings (L2), store in vector DB for cosine similarity. Scales to 100M+ docs with ms latency, low storage. Trained $500 compute on Qwen3-VL-4B. No Voyage/Cohere details.

-----

-----

Phase: [EXPLOITATION]

### Source [35]: https://artsmart.ai/blog/top-embedding-models-in-2025/

Query: What are recommended multimodal embedding models like Voyage AI, Cohere, and SigLIP for direct image and document retrieval in RAG systems, including their integration approaches and performance characteristics?

Answer: Voyage-Multilingual-2 (self-hosted open) near-commercial multilingual parity, excels document retrieval. Cohere Embed v3 (cloud API) strong long-context, 100+ languages for RAG. SigLIP 2 (Google DeepMind, multimodal) improved contrastive for high-precision text-image alignment; EVA-CLIP/OpenCLIP/Llava-Next for cross-modal RAG/visual search. Multimodal enables unified text/image indexing for direct retrieval. Trade-offs: heavier compute (1k-4k dims). Integration: SDKs/APIs to vector DBs; fine-tune projection heads for alignment. Decision map: Cross-modal → SigLIP 2/EVA-CLIP.

-----

</details>

<details>
<summary>How do hybrid approaches combining unified embedding and cross-modality attention in multimodal LLMs balance implementation simplicity, accuracy for OCR tasks, and efficiency with high-resolution images?</summary>

Phase: [EXPLOITATION]

### Source [36]: https://magazine.sebastianraschka.com/p/understanding-multimodal-llms

Query: How do hybrid approaches combining unified embedding and cross-modality attention in multimodal LLMs balance implementation simplicity, accuracy for OCR tasks, and efficiency with high-resolution images?

Answer: NVIDIA's NVLM paper explores both Unified Embedding Decoder Architecture (NVLM-D, Method A) and Cross-Modality Attention Architecture (NVLM-X, Method B), developing a hybrid approach (NVLM-H) with apples-to-apples comparison. NVLM-D (unified embedding) is easier to implement without LLM modifications. NVLM-X (cross-attention) is more computationally efficient for high-resolution images by avoiding input context overload with image tokens, introducing them later in cross-attention layers, preserving text-only performance if LLM frozen. NVLM-H combines strengths: image thumbnail as unified embedding input, followed by dynamic patches through cross-attention for finer high-resolution details. Findings: NVLM-X superior efficiency for high-res images; NVLM-D higher OCR accuracy; NVLM-H balances advantages of both, achieving better results than standalone methods for OCR tasks with high-resolution images.

-----

-----

Phase: [EXPLOITATION]

### Source [37]: https://arxiv.org/abs/2409.11402

Query: How do hybrid approaches combining unified embedding and cross-modality attention in multimodal LLMs balance implementation simplicity, accuracy for OCR tasks, and efficiency with high-resolution images?

Answer: NVLM paper (NVIDIA) directly compares NVLM-D (decoder-only, unified embedding: images to tokens same size as text, concatenated to LLM), NVLM-X (cross-attention: image embeddings integrated in attention layers), and NVLM-H (hybrid: low-res thumbnail via unified embedding + high-res patches via cross-attention). NVLM-D simpler implementation. NVLM-X efficient for high-res (fewer tokens early). NVLM-D excels OCR tasks. NVLM-H best overall: thumbnail provides global context simply/efficiently, cross-attention adds fine details accurately without full high-res token overload. Balances simplicity (partial unified embedding), OCR accuracy (cross-attention details), efficiency (dynamic patches, not all high-res tokens). Uses Qwen2-72B-Instruct, frozen InternViT-6B encoder, MLP projector. Hybrid outperforms pure methods on benchmarks including OCR.

-----

</details>

<details>
<summary>What real-world enterprise patterns demonstrate the benefits of adding native multimodal inputs, outputs, and tools for screenshots or external PDFs when evolving text-only AI agents into more capable systems?</summary>

Phase: [EXPLOITATION]

### Source [38]: https://kanerika.com/blogs/multimodal-ai-agents/

Query: What real-world enterprise patterns demonstrate the benefits of adding native multimodal inputs, outputs, and tools for screenshots or external PDFs when evolving text-only AI agents into more capable systems?

Answer: Support centers deploy multimodal AI agents to manage queries across channels including chat, email, voice, and video. They understand screenshots, transcribe voice notes, and read messages to resolve issues quickly and accurately. Real-world example: Zendesk integrates multimodal AI to assist agents with tickets including screenshots, voice notes, and written complaints, improving resolution time. Airbnb uses AI to analyze guest messages, uploaded images, and voice requests to automate responses and enhance host-guest communication. Kanerika builds DokGPT for documents + natural language queries and Jennifer for voice + scheduling. In finance, ING Bank reviews loan applications, analyzes supporting documents, and cross-checks client emails. JP Morgan Chase reviews contracts and financial statements while listening to customer calls. In retail, Amazon’s Alexa enables voice and image product search. Zalando analyzes customer-uploaded outfit photos, reviews, and browsing behavior for recommendations. Mayo Clinic integrates radiology images, pathology reports, and physician voice notes for cancer diagnosis. Multimodal systems increase accuracy by up to 40% compared to single-modal AI per McKinsey 2025 report.

-----

-----

Phase: [EXPLOITATION]

### Source [39]: https://invisibletech.ai/blog/multimodal-enterprise-ai

Query: What real-world enterprise patterns demonstrate the benefits of adding native multimodal inputs, outputs, and tools for screenshots or external PDFs when evolving text-only AI agents into more capable systems?

Answer: Real work involves PDFs, screenshots, emails, tickets, dashboards, audio calls, IoT feeds. Text-only models use lossy OCR/transcription. Multimodal foundations treat text, images, audio, structured data as first-class. Ingestion layer unifies multimodal datasets with shared embeddings. Enterprise cases: reading invoices from vendors, understanding dashboard screenshots, interpreting factory-floor photos for safety/quality. Contact-center: listens to calls, watches screens, reads CRM for QA. Warehouses: camera feeds, notes, sensors for jams, parts. Healthcare: images, notes, labs, history for decision support. Financial/legal: contracts, decks, dashboards, feeds for risks. Multimodal enables cross-modal reasoning, reduces lossy conversions, supports workflows beyond chat.

-----

-----

Phase: [EXPLOITATION]

### Source [40]: https://rasa.com/blog/multimodal-ai-use-cases

Query: What real-world enterprise patterns demonstrate the benefits of adding native multimodal inputs, outputs, and tools for screenshots or external PDFs when evolving text-only AI agents into more capable systems?

Answer: Multimodal AI processes images, audio for natural interactions. Benefits: context-driven (e.g., travel claim with photos/screenshots), accessibility. Uses: customer service with voice/text (bank stolen card: voice biometrics, transaction logs); image/text visual search/support (e-commerce scan-to-search, insurance damage photos, medical images + notes); voice/video coaching (language apps, fitness); sensor/text (smart home temp, rail wheel sensors). Multimodal makes interactions human-like, inclusive, adapts to devices.

-----

</details>

<details>
<summary>What are common real-world applications of multimodal LLMs for object detection, image captioning, and processing medical or technical visuals in enterprise settings?</summary>

Phase: [EXPLOITATION]

### Source [41]: https://github.com/cognitivetech/llm-research-summaries/blob/main/models-review/A-Comprehensive-Survey-and-Guide-to-Multimodal-Large-Language-Models-in-Vision-Language-Tasks.md

Query: What are common real-world applications of multimodal LLMs for object detection, image captioning, and processing medical or technical visuals in enterprise settings?

Answer: Multimodal Large Language Models (MLLMs) have key applications in vision-language tasks relevant to object detection, image captioning, and processing medical/technical visuals in enterprise settings. For object detection, the Pix2seq language modeling framework is highlighted in healthcare and research case studies, enabling concrete applications in diverse environments. Image captioning integrates computer vision and NLP, with applications including assistive technologies (converting visual scenes to audio descriptions), autonomous systems/vehicles (capturing road conditions/obstacles for situational awareness), medical imaging/healthcare (generating diagnostic reports to reduce radiologist workload and speed up high-accuracy reporting), and content moderation/search engines (tagging images and flagging inappropriate content). Visual Question Answering (VQA) supports these by combining visual/textual reasoning. In healthcare, MLLMs analyze medical images with patient records/notes for diagnostics/treatment, revolutionizing the field. Enterprise benefits include enhanced accessibility (e.g., VIAssist for visually impaired via object recognition/description), customer service (handling queries with visual understanding), and content creation/editing (multimodal generation). Case studies like Pix2seq demonstrate object detection in medical contexts, while models like Kosmos-1 enable scene understanding for technical visuals. Challenges include scalability and robustness, but MLLMs show strong potential in enterprise healthcare, autonomous systems, and moderation.

-----

-----

Phase: [EXPLOITATION]

### Source [42]: https://smartdev.com/multimodal-ai-examples-how-it-works-real-world-applications-and-future-trends/

Query: What are common real-world applications of multimodal LLMs for object detection, image captioning, and processing medical or technical visuals in enterprise settings?

Answer: Multimodal LLMs enable object detection, image captioning, and processing of medical/technical visuals in enterprise settings, particularly healthcare. In healthcare diagnostics, they analyze medical images (CT scans, X-rays) alongside patient notes/history for accurate diagnoses and personalized treatment plans, reducing radiologist workload. LLaVa-Med is the first multimodal model for healthcare, supporting visual dialogue, explanation, VQA, and image captioning. Microsoft’s Phi-3-vision processes textual/image inputs for text responses. Vision LLMs assist in analyzing medical images. Enterprise applications include AI-powered radiology for diagnostics, disease diagnosis from images/text, and report generation. Autonomous systems use captioning for road/obstacle awareness (object detection). Retail employs Vision LLMs for product info extraction from images. Security uses multimodal analysis for threat detection in video/audio/sensor data.

-----

-----

Phase: [EXPLOITATION]

### Source [43]: https://www.ibm.com/think/topics/multimodal-llm

Query: What are common real-world applications of multimodal LLMs for object detection, image captioning, and processing medical or technical visuals in enterprise settings?

Answer: Multimodal LLMs (MLLMs) process text, images, audio for object detection, image captioning, and medical/technical visuals in enterprise settings. For image captioning/video description, decoders generate text from visuals (e.g., MiniGPT-4 creates captions/instructions; Visual ChatGPT handles multistep tasks like image description/VQA/visual generation). Object detection/classification uses decoders to map features to labels/decisions. Healthcare example: CONCH (contrastive learning from captions for histopathology) analyzes medical slides (immunohistochemistry) via ChatGPT-like interface for zero-shot pathology image matching to diagnostics (e.g., invasive carcinoma/colitis), aiding pathologists without massive datasets. GITMol processes molecular images/graphs/text for chemical reactions/compound recognition/molecular properties in drug discovery/biological sciences. Enterprise benefits: richer context/reasoning across modalities for diagnostics, content moderation, accessibility.

-----

-----

Phase: [EXPLOITATION]

### Source [44]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12479233/

Query: What are common real-world applications of multimodal LLMs for object detection, image captioning, and processing medical or technical visuals in enterprise settings?

Answer: Multimodal Large Language Models (MLLMs) process heterogeneous data like radiologic images (CT/MRI/X-ray, endoscopy, pathology) with text (reports, EHRs) for object detection, image captioning, and medical/technical visuals in enterprise/clinical settings. Key applications: Radiology Report Generation (RRG) translates images to narrative text (Findings/Impression sections), reducing workload/consistency issues. Visual Question Answering (VQA) enables interactive queries on images for decision-making/education. Text-to-image retrieval searches archives (e.g., 'find CXRs suggesting tuberculosis'). 2D models (e.g., LLaVA-Med, Med-PaLM M, X-rayGPT) handle CXRs for RRG/VQA. 3D models (e.g., RadFM, M3D-LaMed) process CT/MRI volumes for spatial reasoning. Region-focused MLLMs (e.g., MAIRA-2, MedRegion-CT) link outputs to image regions for grounded reports. Enterprise: Automates diagnostics, supports pathologists (CONCH for histopathology), enhances workflows in healthcare settings.

-----

-----

Phase: [EXPLOITATION]

### Source [45]: https://www.nature.com/articles/s41598-025-98483-1

Query: What are common real-world applications of multimodal LLMs for object detection, image captioning, and processing medical or technical visuals in enterprise settings?

Answer: Multimodal LLMs process images alongside text for object detection, image captioning, and medical/technical visuals in enterprise healthcare. Applications include diagnostics (analyzing X-rays/CTs with patient data), personalized treatment, report generation. LLaVa-Med supports VQA/image captioning; Phi-3-vision processes medical images/text. Enterprise: AI radiology for CT/X-ray analysis with notes; disease diagnosis from images/text; LLaVa-Med first healthcare multimodal model; Vision LLMs analyze medical images.

-----

</details>

<details>
<summary>What are the standard pipeline steps for traditional OCR-based document processing of PDFs containing mixed text, tables, diagrams, and charts, including preprocessing, layout analysis, and output structuring, and why does this lead to rigid and fragile systems?</summary>

Phase: [EXPLOITATION]

### Source [46]: https://www.daft.ai/blog/end-to-end-distributed-pdf-processing-pipeline

Query: What are the standard pipeline steps for traditional OCR-based document processing of PDFs containing mixed text, tables, diagrams, and charts, including preprocessing, layout analysis, and output structuring, and why does this lead to rigid and fragile systems?

Answer: Traditional OCR-based PDF processing involves a sequential pipeline: Parallel S3 download for raw PDF bytes, flexible PDF text extraction using OCR or direct parsing to extract text with bounding boxes, spatial layout analysis using coordinate-based grouping to recover line and paragraph structure from fragmented text blocks, GPU embeddings, and structured Parquet output. Raw OCR produces fragmented text blocks that are jumbled, requiring coordinate-based heuristics to infer document structure, sort into reading order (left-to-right, top-to-bottom), and group into lines or paragraphs. Traditional approaches are manual, fragmented across multiple systems, sequential processing without automatic parallelization, complex schema management with 15+ lines of manual Arrow schema code, and lack automatic resource management, leading to operational complexity, scaling bottlenecks, memory limitations, custom OCR scripts, and fragility on edge cases like rotated pages, mixed layouts, handwritten annotations in financial, legal, and healthcare documents with mixed text, tables, diagrams.

-----

-----

Phase: [EXPLOITATION]

### Source [47]: https://learn.microsoft.com/en-us/answers/questions/5668164/why-traditional-ocr-fails-for-complex-business-doc?page=1

Query: What are the standard pipeline steps for traditional OCR-based document processing of PDFs containing mixed text, tables, diagrams, and charts, including preprocessing, layout analysis, and output structuring, and why does this lead to rigid and fragile systems?

Answer: Traditional OCR converts images of text into machine-readable characters without understanding context, meaning, or structure. For complex business documents with mixed text, tables, diagrams, charts, embedded fields, checkboxes, signatures, multi-column layouts, irregular formatting, multi-page tables, annotations, low-quality scans, mixed fonts, intermingling of text and graphics: lacks context and structure recognition leading to errors; struggles with multifaceted/variable layouts deviating from templates, misinterpreting/skipping info; no contextual understanding of data types (totals, tax, IDs) requiring rule-based systems that break on minor layout changes; increased manual intervention for validation/correction; scalability issues with high volumes/diverse formats; compliance risks without validation/confidence scores; inflexibility to changes requiring manual rule updates/monitoring. This renders systems rigid and fragile in dynamic environments.

-----

-----

Phase: [EXPLOITATION]

### Source [48]: https://parseur.com/blog/document-processing-automation-guide

Query: What are the standard pipeline steps for traditional OCR-based document processing of PDFs containing mixed text, tables, diagrams, and charts, including preprocessing, layout analysis, and output structuring, and why does this lead to rigid and fragile systems?

Answer: Traditional OCR pipeline: Capture documents (email/uploads/scanning), Recognition using OCR to read printed/handwritten text, Extraction/structuring of data points into standardized format, Delivery to Excel/ERP/CRM/dashboards. Traditional OCR limitations for mixed content: only converts to machine-readable text without understanding meaning/structure/relationships; no context (reads text not meaning); requires manual rules/templates; struggles with variable layouts/inconsistent formats; needs human review. Works for clean/consistent/simple forms but leads to rigid systems due to template dependency, manual setup, and fragility on layout variations in complex PDFs with tables/charts.

-----

-----

Phase: [EXPLOITATION]

### Source [49]: https://www.llamaindex.ai/blog/ocr-for-tables

Query: What are the standard pipeline steps for traditional OCR-based document processing of PDFs containing mixed text, tables, diagrams, and charts, including preprocessing, layout analysis, and output structuring, and why does this lead to rigid and fragile systems?

Answer: Traditional OCR for PDFs with tables/charts: preprocessing (deskewing/orientation correction/binarization/noise reduction), table detection (alignment/whitespace/numeric patterns), structure recognition (row/column boundaries/headers/merged cells), data extraction (OCR per cell mapped to schema with validation). PDFs are positioned text fragments without relational metadata; standard OCR identifies characters but fails to reconstruct spatial relationships (cells/headers/values), leading to misalignments. Template-driven systems use predefined positional rules effective for fixed layouts but fragile/require maintenance on format changes/variability; conventional engines treat as flat text, losing structure in mixed content.

-----

-----

Phase: [EXPLOITATION]

### Source [50]: https://intuitionlabs.ai/articles/ai-pdf-data-extraction-clinical-research

Query: What are the standard pipeline steps for traditional OCR-based document processing of PDFs containing mixed text, tables, diagrams, and charts, including preprocessing, layout analysis, and output structuring, and why does this lead to rigid and fragile systems?

Answer: Traditional OCR pipeline: Image preprocessing (binarization/deskewing/noise reduction/contrast), layout analysis (text blocks/tables/images/form fields with spatial info), OCR transcription. For PDFs with mixed text/tables/diagrams/charts: dumps cells into continuous text losing semantics/row boundaries; ignores/misplaces footnotes/headers/figures; struggles with multi-column layouts/low-quality scans/handwriting/unusual fonts. Rule-based/template/regex parsing precise for uniform forms but rigid/brittle on deviations; requires manual updates. Leads to fragile systems with high error rates (up to 70% manual, 80-95% OCR on complex docs), manual intervention, scalability limits on variable formats.

-----

</details>

<details>
<summary>How can structured output models like Pydantic be combined with multimodal LLMs such as Gemini for tasks like object detection on images or PDF pages, including prompt design, response parsing, and bounding box visualization techniques?</summary>

Phase: [EXPLOITATION]

### Source [51]: https://discuss.ai.google.dev/t/gemini-consistently-producing-valid-pydantic-responses/98992

Query: How can structured output models like Pydantic be combined with multimodal LLMs such as Gemini for tasks like object detection on images or PDF pages, including prompt design, response parsing, and bounding box visualization techniques?

Answer: In a project involving large-scale bounding box detection on over 1,000 images using Gemini, Pydantic models serve as schemas for structured output with minimal post-processing. Gemini consistently produces valid Pydantic responses, even with complex, conditional, and nested schemas, without structure or type failures. This reliability is attributed to Gemini's 'structured output' feature in the API, which ensures schema adherence. Pydantic acts as a second checkpoint for non-determinism in LLMs generally. Recommendations include using Pydantic schemas in applications, improving prompts with few-shot examples, and testing multiple runs. Pydantic's compatibility with many LLMs allows easy model switching. Users note Gemini's decoding process constrains tokens for schema compliance, similar to OpenAI's Context Free Grammar approach.

-----

-----

Phase: [EXPLOITATION]

### Source [52]: https://www.decodingai.com/p/stop-converting-documents-to-text

Query: How can structured output models like Pydantic be combined with multimodal LLMs such as Gemini for tasks like object detection on images or PDF pages, including prompt design, response parsing, and bounding box visualization techniques?

Answer: For object detection with Gemini, define Pydantic schemas like BoundingBox (ymin, xmin, ymax, xmax: float; label: str) and Detections (bounding_boxes: list[BoundingBox]). Use prompt: 'Detect all prominent items. Return 2d boxes normalized to 0-1000.' Pass image as bytes (e.g., WEBP) via types.Part.from_bytes. Configure with response_mime_type='application/json' and response_schema=Detections. Response parses automatically to structured Pydantic objects, e.g., bounding_boxes=[BoundingBox(ymin=272.0, xmin=28.0, ymax=801.0, xmax=535.0, label='kitten')]. Apply to PDF pages by treating as images: load PDF page as image bytes, use same detection prompt/schema. Supports raw bytes, Base64, or GCS URLs. Enables extracting diagrams/tables from PDFs without OCR. Visualization not detailed, but structured boxes enable OpenCV drawing.

-----

-----

Phase: [EXPLOITATION]

### Source [53]: https://tetrate.io/learn/ai/llm-output-parsing-structured-generation

Query: How can structured output models like Pydantic be combined with multimodal LLMs such as Gemini for tasks like object detection on images or PDF pages, including prompt design, response parsing, and bounding box visualization techniques?

Answer: Pydantic integrates with LLM workflows for structured outputs: parse JSON into Pydantic models for automatic structure/type validation; failures provide detailed errors for retry prompts. Supports nested models for hierarchical data (e.g., complex bounding boxes). Generate JSON Schema from Pydantic for structured output APIs, ensuring LLM constraints match validation. Strict mode, extra field handling, aliases configurable. After parsing, use for visualization (e.g., OpenCV bounding boxes). Error handling: use validation errors to refine prompts; nested validation recursive. Compatible with FastAPI for endpoints processing LLM outputs. Best for production: layered validation, monitoring failures.

-----

-----

Phase: [EXPLOITATION]

### Source [54]: https://python.useinstructor.com/blog/2024/10/23/structured-outputs-with-multimodal-gemini/

Query: How can structured output models like Pydantic be combined with multimodal LLMs such as Gemini for tasks like object detection on images or PDF pages, including prompt design, response parsing, and bounding box visualization techniques?

Answer: Use Instructor library with Pydantic for structured outputs from multimodal Gemini (e.g., gemini-2.5-flash). Define models like TouristDestination (name, description, location: str) and Recommendations (chain_of_thought/description: str; destinations: list[TouristDestination]). Client: instructor.from_provider('google/gemini-2.5-flash'). Upload video/PDF/image file via genai.upload_file or bytes. Prompt: e.g., 'What places do they recommend in this video?' with file content. Call client.create(messages=[{'role': 'user', 'content': [prompt, file]}], response_model=Recommendations). Parses to validated Pydantic instances automatically. Extends to images/PDFs/videos; future: timestamps, diarization for detection tasks.

-----

-----

Phase: [EXPLOITATION]

### Source [55]: https://pydantic.dev/articles/llm-intro

Query: How can structured output models like Pydantic be combined with multimodal LLMs such as Gemini for tasks like object detection on images or PDF pages, including prompt design, response parsing, and bounding box visualization techniques?

Answer: Pydantic defines schemas for LLM structured outputs via JSON Schema generation. Validate/coerce types post-parsing (e.g., str to int). Use with OpenAI tools/tool_choice for schema enforcement; Instructor patches client for response_model=PydanticClass, auto-parsing JSON to validated models, retries on failure. Example: nested models like DateRange in SearchQuery. Prompts focus on data; schema handles structure. Compatible with Gemini/OpenAI-compatible APIs. For detection: define BoundingBox models, pass image in messages, get parsed coordinates. Ensures reliable parsing for visualization.

-----

</details>

<details>
<summary>How do shared embedding spaces in multimodal models enable intuitive semantic image retrieval in consumer applications like photo search engines, where natural language queries retrieve visually similar content without explicit metadata?</summary>

Phase: [EXPLOITATION]

### Source [56]: https://opensearch.org/blog/multimodal-semantic-search/

Query: How do shared embedding spaces in multimodal models enable intuitive semantic image retrieval in consumer applications like photo search engines, where natural language queries retrieve visually similar content without explicit metadata?

Answer: During model training, the image and text embeddings are mapped onto a joint embedding space. In this space, similar images and text descriptions are close to each other, while dissimilar images and descriptions are farther away. Thus, in the eyes of the model, there is no fundamental difference between images and descriptions. The joint embedding space enables text-to-image search, which retrieves images based on text queries. Multimodal models generate embeddings by mapping entities (image, text) to multi-dimensional vectors capturing semantic meaning and visual representation. Models like CLIP and Titan have a two-tower architecture with image and text encoders trained on image-text pairs to map into a joint space. This allows text-to-image search without explicit metadata, as the model performs multimodal search through zero-shot learning, eliminating manual metadata enrichment. Traditional methods require scanning images and adding metadata for text-to-text search, but multimodal models avoid this by directly understanding visual and textual semantics in the shared space. For consumer applications like photo search, users can query with natural language (e.g., 'shirt with abstract pattern') to retrieve visually similar images. The Titan Multimodal Embeddings model maps images and text onto a joint embedding space using curated image-text pairs, enabling intuitive semantic retrieval in photo search engines without explicit metadata.

-----

-----

Phase: [EXPLOITATION]

### Source [57]: https://towardsdatascience.com/multimodal-ai-search-for-business-applications-65356d011009/

Query: How do shared embedding spaces in multimodal models enable intuitive semantic image retrieval in consumer applications like photo search engines, where natural language queries retrieve visually similar content without explicit metadata?

Answer: A multimodal embedding model stores text and image embeddings in a shared embedding space, connecting text with relevant images and enabling retrieval across formats without separate databases. This unified approach enhances search relevance for intuitive exploration. Businesses need to search images from repositories without proper metadata using text queries. Cohere's Embed 3 generates embeddings from text and images in a unified space for text-to-image retrieval in product catalogs. Customers search products flexibly by typing queries or uploading images; e.g., describe characteristics to retrieve visually similar items without exact names or metadata. In a furniture catalog example, text queries like 'Find me a chair with metal stands' retrieve relevant images and text via shared embeddings, refined by LLM. Image-to-image retrieval finds similar products from an input photo. The model connects text and image embeddings closely, enabling semantic retrieval without explicit metadata linking them.

-----

-----

Phase: [EXPLOITATION]

### Source [58]: https://assets.amazon.science/89/bf/661d950d4059930c8f1d2e449ac6/joint-visual-textual-embedding-for-multimodal-style-search.pdf

Query: How do shared embedding spaces in multimodal models enable intuitive semantic image retrieval in consumer applications like photo search engines, where natural language queries retrieve visually similar content without explicit metadata?

Answer: Visual and textual modalities share the same embedding space, enabling arithmetic operations to manipulate queries. For a query image I and textual attributes w={w+,w-}, the multimodal query q = fI + sum fw+ - sum fw-, where fI is image embedding, fw are word embeddings. This searches visually similar products with different textual properties without explicit metadata. Images and textual descriptions map into a common embedding space via joint training on catalog data. Text encoder sums word embeddings; image via ResNet. Mini-Batch Match Retrieval loss pulls matching image-text pairs close. Enables intuitive refinement in fashion search, e.g., add 'Sleeves', remove 'Green'. No need for supervised data of before/after manipulations; uses noisy catalog data. In consumer apps like photo search, natural language queries retrieve visually similar content by vector arithmetic in shared space, bypassing manual metadata.

-----

-----

Phase: [EXPLOITATION]

### Source [59]: https://zilliz.com/blog/combine-image-and-text-how-multimodal-retrieval-transforms-search

Query: How do shared embedding spaces in multimodal models enable intuitive semantic image retrieval in consumer applications like photo search engines, where natural language queries retrieve visually similar content without explicit metadata?

Answer: Multimodal retrieval combines text and images in shared embedding space via CLIP-like models for text-to-image retrieval. Composed Image Retrieval (CIR) uses reference image + text for nuanced queries. Models like Pic2Word map image embeddings to pseudo-word tokens in textual space, combining with text for retrieval. CompoDiff uses diffusion to condition visual embeddings on text. CIReVL generates/modifies captions for text embedding retrieval. MagicLens processes image+text into unified embedding. Enables zero-shot retrieval without metadata, as shared space aligns semantics. In photo search engines, natural language refines visual search intuitively, retrieving similar content via cross-modal similarity without explicit tags.

-----

-----

Phase: [EXPLOITATION]

### Source [60]: https://huggingface.co/blog/multimodal-sentence-transformers

Query: How do shared embedding spaces in multimodal models enable intuitive semantic image retrieval in consumer applications like photo search engines, where natural language queries retrieve visually similar content without explicit metadata?

Answer: Multimodal embedding models map text, images, audio, video into shared embedding space, allowing text query comparison against images via similarity. E.g., encode text 'vehicle parked near building' and image URLs; compute cross-modal similarities. encode_query() and encode_document() apply modality-specific prompts. Enables visual document retrieval, cross-modal search without metadata. Rerankers score mixed-modality pairs for refinement. Retrieve with embeddings over millions of docs, rerank top-k. Shared space preserves relative ordering despite modality gap, enabling semantic image retrieval from natural language in photo search apps.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="2025-the-year-ai-reasoning-models-took-over-a-month-by-month.md">
<details>
<summary>2025: The Year AI Reasoning Models Took Over — A Month-by-Month Review of Frontier Breakthroughs</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://medium.com/data-science-in-your-pocket/2025-the-year-ai-reasoning-models-took-over-a-month-by-month-review-of-frontier-breakthroughs-6ea2163f854f>

https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png

**Data Science in Your Pocket**

·

Follow publication

[https://miro.medium.com/v2/resize:fill:38:38/1*azLPGT6SA58kykLPlca3TQ.jpeg](https://medium.com/data-science-in-your-pocket?source=post_page---post_publication_sidebar-60130df77e02-6ea2163f854f---------------------------------------)

YouTube : [https://www.youtube.com/@datascienceinyourpocket](https://www.youtube.com/@datascienceinyourpocket)

# 2025: The Year AI Reasoning Models Took Over — A Month-by-Month Review of Frontier Breakthroughs

[https://miro.medium.com/v2/resize:fill:32:32/1*q4zm4wxMXyaMzEqoG-tY-Q.jpeg](https://medium.com/@gsaidheeraj?source=post_page---byline--6ea2163f854f---------------------------------------)

[Sai Dheeraj Gummadi](https://medium.com/@gsaidheeraj?source=post_page---byline--6ea2163f854f---------------------------------------)

8 min read

·

Dec 31, 2025

Share

Press enter or click to view image in full size

https://miro.medium.com/v2/resize:fit:700/0*RW7aGAHFp_rbpE4D

In 2025, the AI landscape shifted dramatically from scaling parameters to mastering reasoning. “Thinking” or chain-of-thought models became the standard, enabling AI to break down complex problems step-by-step. This led to explosive progress on tough benchmarks like GPQA (PhD-level science), AIME (high-school math olympiad), SWE-bench (real-world coding), and MMMU (multimodal understanding).

Chinese open-source models disrupted the market early, proving frontier performance didn’t require massive compute. By year-end, a November-December frenzy saw four major labs release their most advanced models in rapid succession, pushing AI closer to — and in some cases beyond — human expert levels on specialized tasks.

This review chronicles the key frontier models released in 2025 month by month, highlighting the benchmarks they dominated, their innovations, and how they stack up against human performance.

> My book with 20+ End to End Data Science Case Studies from 5 different domains is available on Amazon.

[**Cracking Data Science Case Study Interview: Data, Features, Models and System Design** \\
\\
**Amazon.com: Cracking Data Science Case Study Interview: Data, Features, Models and System Design eBook : Gummadi, Sai…**\\
\\
www.amazon.com](https://www.amazon.com/Cracking-Data-Science-Study-Interview-ebook/dp/B0FF6CT6SW/ref=sr_1_1?source=post_page-----6ea2163f854f---------------------------------------)

## January–February: early 2025 consolidation

By early 2025, the field is led by late‑2024 models (GPT‑4.1/4o, Claude 3.5, Gemini 2.0, DeepSeek‑V3, Llama 3.3), but evaluation hubs like Epoch and emerging councils start harmonizing multi‑benchmark leaderboards. Human‑competitive scores on standard MMLU and GSM8K are already common, so attention shifts to harder math and agentic tasks.​

You can frame Jan–Feb as the “baseline” chapter:

- MMLU regular at or above 85–90% for top models, near or above typical graduate‑level human performance on those question formats.​
- GSM8K and standard coding benchmarks largely saturated by best models; the gap is now in robustness, tool use, and long‑horizon tasks.​

## March: Gemini 2.5 Pro and Deep‑Think style reasoning

Gemini 2.5 Pro (released around March 2025) is Google’s first “deep thinking” reasoning flagship with a 1M‑token context window and native multimodal support.​

Benchmarks to highlight:

- AIME 2025 around 88% for math olympiad‑style problems, competitive with top high‑school olympiad contestants though still shy of gold‑medalist levels near 90–95%.​
- GPQA/grad‑level QA in the mid‑80% range; comparable to strong PhD‑track students on those curated questions.​
- GSM8K ~97% and high 80s F1 on MMLU, indicating saturation on many “standard” academic benchmarks.​

Novelty angle:

- Deep Think mode: explicit slow‑thinking inference similar to OpenAI’s “o‑series,” trading latency and cost for better chain‑of‑thought robustness.​
- 1M‑token context: several orders of magnitude beyond human working memory, letting the model process book‑scale inputs but still limited by attention patterns and retrieval tooling.​

## April: o3 / GPT‑4.5 style “deliberate” models

OpenAI’s intermediate “o3/high” and “4.5”‑class models reach strong performance on multi‑benchmark suites and Chatbot Arena but are later overshadowed by GPT‑5.​

Benchmarks worth mentioning:

- Near‑SOTA on math and coding (AIME 2025 in the high 80s, SWE‑bench ~75–80% style numbers from public comparisons).​
- Very strong Chatbot or LMArena Elo around the 1400s for top instruction‑following and general‑purpose capabilities, rivaling earlier GPT‑4 variants.​

Novelty:

- Explicit “thinking” tiers and cost‑latency trade‑offs (low/medium/high) foreshadow GPT‑5’s multi‑tier lineup.​

## May–June: DeepSeek R1 and open‑source reasoning surge

DeepSeek R1 and its R1‑0528 update become the first widely‑accessible open‑weight models that are clearly in the frontier reasoning conversation.​

Benchmarks:

- AIME 2025 jumps from ~70% in earlier R1 releases to ~87.5% on the May 28 revision, putting it around the same band as Gemini 2.5 and just under models like Grok 3/4 and GPT‑5.​
- Strong performance on math‐heavy and logical benchmarks while remaining significantly cheaper to train and run than many Western closed models.​

Novelty:

- Heavy use of reinforcement learning for reasoning traces, and broad distill lines (R1‑distill on Qwen/Llama backbones) that make “thinking” accessible on commodity hardware.​
- Aggressive cost efficiency: training costs in the low‑to‑mid single‑digit millions USD compared with tens of millions for comparable GPT‑class models.​

In the same window, Gemini 2.5 Pro Preview (June) and Gemini 2.5 Flash variants start appearing on aggregate leaderboards, scoring above 60% on composite multi‑benchmark scores and surfacing near the top on complex multimodal tests.​

## July: Grok 4 and the first >85% GPQA Diamond

July is pivotal: Grok 4 from xAI takes the top slot in several independent intelligence indices.​

Benchmarks (from AAII / July 2025 Intelligence Index):

- GPQA Diamond: 88% — an all‑time high, surpassing Gemini 2.5 Pro’s 84% and matching or beating many subject‑matter experts on those grad‑level science questions.​
- Humanity’s Last Exam: 24%, beating Gemini 2.5 Pro’s 21%; this benchmark is designed as an ultra‑hard cross‑domain exam approximating top‑tier human generalists.​
- MMLU‑Pro: 87%, joint highest with Gemini 2.5 Pro, firmly in the expert‑human performance band.​
- AIME 2025: around 93% in embedded evaluations, exceeding typical IMO cutoff‑level performance.​

Novelty:

- Massive training scale on the “Colossus” cluster (>200k H100‑class GPUs), plus stronger RL‑based reasoning and integrated tool use (“agentic” model with real‑time web, code and system tools).​
- Emphasis on transparency through “Think” style modes and thought summaries, bringing explicit reasoning traces closer to human scratch‑work.​

## August: GPT‑5 arrives

GPT‑5 (announced 6 August 2025) becomes the anchor of OpenAI’s lineup, with integrated “built‑in thinking” and multiple pricing tiers.​

## Get Sai Dheeraj Gummadi’s stories in your inbox

Key benchmarks (from multi‑model comparisons and leaderboards):

- AIME 2025: ~94.6% — top of public leaderboards, effectively superhuman relative to median contest participants and around or above typical gold medalist performance.​
- GPQA: ~88.4%, slightly above Grok 4 and Gemini 2.5 Pro, and higher than most tested PhD‑level human baselines reported in earlier GPQA work.​
- SWE‑bench: ~74.9% pass rate, near leading scores on large‑scale real‑world GitHub issues and at least competitive with strong professional developers under time pressure.​
- Composite multi‑benchmark scores: GPT‑5 variants score near the top on multi‑benchmark dashboards, often trading first place with Gemini 3 Pro Preview or Claude 4.5 on specific suites.​

Novelty:

- Unified multi‑tier family (low/medium/high/Pro) with different “thinking depth” and tool‑use profiles, enabling cost‑performance tuning and explicit slow‑mode reasoning.​
- Much stronger reliability in math and coding, with near‑perfect scores on some coding correctness tests (e.g., HumanEval‑style tasks in the high 90s).​

## September: cross‑lab SOTA arms race

By September 2025, several analyses compare GPT‑5, Grok 4, Gemini 2.5 Pro, Qwen 3 Max, Claude Opus 4.1 side‑by‑side on real‑world workloads.​

Representative numbers:

- GPT‑5: AIME 94.6%, GPQA 88.4%, SWE‑bench 74.9%, Intelligence Index 69, 400k context.​
- Grok 4: AIME ~93%, HumanEval coding ~98%, mid‑80s on GPQA, strong Chatbot/LMArena preference.​
- Gemini 2.5 Pro: AIME 88%, GPQA 84%, SWE‑bench ~63.8%, Intelligence Index 65, 1M‑token context with strong video/audio input.​
- Qwen 3 / Qwen 3 Max: AIME around 80–81%, top‑6 on LMArena, strong multi‑lingual performance and cost efficiency as open/enterprise offerings.​
- Claude Opus 4.1: AIME high‑70s, GPQA ~81%, SWE‑bench ~74.5%, very strong on complex text reasoning and extended tool‑based tasks.​

Novelty themes to spotlight:

- Emergence of agentic capabilities: many of these models are evaluated on “Terminal‑Bench” style tasks that require multi‑step computer control, not just Q&A.​
- Public multi‑benchmark councils (Epoch, LM Council) reduce cherry‑picking; models are ranked across 15–20 tasks with uncertainty intervals.​

## October–December: Gemini 3, Claude 4.5, Llama 4 and the open‑weight wave

Late 2025 brings a wave of updates rather than completely new paradigms. You can frame this as the chapter where frontier performance spreads to open models and specialized enterprise systems.​

Key points:

- Gemini 3 Pro Preview shows the highest scores on several composite benchmark suites (e.g., >90% on very hard reasoning suites and top overall multi‑benchmark scores).​
- Claude Sonnet 4.5 tops several reasoning and safety‑adjusted benchmarks, and is reported to sustain complex autonomous workflows for tens of hours.​
- Llama 4 (Scout/Maverick) and Qwen 3 make open‑weight models viable for tasks that previously required GPT‑class closed models, including high‑level coding and multi‑modal reasoning.​
- Enterprise‑focused models like Cohere Command A and Mistral’s Magistral Medium prioritize controllability, RAG‑friendliness, and deployment efficiency over topping single‑number leaderboards.​

Novelty:

- Context windows in the multi‑million token range (Llama 4 Scout, Gemini 3 Pro) start to redefine document‑scale workflows.​
- Open‑source and open‑weight ecosystems (DeepSeek V3.1, Qwen3, Llama 4, Mistral/Mixtral) deliver near‑frontier performance with permissive licenses and aggressive MoE efficiency.​

## Benchmarks vs humans: where models stand

You’ll want one or two sections that explicitly answer “are we past human?” per task family.

### Math and STEM benchmarks

- AIME 2025: top models (GPT‑5, Grok 4, DeepSeek R1, Gemini 2.5 Pro) sit in the 88–95% band. Typical good AIME performers are far lower; elite olympiad students cluster nearer these levels, so frontier models are operating in high‑olympiad territory.​
- GPQA / GPQA Diamond: GPT‑5 around 88.4%, Grok 4 at 88%, Gemini 2.5 Pro near 84%. These are at or above typical human experts on those question sets (original GPQA work framed ~60–70% as strong expert).​
- Humanity’s Last Exam and FrontierMath: Grok 4’s ~24% on HLE and GPT‑5’s mid‑20s percentile on ultra‑hard math show substantial gaps remain on adversarial, research‑like problems; strong human researchers still dominate here.​

### Coding and software engineering

- SWE‑bench: GPT‑5 and Claude Opus 4.1 sit in the mid‑70s on full GitHub issue resolution, compared to far lower rates for earlier GPT‑4‑class models. Human professional baselines vary, but these scores indicate parity or advantage on many isolated tickets under ideal conditions.​
- HumanEval and LiveCodeBench: Grok 4 near 98% on HumanEval‑style tasks, GPT‑5 and Gemini 2.5 Pro in similarly high bands, meaning near‑perfect performance on short coding puzzles but still limited in large‑system refactors and long‑term maintenance.​

## General knowledge, language, and multimodal

- MMLU / MMLU‑Pro: frontier models cluster between 85–90% on the harder variants, consistent with or above strong college‑educated human generalists.​
- CommonsenseQA, SQuAD, GSM8K etc. are essentially saturated; gains are marginal and focus shifts to calibration, hallucination and safety.​
- Video and audio understanding benchmarks (e.g., VideoMME) show Gemini 2.5 Pro and Gemini‑Veo stacks taking the lead, but direct human comparison is less standardized.​

A nice narrative hook: models are superhuman on many curated tests, roughly human‑level on complex coding and broad knowledge, but still clearly sub‑human on open‑ended scientific reasoning, long‑horizon planning, and real‑world accountability.

## Architectural novelties that actually mattered

Rather than treating 2025 as “more parameters,” anchor your closing sections on what changed qualitatively.

### 1\. Deliberate/“thinking” modes

Models like GPT‑5, Gemini 2.5/3, Grok 4, Claude 4.x and DeepSeek R1 all converge on some form of explicit slow‑thinking: long chain‑of‑thought, self‑reflection loops, or intermediate scratchpads. This moves performance on hard reasoning tests more than simple scale‑ups.​

### 2\. Mixture‑of‑Experts and efficient scale

DeepSeek V3.1, Qwen3, Llama 4, Mixtral 8x22B and similar models push sparse MoE architectures so that only a subset of experts fire per token, delivering high benchmark numbers at much lower active parameter counts. This is key for open‑weight accessibility and on‑prem deployment.​

### 3\. Long context and multimodality

1M‑token contexts (Gemini 2.5 Pro) and multi‑million‑token contexts (Llama 4 Scout, Gemini 3 Pro) redefine what “one session” can contain, especially when combined with native image, audio, and video understanding. Human working memory is tiny by comparison, but humans still win at building persistent abstractions over months or years.​

### 4\. Agentic evaluation and tool use

Benchmarks like Terminal‑Bench‑Hard and multi‑tool suites appear in late‑2025 indices, measuring the ability to drive a shell, browser, or IDE over many steps. Frontier models integrate tools deeply (search, code execution, file systems), moving closer to “AI employee” workflows rather than chatbots.​.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="data-llm-from-principles-to-practices.md">
<details>
<summary>Data ×\\times×LLM: From Principles to Practices</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://arxiv.org/html/2505.18458v1>

HTML conversions [sometimes display errors](https://info.dev.arxiv.org/about/accessibility_html_error_messages.html) due to content that did not convert correctly from the source. This paper uses the following packages that are not yet supported by the HTML conversion tool. Feedback on these issues are not necessary; they are known and are being worked on.

- failed: CJKutf8
- failed: forest

Authors: achieve the best HTML results from your LaTeX submissions by following these [best practices](https://info.arxiv.org/help/submit_latex_best_practices.html).

[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)

arXiv:2505.18458v1 \[cs.DB\] 24 May 2025

# Data ×\\times×LLM: From Principles to Practices

Report issue for preceding element

Xuanhe Zhou15,
Junxuan He15,
Wei Zhou15,
Haodong Chen15,
Zirui Tang15,
Haoyu Zhao15,
Xin Tong1,
Guoliang Li2,
Youmin Chen1,
Jun Zhou1,
Zhaojun Sun1,
Binyuan Hui3,
Shuo Wang2,
Conghui He4,

Zhiyuan Liu2,
Jingren Zhou3,
Fan Wu1

[https://github.com/weAIDB/awsome-data-llm](https://github.com/weAIDB/awsome-data-llm "")
5 Co-first authors with equal contributions.

1Shanghai Jiao Tong University
2Tsinghua University
3Alibaba Group
4Shanghai AI Laboratory

Report issue for preceding element

# Advances and Challenges in Data×\\times×LLM

Report issue for preceding element

Xuanhe Zhou15,
Junxuan He15,
Wei Zhou15,
Haodong Chen15,
Zirui Tang15,
Haoyu Zhao15,
Xin Tong1,
Guoliang Li2,
Youmin Chen1,
Jun Zhou1,
Zhaojun Sun1,
Binyuan Hui3,
Shuo Wang2,
Conghui He4,

Zhiyuan Liu2,
Jingren Zhou3,
Fan Wu1

[https://github.com/weAIDB/awsome-data-llm](https://github.com/weAIDB/awsome-data-llm "")
5 Co-first authors with equal contributions.

1Shanghai Jiao Tong University
2Tsinghua University
3Alibaba Group
4Shanghai AI Laboratory

Report issue for preceding element

# A Survey of LLM ×\\times× DATA

Report issue for preceding element

Xuanhe Zhou15,
Junxuan He15,
Wei Zhou15,
Haodong Chen15,
Zirui Tang15,
Haoyu Zhao15,
Xin Tong1,
Guoliang Li2,
Youmin Chen1,
Jun Zhou1,
Zhaojun Sun1,
Binyuan Hui3,
Shuo Wang2,
Conghui He4,

Zhiyuan Liu2,
Jingren Zhou3,
Fan Wu1

[https://github.com/weAIDB/awsome-data-llm](https://github.com/weAIDB/awsome-data-llm "")
5 Co-first authors with equal contributions.

1Shanghai Jiao Tong University
2Tsinghua University
3Alibaba Group
4Shanghai AI Laboratory

Report issue for preceding element

###### Abstract

Report issue for preceding element

The integration of large language model (LLM) and data management (DATA) is rapidly redefining both domains. In this survey, we comprehensively review the bidirectional relationships. On the one hand, DATA4LLM, spanning large-scale data processing, storage, and serving, feeds LLMs with high quality, diversity, and timeliness of data required for stages like pre-training, post-training, retrieval-augmented generation, and agentic workflows: (i)𝑖(i)( italic\_i ) Data processing for LLMs includes scalable acquisition, deduplication, filtering, selection, domain mixing, and synthetic augmentation; (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) Data Storage for LLMs focuses on efficient data and model formats, distributed and heterogeneous storage hierarchies, KV-cache management, and fault-tolerant checkpointing; (i⁢i⁢i)𝑖𝑖𝑖(iii)( italic\_i italic\_i italic\_i ) Data serving for LLMs tackles challenges in RAG (e.g., knowledge post-processing), LLM inference (e.g., prompt compression, data provenance), and training strategies (e.g., data packing and shuffling). On the other hand, in LLM4DATA, LLMs are emerging as general-purpose engines for data management. We review recent advances in (i)𝑖(i)( italic\_i ) data manipulation, including automatic data cleaning, integration, discovery; (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) data analysis, covering reasoning over structured, semi-structured, and unstructured data, and (i⁢i⁢i)𝑖𝑖𝑖(iii)( italic\_i italic\_i italic\_i ) system optimization (e.g., configuration tuning, query rewriting, anomaly diagnosis), powered by LLM techniques like retrieval-augmented prompting, task-specialized fine-tuning, and multi-agent collaboration.

Report issue for preceding element

###### Index Terms:

Report issue for preceding element
Large Language Model, Data Management, DATA4LLM, LLM4DATA

## 1 INTRODUCTION

Report issue for preceding element

Large language models (LLMs111We use LLMs to refer to billion-scale language models capable of supporting general NLP tasks \[ [478](https://arxiv.org/html/2505.18458v1#bib.bib478 "")\] or multimodal tasks \[ [452](https://arxiv.org/html/2505.18458v1#bib.bib452 ""), [323](https://arxiv.org/html/2505.18458v1#bib.bib323 "")\].) have made remarkable progress in both general domain applications (e.g., open-domain question answering \[ [335](https://arxiv.org/html/2505.18458v1#bib.bib335 "")\], cross-modal video summarization \[ [176](https://arxiv.org/html/2505.18458v1#bib.bib176 "")\], general-purpose code generation \[ [192](https://arxiv.org/html/2505.18458v1#bib.bib192 "")\]) and specific domain applications (e.g., biomedical literature analysis \[ [400](https://arxiv.org/html/2505.18458v1#bib.bib400 "")\], legal document review \[ [222](https://arxiv.org/html/2505.18458v1#bib.bib222 "")\], SQL generation for business intelligence \[ [251](https://arxiv.org/html/2505.18458v1#bib.bib251 "")\]). As shown in Figure 1, apart from technical advances in LLMs\[ [290](https://arxiv.org/html/2505.18458v1#bib.bib290 ""), [64](https://arxiv.org/html/2505.18458v1#bib.bib64 ""), [467](https://arxiv.org/html/2505.18458v1#bib.bib467 ""), [302](https://arxiv.org/html/2505.18458v1#bib.bib302 ""), [242](https://arxiv.org/html/2505.18458v1#bib.bib242 ""), [228](https://arxiv.org/html/2505.18458v1#bib.bib228 "")\], data management has emerged as a critical factor in unlocking LLMs’ full potential in these applications (DATA4LLM). It includes efficient and scalable solutions for data processing, storage, and serving across the LLM lifecycle, as evidenced in recent academic studies \[ [158](https://arxiv.org/html/2505.18458v1#bib.bib158 ""), [286](https://arxiv.org/html/2505.18458v1#bib.bib286 ""), [255](https://arxiv.org/html/2505.18458v1#bib.bib255 "")\] and industry reports \[ [328](https://arxiv.org/html/2505.18458v1#bib.bib328 ""), [441](https://arxiv.org/html/2505.18458v1#bib.bib441 ""), [69](https://arxiv.org/html/2505.18458v1#bib.bib69 ""), [39](https://arxiv.org/html/2505.18458v1#bib.bib39 "")\]. Conversely, LLM-powered techniques are increasingly being adopted to enhance data management tasks, such as data manipulation, analysis, and system optimization (LLM4DATA).

Report issue for preceding element

DATA4LLM.
Effective data management is fundamental to the scalable development and deployment of LLMs.
To illustrate this, we highlight representative scenarios where LLMs depend on specialized techniques for data processing, storage, and serving across various stages of the LLM lifecycle.

Report issue for preceding element

Example-① Data Processing for LLMs.
Processing a large-scale training dataset (e.g., ∼similar-to\\sim∼4 TB multi-modal tokens utilized in Qwen2.5-VL pretraining \[ [70](https://arxiv.org/html/2505.18458v1#bib.bib70 "")\]) poses several challenges.
First, acquiring diverse raw data (e.g., over 10,000 object categories for visual grounding) demands substantial efforts in data collection (Section [2.2.1](https://arxiv.org/html/2505.18458v1#S2.SS2.SSS1 "2.2.1 Data Acquisition ‣ 2.2 Data Processing for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")) and, in many cases, data synthesis (Section [2.2.6](https://arxiv.org/html/2505.18458v1#S2.SS2.SSS6 "2.2.6 Data Distillation and Synthesis ‣ 2.2 Data Processing for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")).
Second, preparing high-quality training samples requires robust preprocessing, including rigorous data filtering (Section [2.2.3](https://arxiv.org/html/2505.18458v1#S2.SS2.SSS3 "2.2.3 Data Filtering ‣ 2.2 Data Processing for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")), along with dedicated evaluation approaches.
Third, the overall performance of LLMs depends heavily on an end-to-end pipeline that effectively schedules and coordinates these processing tasks, especially for the pretraining stage (Section [2.2.7](https://arxiv.org/html/2505.18458v1#S2.SS2.SSS7 "2.2.7 End-to-End Data Processing Pipelines ‣ 2.2 Data Processing for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")).

Report issue for preceding element

Example-② Data Storage for LLMs.
Managing storage for LLMs, spanning both training datasets (see Example-①) and massive model parameters (e.g., DeepSeek-R1 with 671B parameters \[ [163](https://arxiv.org/html/2505.18458v1#bib.bib163 "")\]), poses significant challenges.
First, large-scale datasets must be partitioned and distributed across multiple storage nodes, introducing challenges in data placement and consistency management (Section [2.3.2](https://arxiv.org/html/2505.18458v1#S2.SS3.SSS2 "2.3.2 Techniques for LLM Data Distribution ‣ 2.3 Data Storage for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")). Second, to support efficient LLM training and inference, these storage nodes must deliver high I/O throughput for timely data transfer to compute nodes (Section [2.3.4](https://arxiv.org/html/2505.18458v1#S2.SS3.SSS4 "2.3.4 Data Movement ‣ 2.3 Data Storage for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")). Third, the massive size of model parameters increases the risk of training interruptions, necessitating robust fault tolerance mechanisms to recover and resume training from intermediate states (Section [2.3.5](https://arxiv.org/html/2505.18458v1#S2.SS3.SSS5 "2.3.5 Data Fault Tolerance ‣ 2.3 Data Storage for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")).

Report issue for preceding element

Example–③ Data Serving for LLMs. Data serving plays a critical role in selecting and preparing input data (e.g., the task-specific prompts), directly affecting the quality of LLM’s responses. Taking retrieval-augmented generation (RAG) as an example, EyeLevel.ai \[ [37](https://arxiv.org/html/2505.18458v1#bib.bib37 "")\] observed that when relying solely on vector similarity, RAG accuracy declines notably with 10,000-page documents, and the performance degradation can reach up to 12% with 100,000 pages (still fewer than enterprise-scale datasets). Several challenges arise in this context. First, the retrieved knowledge is typically noisy and must be filtered and re-ranked to ensure relevance and factual accuracy (Section [2.4.1](https://arxiv.org/html/2505.18458v1#S2.SS4.SSS1 "2.4.1 Data Shuffling ‣ 2.4 Data Serving for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")). Second, the retrieved content is often lengthy exceeding the input capacity or comprehension of LLMs, necessitating effective compression techniques to preserve utility while improving performance (Section [2.4.2](https://arxiv.org/html/2505.18458v1#S2.SS4.SSS2 "2.4.2 Data Compression ‣ 2.4 Data Serving for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")).

Report issue for preceding element

LLM4DATA.
Conversely, various LLM-based techniques can be leveraged to enhance core data management tasks, including data manipulation, data analysis, and system-level optimization.
The following examples illustrate how LLMs can be applied to improve these tasks in practice.

Report issue for preceding element

Example-① LLM-based Data Manipulation.
Data manipulation, including cleaning, integration, and discovery, is critical for ensuring high-quality datasets.
Traditional methods depend on rigid rules and domain-specific configurations, requiring extensive manual efforts and struggling with complex data samples \[ [244](https://arxiv.org/html/2505.18458v1#bib.bib244 ""), [78](https://arxiv.org/html/2505.18458v1#bib.bib78 ""), [74](https://arxiv.org/html/2505.18458v1#bib.bib74 "")\].
For instance, standardizing date formats (e.g., “Fri Jan 1st 10:36:28 2021” vs. “1996.07.10 AD at 15:08:56”) or resolving textual inconsistencies (e.g., “Monticello VA, Jasper” vs. “Monticello VAA”) typically requires intricate programming scripts or handcrafted constraints \[ [320](https://arxiv.org/html/2505.18458v1#bib.bib320 ""), [440](https://arxiv.org/html/2505.18458v1#bib.bib440 "")\].
These approaches also struggle with cross-row error detection, such as mismatched city-state-zip entries.
In contrast, LLMs can infer semantic similarities and autonomously generate cleaning workflows to resolve such inconsistencies without requiring explicit rule definitions \[ [238](https://arxiv.org/html/2505.18458v1#bib.bib238 ""), [440](https://arxiv.org/html/2505.18458v1#bib.bib440 ""), [461](https://arxiv.org/html/2505.18458v1#bib.bib461 "")\].
This semantic understanding enables LLMs to adapt flexibly to diverse data issues and support more scalable and context-aware data manipulation (Section [3.1](https://arxiv.org/html/2505.18458v1#S3.SS1 "3.1 LLM for Data Manipulation ‣ 3 LLM for Data Management ‣ Data × LLM: From Principles to Practices")).

Report issue for preceding element

Example-② LLM-based Data Analysis.
Data analysis over heterogeneous sources, such as medical records and transactional data, is essential in many real-world applications.
Traditional deep learning models, while effective at performing specific semantic-level analysis, struggle to generalize across diverse data formats and task types.
For instance, tasks such as table extraction and table-based question answering across heterogeneous sources (e.g., relational tables and knowledge graphs) often require the development of separate, specialized models.
This process is both resource-intensive and difficult to scale.
In contrast, LLMs offer a unified reasoning framework that leverages broad semantic understanding, enabling them to support a wide range of analytical tasks across various data modalities with greater flexibility and reduced efforts for task-specific engineering (Section [3.2](https://arxiv.org/html/2505.18458v1#S3.SS2 "3.2 LLM for Data Analysis ‣ 3 LLM for Data Management ‣ Data × LLM: From Principles to Practices")).

Report issue for preceding element

Example-③ LLM-based System Optimization.
System optimization entails configuring parameters (e.g., memory settings) and monitoring runtime status (e.g., resource utilization) to ensure optimal system performance.
Traditional approaches, such as manual tuning or deep learning-based methods, are time-consuming and inefficient \[ [480](https://arxiv.org/html/2505.18458v1#bib.bib480 "")\].
For instance, methods of Bayesian Optimization (BO) or Reinforcement Learning (RL) require numerous workload replays over 20 hours to identify promising configurations for a single TPC-H workload \[ [178](https://arxiv.org/html/2505.18458v1#bib.bib178 "")\].
Moreover, root cause analysis over anomalies can be error-prone, particularly in multi-cause scenarios where metrics are highly interdependent \[ [496](https://arxiv.org/html/2505.18458v1#bib.bib496 "")\].
In contrast, LLMs offer a new paradigm by integrating domain knowledge (e.g., tuning manuals) and applying advanced reasoning to instruct optimization.
By leveraging retrieval-augmented prompts, LLMs can efficiently identify root causes or recommend precise configurations, enabling faster and more accurate optimization in complex environments \[ [495](https://arxiv.org/html/2505.18458v1#bib.bib495 ""), [249](https://arxiv.org/html/2505.18458v1#bib.bib249 ""), [224](https://arxiv.org/html/2505.18458v1#bib.bib224 "")\] (Section [3.3](https://arxiv.org/html/2505.18458v1#S3.SS3 "3.3 LLM for Data System Optimization ‣ 3 LLM for Data Management ‣ Data × LLM: From Principles to Practices")).

Report issue for preceding element

### 1.1 Techniques of DATA4LLM

Report issue for preceding element

Data Characteristics across LLM Stages (§ [2.1](https://arxiv.org/html/2505.18458v1#S2.SS1 "2.1 Data Characteristics across LLM Stages ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")). As shown in Figure 1, datasets play a critical role in enabling the desired capabilities at each LLM stage, including (1) pre-training, (2) continual pre-training, (3) fine-tuning, (4) reinforcement learning, (5) retrieval-augmented generation (RAG), (6) LLM agents, and (7) evaluation. For each stage, we separately analyze the required data across multiple dimensions (e.g., data format, scale, and domain diversity).

Report issue for preceding element

Data Processing for LLMs (§ [2.2](https://arxiv.org/html/2505.18458v1#S2.SS2 "2.2 Data Processing for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")).
We introduce techniques to prepare high-quality datasets for LLMs based on a series of processing steps.

Report issue for preceding element

∙∙\\bullet∙Data Acquisition. Data acquisition aims to (1) extract relevant data (e.g., text and images) from noisy data sources with certain structures (e.g., dynamically rendered web pages) \[ [73](https://arxiv.org/html/2505.18458v1#bib.bib73 ""), [144](https://arxiv.org/html/2505.18458v1#bib.bib144 ""), [76](https://arxiv.org/html/2505.18458v1#bib.bib76 ""), [73](https://arxiv.org/html/2505.18458v1#bib.bib73 ""), [6](https://arxiv.org/html/2505.18458v1#bib.bib6 ""), [19](https://arxiv.org/html/2505.18458v1#bib.bib19 ""), [30](https://arxiv.org/html/2505.18458v1#bib.bib30 ""), [31](https://arxiv.org/html/2505.18458v1#bib.bib31 "")\], and (2) extract data from complicated data sources (e.g., scanned or handwritten documents) with techniques such as complex layout analysis \[ [203](https://arxiv.org/html/2505.18458v1#bib.bib203 ""), [18](https://arxiv.org/html/2505.18458v1#bib.bib18 ""), [398](https://arxiv.org/html/2505.18458v1#bib.bib398 ""), [181](https://arxiv.org/html/2505.18458v1#bib.bib181 ""), [397](https://arxiv.org/html/2505.18458v1#bib.bib397 ""), [414](https://arxiv.org/html/2505.18458v1#bib.bib414 ""), [258](https://arxiv.org/html/2505.18458v1#bib.bib258 ""), [327](https://arxiv.org/html/2505.18458v1#bib.bib327 ""), [413](https://arxiv.org/html/2505.18458v1#bib.bib413 "")\].

Report issue for preceding element

∙∙\\bullet∙Data Deduplication. Data deduplication aims to identify duplicates in large-scale textual or multi-modal data, including exact string matching  \[ [122](https://arxiv.org/html/2505.18458v1#bib.bib122 ""), [300](https://arxiv.org/html/2505.18458v1#bib.bib300 "")\], hash identification \[ [88](https://arxiv.org/html/2505.18458v1#bib.bib88 ""), [81](https://arxiv.org/html/2505.18458v1#bib.bib81 ""), [122](https://arxiv.org/html/2505.18458v1#bib.bib122 ""), [300](https://arxiv.org/html/2505.18458v1#bib.bib300 ""), [351](https://arxiv.org/html/2505.18458v1#bib.bib351 ""), [362](https://arxiv.org/html/2505.18458v1#bib.bib362 ""), [208](https://arxiv.org/html/2505.18458v1#bib.bib208 ""), [299](https://arxiv.org/html/2505.18458v1#bib.bib299 "")\], sample reweighing \[ [168](https://arxiv.org/html/2505.18458v1#bib.bib168 "")\] and embedding-based clustering \[ [46](https://arxiv.org/html/2505.18458v1#bib.bib46 ""), [390](https://arxiv.org/html/2505.18458v1#bib.bib390 ""), [364](https://arxiv.org/html/2505.18458v1#bib.bib364 "")\].

Report issue for preceding element

∙∙\\bullet∙Data Filtering. We review data filtering methods at two primary levels: (1) Sample-level filtering selects high-quality and diverse samples using strategies like perplexity measuring \[ [388](https://arxiv.org/html/2505.18458v1#bib.bib388 ""), [61](https://arxiv.org/html/2505.18458v1#bib.bib61 ""), [289](https://arxiv.org/html/2505.18458v1#bib.bib289 "")\], influence assessment \[ [255](https://arxiv.org/html/2505.18458v1#bib.bib255 ""), [169](https://arxiv.org/html/2505.18458v1#bib.bib169 "")\], clustering methods \[ [45](https://arxiv.org/html/2505.18458v1#bib.bib45 ""), [444](https://arxiv.org/html/2505.18458v1#bib.bib444 "")\], prompt-based scoring \[ [418](https://arxiv.org/html/2505.18458v1#bib.bib418 ""), [265](https://arxiv.org/html/2505.18458v1#bib.bib265 ""), [349](https://arxiv.org/html/2505.18458v1#bib.bib349 "")\], or mixes of these strategies \[ [286](https://arxiv.org/html/2505.18458v1#bib.bib286 ""), [84](https://arxiv.org/html/2505.18458v1#bib.bib84 ""), [126](https://arxiv.org/html/2505.18458v1#bib.bib126 "")\]; (2) Content-level filtering aims to remove undesirable or harmful content from large-scale datasets, such as toxic language, personal identifiable information (PII), biased statements \[ [269](https://arxiv.org/html/2505.18458v1#bib.bib269 ""), [276](https://arxiv.org/html/2505.18458v1#bib.bib276 "")\], and improper images and videos \[ [445](https://arxiv.org/html/2505.18458v1#bib.bib445 ""), [217](https://arxiv.org/html/2505.18458v1#bib.bib217 ""), [396](https://arxiv.org/html/2505.18458v1#bib.bib396 "")\].

Report issue for preceding element

∙∙\\bullet∙Data Selection. Data selection aims to select sub-datasets and evaluate their ability to accurately represent the target distribution, especially when handling diverse datasets or domains. There are methods like similarity-based data selection \[ [431](https://arxiv.org/html/2505.18458v1#bib.bib431 ""), [429](https://arxiv.org/html/2505.18458v1#bib.bib429 ""), [322](https://arxiv.org/html/2505.18458v1#bib.bib322 ""), [80](https://arxiv.org/html/2505.18458v1#bib.bib80 "")\], optimization-based data selection \[ [130](https://arxiv.org/html/2505.18458v1#bib.bib130 ""), [424](https://arxiv.org/html/2505.18458v1#bib.bib424 ""), [270](https://arxiv.org/html/2505.18458v1#bib.bib270 "")\], and model-based data selection \[ [472](https://arxiv.org/html/2505.18458v1#bib.bib472 "")\].

Report issue for preceding element

∙∙\\bullet∙Data Mixing. Data mixing aims to effectively integrate datasets from diverse domains without degrading quality or destabilizing LLM performance. Key techniques include:
(1) _Heuristic optimization_, which empirically tunes data ratios to enhance downstream performance. Examples include two-stage mixing \[ [139](https://arxiv.org/html/2505.18458v1#bib.bib139 "")\], source rebalancing \[ [351](https://arxiv.org/html/2505.18458v1#bib.bib351 "")\], and entropy-based weighting \[ [153](https://arxiv.org/html/2505.18458v1#bib.bib153 "")\];
(2) _Bilevel optimization_, which formulates data weighting as a nested optimization problem to jointly balance training and validation objectives \[ [303](https://arxiv.org/html/2505.18458v1#bib.bib303 ""), [135](https://arxiv.org/html/2505.18458v1#bib.bib135 "")\];
(3) _Distributionally robust optimization_, which enhances resilience to worst-case domain shifts by emphasizing underperforming or rare data domains \[ [428](https://arxiv.org/html/2505.18458v1#bib.bib428 ""), [279](https://arxiv.org/html/2505.18458v1#bib.bib279 "")\];
(4) _Model-based optimization_, which builds predictive models to map data mixing ratios to loss and task performance. Approaches include linear predictive modeling (e.g., REGMIX \[ [264](https://arxiv.org/html/2505.18458v1#bib.bib264 "")\]), nonlinear function fitting \[ [153](https://arxiv.org/html/2505.18458v1#bib.bib153 ""), [447](https://arxiv.org/html/2505.18458v1#bib.bib447 ""), [161](https://arxiv.org/html/2505.18458v1#bib.bib161 "")\], scaling law-based estimation \[ [324](https://arxiv.org/html/2505.18458v1#bib.bib324 "")\], and latent source attribution \[ [252](https://arxiv.org/html/2505.18458v1#bib.bib252 "")\].

Report issue for preceding element

∙∙\\bullet∙Data Synthesis. We introduce data synthesis techniques designed to address the following key challenges:
(1) _Mitigating harmful characteristics_ such as toxicity or bias, which can be inherited or amplified in synthetic data (e.g., program-aided verification \[ [502](https://arxiv.org/html/2505.18458v1#bib.bib502 "")\], semantic scoring \[ [174](https://arxiv.org/html/2505.18458v1#bib.bib174 "")\], and multi-agent consistency filtering \[ [350](https://arxiv.org/html/2505.18458v1#bib.bib350 "")\]);
(2) _Balancing data utility and privacy_, through privacy-preserving synthetic rewriting and key-entity obfuscation methods during the RAG stage \[ [457](https://arxiv.org/html/2505.18458v1#bib.bib457 "")\];
(3) _Generating diverse and logically consistent reasoning data_ using approaches like formal proof-based validation \[ [179](https://arxiv.org/html/2505.18458v1#bib.bib179 "")\], Chain-of-Thought (CoT) branching and error correction \[ [174](https://arxiv.org/html/2505.18458v1#bib.bib174 "")\], and high-quality problem synthesis guided by structure and complexity constraints \[ [261](https://arxiv.org/html/2505.18458v1#bib.bib261 ""), [450](https://arxiv.org/html/2505.18458v1#bib.bib450 "")\];
(4) _Automating human-like evaluation and feedback generation_ with LLM-based preference modeling \[ [71](https://arxiv.org/html/2505.18458v1#bib.bib71 "")\], judge models for response ranking \[ [482](https://arxiv.org/html/2505.18458v1#bib.bib482 "")\], and clustering-based diversity quantification \[ [92](https://arxiv.org/html/2505.18458v1#bib.bib92 "")\].

Report issue for preceding element

∙∙\\bullet∙Data Pipelines. We first introduce _frameworks_ that integrate basic data processing operators and interfaces, serving as the general foundation for building data pipelines \[ [90](https://arxiv.org/html/2505.18458v1#bib.bib90 ""), [306](https://arxiv.org/html/2505.18458v1#bib.bib306 ""), [373](https://arxiv.org/html/2505.18458v1#bib.bib373 "")\]. Then we showcase _typical pipelines_ with heuristic mechanisms that properly arrange these operators (mainly for LLM pretraining) \[ [312](https://arxiv.org/html/2505.18458v1#bib.bib312 ""), [237](https://arxiv.org/html/2505.18458v1#bib.bib237 ""), [311](https://arxiv.org/html/2505.18458v1#bib.bib311 "")\]. Finally, we discuss strategies that go beyond heuristic designs to further optimize these data processing pipelines \[ [91](https://arxiv.org/html/2505.18458v1#bib.bib91 "")\].

Report issue for preceding element

Data Storage for LLMs (§ [2.3](https://arxiv.org/html/2505.18458v1#S2.SS3 "2.3 Data Storage for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")). We review data storage techniques for LLMs from the following main aspects.

Report issue for preceding element

∙∙\\bullet∙Data Formats.
We review commonly-used dataset and model data formats for LLMs. Dataset formats include TFRecord\[ [44](https://arxiv.org/html/2505.18458v1#bib.bib44 "")\], MindRecord\[ [40](https://arxiv.org/html/2505.18458v1#bib.bib40 "")\] for multimodal data, and tf.data.Dataset that can be directly fed into LLMs \[ [43](https://arxiv.org/html/2505.18458v1#bib.bib43 "")\].
For model data storage, there are formats like Pickle\[ [13](https://arxiv.org/html/2505.18458v1#bib.bib13 "")\] and ONNX\[ [27](https://arxiv.org/html/2505.18458v1#bib.bib27 "")\].

Report issue for preceding element

∙∙\\bullet∙LLM Data Distribution. LLM data distribution aims to store data across multiple storage nodes in a cluster, which mainly serves for storing large-scale LLM training data. Key approaches include (1) distributed storage systems like JuiceFS \[ [16](https://arxiv.org/html/2505.18458v1#bib.bib16 "")\] and 3FS \[ [15](https://arxiv.org/html/2505.18458v1#bib.bib15 "")\]; and (2) heterogeneous storage systems for model data (e.g., across GPUs and CPUs) \[ [336](https://arxiv.org/html/2505.18458v1#bib.bib336 ""), [337](https://arxiv.org/html/2505.18458v1#bib.bib337 ""), [340](https://arxiv.org/html/2505.18458v1#bib.bib340 ""), [339](https://arxiv.org/html/2505.18458v1#bib.bib339 ""), [443](https://arxiv.org/html/2505.18458v1#bib.bib443 "")\].

Report issue for preceding element

∙∙\\bullet∙LLM Data Organization. LLM data organization aims to transform data into a format suitable for storage and retrieval (mainly for the RAG stage) in heterogeneous forms. First, for vector RAG, relevant techniques include content formatting \[ [98](https://arxiv.org/html/2505.18458v1#bib.bib98 ""), [173](https://arxiv.org/html/2505.18458v1#bib.bib173 ""), [57](https://arxiv.org/html/2505.18458v1#bib.bib57 ""), [89](https://arxiv.org/html/2505.18458v1#bib.bib89 "")\], chunking \[ [486](https://arxiv.org/html/2505.18458v1#bib.bib486 "")\], embedding \[ [94](https://arxiv.org/html/2505.18458v1#bib.bib94 ""), [24](https://arxiv.org/html/2505.18458v1#bib.bib24 ""), [250](https://arxiv.org/html/2505.18458v1#bib.bib250 "")\], compression \[ [50](https://arxiv.org/html/2505.18458v1#bib.bib50 ""), [385](https://arxiv.org/html/2505.18458v1#bib.bib385 ""), [386](https://arxiv.org/html/2505.18458v1#bib.bib386 ""), [386](https://arxiv.org/html/2505.18458v1#bib.bib386 "")\]. Second, for graph RAG, we discuss indexing techniques such as generating textual summary for quick retrieval \[ [127](https://arxiv.org/html/2505.18458v1#bib.bib127 ""), [165](https://arxiv.org/html/2505.18458v1#bib.bib165 ""), [136](https://arxiv.org/html/2505.18458v1#bib.bib136 "")\]. We also introduce the systems that integrate these techniques, including vector search engines \[ [125](https://arxiv.org/html/2505.18458v1#bib.bib125 ""), [26](https://arxiv.org/html/2505.18458v1#bib.bib26 ""), [34](https://arxiv.org/html/2505.18458v1#bib.bib34 ""), [25](https://arxiv.org/html/2505.18458v1#bib.bib25 "")\] and graph storage platforms \[ [293](https://arxiv.org/html/2505.18458v1#bib.bib293 ""), [65](https://arxiv.org/html/2505.18458v1#bib.bib65 ""), [1](https://arxiv.org/html/2505.18458v1#bib.bib1 "")\].

Report issue for preceding element

∙∙\\bullet∙LLM Data Movement. LLM data movement aims to improve the speed of data movement across storage and compute nodes.
Relevant techniques include (1) caching data \[ [220](https://arxiv.org/html/2505.18458v1#bib.bib220 ""), [162](https://arxiv.org/html/2505.18458v1#bib.bib162 ""), [476](https://arxiv.org/html/2505.18458v1#bib.bib476 "")\]; (2) offloading data/operator to multiple devices (e.g., across CPUs)  \[ [159](https://arxiv.org/html/2505.18458v1#bib.bib159 ""), [67](https://arxiv.org/html/2505.18458v1#bib.bib67 ""), [160](https://arxiv.org/html/2505.18458v1#bib.bib160 ""), [475](https://arxiv.org/html/2505.18458v1#bib.bib475 "")\]; and (3) overlapping of storage and computing in training stage \[ [473](https://arxiv.org/html/2505.18458v1#bib.bib473 ""), [485](https://arxiv.org/html/2505.18458v1#bib.bib485 "")\].

Report issue for preceding element

∙∙\\bullet∙LLM Model Data Fault Tolerance. LLM model data fault tolerance aims to enhance the ability to recover from system failures during model training.
Relevant techniques include (1) checkpointing \[ [292](https://arxiv.org/html/2505.18458v1#bib.bib292 ""), [195](https://arxiv.org/html/2505.18458v1#bib.bib195 ""), [410](https://arxiv.org/html/2505.18458v1#bib.bib410 ""), [395](https://arxiv.org/html/2505.18458v1#bib.bib395 "")\], which stores checkpoints across a hierarchical storage system;
and (2) redundant computation \[ [387](https://arxiv.org/html/2505.18458v1#bib.bib387 ""), [187](https://arxiv.org/html/2505.18458v1#bib.bib187 ""), [147](https://arxiv.org/html/2505.18458v1#bib.bib147 "")\], which replicates the state data of LLMs to support rapid fault recovery.

Report issue for preceding element

∙∙\\bullet∙KV Cache in LLMs. KV caching in LLMs is essential for enabling fast and efficient inference by managing key-value memory usage. Existing techniques include:
(1) _Memory layout and allocation_, which optimize the physical organization of KV memory for high performance and scalability \[ [221](https://arxiv.org/html/2505.18458v1#bib.bib221 ""), [436](https://arxiv.org/html/2505.18458v1#bib.bib436 "")\];
(2) _Storage offloading_, which places KV data on suitable storage media to balance speed and capacity \[ [198](https://arxiv.org/html/2505.18458v1#bib.bib198 ""), [148](https://arxiv.org/html/2505.18458v1#bib.bib148 "")\];
(3) _KV compression_, which reduces memory footprint through techniques like encoding compression \[ [266](https://arxiv.org/html/2505.18458v1#bib.bib266 ""), [256](https://arxiv.org/html/2505.18458v1#bib.bib256 ""), [151](https://arxiv.org/html/2505.18458v1#bib.bib151 "")\];
(4) _Efficient indexing_, which accelerates KV access via specialized retrieval structures \[ [448](https://arxiv.org/html/2505.18458v1#bib.bib448 ""), [484](https://arxiv.org/html/2505.18458v1#bib.bib484 "")\].

Report issue for preceding element

Data Serving for LLMs (§ [2.4](https://arxiv.org/html/2505.18458v1#S2.SS4 "2.4 Data Serving for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")). We provide an overview of data serving techniques tailored for LLMs from four aspects.

Report issue for preceding element

∙∙\\bullet∙LLM Data Shuffling.LLM data shuffling aims to determine the appropriate order of data application during stages like LLM training and RAG. In the training stage, we discuss data pruning techniques (e.g., sample-scoring-based approaches \[ [137](https://arxiv.org/html/2505.18458v1#bib.bib137 ""), [66](https://arxiv.org/html/2505.18458v1#bib.bib66 "")\], model-state-based approaches \[ [377](https://arxiv.org/html/2505.18458v1#bib.bib377 ""), [56](https://arxiv.org/html/2505.18458v1#bib.bib56 ""), [423](https://arxiv.org/html/2505.18458v1#bib.bib423 ""), [277](https://arxiv.org/html/2505.18458v1#bib.bib277 "")\]) and data-centric training strategies \[ [123](https://arxiv.org/html/2505.18458v1#bib.bib123 "")\]. In the RAG stage, we discuss RAG knowledge filtering \[ [281](https://arxiv.org/html/2505.18458v1#bib.bib281 ""), [115](https://arxiv.org/html/2505.18458v1#bib.bib115 ""), [87](https://arxiv.org/html/2505.18458v1#bib.bib87 "")\] and re-ranking \[ [128](https://arxiv.org/html/2505.18458v1#bib.bib128 ""), [12](https://arxiv.org/html/2505.18458v1#bib.bib12 ""), [319](https://arxiv.org/html/2505.18458v1#bib.bib319 ""), [47](https://arxiv.org/html/2505.18458v1#bib.bib47 "")\].

Report issue for preceding element

∙∙\\bullet∙LLM Data Compression.LLM data compression aims to compress the model’s input data to stay within the context window limit or to facilitate model understanding.
Relevant techniques include: (1) RAG knowledge compression (e.g., rule-based \[ [435](https://arxiv.org/html/2505.18458v1#bib.bib435 ""), [352](https://arxiv.org/html/2505.18458v1#bib.bib352 ""), [201](https://arxiv.org/html/2505.18458v1#bib.bib201 "")\] and model-based method \[ [102](https://arxiv.org/html/2505.18458v1#bib.bib102 ""), [338](https://arxiv.org/html/2505.18458v1#bib.bib338 "")\]);
and (2) prompt compression (e.g., metric-based \[ [190](https://arxiv.org/html/2505.18458v1#bib.bib190 ""), [191](https://arxiv.org/html/2505.18458v1#bib.bib191 "")\] and model-based method \[ [304](https://arxiv.org/html/2505.18458v1#bib.bib304 ""), [294](https://arxiv.org/html/2505.18458v1#bib.bib294 ""), [103](https://arxiv.org/html/2505.18458v1#bib.bib103 "")\]).

Report issue for preceding element

∙∙\\bullet∙LLM Training Data Packing.LLM training data packing aims to ensure uniform sequence lengths in training inputs.
Relevant techniques include: (1) short sequence insertion \[ [117](https://arxiv.org/html/2505.18458v1#bib.bib117 ""), [260](https://arxiv.org/html/2505.18458v1#bib.bib260 "")\];
(2) optimizing sequence combination \[ [219](https://arxiv.org/html/2505.18458v1#bib.bib219 ""), [317](https://arxiv.org/html/2505.18458v1#bib.bib317 "")\];
and (3) semantic-cased packing \[ [369](https://arxiv.org/html/2505.18458v1#bib.bib369 ""), [353](https://arxiv.org/html/2505.18458v1#bib.bib353 "")\]).

Report issue for preceding element

∙∙\\bullet∙LLM Inference Data Provenance.LLM inference data provenance aims to ensure the factual consistency of LLM-generated content.
Relevant techniques include: (1) embedding markers \[ [488](https://arxiv.org/html/2505.18458v1#bib.bib488 ""), [106](https://arxiv.org/html/2505.18458v1#bib.bib106 ""), [257](https://arxiv.org/html/2505.18458v1#bib.bib257 "")\];
and (2) statistical provenance \[ [213](https://arxiv.org/html/2505.18458v1#bib.bib213 "")\]).

Report issue for preceding element

### 1.2 Techniques of LLM4DATA

Report issue for preceding element

LLM for Data Manipulation (§ [3.1](https://arxiv.org/html/2505.18458v1#S3.SS1 "3.1 LLM for Data Manipulation ‣ 3 LLM for Data Management ‣ Data × LLM: From Principles to Practices")).LLMs have been increasingly applied to data manipulation tasks, with the goal of preparing high-quality datasets for non-LLM applications and enhancing data quality for downstream usage.
Key areas include data cleaning, data integration, and data discovery.

Report issue for preceding element

∙∙\\bullet∙Data Cleaning.
This task involves standardizing and refining datasets through a series of operations.
We highlight three major subtasks:
(1) Data Standardization, which reformats data samples using handcrafted standardization prompts \[ [280](https://arxiv.org/html/2505.18458v1#bib.bib280 ""), [63](https://arxiv.org/html/2505.18458v1#bib.bib63 "")\] or agents that generate cleaning operations or pipelines \[ [320](https://arxiv.org/html/2505.18458v1#bib.bib320 ""), [238](https://arxiv.org/html/2505.18458v1#bib.bib238 "")\];
(2) Data Error Processing, which identifies and corrects noisy data via direct LLM prompting \[ [104](https://arxiv.org/html/2505.18458v1#bib.bib104 ""), [468](https://arxiv.org/html/2505.18458v1#bib.bib468 ""), [440](https://arxiv.org/html/2505.18458v1#bib.bib440 "")\], context-enrichment techniques \[ [78](https://arxiv.org/html/2505.18458v1#bib.bib78 ""), [74](https://arxiv.org/html/2505.18458v1#bib.bib74 "")\], or task-specific fine-tuning for error handling \[ [440](https://arxiv.org/html/2505.18458v1#bib.bib440 "")\];
(3) Data Imputation, which fills in missing values using explicit imputation instructions and retrieval-augmented generation (RAG) methods \[ [129](https://arxiv.org/html/2505.18458v1#bib.bib129 "")\].

Report issue for preceding element

∙∙\\bullet∙Data Integration.
This task focuses on identifying and reconciling semantically related datasets across heterogeneous sources.
We review two core subtasks:
(1) Entity Matching, which aligns data entries referring to the same real-world entity using structured prompts \[ [309](https://arxiv.org/html/2505.18458v1#bib.bib309 ""), [134](https://arxiv.org/html/2505.18458v1#bib.bib134 "")\], sometimes augmented with predefined code-based reasoning strategies \[ [438](https://arxiv.org/html/2505.18458v1#bib.bib438 "")\];
(2) Schema Matching, which establishes correspondences between schema elements using direct prompting \[ [305](https://arxiv.org/html/2505.18458v1#bib.bib305 "")\], RAG techniques incorporating multiple models \[ [268](https://arxiv.org/html/2505.18458v1#bib.bib268 "")\], knowledge graph-based methods \[ [278](https://arxiv.org/html/2505.18458v1#bib.bib278 "")\], and agent-based workflow generation \[ [321](https://arxiv.org/html/2505.18458v1#bib.bib321 ""), [343](https://arxiv.org/html/2505.18458v1#bib.bib343 "")\].

Report issue for preceding element

∙∙\\bullet∙Data Discovery.
This task aims to extract informative insights from a dataset.
We cover two key subtasks:
(1) Data Profiling, which generates descriptive metadata and summaries using task-specific prompts \[ [463](https://arxiv.org/html/2505.18458v1#bib.bib463 ""), [58](https://arxiv.org/html/2505.18458v1#bib.bib58 "")\], and enhanced with context via RAG techniques \[ [72](https://arxiv.org/html/2505.18458v1#bib.bib72 "")\];
(2) Data Annotation, which assigns semantic labels or types through various prompting strategies \[ [204](https://arxiv.org/html/2505.18458v1#bib.bib204 ""), [205](https://arxiv.org/html/2505.18458v1#bib.bib205 ""), [218](https://arxiv.org/html/2505.18458v1#bib.bib218 "")\], supported by classical retrieval-based \[ [415](https://arxiv.org/html/2505.18458v1#bib.bib415 "")\] and LLM-generated context \[ [164](https://arxiv.org/html/2505.18458v1#bib.bib164 "")\].

Report issue for preceding element

LLM for Data Analysis (§ [3.2](https://arxiv.org/html/2505.18458v1#S3.SS2 "3.2 LLM for Data Analysis ‣ 3 LLM for Data Management ‣ Data × LLM: From Principles to Practices")).LLMs significantly improve the analytical capabilities across structured, semi-structured, and unstructured data.

Report issue for preceding element

∙∙\\bullet∙Structured Data Analysis. For relational data analysis, natural language interfaces allow users to write high-level questions instead of SQL/Python code \[ [459](https://arxiv.org/html/2505.18458v1#bib.bib459 "")\]. Multi-step QA frameworks (e.g., TAPERA \[ [481](https://arxiv.org/html/2505.18458v1#bib.bib481 "")\] and ReAcTable \[ [471](https://arxiv.org/html/2505.18458v1#bib.bib471 "")\]) decompose complex queries, while some end-to-end solutions fine-tune LLMs specifically for tabular tasks (e.g., TableGPT \[ [241](https://arxiv.org/html/2505.18458v1#bib.bib241 "")\]), apply content retrieval (e.g., CABINET \[ [307](https://arxiv.org/html/2505.18458v1#bib.bib307 "")\]) or convert tables into images for analysis (e.g., Table-LLaVA \[ [483](https://arxiv.org/html/2505.18458v1#bib.bib483 "")\]). For graph data, LLMs facilitate semantic queries with GQL generation (e.g., R3superscript𝑅3R^{3}italic\_R start\_POSTSUPERSCRIPT 3 end\_POSTSUPERSCRIPT-NL2GQL \[ [499](https://arxiv.org/html/2505.18458v1#bib.bib499 "")\]) and knowledge-aware QA by retrieving or reasoning over relevant subgraphs \[ [432](https://arxiv.org/html/2505.18458v1#bib.bib432 "")\].

Report issue for preceding element

∙∙\\bullet∙Semi-Structured Data Analysis. Meanwhile, handling semi-structured data (e.g., JSON and spreadsheets) remains challenging. Recent benchmarks (e.g., TEMPTABQA \[ [166](https://arxiv.org/html/2505.18458v1#bib.bib166 "")\] and SPREADSHEETBENCH \[ [282](https://arxiv.org/html/2505.18458v1#bib.bib282 "")\]) reveal substantial performance gaps.

Report issue for preceding element

∙∙\\bullet∙Unstructured Data Analysis. Finally, unstructured data analysis leverages LLMs to address document and program analysis tasks. For document analysis, OCR-dependent approaches involve performing OCR on document images followed by the integration of textual, layout, and visual features for reasoning (e.g., UDOP \[ [381](https://arxiv.org/html/2505.18458v1#bib.bib381 "")\] and DocFormerV2 \[ [62](https://arxiv.org/html/2505.18458v1#bib.bib62 "")\]). OCR-free methods directly generate the answer with end-to-end multimodal LLMs (e.g., Pix2Struct \[ [226](https://arxiv.org/html/2505.18458v1#bib.bib226 "")\] and DUBLIN \[ [49](https://arxiv.org/html/2505.18458v1#bib.bib49 "")\]). For program analysis, LLMs could serve as vulnerability detection tools using program analysis based training (e.g., PDBER \[ [272](https://arxiv.org/html/2505.18458v1#bib.bib272 "")\]) or case-driven prompt engineering (e.g., VUL-GPT \[ [271](https://arxiv.org/html/2505.18458v1#bib.bib271 "")\]). For program related analysis, LLMs could summarize repositories (e.g., SCLA \[ [285](https://arxiv.org/html/2505.18458v1#bib.bib285 "")\]) or serve as a repository-level code completer (e.g., RepoFusion \[ [361](https://arxiv.org/html/2505.18458v1#bib.bib361 "")\]) using their powerful semantic reasoning abilities.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2505.18458v1/x1.png)Figure 2: Example Data Characteristics across LLM Stages \- (a) Pretraining data \[ [110](https://arxiv.org/html/2505.18458v1#bib.bib110 ""), [225](https://arxiv.org/html/2505.18458v1#bib.bib225 "")\], (b) Continual pre-training \[ [112](https://arxiv.org/html/2505.18458v1#bib.bib112 "")\], (c) SFT \[ [454](https://arxiv.org/html/2505.18458v1#bib.bib454 "")\], (d) Reinforcement learning \[ [437](https://arxiv.org/html/2505.18458v1#bib.bib437 ""), [163](https://arxiv.org/html/2505.18458v1#bib.bib163 ""), [254](https://arxiv.org/html/2505.18458v1#bib.bib254 "")\], (e) RAG \[ [422](https://arxiv.org/html/2505.18458v1#bib.bib422 "")\], (f) Agent \[ [402](https://arxiv.org/html/2505.18458v1#bib.bib402 ""), [355](https://arxiv.org/html/2505.18458v1#bib.bib355 "")\].Report issue for preceding element

LLM for Data System Optimization (§ [3.3](https://arxiv.org/html/2505.18458v1#S3.SS3 "3.3 LLM for Data System Optimization ‣ 3 LLM for Data Management ‣ Data × LLM: From Principles to Practices")).LLMs equipped with advanced reasoning and code generation capabilities have been increasingly adopted in core system optimization tasks.
These include: (1) configuration tuning (identifying optimal system settings); (2) query optimization (rewriting or refining input queries for performance gains); and (3) anomaly diagnosis (analyzing system issues to ensure performance reliability).

Report issue for preceding element

∙∙\\bullet∙Configuration Tuning.
This task leverages LLMs to determine effective configuration parameters for improved system performance through:
(1) Prompt engineering tailored to tuning tasks, using both manually crafted \[ [244](https://arxiv.org/html/2505.18458v1#bib.bib244 ""), [132](https://arxiv.org/html/2505.18458v1#bib.bib132 ""), [157](https://arxiv.org/html/2505.18458v1#bib.bib157 "")\] and automatically generated prompts \[ [497](https://arxiv.org/html/2505.18458v1#bib.bib497 ""), [479](https://arxiv.org/html/2505.18458v1#bib.bib479 "")\];
(2) Retrieval-augmented generation (RAG), which incorporates prior tuning experiences during offline knowledge base preparation \[ [224](https://arxiv.org/html/2505.18458v1#bib.bib224 "")\] and online knowledge retrieval \[ [97](https://arxiv.org/html/2505.18458v1#bib.bib97 "")\];
(3) Objective-aligned tuning, which is enhanced through targeted training techniques \[ [497](https://arxiv.org/html/2505.18458v1#bib.bib497 ""), [178](https://arxiv.org/html/2505.18458v1#bib.bib178 "")\].

Report issue for preceding element

∙∙\\bullet∙Query Optimization.
This task utilizes LLMs to rewrite queries or improve execution plans by:
(1) Designing optimization-oriented prompts that include explicit guidance \[ [368](https://arxiv.org/html/2505.18458v1#bib.bib368 ""), [497](https://arxiv.org/html/2505.18458v1#bib.bib497 ""), [446](https://arxiv.org/html/2505.18458v1#bib.bib446 "")\] and in-context examples \[ [249](https://arxiv.org/html/2505.18458v1#bib.bib249 "")\];
(2) Enriching optimization knowledge using RAG techniques, including LLM-generated and hybrid retrieval strategies \[ [374](https://arxiv.org/html/2505.18458v1#bib.bib374 "")\];
(3) Enhancing optimization performance through task-specific training \[ [53](https://arxiv.org/html/2505.18458v1#bib.bib53 ""), [197](https://arxiv.org/html/2505.18458v1#bib.bib197 ""), [446](https://arxiv.org/html/2505.18458v1#bib.bib446 "")\].

Report issue for preceding element

∙∙\\bullet∙Anomaly Diagnosis.
This task involves identifying the root causes of anomalies and suggesting effective solutions via:
(1) Direct LLM prompting based on detailed diagnosis context \[ [156](https://arxiv.org/html/2505.18458v1#bib.bib156 "")\];
(2) RAG-based enrichment using relevant historical diagnosis experience \[ [496](https://arxiv.org/html/2505.18458v1#bib.bib496 ""), [433](https://arxiv.org/html/2505.18458v1#bib.bib433 "")\];
(3) Multi-agent collaboration mechanisms for comprehensive diagnosis \[ [496](https://arxiv.org/html/2505.18458v1#bib.bib496 ""), [363](https://arxiv.org/html/2505.18458v1#bib.bib363 "")\].

Report issue for preceding element

### 1.3 Comparison with Existing Surveys

Report issue for preceding element

Different from existing LLM and data management surveys \[ [412](https://arxiv.org/html/2505.18458v1#bib.bib412 ""), [55](https://arxiv.org/html/2505.18458v1#bib.bib55 ""), [86](https://arxiv.org/html/2505.18458v1#bib.bib86 ""), [404](https://arxiv.org/html/2505.18458v1#bib.bib404 ""), [273](https://arxiv.org/html/2505.18458v1#bib.bib273 ""), [275](https://arxiv.org/html/2505.18458v1#bib.bib275 ""), [379](https://arxiv.org/html/2505.18458v1#bib.bib379 ""), [494](https://arxiv.org/html/2505.18458v1#bib.bib494 "")\], our survey offers a comprehensive and detailed overview of the key intersections between LLMs and data management, highlighting how they can mutually benefit from each other. We uniquely position our work at the intersection of data for LLMs (e.g., how to acquire, process, store, and serve data for training and using LLMs) and LLMs for data (e.g., how LLMs can be leveraged to enhance data management tasks).

Report issue for preceding element

∙∙\\bullet∙We investigate the unique characteristics of data across different LLM development stages (Figure [2](https://arxiv.org/html/2505.18458v1#S1.F2 "Figure 2 ‣ 1.2 Techniques of LLM4DATA ‣ 1 INTRODUCTION ‣ Data × LLM: From Principles to Practices")), and provide a systematic overview of the associated challenges and techniques in data processing, storage, and serving (Table [I](https://arxiv.org/html/2505.18458v1#S2.T1 "TABLE I ‣ 2.1 Data Characteristics across LLM Stages ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")). Instead, prior surveys \[ [412](https://arxiv.org/html/2505.18458v1#bib.bib412 ""), [55](https://arxiv.org/html/2505.18458v1#bib.bib55 ""), [86](https://arxiv.org/html/2505.18458v1#bib.bib86 "")\] primarily center on the pre-training stage without covering the full LLM lifecycle like supervised fine-tuning (SFT), retrieval-augmented generation (RAG), and agent-based applications.

Report issue for preceding element

∙∙\\bullet∙We provide a lifecycle-based taxonomy of DATA4LLM, introducing key tasks in data processing, storage, and serving. For each task, we summarize representative methodologies, discuss their design principles, and analyze their strengths and limitations. In comparison, \[ [412](https://arxiv.org/html/2505.18458v1#bib.bib412 "")\] focuses on deduplication and filtering, \[ [55](https://arxiv.org/html/2505.18458v1#bib.bib55 "")\] emphasizes data selection, and \[ [378](https://arxiv.org/html/2505.18458v1#bib.bib378 "")\] reviews data annotation strategies, none of which offer a systematic perspective across the data management pipeline.

Report issue for preceding element

∙∙\\bullet∙ We introduce recent advances in LLM4DATA, outlining key components of LLM-driven data optimization. While earlier work \[ [494](https://arxiv.org/html/2505.18458v1#bib.bib494 "")\] has investigated the application of classical machine learning in data management, it largely neglects the distinctive strengths and limitations of LLMs, particularly in manipulating data for non-LLM tasks, processing semi-structured and unstructured data, and enabling system-level optimizations.

Report issue for preceding element

∙∙\\bullet∙We highlight open challenges and future directions from both ends: (1) improving data management techniques to meet practical LLM training and deployment needs (e.g., efficient data evaluation, scalable multi-modal storage), and (2) enhancing LLMs’ ability (e.g., private knowledge understanding, informative representation for non-sequential and non-textual data) to perform complex data management tasks across diverse real-world scenarios.

Report issue for preceding element

## 2 Data Management for LLM (DATA4LLM)

Report issue for preceding element

### 2.1 Data Characteristics across LLM Stages

Report issue for preceding elementTABLE I: Technique Comparison \- Data Processing, Storage, and Serving Techniques for Different LLM Stages. “N/A” indicates that no relevant work has been reported yet, although the corresponding techniques could potentially be applied.

|     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Stage | Pre-training /Incremental Pre-training | SupervisedFine-Tuning | ReinforcementLearning | Inference | RAG | Evaluation |
|  | Acquisition | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ | N/A | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ |
|  | De-duplication | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ | N/A | N/A | N/A | N/A |
|  | Filtering | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ | N/A | N/A | × | N/A |
|  | Selection | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ | N/A | N/A | N/A | N/A |
|  | Mixing | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ | × | N/A | × | × |
| DataProcessing | Synthesis | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ | N/A | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ |
|  | Distribution | Distributed File SystemModel Offload (GPUs, CPUs) | Model Offload(GPUs, CPUs) | Model Offload(GPUs, CPUs) | Model Offload(GPUs, CPUs) | Model Offload(GPUs, CPUs) | Model Offload(GPUs, CPUs) |
|  | Transmission | Caching Data PlacementParallelized PipelineData/Operator Offloading (CPUs) | Parallelized PipelineData/Operator Offloading (CPUs) | Parallelized PipelineData/Operator Offloading (CPUs) | × | N/A | N/A |
|  | Fault Tolerance | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ | × | × | × |
| DataStorage | KV Cache | N/A | N/A | N/A | Cache Space ManagemenKV IndexingKV PlacementKV Shrinking | KV PlacementKV Shrinking | N/A |
|  | Selection | Sample-Scoring-BasedModel-State-Based | Model-State-BasedExperience-Based | N/A | × | SLM-Based FilteringLLM-Based FilteringMetric-Based Re-rankingLLM-Based Re-ranking | × |
|  | Compression | N/A | N/A | N/A | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ | N/A |
|  | Packing | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ | ✓✓\\checkmark✓ | × | × | × |
| DataServing | Provenance | × | × | × | ✓✓\\checkmark✓ | N/A | × |

Report issue for preceding element![Refer to caption](https://arxiv.org/html/2505.18458v1/x2.png)Figure 3: Example LLM Data Distribution \- (a) General Domain (SFT)\[ [111](https://arxiv.org/html/2505.18458v1#bib.bib111 "")\], (b) General Domain (Eval) \[ [245](https://arxiv.org/html/2505.18458v1#bib.bib245 "")\], (c) Law (SFT)\[ [454](https://arxiv.org/html/2505.18458v1#bib.bib454 "")\], (d) Law (Eval)\[ [116](https://arxiv.org/html/2505.18458v1#bib.bib116 "")\], (e) Code (SFT) \[ [295](https://arxiv.org/html/2505.18458v1#bib.bib295 "")\], (f) Code (Eval)\[ [209](https://arxiv.org/html/2505.18458v1#bib.bib209 "")\].Report issue for preceding element

Before discussing specific data management techniques for LLMs, we first provide an overview of the data characteristics across different stages of LLM development. These characteristics include (1) the data scale, (2) the drawn data domain diversity, and (3) the data formats (e.g., question-answer pairs with or without explicit labels).
Given the differences in these characteristics across stages, distinct techniques for data processing, storage, and serving are required (Table [I](https://arxiv.org/html/2505.18458v1#S2.T1 "TABLE I ‣ 2.1 Data Characteristics across LLM Stages ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")).

Report issue for preceding element

Data for Pretraining. In the pre-training stage, LLMs rely on TB-scale, diverse datasets to acquire broad language and even cross-modality understanding capabilities, while reducing the risk of overfitting. These datasets are typically sourced from a wide range of domains and formats, including web crawls (e.g., HTML pages and WARC files) \[ [11](https://arxiv.org/html/2505.18458v1#bib.bib11 "")\], open-source code repositories (e.g., raw source code files with metadata) \[ [14](https://arxiv.org/html/2505.18458v1#bib.bib14 "")\], books (e.g., plain text or EPUB formats) \[ [503](https://arxiv.org/html/2505.18458v1#bib.bib503 "")\], academic papers (e.g., LaTeX source or PDF-converted text)  \[ [2](https://arxiv.org/html/2505.18458v1#bib.bib2 "")\], and interleaved image-text corpora (e.g., aligned captioned images in JSON or WebDataset format) \[ [225](https://arxiv.org/html/2505.18458v1#bib.bib225 "")\].

Report issue for preceding element

Data for Continual Pre-training. Continual pre-training (or continued pre-training) typically involves datasets containing millions to billions of tokens, which are often over 100 times smaller than those used in the initial pre-training stage. The primary objective is to fill knowledge gaps and adapt the model to specific domains. Representative domain-specific datasets are like: (1) Finance: BBT-FinCorpus \[ [274](https://arxiv.org/html/2505.18458v1#bib.bib274 "")\], a large-scale and diverse financial datasets comprising approximately 300 GB of text; and (2) Healthcare: Medical-pt \[ [437](https://arxiv.org/html/2505.18458v1#bib.bib437 "")\], a Chinese-English medical dataset containing 360,000 entries curated from medical encyclopedias.

Report issue for preceding element

Data for Supervised Fine-Tuning (SFT). Unlike pre-training, SFT relies on data presented in the form of instruction-response pairs, where the response includes not only the correct answer but also guidelines on tone, style, and reasoning steps to ensure user-friendly output.

Report issue for preceding element

The SFT stage typically involves much smaller datasets compared to pre-training. These datasets often consist of thousands to millions of labeled examples, with each example carefully crafted to guide the model in learning a specific, narrower set of tasks. For instance, in Figure [2](https://arxiv.org/html/2505.18458v1#S1.F2 "Figure 2 ‣ 1.2 Techniques of LLM4DATA ‣ 1 INTRODUCTION ‣ Data × LLM: From Principles to Practices"), (1) the summarization task constructs prompts using problem descriptions and summarization objects; (2) closed QA using questions and corresponding knowledge texts; (3) open QA tasks using only questions without knowledge text; and (4) captioning tasks using task descriptions and images. These prompts are paired with unique responses for model finetuning.

Report issue for preceding element

The composition of SFT datasets varies based on the application scenarios:

Report issue for preceding element

(1) General Instruction Following: For LLMs as general-purpose chatbots, SFT data include instructions for various daily tasks. Databricks-dolly-15K \[ [111](https://arxiv.org/html/2505.18458v1#bib.bib111 "")\] is a corpus containing over 15,000 records. It encompasses seven types of tasks, including creative writing, closed QA, open QA, summarization, information extraction, classification, brainstorming. This dataset is designed to enhance LLM to better adapt to specialized outputs that align with human-style requirements across diverse tasks. For example, in text summarization, it provides concise summary statements; whereas in text organization tasks, it structures outputs in table-of-contents format.

Report issue for preceding element

(2) Specific Domain Usage: For models specialized in fields such as law, finance, or medicine, the SFT data focuses on tasks pertinent to these fields. For example, DISC-Law-SFT \[ [454](https://arxiv.org/html/2505.18458v1#bib.bib454 "")\] is a legal SFT dataset containing 295k data entries from various legal scenarios, such as legal information extraction (32k), legal judgment prediction (16k), legal event detection (27k), and legal question-answering (93k). Similarly, Medical-SFT \[ [437](https://arxiv.org/html/2505.18458v1#bib.bib437 "")\] is a medical SFT dataset (totaling 2,060k pieces), composed of medical inquikry data (790k), online medical encyclopedia QA data (360k), English medical inquiry data (110k), medical knowledge graph QA data (79k). For tasks such as legal question-answering and legal judgment prediction, the data is structured as triplets, comprising the prompt, response, and supporting reference information (e.g., legal provisions, case-based evidence, or regulatory documents). For the remaining tasks, they all take the form of instruction pairs composed of prompt and response.

Report issue for preceding element

Data for Reinforcement Learning (RL). RL is generally divided into two types: one is RLHF (Reinforcement Learning with Human Feedback), and the other is Reasoning-oriented Reinforcement Learning (RoRL).

Report issue for preceding element

(1) RLHF: RLHF data is typically smaller than SFT data (e.g., thousands to dozens of millions of data samples), which involve more complex data annotations. Specifically, annotators compare multiple candidate responses to the same instruction and rank them according to human preference (e.g., levels from most helpful to least helpful). Collecting these preference pairs or rankings is more time-consuming than constructing instruction-response pairs in SFT.

Report issue for preceding element

In the general domain, UltraFeedback \[ [114](https://arxiv.org/html/2505.18458v1#bib.bib114 "")\] consists of 64,000 samples. For each sample, different models are used to generate 4 responses for each prompt (totaling 256,000 responses). GPT-4 is then employed to generate feedback for these four responses, which is used to help LLMs to generate outputs that are in line with human standards and appropriateness.

Report issue for preceding element

In specific domains such as healthcare, Medical-RLHF \[ [437](https://arxiv.org/html/2505.18458v1#bib.bib437 "")\] has 4,000 random questions from a Chinese medical dialogue dataset. Each question is paired with a well-organized answer (i.e., the human doctor’s reply) and a weaker answer from Llama-based model fine-tuned over synthesized QA samples. These labeled data are used to train a reward model. During the training of the LLM, the reward model provides feedback based on the LLM’s answers, guiding the training process towards generating high-quality responses.

Report issue for preceding element

(2) RoRL: Compared to the complex annotated data in RLHF, RoRL allows the model to discover the best reasoning approach on its own through the correctness of the reward model. Specifically, it focuses on tasks requiring long-term reasoning, such as mathematical, coding, and logical designing experiments \[ [163](https://arxiv.org/html/2505.18458v1#bib.bib163 "")\]. Under the premise of providing feedback on whether the answer is correct or not, algorithm such as the Group Relative Policy Optimization (GRPO) \[ [163](https://arxiv.org/html/2505.18458v1#bib.bib163 "")\] and long-CoT RL \[ [382](https://arxiv.org/html/2505.18458v1#bib.bib382 "")\] are adopted to train the model to independently discover the optimal problem-solving steps and converge.

Report issue for preceding element

Data for Retrieval-Augmented Generation (RAG). The RAG stage differs from above training stages, which involves large-scale dataset (reference corpus) for LLMs to retrieve from during inference. In this stage, data must be strictly reviewed to ensure authenticity and validity, while dynamic data requires real-time updates. The domain of RAG datasets varies depending on the specific application scenarios. For instance, (1) in the medicine-specific LLM application (Medical-Graph-RAG), MIMIC-IV is used as the RAG dataset \[ [422](https://arxiv.org/html/2505.18458v1#bib.bib422 "")\]. This dataset contains data from over 65,000 ICU patients and more than 200,000 patients treated in emergency departments; (2) in the legal field, the RAG knowledge base used by DISC-LawLLM \[ [454](https://arxiv.org/html/2505.18458v1#bib.bib454 "")\] contains more than 800 national and local laws, regulations, and rules, as well as 24,000 legal-related exam questions. Besides, RAG data can include users’ historical conversation records or personal information, in order to build a user-personalized LLM\[ [354](https://arxiv.org/html/2505.18458v1#bib.bib354 ""), [458](https://arxiv.org/html/2505.18458v1#bib.bib458 ""), [460](https://arxiv.org/html/2505.18458v1#bib.bib460 "")\].

Report issue for preceding element

Data for LLM Evaluation. Suitable evaluation datasets are essential for evaluating the performance of LLMs. They provide representative data samples that reflect different aspects of an LLM’s capabilities.

Report issue for preceding element

In the general domain, the MMMU benchmark is used to assess the performance of LLMs across major multi-modal tasks in six key disciplines, covering 30 subjects and 183 subfields. It is built from 11,500 carefully curated questions and effectively tests models’ perception, knowledge, and reasoning abilities \[ [455](https://arxiv.org/html/2505.18458v1#bib.bib455 "")\].

Report issue for preceding element

In specific domains, typical evaluation datasets include those in coding, healthcare and law domains: (1) OpenAI’s HumanEval dataset includes 164 programming problems, complete with function signatures, docstrings, bodies, and multiple unit tests. These problems are handcrafted to ensure they are not part of the training sets used for code generation models \[ [95](https://arxiv.org/html/2505.18458v1#bib.bib95 "")\]; (2) MedQA \[ [199](https://arxiv.org/html/2505.18458v1#bib.bib199 "")\] contains a large number of medical exam questions from various regions, totaling 61,097 questions; (3) LexEval \[ [233](https://arxiv.org/html/2505.18458v1#bib.bib233 "")\] constructs 23 evaluation tasks based on a legal cognitive classification framework, covering different aspects of legal knowledge, with at least 100 evaluation samples for each task.

Report issue for preceding element

Data for LLM Agents. Beyond vanilla LLMs, agents strive for more advanced capabilities such as planning and tool orchestration \[ [263](https://arxiv.org/html/2505.18458v1#bib.bib263 "")\]. These capabilities impose higher requirements on the training data for LLMs. First, many studies \[ [402](https://arxiv.org/html/2505.18458v1#bib.bib402 "")\] aim to enhance planning abilities through interaction trajectory data, which refers to a sequence of records generated during the interaction between the agent and the environment, typically represented as (instruction ⁢i, action ⁢a1, observation ⁢o1,…, action ⁢an)instruction 𝑖 action subscript𝑎1 observation subscript𝑜1… action subscript𝑎𝑛(\\text{instruction }i,\\text{ action }a\_{1},\\text{ observation }o\_{1},\\ldots,%
\\text{ action }a\_{n})( instruction italic\_i , action italic\_a start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , observation italic\_o start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , … , action italic\_a start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT ). Second, other studies focus on enhancing the agent’s tool usage capabilities using tool usage data. For instance, AutoTools \[ [355](https://arxiv.org/html/2505.18458v1#bib.bib355 "")\] fine-tunes models on tool data that is labeled with special tags, such as <python>⁢c⁢o⁢d⁢e⁢</python><python>𝑐𝑜𝑑𝑒</python>\\texttt{<python>}code\\texttt{</python>}<python> italic\_c italic\_o italic\_d italic\_e </python>, thereby grounding language in concrete tool invocations.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2505.18458v1/x3.png)Figure 4: Overview of DATA4LLM Techniques.Report issue for preceding element

### 2.2 Data Processing for LLM

Report issue for preceding elementTABLE II: Data Acquisition for LLMs.

|     |     |     |     |
| --- | --- | --- | --- |
| Method | Objective | Solution | Tools |
| WebsiteCrawling | HTML TextualContent Extraction | Rule-based | Trafilatura \[ [73](https://arxiv.org/html/2505.18458v1#bib.bib73 "")\] |
| Rule-based | BET \[ [144](https://arxiv.org/html/2505.18458v1#bib.bib144 "")\] |
| ML-based | Dragnet \[ [314](https://arxiv.org/html/2505.18458v1#bib.bib314 "")\] |
| Automate BrowserInteractions | HTML parsing | Beautiful Soup \[ [6](https://arxiv.org/html/2505.18458v1#bib.bib6 "")\] |
| Control web driver | Selenium \[ [19](https://arxiv.org/html/2505.18458v1#bib.bib19 "")\] |
| Wrap high-level API | Playwright \[ [30](https://arxiv.org/html/2505.18458v1#bib.bib30 "")\] |
| DevTools protocol | Puppeteer \[ [31](https://arxiv.org/html/2505.18458v1#bib.bib31 "")\] |
| Layout-based | Content Extractionfrom Handwrittenor Non-text Data | Model pipeline | PaddleOCR |
| Model pipeline | MinerU \[ [398](https://arxiv.org/html/2505.18458v1#bib.bib398 "")\] |
| Multimodal LLM | GOT2.0 \[ [414](https://arxiv.org/html/2505.18458v1#bib.bib414 "")\] |
| Multimodal LLM | Fox \[ [258](https://arxiv.org/html/2505.18458v1#bib.bib258 "")\] |
| Entityrecognition& linking | New Sample Derivation | Bi-Transformer | ReFinED \[ [68](https://arxiv.org/html/2505.18458v1#bib.bib68 "")\] |
| Translation Consistency | Seq2seq Frameworkusing References | AACTRANS \[ [216](https://arxiv.org/html/2505.18458v1#bib.bib216 "")\] |
| Text-Image Integration | Multimodal LLM | UMIE \[ [372](https://arxiv.org/html/2505.18458v1#bib.bib372 "")\] |

Report issue for preceding element

#### 2.2.1 Data Acquisition

Report issue for preceding element

Unlike classic machine learning, which primarily relies on collecting labeled data within a specific domain for supervised training (e.g., data for sentiment analysis and sentence similarity estimation), data acquisition for LLMs typically (1) relies on large-scale web scraping to collect extensive data across diverse domains for unsupervised pretraining and (2) employs techniques such as layout analysis and entity linking to extract additional data from the collected content.

Report issue for preceding element

PrinciplesUnlike classic ML data acquisition, LLMs rely heavily on large-scale web scraping to ensure broad coverage and robust generalization. The main challenge is extracting high-quality textual content, often aided by layout-based and entity-linking methods. Managing time and resource efficiency at scale remains vital.Report issue for preceding element

Data Sources. The data is gathered from two primary sources:

Report issue for preceding element

(1) Public Data, often freely available under open licenses, include resources such as webpages \[ [11](https://arxiv.org/html/2505.18458v1#bib.bib11 "")\], books \[ [503](https://arxiv.org/html/2505.18458v1#bib.bib503 "")\], and publicly accessible code repositories \[ [215](https://arxiv.org/html/2505.18458v1#bib.bib215 "")\].

Report issue for preceding element

∙∙\\bullet∙Webpage sources provide extensive pre-processed website content, such as 1.56T english text from crawled websites in C4 \[ [333](https://arxiv.org/html/2505.18458v1#bib.bib333 "")\], 6.6B multilingual pages in mC4 \[ [439](https://arxiv.org/html/2505.18458v1#bib.bib439 "")\], 6.3 trillion tokens of multilingual pages in CulturaX \[ [298](https://arxiv.org/html/2505.18458v1#bib.bib298 "")\].

Report issue for preceding element

∙∙\\bullet∙Digitized books supply structured, high-quality text, such as over 75,000 eBooks in Project Gutenberg \[ [38](https://arxiv.org/html/2505.18458v1#bib.bib38 "")\], over two million free ebooks in Open Library \[ [28](https://arxiv.org/html/2505.18458v1#bib.bib28 "")\], and film-aigned book descriptions in BookCorpus \[ [503](https://arxiv.org/html/2505.18458v1#bib.bib503 "")\]).

Report issue for preceding element

∙∙\\bullet∙Code repositories (e.g., GitHub \[ [14](https://arxiv.org/html/2505.18458v1#bib.bib14 "")\], GitLab \[ [20](https://arxiv.org/html/2505.18458v1#bib.bib20 "")\], Bitbucket \[ [7](https://arxiv.org/html/2505.18458v1#bib.bib7 "")\]) offer abundant programming data that can facilitate code search and analysis tasks, such as CodeSearchNet \[ [182](https://arxiv.org/html/2505.18458v1#bib.bib182 "")\] with 2M (comment, code) pairs.

Report issue for preceding element

(2) Private Data involve proprietary or confidential information not publicly available, such as internal company documents, customer support logs, application event logs, subscriber-only content (e.g., premium news articles, licensed scientific databases). Collecting this data requires careful attention to ethical and legal constraints (e.g., GDPR, CCPA) and mandates removing sensitive details (e.g., employing anonymization or pseudonymization) and using secure pipelines (e.g., CI/CD systems) with encryption and role-based access controls. For instance, proprietary codebases and user-generated content (chat logs, Q&A sessions) must be gathered under secure processes to maintain confidentiality.

Report issue for preceding element

Data Acquisition Methods. As shown in Table [II](https://arxiv.org/html/2505.18458v1#S2.T2 "TABLE II ‣ 2.2 Data Processing for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices"), there are three main techniques for data acquisition, including website crawling, layout analysis, and entity recognition and linking.

Report issue for preceding element

(1) Website Crawling. Most data are obtained through website crawling, which aims to extract textual content from crawled HTML files or multimodal image-text pairs using various extraction tools and browser automation assistants.

Report issue for preceding element

Generally, we first parse the raw HTML to separate meaningful textual content from boilerplate elements. Second, since typical extraneous components (e.g., headers, footers, advertisements, sidebars) often contribute little to the data value (e.g., for LLM training), we execute scripts (using CSS selectors or XPath queries) to identify and extract critical elements like article text, headlines, dates, and author bylines. Third, once the relevant text has been scraped, we store it in structured format such as JSON, CSV, database (see data storage in Section [2.3](https://arxiv.org/html/2505.18458v1#S2.SS3 "2.3 Data Storage for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")) for further processing. Specifically, for image elements encountered in HTML files, the image source URL is recorded, and the content of the alt attribute within the <img> tag is extracted and utilized as the corresponding image’s textual caption.

Report issue for preceding element

∙∙\\bullet∙_Rule-based Crawling._ Most existing tools use heuristic rule-based matching algorithm. Trafilatura \[ [73](https://arxiv.org/html/2505.18458v1#bib.bib73 "")\] is a heuristic algorithm based on hand-crafted rules (e.g., match HTML DOM nodes with the class equal to “navbar” to filter the navigation bar). BET \[ [144](https://arxiv.org/html/2505.18458v1#bib.bib144 "")\] employs the cumulative HTML tag distribution to find the largest region of fewest tags per text and extracts the corresponding text as the main content.

Report issue for preceding element

∙∙\\bullet∙_ML-based Crawling._ Since many website regions cannot be easily classified by rules, some works \[ [76](https://arxiv.org/html/2505.18458v1#bib.bib76 ""), [73](https://arxiv.org/html/2505.18458v1#bib.bib73 "")\] design a HTML tag classifier to judge whether a DOM node contains textual content, where they adopt L2superscript𝐿2L^{2}italic\_L start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT regularized logistic regression that inputs text density features and word frequencies in ”id“ and ”class“ attributes and outputs the probability that a given node contains textual useful content.

Report issue for preceding element

∙∙\\bullet∙_Auxiliary Tools._ Moreover, some auxiliary tools integrate user-friendly APIs for operating and interacting with HTML DOM trees. Beautiful Soup \[ [6](https://arxiv.org/html/2505.18458v1#bib.bib6 "")\] is widely used to parse the raw HTML in Python. Selenium \[ [19](https://arxiv.org/html/2505.18458v1#bib.bib19 "")\] automates browser actions and handles dynamic pages by controlling a web driver that communicates with the browser. Playwright \[ [30](https://arxiv.org/html/2505.18458v1#bib.bib30 "")\] provides a high-level API to automate browser tasks while Puppeteer \[ [31](https://arxiv.org/html/2505.18458v1#bib.bib31 "")\] communicates directly with the browser using the DevTools Protocol, allowing for headless browser interactions (e.g., in JavaScript-heavy websites).

Report issue for preceding element

(2) Layout Analysis. Layout analysis focuses on extracting textual content from handwritten or non-textual data (e.g., from the crawled ones), which can contain valuable information and require advanced layout analysis techniques for effective extraction. Existing methods include pipeline-based and end-to-end approaches.

Report issue for preceding element

∙∙\\bullet∙_Layout Analysis Pipelines._ Intuitively, many works adopt OCR technology (e.g., Tesseract \[ [203](https://arxiv.org/html/2505.18458v1#bib.bib203 "")\]) to convert raw data (e.g., scanned books) into machine-readable formats \[ [18](https://arxiv.org/html/2505.18458v1#bib.bib18 ""), [398](https://arxiv.org/html/2505.18458v1#bib.bib398 "")\] in a pipeline manner, which consist of multiple small models. PaddleOCR \[ [18](https://arxiv.org/html/2505.18458v1#bib.bib18 "")\] passes an image through a Layout Analysis model, which divides the image into different regions such as text, tables, and formulas for separate processing. The table area is sent to the Form Recognition module for structured recognition, and the text areas and formulas are input to the OCR engine for text recognition. Finally, the Layout Restoration module reconstructs all the regions in textual format using heuristic rules based on the relative location information of different extracted regions.

Report issue for preceding element

Similarly, MinerU \[ [398](https://arxiv.org/html/2505.18458v1#bib.bib398 "")\] works in a pipeline manner. It fine-tunes LayoutLMv3 \[ [181](https://arxiv.org/html/2505.18458v1#bib.bib181 "")\] for layout detection and YOLOv8 \[ [397](https://arxiv.org/html/2505.18458v1#bib.bib397 "")\] for formula detection to improve the system’s generalization (handling a wider range of document types). The detected data are kept in markdown or JSON format.

Report issue for preceding element

∙∙\\bullet∙_End-to-End Models._ End-to-End layout analysis refers to adopt multi-modal LLMs to conduct end-to-end text acquisition. For instance, GOT2.0 \[ [414](https://arxiv.org/html/2505.18458v1#bib.bib414 "")\] is a acquisition model composed of (i)𝑖(i)( italic\_i ) a high-compression encoder that transforms the image to tokens, (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) a long-context decoder that outputs the corresponding OCR results, and (i⁢i⁢i)𝑖𝑖𝑖(iii)( italic\_i italic\_i italic\_i ) a linear layer acting as the connector to map the channel dimension between the vision encoder and the language decoder. Another example is Fox \[ [258](https://arxiv.org/html/2505.18458v1#bib.bib258 "")\], which employs the natural content-aware CLIP-ViT \[ [327](https://arxiv.org/html/2505.18458v1#bib.bib327 "")\] and the artificial content-aware Vary \[ [413](https://arxiv.org/html/2505.18458v1#bib.bib413 "")\] as two vision encoders, enabling the model to perform fine-grained interactions and multi-page document understanding.
The end-to-end architecture reduces maintenance costs and enhances versatility, enabling the recognition of more complex elements (e.g., charts, sheet music) and supporting improved readability formats for formulas and tables (e.g., LaTeX, Markdown). However, due to the use of LLMs with larger parameter size (e.g, <20M for PaddleOCR vs. 580M for GOT2.0 and 1.8B for Fox), the inference efficiency of these methods still needs improvement.

Report issue for preceding element

(3) Entity Recognition &\\&& Linking. Additionally, we can derive more valuable LLM samples by identifying and linking entities from the above extracted data.
WEBIE \[ [419](https://arxiv.org/html/2505.18458v1#bib.bib419 "")\] introduces a large-scale, entity-linked information extraction dataset with 1.6M sentences from Common Crawl. It links entities using ReFinED \[ [68](https://arxiv.org/html/2505.18458v1#bib.bib68 "")\], and applies distant supervision (DS) to extract 4.8M triples, where each triple consists of a subject, a relationship, and an object.

Report issue for preceding element

Furthermore, to ensure the consistency of derived and origin samples (e.g., translation across English and other languages), Alignment-Augmented Consistent Translation (AACTRANS) model \[ [216](https://arxiv.org/html/2505.18458v1#bib.bib216 "")\] uses a Seq2Seq framework that incorporates reference text in the target language to guide translations, ensuring consistency across related pieces of text. During training, aligned text pairs are augmented with reference-based word alignments to bias the model toward consistent translations. At inference, a common reference translation of the original sentence is used to align and translate related extractions using the AACTRANS model.

Report issue for preceding element

However, AACTRANS fails to leverage shared knowledge across tasks, limiting the alignment performance. Instead, UMIE \[ [372](https://arxiv.org/html/2505.18458v1#bib.bib372 "")\] integrates text and visual inputs and produces structured outputs to learn linking knowledge from multiple tasks. The UMIE model is composed of four modules: (1) a text encoder for task instruction comprehension, (2) a visual encoder for image understanding, (3) a gated attention mechanism for cross-modal integration, and (4) a text decoder for structured output generation. Following different task instructors, UMIE is capable of performing various MIE tasks and generating corresponding structured outputs, thereby facilitating knowledge sharing.

Report issue for preceding element

Notably, recent LLMs could automatically learn the relationships among samples from randomly provided data, rendering the explicit entity linking an optional procedure in the data acquisition process \[ [119](https://arxiv.org/html/2505.18458v1#bib.bib119 "")\].

Report issue for preceding element

#### 2.2.2 Data Deduplication

Report issue for preceding elementTABLE III: Data Deduplication for LLMs.

|     |     |     |     |
| --- | --- | --- | --- |
| Method | Objective | Modality | Work |
| |     |
| --- |
| Exact |
| substring |
| matching | | |     |
| --- |
| Deduplicate |
| samples with |
| identical substrings | | Text | |     |
| --- |
| MD5 \[ [122](https://arxiv.org/html/2505.18458v1#bib.bib122 "")\] |
| Suffix Array \[ [300](https://arxiv.org/html/2505.18458v1#bib.bib300 "")\] | |
| |     |
| --- |
| Hashing |
| identification | | |     |
| --- |
| Deduplicate |
| samples with |
| similar substrings | | Text | |     |
| --- |
| SimHash \[ [88](https://arxiv.org/html/2505.18458v1#bib.bib88 "")\] |
| MinHash \[ [81](https://arxiv.org/html/2505.18458v1#bib.bib81 ""), [122](https://arxiv.org/html/2505.18458v1#bib.bib122 ""), [300](https://arxiv.org/html/2505.18458v1#bib.bib300 "")\] |
| MinHashLSH \[ [351](https://arxiv.org/html/2505.18458v1#bib.bib351 ""), [362](https://arxiv.org/html/2505.18458v1#bib.bib362 "")\] |
| MinHash + |
| Bloom Filter \[ [208](https://arxiv.org/html/2505.18458v1#bib.bib208 "")\] |
| DotHash \[ [299](https://arxiv.org/html/2505.18458v1#bib.bib299 "")\] | |
| |     |
| --- |
| Frequency |
| analysis | | |     |
| --- |
| Down-weighing |
| samples with |
| higher commonness | | Text | SoftDeDup \[ [168](https://arxiv.org/html/2505.18458v1#bib.bib168 "")\] |
| |     |
| --- |
| Embedding- |
| based |
| clustering | | |     |
| --- |
| Deduplicate |
| samples with |
| identical topics but |
| different formats | | |     |
| --- |
| Text + |
| Image | | |     |
| --- |
| SemDeDup \[ [46](https://arxiv.org/html/2505.18458v1#bib.bib46 "")\] |
| SemDeDup + |
| SSL Prototypes\[ [390](https://arxiv.org/html/2505.18458v1#bib.bib390 "")\] |
| FairDeDup \[ [364](https://arxiv.org/html/2505.18458v1#bib.bib364 "")\] | |

Report issue for preceding element

The collected raw data often contains significant redundancy, which can negatively impact LLM performance either by reducing its generalization ability to new or rarely-seen tasks \[ [300](https://arxiv.org/html/2505.18458v1#bib.bib300 "")\] or by memorizing and overfitting to the repeated subsets \[ [170](https://arxiv.org/html/2505.18458v1#bib.bib170 ""), [430](https://arxiv.org/html/2505.18458v1#bib.bib430 "")\]. Various deduplication methods have been proposed to detect and mitigate duplication, either by (1) completely removing duplicate samples \[ [122](https://arxiv.org/html/2505.18458v1#bib.bib122 ""), [300](https://arxiv.org/html/2505.18458v1#bib.bib300 ""), [351](https://arxiv.org/html/2505.18458v1#bib.bib351 ""), [362](https://arxiv.org/html/2505.18458v1#bib.bib362 ""), [208](https://arxiv.org/html/2505.18458v1#bib.bib208 ""), [46](https://arxiv.org/html/2505.18458v1#bib.bib46 ""), [390](https://arxiv.org/html/2505.18458v1#bib.bib390 ""), [364](https://arxiv.org/html/2505.18458v1#bib.bib364 "")\] or by (2) down-weighing duplicate samples for data resampling \[ [168](https://arxiv.org/html/2505.18458v1#bib.bib168 "")\]. We classify these methods into four main categories.

Report issue for preceding element

PrinciplesCompared to structured classic ML data, LLM data is unstructured and requires careful identification and removal of duplicate or near-duplicate content from training datasets to improve efficiency, prevent overfitting, and mitigate bias using statistical metrics like perplexity or model evaluation. Challenges include (1) how to encode semantic texts into representations that could be precisely and efficiently compared and (2) the scalability of the deduplication methods.Report issue for preceding element

Exact Substring Matching. Exact substring matching methods identify and remove exactly identical samples across datasets, which can happen if (1) a sample references another sample (e.g., a report related to another), or (2) two individual datasets accidentally include the same sample (e.g., a webpage of a popular website). It is commonly used as a preliminary step to remove duplications. Relevant methods leverage techniques like hashing \[ [122](https://arxiv.org/html/2505.18458v1#bib.bib122 "")\] and suffix array \[ [300](https://arxiv.org/html/2505.18458v1#bib.bib300 "")\] at the sample or sentence level.

Report issue for preceding element

∙∙\\bullet∙_Sample-Level._\[ [122](https://arxiv.org/html/2505.18458v1#bib.bib122 "")\] conducts sample-level deduplication by calculating the MD5 hashing value of each sample and deduplicate samples with identical MD5 values.

Report issue for preceding element

∙∙\\bullet∙_Sentence-Level._\[ [300](https://arxiv.org/html/2505.18458v1#bib.bib300 "")\] performs sentence-level deduplication by using Suffix Array, which combines all the samples into one sentence, computes the sentence Suffix Array, and deduplicates samples with common prefixes in the Suffix Array. Suffix Array \[ [284](https://arxiv.org/html/2505.18458v1#bib.bib284 "")\] is a data structure that stores the starting indices of string suffixes in lexicographical order. For instance, given the string “patata”, its suffixes in lexicographical order are _\[“a” (index 5), “ata” (index 3), “atata” (index 1), “patata” (index 0), “ta” (index 4), “tata” (index 2)\]_, so its suffix array is _(5, 3, 1, 0, 4, 2)_. As identically duplicate samples have the same prefix, they will become adjacent in the suffix array, making it easier to find the duplicates across the samples. In practice, they construct a suffix array on the sequence with a threshold of 50 tokens (empirically determined for significantly reducing the false positives), and find the duplicate samples with common prefixes in linear time.

Report issue for preceding element

Approximate Hashing-based Deduplication. Hashing-based methods hash each sample into a fixed-length vector and deduplicate samples with significant vector overlap. Compared with the exact matching-based approach, it can identify near-duplicate samples with only a few words of difference (e.g., advertisements generated using the same template). Unlike normal hashing algorithms like MD5, hashes generated in this approach do not change significantly with even a bit of modification, making it possible to detect near-duplicate samples. There are various hashing algorithms, including SimHash \[ [88](https://arxiv.org/html/2505.18458v1#bib.bib88 "")\], MinHash \[ [81](https://arxiv.org/html/2505.18458v1#bib.bib81 "")\], DotHash \[ [299](https://arxiv.org/html/2505.18458v1#bib.bib299 "")\], and their variants \[ [351](https://arxiv.org/html/2505.18458v1#bib.bib351 ""), [362](https://arxiv.org/html/2505.18458v1#bib.bib362 "")\].

Report issue for preceding element

∙∙\\bullet∙_MinHash \[ [81](https://arxiv.org/html/2505.18458v1#bib.bib81 "")\]_ hashes samples into vectors using a series of hashing functions, where only the minimum value is retained for each function, and estimates similarity for each pair of vectors through Jaccard Index J⁢a⁢c⁢c⁢a⁢r⁢d⁢(X,Y)=X∩YX∪Y𝐽𝑎𝑐𝑐𝑎𝑟𝑑𝑋𝑌𝑋𝑌𝑋𝑌Jaccard(X,Y)=\\frac{X\\cap Y}{X\\cup Y}italic\_J italic\_a italic\_c italic\_c italic\_a italic\_r italic\_d ( italic\_X , italic\_Y ) = divide start\_ARG italic\_X ∩ italic\_Y end\_ARG start\_ARG italic\_X ∪ italic\_Y end\_ARG, where X and Y represent sets of elements (For example, if X = a, b, c, d and Y = b, c, d, e, f, the Jaccard Index over X and Y would be 1212\\frac{1}{2}divide start\_ARG 1 end\_ARG start\_ARG 2 end\_ARG). \[ [360](https://arxiv.org/html/2505.18458v1#bib.bib360 "")\] demonstrates that MinHash generally outperforms SimHash. In practice, \[ [122](https://arxiv.org/html/2505.18458v1#bib.bib122 "")\] employed MinHash to the code data on both the sample and the repository levels for diversity and integrity, and \[ [300](https://arxiv.org/html/2505.18458v1#bib.bib300 "")\] employed MinHash on the sample level.

Report issue for preceding element

Moreover, MinHash has various variants for acceleration. MinHashLSH \[ [351](https://arxiv.org/html/2505.18458v1#bib.bib351 ""), [362](https://arxiv.org/html/2505.18458v1#bib.bib362 "")\] improves MinHash by involving locality-sensitive hashing (LSH), which divides a vector into multiple bands and only compares the samples with partially identical vector bands instead of the whole vector, mitigating the computational overhead in sample comparison. LSHBloom \[ [208](https://arxiv.org/html/2505.18458v1#bib.bib208 "")\] further improves MinHashLSH by using Bloom Filter, which hashes each band into a single integer value and inserting it into each corresponding Bloom Filter, and the sample will be flagged as a duplicate if any band’s hashed value collides with an entry in the Bloom filter, accelerating duplicate samples searching while reducing memory usage with negligible false positive rate (e.g., 1e-5 in experiments).

Report issue for preceding element

However, MinHash-based methods require building massive vector sets. When the number of samples and their lengths grow large, constructing vector sets becomes exceedingly expensive in terms of both time and space. Moreover, as the feature vector computation for each sample depends on this shared vocabulary, it is difficult to fully parallelize the process.

Report issue for preceding element

∙∙\\bullet∙_SimHash \[ [88](https://arxiv.org/html/2505.18458v1#bib.bib88 "")\]._ To address MinHash’s issues, SimHash \[ [88](https://arxiv.org/html/2505.18458v1#bib.bib88 "")\] generates a sample’s feature vector _solely from the words it contains_, converts each sample into a fixed-dimensional binary vector for similarity comparison. Specifically, it first hashes each token in the sample (e.g., by BPE tokenizer \[ [75](https://arxiv.org/html/2505.18458v1#bib.bib75 "")\]) into a fixed-dimension vector of {0,1}dsuperscript01𝑑\\{0,1\\}^{d}{ 0 , 1 } start\_POSTSUPERSCRIPT italic\_d end\_POSTSUPERSCRIPT (e.g., \[1,0,0,1\]1001\[1,0,0,1\]\[ 1 , 0 , 0 , 1 \] and \[1,1,0,0\]1100\[1,1,0,0\]\[ 1 , 1 , 0 , 0 \] ) weighted by the pre-defined weight w𝑤witalic\_w (e.g., w1subscript𝑤1w\_{1}italic\_w start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT and w2subscript𝑤2w\_{2}italic\_w start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT), where the weight is positive for 1111 and negative for 00 (e.g., \[w1,−w1,−w1,w1\]subscript𝑤1subscript𝑤1subscript𝑤1subscript𝑤1\[w\_{1},-w\_{1},-w\_{1},w\_{1}\]\[ italic\_w start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , - italic\_w start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , - italic\_w start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , italic\_w start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT \], \[w2,w2,−w2,−w2\]subscript𝑤2subscript𝑤2subscript𝑤2subscript𝑤2\[w\_{2},w\_{2},-w\_{2},-w\_{2}\]\[ italic\_w start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT , italic\_w start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT , - italic\_w start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT , - italic\_w start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT \]). Then it added up these weighted vectors to a new vector of the same dimension d𝑑ditalic\_d (e.g., \[w1+w2,−w1+w2,−w1−w2,w1−w2\]subscript𝑤1subscript𝑤2subscript𝑤1subscript𝑤2subscript𝑤1subscript𝑤2subscript𝑤1subscript𝑤2\[w\_{1}+w\_{2},-w\_{1}+w\_{2},-w\_{1}-w\_{2},w\_{1}-w\_{2}\]\[ italic\_w start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT + italic\_w start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT , - italic\_w start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT + italic\_w start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT , - italic\_w start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT - italic\_w start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT , italic\_w start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT - italic\_w start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT \]). Finally, the values of the new vector are mapped to another vector of {0,1}dsuperscript01𝑑\\{0,1\\}^{d}{ 0 , 1 } start\_POSTSUPERSCRIPT italic\_d end\_POSTSUPERSCRIPT, where the positive values are mapped to 1 and 0 otherwise. The final vector is the fingerprint of each sample, and the similarity of the two samples is estimated by calculating the Hamming distance between their vectors.

Report issue for preceding element

Compared with MinHash, SimHash stores and compares only one hash signature for each sample, greatly reducing the storage and computing overhead. However, keeping only one signature makes it harder to distinguish between two samples, especially those with low Hamming distances, requiring careful curation of data features.

Report issue for preceding element

∙∙\\bullet∙_DotHash \[ [299](https://arxiv.org/html/2505.18458v1#bib.bib299 "")\]._ Moreover, to further improve the deduplication accuracy and efficiency, DotHash \[ [299](https://arxiv.org/html/2505.18458v1#bib.bib299 "")\] assumes that uniformly sampled vectors in high-dimensional space are quasi-orthogonal. It encodes sample elements into fixed-length basis vectors, and treats the samples as combinations of these basis vectors, thus the dot product of these vectors is an unbiased estimate of their intersection. For example, given the set a=∑a∈Aψ⁢(a)𝑎subscript𝑎𝐴𝜓𝑎a=\\sum\_{a\\in A}\\psi(a)\\quaditalic\_a = ∑ start\_POSTSUBSCRIPT italic\_a ∈ italic\_A end\_POSTSUBSCRIPT italic\_ψ ( italic\_a ) and the set b=∑b∈Bψ⁢(b)𝑏subscript𝑏𝐵𝜓𝑏\\quad b=\\sum\_{b\\in B}\\psi(b)italic\_b = ∑ start\_POSTSUBSCRIPT italic\_b ∈ italic\_B end\_POSTSUBSCRIPT italic\_ψ ( italic\_b ), the intersection is calculated by 𝔼⁢\[a⋅b\]=\|A∩B\|𝔼delimited-\[\]⋅𝑎𝑏𝐴𝐵\\mathbb{E}\[a\\cdot b\]=\|A\\cap B\|blackboard\_E \[ italic\_a ⋅ italic\_b \] = \| italic\_A ∩ italic\_B \|.

Report issue for preceding element

However, \[ [121](https://arxiv.org/html/2505.18458v1#bib.bib121 "")\] found that DotHash would perform badly if the basis vector has a shorter length than the number of basis vectors, where quasi-orthogonal no longer holds.

Report issue for preceding element

Approximate Frequency-based Down-Weighting. To prevent the loss of potentially valuable information by retaining only one sample and removing the rest, SoftDeDup \[ [168](https://arxiv.org/html/2505.18458v1#bib.bib168 "")\] deduplicates by reweighting samples, where samples with higher commonness will be assigned higher sampling weights, and others with lower commonness will be assigned lower sampling weights. Specifically, SoftDeDup computes the frequency of each n-gram across all the samples, and then calculates the commonness of each sample by multiplying the frequencies of all the n-grams that appear in the document. The samples with higher commonness would be seen as more likely to be duplicate and thus be down-weighted.

Report issue for preceding element

Embedding-Based Clustering. Except for samples with the same or similar substrings, some samples with similar semantics but different formats (i.e, expressed differently) may also negatively affect LLM training performance. For instance, for the following two sentences: (i)𝑖(i)( italic\_i )“Unleash your potential with our lightweight, high-performance sports shoes – designed for comfort, speed, and style”; (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i )“Step into greatness with durable, breathable sports shoes perfect for running, training, and everyday adventures”. Both of the sentences are sports shoe advertisements but expressed differently, and such duplicates could degenerate model performance by making data imbalanced and introducing bias to the model. To address this issue, another approach leverages language models’ embeddings (representing similar items as vectors close to each other in the vector space) for deduplication.

Report issue for preceding element

SemDeDup \[ [46](https://arxiv.org/html/2505.18458v1#bib.bib46 "")\] identifies semantic duplicates by clustering embeddings and deduplicating those with high cosine similarities. It first encodes each data point into an embedding by leveraging the OPT \[ [469](https://arxiv.org/html/2505.18458v1#bib.bib469 "")\] text encoder and the CLIP \[ [326](https://arxiv.org/html/2505.18458v1#bib.bib326 ""), [183](https://arxiv.org/html/2505.18458v1#bib.bib183 "")\] image encoder, and clusters the embeddings with k-means, so one can save time by finding duplicates within the cluster rather than the whole vector space. Then, within each cluster, it searches for semantic duplicates with cosine similarity above the pre-defined threshold. Finally, within each group of duplicates, it retains the example with the lowest cosine similarity to the cluster centroid and removes the rest. As a multi-modal method, it can be applied to both text and image data, making it possible to deduplicate image data. In practice, \[ [45](https://arxiv.org/html/2505.18458v1#bib.bib45 "")\] leverages SemDeDup to deduplicate the image-text pair dataset LAION-400M \[ [344](https://arxiv.org/html/2505.18458v1#bib.bib344 "")\].

Report issue for preceding element

Like MinHash, SemDeDup also has many variants for performance improvement. \[ [390](https://arxiv.org/html/2505.18458v1#bib.bib390 "")\] combines SemDeDup with the Self-Supervised Learning (SSL) Prototypes metric, such as representing unlabeled data in terms of their cluster centroids in an embedding space, for data pruning to further remove semantic duplicates that cannot be removed by MinHash. FairDeDup \[ [364](https://arxiv.org/html/2505.18458v1#bib.bib364 "")\] modifies the logic of SemDeDup to improve the representation of underrepresented sensitive groups by prioritizing the retention of data samples that align with sensitive concepts defined through user-provided prototypes, such as demographic subgroups. Within each cluster, instead of selecting the farthest sample from the centroid, it selects the sample that maximizes similarity to the least-represented group in the cluster to prevent samples with sensitive concepts from being pruned.

Report issue for preceding element

Non-Text Data Deduplication. As LLMs are increasingly applied to multimodal tasks (e.g., image-text retrieval, visual question answering), non-text data types such as images are becoming integral to LLM training datasets, necessitating dedicated deduplication techniques. Like texts, images can be encoded into embeddings through neural networks designed for images, like CNN, after which embedding-based deduplication methods can be applied. SemDedup\[ [46](https://arxiv.org/html/2505.18458v1#bib.bib46 "")\] adopts a semantic-based method by computing cosine similarity between image embeddings; two images are considered duplicates if their similarity exceeds a predefined threshold, which is tuned to balance detection precision and recall. In contrast, MINT-1T employs a hash-based approach, using SHA256 checksums to identify and remove exact duplicates efficiently. Meanwhile, the DataComp pipeline \[ [146](https://arxiv.org/html/2505.18458v1#bib.bib146 "")\] leverages the CNN-based near-duplicate detector \[ [453](https://arxiv.org/html/2505.18458v1#bib.bib453 "")\] to eliminate subtle duplicates and prevent evaluation set leakage. Models trained on these deduplicated image sets exhibit improved performance over baselines such as CLIP \[ [326](https://arxiv.org/html/2505.18458v1#bib.bib326 "")\] for higher precision and recall.

Report issue for preceding element

TABLE IV: Data Filtering Methods for LLMs.

|     |     |     |     |
| --- | --- | --- | --- |
| Category | Objective | Methods |  |
| Sample-levelFiltering | Removelow-qualitysamples | Perplexity Measuring \[ [388](https://arxiv.org/html/2505.18458v1#bib.bib388 ""), [61](https://arxiv.org/html/2505.18458v1#bib.bib61 ""), [289](https://arxiv.org/html/2505.18458v1#bib.bib289 ""), [240](https://arxiv.org/html/2505.18458v1#bib.bib240 ""), [239](https://arxiv.org/html/2505.18458v1#bib.bib239 "")\] |  |
| Influence Assessment \[ [255](https://arxiv.org/html/2505.18458v1#bib.bib255 ""), [169](https://arxiv.org/html/2505.18458v1#bib.bib169 "")\] |  |
| Clustering \[ [45](https://arxiv.org/html/2505.18458v1#bib.bib45 ""), [444](https://arxiv.org/html/2505.18458v1#bib.bib444 "")\] |  |
| Model Scoring \[ [418](https://arxiv.org/html/2505.18458v1#bib.bib418 ""), [265](https://arxiv.org/html/2505.18458v1#bib.bib265 ""), [349](https://arxiv.org/html/2505.18458v1#bib.bib349 "")\] |  |
| Mixed Methods \[ [286](https://arxiv.org/html/2505.18458v1#bib.bib286 ""), [84](https://arxiv.org/html/2505.18458v1#bib.bib84 ""), [126](https://arxiv.org/html/2505.18458v1#bib.bib126 "")\] |  |
| |     |
| --- |
| Content- |
| level |
| Filtering | | |     |
| --- |
| Remove |
| partial-noising |
| samples | | |     |
| --- |
| Privacy Anonymization \[ [276](https://arxiv.org/html/2505.18458v1#bib.bib276 ""), [269](https://arxiv.org/html/2505.18458v1#bib.bib269 "")\] |
| Image & Video Filtering \[ [445](https://arxiv.org/html/2505.18458v1#bib.bib445 ""), [217](https://arxiv.org/html/2505.18458v1#bib.bib217 ""), [396](https://arxiv.org/html/2505.18458v1#bib.bib396 "")\] | |  |

Report issue for preceding element![Refer to caption](https://arxiv.org/html/2505.18458v1/x4.png)Figure 5: Example Data Filtering Workflows \[ [239](https://arxiv.org/html/2505.18458v1#bib.bib239 ""), [45](https://arxiv.org/html/2505.18458v1#bib.bib45 ""), [265](https://arxiv.org/html/2505.18458v1#bib.bib265 "")\].Report issue for preceding element

#### 2.2.3 Data Filtering

Report issue for preceding element

Data filtering removes low-quality or sensitive samples from the dataset to reduce computational overhead and protect privacy, while the model trained on the subset exhibits similar or even better performance than the one trained on the original dataset. To achieve this, one has to (i)𝑖(i)( italic\_i ) remove samples with low quality ( _Sample-level filtering_) or partial noisy information ( _Content-level filtering_), and (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) keep the selected samples diverse enough to cover various domains.

Report issue for preceding element

PrinciplesCompared to classic ML data filtering, LLM data filtering emphasizes turning unstructured text into measurable metrics, with the main challenge being the effectiveness of evaluation methods, the standards of low-quality samples, and the computational complexity of these methods across massive datasets.Report issue for preceding element

Sample-level Filtering refers to evaluating samples using metrics or models and removing the samples that fail to meet the threshold (e.g., quality and diversity).
There are multiple metrics in this category:

Report issue for preceding element

(1) Statistical Evaluation uses various statistical methods to evaluate samples by directly applying statistical metrics to the samples (e.g., clustering results) or indirectly capturing characteristics from the models trained on the dataset (e.g., loss or perplexity from a surrogate model). Applicable statistical metrics include perplexity (and its variants), influence on model parameters, and clustering.

Report issue for preceding element

∙∙\\bullet∙Perplexity Measuring. Perplexity measures the difficulty of a model generating the responses, represented as aggregated probabilities of the j𝑗jitalic\_j-th response token given the question tokens and previous j−1𝑗1j-1italic\_j - 1 response tokens PPL⁢(y\|x)=exp⁡(−1N⁢∑j=1Nlog⁡p⁢(yj\|x,y1,…,yj−1))PPLconditional𝑦𝑥1𝑁superscriptsubscript𝑗1𝑁𝑝conditionalsubscript𝑦𝑗𝑥subscript𝑦1…subscript𝑦𝑗1\\text{PPL}(y\|x)=\\exp\\left(-\\frac{1}{N}\\sum\_{j=1}^{N}\\log p(y\_{j}\|x,y\_{1},...,y%
\_{j-1})\\right)PPL ( italic\_y \| italic\_x ) = roman\_exp ( - divide start\_ARG 1 end\_ARG start\_ARG italic\_N end\_ARG ∑ start\_POSTSUBSCRIPT italic\_j = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_N end\_POSTSUPERSCRIPT roman\_log italic\_p ( italic\_y start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT \| italic\_x , italic\_y start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , … , italic\_y start\_POSTSUBSCRIPT italic\_j - 1 end\_POSTSUBSCRIPT ) ). The higher the perplexity value is, the harder the model generates the response. It is commonly used in selecting high-quality subsets in pre-training and fine-tuning phases. Based on the original perplexity, there have been several studies for improving the metric, including computing perplexities using a smaller-sized model for training a larger-sized model to reduce computational overhead, or employing advanced techniques such as Learning Percentage (LP) and Instruction-Following Difficulty (IFD) to identify and select challenging samples.

Report issue for preceding element

Specifically, \[ [388](https://arxiv.org/html/2505.18458v1#bib.bib388 "")\] uses an existing model to compute perplexity scores for multiple domains and selects pre-training samples from the domains with high correlation between the downstream benchmark error and the perplexity scores on the domain samples. The correlation is measured through a rank-based correlation coefficient γj=∑sign⁢(yk−yl)⁢(rankj⁢(xk,j)−rankj⁢(xl,j))subscript𝛾𝑗signsubscript𝑦𝑘subscript𝑦𝑙subscriptrank𝑗subscript𝑥𝑘𝑗subscriptrank𝑗subscript𝑥𝑙𝑗\\gamma\_{j}=\\sum\\text{sign}(y\_{k}-y\_{l})(\\text{rank}\_{j}(x\_{k,j})-\\text{rank}\_{%
j}(x\_{l,j}))italic\_γ start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT = ∑ sign ( italic\_y start\_POSTSUBSCRIPT italic\_k end\_POSTSUBSCRIPT - italic\_y start\_POSTSUBSCRIPT italic\_l end\_POSTSUBSCRIPT ) ( rank start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT ( italic\_x start\_POSTSUBSCRIPT italic\_k , italic\_j end\_POSTSUBSCRIPT ) - rank start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT ( italic\_x start\_POSTSUBSCRIPT italic\_l , italic\_j end\_POSTSUBSCRIPT ) ), where the rank difference reflects the model performance difference on the same sample, helpful in estimating θ∗superscript𝜃\\theta^{\*}italic\_θ start\_POSTSUPERSCRIPT ∗ end\_POSTSUPERSCRIPT. They then rank the domains based on γjsubscript𝛾𝑗\\gamma\_{j}italic\_γ start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT and select samples from the top-ranked domains. To scale the process, a fastText classifier \[ [200](https://arxiv.org/html/2505.18458v1#bib.bib200 "")\] is trained to distinguish selected documents, enabling page-level data selection.

Report issue for preceding element

To enhance efficiency, \[ [61](https://arxiv.org/html/2505.18458v1#bib.bib61 "")\] leverages a smaller-sized surrogate model to select high-quality pre-training subsets via perplexity score for training larger-sized models, greatly reducing the computational overhead in model training while still achieving the same performance as with the full dataset. They first train a surrogate model, a smaller-sized MosaicML \[ [383](https://arxiv.org/html/2505.18458v1#bib.bib383 "")\] model with 125 million parameters, on a random subset of the pre-training dataset to compute the perplexity scores for the remaining samples. Based on the perplexity scores, they find the optimal subset through a combination of selection criteria: (i)𝑖(i)( italic\_i ) the part of samples to keep (e.g., samples with low/medium/high perplexity scores), and (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) the fraction of samples to keep (e.g., 25%, 50%, 75%). The subset is evaluated by training a larger-sized MosaicML model on it and analyzing the model’s performance on downstream benchmarks. While the result shows that the smaller-sized model can effectively and efficiently filter data for the larger-sized model, they also find that the effectiveness highly depends on the dataset. For example, keeping the high perplexity samples exhibits better performance on the Pile dataset \[ [149](https://arxiv.org/html/2505.18458v1#bib.bib149 "")\], while keeping the medium perplexity samples exhibits better performance on the Dolma dataset \[ [365](https://arxiv.org/html/2505.18458v1#bib.bib365 "")\].

Report issue for preceding element

Furthermore, there are some variants of perplexity-based evaluation. First, \[ [289](https://arxiv.org/html/2505.18458v1#bib.bib289 "")\] proposes a perplexity-based metric, Learning Percentage (LP), to select samples that are more challenging for models to learn. Learning Percentage ℒ⁢𝒫⁢(i)=𝒫i−1−𝒫i𝒫0−𝒫nℒ𝒫𝑖subscript𝒫𝑖1subscript𝒫𝑖subscript𝒫0subscript𝒫𝑛\\mathcal{LP}(i)=\\frac{\\mathcal{P}\_{i-1}-\\mathcal{P}\_{i}}{\\mathcal{P}\_{0}-%
\\mathcal{P}\_{n}}caligraphic\_L caligraphic\_P ( italic\_i ) = divide start\_ARG caligraphic\_P start\_POSTSUBSCRIPT italic\_i - 1 end\_POSTSUBSCRIPT - caligraphic\_P start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_ARG start\_ARG caligraphic\_P start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT - caligraphic\_P start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT end\_ARG measures the perplexity drop ratio of a sample between the specific epoch i𝑖iitalic\_i and the whole training procedure. The key idea is that models tend to learn easier samples first and harder samples later, so one can find harder samples that are not thoroughly learned during early epochs. The authors use ℒ⁢𝒫⁢(1)ℒ𝒫1\\mathcal{LP}(1)caligraphic\_L caligraphic\_P ( 1 ) (the learning percentage after the first epoch) to rank the training samples from the hardest to the easiest and split them into three equal-sized parts. It shows that the smaller-sized variant of the model can effectively select samples for the larger-sized variant, and models of all sizes trained on the harder part outperform the ones trained on all the samples.

Report issue for preceding element

Also based on perplexity, \[ [240](https://arxiv.org/html/2505.18458v1#bib.bib240 "")\] proposes the Instruction-Following Difficulty (IFD) metric to select samples that are more difficult for models to follow. IFD (IFDθ⁢(Q,A)=P⁢P⁢L⁢(A\|Q)P⁢P⁢L⁢(A)subscriptIFD𝜃𝑄𝐴𝑃𝑃𝐿conditional𝐴𝑄𝑃𝑃𝐿𝐴\\text{IFD}\_{\\theta}(Q,A)=\\frac{PPL(A\|Q)}{PPL(A)}IFD start\_POSTSUBSCRIPT italic\_θ end\_POSTSUBSCRIPT ( italic\_Q , italic\_A ) = divide start\_ARG italic\_P italic\_P italic\_L ( italic\_A \| italic\_Q ) end\_ARG start\_ARG italic\_P italic\_P italic\_L ( italic\_A ) end\_ARG) measures the influence of the questions (instructions and inputs combined) on generating corresponding responses by comparing the perplexity of the response with or without the question strings P⁢P⁢L⁢(A\|Q)𝑃𝑃𝐿conditional𝐴𝑄PPL(A\|Q)italic\_P italic\_P italic\_L ( italic\_A \| italic\_Q ) and P⁢P⁢L⁢(A)𝑃𝑃𝐿𝐴PPL(A)italic\_P italic\_P italic\_L ( italic\_A ). A higher IFD score suggests higher model following difficulty. The authors first build a pre-experienced subset by clustering and resampling the samples from the WizardLM \[ [434](https://arxiv.org/html/2505.18458v1#bib.bib434 "")\] and Alpaca-GPT4 \[ [313](https://arxiv.org/html/2505.18458v1#bib.bib313 "")\] datasets, on which they train the model for one epoch to obtain initial knowledge. The model is then used to calculate the IFD score on all the samples, and the ones with high IFD scores are prioritized.

Report issue for preceding element

Superfiltering \[ [239](https://arxiv.org/html/2505.18458v1#bib.bib239 "")\] further enhances \[ [240](https://arxiv.org/html/2505.18458v1#bib.bib240 "")\] by employing the surrogate model from \[ [61](https://arxiv.org/html/2505.18458v1#bib.bib61 "")\]. Instead of training a smaller-sized model, the authors directly use GPT-2 \[ [328](https://arxiv.org/html/2505.18458v1#bib.bib328 "")\] as the surrogate model to calculate IFD scores on the same datasets. Compared to their previous work \[ [240](https://arxiv.org/html/2505.18458v1#bib.bib240 "")\], the adoption of surrogate model simplifies the procedure and accelerates the filtering process.

Report issue for preceding element

∙∙\\bullet∙Influence Assessment. Another data filtering approach is to assess the influence of a sample on LLM model performance or learning process by measuring how the metrics change _when the sample is upweighted or removed_. The samples with substantial impact on the model parameters are regarded as influential and thus are selected.

Report issue for preceding element

DEALRec \[ [255](https://arxiv.org/html/2505.18458v1#bib.bib255 "")\] identifies influential and challenging fine-tuning samples through two metrics: (i)𝑖(i)( italic\_i )Influence Score for assessing the influence of a specific sample on the model performance. It starts by measuring the influence on parameter change, where a surrogate model is trained on the full dataset to estimate how the model parameters would change when certain sample is removed or upweighted, expressed by θ^−s−θ^≈1n⁢Hθ^−1⁢∇θℒ⁢(s,θ^)subscript^𝜃𝑠^𝜃1𝑛superscriptsubscript𝐻^𝜃1subscript∇𝜃ℒ𝑠^𝜃\\hat{\\theta}\_{-s}-\\hat{\\theta}\\approx\\frac{1}{n}H\_{\\hat{\\theta}}^{-1}\\nabla\_{%
\\theta}\\mathcal{L}(s,\\hat{\\theta})over^ start\_ARG italic\_θ end\_ARG start\_POSTSUBSCRIPT - italic\_s end\_POSTSUBSCRIPT - over^ start\_ARG italic\_θ end\_ARG ≈ divide start\_ARG 1 end\_ARG start\_ARG italic\_n end\_ARG italic\_H start\_POSTSUBSCRIPT over^ start\_ARG italic\_θ end\_ARG end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT - 1 end\_POSTSUPERSCRIPT ∇ start\_POSTSUBSCRIPT italic\_θ end\_POSTSUBSCRIPT caligraphic\_L ( italic\_s , over^ start\_ARG italic\_θ end\_ARG ), where Hθ^subscript𝐻^𝜃H\_{\\hat{\\theta}}italic\_H start\_POSTSUBSCRIPT over^ start\_ARG italic\_θ end\_ARG end\_POSTSUBSCRIPT is the Hessian matrix and ∇θℒ⁢(s,θ^)subscript∇𝜃ℒ𝑠^𝜃\\nabla\_{\\theta}\\mathcal{L}(s,\\hat{\\theta})∇ start\_POSTSUBSCRIPT italic\_θ end\_POSTSUBSCRIPT caligraphic\_L ( italic\_s , over^ start\_ARG italic\_θ end\_ARG ) is the loss gradient of sample s𝑠sitalic\_s. The formula is then evolved to measure the influence on empirical risk change, expressed by Iremove, loss⁢(s,𝒟)=1n⁢∑i1n⁢∇θℒ⁢(si,θ^)T⁢Hθ^−1⁢∇θℒ⁢(s,θ^)subscript𝐼remove, loss𝑠𝒟1𝑛subscript𝑖1𝑛subscript∇𝜃ℒsuperscriptsubscript𝑠𝑖^𝜃Tsuperscriptsubscript𝐻^𝜃1subscript∇𝜃ℒ𝑠^𝜃I\_{\\text{remove, loss}}(s,\\mathcal{D})=\\frac{1}{n}\\sum\_{i}\\frac{1}{n}\\nabla\_{%
\\theta}\\mathcal{L}(s\_{i},\\hat{\\theta})^{\\mathrm{T}}H\_{\\hat{\\theta}}^{-1}\\nabla%
\_{\\theta}\\mathcal{L}(s,\\hat{\\theta})italic\_I start\_POSTSUBSCRIPT remove, loss end\_POSTSUBSCRIPT ( italic\_s , caligraphic\_D ) = divide start\_ARG 1 end\_ARG start\_ARG italic\_n end\_ARG ∑ start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT divide start\_ARG 1 end\_ARG start\_ARG italic\_n end\_ARG ∇ start\_POSTSUBSCRIPT italic\_θ end\_POSTSUBSCRIPT caligraphic\_L ( italic\_s start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT , over^ start\_ARG italic\_θ end\_ARG ) start\_POSTSUPERSCRIPT roman\_T end\_POSTSUPERSCRIPT italic\_H start\_POSTSUBSCRIPT over^ start\_ARG italic\_θ end\_ARG end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT - 1 end\_POSTSUPERSCRIPT ∇ start\_POSTSUBSCRIPT italic\_θ end\_POSTSUBSCRIPT caligraphic\_L ( italic\_s , over^ start\_ARG italic\_θ end\_ARG ); (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i )Effort Score for assessing the difficulty for the surrogate model to learn a specific sample for generalization to new samples, defined as δs=‖∇ϕℒLLM⁢(s)‖2,subscript𝛿𝑠subscriptnormsubscript∇italic-ϕsuperscriptℒLLM𝑠2\\delta\_{s}=\\\|\\nabla\_{\\phi}\\mathcal{L}^{\\text{LLM}}(s)\\\|\_{2},italic\_δ start\_POSTSUBSCRIPT italic\_s end\_POSTSUBSCRIPT = ∥ ∇ start\_POSTSUBSCRIPT italic\_ϕ end\_POSTSUBSCRIPT caligraphic\_L start\_POSTSUPERSCRIPT LLM end\_POSTSUPERSCRIPT ( italic\_s ) ∥ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT , where ΦΦ\\Phiroman\_Φ is the model parameter. A higher effort score suggests greater difficulty. The final score combines the above two scores, written as Is=Influence Score+λ⋅Effort Scoresubscript𝐼𝑠Influence Score⋅𝜆Effort ScoreI\_{s}=\\text{Influence Score}+\\lambda\\cdot\\text{Effort Score}italic\_I start\_POSTSUBSCRIPT italic\_s end\_POSTSUBSCRIPT = Influence Score + italic\_λ ⋅ Effort Score.

Report issue for preceding element

Besides, SHED \[ [169](https://arxiv.org/html/2505.18458v1#bib.bib169 "")\] utilizes the Shapley value \[ [342](https://arxiv.org/html/2505.18458v1#bib.bib342 "")\], which estimates the contribution of a member to the group, to calculate the influence of a sample on the model performance and select representative samples with high influence. The method first clusters the samples and selects the ones closest to each cluster centroid as the representative samples to reduce computational overhead. It then calculates the Shapley value for each representative sample i𝑖iitalic\_i by iteratively removing n𝑛nitalic\_n samples from the dataset until all the samples have been removed and calculating the contribution of the removed n𝑛nitalic\_n samples in each iteration a𝑎aitalic\_a to the model performance compared with the previous iteration, written as: c(an+1..(a+1)n)∈Dp=v(Dp∖{1..an})−v(Dp∖{1..(a+1)n})c\_{(an+1..(a+1)n)\\in D\_{p}}=v(D\_{p}\\setminus\\{1..an\\})-v(D\_{p}\\setminus\\{1..(a%
+1)n\\})italic\_c start\_POSTSUBSCRIPT ( italic\_a italic\_n + 1 . . ( italic\_a + 1 ) italic\_n ) ∈ italic\_D start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT end\_POSTSUBSCRIPT = italic\_v ( italic\_D start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT ∖ { 1 . . italic\_a italic\_n } ) - italic\_v ( italic\_D start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT ∖ { 1 . . ( italic\_a + 1 ) italic\_n } ). The process will be repeated for k𝑘kitalic\_k times for higher accuracy, after which the Shapley value for each representative sample i𝑖iitalic\_i is defined as Si≈1k⁢∑kci⁢(k)nsubscript𝑆𝑖1𝑘subscript𝑘subscript𝑐𝑖𝑘𝑛S\_{i}\\approx\\frac{1}{k}\\sum\_{k}\\frac{c\_{i}(k)}{n}italic\_S start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ≈ divide start\_ARG 1 end\_ARG start\_ARG italic\_k end\_ARG ∑ start\_POSTSUBSCRIPT italic\_k end\_POSTSUBSCRIPT divide start\_ARG italic\_c start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ( italic\_k ) end\_ARG start\_ARG italic\_n end\_ARG. Finally, the subsets can be selected either by selecting from the top-rank samples or weighted sampling the samples through Pr⁡(i)=ef⁢Si∑ief⁢SiPr𝑖superscript𝑒𝑓subscript𝑆𝑖subscript𝑖superscript𝑒𝑓subscript𝑆𝑖\\Pr(i)=\\frac{e^{fS\_{i}}}{\\sum\_{i}e^{fS\_{i}}}roman\_Pr ( italic\_i ) = divide start\_ARG italic\_e start\_POSTSUPERSCRIPT italic\_f italic\_S start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT end\_ARG start\_ARG ∑ start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT italic\_e start\_POSTSUPERSCRIPT italic\_f italic\_S start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT end\_ARG, where f𝑓fitalic\_f controls the trade-off between quality and diversity.

Report issue for preceding element

∙∙\\bullet∙Clustering. A common approach to select high-quality and diverse subsets is to encode the samples into embeddings in the latest space and cluster them using cosine similarity, where similar samples are usually clustered into the same group. Selecting within the clusters reduces redundancy, while selecting across the clusters increases diversity.

Report issue for preceding element

Density-Based Pruning (DBP) \[ [45](https://arxiv.org/html/2505.18458v1#bib.bib45 "")\] selects high-quality and diverse subsets by clustering samples into clusters and resampling the samples based on the cluster complexity. They encode the samples into embeddings using a pre-trained vision model DINOV2-L/14 \[ [301](https://arxiv.org/html/2505.18458v1#bib.bib301 "")\] and cluster them using K-means. For each cluster, they calculate the average intra-cluster cosine-distance to the internal centroid di⁢n⁢t⁢r⁢asubscript𝑑𝑖𝑛𝑡𝑟𝑎d\_{intra}italic\_d start\_POSTSUBSCRIPT italic\_i italic\_n italic\_t italic\_r italic\_a end\_POSTSUBSCRIPT and inter-cluster cosine distance to the other centroids di⁢n⁢t⁢e⁢rsubscript𝑑𝑖𝑛𝑡𝑒𝑟d\_{inter}italic\_d start\_POSTSUBSCRIPT italic\_i italic\_n italic\_t italic\_e italic\_r end\_POSTSUBSCRIPT, and the cluster complexity as a product of the two distances C=di⁢n⁢t⁢r⁢a×di⁢n⁢t⁢e⁢r𝐶subscript𝑑𝑖𝑛𝑡𝑟𝑎subscript𝑑𝑖𝑛𝑡𝑒𝑟C=d\_{intra}\\times d\_{inter}italic\_C = italic\_d start\_POSTSUBSCRIPT italic\_i italic\_n italic\_t italic\_r italic\_a end\_POSTSUBSCRIPT × italic\_d start\_POSTSUBSCRIPT italic\_i italic\_n italic\_t italic\_e italic\_r end\_POSTSUBSCRIPT. The cluster complexity is later converted to probability using softmax to resample the samples across clusters, where clusters with higher complexity have higher weights.

Report issue for preceding element

Rather than the sample embedding itself, SmallToLarge \[ [444](https://arxiv.org/html/2505.18458v1#bib.bib444 "")\] selects a diverse subset by clustering the samples based on their loss trajectories. It first trains a smaller-sized surrogate LLM model on the whole dataset to obtain the loss trajectories of each training sample, defined as ℒi⁢(ϕ(t))=−log⁡pϕ(t)⁢(𝐲i\|𝐱i)subscriptℒ𝑖superscriptbold-italic-ϕ𝑡subscript𝑝superscriptbold-italic-ϕ𝑡conditionalsubscript𝐲𝑖subscript𝐱𝑖\\mathcal{L}\_{i}(\\bm{\\phi}^{(t)})=-\\log p\_{\\bm{\\phi}^{(t)}}(\\mathbf{y}\_{i}\|%
\\mathbf{x}\_{i})caligraphic\_L start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ( bold\_italic\_ϕ start\_POSTSUPERSCRIPT ( italic\_t ) end\_POSTSUPERSCRIPT ) = - roman\_log italic\_p start\_POSTSUBSCRIPT bold\_italic\_ϕ start\_POSTSUPERSCRIPT ( italic\_t ) end\_POSTSUPERSCRIPT end\_POSTSUBSCRIPT ( bold\_y start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT \| bold\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ), where ϕ(t)superscriptbold-italic-ϕ𝑡\\bm{\\phi}^{(t)}bold\_italic\_ϕ start\_POSTSUPERSCRIPT ( italic\_t ) end\_POSTSUPERSCRIPT is the model parameters at time t𝑡titalic\_t. These samples are then clustered based on loss trajectories and randomly resampled to form a diverse subset.

Report issue for preceding element

(2) Model Scoring uses LLMs for evaluating sample quality. The quality criteria can either be specified (i)𝑖(i)( italic\_i ) explicitly via LLM prompt engineering or (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) implicitly learned from human-labeled data.

Report issue for preceding element

QuRating \[ [418](https://arxiv.org/html/2505.18458v1#bib.bib418 "")\] selects high-quality pre-training samples by prompting LLM to compare pairs of samples along the four quality criteria (writing style, fact & trivia amount, educational value, and the expertise required to understand), training a rater on the scalar quality ratings, and filtering samples using the rater. Initially, GPT-3.5-turbo is prompted on each pair of samples to judge which one is better on each quality criterion, where the binary confidence pB≻A∈\[0,1\]subscript𝑝succeeds𝐵𝐴01p\_{B\\succ A}\\in\[0,1\]italic\_p start\_POSTSUBSCRIPT italic\_B ≻ italic\_A end\_POSTSUBSCRIPT ∈ \[ 0 , 1 \] that the sample B is preferred over the sample A is recorded. The pairwise binary confidence is then translated into sample quality ratings pB≻A=σ⁢(sB−sA)subscript𝑝succeeds𝐵𝐴𝜎subscript𝑠𝐵subscript𝑠𝐴p\_{B\\succ A}=\\sigma(s\_{B}-s\_{A})italic\_p start\_POSTSUBSCRIPT italic\_B ≻ italic\_A end\_POSTSUBSCRIPT = italic\_σ ( italic\_s start\_POSTSUBSCRIPT italic\_B end\_POSTSUBSCRIPT - italic\_s start\_POSTSUBSCRIPT italic\_A end\_POSTSUBSCRIPT ) through the Bradley-Terry model. A QuRater model is later trained on these quality ratings to predict quality ratings for new samples on each criterion. The new samples are resampled with the probability p⁢(di)∝exp⁡(siτ)proportional-to𝑝subscript𝑑𝑖subscript𝑠𝑖𝜏p(d\_{i})\\propto\\exp\\left(\\frac{s\_{i}}{\\tau}\\right)italic\_p ( italic\_d start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) ∝ roman\_exp ( divide start\_ARG italic\_s start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_ARG start\_ARG italic\_τ end\_ARG ), where τ𝜏\\tauitalic\_τ adjusts the trade-off between quality and diversity.

Report issue for preceding element

Rather than prompting the models to compare samples, Data-Efficient Instruction Tuning for Alignment (DEITA) \[ [265](https://arxiv.org/html/2505.18458v1#bib.bib265 "")\] prompts LLM models to evolve and score the samples for building sample scorers. The authors first prompt ChatGPT to evolve the samples along instruction complexity and response quality, and again prompt ChatGPT to score these evolved samples. They then train scorers on the evolved samples with their corresponding scores to enable their scoring abilities. Finally, they use these scorers to score new samples and multiply the scores to form the final score, where the new samples are resampled based on the final scores for diversity.

Report issue for preceding element

Model scoring methods also help mitigate bias and toxicity. LLM often exhibit harmful biases due to the massive and unchecked datasets they are trained on, which can have various biases, ranging from gender and racial stereotypes to cultural and socioeconomic prejudices \[ [297](https://arxiv.org/html/2505.18458v1#bib.bib297 "")\].
Safety-enhanced Aligned LLM Fine-tuning (SEAL) \[ [349](https://arxiv.org/html/2505.18458v1#bib.bib349 "")\] selects high-quality and safe fine-tuning samples through a safety-aligned selector. The selector is trained based on a safety-aligned model, Merlinite-7b \[ [371](https://arxiv.org/html/2505.18458v1#bib.bib371 "")\], using bi-level optimization, which minimizes the safety loss on the safe dataset while minimizing the fine-tuning loss on the filtered dataset during training to ensure the selector always prioritizes safe and high-quality samples during selection. After the selection, the top-p% samples will be selected.

Report issue for preceding element

(3) Hybrid Methods. Instead of relying on a single method, some methods mix various kinds of data filtering methods and evaluate each permutation of these methods or parameters to find the best combination of methods or parameters that further boosts model performance.

Report issue for preceding element

\[ [286](https://arxiv.org/html/2505.18458v1#bib.bib286 "")\] selects high-quality pre-training data based on three metrics: (i)𝑖(i)( italic\_i ) Perplexity, (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) EL2N χ⁢(xi,yi)=𝔼⁢‖f⁢(xi)−yi‖2𝜒subscript𝑥𝑖subscript𝑦𝑖𝔼subscriptnorm𝑓subscript𝑥𝑖subscript𝑦𝑖2\\chi(x\_{i},y\_{i})=\\mathbb{E}\\\|f(x\_{i})-y\_{i}\\\|\_{2}italic\_χ ( italic\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT , italic\_y start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) = blackboard\_E ∥ italic\_f ( italic\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) - italic\_y start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ∥ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT for measuring the prediction probability discrepancy between the reference model and the ground truth, and (i⁢i⁢i)𝑖𝑖𝑖(iii)( italic\_i italic\_i italic\_i ) Memorization factor s⁢c⁢o⁢r⁢e⁢(M,N)=1N⁢∑iN1⁢(zM+i=z^M+i)𝑠𝑐𝑜𝑟𝑒𝑀𝑁1𝑁subscriptsuperscript𝑁𝑖1subscript𝑧𝑀𝑖subscript^𝑧𝑀𝑖score(M,N)=\\frac{1}{N}\\sum^{N}\_{i}1(z\_{M+i}=\\hat{z}\_{M+i})italic\_s italic\_c italic\_o italic\_r italic\_e ( italic\_M , italic\_N ) = divide start\_ARG 1 end\_ARG start\_ARG italic\_N end\_ARG ∑ start\_POSTSUPERSCRIPT italic\_N end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT 1 ( italic\_z start\_POSTSUBSCRIPT italic\_M + italic\_i end\_POSTSUBSCRIPT = over^ start\_ARG italic\_z end\_ARG start\_POSTSUBSCRIPT italic\_M + italic\_i end\_POSTSUBSCRIPT ) for measuring the fraction of N tokens correctly generated after prompting the model with the first M tokens \[ [77](https://arxiv.org/html/2505.18458v1#bib.bib77 "")\].
For each metric, they retain samples based on two criteria: (i)𝑖(i)( italic\_i ) the fraction of samples to keep (10%, 30%, 50%, and 70%) and (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) the part of samples to keep, e.g., the bottom (for Perplexity and L2-Norm Error) and top (for Memorization). They train LLM for each case and select the best-performing one, and the result shows that Perplexity effectively removes the “easiest” samples, improving model performance and outperforming other metrics.

Report issue for preceding element

Instead of comparing metrics and choosing the best of them, InstructionMining \[ [84](https://arxiv.org/html/2505.18458v1#bib.bib84 "")\] combines various metrics (e.g., including input/output length, reward score, perplexity, etc.) into one linear function with each metric as indicator, written as l⁢o⁢g⁢Ll⁢o⁢s⁢s∝L0+β0+β1⁢I1+β2⁢I2+⋯+βn⁢In+ϵproportional-to𝑙𝑜𝑔subscript𝐿𝑙𝑜𝑠𝑠subscript𝐿0subscript𝛽0subscript𝛽1subscript𝐼1subscript𝛽2subscript𝐼2⋯subscript𝛽𝑛subscript𝐼𝑛italic-ϵlogL\_{loss}\\propto L\_{0}+\\beta\_{0}+\\beta\_{1}I\_{1}+\\beta\_{2}I\_{2}+\\cdots+\\beta\_%
{n}I\_{n}+\\epsilonitalic\_l italic\_o italic\_g italic\_L start\_POSTSUBSCRIPT italic\_l italic\_o italic\_s italic\_s end\_POSTSUBSCRIPT ∝ italic\_L start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT + italic\_β start\_POSTSUBSCRIPT 0 end\_POSTSUBSCRIPT + italic\_β start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT italic\_I start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT + italic\_β start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT italic\_I start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT + ⋯ + italic\_β start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT italic\_I start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT + italic\_ϵ. The β𝛽\\betaitalic\_β parameters are estimated using least squares. In practice, it evaluates fine-tuning samples on a fine-tuned model LLaMA-2-7B \[ [391](https://arxiv.org/html/2505.18458v1#bib.bib391 "")\] and selects samples by finding the optimal set of samples to keep using the hyperparameter optimizer BlendSearch \[ [401](https://arxiv.org/html/2505.18458v1#bib.bib401 "")\].

Report issue for preceding element

MoDS \[ [126](https://arxiv.org/html/2505.18458v1#bib.bib126 "")\] considers diversity into selection and iteratively selects high-quality, diverse, and necessary subsets and adds the samples the LLM model performs poorly on during fine-tuning using a reward model and the K-Center greedy algorithm \[ [345](https://arxiv.org/html/2505.18458v1#bib.bib345 "")\]. The method is conducted mainly in three steps: (i)𝑖(i)( italic\_i ) Use a reward model to score the quality of each (instruction, input, output) triplet in the dataset, where the low-quality ones are filtered out, forming a high-quality dataset. (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) Use the K-Center greedy algorithm \[ [346](https://arxiv.org/html/2505.18458v1#bib.bib346 "")\] to select the samples in the high-quality dataset that are farthest apart from each other in the BERT \[ [207](https://arxiv.org/html/2505.18458v1#bib.bib207 "")\] embedding space, forming a diverse seed dataset. (i⁢i⁢i)𝑖𝑖𝑖(iii)( italic\_i italic\_i italic\_i ) Fine-tune a pre-trained LLM model on the seed dataset to enable its instruction-following ability and generate responses for the high-quality dataset. The generated responses are evaluated using the same reward model, and those with low quality scores, which means the model is weak at generating such responses, will be collected. The collected samples with their original responses will be selected again using the K-Center greedy algorithm and then added to the seed dataset, forming the final dataset.

Report issue for preceding element

Content-level Filtering. To avoid removing too many critical samples from the dataset and weakening the model performance, some works only filter out noise or sensitive content within the samples. For noise removal, common methodologies include removing or replacing specific characters (e.g., remove invisible or invalid characters, unescape HTML characters and detect punctuation misuse), removing unnecessary texts (e.g., the texts that appear as decorating elements on the web pages such as “print”, “likes” and “loading” ), and cleaning harmful information (e.g., spam, gambling, pornographic content and site links) \[ [441](https://arxiv.org/html/2505.18458v1#bib.bib441 "")\].

Report issue for preceding element

For privacy anonymization, LLMs can memorize private and sensitive information (e.g, user identity details or clinical health data) from datasets during pre-training and fine-tuning, which can be leaked through specially crafted prompts, thereby posing significant privacy risks. \[ [276](https://arxiv.org/html/2505.18458v1#bib.bib276 "")\] demonstrates that it is possible to extract, reconstruct, and infer personally identifiable information (PII) from LLM models by identifying the most frequent PII appearing in model responses or by prompting models with partial information about a specific individual. From a data management perspective, these privacy threats can be mitigated by identifying and filtering out potential sensitive information in the datasets.

Report issue for preceding element

DeID-GPT \[ [269](https://arxiv.org/html/2505.18458v1#bib.bib269 "")\] utilizes existing LLMs to identify and remove PII from unstructured medical text without changing its meaning. In their case, the LLMs are prompted to de-identify information from clinical notes in accordance with HIPAA privacy regulations. An example prompt is: “Please de-identify the following clinical notes by replacing any terms that could be a name, an address, a date, or an ID with the term ‘\[redacted\]’.”

Report issue for preceding element

Instead of using general LLMs, \[ [276](https://arxiv.org/html/2505.18458v1#bib.bib276 "")\] uses Named Entity Recognition (NER) models such as spaCy \[ [33](https://arxiv.org/html/2505.18458v1#bib.bib33 "")\] and Flair \[ [52](https://arxiv.org/html/2505.18458v1#bib.bib52 "")\] to tag PII in the samples and removes or replaces them with hashed tags, entity tags like “\[NAME\]” or “\[LOCATION\]”, or a simple tag like “\[MASK\]”. The last tag was adopted to maximize privacy, as the other ones are still vulnerable to membership inference by linking the samples.

Report issue for preceding element

The rise of multi-modal LLMs, particularly large video generation models, drives the need for robust video data filtering. CogVideoX \[ [445](https://arxiv.org/html/2505.18458v1#bib.bib445 "")\] employs a pipeline focusing on coherent motion, removing videos with poor dynamics. It defines negative labels for artificial edits, low motion connectivity, visual flaws, and excessive text. A manually annotated subset trains six Video-LLaMA\[ [462](https://arxiv.org/html/2505.18458v1#bib.bib462 "")\]-based filters, while optical flow and aesthetic scores ensure motion coherence and visual appeal, refining the dataset to approximately 35M high-quality 6-second clips.

Report issue for preceding element

HunyuanVideo \[ [217](https://arxiv.org/html/2505.18458v1#bib.bib217 "")\] uses a multi-step pipeline: splitting videos into clips, encoding embeddings, deduplication, and resampling. Filters include motion (OpenCV-based optical flow), OCR (text removal), clarity (visual blur detection), aesthetic (Dover\[ [421](https://arxiv.org/html/2505.18458v1#bib.bib421 "")\]-based scoring), and source (YOLOX\[ [154](https://arxiv.org/html/2505.18458v1#bib.bib154 "")\]-like watermark/border removal). This process generates five progressive training sets with increasing thresholds.

Report issue for preceding element

Wan \[ [396](https://arxiv.org/html/2505.18458v1#bib.bib396 "")\] applies pre- and post-processing pipelines. Pre-processing filters unsuitable data using OCR, aesthetic evaluation (LAION-5B \[ [344](https://arxiv.org/html/2505.18458v1#bib.bib344 "")\]), NSFW scoring, watermark detection, and resolution thresholds, removing approximately 50% of low-quality data. Samples are clustered for diversity, manually scored, and an expert model selects high-quality, naturally distributed data. Videos are classified into six tiers, prioritizing smooth motion. Post-processing refines images by selecting top 20% via an expert model and manually curating gaps. For videos, top candidates are filtered by visual quality and motion complexity, ensuring balance and diversity across 12 themes.

Report issue for preceding element

#### 2.2.4 Data Selection

Report issue for preceding elementTABLE V: Comparison of Different Data Selection Methods.

|     |     |     |
| --- | --- | --- |
| Method | Stage | Evaluation Metric |
| Similarity | |     |
| --- |
| Pre-training, |
| Fine-tuning | | |     |
| --- |
| Cosine Similarity \[ [431](https://arxiv.org/html/2505.18458v1#bib.bib431 "")\] |
| Bag-of-Words Similarity \[ [429](https://arxiv.org/html/2505.18458v1#bib.bib429 "")\] |
| Lexicon Set Overlap \[ [322](https://arxiv.org/html/2505.18458v1#bib.bib322 "")\] |
| Bayes-based Selection \[ [80](https://arxiv.org/html/2505.18458v1#bib.bib80 "")\] | |
| Optimization | Fine-tuning | |     |
| --- |
| Linear Search \[ [130](https://arxiv.org/html/2505.18458v1#bib.bib130 "")\] |
| Gradient-Influence Search \[ [424](https://arxiv.org/html/2505.18458v1#bib.bib424 "")\] |
| Kernel-Density Regularization \[ [270](https://arxiv.org/html/2505.18458v1#bib.bib270 "")\] | |
| Model | Pre-training | Logits-based LM-Score \[ [472](https://arxiv.org/html/2505.18458v1#bib.bib472 "")\] |

Report issue for preceding element

Different from previous reviews \[ [55](https://arxiv.org/html/2505.18458v1#bib.bib55 ""), [405](https://arxiv.org/html/2505.18458v1#bib.bib405 "")\], we define data selection as the process of choosing subsets of already well-cleaned data samples in order to adapt LLMs to specific domains (e.g., medical or legal LLMs).

Report issue for preceding element

PrinciplesUnlike traditional ML data selection, LLM data selection focuses on aligning the topics of the text samples, requiring encoding semantic topics into measurable distributions. However, managing computational efficiency and ensuring robust generalization across diverse tasks remain critical unresolved issues.Report issue for preceding element

Similarity-based Data Selection. One class of methods aims to select subsets similar to the specified target data.

Report issue for preceding element

∙∙\\bullet∙_Cosine Similarity:_ Domain-Adaptive Continual Pre-training (DACP) \[ [431](https://arxiv.org/html/2505.18458v1#bib.bib431 "")\] adapts a general-purpose LLM to a target task by selecting domain-specific unlabeled data based on similarity (cosine similarity), novelty (perplexity), and diversity (entropy). For the similarity part, it identifies data most similar to the task-specific labeled data by encoding both into embeddings (using \[ [33](https://arxiv.org/html/2505.18458v1#bib.bib33 "")\]) and choosing domain samples that align with the task’s embedding distribution.

Report issue for preceding element

∙∙\\bullet∙_Bag-of-Words Similarity:_ DSIR \[ [429](https://arxiv.org/html/2505.18458v1#bib.bib429 "")\] selects a subset of unlabeled pre-training data matching the target distribution by computing feature distributions (p^featsubscript^𝑝feat\\hat{p}\_{\\text{feat}}over^ start\_ARG italic\_p end\_ARG start\_POSTSUBSCRIPT feat end\_POSTSUBSCRIPT, q^featsubscript^𝑞feat\\hat{q}\_{\\text{feat}}over^ start\_ARG italic\_q end\_ARG start\_POSTSUBSCRIPT feat end\_POSTSUBSCRIPT) for raw and target data represented as bag-of-words, estimating importance weights wi=p^feat⁢(zi)q^feat⁢(zi)subscript𝑤𝑖subscript^𝑝featsubscript𝑧𝑖subscript^𝑞featsubscript𝑧𝑖w\_{i}=\\frac{\\hat{p}\_{\\text{feat}}(z\_{i})}{\\hat{q}\_{\\text{feat}}(z\_{i})}italic\_w start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT = divide start\_ARG over^ start\_ARG italic\_p end\_ARG start\_POSTSUBSCRIPT feat end\_POSTSUBSCRIPT ( italic\_z start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) end\_ARG start\_ARG over^ start\_ARG italic\_q end\_ARG start\_POSTSUBSCRIPT feat end\_POSTSUBSCRIPT ( italic\_z start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) end\_ARG, and resampling raw data with probability wi∑i=1Nwisubscript𝑤𝑖subscriptsuperscript𝑁𝑖1subscript𝑤𝑖\\frac{w\_{i}}{\\sum^{N}\_{i=1}w\_{i}}divide start\_ARG italic\_w start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_ARG start\_ARG ∑ start\_POSTSUPERSCRIPT italic\_N end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT italic\_i = 1 end\_POSTSUBSCRIPT italic\_w start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_ARG.

Report issue for preceding element

∙∙\\bullet∙_Lexicon Set Overlap:_\[ [322](https://arxiv.org/html/2505.18458v1#bib.bib322 "")\] selects the subset with the most shared lexicons using the Domain Specific Score (DSS), which quantifies the relevance of a dialogue set T𝑇Titalic\_T to specific domains by measuring the overlap between T𝑇Titalic\_T and domain lexicons L={l1,l2,…,lm}𝐿subscript𝑙1subscript𝑙2…subscript𝑙𝑚L=\\{l\_{1},l\_{2},\\dots,l\_{m}\\}italic\_L = { italic\_l start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , italic\_l start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT , … , italic\_l start\_POSTSUBSCRIPT italic\_m end\_POSTSUBSCRIPT }, calculated as DSS⁢(T,L)=1m⁢∑i=1m\|T∩li\|nDSS𝑇𝐿1𝑚superscriptsubscript𝑖1𝑚𝑇subscript𝑙𝑖𝑛\\text{DSS}(T,L)=\\frac{1}{m}\\sum\_{i=1}^{m}\\frac{\|T\\cap l\_{i}\|}{n}DSS ( italic\_T , italic\_L ) = divide start\_ARG 1 end\_ARG start\_ARG italic\_m end\_ARG ∑ start\_POSTSUBSCRIPT italic\_i = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_m end\_POSTSUPERSCRIPT divide start\_ARG \| italic\_T ∩ italic\_l start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT \| end\_ARG start\_ARG italic\_n end\_ARG, where n𝑛nitalic\_n is the number of tokens in T𝑇Titalic\_T.

Report issue for preceding element

∙∙\\bullet∙_Bayes-based Selection:_ CoLoR-filter \[ [80](https://arxiv.org/html/2505.18458v1#bib.bib80 "")\] formulates pre-training subset selection as a Bayesian optimization problem, which selects a subset S𝑆Sitalic\_S by minimizing downstream loss or maximizing downstream task performance Pr⁢(Ddown\|S)Prconditionalsubscript𝐷down𝑆\\text{Pr}(D\_{\\text{down}}\|S)Pr ( italic\_D start\_POSTSUBSCRIPT down end\_POSTSUBSCRIPT \| italic\_S ). It uses two auxiliary models: A “prior” model (θpriorsubscript𝜃prior\\theta\_{\\text{prior}}italic\_θ start\_POSTSUBSCRIPT prior end\_POSTSUBSCRIPT) trained on a large general dataset Ddownsubscript𝐷downD\_{\\text{down}}italic\_D start\_POSTSUBSCRIPT down end\_POSTSUBSCRIPT and a “conditional” model (θpriorsubscript𝜃prior\\theta\_{\\text{prior}}italic\_θ start\_POSTSUBSCRIPT prior end\_POSTSUBSCRIPT) fine-tuned on the union of the large general dataset and a small downstream dataset Dprior+downsubscript𝐷prior+downD\_{\\text{prior+down}}italic\_D start\_POSTSUBSCRIPT prior+down end\_POSTSUBSCRIPT. The selection criterion for a data point xisubscript𝑥𝑖x\_{i}italic\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT is the conditional loss reduction (CoLoR): CoLoR⁢(xi)=−log⁡Pr⁡(xi\|θprior+down)−(−log⁡Pr⁡(xi\|θprior))CoLoRsubscript𝑥𝑖Prconditionalsubscript𝑥𝑖subscript𝜃prior+downPrconditionalsubscript𝑥𝑖subscript𝜃prior\\text{CoLoR}(x\_{i})=-\\log\\Pr(x\_{i}\|\\theta\_{\\text{prior+down}})-(-\\log\\Pr(x\_{i}%
\|\\theta\_{\\text{prior}}))CoLoR ( italic\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) = - roman\_log roman\_Pr ( italic\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT \| italic\_θ start\_POSTSUBSCRIPT prior+down end\_POSTSUBSCRIPT ) - ( - roman\_log roman\_Pr ( italic\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT \| italic\_θ start\_POSTSUBSCRIPT prior end\_POSTSUBSCRIPT ) ). The key idea is to score data points based on the difference in their likelihood under these two models, selecting those that are more likely under the conditional model. This conditional loss reduction (CoLoR) criterion helps identify data that is particularly useful for the target tasks.

Report issue for preceding element

Optimization-based Data Selection. Optimization-based data selection methods select subsets towards reducing model loss and improving model performance on the target tasks.

Report issue for preceding element

∙∙\\bullet∙_Linear Search._ Model-Aware Dataset Selection with Datamodels (DsDm) \[ [130](https://arxiv.org/html/2505.18458v1#bib.bib130 "")\] selects the optimal subset of training data that minimizes the model’s loss on target tasks by employing linear datamodel \[ [185](https://arxiv.org/html/2505.18458v1#bib.bib185 "")\], a parameterized function that maps a subset of training data to the model outputs for the specified target, to estimate how the inclusion of each training example would affect the model’s loss on the target, avoiding infeasible computations. In practice, a linear datamodel τθx⁢(1S)=θx⊤⁢1Ssubscript𝜏subscript𝜃𝑥subscript1𝑆superscriptsubscript𝜃𝑥topsubscript1𝑆\\tau\_{\\theta\_{x}}(1\_{S})=\\theta\_{x}^{\\top}1\_{S}italic\_τ start\_POSTSUBSCRIPT italic\_θ start\_POSTSUBSCRIPT italic\_x end\_POSTSUBSCRIPT end\_POSTSUBSCRIPT ( 1 start\_POSTSUBSCRIPT italic\_S end\_POSTSUBSCRIPT ) = italic\_θ start\_POSTSUBSCRIPT italic\_x end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ⊤ end\_POSTSUPERSCRIPT 1 start\_POSTSUBSCRIPT italic\_S end\_POSTSUBSCRIPT with parameters θxsubscript𝜃𝑥\\theta\_{x}italic\_θ start\_POSTSUBSCRIPT italic\_x end\_POSTSUBSCRIPT and a characteristic vector 1Ssubscript1𝑆1\_{S}1 start\_POSTSUBSCRIPT italic\_S end\_POSTSUBSCRIPT (a binary vector indicating which data points are in S𝑆Sitalic\_S) is adopted to map the subset S𝑆Sitalic\_S to the model loss on a sample x𝑥xitalic\_x through Lx⁢(S)=𝔼⁢\[ℓ⁢(x;A⁢(S))\]subscript𝐿𝑥𝑆𝔼delimited-\[\]ℓ𝑥𝐴𝑆L\_{x}(S)=\\mathbb{E}\[\\ell(x;A(S))\]italic\_L start\_POSTSUBSCRIPT italic\_x end\_POSTSUBSCRIPT ( italic\_S ) = blackboard\_E \[ roman\_ℓ ( italic\_x ; italic\_A ( italic\_S ) ) \]. For each target, the characteristic vector 1Ssubscript1𝑆1\_{S}1 start\_POSTSUBSCRIPT italic\_S end\_POSTSUBSCRIPT is adjusted to reflect the subset, and the parameters θxsubscript𝜃𝑥\\theta\_{x}italic\_θ start\_POSTSUBSCRIPT italic\_x end\_POSTSUBSCRIPT are estimated using a regression loss function like mean squared error over the training subset. After training, the datamodel selects the subset S𝑆Sitalic\_S of the size k𝑘kitalic\_k that minimizes the loss L^Dtarg⁢(S)=1n⁢∑i=1nτθxi⁢(1S)subscript^𝐿subscript𝐷targ𝑆1𝑛superscriptsubscript𝑖1𝑛subscript𝜏subscript𝜃subscript𝑥𝑖subscript1𝑆\\hat{L}\_{D\_{\\text{targ}}}(S)=\\frac{1}{n}\\sum\_{i=1}^{n}\\tau\_{\\theta\_{x\_{i}}}(1\_%
{S})over^ start\_ARG italic\_L end\_ARG start\_POSTSUBSCRIPT italic\_D start\_POSTSUBSCRIPT targ end\_POSTSUBSCRIPT end\_POSTSUBSCRIPT ( italic\_S ) = divide start\_ARG 1 end\_ARG start\_ARG italic\_n end\_ARG ∑ start\_POSTSUBSCRIPT italic\_i = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_n end\_POSTSUPERSCRIPT italic\_τ start\_POSTSUBSCRIPT italic\_θ start\_POSTSUBSCRIPT italic\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_POSTSUBSCRIPT end\_POSTSUBSCRIPT ( 1 start\_POSTSUBSCRIPT italic\_S end\_POSTSUBSCRIPT ) for the target task.

Report issue for preceding element

∙∙\\bullet∙_Gradient-Influence Search._ Low-rank Gradient Similarity Search (LESS) \[ [424](https://arxiv.org/html/2505.18458v1#bib.bib424 "")\] identifies the most impactful subset of data for fine-tuning LLMs by analyzing gradient similarities. It first fine-tunes the model on a random subset (e.g., 5% of data) for a few epochs using LoRA to reduce trainable parameters and accelerate gradient computation, and saves the checkpoints after each epoch. Next, LESS computes Adam LoRA gradients for each training sample, projects them into lower-dimensional gradient features via random projection, and stores them in a gradient datastore. For downstream tasks, it calculates gradient features of few-shot validation samples and estimates the influence of each training sample 𝒛𝒛\\bm{z}bold\_italic\_z on a validation sample 𝒛′superscript𝒛′\\bm{z}^{\\prime}bold\_italic\_z start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT using cosine similarity: InfAdam⁢(𝒛,𝒛′)≜∑i=1Nη¯i⁢cos⁡(∇ℓ⁢(𝒛′;𝜽i),Γ⁢(𝒛,𝜽i))≜subscriptInfAdam𝒛superscript𝒛′superscriptsubscript𝑖1𝑁subscript¯𝜂𝑖∇ℓsuperscript𝒛′subscript𝜽𝑖Γ𝒛subscript𝜽𝑖\\text{Inf}\_{\\text{Adam}}(\\bm{z},\\bm{z}^{\\prime})\\triangleq\\sum\_{i=1}^{N}\\bar{%
\\eta}\_{i}\\cos(\\nabla\\ell(\\bm{z}^{\\prime};\\bm{\\theta}\_{i}),\\Gamma(\\bm{z},\\bm{%
\\theta}\_{i}))Inf start\_POSTSUBSCRIPT Adam end\_POSTSUBSCRIPT ( bold\_italic\_z , bold\_italic\_z start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ) ≜ ∑ start\_POSTSUBSCRIPT italic\_i = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_N end\_POSTSUPERSCRIPT over¯ start\_ARG italic\_η end\_ARG start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT roman\_cos ( ∇ roman\_ℓ ( bold\_italic\_z start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ; bold\_italic\_θ start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) , roman\_Γ ( bold\_italic\_z , bold\_italic\_θ start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) ), where Γ⁢(𝒛,𝜽)Γ𝒛𝜽\\Gamma(\\bm{z},\\bm{\\theta})roman\_Γ ( bold\_italic\_z , bold\_italic\_θ ) is the Adam update. The training samples with the highest influence scores are selected for fine-tuning. Experiments show that models trained on this subset outperform those trained on full data, and the approach can scale to larger models.

Report issue for preceding element

∙∙\\bullet∙_Kernel-Density Regularization._ Task-Specific Data Selection (TSDS) \[ [270](https://arxiv.org/html/2505.18458v1#bib.bib270 "")\] identifies high-quality pre-training or fine-tuning data for particular tasks by balancing two objectives: (i)𝑖(i)( italic\_i ) distribution alignment with the target task data and (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) diversity to avoid near-duplicates. It accomplishes this via an optimal transport formulation enhanced by kernel density estimation (KDE) regularization. Concretely, one begins with a small set of query examples Q={qi}i=1M𝑄superscriptsubscriptsubscript𝑞𝑖𝑖1𝑀Q=\\{q\_{i}\\}\_{i=1}^{M}italic\_Q = { italic\_q start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT } start\_POSTSUBSCRIPT italic\_i = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_M end\_POSTSUPERSCRIPT (representing the target task) and a large candidate pool D={xj}j=1N𝐷superscriptsubscriptsubscript𝑥𝑗𝑗1𝑁D=\\{x\_{j}\\}\_{j=1}^{N}italic\_D = { italic\_x start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT } start\_POSTSUBSCRIPT italic\_j = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_N end\_POSTSUPERSCRIPT. Both Q𝑄Qitalic\_Q and D𝐷Ditalic\_D are then embedded into a shared metric space (e.g., using gradient-based or semantic embeddings). The optimization for distribution alignment is conducted by solving for probability mass γi⁢jsubscript𝛾𝑖𝑗\\gamma\_{ij}italic\_γ start\_POSTSUBSCRIPT italic\_i italic\_j end\_POSTSUBSCRIPT (transported from qisubscript𝑞𝑖q\_{i}italic\_q start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT to xjsubscript𝑥𝑗x\_{j}italic\_x start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT): minγ∈ℝ≥0M×N⁡αC⁢∑i=1M∑j=1Nγi⁢j⁢di⁢j+(1−α)⁢GKDE⁢(γ)s.t.∑j=1Nγi⁢j=1M,∀i∈\[M\]formulae-sequencesubscript𝛾superscriptsubscriptℝabsent0𝑀𝑁𝛼𝐶superscriptsubscript𝑖1𝑀superscriptsubscript𝑗1𝑁subscript𝛾𝑖𝑗subscript𝑑𝑖𝑗1𝛼subscript𝐺KDE𝛾s.t.superscriptsubscript𝑗1𝑁subscript𝛾𝑖𝑗1𝑀for-all𝑖delimited-\[\]𝑀\\min\_{\\gamma\\in\\mathbb{R}\_{\\geq 0}^{M\\times N}}\\frac{\\alpha}{C}\\sum\_{i=1}^{M}%
\\sum\_{j=1}^{N}\\gamma\_{ij}d\_{ij}+(1-\\alpha)G\_{\\text{KDE}}(\\gamma)\\quad\\text{s.t%
.}\\quad\\sum\_{j=1}^{N}\\gamma\_{ij}=\\frac{1}{M},\\forall i\\in\[M\]roman\_min start\_POSTSUBSCRIPT italic\_γ ∈ blackboard\_R start\_POSTSUBSCRIPT ≥ 0 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_M × italic\_N end\_POSTSUPERSCRIPT end\_POSTSUBSCRIPT divide start\_ARG italic\_α end\_ARG start\_ARG italic\_C end\_ARG ∑ start\_POSTSUBSCRIPT italic\_i = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_M end\_POSTSUPERSCRIPT ∑ start\_POSTSUBSCRIPT italic\_j = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_N end\_POSTSUPERSCRIPT italic\_γ start\_POSTSUBSCRIPT italic\_i italic\_j end\_POSTSUBSCRIPT italic\_d start\_POSTSUBSCRIPT italic\_i italic\_j end\_POSTSUBSCRIPT + ( 1 - italic\_α ) italic\_G start\_POSTSUBSCRIPT KDE end\_POSTSUBSCRIPT ( italic\_γ ) s.t. ∑ start\_POSTSUBSCRIPT italic\_j = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_N end\_POSTSUPERSCRIPT italic\_γ start\_POSTSUBSCRIPT italic\_i italic\_j end\_POSTSUBSCRIPT = divide start\_ARG 1 end\_ARG start\_ARG italic\_M end\_ARG , ∀ italic\_i ∈ \[ italic\_M \], where di⁢jsubscript𝑑𝑖𝑗d\_{ij}italic\_d start\_POSTSUBSCRIPT italic\_i italic\_j end\_POSTSUBSCRIPT is the distance between qisubscript𝑞𝑖q\_{i}italic\_q start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT and xjsubscript𝑥𝑗x\_{j}italic\_x start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT in the metric space, and GKDE⁢(γ)subscript𝐺KDE𝛾G\_{\\text{KDE}}(\\gamma)italic\_G start\_POSTSUBSCRIPT KDE end\_POSTSUBSCRIPT ( italic\_γ ) is the regularization term that adds diversity and penalizes over-density using KDE estimates: GKDE⁢(γ)=M⁢maxi,j⁡ρj⁢\|γi⁢j−1/ρjM⁢∑j′1/ρj′\|subscript𝐺KDE𝛾𝑀subscript𝑖𝑗subscript𝜌𝑗subscript𝛾𝑖𝑗1subscript𝜌𝑗𝑀subscriptsuperscript𝑗′1subscript𝜌superscript𝑗′G\_{\\text{KDE}}(\\gamma)=M\\max\_{i,j}\\rho\_{j}\\left\|\\gamma\_{ij}-\\frac{1/\\rho\_{j}}{%
M\\sum\_{j^{\\prime}}1/\\rho\_{j^{\\prime}}}\\right\|italic\_G start\_POSTSUBSCRIPT KDE end\_POSTSUBSCRIPT ( italic\_γ ) = italic\_M roman\_max start\_POSTSUBSCRIPT italic\_i , italic\_j end\_POSTSUBSCRIPT italic\_ρ start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT \| italic\_γ start\_POSTSUBSCRIPT italic\_i italic\_j end\_POSTSUBSCRIPT - divide start\_ARG 1 / italic\_ρ start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT end\_ARG start\_ARG italic\_M ∑ start\_POSTSUBSCRIPT italic\_j start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT end\_POSTSUBSCRIPT 1 / italic\_ρ start\_POSTSUBSCRIPT italic\_j start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT end\_POSTSUBSCRIPT end\_ARG \|, where ρj=∑x′∈D(1−f(xj,x′)2/h2\\rho\_{j}=\\sum\_{x^{\\prime}\\in D}(1-f(x\_{j},x^{\\prime})^{2}/h^{2}italic\_ρ start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT = ∑ start\_POSTSUBSCRIPT italic\_x start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ∈ italic\_D end\_POSTSUBSCRIPT ( 1 - italic\_f ( italic\_x start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT , italic\_x start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ) start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT / italic\_h start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT is the density estimate for candidate xjsubscript𝑥𝑗x\_{j}italic\_x start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT (higher for near-duplicates). Afterwards, it selects samples by sampling xjsubscript𝑥𝑗x\_{j}italic\_x start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT with probability pj=∑iγi⁢j∗subscript𝑝𝑗subscript𝑖superscriptsubscript𝛾𝑖𝑗p\_{j}=\\sum\_{i}\\gamma\_{ij}^{\*}italic\_p start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT = ∑ start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT italic\_γ start\_POSTSUBSCRIPT italic\_i italic\_j end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ∗ end\_POSTSUPERSCRIPT.

Report issue for preceding element

Model-based Data Selection. These methods aim to determine subsets guided by prompting the LLM itself.

Report issue for preceding element

Autonomous Data Selection (AutoDS) \[ [472](https://arxiv.org/html/2505.18458v1#bib.bib472 "")\] prompts the LLM to assess and select mathematical and educational samples from a larger dataset. For each sample, the LLM is asked two questions: (i)𝑖(i)( italic\_i ) Is it mathematically relevant, and (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) It it educationally valuable. The LLM responds to each question with “Yes” or “No”, and the logit of each response is extracted to compute the LM-Score: LM-Score⁢(⋅)=exp⁡(logit⁢(‘YES’))exp⁡(logit⁢(‘YES’))+exp⁡(logit⁢(‘NO’))LM-Score⋅logit‘YES’logit‘YES’logit‘NO’\\text{LM-Score}(\\cdot)=\\frac{\\exp(\\text{logit}(\\text{\`YES'}))}{\\exp(\\text{%
logit}(\\text{\`YES'}))+\\exp(\\text{logit}(\\text{\`NO'}))}LM-Score ( ⋅ ) = divide start\_ARG roman\_exp ( logit ( ‘YES’ ) ) end\_ARG start\_ARG roman\_exp ( logit ( ‘YES’ ) ) + roman\_exp ( logit ( ‘NO’ ) ) end\_ARG, and the composite score: LM-Score⁢(Q1,Q2)=LM-Score⁢(Q1)⋅LM-Score⁢(Q2)LM-Scoresubscript𝑄1subscript𝑄2⋅LM-Scoresubscript𝑄1LM-Scoresubscript𝑄2\\text{LM-Score}(Q\_{1},Q\_{2})=\\text{LM-Score}(Q\_{1})\\cdot\\text{LM-Score}(Q\_{2})LM-Score ( italic\_Q start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , italic\_Q start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT ) = LM-Score ( italic\_Q start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT ) ⋅ LM-Score ( italic\_Q start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT ). The composite score ranks and selects high-quality math samples.

Report issue for preceding element

#### 2.2.5 Data Mixing

Report issue for preceding element

Since LLMs rely on massive and diverse datasets, the composition of these datasets significantly impacts model performance \[ [296](https://arxiv.org/html/2505.18458v1#bib.bib296 "")\]. For instance, as shown in Figure [3](https://arxiv.org/html/2505.18458v1#S2.F3 "Figure 3 ‣ 2.1 Data Characteristics across LLM Stages ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices"), we can see LLMs require different ratios of domain data to achieve capabilities such as medical diagnosis, coding, and solving math problems. To this end, data mixing refers to the strategy of (1) combining datasets from different domains, sources or structures in specific proportions to train LLMs or (2) making LLMs give different proportions of attention on different domains (e.g., by changing the sampling probabilities) in the training session. Effective data mixing ensures that the model captures broad generalization capabilities while balancing performance across tasks and domains \[ [140](https://arxiv.org/html/2505.18458v1#bib.bib140 "")\]. Existing data mixing methods can be classified into two main categories:

Report issue for preceding element

PrinciplesUnlike traditional ML models like BERT (trained on smaller, domain-specific data with homogeneous distributions), LLMs require massive multilingual or multi-domain corpora, raising the critical challenge of optimizing dataset mixing ratios for performance. Current methods use heuristic experimentation or formulate ratio-performance relationships (e.g., validation loss), but cost-effective determination of optimal ratios, beyond heuristics, remains unresolved due to high cost demands for functional approximations.
Report issue for preceding element

Heuristic Optimization provides empirical data mixing strategies such as setting different ratios of datasets based on various factors (e.g., complexity and diversity of the datasets) that likely improve LLMs’ abilities.

Report issue for preceding element

First, to study the effect of data mixture, there are works that experiment heuristically on different data ratios for pre-training of LLMs. \[ [139](https://arxiv.org/html/2505.18458v1#bib.bib139 "")\] suspects training sequence from simple to complex data would improve LLMs’ performance, thus introduces a two-stage data mixing strategy for LLM pre-training: (1) It first blends web-crawled data with minimal high-quality content (1.9% math, 15% code), testing ratios (<<<35% high-quality) and selecting optimal mixtures via evaluations on CommonsenseQA \[ [376](https://arxiv.org/html/2505.18458v1#bib.bib376 "")\] and HumanEval \[ [96](https://arxiv.org/html/2505.18458v1#bib.bib96 "")\]. (2) It then filters low-quality data, boosting math (24%→29%), code (20%→29%), and instructional alignment data. Ratios are similarly optimized through empirical validation.
The method iteratively refines proportions using down-sampled Megatron-8B \[ [359](https://arxiv.org/html/2505.18458v1#bib.bib359 "")\] for efficiency, then scales findings to a 25B model, balancing diversity-quality tradeoffs with reduced experimental overhead. Similarly, Slimpajama \[ [351](https://arxiv.org/html/2505.18458v1#bib.bib351 "")\] explores the impact of data source diversity and weight distribution on model performance by adjusting the proportions of data from multiple sources, such as Commoncrawl \[ [11](https://arxiv.org/html/2505.18458v1#bib.bib11 "")\], C4 \[ [331](https://arxiv.org/html/2505.18458v1#bib.bib331 "")\], Github \[ [14](https://arxiv.org/html/2505.18458v1#bib.bib14 "")\] .

Report issue for preceding element

Second, we can utilize metrics to judge different datasets and mix them. To calculate the best result rather than just try different combinations, Bimix  \[ [153](https://arxiv.org/html/2505.18458v1#bib.bib153 "")\] adopts entropy metrics (e.g., Shannon entropy \[ [347](https://arxiv.org/html/2505.18458v1#bib.bib347 "")\], conditional entropy \[ [347](https://arxiv.org/html/2505.18458v1#bib.bib347 "")\]) as the quality scores which are then normalized to compute the proportions of each domain (e.g., conditional entropy, written as as Hi⁢(Xi(t+1)∣Xi(t))=−∑x∈Xi(t)∑x′∈Xi(t+1)P⁢(x,x′)⁢log⁡P⁢(x′∣x)subscript𝐻𝑖conditionalsuperscriptsubscript𝑋𝑖𝑡1superscriptsubscript𝑋𝑖𝑡subscript𝑥superscriptsubscript𝑋𝑖𝑡subscriptsuperscript𝑥′superscriptsubscript𝑋𝑖𝑡1𝑃𝑥superscript𝑥′𝑃conditionalsuperscript𝑥′𝑥H\_{i}\\left(X\_{i}^{(t+1)}\\mid X\_{i}^{(t)}\\right)=-\\sum\_{x\\in X\_{i}^{(t)}}\\sum\_{%
x^{\\prime}\\in X\_{i}^{(t+1)}}P(x,x^{\\prime})\\log P(x^{\\prime}\\mid x)italic\_H start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ( italic\_X start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ( italic\_t + 1 ) end\_POSTSUPERSCRIPT ∣ italic\_X start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ( italic\_t ) end\_POSTSUPERSCRIPT ) = - ∑ start\_POSTSUBSCRIPT italic\_x ∈ italic\_X start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ( italic\_t ) end\_POSTSUPERSCRIPT end\_POSTSUBSCRIPT ∑ start\_POSTSUBSCRIPT italic\_x start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ∈ italic\_X start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ( italic\_t + 1 ) end\_POSTSUPERSCRIPT end\_POSTSUBSCRIPT italic\_P ( italic\_x , italic\_x start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ) roman\_log italic\_P ( italic\_x start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ∣ italic\_x ), where Xi(t+1)superscriptsubscript𝑋𝑖𝑡1X\_{i}^{(t+1)}italic\_X start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ( italic\_t + 1 ) end\_POSTSUPERSCRIPTXi(t)superscriptsubscript𝑋𝑖𝑡X\_{i}^{(t)}italic\_X start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT ( italic\_t ) end\_POSTSUPERSCRIPT are sets of tokens at positions t+1𝑡1t+1italic\_t + 1 and t𝑡titalic\_t separately, x𝑥xitalic\_x and x′superscript𝑥′x^{\\prime}italic\_x start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT are tokens belonging to them, P⁢(x,x′)𝑃𝑥superscript𝑥′P(x,x^{\\prime})italic\_P ( italic\_x , italic\_x start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ) is the joint probability, P⁢(x′∣x)𝑃conditionalsuperscript𝑥′𝑥P(x^{\\prime}\\mid x)italic\_P ( italic\_x start\_POSTSUPERSCRIPT ′ end\_POSTSUPERSCRIPT ∣ italic\_x ) is the conditional probability.

Report issue for preceding element

Bilevel Optimization. Bilevel Optimization \[ [109](https://arxiv.org/html/2505.18458v1#bib.bib109 "")\] is a closed-loop optimization technique that ensures model parameters are well optimized. Generally, Bilevel optimization
involves two nested optimization problems:
(1) the inner-level problem ensures model parameters are optimized under given weights (e.g., minimizing weighted training loss), while (2) the outer-level updates weights through backpropagation of validation loss, forming a closed-loop optimization.

Report issue for preceding element

Typically, ScaleBiO \[ [303](https://arxiv.org/html/2505.18458v1#bib.bib303 "")\] reconstructs the data sampling weight optimization problem into a bilevel optimization problem, where outer-level problem is adjusting data weights to minimize validation loss; and the inner-level problem is adjusting model parameters to minimize weighted training loss and it could be applied to tasks like multilingual training (mixture of languages) and instruction following (mixture of quality).
ScaleBio first experiments on small models. Then it extends to larger models like LLaMA-3. ScaleBiO initialize the weights equably for all data sources. In each iteration, it randomly selects a subset of data sources to update their weights: for the selected data sources, it adjusts the weights by optimizing the gradient of the validation loss, prioritizing the increase of weights for data that contribute significantly to model performance, while decreasing the weights for data that have less impact on performance. After updating the weights, retrain the model parameters and repeat the process until convergence.

Report issue for preceding element

To enhance the efficiency of BiO-based data mixing, DoGE \[ [135](https://arxiv.org/html/2505.18458v1#bib.bib135 "")\] defines (i)𝑖(i)( italic\_i ) inner-level problem as that under the condition of fixed data mixing ratios, optimize the proxy model parameters to minimize the weighted sum of domain losses; and (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) outer-level problem as _adjusting the data mixing ratios such that the model parameters obtained through inner-level problem optimization achieve optimal performance on the target loss_. The method is executed on a small-scale proxy by following steps: Initially, it sets the domain weights as a uniform distribution. In each iteration, it dynamically adjusts the weight of each domain based on the gradient alignment value (calculated as the inner product of the gradient of current data domain and the sum of gradients from all data domains), which measures the contribution of the data from the current domain to the gradient direction of all other domains’ data. Using the updated weights, it resamples the data and updates the model parameters. Repeat the process for multiple iterations until the weights stabilize, then apply to actual LLM pre-training.

Report issue for preceding element

TABLE VI: Comparison of Data Mixing Methods for LLM

|     |     |     |     |
| --- | --- | --- | --- |
| Taxonomy | Stage | Methods | Traits |
| Heuristic Optimization | Pre-training | Multi-source Data Adjusting | Intuitive and easy to implement, suitable for rapid experimentation |
| \[ [139](https://arxiv.org/html/2505.18458v1#bib.bib139 "")\], \[ [351](https://arxiv.org/html/2505.18458v1#bib.bib351 "")\] |
| Entropy-Based Mixing \[ [153](https://arxiv.org/html/2505.18458v1#bib.bib153 "")\] | Low computation cost with quality quantification by entropy |
| Bilevel Optimization | Pre-training | Calculate domain contribution by | Requires a proxy model, performances well in OOD datasets |
| gradient inner products\[ [135](https://arxiv.org/html/2505.18458v1#bib.bib135 "")\] |
| Fine-tuning | Dynamically adjust weights by | Multiple applications like multilingual training, |
|  | gradient alignment values \[ [303](https://arxiv.org/html/2505.18458v1#bib.bib303 "")\] | instruction following, large-scale data reweighting |
| Distributionally Robust Optimization | Pre-training | Group DRO \[ [428](https://arxiv.org/html/2505.18458v1#bib.bib428 "")\] | Only need one proxy model compared to \[ [279](https://arxiv.org/html/2505.18458v1#bib.bib279 "")\] |
| which uses a proxy model and a reference model |
| Fine-tuning | Task-level DRO \[ [279](https://arxiv.org/html/2505.18458v1#bib.bib279 "")\] | Performs well with problems caused by significant |
| different loss across datasets |
| Model-Based | Pre-training | Linear Regression Model \[ [264](https://arxiv.org/html/2505.18458v1#bib.bib264 "")\] | Only 10% of DoReMi’s \[ [428](https://arxiv.org/html/2505.18458v1#bib.bib428 "")\] computational resources are required. |
| Supports simultaneous training hundreds of small models to accelerate the optimization |
| Pre-training | Bivariate Data Mixing Law \[ [153](https://arxiv.org/html/2505.18458v1#bib.bib153 "")\] | Avoid iterative training of proxy models, resulting in lower |
| computational costs. Shows relation between loss and training steps additionally |
| Continual Pre-training | Chinchilla Scaling Law \[ [324](https://arxiv.org/html/2505.18458v1#bib.bib324 "")\] | Supports knowledge transfering to new domains, reducing training costs by over 95% |
| Pre-training | Exponential Functions \[ [447](https://arxiv.org/html/2505.18458v1#bib.bib447 "")\] | Supports datasets without explicit domain division. |
| Continual Pre-training | Power-law Function \[ [161](https://arxiv.org/html/2505.18458v1#bib.bib161 "")\] | Compared to \[ [324](https://arxiv.org/html/2505.18458v1#bib.bib324 "")\] which is single-objective optimization |
| essentially, \[ [161](https://arxiv.org/html/2505.18458v1#bib.bib161 "")\] ensures that domain performance improvement |
| does not compromise general capabilities. |
| Pre-training | Classification Model \[ [252](https://arxiv.org/html/2505.18458v1#bib.bib252 "")\] | Reverse engineering for finding the data recipe of LLMs |

Report issue for preceding element

Distributionally Robust Optimization. To search for a robust data mixing strategy (which can be sub-optimal but with low uncertainty), some methods adopt Distributionally Robust Optimization (DRO) for data mixing. DRO achieves robustness against distributional uncertainty by optimizing for the worst-case scenario within a set of distributions (referred to as the uncertainty set or ambiguity set).

Report issue for preceding element

∙∙\\bullet∙ For LLM pre-training, DoReMi \[ [428](https://arxiv.org/html/2505.18458v1#bib.bib428 "")\] defines the worst case as domains where the proxy model underperforms compared to the reference model, which initially sets the domain weights as a uniform distribution and each domains contains several sample sets, and uses it to train Transformer decoder-only LM with 280M parameters and computes loss in each example set, which provides a reference point to measure the improvement potential (the loss difference) of the proxy model in each domain. Next, DoReMi trains a small-scale proxy model (also Transformer decoder-only LM with 280M parameters) by adjusting the domain data weights through DRO, which dynamically adjusts the domain weights and tilt the weights toward domains with larger losses (compared to the reference model). Finally, validate performance of weighted domain data on large models (Transformer decoder-only LM with 8B parameters).

Report issue for preceding element

∙∙\\bullet∙ For LLM fine-tuning, tDRO \[ [279](https://arxiv.org/html/2505.18458v1#bib.bib279 "")\] defines the worst case the same as DoReMi, which computes the relative loss for each domain with a proxy model (e.g. Qwen1.5-0.5B \[ [69](https://arxiv.org/html/2505.18458v1#bib.bib69 "")\]); and they compare the training loss of domain data with the reference model (e.g., Qwen1.5-0.5B), and evaluate each domain’s potential for model improvement, and update the domain weights accordingly, giving more attention to high-loss domains. Finally, the updated weights are normalized to form a new sampling distribution and repeat the process to get final data distribution.

Report issue for preceding element

Model-Based Optimization. This category of methods design linear or non-linear models that depict (i)𝑖(i)( italic\_i ) the relation between the distribution of each domain, (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) validation loss, and (i⁢i⁢i)𝑖𝑖𝑖(iii)( italic\_i italic\_i italic\_i ) some other variables like training steps, based on which they find the optimal settings through various model-based techniques.

Report issue for preceding element

(1) Linear Regression Model: Some methods utilize pairs like data mixtures and corresponding model performance to fit a linear regressing model, such that finding the best data mixture ratios.

Report issue for preceding element

Typically, REGMIX \[ [264](https://arxiv.org/html/2505.18458v1#bib.bib264 "")\] defines the domains by source (like ArXiv, FreeLaw, etc.), which uses Dirichlet distribution (which
controls the distribution of probabilities across multiple categories with a parameter) to generate all kinds of data distribution of several domains to trains small-scale proxy model to collect performance data, which is then used to fit a linear regression model (LightGBM \[ [206](https://arxiv.org/html/2505.18458v1#bib.bib206 "")\]) to predict the optimal data mixing distribution. Then REGMIX uses both the best distribution and the average of top-100 distributions to verify on variations of TinyLlama \[ [466](https://arxiv.org/html/2505.18458v1#bib.bib466 "")\] with additional layers with versions of 1B and 7B.

Report issue for preceding element

(2) Non-linear Regression Model: There are also many methods that design non-linear regression models for data mixing by considering more complex training characters.

Report issue for preceding element

∙∙\\bullet∙ _Bivariate Data Mixing Law._ Based on observations of validation loss changes due to variables like domain proportion (where the data come from different sources like Pile-CC) and training steps, BiMix \[ [153](https://arxiv.org/html/2505.18458v1#bib.bib153 "")\] proposes Bivariate Data Mixing Law that depicts the relation among domain’s proportion, training steps and validation loss, which can be written as Li⁢(ri,s)=Airiαi⁢(Bisβi+Ci)subscript𝐿𝑖subscript𝑟𝑖𝑠subscript𝐴𝑖superscriptsubscript𝑟𝑖subscript𝛼𝑖subscript𝐵𝑖superscript𝑠subscript𝛽𝑖subscript𝐶𝑖L\_{i}\\left(r\_{i},s\\right)=\\frac{A\_{i}}{r\_{i}^{\\alpha\_{i}}}\\left(\\frac{B\_{i}}{s%
^{\\beta\_{i}}}+C\_{i}\\right)italic\_L start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ( italic\_r start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT , italic\_s ) = divide start\_ARG italic\_A start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_ARG start\_ARG italic\_r start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_α start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT end\_ARG ( divide start\_ARG italic\_B start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_ARG start\_ARG italic\_s start\_POSTSUPERSCRIPT italic\_β start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT end\_ARG + italic\_C start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ), where Aisubscript𝐴𝑖A\_{i}italic\_A start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT,Bisubscript𝐵𝑖B\_{i}italic\_B start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT,Cisubscript𝐶𝑖C\_{i}italic\_C start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT are domain-dependent scaling coefficients, αisubscript𝛼𝑖\\alpha\_{i}italic\_α start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT and βisubscript𝛽𝑖\\beta\_{i}italic\_β start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT are power-law exponents that control the influence of domain proportion and training steps respectively, s𝑠sitalic\_s represents the training step count. It utilizes the law to fit the actual data curves by fixing the domain’s proportion or training steps and varies the other one to get validation loss by training a small model (decoder-only transformers based on the DoReMi \[ [427](https://arxiv.org/html/2505.18458v1#bib.bib427 "")\] architecture with 280M parameters). After depicting the relation, we model the task as an optimization problem (resolvable by Lagrange multipliers) and then verify on larger LLM (decoder-only transformers based on the DoReMi \[ [427](https://arxiv.org/html/2505.18458v1#bib.bib427 "")\] architecture with 1B parameters).

Report issue for preceding element

∙∙\\bullet∙ _Chinchilla Scaling Law._ D-CPT \[ [324](https://arxiv.org/html/2505.18458v1#bib.bib324 "")\] establishes a mathematical relationship which could be used to find the best mixture of general and domain-specific data between validation loss, model size, data size, and domain data mixing ratios based on Chinchilla Scaling Law \[ [171](https://arxiv.org/html/2505.18458v1#bib.bib171 "")\] to optimize domain-specific continual pre-training as L⁢(N,D,r)=E+ANα+B⋅rηDβ+C(r+ϵ)γ𝐿𝑁𝐷𝑟𝐸𝐴superscript𝑁𝛼⋅𝐵superscript𝑟𝜂superscript𝐷𝛽𝐶superscript𝑟italic-ϵ𝛾L(N,D,r)=E+\\frac{A}{N^{\\alpha}}+\\frac{B\\cdot r^{\\eta}}{D^{\\beta}}+\\frac{C}{(r+%
\\epsilon)^{\\gamma}}italic\_L ( italic\_N , italic\_D , italic\_r ) = italic\_E + divide start\_ARG italic\_A end\_ARG start\_ARG italic\_N start\_POSTSUPERSCRIPT italic\_α end\_POSTSUPERSCRIPT end\_ARG + divide start\_ARG italic\_B ⋅ italic\_r start\_POSTSUPERSCRIPT italic\_η end\_POSTSUPERSCRIPT end\_ARG start\_ARG italic\_D start\_POSTSUPERSCRIPT italic\_β end\_POSTSUPERSCRIPT end\_ARG + divide start\_ARG italic\_C end\_ARG start\_ARG ( italic\_r + italic\_ϵ ) start\_POSTSUPERSCRIPT italic\_γ end\_POSTSUPERSCRIPT end\_ARG (N𝑁Nitalic\_N is model parameter count, D𝐷Ditalic\_D is training data volume (number of tokens), r𝑟ritalic\_r is domain corpus ratio, E,A,B,C,α,β,γ,η,ϵ𝐸𝐴𝐵𝐶𝛼𝛽𝛾𝜂italic-ϵE,A,B,C,\\alpha,\\beta,\\gamma,\\eta,\\epsilonitalic\_E , italic\_A , italic\_B , italic\_C , italic\_α , italic\_β , italic\_γ , italic\_η , italic\_ϵ are fitting parameters), with a variation which introduces K which describes the difficulty to learn the domain’s knowledge as L⁢(N,D,r)=E+ANα+B⋅rηDβ+C(r+ϵ)γ+FKμ𝐿𝑁𝐷𝑟𝐸𝐴superscript𝑁𝛼⋅𝐵superscript𝑟𝜂superscript𝐷𝛽𝐶superscript𝑟italic-ϵ𝛾𝐹superscript𝐾𝜇L(N,D,r)=E+\\frac{A}{N^{\\alpha}}+\\frac{B\\cdot r^{\\eta}}{D^{\\beta}}+\\frac{C}{(r+%
\\epsilon)^{\\gamma}}+\\frac{F}{K^{\\mu}}italic\_L ( italic\_N , italic\_D , italic\_r ) = italic\_E + divide start\_ARG italic\_A end\_ARG start\_ARG italic\_N start\_POSTSUPERSCRIPT italic\_α end\_POSTSUPERSCRIPT end\_ARG + divide start\_ARG italic\_B ⋅ italic\_r start\_POSTSUPERSCRIPT italic\_η end\_POSTSUPERSCRIPT end\_ARG start\_ARG italic\_D start\_POSTSUPERSCRIPT italic\_β end\_POSTSUPERSCRIPT end\_ARG + divide start\_ARG italic\_C end\_ARG start\_ARG ( italic\_r + italic\_ϵ ) start\_POSTSUPERSCRIPT italic\_γ end\_POSTSUPERSCRIPT end\_ARG + divide start\_ARG italic\_F end\_ARG start\_ARG italic\_K start\_POSTSUPERSCRIPT italic\_μ end\_POSTSUPERSCRIPT end\_ARG (F𝐹Fitalic\_F is a fitting parameter). It fits formula parameters through small-scale experiments to predict performance under different training configurations and find the suitable ratio to minimize the domain validation loss while ensuring the generalization loss does not exceed the specified threshold.

Report issue for preceding element

∙∙\\bullet∙ _Exponential Functions._\[ [447](https://arxiv.org/html/2505.18458v1#bib.bib447 "")\] establishes an exponential relationship between validation loss and data mixing ratios of several domains (e.g., public datasets like Pile-CC, Books3), L⁢(r)=c+k⁢exp⁡(∑iti⁢ri)𝐿𝑟𝑐𝑘subscript𝑖subscript𝑡𝑖subscript𝑟𝑖L({r})=c+k\\exp\\left(\\sum\_{i}t\_{i}r\_{i}\\right)italic\_L ( italic\_r ) = italic\_c + italic\_k roman\_exp ( ∑ start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT italic\_t start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT italic\_r start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ), where L⁢(r)𝐿𝑟L({r})italic\_L ( italic\_r ) is the validation loss, r𝑟{r}italic\_r represents the mixing ratios of different domains, and c𝑐citalic\_c, k𝑘kitalic\_k, and tisubscript𝑡𝑖t\_{i}italic\_t start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT are learnable parameters. That is, it experiments on a small model with the exponential relationships to predict the best data domain mixing ratios on LLM performance with scaling laws, which combines training step scaling laws (L⁢(S)=c+k⁢Sα𝐿𝑆𝑐𝑘superscript𝑆𝛼L(S)=c+kS^{\\alpha}italic\_L ( italic\_S ) = italic\_c + italic\_k italic\_S start\_POSTSUPERSCRIPT italic\_α end\_POSTSUPERSCRIPT, where S𝑆Sitalic\_S is the number of training steps, and α𝛼\\alphaitalic\_α is a fitting parameter.), which is used to infer the validation loss at target training steps from results at smaller steps, and model size scaling laws (L⁢(N)=c+k⁢Nβ𝐿𝑁𝑐𝑘superscript𝑁𝛽L(N)=c+kN^{\\beta}italic\_L ( italic\_N ) = italic\_c + italic\_k italic\_N start\_POSTSUPERSCRIPT italic\_β end\_POSTSUPERSCRIPT, where N𝑁Nitalic\_N is the number of model parameters, and β𝛽\\betaitalic\_β is a fitting parameter), which is used to infer the validation loss for large model sizes from smaller model sizes.

Report issue for preceding element

∙∙\\bullet∙ _Classification Model._\[ [252](https://arxiv.org/html/2505.18458v1#bib.bib252 "")\] aims to find the data proportion of closed-source model by data proportion detection, which first generating large-scale data from the LLM, then using a classification model to categorize the generated data and compute perplexity, deriving the proportions of pre-training data based on the Data Mixing Law (which is a mathematical formula describing the relationship between the proportion of pre-training data and the model’s loss in different domains.).

Report issue for preceding element

∙∙\\bullet∙ _Power-law Function._ CMR \[ [161](https://arxiv.org/html/2505.18458v1#bib.bib161 "")\] aims to optimize the continual pre-training by finding the best ratio of generic dataset and domain-specific dataset. Based on the research before and the data observed on different sizes of models with different ratios of data, the relationships between loss and mixture ratio, and training volume fit in power-law forms, which are described as L⁢(R)=α⋅Rs+β𝐿𝑅⋅𝛼superscript𝑅𝑠𝛽L(R)=\\alpha\\cdot R^{s}+\\betaitalic\_L ( italic\_R ) = italic\_α ⋅ italic\_R start\_POSTSUPERSCRIPT italic\_s end\_POSTSUPERSCRIPT + italic\_β and L⁢(T)=α1⋅Ts1+β1𝐿𝑇⋅subscript𝛼1superscript𝑇subscript𝑠1subscript𝛽1L(T)=\\alpha\_{1}\\cdot T^{s\_{1}}+\\beta\_{1}italic\_L ( italic\_T ) = italic\_α start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT ⋅ italic\_T start\_POSTSUPERSCRIPT italic\_s start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT end\_POSTSUPERSCRIPT + italic\_β start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT, where α𝛼\\alphaitalic\_α, β𝛽\\betaitalic\_β, s𝑠sitalic\_s, α1subscript𝛼1\\alpha\_{1}italic\_α start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT, β1subscript𝛽1\\beta\_{1}italic\_β start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT and s1subscript𝑠1s\_{1}italic\_s start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT are fitting parameters. Based the relationships, they propose a metric _Critical Mixture Ratio_, which is the maximum data mixing ratio that balances between (1) significantly reducing domain loss while (2) keeping the increase in general loss within a pre-defined tolerance range.
Based on the two aspects, the ratio is defined as R∗=max⁡{R∣R∈F}superscript𝑅conditional𝑅𝑅𝐹R^{\*}=\\max\\{R\\mid R\\in F\\}italic\_R start\_POSTSUPERSCRIPT ∗ end\_POSTSUPERSCRIPT = roman\_max { italic\_R ∣ italic\_R ∈ italic\_F }, where R𝑅Ritalic\_R is the ratio of generic dataset and domain-specific dataset, F𝐹Fitalic\_F is feasible mixture ratios which comprises all mixing proportions that satisfy the constraints of the general loss function.

Report issue for preceding element

#### 2.2.6 Data Distillation and Synthesis

Report issue for preceding element

Synthetic data, which mimics real-world scenarios, is particularly valuable for resolving problems such as (i)𝑖(i)( italic\_i ) data scarcity (e.g., augmenting data for a small dataset) \[ [434](https://arxiv.org/html/2505.18458v1#bib.bib434 "")\], (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) privacy concerns (e.g., replacing sensitive data with synthesis data) \[ [426](https://arxiv.org/html/2505.18458v1#bib.bib426 "")\], (i⁢i⁢i)𝑖𝑖𝑖(iii)( italic\_i italic\_i italic\_i ) the need for diverse and high-quality datasets (e.g., generating examples for underrepresented cases) \[ [261](https://arxiv.org/html/2505.18458v1#bib.bib261 "")\], (i⁢v)𝑖𝑣(iv)( italic\_i italic\_v ) lack of reasoning data (e.g., for code, chain of thought), (v)𝑣(v)( italic\_v ) human alignment (e.g., label better LLM’s response by human beings or LLMs).

Report issue for preceding element

PrinciplesTraditional ML methods use rule-based templates, basic augmentation (lexical substitution, back-translation), or statistical models to create limited synthetic data, addressing data scarcity/class imbalance. While LLM-driven synthesis employs LLMs to produce diverse, high-quality data, tackling data scarcity, privacy concerns, and diverse training needs. Key paradigms include: (i) sample-driven generation, (ii) domain-aligned synthesis, and (iii) reasoning-centric formatting. Challenges involve ensuring rigorous reasoning chain synthesis and optimizing cost-quality balance in data production.Report issue for preceding element

Despite the advantages, synthetic data can negatively impact LLM training, such as when characteristics like toxicity are inherited from the source model or even amplified \[ [356](https://arxiv.org/html/2505.18458v1#bib.bib356 "")\]. Thus, it is vital to design data synthesis methods for LLMs\[ [501](https://arxiv.org/html/2505.18458v1#bib.bib501 "")\]. As shown in Figure [4](https://arxiv.org/html/2505.18458v1#S2.F4 "Figure 4 ‣ 2.1 Data Characteristics across LLM Stages ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices"), we discuss methods dealing these problem through the diverse LLM stages, including pre-Training, SFT, Reinforcement Learning and RAG.

Report issue for preceding element

Knowledge Distillation. Due to LLMs’ massive parameter scale and high resource demands which make practical deployment challenging, so we utilize knowledge distillation (such as designing paradigms to prompt LLM to generate high-quality data) to training a student LLM with less parameters to mimic the target model’s generation ability.

Report issue for preceding element

∙∙\\bullet∙ _Task-Specific Prompt Distillation._ To significantly reduce inference costs and latency while maintaining performance,
\[ [357](https://arxiv.org/html/2505.18458v1#bib.bib357 "")\] employs task-specific prompts: (1)
Chain-of-Density (CoD): Iteratively adds entities to summarize for enhanced density.
(2) Chain-of-Thought (CoT): Guides reasoning tasks (e.g., math) through stepwise logic.
Using GSM8K \[ [107](https://arxiv.org/html/2505.18458v1#bib.bib107 "")\] data and Llama-3.1-405B-Instruct, synthetic data is generated for fine-tuning smaller models (Llama-3.1-8B/70B-Instruct) paired with simplified prompts, balancing efficiency and task specialization.

Report issue for preceding element

∙∙\\bullet∙ _Code Verification and Error Correction Distillation._ Existing knowledge distillation methods (e.g., Chain-of-Thought Fine-tuning) rely on synthetic data generated by LLMs, but such data often contains incorrect intermediate reasoning steps which can mislead small models during learning, hindering the improvement of their reasoning capabilities.

Report issue for preceding element

Pad \[ [502](https://arxiv.org/html/2505.18458v1#bib.bib502 "")\] proposes Program-aided Distillation (PaD) to address error-prone synthetic data in knowledge distillation with
(i) Programmatic Reasoning: LLMs generate executable code (e.g., math problems as Python calculations) instead of natural language CoT, with Python compilers auto-filtering logic errors.
(ii) Error-Injection Training: Models learn error correction by fixing synthetically injected AST-based errors (e.g., NameError).
(iii) Semantic Validation: Decoding selects steps via semantic alignment scoring (e.g., cosine similarity) to prevent error propagation.
PaD replaces flawed CoT steps with verifiable program logic, enhancing small models’ reasoning robustness through code-based distillation and self-correction mechanisms.

Report issue for preceding element

∙∙\\bullet∙ _Multi-stage Collaboration Distillation Between Student models._
In domains with high annotation costs (e.g., biomedical parsing) or complex task structures (e.g., syntactic/semantic parsing), labeled data is extremely scarce, making traditional supervised fine-tuning ineffective.
MCKD \[ [474](https://arxiv.org/html/2505.18458v1#bib.bib474 "")\] introduces Multi-stage Collaborative KD (MCKD) for low-resource generation as 3 steps.
(i) Initialization: GPT-3.5 generates pseudo-labels for unlabeled data.
(ii) Collaborative Distillation:
Splits data into two subsets for cross-labeling via paired T5-Base models, reducing noise overfitting.
Iteratively refines labels over 3 iterations.
(iii) Final Training: Trains a single model on refined labels.
Achieves near-supervised performance with 50 labeled examples (vs. 500 required traditionally) through multi-stage noise reduction and collaborative pseudo-label optimization.

Report issue for preceding element

Pre-training Data Augmentation. The pre-training stage of LLM requires a vast amount of data and it can be costly to synthesize such data with powerful models like GPT-4. Therefore, there are techniques like distillation \[ [487](https://arxiv.org/html/2505.18458v1#bib.bib487 "")\], or simply mixing synthetic data into the whole corpus.

Report issue for preceding element

∙∙\\bullet∙ _Distilled LLM for Mathematical Data Synthesis._
JiuZhang3.0 \[ [487](https://arxiv.org/html/2505.18458v1#bib.bib487 "")\] proposes an LLM-based synthesis method for high-quality math problems:
(i) Model Distillation, fine-tunes DeepSeekMath-7B on GPT-4-generated QA pairs (with curated prompts and math texts) to mimic GPT-4’s generation.
(ii) Uses gradient similarity to prioritize task-relevant data.
(iii) Refines the model with filtered data to produce aligned outputs.
The final math synthetic corpus are generated by the refined model based on the multi-source corpus (e.g., Wikipedia) and prompt sets.

Report issue for preceding element

∙∙\\bullet∙ _Fintuned LLM for Instruction-Response Pair Synthesis._ In order to study the effect of supervised pre-training,
Instruction PT \[ [100](https://arxiv.org/html/2505.18458v1#bib.bib100 "")\] introduces an Instruction Synthesizer (Mistral-7B finetuned on 40+ task categories) to augment raw text with few-shot multi-task instructions (e.g., ”Summarize school activities” → QA/reasoning pairs). Unlike GPT-style pre-training, it integrates structured task execution (QA, classification) alongside language modeling. This hybrid approach boosts data efficiency (500M model ≈\\approx≈ 1B baseline) and multi-task adaptability from pre-training.

Report issue for preceding element

∙∙\\bullet∙ _LLM Prompting for Mathematical Data Synthesis._
Current math-specialized LLMs rely on SFT with problem-solving data (e.g., step-by-step solutions). However, since CPT improvements in math are far less significant than SFT gains.

Report issue for preceding element

To study the impact of problem-solving data in continual pre-training, \[ [99](https://arxiv.org/html/2505.18458v1#bib.bib99 "")\] proposes enhancing models’ mathematical reasoning capabilities by augmenting problem-solving data (e.g., step-by-step solutions for common math problems) during pre-training, rather than relying solely on traditional math corpora (e.g., theorem texts). First, a student model (Llama2 \[ [392](https://arxiv.org/html/2505.18458v1#bib.bib392 "")\]) is utilized to generate answers from the collected math problems. Then, it uses a teacher model (Llama2 \[ [392](https://arxiv.org/html/2505.18458v1#bib.bib392 "")\] with more parameters) detects errors in a student model’s solutions and generates corrective steps guided by prompts. This teaches the target LLM self-checking and error-correction skills. Experiments indicate continual pre-training excels at learning complex reasoning (e.g., multi-step equation solving) than SFT, where MathGPT-8B using only 100B well-generated math-related tokens can exhibit capabilities comparable to Qwen2-Math-72B \[ [442](https://arxiv.org/html/2505.18458v1#bib.bib442 "")\].

Report issue for preceding element

∙∙\\bullet∙ _LLM Prompting for Rephrasing Synthesis._ To introduce more diversity to the data, some methods rephrase the data to different styles of texts like Q&A or concise definition.
WRAP \[ [283](https://arxiv.org/html/2505.18458v1#bib.bib283 "")\] leverages instruction-tuned models (e.g., Mistral-7B) to rephrase web text (C4) into four formats:
(i) simple vocabulary and sentence structures that are understandable to young children.
(ii) Standardized encyclopedia-style expression.
(iii) Complex terminology and concise academic sentence structures.
(iv) multi-turn dialogue.
Mixing rephrased and original data trains LLMs to adapt to diverse formats (e.g., zero-shot QA), achieving 3× faster training and 50% lower perplexity on Pile benchmark \[ [150](https://arxiv.org/html/2505.18458v1#bib.bib150 "")\] via hybrid real-synthetic data synergy.

Report issue for preceding element

∙∙\\bullet∙ _LLM Prompting for Cross-language Synthesis._ LLMs like Llama-3 exhibit deficiencies in cross-language tasks and multidisciplinary scientific reasoning, while continual pre-training often triggers catastrophic forgetting (e.g., performance degradation in original capabilities like English tasks). \[ [93](https://arxiv.org/html/2505.18458v1#bib.bib93 "")\] proposes to synthesize data so as to enhance Llama-3’s Chinese proficiency and scientific reasoning capabilities while mitigating catastrophic forgetting. They utilize Mistral-7B \[ [189](https://arxiv.org/html/2505.18458v1#bib.bib189 "")\] to generate multidisciplinary scientific question-answer pairs (e.g., Q&A on “explaining the electrostatic repulsion principle of ion double layers in electrolyte solutions”) from seed data collected and classified into multiple disciplines by TinyBERT \[ [196](https://arxiv.org/html/2505.18458v1#bib.bib196 "")\] and BERT-Tiny-Chinese \[ [23](https://arxiv.org/html/2505.18458v1#bib.bib23 "")\] from Dolma’s CC \[ [366](https://arxiv.org/html/2505.18458v1#bib.bib366 "")\] and C4 \[ [120](https://arxiv.org/html/2505.18458v1#bib.bib120 "")\]. And generate coding problems with LeetCode algorithm tasks as seeds by Magicoder-S-DS-6.7B \[ [416](https://arxiv.org/html/2505.18458v1#bib.bib416 "")\] .These are mixed with Chinese, English, and synthetic data in a 1:7:2 ratio, significantly boosting scientific reasoning.

Report issue for preceding element

Additionally, through substitution experiments (validating data strategies using TinyLlama-1.1B \[ [466](https://arxiv.org/html/2505.18458v1#bib.bib466 "")\] as a proxy model), they find that (1) a 20% synthetic data ratio with an error rate below 30% yields optimal results; and (2) a curriculum progressing from simple to complex topics outperforms random training.

Report issue for preceding element

∙∙\\bullet∙ _Code Interpreter + LLM Prompting for Code Synthesis._ Current code generation models rely heavily on large teacher models (e.g., GPT-4) to generate synthetic training data, leading to poor scalability, high costs. And most datasets focus on direct code completion or text-to-code translation, but lack Input-Output (I/O) case-based reasoning tasks (e.g., inferring code from example mappings like “hello” →→\\rightarrow→ “olleh”).
This gap results in weak generalization for inductive programming challenges.

Report issue for preceding element

To bridge this gap, Case2Code \[ [348](https://arxiv.org/html/2505.18458v1#bib.bib348 "")\] generates training data through four steps: (i) Extract executable Python functions (with input/output parameters) from open-source repositories; (ii) Use lightweight LLMs (e.g., InternLM2-7B) to analyze function logic and generate diverse input samples; (iii) Execute functions to obtain real outputs and filter invalid results; (iv) Convert I/O pairs into natural language prompts with diversified templates for improved generalization. This method leverages ”code interpreter + lightweight LLM” to cost-effectively produce 1.3M training samples, eliminating reliance on expensive teacher models.

Report issue for preceding element

∙∙\\bullet∙ _LLM-based Clustering for Synthetic Data Evaluation._ In order to study the impact of diversity of large-scale synthetic data, \[ [92](https://arxiv.org/html/2505.18458v1#bib.bib92 "")\] introduces an LLM-based clustering method to quantify synthetic data diversity and analyze its impact on model performance. (i) Builds hierarchical topic trees from web-crawled data via GPT-4 (e.g., Quantum Computing → Qubit Types → Superposition); (ii) Generates diverse datasets by varying topics, prompts (styles, target audiences, etc.) and LLMs (GPT-4o, Llama-3, etc.). Experiments across different diversity combinations show synthetic data diversity positively correlates with model performance on benchmarks like HellaSwag \[ [456](https://arxiv.org/html/2505.18458v1#bib.bib456 "")\] and ARC-Challenge \[ [142](https://arxiv.org/html/2505.18458v1#bib.bib142 "")\].

Report issue for preceding element

∙∙\\bullet∙ _LLM Prompting for Multimodal Image-Text Synthesis._ Current approaches for synthesizing multimodal pre-training data typically employ two main approaches: (1) the generation of images conditioned on textual input using text-to-image models, and (2) the augmentation of uncaptioned or simple-captioned source images via multimodal models.
In the domain of text-to-image synthesis, current methods use diffusion models \[ [145](https://arxiv.org/html/2505.18458v1#bib.bib145 "")\] for image generation.
Examples include DiffuseMix \[ [186](https://arxiv.org/html/2505.18458v1#bib.bib186 "")\], which enhances datasets by augmenting image samples through the blending of original and diffusion-generated images, and EDA \[ [393](https://arxiv.org/html/2505.18458v1#bib.bib393 "")\], which applies diffusion models to produce variations of real images that retain semantic consistency while augmenting the dataset.
Concerning image captioning, several studies focus on improving the quality of image-text pairs. LaCLIP \[ [133](https://arxiv.org/html/2505.18458v1#bib.bib133 "")\] uses ChatGPT to rewrite existing captions, thereby introducing greater diversity in linguistic expression while maintain the core semantic content. A limitation of this method is the potential for visual semantic loss due to the language model’s lack of direct access to the image. To mitigate this, VeCLIP \[ [223](https://arxiv.org/html/2505.18458v1#bib.bib223 "")\] incorporates a multimodal LLM (LLaVA) to provide a detailed visual description of the image contents (e.g., color and shape attributes, objects, and relations among objects). This description is then fused with the original caption by a LLM to yield a more comprehensive final caption.
To simultaneously synthesize both image and text samples, CtrlSynth \[ [83](https://arxiv.org/html/2505.18458v1#bib.bib83 "")\] proposes a system comprising three modules: the Florence-large \[ [425](https://arxiv.org/html/2505.18458v1#bib.bib425 "")\] vision tagging model to extract basic visual elements of an image (e.g., color and shape attributes, objects, and relations among objects), the Qwen2-7B-Instruct \[ [442](https://arxiv.org/html/2505.18458v1#bib.bib442 "")\] language model to generate synthetic text which meets the requirements in the instruction, and the stable-diffusion-x1-base-1.0 \[ [315](https://arxiv.org/html/2505.18458v1#bib.bib315 "")\] text-to-image model to generate novel and diverse image samples based on text prompts.

Report issue for preceding element

SFT Data Augmentation. The SFT stage of LLM training mainly focus on improvement of specific domains (math, medicine, etc.), aligning LLM’s knowledge to instructions, enhancing reasoning ability, etc. Current methods take LLMs as the main method to generate data with some designed frameworks. Many works \[ [180](https://arxiv.org/html/2505.18458v1#bib.bib180 ""), [261](https://arxiv.org/html/2505.18458v1#bib.bib261 ""), [291](https://arxiv.org/html/2505.18458v1#bib.bib291 "")\] take existed datasets as seeds to synthesize mimic datasets.

Report issue for preceding element

∙∙\\bullet∙ _LLM-based Knowledge and Q&A Pairs Synthesis._
To enrich or enhance the diversity of data for better model performance, there are various prompt frameworks such as building topic taxonomy \[ [234](https://arxiv.org/html/2505.18458v1#bib.bib234 "")\] and iterative synthesis \[ [180](https://arxiv.org/html/2505.18458v1#bib.bib180 "")\].

Report issue for preceding element

For example, to cover various domains of human knowledge,
GLAN \[ [234](https://arxiv.org/html/2505.18458v1#bib.bib234 "")\] introduces a knowledge-classification framework for synthetic text generation by GPT-4. (i) Organize knowledge domains (natural sciences/humanities) into disciplines (math/programming) by; (ii) Develop course outlines with units (e.g., ”Intro to Calculus”) and core concepts (e.g., ”Limits”); (iii) Use GPT-4 to create diverse questions by combining concepts, then generate answers with faster GPT-3.5. This structured approach ensures systematic coverage of knowledge areas while balancing generation quality and efficiency.

Report issue for preceding element

Though this could enhance understanding of LLM about many domains, but to get better enhancement still needs to focus on one aspect, like math,
KPDDS \[ [180](https://arxiv.org/html/2505.18458v1#bib.bib180 "")\] identifies mathematical problem themes (e.g., algebra, geometry) and core skills (e.g., factoring) using GPT-4, then constructs a matrix mapping theme co-occurrence probabilities to guide logical problem generation. GPT-4 synthesizes new questions based on these themes and solutions, which are evaluated for quality (clarity, coherence) and refined via GPT-4 voting. The method further diversifies questions through variations and applies iterative voting to optimize output. This structured approach ensures contextually coherent, avoiding random combinations.

Report issue for preceding element

Instead of combining elements like KPDDS (e.g., combining algebra and geometry to synthesize problems),
MMIQC \[ [261](https://arxiv.org/html/2505.18458v1#bib.bib261 "")\] enhances mathematical reasoning by iteratively generating complex, diverse problems from existing ones for fine-tuning. Using a seed dataset, GPT-4 creates problems via added constraints, variables, or extended reasoning. A filtering mechanism ensures logical consistency, problem-solution alignment, and correctness, with validated data expanding the dataset iteratively.

Report issue for preceding element

∙∙\\bullet∙ _LLM-based Alignment Data Augmentation._ Domain knowledge is one thing, and lead LLM’s knowledge align with instruction is another thing that could be done to get better performance through techniques like few-shot prompting.

Report issue for preceding element

AgentInstruct \[ [291](https://arxiv.org/html/2505.18458v1#bib.bib291 "")\] uses LLMs to create scalable, diverse Q&\\&&A data. GPT-4 converts raw input (text/code) into structured formats (argument passages, API lists) to enable diverse instruction creation. Multiple GPT-4 agents generate varied task instructions and answers following a detailed taxonomy (e.g., reading comprehension, coding tasks). GPT-4 and Claude-3 then refine tasks by adding complexity (e.g., integrating dense context or escalating difficulty), ensuring high-quality, adaptable outputs.

Report issue for preceding element

Similarly, SELF-INSTRUCT \[ [408](https://arxiv.org/html/2505.18458v1#bib.bib408 "")\] aligns LLM’s knowledge to prompts by generating task instructions and examples: Starting with a small set of manually written seed tasks, a LLM (e.g., GPT-3) is prompted to generate new task instructions covering various task types, such as classification, question-answering, and generation. Next, different strategies are employed to generate inputs and outputs based on the task type. For instance, for classification tasks, possible class labels (e.g., ”positive” and ”negative”) are generated first, followed by inputs corresponding to each label. For open-ended tasks, a question description is generated first, followed by an answer. The generated data undergoes multiple rounds of filtering, including removing duplicates or invalid data and ensuring input-output alignment.

Report issue for preceding element

TABLE VII: Data Synthesis for LLM.

|     |     |     |
| --- | --- | --- |
| Stage | Category | Methods |
| Distillation | Reasoning Augmentation | Cot \[ [357](https://arxiv.org/html/2505.18458v1#bib.bib357 "")\] |
| Prompt with Tools \[ [502](https://arxiv.org/html/2505.18458v1#bib.bib502 "")\] |
| Data Augmentation | Prompt with Multi-Agent \[ [474](https://arxiv.org/html/2505.18458v1#bib.bib474 "")\] |
| Pre-Training | Data Augmentation | Distillation + Fine Tuning + Prompt \[ [487](https://arxiv.org/html/2505.18458v1#bib.bib487 "")\] |
| Prompt \[ [100](https://arxiv.org/html/2505.18458v1#bib.bib100 "")\], \[ [99](https://arxiv.org/html/2505.18458v1#bib.bib99 "")\], \[ [283](https://arxiv.org/html/2505.18458v1#bib.bib283 "")\], \[ [93](https://arxiv.org/html/2505.18458v1#bib.bib93 "")\],\[ [348](https://arxiv.org/html/2505.18458v1#bib.bib348 "")\], \[ [92](https://arxiv.org/html/2505.18458v1#bib.bib92 "")\] |
| SFT | Data Augmentation | Prompt \[ [234](https://arxiv.org/html/2505.18458v1#bib.bib234 "")\], \[ [180](https://arxiv.org/html/2505.18458v1#bib.bib180 "")\], \[ [261](https://arxiv.org/html/2505.18458v1#bib.bib261 "")\], \[ [291](https://arxiv.org/html/2505.18458v1#bib.bib291 "")\] |
| Reasoning Augmentation | Prompt \[ [179](https://arxiv.org/html/2505.18458v1#bib.bib179 "")\], \[ [174](https://arxiv.org/html/2505.18458v1#bib.bib174 "")\], \[ [350](https://arxiv.org/html/2505.18458v1#bib.bib350 "")\] |
| Human Label \[ [254](https://arxiv.org/html/2505.18458v1#bib.bib254 "")\] |
| Automated Label \[ [406](https://arxiv.org/html/2505.18458v1#bib.bib406 "")\] |
| High Quality Reasoning Data \[ [450](https://arxiv.org/html/2505.18458v1#bib.bib450 "")\], \[ [231](https://arxiv.org/html/2505.18458v1#bib.bib231 "")\] |
| RL | Prompts Optimization | Prompt \[ [408](https://arxiv.org/html/2505.18458v1#bib.bib408 "")\] |
| Human Feedback | RLHF \[ [71](https://arxiv.org/html/2505.18458v1#bib.bib71 "")\] |
| RLHF By LLM \[ [482](https://arxiv.org/html/2505.18458v1#bib.bib482 "")\] |
| RAG | Privacy Protection | Prompt \[ [457](https://arxiv.org/html/2505.18458v1#bib.bib457 "")\] |

Report issue for preceding element

SFT Reasoning Data Augmentation. Synthesize reasoning data (e.g., code, chain of thought) through techniques like Chain-of-thought(CoT), or utilizing verification tools for more rigorous reasoning.

Report issue for preceding element

∙∙\\bullet∙ _Prompting LLM To Math Reasoning With Verify Tool._ Also for math, MUSTARD \[ [179](https://arxiv.org/html/2505.18458v1#bib.bib179 "")\] utilizes mathematical proof tools to get reasoning enhancement. First, fundamental concepts from the field of mathematics are selected as seeds, and GPT-4 generates corresponding problems through two types of solutions: (1) One is a natural language explanation of the reasoning process, and (2) the other is a formal language solution that can be verified (e.g., code compatible with mathematical proof tools). Next, formal solutions are verified using mathematical proof tools to ensure the correctness of the reasoning and answers. For content that fails verification, the model adjusts based on feedback and re-verifies until a correct result is generated.

Report issue for preceding element

∙∙\\bullet∙ _CoT Data Synthesis By LLM Exploring._ Works mentioned above highly rely GPT-4 for its advanced ability for math to generate problems and solutions to fine-tune for higher reasoning ability. While more recent research try to enhance LLMs’ reasoning ability by technique like Chain-of-Thought (CoT, which let LLMs use tokens to output their reasoning steps) and synthesis or label finer reasoning data for training.

Report issue for preceding element

By generating CoT data that covers a wide range of reasoning paths through a trial-and-error self-verification loop, \[ [174](https://arxiv.org/html/2505.18458v1#bib.bib174 "")\] breaks the traditional limitation of relying solely on correct reasoning paths. Specifically, multiple LLMs (e.g., Qwen-7B, Llama-3-8B) are utilized to generate diverse solutions for the same mathematical problem (20-50 responses per problem) to encourage models to explore incorrect paths (e.g., wrong formulas, logical leaps) while retaining complete error analysis. Then a verifier LLM (e.g., GPT-4) performs critical analysis on each response:
(a) For incorrect paths, annotate the error steps and generate correction suggestions (e.g., “Step 3 misapplies the cosine theorem, which should be replaced with the Pythagorean theorem”).
(b) For correct paths, extract key reasoning steps to form a concise CoT.
Merge corrected incorrect attempts with correct paths to construct multi-branch CoT.

Report issue for preceding element

Similarly, Satori \[ [350](https://arxiv.org/html/2505.18458v1#bib.bib350 "")\] introduces Chain-of-Action-Thought (COAT), a reasoning framework with meta-action tokens (Continue / Reflect / Explore) enabling dynamic pauses, logic verification, and strategy shifts with a two-stage pipeline: (i) Multiple LLM agents generate COAT-formatted reasoning chains to fine-tune a base model for COAT-formatted syntax mastery. (ii) Partial rollbacks (≤\\leq≤5 steps) from historical reasoning (correct/incorrect paths) append <<<reflect>>> to trigger revised reasoning with reinforcement learning (RL) combined with rewards for answer correctness, error correction, and penalties for failures. The RL-enhanced model is distilled into base models (e.g., Llama8B) for iterative refinement.

Report issue for preceding element

These works propose framework by letting LLM reason by themselves, and we also have works that label reasoning data for fine tuning to get reasoning ability.

Report issue for preceding element

∙∙\\bullet∙ _Reasoning Data Labeling._\[ [254](https://arxiv.org/html/2505.18458v1#bib.bib254 "")\] compares the effects of outcome supervision (provides feedback based solely on the correctness of the final answer) and process supervision (provides feedback for each step in the reasoning process) on mathematical reasoning tasks by comparing manually labeling the reasoning steps generated by GPT-4 with outcome supervision. The results showed that process supervision model achieved significantly higher problem-solving accuracy (78.2%) compared to outcome supervision model (72.4%)

Report issue for preceding element

But this would cost too much manual effort, so MATH-SHEPHERD  \[ [406](https://arxiv.org/html/2505.18458v1#bib.bib406 "")\] proposes a method to automatically generate process-annotated data for training Process Reward Models (PRM, which evaluate the quality of each reasoning step). First, complete the remaining reasoning and answers multiple times for the initially generated reasoning steps with LLM, then each step is scored based on two metrics:
(1) Hard Estimation (whether the correct answer is generated, with values of 0 or 1).
(2) Soft Estimation (the proportion of correct answers generated through this step).
These scores assess the step’s ability to derive the correct answer.

Report issue for preceding element

∙∙\\bullet∙ _High Quality and Well Format Data Are The Keys To Better Reasoning._ Moreover, LIMO \[ [450](https://arxiv.org/html/2505.18458v1#bib.bib450 "")\] and \[ [231](https://arxiv.org/html/2505.18458v1#bib.bib231 "")\] state that high quality and well-formatted reasoning data are keys to high performance. \[ [450](https://arxiv.org/html/2505.18458v1#bib.bib450 "")\] emphasizes stimulating complex reasoning capabilities in LLMs through a small number of high-quality training examples with questions and reasoning chains.
Powerful models (such as R1, DeepSeek-R1-Distill-Qwen32B) are used for evaluation and synthesis, retaining problems that remain challenging. Each problem is accompanied by detailed solutions and reasoning chains (from official solutions, expert solutions, and LLMs-generated Cot, etc.) and filtered by rules-based and LLM-assisted methods.

Report issue for preceding element

\[ [231](https://arxiv.org/html/2505.18458v1#bib.bib231 "")\] finds that the overall structure of the reasoning steps is more important than the specific content. With problems from Numina-Math \[ [236](https://arxiv.org/html/2505.18458v1#bib.bib236 "")\] etc. and long CoT generated by DeepSeek-R1 \[ [163](https://arxiv.org/html/2505.18458v1#bib.bib163 "")\] and QwQ-32B-Preview \[ [384](https://arxiv.org/html/2505.18458v1#bib.bib384 "")\] as data to fine-tune. With modification of the fine-tune data, reveals that training the model with incorrect answer samples results in an accuracy drop of only 3.2% compared to training with correct samples. However, shuffling 67% of the reasoning steps in the training samples leads to a 13.3% drop in accuracy on AIME 2024 problems relative to training with correct samples.

Report issue for preceding element

Reinforcement Learning The RL stage of LLMs find the most human-preferential responses within the multiple responses generated by LLM of one instruction. Works like \[ [71](https://arxiv.org/html/2505.18458v1#bib.bib71 ""), [482](https://arxiv.org/html/2505.18458v1#bib.bib482 "")\] manually label the responses or let LLMs do the job.

Report issue for preceding element

Label better LLM’s response by human or LLMs. To align the model’s responses with human expectations, \[ [71](https://arxiv.org/html/2505.18458v1#bib.bib71 "")\] gathers helpful and harmless data through open-ended conversations. Then, a preference model is trained to score the responses in the data, providing a basis for reward optimization in reinforcement learning. The preference scores guide the optimization of the language model’s responses. Next, the latest model generates new data, continuously updating the preference model to improve performance on high-quality data. To improve efficiency, \[ [482](https://arxiv.org/html/2505.18458v1#bib.bib482 "")\] proposes a new chatbot evaluation method using language models as ”judges” to compare and score chatbot responses, with the goal of automating the evaluation process and reducing human involvement. It introduces two benchmarks: one focusing on multi-turn conversation performance and another collecting user preferences via crowdsourcing. The method also addresses potential biases, such as preferences for answer order or length, through strategies like swapping answers, using few-shot examples or Chain-of-Thought. The approach demonstrates that language models can achieve high consistency with human evaluators, providing a scalable and interpretable framework for efficient chatbot assessment.

Report issue for preceding element

Retrieval-Augmentation Generation. The RAG stage mainly offers knowledge and documents from outside to avoid additional training cost. Main works in this stage of data synthesis focus on privacy issues.

Report issue for preceding element

Replace sensitive data with synthesis data. In order to mitigate the privacy issue, \[ [457](https://arxiv.org/html/2505.18458v1#bib.bib457 "")\] proposes a two-stage synthetic data generation and privacy-enhancing method for the RAG stage of LLM.

Report issue for preceding element

In the first stage, key information is extracted from the original data (such as “symptom description” and “treatment plan” in medical dialogues), and LLM is used to generate synthetic data based on key information but does not contain sensitive details.

Report issue for preceding element

In the second stage, LLMs are applied to the synthetic data, and rewriting strategies are employed to eliminate potential privacy leaks (such as removing specific names or obfuscating descriptions).

Report issue for preceding element

This process of evaluation and rewriting is repeated to ensure that the generated data retains its key utility while completely avoiding privacy concerns.

Report issue for preceding element

#### 2.2.7 End-to-End Data Processing Pipelines

Report issue for preceding element

With above data processing methods, we separately introduce existing frameworks that support common processing operations; practices of integrating some of these methods within pipelines in real-world LLM data preparation; together with some preliminary pipeline orchestration methods.

Report issue for preceding element

PrinciplesWhen designing data processing pipelines, several critical factors must be considered: (1) the trade-off between data quality and quantity; (2) dependencies across the processing operations (e.g., text extraction necessarily preceding operations like deduplication and filtering); (3) efficiency optimization (e.g., conducting computationally intensive steps like model-based filtering after lightweight processing steps like URL filtering).Report issue for preceding element

#### 2.2.7.1 Typical data processing frameworks

Report issue for preceding element

Data processing frameworks provide built-in libraries, operators, and intuitive interfaces that can benefit the design of data processing pipelines for different LLMs. Here we showcase three typical data processing frameworks.

Report issue for preceding element

(1) Data-juicer \[ [90](https://arxiv.org/html/2505.18458v1#bib.bib90 "")\] is an open-source data processing framework with customization, high-quality, diverse, and efficient data recipes. It has 50 built-in operators for tasks like formatting, mapping, filtering, and deduplication. Besides, Data-juicer incorporates visualization and auto-evaluation capabilities to provide timely feedback, and is optimized for distributed computing to handle large-scale data efficiently.

Report issue for preceding element

(2) Dataverse \[ [306](https://arxiv.org/html/2505.18458v1#bib.bib306 "")\] is an open-source pipeline to streamline the development of custom ETL (Extract-Transform-Load) pipelines using a block-based interface that allows users to intuitively customize their ETL pipelines by simply adding, removing, or reshuffling blocks. Dataverse includes a wide range of native operations for data processing, such as deduplication, decontamination, bias mitigation, and toxicity reduction, and supports multi-source data ingestion. Similar to Data-juicer, Dataverse integrates with Apache Spark for distributed processing and supports AWS integration for cloud scalability.

Report issue for preceding element

(3) \[ [373](https://arxiv.org/html/2505.18458v1#bib.bib373 "")\] introduces a data processing framework that allows users to customize data processing pipelines without manual coding. It has two main modules: (1) The processing module consists of operators for data reformatting (read and import strctured data), cleaning (removed undesired data such as HTML tags and translate text), filtering, and deduplication (using MinHashLSH in Section [2.2.2](https://arxiv.org/html/2505.18458v1#S2.SS2.SSS2 "2.2.2 Data Deduplication ‣ 2.2 Data Processing for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")); (2) The analyzing module supports probing and evaluation of the refined data.

Report issue for preceding element

#### 2.2.7.2 Typical data pipelines

Report issue for preceding element

Data processing pipelines aim to orchestrate a subset of data processing operations (in a specific order) that transform raw data into high-quality LLM training data (mostly for the pre-training stage). Here we showcase three representative pipelines.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2505.18458v1/x5.png)Figure 6: Typical data processing pipelines for LLMs.Report issue for preceding element

∙∙\\bullet∙The MacroData Refinement (MDR) pipeline is designed to construct the RefinedWeb Dataset, which has been used for pre-training Falcon LLMs \[ [312](https://arxiv.org/html/2505.18458v1#bib.bib312 "")\]. MDR refines web-scale data from Common Crawl \[ [11](https://arxiv.org/html/2505.18458v1#bib.bib11 "")\] through three main operations.

Report issue for preceding element

(i) Data acquisition: MDR first applies a lightweight URL filter to exclude irrelevant links before any computationally intensive steps. It then extracts text from WARC files using warcio and Trafilatura  \[ [73](https://arxiv.org/html/2505.18458v1#bib.bib73 "")\], followed by language identification (i.e., removing content with limited natural language) using fastText  \[ [200](https://arxiv.org/html/2505.18458v1#bib.bib200 "")\] as implemented in CCNet \[ [417](https://arxiv.org/html/2505.18458v1#bib.bib417 "")\].

Report issue for preceding element

(ii) Data filtering: To eliminate low-quality content, MDR employs both (1) document-level filtering \[ [329](https://arxiv.org/html/2505.18458v1#bib.bib329 "")\] and (2) line-level filtering, which removes noisy content such as social media counters or navigation links.

Report issue for preceding element

(iii) Data deduplication: Despite prior filtering, substantial content duplication remains, which can degrade model performance. MDR performs both fuzzy deduplication using MinHash and exact deduplication with suffix arrays to minimize redundancy. To address computational limits, the Common Crawl corpus is partitioned into 100 segments, with deduplication performed per segment. Additionally, to avoid cross-part redundancy, URL-level deduplication is applied by excluding URLs already retained in earlier segments.

Report issue for preceding element

Overall, MDR follows three core design principles: (i) scale first, by maximizing data volume from Common Crawl to support large model training; (ii) strict deduplication, as rigorous redundancy elimination is critical for training efficiency and generalization; and (iii) heuristic filtering, favoring rule-based filters over ML-based ones to reduce bias and maintain transparency.

Report issue for preceding element

∙∙\\bullet∙The DCLM-Baseline pipeline also processes data from the Common Crawl dataset. Different from MDR, in addition to text extraction and language identification, it applies efficient heuristic filtering \[ [312](https://arxiv.org/html/2505.18458v1#bib.bib312 "")\] to exclude irregular content (e.g., toxic words or webpages from illegal sources). Next, DCLM-Baseline adopts a Bloom filter for data deduplication, ensuring its scalability with large datasets. Finally, over the processed data with much smaller size, it conducts model-based quality filtering (most computationally intensive) to remove low-quality content. Specifically, a fastText classifier trained on instruction-formatted data, including OH-2.5 (OpenHermes 2.5) and ELI5 (ExplainLikeImFive), is used to retain the top 10% of documents.

Report issue for preceding element

∙∙\\bullet∙The FineWeb pipeline (for preparing a 15T-token pretraining dataset) starts with text extraction from WARC files using Trafilatura \[ [73](https://arxiv.org/html/2505.18458v1#bib.bib73 "")\], which is more custom than directly using WET format data and language filtering with fastText. Different from the above pipelines, it conducts MassiveText filtering, i.e., heuristic quality filters and repetition filters on paragraph, line, and gram level \[ [329](https://arxiv.org/html/2505.18458v1#bib.bib329 "")\]. Besides, it conducts fuzzy deduplication using individual MinHash deduplication for each CommonCrawl snapshot, as this approach matches RefinedWeb’s performance, whereas global deduplication yields little improvement over non-deduplicated data. After deduplication, given the observation that the C4 dataset yields superior performance on some benchmarks despite its smaller size, a selection of C4 \[ [332](https://arxiv.org/html/2505.18458v1#bib.bib332 "")\]’s heuristic filters is applied to drop low-quality content such as unpunctuated lines and policy statements. Finally, to further enhance data quality, additional custom heuristic filters are developed through a systematic process. Moreover, personal identifiable information (PII) such as email addresses is anonymized using regex patterns in the public release of the dataset.

Report issue for preceding element

Compared to MDR and DCLM-Baseline, the FineWeb pipeline is considerably more complex due to its integration of multiple layers of filtering, each inspired by empirical evaluations and comparisons with other datasets such as C4 and RefinedWeb. Its design reflects a trade-off that prioritizes performance over simplicity.

Report issue for preceding element

#### 2.2.7.3 Orchestration of data pipelines

Report issue for preceding element

The above data pipelines are mostly designed by experience. Instead, Data-Juicer Sandbox \[ [91](https://arxiv.org/html/2505.18458v1#bib.bib91 "")\] proposes a “Probe-Analyze-Refine” workflow, which involves systematically exploring the impact of various data processing operations and their orders on model performance, combining effective operations into data recipes, and optimizing data utilization through a dual analysis focusing on duplication and diversity. The orchestrated pipelines are validated through applications on state-of-the-art models like Mini-Gemini (for image-to-text generation) and EasyAnimate (for text-to-video generation).

Report issue for preceding element

### 2.3 Data Storage for LLM

Report issue for preceding element

In this section, we introduce storage techniques for LLMs, which we categorize accroding to the tasks they address, including (1) data formats, (2) data distribution, (3) data organization, (4) data movement, (5) data fault tolerance, and (6) KV cache.

Report issue for preceding element

#### 2.3.1 Data Formats

Report issue for preceding element

Data formats are file formats for training data and models.
For LLMs, appropriate file formats for data and models can enhance storage efficiency, accommodate multimodal data, be suitable for model training, ensure security, and influence compatibility across different frameworks.

Report issue for preceding element

PrinciplesCompared to traditional machine learning, LLMs place greater demands on data being multi-modal and in a unified format. The main challenge is how to achieve high data reading efficiency in multi-modal scenarios. Current methods address this using techniques like sequential storage.Report issue for preceding element

Training Data Format.
For training data, file formats are required to have good storage efficiency (e.g., TFRecord \[ [44](https://arxiv.org/html/2505.18458v1#bib.bib44 "")\]), be adaptable to large amounts of data (e.g., MindRecord \[ [40](https://arxiv.org/html/2505.18458v1#bib.bib40 "")\]), and sometimes be suitable for model training (e.g., tf.data.Dataset\[ [43](https://arxiv.org/html/2505.18458v1#bib.bib43 "")\]).

Report issue for preceding element

(1) Pure-Text Formats. Common formats such as CSV, JSON, TSV, and TXT are often used to store pure-text LLM data (though they are not limited to such content). However, for large-scale training datasets (at the PB scale), these formats incur significant storage overhead due to the lack of compression (e.g., not supporting binary encoding), leading to storage waste and slow data loading during LLM training.

Report issue for preceding element

To address these issues, TFRecord \[ [44](https://arxiv.org/html/2505.18458v1#bib.bib44 "")\] is based on Protobuf (a highly efficient binary serialization protocol) and stores data in a row-based format. As a binary format, its size is significantly smaller than JSON or CSV. Besides, data can be written and read in a streaming manner, making it especially suitable for scenarios like training where data is consumed sample by sample.

Report issue for preceding element

(2) Multimodal Formats.
Pure-text formats are not well-suited for multimodal datasets containing images, videos, and text. To address this, file formats such as TFRecord \[ [44](https://arxiv.org/html/2505.18458v1#bib.bib44 "")\] in TensorFlow and MindRecord \[ [40](https://arxiv.org/html/2505.18458v1#bib.bib40 "")\] in MindSpore have been developed to natively support efficient multimodal data storage.

Report issue for preceding element

∙∙\\bullet∙ Unlike traditional formats (e.g., COCO JSON \[ [10](https://arxiv.org/html/2505.18458v1#bib.bib10 "")\], which store image metadata in separate JSON files), TFRecord \[ [44](https://arxiv.org/html/2505.18458v1#bib.bib44 "")\] allows users to encapsulate images, labels, and metadata within a single tf.train.Example, eliminating the need for separate label files. Moreover, as multimodal datasets substantially increase data volume, TFRecord supports data sharding, enabling the creation of distributed files that can be assigned across multiple servers to facilitate parallel training.

Report issue for preceding element

∙∙\\bullet∙ MindRecord organizes data into two types of files: (i)𝑖(i)( italic\_i ) the data file, which contains a file header, scalar data pages (e.g., image labels and filenames), and block data pages (e.g., image and text) to store training data; and (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) the index file, which maintains indexing information based on scalar data to support efficient retrieval and dataset analysis.

Report issue for preceding element

(4) Tensor Data Formats. Compared to the storage formats mentioned above, tensor formats represent data as multi-dimensional arrays. On GPUs or TPUs, such multi-dimensional structures can be partitioned and processed in parallel, making them highly suitable for large-scale computation. For example, tf.data.Dataset\[ [43](https://arxiv.org/html/2505.18458v1#bib.bib43 "")\] can organize various raw data types (e.g., images, text) into a unified tensor format, ready for direct use by models. However, tensor formats, due to their dense multi-dimensional storage, incur large storage overhead and offer poor readability, and are typically adopted only in model training.

Report issue for preceding element

Model Data Format. Model storage formats need to pay attention to security (e.g., Safetensors \[ [85](https://arxiv.org/html/2505.18458v1#bib.bib85 "")\]) and are usually closely tied to their respective model training frameworks \[ [32](https://arxiv.org/html/2505.18458v1#bib.bib32 ""), [42](https://arxiv.org/html/2505.18458v1#bib.bib42 ""), [22](https://arxiv.org/html/2505.18458v1#bib.bib22 "")\].

Report issue for preceding element

∙∙\\bullet∙ Pickle (.pkl \[ [13](https://arxiv.org/html/2505.18458v1#bib.bib13 "")\]) is a Python-specific format supported by almost all Python frameworks and can store any Python object, not limited to model parameters, making it convenient for saving model states and other custom information.

Report issue for preceding element

∙∙\\bullet∙ Safetensors \[ [85](https://arxiv.org/html/2505.18458v1#bib.bib85 "")\] was introduced by Huggingface to address the security concerns inherent in Python’s Pickle-based serialization. While Pickle serializes both the data and behavior of Python objects—enabling arbitrary code execution during deserialization—safetensors avoids this risk by focusing exclusively on tensors and their associated metadata. This design ensures safe deserialization without the possibility of executing malicious code. Additionally, safetensors supports memory mapping (mmap), which significantly enhances the efficiency of model loading.

Report issue for preceding element

∙∙\\bullet∙ PyTorch-specific formats (e.g., .pt, .pth\[ [32](https://arxiv.org/html/2505.18458v1#bib.bib32 "")\]) are optimized for model storage. Typically, .pth files are used to save training checkpoints, including model parameters, optimizer states, and epoch information, while .pt files are used to store only the model parameters.

Report issue for preceding element

∙∙\\bullet∙ TensorFlow offers two common saving formats \[ [42](https://arxiv.org/html/2505.18458v1#bib.bib42 "")\]: (1) SavedModel format for saving the entire model, including computation graph, weights, optimizer; (2) .ckpt for storing model weights, optimizer states, and training metadata, and is used to save and restore progress during training.

Report issue for preceding element

∙∙\\bullet∙ ONNX \[ [27](https://arxiv.org/html/2505.18458v1#bib.bib27 "")\] is a cross-framework deep learning model format that supports interoperability across frameworks like PyTorch, TensorFlow, and Caffe2. It offers cross-platform and cross-framework advantages, but does not store training state information.

Report issue for preceding element

∙∙\\bullet∙ The Hugging Face Transformers library \[ [22](https://arxiv.org/html/2505.18458v1#bib.bib22 "")\] adopts a modular storage design, i.e., model weights are stored in binary .bin files, model configurations are stored in .json or .txt files.

Report issue for preceding element

#### 2.3.2 Techniques for LLM Data Distribution

Report issue for preceding element

With the development of LLMs, the scale of LLM training datasets and the number of parameters of LLMs themselves are growing rapidly (e.g., 9.5 PB data form Common Crawl  \[ [184](https://arxiv.org/html/2505.18458v1#bib.bib184 "")\], DeepSeek-R1 \[ [163](https://arxiv.org/html/2505.18458v1#bib.bib163 "")\] has 617B parameters). A single node cannot store such large-scale data, and the data needs to be distributed across multiple nodes. The key technologies involved mainly include (1) distributed storage systems and (2) heterogeneous storage systems.

Report issue for preceding element

PrinciplesCompared to traditional machine learning, the data (e.g., training data and model data) used in LLMs including both is growing exponentially. The main challenge lies in how to efficiently store and manage such large-scale data. Current approaches address this through distributed and heterogeneous storage systems.Report issue for preceding element

Distributed Storage Systems.
Distributed storage systems refer to storing a large-scale datasets across multiple nodes (e.g., JuiceFS \[ [16](https://arxiv.org/html/2505.18458v1#bib.bib16 "")\], 3FS \[ [15](https://arxiv.org/html/2505.18458v1#bib.bib15 "")\]). Traditional distributed file systems (such as HDFS \[ [79](https://arxiv.org/html/2505.18458v1#bib.bib79 "")\]) often come with high costs. Moreover, most distributed file systems still use the POSIX protocol when loading the training data for LLMs, which bring about significant software overhead.

Report issue for preceding element

JuiceFS \[ [16](https://arxiv.org/html/2505.18458v1#bib.bib16 "")\], a typical distributed file system based on object storage, uses object storage (e.g., S3 \[ [4](https://arxiv.org/html/2505.18458v1#bib.bib4 "")\]) as the backend to store data. Compared to traditional distributed file systems (file or block storage), distributed file systems based on object storage enables simpler horizontal scaling. It does not need complex directory hierarchy (File Storage) and does not involve complex management logic (Block Storage), thereby significantly reducing storage costs (approximately 20% of the cost of traditional file systems).

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2505.18458v1/x6.png)Figure 7: The storage architecture of 3FS \[ [15](https://arxiv.org/html/2505.18458v1#bib.bib15 "")\].Report issue for preceding element

As shown in Figure [7](https://arxiv.org/html/2505.18458v1#S2.F7 "Figure 7 ‣ 2.3.2 Techniques for LLM Data Distribution ‣ 2.3 Data Storage for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices"), 3FS \[ [15](https://arxiv.org/html/2505.18458v1#bib.bib15 "")\] employs a large number of SSDs for distributed data storage and uses the CRAQ algorithm to ensure data consistency. Specifically, a piece of data is saved as multiple same chunks, which together form a Chain. For read requests, they can be sent to any chunk in the Chain, and the chunk will return the data. For write requests, the writing operation is carried out sequentially on each chunk. When a certain chunk malfunctions, instead of using the incremental data generated during the abnormal period to overwrite the data as in traditional methods, it first moves the chunk to the end of the chain. Only when the chunk returns to normal will the entire content of other samples be copied to the abnormal chunk. These operations, while ensuring data consistency, will cause a certain delay in write operations. However, they have almost no impact on read operations, which are more important for LLM training.

Report issue for preceding element

Meanwhile, 3FS \[ [15](https://arxiv.org/html/2505.18458v1#bib.bib15 "")\] discovers that in the context of LLM training, the File Cache significantly consumes system memory, thereby degrading overall I/O performance. To address this, 3FS adopts an asynchronous data loading approach, disables file caching and exclusively utilizes Direct I/O for data access, significantly reducing memory pressure. Moreover, it performs system-level alignment of buffer pointers, offsets, and lengths to satisfy Direct I/O requirements, thereby avoiding additional memory copies caused by user-side alignment operations.

Report issue for preceding element

Heterogeneous Storage Systems.
Heterogeneous storage systems refers to deploying the model state across diverse storage media (e.g., GPUs, CPUs, NVMes Memory). When deploying the model, The Zero Redundancy Optimizer (ZeRO) \[ [336](https://arxiv.org/html/2505.18458v1#bib.bib336 "")\] deploys model states across multiple GPUs. However, simply distributing the model across multiple GPUs often significantly increases computational costs.

Report issue for preceding element

Some methods \[ [337](https://arxiv.org/html/2505.18458v1#bib.bib337 ""), [340](https://arxiv.org/html/2505.18458v1#bib.bib340 ""), [339](https://arxiv.org/html/2505.18458v1#bib.bib339 ""), [443](https://arxiv.org/html/2505.18458v1#bib.bib443 "")\] alleviate GPU memory pressure by storing data in host memory or NVMe SSD.
vDNN \[ [340](https://arxiv.org/html/2505.18458v1#bib.bib340 "")\] utilizes a per-layer memory management approach based on a sliding window that dynamically allocates memory at runtime based on the computational demands of the current layer.
Its memory transfer mechanism includes both static and dynamic policies: the static policy offloads feature maps of all layers or only convolutional layers, while the dynamic policy determines which layers and convolutional algorithms to offload at runtime, balancing trainability and performance based on network characteristics. vDNN fully utilizes CPU memory by offloading intermediate feature maps that are not immediately needed and prefetching them prior to backpropagation.
ZeRO-Infinity \[ [337](https://arxiv.org/html/2505.18458v1#bib.bib337 "")\] offloads model states to CPU (e.g. activations) and NVMe memory, effectively alleviating the GPU memory bottleneck.
To further reduce memory pressure, it introduces a memory-centric tiling technique that lowers the working memory requirements for LLM training, enabling the execution of large operators without relying on model parallelism.

Report issue for preceding element

However, both vDNN and ZeRO-Infinity only utilize CPU’s memory without leveraging its computational capabilities. In contrast, ZeRO-Offload \[ [339](https://arxiv.org/html/2505.18458v1#bib.bib339 "")\] retains the parameters and forward/backward computations on the GPU while offloading the remaining computations (such as optimizer calculations) to the CPU, thereby harnessing the CPU’s computational power.

Report issue for preceding element

Unlike the aforementioned methods that often rely on manual parameter tuning (e.g., specifying offloading targets like CPU or NVMe), ProTrain \[ [443](https://arxiv.org/html/2505.18458v1#bib.bib443 "")\] introduces a model- and hardware-aware automated framework. It incorporates a Memory-Aware Runtime Profiler for monitoring real-time memory and compute loads, partitions parameters into persistent (resident on GPU) and non-persistent (offloaded/loaded on demand) chunks based on their usage patterns, and reduces redundant data copying via pre-allocated chunk buffers.

Report issue for preceding element

#### 2.3.3 Data Organization

Report issue for preceding element

Data organization refers to data operations (e.g., content organization in vector-based organization) during the storage stage that are designed to optimize retrieval accuracy and efficiency in RAG systems.
When LLM answers questions, issues like hallucination \[ [188](https://arxiv.org/html/2505.18458v1#bib.bib188 "")\] and lack of timeliness often arise.
To address these limitations, RAG \[ [229](https://arxiv.org/html/2505.18458v1#bib.bib229 "")\] (e.g., vector-based retrieval and graph-based retrieval) have been introduced. They provide models with real-time, reliable context during inference. And both retrieval methods are based on the relevant data organization operations (e.g., vector-based organization and graph-based organization).

Report issue for preceding element

PrinciplesCompared to traditional machine learning, LLMs require RAG knowledge to access real-time information. The main challenge is how to ensure both the efficiency and accuracy of retrieval. Current methods address this through vector-based and graph-based data organization techniques. However, existing RAG systems still fall short of meeting the high-quality retrieval demands at the enterprise level, where the document scale can reach millions of pages.Report issue for preceding element

Vector-Based Organization Vector-based organization refers to converting data into vector form for efficient retrieval. It processes the original data through multiple stages (e.g., Content Organization, Chunking, Embedding, Compression and Storage).

Report issue for preceding element

(1) Content Organization.
For the source data, organizing the content can enhance its logical structure, thereby facilitating improved efficiency and accuracy in retrieval. Works like Dense x retrieval \[ [98](https://arxiv.org/html/2505.18458v1#bib.bib98 "")\], APS \[ [173](https://arxiv.org/html/2505.18458v1#bib.bib173 "")\] refine text into independent semantic units, which could be described as the minimal sentence that include all the necessary context information from the original text to express its meanings, and Thread \[ [57](https://arxiv.org/html/2505.18458v1#bib.bib57 "")\] reorganizes documents into logical units, with each unit containing prerequisites, headers, body content, linkers (describing possible paths for next step), and metadata, enabling a logical and structured representation of the document’s content, which significantly enhances the system’s logical coherence and processing efficiency especially in complex tasks (e.g., troubleshooting and dynamic operational workflows).

Report issue for preceding element

Similarly, \[ [89](https://arxiv.org/html/2505.18458v1#bib.bib89 "")\] organizes the content of scientific papers into a hierarchical tree structure, where the root node of the tree is the paper’s title and child nodes are different sections, such as the introduction and methods. The relationship between parent and child nodes represents the global-local content relationships, such as the connection between the abstract and introduction. Then it traverses the paths from the root node to the leaf nodes to extract important contextual information.

Report issue for preceding element

(2) Chunking.
In vector-based retrieval, embedding long texts may reduce retrieval efficiency. Thus, an effective chunking strategy is required to divide the text into appropriately sized segments for encoding. The optimal chunk length needs to balance retaining fine-grained semantics and maintaining sufficient context, since a too long text might suffer from significant semantic compression during embedding, while too short a text would increase processing costs.

Report issue for preceding element

Allowing overlap between consecutive chunks ensures that important information at the boundaries is not lost and the continuity of context is maintained. Different from traditional chunking, MoG \[ [486](https://arxiv.org/html/2505.18458v1#bib.bib486 "")\] adopts a dynamic chunking strategy, which chunks data when building the knowledge base, where MoG dynamically determines the optimal granularity (e.g., sentence-level, paragraph-level, or section-level) of the knowledge source based on the input query through a trained router. The router, implemented as an MLP, assigns weights to different granularities to guide snippet selection. MoGG \[ [486](https://arxiv.org/html/2505.18458v1#bib.bib486 "")\] extends MPG by converting reference documents into graphs and redefining granularity as hopping ranges, enabling effective retrieval of dispersed information for complex queries.

Report issue for preceding element

(3) Embedding.
In vector-based retrieval, the original input (text, images, audio, or other domains) is transformed into dense vector representations using models specifically adjusted for each data type. These representations encapsulate the underlying semantic meaning of the original content, and are then stored in a vector database for storage and retrieval. Various embedding models are used to correctly encode semantic information:

Report issue for preceding element

∙∙\\bullet∙ _BGE_ uses a bilingual joint training framework that combines language-specific subword tokenization and specialized adaptation layers. This design aligns semantic representations across languages, improving cross-lingual retrieval accuracy \[ [94](https://arxiv.org/html/2505.18458v1#bib.bib94 "")\].

Report issue for preceding element

∙∙\\bullet∙ _STELLA_ features a cross-instance attention aggregation mechanism that explicitly captures inter-sentence dependencies during pretraining. Besides the general embedding model, STELLA offers an extra dialogue model in incomplete query situations where the user input has problems such as semantic omission and reference digestion. This reduces the embedding dimensions and inference latency, making it especially effective for large-scale tasks \[ [24](https://arxiv.org/html/2505.18458v1#bib.bib24 "")\].

Report issue for preceding element

∙∙\\bullet∙ _GTE_ introduces a dual-negative sampling strategy within its contrastive learning paradigm. Though introducing negative samples usually works in series of embedding models, this strategy incorporates more reverse contrastive terms within a fixed batch, strengthening the model’s ability to distinguish subtle semantic differences. \[ [250](https://arxiv.org/html/2505.18458v1#bib.bib250 "")\].

Report issue for preceding element

(4) Compression.
Vector retrieval in LLMs differs from regular vector retrieval in that semantically similar vectors are often high-dimensional, so dimensionality reduction techniques are needed to reduce storage pressure.

Report issue for preceding element

∙∙\\bullet∙Linear Dimensionality Reduction.
Locally-adaptive Vector Quantization (LVQ) \[ [50](https://arxiv.org/html/2505.18458v1#bib.bib50 "")\] centralizes the data and scales each vector individually, calculating the quantization bounds adaptively in a localized manner, fully utilizing the quantization range to compress the vectors. This method is typically suitable for compressing vectors with around 100 dimensions, but it performs poorly when the vector dimension is very large, such as tens of thousands.

Report issue for preceding element

LeanVec \[ [385](https://arxiv.org/html/2505.18458v1#bib.bib385 "")\] combines linear dimensionality reduction with LVQ for vector compression. In ID (In-distribution) scenarios, LeanVec uses PCA, while in OOD (Out-of-distribution) scenarios, it introduces the LeanVec-OOD optimization method, which identifies the optimal projection subspace for both the dataset and the query set by minimizing the squared inner product between the query vector and the representation error, thereby reducing vector dimensionality. However, LeanVec is a simple linear dimensionality reduction method, and its performance may be affected in terms of accuracy when reducing the dimensionality drastically.

Report issue for preceding element

LeanVec-Sphering \[ [386](https://arxiv.org/html/2505.18458v1#bib.bib386 "")\] modifies the loss function, transforming the problem of finding the projection matrix into an optimization problem under the Mahalanobis distance, which allows for more effective discovery of the optimal projection matrix, thereby better preserving the similarity structure between vectors when processing high-dimensional vectors.

Report issue for preceding element

∙∙\\bullet∙Non-linear Dimensionality Reduction.
GleanVec \[ [386](https://arxiv.org/html/2505.18458v1#bib.bib386 "")\] uses spherical k-means clustering in the data partitioning stage to group vectors based on direction, capturing the data’s structural features. By associating cluster labels with vectors, it narrows the search range and reduces unnecessary calculations during inner product computation. In the local linear dimensionality reduction stage, GleanVec applies the LeanVec-Sphering method to reduce dimensionality within each cluster, preserving the inner-product relationship, which simplifies calculations while maintaining accuracy.

Report issue for preceding element

(5) Storage.
After the above steps, the data will be stored in vector form in a vector database. During LLM inference, the model vectorizes the input and uses similarity metrics such as cosine similarity or dot product to retrieve the most relevant data from the database.

Report issue for preceding element

Faiss \[ [125](https://arxiv.org/html/2505.18458v1#bib.bib125 "")\], when storing vectors, relies on the chosen index type. The Flat Index stores all vectors directly, such as IndexFlatCodes, which stores vectors in a flat array and supports sequential IDs. It is ideal for small datasets with high-precision requirements. The IVF Index clusters vectors with a coarse quantizer and stores them in inverted lists, supporting user ID operations and optionally using a DirectMap for efficient access. This reduces the search range and speeds up retrieval, making it suitable for large datasets. The PQ Index compresses vectors by splitting them into sub-vectors and quantizing them with a k-means quantizer (e.g., PQ6x10), trading accuracy for reduced storage space, making it suitable for high storage demands and lower precision needs.

Report issue for preceding element

In the Milvus \[ [26](https://arxiv.org/html/2505.18458v1#bib.bib26 "")\], vector storage differs based on the number of vectors per entity. For single-vector entities, vectors are stored continuously without row IDs. Since vectors are sorted by row ID and have the same length, a vector can be directly accessed using its row ID, reducing storage overhead and improving query access efficiency. For multi-vector entities, vectors are stored in a columnar format. For example, for entities A and B, each with two vectors, the storage format is (A.v1, B.v1, A.v2, B.v2). This columnar storage enables more efficient data processing by vector dimension, facilitating batch operations and improving processing performance.

Report issue for preceding element

Weaviate \[ [34](https://arxiv.org/html/2505.18458v1#bib.bib34 "")\] utilizes a graph data model to manage data entities, storing vectors as node attributes linked to these entities. For example, in the case of text data, vectors generated by a text embedding model are associated with their corresponding text entity nodes, enabling efficient graph traversal and multi-hop queries based on vector similarity. Additionally, Weaviate can store vectors alongside structured attributes. For instance, the vectors of e-commerce products, along with structured attributes such as price and category, are stored in the corresponding entity nodes. This allows for hybrid queries that combine vector similarity and structured attribute conditions, enhancing query flexibility and practicality.

Report issue for preceding element

LanceDB \[ [25](https://arxiv.org/html/2505.18458v1#bib.bib25 "")\] uses a columnar storage format called Lance to store data. Compared to traditional Parquet formats, Lance introduces the concept of a table schema. A single row in LanceDB can store images, text, audio, video, and any number of vectors corresponding to different parts of the original data, and it can be dynamically updated. This makes LanceDB particularly suitable for storing multi-modal data. Currently, LanceDB is used for handling various RAG tasks.

Report issue for preceding element

Graph-Based Organization. Unlike vector-based organization, which helps LLM find knowledge related to a user’s query through fuzzy searching, graph-based data explicitly represents entities and their relationships, enabling the identification of precise matching information in the database.
We will introduce graph-based organization from two aspects: indexing and storage.

Report issue for preceding element

(1) Indexing.
In the indexing phase, it is necessary to establish an efficient indexing architecture to address the issue that directly retrieving raw triples is inefficient for complex queries such as multi-hop reasoning or path search, because the inherent sparsity in the graph structure often leads to significant query latency.

Report issue for preceding element

GraphRAG \[ [127](https://arxiv.org/html/2505.18458v1#bib.bib127 "")\] adopts community clustering and hierarchical summarization strategies. It uses the Leiden algorithm to detect tightly connected subgraphs, called communities, in the knowledge graph. Then, it generates hierarchical summaries for each community. Once a certain element in a triple is retrieved, the index collects relevant community summaries and sends them for inference. For example, it can condense hundreds of triples related to ”quantum mechanics” into a semantic summary: ”Quantum mechanics is the fundamental theory describing the behavior of matter and energy at microscopic scales”.

Report issue for preceding element

Furthermore, LightRAG \[ [165](https://arxiv.org/html/2505.18458v1#bib.bib165 "")\] integrates deduplication functionality to identify and merge identical entities and relations from different paragraphs. In real-time update scenarios, LightRAG introduces the Delta Index mechanism, which builds local indexes only for newly inserted edges and entities, using background merging threads without the need for community reconstruction, significantly reducing overhead related to community detection compared to GraphRAG.

Report issue for preceding element

MiniRAG \[ [136](https://arxiv.org/html/2505.18458v1#bib.bib136 "")\] proposes a semantic-aware heterogeneous graph indexing mechanism, integrating text chunks and named entities into a unified structure, reducing the reliance on large language models for complex semantic understanding. The low semantic calculating requirement while deploying grants MiniRAG a more excellent performance on resource-constrained devices compared to other methods.

Report issue for preceding element

(2) Storage. Graph data is usually stored in graph databases in three models: property graph models \[ [293](https://arxiv.org/html/2505.18458v1#bib.bib293 "")\], RDF (Resource Description Framework) models \[ [65](https://arxiv.org/html/2505.18458v1#bib.bib65 "")\], and multi-model \[ [1](https://arxiv.org/html/2505.18458v1#bib.bib1 "")\].

Report issue for preceding element

Neo4j, JanusGraph, and TigerGraph use property graph models \[ [293](https://arxiv.org/html/2505.18458v1#bib.bib293 "")\] to store graph-based data. A property graph model consists of ”nodes” and ”edges,” where both can contain attributes (key-value pairs). This model uses query languages like Cypher and GSQL, designed for relationship modeling and querying, making them highly suitable for complex relationship queries during RAG in LLMs.

Report issue for preceding element

Amazon Neptune \[ [65](https://arxiv.org/html/2505.18458v1#bib.bib65 "")\] supports both property graph models and RDF models for graph-based data storage. The RDF model, based on triples (subject, predicate, object), represents entities, attributes, and relationships in a way that enhances knowledge reasoning. By combining these two models, Neptune can meet diverse knowledge storage needs, such as rapid queries and deep reasoning.

Report issue for preceding element

ArangoDB \[ [1](https://arxiv.org/html/2505.18458v1#bib.bib1 "")\] uses a multi-model approach to store graph-based data. It supports multiple data models (e.g., document, key-value pair, graph), allowing the selection of appropriate storage and query methods depending on the requirements. This allows ArangoDB to store graph data (relationship information), document data (context or factual information), and key-value pairs (configuration or metadata) in the same database, facilitating LLMs to extract relationships from knowledge graphs while also retrieving document-type data (e.g., specific context information).

Report issue for preceding element

#### 2.3.4 Data Movement

Report issue for preceding element

Data movement refers to the process of moving data from storage nodes to computing nodes. This process can achieve high data movement performance by caching data. Additionally, the highest overall performance can be achieved by overlapping data storage and computation operations to jointly schedule storage and computing resources.

Report issue for preceding element

PrinciplesCompared to traditional machine learning, LLMs involve massive data transfers from storage nodes to compute nodes. The main challenge is how to accelerate the data moving rate. Current methods address this through data caching, compute-storage overlap, and data/operator offloading.Report issue for preceding element

Caching Data in advance can increase the data moving rate. However, if a fixed cache policy is used, in order to meet the IO requirements of training, the configured storage capacity often far exceeds that required for storing the dataset \[ [476](https://arxiv.org/html/2505.18458v1#bib.bib476 "")\]. Therefore, a dynamically adjustable cache policy is needed. Some methods \[ [220](https://arxiv.org/html/2505.18458v1#bib.bib220 ""), [162](https://arxiv.org/html/2505.18458v1#bib.bib162 ""), [476](https://arxiv.org/html/2505.18458v1#bib.bib476 "")\] dynamically adjust the cache mechanism by analyzing the characteristics and requirements of LLM jobs in real time.

Report issue for preceding element

Quiver \[ [220](https://arxiv.org/html/2505.18458v1#bib.bib220 "")\]
optimizes cache sharing strategies based on the following IO characters during model training: (1) data shareability (due to significant overlap in data access within and across jobs), (2) substitutability (the I/O order does not affect job correctness, enabling small caches to improve performance by substituting data and reducing thrashing), and (3) predictability (using mini-batch processing times to estimate job sensitivity to I/O performance for informed cache allocation).

Report issue for preceding element

Fluid \[ [162](https://arxiv.org/html/2505.18458v1#bib.bib162 "")\] dynamically adjusts cache capacity according to I/O conditions, optimizing the online training speed for each individual LLM job. Specifically, Fluid uses a coordinator to monitor the processes of LLM jobs. It calculates the number of samples within a specific time window based on the batch sizes fed back by the jobs, and thus obtains the real-time training speed. Subsequently, based on the concept of the TCP congestion control algorithm \[ [316](https://arxiv.org/html/2505.18458v1#bib.bib316 "")\], it adopts a trial-and-error approach to dynamically adjust the cache capacity. When the training speed increases, the cache capacity is increased according to the preset scaling-up factor and scaling step. Conversely, when the training speed decreases, the cache capacity is decreased according to the preset scaling-down factor and scaling step.

Report issue for preceding element

Meta proposes Tectonic-Shift \[ [476](https://arxiv.org/html/2505.18458v1#bib.bib476 "")\], a hybrid storage architecture that integrates flash memory with the traditional HDD-based distributed file system Tectonic. Tectonic-Shift organizes data segments into buckets for storage in flash memory and determines segment admission and reinsertion by comparing bucket priorities (computed from both historical and predicted future access patterns) against dynamically adjusted thresholds. It also optimizes the segment size (e.g., 256 KB) of CacheLib \[ [9](https://arxiv.org/html/2505.18458v1#bib.bib9 "")\] to improve flash memory utilization.

Report issue for preceding element

Data/Operator Offloading refers to offloading data preprocessing operations such as shuffling, sampling, and augmentation, to multiple devices in order to improve processing speed. Currently, data preprocessing pipelines (e.g., tf.data) are typically performed on the CPU, whose efficiency is often lower than the training speed achieved by Machine Learning (ML) accelerators like GPUs and TPUs. So enhancing the efficiency of data preprocessing to match the high-speed processing capabilities of ML accelerators has become a challenge \[ [160](https://arxiv.org/html/2505.18458v1#bib.bib160 "")\].

Report issue for preceding element

Some research \[ [159](https://arxiv.org/html/2505.18458v1#bib.bib159 ""), [67](https://arxiv.org/html/2505.18458v1#bib.bib67 "")\] offload data preprocessing tasks to remote CPU servers. Cachew \[ [159](https://arxiv.org/html/2505.18458v1#bib.bib159 "")\] divides the input dataset of each job into independent subsets for processing by remote CPU nodes. Additionally, users can specify locations for caching and reusing data in the input pipeline. The scheduler makes decisions during runtime based on specific metrics and algorithms through automatic scaling and caching strategies. The automatic scaling strategy adjusts the number of worker nodes according to client-reported metrics. The automatic caching strategy compares the processing times of different cache locations and selects the optimal caching scheme.
The tf.data service \[ [67](https://arxiv.org/html/2505.18458v1#bib.bib67 "")\] addresses input data bottlenecks by horizontally scaling CPU nodes and leveraging a coordinated read mechanism to mitigate straggler issues caused by input size variability in distributed training. Specifically, it is comprised of four key components: a dispatcher, a pool of workers, clients, and an orchestrator. The dispatcher manages dataset assignment to workers using various sharding strategies, for example, the OFF strategy performs no sharding, the DYNAMIC strategy applies disjoint first-come-first-served sharding, and several static sharding strategies are also supported. Workers are responsible for actual data processing. Clients issue data processing requests to the workers. Orchestrator deploys the aforementioned three components as containers within the same Borg \[ [389](https://arxiv.org/html/2505.18458v1#bib.bib389 "")\] unit.

Report issue for preceding element

Although the above method of offloading to remote CPU servers can alleviate data stalls, the cost of remote CPUs is high, and the resources of ML accelerator nodes are not fully utilized. Pecan \[ [160](https://arxiv.org/html/2505.18458v1#bib.bib160 "")\] introduces two strategies, AutoPlacement and AutoOrder, to alleviate input data preprocessing bottlenecks and reduce training costs. The AutoPlacement strategy dynamically schedules data preprocessing workers across ML accelerator hosts and remote CPU servers. It first establishes a baseline batch processing time for model training, incrementally adds local workers, and then prunes redundant remote workers to determine the optimal combination of local and remote resources. The AutoOrder strategy analyzes the transformation operations within the input data pipeline, reordering them to place data-reducing transformations (such as sampling, filtering, or image cropping) earlier and data-expanding ones (such as image padding and one-hot encoding) later. While adhering to user-specified ordering constraints, this reorganization improves the preprocessing throughput of individual workers.

Report issue for preceding element

Different from the works that are only compatible with a single training framework as mentioned above (e.g., Cachew and tf.data service can only work with TensorFlow). Powered by native composable operators (e.g., data loading, transformation, and filtering functions), Cedar \[ [475](https://arxiv.org/html/2505.18458v1#bib.bib475 "")\] can flexibly support different ML frameworks and libraries, enabling users to effortlessly build data pipelines.

Report issue for preceding element

Overlapping of storage and computing means that the data loading and computation processes in LLM training alternate. In LLM training, which proceeds in data batches, ideally the data loading unit can prepare the next batch while the computing unit processes the current one, reducing overall training time. However, if a data isn’t cached locally, its need to load the data through remote I/O bandwidth. When this bandwidth is insufficient, computation pauses to wait for data loading, creating an IO bottleneck. Some researches optimize the pipeline at different training stages (e.g., the pre-training and SFT stage \[ [473](https://arxiv.org/html/2505.18458v1#bib.bib473 "")\], the RL stage \[ [485](https://arxiv.org/html/2505.18458v1#bib.bib485 "")\]).

Report issue for preceding element

SiloD \[ [473](https://arxiv.org/html/2505.18458v1#bib.bib473 "")\] leverages the characteristics of the pipelined execution of data loading and computation at the pre-training and SFT stage to build an enhanced performance evaluator. When data loading becomes the bottleneck, it uses a learned model (IOPerf) to quantify the cache and remote I/O demands of different training jobs,providing support for resource allocation in the pipelined execution of data loading and computation.

Report issue for preceding element

Compared with the pre-training and SFT stages, the RL stage requires an additional training of the reward model to evaluate the output of the original model. This leads to a greater amount of computational resources remaining idle (pipeline bubbles) during the RL stage.
RLHFuse \[ [485](https://arxiv.org/html/2505.18458v1#bib.bib485 "")\] takes advantage of the independence between the original and reward models during the training stage to break the training task into sub-tasks of micro-batches. In the case of differences in the sizes and parallel strategies of the two models, it first transforms the problem to ensure that each stage of the two models uses the same number of GPU resources, and then uses the simulated annealing algorithm \[ [214](https://arxiv.org/html/2505.18458v1#bib.bib214 "")\] to generate a fused pipeline schedule.

Report issue for preceding element

#### 2.3.5 Data Fault Tolerance

Report issue for preceding element

Data fault tolerance refers to the ability to quickly resume from the point of interruption during model training by storing checkpoints or performing redundant computations in the event of training interruptions.

Report issue for preceding element

PrinciplesCompared to traditional machine learning, LLMs place greater emphasis on fault tolerance during training due to their large model sizes and the high cost of retraining. The main challenge is how to quickly resume normal training in the event of an interruption. Current methods address this by saving checkpoints or using redundant computation.Report issue for preceding element

Checkpoints.
Some methods store the model state as checkpoints to handle training interruptions. However, restoring model states across multiple platforms or frameworks may encounter compatibility issues. At the same time, frequently saving model checkpoints can consume a large amount of storage space, especially during large-scale model training.

Report issue for preceding element

For compatibility issues, PaddleNLP \[ [29](https://arxiv.org/html/2505.18458v1#bib.bib29 "")\] has developed a unified model storage technology. It stores model weights, optimizer weights, and other data in a unified safetensors format, eliminating the need to differentiate distributed strategies during checkpoint storage. Specifically, when the distributed training strategy changes (e.g., switching between data parallelism and model parallelism) or the number of machines is adjusted, Unified Checkpoint enables training to resume using only a single complete checkpoint, without requiring separate checkpoints for each configuration.

Report issue for preceding element

(1) Asynchronous Storage.
Apart from standardized checkpoint storage, for frequently saving model, some researches \[ [292](https://arxiv.org/html/2505.18458v1#bib.bib292 ""), [195](https://arxiv.org/html/2505.18458v1#bib.bib195 "")\] aim to accelerate checkpoint saving through asynchronous storage without affecting the model’s training speed.

Report issue for preceding element

CheckFreq \[ [292](https://arxiv.org/html/2505.18458v1#bib.bib292 "")\] employs a two-stage checkpointing technique designed to capture model state copies in memory for asynchronous storage while ensuring model parameter consistency through pipelining with subsequent iteration computations. Specifically, when idle GPU memory is available, it prioritizes snapshotting on the GPU to reduce costs; otherwise, it stores checkpoints in CPU memory and adjusts the checkpoint frequency accordingly.

Report issue for preceding element

In the training of LLMs on the MegaScale system \[ [195](https://arxiv.org/html/2505.18458v1#bib.bib195 "")\], HDFS is used to store the model state. When storing model states, there are problems of balancing the checkpoint frequency and dealing with the HDFS bandwidth bottleneck during model recovery in the training process. To address this, MegaScale adopts a two-phase storage approach: (1) GPU worker nodes quickly write the on-chip state to the host memory and continue training; (2) a background process asynchronously transfers the state to HDFS to reduce interference with training. When resuming training, a worker node in the specified data parallel group reads the shared state partition and broadcasts it to other nodes, reducing the HDFS load and alleviating bandwidth pressure.

Report issue for preceding element

(2) Hierarchical Management
refers to storing model checkpoints across a multi-level storage system, storing the checkpoints that may be needed in the closer storage nodes, aiming to improve recovery speed.
Gemini \[ [410](https://arxiv.org/html/2505.18458v1#bib.bib410 "")\] stores checkpoints in a hierarchical storage system composed of local CPU memory, remote CPU memory, and remote persistent storage. It introduces a near-optimal checkpoint placement strategy for CPU memory. By analyzing the relationship between the number of machines and checkpoint replicas, it flexibly adopts group placement or ring placement to maximize the likelihood of recovery from CPU memory in the event of failures.
ByteCheckpoint \[ [395](https://arxiv.org/html/2505.18458v1#bib.bib395 "")\] manages checkpoint files using an architecture combining SSD and HDD storage servers. New checkpoint files are stored as ”hot” data on SSDs for quick access due to evaluation task downloads after creation. Once the evaluation is completed and there are no training anomalies, their access frequency drops, and they become ”cold” data, being migrated to HDDs to free up SSD space and ensure the hot storage can efficiently store currently frequently accessed checkpoint files.

Report issue for preceding element

Redundant Computations
Unlike checkpoint, some methods \[ [387](https://arxiv.org/html/2505.18458v1#bib.bib387 ""), [187](https://arxiv.org/html/2505.18458v1#bib.bib187 ""), [147](https://arxiv.org/html/2505.18458v1#bib.bib147 "")\] are based on parallel computing and redundantly compute the state data of the model, enabling quick recovery of the training state from non-failed nodes in case of failures.

Report issue for preceding element

Inspired by the RAID disk redundancy technology \[ [308](https://arxiv.org/html/2505.18458v1#bib.bib308 "")\], Bamboo \[ [387](https://arxiv.org/html/2505.18458v1#bib.bib387 "")\] enables each computing node to perform computations not only on the neural network layers it is responsible for, but also on some layers of its neighboring nodes as redundant computations. When a node is preempted, its predecessor node has all the information required for training, allowing the training to continue without wasting previous computational results.

Report issue for preceding element

Unlike Bamboo’s node-based redundant computation, Oobleck \[ [187](https://arxiv.org/html/2505.18458v1#bib.bib187 "")\] uses pipeline templates to define training pipeline execution, specifying node allocation, stage numbers, and model layer-GPU mappings. During training, at least f+1𝑓1f+1italic\_f + 1 logically-equivalent yet physically-heterogeneous pipelines are instantiated from these templates, considering the fault tolerance threshold f𝑓fitalic\_f and batch size. When a pipeline node fails, Oobleck leverages other pipelines’ model state redundancy and reinstantiates the pipeline to resume training.

Report issue for preceding element

Unlike Bamboo and Oobleck, which use pre-set redundant computations in standby, ReCycle \[ [147](https://arxiv.org/html/2505.18458v1#bib.bib147 "")\] leverages the computational redundancy inherent in parallel training to reassign the tasks of failed nodes to nodes with the same processing in other data-parallel groups. This unique approach enables quick resumption of training without the need for spare servers.

Report issue for preceding element

#### 2.3.6 KV Cache

Report issue for preceding element

LLMs use auto-regressive generation, where each token depends on prior ones. KV Cache avoids redundant computation by reusing stored key-value pairs, improving efficiency. However, its memory grows with sequence length, making efficient cache management crucial.

Report issue for preceding element

PrinciplesCompared to traditional machine learning, LLMs require KV cache to accelerate inference. The main challenge lies in efficiently managing the cache as the KV size grows rapidly. Current methods address this by indexing KV, shrinking KV, and managing KV placement or cache space.Report issue for preceding element

Cache Space Management refers to separating the logical structure of the KV cache from its physical storage implementation, which facilitates memory allocation and improves memory utilization.
vLLM \[ [221](https://arxiv.org/html/2505.18458v1#bib.bib221 "")\] and vTensor \[ [436](https://arxiv.org/html/2505.18458v1#bib.bib436 "")\] divide the KV cache into fixed-size blocks and store them in a non-contiguous manner. vLLM manages these blocks through a mapping mechanism, while vTensor stores the fixed-size KV cache blocks non-contiguously in physical memory. This decouples the logical and physical KV blocks, utilizing a block table to manage dynamic memory allocation by tracking the mapping relationships and fill states.

Report issue for preceding element

KV Placement
refers to using a perception strategy to store frequently used KV in faster storage media (such as GPU memory), while storing less frequently used KV in slower storage media (such as SSD), or releasing them directly.
RAGCache \[ [198](https://arxiv.org/html/2505.18458v1#bib.bib198 "")\] provides a prefix-aware PGDSF replacement policy that prioritizes cache nodes based on access frequency, size, and recomputation cost. And stores frequently accessed data in fast GPU memory and less frequent data in slower host memory, maximizing cache efficiency.
CachedAttention \[ [148](https://arxiv.org/html/2505.18458v1#bib.bib148 "")\] leverages the inference job scheduler to observe the jobs waiting for execution. To improve cache efficiency, the KV cache of a pending job is prefetched into the host memory from disk before execution. Meanwhile, KV caches that are no longer required are evicted, based on the jobs waiting to be executed.

Report issue for preceding element

KV Shrinking
KV Cache Shrinking refers to trimming or reducing the KV Cache in order to lower memory usage and improve inference efficiency.
CacheGen \[ [266](https://arxiv.org/html/2505.18458v1#bib.bib266 "")\] uses a customized tensor encoder to encode the KV cache into a more efficient bitstream, thereby reducing bandwidth usage. It also compresses the KV cache using techniques such as block-based encoding, hierarchical quantization, and arithmetic encoding, while dynamically adjusting the compression level and transmission method based on network conditions to ensure low latency and high generation quality.

Report issue for preceding element

Unlike CacheGen, which only considers intra-layer redundancy, MiniCache \[ [256](https://arxiv.org/html/2505.18458v1#bib.bib256 "")\] is based on the similarity of KV cache states in adjacent layers. It decomposes the state vectors into magnitude and direction components, calculates the direction vectors using SLERP \[ [358](https://arxiv.org/html/2505.18458v1#bib.bib358 "")\], and merges the KV caches of adjacent layers to form a merged cache that contains information such as direction vectors, magnitudes, and angles.

Report issue for preceding element

Compared with the traditional method of storing the complete KV data, HCache \[ [151](https://arxiv.org/html/2505.18458v1#bib.bib151 "")\] only stores the hidden states (the size of the hidden states is only half that of the KV cache, and recomputing the KV cache from the hidden states can reduce the computational load). When restoring the state, a bubble-free restoration scheduler is used to concurrently execute the transmission of hidden states and the recomputation from hidden states, maximizing the overall resource utilization.

Report issue for preceding element

KV Indexing
refers to the process of constructing an indexing architecture for the KV Cache to accelerate the query process of the KV Cache.
ChunkAttention \[ [448](https://arxiv.org/html/2505.18458v1#bib.bib448 "")\] organizes the KV cache into a prefix tree using a prefix-aware KV cache (PAKV), sharing key-value tensors of common prefixes to accelerate the corresponding KV query process.
\[ [484](https://arxiv.org/html/2505.18458v1#bib.bib484 "")\] proposes Prefix Sharing Maximization (PSM): By dynamically reordering data columns and rows, it maximizes prefix sharing among requests to improve cache hit rates. Column Reordering sorts columns based on value frequency and size, prioritizing those with more shared prefixes. Row Sorting groups requests with identical prefixes together, further enhancing cache reuse.

Report issue for preceding element

### 2.4 Data Serving for LLM

Report issue for preceding element

Data service encompasses data preprocessing operations carried out after data is transferred from storage to computing nodes and before its actual utilization by the LLM, aiming to facilitate more effective data consumption by the LLM. These data preprocessing operations include: data shuffling, data compression, data packing, and data provenance.

Report issue for preceding element

#### 2.4.1 Data Shuffling

Report issue for preceding element

Data shuffling in data serving means that different data needs to be selected and provided to LLMs at various stages (e.g., in different epochs for pretraining). For example, corresponding training data needs to be supplied according to the training requirements during the training stage; during the RAG stage, corresponding knowledge needs to be supplied based on the degree of relevance to the questions.

Report issue for preceding element

PrinciplesCompared to traditional machine learning, LLM applications are divided into multiple stages, each requiring different types of data to be fed into the model. The main challenge is how to select data that meets the specific requirements of LLMs. In the training stage, current methods provide training data by scoring based on data samples or model states, or by using empirical training strategies. In the RAG stage, data is selected through metrics, rules, or models to supply relevant knowledge to the LLM.Report issue for preceding element

Data Shuffling for Training.
As LLMs continuously trained over new tasks, it may begin to lose its ability to retain early task knowledge, a phenomenon known as catastrophic forgetting \[ [288](https://arxiv.org/html/2505.18458v1#bib.bib288 ""), [287](https://arxiv.org/html/2505.18458v1#bib.bib287 "")\]. To address this, some data supply methods are employed to manage datasets during the training process and provide high-quality data. Meanwhile, some methods, instead of altering the dataset, propose reasonable learning strategies.

Report issue for preceding element

(1) Data Pruning. Data pruning refers that during the training process, partial shuffling is carried out on the training dataset, and high-quality data is retained, so that the model is trained on the data that has not been fully learned and is of high quality.

Report issue for preceding element

Sample Scoring. Some methods \[ [137](https://arxiv.org/html/2505.18458v1#bib.bib137 ""), [66](https://arxiv.org/html/2505.18458v1#bib.bib66 "")\] prune datasets by scoring samples, selecting high-scoring samples for subsequent training. \[ [137](https://arxiv.org/html/2505.18458v1#bib.bib137 "")\] applies the EL2N metric to identify important examples in a dataset, written as χ⁢(xi,yi)=𝔼⁢‖f⁢(xi)−yi‖2𝜒subscript𝑥𝑖subscript𝑦𝑖𝔼subscriptnorm𝑓subscript𝑥𝑖subscript𝑦𝑖2\\chi(x\_{i},y\_{i})=\\mathbb{E}\\\|f(x\_{i})-y\_{i}\\\|\_{2}italic\_χ ( italic\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT , italic\_y start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) = blackboard\_E ∥ italic\_f ( italic\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) - italic\_y start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ∥ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT, where f⁢(xi)𝑓subscript𝑥𝑖f(x\_{i})italic\_f ( italic\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) is the model’s prediction and yisubscript𝑦𝑖y\_{i}italic\_y start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT is the true sample. Based on the computed EL2N values, it periodically prunes irrelevant data during training. \[ [66](https://arxiv.org/html/2505.18458v1#bib.bib66 "")\] extends the EL2N metric to evaluate sample importance, written as χ^e⁢m⁢a⁢(x,y)←α⋅χ^n⁢l⁢u⁢(x,y)+(1−α)⋅χ^e⁢m⁢a⁢(x,y)←subscript^𝜒𝑒𝑚𝑎𝑥𝑦⋅𝛼subscript^𝜒𝑛𝑙𝑢𝑥𝑦⋅1𝛼subscript^𝜒𝑒𝑚𝑎𝑥𝑦\\hat{\\chi}\_{ema}(x,y)\\leftarrow\\alpha\\cdot\\hat{\\chi}\_{nlu}(x,y)+(1-\\alpha)%
\\cdot\\hat{\\chi}\_{ema}(x,y)over^ start\_ARG italic\_χ end\_ARG start\_POSTSUBSCRIPT italic\_e italic\_m italic\_a end\_POSTSUBSCRIPT ( italic\_x , italic\_y ) ← italic\_α ⋅ over^ start\_ARG italic\_χ end\_ARG start\_POSTSUBSCRIPT italic\_n italic\_l italic\_u end\_POSTSUBSCRIPT ( italic\_x , italic\_y ) + ( 1 - italic\_α ) ⋅ over^ start\_ARG italic\_χ end\_ARG start\_POSTSUBSCRIPT italic\_e italic\_m italic\_a end\_POSTSUBSCRIPT ( italic\_x , italic\_y ), where α𝛼\\alphaitalic\_α is a smoothing parameter. Based on extended EL2N values, it periodically selects data subsets for training.

Report issue for preceding element

Model State Scoring. Unlike the aforementioned approach of scoring samples and prune the dataset, some methods \[ [377](https://arxiv.org/html/2505.18458v1#bib.bib377 ""), [56](https://arxiv.org/html/2505.18458v1#bib.bib56 ""), [423](https://arxiv.org/html/2505.18458v1#bib.bib423 ""), [277](https://arxiv.org/html/2505.18458v1#bib.bib277 "")\] prune the distribution of dataset by scoring the model’s state (such as training loss and learning status).

Report issue for preceding element

Moving-one-Sample-out (MoSo) \[ [377](https://arxiv.org/html/2505.18458v1#bib.bib377 "")\] identifies and selects the most informative LLM pre-training samples by assessing the influence of a specific sample on the training loss. The MoSo score measures how the training loss over the dataset 𝒮𝒮\\mathcal{S}caligraphic\_S excluding z𝑧zitalic\_z (i.e., S∖z𝑆𝑧S\\setminus zitalic\_S ∖ italic\_z) would change when the sample z𝑧zitalic\_z is removed.
This approximation measures the agreement between z𝑧zitalic\_z and S∖z𝑆𝑧S\\setminus zitalic\_S ∖ italic\_z, where the sample is considered important and receives a higher score if the gradient of z𝑧zitalic\_z is consistently aligned with the average gradient.

Report issue for preceding element

Similarly, Velocitune \[ [277](https://arxiv.org/html/2505.18458v1#bib.bib277 "")\] is a dynamic domain weight adjustment method based on learning velocity, which is defined as Vt⁢\[i\]=ℓt⁢\[i\]−ℓtarget⁢\[i\]ℓinit⁢\[i\]−ℓtarget⁢\[i\]subscript𝑉𝑡delimited-\[\]𝑖subscriptℓ𝑡delimited-\[\]𝑖subscriptℓtargetdelimited-\[\]𝑖subscriptℓinitdelimited-\[\]𝑖subscriptℓtargetdelimited-\[\]𝑖V\_{t}\[i\]=\\frac{\\ell\_{t}\[i\]-\\ell\_{\\text{target}\[i\]}}{\\ell\_{\\text{init}\[i\]}-\\ell%
\_{\\text{target}\[i\]}}italic\_V start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT \[ italic\_i \] = divide start\_ARG roman\_ℓ start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT \[ italic\_i \] - roman\_ℓ start\_POSTSUBSCRIPT target \[ italic\_i \] end\_POSTSUBSCRIPT end\_ARG start\_ARG roman\_ℓ start\_POSTSUBSCRIPT init \[ italic\_i \] end\_POSTSUBSCRIPT - roman\_ℓ start\_POSTSUBSCRIPT target \[ italic\_i \] end\_POSTSUBSCRIPT end\_ARG, where Vt⁢\[i\]subscript𝑉𝑡delimited-\[\]𝑖V\_{t}\[i\]italic\_V start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT \[ italic\_i \] denotes the learning velocity for domain i𝑖iitalic\_i at step t𝑡titalic\_t, ℓt⁢\[i\]subscriptℓ𝑡delimited-\[\]𝑖\\ell\_{t}\[i\]roman\_ℓ start\_POSTSUBSCRIPT italic\_t end\_POSTSUBSCRIPT \[ italic\_i \] is the current loss for domain i𝑖iitalic\_i, ℓtarget⁢\[i\]subscriptℓtargetdelimited-\[\]𝑖\\ell\_{\\text{target}\[i\]}roman\_ℓ start\_POSTSUBSCRIPT target \[ italic\_i \] end\_POSTSUBSCRIPT is the target loss for domain i𝑖iitalic\_i, predicted by the scaling law \[ [202](https://arxiv.org/html/2505.18458v1#bib.bib202 "")\], ℓinit⁢\[i\]subscriptℓinitdelimited-\[\]𝑖\\ell\_{\\text{init}\[i\]}roman\_ℓ start\_POSTSUBSCRIPT init \[ italic\_i \] end\_POSTSUBSCRIPT is the initial loss for domain i𝑖iitalic\_i, calculated before training starts. The method calculates the learning velocity of each domain and dynamically adjusts the sampling weights, giving more attention to domains with slower learning progress, thereby achieving a balanced learning effect.

Report issue for preceding element

Some methods \[ [56](https://arxiv.org/html/2505.18458v1#bib.bib56 ""), [423](https://arxiv.org/html/2505.18458v1#bib.bib423 "")\] combine reinforcement learning based on scoring the model to adjust the dataset.
ODM \[ [56](https://arxiv.org/html/2505.18458v1#bib.bib56 "")\] is based on the multi-armed bandit algorithm. It regards each data domain as an arm and uses classical reinforcement learning methods. By taking the training loss as the reward function, it optimizes the data mixing ratio online to adapt to training dynamics. That is, it dynamically adjusts the sampling weights of each data domain and preferentially selects data with high information gain and large losses.

Report issue for preceding element

MOS \[ [423](https://arxiv.org/html/2505.18458v1#bib.bib423 "")\] proposes a scoring network that dynamically adjusts the sampling probabilities of different datasets based on the model’s current learning state, combined with reinforcement learning, to alter the distribution of training data. This adjustment is guided by three reward functions: (i)𝑖(i)( italic\_i ) Transferability for measuring the similarity (e.g, cosine distance) between datasets as the reward. (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) Learning difficulty for measuring the perplexity changes. (i⁢i⁢i)𝑖𝑖𝑖(iii)( italic\_i italic\_i italic\_i ) Learning trajectory for smoothing the reward values using Exponential Moving Average (EMA) to more stably optimize the sampling distribution.

Report issue for preceding element

(2) Training Strategy.
In addition to directly prune the dataset during training, appropriate learning strategies can also alleviate catastrophic forgetting.  \[ [123](https://arxiv.org/html/2505.18458v1#bib.bib123 "")\] found that different abilities vary with data volume, with mixed data improving abilities at low resources and causing conflicts at high resources. Thus, DMT \[ [211](https://arxiv.org/html/2505.18458v1#bib.bib211 "")\] is proposed, which first fine-tunes on a specific dataset and then fine-tunes on mixed data to effectively balance general and specialized abilities and mitigate conflicts and forgetting. It proposes a strategy where training data are sorted based on criteria like input length, attention weights and training loss, allowing the model to gradually learn from simple tasks to more complex ones.

Report issue for preceding element

Data Selection for RAG.
In the RAG stage, it is necessary to retrieve the stored knowledge (see details in [2.3.3](https://arxiv.org/html/2505.18458v1#S2.SS3.SSS3 "2.3.3 Data Organization ‣ 2.3 Data Storage for LLM ‣ 2 Data Management for LLM (DATA4LLM) ‣ Data × LLM: From Principles to Practices")) and provided the retrieved results to the LLM. During this process, it needs to ensure the effectiveness of the retrieved results in order to obtain better answers from the LLM\[ [281](https://arxiv.org/html/2505.18458v1#bib.bib281 "")\]. Currently, the retrieval quality is mainly guaranteed through RAG knowledge filtering and RAG knowledge re-ranking.

Report issue for preceding element

(1) RAG Knowledge Filtering.
RAG knowledge filtering refers to filtering out documents with poor relevance after retrieval. Some methods \[ [281](https://arxiv.org/html/2505.18458v1#bib.bib281 ""), [115](https://arxiv.org/html/2505.18458v1#bib.bib115 ""), [87](https://arxiv.org/html/2505.18458v1#bib.bib87 "")\] use a model as a judge to filter documents. \[ [281](https://arxiv.org/html/2505.18458v1#bib.bib281 "")\] uses small language models (SLMs) as filters, performing preliminary predictions and evaluating difficulty. For easy samples, the SLM’s predictions are used as the final decision; for difficult samples, the top N most likely labels are selected from the SLM’s predictions for subsequent re-ranking. In Chatlaw \[ [115](https://arxiv.org/html/2505.18458v1#bib.bib115 "")\], after retrieving relevant information, the LLM evaluates the retrieved content. Only content that is deemed highly relevant after evaluation is used to generate the final response, effectively reducing interference from irrelevant or incorrect information. MAIN-RAG \[ [87](https://arxiv.org/html/2505.18458v1#bib.bib87 "")\] collaboratively filters and scores retrieved documents by leveraging multiple LLM agents to enhance relevance and reduce noise. The framework adopts a dynamic filtering mechanism that uses score distributions to adjust relevance thresholds, ensuring high recall of relevant documents while minimizing computational overhead.

Report issue for preceding element

(2) RAG Knowledge Re-ranking.
After filtering, multiple documents may remain, requiring re-ranking of the retrieval results to place the most relevant ones at the top for more accurate model output. Research on \[ [128](https://arxiv.org/html/2505.18458v1#bib.bib128 "")\] shows that using a large model for re-ranking performs better than methods like Maximum Marginal Relevance (MMR) and Cohere re-ranking. For large model re-ranking, general-purpose large language models (e.g., GPT) can be used directly, or specialized zero-shot re-ranking models such as Cohere rerank  \[ [12](https://arxiv.org/html/2505.18458v1#bib.bib12 "")\] or RankVicuna \[ [319](https://arxiv.org/html/2505.18458v1#bib.bib319 "")\] can be employed. The latest ASRank \[ [47](https://arxiv.org/html/2505.18458v1#bib.bib47 "")\] leverages pre-trained LLM to compute the matching probability between document answers and answer cues, scoring and re-ranking the retrieved documents.

Report issue for preceding element

#### 2.4.2 Data Compression

Report issue for preceding element

Data compression refers to compressing the input data for the model.
Previous studies have shown that prompts are crucial for triggering LLM domain-specific knowledge, and prompts are typically designed based on specific tasks (including chain-of-thought, context learning, and historical dialogues). As the complexity of chain-of-thought, context learning, and RAG increase, longer prompts are required \[ [190](https://arxiv.org/html/2505.18458v1#bib.bib190 "")\]. However, overly long prompts may lead to higher response latency, increased costs, and even exceeding the maximum token limit. Existing methods mainly compress the model inputs in two aspects. Some methods \[ [435](https://arxiv.org/html/2505.18458v1#bib.bib435 ""), [102](https://arxiv.org/html/2505.18458v1#bib.bib102 ""), [352](https://arxiv.org/html/2505.18458v1#bib.bib352 ""), [201](https://arxiv.org/html/2505.18458v1#bib.bib201 ""), [338](https://arxiv.org/html/2505.18458v1#bib.bib338 "")\] compress the retrieved results in the RAG stage and then put them into the prompt, while other methods compress the entire prompt \[ [190](https://arxiv.org/html/2505.18458v1#bib.bib190 ""), [191](https://arxiv.org/html/2505.18458v1#bib.bib191 ""), [304](https://arxiv.org/html/2505.18458v1#bib.bib304 ""), [294](https://arxiv.org/html/2505.18458v1#bib.bib294 ""), [103](https://arxiv.org/html/2505.18458v1#bib.bib103 "")\].

Report issue for preceding element

PrinciplesCompared to traditional machine learning, LLMs often require longer inputs, and in some cases, the input must be compressed to fit into the model. The main challenge is how to compress the input without losing important information. Current methods mainly achieve this through compression based on information entropy, rule-based templates, or model-driven approaches.Report issue for preceding element

RAG Knowledge Compression
The retrieved RAG knowledge can be compressed by a model to make small texts carry more information. Techniques like RECOMP \[ [435](https://arxiv.org/html/2505.18458v1#bib.bib435 "")\], CompAct \[ [352](https://arxiv.org/html/2505.18458v1#bib.bib352 "")\], and FAVICOMP \[ [201](https://arxiv.org/html/2505.18458v1#bib.bib201 "")\] adopt rule-based RAG context compression schemes, where predefined rules or templates explicitly guide the model to extract key information and remove redundant content. Alternatively, methods like xRAG \[ [102](https://arxiv.org/html/2505.18458v1#bib.bib102 "")\] and COCOM \[ [338](https://arxiv.org/html/2505.18458v1#bib.bib338 "")\] use soft prompt-based RAG context compression schemes, where learnable parameters (such as the modality projector W in xRAG or the overall model training in COCOM) enable implicit vector learning. These implicit vectors dynamically adjust attention weights when the model processes input, allowing the model to adaptively optimize context representations under context compression.

Report issue for preceding element

Prompt Compression.
Prompt compression means that after the retrieved knowledge is put into the Prompt, the entire Prompt will be compressed.

Report issue for preceding element

(1) Metric-Based Compression. Some studies \[ [190](https://arxiv.org/html/2505.18458v1#bib.bib190 ""), [191](https://arxiv.org/html/2505.18458v1#bib.bib191 "")\], based on the hypothesis that a vast amount of knowledge is stored in the model parameters, have proposed methods to compress prompts while minimizing information loss.
LLMLingua \[ [190](https://arxiv.org/html/2505.18458v1#bib.bib190 "")\] uses a self-information criterion to remove redundant tokens from the original prompt. By quantifying the negative logarithmic probability (information entropy) of each token, LLMLingua identifies and removes tokens that can be predicted from the model’s inherent knowledge, thereby shortening the prompt while retaining essential context.

Report issue for preceding element

LLMLingua’s extended version, LongLLMLingua \[ [191](https://arxiv.org/html/2505.18458v1#bib.bib191 "")\], uses a dual-granularity compression strategy:
(i)𝑖(i)( italic\_i ) Coarse-grained compression initially filters key information at the document level to provide more focused content for fine-grained compression;
(i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) Fine-grained compression further optimizes at the token level to precisely retain key information.
These two strategies work together to improve the quality of the prompt and model performance. LongLLMLingua also assigns different “compression budgets” to documents based on their importance, aiming to achieve the best global compression effect.

Report issue for preceding element

(2) Finetuned-Model-Based Compression. Some methods \[ [304](https://arxiv.org/html/2505.18458v1#bib.bib304 ""), [294](https://arxiv.org/html/2505.18458v1#bib.bib294 ""), [103](https://arxiv.org/html/2505.18458v1#bib.bib103 "")\] use fine-tuned models to compress prompts.
Unlike direct pruning strategies, LLMLingua-2 \[ [304](https://arxiv.org/html/2505.18458v1#bib.bib304 "")\] defines prompt compression as a problem of classifying tokens and trains a dedicated model for compression. It uses a Transformer encoder to capture bidirectional contextual information, ensuring that the compressed prompt is faithful to the original. \[ [294](https://arxiv.org/html/2505.18458v1#bib.bib294 "")\] proposes a technique called ’gisting’, where a language model is trained to condense the prompt into a compact ’gist token’. These tokens encapsulate the core semantic content of the prompt and can be cached for later use. This method achieves a compression rate of up to 26 times.  \[ [103](https://arxiv.org/html/2505.18458v1#bib.bib103 "")\] suggests a method to transform pre-trained language models into AutoCompressors. The AutoCompressor compresses long contexts into summary vectors, and training is performed on the model parameters using these summary vectors.

Report issue for preceding element

#### 2.4.3 Data Packing

Report issue for preceding element

Data Packing aims to address the requirement for uniform sequence lengths in LLMs’ training inputs, which combines short texts in an appropriate way to enhance text coherence and reduce the number of padding tokens. In this way, we can avoid the excessive truncation caused by the drawbacks of simple concatenation and splitting methods \[ [117](https://arxiv.org/html/2505.18458v1#bib.bib117 "")\].

Report issue for preceding element

Short Sequence Insertion. Some methods \[ [117](https://arxiv.org/html/2505.18458v1#bib.bib117 ""), [260](https://arxiv.org/html/2505.18458v1#bib.bib260 "")\] involve inserting short sequences into long sequences to minimize padding. The Best-fit Packing method \[ [117](https://arxiv.org/html/2505.18458v1#bib.bib117 "")\] first splits long documents according to the model’s context length, then sorts all document blocks in descending order of length. For each document block, it selects the training sequence set with the smallest remaining capacity that can accommodate it. \[ [260](https://arxiv.org/html/2505.18458v1#bib.bib260 "")\] prioritizes long documents and uses a greedy algorithm to fill remaining space with short document segments (sequences), reducing padding and minimizing document concatenation to lower contextual noise.

Report issue for preceding element

PrinciplesCompared to traditional machine learning, LLMs place higher demands on the semantic quality of training data. Additionally, due to the requirement for uniform input lengths, a key challenge is maintaining semantic integrity without excessive truncation. Existing techniques tackle this through short-sequence insertion, sequence concatenation, and semantic-aware composition. However, it remains crucial to account for the impact of these data packaging operations on overall training efficiency.Report issue for preceding element

Sequence Combination Optimization. Some methods \[ [219](https://arxiv.org/html/2505.18458v1#bib.bib219 ""), [317](https://arxiv.org/html/2505.18458v1#bib.bib317 "")\] optimize sequence combinations for efficient packing. \[ [219](https://arxiv.org/html/2505.18458v1#bib.bib219 "")\] proposes two efficient sequence packing algorithms:
(1) The Shortest Pack First Histogram Packing (SPFHP) uses a sequence length histogram, sorts sequences from long to short, and applies a worst-fit algorithm to prioritize placing the histogram intervals into the remaining largest “packs”, while limiting packing depth to avoid creating excessive small packs, thus improving space utilization.
(2) The Non-Negative Least Squares Histogram Packing (NNLSHP) converts the packing problem into a non-negative least squares problem, using dynamic programming to enumerate reasonable sequence combination strategies, constructing a packing matrix to determine the strategy’s repetition count. It also assigns small weights to short sequences’ residuals to reduce long sequence leftovers, achieving efficient packing. \[ [317](https://arxiv.org/html/2505.18458v1#bib.bib317 "")\] splits documents into multiple fixed-length “buckets” based on their length, ensuring that each sequence comes from the same document to avoid cross-document attention issues. Additionally, by combining Variable Sequence Length Curriculum (VSL), different lengths of sequences are dynamically sampled during training to maintain a consistent total token count.

Report issue for preceding element

Semantic-Based Packing. Some methods \[ [369](https://arxiv.org/html/2505.18458v1#bib.bib369 ""), [353](https://arxiv.org/html/2505.18458v1#bib.bib353 "")\] improve data coherence through semantic-based data packing. \[ [353](https://arxiv.org/html/2505.18458v1#bib.bib353 "")\] reorders pretraining data by combining semantically related documents into coherent input contexts, allowing the LLM to read and reason across document boundaries. Similarly, SPLICE \[ [369](https://arxiv.org/html/2505.18458v1#bib.bib369 "")\] randomly selects a document as the root document, and in a breadth-first manner, uses retrieval methods like BM25 and Contriever (trained from a mix of Wiki and CCNet data) to retrieve k𝑘kitalic\_k similar documents, adding them to the training sample until the maximum length is reached. Finally, the tree structure is flattened using a specific tree traversal strategy to generate the training example.

Report issue for preceding element

#### 2.4.4 Data Provenance

Report issue for preceding element

Data Provenance is the process of tracking the sources, transformations, and lineage of data, which is increasingly recognized critical in ensuring the reliability, transparency, and accountability of LLM data \[ [54](https://arxiv.org/html/2505.18458v1#bib.bib54 "")\].

Report issue for preceding element

PrinciplesCompared with traditional machine-learning models, LLMs demand heightened safeguards for output security owing to their powerful generative capabilities. The central challenge is to preserve output integrity without degrading quality. Current solutions embed watermarks or deploy statistical-detection techniques to reveal any tampering.Report issue for preceding element

Embedding Markers. Current data provenance methods \[ [488](https://arxiv.org/html/2505.18458v1#bib.bib488 ""), [106](https://arxiv.org/html/2505.18458v1#bib.bib106 ""), [257](https://arxiv.org/html/2505.18458v1#bib.bib257 ""), [213](https://arxiv.org/html/2505.18458v1#bib.bib213 "")\] generally modify the generation logic to embed covert markers into the text. This is done in a way that does not disrupt the text itself, thereby providing a medium for tracing the origin of the data.

Report issue for preceding element

Bileve \[ [488](https://arxiv.org/html/2505.18458v1#bib.bib488 "")\] enhances the traceability and integrity of text by embedding two distinct levels of signals: (1) Statistical signal embedded globally to detect whether the text originates from a specific model. (2) Content-related signature embedded within each generation unit to verify if the text has been tampered with. During detection, the validity of the signature is first verified; if the signature is invalid, a statistical test is then used to determine whether the text comes from the target model.

Report issue for preceding element

Unlike Bileve that emphasizes strict traceability after text tampering, \[ [106](https://arxiv.org/html/2505.18458v1#bib.bib106 "")\] focuses on embedding watermarks in a way that preserves the quality of the generated output. It embeds hidden markers that can only be detected by individuals possessing a specific key, while remaining imperceptible to others that the text has been altered. Specifically, the method employs a pseudo-random function (PRF, used to generate seemingly random numbers) to determine the shuffling of each output word, ensuring that the generated text is statistically indistinguishable from the original model’s output. During detection, the presence of hidden markers is ascertained by calculating a score for each word in the text (based on the numbers generated by the pseudo-random function).

Report issue for preceding element

Unlike previous approaches, UPV  \[ [257](https://arxiv.org/html/2505.18458v1#bib.bib257 "")\] introduces a watermarking method that enables detection without requiring access to the key used during generation, thereby eliminating the risk of key leakage. It employs two independent neural networks for watermarking. During text generation, the watermark generation network utilizes an embedding module and a fully connected classifier to predict watermark signals based on token information within a sliding window, and accordingly adjusts the language model’s output distribution. For detection, an LSTM-based network takes the text sequence as input and identifies the watermark, leveraging shared token embedding parameters with the generation network.

Report issue for preceding element

Compared to methods that require specific keys for detection,  \[ [131](https://arxiv.org/html/2505.18458v1#bib.bib131 "")\] embeds a special type of watermark into text generated by language models, which can be detected by anyone without the need for any secret information. It selects specific lexical combinations (rejection sampling, ensuring that the embedding of the marker does not affect the naturalness of the text) during text generation, in conjunction with an error correction mechanism (error-correcting codes, allowing the marker to be recovered even after partial modification of the text), to embed an encrypted signature (public key signature, ensuring the non-forgeability of the marker) into the text. During detection, one only needs to extract these specific lexical combinations from the text and verify the validity of the signature to determine whether the text contains the marker.

Report issue for preceding element

Statistical Provenance. Unlike the aforementioned methods that rely on detecting special markers for tracing the origin,  \[ [213](https://arxiv.org/html/2505.18458v1#bib.bib213 "")\] achieve data provenance through the statistical information of the vocabulary. Specifically, before generating each word, the model randomly divides the vocabulary into two parts (green-listed and red-listed tokens) and tends to favor the shuffling of green-listed tokens during the generation process (green-listed tokens are a randomly selected subset of the vocabulary). By employing statistical tests (a mathematical method used to determine whether text adheres to specific rules), it is possible to detect whether the proportion of green-listed tokens in the text is abnormal, thereby ascertaining if the text is machine-generated.

Report issue for preceding element

## 3 LLM for Data Management

Report issue for preceding element

After preparing the LLMs with carefully processed / stored / served data, we next introduce the LLM techniques that can be utilized to enhance data management tasks, including data manipulation, data analysis, and data system optimization.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2505.18458v1/x7.png)Figure 8: Overview of LLM4DATA Techniques.Report issue for preceding element

### 3.1 LLM for Data Manipulation

Report issue for preceding element

LLM can be employed to explore and prepare appropriate data for non-LLM-oriented tasks, such as data cleaning for classification tasks, data integration for extracting well-structured tables from unstructured sources, and data discovery for identifying relevant datasets.
Unlike data preparation pipelines designed specifically for LLM applications, these methods focus on enhancing the quality and utility of data for downstream analytical or machine learning tasks.

Report issue for preceding element

#### 3.1.1 LLM for Data Cleaning

Report issue for preceding element

Data cleaning focuses on transforming corrupted or low-quality data into a reliable form suitable for downstream applications (e.g., statistical analysis or training machine learning models).
It encompasses a range of tasks such as handling missing values, correcting typos, resolving formatting inconsistencies, and addressing dependency violations.
These tasks are typically categorized into data standardization, error detection and correction, and data imputation.

Report issue for preceding element

Traditional data cleaning methods depend on rigid rules and constraints (e.g., zip code validation), demanding substantial manual effort and domain expertise (e.g., schema knowledge in financial data) \[ [238](https://arxiv.org/html/2505.18458v1#bib.bib238 ""), [440](https://arxiv.org/html/2505.18458v1#bib.bib440 "")\].
Additionally, they often require domain-specific training, which restricts their generalizability \[ [63](https://arxiv.org/html/2505.18458v1#bib.bib63 "")\].
Recent studies show that large language models (LLMs) can address these limitations by offering natural language interfaces that reduce manual and programming effort, eliminate the need for complex runtime environments, and support seamless integration of domain knowledge. These methods primarily target the following tasks.

Report issue for preceding element

Data Standardization.
Data standardization involves converting diverse, inconsistent, or non-conforming values into a consistent format to ensure reliable analysis and effective downstream processing.
Existing methods use either structured LLM prompting for specific cleaning operations or LLM agents for automated pipeline generation.

Report issue for preceding element

(1) Prompt Based End-to-End Standardization.
The first approach constructs well-structured prompts with explicit standardization instructions and employs advanced prompting techniques (e.g., Chain-of-Thought) to improve the effectiveness of LLM-based standardization methods.
For example, LLM-GDO \[ [280](https://arxiv.org/html/2505.18458v1#bib.bib280 "")\] utilizes user-defined prompts (UDPs), including in-context learning examples, to implement LLM-based operators that replace traditional user-defined functions (UDFs) across various standardization tasks (e.g., normalizing numerical values).
This method simplifies logic implementation and facilitates the seamless integration of domain knowledge.
Evaporate \[ [63](https://arxiv.org/html/2505.18458v1#bib.bib63 "")\] employs LLMs to transform semi-structured documents into structured views through two main strategies: (i) Evaporate-Direct, which prompts the LLM to extract values directly, and (ii) Evaporate-Code, which guides the LLM to synthesize extraction code and ensembles multiple candidate functions using weak supervision to improve output quality while maintaining low cost.

Report issue for preceding element

(2) Agent Based Operation and Pipeline Generation.
To address the inefficiencies of LLM-based solutions, such as the reliance on multi-turn prompts and expert-level prompt engineering, the second method employs LLM agents to automatically generate cleaning operations and orchestrate end-to-end pipelines.
For instance, CleanAgent \[ [320](https://arxiv.org/html/2505.18458v1#bib.bib320 "")\] integrates domain-specific APIs with autonomous agents to execute a standardization pipeline that includes API call generation (e.g., clean\_date(df, ‘‘Admission Date’’, ‘‘MM/DD/YYYY’’)) and iterative code execution.
Similarly, AutoDCWorkflow \[ [238](https://arxiv.org/html/2505.18458v1#bib.bib238 "")\] adopts LLM agents to construct pipelines for resolving duplicates and inconsistent formats.
The agent performs step-by-step reasoning to identify relevant columns, evaluate data quality, and generate appropriate operations (e.g., upper() and trim()), while leveraging tools such as OpenRefine for execution and feedback.

Report issue for preceding element

Data Error Processing.
Given a data entry, error processing typically involves two steps: detecting erroneous values and correcting these values.
Typical errors include typos, invalid formats, type mismatches, numeric outliers, and dependency violations.
Existing methods generally fall into two categories: employing LLMs for direct end-to-end error processing, or enhancing context models to better guide the detection and correction process.

Report issue for preceding element

(1) Prompt Based End-to-End Error Processing.
To support end-to-end data error processing, the first approach employs prompting techniques to either directly handle data errors or generate the corresponding processing functions.
For instance, Multi-News+superscriptMulti-News\\text{Multi-News}^{+}Multi-News start\_POSTSUPERSCRIPT + end\_POSTSUPERSCRIPT\[ [104](https://arxiv.org/html/2505.18458v1#bib.bib104 "")\] employs Chain-of-Thought (CoT) prompting, majority voting inspired by human annotation practices, and self-consistency checks to enhance classification accuracy and transparency when processing noisy documents.
Similarly, Cocoon \[ [468](https://arxiv.org/html/2505.18458v1#bib.bib468 "")\] constructs semantic detection prompts and divides datasets into batches, allowing the LLM to analyze sampled values (e.g., 1,000 entries per column) and identify typos or inconsistencies (e.g., “mapping English” →→\\rightarrow→ “eng”), thereby supporting batch-wise data cleaning.
GIDCL \[ [440](https://arxiv.org/html/2505.18458v1#bib.bib440 "")\] adopts a creator-critic framework in which the LLM iteratively refines lightweight error detection models and generates pseudo-labeled data using handcrafted prompts and in-context examples to produce both detection and correction functions, further enhanced by structural correlation learning with Graph Neural Networks (GNNs).

Report issue for preceding element

(2) LLM Based Cleaning Context Enrichment.
To address the inefficiencies and limited scalability of manual cleaning context model construction in dynamic environments, the second approach leverages LLMs to enrich data cleaning context models and more effectively capture semantic relationships within the data.
For example, LLMClean \[ [78](https://arxiv.org/html/2505.18458v1#bib.bib78 "")\] proposes an automated LLM-based method for generating context models by extracting ontological functional dependencies (OFDs) using both prompt ensembling and fine-tuned LLMs (e.g., Llama-2).
The extracted OFDs are then used to identify data errors (e.g., value inconsistencies) and guide LLM-based repairs through iterative feedback from integrated correction tools such as Baran.
LLMErrorBench \[ [74](https://arxiv.org/html/2505.18458v1#bib.bib74 "")\] employs LLM agents equipped with Python (via IPython) and prompted with task-specific instructions and contextual hints (e.g., error locations) to explore, modify, and repair datasets iteratively.
Corrections (e.g., value replacement, missing data handling) are guided by performance feedback from pre-defined code execution and evaluation pipelines.

Report issue for preceding element

(3) Fine-tuning Based End-to-End Error Processing.
To improve error correction accuracy while preserving computational efficiency and model adaptability, the third approach fine-tunes LLMs to capture dataset-specific patterns and dependencies that are typically difficult to model through prompting alone.
For example, GIDCL \[ [440](https://arxiv.org/html/2505.18458v1#bib.bib440 "")\] fine-tunes a local LLM (e.g., Mistral-7B) using Low-Rank Adaptation (LoRA) to optimize error correction, constructing training data from labeled tuples and pseudo-labeled tuples generated via LLM-based augmentation, with each training instance formatted as a context-enriched prompt comprising: (i) an instruction (e.g., “Correct the ProviderID to a valid numeric format”), (ii) a serialized erroneous cell with row and column context (e.g., “<COL>ProviderID<VAL>1x1303...”), (iii) in-context learning demonstrations (e.g., “bxrmxngham →→\\rightarrow→ birmingham”), and (iv) retrieval-augmented examples from the same cluster (e.g., clean tuples via k-means).

Report issue for preceding element

Data Imputation.
Given a data entry with missing attribute values (e.g., NULL), data imputation aims to infer the missing values using available contextual information accurately.
Existing methods either (i) use structured prompts to convey contextual hints to LLM, or (ii) apply retrieval-augmented generation (RAG) to integrate relevant external data.

Report issue for preceding element

(1) Prompt Based End-to-End Imputation.
To incorporate contextual information for imputing missing values, the first approach constructs structured prompts.
For example, RetClean \[ [129](https://arxiv.org/html/2505.18458v1#bib.bib129 "")\] enhances LLM effectiveness by serializing each tuple into a formatted representation (e.g., “\[Name: John; Age: 25; Gender: NULL\]”) and pairing it with a targeted question such as “What is the correct value for Gender?”.
This prompt design enables the LLM to generate accurate, context-aware missing values.

Report issue for preceding element

(2) RAG Assisted Localized Imputation.
To enable online LLMs in handling unseen, domain-specific, or private datasets, the second approach adopts the retrieval-augmented generation (RAG) paradigm.
For example, RetClean \[ [129](https://arxiv.org/html/2505.18458v1#bib.bib129 "")\] introduces a retrieval-based data cleaning framework that indexes a data lake using both syntactic (Elasticsearch) and semantic (Faiss/Qdrant) methods.
It retrieves the top-k𝑘kitalic\_k relevant tuples, reranks them (e.g., using ColBERT), and then leverages an LLM to infer missing values, while maintaining lineage tracking for transparency and traceability.

Report issue for preceding element

#### 3.1.2 LLM for Data Integration

Report issue for preceding element

Data integration aims to align elements across heterogeneous datasets to enable unified access, analysis, and knowledge extraction.
For instance, it includes identifying tables or records that correspond to the same real-world entity.
Moreover, it facilitates downstream tasks such as data augmentation by establishing semantic relationships across sources.

Report issue for preceding element

Traditional integration methods often struggle with semantic ambiguities and conflicts, particularly in complex integration scenarios without domain-specific knowledge \[ [278](https://arxiv.org/html/2505.18458v1#bib.bib278 "")\].
Furthermore, classical models (e.g., pretrained models) generally require large amounts of task-specific training data and tend to degrade in performance when encountering out-of-distribution entities \[ [309](https://arxiv.org/html/2505.18458v1#bib.bib309 "")\].
In contrast, recent studies have shown that LLMs possess strong semantic understanding, enabling them to uncover correlations across datasets and incorporate domain-specific knowledge, thereby offering robust generalization across diverse integration tasks.

Report issue for preceding element

Entity Matching.
The goal of entity matching is to determine whether two entries refer to the same real-world entity.
Existing methods leverage LLMs through well-structured prompts and advanced reasoning mechanisms, incorporate multiple models for collaborative matching, and apply multi-task fine-tuning to further enhance performance.

Report issue for preceding element

(1) Prompt Based End-to-End Matching.
To improve LLM’s effectiveness on matching tasks, the first approach crafts well-structured prompts and integrates auxiliary mechanisms to strengthen the robustness of the reasoning process.

Report issue for preceding element

∙∙\\bullet∙ _Manually-Crafted Prompt._
This method incorporates detailed instructions and illustrative examples into the prompts to guide LLM in performing entity matching more effectively.
For example, MatchGPT \[ [309](https://arxiv.org/html/2505.18458v1#bib.bib309 "")\] evaluates the performance of both open-source and closed-source LLMs (e.g., Llama 3.1 and GPT-4o mini) with (i) different prompt designs, (ii) the selection of in-context demonstrations, (iii) automatic generation of matching rules, and (iv) fine-tuning LLMs using a shared pool of training data.
To reduce inference costs, BATCHER \[ [134](https://arxiv.org/html/2505.18458v1#bib.bib134 "")\] introduces a batch prompting method that allows multiple entity pairs to be processed simultaneously.
It optimizes in-context learning by (i) grouping entity pairs into a single prompt and (ii) applying a greedy cover-based strategy to select demonstrations such that each query in the batch is semantically close to at least one example.

Report issue for preceding element

∙∙\\bullet∙ _Pseudo-Code Guided Reasoning._
To mitigate hallucinations arising from over-reliance on an LLM’s internal knowledge, this method integrates external formalized representations to enhance the robustness and reliability of the reasoning process.
For example, KcMF \[ [438](https://arxiv.org/html/2505.18458v1#bib.bib438 "")\] guides LLMs using expert-designed pseudo-code instructions structured as a sequence of if-then-else logical conditions, combined with external domain knowledge (e.g., datasets and examples).
It further adopts an ensemble strategy by generating outputs from different knowledge sources (e.g., Wikidata and domain-specific datasets) and applies a voting mechanism to aggregate results, improving consistency and accuracy.

Report issue for preceding element

(2) End-to-End Matching with Multi-Model Collaboration.
To leverage the strengths of different models across tasks, the second approach employs collaborative entity matching using models of varying sizes.
For example, COMEM \[ [407](https://arxiv.org/html/2505.18458v1#bib.bib407 "")\] introduces a compound entity matching framework that combines multiple strategies with LLM collaboration to address global consistency, which is often ignored in binary matching.
It employs (i) a local strategy using a medium-sized LLM (3B-11B) as a matcher or comparator to rank top-k𝑘kitalic\_k candidates via bubble sort, reducing position bias and context length dependency; and (ii) a global selection strategy using a stronger LLM (e.g., GPT-4o) to refine top-k𝑘kitalic\_k candidates by modeling inter-record interactions.

Report issue for preceding element

(3) Localized LLM Fine-tuning of Multi-Task Learning.
To enhance the generalization capability of local LLMs, the last approach integrates multiple task-specific datasets within a unified multi-task instruction tuning framework.
For example, Jellyfish \[ [461](https://arxiv.org/html/2505.18458v1#bib.bib461 "")\] applies parameter-efficient instruction tuning to locally deployed LLMs (7B-13B) across diverse data processing tasks.
It employs techniques such as chain-of-thought prompting over task-specific serialized data and reasoning data distillation, using explanation traces generated by a larger mixture-of-experts model (Mixtral-8x7B-Instruct) to guide the learning process.

Report issue for preceding element

Schema Matching.
The objective of schema matching is to identify correspondences between elements of different database schemas (e.g., matching attribute names “employee ID” and “staff number”).
Existing approaches directly apply prompting techniques to enable LLMs to perform end-to-end matching, utilize retrieval-augmented generation (RAG) to enhance contextual understanding, and employ LLM agents to orchestrate the overall matching workflow.

Report issue for preceding element

(1) Prompt Based End-to-End Matching.
To facilitate schema matching without requiring rigid code implementations, the first method employs various prompting techniques to guide LLM in identifying the desired mappings.
For example, LLMSchemaBench \[ [305](https://arxiv.org/html/2505.18458v1#bib.bib305 "")\] applies prompt engineering techniques to interact with LLMs, defining four task scopes that differ in the level of contextual information included in the prompts.
The prompts are constructed using established design patterns: the persona pattern (e.g., instructing the LLM to act as a schema matcher), meta language creation (e.g., explicitly defining valid match criteria), Chain-of-Thought reasoning, and the output automater (e.g., generating structured JSON outputs for downstream automation).

Report issue for preceding element

(2) End-to-End Matching via Context-Enriched RAG.
To enrich the matching context and improve accuracy, the second method integrates retrieval-augmented generation (RAG) with various strategies.
For example, Magneto \[ [268](https://arxiv.org/html/2505.18458v1#bib.bib268 "")\] employs a retrieve-rerank framework that combines small pre-trained language models (SLMs) with LLMs to deliver cost-effective and generalizable schema matching.
SLMs serve as candidate retrievers, generating an initial ranked list of potential matches from the target table for each input column, which is then refined by LLMs acting as rerankers to improve accuracy.
KG-RAG4SM \[ [278](https://arxiv.org/html/2505.18458v1#bib.bib278 "")\] incorporates multiple retrieval strategies, including vector-based, graph traversal-based, and query-based, to extract relevant subgraphs from knowledge graphs (KGs).
These subgraphs are further refined through ranking mechanisms and used to augment LLM prompts, thereby improving schema matching performance through enriched contextual input.

Report issue for preceding element

(3) Agent-Based Matching Workflow Orchestration.
To address complex matching patterns, the final approach leverages LLM-based agents to orchestrate the end-to-end matching workflow.
For example, Agent-OM \[ [321](https://arxiv.org/html/2505.18458v1#bib.bib321 "")\] employs two LLM agents (i.e., Retrieval Agent and Matching Agent) to control the workflow by decomposing tasks via Chain-of-Thought (CoT) prompting, invoking specialized tools (e.g., syntactic/lexical/semantic retrievers and matchers), and accessing a hybrid database (relational + vector) for memory storage and retrieval.
Harmonia \[ [343](https://arxiv.org/html/2505.18458v1#bib.bib343 "")\] leverages LLM-based agents to orchestrate data harmonization tasks, combining predefined data integration primitives (e.g., schema matching, value matching) with on-demand code generation when the primitives are insufficient.
In addition, it employs techniques like ReAct for reasoning and action planning, interactive user feedback for error correction, and declarative pipeline specifications for reproducibility.

Report issue for preceding element

#### 3.1.3 LLM for Data Discovery

Report issue for preceding element

Data discovery focuses on identifying relationships within datasets through tasks like data annotation (e.g., column type classification) and profiling (e.g., metadata generation).
Unlike data analysis, which emphasizes statistical computations or factual answer generation, data discovery enables deeper semantic understanding critical for downstream applications such as integration, search, and recommendation.

Report issue for preceding element

Existing data discovery methods face two limitations.
First, they typically consider limited interaction between queries and tables \[ [164](https://arxiv.org/html/2505.18458v1#bib.bib164 "")\].
Second, many of these approaches rely heavily on large training datasets, struggle with distribution shifts, and fail to generalize to rare or domain-specific data \[ [143](https://arxiv.org/html/2505.18458v1#bib.bib143 ""), [218](https://arxiv.org/html/2505.18458v1#bib.bib218 "")\].
Recent studies have shown that LLMs can effectively address these challenges by generating high-quality metadata, enriching dataset context, and supporting natural language interfaces for data discovery tasks.

Report issue for preceding element

Data Profiling.
Data profiling typically involves characterizing a given dataset by generating additional information (e.g., dataset descriptions).
Recent methods often employ prompting techniques to guide LLM in generating such metadata by leveraging their pretrained knowledge and contextual understanding.

Report issue for preceding element

(1) Manually Crafted Profiling Prompt Engineering.
To profile different aspects of a dataset without extensive manual effort or code implementation, the first approach relies on a set of manually crafted profiling prompts.
For example, AutoDDG \[ [463](https://arxiv.org/html/2505.18458v1#bib.bib463 "")\] utilizes LLM with carefully designed prompts to generate two types of descriptions (i.e., User-Focused Descriptions (UFDs) for readability and Search-Focused Descriptions (SFDs) for search optimization) tailored to the dataset’s content and intended usage.
LEDD \[ [58](https://arxiv.org/html/2505.18458v1#bib.bib58 "")\] employs carefully crafted prompts to support core data discovery tasks in data lakes.
For hierarchical cataloging, prompts instruct LLM to summarize data clusters into semantically meaningful categories.
For semantic search, prompts refine natural language queries before embedding and retrieval.
For real-time relation analysis, prompts guide LLM in comparing expanded graph nodes and describing inter-table relationships.

Report issue for preceding element

(2) RAG Assisted Context Enrichment.
To enhance retrieval effectiveness across diverse query types, the second method adopts a hybrid approach that integrates diverse retrieval techniques.
For example, Pneuma \[ [72](https://arxiv.org/html/2505.18458v1#bib.bib72 "")\] adopts a RAG framework to retrieve relevant tables from databases, data lakes, or repositories based on natural language queries.
It combines LLMs with traditional retrieval techniques, such as full-text and vector search, using LLMs for both schema narration (i.e., generating meaningful column descriptions) and as judges to refine and rerank retrieved results.

Report issue for preceding element

Data Annotation.
Data annotation involves assigning semantic or structural labels to data elements, such as identifying column types (e.g., Manufacturer or birthDate from the DBPedia ontology).
Recent methods leveraging LLM typically design prompts with task-specific annotation instructions.
Additionally, some approaches employ retrieval-augmented generation (RAG) techniques and the contextual reasoning capabilities of LLMs to further enrich the annotation context and improve performance.

Report issue for preceding element

(1) Task-Specific Annotation Prompt Engineering.
To flexibly support diverse annotation tasks, the first approach encodes task-specific instructions and requirements within carefully crafted prompt templates.
For example, CHORUS \[ [204](https://arxiv.org/html/2505.18458v1#bib.bib204 "")\] integrates LLMs into the annotation pipeline using task-specific prompts that incorporate instructions, demonstrations, data samples, metadata, domain knowledge, and output formatting guidance.
Goby \[ [205](https://arxiv.org/html/2505.18458v1#bib.bib205 "")\] explores the use of LLMs for semantic column type annotation in a domain-specific enterprise setting by crafting a set of tailored prompts.
It proposes several techniques to improve performance, including tree serialization (providing the full ontology as prompt context), grammar-constrained decoding (enforcing hierarchical structure during generation), and step-by-step prompting (Chain-of-Thought strategy to guide ontology navigation).
LLMCTA \[ [218](https://arxiv.org/html/2505.18458v1#bib.bib218 "")\] evaluates diverse LLMs for generating and refining label definitions by employing methods like knowledge generation prompting (e.g., producing initial demonstrations), self-refinement (error-based definition improvement), and self-correction (two-step pipeline featuring a reviewer model).

Report issue for preceding element

(2) RAG Assisted Annotation Context Enrichment.
To supply LLM with relevant annotation context, the second approach utilizes diverse retrieval strategies within retrieval-augmented generation (RAG) frameworks to enrich the input.

Report issue for preceding element

∙∙\\bullet∙ _Classical Retrieval Technique._
To mitigate the shortcomings of vanilla LLM-based annotation, such as outdated knowledge, this method augments the context with retrieved external knowledge.
For example, RACOON \[ [415](https://arxiv.org/html/2505.18458v1#bib.bib415 "")\] performs semantic type annotation by leveraging a Knowledge Graph (KG) to retrieve entity-related information (e.g., labels and triples) associated with column cells.
This information is then processed into concise contextual representations and incorporated into LLM prompts to improve annotation accuracy.

Report issue for preceding element

∙∙\\bullet∙ _LLM Based Generation._
To fully leverage LLM’s internal knowledge, this method relies on the model itself to generate relevant contextual information.
For example, Birdie \[ [164](https://arxiv.org/html/2505.18458v1#bib.bib164 "")\] leverages LLMs to automatically generate natural language queries for training a differentiable search index (DSI), which facilitates linking relational tables to queryable knowledge by enriching them with contextual semantics.
It supports scalable structured data annotation, using prompts composed of structured markdown tables comprising captions, headers, and sample rows alongside explicit task instructions.

Report issue for preceding element

{forest}

for tree=
grow=east,
reversed=true,
parent anchor=east,
child anchor=west,
edge path=\[\\forestoptionedge,-¿, ¿=latex\]
(!u.parent anchor) – +(5pt,0pt) —- (.child anchor)
\\forestoptionedge label;

\[Data Analysis, root, rotate=90, parent anchor=south, child anchor=north\
\[Structured, data\_type\_node, rotate=90, parent anchor=south, child anchor=north\
\[Relational Data, str\_child, rotate=90, parent anchor=south, child anchor=north\
\[LLM as\
\
NL-Interface, str\_child\_child\
\[NL2SQL \[ [459](https://arxiv.org/html/2505.18458v1#bib.bib459 ""), [248](https://arxiv.org/html/2505.18458v1#bib.bib248 ""), [375](https://arxiv.org/html/2505.18458v1#bib.bib375 ""), [235](https://arxiv.org/html/2505.18458v1#bib.bib235 ""), [230](https://arxiv.org/html/2505.18458v1#bib.bib230 ""), [318](https://arxiv.org/html/2505.18458v1#bib.bib318 ""), [235](https://arxiv.org/html/2505.18458v1#bib.bib235 "")\], str\_leaf\]\
\[NL2Code \[ [451](https://arxiv.org/html/2505.18458v1#bib.bib451 ""), [105](https://arxiv.org/html/2505.18458v1#bib.bib105 ""), [177](https://arxiv.org/html/2505.18458v1#bib.bib177 ""), [172](https://arxiv.org/html/2505.18458v1#bib.bib172 "")\], str\_leaf\] \]\
\[Semantic-Aware, str\_child\_child\
\[Multi-Step QA \[ [500](https://arxiv.org/html/2505.18458v1#bib.bib500 ""), [227](https://arxiv.org/html/2505.18458v1#bib.bib227 ""), [481](https://arxiv.org/html/2505.18458v1#bib.bib481 ""), [471](https://arxiv.org/html/2505.18458v1#bib.bib471 ""), [411](https://arxiv.org/html/2505.18458v1#bib.bib411 "")\], str\_leaf\
\]\
\[End-to-End QA \[ [241](https://arxiv.org/html/2505.18458v1#bib.bib241 ""), [370](https://arxiv.org/html/2505.18458v1#bib.bib370 ""), [307](https://arxiv.org/html/2505.18458v1#bib.bib307 ""), [82](https://arxiv.org/html/2505.18458v1#bib.bib82 ""), [483](https://arxiv.org/html/2505.18458v1#bib.bib483 ""), [477](https://arxiv.org/html/2505.18458v1#bib.bib477 "")\], str\_leaf\
\] \] \]\
\[Graph Data, str\_child, rotate=90, parent anchor=south, child anchor=north\
\[LLM as\
\
NL-Interface, str\_child\_child\
\[NL2GQL \[ [253](https://arxiv.org/html/2505.18458v1#bib.bib253 ""), [499](https://arxiv.org/html/2505.18458v1#bib.bib499 "")\], str\_leaf\] \]\
\[Semantic-Aware, str\_child\_child\
\[Retrieval-Then-Reasoning \[ [465](https://arxiv.org/html/2505.18458v1#bib.bib465 ""), [194](https://arxiv.org/html/2505.18458v1#bib.bib194 "")\], str\_leaf\]\
\[Execution-Then-Reasoning \[ [432](https://arxiv.org/html/2505.18458v1#bib.bib432 ""), [247](https://arxiv.org/html/2505.18458v1#bib.bib247 "")\], str\_leaf\]\
\[Fine-Tuning Based \[ [449](https://arxiv.org/html/2505.18458v1#bib.bib449 ""), [403](https://arxiv.org/html/2505.18458v1#bib.bib403 ""), [380](https://arxiv.org/html/2505.18458v1#bib.bib380 "")\], str\_leaf\]\
\[Agent Based \[ [193](https://arxiv.org/html/2505.18458v1#bib.bib193 ""), [101](https://arxiv.org/html/2505.18458v1#bib.bib101 "")\], str\_leaf\] \] \]\
\]\
\[Semi-Structured, data\_type\_node, rotate=90, parent anchor=south, child anchor=north\
\[Markup Language, sem\_leaf\]\
\[Semi-Structured Tables \[ [166](https://arxiv.org/html/2505.18458v1#bib.bib166 ""), [282](https://arxiv.org/html/2505.18458v1#bib.bib282 ""), [246](https://arxiv.org/html/2505.18458v1#bib.bib246 "")\], sem\_leaf\]\
\]\
\[Unstructured, data\_type\_node, rotate=90, parent anchor=south, child anchor=north\
\[Document, uns\_child, rotate=90, parent anchor=south, child anchor=north\
\[OCR-Dependent \[ [381](https://arxiv.org/html/2505.18458v1#bib.bib381 ""), [62](https://arxiv.org/html/2505.18458v1#bib.bib62 "")\], uns\_child\_child\]\
\[OCR-Free, uns\_child\_child\
\[Text Masked Learning \[ [226](https://arxiv.org/html/2505.18458v1#bib.bib226 ""), [49](https://arxiv.org/html/2505.18458v1#bib.bib49 "")\], uns\_leaf\]\
\[Visual Embedded Learning \[ [175](https://arxiv.org/html/2505.18458v1#bib.bib175 ""), [138](https://arxiv.org/html/2505.18458v1#bib.bib138 "")\], uns\_leaf\] \] \],\
\[Program Language, uns\_child, rotate=90, parent anchor=south, child anchor=north, text width=70pt\
\[Vulnerability Detection, uns\_child\_child\
\[Program Analysis Based \[ [272](https://arxiv.org/html/2505.18458v1#bib.bib272 ""), [464](https://arxiv.org/html/2505.18458v1#bib.bib464 "")\], uns\_leaf\]\
\[Case-driven Prompt Engineering \[ [271](https://arxiv.org/html/2505.18458v1#bib.bib271 ""), [498](https://arxiv.org/html/2505.18458v1#bib.bib498 "")\], uns\_leaf\] \]\
\[Semantic-Aware, uns\_child\_child\
\[Code Summarization\
\
\[ [155](https://arxiv.org/html/2505.18458v1#bib.bib155 ""), [51](https://arxiv.org/html/2505.18458v1#bib.bib51 ""), [285](https://arxiv.org/html/2505.18458v1#bib.bib285 "")\], uns\_leaf\]\
\[Code Completion\
\
\[ [361](https://arxiv.org/html/2505.18458v1#bib.bib361 ""), [118](https://arxiv.org/html/2505.18458v1#bib.bib118 ""), [420](https://arxiv.org/html/2505.18458v1#bib.bib420 "")\], uns\_leaf\] \] \]\
\]\
\]

Report issue for preceding element

Figure 9: Overview of LLM for Data Analysis.Report issue for preceding element

### 3.2 LLM for Data Analysis

Report issue for preceding element

Apart from data manipulation, LLMs hold the potential to revolutionize traditional data analysis paradigms by supporting natural language interfaces and enabling advanced, semantic-aware analysis tasks that typically require human involvement. In this section, we discuss the challenges and techniques of LLM-based data analysis, including structured data analysis, semi-structured data analysis, and unstructured data analysis.

Report issue for preceding element

#### 3.2.1 LLM for Structured Data Analysis

Report issue for preceding element

Structured data refers to data with well-defined schemas like relational (tabular) data \[ [108](https://arxiv.org/html/2505.18458v1#bib.bib108 "")\] and graph data \[ [60](https://arxiv.org/html/2505.18458v1#bib.bib60 "")\].

Report issue for preceding element

#### 3.2.1.1 Relational Data Analysis

Report issue for preceding element

LLM for Natural Language Interfaces. Basic analysis jobs for relational data are typically characterized by well-defined operations. These include basic calculations (e.g., summation, averaging, counting, ranking), statistical analysis (e.g., regression, K-means clustering), and data quality assurance processes (e.g., constraint validation, outlier detection). Such tasks can generally be supported by tools like SQL or Python libraries (e.g., Pandas).

Report issue for preceding element

(1) NL2SQL. With the help of LLM, users can directly perform operations using natural language. NL2SQL focuses on translating natural language queries into SQL commands by leveraging techniques such as (i)𝑖(i)( italic\_i ) schema linking, which aligns user intents with database schema to resolve ambiguities \[ [459](https://arxiv.org/html/2505.18458v1#bib.bib459 ""), [248](https://arxiv.org/html/2505.18458v1#bib.bib248 "")\], (i⁢i)𝑖𝑖(ii)( italic\_i italic\_i ) content retrieval, which dynamically extracts relevant information from the database to refine query generation \[ [375](https://arxiv.org/html/2505.18458v1#bib.bib375 ""), [235](https://arxiv.org/html/2505.18458v1#bib.bib235 "")\], and (i⁢i⁢i)𝑖𝑖𝑖(iii)( italic\_i italic\_i italic\_i ) SQL generation strategies such as multi-step generation, intermediate SQL representation, and different decoding strategies \[ [230](https://arxiv.org/html/2505.18458v1#bib.bib230 ""), [318](https://arxiv.org/html/2505.18458v1#bib.bib318 ""), [235](https://arxiv.org/html/2505.18458v1#bib.bib235 ""), [489](https://arxiv.org/html/2505.18458v1#bib.bib489 ""), [490](https://arxiv.org/html/2505.18458v1#bib.bib490 "")\].

Report issue for preceding element

(2) NL2Code. Different from NL2SQL, NL2Code approaches emphasize enhancing relational data analysis through generating Python code (e.g., Pandas, NumPy), which includes a vast number of library APIs characterized by high variability and complexity, and often requiring the handling of complex chain operations. Recent advancements address these issues to some extent.

Report issue for preceding element

∙∙\\bullet∙ _Model Finetuning:_ PACHINCO \[ [451](https://arxiv.org/html/2505.18458v1#bib.bib451 "")\] fine-tunes a 62B parameter PALM \[ [105](https://arxiv.org/html/2505.18458v1#bib.bib105 "")\] model in two stages (i.e., separately using a Python source code corpus with 64B tokens and a Jupyter notebook corpus with 9.6B tokens) so as to improve model performance on analysis-related tasks (e.g., calculate the amount of games added in each year for each month). DataCoder \[ [177](https://arxiv.org/html/2505.18458v1#bib.bib177 "")\] utilizes different types of contexts (e.g., code, text, and data) by employing dual encoders (e.g., data encoder and code + text encoder) and one general decoder to generate code in notebooks.

Report issue for preceding element

∙∙\\bullet∙ _LLM Based Analysis Agent:_
Data Interpreter \[ [172](https://arxiv.org/html/2505.18458v1#bib.bib172 "")\], on the other hand, leverages LLMs through APIs to generate task and action graphs. Specifically, they utilize LLM’s semantic reasoning ability to accurately decompose complex user queries into subproblems (e.g., correlation analysis, data exploration, and anomaly detection), and refine and verify each subproblem to improve code generation results for data science tasks.

Report issue for preceding element

![Refer to caption](https://arxiv.org/html/2505.18458v1/x8.png)Figure 10: General Workflows \- (a) Multi-Step Relational Data QA. (b) End-to-End Relational Data QA.Report issue for preceding element

LLM for Semantic Analysis. Moreover, some jobs require LLM-based analysis, such as those that involve semantic understanding or demand outputs in natural language format (e.g., table summarization). These challenges call for methodologies like (1) multi-step question answering (QA) with diverse decomposition strategies and (2) end-to-end QA leveraging specifically optimized LLMs.

Report issue for preceding element

∙∙\\bullet∙Multi-Step QA. Multi-step question answering (QA) refers to decomposing complex queries into a sequence of sub-questions to facilitate step-by-step reasoning. According to the question decomposition mechanisms, existing methods can be categorized into two types: (1) static decomposition, which follows predefined and fixed processing steps (e.g., retrieve-select-reason), and (2) LLM-driven iterative decomposition, in which the LLM dynamically determines the next operation based on the contextual history of the reasoning process.

Report issue for preceding element

(1) Static Decomposition. The static decomposition includes Retriever-Selector-Reasoner frameworks and the variants, which partition tasks into modular components for better multi-step inference and enhanced interpretability. The Extractor-Reasoner-Executor paradigm \[ [500](https://arxiv.org/html/2505.18458v1#bib.bib500 "")\] extracts the relevant segments from the context, generates the logic rules or equations, and performs the rules or executes the equations to get the final answer through LLM prompting. S3HQA \[ [227](https://arxiv.org/html/2505.18458v1#bib.bib227 "")\] trains a retriever which aims to perform initial filtering of heterogeneous resources, utilizes a selector to select the most relevant factual knowledge, and a generation-based reasoner to obtain final answers.

Report issue for preceding element

(2) Iterative Decomposition. However, static decomposition paradigm performs poorly on multi-hop queries, while LLM-driven iterative decomposition, which dynamically refines subtasks through recursive reasoning, could effectively address the issue.

Report issue for preceding element

TAPERA \[ [481](https://arxiv.org/html/2505.18458v1#bib.bib481 "")\] introduces the query decomposition step into the question answering process by adopting the LLM-driven approach. The Planner decomposes the query into sub-queries, forming an initial plan. The Reasoner then generates executable programs for each sub-query, while the Answer Generator derives answers based on the program outputs to fulfill the plan. Finally, the Planner updates or finalizes the plan as needed.

Report issue for preceding element

Similarly, ReAcTable \[ [471](https://arxiv.org/html/2505.18458v1#bib.bib471 "")\] and CHAIN-OF-TABLE \[ [411](https://arxiv.org/html/2505.18458v1#bib.bib411 "")\] iteratively generate operations and update the table to present a reasoning chain as a proxy for intermediate thoughts through prompting LLMs and in-context learning.

Report issue for preceding element

∙∙\\bullet∙End-to-End QA. End-to-End Question Answering (QA) refers to approaches in which the answer-generating LLM directly produces the final response without intermediate steps or iterative refinement. Based on the data representation and processing mechanisms, the relevant methods can be classified into table-specific LLM fine-tuning, table content retrieval, and table-as-image analysis.

Report issue for preceding element

(1) Table-Specific LLM Fine-Tuning. Fine-tuning LLMs on task-specific table datasets enables them to internalize analytical knowledge directly within their parameters. TableGPT \[ [241](https://arxiv.org/html/2505.18458v1#bib.bib241 "")\] fine-tunes LLMs like GPT-3.5 using a diverse set of table tasks synthesized from real-world tables. Building on Qwen2.5 \[ [325](https://arxiv.org/html/2505.18458v1#bib.bib325 "")\], TableGPT2 \[ [370](https://arxiv.org/html/2505.18458v1#bib.bib370 "")\] introduces a table encoder to generate a hybrid table representation, an adapter to generate query representations, and a LLM decoder generates an agent workflow (i.e., the tool execution pipeline) to derive the final answer. The TableGPT2 model is pre-trained on 593.8K tables and fine-tuned 2.36M question-answer pairs.

Report issue for preceding element

(2) Table Content Retrieval. Instead of embedding the whole table, table content retrieval enhances model performance by eliminating noisy parts of the table while retaining information relevant to question answering. CABINET \[ [307](https://arxiv.org/html/2505.18458v1#bib.bib307 "")\] employs a weakly supervised component to produce a parsing statement that defines the criteria for selecting relevant rows and columns, emphasizing the corresponding table cell content. TableMaster \[ [82](https://arxiv.org/html/2505.18458v1#bib.bib82 "")\] constructs a refined subtable through row and column lookup. By leveraging carefully designed LLM prompts (e.g., provide objective, table definition, table information, question, instructions, and response format), it ranks all candidate columns, selects a relevant subset based on the query, and then instructs the LLM to generate an SQL query for extracting the most relevant rows.

Report issue for preceding element

(3) Table-As-Image Analysis. Due to the limitations of (text-only) LLMs in understanding table structures, the Table-as-Image approach has been proposed, converting tables into images for analysis using multimodal LLMs. Table-LLaVA \[ [483](https://arxiv.org/html/2505.18458v1#bib.bib483 "")\] applies incremental pretraining to LLaVA-7B \[ [259](https://arxiv.org/html/2505.18458v1#bib.bib259 "")\] on 150K table recognition samples (e.g., input a table image and output table representations in HTML, Markdown, or LaTeX), enabling the model to align table structures and elements with textual modality. It is further fine-tuned on 232K samples on question answering, text generation, fact verification, and structure understanding tasks to enhance its instruction-following ability. To enable a single model to perform various analytical tasks, TabPedia \[ [477](https://arxiv.org/html/2505.18458v1#bib.bib477 "")\] introduces the concept synergy mechanism, abstracting all table analysis tasks into concepts. Built on Vicuna-7B \[ [482](https://arxiv.org/html/2505.18458v1#bib.bib482 "")\], it appends meditative tokens to the input of the LLM decoder, which adaptively activates different regions of visual tokens and helps the model interpret the intent behind specific task questions. However, such methods face limitations when processing twisted or distorted tables, and their performance degrades significantly when directly handling document images.

Report issue for preceding element

#### 3.2.1.2 Graph Data Analysis

Report issue for preceding element

Different from relational data, graph data represents entities (vertices) and their inter-dependencies (relationships) to explicit model of complex network semantics (e.g., social networks and knowledge graphs) beyond rigid tabular schema, which presents unique challenges due to the vast search space and complex path reasoning in multi-hop queries \[ [59](https://arxiv.org/html/2505.18458v1#bib.bib59 "")\]. Compared with relational data analysis, graph data analysis involves more complex jobs like summarization based on the multi-hop relations across the graph vertices and reasoning over text-attributed graphs whose nodes and edges are associated with text \[ [253](https://arxiv.org/html/2505.18458v1#bib.bib253 ""), [499](https://arxiv.org/html/2505.18458v1#bib.bib499 "")\]. Graph data can not only be stored in relational databases, but also be stored and queried in knowledge graphs and accessed through SPARQL in RDF databases (e.g., Blazegraph \[ [8](https://arxiv.org/html/2505.18458v1#bib.bib8 "")\] and GraphDB \[ [21](https://arxiv.org/html/2505.18458v1#bib.bib21 "")\]) or Cypher in Neo4j \[ [17](https://arxiv.org/html/2505.18458v1#bib.bib17 "")\].

Report issue for preceding element

Traditional graph analysis (e.g., statistical methods, graph neural network (GNN) based methods) encompasses a spectrum of tasks, including node classification (e.g., categorizing academic papers into research domains), graph classification (e.g., predicting node properties over molecular graphs), link prediction (i.e., inferring latent relationships between graph nodes), community detection (i.e., identifying densely connected subgraphs), anomaly detection (i.e., identifying deviations from expected patterns), graph clustering, and etc. However, these methods have their own limitations. Statistics-based methods fail to handle complex semantic information (e.g., query can be extremely complex and requires human expertise), while graph neural networks (GNNs) exhibit limited generalization capabilities, necessitating task-specific retraining on different tasks.

Report issue for preceding element

In contrast, the advent of LLMs offers transformative potential by leveraging their advanced reasoning capacities and cross-domain generalization abilities, which can (1) simplify the query writing costs (e.g., NL interfaces) and (2) achieve semantic-aware analysis unsupported in traditional ones.

Report issue for preceding element

Natural Language To Graph Analysis Query. Different from NL2SQL, the syntax of graph query language generation is more complex (i.e., MATCH, LOOKUP, GET and other operations unique to graph data manipulation) and there exist two operation objects (i.e., vertex and edge) \[ [499](https://arxiv.org/html/2505.18458v1#bib.bib499 "")\].
By integrating natural language interfaces with graph data, LLMs facilitate flexible and efficient query generation without the need for specialized model architectures.

Report issue for preceding element

To enhance LLMs’ comprehension of the complex syntax of Graph Query Language (GQL), R3superscript𝑅3R^{3}italic\_R start\_POSTSUPERSCRIPT 3 end\_POSTSUPERSCRIPT-NL2GQL \[ [499](https://arxiv.org/html/2505.18458v1#bib.bib499 "")\] proposes a hybrid approach leveraging relatively small LLM (e.g., LLaMA3-7B) as a selector and GQL rewriter, while employing a larger LLM (e.g., GPT-4) as a reasoner. The selector identifies the necessary CRUD functions, clauses, and schema, while the rewriter refines the query by aligning it with the relevant graph data retrieved by minimum edit distance and semantic similarity calculation. The LLM then synthesizes the aligned question, selected operations, and schema to generate the final GQL query.

Report issue for preceding element

To address the limitations of LLMs in planning and collaborating with other LLMs, NAT-NL2GQL \[ [253](https://arxiv.org/html/2505.18458v1#bib.bib253 "")\] introduces a three-agent framework. The Preprocessor agent constructs context information, including query rewriting, path linking, and the extraction of query-relevant schemas. The Generator agent, an LLM fine-tuned with NL-GQL data, generates GQL statements based on the rewritten queries and extracted schemas. The Refiner agent iteratively enhances the GQL or contextual information by leveraging error feedback from GQL execution results.

Report issue for preceding element

Note that, within the context of AI for Science (AI4Science), the integration of LLMs with graph data analysis has also shown significant potential and wide-ranging applications (e.g., treat polymers as graphs and predict their properties \[ [243](https://arxiv.org/html/2505.18458v1#bib.bib243 ""), [310](https://arxiv.org/html/2505.18458v1#bib.bib310 "")\]), which is not the primary focus of this survey.

Report issue for preceding element

LLM-based Semantic Analysis. Furthermore, certain jobs necessitate semantic-aware analysis, such as summarizing textual paragraphs embedded within graph nodes.
Based on the adopted LLM strategies, we classify the relevant methods into retrieval-then-reasoning methods, execution-then-reasoning methods, graph task based fine-tuning methods, and agent based methods.

Report issue for preceding element

∙∙\\bullet∙Retrieval-Then-Reasoning.
Retrieval-then-reasoning first extracts a question-specific subgraph from the graph to identify the most relevant entities and then generates answers using LLMs.
To address the challenge of a vast search space, \[ [465](https://arxiv.org/html/2505.18458v1#bib.bib465 "")\] introduces a two-stage approach. First, a trainable and decoupled subgraph retriever selects a relevant subgraph based on the query. Then, reasoning is performed over the retrieved subgraph to derive the final answer. UniKGQA \[ [194](https://arxiv.org/html/2505.18458v1#bib.bib194 "")\] integrates retrieval and reasoning within a unified model architecture. It comprises a semantic matching module, leveraging a pre-trained RoBERTa \[ [267](https://arxiv.org/html/2505.18458v1#bib.bib267 "")\] for the semantic alignment between questions and relations in graphs, and a matching information propagation module that propagates matching signals along directed edges in graphs.

Report issue for preceding element

∙∙\\bullet∙Execution-Then-Reasoning. Execution-then-reasoning refers to the process of parsing natural language queries into executable logical forms (e.g., SPARQL) that align with the graph data, followed by reasoning based on the output of the executed program.
Interactive-KBQA \[ [432](https://arxiv.org/html/2505.18458v1#bib.bib432 "")\] introduces an interactive LLM QA framework with a unified SPARQL-based toolset (e.g., entity search, graph pattern search, SPARQL execution, etc.) designed to address complex queries.
FlexKBQA  \[ [247](https://arxiv.org/html/2505.18458v1#bib.bib247 "")\] addresses the challenge of lacking high-quality annotated data in real-world scenarios. By prompting LLMs as program translators, it samples program-answer pairs from the knowledge base and generates corresponding natural language questions. The synthetic question-program-answer dataset is used to train lightweight models through execution-guided self-training, which are subsequently employed to annotate real user queries. This approach addresses the distribution shifts between synthetic and actual data, leading to significant improvements in few-shot learning scenarios.

Report issue for preceding element

∙∙\\bullet∙Graph Task Based Fine-tuning Methods.
InstructGLM \[ [449](https://arxiv.org/html/2505.18458v1#bib.bib449 "")\] enables generative graph learning by fine-tuning an LLM and leveraging natural language descriptions of graph structures (e.g., offer the first node and the 1-/2-/3-hop neighbors’ information).
InstructGraph \[ [403](https://arxiv.org/html/2505.18458v1#bib.bib403 "")\] introduces a stricter code-like graph representation format which constructs entities and triples in the form of list, whose backbone LLM (LLaMA2-7B) is fine-tuned on a graph-centric corpus comprising 1.6 million instances. To mitigate the issue of hallucination, it incorporates Direct Preference Optimization (DPO) algorithm \[ [330](https://arxiv.org/html/2505.18458v1#bib.bib330 "")\] for preference alignment.
GraphGPT \[ [380](https://arxiv.org/html/2505.18458v1#bib.bib380 "")\] enhances model performance in zero-shot scenarios by incorporating a structural information encoding module based on Graph-SAGE \[ [167](https://arxiv.org/html/2505.18458v1#bib.bib167 "")\] and GCN \[ [212](https://arxiv.org/html/2505.18458v1#bib.bib212 "")\]. It fine-tunes the projector bridging the graph encoder and the LLM decoder to align the language capabilities of the foundation LLM (Vicuna-7B) with the graph learning tasks.

Report issue for preceding element

∙∙\\bullet∙Agent Based Methods.
Agent-based methods involve leveraging LLM-based agents with predefined tools (e.g., human-written interfaces or graph processing library APIs) that iteratively interact with the graph data to retrieve, refine, and operate information.
StructGPT \[ [193](https://arxiv.org/html/2505.18458v1#bib.bib193 "")\] introduces an iterative reading-then-reasoning framework, leveraging specialized interfaces to operate on graph data. It repeatedly applies an invoke-linearize-generate procedure to derive query results.
Another approach is to generate an entire reasoning path based on the query and refine it only when necessary. Readi \[ [101](https://arxiv.org/html/2505.18458v1#bib.bib101 "")\] initially constructs a reasoning path and instantiates it on the graph. When execution errors occur, it collects error messages and invokes an LLM to revise the path. The final answer is inferred from the instantiated graphs.

Report issue for preceding element

#### 3.2.2 LLM for Semi-Structured Data Analysis

Report issue for preceding element

Semi-structured data refers to data that are neither with strictly predefined schema like relational models nor raw data (e.g., plain text or images) \[ [48](https://arxiv.org/html/2505.18458v1#bib.bib48 "")\]. Meanwhile, they still maintain part of organizational properties (e.g., tags, headers) and have hierarchical or nested representation (e.g., County \- Province \- City in a nested JSON).

Report issue for preceding element

#### 3.2.2.1 Markup Language

Report issue for preceding element

Markup languages (e.g., XML, JSON, and HTML) are widely used for structuring and exchanging data across systems. Traditional approaches for processing these formats typically involve transforming them into structured tables or representing them as hierarchical tree structures. Leveraging the reasoning capabilities of LLMs, it becomes possible to directly extract and interpret hierarchical relationships, attributes, and nested structures from data without the need for intermediate transformations.

Report issue for preceding element

#### 3.2.2.2 Semi-Structured Tables

Report issue for preceding element

Compared to structured relational data, semi-structured tables exhibit a more complex structural organization characterized by merged cells. This inherent complexity presents a significant challenge in aligning queries with the table content and structure in query answering tasks. The lack of efficient tools (usually using the openpyxl library) and representation methods (usually stored in Excel or HTML files) for handling semi-structured tables makes it more difficult to process such data.

Report issue for preceding element

Although research on semi-structured table analysis is limited, several studies have compiled various semi-structured table reasoning datasets, providing valuable data support.
TEMPTABQA \[ [166](https://arxiv.org/html/2505.18458v1#bib.bib166 "")\] consists of 11,454 question-answer pairs focused on temporal queries, while SPREADSHEETBENCH \[ [282](https://arxiv.org/html/2505.18458v1#bib.bib282 "")\] presents a challenging benchmark for spreadsheet manipulation, with 912 questions derived from real-world scenarios. MiMoTable \[ [246](https://arxiv.org/html/2505.18458v1#bib.bib246 "")\] incorporates reasoning across multiple sheets and files, containing 1,719 queries within 428 spreadsheets. Evaluation results on these benchmarks highlight a significant performance gap (ranging from 20% to 50%) between state-of-the-art models and human performance, calling for further exploration in this area.

Report issue for preceding element

#### 3.2.3 LLM for Unstructured Data Analysis

Report issue for preceding element

Unstructured data refers to data that lacks explicit structure, as it does not adhere to a predefined schema. Additionally, it exhibits high variability in format, length, and modality, which further complicates its processing and analysis.

Report issue for preceding element

#### 3.2.3.1 Documents

Report issue for preceding element

Documents exhibit complex layouts and styles with diverse elements, including a hybrid of images, tables, charts, plain text, and formulas.

Report issue for preceding element

∙∙\\bullet∙OCR-Dependent Methods.
OCR-based methods refer to approaches that involve performing Optical Character Recognition on document images, followed by the integration of textual, layout, and visual features for reasoning.
UDOP \[ [381](https://arxiv.org/html/2505.18458v1#bib.bib381 "")\] integrates text and layout modalities within a unified encoder, dynamically fusing image patch tokens and text tokens based on their spatial information. Specifically, when the center of a text token’s bounding box falls within an image patch, the corresponding image patch embedding is added to the text token embedding, enabling a more cohesive representation of document structure.
DocFormerV2 \[ [62](https://arxiv.org/html/2505.18458v1#bib.bib62 "")\] preserves the integrity of layout information by employing a visual encoder. Image patches and text bounding box positions are embedded through a linear layer and added to the corresponding token embeddings as input to the T5 \[ [334](https://arxiv.org/html/2505.18458v1#bib.bib334 "")\] encoder. To achieve local feature semantic alignment, the model undergoes pretraining on token-to-line (i.e., predict whether a key-value pair is on the same line or adjacent lines) and token-to-grid (i.e., predict each token located in which image grid) tasks. The T5 decoder is then incorporated to fine-tune the whole model on downstream tasks.

Report issue for preceding element

∙∙\\bullet∙OCR Free Methods.
However, the OCR step often introduces semantic errors, resulting in suboptimal performance. To fill this gap, OCR-free methods have emerged, directly generating the target token sequences with end-to-end multimodal LLMs\[ [258](https://arxiv.org/html/2505.18458v1#bib.bib258 ""), [414](https://arxiv.org/html/2505.18458v1#bib.bib414 "")\]. Based on different approaches to enhancing model understanding of textual semantics, related works can be categorized into text masked learning and visual embedded learning.

Report issue for preceding element

(1) Text Masked Learning.
Text Masked Learning involves masking textual content within a document and training the model to predict the missing text.
Pix2Struct \[ [226](https://arxiv.org/html/2505.18458v1#bib.bib226 "")\] is a typical vision-encoder-text-decoder pre-trained image-to-text model designed for visual language understanding based on ViT \[ [124](https://arxiv.org/html/2505.18458v1#bib.bib124 "")\]. It is pretrained to parse masked web pages into simplified HTML. The model introduces a variable-resolution input representation, rescaling input images to maximize the number of patches that can fit within the given sequence length, to prevent aspect ratio distortion.
DUBLIN \[ [49](https://arxiv.org/html/2505.18458v1#bib.bib49 "")\] designed multiple fine-tuning tasks (i.e., bounding box prediction based on given text, text prediction based on given bounding box, masked text generation, and query answering) to improve the generalization ability.

Report issue for preceding element

(2) Visual Embedded Learning.
In Visual Embedded Learning, there are no specially designed training objectives. Instead, the model is directly fine-tuned on downstream tasks to enhance its understanding of textual content within images.
mPLUG-DocOwl1.5 \[ [175](https://arxiv.org/html/2505.18458v1#bib.bib175 "")\] introduces a spatial-aware vision-to-text module designed for representing high-resolution, text-rich images. This module preserves structural information while reducing the length of visual features. It consists of a convolution layer to shorten the sequence length and a fully connected layer that projects visual features into the language embedding space.
Unlike most methods that crop or resize the initial image before feeding it into a vision encoder, DocPedia \[ [138](https://arxiv.org/html/2505.18458v1#bib.bib138 "")\] directly processes visual input in the frequency domain. It utilizes JPEG DCT \[ [394](https://arxiv.org/html/2505.18458v1#bib.bib394 "")\] extraction to obtain DCT coefficients, which are then processed using a frequency adapter before being input into the vision encoder. This approach allows the model to capture more visual and textual information while using a limited number of tokens. The performance improvement observed in the experiment suggests that this method offers a novel approach for processing high-resolution images.

Report issue for preceding element

#### 3.2.3.2 Program Language Analysis

Report issue for preceding element

Programming language analysis involves multiple levels of abstraction, including lexical analysis, parsing, and semantic analysis, each requiring distinct techniques to process source code effectively. Additionally, it must handle both local and global information, such as variable scopes, function call chains, and complex dependencies, which pose significant challenges for accurate program understanding.

Report issue for preceding element

LLM as Program Vulnerability Detection Tools.
Recent advancements in LLMs have opened new avenues for improving vulnerability detection tools. Training LLMs based on program analysis techniques enhances their ability to understand programs at both the lexical and syntactic levels. Leveraging in-context learning through case-driven prompt engineering enhances the model’s accuracy by providing relevant examples.

Report issue for preceding element

∙∙\\bullet∙Program Analysis based Training.
Static and dynamic program analysis are commonly used methods for detecting vulnerabilities in programs. By assisting these processes, LLMs improve the accuracy of vulnerability detection.
PDBER \[ [272](https://arxiv.org/html/2505.18458v1#bib.bib272 "")\] is a model fine-tuned on CodeBERT \[ [141](https://arxiv.org/html/2505.18458v1#bib.bib141 "")\] through three tasks (i.e., Predicting Masked Tokens, Predicting Statement-Level Control Dependencies, and Predicting Token-Level Data Dependencies). This enables more fine-grained vulnerability analysis at the statement level.
To reduce the impact of irrelevant information, \[ [464](https://arxiv.org/html/2505.18458v1#bib.bib464 "")\] decomposes the control flow graph (CFG) into multiple execution paths from the entry node to the exit node. CodeBERT and a CNN are employed to capture intra-path and inter-path representations, respectively. The extracted feature vectors are then combined as a unified program representation, which serves as input to a MLP classifier for vulnerability detection.

Report issue for preceding element

∙∙\\bullet∙Case-driven Prompt Engineering.
Leveraging the in-context learning and few-shot learning capabilities of LLMs can significantly improve their accuracy in vulnerability detection.
VUL-GPT \[ [271](https://arxiv.org/html/2505.18458v1#bib.bib271 "")\] uses GPT-3.5 to generate analysis content (i.e., the program interpretation) for the input code and retrieves similar code snippets and corresponding vulnerability information through BM25 \[ [341](https://arxiv.org/html/2505.18458v1#bib.bib341 "")\] or TF-IDF. The retrieved information, along with the original code and analysis, is then input into GPT to detect vulnerabilities.
\[ [498](https://arxiv.org/html/2505.18458v1#bib.bib498 "")\] designs various prompts, such as random code samples and retrieve-based code samples, and demonstrates that GPT-4 outperforms state-of-the-art models in vulnerability detection.

Report issue for preceding element

LLM-based Semantic-aware Analysis.
Traditional semantic-aware tasks convert programs into ASTs \[ [367](https://arxiv.org/html/2505.18458v1#bib.bib367 "")\] or graph structures \[ [152](https://arxiv.org/html/2505.18458v1#bib.bib152 "")\] and train Seq2Seq models to learn program syntax, dependencies, and semantics. However, these approaches lack general knowledge, leading to limited generalization ability. By leveraging the world knowledge and few-shot learning capabilities of LLMs, the performance of tasks such as code summarization and code completion has been significantly improved.

Report issue for preceding element

∙∙\\bullet∙LLM as Code Summarizer.
Recent advancements in LLM-powered code summarization focus on retrieving similar code snippets and leverage LLMs’ few-shot learning capability to enhance performance.
\[ [155](https://arxiv.org/html/2505.18458v1#bib.bib155 "")\] retrieves similar code examples by measuring token overlap and the cosine distance between embedding vectors of code snippets. In contrast,  \[ [51](https://arxiv.org/html/2505.18458v1#bib.bib51 "")\] employs the BM25 algorithm and incorporates repository information, data flow information, and variable information to construct three-shot prompts.
SCLA \[ [285](https://arxiv.org/html/2505.18458v1#bib.bib285 "")\] further enhances code semantics in LLM prompts by preprocessing the code sample pool to extract semantic information. By simultaneously leveraging few-shot learning, it achieves state-of-the-art performance based on Gemini-1.5-Pro.

Report issue for preceding element

∙∙\\bullet∙LLM as Repository-Level Code Completer.
Repository context (e.g., imports, related classes, etc.) plays a crucial role in code completion. Given the strong semantic understanding and generative capabilities of LLMs, how to integrate contextual information into code completion has become a key research focus.
RepoFusion \[ [361](https://arxiv.org/html/2505.18458v1#bib.bib361 "")\] appends the surrounding text of the target code to the repository context retrieved based on BM25, encoding and concatenating them as input to the decoder for code generation. This approach enables the model to produce context-aware code completions by leveraging both local and repository-level information.
CoCoMIC \[ [118](https://arxiv.org/html/2505.18458v1#bib.bib118 "")\] proposes a more robust retrieval method based on program dependency graphs. Given an incomplete program, it retrieves the most relevant context by analyzing file imports within the constructed graph. By defining the relevant context as files within a two-hop neighborhood, this approach mitigates the risk of excluding vital dependencies while avoiding the inclusion of irrelevant information.
However, some researchers have found that simple retrieval methods fail to improve performance in up to 80% of cases and may even degrade performance due to the inclusion of irrelevant information \[ [420](https://arxiv.org/html/2505.18458v1#bib.bib420 "")\]. As a result, Repoformer introduces a self-supervised learning approach to enable the model to accurately judge whether retrieval can improve its output quality. A new <<<eof>>> token is introduced to guide the model in determining whether context retrieval is necessary. Based on the output after <<<eof>>> token, it decides whether to generate the output directly or to perform retrieval first.

Report issue for preceding element

### 3.3 LLM for Data System Optimization

Report issue for preceding element

This section presents the application of LLM to optimize the performance of different data systems across three key tasks:
_(1) Configuration Tuning:_ selecting effective system configurations, such as database knobs and indexes;
_(2) Query Optimization:_ accelerating input SQL queries through logical rewrites and physical plan selection;
_(3) Anomaly Diagnosis:_ addressing system anomalies, such as spikes in the usage of specific system resources.

Report issue for preceding element

#### 3.3.1 LLM for Configuration Tuning

Report issue for preceding element

Configuration tuning aims to identify effective configurations, such as database knobs \[ [232](https://arxiv.org/html/2505.18458v1#bib.bib232 ""), [480](https://arxiv.org/html/2505.18458v1#bib.bib480 "")\] and indexes \[ [491](https://arxiv.org/html/2505.18458v1#bib.bib491 ""), [493](https://arxiv.org/html/2505.18458v1#bib.bib493 ""), [492](https://arxiv.org/html/2505.18458v1#bib.bib492 "")\], to optimize the system performance.
Traditional tuning approaches, including rule-based methods and learning-based techniques with classical machine learning models, often require extensive explorations without a promising starting point \[ [232](https://arxiv.org/html/2505.18458v1#bib.bib232 "")\].
Furthermore, they might result in sub-optimal configurations, despite using advanced techniques such as transfer learning \[ [470](https://arxiv.org/html/2505.18458v1#bib.bib470 ""), [409](https://arxiv.org/html/2505.18458v1#bib.bib409 "")\].

Report issue for preceding element

A key limitation of these methods is the failure to incorporate extensive domain knowledge (e.g., information from system manuals and public forum discussions) into the tuning process, relying solely on runtime feedback from benchmark evaluations to guide optimization.
To address this issue, recent approaches utilize LLM with large-scale domain knowledge to enhance the tuning process via the following methods.

Report issue for preceding element

Tuning Task-Aware Prompt Engineering.
The first method manually designs prompts with informative details (e.g., system status) to assist LLM in configuration tuning (e.g., database knobs and indexes).
Some approaches further enhance this by introducing automatic prompt generation techniques or by formulating it as an optimization problem.

Report issue for preceding element

(1) Manually-Crafted Tuning Prompt.
Existing methods design prompts that incorporate essential details (e.g., system status) tailored to the characteristics of specific tasks.
In particular, the constructed prompts typically consist of the following components.

Report issue for preceding element

∙∙\\bullet∙Configuration Task Instruction.
To convey the overall tuning objective, existing methods specify task instructions in the prompts using chain-of-thought (CoT) and role-play-based guidance.
For instance, LLMBench \[ [244](https://arxiv.org/html/2505.18458v1#bib.bib244 "")\] explicitly defines the goals of three key subtasks in knob tuning: (i) knob pruning to retain the most influential knobs, (ii) model initialization to select promising knobs for warm-starting bayesian optimization, and (iii) knob recommendation to return optimal configurations for specific workloads.
Similarly, LATuner \[ [132](https://arxiv.org/html/2505.18458v1#bib.bib132 "")\] instructs LLM to identify critical knobs for warm-starting the tuning process and select promising knobs as training samples for boosting the sampling procedure.

Report issue for preceding element

∙∙\\bullet∙Input Tuning Context.
To enable LLM to effectively support the tuning process for specific workloads, existing methods enrich the tuning context with detailed information. Specifically, prompts are carefully structured to include: (i) Configuration Specifications: list of tunable knobs (e.g., names and allowable value ranges) and usage descriptions, including fixed-task demonstrations (e.g., LLMBench \[ [244](https://arxiv.org/html/2505.18458v1#bib.bib244 "")\], LATuner \[ [132](https://arxiv.org/html/2505.18458v1#bib.bib132 "")\]);
(ii) Environment Information: covering workload and database characteristics (e.g., compressed SQL snippets with join conditions in λ⁢-⁢T⁢u⁢n⁢e𝜆-𝑇𝑢𝑛𝑒\\lambda\\text{-}Tuneitalic\_λ - italic\_T italic\_u italic\_n italic\_e\[ [157](https://arxiv.org/html/2505.18458v1#bib.bib157 "")\]), as well as hardware settings (e.g., memory size and CPU core count).

Report issue for preceding element

∙∙\\bullet∙Output Tuning Requirement.
To ensure accurate parsing and interpretation of configurations generated by LLM, output formats are explicitly specified in the prompt. For instance, LLMBench \[ [244](https://arxiv.org/html/2505.18458v1#bib.bib244 "")\] requires that recommended knob values be returned in JSON format, while LATuner \[ [132](https://arxiv.org/html/2505.18458v1#bib.bib132 "")\] enforces constraints such as excluding the use of the “None” value in the configuration output.

Report issue for preceding element

(2) Automatic Tuning Prompt Generation.
To improve the efficiency of prompt generation for different workloads, existing methods propose the following techniques to automate the process of identifying effective prompts.

Report issue for preceding element

∙∙\\bullet∙Input Specific Prompt Generation.
To identify the most suitable prompts for varying tasks, existing methods automatically tailor prompt generation based on specific inputs.
For example, DB-GPT \[ [497](https://arxiv.org/html/2505.18458v1#bib.bib497 "")\] introduces an automatic prompt generation framework that leverages LLM to produce multiple instruction candidates, selecting the optimal ones using scoring functions associated with the performance improvement.
Additionally, DB-GPT \[ [497](https://arxiv.org/html/2505.18458v1#bib.bib497 "")\] and LLMIdxAdvis \[ [479](https://arxiv.org/html/2505.18458v1#bib.bib479 "")\] select demonstration examples in the prompts based on semantic similarity between candidate examples and input queries, as computed by a model-based encoder.

Report issue for preceding element

∙∙\\bullet∙Optimization Problem Formulation.
To reduce token usage and convey the most relevant context to the LLM, some methods formulate prompt generation as a cost-based optimization problem.
For instance, λ⁢-⁢T⁢u⁢n⁢e𝜆-𝑇𝑢𝑛𝑒\\lambda\\text{-}Tuneitalic\_λ - italic\_T italic\_u italic\_n italic\_e\[ [157](https://arxiv.org/html/2505.18458v1#bib.bib157 "")\] compresses workload representations by modeling the selection of join conditions as an integer linear programming problem, introducing binary decision variables to capture the positional relationships of different columns.

Report issue for preceding element

RAG Based Tuning Experience Enrichment.
The second method builds an offline knowledge base from diverse external sources and performs online retrieval to provide LLM with context-specific knowledge (e.g., similar historical tuning cases). This approach addresses the limitations of direct prompting, which often yields overly generic responses lacking concrete commands and effective configurations \[ [97](https://arxiv.org/html/2505.18458v1#bib.bib97 "")\].

Report issue for preceding element

(1) LLM Based Tuning Experience Preparation.
Given that existing tuning knowledge is distributed across heterogeneous formats, LLMs are employed to construct a knowledge base by processing and integrating multi-source external experience in an offline manner.
For example, GPTuner \[ [224](https://arxiv.org/html/2505.18458v1#bib.bib224 "")\] prompts LLM to extract implicit knowledge, remove noisy content, and summarize relevant information from multiple sources. Additionally, it introduces a prompt ensemble algorithm that generates multiple prompts by varying the demonstration examples, aiming to mitigate hallucination issues.

Report issue for preceding element

(2) Semantic Based Tuning Experience Retrieval.
To improve the accuracy of relevant experience retrieval, existing methods employ model-based encoders to capture semantic relationships (e.g., documents conveying similar meanings with different expressions).
For instance, Andromeda \[ [97](https://arxiv.org/html/2505.18458v1#bib.bib97 "")\] utilizes a Sentence-BERT encoder trained with contrastive learning to generate embeddings, which are then used to perform similarity searches across various sources, including historical queries and troubleshooting manuals.

Report issue for preceding element

Training Enhanced Tuning Goal Alignment.
The third method introduces additional training to further refine LLMs, improving their alignment with tuning objectives.
For example, DB-GPT \[ [497](https://arxiv.org/html/2505.18458v1#bib.bib497 "")\] proposes techniques to facilitate effective fine-tuning, including: (i) heuristic statistical data embedding, (ii) LLM-assisted annotation of high-quality samples, (iii) contrastive learning of supplementary training data generation, and (iv) delta tuning to minimize trainable parameters while maintaining performance.
Similarly, E2ETune \[ [178](https://arxiv.org/html/2505.18458v1#bib.bib178 "")\] fine-tunes LLMs (e.g., Mistral-7B) using training data comprising “ _(workload) →→\\rightarrow→ (configuration)_” pairs, where diverse workloads are generated via GPT-4 prompting and optimal configurations are identified using the HEBO algorithm \[ [113](https://arxiv.org/html/2505.18458v1#bib.bib113 "")\].

Report issue for preceding element

#### 3.3.2 LLM for Query Optimization

Report issue for preceding element

Query optimization aims to accelerate SQL execution through logical (e.g., query rewriting) and physical (e.g., join order and plan selection) enhancements.
Traditional logical optimization relies on predefined rewrite rules or learning-based approaches to determine rule application order, while physical optimization employs heuristic algorithms using statistical data or learning-based techniques leveraging query plan features. However, these approaches often overlook external SQL optimization knowledge, limiting their effectiveness and generalizability across diverse SQL patterns.

Report issue for preceding element

To address these limitations, recent studies investigate the use of LLM to directly rewrite input SQL queries or determine optimal rule application sequences for logical optimization.
They also explore leveraging LLM to select optimal query execution plans for physical optimization, drawing on the extensive SQL optimization knowledge encoded within the model.
These methods can be broadly categorized as follows.

Report issue for preceding element

Optimization-Aware Prompt Engineering.
The first method directly employs LLMs to perform query optimization using well-structured prompts composed of two key components: (i) manually crafted templates enriched with task-specific details (e.g., explicit task instructions), and (ii) relevant optimization examples automatically selected to more effectively guide the optimization process.

Report issue for preceding element

(1) Manually-Crafted Optimization Prompt.
Existing methods construct prompts with the following components to facilitate the query optimization task.

Report issue for preceding element

∙∙\\bullet∙Optimization Task Instruction.
To clarify the optimization objective and guide LLMs to produce specific optimization actions, detailed task instructions are included in the prompts.
For logical query optimization, some methods instruct LLMs to directly generate equivalent rewritten queries with improved performance (e.g., DB-GPT \[ [497](https://arxiv.org/html/2505.18458v1#bib.bib497 "")\], GenRewrite \[ [262](https://arxiv.org/html/2505.18458v1#bib.bib262 "")\], and LITHE \[ [368](https://arxiv.org/html/2505.18458v1#bib.bib368 "")\]), while others ask them to determine the optimal sequence of rewrite rule applications for a given query (e.g., LLM-⁢R2LLM-superscript𝑅2\\textsc{LLM}\\text{-}R^{2}smallcaps\_LLM - italic\_R start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT\[ [249](https://arxiv.org/html/2505.18458v1#bib.bib249 "")\] and R-Bot\[ [374](https://arxiv.org/html/2505.18458v1#bib.bib374 "")\]).
For physical query optimization, some approaches prompt LLMs to generate complete query plans with specified operators and join orders (e.g., LLM-QO \[ [197](https://arxiv.org/html/2505.18458v1#bib.bib197 "")\]), while others instruct LLMs to generate optimization hints or select the most effective plan from a set of candidates (e.g., LLMOpt \[ [446](https://arxiv.org/html/2505.18458v1#bib.bib446 "")\]).

Report issue for preceding element

∙∙\\bullet∙Input Optimization Context.
To enable effective query optimization for specific workloads, existing methods augment prompts with additional contextual information to better inform LLMs. This includes:
(i) Database Statistics: column selectivity \[ [368](https://arxiv.org/html/2505.18458v1#bib.bib368 "")\], histograms, distinct value counts, and estimated cardinalities \[ [197](https://arxiv.org/html/2505.18458v1#bib.bib197 "")\];
(ii) Rule Specifications: a list of applicable rewrite rules accompanied by usage descriptions (e.g., GenRewrite \[ [262](https://arxiv.org/html/2505.18458v1#bib.bib262 "")\] presents natural language hints as the rules) and illustrative examples \[ [249](https://arxiv.org/html/2505.18458v1#bib.bib249 "")\].

Report issue for preceding element

∙∙\\bullet∙Output Optimization Requirement.
To ensure that the optimizations produced by LLMs are valid and easily processed for downstream use, some methods explicitly define output formatting requirements within the prompts.
For example, LLM-⁢R2LLM-superscript𝑅2\\textsc{LLM}\\text{-}R^{2}smallcaps\_LLM - italic\_R start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT enforces that selected rewrite rules be returned in the format “rules selected: \[rule names\]” \[ [249](https://arxiv.org/html/2505.18458v1#bib.bib249 "")\], while LLM-QO specifies that the generated query plan should follow the “join operator(table1, table2)” format \[ [197](https://arxiv.org/html/2505.18458v1#bib.bib197 "")\].

Report issue for preceding element

(2) In-Context Learning with Optimization Example.
Rather than relying on fixed examples to illustrate how LLM should perform optimization, some methods automatically retrieve examples that are semantically similar to the input query to provide more effective guidance.
For instance, LLM-⁢R2LLM-superscript𝑅2\\textsc{LLM}\\text{-}R^{2}smallcaps\_LLM - italic\_R start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT\[ [249](https://arxiv.org/html/2505.18458v1#bib.bib249 "")\] introduces a contrastive representation model to encode query plans based on features such as operators, cardinalities, and costs, and retrieves a set of high-quality demonstrations, i.e., successfully optimized rewritten queries.

Report issue for preceding element

RAG Based Optimization Experience Enrichment.
The second method adopts the retrieval-augmented generation (RAG) paradigm to equip LLM with relevant contextual information for targeted optimization of specific queries.
It constructs and retrieves optimization knowledge from multiple sources that are semantically related to the input query.

Report issue for preceding element

(1) LLM Based Optimization Experience Preparation.
To consolidate optimization experience from multiple sources, existing methods introduce an offline preparation pipeline that leverages LLM to process and integrate data into a unified format.
For example, R-Bot \[ [374](https://arxiv.org/html/2505.18458v1#bib.bib374 "")\] employs LLM to generate rewrite rule specifications by (i) summarizing rule code within a hierarchical structure and (ii) extracting information from structured documentation blocks.
It further uses LLM to standardize the resulting specifications, explicitly outlining application conditions and detailed rewrite transformations.

Report issue for preceding element

(2) Hybrid Optimization Experience Retrieval.
To more accurately identify relevant optimization experiences, both structural and semantic characteristics of the input queries are considered during similarity search.
For instance, R-Bot \[ [374](https://arxiv.org/html/2505.18458v1#bib.bib374 "")\] introduces a hybrid retrieval approach that computes similarity using concatenated embeddings capturing structural features (e.g., rewrite rule explanations) and semantic representations (e.g., query template structures).
Based on the retrieved experience, R-Bot employs a step-by-step LLM-driven rewrite process, further enhanced through a self-reflection mechanism to improve rewrite quality.

Report issue for preceding element

Training Enhanced Optimization Improvement.
The third method either uses LLM outputs to train smaller models or fine-tunes LLMs on task-specific data to support various query optimization tasks (e.g., query plan generation).
For instance, LLMSteer \[ [53](https://arxiv.org/html/2505.18458v1#bib.bib53 "")\] uses LLM-generated embeddings to train a classifier for selecting optimal hints of the input SQL.
LLM-QO \[ [197](https://arxiv.org/html/2505.18458v1#bib.bib197 "")\] fine-tunes LLMs to generate execution plans directly through a two-stage pipeline: (i) Query Instruction Tuning (QIT) for producing valid plans; (ii) Query Direct Preference Optimization (QDPO) for distinguishing high-quality plans.
The fine-tuning data is structured as “ _(query, task instruction, auxiliary information such as schema and statistics, demonstration)_” paired with the corresponding efficient execution plan.
LLMOpt \[ [446](https://arxiv.org/html/2505.18458v1#bib.bib446 "")\] fine-tunes two models: (i) LLMOpt(G), which generates candidate hints, and (ii) LLMOpt(S), which selects the optimal hint as a list-wise cost model.
The fine-tuning data is structured as “ _(query, statistics such as histograms) →→\\rightarrow→ (optimal hint)_” for LLMOpt(G) and “ _(query, statistics such as histograms, candidate hints) →→\\rightarrow→ (index of optimal hint)_” for LLMOpt(S).

Report issue for preceding element

#### 3.3.3 LLM for Anomaly Diagnosis

Report issue for preceding element

Anomaly diagnosis focuses on analyzing root causes and identifying recovery solutions for anomalies (e.g., spikes in system resource usage) during the system runtime, such as databases.
Traditional rule-based methods often fail to accurately identify root causes across diverse scenarios, while classical machine learning models (e.g., random forests) cannot generate comprehensive reports with detailed recovery solutions.

Report issue for preceding element

Recent studies demonstrate that LLMs, with their advanced textual understanding and reasoning capabilities, can effectively pinpoint root causes and generate detailed diagnosis reports with recovery solutions in various formats.
These LLM-based approaches can be categorized as follows.

Report issue for preceding element

Manually Crafted Prompts for Anomaly Diagnosis.
The first method emulates the reasoning process of a human DBA, which involves referencing essential statistical information and conducting an in-depth analysis during diagnosis.
The information is incorporated into well-structured prompts to enhance diagnosis accuracy.
For example, DBG-PT \[ [156](https://arxiv.org/html/2505.18458v1#bib.bib156 "")\] utilizes LLM to detect query execution slowdowns caused by changes in query plans, using prompts that include: (i) a summary of plan differences, (ii) a request for feasible configuration recommendations, and (iii) a specification of the reasoning process with output formatted in JSON format.

Report issue for preceding element

RAG Based Diagnosis Experience Enrichment.
The second method adopts retrieval-augmented generation (RAG) paradigm to provide LLM with relevant diagnosis knowledge, leveraging two key components: a knowledge base and a retriever.
For instance, D-Bot \[ [496](https://arxiv.org/html/2505.18458v1#bib.bib496 ""), [495](https://arxiv.org/html/2505.18458v1#bib.bib495 "")\] enhances database anomaly diagnosis by preparing a corpus of documents and tools considering the hierarchical document structure, then using a fine-tuned Sentence-BERT encoder to retrieve relevant materials and guide LLM via prompts enriched with the retrieved content.
ByteHTAP \[ [433](https://arxiv.org/html/2505.18458v1#bib.bib433 "")\] supports LLM-based diagnosis of query performance regressions in HTAP systems by first constructing a knowledge base of historical queries and their associated performance explanations.
It then employs an enhanced tree-CNN classifier to encode and retrieve relevant plan pairs.
The retrieved information is incorporated into prompts that include: (i) background information (e.g., key differences among HTAP system engines), (ii) a task description (e.g., retrieved diagnosis knowledge with explicit input-output specifications), and (iii) additional user-provided context (e.g., recent index changes).

Report issue for preceding element

Multi-Agent Mechanism for Collaborative Diagnosis.
The third method adopts an agent-based diagnosis framework, where specialized agents with distinct responsibilities collaborate to improve diagnosis accuracy and efficiency.
For example, D-Bot \[ [496](https://arxiv.org/html/2505.18458v1#bib.bib496 ""), [495](https://arxiv.org/html/2505.18458v1#bib.bib495 "")\] orchestrates multiple domain-specific LLM agents, each aligned with a cluster of preprocessed diagnosis knowledge, to support precise anomaly diagnosis in databases.
These agents, coordinated by a chief agent, conduct multi-step root cause analysis via a tree-search algorithm.
Similarly, Panda \[ [363](https://arxiv.org/html/2505.18458v1#bib.bib363 "")\] emulates experienced database engineers by leveraging LLM agents across five functional components: (i) question verification to eliminate irrelevant queries, (ii) grounding to provide necessary input query context, (iii) verification to ensure diagnosis accuracy and source attribution, (iv) feedback integration to incorporate user input, and (v) affordance assessment to estimate the performance impact of generated solutions.

Report issue for preceding element

Localized LLM Enhancement via Specialized Fine-Tuning.
The last method employs specialized fine-tuning strategies for localized LLMs of modest scale (e.g., 6B-14B), leveraging distilled knowledge to approximate the outputs of larger models while achieving comparable performance.
For instance, D-Bot \[ [496](https://arxiv.org/html/2505.18458v1#bib.bib496 "")\] applies multi-task fine-tuning to improve the diagnosis capabilities of localized LLMs.
Specifically, three models (i.e., Llama2-13B, CodeLlama-13B, and Baichuan2-13B) are fine-tuned to replicate the diagnosis results generated by the GPT-4-powered D-Bot.
The fine-tuning dataset consists of samples covering D-Bot diagnosis workflows across five sub-tasks (e.g., tool invocation), along with associated prompts and historical dialogue messages.

Report issue for preceding element

Practices of LLMs for Data ManagementAlibaba Cloud \[ [5](https://arxiv.org/html/2505.18458v1#bib.bib5 "")\] has integrated Text-to-SQL features into its BI platform, facilitating NL queries over structured datasets. Amazon Nova \[ [3](https://arxiv.org/html/2505.18458v1#bib.bib3 "")\] employs automated document processing to extract structured information from diverse unstructured sources. In terms of data systems, PawSQL \[ [41](https://arxiv.org/html/2505.18458v1#bib.bib41 "")\], an advanced query optimization platform, offers both SQL rewriting and index recommendation capabilities, adopted by over 10,000 professionals. Database diagnosis also thrives on a robust ecosystem. For instance, DBDoctor \[ [35](https://arxiv.org/html/2505.18458v1#bib.bib35 "")\], compatible with mainstream databases, delivers kernel-level performance diagnostics for comprehensive system analysis and optimization.Report issue for preceding element

## 4 Challenges and Future Directions

Report issue for preceding element

### 4.1 Data Management for LLM

Report issue for preceding element

### 4.1.1 Task-Specific Data Selection for Efficient Pretraining

Report issue for preceding element

In LLM pre-training, vast amounts of general data are typically used, but much of this data may not be relevant to the target task. The inclusion of irrelevant data not only increases training time but also impedes the model’s adaptability to specific tasks. For instance, when training a model for the medical domain, unrelated data sources such as news articles and social media posts may hinder the learning of domain-specific knowledge. Consequently, the challenge lies in automatically selecting task-relevant data while discarding irrelevant information during pretraining. Currently, most approaches rely on hand-crafted filtering rules or fixed labeled datasets for data selection, lacking dynamic strategies that adapt to the model’s evolving task-specific needs. Exploring methods to automatically select relevant data and discard irrelevant data during pre-training represents a promising avenue for improving task adaptability and training efficiency.

Report issue for preceding element

### 4.1.2 Optimizing Data Processing Pipelines

Report issue for preceding element

Currently, the construction of data processing pipelines for LLMs relies heavily on experience and experimentation. For instance, in building the FineWeb dataset, decisions such as whether to use the WET or WARC format for text extraction from CommonCrawl, or whether to apply a global MinHash approach for deduplication or perform it separately for each snapshot, are made only after training models and benchmarking their performance. However, this experimental methodology is resource-intensive. In the case of FineWeb, over 70 models with 1 billion parameters were trained, consuming a total of 80,000 H100 GPU hours. To improve the efficiency of these pipelines, future research should focus on developing data-driven methods that can predict optimal preprocessing configurations. in advance, reducing the reliance on costly trial-and-error approaches. This would not only minimize computational costs but also accelerate the development of high-quality datasets for LLMs.

Report issue for preceding element

### 4.1.3 LLM Knowledge Update and Version Control

Report issue for preceding element

In fast-evolving domains (e.g., healthcare, finance, law), knowledge is constantly updated. To ensure the reliability of LLMs, the data used for training and fine-tuning must be up-to-date. Delays in incorporating the latest knowledge can result in outdated or harmful outputs, particularly in fields like medicine where guidelines frequently change. While there have been various approaches to data synthesis and augmentation, little attention has been given to efficiently managing rapid knowledge updates or resolving contradictions when new information conflicts with older data. Existing systems often rely on static datasets, which are problematic in dynamic sectors. Although platforms like ChatGPT and Deepseek allow LLMs to search the web, this approach may not always guarantee accuracy or relevance, leading to suboptimal results. A more effective solution would involve a platform that facilitates the creation, sharing, and version control of datasets with real-time knowledge updates. By leveraging community-driven contributions, this platform could enable users to synthesize and share datasets using customizable methods, such as LLM-generated prompts from documents or websites, offering continuous, high-quality updates and improving the overall accuracy and reliability of LLMs.

Report issue for preceding element

### 4.1.4 Comprehensive Dataset Evaluation

Report issue for preceding element

The performance enhancement of models is closely tied to the use of ’high-quality’ datasets. However, determining what constitutes a high-quality dataset remains a challenge. Typically, the quality of a dataset can only be inferred after training and evaluating a model, which makes the process indirect and resource-intensive. When a dataset’s quality is subpar, it can lead to significant computational overhead and inefficiencies. While existing research  \[ [399](https://arxiv.org/html/2505.18458v1#bib.bib399 "")\] has proposed a model-agnostic method for evaluating datasets across three aspects: reliability, difficulty, and validity. These dimensions alone do not fully capture a dataset’s quality. The current framework falls short of providing a comprehensive evaluation that aligns with the model’s capabilities and performance improvements. Therefore, a promising direction for future research is the development of a robust dataset evaluation system that does not rely on model training. This system should provide consistent quality scores that directly correlate with model performance enhancements, enabling more efficient dataset selection and use without the need for exhaustive training cycles.

Report issue for preceding element

### 4.1.5 Hybrid RAG Indexing and Retrieval

Report issue for preceding element

Currently, there lacks a single database that integrates full-text, vector, knowledge graph, and structured search interfaces into a cohesive indexing and retrieval engine for Retrieval-Augmented Generation (RAG) training. While systems like Elasticsearch \[ [36](https://arxiv.org/html/2505.18458v1#bib.bib36 "")\] excel in full-text and vector search, and LightRAG \[ [165](https://arxiv.org/html/2505.18458v1#bib.bib165 "")\] has introduced advanced vector and graph processing, these solutions remain siloed. They lack a unified platform designed specifically for hybrid RAG, where multiple indexing and search mechanisms coexist to support efficient downstream applications. Although emerging platforms like AutoRAG \[ [210](https://arxiv.org/html/2505.18458v1#bib.bib210 "")\] provide frameworks for constructing RAG pipelines, they focus on workflow management, model integration, and automation rather than offering a fully integrated database with indexing and retrieval engines. A promising direction for future RAG data serving is the development of an integrated platform that provides seamless indexing and retrieval for diverse data types, while also integrating data serving features such as knowledge filtering and re-ranking \[ [47](https://arxiv.org/html/2505.18458v1#bib.bib47 "")\], thereby improving the efficiency and flexibility of RAG applications.

Report issue for preceding element

### 4.2 LLM for Data Management

Report issue for preceding element

### 4.2.1 Unified Data Analysis System

Report issue for preceding element

One of the major challenges in LLM for Data Analysis is the absence of a unified system capable of handling diverse data types. Currently, analyzing different data formats often requires designing task-specific models separately. The most straightforward approach to enabling a system to process all types of data is to integrate these models into a single framework. However, this leads to prohibitively high deployment and maintenance costs due to the need to manage multiple models simultaneously.
A more promising direction is to develop a model that can flexibly accommodate various data inputs and user requirements while supporting the analysis of structured, semi-structured, and unstructured data. Such a system would establish a paradigm for LLM for Data Analysis at the system level and offer a generalized capability for analyzing data across different structural types, thereby facilitating data automation.

Report issue for preceding element

### 4.2.2 Data Analysis with Private Domain Knowledge

Report issue for preceding element

Another challenge in leveraging LLMs for data analysis is the effective utilization of private domain knowledge. Current approaches primarily rely on RAG to retrieve relevant knowledge or fine-tune models on domain-specific datasets. However, these methods struggle when dealing with novel or highly complex domain knowledge. For example, in Text-to-SQL tasks involving large-scale databases with 10,000 columns and 1,000,000 rows, where each column is associated with specific domain knowledge, existing techniques often fail to generalize effectively. The lack of datasets that explicitly incorporate domain knowledge further exacerbates this issue, making it difficult to meet the demands of real-world industrial applications. Consequently, developing more advanced mechanisms for integrating domain knowledge into LLMs remains a critical open research problem.

Report issue for preceding element

### 4.2.3 Representing Non-Sequential and Non-Textual Data

Report issue for preceding element

Current LLM-based approaches typically transform non-sequential and non-textual data into serialized textual formats to align with the input requirements of LLMs\[ [129](https://arxiv.org/html/2505.18458v1#bib.bib129 ""), [197](https://arxiv.org/html/2505.18458v1#bib.bib197 ""), [446](https://arxiv.org/html/2505.18458v1#bib.bib446 "")\].
While this enables basic compatibility, it overlooks the original structural semantics of the data and can lead to significant information loss in downstream tasks.
For instance, in data manipulation and analysis, relational tables (originally structured as two-dimensional matrices) are typically flattened into multiple serialized sequences, obscuring inherent row-column relationships \[ [78](https://arxiv.org/html/2505.18458v1#bib.bib78 ""), [74](https://arxiv.org/html/2505.18458v1#bib.bib74 ""), [320](https://arxiv.org/html/2505.18458v1#bib.bib320 "")\].
Similarly, in system optimization tasks, crucial statistical signals such as column selectivities and histograms are either omitted or naively encoded as plain texts, limiting their utility in guiding optimization decisions \[ [157](https://arxiv.org/html/2505.18458v1#bib.bib157 ""), [132](https://arxiv.org/html/2505.18458v1#bib.bib132 "")\].
Consequently, a promising future direction is to develop more expressive and task-aware representations that preserve the structural and statistical integrity of such data.
This includes leveraging multi-modal LLMs or designing tailored encoding strategies that maintain the uniqueness of these data types, thereby enabling more effective and semantically informed LLM applications.

Report issue for preceding element

### 4.2.4 Efficient LLM Utilization Under Budget Constraints

Report issue for preceding element

While LLMs have shown strong potential across data manipulation, analysis, and system optimization tasks, their high computational cost and latency pose challenges for real-time or large-scale applications \[ [197](https://arxiv.org/html/2505.18458v1#bib.bib197 ""), [53](https://arxiv.org/html/2505.18458v1#bib.bib53 "")\].
For example, relying solely on LLMs is impractical for processing tens of millions of rows in relational table analysis due to prohibitive resource demands \[ [440](https://arxiv.org/html/2505.18458v1#bib.bib440 ""), [305](https://arxiv.org/html/2505.18458v1#bib.bib305 "")\].
Similarly, current LLM-based query optimizers often require minutes per query, far exceeding the millisecond-level efficiency of traditional statistical methods \[ [374](https://arxiv.org/html/2505.18458v1#bib.bib374 ""), [249](https://arxiv.org/html/2505.18458v1#bib.bib249 "")\].
Therefore, a promising direction is to develop hybrid strategies that integrate LLMs with traditional techniques or to devise scheduling mechanisms that allocate tasks across multiple LLMs based on cost-performance trade-offs.
Such approaches can enhance the practicality and scalability of LLM-based systems under real-world budget constraints.

Report issue for preceding element

## 5 Conclusion

Report issue for preceding element

In this paper, we summarize the recent techniques on DATA4LLM and LLM4DATA. The former focuses on utilizing data processing, storage, serving techniques to address the data problems in different LLM stages. The latter focuses on using LLM capabilities to reduce the complexity of conducting data management, e.g., data manipulation, data analysis, and data system optimization. We also provide some research challenges and open problems in DATA4LLM,
LLM4DATA, and hybrid data and LLM optimization.

Report issue for preceding element

# Financial analysis with ChatGPT: possibilities and limitations

Publication:

27. Juni 2025

- updated: 06. Aug. 2025

Ever since ChatGPT outperformed professional financial analysts in a study by the University of Chicago, they have been asking themselves how they can use the tool as profitably as possible. The field of application in finance and accounting has recently been expanded considerably, and precision is increasing. This is also due to the improved mathematical capabilities of the model, which benefit financial analyses, forecasts and decision-making. Of course, there are still some shortcomings - compared to human analysts and professional enterprise AI software.

Table of contents

## Growing relevance for the financial sector

In recent decades, finance has been increasingly characterized by data-driven processes. Complex financial decisions, whether in the area of treasury management, strategic controlling or company valuation, are now made on the basis of extensive data sets and detailed analyses. Against this backdrop, data processing and analysis technologies are becoming increasingly important. Artificial intelligence (AI), particularly in the form of language models, offers opportunities for automation and increased efficiency. Unlike traditional business intelligence tools or statistical models, ChatGPT has the ability to process natural language in a context-sensitive manner. This capability opens up new fields of application, as it allows the tool not only to analyze financial data, but also to present it in a narrative form - a function that is particularly valuable when communicating complex content with non-financial stakeholders.

In practice, ChatGPT can be used for automated financial reporting, scenario analyses or language translation of complex financial reports, among other things. It also offers starting points for decision simulations using hypothetical scenarios. This makes the application a low-threshold entry into data-based financial analyses, even for companies that do not have access to fully integrated enterprise solutions. However, the integration of ChatGPT into everyday professional finance raises important questions. From data protection and ethical use to the validity and robustness of the results - it is essential to take a critical look at these aspects and clearly define the areas in which its use makes sense and where specialized software solutions remain superior.

## Practical application possibilities

The versatility of ChatGPT is demonstrated by the breadth of possible applications within the financial value chain. Here are some practical application examples for financial professionals:

### Automated creation of financial reports

The preparation of regular reports, such as quarterly or annual financial statements and internal reports, is a central component of day-to-day financial work. [KPI reports](https://konfuzio.com/en/report-automation/) for management. In this area, ChatGPT can create significant time advantages by processing structured data records.

**Example:**

A financial analyst enters the most important key figures of a company for the past quarter - such as sales, operating costs, depreciation and net results. With appropriate input, such as "Create a narrative report on sales and cost development as well as net results and point out significant trends", ChatGPT generates a complete, structured report. Optionally, benchmark data can also be included to integrate a peer group analysis.

### Development and comparison of scenarios for future cash flows

Another area of application is scenario analysis. ChatGPT can serve as a supporting tool, particularly when predicting future development opportunities, by modeling hypothetical business scenarios according to certain parameters.

**Example:**

A company's treasury team would like to simulate the effects of an inflation rate of 5 % and a simultaneous reduction in operating costs through efficiency measures. ChatGPT can perform a qualitative assessment of the scenario based on defined parameters (e.g. "What is the impact of scenario X on free cash flow?") and highlight potential risks.

### Automation of peer analysis based on public financial data

ChatGPT can be used to compare publicly available reports from listed companies.

**Example:**

With a query such as "Compare the gross margins of ABC Corp, DEF Corp and GHI Inc. in 2022", ChatGPT extracts relevant information from the reports and generates a structured comparison overview. Such applications significantly save time and reduce the manual effort of reviewing reports individually.

### Risk modeling for budget planning

The modeling of risks within a budgeting process is one of the core tasks of controlling. ChatGPT can evaluate hypothetical parameter structures in narrative analyses and thus support the decision-making process.

**Example:**

A company is preparing a budget plan for the next five years and would like to know what impact an interest rate increase of 2 % could have on projected investment loans. ChatGPT generates a qualitative assessment and suggests potential measures to mitigate the risk.

### Further background information

<Base64-Image-Removed>

By loading the video, you accept YouTube's privacy policy.

[Load video](https://konfuzio.com/en/chatgpt-financial-analysis/#)

Always unlock YouTube

Video overview of relevant use cases for analysts.

## Fictitious use case: Scenario analysis to increase profits

BetaClean GmbH is a medium-sized supplier of cleaning systems for industrial applications. The company is facing the challenge of cushioning rising raw material costs with stagnating sales volumes. To address this, the management is considering a price increase of 8 %, coupled with optimizations in the supply chain. The aim is to secure the profit margin for the coming financial year. All data was generated and processed using ChatGPT as an example.

### Calculations and scenario analysis

**1. initial figures 2023 (reference):**

- Turnover: € 100 million
- Variable costs: € 55 million
- Fixed costs: € 20 million
- Profit: € 25 million

**2. forecasts for 2024 - without adjustment:**

- Turnover remains at € 100 million, fixed costs remain constant.
- Variable costs increase to € 58 million.
- Profit falls from € 25 million to € 22 million (-12 %).

**3rd forecast with price increase (+8 %) and reduced demand (-2 %):**

- Calculated turnover:

€100m x (1.08⋅0.98)=€105.84m
- Variable costs: Increase proportionally:

55m€ x 105.84/100=57.9m€.
- Fixed costs remain unchanged at € 20 million.
- Profit:

105.84m€ - (57.9m€ + 20m€) = 27.94m€.

**Results in comparison:**

| Scenario | Turnover (€ million) | Variable costs (€ million) | Fixed costs (€ million) | Profit (€ million) |
| --- | --- | --- | --- | --- |
| 2023 (actual) | 100,00 | 55,00 | 20,00 | 25,00 |
| 2024 (old, unoptimized) | 100,00 | 58,00 | 20,00 | 22,00 |
| 2024 (new, optimized) | 105,84 | 57,90 | 20,00 | 27,94 |

### **Findings from the modeling**

1. The planned price increase of 8 % more than compensated for the decline in demand of 2 %. As a result, turnover rose to € 105.84 million.
2. Profit improves despite increased variable costs (€ 57.9 million) and remains robust at € 27.94 million. This corresponds to an increase of € 27 % compared to the unsupported 2024 scenario (€ 22 million).
3. Supply chain optimization will only have a limited impact as long as raw material prices continue to rise. Continuous monitoring of these factors is essential.

### **Visualization**

The following prompt can be used to visualize the development of the parameters:

**Prompt:**

> "Create a stacked bar chart that compares the turnover, variable costs, fixed costs and profit of BetaClean GmbH in 2023, in the unoptimized scenario 2024 and in the optimized scenario 2024. The X-axis should show the years (2023, 2024-old, 2024-new), the Y-axis the amounts in € million. Use contrasting colors to clearly highlight the individual parameters."

**Additional visualization idea**:

- A separate line graph to show the percentage profit share of sales (profit margin).
- Color highlighting of the "leap" in profit development due to the optimization measures could be another added value.

## Study: ChatGPT compared with analysts

The [Study by the University of Chicago](https://venturebeat.com/ai/the-future-of-financial-analysis-how-gpt-4-is-disrupting-the-industry-according-to-new-research/) investigated the performance of GPT-4, one of OpenAI's most advanced language models, in financial analysis. The aim was to find out whether a Large Language Model (LLM) like GPT-4 is able to predict the future profit development of companies based on standardized, anonymized balance sheet and profit and loss statements (P&L) - without any textual context. An innovative method was used here: so-called "chain-of-thought" prompts systematically guided the model through the analysis process of a financial analyst. This approach included key steps such as identifying trends, calculating key financial ratios and drawing conclusions about future developments.

The result: GPT-4 achieved a prediction accuracy of 60 %, which is above the range of 53-57 % typically achieved by human analysts. In addition, a [F1 score](https://konfuzio.com/en/llm-benchmarks/#wichtige-metriken-zur-leistungsbewertung-und-evaluierung) of 0.609 was achieved, which further underlines the precision and robustness of the predictions. The researchers note that GPT-4's extensive knowledge base and pattern recognition capability allows it to draw intuitive conclusions even with incomplete data. Impressively, GPT-4 has proven itself in a traditionally difficult area for AI - namely numerical analysis. Despite its potential, however, the researchers emphasized that the model's results should always be validated by human experts. The study emphasizes that such LLMs could not replace the work of financial analysts, but rather complement it and make it more efficient by speeding up time-consuming tasks such as financial data analysis. The study thus shows the transformative potential of AI in finance, especially in precise and data-driven decision-making.

<Base64-Image-Removed>

By loading the video, you accept YouTube's privacy policy.

[Load video](https://konfuzio.com/en/chatgpt-financial-analysis/#)

Always unlock YouTube

Background discussion on the study regarding financial statement analyses.

## Limitations and risks

Despite the potential benefits of ChatGPT in financial analysis, financial professionals should be aware of some critical limitations and risks. These arise from both the technical nature of the tool and the specific requirements of the financial sector:

- **Data quality and scope for interpretation** - The accuracy and reliability of the insights provided by ChatGPT depends on the quality of the underlying data. Inaccurate or insufficiently cleansed data can lead to misleading forecasts or analyses. In addition, ChatGPT's ability to interpret data correctly is limited to the available inputs and contextual information, which can be problematic for complex financial models or market determinations. Errors due to text-based probability assumptions cannot be ruled out either.
- **Limited industry specificity and application understanding** - Even though ChatGPT has impressive text processing capabilities, the AI lacks a deep understanding of nuanced industry or business-specific topics. For example, the model is not able to comprehensively understand the highly specialized requirements of areas such as investment banking, risk management or treasury operations. This can lead to industry-specific patterns, legal peculiarities or regulatory requirements being overlooked.
- **Data protection, security and compliance** - A key risk lies in the processing of sensitive data by public AI models. Financial data is among a company's most sensitive information and is subject to strict legal and regulatory requirements. Feeding such data into an AI such as ChatGPT can not only violate data protection regulations such as the GDPR, but also create potential security vulnerabilities. Companies must ensure that confidential information does not end up in external systems whose security mechanisms can only be traced to a limited extent.
- **Lack of transparency and traceability** - The "black box" nature of many AI models, including ChatGPT, is an obstacle for many financial experts. The lack of transparency in decision-making can be particularly problematic in the context of compliance audits or the creation of audit-proof documentation. It is essential for financial professionals to be able to justify analyses or forecasts in detail - a requirement that generative AI models cannot always fulfill.

## The solution - specialized AI software

Konfuzio's specialized AI software overcomes ChatGPT's limitations in financial analytics by providing industry-specific functionalities, highest data security and traceability:

1. **Functionality** - Konfuzio is specialized in specific financial applications such as [Balance sheet analysis](https://konfuzio.com/en/balance-sheet-analysis-financial-spreading-software/) or [Analysis of annual financial statements](https://konfuzio.com/en/automate-financial-statement-analysis/) recognizes data from complex formats and delivers precise, customizable results that take industry-specific requirements into account. Data pipelines can be individually defined in order to be used for corresponding **Traceability and controls** to provide. In addition, individually customizable [Conversational AI for banks](https://konfuzio.com/en/conversational-ai-in-banks/) available.
2. **Data security & hosting** - With the possibility of **On-prem hosting** guaranteed GDPR compliance and full data control, Konfuzio minimizes risks that exist with public AI models such as ChatGPT. Sensitive financial data remains on its own servers or in the private cloud.
3. **Integration** - Konfuzio can interact with various company applications via web-based interfaces and is therefore not dependent on manual input. Compared to ChatGPT, a significantly greater variety of data is used with a higher degree of automation.

## Conclusion

ChatGPT is a relevant tool for operational financial processes, especially when it comes to increasing the efficiency of standardized tasks. For complex applications with high demands on precision, transparency and data protection, specialized software solutions, such as those offered by Konfuzio, remain indispensable. The decisive criterion when using ChatGPT is the integration of the most robust validation and control processes in order to guarantee the integrity of all financial results.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="multimodal-pdf-retrieval-with-snowflake-cortex-arctic-agenti.md">
<details>
<summary>Evaluating Multimodal vs. Text-Based Retrieval for RAG with Snowflake Cortex</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.snowflake.com/en/engineering-blog/arctic-agentic-rag-multimodal-pdf-retrieval/>

Gen AI

Apr 21, 2025\|8 min read

# Evaluating Multimodal vs. Text-Based Retrieval for RAG with Snowflake Cortex

https://www.snowflake.com/adobe/dynamicmedia/deliver/dm-aid--b1aa056b-f206-4c84-bcb1-5337938b10e6/sf-eng-blog-ml-0.png?preferwebp=true&quality=85

In this blog post, we show how we improved Snowflake Cortex AI multimodal retrieval by treating each PDF page as a stand-alone image — allowing natural language queries to match both text _and_ visuals. We walk through our results, highlighting when this works best (and when it doesn’t).

➡️ [Try it yourself with our open source example](https://github.com/Snowflake-Labs/cortex-search/tree/main/examples/08_multimodal_rag)

## Why traditional RAG struggles with enterprise PDFs

Enterprise PDFs push traditional text-based retrieval systems to their limits. These documents combine long-form text, financial tables, technical diagrams and slide visuals — all packed into complex layouts that don’t play nicely with traditional retrieval-augmented generation (RAG) systems.

Traditional RAG pipelines break down in the face of rich, structured layouts for three reasons:

- **OCR is error-prone:** Optical character recognition (OCR) is the process of converting text from images — such as scanned PDFs or photos — into machine-readable text. While Snowflake’s `PARSE_DOCUMENT` and other OCR tools are powerful, they can stumble on older scans, unconventional layouts or blurry text. Errors here ripple downstream, weakening both retrieval and generation quality.

- **Visual data is lost:** Charts and diagrams often contain the most important insights — but since these are not extractable as text, they are often invisible to the model.

- **Workflow is complex:** Multistep pipelines (OCR → chunk → embed → search) can be hard to operationalize. They require tuning, orchestration and infrastructure — a tall order for many enterprise teams.

These challenges inspired us to rethink retrieval from the ground up. What if, instead of extracting text, we treated PDFs as multimodal documents from the start — and matched queries directly against their visual and textual content?

## Our multimodal approach: Searching PDFs as images

Instead of extracting text from PDFs using OCR, which often misses layout and visual context, _we treat each page as a stand-alone image_.

This preserves both the structure and content — including charts and tables — in a single snapshot. We then embed each image into the same vector space as natural language queries, enabling unified search across both text _and_ visuals.

This design offers key advantages:

- **No need for OCR:** No manual parsing – the full layout is preserved by default.

- **Visual awareness:** Queries can match based on tables, diagrams or slide content — even when no clean text exists.

- **Efficiency:** Each page uses a single embedding, reducing compute and latency costs.

While many multimodal systems use patch-based models (for instance, ColBERT-style late interaction), we focus on _single-vector models_ for better efficiency at scale.

### Models we evaluated

To compare retrieval effectiveness across document types, we tested several single-vector multimodal models:

- Voyage Multimodal 3 (Snowflake Cortex functions, closed source)

- GME-Qwen2-VL (2B and 7B, open source)

- Nomic-Embed-Multimodal (3B and 7B, open source)

For baseline comparisons, we also evaluated text-only retrieval using OCR for `PARSE_DOCUMENT`. All text embeddings used Voyage Multilingual 2, a strong multilingual model, to ensure a fair comparison with billion-scale multimodal models.

This unified evaluation setup allowed us to directly compare retrieval power across both structured and unstructured enterprise content — from SEC filings to slide decks.

### Existing benchmarks aren't realistic — so we built one

Most popular benchmarks for multimodal document retrieval don’t reflect how search works in real enterprise settings. They often focus on question answering, where the model is already given the correct document or page and asked to extract a specific answer.

For example: _“What is 3M’s 2018 capital expenditure?”_ — along with a preselected cash flow statement. This tests whether the model can understand a page, not whether it can find that page _in the first place_.

Even retrieval-focused data sets such as ViDoRe (versions 1 and 2) operate over small collections — usually thousands of pages at most. But real-world enterprise search systems must be able to operate over millions of pages, spanning a wide range of formats and layouts.

To better evaluate how retrieval systems perform under these conditions, we built a custom benchmark using three types of enterprise documents, each chosen to address a specific challenge (see table 1):

- **Tech manuals**( [such as this one](https://www.publications.usace.army.mil/USACE-Publications/Engineer-Manuals/)): Dense guides filled with diagrams, spec tables and nonlinear layouts that are difficult for traditional text-based methods. To evaluate different retrieval strengths, we split queries into two groups: one focused on charts, the other on text.

- **SEC financial filings:** A large collection of quarterly reports, annual statements and regulatory documents. Building on our [previous work](https://www.snowflake.com/en/engineering-blog/impact-retrieval-chunking-finance-rag/), these are ideal for evaluating structured text retrieval, across long, table-heavy documents.

- **Presentation slides (SlideVQA):** Visually rich decks where layout and graphics carry key information, ideal for testing multimodal retrieval.

This setup let us evaluate retrieval performance across a wide range of structured and visual document formats, reflecting realistic, large-scale conditions.

| | | | |
| --- | --- | --- | --- |
| **Data set** | **\# Queries** | **\# Relevant pages per query** | **\# Pages in the collection** |
| Tech Manuals (Chart) | 143 | 1.0 | 27,000 |
| Tech Manuals (Text) | 69 | 1.3 | 27,000 |
| SEC Financial Filings | 495 | 3.9 | 2.3 million |
| SlideVQA | 2,215 | 1.3 | 52,000 |

_Table 1. Statistics of data sets used in this study._

## What we learned: The best retrieval method depends on the document

With this evaluation framework in place, we tested how both text-based and multimodal retrieval methods performed across different document types and retrieval challenges.

To measure performance, we used:

- **Mean reciprocal rank (mRR):** Evaluates the average rank of the first correct result returned.

- **Embedding throughput:** The number of document embeddings generated per second, which assesses system efficiency, including the time cost of OCR for text-based methods.

### Multimodal models outperform on visual-heavy documents

The result? On technical manuals (chart-based queries) and presentation slides, multimodal models consistently ranked the correct page higher and achieved faster embedding throughput. These models were able to capture layout and visual structure that text-only pipelines missed.

https://www.snowflake.com/adobe/dynamicmedia/deliver/dm-aid--82938aa8-00be-4cfa-815e-3c2093bbb3c5/multimodalfig1.png?preferwebp=true&quality=85

Figure 1. Average mRR on tech manuals (text, chart) and SlideVQA versus throughput measured in number of embeddings generated per second. Text embedding models also need to account for time invested in OCR processing. The top right corner represents the best combination of quality and efficiency.

### Text-based retrieval still leads for structured documents

However, for financial reports, such as SEC filings — which feature clean text and highly structured tables — traditional pipelines using OCR and chunked text embeddings still delivered the highest retrieval accuracy. In these cases, the structure of the text itself was more informative than visual layout.

https://www.snowflake.com/adobe/dynamicmedia/deliver/dm-aid--7fd34372-53c9-4c28-bff2-46ee5bb3263f/multimodalfig2.png?preferwebp=true&quality=85

Figure 2. mRR on SEC filing reports versus throughput.

This confirmed a key insight: _Retrieval performance depends heavily on document type_. Multimodal systems excel with layout-heavy content, while text-based approaches remain strong for structured, well-formatted documents.

### No single modality wins everywhere

In some cases, results varied significantly by model, with text-based retrieval outperforming multimodal, depending on the setup.

To assess how this impacts the quality of generated answers, we ran a full RAG setup using Claude 3.5 Sonnet, a multimodal LLM capable of processing both text and images. For each query, we passed in content retrieved by text-only, multimodal or hybrid methods, then scored the model’s output for factual accuracy.

We used an LLM-as-a-judge system — an automated approach where another language model evaluates responses against human-verified correct answers. Final judgments were reviewed by humans for quality control.

https://www.snowflake.com/adobe/dynamicmedia/deliver/dm-aid--2835908b-0c9e-41cf-bc12-3dcc72325a3f/multimodalfig3.png?preferwebp=true&quality=85

Figure 3. Average answerability score across tech manuals, SEC filing reports and SlideVQA data sets versus model efficiency measured in embeddings per second. Multimodal models (blue) generally outperform text-based models (black) on visual-heavy documents, while text-based models show strength on structured documents.

These results demonstrate that optimal retrieval approaches vary significantly by document type, with no universal solution across different enterprise content formats.

## Combining the best of all worlds: Hybrid retrieval with Cortex Search

While multimodal models are strong at capturing layout and visual context, they — like text-based embeddings — often prioritize topical relevance. This can cause them to miss finer-grained matches, such as specific keywords, identifiers or phrases.

To address this, we built a hybrid retrieval strategy using Cortex Search, combining the strengths of multiple methods:

- **Multimodal embeddings:** To capture layout and visual structure

- **Keyword search:** For fast, high-precision filtering

- **Text-based reranking:** To refine top results based on semantic relevance

This approach significantly improved Recall@5, especially for ambiguous or mixed-format queries. While it introduces some additional system complexity and compute cost, the improvements in answer quality made it well worth it for most enterprise use cases.

https://www.snowflake.com/adobe/dynamicmedia/deliver/dm-aid--71efc0cc-ff1c-44ed-b872-19df22fac7f9/multimodal-fig4.png?preferwebp=true&quality=85

Figure 4. Augmenting multimodal vector retrieval with keyword search and neural reranking on Cortex Search leads to significant quality improvement.

Together, these retrieval strategies form a flexible foundation for building high-quality RAG systems that work across the full spectrum of enterprise documents — from structured filings to layout-heavy slide decks.

## Final takeaways

Should you use text embeddings or multimodal embeddings? It depends!

- For text-heavy PDFs in clean, OCR-friendly formats (such as financial reports), text embeddings typically perform best.

- For documents with complex layouts or heavy visual content (such as slides, manuals or charts), multimodal embeddings offer a clear advantage.

- _Snowflake Cortex Search supports all three approaches out of the box_, allowing teams to easily experiment, combine methods and scale high-quality retrieval across enterprise data.

Choosing the right retrieval method (or combination of them) can be the difference between a generic response and a precise, enterprise-grade answer.

## Interested in trying it out?

Contact your account representative to join as an early user and get access to this feature. Then check out the open source Jupyter notebook [Multimodal RAG with Cortex Search](https://github.com/Snowflake-Labs/cortex-search/tree/main/examples/08_multimodal_rag) to help you get started.

It walks through:

- PDF processing for both multimodal retrieval and OCR

- Indexing and searching with Cortex Search

- Running RAG-style prompting using retrieved results

Hit a snag or find something cool? Jump into the [Snowflake Community Forum](https://community.snowflake.com/s/login/) — we’re there to help and would love to see what you’re building.

## Explore more from the Arctic Agentic RAG series

This post is Episode 2 in our Arctic Agentic RAG series, in which we explore innovations in retrieval-augmented generation for enterprise AI.

- [Series Overview: Arctic Agentic RAG for Enterprise AI](https://www.snowflake.com/en/engineering-blog/arctic-agentic-rag-enterprise-ai/)

- [Episode 1: Clarifying Ambiguous Queries with Agentic RAG](https://www.snowflake.com/en/engineering-blog/arctic-agentic-rag-query-clarification/)

More episodes coming soon — stay tuned.

***

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="ocr-accuracy-explained-how-to-improve-it.md">
<details>
<summary>OCR Accuracy Explained: How to Improve It</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.llamaindex.ai/blog/ocr-accuracy>

# OCR Accuracy Explained: How to Improve It

https://cdn.sanity.io/images/7m9jw85w/production/08b48679423850d08df1c40b761fd82bb99f9929-1200x676.png?w=1200

OCR accuracy is one of those metrics that sounds simple until you try to actually measure it in production. 'Our system is 99% accurate' means almost nothing without knowing what that 99% is measuring, on what kinds of documents, and under what conditions.

The gap between OCR accuracy on clean, printed test documents and OCR accuracy on real-world business documents is where most projects run into trouble. A system that benchmarks at 98% in a controlled test can drop to 85% on your actual document corpus without anyone realizing it until the errors start causing downstream problems.

This article breaks down how OCR accuracy is actually measured, what causes performance to degrade, how to improve it, and how to choose a solution that holds up in production.

## How OCR Accuracy Is Actually Measured

OCR accuracy isn't a single number. Depending on what your system does with the extracted text, different metrics tell you different things. High-performing systems in 2026 are evaluated across three layers:

| Metric | What It Measures | 2026 Benchmark | When It Matters |
| --- | --- | --- | --- |
| **Character Error Rate (CER)** | % of characters incorrectly converted | < 1% printed; 3–5% handwriting | Archive digitization, legal documents |
| **Word Error Rate (WER)** | % of words containing at least one error | < 2% standard documents | NLP pipelines, searchable text |
| **Field-Level Accuracy** | Whether a specific field (e.g. invoice total) is 100% correct | 99.9% for critical financial fields | Invoice processing, KYC, data extraction |

### Character Error Rate (CER)

CER is the technical gold standard. It measures the percentage of individual characters that are incorrectly converted, calculated using Levenshtein distance—counting insertions, deletions, and substitutions needed to transform the OCR output into the correct text.

Formula: _CER = (Insertions + Deletions + Substitutions) / Total Characters in Ground Truth_

Current benchmarks: **below 1%** for clean printed text, while **3–5%** for handwriting recognition. CER is the right metric when you need character-level fidelity (, anything where a single wrong character changes meaning).

### Word Error Rate (WER)

WER tracks the percentage of words containing at least one error. It's less granular than CER but more intuitive for evaluating business utility. If a word is wrong, it's wrong, regardless of how many characters are off.

Current benchmark: **below 2%** for standard documents. WER is the relevant metric when extracted text feeds into NLP pipelines, search indexes, or any downstream process that operates at the word level.

### Field-Level (Semantic) Accuracy

This is the metric that matters most for document automation. Field-level accuracy measures whether a specific extracted field (such as invoice total, expiry date, or policy number) is completely correct, regardless of how accurate the surrounding text is.

A system can have 99% CER and still extract an invoice total incorrectly. That's an error that costs money. For financial fields and identity documents, the 2026 benchmark is **99.9%** field-level accuracy. This number is the threshold required to enable straight-through processing (STP), where documents move through the workflow without any human review.

## What Actually Affects OCR Accuracy

Even the best OCR engines fail when the input is flawed or the document type is outside their training distribution. These are the factors that most commonly degrade accuracy in real-world deployments.

### Image Resolution

Resolution is the most controllable factor and the one most often overlooked. Anything below 300 DPI causes a measurable drop in character recognition accuracy. Some studies put it at 20% or more for degraded scans. For high-stakes text extraction, 300–600 DPI is the current standard.

The practical implication: if your documents are being scanned at the point of intake, standardizing scan settings is one of the cheapest accuracy improvements available. It costs nothing to change a scanner setting; it costs a lot to correct downstream errors caused by low-resolution inputs.

### Document Types and Layout Complexity

OCR software struggles with layouts that deviate from clean, single-column text. Multi-column formats, nested tables, documents with overlapping text layers, faded watermarks, and embedded graphics all introduce recognition errors.

This is where the gap between traditional OCR and modern agentic document parsing becomes significant. Traditional OCR engines treat the page as a flat text grid. Layout-aware systems understand structure, capable of detecting column boundaries, identifying table cells, and processing each document region appropriately.

### Handwriting Variability

Handwriting recognition has improved substantially with LLM-based systems, but it remains the hardest problem in document processing. Cursive text, overlapping characters, non-standard letterforms, and mixed print-and-cursive documents still produce high character error rates even in top-performing systems.

The honest benchmark for handwriting: 3–5% CER is considered good. For anything requiring high accuracy on handwritten content, a human-in-the-loop validation step is still necessary for low-confidence extractions.

### Hardware and Infrastructure Constraints

Running local OCR models, like Tesseract, on underpowered machines introduces a class of errors that's easy to miss: tiling errors, where the engine processes the image in segments and misses text at segment boundaries. Low VRAM forces lower-resolution processing, which compounds with any existing image quality issues.

Cloud-based solutions sidestep this entirely. But for teams running on-premise for privacy or compliance reasons, hardware constraints need to be accounted for in accuracy benchmarking.

### Document Condition

Scanned paper documents carry physical artifacts that degrade OCR performance: fold lines, shadows, ink bleed, physical damage, coffee stains, skewed orientation. A 5-degree tilt can increase word error rate by 15% or more without pre-processing to correct it. Documents that look fine to a human reader can be surprisingly difficult for an OCR engine working from pixel data.

## How to Improve OCR Results: A Practical Toolkit

Improving OCR accuracy in practice is a pipeline problem, not an engine problem. The engine matters, but the biggest gains usually come from what happens before and after recognition.

### Phase 1: Pre-Processing

Pre-processing is where you clean the input before the OCR engine sees it. The most impactful techniques:

- **Binarization and denoising**: Converting images to high-contrast black and white while removing noise. Libraries like OpenCV handle this well. The goal is to give the OCR engine the clearest possible signal before recognition.
- **Adaptive deskewing**: Automatically detecting and correcting page orientation. A 5-degree tilt that looks minor visually can meaningfully spike your WER. Deskewing should be automatic, not manual.
- **Resolution normalization**: Upsampling low-DPI inputs to at least 300 DPI before processing. This won't recover detail that was never captured, but it prevents the engine from misreading artifacts caused by low-resolution rendering.

### Phase 2: Synthetic Data for Training

For teams training or fine-tuning their own models, synthetic data generation is now a standard practice. Tools like SynthOCR-Gen and Genalog create large volumes of labeled training documents that mimic real-world noise conditions—smudges, folds, compression artifacts, variable fonts.

The practical benefit: training on synthetic noisy data can reduce production error rates by up to 40% compared to models trained only on clean documents. The synthetic data teaches the model what real intake conditions actually look like, rather than the clean benchmark conditions it might otherwise optimize for.

### Phase 3: LLM Post-OCR Correction

This is the most significant development in OCR accuracy improvement over the past few years. Raw OCR output is passed through a language model with a targeted correction prompt—the model fixes clear misrecognitions without rewriting or paraphrasing the original text.

The key is prompt specificity. A prompt like "Fix ONLY OCR misrecognitions such as character transpositions or substitutions. Do not rewrite, rephrase, or improve the prose. Preserve original formatting exactly." produces far more reliable corrections than a generic proofreading prompt.

This approach works because language models have strong priors about what words and phrases should look like. An OCR output of 'app1e' gets corrected to 'apple' because the model recognizes the pattern. It's not a replacement for good OCR per se, but rather a validation layer that catches the errors that slip through.

LlamaParse handles this natively as part of its agentic document parsing pipeline. Rather than requiring you to build a separate post-processing step, the validation loops are built into the extraction workflow, with confidence scores surfaced at the field level so you know exactly where corrections were applied.

## Validation: Comparing Output Against Ground Truth

You can't improve what you don't measure. The only way to know your actual OCR accuracy is to compare OCR output against human-verified ground truth.

### Building a Ground Truth Set

A ground truth set is a sample of documents that have been manually verified to be 100% correct. The size requirement depends on your document variability: for a homogeneous corpus (one document type, consistent format), 5,000 words is usually sufficient to get stable accuracy estimates. For diverse, multi-format corpora, 10,000 words or more gives you a more reliable baseline.

The ground truth set should reflect your actual document distribution; not your cleanest documents, not your worst, but a representative sample. Accuracy measured on cherry-picked easy documents tells you nothing useful.

### Automated Comparison and the Cost-of-Error Framework

Once you have ground truth, automated diff tools can calculate CER, WER, and flag field-level discrepancies across your sample. The raw numbers are useful, but the more important framing is cost of error: what does each type of error actually cost your operation?

An error in a vendor name is an annoyance. An error in an invoice total is a financial risk. An error in a drug name on a medical record is a safety issue. Weighting your accuracy assessment by error cost tells you where to focus improvement efforts.

## Choosing Your OCR Solution: 2026 Landscape

The right solution depends on your document complexity, volume, accuracy requirements, and how much engineering overhead you're willing to carry. Here's an honest breakdown:

| Solution Type | Best For | Typical Accuracy |
| --- | --- | --- |
| **Open Source (PaddleOCR, Tesseract)** | High-volume, simple layouts, privacy-first | 88% – 94% |
| **Enterprise APIs (Google, Azure, AWS)** | Scalable, multi-language, standard forms | 96% – 98% |
| **Agentic Document Processing (LlamaParse)** | Complex documents, messy scans, tables, handwriting — with built-in validation loops | 99%+ with straight-through processing |

### Open Source: Where It Works and Where It Doesn't

Tesseract and PaddleOCR are legitimate options for high-volume, simple document types where privacy requirements make cloud processing impractical. They're free, customizable, and have active communities.

The ceiling is real though. On complex layouts, mixed content types, or degraded scans, open source OCR engines top out around 88–94% accuracy without significant additional engineering. That accuracy level is fine for some use cases; it's not sufficient for financial data extraction or any workflow where errors carry meaningful cost.

### Enterprise APIs: The Middle Ground

Google Document AI, Azure Form Recognizer, and AWS Textract represent the current enterprise standard for general-purpose document processing. They handle multi-language documents well, scale without infrastructure management, and perform reliably on standard document types.

The limitation is customization and complex document handling. These systems are optimized for common formats. When your documents are genuinely complex—irregular layouts, heavy tables, embedded charts, mixed handwriting and print—accuracy drops and you're left with limited ability to tune the system for your specific corpus.

### Agentic Document Processing: Why It's Different

This is where LlamaParse operates, and the distinction from traditional OCR is worth being precise about. LlamaParse is an agentic document parsing platform where OCR is one component of a larger orchestration system.

What that means in practice: an LLM orchestration layer decides which specialized model handles each element of a document. Text goes to the OCR engine, charts go to a vision model, tables get processed with layout-aware computer vision. The outputs are validated through multiple correction loops and stitched together into a single structured output—Markdown, JSON, or HTML—with confidence scores and source citations at the field level.

The practical result is that it handles the document types that break traditional OCR: complex invoices, multi-page contracts, scanned documents with mixed content, handwritten annotations on printed forms. And because the system is model-agnostic and layout-aware rather than template-dependent, it doesn't require retraining or reconfiguration when document formats change.

## Summary: Accuracy Is a Pipeline Problem

OCR accuracy is a pipeline problem. The engine you choose matters, but input quality, pre-processing, post-correction, and solution architecture often have a bigger impact on real-world performance than the model itself.

The first thing to understand is that accuracy means different things depending on what you're measuring. Character error rate tells you how many characters are wrong. Word error rate tells you how many words are wrong. Field-level accuracy tells you whether the specific data you actually need is correct. For document automation, field-level accuracy is the only number that matters, and 99.9% is the threshold you need to hit to enable straight-through processing.

Getting there requires working every part of the pipeline. Start with input quality since a scan resolution below 300 DPI degrades accuracy before the engine even runs. Layer in pre-processing to correct orientation, remove noise, and normalize resolution. Add LLM post-correction as a validation layer to catch the misrecognitions that slip through even well-tuned engines. And measure your accuracy against ground truth built from your actual documents, not vendor benchmark numbers from controlled test sets.

The solution you choose sets the ceiling. Open source engines like Tesseract top out around 88–94% on anything complex. Enterprise APIs from Google, Azure, and AWS get you to 96–98% on standard formats. For complex, variable, or high-stakes documents, agentic document parsing is where the accuracy gap closes. LlamaParse handles OCR as one component of a larger orchestration system, routing each document element to the right model, validating outputs through multiple correction loops, and surfacing confidence scores at the field level so you know exactly where to focus human review.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="techtoday-lenovo-com.md">
<details>
<summary>Top 5 uses of AI in medical imaging</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://techtoday.lenovo.com/sites/default/files/2025-05/Medical%20Imaging%20White%20Paper%20NVIDIA%20and%20Lenovo.pdf>

# Top 5 uses of AI in medical imaging

Uncover how imaging AI is empowering healthcare providers and improving patient outcomes

* * *

Artificial intelligence is rapidly emerging as a transformative technology in the healthcare industry, particularly in medical imaging. Through deep learning frameworks, improved medical imaging, AI development, and deployment, researchers are using computer vision to perform accurate, early detection, medical classification, and advanced 3D automated segmentation. When these models are taken to the clinical environment, they help clinicians streamline imaging workflows, uncover hidden insights, improve productivity, and connect multimodal patient information for deeper patient understanding.

With the integration of medical imaging and AI, the industry is seeing efficiencies once thought impossible. Workflows are now automated, clinicians have immediate clinical support toward diagnosis, and patient outcomes are improved. For instance, AI is removing tedious, manual processes so that what once took minutes to hours can now be accomplished within seconds. As a result, clinicians can focus more on interacting with patients and engaging in other value-add activities, such as research. Additionally, they’re able to improve the accuracy and efficiency of critical tasks and detect problems earlier to improve patient outcomes.

The convergence of AI and medical imaging also addresses key industry challenges that include a global shortage of radiologists, an aging population, and the growing demand for medical imaging. It’s projected that medical imaging analysis, the largest use case in healthcare, will reach $2.6 billion (23 percent CAGR) in 2027.1

It’s anticipated that by 2025, 40 percent of healthcare providers globally will have invested in AI-enabled imaging solutions2, as worldwide increasingly exploring the use of AI tools to manage heavy reporting workloads and a growing demand for precision medicine. For example, the Sydney Neuroimaging Analysis Centre (SNAC) is building a comprehensive neuroimaging AI platform with solutions embedded in radiology workflows to improve reporting efficiency and accuracy. These solutions will also facilitate the rapid, accurate quantification of brain disease progression by automating labor-intensive analysis tasks with AI.

From automating workflows to improving processing speed and image quality, there are numerous ways AI can help detect and diagnose disease. Here are the top 5 use cases.

* * *

Segmentation

Segmentation refers to the process of outlining and separating specific structures within an image, such as tumors, organs, blood vessels, or bones. The goal is to identify and isolate a specific region of interest within an image for further analysis or manipulation of that area.

From diagnosis to treatment planning and image-guided surgery, segmentation is a key step in many medical imaging applications. For example, in the diagnosis of cancer, it can be used to isolate and analyze a tumor within an image of the patient’s body to determine size, volume, shape, and location. When planning patient treatment, segmentation can identify and isolate specific structures, such as organs or blood vessels. It can also guide a surgeon during image-guided surgery.

There are several different techniques used for segmentation: manual, semiautomatic, and fully automatic. With manual segmentation, a clinician manually segments a particular area of interest, a time-consuming process subject to human error. In semiautomatic segmentation, a combination of human input and computer algorithms are utilized, which reduces the time and effort required from the clinician. However, with this method, interobserver variability is still present. Finally, there’s fully automatic segmentation that uses an algorithm and minimal clinician input.

AI-assisted segmentation automates the processes of outlining and separating specific structures. As a result, not only is the consistency of segmentation greatly improved, but there’s also a significant reduction in the time and effort required by the clinician. Deep learning is used in AI-assisted segmentation to understand features and patterns of specific structures, such as tumors or organs, and to segment new images by identifying and outlining the structures it’s been trained to recognize.

For instance, the State University of New York (SUNY) Upstate Medical University Department of Urology is developing AIpowered imaging tools to speed up cancer diagnosis and time to treatment. 3D volumetric segmentation algorithms are typically challenging to implement, requiring a great deal of customization and fine-tuning. However, SUNY is using MONAI to streamline the process and accelerate deep learning training with techniques like transfer learning for localization of the prostate in pelvic imaging. Through AI-enabled technologies, SUNY is using its prostate segmentation learnings to build new models for kidney stone identification and cancer detection.

* * *

**Detection** As with segmentation, detection is used in diagnosis, treatment planning, and image-guided surgery. The process of detection involves identifying and locating specific structures, patterns, or abnormalities within an image. This can include tumors, blood clots, or other pathological conditions, as well as identifying and locating normal structures such as blood vessels or organs. Like segmentation, the three techniques used for detection in medical imaging are manual, semiautomatic, and fully automatic. AI can improve patient outcomes and clinician efficiencies by automating the process of identifying and locating specific structures, patterns, or abnormalities. AI-enabled detection does this by learning the features and patterns that are characteristic of specific structures and then identifying and locating the structures it’s been trained to recognize in new images. Another technique used for AI-assisted detection is computer-aided detection (CAD) systems, which use algorithms to analyze medical images and detect abnormalities. This improves diagnostic accuracy and reduces the time clinicians spend on manually reviewing images, giving them more time to spend on patient care.

* * *

Classification

Classification uses computer algorithms to categorize or label specific structures, patterns, or abnormalities within an image. This can include categorizing or labeling tumors, blood clots, or other pathological conditions, as well as identifying normal physical structures.

An example of classification is categorizing a detected tumor as malignant or benign to determine the best course of treatment. In treatment planning and image-guided surgery, classification can also be used to identify and locate specific structures within an image to improve patient outcomes.

Methods used for classification include manual, semiautomatic, and fully automatic. In manual classification, a clinician puts in laborious hours through visual inspection of an image and categorizes or labels specific structures, patterns, or abnormalities. Semiautomatic classification uses a combination of clinician input and computer algorithms, and fully automatic classification relies primarily on algorithms.

In recent years, AI-assisted classification has been increasingly used to analyze medical images and classify abnormalities that can be difficult to interpret with the human eye. AI-enabled classification is having a big influence on hospital care by greatly reducing the time and effort required for clinicians. Diagnoses are made faster and more accurately so that clinicians can obtain results quicker, reduce patient time to treatment, and improve health outcomes.

A common classification use that AI is improving is the detection of breast cancer. Early detection through mammography is critical when it comes to reducing breast cancer deaths, but breast density can make it harder to detect the disease. The American College of Radiology (ACR), Diagnósticos da America (DASA), Ohio State University (OSU), Partners HealthCare (PHS), and Stanford University collaborated to improve an AI model for breast density classification using MONAI. Each institution obtained a better-performing model with superior predictive power on their local dataset. They were able to improve breast density classification from mammograms, which can lead to better breast cancer risk assessment.

* * *

Registration

By aligning and merging multiple images of the same body part taken from different modalities or at different times, clinicians can create a composite image that provides more information than individual images alone. For example, in cancer diagnosis, registration can be used to align and merge images from CT or MRI scans to create a composite image that provides more information about the size, shape, and location of a tumor. Additional use cases include tracking disease progression and guiding a surgeon during a procedure. As with the other use cases explored, registration techniques include manual, semiautomatic, and fully automatic, with tactics ranging from manual processes to utilizing computer algorithms with minimal input from clinicians.

Through AI-assisted registration, machine learning algorithms improve accuracy and consistency, as well as unburden clinicians from physically registering a multitude of images. This not only improves workflow efficiencies but also precision in diagnosis and treatment planning. Additionally, AI-assisted registration can be trained to recognize specific features and patterns, is capable of extracting image features like edges and corners, and can be used in optimization-based registration, which is helpful when images have different modalities or contrasts.

Reconstruction

Reconstruction in medical imaging is building images from the complex signals, such as those acquired by MR and CT machines. This process can be used to create detailed images of internal bodily structures that otherwise aren’t visible. For example, reconstruction can create detailed 3D depictions of a tumor that clinicians can use to determine size, shape, and location.

Reconstruction relies primarily on computer algorithms. AI can automate and accelerate the reconstruction process, while improving the quality of results.

MRI uses reconstruction techniques to transform raw data from the scanner into images that can be interpreted by clinicians. These reconstruction techniques are critical for obtaining accurate and detailed images for diagnostic and therapeutic purposes.

For instance, MRI is commonly used to diagnose conditions such as blocked or narrowed blood vessels, injuries to bones and ligaments, and neurological disorders like brain tumors and strokes.

AI-enabled technologies can improve MRI imaging by automating the process of creating detailed, accurate images, reducing noise and artifacts, and increasing the visibility of small structures not visible to the human eye. As a result, the accuracy and consistency of reconstruction are improved and the amount of radiation time a patient is exposed to is greatly reduced.

* * *

Yet, industry-wide challenges remain, including a lack of adoption readiness, the need to meet regulatory requirements, and scalability issues. Delivering AI solutions at scale — namely, creating, training, validating, deploying, monitoring, and using AI in medical imaging — requires an enterprise approach to meet the demands of today’s healthcare institutions.

Researchers and clinicians need a collaborative learning environment that enables research hospitals and institutions to exchange ideas and develop more robust AI algorithms without sharing private data. Foundational models are needed for quicker training. To accelerate the development and adoption of AI in clinical practice, radiologists must be involved in the creation of AI tools at their institutions. And AI components need to be integrated into a variety of clinical settings, including hospitals, imaging departments, private medical practices, skilled nursing facilities, clinics, and patients’ homes.

MONAI: Providing deep learning infrastructure and workflow optimization for medical imaging

MONAI is an open-source, collaborative framework designed to accelerate research and clinical collaboration in medical imaging. Its goal is to accelerate the pace of innovation and clinical translation by providing a robust software framework that benefits nearly every level of medical imaging, deep learning research, and deployment. MONAI offers specialized tools and libraries tailored to medical imaging, including advanced algorithms like UNETR for 3D segmentation. Built on top of PyTorch, MONAI offers a standardized and optimized approach to creating and evaluating deep learning models, ensuring reproducibility and capturing best practices in AI development for healthcare.

NVIDIA MONAI is a fully managed platform offering enterprises a range of capabilities, from infrastructure to pre-built state-of-the-art models and AI workflows. Part of the NVIDIA AI Enterprise suite, NVIDIA MONAI provides enhanced features and enterprise-grade support tailored for commercial applications.

Expanding the MONAI Ecosystem: MONAI Foundational Models

The landscape of medical AI is rapidly evolving with the emergence of Vision Language Models (VLMs) and Generative AI (GenAI). These cutting-edge technologies hold immense potential for transformative applications, including automated generation of radiology report and enhanced image interpretation. MONAI Foundational Models offer a streamlined pathway for deploying MONAI-trained models into clinical workflows. These models include VISTA-3D for interactive 3D segmentation, MAISI for synthetic CT data generation, VISTA-2D for cell segmentation and morphology analysis, and VILA-M3 for enhanced VLMs with expert AI models.

The Future of Medical AI: Multimodal

The MONAI framework extends beyond single modalities with MONAI Multimodal. This advancement integrates sophisticated agentic architectures, fostering a comprehensive multimodal medical AI ecosystem. By leveraging diverse data sources such as CT, MRI, X-ray, ultrasound, EHRs, clinical documentation, multimodal AI promises deeper clinical insights and more holistic patient understanding. MONAI Multimodal platform features advanced agentic AI, which leverages autonomous agents for multistep reasoning across images and text as well as specialized LLMs and VLMs, which are tailored models designed for medical applications that simplify cross-modal data integration. Furthermore, NVIDIA NIM microservices offer a streamlined pathway for deploying MONAItrained models into clinical workflows. These optimized containers simplify the inference process and streamline the development of medical AI applications.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="why-ocr-technology-fails-on-real-world-documents-blog.md">
<details>
<summary>Why OCR Fails on Real-World Documents - and How Intelligent Document Processing Can Help</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://netfira.com/why-ocr-technology-fails-on-real-world-documents-and-how-intelligent-document-processing-can-help/>

https://k8g6v2q5.delivery.rocketcdn.me/wp-content/uploads/2026/01/Why-OCR-Fails-web.webp

# Why OCR Fails on Real-World Documents - and How Intelligent Document Processing Can Help

- [February 18, 2026](https://netfira.com/2026/02/18/)

[Optical Character Recognition](https://netfira.com/what-is-optical-character-recognition/) (OCR) has been a foundational technology in document processing for decades. It converts images of text into machine-readable characters and, on the surface, appears to solve the core challenge of working with documents at scale. If text can be read automatically, surely the rest is straightforward.

In practice, OCR alone struggles in real-world business environments. While it performs well in controlled conditions, many organisations discover that OCR-based systems break down when faced with the variability, ambiguity and complexity of everyday transactional documents. This article aims to explain why Optical Character Recognition on a standalone basis can fail, and why an intelligent document processing solution (such as the Netfira Platform) can overcome these shortcomings.

## What OCR Is Designed to Do

OCR technology focuses on one specific task: recognising characters in an image. It analyses shapes and patterns to identify letters, numbers and symbols, then outputs those characters as text.

Modern OCR systems can be highly accurate when documents are clean and consistent. Typical ideal conditions include:

- high-resolution scans
- standard fonts and layouts
- minimal background noise
- clearly separated text
- single-language content

In these scenarios, OCR technologies are effective for digitisation and basic text capture. Many organisations still rely on OCR successfully for archiving, searchability and low-risk use cases.

However, these ideal conditions rarely reflect how documents arrive in real business workflows.

## The Reality of Business Documents

B2B documents come from many sources: suppliers, customers, logistics partners and legacy systems. Formats change over time. Quality varies. Documents may be scanned on different devices, annotated by hand or generated by outdated systems.

Common real-world challenges include:

- skewed or poorly scanned pages
- low contrast or faded text
- multiple columns and nested tables
- mixed languages or character sets
- logos, stamps and watermarks
- handwritten notes or signatures
- inconsistent spacing and alignment

OCR can still produce text under these conditions, but the output is often unreliable. Characters may be misread, merged or separated incorrectly, and important contextual information is lost.

## Character Accuracy Is Not Business Accuracy

One of the most common misconceptions about OCR technology is equating character accuracy with usable data. An OCR system might recognise most characters correctly while still failing to produce data that can be trusted in a business process.

For example, OCR may correctly read several numbers on a page, but it does not know which number represents an invoice total, which is a purchase order reference, or which belongs to a line item. From a business perspective, recognising text is only the first step. Understanding meaning is the real challenge.

This gap becomes critical when documents feed into downstream systems such as ERP platforms, finance tools or supply chain workflows. A single misinterpreted value can cause mismatches, incorrect postings or compliance issues.

This is why Optical Character Recognition alone is not sufficient for operational document automation.

## Layout Sensitivity and Template Dependence

Many OCR-based document processing solutions rely on templates or fixed coordinates to extract data. This assumes that key fields always appear in the same position on the page as is the case for structured documents.

While this can work in tightly controlled environments, it quickly becomes fragile in real-world scenarios. Semi-structured and unstructured documents such as invoices, shipping notices and purchase order confirmations are common in the business world. Small layout changes, such as an extra column, a shifted header or a resized logo, can cause extraction logic to fail.

Template maintenance then becomes a hidden operational cost. Each document change requires manual updates, testing and redeployment. As document volumes and supplier diversity increase, template-driven OCR systems struggle to scale.

## OCR Does Not Understand Relationships

Business documents are not just collections of text. They contain relationships between data elements. Line items belong to headers. Totals are derived from calculations. Quantities relate to units of measure.

Optical Character Recognition does not understand these relationships. It reads characters, not structure or intent. As a result, OCR output often requires extensive post-processing, complex rules or manual correction before it can be used reliably.

This limitation becomes especially apparent in documents such as invoices, shipping notices or order confirmations, where tabular and hierarchical data is common.

## The Confidence Score Problem

Some OCR systems attempt to address uncertainty by providing confidence scores. While useful at a character level, confidence scores do not solve the underlying issue of context.

A character can be recognised with high confidence and still be placed in the wrong field. From a business perspective, this is still an error. Confidence scores can also create false reassurance, encouraging teams to trust outputs that are structurally incorrect.

In practice, organisations often respond by increasing manual review, which undermines the efficiency gains automation was meant to deliver.

## Why OCR-Only Approaches Do Not Scale

As document volumes grow, the limitations of OCR-only systems become more pronounced. Manual correction effort increases. Template maintenance expands. Exception rates remain high.

Rather than removing work, OCR-only automation often shifts work. Humans spend less time reading documents and more time reviewing and fixing OCR output. These hidden costs are not always visible during pilot projects but become clear at scale.

Scalability is not just about processing speed. It is about stability and maintainability as documents, suppliers and requirements change.

## How Intelligent Document Processing Goes Beyond OCR

[Intelligent Document Processing](https://netfira.com/what-is-intelligent-document-processing/), such as Netfira’s software solution, builds on OCR rather than replacing it entirely. OCR remains a useful component for converting images into text, but IDP adds additional layers that address OCR’s structural and contextual limitations.

These layers typically include:

- document classification
- layout and structure analysis
- contextual data extraction
- validation and business rules
- exception handling workflows
- targeted human oversight

This broader approach is explained in Netfira’s overview of intelligent document processing, which positions OCR technology as one part of a wider automation workflow rather than the foundation of the system.

## Handling Variability Instead of Avoiding It

A key difference between OCR-only systems and IDP platforms is how they deal with variability. OCR performs best when variability is minimised. IDP is designed to cope with variability.

Instead of rigid templates, IDP platforms analyse structure and patterns. Instead of blind extraction, they apply validation logic. Instead of failing silently, they surface exceptions clearly and route them appropriately.

Modern approaches to [AI document processing](https://netfira.com/ai-document-processing/) focus on using AI to understand documents during onboarding and to react to changes such as a new document layout or an edge case, while keeping runtime processing stable and predictable.

## The Role of Human Oversight

Even with intelligent document processing, human involvement remains important. The difference lies in how humans are involved.

Rather than reviewing every document, human effort is focused on:

- confirming mappings during setup
- reviewing genuine exceptions
- adjusting rules and tolerances
- approving changes when formats evolve

This approach aligns with [human-in-the-loop automation](https://netfira.com/human-in-the-loop-automation), where oversight is deliberate and targeted, not continuous. It allows automation to improve over time without becoming opaque or uncontrollable.

## When OCR Still Makes Sense

OCR technology still has a place. For simple digitisation, archival use cases or low-risk scenarios, OCR may be sufficient.The problem arises when OCR is treated as a complete document automation solution rather than a component. In operational workflows where accuracy, traceability and scale matter, OCR alone is rarely enough.

## The Limits of OCR Technology and the Potential of IDP Solutions

OCR is effective at recognising characters, but real-world document processing requires more than character recognition. Business documents are complex, variable and context-dependent. OCR alone cannot reliably interpret meaning, structure or business relevance.

Intelligent Document Processing addresses these challenges by combining OCR technology with document understanding, validation logic and controlled human oversight. This allows organisations to move beyond digitisation towards automation that scales.

For teams handling high volumes of operational documents, understanding why OCR systems fail is the first step towards building document workflows that are resilient, accurate and fit for real-world complexity.

</details>

</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

<details>
<summary>Repository analysis for https://github.com/towardsai/course-ai-agents/blob/dev/lessons/11_multimodal/notebook.ipynb</summary>

# Repository analysis for https://github.com/towardsai/course-ai-agents/blob/dev/lessons/11_multimodal/notebook.ipynb

## Summary
Repository: towardsai/course-ai-agents
Branch: dev
File: notebook.ipynb
Lines: 1,402

Estimated tokens: 11.4k

## File tree
```Directory structure:
└── notebook.ipynb

```

## Extracted content
================================================
FILE: lessons/11_multimodal/notebook.ipynb
================================================
# Jupyter notebook converted to Python script.

"""
# Lesson 11: Multimodal

This notebook demonstrates how to build multimodal AI systems that can process and understand multimodal data such text, images and documents using Google's Gemini models.

We will use the `google-genai` library to interact with Google's Gemini models.

**Learning Objectives:**

1. **Process multimodal content**: Learn to handle images and PDFs in different formats (bytes, base64, URLs) with Gemini models
2. **Implement object detection**: Use multimodal LLMs for visual analysis and structured output generation
3. **Build multimodal RAG systems**: Create and index embeddings for images, documents and text to enable semantic search across multimodal content
4. **Develop multimodal AI agents**: Construct ReAct agents that can search through and reason about multimodal information
"""

"""
## 1. Setup

First, we define some standard Magic Python commands to autoreload Python packages whenever they change:
"""

%load_ext autoreload
%autoreload 2

"""
### Set Up Python Environment

To set up your Python virtual environment using `uv` and load it into the Notebook, follow the step-by-step instructions from the `Course Admin` lesson from the beginning of the course.

**TL/DR:** Be sure the correct kernel pointing to your `uv` virtual environment is selected.
"""

"""
### Configure Gemini API

To configure the Gemini API, follow the step-by-step instructions from the `Course Admin` lesson.

But here is a quick check on what you need to run this Notebook:

1.  Get your key from [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  From the root of your project, run: `cp .env.example .env` 
3.  Within the `.env` file, fill in the `GOOGLE_API_KEY` variable:

Now, the code below will load the key from the `.env` file:
"""

from lessons.utils import env

env.load(required_env_vars=["GOOGLE_API_KEY"])
# Output:
#   Trying to load environment variables from `/Users/pauliusztin/Documents/01_projects/TAI/course-ai-agents/.env`

#   Environment variables loaded successfully.


"""
### Import Key Packages
"""

import base64
import io
from pathlib import Path
from typing import Literal

from google import genai
from google.genai import types
from IPython.display import Image as IPythonImage
from PIL import Image as PILImage

from lessons.utils import pretty_print

"""
### Initialize the Gemini Client
"""

client = genai.Client()

"""
### Define Constants

We will use the `gemini-2.5-flash` model, which is fast and cost-effective:
"""

MODEL_ID = "gemini-2.5-flash"

"""
## 2. Applying multimodal LLMs to images and PDFs

There are three core ways we can process images and PDFs with multimodal LLMs:
1. As raw bytes
2. As base64 encoded strings
3. As URLs

We will first look into how we can process images and then PDFs.

Now, let's look at our test image:

"""

def display_image(image_path: Path) -> None:
    """
    Display an image from a file path in the notebook.

    Args:
        image_path: Path to the image file to display

    Returns:
        None
    """

    image = IPythonImage(filename=image_path, width=400)
    display(image)


display_image(Path("images") / "image_1.jpeg")
# Output:
#   <IPython.core.display.Image object>

"""
### 2.1 As raw bytes
"""

def load_image_as_bytes(
    image_path: Path, format: Literal["WEBP", "JPEG", "PNG"] = "WEBP", max_width: int = 600, return_size: bool = False
) -> bytes | tuple[bytes, tuple[int, int]]:
    """
    Load an image from file path and convert it to bytes with optional resizing.

    Args:
        image_path: Path to the image file to load
        format: Output image format (WEBP, JPEG, or PNG). Defaults to "WEBP"
        max_width: Maximum width for resizing. If image width exceeds this, it will be resized proportionally. Defaults to 600
        return_size: If True, returns both bytes and image size tuple. Defaults to False

    Returns:
        bytes: Image data as bytes, or tuple of (bytes, (width, height)) if return_size is True
    """

    image = PILImage.open(image_path)
    if image.width > max_width:
        ratio = max_width / image.width
        new_size = (max_width, int(image.height * ratio))
        image = image.resize(new_size)

    byte_stream = io.BytesIO()
    image.save(byte_stream, format=format)

    if return_size:
        return byte_stream.getvalue(), image.size

    return byte_stream.getvalue()

"""
Load image:
"""

image_bytes = load_image_as_bytes(image_path=Path("images") / "image_1.jpeg", format="WEBP")
pretty_print.wrapped([f"Bytes `{image_bytes[:30]}...`", f"Size: {len(image_bytes)} bytes"], title="Image as Bytes")
# Output:
#   [93m------------------------------------------ Image as Bytes ------------------------------------------[0m

#     Bytes `b'RIFF`\xad\x00\x00WEBPVP8 T\xad\x00\x00P\xec\x02\x9d\x01*X\x02X\x02'...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#     Size: 44392 bytes

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Compute captions:
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/webp",
        ),
        "Tell me what is in this image in one paragraph.",
    ],
)
pretty_print.wrapped(response.text, title="Image 1 Caption")

# Output:
#   [93m----------------------------------------- Image 1 Caption -----------------------------------------[0m

#     This striking image features a massive, dark metallic robot, its powerful form detailed with intricate circuit patterns on its head and piercing red glowing eyes. Perched playfully on its right arm is a small, fluffy grey tabby kitten, its front paw raised as if exploring or batting at the robot's armored limb, while its gaze is directed slightly off-frame. The robot's large, segmented hand is visible beneath the kitten. The background suggests an industrial or workshop environment, with hints of metal structures and natural light filtering in from an unseen window, creating a dramatic contrast between the soft, vulnerable kitten and the formidable, mechanical sentinel.

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Using the same approach, we can easily pass multiple images simultaneously. For example, the previous one plus the one below, and compare them:
"""

display_image(Path("images") / "image_2.jpeg")
# Output:
#   <IPython.core.display.Image object>

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(
            data=load_image_as_bytes(image_path=Path("images") / "image_1.jpeg", format="WEBP"),
            mime_type="image/webp",
        ),
        types.Part.from_bytes(
            data=load_image_as_bytes(image_path=Path("images") / "image_2.jpeg", format="WEBP"),
            mime_type="image/webp",
        ),
        "What's the difference between these two images? Describe it in one paragraph.",
    ],
)
pretty_print.wrapped(response.text, title="Differences between images")

# Output:
#   [93m------------------------------------ Differences between images ------------------------------------[0m

#     The primary difference between the two images lies in the nature of the interaction depicted and their respective settings. In the first image, a small, grey kitten is shown curiously interacting with a large, metallic robot, gently perched on its arm within what appears to be a clean, well-lit workshop or industrial space. Conversely, the second image portrays a tense and aggressive confrontation between a fluffy white dog and a sleek black robot, both in combative stances, amidst a cluttered and grimy urban alleyway filled with trash and graffiti.

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
### 2.2 As base64 encoded strings

Now, let's load the same image as base64:
"""

from typing import cast


def load_image_as_base64(
    image_path: Path, format: Literal["WEBP", "JPEG", "PNG"] = "WEBP", max_width: int = 600, return_size: bool = False
) -> str:
    """
    Load an image and convert it to base64 encoded string.

    Args:
        image_path: Path to the image file to load
        format: Output image format (WEBP, JPEG, or PNG). Defaults to "WEBP"
        max_width: Maximum width for resizing. If image width exceeds this, it will be resized proportionally. Defaults to 600
        return_size: Parameter passed to load_image_as_bytes function. Defaults to False

    Returns:
        str: Base64 encoded string representation of the image
    """

    image_bytes = load_image_as_bytes(image_path=image_path, format=format, max_width=max_width, return_size=False)

    return base64.b64encode(cast(bytes, image_bytes)).decode("utf-8")

image_base64 = load_image_as_base64(image_path=Path("images") / "image_1.jpeg", format="WEBP")
pretty_print.wrapped(
    [f"Base64: {image_base64[:100]}...`", f"Size: {len(image_base64)} characters"], title="Image as Base64"
)
# Output:
#   [93m----------------------------------------- Image as Base64 -----------------------------------------[0m

#     Base64: UklGRmCtAABXRUJQVlA4IFStAABQ7AKdASpYAlgCPm0ylEekIqInJnQ7gOANiWdtk7FnEo2gDknjPixW9SNSb5P7IbBNhLn87Vtp...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#     Size: 59192 characters

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
On average base64 format is 33% larger than raw bytes. As we can see in this use case as well:
"""

print(f"Image as Base64 is {(len(image_base64) - len(image_bytes)) / len(image_bytes) * 100:.2f}% larger than as bytes")
# Output:
#   Image as Base64 is 33.34% larger than as bytes


"""
Now, let's recompute the image caption using this method:
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(data=image_base64, mime_type="image/webp"),
        "Tell me what is in this image in one paragraph.",
    ],
)
response.text
# Output:
#   "The image features a striking contrast between a large, formidable robot and a small, adorable kitten. The robot, crafted from dark, sleek metallic armor with intricate circuitry patterns on its head, possesses piercing red glowing eyes that appear to be focused on its tiny companion. A fluffy, gray tabby kitten is playfully perched on the robot's massive metallic arm and shoulder, its small paws resting gently on the armored surface as it looks up with curiosity. The scene is set in what looks like an industrial or workshop environment, with warm light filtering in from the background, highlighting this unexpected and endearing interaction between advanced technology and natural innocence."

"""
### 2.3 As public URLs

Using Gemini `url_context` out-of-the-box tool, we can automatically visit and parse webpages, PDFs, and images from the open internet. You only have to provide the direct URL in the prompt and configure the `url_context` tool. This makes it a no-brainer to parse multiple data formats when available online:
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents="Based on the provided paper as a PDF, tell me how ReAct works: https://arxiv.org/pdf/2210.03629",
    config=types.GenerateContentConfig(tools=[{"url_context": {}}]),
)
pretty_print.wrapped(response.text, title="How ReAct works")
# Output:
#   [93m----------------------------------------- How ReAct works -----------------------------------------[0m

#     

#   

#   ReAct is a novel paradigm for large language models (LLMs) that combines reasoning (Thought) and acting (Action) in an interleaved manner to solve diverse language and decision-making tasks. This approach allows the model to:

#   

#   *   **Reason to Act:** Generate verbal reasoning traces to induce, track, and update action plans, and handle exceptions.

#   *   **Act to Reason:** Interface with and gather additional information from external sources (like knowledge bases or environments) to incorporate into its reasoning.

#   

#   **How it works:**

#   

#   Instead of just generating a direct answer (Standard prompting) or a chain of thought without external interaction (CoT), or only actions (Act-only), ReAct augments the LLM's action space to include a "language space" for generating "thoughts" or reasoning traces.

#   

#   1.  **Thought:** The model explicitly generates a thought, which is a verbal reasoning trace. This thought helps the model to:

#       *   Decompose task goals and create action plans.

#       *   Inject commonsense knowledge.

#       *   Extract important information from observations.

#       *   Track progress and adjust action plans.

#       *   Handle exceptions.

#   2.  **Action:** Based on the current thought and context, the model performs a task-specific action. This could involve:

#       *   Searching external databases (e.g., Wikipedia API using `search[entity]` or `lookup[string]`).

#       *   Interacting with an environment (e.g., `go to cabinet 1`, `take pepper shaker 1`).

#       *   Finishing the task with an answer (`finish[answer]`).

#   3.  **Observation:** The environment provides an observation feedback based on the executed action.

#   

#   This cycle of Thought, Action, and Observation continues until the task is completed.

#   

#   **Benefits of ReAct:**

#   

#   *   **Improved Performance:** ReAct consistently outperforms baselines that only perform reasoning or acting in isolation on tasks like question answering (HotpotQA), fact verification (FEVER), text-based games (ALFWorld), and webpage navigation (WebShop).

#   *   **Reduced Hallucination and Error Propagation:** By interacting with external sources, ReAct can overcome issues of hallucination and error propagation common in chain-of-thought reasoning that relies solely on internal knowledge.

#   *   **Human Interpretability and Trustworthiness:** The interleaved reasoning traces make the model's decision-making process more interpretable and trustworthy, as humans can inspect the thoughts and actions.

#   *   **Flexibility and Generalizability:** ReAct is flexible enough to be applied to diverse tasks with different action spaces and reasoning needs, and it shows strong generalization with only a few in-context examples.

#   *   **Human Alignment and Controllability:** Humans can control or correct the agent's behavior by editing its thoughts, enabling new forms of human-machine collaboration.

#   

#   For example, in a question-answering task, ReAct might first *think* about what to search, then *act* by searching Wikipedia, *observe* the results, *think* about what the results mean and what to search next, and so on, until it can *think* of the final answer and *act* to finish the task.

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
### 2.4 As URLs from private data lakes

At the time of writing this notebook, Gemini works well primarily with GCP Cloud Storage links and not with other buckets such as S3. Buckets are excellent for production use cases, but they complicate our simple demonstration. Therefore, we will show you a mocked example.

The code would look like this, where you have to change the `uri` and ensure the LLM has the right permissions to your GCS bucket:
```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_uri(uri="gs://gemini-images/image_1.jpeg", mime_type="image/webp"),
        "Tell me what is in this image in one paragraph.",
    ],
)
```
"""

"""
### 2.5 Object detection with LLMs

As a more exciting example, let's do object detection with multimodal LLMs.

First, let's define the output Pydantic models:
"""

from pydantic import BaseModel, Field


class BoundingBox(BaseModel):
    ymin: float
    xmin: float
    ymax: float
    xmax: float
    label: str = Field(
        default="The category of the object found within the bounding box. For example: cat, dog, diagram, robot."
    )


class Detections(BaseModel):
    bounding_boxes: list[BoundingBox]

"""
Then the prompt and image:
"""

prompt = """
Detect all of the prominent items in the image. 
The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000.
Also, output the label of the object found within the bounding box.
"""

image_bytes, image_size = load_image_as_bytes(
    image_path=Path("images") / "image_1.jpeg", format="WEBP", return_size=True
)

"""
Now, let's call the LLM:
"""

config = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=Detections,
)

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/webp",
        ),
        prompt,
    ],
    config=config,
)

detections = cast(Detections, response.parsed)
pretty_print.wrapped([f"Image size: {image_size}", *detections.bounding_boxes], title="Detections")
# Output:
#   [93m-------------------------------------------- Detections --------------------------------------------[0m

#     Image size: (600, 600)

#   [93m----------------------------------------------------------------------------------------------------[0m

#     ymin=1.0 xmin=450.0 ymax=997.0 xmax=1000.0 label='robot'

#   [93m----------------------------------------------------------------------------------------------------[0m

#     ymin=269.0 xmin=39.0 ymax=782.0 xmax=530.0 label='kitten'

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Let's also visualize the bounding boxes: 
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def visualize_detections(detections: Detections, image_path: Path) -> None:
    """
    Visualize detected bounding boxes on an image with red rectangles and labels.

    Args:
        detections: Detections object containing bounding boxes in [ymin, xmin, ymax, xmax] format normalized to 0-1000
        image_path: Path to the image file to visualize

    Returns:
        None: Displays the image with bounding boxes in the notebook
    """

    # Clear any existing plots to prevent overlapping
    plt.clf()

    image = PILImage.open(image_path)
    image_array = np.array(image)
    img_height, img_width = image_array.shape[:2]

    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    ax.imshow(image_array)

    for bbox in detections.bounding_boxes:
        # Convert normalized coordinates (0-1000) to pixel coordinates
        xmin = (bbox.xmin / 1000) * img_width
        ymin = (bbox.ymin / 1000) * img_height
        xmax = (bbox.xmax / 1000) * img_width
        ymax = (bbox.ymax / 1000) * img_height

        # Calculate box dimensions (matplotlib uses bottom-left corner + width/height)
        width = xmax - xmin
        height = ymax - ymin

        # Create rectangle patch (x, y is bottom-left corner)
        rect = patches.Rectangle((xmin, ymin), width, height, linewidth=3, edgecolor="red", facecolor="none")

        # Add rectangle to the plot
        ax.add_patch(rect)

        # Add label text (positioned at top-left of bounding box)
        ax.text(
            xmin,
            ymin + 5,  # Slightly above the box
            bbox.label[:15],
            fontsize=12,
            color="red",
            fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
        )

    # Remove axis ticks and labels for cleaner display
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(f"Object Detection Results: {image_path.name}", fontsize=14, fontweight="bold")

    plt.tight_layout()
    plt.show()

visualize_detections(detections, Path("images") / "image_1.jpeg")
# Output:
#   <Figure size 640x480 with 0 Axes>
#   <Figure size 800x600 with 1 Axes>

"""
### 2.6 Working with PDFs

Ultimately, let's see how we can work with PDFs. We will use the legendary `Attention Is All You Need` Paper as an example. 

To display it, we extracted the first 3 pages of the PDF as images. For example, this is how the page looks:

"""

display_image(Path("images") / "attention_is_all_you_need_0.jpeg")
# Output:
#   <IPython.core.display.Image object>

"""
We can treat PDFs similarly to images. Therefore, we can pass PDFs as bytes:
"""

pdf_bytes = (Path("pdfs") / "attention_is_all_you_need_paper.pdf").read_bytes()
pretty_print.wrapped(f"Bytes: {pdf_bytes[:40]}...", title="PDF bytes")
# Output:
#   [93m-------------------------------------------- PDF bytes --------------------------------------------[0m

#     Bytes: b'%PDF-1.7\n%\xe2\xe3\xcf\xd3\n24 0 obj\n<<\n/Filter /Flat'...

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Call the LLM:
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf"),
        "What is this document about? Provide a brief summary of the main topics.",
    ],
)
pretty_print.wrapped(response.text, title="PDF Summary (as bytes)")
# Output:
#   [93m-------------------------------------- PDF Summary (as bytes) --------------------------------------[0m

#     This document introduces the **Transformer**, a novel neural network architecture designed for **sequence transduction tasks** (like machine translation).

#   

#   Its main topics include:

#   

#   1.  **Dispensing with Recurrence and Convolutions**: Unlike previous dominant models (RNNs and CNNs), the Transformer relies *solely* on **attention mechanisms**, eliminating the need for sequential computation.

#   2.  **Attention Mechanisms**: It details the **Scaled Dot-Product Attention** and **Multi-Head Attention** as its core building blocks, explaining how they allow the model to weigh different parts of the input sequence.

#   3.  **Parallelization and Efficiency**: The paper highlights that the Transformer's architecture allows for significantly more parallelization during training, leading to **faster training times** compared to prior models.

#   4.  **Superior Performance**: It demonstrates that the Transformer achieves **state-of-the-art results** on machine translation tasks (English-to-German and English-to-French) and generalizes well to other tasks like English constituency parsing.

#   5.  **Positional Encoding**: Since the model lacks recurrence or convolution, it introduces positional encodings to inject information about the relative or absolute position of tokens in the sequence.

#   

#   In essence, the document proposes and validates that **attention alone is sufficient** for building high-quality, efficient, and parallelizable sequence transduction models.

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Alternatively, as base64 encoded strings:
"""

def load_pdf_as_base64(pdf_path: Path) -> str:
    """
    Load a PDF file and convert it to base64 encoded string.

    Args:
        pdf_path: Path to the PDF file to load

    Returns:
        str: Base64 encoded string representation of the PDF
    """

    with open(pdf_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

"""
Load the PDF:
"""

pdf_base64 = load_pdf_as_base64(pdf_path=Path("pdfs") / "attention_is_all_you_need_paper.pdf")
pretty_print.wrapped(f"Base64: {pdf_base64[:40]}...", title="PDF as Base64")
# Output:
#   [93m------------------------------------------ PDF as Base64 ------------------------------------------[0m

#     Base64: JVBERi0xLjcKJeLjz9MKMjQgMCBvYmoKPDwKL0Zp...

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Call the LLM:
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        "What is this document about? Provide a brief summary of the main topics.",
        types.Part.from_bytes(data=pdf_base64, mime_type="application/pdf"),
    ],
)

pretty_print.wrapped(response.text, title="PDF Summary (as base64)")
# Output:
#   [93m------------------------------------- PDF Summary (as base64) -------------------------------------[0m

#     This document introduces the **Transformer**, a novel neural network architecture for **sequence transduction models**, primarily applied to **machine translation**.

#   

#   Here's a brief summary of the main topics:

#   

#   *   **Core Innovation:** The Transformer proposes to completely abandon recurrent neural networks (RNNs) and convolutional neural networks (CNNs), relying *solely on attention mechanisms* (specifically "multi-head self-attention") for learning dependencies between input and output sequences.

#   *   **Problem Addressed:** Traditional RNNs/CNNs suffer from inherent sequential computation, which limits parallelization and makes it difficult to efficiently learn long-range dependencies. The Transformer addresses this by allowing constant-time operations for relating any two positions in a sequence.

#   *   **Architecture:** It maintains an encoder-decoder structure, where both the encoder and decoder are composed of stacks of self-attention and point-wise fully connected layers. Positional encodings are added to input embeddings to inject information about the order of the sequence.

#   *   **Key Advantages:** The Transformer is significantly more parallelizable and requires substantially less training time compared to previous state-of-the-art models.

#   *   **Performance:** It achieves new state-of-the-art results on major machine translation benchmarks (WMT 2014 English-to-German and English-to-French) and demonstrates strong generalization to other tasks, such as English constituency parsing.

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Now, let's do a more interesting example and detect the diagrams from a page of the transformers paper, such as the one below:
"""

display_image(Path("images") / "attention_is_all_you_need_1.jpeg")
# Output:
#   <IPython.core.display.Image object>

"""
Define the object detection prompt to detect diagrams (similar to how we did for images):
"""

prompt = """
Detect all the diagrams from the provided image as 2d bounding boxes. 
The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000.
Also, output the label of the object found within the bounding box.
"""

image_bytes, image_size = load_image_as_bytes(
    image_path=Path("images") / "attention_is_all_you_need_1.jpeg", format="WEBP", return_size=True
)

"""
Call the LLM:
"""

config = types.GenerateContentConfig(
    response_mime_type="application/json",
    response_schema=Detections,
)
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/webp",
        ),
        prompt,
    ],
    config=config,
)
detections = cast(Detections, response.parsed)
pretty_print.wrapped([f"Image size: {image_size}", *detections.bounding_boxes], title="Detections")
# Output:
#   [93m-------------------------------------------- Detections --------------------------------------------[0m

#     Image size: (600, 776)

#   [93m----------------------------------------------------------------------------------------------------[0m

#     ymin=88.0 xmin=309.0 ymax=515.0 xmax=681.0 label='diagram'

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
Visualize the detections:
"""

visualize_detections(detections, Path("images") / "attention_is_all_you_need_1.jpeg")
# Output:
#   <Figure size 640x480 with 0 Axes>
#   <Figure size 800x600 with 1 Axes>

"""
## 3. Implementing multimodal RAG for images, PDFs and text

To bring everything we did in this course together, let's implement a multimodal RAG system that works with text, images, and PDFs.

These are the images and PDF pages (as images) we will index for semantic search:
"""

def display_image_grid(image_paths: list[Path], rows: int = 2, cols: int = 2, figsize: tuple = (8, 6)) -> None:
    """
    Display a grid of images.

    Args:
        image_paths: List of paths to images to display
        rows: Number of rows in the grid
        cols: Number of columns in the grid
        figsize: Figure size as (width, height)
    """

    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    axes = axes.ravel()

    for idx, img_path in enumerate(image_paths[: rows * cols]):
        img = PILImage.open(img_path)
        axes[idx].imshow(img)
        axes[idx].axis("off")

    plt.tight_layout()
    plt.show()


display_image_grid(
    image_paths=[
        Path("images") / "image_1.jpeg",
        Path("images") / "image_2.jpeg",
        Path("images") / "image_3.jpeg",
        Path("images") / "image_4.jpeg",
        Path("images") / "attention_is_all_you_need_1.jpeg",
        Path("images") / "attention_is_all_you_need_2.jpeg",
    ],
    rows=2,
    cols=3,
)
# Output:
#   <Figure size 800x600 with 6 Axes>

"""
Now, let's define the core functions.

First, one that creates image descriptions:
"""

from io import BytesIO
from typing import Any

import numpy as np


def generate_image_description(image_bytes: bytes) -> str:
    """
    Generate a detailed description of an image using Gemini Vision model.

    Args:
        image_bytes: Image data as bytes

    Returns:
        str: Generated description of the image
    """

    try:
        # Convert bytes back to PIL Image for vision model
        img = PILImage.open(BytesIO(image_bytes))

        # Use Gemini Vision model to describe the image
        prompt = """
        Describe this image in detail for semantic search purposes. 
        Include objects, scenery, colors, composition, text, and any other visual elements that would help someone find 
        this image through text queries.
        """

        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[prompt, img],
        )

        if response and response.text:
            description = response.text.strip()

            return description
        else:
            print("❌ No description generated from vision model")

            return ""

    except Exception as e:
        print(f"❌ Failed to generate image description: {e}")

        return ""


"""
Another one that creates embedding using `gemini_embedding-001`, based on the given input:
"""

def embed_text_with_gemini(content: str) -> np.ndarray | None:
    """
    Embed text content using Gemini's text embedding model.

    Args:
        content: Text string to embed

    Returns:
        np.ndarray | None: Embedding vector as numpy array or None if failed
    """

    try:
        result = client.models.embed_content(
            model="gemini-embedding-001",  # Gemini's text embedding model
            contents=[content],
        )
        if not result or not result.embeddings:
            print("❌ No embedding data found in response")
            return None

        return np.array(result.embeddings[0].values)

    except Exception as e:
        print(f"❌ Failed to embed text: {e}")
        return None

"""
Let's see how this works:
"""

embedding = embed_text_with_gemini("This is a test")
embedding
# Output:
#   array([-0.02252334, -0.00076438,  0.00240217, ..., -0.00574729,

#          -0.00052345, -0.00213343], shape=(3072,))

"""
As we can see below, it creates a 3072 embedding from the input text:
"""

embedding.shape
# Output:
#   (3072,)

"""
Let's glue these functions and create the vector index out of our test images and PDF pages:
"""

from typing import cast


def create_vector_index(image_paths: list[Path]) -> list[dict]:
    """
    Create embeddings for images by generating descriptions and embedding them.

    This function processes a list of image paths by:
    1. Loading each image as bytes
    2. Generating a text description using Gemini Vision
    3. Creating an embedding of that description using Gemini Embeddings

    Args:
        image_paths (list[Path]): List of paths to image files to process

    Returns:
        list[dict]: List of dictionaries with the following keys:
            - content (bytes): Raw image bytes
            - type (str): Always "image"
            - filename (Path): Original image path
            - description (str): Generated image description
            - embedding (np.ndarray): Vector embedding of the description
    """

    vector_index = []
    for image_path in image_paths:
        image_bytes = cast(bytes, load_image_as_bytes(image_path, format="WEBP", return_size=False))

        image_description = generate_image_description(image_bytes)
        pretty_print.wrapped(f"`{image_description[:500]}...`", title="Generated image description:")

        # IMPORTANT NOTE: When working with multimodal embedding models, we can directly embed the
        # `image_bytes` instead of generating and embedding the description. Otherwise, everything
        # else remains the same within the whole RAG system.
        image_embedding = embed_text_with_gemini(image_description)

        vector_index.append(
            {
                "content": image_bytes,
                "type": "image",
                "filename": image_path,
                "description": image_description,
                "embedding": image_embedding,
            }
        )

    return vector_index

"""
We call the `create_vector_index` function on all the images from the `images` dir:
"""

image_paths = list(Path("images").glob("*.jpeg"))
vector_index = create_vector_index(image_paths)
# Output:
#   [93m----------------------------------- Generated image description: -----------------------------------[0m

#     `This image is a page from a technical or scientific document, likely a research paper, textbook, or dissertation related to machine learning, deep learning, or artificial intelligence.

#   

#   **Overall Composition & Scenery:**

#   The image is a vertically oriented page (A4 or similar size) with a clean, academic layout. The dominant colors are black text on a white background. The page is filled with text and features two prominent block diagrams at the top, along with a mathematical equation in the lowe...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m----------------------------------- Generated image description: -----------------------------------[0m

#     `This image is a detailed, photorealistic digital rendering or illustration depicting an unlikely interaction between a large, imposing robot and a small, delicate kitten in an industrial setting.

#   

#   **Objects:**

#   *   **Robot:** The dominant figure is a large, humanoid robot, occupying the right side of the frame. Its body is constructed from dark, metallic armored plates in shades of charcoal, gunmetal, and dark grey, with visible bolts, rivets, and segmented joints suggesting a heavy, industrial d...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m----------------------------------- Generated image description: -----------------------------------[0m

#     `This image depicts a dramatic and tense confrontation between a large, fluffy white dog and a sleek, dark humanoid robot in a desolate urban alleyway.

#   

#   **Objects and Characters:**

#   

#   *   **White Dog:** Positioned on the left, a large, fluffy white dog, strongly resembling a Samoyed or other Spitz breed (like a white husky or malamute), is captured mid-lunge. Its mouth is wide open, baring sharp teeth, indicative of barking, snarling, or attacking. Its ears are forward, and its tail is high and cur...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m----------------------------------- Generated image description: -----------------------------------[0m

#     `This image is a detailed, close-up shot of an African American man intently working on the internal components of an open desktop computer tower.

#   

#   **Objects:**

#   *   **Person:** An adult African American male with a neatly trimmed beard (streaked with some grey) and black-rimmed glasses is positioned on the left side, looking down with a focused expression into the computer case. His dark-skinned hands are prominent, one holding a screwdriver and the other steadying a component or pointing. He wea...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m----------------------------------- Generated image description: -----------------------------------[0m

#     `This image is a detailed technical document, likely from a research paper or academic publication, featuring a prominent diagram of the Transformer model architecture alongside explanatory text.

#   

#   **Overall Composition & Scenery:**

#   The image is set against a clean white background. The top half is dominated by a multi-colored block diagram, while the bottom half contains black text organized into sections and paragraphs. A page number "3" is centered at the very bottom.

#   

#   **Objects & Diagram Eleme...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m----------------------------------- Generated image description: -----------------------------------[0m

#     `This image depicts a dynamic, high-energy futuristic battle scene between two humanoid robots or mechs.

#   

#   **Objects:**

#   *   **Two Robots/Mechs:**

#       *   **Left Robot:** Appears sleek and agile, made of highly reflective, polished silver or chrome metal. Its head, chest, and arms feature prominent electric blue glowing lines and accents, including a bright blue visor or eye piece. It is in the process of delivering a powerful punch with its right fist into the other robot. Its posture suggests for...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   [93m----------------------------------- Generated image description: -----------------------------------[0m

#     `This image is a digital scan or representation of the first page of a widely recognized academic research paper. The dominant visual element is text, set against a plain white background, simulating a printed document.

#   

#   **Overall Composition & Layout:**

#   The page is organized in a standard academic paper format with a title, author list, abstract, and footnotes. Text is primarily black, with a small section of red text at the very top. A vertical, faint grey text string (likely a watermark or ide...`

#   [93m----------------------------------------------------------------------------------------------------[0m


if len(vector_index) == 0:
    pretty_print.wrapped("Could not create the vector index.", title="❌")
else:
    pretty_print.wrapped(f"Successfully created {len(vector_index)} embeddings under the `vector_index` variable", title="✅")
# Output:
#   [93m------------------------------------------------ ✅ ------------------------------------------------[0m

#     Successfully created 7 embeddings under the `vector_index` variable

#   [93m----------------------------------------------------------------------------------------------------[0m


"""
This is how an element from the `vector_index` looks like:
"""

vector_index[0].keys()
# Output:
#   dict_keys(['content', 'type', 'filename', 'description', 'embedding'])

vector_index[0]["embedding"].shape
# Output:
#   (3072,)

print(f"{vector_index[0]['description'][:150]}...")
# Output:
#   This image is a page from a technical or scientific document, likely a research paper, textbook, or dissertation related to machine learning, deep lea...


"""
Now let's define a function that finds `top_k` most similar items from the vector_index based on a user query:
"""

from sklearn.metrics.pairwise import cosine_similarity


def search_multimodal(query_text: str, vector_index: list[dict], top_k: int = 3) -> list[Any]:
    """
    Search for most similar documents to query using direct Gemini client.

    This function embeds the query text and compares it against pre-computed embeddings
    of document descriptions to find the most semantically similar matches.

    Args:
        query_text: Text query to search for
        docs: List of document dictionaries containing embeddings and metadata
        top_k: Number of top results to return. Defaults to 3

    Returns:
        list[Any]: List of document dictionaries with similarity scores, sorted by relevance
    """

    print(f"\n🔍 Embedding query: '{query_text}'")

    query_embedding = embed_text_with_gemini(query_text)

    if query_embedding is None:
        print("❌ Failed to embed query")
        return []
    else:
        print("✅ Query embedded successfully")

    # Calculate similarities using our custom function
    embeddings = [doc["embedding"] for doc in vector_index]
    similarities = cosine_similarity([query_embedding], embeddings).flatten()

    # Get top results
    top_indices = np.argsort(similarities)[::-1][:top_k]  # type: ignore

    results = []
    for idx in top_indices.tolist():
        results.append({**vector_index[idx], "similarity": similarities[idx]})

    return results

"""
Let's test this with an example:
"""

query = "what is the architecture of the transformer neural network?"
results = search_multimodal(query, vector_index, top_k=1)

if not results:
    pretty_print.wrapped("❌ No results found", title="❌")
else:
    result = results[0]

    pretty_print.wrapped(
        [
            f"Similarity {result['similarity']:.3f}",
            f"Filename {result['filename']}",
            f"Description `{result['description'][:1000]}...`",
        ],
        title=f"Results for query = {query}",
    )
    display_image(Path(result["filename"]))
# Output:
#   

#   🔍 Embedding query: 'what is the architecture of the transformer neural network?'

#   ✅ Query embedded successfully

#   [93m--------- Results for query = what is the architecture of the transformer neural network? ---------[0m

#     Similarity 0.744

#   [93m----------------------------------------------------------------------------------------------------[0m

#     Filename images/attention_is_all_you_need_1.jpeg

#   [93m----------------------------------------------------------------------------------------------------[0m

#     Description `This image is a detailed technical document, likely from a research paper or academic publication, featuring a prominent diagram of the Transformer model architecture alongside explanatory text.

#   

#   **Overall Composition & Scenery:**

#   The image is set against a clean white background. The top half is dominated by a multi-colored block diagram, while the bottom half contains black text organized into sections and paragraphs. A page number "3" is centered at the very bottom.

#   

#   **Objects & Diagram Elements:**

#   

#   *   **Main Diagram:** Titled "Figure 1: The Transformer - model architecture," it is a flowchart or block diagram illustrating a neural network architecture. It's broadly divided into two main vertical stacks: an **Encoder** on the left and a **Decoder** on the right.

#   *   **Encoder (Left Stack):**

#       *   Starts with "Inputs" at the bottom, receiving combined data from a pink "Input Embedding" rectangular block and a circular "Positional Encoding" icon.

#       *   Above the input, a vertica...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   <IPython.core.display.Image object>

"""
...and another example:
"""

query = "a kitten with a robot"
results = search_multimodal(query, vector_index, top_k=1)

if not results:
    pretty_print.wrapped("❌ No results found", title="❌")
else:
    result = results[0]

    pretty_print.wrapped(
        [
            f"Similarity {result['similarity']:.3f}",
            f"Filename {result['filename']}",
            f"Description `{result['description'][:1000]}...`",
        ],
        title=f"Results for query = {query}",
    )
    display_image(Path(result["filename"]))
# Output:
#   

#   🔍 Embedding query: 'a kitten with a robot'

#   ✅ Query embedded successfully

#   [93m---------------------------- Results for query = a kitten with a robot ----------------------------[0m

#     Similarity 0.811

#   [93m----------------------------------------------------------------------------------------------------[0m

#     Filename images/image_1.jpeg

#   [93m----------------------------------------------------------------------------------------------------[0m

#     Description `This image is a detailed, photorealistic digital rendering or illustration depicting an unlikely interaction between a large, imposing robot and a small, delicate kitten in an industrial setting.

#   

#   **Objects:**

#   *   **Robot:** The dominant figure is a large, humanoid robot, occupying the right side of the frame. Its body is constructed from dark, metallic armored plates in shades of charcoal, gunmetal, and dark grey, with visible bolts, rivets, and segmented joints suggesting a heavy, industrial design.

#       *   **Head/Face:** The robot's head is highly detailed, featuring intricate circuit board patterns or etched lines across its dark surface, implying advanced technology or artificial intelligence. Its most striking feature is its eyes, which are large, glowing red lights, casting a subtle red ambient glow. The face design is angular and segmented, reminiscent of a protective helmet or mask, with no visible mouth.

#       *   **Body:** Parts of its robust shoulder, upper arm, and a large, ...`

#   [93m----------------------------------------------------------------------------------------------------[0m

#   <IPython.core.display.Image object>

"""
## 4. Building multimodal AI agents
"""

"""
The last step is to hook our RAG `search_multimodal` function to a ReAct agent to create an agentic RAG system.

First, we define the `multimodal_search_tool` using LangGraph:
"""

from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent


@tool
def multimodal_search_tool(query: str) -> dict[str, Any]:
    """
    Search through a collection of images and their text descriptions to find relevant content.

    This tool searches through a pre-indexed collection of image-text pairs using the query
    and returns the most relevant match. The search uses multimodal embeddings to find
    semantic matches between the query and the content.

    Args:
        query: Text query describing what to search for (e.g., "cat", "kitten with robot")

    Returns:
        A formatted string containing the search result with description and similarity score
    """

    pretty_print.wrapped(query, title="🔍 Tool executing search for:")

    results = search_multimodal(query, vector_index, top_k=1)

    if not results:
        return {"role": "tool_result", "content": "No relevant content found for your query."}
    else:
        pretty_print.wrapped(str(results[0]["filename"]), title="🔍 Found results:")
    result = results[0]

    content = [
        {
            "type": "text",
            "text": f"Image description: {result['description']}",
        },
        types.Part.from_bytes(
            data=result["content"],
            mime_type="image/jpeg",
        ),
    ]

    return {
        "role": "tool_result",
        "content": content,
    }

"""
Next, we create a ReAct agent using LangGraph's `create_react_agent` function and the RAG tool defined above:
"""

def build_react_agent() -> Any:
    """
    Build a ReAct agent with multimodal search capabilities.

    This function creates a LangGraph ReAct agent that can search through images
    and text using the multimodal_search_tool. The agent uses Gemini 2.5 Pro
    for reasoning and tool execution.

    Returns:
        Any: A LangGraph ReAct agent instance configured with multimodal search tools
    """

    tools = [multimodal_search_tool]

    system_prompt = """You are a helpful AI assistant that can search through images and text to answer questions.
    
    When asked about visual content like animals, objects, or scenes:
    1. Use the multimodal_search_tool to find relevant images and descriptions
    2. Carefully analyze the image or image descriptions from the search results
    3. Look for specific details like colors, features, objects, or characteristics
    4. Provide a clear, direct answer based on the search results
    5. If you can't find the specific information requested, be honest about limitations
    
    Pay special attention to:
    - Colors and visual characteristics
    - Animal features and breeds
    - Objects and their properties
    - Scene descriptions and context
    
    Always search first using your tools before attempting to answer questions about specific images or visual content.
    """

    agent = create_react_agent(
        model=ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.1),
        tools=tools,
        prompt=system_prompt,
    )

    return agent

react_agent = build_react_agent()
react_agent

"""
Now, let's test it and make the ReAct agent find the color of our kitten from the indexed dataset:
"""

try:
    test_question = "what color is my kitten?"
    pretty_print.wrapped(test_question, title="🧪 Asking question:")

    response = react_agent.invoke(input={"messages": test_question})
    messages = response.get("messages", [])
    if messages:
        final_message = messages[-1].content
    else:
        final_message = "No response from the agent"
    pretty_print.wrapped(final_message, title="🤖 Agent response")
except Exception as e:
    print(f"❌ Error in ReAct agent: {e}")



# Output:
#  ---------------------------------------- 🧪 Asking question: ----------------------------------------
# ----------------------------------------------------------------------------------------------------
#   what color is my kitten?
# ----------------------------------- 🔍 Tool executing search for: -----------------------------------
#   my kitten
# ----------------------------------------------------------------------------------------------------
# 
# 🔍 Embedding query: 'my kitten'
# ✅ Query embedded successfully
# ----------------------------------------- 🔍 Found results: -----------------------------------------
#   images/image_1.jpeg
# ----------------------------------------------------------------------------------------------------
# ----------------------------------------- 🤖 Agent response -----------------------------------------
#   Based on the image, your kitten is a gray tabby. It has soft, short gray fur with darker tabby stripe patterns.
# ----------------------------------------------------------------------------------------------------
# Based on the image from the previous section (the one with the kitten and robot), the answer is correct.

</details>

</golden_source>

<golden_source type="guideline_youtube">
## YouTube Video Transcripts (from Article Guidelines)

<details>
<summary>Multimodal Embeddings: An Introduction</summary>

# Multimodal Embeddings: An Introduction

[00:00] Although AI research is traditionally split into distinct fields like NLP and computer vision, countless real-world problems require solutions that integrate information across these modalities. (On-screen text: "AI Research" appears, then replaced by "NLP" with a robot saying "Hello." and "CV" with a cartoon laptop saying "Aisle 2" to a banana image with "Where can I find this?")

In this video, I'll discuss how we can solve such problems using multimodal embeddings. (On-screen text: "Multimodal Embeddings" appears, then replaced by a banana image with "Apple, Banana, Papaya" and "Banana" checked, then another image search bar with "Papaya" and a papaya image checked) Then show how to use them to do things like zero-shot image classification and image search. And if you're new here, welcome! (On-screen text: "Shaw Talebi, Data Scientist, Bread Enthusiast" appears) I'm Shaw. I make videos about the things I'm learning about and building in AI. And if you enjoyed this content, please consider clicking the subscribe button. That's a great no-cost way you can support me in all the videos that I make.

[00:30] (A red "SUBSCRIBE" button with a white outline appears and is clicked)

[00:44] Here we're going to talk about multimodal embeddings. (Slide title: "Multimodal Embeddings: An introduction with example code (ft. CLIP)"). Although the discussion here will focus around CLIP, which works with text and image data, this is a much more general idea that can be extended to many other modalities.

_This section introduces the concept of multimodal embeddings and the general scope of the video, mentioning CLIP as a primary example._

[01:00] Before talking about multimodal embeddings, it's worth answering the question, what are embeddings? The way I'll define embeddings here are useful numerical representations of data learned through model training. A classic example of this is BERT, which is a popular language model before the era of GPT-3 and all the modern large language models. BERT used to be state of the art, and one of the things that it does is masked language modeling. In other words, you can give it a sequence of text where one of the tokens in that sequence is masked, meaning that it's not visible, and BERT will predict the most likely token that goes in the place of that mask.

[01:30] (Slide shows title: "What are Embeddings?", then an image of a BERT model appears. Text input: "Listen to your [MASK]. -> BERT". Text output: "Listen to your instincts." appears) So if you pass in the sequence listen to your, the most likely token that goes in this sequence is instincts. So it turns out that through learning how to do this prediction, BERT learns useful representations of text, which can be extended to other NLP tasks. (An arrow points down from BERT with "Drop head", showing a "BERT (mutilated)" model below it. Then text "Listen to your instincts." is input to this model, outputting a matrix of numbers n x d.) The basic idea here is that you'll take BERT and you'll drop its head, so the classification head, which is doing this masked language modeling, and you'll have this mutilated version of BERT, which instead of doing this token prediction, it'll take an input sequence of text and return a numerical representation of it.

[02:00] (The matrix of numbers is highlighted) Where each row in this matrix corresponds to each token in this text sequence, and then each of these columns corresponds to the embedding dimension, the dimension of this internal representation of text that BERT uses in order to do masked language modeling. (The row of the matrix is highlighted, then columns, indicating dimensions.) We can go one step further and go from token-level representations to sequence-level representations, so we could do something like take the average across all these tokens in the sequence, and we're left with a one by D matrix, which represents the entire sequence. (An arrow points from the matrix to a single row vector, 1 x d). And of course, to get these embeddings to be a bit more practical, people will often do additional fine-tuning on top of these embeddings, but this is the basic idea of where they are coming from.

[02:30] A key point about embeddings is that these aren't just arbitrary numerical representations, they are typically semantically meaningful, such that if we were to look at how text were organized in this embedding space, similar concepts would tend to be located close together, while dissimilar concepts will tend to be far apart. (Slide updates to "What are Embeddings?" with two subsections "Text Embeddings" and "Image Embeddings". A 2D coordinate system is shown for "Text Embeddings" with phrases like "A cute puppy", "A good boy", "Best pet in the world", "A cute cat", "Funny cat meme" plotted, with similar concepts clustered).

[03:00] For example, the sequence a cute puppy might be relatively close to the sequence a good boy, while that same sequence a cute puppy might be relatively far from a sequence like funny cat meme. However, this isn't limited to just text, we can generate embeddings for any type of data. (A second 2D coordinate system for "Image Embeddings" appears, showing images of cats, dogs, and a goat. Cats are clustered, dogs are clustered, and the goat is separate). Another popular type of data we might work with are images, so if we had some image embeddings, the space might be structured like this, where we tend to have cats in the top left part, the dogs tend to be in the bottom right part, and then we have a goat further away from these. Although text embeddings and image embeddings are super helpful in that they can be adapted and repurposed to solve other either NLP tasks or computer vision tasks, one major limitation here is that any random text embedding space we might be working with and any random image embedding space we might be working in don't have any relationship to one another.

[04:00] There's no way out of the box to directly map this text embedding space to this image embedding space and vice versa, even if they are semantically meaningful in of themselves. (Text on screen: "Text Embeddings spaces are not aligned!" appears). And that's something we can plainly see here in that the text and image embedding spaces are not aligned because for this text embedding space, the puppies tend to be in the top right, the cats tend to be at the bottom, while in our image embedding space the cats tend to be up here and the dogs tend to be down here. But what if there was a way we could merge these two embedding spaces together? (Text on screen: "Image Embeddings spaces are not aligned!" appears, then both text and image embedding spaces are shown as "not aligned").

[05:00] _This section defines embeddings, illustrates them with BERT for text and examples for text and image data, and highlights the limitation of separate embedding spaces._

[05:08] That's exactly the key idea behind multimodal embeddings, which are embeddings which align representations of different data modalities. (Slide title: "Multimodal Embeddings: Embeddings which align representations of different data modalities." The two separate 2D coordinate systems merge into one, showing both text phrases and animal images within the same space, clustered by concept, e.g., "A cute cat" near cat images, "A cute puppy" near dog images). And the basic intuition here is that if we had a multimodal embedding space, we could represent text and images in the same vector space. So now, indeed, text like a cute puppy will be close to images of cute puppies, the text a cute cat will be close to images of a cute cat, and the same thing will hold for other concepts. However, this idea is not limited to just images and text. We could just as easily embed audio and images together.

[06:00] (Icons for audio are added to the multimodal embedding space) Maybe this is an audio file that is a cat meowing, this is a goat making goat noises, we have a puppy with like a cute bark, and then maybe we have like a funny shrieking sound associated with this cat meme here. Another application of this is aligning representations of brain signals with images and text. (Images of brain activity maps replace audio icons). What this means is, if we were to record someone's brain activity and then represent it in this embedding space, we could in principle decode the brain information to generate images and text, so in essence, reading people's thoughts. (Text on screen: "Reading people's thoughts" appears). Actually, in reference number four, they are aiming to do exactly this with large language models.

[06:30] Intuitively, this idea of multimodal embeddings is pretty simple to understand, we have this embedding space which is agnostic to modality, so it doesn't matter if it's an image of a cat, a text description of a cat, or the brain signals of someone looking at a picture of a cat, these numerical representations will be relatively similar. But how do we create these aligned numerical representations? In other words, how does this work under the hood?

_This section defines multimodal embeddings, illustrates how different modalities like text and images can be aligned in a shared space, and gives futuristic examples like aligning audio and brain signals._

[06:56] So the key technique behind creating these types of embeddings is contrastive learning, which is an approach that seeks to represent different views of the same underlying information similarly. (Slide title: "Contrastive Learning: Learning approach that seeks to represent different views of the same information similarly"). And the way this works is that we'll train a model on two things. One, positive pairs of data, and two, negative pairs. (On-screen text: "Positive Pairs" appears, then "Negative Pairs" appears). So in the case of aligning image and text representations, positive pairs might be a picture of a cute cat and a textual caption for this image, and then we might have the text and an image of a cute puppy, and then we might have the same thing for a baby goat.

[07:30] (Images of a cat, puppy, and baby goat with corresponding text captions, all marked with a green checkmark as "Positive Pairs"). On the other hand, negative captions might look something like this, where you have the image of a cat, but the caption is a cute puppy, image of a puppy and the caption is a goat, and you have a goat and the caption is a cat. (Images of a cat with "A cute puppy" text, a puppy with "Cute baby goat" text, and a baby goat with "A cute cat" text, all marked with a red X as "Negative Pairs"). The intuition here is that we train a model to maximize the similarity between these positive pairs and minimize the similarity between these negative pairs. That's the key intuition. In the following slides, we're going to go one level deeper and look at the loss function and the math behind how this is accomplished. If you don't care about the math and how this is working under the hood, feel free to skip ahead to the example code, but if you're interested in the math, we're about to jump right into it.

[08:00] The way we can use contrastive learning to align image and text representations is we can take images, generate image embeddings using an image encoder. (Images of a cat, puppy, and baby goat are shown, each with an arrow pointing to a vector of numbers, labeled as "Generate image embeddings using any image encoder"). So basically we take our images and generate a single numerical representation for them. And then we can take all these image embeddings, and we can concatenate them into a matrix that I'll call I sub E. So this will be an N by D matrix, where N is the number of images, so if you have three images here, it'll be one, two, three. And then D, so the number of columns, will be the embedding dimension.

[08:30] (The individual image embeddings are concatenated into a matrix I_e (n x d)). Then we can do a similar thing for text, so we can get a text encoder from off the shelf. We can generate these text embeddings. (Text captions "A cute cat", "A cute puppy", "Cute baby goat" are shown, each with an arrow pointing to a vector of numbers, labeled as "Generate text embeddings using any text encoder"). And then we can concatenate them into a matrix that I'll call T sub E, and that will have the same shape. So we'll have N captions, and then they'll have some embedding dimension. (The individual text embeddings are concatenated into a matrix T_e (n x d)). Just to point out here that the representations that we would put into these matrices won't directly come from an image encoder and text encoder. Instead, these will be multiplied by some learnable weight matrix and then normalized before being organized in this matrix. (Mathematical expression: Z_i W_I / ||Z_i W_I|| = I_e and Z_j W_T / ||Z_j W_T|| = T_e, with "Raw embeddings" and "Learnable weights" highlighted).

[09:30] So that weight matrix that we multiply the original embeddings by are the learnable parameters. Once we have these matrices I and T, we can construct this logits matrix. (Mathematical formula: `logits_i,j = sim(I_e[i], T_e[j]) / tau` appears). Basically, what that means is we're going to take each image in our image embedding matrix, and then each text sequence in our text embedding matrix, and we're going to compute their similarity. Typically, this is just a cosine similarity, so you do the dot product between these two matrices, and then you'll divide it by a temperature parameter. That's what this tau parameter is representing. And the reason we call them logits is because at some point, it's going to be the argument in an exponential function. And we'll see that in a little bit here. (A grid matrix of `logits_i,j` is shown, with image rows and text column headers. Diagonal elements `logits_1,1`, `logits_2,2`, `logits_3,3` are green, others are red).

[10:00] So taking just those three examples from the previous slide, the similarity between the first image and the first text sequence will be in this one, one position of the matrix, and then the similarity between this cat image and the sequence a cute puppy will be represented by this value here, then the similarity between this cat image and the text sequence a cute baby goat will be represented by this value here, and so on and so forth. Just looking at this, we can see that what we want is to make the logits on the diagonal of this matrix as big as possible. So in other words, we want to maximize the similarity between the positive pairs. And then we want to minimize the off-diagonal elements, which correspond to negative pairs. (Mathematical formula for contrastive loss for images: `l_i = - log ( exp(logits_i,i) / sum_{j=1}^{n} exp(logits_i,j) )` appears).

[11:00] One way we can do this is via the contrastive loss. So this might take slightly different forms depending on the context or the paper that you're reading. But here I'm going to follow what was done in developing CLIP, which is reference number three here. And so basically, one way we can achieve this goal of maximizing the similarity of these on-diagonal elements and minimizing the similarity between these off-diagonal elements is via this equation here. Which is basically saying for the I-th image, so let's say this cat image here, we want the numerator to be as big as possible. So the numerator will be the II element, so this will be either one, one or two, two or three, three. And then we want the denominator to be as small as possible. So if the numerator is big, the denominator is small, that means this fraction becomes big. And then if we take the log of that, we'll still have a big number. And then we want this number to be as big as possible, because the goal of training is to minimize the loss. And then if this number is big, and we have a minus sign next to it, then this will be as minimal as possible.

[12:00] That was probably a bit abstract, so let's walk through this step by step. Let's look at just the first image first. With this notation, I call the loss associated with the first image L1. This will consist of taking this one, one logit, and then summing over all the logits in this first row. So we're basically taking this image and comparing it to every single caption. Then we do the same thing for the second image. We have the positive pair similarity here. And then we sum over all the logits in this row. And then we do a similar thing for image number three. So we look at the positive pair similarity, and then we sum over all the logits or similarities in this row. (The loss calculation is animated for each image row).

[12:30] We can do this for every single image in our batch, or even in our whole training dataset. And then we can aggregate them to get the final contrastive loss. (Mathematical formula: `L_I = (1/n) sum_{i=1}^{n} l_i` appears, then `L_I = (l_1 + l_2 + l_3) / 3` for n=3). What that'll look like is we'll take the loss according to the first image, the loss according to the second image, and the loss corresponding to the third image, and then we can just take their average. And that'll give us the contrastive loss for the images. But we can do the same exact thing for text. (Mathematical formula for contrastive loss for text: `l_j = - log ( exp(logits_j,j) / sum_{i=1}^{n} exp(logits_i,j) )` appears). This is how I'm notating contrastive loss for the text. I've switched the index here from J to I, and then I've changed the summation here to I.

[13:30] I feel this notation might be a bit too subtle, but hopefully explaining it step by step, it makes sense what I mean here. So let's see what this looks like for the first text sequence. We're going to be evaluating a cute cat, so we'll look at logits one, one here, and then we'll sum over the logits in this first column. We'll do the same thing for this second text sequence, a cute puppy, and we'll sum over all the logits in this column. And then finally, we do it for the final text sequence. It's important to note here that generally this logits matrix is asymmetric, because the similarity between the text a cute puppy and this image of a cat is in general different than the similarity between this image of a puppy and the text sequence a cute cat. (The loss calculation is animated for each text column).

[14:00] That's an important thing to note here and that's the reason why we go through this whole procedure for the images and the text sequences separately. And then we can aggregate the loss over all the text examples just like we did for the images like this. (Mathematical formula: `L_T = (1/n) sum_{j=1}^{n} l_j` appears, then `L_T = (l_1 + l_2 + l_3) / 3` for n=3). And then we'll get a total text loss by taking the average of all the examples in our mini-batch. (Mathematical formula for final loss: `L = (L_I + L_T) / 2` appears). We can then combine the image loss and text loss together by taking their average. Then we can write it all out to have this big monstrosity all on one page. (The full loss formula is shown, indicating "Image term" and "Text term").

[14:30] But basically, this first term here corresponds to the image loss, the second term here corresponds to the text loss, and this is how we train the weights which translate the raw image and text encodings into our multimodal embedding space. This will give us a training signal which we can use to update the weights of these projection matrices, can just keep doing that until we're satisfied with the loss.

_This section details contrastive learning, explaining positive and negative pairs, and then delves into the mathematical formulation of the contrastive loss used to align different modalities._

[15:12] So if that was much more math than you were hoping to get out of this video, I apologize for that, but let's jump to practical applications of multimodal embeddings. Here I'm going to use CLIP for two different use cases. This first use case is zero-shot image classification. The meaning of that is, we're going to do image classification without explicitly training CLIP to distinguish between the different image classes that we're considering. (Text: "Example 1: Using CLIP for 0-shot Image Classification"). The first step is to import transformers. I'm going to bring in these two things. And then I'm importing this PIL library, which will allow us to work with images in Python.

[15:40] (Code snippet showing imports from `transformers` and `PIL`). Next, we'll load in the model and the data processor. (Code snippet showing loading of CLIPModel and CLIPProcessor). The image pre-processing is important because images could be any type of size and shape and all that. The CLIP processor is an abstraction that ensures the data aren't in a suitable format to be passed through the model. Next, we're going to load in our image. So I'm going to load in this image of a cute cat, so it's the same one we've seen so far. Then I'm going to define the text classes. (Code snippet showing image loading and text class definition for "a photo of a cat" and "a photo of a dog". The image of the cute cat appears).

[16:10] So this is a really interesting aspect of using CLIP for zero-shot image classification, because before if you wanted to do image classification, traditionally, that was something that was set at model training. It was implicitly coded into the architecture of the model in that you had this classification head, and each value in the output layer corresponded to the probability of class one versus class two versus class three, so on and so forth. But now, when using CLIP, which is trained via contrastive learning, we actually pass these classes as text inputs. (Code snippet for passing image and text to processor and then to CLIP model). So with our text and image inputs defined, we can pass these through our processor to put them in a suitable format as CLIP. And then we can just pass it to the model.

[16:50] Then, with this one line of code, we'll generate these outputs. (Code snippet for extracting `logits_per_image` and converting to probabilities via `softmax`). Then we can extract the logits per image. Recall the logits matrix that we saw a few slides ago, where we had an image, and then we had logit values or similarity values between that image and every single piece of text that we passed into the model. That's exactly what we're extracting here. We're extracting the similarity score of the input image to both the text inputs. We can then convert these logits to probabilities via the softmax. (The diagram of `logits_i,j` from earlier is recalled, focusing on the first row's logits).

[17:20] And then this will give us a prediction. (Code snippet for printing `predicted_class` and `Probability`). What I'm doing here is I'm just doing argmax of the probabilities tensor and using that to pick out the predicted class from this original list that I created. And then I'm just going to print everything like this, so I'll print the predicted class as well as a rounded probability corresponding to that class. With that, the most probable class is a photo of a cat with a associated probability of 99.79%. (Output: `>> a photo of a cat | Probability = 0.9979`). So basically nails the classification of this image. But let's see what happens when we use different text classes. (New text: "Classes: "ugly cat" vs "cute cat""). Instead of passing in a photo of a cat and a photo of a dog, which are pretty easy classes to distinguish between, let's try something a bit more nuanced like a ugly cat versus cute cat. And again, here the model basically nails it with a 97% probability of this cute cat class. (Output: `>> cute cat | Probability = 0.9703`).

[18:20] (New text: "Classes: "cat meme" vs "not cat meme""). And then we can try something even more challenging, like trying to distinguish if this is a cat meme or not a cat meme, and it indeed gets that it's not a cat meme, but we can see that the probability dropped significantly. (Output: `>> not cat meme | Probability = 0.5464`). Then as a final test of this model, let's see what happens when we pass in an actual cat meme and give it the class choices of cat meme versus not cat meme. (The image of the cat meme is shown). And so here the model again nails it. It correctly classifies this as a cat meme with a probability of 83%. (Output: `>> cat meme | Probability = 0.8338`). And so again, what we're doing here, using CLIP, is we're taking these three entities, we're taking the text sequence of cat meme, the text sequence of not cat meme, and this image of a cat, encoding them in a shared embedding space, and we're evaluating the similarity between this image of a cat and the text sequence cat meme, and the similarity between this image of a cat and the text sequence not a cat meme. And then we can convert that similarity into a probability as well as a class prediction.

[19:20] The key unlock here is that you are not restricted or limited in the different class labels you can use for image classification. You can be as detailed or vague as you like. You can adapt this to endless different use cases, which is pretty amazing.

_This section demonstrates CLIP's ability to perform zero-shot image classification by comparing image embeddings to text embeddings representing different classes, showcasing its flexibility and performance on various class definitions._

[19:50] This second example is basically the inverse of zero-shot image classification. There, we had an input image and we wanted to match it with one of the input text sequences. Here, in example two, we're going to do the exact opposite. So instead of starting with an image, we're going to start with a piece of text, in other words, a search query, and then we're going to match it to a set of images. So essentially, what we're doing is we're doing a search over a set of images. (Text: "Example 2: Using CLIP for Image Search"). The way this looks is we'll first load in our images. (Code snippet for loading image files: `cat_cute.png`, `dog.png`, `goat.png`. The three animal images appear below the code). Here we have a picture of a cute cat, a picture of a dog, and a picture of a goat. We'll store them in this image list. We're using the PIL library to open the images and just store them in this list. Then we're going to define a query and process the inputs. (Code snippet for defining query `a cute dog` and passing it with the image list to the processor). Here our query will be a cute dog. And then we'll pass this query along with our image list through the processor, so it's in the appropriate format for CLIP. Then we'll run these inputs through our model, get these outputs, extract the logits per text now. (Code snippet for running model and extracting `logits_per_text`). Before we did logits per image, now we're doing logits per text. So these are going to be the similarity scores between the input text and all the images that we inputted. And then we'll convert these logits into probabilities. (Code snippet for converting logits to probabilities).

[20:50] So with that, we can evaluate the best match. (Code snippet for evaluating and printing the best match). So I'm doing that again in a similar way, so we have these probabilities, doing argmax, which will give us an integer zero, one or two. We can use that to pick out the best matched image, and then we can take the probability associated with that image. And then we can just print everything. (Output: `>> Match probability: 0.9817`). Again, the query here was a cute dog, and this is the best matched image with a probability of about 98%. (The dog image appears). But again, that was a super easy example. So let's try a trickier query like something cute but metal. In this case, the model returns the goat, which is indeed cute. But also goats are associated with heavy metal music, and it got a 77% match probability. (Output: `>> Match probability: 0.7715`, and the goat image appears). Reading this, a good boy. The text itself doesn't have anything to do with animals. You know, maybe it's a human boy and he's well-behaved. But a good boy is a colloquialism for dogs that we use often. And the model can pick that up quite easily, so it matches it with a dog with 82% probability. (Output: `>> Match probability: 0.8248`, and the dog image appears). It would be interesting to see if we threw in a picture of a human boy to see how the model would handle that case. This could be something that you do with the example code from the GitHub. And then we can try an extremely controversial query like the best pet in the world. (Output: `>> Match probability: 0.5664`). For this, the model returns a cat with a 56% match probability. (The cute cat image appears). This is likely indicating that on average, people on the internet love cats more than they love dogs. Nevertheless, it's super interesting how we can use this model in order to do search like this.

_This section showcases CLIP's capability for image search. It demonstrates how a text query is used to find the most relevant image from a collection, highlighting CLIP's understanding of subtle semantic relationships, even with nuanced queries._

[22:47] So those were the two examples. Code is on the GitHub, link in the description below. Let's look ahead to the next video of this series. In the previous video, so part one, we talked about multimodal large language models. So basically, large language models that can process or generate multiple data modalities. (Text: "What's Next? Part 1 (i.e. last video)"). In this video, we talked about multimodal embeddings, like those generated by CLIP, which can be used to do things like image search. So we pass in a query and a set of potential images, and then it'll spit out the best matched image. (Diagram shows "Multimodal LLM" processing text, image, audio to generate text. Then "Multimodal Embedding" processes text and image to output an image.) In the next video of this series, we're going to bring these two ideas together to create a multimodal RAG system. (Text: "What's Next? Multimodal RAG"). The basic flow here will be to take a user query, like what's there to do in Bali? (Text: "User Query: What's there to do in Bali?"). We'll pass the query into a multimodal retrieval system, which involves using a multimodal embedding model to pick out the documents and images that are most relevant to this query. We'll take the user query and relevant documents and images to generate a prompt. And then we'll pass that prompt into a multimodal large language model, which can process the user query, relevant text documents, and relevant images to generate a helpful response. (Diagram shows User Query -> Multimodal Embedding -> Retrieve relevant (multimodal) context -> Create Prompt -> Multimodal LLM -> Model Response).

[24:10] And as a final note, if you enjoyed this video and you want to learn more, check out the blog published in Towards Data Science. There I went into some details that I probably missed here. And as always, even though this is going to be a member-only story, you can access it completely for free using the friend link in the description below. And with that, thank you so much for your time and thanks for watching. (Text on screen: "Thanks for watching.").

_This section summarizes the current video and the previous one in the series, then introduces the topic of the next video: building a multimodal RAG system by combining multimodal LLMs and multimodal embeddings._

</details>

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

<details>
<summary>ColPali: Efficient Document Retrieval with Vision Language Models</summary>

# ColPali: Efficient Document Retrieval with Vision Language Models

**Source URL:** <https://arxiv.org/pdf/2407.01449v6>

## Abstract

Documents are visually rich structures that convey information through text, but also figures, page layouts, tables, or even fonts. Since modern retrieval systems mainly rely on the textual information they extract from document pages to index documents — often through lengthy and brittle processes — they struggle to exploit key visual cues efficiently. This limits their capabilities in many practical document retrieval applications such as Retrieval Augmented Generation (RAG).
To benchmark current systems on visually rich document retrieval, we introduce the Visual Document Retrieval Benchmark ViDoRe, composed of various page-level retrieval tasks spanning multiple domains, languages, and practical settings.
The inherent complexity and performance shortcomings of modern systems motivate a new concept; doing document retrieval by directly embedding the images of the document pages. We release ColPali, a Vision Language Model trained to produce high-quality multi-vector embeddings from images of document pages. Combined with a late interaction matching mechanism, ColPali largely outperforms modern document retrieval pipelines while being drastically simpler, faster and end-to-end trainable.
We release models, data, code and benchmarks under open licenses at https://hf.co/vidore.

## 1 Introduction

Document Retrieval consists of matching a user query to relevant documents in a given corpus. It is central to many widespread industrial applications, either as a standalone ranking system (search engines) or as part of more complex information extraction or Retrieval Augmented Generation (RAG) pipelines.

Over recent years, pretrained language models have enabled large improvements in text embedding models. In practical industrial settings, however, the primary performance bottleneck for efficient document retrieval stems not from embedding model performance but from the prior data ingestion pipeline. Indexing a standard PDF document involves several steps. First, PDF parsers or Optical Character Recognition (OCR) systems are used to extract words from the pages. Document layout detection models can then be run to segment paragraphs, titles, and other page objects such as tables, figures, and headers. A chunking strategy is then defined to group text passages with some semantical coherence, and modern retrieval setups may even integrate a captioning step to describe visually rich elements in a natural language form, more suitable for embedding models.
In our experiments (Table 2), we typically find that optimizing the ingestion pipeline yields much better performance on visually rich document retrieval than optimizing the text embedding model.

**Contribution 1: ViDoRe.**
In this work, we argue that document retrieval systems should not be evaluated solely on the capabilities of text embedding models, but should also consider the context and visual elements of the documents to be retrieved. To this end, we create and openly release ViDoRe, a comprehensive benchmark to evaluate systems on page-level document retrieval with a wide coverage of domains, visual elements, and languages. ViDoRe addresses practical document retrieval scenarios, where queries often necessitate both textual and visual understanding for accurate document matching. We highlight the shortcomings of current text-centric systems in these settings.
[^1]: The ViDoRe benchmark leaderboard is hosted publicly at [https://huggingface.co/spaces/vidore/vidore-leaderboard](https://huggingface.co/spaces/vidore/vidore-leaderboard) to encourage further developments.

**Contribution 2: ColPali.**
We propose a novel concept and model architecture based on Vision Language Models (VLMs) to efficiently index documents purely from their visual features, allowing for subsequent fast query matching with late interaction mechanisms. Our method, ColPali, significantly outperforms all other retrieval systems on ViDoRe while being fast and end-to-end trainable.
These results demonstrate the potential and the many benefits of this novel Retrieval in Vision Space concept, which could significantly alter the way document retrieval is approached in the industry moving forward.
We release all resources at [https://hf.co/vidore](https://hf.co/vidore).

Figure 1: ColPali simplifies document retrieval w.r.t. standard retrieval methods while achieving stronger performances with better latencies. Latencies and results are detailed in section 5 and Appendix B.4.
Image: extracted/6240861/images/final_architecture.png

## 2 Problem Formulation & Related Work

**Problem Setting.**
In our setting, a retrieval system scores how relevant a document $d$ from corpus $\mathcal{D}$ is with respect to a query $q$. Computing the similarity score $s(q,d) \in \mathbb{R}$ for each of the $|\mathcal{D}|$ documents in the corpus creates a ranking we can use to extract the most relevant documents. In this work, we focus on page-level retrieval: given a query, is the correct document page retrieved by the system? For coherence with existing literature, we further use the term document to refer to individual pages, i.e. the atomic retrieved elements in our setting. As we focus on practical industrial retrieval applications (RAG, search engines) with potentially large corpora sizes, latency constraints are imposed on scoring systems. Most current retrieval systems can be decomposed into (1) an offline indexation phase in which a document index is built and (2) an online querying phase in which a query is matched to documents from the index and where low latency is vital to the user experience.

Under these industrial constraints, we identify three main properties an efficient document retrieval systems should exhibit: (R1) strong retrieval performance, as measured by standard retrieval metrics; (R2) fast online querying, measured through average latencies; (R3) high throughput corpus indexation, ie. the number of pages that can be embedded in a given timeframe.

### 2.1 Textual Retrieval Methods

**Document Retrieval in Text Space.**

Statistical methods based on word frequency like TF-IDF and BM25 are still widely used due to their simplicity and efficiency. More recently, neural embedding models based on fine-tuned large language models display state-of-the-art performance on a variety of text embedding tasks and top the retrieval leaderboards.

**Neural Retrievers.**
In bi-encoder models, documents are independently mapped offline to a dense vector space. Queries are embedded online and matched to documents through a fast cosine distance computation.
A slower, but slightly more performant alternative, cross-encoder systems concatenate query and document as a single input sequence and iteratively attribute matching scores to each possible combination. This enables full attention computation between query and document terms but comes at the cost of computational efficiency, as $|\mathcal{D}|$ encoding passes must be done online.

**Multi-Vector retrieval via late interaction.**
In the late interaction paradigm introduced by ColBERT, an embedding is pre-computed and indexed per document token. At runtime, similarity can be computed with individual query token embeddings. The idea is to benefit from the rich interaction between individual query and document terms while taking advantage of the offline computation and fast query matching enabled by bi-encoders. See Appendix E for more details.

**Retrieval Evaluation.**
Although benchmarks and leaderboards have been developed to evaluate text embedding models, much of the performance improvements in industrial use cases of embedding models stem from the prior data ingestion pipeline. While documents often rely on visual elements to more efficiently convey information to human readers, text-only systems barely tap into these visual cues. Other work has also independently studied table or chart retrieval systems through repurposed Question Answering datasets but only assessing specialized methods for each task.

To our knowledge, no benchmark evaluates document retrieval systems in practical settings; in an end-to-end manner, across several document types and topics, and by evaluating the use of both textual and visual document features.

### 2.2 Integrating Visual features

**Contrastive Vision Language Models.**
Mapping latent representations of textual content to corresponding representations of visual content has been done by aligning disjoint visual and text encoders through contrastive losses. While some OCR capabilities exist in these models, the visual component is often not optimized for text understanding.

The Fine-grained Interactive Language-Image Pre-training framework extends the late interaction mechanism to cross-modal Vision Language Models, relying on max similarity operations between text tokens and image patches.

**Visually Rich Document Understanding.**
To go beyond text, some document-focused models jointly encode text tokens alongside visual or document layout features.
Large Language transformer Models (LLMs) with strong reasoning capabilities have recently been combined with Vision Transformers (ViTs) to create VLMs where image patch vectors from contrastively trained ViT models are fed as input embeddings to the LLM and concatenated with the text-token embeddings.

**PaliGemma.**
The PaliGemma-3B model extends concepts from Pali3, and projects SigLIP-So400m/14 patch embeddings into Gemma-2B’s text vector space. Along with its reasonable size w.r.t. other performant VLMs, an interesting property of PaliGemma’s text model is that it is fine-tuned with full-block attention on the prefix (instruction text and image tokens). See Appendix E for more details.

VLMs display enhanced capabilities in Visual Question Answering, captioning, and document understanding, but are not optimized for retrieval tasks.

## 3 The ViDoRe Benchmark

Existing benchmarks for contrastive vision-language models primarily evaluate retrieval for natural images. On the other hand, textual retrieval benchmarks are evaluated at a textual passage level and are not tailored for document retrieval tasks. We fill the gap with ViDoRe, a comprehensive benchmark for document retrieval using visual features.

### 3.1 Benchmark Design

ViDoRe is designed to comprehensively evaluate retrieval systems on their capacity to match queries to relevant documents at the page level. This benchmark encompasses multiple orthogonal subtasks, with focuses on various modalities - text, figures, infographics, tables; thematic domains - medical, business, scientific, administrative; or languages - English, French. Tasks also span varying levels of complexity, in order to capture signals from both weaker and stronger systems.
As many systems require large amounts of time to index pages (captioning-based approaches can take dozens of seconds per page for instance), we limit the number of candidate documents for each retrieval task in order to evaluate even complex systems in a reasonable timeframe without sacrificing quality. For trainable retrieval systems, we provide a reference training set that can be used to facilitate comparisons.

**Table 1: ViDoRe comprehensively evaluates multimodal retrieval methods.**

| Dataset | Language | # Queries | # Documents | Description |
|---|---|---|---|---|
| Academic Tasks | | | | |
| DocVQA | English | 500 | 500 | Scanned documents from UCSF Industry |
| InfoVQA | English | 500 | 500 | Infographics scrapped from the web |
| TAT-DQA | English | 1600 | 1600 | High-quality financial reports |
| arXiVQA | English | 500 | 500 | Scientific Figures from arXiv |
| TabFQuAD | French | 210 | 210 | Tables scrapped from the web |
| Practical Tasks | | | | |
| Energy | English | 100 | 1000 | Documents about energy |
| Government | English | 100 | 1000 | Administrative documents |
| Healthcare | English | 100 | 1000 | Medical documents |
| AI | English | 100 | 1000 | Scientific documents related to AI |
| Shift Project | French | 100 | 1000 | Environmental reports |

**Academic Tasks.**
We repurpose widely used visual question-answering benchmarks for retrieval tasks: for each page-question-answer triplet, we use the question as the query, and the associated page as the gold document (Table 1). These academic datasets either focus on single specific modalities or target more varied visually rich documents. Moreover, we consider TabFQuAD, a human-labeled dataset on tables extracted from French industrial PDF documents released with this work. Details can be found in Appendix A.1.

**Practical tasks.**
We construct topic-specific retrieval benchmarks spanning multiple domains to go beyond repurposed QA datasets and evaluate retrieval in more realistic industrial situations (e.g. RAG). To achieve this, we collect publicly accessible PDF documents and generate queries pertaining to document pages using Claude-3 Sonnet, a high-quality proprietary vision-language model. In total, we collect 1,000 document pages per topic, which we associate with 100 queries extensively filtered for quality and relevance by human annotators. The corpus topics are intentionally specific to maximize syntactic proximity between documents, creating more challenging retrieval tasks and covering an array of orthogonal domains (Table 1).
[^2]: Answers are generated alongside queries to (1) ground queries and improve their quality and (2) provide resources to foster future work.

**Evaluation Metrics.**
We evaluate performance on our benchmark (Requirement R1) using standard metrics from the retrieval literature (nDCG, Recall@K, MRR). We report nDCG@5 values as the main performance metric in this work and release the complete sets of results along with the models.
[^3]: [https://huggingface.co/vidore](https://huggingface.co/vidore)
To validate compliance with practical industrial requirements (section 2), we also consider query latencies (R2) and indexing throughputs (R3).

### 3.2 Assessing Current Systems

**Unstructured.** We evaluate retrieval systems representative of those found in standard industrial RAG pipelines. As is common practice, we rely on the Unstructured
[^4]: [www.unstructured.io](www.unstructured.io)
off-the-shelf tool in the highest resolution settings to construct high-quality text chunks from PDF documents. Unstructured orchestrates the document parsing pipeline, relying on deep learning vision models to detect titles and document layouts, OCR engines to extract text in non-native PDFs, specialized methods or models to detect and reconstruct tables, and implements a chunking strategy (by-title) that leverages the detected document structure to preserve section boundaries when concatenating texts. As is common practice, in our simplest Unstructured configuration (text-only), only textual elements are kept and figures, images, and tables are considered noisy information and are filtered out.

**Unstructured + X.** While Unstructured is a strong baseline by itself, we further augment Unstructured’s output by integrating the visual elements. In (+ OCR), tables, charts, and images are run through an OCR engine, processed by Unstructured, and chunked independently. In (+ Captioning), we set up a fully-fledged captioning strategy, in which we feed visual elements to a strong proprietary Vision Language Model (Claude-3 Sonnet) to obtain highly detailed textual descriptions of the elements.
Both strategies aim to integrate visual elements in the retrieval pipeline but incur significant latency and resource costs (subsection 5.2).

**Embedding Model.** To embed textual chunks, we evaluate Okapi BM25, the de facto standard sparse statistical retrieval method, and the dense encoder of BGE-M3, a multilingual neural method with SOTA performance in its size category. Chunks are embedded and scored independently, and page-level scores are obtained by max-pooling over the page’s chunk scores.
[^5]: We empirically validated the max-pooling strategy over sub-page chunks to be more effective than concatenating all page chunks before embedding pagewise.

**Contrastive VLMs.** We also evaluate the strongest available vision-language embedding models; Jina CLIP, Nomic Embed Vision, and SigLIP-So400m/14.

**Results.** From a performance perspective, best results are obtained by combining the Unstructured parser with visual information, either from captioning strategies or by running OCR on the visual elements (Table 2). Little difference is seen between BM25 and BGE-M3 embeddings highlighting the visual information bottleneck. Contrastive VLMs lag behind. Beyond retrieval performance (R1), the indexing latencies (R2) reported in Figure 2 illustrate that PDF parsing pipelines can be very lengthy, especially when incorporating OCR or captioning strategies. Querying latencies at runtime (R3) are very good for all evaluated systems ($\leq 22$ ms on a NVIDIA L4) due to fast query encoding and cosine similarity matching.

Figure 2: Offline document indexing with ColPali is much simpler and faster compared to standard retrieval methods. The PDF Parser results are obtained following the Unstructured settings with BGE-M3 detailed in subsection 3.2. All indexing speeds are averaged per-page latencies. More details in Appendix B.4
Image: x1.png

## 4 Late interaction based Vision Retrieval

### 4.1 Architecture

**Vision-Language Models.**
Encouraged by their strong document understanding capabilities, we propose adapting recent VLMs for retrieval. The key concept is to leverage the alignment between output embeddings of text and image tokens acquired during multi-modal fine-tuning.
To this extent, we introduce ColPali, a Paligemma-3B extension that is capable of generating ColBERT-style multi-vector representations of text and images (Figure 1).
PaliGemma-3B is a strong candidate due to its small size, the many released checkpoints fine-tuned for different image resolutions and tasks, and the promising performances on various document understanding benchmarks.
We add a projection layer to map each of the language model’s output token embeddings (whether from text or image tokens) to a vector space of reduced dimension $D=128$ as used in the ColBERT paper to keep lightweight bag-of-embedding representations.

**Late Interaction.**
Given query $q$ and document $d$, we denote as $\mathbf{E_{q}} \in \mathbb{R}^{{N_{q}} \times D}$ and $\mathbf{E_{d}} \in \mathbb{R}^{N_{d} \times D}$ their respective multi-vector representation in the common embedding space $\mathbb{R}^{D}$, where $N_{q}$ and $N_{d}$ are respectively the number of vectors in the query and in the document page embeddings. The late interaction operator, $\text{LI}\left(q,d\right)$, is the sum over all query vectors $\mathbf{E_{q}}^{(j)}$, of its maximum dot product $\langle\cdot|\cdot\rangle$ with each of the $N_{d}$ document embedding vectors $\mathbf{E_{d}}_{(1:N_{d})}$.

$$
\text{LI}\left(q,d\right)=\sum_{i\in[|1,N_{q}|]}\max_{j\in[|1,N_{d}|]}\langle \mathbf{E_{q}}^{(i)}|\mathbf{E_{d}}^{(j)}\rangle \quad (1)
$$

**Contrastive Loss.**
The Late Interaction operation is fully differentiable, enabling backpropagation.
Let a batch $\left\{q_{k},d_{k}\right\}_{k\in[|1,b|]}$ composed of $b$ query-page pairs, where for all $k\in[|1,b|]$, the document page $d_{k}$ is the document corresponding to query $q_{k}$.
Following, we define our in-batch contrastive loss $\mathcal{L}$ as the softmaxed cross-entropy of the positive scores $s_{k}^{+}=\text{LI}\left(q_{k},d_{k}\right)$ w.r.t. to the maximal in-batch negative scores $s_{k}^{-}=\max_{l,l\neq k}\hskip 8.53581pt\text{LI}\left(q_{k},d_{l}\right)$
[^6]: We reformulate the loss to leverage the numerically stable softplus function where $\texttt{softplus(x)}=\log\left(1+\exp\left(x\right)\right)$
:

$$
\mathcal{L}=-\frac{1}{b}\sum_{k=1}^{b}\log\left[\frac{\exp\left(s_{k}^{+} \right)}{\exp\left(s_{k}^{+}\right)+\exp\left(s_{k}^{-}\right)}\right]=\frac{1 }{b}\sum_{k=1}^{b}\log\left(1+\exp\left(s_{k}^{-}-s_{k}^{+}\right)\right) \quad (2)
$$

### 4.2 Model training

**Dataset.** Our training dataset of 118,695 query-page pairs is comprised of train sets of openly available academic datasets ($63\%$) and a synthetic dataset made up of pages from web-crawled PDF documents and augmented with VLM-generated (Claude-3 Sonnet) pseudo-questions ($37\%$). Dataset split details are given in Appendix A.3.
Our training set is fully English by design, enabling us to study zero-shot generalization to non-English languages.
[^7]: Multilingual data is present in the pretraining corpus of the language model (Gemma-2B) and potentially occurs during PaliGemma-3B’s multimodal training.
We explicitly verify no multi-page PDF document is used both ViDoRe and in the train set to prevent evaluation contamination. A validation set is created with $2\%$ of the samples to tune hyperparameters. We openly release the training dataset
[^8]: [https://huggingface.co/datasets/vidore/colpali_train_set](https://huggingface.co/datasets/vidore/colpali_train_set)
for reproducibility and to encourage further research.

**Parameters.** All models are trained for 1 epoch on the train set. Unless specified otherwise, we train models in bfloat16 format, use low-rank adapters (LoRA) with $\alpha=32$ and $r=32$ on the transformer layers from the language model, as well as the final randomly initialized projection layer, and use a paged_adamw_8bit optimizer. We train on an 8 GPU setup with data parallelism, a learning rate of $5e-5$ with linear decay with 2.5% warmup steps, and a batch size of 32.

**Query Augmentation.** As in, we append 5 `<unused0>` tokens to the query tokens to serve as a soft, differentiable query expansion or re-weighting mechanism.

## 5 Results

**Table 2: Comprehensive evaluation of baseline models and our proposed method on ViDoRe. Results are presented using nDCG@5 metrics, and illustrate the impact of different components. Text-only metrics are not computed for benchmarks with only visual elements.**

| | ArxivQ | DocQ | InfoQ | TabF | TATQ | Shift | AI | Energy | Gov. | Health. | Avg. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Unstructured text-only | | | | | | | | | | | |
| - BM25 | - | 34.1 | - | - | 44.0 | 59.6 | 90.4 | 78.3 | 78.8 | 82.6 | - |
| - BGE-M3 | - | 28.4$\downarrow$5.7 | - | - | 36.1$\downarrow$7.9 | 68.5$\uparrow$8.9 | 88.4$\downarrow$2.0 | 76.8$\downarrow$1.5 | 77.7$\downarrow$1.1 | 84.6$\uparrow$2.0 | - |
| Unstructured + OCR | | | | | | | | | | | |
| - BM25 | 31.6 | 36.8 | 62.9 | 46.5 | 62.7 | 64.3 | 92.8 | 85.9 | 83.9 | 87.2 | 65.5 |
| - BGE-M3 | 31.4$\downarrow$0.2 | 25.7$\downarrow$11.1 | 60.1$\downarrow$2.8 | 70.8$\uparrow$24.3 | 50.5$\downarrow$12.2 | 73.2$\uparrow$8.9 | 90.2$\downarrow$2.6 | 83.6$\downarrow$2.3 | 84.9$\uparrow$1.0 | 91.1$\uparrow$3.9 | 66.1$\uparrow$0.6 |
| Unstructured + Captioning | | | | | | | | | | | |
| - BM25 | 40.1 | 38.4 | 70.0 | 35.4 | 61.5 | 60.9 | 88.0 | 84.7 | 82.7 | 89.2 | 65.1 |
| - BGE-M3 | 35.7$\downarrow$4.4 | 32.9$\downarrow$5.4 | 71.9$\uparrow$1.9 | 69.1$\uparrow$33.7 | 43.8$\downarrow$17.7 | 73.1$\uparrow$12.2 | 88.8$\uparrow$0.8 | 83.3$\downarrow$1.4 | 80.4$\downarrow$2.3 | 91.3$\uparrow$2.1 | 67.0$\uparrow$1.9 |
| Contrastive VLMs | | | | | | | | | | | |
| Jina-CLIP | 25.4 | 11.9 | 35.5 | 20.2 | 3.3 | 3.8 | 15.2 | 19.7 | 21.4 | 20.8 | 17.7 |
| Nomic-vision | 17.1 | 10.7 | 30.1 | 16.3 | 2.7 | 1.1 | 12.9 | 10.9 | 11.4 | 15.7 | 12.9 |
| SigLIP (Vanilla) | 43.2 | 30.3 | 64.1 | 58.1 | 26.2 | 18.7 | 62.5 | 65.7 | 66.1 | 79.1 | 51.4 |
| Ours | | | | | | | | | | | |
| SigLIP (Vanilla) | 43.2 | 30.3 | 64.1 | 58.1 | 26.2 | 18.7 | 62.5 | 65.7 | 66.1 | 79.1 | 51.4 |
| BiSigLIP (+fine-tuning) | 58.5$\uparrow$15.3 | 32.9$\uparrow$2.6 | 70.5$\uparrow$6.4 | 62.7$\uparrow$4.6 | 30.5$\uparrow$4.3 | 26.5$\uparrow$7.8 | 74.3$\uparrow$11.8 | 73.7$\uparrow$8.0 | 74.2$\uparrow$8.1 | 82.3$\uparrow$3.2 | 58.6$\uparrow$7.2 |
| BiPali (+LLM) | 56.5$\downarrow$-2.0 | 30.0$\downarrow$-2.9 | 67.4$\downarrow$-3.1 | 76.9$\uparrow$14.2 | 33.4$\uparrow$2.9 | 43.7$\uparrow$17.2 | 71.2$\downarrow$-3.1 | 61.9$\downarrow$-11.7 | 73.8$\downarrow$-0.4 | 73.6$\downarrow$-8.8 | 58.8$\uparrow$0.2 |
| ColPali (+Late Inter.) | 79.1$\uparrow$22.6 | 54.4$\uparrow$24.5 | 81.8$\uparrow$14.4 | 83.9$\uparrow$7.0 | 65.8$\uparrow$32.4 | 73.2$\uparrow$29.5 | 96.2$\uparrow$25.0 | 91.0$\uparrow$29.1 | 92.7$\uparrow$18.9 | 94.4$\uparrow$20.8 | 81.3$\uparrow$22.5 |

### 5.1 Performance (R1)

We show performance is achieved iteratively through the combination of three factors; (1) a carefully crafted task-specific dataset, (2) pairing a pretrained LLM to a vision model to better leverage text semantics from the image, and (3) using multi-vector embeddings rather than a single vector representation to better capture the vast amount of visual information present in a document.

**Fine-tuning a Vision Model on a document retrieval oriented dataset: BiSigLIP.** SigLIP
[^9]: [https://huggingface.co/google/siglip-so400m-patch14-384](https://huggingface.co/google/siglip-so400m-patch14-384)
is a strong vision-language bi-encoder producing single vector embeddings, and pretrained on billions of image-text pairs from the English split of WebLI. Further fine-tuning the textual component of this model on our document-oriented dataset (BiSigLIP) yields clear improvements across the board, particularly on figure retrieval (ArxivQA) and table retrieval tasks (TabFQuAD).

**Feeding image patches to a LLM: BiPali.** In the PaliGemma model architecture, SigLIP-generated patch embeddings are fed to a text language model and we can obtain LLM contextualized output patch embeddings.
[^10]: Note that the SigLIP model used in PaliGemma slightly differs in terms of number patches - 1024 patches for PaliGemma’s vision encoder, and 729 for the standalone SigLIP model.
This technique aligns the image token representations with the text token embeddings in the LLM’s embeddings space, and augments the vision model embeddings with the language model’s text understanding capabilities. We average pool these representations to obtain a single dense vector, effectively creating a PaliGemma bi-encoder model (BiPali). After fine-tuning on the training dataset, we obtain a model that performs slightly worse in English than the tuned BiSigLIP variant.
[^11]: This can be explained by the fact that contrary to SigLIP, the original PaliGemma is not trained on contrastive matching tasks, but rather on next token prediction. Our contrastive fine-tuning phase on 119K images to transform PaliGemma into a bi-encoder is 5 orders of magnitude smaller than SigLIP’s original contrastive training.
However, we see notable improvements in French tasks, indicating that BiPali’s LLM (Gemma 2B) helps multilingual text understanding. This is particularly notable as our training dataset does not contain non-English samples.

**Leveraging Multi-Vector Embeddings through Late Interaction: ColPali.**
One benefit of inputting image patch embeddings through a language model is that they are natively mapped to a latent space similar to the textual input (query). This enables leveraging the ColBERT strategy to construct one embedding per image patch token, and at inference compute all interactions between text tokens and image patches, resulting in a step-change improvement in performance compared to BiPali.
Results in Table 2 show that our ColPali model also largely outperforms the strong baselines based on Unstructured and captioning, as well as all evaluated text-image embedding models. The difference is particularly stark on the more visually complex benchmark tasks, such as InfographicVQA, ArxivQA, and TabFQuAD, respectively representing infographics, figures, and tables. However, text-centric documents are also better retrieved by the ColPali models across all evaluated domains and languages, making our approach the overall best-performing document-retrieval model.

**Negative Results.** For extensiveness, we also train ColSigLIP, a late interaction variant of the BiSigLIP model but obtain abysmal performances. We attribute this to the large gaps w.r.t. SigLIP’s pre-training, in which only a pooled latent representation is used in the contrastive loss, which does not optimize the representations of individual patch and token embeddings. Similarly, we train a BiSigLIPPaliGemma variant, in which we retrieve the image representations from the SigLIP model that has been further updated by PaliGemma fine-tuning, and use the text representations from PaliGemma’s text model. After fine-tuning on our dataset, performance is severely inferior to SigLIPVanilla which simply encodes with SigLIP’s original text and vision components. This indicates a logical misalignment between SigLIP embeddings, and Gemma embeddings after PaliGemma training. We detail these results in Appendix C.1.

### 5.2 Latencies & Memory Footprint

**Online Querying.** (R2) Logically, querying latencies differ between ColPali and a BGE-M3 embedding model. For BGE, encoding takes about $22$ ms for 15 tokens, while encoding a query with ColPali’s language model takes about $30$ ms.
[^12]: Computed for a batch size of $1$ (online), and averaged over 1000 queries. See Appendix B.4.
For smaller corpus sizes, computing the late interaction operation induces marginally small overheads ($\approx 1$ ms per 1000 pages in the corpus), and the cosine similarity computation between bi-encoder vectors is even faster. Optimized late interaction engines enable to easily scale corpus sizes to millions of documents with reduced latency degradations.

**Offline Indexing.** (R3)
Standard retrieval methods using bi-encoders represent each chunk as a single vector embedding, which is easy to store and fast to compute. However, processing a PDF to get the different chunks is the most time-consuming part (layout detection, OCR, chunking), and using captioning to handle multimodal data will only exacerbate this already lengthy process. On the other hand, ColPali directly encodes pages from their image representation. Although the model is larger than standard retrieval encoders, skipping the preprocessing allows large speedups at indexing
[^13]: Measures a NVIDIA L4 GPU, averaged on 100 pages, with a batch size of 4 pages for ColPali and 8 text chunks for Bi-Encoders. On average, a page is divided into 2.1 chunks. See Appendix B.4.
(Figure 2). As pages are embedded end-to-end in single forward pass, the VRAM usage depends exclusively on the sequence length (number of patches per image) which is fixed as well, enabling efficient batching strategies to fully leverage hardware acceleration. ColPali also benefits from most LLM efficiency improvements introduced in the ecosystem such as Flash Attention.

**Storage Footprint.** Our method requires storing a vector per image patch, along with 6 extra text tokens “Describe the image” concatenated to image patches. We project each PaliGemma vector to a lower dimensional space ($D=128$) to maximize efficiency, leading to a memory footprint of $257.5$ KB per page (Appendix B.3). Importantly, the memory footprint of the naive ColBERT indexing strategy can be drastically improved through compression and clustering mechanisms.

**Token pooling.**
Token pooling is a CRUDE-compliant method (document addition/deletion-friendly) that aims to reduce the amount of multi-vector embeddings. For ColPali, many image patches share redundant information, e.g. white background patches. By pooling these patches together, we can reduce the amount of embeddings while retaining most information. Retrieval performance with hierarchical mean token pooling on image embeddings is shown in Figure 3 (left).
With a pool factor of 3, the total number of vectors is reduced by $66.7\%$ while $97.8\%$ of the original performance is maintained. We note that the Shift dataset—composed of the most text-dense documents—is a clear outlier, showcasing more information dense documents contain less redundant patches and may be prone to worse performance degradation with such pooling techniques.

### 5.3 Interpretability

Figure 3: (Left: Token Pooling) Relative performance degradation when reducing the number of stored embeddings per document. (Right: Interpretability) For each term in a user query, ColPali identifies the most relevant document image patches (highlighted zones) and computes a query-to-page matching score.
Image: x2.png

By superimposing the late interaction heatmap on top of the original image, we can visualize the most salient image patches with respect to each term of the query, yielding interpretable insights into model focus zones. As epitomized in Figure 3 (right), we observe ColPali exhibits strong OCR capabilities as both the words “hourly” and “hours” present a high similarity score with the query token `<_hour>`. We also note particular focus on other non-trivial image features such as the x-axis representing hours being salient. Other visualization examples are shown in Appendix D.

## 6 Ablation study

We run various ablations to better understand the mechanisms at play. By default, result deltas reported below refer to nDCG@5 values averaged over all ViDoRe tasks. Detailed results in Appendix C.2.

**Tradeoffs between model size and the number of image patches.** We train a variant of PaliGemma with half the number of image patches (512). While we observe a clear performance degradation with respects to the 1024-patch ColPali model ($-24.8$ nDCG@5), memory usage is much lower.
As an alternative to PaliGemma, we train Idefics2-8B, a VLM with a similar architecture and based on a Mistral-7B language backbone and a SigLIP vision encoder paired with a perceiver resampler. The most notable differences with PaliGemma lie in the size of the language model (2B and 7B resp.) and the number of image patches (between 512 and 2048 for PaliGemma, and 64 post-resampling for Idefics2
[^14]: With the option of adding 4 sub-image crops of 64 tokens each to the sequence, for a total of 320 tokens.
). Our results suggest better language models enable more efficient representations of image embeddings - ColIdefics2 with 64 patches largely outperforms out ColPali with 512 patches (+20.1 nDCG@5). However ColIdefics2 (64) remains less accurate than ColPali (1024) ($-4.7$ nDCG@5) while being about twice as slow in terms of training and inference latency.
These results suggest there are tradeoffs between performance (R1), latencies during online querying (R2) and offline indexation phases (R3), and index memory size.

**Unfreezing the vision component.** We train a ColPali variant by also backpropagating through and updating the vision encoder and the projection layer. This leads to a slight performance degradation ($-0.7$ nDCG@5). These conclusions may change with larger scales of training data.

**Impact of “query augmentation” tokens.** In ColBERT, special tokens are concatenated to the input query to serve as soft query augmentation buffers. Training without these tokens, we observe no significant performance difference in the English benchmarks. However, performance on the French tasks seems to improve ($+9.8$ nDCG@G on Shift, $+6.3$ nDCG@5 on TabFQuAD, Table 7).

**Impact of the Pairwise CE loss.** Training with an in-batch negative contrastive loss, instead of the pairwise CE loss that only considers the hardest negative sample, leads to a slight performance degradation ($-1.6$ nDCG@5) on the aggregated benchmark.

**Adapting models to new tasks.** Contrary to more complex multi-step retrieval pipelines, ColPali can be trained end-to-end, directly optimizing the downstream retrieval task which greatly facilitates fine-tuning to boost performance on specialized domains, multilingual retrieval, or specific visual elements the model struggles with. To demonstrate, we add 1552 samples representing French tables and associated queries to the training set. This represents the only French data in the training set, with all other examples being kept unchanged. We see clear nDCG@5 improvements ($+2.6$) and even starker Recall@1 gains ($+5$) on the TabFQuAD benchmark, with no performance degradation on the rest of the benchmark tasks ($+0.4$ nDCG@5 overall).

**Better VLMs lead to better visual retrievers.** As improved VLMs are released, it is interesting to observe if improved performances on generative tasks translate once these models are adapted for image retrieval tasks through ColPali training strategies. We train the recently released Qwen2-VL 2B, a SOTA 2 billion parameter generative VLM, with the same data and training strategy, obtaining ColQwen2-VL. To approximately match ColPali’s memory requirements, we limit the number of image patches to 768, slightly less than ColPali’s 1024 patches. We observe clear performance improvements of $+5.3$ nDCG@5 values over ColPali showcasing clear performance correlations between generative benchmarks performance and retrieving metrics.

**Out-of-domain generalization.** Some of the datasets in the ViDoRe benchmark have train sets, which we have integrated within the ColPali train set (eg. academic tasks). This is standard in embedding models, and while ColPali also exhibits strong performance on tasks in which this is not the case (French data is never seen by the model during training for instance), it remains interesting to evaluate model performance when training is done on a fully disjoint data distribution. We train a ColPali variant solely using the recent DocMatix dataset, a large scale, synthetically annotated visual document question answering dataset, which we subsample to obtain a comparably-sized train set. Results on ViDoRe show the performance drop is minor ($-2.2$ nDCG@5), still outperforming the closest baseline method by over 12 points. These results showcase
ColPali generalizes well outside of its training distribution, and demonstrate that our results are not unreasonably boosted with respect to baselines (BGE-M3) that cannot be fine-tuned on the same data.
[^15]: To train with data resembling the one BGE-M3 models would see at inference time would require running complex extraction pipelines for the more than 100K documents in the training set, notably relying on external proprietary captioning models which is both too costly and lengthy. This is not needed to train vision-based models.

## 7 Conclusions

In this work, we introduced the Visual Document Retrieval Benchmark (ViDoRe), which evaluates document retrieval systems in realistic settings involving visually complex documents. We demonstrated that current retrieval pipelines and contrastive vision-language models struggle to efficiently exploit visual information embedded in documents, leading to suboptimal performance. To address this, we presented ColPali, a novel retrieval method that leverages Vision-Language Models to create high-quality, multi-vector embeddings purely from visual document features. ColPali largely outperforms the best existing document retrieval methods while enabling faster corpus indexing times and maintaining low querying latencies, thus circumventing many pain points of modern document retrieval applications. We hope to drive industrial adoption, and to encourage future work by publicly releasing the ViDoRe benchmark, the data, the codebase, and all models and baselines from our work.

**Future Work.**
Beyond performance improvements that could be obtained through better data, backbone models or training strategies, our vision at term is to combine visual retrieval systems and visually grounded query answering to create end-to-end RAG systems that purely function from image features. This idea is supported by concurrent work showcasing the strong promises of VLMs for visual QA, and may eventually become a new industrial standard for document processing. In this line of work, reliability is key, and confidence estimation techniques for Information Retrieval methods could become central to implement abstention mechanisms, and are particularly interesting given the information rich multi-vector scoring mechanisms of late interaction systems.
Expanding benchmarking efforts to cover more languages, modalities, and tasks is also a crucial future research direction.

## Reproducibility Statement

For transparency, reproducibility and to foster future work, we release our training data, model checkpoints (adapters), entire codebase, and complete evaluation benchmark under MIT licenses as detailed in the main paper. We also host a public ViDoRe leaderboard
[^16]: [https://huggingface.co/spaces/vidore/vidore-leaderboard](https://huggingface.co/spaces/vidore/vidore-leaderboard)
to foster concurrent work in the space. The supplementary material further details training configurations for our models (also specified in HuggingFace model repositories), and dives into the process we used to generate synthetic data, how latency computations are performed, as well as provides further detailed evaluation results.

## Acknowledgements

This work is partially supported by Illuin Technology, and by a grant from ANRT France. This work was performed using HPC resources from the CINES ADASTRA through Grant 2024-AD011015443 and from IDRIS with grant 2024-AD011015724R1.
We extend our warm thanks to Jonathan Dong, Caio Corro, Victor Pellegrain and Ender Konukoglu for their valuable feedback on the paper.

## Appendix A Benchmark Datasets

### A.1 Academic Datasets

**DocVQA** includes collected images from the UCSF Industry Documents Library. Questions and answers were manually annotated.

**InfoVQA** includes infographics collected from the Internet using the search query “infographics”. Questions and answers were manually annotated.

**TAT-DQA** is a large-scale Document VQA dataset that was constructed from publicly available real-world financial reports. It focuses on rich tabular and textual content requiring numerical reasoning. Questions and answers were manually annotated by human experts in finance.

**arXivQA** is a VQA dataset based on figures extracted from arXiv publications. The questions were generated synthetically using GPT-4 Vision.

**TabFQuAD** (Table French Question Answering Dataset) is designed to evaluate TableQA models in realistic industry settings. We create additional queries to augment the existing human-annotated ones using the same method described in Appendix A.2.

### A.2 Practical Datasets

**Methodology.** Creating a relevant retrieval dataset close to real use cases is a major challenge as the dataset needs to be both sufficiently large for effective fine-tuning and sufficiently diverse to cover a broad range of modalities (full text, tables, charts, …), domains (industry, healthcare, …), and query-document interactions (extractive questions, open-ended questions, …). Our approach to building this dataset involves several steps: (1) we use a web crawler to collect publicly available documents on various themes and sources, (2) we convert these PDFs into a series of images, one per page, and (3) we generate queries related to each image using a VLM.

**Web-Crawler.** We implemented a web crawler to efficiently collect large volumes of documents related to a given topic. The crawler is seeded with a user-defined query (e.g. “artificial intelligence”) and then uses GPT-3.5 Turbo to brainstorm related topics and subtopics. This query augmentation strategy aims at both broadening and deepening the search. GPT-3.5 Turbo is further used to generate diverse search queries from each subtopic. This query set is then consumed by a pool of parallel workers whose job is to fetch the associated most relevant documents. We use SerpAPI
[^17]: [https://serpapi.com/](https://serpapi.com/)
along with a filetype filter (PDF documents only) to programmatically scrape Google Search rankings. Each file is hashed and stored in a Bloom filter shared among workers to avoid duplicate documents in the final corpus. Unique scraped files are downloaded, and inserted into a SQLite database along with additional metadata.

**Datamix.** Using the web crawler, we collected approximately 100 documents for each of the following four seeds: “energy”, “government reports”, “healthcare industry”, and “artificial intelligence”. These seeds were meticulously hand-picked to align with real-use cases for retrieval models and visually rich pages. We also removed all documents containing any private information.

**Query Generation.** To increase the efficiency of our query generation scheme and to limit API calls, we generate at most 3 questions per image. From all the documents collected, we randomly sample 10,000 images per theme and call Claude-3 Sonnet with the following prompt:

**Human Validation.** We manually validate every single synthetically created query in ViDoRe to ensure quality, query relevance, and consistency with the benchmark objective of evaluating retrieval in practical industrial settings. During this step, we randomly assign document-pair queries to 4 volunteer annotators and instruct them to filter out queries that do not fit the above-listed criteria. We also instruct annotators to flag any documents they deem to contain PII information or content not suited for an academic benchmark. No flag was raised during the entirety of the process, validating our prior PDF collection strategy. 100 queries per topic are collected in this manner. Annotators are colleagues and collaborators of the authors who volunteered to help. Each annotator spent approximately 3 hours filtering the larger query set down to 100 high-quality queries per topic.

### A.3 Training Dataset

The statistics of the train set are given in the following table. The creation of the train set follows the same methodology as in Appendix A.2. We made sure that a PDF document cannot have pages in both the training set and the test set to prevent data leakage and that there are no duplicate documents in each split.

**Table 3: Details on the different splits in the dataset used to train ColPali.**

| Dataset Split | Split Size | Language | Domain |
|---|---|---|---|
| DocVQA | 39,463 | English | Scanned documents from UCSF Industry |
| InfoVQA | 10,074 | English | Infographics scrapped from the web |
| TATDQA | 13,251 | English | High-quality financial reports |
| arXivQA | 10,000 | English | Scientific Figures from arXiv |
| Scrapped PDFs | 45,940 | English | Varied PDFs from 3885 distinct URL domains |
| TOTAL | 118,695 | English-only | Mixed |

## Appendix B Implementation details

### B.1 Codebase

The codebase is written in PyTorch
[^18]: [https://pytorch.org/](https://pytorch.org/)
and leverages HuggingFace tooling for model implementations and trainers.
[^19]: [https://huggingface.co](https://huggingface.co)

### B.2 Hyperparameters

Hyperparameters are tuned on a validation split composed of $2\%$ of the training dataset. We find bi-encoder methods to be more sensible to learning rate variations than late interaction-based models and achieve the best performance for all models with a learning rate of $5e-5$. We experiment with LoRA rank and $\alpha$ values and do not notice particular improvements past $r=\alpha=32$. Per-device batch sizes are kept small due to long sequence lengths that complicate scaling past $b=4$. We simulate larger batch sizes with multi-GPU training and train with a total batch size $b=32$ with no accumulation, for 1 epoch on our training set.

### B.3 Embedding size

Minimizing storage footprint can be essential to industrial retrieval systems if databases contain millions of documents. With this criterion in view, we have compared the embedding sizes of the models in our study. As shown in Table 4, ColPali’s embedding size is an order of magnitude larger than BM25 and two orders of magnitude larger than BGE-M3. However, in practical scenarios, pooling multi-vector embeddings by centroid cluster, or quantizing embeddings to binary representations
[^20]: [https://blog.vespa.ai/scaling-colpali-to-billions/](https://blog.vespa.ai/scaling-colpali-to-billions/)
can reduce storage costs by two orders of magnitude with minimal performance hits, and make storage costs competitive with other systems.

**Table 4: Comparison of the embedding sizes for the DocVQA test set from ViDoRe w.r.t. different retrieval models. The mean ± std size is given for the sparse embeddings. In general multiple vectors (2-5) per page are used for BGE-M3 and BM25.**

| Model | Embedding size (KB) |
|---|---|
| BGE-M3 | 8.60 |
| BM25 (dense emb.) | 3.00 |
| BM25 (sparse emb.) | 1.56 ± 0.51 |
| ColPali (float16) | 257.5 |

### B.4 Latency computations

To ensure comparison fairness, the latencies of the different retrieval systems shown in Figure 2 are measured on the same g2-standard-8 GCP VM with a NVIDIA L4 GPU. Document pages are embedded using the highest settings of Unstructured with captioning (see subsection 3.2). SigLIP and ColPali are both loaded with bfloat16 parameter dtypes. The reported times in Table 5 are the average per-page latencies for each indexing operation on 1000 randomly chosen documents across all splits of the ViDoRe benchmark test set. A batch size of $8$ was used for the BGE-M3 model used with Unstructured, and a batch size of $4$ was used for SigLIP and ColPali.

**Table 5: Page-level latencies for document indexing using various retrieval systems. SigLIP and ColPali are much faster than Unstructured because they don’t require the layout detection, OCR, and captioning operations.**

| Indexing operation | Latency (s) | | |
|---|---|---|---|
| Unstructured | SigLIP | ColPali | |
| Layout detection | 0.81 | NA | NA |
| OCR | 2.67 | NA | NA |
| Captioning | 3.71 | NA | NA |
| Page encoding | 0.03 | 0.12 | 0.39 |
| Total | 7.22 | 0.12 | 0.39 |

### B.5 Captioning

Examples of captions generated for visually rich document chunks with Claude-3 Sonnet are shown in Figure 5 and Figure 4. The prompt used for generating the description is the following:

Figure 4: Example from the “Energy” test set. Caption: The image depicts the hourly energy generation profile, illustrating the contributions of various energy sources over 24 hours. The data is presented as a stacked bar chart, with the x-axis representing the hours of the day from 1 to 2, and the y-axis showing the average hourly generation in MW. The bars are segmented into different colors, each representing a distinct energy source: nuclear, bio, geothermal, solar, wind, hydro, natural gas, and other imports. The chart provides insights into the temporal variations in energy generation across different sources, highlighting the interplay between baseload and intermittent sources throughout the day.
Image: x3.png

Figure 5: Example from the “Government Reports” test set. Caption: The image shows a table titled “System of Record” which outlines the different types of documents or records maintained across various systems or departments within an organization related to project management and construction. The rows list documents like project plans, budgets, schedules, contracts, purchase orders, invoices, change requests, bid submissions, drawings, manuals, meeting minutes, and reports. The columns indicate the system or department responsible for maintaining each record, such as County Servers, Project View, OnBase, CGI Advantage Financial System, and Purchasing Department. The table uses ”W” and ”T” markers to denote which system or department serves as the primary source (writer) or storage location (trailer) for each type of document.
Image: x4.png

## Appendix C Additional results

### C.1 Other Metrics

**Table 6: Comprehensive evaluation of baseline models and our proposed method on ViDoRe. Results are presented using Recall@1 metrics. Text-only metrics are not computed for benchmarks with only visual elements.**

| | ArxivQ | DocQ | InfoQ | TabF | TATQ | Shift | AI | Energy | Gov. | Health. | Avg. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Unstructured text-only | | | | | | | | | | | |
| BM25 | - | 26.6 | - | - | 34.6 | 45.0 | 86.0 | 70.0 | 68.0 | 74.0 | - |
| BGE-M3 | - | 22.8$\downarrow$3.8 | - | - | 26.1$\downarrow$8.5 | 51.0$\uparrow$6.0 | 81.0$\downarrow$5.0 | 72.0$\uparrow$2.0 | 67.0$\downarrow$1.0 | 77.0$\uparrow$3.0 | - |
| Unstructured + OCR | | | | | | | | | | | |
| BM25 | 26.7 | 28.9 | 54.0 | 30.4 | 50.0 | 52.0 | 86.0 | 77.0 | 74.0 | 80.0 | 55.9 |
| BGE-M3 | 28.1$\uparrow$1.4 | 22.9$\downarrow$6.0 | 53.8$\downarrow$0.2 | 55.7$\uparrow$25.3 | 38.6$\downarrow$11.4 | 56.0$\uparrow$4.0 | 82.0$\downarrow$4.0 | 79.0$\uparrow$2.0 | 76.0$\uparrow$2.0 | 83.0$\uparrow$3.0 | 57.5$\uparrow$1.6 |
| Unstructured + Captioning | | | | | | | | | | | |
| BM25 | 35.5 | 30.2 | 61.5 | 24.3 | 49.0 | 47.0 | 79.0 | 76.0 | 75.0 | 81.0 | 55.9 |
| BGE-M3 | 29.3$\downarrow$6.2 | 26.0$\downarrow$4.2 | 62.1$\uparrow$0.6 | 58.6$\uparrow$34.3 | 30.6$\downarrow$18.4 | 55.0$\uparrow$8.0 | 80.0$\uparrow$1.0 | 78.0$\uparrow$2.0 | 69.0$\downarrow$6.0 | 83.0$\uparrow$2.0 | 57.2$\uparrow$1.3 |
| Contrastive VLMs | | | | | | | | | | | |
| Jina-CLIP | 19.4 | 7.3 | 26.7 | 12.5 | 1.6 | 2.0 | 11.0 | 13.0 | 15.0 | 17.0 | 12.6 |
| Nomic-vision | 10.4 | 6.7 | 22.1 | 9.6 | 1.6 | 0.0 | 9.0 | 9.0 | 7.0 | 13.0 | 8.8 |
| SigLIP (Vanilla) | 34.2 | 21.3 | 51.8 | 46.1 | 17.9 | 13.0 | 50.0 | 51.0 | 47.0 | 65.0 | 39.7 |
| Ours | | | | | | | | | | | |
| SigLIP (Vanilla) | 34.2 | 21.3 | 51.8 | 46.1 | 17.9 | 13.0 | 50.0 | 51.0 | 47.0 | 65.0 | 39.7 |
| BiSigLIP (+fine-tuning) | 49.2$\uparrow$15.0 | 23.8$\uparrow$2.5 | 59.0$\uparrow$7.2 | 52.1$\uparrow$6.0 | 20.7$\uparrow$2.8 | 16.0$\uparrow$3.0 | 62.0$\uparrow$12.0 | 61.0$\uparrow$10.0 | 55.0$\uparrow$8.0 | 72.0$\uparrow$7.0 | 47.1$\uparrow$7.4 |
| BiPali (+LLM) | 46.4$\downarrow$-2.8 | 20.0$\downarrow$-3.8 | 54.6$\downarrow$-4.4 | 63.2$\uparrow$11.1 | 20.4$\downarrow$-0.4 | 34.0$\uparrow$18.0 | 59.0$\downarrow$-3.0 | 45.0$\downarrow$-16.0 | 57.0$\uparrow$2.0 | 56.0$\downarrow$-16.0 | 45.6$\downarrow$-1.5 |
| ColPali (+Late Inter.) | 72.4$\uparrow$26.0 | 45.6$\uparrow$25.6 | 74.6$\uparrow$20.0 | 75.4$\uparrow$12.1 | 53.1$\uparrow$32.7 | 55.0$\uparrow$21.0 | 93.0$\uparrow$34.0 | 85.0$\uparrow$40.0 | 85.0$\uparrow$28.0 | 88.0$\uparrow$32.0 | 72.7$\uparrow$27.1 |

### C.2 Model Variants

**Table 7: Benchmark scores for the “negative results” and various ablations on ViDoRe; ColPali for reference. Results are presented using nDCG@5 metrics. Text-only metrics are not computed for benchmarks with only visual elements.**

| | ArxivQ | DocQ | InfoQ | TabF | TATQ | Shift | AI | Energy | Gov. | Health. | Avg. |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ColSigLIP (PaliGemma) | 3.1 | 3.0 | 5.1 | 6.2 | 2.5 | 1.0 | 3.4 | 3.4 | 2.3 | 2.2 | 3.2 |
| BiSigLIP (PaliGemma) | 18.5 | 14.6 | 33.4 | 39.5 | 16.1 | 5.2 | 27.6 | 32.6 | 36.6 | 35.7 | 26.0 |
| ColSigLIP (Original) | 2.6 | 2.2 | 2.3 | 5.7 | 1.8 | 1.0 | 2.6 | 4.1 | 1.4 | 1.5 | 2.5 |
| ColPali (No Q.A. Tokens) | 80.4 | 53.2 | 82.4 | 77.4 | 65.7 | 63.4 | 97.0 | 89.9 | 93.6 | 92.4 | 79.6 |
| ColPali (Docmatix) | 71.3 | 48.0 | 80.0 | 83.9 | 59.1 | 73.8 | 95.7 | 93.8 | 92.5 | 93.1 | 79.1 |
| ColPali (224) | 71.0 | 37.4 | 62.3 | 65.7 | 28.6 | 20.4 | 65.7 | 66.8 | 73.9 | 73.0 | 56.5 |
| ColPali (Vision Trained) | 78.8 | 53.9 | 81.3 | 81.7 | 64.4 | 70.6 | 95.3 | 91.7 | 93.5 | 94.7 | 80.6 |
| ColPali (No Pairwise) | 79.0 | 53.0 | 82.1 | 85.3 | 63.2 | 66.2 | 94.9 | 88.9 | 92.7 | 92.1 | 79.7 |
| ColPali (+TabFQuAD training) | 77.6 | 54.7 | 82.6 | 86.5 | 65.4 | 73.9 | 94.8 | 92.4 | 94.2 | 94.8 | 81.7 |
| ColIdefics2 (64) | 73.6 | 48.0 | 82.4 | 81.6 | 63.0 | 57.2 | 95.5 | 86.9 | 86.6 | 91.2 | 76.6 |
| ColQwen2 (768) | 86.4 | 56.2 | 89.8 | 88.7 | 75.2 | 85.7 | 98.8 | 94.8 | 93.6 | 97.3 | 86.6 |
| ColPali (Reference: 448) | 79.1 | 54.4 | 81.8 | 83.9 | 65.8 | 73.2 | 96.2 | 91.0 | 92.7 | 94.4 | 81.3 |

## Appendix D More similarity maps

In Figure 6, ColPali assigns a high similarity to all patches with the word “Kazakhstan” when given the token `<_Kazakhstan>`. Moreover, our model seems to exhibit world knowledge capabilities as the patch around the word ”Kashagan”—an offshore oil field in Kazakhstan—also shows a high similarity score.

Figure 6: Similarity of the image patches w.r.t. the underlined token in the user query. This example is from the Shift test set.
Image: extracted/6240861/images/similarity_maps/similarity_map_kazakhstan.png

It is also interesting to highlight that both this similarity map and the one displayed in Figure 3 (right) showcase a few white patches with high similarity scores. This behavior might first seem surprising as the white patches should not carry a meaningful signal from the original images. We believe the vectors associated with these patches share a similar role with the ViT registers, i.e. these patches were repurposed for internal computations and stored the global information from the whole image.

## Appendix E Model glossary

### SigLIP

SigLIP (Sigmoid Loss for Language Image Pre-Training) builds upon CLIP (Contrastive Language-Image Pretraining)—a foundational model that aligns images and text by maximizing the similarity between correct image-text pairs while minimizing it for incorrect ones, leveraging a contrastive loss. Unlike CLIP, which applies the softmax function to the logits, SigLIP uses the sigmoid activation function. This innovation eliminates the need for a global view of all pairwise similarities between images and texts within a batch, enabling more flexible batch size scaling (up to 1M items per batch, with an effective optimal batch size of 32k). This approach allows SigLIP to achieve state-of-the-art performance in zero-shot image classification tasks.

### PaliGemma

PaliGemma is a 3B-parameter vision-language model. It integrates the SigLIP vision encoder with a Gemma-2B language decoder, connected via a multimodal linear projection layer. The model processes images by segmenting them into a fixed number of Vision Transformer tokens, which are prepended to an optional text prompt.

A distinguishing feature of PaliGemma is its operation as a Prefix-Language Model (Prefix-LM). This design ensures full attention between image tokens and the user-provided input (prefix) while generating outputs auto-regressively (suffix). This architecture allows image tokens to access the task-specific query during processing, facilitating more effective task-dependent reasoning.

PaliGemma was trained in four stages: unimodal pretraining with existing components, extended multimodal pretraining, short high-resolution pretraining, and task-specific fine-tuning.

### ColBERT

ColBERT (Contextualized Late Interaction over BERT) is a retrieval model designed to balance speed and effectiveness in information retrieval tasks. Traditional retrieval models are typically categorized based on their type of interaction: either processing queries and documents independently for efficiency (bi-encoders) or jointly to capture rich contextual relationships (cross-encoders). ColBERT combines the advantages of both approaches through a novel late interaction mechanism.

Queries and documents are encoded separately using BERT, enabling offline pre-computation of document representations for scalability. Instead of pooling embeddings into a single vector, ColBERT retains token-level embeddings and employs a MaxSim operator to compute fine-grained similarity scores. For each query token, the model determines the maximum similarity with document tokens, summing these scores to compute relevance.

This architecture preserves the contextual richness of deep language models while significantly improving computational efficiency. By delaying the interaction step, ColBERT supports vector similarity indexing, facilitating end-to-end retrieval from large collections without prohibitive costs. Empirical evaluations on passage search datasets demonstrate that ColBERT achieves competitive effectiveness compared to existing BERT-based models, while executing queries orders of magnitude faster and with drastically reduced computational requirements.

## Appendix F Examples from the ViDoRe benchmark

**Energy**

Figure: Query: What types of accounts or products allow investors to defer paying taxes?
Image: extracted/6240861/images/dataset_samples/energy_1.jpeg

**Artificial Intelligence**

Figure: Query: What are some common outcome areas targeted by TAII for different age groups?
Image: extracted/6240861/images/dataset_samples/ai_1.jpeg

**Healthcare Industry**

Figure: Query: What is the chemical formula for the ferroelectric material Lead Zirconium Titanate (PZT)?
Image: extracted/6240861/images/dataset_samples/healthcare_1.jpeg

**Government Reports**

Figure: Query: What are some mandates for the EPA under the Pollution Prevention Act?
Image: extracted/6240861/images/dataset_samples/gov_1.jpeg

**Shift**

Figure: Query: Selon le graphique, quelle est la capacité d’import et la consommation réelle de carburants SAF (biocarburants durables pour l’aviation) prévues en 2050 ?
Image: extracted/6240861/images/dataset_samples/shift_1.jpeg

</details>

<details>
<summary>Multi-modal ML with OpenAI's CLIP</summary>

# Multi-modal ML with OpenAI's CLIP

**Source URL:** <https://www.pinecone.io/learn/series/image-search/clip/>

* * *

Language models (LMs) can not rely on language alone. That is the idea behind the “Experience Grounds Language” paper, that proposes a framework to measure LMs' current and future progress. A key idea is that, beyond a certain threshold LMs need other forms of data, such as visual input \[1\] \[2\].

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2F25e7f2f54b543af8c34c143448a4b0c55f77c6b5-2360x854.png&w=3840&q=75

World Scopes (WS), as datasets become larger in scope and span multiple modalities, the capabilities of models trained with them increase.

The next step beyond well-known language models; BERT, GPT-3, and T5 is _”World Scope 3”_. In World Scope 3, we move from large text-only datasets to large multi-modal datasets. That is, datasets containing information from multiple forms of media, like _both_ images and text.

The world, both digital and real, is multi-modal. We perceive the world as an orchestra of language, imagery, video, smell, touch, and more. This chaotic ensemble produces an inner state, our “model” of the outside world.

AI must move in the same direction. Even specialist models that focus on language or vision must, at some point, have input from the other modalities. How can a model fully understand the concept of the word “person” without _seeing_ a person?

OpenAI **C** ontrastive **L** earning **I** n **P** retraining (CLIP) is a world scope three model. It can comprehend concepts in both text and image and even connect concepts between the two modalities. In this chapter we will learn about multi-modality, how CLIP works, and how to use CLIP for different use cases like encoding, classification, and object detection.

* * *

## Multi-modality

The multi-modal nature of CLIP is powered by two encoder models trained to “speak the same language”. Text inputs are passed to a text encoder, and image inputs to an image encoder \[3\]. These models then create a _vector representation_ of the respective input.

Both models “speak the same language” by encoding similar concepts in text and images into similar vectors. That means that the text “two dogs running across a frosty field” would output a vector similar to an _image_ of two dogs running across a frosty field.

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fa54a2f1fa0aeac03748c09df0fdfbb42aadc96b7-2430x1278.png&w=3840&q=75

Similar text and images will be encoded into a similar vector space. Dissimilar text and images do not share a similar vector space.

We can think of the language these models speak as the vector space in which they encode vectors. These two models can express nuanced information about text and images through this vector space. However, this “vector language” is far too abstract for us to directly understand.

Rather than directly reading this “language”, we can train other simple neural networks to understand it and make predictions that we can understand. Or we use vector search to identify similar concepts and patterns across text and image domains.

Let’s take a look at an example of CLIP in action.

### Text-to-Image Search

Entering a prompt in the search bar above allows us to search through images based on their _content_ rather than any attached textual metadata. We call this **C** ontent **B** ased **I** mage **R** etrieval (CBIR).

With CBIR, we can search for specific phrases such as “two dogs running across a frosty field”. We can even drop the word “dogs” and replace it with everyday slang for dogs like “good boy” or “mans best friend”, and we return the same images showing dogs running across fields.

CLIP can accurately understand language. It understands that _in the context_ of running across a field, we are likely referring to dogs and do not literally mean good children or someone’s “human” best friend.

Amusingly, the dataset contains no images of the food hot dogs (other than one). So, suppose we search for “hot dogs”. In that case, we first get an image containing a hot dog (and a dog), a dog looking toasty in a warm room, another dog looking warm with wooly clothing, and another dog posing for the camera. All of these portray a hot dog in one sense or another.

* * *

_After being processed by CLIP’s text or image encoder, we are left with vectors. That means we can search across_ **_any_** _modality with_ **_any_** _modality; we can search in either direction. We can also stick to a single modality, like text-to-text or image-to-image._

* * *

Now that we’ve seen what CLIP can do, let’s take a look at _how_ it can do this.

## CLIP

CLIP actually consists of two models trained in parallel. A 12-layer text transformer for building text embeddings and a ResNet or vision transformer (ViT) for building image embeddings \[3\].

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2F539716ea1571e459908c1fdc5a898fea239d8243-2803x1672.png&w=3840&q=75

Architecture diagram of CLIP with the text encoder and ViT or ResNet as the image encoder.

The text encoder and image encoder (ResNet _or_ ViT) output single vector embeddings for each text/image record fed into the encoders. All vectors are 512 dimensional and can be represented in the same vector space, meaning similar images and text produce vectors that appear near each other.

### Contrastive Pretraining

Across both [**N** atural](https://www.pinecone.io/learn/series/nlp/) [**L** anguage](https://www.pinecone.io/learn/series/nlp/) [**P** rocessing (NLP)](https://www.pinecone.io/learn/series/nlp/) and computer vision (CV), large pretrained models dominate the SotA. The idea is that by giving a big model a lot of data, they can learn general patterns from the dataset.

For language models, that may be the general rules and patterns in the English language. For vision models, that may be the characteristics of different scenes or objects.

The problem with multi-modality is that these models are trained separately and, by default, have no understanding of one another. CLIP solves this thanks to image-text _contrastive pretraining_. With CLIP, text and image encoders are trained while considering the other modality and context. Meaning that the text and image encoders share an “indirect understanding” of patterns in both modalities; language and vision.

Contrastive pretraining works by taking a _(text, image)_ pair – where the text describes the image – and learning to encode the pairs as closely as possible in vector space.

For this to work well, we also need negative pairs to provide a contrastive comparison. We need positive pairs that should output similar vectors and negative pairs that should output dissimilar vectors.

This is the general idea behind contrastive learning, which can be found in the training functions of many models, particularly those that produce embedding vectors.

The negative pairs can be extracted directly from positive pairs. If we have positive pairs (T1,I1)(T\_1,I\_1)(T1​,I1​) and (T2,I2)(T\_2,I\_2)(T2​,I2​), we simply swap the components, giving us the negative pairs (T1,I2)(T\_1,I\_2)(T1​,I2​) and (T2,I1)(T\_2,I\_1)(T2​,I1​).

With this, we can apply a loss function that maximizes the similarity between (T1,I1)(T\_1,I\_1)(T1​,I1​) and (T2,I2)(T\_2,I\_2)(T2​,I2​), and minimizes the similarity between (T1,I2)(T\_1,I\_2)(T1​,I2​) and (T2,I1)(T\_2,I\_1)(T2​,I1​). Altogether, this looks like this:

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fd6868e6dae721512fed8f1287fc9ffe6b6a2cddd-2332x1342.png&w=3840&q=75

Contrastive pretraining with CLIP.

In this image, we can see a single pretraining step on a single batch. The loss function assumes pairs in the diagonal should have a maximized dot product score, and all other pairs should have a minimized dot product score. Both text and image encoder models are optimized for this.

A fundamental assumption is that there are no other positive pairs within a single batch. For example, we assume that “two dogs running across a frosty field” is only relevant to the image it is paired with. We assume there are no other texts or images with similar meanings.

This assumption is possible because the datasets used for pretraining are diverse and large enough that the likelihood of two similar pairs appearing in a single batch is negligible. Therefore, rare enough to have a little-to-no negative impact on pretraining performance.

## Using CLIP

We have a good idea of what CLIP can be used for and how it is trained. With that, how can we get started with it?

OpenAI released a few implementations of CLIP via the Hugging Face library; this is the fastest way to get started. First, we need to install the necessary libraries.

`pip install transformers torch datasets`

Before we can do anything with CLIP, we need some text and images. The `jamescalam/image-text-demo` dataset contains a small number of image-text pairs we can use in our examples.

```python

```

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fa40f673ed52e07f497c7a39b032c27b33ce9f565-1128x761.png&w=3840&q=75

Example of text-image pair found in the dataset. Text is stored in the "text" feature and images in the "image" feature.

With these sample records ready, we can move on to initializing CLIP and an image/text preprocessor like so:

```python

```

The `model` is CLIP itself. Note that we use the ViT image encoder (the model is `clip-vit`). Text and image data cannot be fed directly into CLIP. The text must be preprocessed to create “tokens IDs”, and images must be resized and normalized. The `processor` handles both of these functions.

### Encoding Text

We will start with encoding text using the CLIP text transformer. Before feeding text into CLIP, it must be preprocessed and converted into token IDs. Let’s take a batch of sentences from the `unsplash` data and encode them.

In\[5\]:

```python

```

Out\[5\]:

```
dict_keys(['input_ids', 'attention_mask'])
```

This returns the typical text transformer inputs of `input_ids` and `attention_mask`.

The `input_ids` are token ID values where each token ID is an integer value ID that maps to a specific word or sub-word. For example the phrase _“multi-modality”_ may be split into tokens _\[“multi”, “-”, “modal”, “ity”\]_, which are then mapped to IDs _\[1021, 110, 2427, 425\]_.

A text transformer maps these token IDs to semantic vector embeddings that the model learned during pretraining.

The `attention_mask` is a tensor of 1s and 0s used by the model’s internal mechanisms to “pay attention” to real token IDs and ignore padding tokens.

* * *

_Padding tokens are a special type of token used by text transformers to create input sequences of a fixed length from sentences of varying length. They are appended to the end of shorter sentences, so “hello world” may become “hello world \[PAD\] \[PAD\] \[PAD\]”._

* * *

We then use CLIP to encode all of these text descriptions with `get_text_features` like so:

```python

```

One important thing to note here is that these embeddings are _not_ normalized. If we plan on using a similarity metric like the dot product, we must normalize the embeddings:

In\[9\]:

```python

```

Out\[9\]:

```
torch.Size([21, 512])
tensor(-1.1893, grad_fn=<MinBackward1>) tensor(4.8015, grad_fn=<MaxBackward1>)
```

In\[40\]:

```python

```

Out\[40\]:

```
(21,)
```

In\[41\]:

```python

```

Out\[41\]:

```
(21, 512)
-0.1526844 0.53449875
```

Alternatively, we can use cosine similarity as our metric as this only considers angular similarity and not vector magnitude (like dot product). For our examples, we will normalize and use dot product similarity.

We now have our text embeddings; let’s see how to do the same for images.

### Encoding Images

Images will be encoded using the ViT portion of CLIP. Similar to text encoding, we need to preprocess these images using the `preprocessor` like so:

In\[42\]:

```python

```

Out\[42\]:

```
(6000, 3376)
```

In\[43\]:

```python

```

Out\[43\]:

```
torch.Size([21, 3, 224, 224])
```

Preprocessing images does _not_ produce token IDs like those we saw from preprocessing our text. Instead, preprocessing images consists of resizing the image to a 244x244 array with three color channels (red, green, and blue) and normalizing pixel values into a \[0,1\]\[0,1\] range.

After preprocessing our images, we get the image features with `get_image_features` and normalize them as before:

In\[44\]:

```python

```

Out\[44\]:

```
torch.Size([21, 512])
tensor(-8.6533, grad_fn=<MinBackward1>) tensor(2.6551, grad_fn=<MaxBackward1>)
```

In\[45\]:

```python

```

Out\[45\]:

```
(21, 512)
-0.7275361 0.23383287
```

With this, we have created CLIP embeddings for both text and images. We can move on to comparing items across the two modalities.

### Calculating Similarity

CLIP embedding similarities are represented by their angular similarity. Meaning we can identify similar pairs using cosine similarity:

cossim(A,B)=A⋅B∣∣A∣∣∗∣∣B∣∣=∑inAiBi∑inAi2∑inBi2cossim(A, B) = \\frac{A \\cdot B}{\|\|A\|\| \* \|\|B\|\|} = \\frac{\\sum\_i^nA\_iB\_i}{\\sqrt{\\sum\_i^nA\_i^2} \\sqrt{\\sum\_i^nB\_i^2}}cossim(A,B)=∣∣A∣∣∗∣∣B∣∣A⋅B​=∑in​Ai2​​∑in​Bi2​​∑in​Ai​Bi​​

Or, if we have normalized the embeddings, we can use dot product similarity:

dotproduct(A,B)=A⋅B=∑i=0n−1AiBidotproduct(A, B) = A \\cdot B = \\sum\_{i=0}^{n-1}A\_iB\_idotproduct(A,B)=A⋅B=i=0∑n−1​Ai​Bi​

Let’s try both. First, for cosine similarity, we do:

In\[46\]:

```python

```

Out\[46\]:

```
(21, 21)
```

In\[47\]:

```python

```

Out\[47\]:

```
<Figure size 432x288 with 1 Axes>
```

And if we perform the same operation for dot product similarity, we should return the same results:

In\[48\]:

```python

```

Out\[48\]:

```
<Figure size 432x288 with 1 Axes>
```

Both of these similarity score arrays look the same, and if we check for the difference between the two arrays, we will see that the scores are the same. We see some slight differences due to floating point errors.

In\[51\]:

```python

```

Out\[51\]:

```
(0.0, 2.9802322e-08)
```

Using the embedding functions of CLIP in this way, we can perform a semantic search across the modalities of text and image in any direction. We can search for images with text, text with images, text with text, and images with images.

These use cases are great, but we can make slight modifications to this for many other tasks.

### Classification

One of the most impressive demonstrations of CLIP is its unparalleled zero-shot performance on various tasks. For example, given the `fragment/imagenette` dataset from Hugging Face _Datasets_, we can write a list of brief sentences that align with the ten class labels.

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Ff841984e7617686f5041ca95797498e2b0b085b5-1348x542.png&w=3840&q=75

We take the original imagenette labels and preappend "a photo of a ..." to each to create a set of CLIP-friendly sentence representations.

From this, we can calculate the cosine similarity between the text embeddings of these ten labels against an image we’d like to classify. The text that returns the highest similarity is our predicted class.

### Object Detection

Another compelling use case of zero-shot CLIP is object detection. We can do this by splitting our images into smaller patches and running each patch through the image encoder of CLIP. We then compare these patch embeddings to a text encoding describing what we are looking for. After calculating the similarity scores for all patches, we can collate them into a map of relevance.

For example, given an image of a butterfly and a cat, we could break it into many small patches. Given the prompt `"a fluffy cat"`, we will return an outline of the cat, whereas the prompt `"a butterfly"` will produce an outline of the butterfly.

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fbe4800918976efd9d974d9e5453985a5106f2558-2389x1455.png&w=3840&q=75

Zero-shot object detection with CLIP allows us to find specific objects with natural language prompts.

These are only a few of the use cases of CLIP and only scratch the surface of what is possible with this model and others in the scope of multi-modal ML.

* * *

That’s it for this introduction to multi-modal ML with OpenAI’s CLIP. The past years since the CLIP release have seen ever more fascinating applications of the model.

DALL-E 2 is a well-known example of CLIP. The incredible images generated by DALL-E 2 start by embedding the user’s text prompt with CLIP \[4\]. That text embedding is then passed to the diffusion model, which generates some mind-blowing images.

The fields of NLP and CV have mainly progressed independently of each other for the past decade. However, with the introduction of world scope three models, they’re becoming more entwined into a majestic multi-modal field of Machine Learning.

## Resources

\[1\] Y. Bisk et al., [Experience Grounds Language](https://arxiv.org/abs/2004.10151) (2020), EMNLP

\[2\] J. Alammar, [Experience Grounds Language: Improving language models beyond the world of text](https://www.youtube.com/watch?v=WQm7-X4gts4) (2022), YouTube

\[3\] A. Radford et al., [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020) (2021), arXiv

\[4\] A. Ramesh, P. Dhariwal, A. Nichol, C. Chu, M. Chen, [Hierarchical Text-Conditional Image Generation with CLIP Latents](https://arxiv.org/abs/2204.06125) (2022), arXiv

</details>

<details>
<summary>Multimodal Embeddings: An Introduction</summary>

# Multimodal Embeddings: An Introduction

**Source URL:** <https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/>

Mapping text and images into a common space

Shaw Talebi

Nov 29, 2024

8 min read

This is the 2nd article in a [larger series](https://shawhin.medium.com/list/multimodal-ai-fe9521d0e77a) on multimodal AI. In the [previous post](https://towardsdatascience.com/multimodal-models-llms-that-can-see-and-hear-5c6737c981d3), we saw how to augment [large language models (LLMs)](https://shawhin.medium.com/list/large-language-models-llms-8e009ae3054c) to understand new data modalities (e.g., images, audio, video). One such approach relied on encoders that generate vector representations (i.e. embeddings) of non-text data. In this article, I will discuss _multimodal_ embeddings and share what they can do via two practical use cases.

https://towardsdatascience.com/wp-content/uploads/2024/11/1a6BF-kEeo8rd7OW2a3JYGA.pngImage from Canva.

* * *

Multimodal Embeddings: Introduction & Use Cases (with Python) - YouTube

Tap to unmute

[Multimodal Embeddings: Introduction & Use Cases (with Python)](https://www.youtube.com/watch?v=YOvxh_ma5qE) Shaw Talebi

Shaw Talebi94.3K subscribers

[Watch on](https://www.youtube.com/watch?v=YOvxh_ma5qE)

AI research is traditionally split into distinct fields: NLP, computer vision (CV), robotics, human-computer interface (HCI), etc. However, countless practical tasks require the **integration of these different research areas** e.g. autonomous vehicles (CV + robotics), AI agents (NLP + CV + HCI), personalized learning (NLP + HCI), etc.

Although these fields aim to solve different problems and work with different data types, they all share a fundamental process. Namely, **generating useful numerical representations of real-world phenomena**.

Historically, this was done by hand. This means that researchers and practitioners would use their (or other people’s) expertise to explicitly transform data into a more helpful form. Today, however, _these can be derived another way_.

## **Embeddings**

**Embeddings** are **(useful) numerical representations of data learned implicitly through model training**. For example, through learning how to predict text, BERT learned representations of text, which are helpful for many NLP tasks \[1\]. Another example is the Vision Transformer (ViT), trained for image classification on Image Net, which can be repurposed for other applications \[2\].

A key point here is that these learned embedding spaces will have some underlying structure so that **similar concepts are located close together**. As shown in the toy examples below.

https://towardsdatascience.com/wp-content/uploads/2024/11/1jpmC6Kx7DxVeikEr15vooA.pngToy represetation of text and image embeddings, respectively. Image by author.

One **key limitation** of the previously mentioned models is they are restricted to a single data modality, e.g., text or images. Preventing cross-modal applications like image captioning, content moderation, image search, and more. _But what if we could merge these two representations?_

## **Multimodal Embeddings**

Although text and images may look very different to us, in a neural network, these are **represented via the same mathematical object**, i.e., a vector. Therefore, in principle, text, images, or any other data modality can processed by a single model.

This fact underlies **multimodal embeddings**, which **represent multiple data modalities in the same vector space** such that similar concepts are co-located (independent of their original representations).

https://towardsdatascience.com/wp-content/uploads/2024/11/15d3HBNjNIXLy0oMIvJjxWw.pngToy representation of multimodal embedding space. Image by author.

For example, CLIP encodes text and images into a shared embedding space \[3\]. A key insight from CLIP is that by aligning text and image representations, the **model is capable of 0-shot image classification on an arbitrary set of target classes** since any input text can be treated as a class label (we will see a concrete example of this later).

However, this idea is not limited to text and images. Virtually any data modalities can be aligned in this way e.g., text-audio, audio-image, text-EEG, image-tabular, and text-video. Unlocking use cases such as video captioning, advanced OCR, audio transcription, video search, and EEG-to-text \[4\].

## **Contrastive Learning**

The standard approach to aligning disparate embedding spaces is **contrastive learning (CL)**. A key intuition of CL is to **represent different views of the same _information_ similarly** \[5\].

This consists of learning representations that **maximize the similarity between positive pairs** and **minimize the similarity of negative pairs**. In the case of an image-text model, a positive pair might be an image with an appropriate caption, while a negative pair would be an image with an irrelevant caption (as shown below).

https://towardsdatascience.com/wp-content/uploads/2024/11/1AGHBVjzwjXapJSe4aUPrjg.pngExample positive and negative pairs used in contrastive training. Image by author.

**Two key aspects** **of CL** contribute to its effectiveness

1.  Since positive and negative pairs can be curated from the data’s inherent structure (e.g., metadata from web images), CL training data **do not require manual labeling**, which unlocks larger-scale training and more powerful representations \[3\].
2.  It simultaneously maximizes positive and minimizes negative pair similarity via a special loss function, as demonstrated by CLIP \[3\].

![CLIP's contrastive loss for text-image representation alignment [3]. Image by author.](https://towardsdatascience.com/wp-content/uploads/2024/11/12X1aT8fzFsgbqn23zXmmAA.png)CLIP’s contrastive loss for text-image representation alignment \[3\]. Image by author.

## **Example Code:** Using CLIP for 0-shot classification and image search

With a high-level understanding of how multimodal embeddings work, let’s see two concrete examples of what they can do. Here, I will use the open-source [CLIP model](https://huggingface.co/openai/clip-vit-base-patch16) to perform two tasks: 0-shot image classification and image search.

The **code for these examples** is freely available on the [GitHub repository](https://github.com/ShawhinT/YouTube-Blog/tree/main/multimodal-ai/2-mm-embeddings).

* * *

### Use case 1: 0-shot Image Classification

The basic idea behind using CLIP for 0-shot image classification is to pass an image into the model along with a set of possible class labels. Then, a classification can be made by **evaluating which text input is most similar to the input image**.

We’ll start by importing the [Hugging Face Transformers library](https://huggingface.co/docs/transformers/en/installation) so that the CLIP model can be downloaded locally. Additionally, the PIL library is used to load images in Python.

```python
from transformers import CLIPProcessor, CLIPModel
from PIL import Image
```

Next, we can import a version of the clip model and its associated data processor. _Note: the processor handles tokenizing input text and image preparation._

```ini
# import model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch16")

# import processor (handles text tokenization and image preprocessing)
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch16")
```

We load in the below image of a cat and create a list of two possible class labels: " _a photo of a cat_" or " _a photo of a dog_".

```ini
# load image
image = Image.open("images/cat_cute.png")

# define text classes
text_classes = ["a photo of a cat", "a photo of a dog"]
```

https://towardsdatascience.com/wp-content/uploads/2024/11/1Nzo536sqahqm1Q24Ms2vmA.pngInput cat photo. Image from Canva.

Next, we’ll preprocess the image/text inputs and pass them into the model.

```ini
# pass image and text classes to processor
inputs = processor(text=text_classes, images=image, return_tensors="pt",
                                                    padding=True)

# pass inputs to CLIP
outputs = model(**inputs) # note: "**" unpacks dictionary items
```

To make a class prediction, we must extract the image logits and evaluate which class corresponds to the maximum.

```makefile
# image-text similarity score
logits_per_image = outputs.logits_per_image
# convert scores to probs via softmax
probs = logits_per_image.softmax(dim=1)

# print prediction
predicted_class = text_classes[probs.argmax()]
print(predicted_class, "| Probability = ",
                       round(float(probs[0][probs.argmax()]),4))
```

```none
>> a photo of a cat | Probability =  0.9979
```

The model nailed it with a 99.79% probability that it’s a cat photo. However, this was a super easy one. Let’s see what happens when we change the class labels to: " _ugly cat_" and " _cute cat_" for the same image.

```none
>> cute cat | Probability =  0.9703
```

The model easily identified that the image was indeed a cute cat. Let’s do something more challenging like the labels: " _cat meme_" or " _not cat meme_".

```none
>> not cat meme | Probability =  0.5464
```

While the model is less confident about this prediction with a 54.64% probability, it correctly implies that the image is not a meme.

### Use case 2: Image Search

Another application of CLIP is essentially the inverse of Use Case 1. Rather than identifying which text label matches an input image, we can evaluate **which image (in a set) best matches a text input (i.e. query)**—in other words, performing a search over images.

We start by storing a set of images in a list. Here, I have three images of a cat, dog, and goat, respectively.

```python
# create list of images to search over
image_name_list = ["images/cat_cute.png", "images/dog.png", "images/goat.png"]

image_list = []
for image_name in image_name_list:
    image_list.append(Image.open(image_name))
```

Next, we can define a query like " _a cute dog_" and pass it and the images into CLIP.

```python
# define a query
query = "a cute dog"

# pass images and query to CLIP
inputs = processor(text=query, images=image_list, return_tensors="pt",
                                                  padding=True)
```

We can then match the best image to the input text by extracting the text logits and evaluating the image corresponding to the maximum.

```python
# compute logits and probabilities
outputs = model(**inputs)
logits_per_text = outputs.logits_per_text
probs = logits_per_text.softmax(dim=1)

# print best match
best_match = image_list[probs.argmax()]
prob_match = round(float(probs[0][probs.argmax()]),4)

print("Match probability: ",prob_match)
display(best_match)
```

```none
>> Match probability:  0.9817
```

https://towardsdatascience.com/wp-content/uploads/2024/11/14wnqr5p_7N3QD5EkXIQeew.pngBest match for query "a cute dog". Image from Canva.

We see that (again) the model nailed this simple example. But let’s try some trickier examples.

```python
query = "something cute but metal 🤘"
```

```none
>> Match probability:  0.7715
```

https://towardsdatascience.com/wp-content/uploads/2024/11/1tIY3_ONQQT_cracAPWm8NQ.pngBest match for query "something cute but metal 🤘". Image from Canva.

```python
query = "a good boy"
```

```none
>> Match probability:  0.8248
```

https://towardsdatascience.com/wp-content/uploads/2024/11/14wnqr5p_7N3QD5EkXIQeew.pngBest match for query "a good boy". Image from Canva.

```python
query = "the best pet in the world"
```

```none
>> Match probability:  0.5664
```

https://towardsdatascience.com/wp-content/uploads/2024/11/1Nzo536sqahqm1Q24Ms2vmA.pngBest match for query "the best pet in the world". Image from Canva.

Although this last prediction is quite controversial, all the other matches were spot on! This is likely since images like these are ubiquitous on the internet and thus were seen many times in CLIP’s pre-training.

> [**YouTube-Blog/multimodal-ai/2-mm-embeddings at main · ShawhinT/YouTube-Blog**](https://github.com/ShawhinT/YouTube-Blog/tree/main/multimodal-ai/2-mm-embeddings)

## What’s Next?

Multimodal embeddings unlock countless AI use cases that involve multiple data modalities. Here, we saw two such use cases, i.e., 0-shot image classification and image search using CLIP.

Another practical application of models like CLIP is multimodal RAG, which consists of the automated retrieval of multimodal context to an LLM. In the [next article](https://medium.com/towards-data-science/multimodal-rag-process-any-file-type-with-ai-e6921342c903) of this [series](https://shawhin.medium.com/list/multimodal-ai-fe9521d0e77a), we will see how this works under the hood and review a concrete example.

**More on Multimodal models 👇**

> [**Multimodal AI**](https://shawhin.medium.com/list/fe9521d0e77a)

* * *

**My website**: [https://www.shawhintalebi.com/](https://www.shawhintalebi.com/)

- \[1\] [BERT](https://arxiv.org/abs/1810.04805)
- \[2\] [ViT](https://arxiv.org/abs/2010.11929)
- \[3\] [CLIP](https://arxiv.org/abs/2103.00020)
- \[4\] [Thought2Text: Text Generation from EEG Signal using Large Language Models (LLMs)](https://arxiv.org/abs/2410.07507)
- \[5\] [A Simple Framework for Contrastive Learning of Visual Representations](https://arxiv.org/abs/2002.05709)

* * *

Written By

Shaw Talebi

</details>

<details>
<summary>Understanding Multimodal LLMs</summary>

# Understanding Multimodal LLMs

**Source URL:** <https://magazine.sebastianraschka.com/p/understanding-multimodal-llms>

### An introduction to the main techniques and latest models

[Sebastian Raschka, PhD](https://substack.com/@rasbt)

Nov 03, 2024

It was a wild two months. There have once again been many developments in AI research, with two Nobel Prizes awarded to AI and several interesting research papers published.

Among others, Meta AI released their latest Llama 3.2 models, which include open-weight versions for the 1B and 3B large language models and two multimodal models.

In this article, I aim to explain how multimodal LLMs function. Additionally, I will review and summarize roughly a dozen other recent multimodal papers and models published in recent weeks (including Llama 3.2) to compare their approaches.

(To see a table of contents menu, click on the stack of lines on the left-hand side.)

https://substackcdn.com/image/fetch/$s_!Pq2z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d76dab1-362f-45b6-9b12-a12ac131edc5_1600x944.png _An illustration of a multimodal LLM that can accept different input modalities (audio, text, images, and videos) and returns text as the output modality._

# 1. Use cases of multimodal LLMs

What are multimodal LLMs? As hinted at in the introduction, multimodal LLMs are large language models capable of processing multiple types of inputs, where each "modality" refers to a specific type of data—such as text (like in traditional LLMs), sound, images, videos, and more. For simplicity, we will primarily focus on the image modality alongside text inputs.

A classic and intuitive application of multimodal LLMs is image captioning: you provide an input image, and the model generates a description of the image, as shown in the figure below.

https://substackcdn.com/image/fetch/$s_!8kaL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93884822-79f1-498d-a33a-8a367ba57134_1500x1222.png _Example use of a multimodal LLM explaining [a meme](https://x.com/PainSci/status/1309570607458086914)._

Of course, there are many other use cases. For example, one of my favorites is extracting information from a PDF table and converting it into LaTeX or Markdown.

# 2. Common approaches to building multimodal LLMs

There are two main approaches to building multimodal LLMs:

- Method A: Unified Embedding Decoder Architecture approach;

- Method B: Cross-modality Attention Architecture approach.


(By the way, I don’t believe official terms for these techniques exist yet, but let me know if you’ve come across any. For instance, briefer descriptions may be "decoder-only" and "cross-attention-based" approaches.)

https://substackcdn.com/image/fetch/$s_!8miE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F53956ae8-9cd8-474e-8c10-ef6bddb88164_1600x938.png _The two main approaches to developing multimodal LLM architectures._

As shown in the figure above, the _**Unified Embedding-Decoder Architecture**_ utilizes a single decoder model, much like an unmodified LLM architecture such as GPT-2 or Llama 3.2. In this approach, images are converted into tokens with the same embedding size as the original text tokens, allowing the LLM to process both text and image input tokens together after concatenation.

The _**Cross-Modality Attention Architecture**_ employs a cross-attention mechanism to integrate image and text embeddings directly within the attention layer.

In the following sections, we will explore how these methods work on a conceptual level. Then, we will look at recent research papers on multimodal LLMs to see how they are applied in practice.

## **2.1 Method A: Unified Embedding Decoder Architecture**

Let’s begin with the unified embedding decoder architecture, illustrated again in the figure below.

https://substackcdn.com/image/fetch/$s_!Ws6n!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91955021-7da5-4bc4-840e-87d080152b18_1166x1400.png _Illustration of the unified embedding decoder architecture, which is an unmodified decoder-style LLM (like GPT-2, Phi-3, Gemma, or Llama 3.2) that receives inputs consisting of image token and text token embeddings._

In the unified embedding-decoder architecture, an image is converted into embedding vectors, similar to how input text is converted into embeddings in a standard text-only LLM.

For a typical text-only LLM that processes text, the text input is usually tokenized (e.g., using Byte-Pair Encoding) and then passed through an embedding layer, as shown in the figure below.

https://substackcdn.com/image/fetch/$s_!dOba!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc97009dd-cee6-455f-87fe-64c33a868e9f_986x858.png _Illustration of the standard process for tokenizing text and converting it into token embedding vectors, which are subsequently passed to an LLM during training and inference._

### **2.1.1 Understanding Image encoders**

Analogous to the tokenization and embedding of text, image embeddings are generated using an image encoder module (instead of a tokenizer), as shown in the figure below.

https://substackcdn.com/image/fetch/$s_!PlBh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F15e9cc2f-95de-4723-9de5-9f2af7571aaa_790x750.png _Illustration of the process for encoding an image into image patch embeddings._

What happens inside the image encoder shown above? To process an image, we first divide it into smaller patches, much like breaking words into subwords during tokenization. These patches are then encoded by a pretrained vision transformer (ViT), as shown in the figure below.

https://substackcdn.com/image/fetch/$s_!_DNf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffef5f8cb-c76c-4c97-9771-7fdb87d7d8cd_1600x1135.png _Illustration of a classic vision transformer (ViT) setup, similar to the model proposed in [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929) (2020)._

Note that ViTs are often used for classification tasks, so I included the classification head in the figure above. However, in this case, we only need the image encoder part.

### **2.1.2 The role of the linear projection module**

The "linear projection" shown in the previous figure consists of a single linear layer (i.e., a fully connected layer). The purpose of this layer is to project the image patches, which are flattened into a vector, into an embedding size compatible with the transformer encoder. This linear projection is illustrated in the figure below. An image patch, flattened into a 256-dimensional vector, is up-projected to a 768-dimensional vector.

https://substackcdn.com/image/fetch/$s_!i9i4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fee32d720-92d7-48c2-b39d-adf61a870075_1600x681.png _Illustration of a linear projection layer that projects flattened image patches from a 256-dimensional into a 768-dimensional embedding space._

For those who prefer seeing a code example, In PyTorch code, we could implement the linear projection for the image patches as follows:

```
import torch

class PatchProjectionLayer(torch.nn.Module):

    def __init__(self, patch_size, num_channels, embedding_dim):
        super().__init__()
        self.patch_size = patch_size
        self.num_channels = num_channels
        self.embedding_dim = embedding_dim
        self.projection = torch.nn.Linear(
            patch_size * patch_size * num_channels, embedding_dim
        )

    def forward(self, x):

        batch_size, num_patches, channels, height, width = x.size()
        x = x.view(batch_size, num_patches, -1)  # Flatten each patch
        x = self.projection(x)  # Project each flattened patch
        return x

# Example Usage:
batch_size = 1
num_patches = 9  # Total patches per image
patch_size = 16  # 16x16 pixels per patch
num_channels = 3  # RGB image
embedding_dim = 768  # Size of the embedding vector

projection_layer = PatchProjectionLayer(patch_size, num_channels, embedding_dim)

patches = torch.rand(
    batch_size, num_patches, num_channels, patch_size, patch_size
)

projected_embeddings = projection_layer(patches)
print(projected_embeddings.shape)

# This prints
# torch.Size([1, 9, 768])
```

If you have read my [Machine Learning Q and AI](https://www.amazon.com/Machine-Learning-AI-Essential-Questions/dp/1718503768/) book by chance, you may know there are ways to replace linear layers with convolution operations that can be implemented to be mathematically equivalent. Here, this can be especially handy as we can combine the creation of patches and projection into two lines of code:

```
layer = torch.nn.Conv2d(3, 768, kernel_size=(16, 16), stride=(16, 16))

image = torch.rand(batch_size, 3, 48, 48)
projected_patches = layer(image)

print(projected_patches.flatten(-2).transpose(-1, -2).shape)
# This prints
# torch.Size([1, 9, 768])
```

### **2.1.3 Image vs text tokenization**

Now that we briefly discussed the purpose of the image encoder (and the linear projection that is part of the encoder), let's return to the text tokenization analogy from earlier and look at text and image tokenization and embedding side by side, as depicted in the figure below.

https://substackcdn.com/image/fetch/$s_!zjmg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d56ea06-d202-4eb7-9e01-9aac492ee309_1522x1206.png _Image tokenization and embedding (left) and text tokenization and embedding (right) side by side._

As you can see in the figure above, I included an additional _**projector**_ module that follows the image encoder. This _projector_ is usually just another _**linear projection**_ layer that is similar to the one explained earlier. The purpose is to project the image encoder outputs into a dimension that matches the dimensions of the embedded text tokens, as illustrated in the figure below. (As we will see later, the projector is sometimes also called adapter, adaptor, or connector.)

https://substackcdn.com/image/fetch/$s_!TaTW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d0be64c-da90-4193-86db-804f6a8a0abb_1542x1242.png _Another side-by-side comparison between image tokenization and text tokenization, where the role of the projector is to match the text token embedding dimensions._

Now that the image patch embeddings have the same embedding dimension as the text token embeddings, we can simply concatenate them as input to the LLM, as shown in the figure at the beginning of this section. Below is the same figure again for easier reference.

https://substackcdn.com/image/fetch/$s_!FTft!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa219f185-211b-4569-9398-2e080e2c5619_1166x1400.png _After projecting the image patch tokens into the same dimension as the text token embeddings, we can simply concatenate them as input to a standard LLM._

By the way, the image encoder we discussed in this section is usually a pretrained vision transformer. A popular choice is [CLIP](https://github.com/openai/CLIP) or [OpenCLIP](https://github.com/mlfoundations/open_clip).

However, there are also versions of Method A that operate directly on patches, such as [Fuyu](https://www.adept.ai/blog/fuyu-8b), which is shown in the figure below.

https://substackcdn.com/image/fetch/$s_!LB1L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28269d0d-b806-4ae7-bf96-b282affd7e93_1600x645.png _Annotated figure of the Fuyu multimodal LLM that operates directly on the image patches without image encoder. (Annotated figure from [https://www.adept.ai/blog/fuyu-8b](https://www.adept.ai/blog/fuyu-8b).)_

As illustrated in the figure above, Fuyu passes the input patches directly into a linear projection (or embedding layer) to learn its own image patch embeddings rather than relying on an additional pretrained image encoder like other models and methods do. This greatly simplifies the architecture and training setup.

## **2.2 Method B: Cross-Modality Attention Architecture**

Now that we have discussed the unified embedding decoder architecture approach to building multimodal LLMs and understand the basic concept behind image encoding, let's talk about an alternative way of implementing multimodal LLMs via cross-attention, as summarized in the figure below.

https://substackcdn.com/image/fetch/$s_!7Xvv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9c06055-b959-45d1-87b2-1f4e90ceaf2d_1296x1338.png _An illustration of the Cross-Modality Attention Architecture approach to building multimodal LLMs._

In the Cross-Modality Attention Architecture method depicted in the figure above, we still use the same image encoder setup we discussed previously. However, instead of encoding the patches as input to the LLM, we connect the input patches in the multi-head attention layer via a cross-attention mechanism.

The idea is related and goes back to the original transformer architecture from the 2017 [Attention Is All You Need](https://arxiv.org/abs/1706.03762) paper, highlighted in the figure below.

https://substackcdn.com/image/fetch/$s_!JYyE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d028b95-7965-43e0-b8fc-350609a69377_1370x1582.png _High-level illustration of the cross-attention mechanism used in the original transformer architecture. (Annotated figure from the "Attention Is All You Need" paper: https://arxiv.org/abs/1706.03762.)_

Note that the original "Attention Is All You Need" transformer depicted in the figure above was originally developed for language translation. So, it consists of a text **en** coder (left part of the figure) that takes the sentence to be translated and generates the translation via a text **de** coder (right part of the figure). In the context of multimodal LLM, the encoder is an image encoder instead of a text encoder, but the same idea applies.

How does cross-attention work? Let's have a look at a conceptual drawing of what happens inside the regular self-attention mechanism.

https://substackcdn.com/image/fetch/$s_!HqoQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff763532b-1eed-4f7d-ae2c-7783d4f4fc46_1440x1194.png _Outline of the regular self-attention mechanism. (This flow depicts one of the heads in a regular multi-head attention module.)_

In the figure above, x is the input, and _Wq_ is a weight matrix used to generate the queries ( _Q_). Similarly, _K_ stands for keys, and _V_ stands for values. A represents the attention scores matrix, and _Z_ are the inputs (x) transformed into the output context vectors. (If this seems confusing, you may find a comprehensive introduction in Chapter 3 of my [Build a Large Language Model from Scratch book](https://www.amazon.com/Build-Large-Language-Model-Scratch/dp/1633437167/) helpful; alternatively, you may also find my article, [Understanding and Coding Self-Attention, Multi-Head Attention, Cross-Attention, and Causal-Attention in LLMs](https://magazine.sebastianraschka.com/p/understanding-and-coding-self-attention) helpful here.)

In cross-attention, in contrast to self-attention, we have two different input sources, as illustrated in the following figure.

https://substackcdn.com/image/fetch/$s_!3PZD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe4cc6f4-ca9a-431b-b572-95a1fda373a7_1508x1120.png _Illustration of cross attention, where there can be two different inputs x1 and x2_

As illustrated in the previous two figures, in self-attention, we work with the same input sequence. In cross-attention, we mix or combine two different input sequences.

In the case of the original transformer architecture in the _Attention Is All You Need_ paper, the two inputs _x1_ and _x2_ correspond to the sequence returned by the encoder module on the left ( _x2_) and the input sequence being processed by the decoder part on the right ( _x1_). In the context of a multimodal LLM, _x2_ is the output of an image encoder. (Note that the queries usually come from the decoder, and the keys and values typically come from the encoder.)

Note that in cross-attention, the two input sequences _x1_ and _x2_ can have different numbers of elements. However, their embedding dimensions must match. If we set _x1 = x2_, this is equivalent to self-attention.

# 3. Unified decoder and cross-attention model training

Now that we have talked a bit about the two major multimodal design choices, let's briefly talk about how we deal with the three major components during model training, which are summarized in the figure below.

https://substackcdn.com/image/fetch/$s_!e2P-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24a12032-d32e-41f6-b390-4e321e1ea29f_1600x770.png _An overview of the different components in a multimodal LLM. The components numbered 1-3 can be frozen or unfrozen during the multimodal training process._

Similar to the development of traditional text-only LLMs, the training of multimodal LLMs also involves two phases: pretraining and instruction finetuning. However, unlike starting from scratch, multimodal LLM training typically begins with a pretrained, instruction-finetuned text-only LLM as the base model.

For the image encoder, CLIP is commonly used and often remains unchanged during the entire training process, though there are exceptions, as we will explore later. Keeping the LLM part frozen during the pretraining phase is also usual, focusing only on training the projector—a linear layer or a small multi-layer perceptron. Given the projector's limited learning capacity, usually comprising just one or two layers, the LLM is often unfrozen during multimodal instruction finetuning (stage 2) to allow for more comprehensive updates. However, note that in the cross-attention-based models (Method B), the cross-attention layers are unfrozen throughout the entire training process.

After introducing the two primary approaches (Method A: Unified Embedding Decoder Architecture and Method B: Cross-modality Attention Architecture), you might be wondering which is more effective. The answer depends on specific trade-offs.

The Unified Embedding Decoder Architecture (Method A) is typically easier to implement since it doesn't require any modifications to the LLM architecture itself.

The Cross-modality Attention Architecture (Method B) is often considered more computationally efficient because it doesn't overload the input context with additional image tokens, introducing them later in the cross-attention layers instead. Additionally, this approach maintains the text-only performance of the original LLM if the LLM parameters are kept frozen during training.

We will revisit the discussion on modeling performance and response quality in a later section, where we will discuss NVIDIA's NVLM paper.

This marks the end of what turned out to be a rather extensive introduction to multimodal LLMs. As I write this, I realize that the discussion has become lengthier than initially planned, which probably makes this a good place to conclude the article.

However, to provide a practical perspective, it would be nice to examine a few recent research papers that implement these approaches. So, we will explore these papers in the remaining sections of this article.

# 4. Recent multimodal models and methods

For the remainder of this article, I will review recent literature concerning multimodal LLMs, focusing specifically on works published in the last few weeks to maintain a reasonable scope.

Thus, this is not a historical overview or comprehensive review of multimodal LLMs but rather a brief look at the latest developments. I will also try to keep these summaries short and without too much fluff as there are 10 of them.

The conclusion section at the end of this has an overview that compares the methods used in these papers.

## **4.1 The Llama 3 Herd of Models**

_[The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783)_ paper (July 31, 2024) by Meta AI came out earlier this summer, which feels like ages ago in LLM terms. However, given that they only described but did not release their multimodal models until much later, I think it's fair to include Llama 3 in this list. (Llama 3.2 models were officially announced and made available on September 25.)

The multimodal Llama 3.2 models, which come in an 11-billion and 90-billion parameter version, are image-text models that use the previously described cross-attention-based approach, which is illustrated in the figure below.

https://substackcdn.com/image/fetch/$s_!fTYU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7c8578fa-70f2-474f-9e98-87621f2dce96_1600x833.png _Illustration of the multimodal LLM approach used by Llama 3.2. (Annotated figure from the Llama 3 paper: https://arxiv.org/abs/2407.21783.The video and speech parts are visually occluded to focus the attention on the image part.)_

Note that while the figure also depicts video and speech as possible modalities, the models that were released as of this writing focus only on image and text.

Llama 3.2 uses the cross-attention-based approach. However, it differs a bit from what I wrote about earlier, namely that in multimodal LLM development, we usually freeze the image encoder and only update the LLM parameters during pretraining.

Here, the researchers almost take the opposite approach: they update the image encoder but do not update the language model's parameters. They write that this is intentional and done to preserve the text-only capabilities so that the 11B and 90B multimodal models can be used as drop-in replacements for the Llama 3.1 8B and 70B text-only model on text tasks.

The training itself is done in multiple iterations, starting with the Llama 3.1 text models. After adding the image encoder and projection (here called "adapter") layers, they pretrain the model on image-text data. Then, similar to the Llama 3 model text-only training (I wrote about it in [an earlier article](https://magazine.sebastianraschka.com/i/147749119/llama-overview)), they follow up with instruction and preference finetuning.

Instead of adopting a pretrained model such as CLIP as an image encoder, the researchers used a vision transformer that they pretrained from scratch. Specifically, they adopted the  ViT-H/14 variant (630 million parameters) of the classic vision transformer architecture ( [Dosovitskiy et al., 2020](https://arxiv.org/abs/2010.11929)). They then pretrained the ViT on a dataset of 2.5 billion image-text pairs over five epochs; this was done before connecting the image encoder to the LLM. (The image encoder takes 224×224 resolution images and divides them into a 14×14 grid of patches, with each patch sized at 16×16 pixels.)

As the cross-attention layers add a substantial amount of parameters, they are only added in every fourth transformer block. (For the 8B model, this adds 3B parameters, and for the 70B model, this adds 20 billion parameters.)

## **4.2 Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Multimodal Models**

_[The Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Multimodal Models](https://www.arxiv.org/abs/2409.17146)_ paper (September 25, 2024) is notable because it promises to open source not only the model weights but also the dataset and source code similar to the language-only OLMo LLM. (This is great for LLM research as it allows us to take a look at the exact training procedure and code and also lets us run ablation studies and reproduce results on the same dataset.)

If you are wondering why there are two names in the paper title, Molmo refers to the model (Multimodal Open Language Model), and PixMo (Pixels for Molmo) is the dataset.

https://substackcdn.com/image/fetch/$s_!9P0w!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73337002-8feb-4f1b-a109-1407096e32c5_1104x704.png _Illustration of the Molmo decoder-only approach (Method A). Annotated figure adapted from the Molmo and PixMo: Open Weights and Open Data for State-of-the-Art Multimodal Models paper: https://www.arxiv.org/abs/2409.17146._

As illustrated in the figure above, the image encoder employs an off-the-shelf vision transformer, specifically CLIP. The term "connector" here refers to a "projector" that aligns image features with the language model.

Molmo streamlines the training process by avoiding multiple pretraining stages, choosing instead a simple pipeline that updates all parameters in a unified approach—including those of the base LLM, the connector, and the image encoder.

The Molmo team offers several options for the base LLM:

- OLMo-7B-1024 (a fully open model backbone),

- OLMoE-1B-7B (a mixture-of-experts architecture; the most efficient model),

- Qwen2 7B (an open-weight model that performs better than OLMo-7B-1024),

- Qwen2 72B (an open-weight model and the best-performing model)


## **4.3 NVLM: Open Frontier-Class Multimodal LLMs**

NVIDIA's _[NVLM: Open Frontier-Class Multimodal LLMs](https://arxiv.org/abs/2409.11402)_ paper (September 17, 2024) is particularly interesting because, rather than focusing on a single approach, it explores both methods:

- Method A, the Unified Embedding Decoder Architecture ("decoder-only architecture," NVLM-D), and

- Method B, the Cross-Modality Attention Architecture ("cross-attention-based architecture," NVLM-X).


Additionally, they develop a hybrid approach (NVLM-H) and provide an apples-to-apples comparison of all three methods.

https://substackcdn.com/image/fetch/$s_!6n6Y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F45916952-b1ee-4972-a956-e45703e3fe36_1600x927.png _Overview of the three multimodal approaches. (Annotated figure from the NVLM: Open Frontier-Class Multimodal LLMs paper: https://arxiv.org/abs/2409.11402)_

As summarized in the figure below, NVLM-D corresponds to Method A, and NVLM-X corresponds to Method B, as discussed earlier. The concept behind the hybrid model (NVLM-H) is to combine the strengths of both methods: an image thumbnail is provided as input, followed by a dynamic number of patches passed through cross-attention to capture finer high-resolution details.

In short, the research team find that:

- NVLM-X demonstrates superior computational efficiency for high-resolution images.

- NVLM-D achieves higher accuracy in OCR-related tasks.

- NVLM-H combines the advantages of both methods.


Similar to Molmo and other approaches, they begin with a text-only LLM rather than pretraining a multimodal model from scratch (as this generally performs better). Additionally, they use an instruction-tuned LLM instead of a base LLM. Specifically, the backbone LLM is Qwen2-72B-Instruct (to my knowledge, Molmo used the Qwen2-72B base model).

While training all LLM parameters in the NVLM-D approach, they found that for NVLM-X, it works well to freeze the original LLM parameters and train only the cross-attention layers during both pretraining and instruction finetuning.

For the image encoder, instead of using a typical CLIP model, they use [InternViT-6B](https://arxiv.org/abs/2312.14238), which remains frozen throughout all stages.

The projector is a multilayer perceptron rather than a single linear layer.

## **4.4 Qwen2-VL: Enhancing Vision-Language Model’s Perception of the World at Any Resolution**

The previous two papers and models, Molmo and NVLM, were based on Qwen2-72B LLM. In this paper, the Qwen research team itself announces a multimodal LLM, _[Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution](https://arxiv.org/abs/2409.12191)_ (October 3rd, 2024).

At the core of this work is their so-called "Naive Dynamic Resolution" mechanism (the term "naive" is intentional and not a typo for "native," though "native" could also be fitting). This mechanism allows the model to handle images of varying resolutions without simple downsampling, enabling the input of images in their original resolution.

https://substackcdn.com/image/fetch/$s_!Zrt8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2247e684-253a-462e-afb4-549411d5741a_1490x1068.png _An overview of the multimodal Qwen model, which can process input images with various different resolutions natively. (Annotated figure from the Qwen2-VL paper: https://arxiv.org/abs/2409.12191)_

The native resolution input is implemented via a modified ViT by removing the original absolute position embeddings and introducing 2D-RoPE.

They used a classic vision encoder with 675M parameters and LLM backbones of varying sizes, as shown in the table below.

https://substackcdn.com/image/fetch/$s_!NdAJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2ce9ce4a-d7ec-476d-91cb-29b6f5440b3b_1396x482.png The components of the different Qwen2-VL models. (Annotated figure from the Qwen2-VL paper: https://arxiv.org/abs/2409.12191)

The training itself consists of 3 stages: (1) pretraining only the image encoder, (2) unfreezing all parameters (including LLM), and (3) freezing the image encoder and instruction-finetuning only the LLM.

## **4.5 Pixtral 12B**

_[Pixtral 12B](https://mistral.ai/news/pixtral-12b/)_ (September 17, 2024), which uses the Method A: Unified Embedding Decoder Architecture approach, is the first multimodal model from Mistral AI. Unfortunately, there is no technical paper or report available, but the Mistral team shared a few interesting tidbits in their [blog post](https://mistral.ai/news/pixtral-12b/).

Interestingly, they chose not to use a pretrained image encoder, instead training one with 400 million parameters from scratch. For the LLM backbone, they used the 12-billion-parameter [Mistral NeMo](https://mistral.ai/news/mistral-nemo/) model.

Similar to Qwen2-VL, Pixtral also supports variable image sizes natively, as illustrated in the figure below.

https://substackcdn.com/image/fetch/$s_!eW3C!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37bb0f12-4533-4f44-8907-1da868006ff3_1144x726.png _Illustration of how Pixtral processes images of different sizes. (Annotated figure from the Pixtral blog  post: https://mistral.ai/news/pixtral-12b/)_

## **4.6 MM1.5: Methods, Analysis & Insights from Multimodal LLM Fine-tuning**

The _[MM1.5: Methods, Analysis & Insights from Multimodal LLM Fine-tuning](https://arxiv.org/abs/2409.20566)_ paper (September 30, 2024) provides practical tips and introduces a mixture-of-experts multimodal model alongside a dense model similar to Molmo. The models span a wide size range, from 1 billion to 30 billion parameters.

The models described in this paper focuse on Method A, a Unified Embedding Transformer Architecture, which structures inputs effectively for multimodal learning.

In addition, the paper has a series of interesting ablation studies looking into data mixtures and the effects of using coordinate tokens.

https://substackcdn.com/image/fetch/$s_!fMsE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F71b22b97-e901-4c5f-a9c2-67e32c867823_1402x1178.png _Illustration of the MM1.5 approach, which includes additional coordinate tokens to denote bounding boxes. (Annotated figure from the MM1.5 paper: https://arxiv.org/abs/2409.20566.)_

## **4.7 Aria: An Open Multimodal Native Mixture-of-Experts Model**

The _[Aria: An Open Multimodal Native Mixture-of-Experts Model](https://arxiv.org/abs/2410.05993)_ paper (October 8, 2024) introduces another mixture-of-experts model approach, similar to one of the variants in the Molmo and MM1.5 lineups.

The Aria model has 24.9 billion parameters, with 3.5 billion parameters allocated per text token. The image encoder ( [SigLIP](https://arxiv.org/abs/2303.15343)) has 438-million-parameters.

This model is based on a cross-attention approach with the following overall training procedure:

1. Training the LLM backbone entirely from scratch.

2. Pretraining both the LLM backbone and the vision encoder.


## **4.8 Baichuan-Omni**

The _[Baichuan-Omni Technical Report](https://arxiv.org/abs/2410.08565)_ (October 11, 2024) introduces Baichuan-Omni, a 7-billion-parameter multimodal LLM based on Method A: the Unified Embedding Decoder Architecture approach, as shown in the figure below.

https://substackcdn.com/image/fetch/$s_!-IYi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F142c39bd-2d3f-4813-9363-5ecf616cb784_2102x1326.png _An overview of the Baichuan-Omni model, which can handle various input modalities. (Annotated figure from the Baichuan-Omni paper: https://arxiv.org/abs/2410.08565)_

The training process for Baichuan-Omni involves a three-stage approach:

1. **Projector training**: Initially, only the projector is trained, while both the vision encoder and the language model (LLM) remain frozen.

2. **Vision encoder training**: Next, the vision encoder is unfrozen and trained, with the LLM still frozen.

3. **Full model training**: Finally, the LLM is unfrozen, allowing the entire model to be trained end-to-end.


The model utilizes the SigLIP vision encoder and incorporates the [AnyRes](https://arxiv.org/abs/2204.07156) module to handle high-resolution images through down-sampling techniques.

While the report does not explicitly specify the LLM backbone, it is likely based on the Baichuan 7B LLM, given the model's parameter size and the naming convention.

## **4.9 Emu3: Next-Token Prediction is All You Need**

The _Emu3: Next-Token Prediction is All You Need_ paper (September 27, 2024) presents a compelling alternative to diffusion models for image generation, which is solely based on a transformer-based decoder architecture. Although it's not a multimodal LLM in the classic sense (i.e., models focused on image understanding rather than generation), Emu3 is super interesting as it demonstrates that it's possible to use transformer decoders for image generation, which is a task typically dominated by diffusion methods. (However, note that there have been other similar approaches before, such as [Autoregressive Model Beats Diffusion: Llama for Scalable Image Generation](https://arxiv.org/abs/2406.06525).)

https://substackcdn.com/image/fetch/$s_!IWU7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F775db9c7-662f-4314-a5c4-c3f5efe0238d_1056x904.png _Emu3 is primarily an LLM for image generation as an alternative to diffusion models. (Annotated figure from the Emu3 paper: https://arxiv.org/abs/2409.18869)_

The researchers trained Emu3 from scratch and then used [Direct Preference Optimization](https://github.com/rasbt/LLMs-from-scratch/blob/main/ch07/04_preference-tuning-with-dpo/dpo-from-scratch.ipynb) (DPO) to align the model with human preferences.

The architecture includes a vision tokenizer inspired by [SBER-MoVQGAN](https://arxiv.org/abs/2209.09002). The core LLM architecture is based on Llama 2, yet it is trained entirely from scratch.

## **4.10 Janus: Decoupling Visual Encoding for Unified Multimodal Understanding and Generation**

We previously focused on multimodal LLMs for image understanding and just saw one example for image generation with Emu 3 above. Now, the _[Janus: Decoupling Visual Encoding for Unified Multimodal Understanding and Generation](https://arxiv.org/abs/2410.13848)_ paper (October 17, 2024) introduces a framework that unifies multimodal understanding and generation tasks within a single LLM backbone.

A key feature of Janus is the decoupling of visual encoding pathways to address the distinct requirements of understanding and generation tasks. The researchers argue that image understanding tasks require high-dimensional semantic representations, while generation tasks require detailed local information and global consistency in images. By separating these pathways, Janus effectively manages these differing needs.

The model employs the SigLIP vision encoder, similar to that used in Baichuan-Omni, for processing visual inputs. For image generation, it utilizes a [Vector Quantized (VQ)](https://arxiv.org/abs/2406.06525) tokenizer to handle the generation process. The base LLM in Janus is the [DeepSeek-LLM](https://arxiv.org/abs/2401.02954) with 1.3 billion parameters.

https://substackcdn.com/image/fetch/$s_!9UFg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89d62626-4386-4e73-8992-158550752ce2_1434x692.png _An overview of the unified decoder-only framework used in Janus. (Annotated figure from the Janus paper: https://arxiv.org/abs/2410.13848.)_

The training process for the model in this image follows three stages, as shown in the figure below.

https://substackcdn.com/image/fetch/$s_!Da5n!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fb4f079-0771-4d21-8805-fded73134983_1536x648.png Illustration of the 3-stage training process of the Janus model. (Annotated figure from the Janus paper: https://arxiv.org/abs/2410.13848)

In Stage I, only the projector layers and image output layer are trained while the LLM, understanding, and generation encoders remain frozen. In Stage II, the LLM backbone and text output layer are unfrozen, allowing for unified pretraining across understanding and generation tasks. Finally, in Stage III, the entire model, including the SigLIP image encoder, is unfrozen for supervised fine-tuning, enabling the model to fully integrate and refine its multimodal capabilities.

# Conclusion

As you may have noticed, I almost entirely skipped both the modeling and the computational performance comparisons. First, comparing the performance of LLMs and multimodal LLMs on public benchmarks is challenging due to prevalent data contamination, meaning that the test data may have been included in the training data.

Additionally, the architectural components vary so much that making an apples-to-apples comparison is difficult. So, big kudos to the NVIDIA team for developing NVLM in different flavors, which allowed for a comparison between the decoder-only and cross-attention approaches at least.

In any case, the main takeaway from this article is that multimodal LLMs can be built successfully in many different ways. Below is a figure that summarizes the different components of the models covered in this article.

https://substackcdn.com/image/fetch/$s_!R_9Y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb043e6d7-78e5-4628-987a-b333d3a58829_2224x1180.png An overview of the different models covered in this article along with their subcomponents and training approaches.

I hope you found reading this article educational and now have a better understanding of how multimodal LLMs work!

</details>

<details>
<summary>Vision Language Models</summary>

# Vision Language Models

**Source URL:** <https://www.nvidia.com/en-us/glossary/vision-language-models/>

Vision language models (VLMs) are multimodal, generative AI models capable of understanding and processing video, image, and text.

## What Makes Up a Vision Language Model?

A vision language model is an AI system built by combining a [large language model](https://www.nvidia.com/en-us/glossary/large-language-models/) (LLM) with a vision encoder, giving the LLM the ability to “see.”

With this ability, VLMs can process and provide advanced understanding of video, image, and text inputs supplied in the prompt to generate text responses.

https://www.nvidia.com/content/nvidiaGDC/us/en_US/glossary/vision-language-models/_jcr_content/root/responsivegrid/nv_container_copy/nv_image.coreimg.100.1290.png/1758650173219/metropolis-iva-diagram-vlm-glossary-ces25-3576177-r1--1-.png

Figure 1: Use cases for vision language models

Unlike traditional [computer vision](https://www.nvidia.com/en-us/glossary/computer-vision/) (CV) models, VLMs aren’t bound by a fixed set of classes or a specific task, like classification or detection. Retrained on a vast corpus of text and image/video-caption pairs, VLMs can be instructed in natural language and used to handle many classic vision tasks, as well as new generative AI-powered tasks such as summarization and visual Q&A.

## Why Are Vision Language Models Important?

To understand the importance of VLMs, it’s helpful to know how traditional CV models work. These convolutional neural network ( [CNN](https://www.nvidia.com/en-us/glossary/convolutional-neural-network/))-based CV models are trained for a specific task on a bounded set of classes. For example:

- A classification model that identifies whether an image contains a cat or a dog
- An optical character detection and recognition CV model that reads text in an image, but doesn’t interpret the format or any visual data within a document

Previous CV models were trained for a specific purpose and didn’t have the ability to go beyond the task or set of classes they were developed for and trained on. If the use case changed at all or required a new class to be added to the model, a developer would have to collect and label a large number of images and retrain the model. This is an expensive, time-consuming process. Additionally, CV models don't have any natural language understanding.

VLMs bring a new class of capabilities by combining the power of [foundation models](https://blogs.nvidia.com/blog/what-are-foundation-models/), like [CLIP](https://github.com/openai/CLIP), and LLMs to have both vision and language capabilities. Out of the box, VLMs have strong zero-shot performance on a variety of vision tasks, like visual question-answering, classification, and optical character recognition. They’re also extremely flexible and can be used not just on a fixed set of classes, but for nearly any use case by simply changing a text prompt.

## How Do Vision Language Models Work?

Using a VLM is very similar to interacting with an LLM. The user supplies text prompts that can be interleaved with images. The inputs are then used to generate text output. The input prompts are open-ended, allowing the user to instruct the VLM to answer questions, summarize, explain the content, or reason with the image. Users can chat back and forth with the VLM, with the ability to add images into the context of the conversation. VLMs can also be integrated into visual agents to autonomously perform vision tasks.

Most VLMs follow an architecture with three parts:

- A vision encoder
- A projector
- An LLM

The vision encoder is typically a CLIP-based model with a transformer architecture that has been trained on millions of image-text pairs, giving it the ability to associate images and text. The projector is a set of layers that translates the output of the vision encoder into a form the LLM can understand, often interpreted as image tokens. This projector can be a simple line layer like LLaVA and VILA, or something more complex like the cross-attention layers used in Llama 3.2 Vision.

Any off-the-shelf LLM can be used to build a VLM. There are hundreds of VLM variants that combine various LLMs with vision encoders.

https://www.nvidia.com/content/nvidiaGDC/us/en_US/glossary/vision-language-models/_jcr_content/root/responsivegrid/nv_container_copy_co_300503066/nv_image.coreimg.svg/1758650173905/vlm-architecture-diagram.svg

Figure 2: A common three-part architecture for vision language models

## How Are Vision Language Models Trained?

VLMs are trained in several stages that include pretraining, followed by supervised fine-tuning. Optionally, parameter-efficient fine-tuning (PEFT) can be applied as a final stage to create a domain-specific VLM on custom data.

The pretraining stage aligns the vision encoder, projector, and LLM to essentially speak the same language when interpreting the text and image input. This is done using large corpora of text and images with image-caption pairs and interleaved image-text data. Once the three components have been aligned through pretraining, the VLM goes through a supervised fine-tuning stage to help it understand how to respond to user prompts.

The data used in this stage is a blend of example prompts with text and/or image input and the expected response of the model. For example, this data could be prompts telling the model to describe the image or to count all the objects in the frame with the expected correct response. After this round of training, the VLM will understand how to best interpret images and respond to user prompts.

https://www.nvidia.com/content/nvidiaGDC/us/en_US/glossary/vision-language-models/_jcr_content/root/responsivegrid/nv_container_copy_co_1755415045/nv_image.coreimg.svg/1758650174299/vlm-training-process-diagram.svg

Figure 3: Training for VLMs is often done in several stages to target certain parts of the model

Once the VLM is trained, it can be used in the same way as an LLM by providing prompts that can also include images interleaved in text. The VLM will then generate a text response based on the inputs. VLMs are typically deployed with an OpenAI-style REST API interface to make it easy to interact with the model.

More advanced techniques are currently being researched to enhance vision capabilities:

- Ensembling vision encoders to process image inputs
- Breaking apart high-resolution image inputs into smaller tiles for processing
- Increasing context length to improve long video understanding

All of these advancements are progressing the capabilities of VLMs from only understanding single-image input to being highly capable models that can compare and contrast images, accurately read text, understand long videos, and have strong spatial understanding.

## How Are Vision Language Models Benchmarked?

Several common benchmarks, such [MMMU](https://mmmu-benchmark.github.io/), [Video-MME](https://video-mme.github.io/home_page.html), [MathVista](https://mathvista.github.io/), [ChartQA](https://github.com/vis-nlp/ChartQA) , and [DocVQA](https://www.docvqa.org/), exist to determine how well vision-language models perform on a variety of tasks, such as:

- Visual question-answering
- Logic and reasoning
- Document understanding
- Multi-image comparisons
- Video understanding

Most benchmarks consist of a set of images with several associated questions, often posed as multiple-choice questions. The multiple-choice format is the easiest way to consistently benchmark and compare VLMs. These questions test the VLMs perception, knowledge, and reasoning capabilities. When running these benchmarks, the VLM is provided with the image, question, and several multiple-choice answers it must choose from.

https://www.nvidia.com/content/nvidiaGDC/us/en_US/glossary/vision-language-models/_jcr_content/root/responsivegrid/nv_container_copy_co_42410027/nv_image.coreimg.100.1290.jpeg/1758650174738/vlm-mmmu-ari.jpeg

Figure 4: Example multiple-choice questions for VLMs used in the MMMU benchmark

Source ( [MMMU](https://mmmu-benchmark.github.io/))

The accuracy of the VLM is the number of correct choices over the set of multiple-choice questions. Some benchmarks also include numerical questions where the VLM must perform a specific calculation and be within a certain percentage of the answer to be considered correct. These questions and images often come from academic sources, such as college-level textbooks.

## How Are Vision Language Models Used?

VLMs are quickly becoming the go-to tool for all types of vision-related tasks due to their flexibility and natural language understanding. They can be easily instructed to perform a wide variety of tasks through natural language:

1. Visual questions-answering
2. Image and video summarization
3. Parsing text and handwritten documents

Previous applications that would have required a large ensemble of specially trained models can now be accomplished with just a single VLM.

VLMs are especially good at summarizing the contents of images and can be prompted to perform specific tasks based on the contents. Take for example, an education use case. A VLM could be given an image of a handwritten math problem, and it could use its optical character recognition and reasoning capabilities to interpret the problem and produce a step-by-step guide on how to solve it. VLMs can not only understand the content of the image but also reason and perform specific tasks.

https://www.nvidia.com/content/nvidiaGDC/us/en_US/glossary/vision-language-models/_jcr_content/root/responsivegrid/nv_container_copy_co_531349501/nv_image.coreimg.svg/1758650175193/vlm-real-world-diagram.svg

Figure 5: video analytics AI agents transform video and image data into real-world insights

With vast amounts of video being produced every day, it isn’t feasible to review and extract insights from this volume of video that is produced by all industries. VLMs can be integrated into a larger system to build [video analytics AI agents](https://www.nvidia.com/en-us/use-cases/video-analytics-ai-agents/) capable of detecting specific events when prompted. These systems could be used to detect malfunctioning robots in a warehouse or generate out-of-stock alerts when shelves are empty. Their general understanding goes beyond simple detection and could be used to generate automated reports. For example, [Pegatron](https://www.nvidia.com/en-us/customer-stories/pegatron-scales-factory-operations-with-visual-ai-digital-twins/) augmented its assembly process using video analytics AI agents and saw a 7% reduction in labor costs per assembly line and a 67% decrease in defect rates. [Linker Vision](https://www.nvidia.com/en-us/customer-stories/linker-vision-ai-smart-city-solutions/) also built video analytics AI agents that process thousands of live camera streams to detect incidents like flooding or traffic hazards, enabling faster response for city operations.

VLMs can be used with technologies like graph databases to understand long videos. This helps them capture the complexity of objects and events in a video. Such systems could be used to summarize operations in a warehouse to find bottlenecks and inefficiencies or produce sports commentary for football, basketball, or soccer games.

## What Are the Challenges of Vision Language Models?

Vision language models are maturing quickly, but they still have some limitations, particularly around spatial understanding and long-context video understanding.

Most VLMs use CLIP-based models as the vision encoder, which are limited to 336x336 or 448x448image input size. This relatively small input image makes it difficult for small objects and details to be detected. For example, an HD 1080x1920 frame from a video must be downsized or cropped to a much smaller input resolution, making it difficult to retain details for small objects or fine details. To fix this, VLMs are starting to use tiling methods that allow a big image to be broken into smaller pieces and then fed into the model. There's also ongoing research to explore the use of higher-resolution image encoders.

VLMs also have difficulty providing precise locations for objects. The training data for CLIP-based vision encoders consists mostly of short text descriptions of images, like captions. These descriptions don't include detailed, fine-grained object locations, and this limitation impacts CLIP’s spatial understanding. This is inherited by VLMs that use it as a vision encoder. New approaches are exploring the use of ensembling several vision encoders to address these limitations [2408.15998 (arxiv.org)](https://arxiv.org/pdf/2408.15998).

Long video understanding is a challenge due to the need to take into account visual information across potentially hours of video to properly analyze or answer questions. Like LLMs, VLMs have limited context length, meaning only a certain number of frames from a video can be included to answer questions. Approaches to increase context length and train VLMs on more video-based data are being researched, such as LongVILA [2408.10188 (arxiv.org)](https://www.arxiv.org/pdf/2408.10188).

VLMs may not have seen enough data for very specific use cases, such as finding manufacturing defects in a specific product line. This limitation can be overcome by fine-tuning the VLM on domain-specific data or using multi-image VLMs with in-context learning to provide examples that can teach the model new information without explicitly training the model. Training the model on domain-specific data with PEFT is another technique that can be used to improve a VLM’s accuracy on custom data.

## How Can You Get Started With Vision Language Models?

NVIDIA offers tools to ease the building and deployment of vision language models:

- [NVIDIA Cosmos™ Reason](https://huggingface.co/nvidia/Cosmos-Reason1-7B), an open, customizable, 7-billion-parameter reasoning VLM for physical AI and robotics.
- [NVIDIA NIM](https://build.nvidia.com/explore/vision) ™, a set of inference microservices that includes industry-standard APIs, domain-specific code, optimized inference engines, and enterprise runtime. Check out the VLM NIMs available today [here](https://build.nvidia.com/explore/vision). We created [NIM reference workflows](https://github.com/NVIDIA/metropolis-nim-workflows/tree/main) to help you get started.
- [NVIDIA Blueprints,](https://www.nvidia.com/en-us/ai-data-science/ai-workflows/) reference workflows for generative AI use cases, built with NVIDIA NIM microservices as part of the NVIDIA AI Enterprise Platform. The NVIDIA Metropolis [Video Search and Summarization](https://build.nvidia.com/nvidia/video-search-and-summarization) (VSS) Blueprint, for example, helps you build and customize interactive video analytics AI agents capable of understanding activity within massive volumes of live or archived video using vision VLMs, LLMs, and [RAG](https://www.nvidia.com/en-us/glossary/retrieval-augmented-generation/).

</details>

</golden_source>

<research_source type="guideline_exploitation" phase="exploitation" file="complex-document-recognition-ocr-doesn-t-work-and-here-s-how.md">
<details>
<summary>Complex Document Recognition: OCR Doesn’t Work and Here’s How You Fix It</summary>

Phase: [EXPLOITATION]

# Complex Document Recognition: OCR Doesn’t Work and Here’s How You Fix It

**Source URL:** <https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it>

by
**Oleg Kokorin**

October 12th, 2023

https://hackernoon.imgix.net/images/2DFAaGGO5cfymtBKn4bFFAoT6sg2-6gd3x5m.jpeg

byOleg Kokorin@olegkokorin

CEO of Businessware Technologies, machine learning engineer

In this article, I will dive into a complex world of complex document recognition using AI and OCR.

Document recognition nowadays is not a complex task.

Modern OCR solutions are able to detect both typed and written text in many languages. One can find dedicated solutions for the detection of specific documents like passports and driver’s licenses.

But where out-of-the-box [AI](https://hackernoon.com/c/ai?ref=hackernoon.com) tends to struggle is when a document includes special symbols or tilted text.

Technical drawings are among the ‘trouble children’ that cause ready-made OCR solutions to struggle: they are nothing but a collection of weird symbols and weirdly placed text.

Having worked on an AI solution for technical drawing recognition, I have insights into the world of modern OCR that I will share in this article.

## Why OCR is bad for OCR

The ‘digital first’ approach, at the forefront of many businesses, has motivated many to convert physical documents into a digital format. This process usually involves the implementation of OCR — optical character recognition — which converts physical documents into PDF files.

Morel OCR tools are capable of recognizing more than just text. In many cases, OCR tools can detect special symbols, written text, signatures, images, and more.

Many of these tools come ready to use: all you need to do is install the tool (or, if you are working on a custom solution, use an API) to scan the documents in question.

Despite all this, OCR tools have certain limitations. They don’t work well for irregular text, also called wild text, like low-quality scanned documents with no predefined structure, car license plates, text on advertisement billboards, etc.

### Low-quality scans

The quality of text recognition depends highly on the quality of the document itself. Warping, scratches, faded ink, and more have a detrimental effect on the recognition quality.

### Symbol mixups

Even the best OCR tools have trouble distinguishing between certain similar-looking letters and numbers, like ‘3’ and ‘8’ or ‘O’ and ‘D.’ The very challenges OCR is supposed to solve often become the stumbling block of document digitization.

### Special symbols

Documents that feature any special symbols, from letters specific to a certain language to symbols denominating certain objects, like symbols used in technical drawings, e.g., diameter ‘Ø,’ square ‘□.’

## AI to the rescue

Using artificial intelligence, OCR tools can be improved and augmented to better handle complex documents, and often even replaced by a custom [AI neural network](https://hackernoon.com/enhancing-neural-network-reasoning-the-promise-of-contrastive-decoding-for-llms?ref=hackernoon.com).

Model-based OCR, or intelligent OCR, is the result of using deep learning for text document recognition.

Neural networks can be trained to recognize text regular OCR tools have trouble with. Intelligent OCR provides superior text recognition results in document recognition applications by improving recognition speed and reducing errors.

## Recognition of complex documents

Despite the widespread digitization, some paperwork remains offline. This usually applies to complex documents that are impossible to digitize due to their complex layouts, the use of special symbols, and unconventional formatting.

Technical drawings are the perfect example of a complex document: their layouts change from one document to another; they include a bunch of symbols specific to technical drawings only, and the text is often formatted in odd ways. All of the above makes technical drawings the perfect candidate for model-based OCR.

While working on a similar project, I’ve developed an understanding of the best strategies to apply when working on digitizing technical drawings. I have had experience with working on an AI for floor plan detection, so that’s what I’ll be using as an example.

I’ve broken the process down into sections, as this is exactly how one should approach the development of AI-based OCR solutions for complex document recognition.

## Stage 1: Detection of text

Recognition of plain text is the most simple part of this entire ordeal. When it comes to technical drawings, plain text is used to specify the drawing type, dimensions, floor plan type, building type, etc. While the detection of plain text is a simple task, detecting text on a technical drawing is far more complex.

The text can come in a variety of fonts, sizes, and colors, can be rotated or upside down, and contains special symbols. Ready-made OCR software like iText and OCRSpace can detect simple text with high accuracy, but they fail spectacularly when it comes to technical drawings (or any other complex document, for that matter). For example, these tools struggle to detect rotated text.

https://hackernoon.imgix.net/images/2DFAaGGO5cfymtBKn4bFFAoT6sg2-v993xj8.jpegOCR tools often have trouble detecting rotated text \| Image by author

Most OCR tools can be fine-tuned to handle problematic text better. The best approach to recognizing complex text is to use multiple fine-tuned OCR tools along with a balancer that compares the results of each tool and chooses the one that produces the most accurate results.

Another benefit of using fine-tuned OCR software is the increase in recognition speed.

https://hackernoon.imgix.net/images/2DFAaGGO5cfymtBKn4bFFAoT6sg2-v9a3xhv.jpegFine-tuning of OCR software leads to better results \| Image by author

By fine-tuning these tools alone, we’ve seen a 200 times decrease in document processing speed.If you add an OCR engine into the equation, like Tesseract, the text recognition quality can be increased up to 99.9%.

## Stage 2: Recognition of special symbols

Each technical drawing includes special symbols of some sort. In the case of floor plan technical drawings, the documents include symbols designating doors, windows, electrical outlets, etc.

These symbols, or labels, look like geometric figures with text inside. They can be difficult to distinguish from their surroundings due to their shape, which blends in perfectly with the rest of the drawing.

In addition, there can be multiple labels representing the same object due to inconsistencies in document design.

https://hackernoon.imgix.net/images/2DFAaGGO5cfymtBKn4bFFAoT6sg2-efb3xu6.jpegSimilar looking objects are often detected as the same one \| Image by author

Pre-trained computer vision solutions, like OpenCV libraries for symbol detection, work best with photographs of real-life objects. Technical drawings are quite a bit different: they are almost always in black and white and mostly consist of geometric shapes.

We’ve tested multiple OpenCV libraries, each of which resulted in albeit different, yet insufficiently low recognition quality. Unless you develop your own neural network from scratch, any pre-trained computer vision model needs to be built upon to achieve decent recognition quality.

One of the main problems with using [pre-trained CV models](https://hackernoon.com/creating-computer-vision-apps-without-building-media-pipelines?ref=hackernoon.com) is the amount of false positive results they produce. Technical drawings consist of simple geometric shapes, but so do special symbols and labels, which results in CV models detecting random parts of the drawings as labels.

The best way of mitigating this issue is to implement deep learning to detect false positive results and remove them from the final detection results.

https://hackernoon.imgix.net/images/2DFAaGGO5cfymtBKn4bFFAoT6sg2-mjc3x1z.jpegDeep learning can be used to remove false positive results \| Image by author

## Stage 3: Spreadsheets

Technical drawings often include large spreadsheets with merged cells and complex structures stretching across multiple pages. While spreadsheets are generally easy to detect, the complex nature of these spreadsheets makes them difficult to crack.

Going a custom software route is the best way to achieve satisfactory results. Here’s how we’ve done it:

### Recognition of text in a spreadsheet

Solutions like Amazon Textract work very well and can extract text with very high accuracy as long as the document scan is of high quality. Documents with 300 DPI result in 100% recognition accuracy and 100 DPI results in ~90% accuracy.

### Recognition of spreadsheet structure

First, you need to detect the spreadsheet structure by detecting vertical and horizontal lines.

Using OpenCV, create a binary matrix by converting the document into black and white, defining its threshold in a way that results in all horizontal and vertical lines being one and the rest — a zero. The binary matrix will then contain the spreadsheet structure.

Using the extracted text and spreadsheet structure, the spreadsheet itself can be extracted in an editable format like Excel.

## Summing Up

Digitizing any complex document comes with its own set of problems. The best approach to solving them is to approach them one by one, researching the best tools for the job, testing them, and comparing results.

The approaches I’ve described work on any document type despite its type, as individual challenges can be similar despite the document type being completely different.

For example, I have experience in working on a passport detection solution where the text recognition challenges were very similar, and we’ve used some of the same techniques.

Knowing your OCR tools, being well-versed in coding neural networks and having decent experience in the field of custom AI development will help overcome any document digitization challenges.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="google-generative-ai-embeddings-ai-studio-gemini-api.md">
<details>
<summary>Google Generative AI Embeddings (AI Studio & Gemini API)</summary>

Phase: [EXPLOITATION]

# Google Generative AI Embeddings (AI Studio & Gemini API)

**Source URL:** <https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/>

This will help you get started with Google Generative AI embedding models using LangChain. For detailed documentation on `GoogleGenerativeAIEmbeddings` features and configuration options, please refer to the [API reference](https://reference.langchain.com/python/langchain-google-genai/embeddings/GoogleGenerativeAIEmbeddings).

## Overview

`gemini-embedding-2-preview` natively supports text, image, video, audio, and PDF inputs via the Google GenAI SDK’s `embed_content()` API. However, the LangChain `Embeddings` interface (`embed_query` / `embed_documents`) currently only accepts text inputs. Multimodal embedding support in LangChain is planned for a future release. For multimodal use cases today, use the [Google GenAI SDK](https://ai.google.dev/gemini-api/docs) directly.

### Integration details

## Setup

To access Google Gemini embedding models you’ll need to create a Google Cloud project, enable the Generative Language API, get an API key, and install the `langchain-google-genai` integration package.

### Credentials

Head to [Google AI Studio](https://aistudio.google.com/apikey) to sign up and generate an API key. See the [Gemini API keys documentation](https://ai.google.dev/gemini-api/docs/api-key) for more details. Once you’ve done this set the `GOOGLE_API_KEY` environment variable:

```
import getpass
import os

if not os.getenv("GOOGLE_API_KEY"):
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")
```

### Installation

The LangChain Google Generative AI integration lives in the `langchain-google-genai` package:

```
pip install -qU langchain-google-genai
```

## Instantiation

Now we can instantiate our model object and generate embeddings:

```
from langchain_google_genai import GoogleGenerativeAIEmbeddings

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
vector = embeddings.embed_query("hello, world!")
vector[:5]
```

```
[-0.024917153641581535,
 0.012005362659692764,
 -0.003886754624545574,
 -0.05774897709488869,
 0.0020742062479257584]
```

### Reduced dimensionality

`gemini-embedding-2-preview` supports flexible output dimensions via Matryoshka Representation Learning (MRL). You can reduce dimensionality to optimize storage and latency:

```
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    output_dimensionality=768,  # Suggested: 768, 1536, or 3072 (default)
)
vector = embeddings.embed_query("hello, world!")
len(vector)
```

```
768
```

## Batch

You can also embed multiple strings at once for a processing speedup:

```
vectors = embeddings.embed_documents(
    [
        "Today is Monday",
        "Today is Tuesday",
        "Today is April Fools day",
    ]
)
len(vectors), len(vectors[0])
```

```
(3, 768)
```

## Indexing and retrieval

Embedding models are often used in retrieval-augmented generation (RAG) flows, both as part of indexing data as well as later retrieving it. For more detailed instructions, please see our [RAG tutorials](https://docs.langchain.com/oss/python/langchain/rag).Below, see how to index and retrieve data using the `embeddings` object we initialized above. In this example, we will index and retrieve a sample document in the `InMemoryVectorStore`.

```
# Create a vector store with a sample text
from langchain_core.vectorstores import InMemoryVectorStore

text = "LangChain is the framework for building context-aware reasoning applications"

vectorstore = InMemoryVectorStore.from_texts(
    [text],
    embedding=embeddings,
)

# Use the vectorstore as a retriever
retriever = vectorstore.as_retriever()

# Retrieve the most similar text
retrieved_documents = retriever.invoke("What is LangChain?")

# show the retrieved document's content
retrieved_documents[0].page_content
```

```
'LangChain is the framework for building context-aware reasoning applications'
```

## Task type

`GoogleGenerativeAIEmbeddings` optionally support a `task_type`, which currently must be one of:

- `SEMANTIC_SIMILARITY`: Used to generate embeddings that are optimized to assess text similarity.
- `CLASSIFICATION`: Used to generate embeddings that are optimized to classify texts according to preset labels.
- `CLUSTERING`: Used to generate embeddings that are optimized to cluster texts based on their similarities.
- `RETRIEVAL_DOCUMENT`, `RETRIEVAL_QUERY`, `QUESTION_ANSWERING`, and `FACT_VERIFICATION`: Used to generate embeddings that are optimized for document search or information retrieval.
- `CODE_RETRIEVAL_QUERY`: Used to retrieve a code block based on a natural language query, such as sort an array or reverse a linked list. Embeddings of the code blocks are computed using `RETRIEVAL_DOCUMENT`.

By default, we use `RETRIEVAL_DOCUMENT` in the `embed_documents` method and `RETRIEVAL_QUERY` in the `embed_query` method. If you provide a task type, we will use that for all methods.

```
pip install -qU matplotlib scikit-learn
```

```
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

query_embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview", task_type="RETRIEVAL_QUERY"
)
doc_embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview", task_type="RETRIEVAL_DOCUMENT"
)

q_embed = query_embeddings.embed_query("What is the capital of France?")
d_embed = doc_embeddings.embed_documents(
    ["The capital of France is Paris.", "Philipp likes to eat pizza."]
)

for i, d in enumerate(d_embed):
    print(f"Document {i + 1}:")
    print(f"Cosine similarity with query: {cosine_similarity([q_embed], [d])[0][0]}")
    print("---")
```

```
Document 1:
Cosine similarity with query: 0.7892893360164779
---
Document 2:
Cosine similarity with query: 0.5438283285204146
---
```

## Additional configuration

You can pass the following parameters to `GoogleGenerativeAIEmbeddings` to customize the SDK’s behavior:

- `base_url`: Custom base URL for the API client (e.g., a custom endpoint)
- `output_dimensionality`: Reduce the dimensionality of returned embeddings (e.g., `output_dimensionality=256`)
- `request_options`: Request options dict (e.g., `{"timeout": 10}`)
- `additional_headers`: Additional HTTP headers to include in API requests
- `client_args`: Additional arguments to pass to the underlying HTTP client

## API reference

For detailed documentation on `GoogleGenerativeAIEmbeddings` features and configuration options, please refer to the [API reference](https://reference.langchain.com/python/langchain-google-genai/embeddings/GoogleGenerativeAIEmbeddings).

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="image-understanding-with-gemini.md">
<details>
<summary>Image understanding with Gemini</summary>

Phase: [EXPLOITATION]

# Image understanding with Gemini

**Source URL:** <https://ai.google.dev/gemini-api/docs/image-understanding>

Gemini models are built to be multimodal from the ground up, unlocking a wide
range of image processing and computer vision tasks including but not limited to
image captioning, classification, and visual question answering without having
to train specialized ML models.

In addition to their general multimodal capabilities, Gemini models offer
**enhanced accuracy** for specific use cases like [object detection](https://ai.google.dev/gemini-api/docs/image-understanding#object-detection) and [segmentation](https://ai.google.dev/gemini-api/docs/image-understanding#segmentation), through additional
training.

## Passing images to Gemini

You can provide images as input to Gemini using two methods:

- [Passing inline image data](https://ai.google.dev/gemini-api/docs/image-understanding#inline-image): Ideal for smaller files (total request
size less than 20MB, including prompts).
- [Uploading images using the File API](https://ai.google.dev/gemini-api/docs/image-understanding#upload-image): Recommended for larger files or for
reusing images across multiple requests.

### Passing inline image data

You can pass inline image data in the
request to `generateContent`. You can provide image data as Base64 encoded
strings or by reading local files directly (depending on the language).

The following example shows how to read an image from a local file and pass
it to `generateContent` API for processing.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding#rest)More

```
  from google import genai
  from google.genai import types

  with open('path/to/small-sample.jpg', 'rb') as f:
      image_bytes = f.read()

  client = genai.Client()
  response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=[\
      types.Part.from_bytes(\
        data=image_bytes,\
        mime_type='image/jpeg',\
      ),\
      'Caption this image.'\
    ]
  )

  print(response.text)
```

```
import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});
const base64ImageFile = fs.readFileSync("path/to/small-sample.jpg", {
  encoding: "base64",
});

const contents = [\
  {\
    inlineData: {\
      mimeType: "image/jpeg",\
      data: base64ImageFile,\
    },\
  },\
  { text: "Caption this image." },\
];

const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: contents,
});
console.log(response.text);
```

```
bytes, _ := os.ReadFile("path/to/small-sample.jpg")

parts := []*genai.Part{
  genai.NewPartFromBytes(bytes, "image/jpeg"),
  genai.NewPartFromText("Caption this image."),
}

contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
  ctx,
  "gemini-3-flash-preview",
  contents,
  nil,
)

fmt.Println(result.Text())
```

```
IMG_PATH="/path/to/your/image1.jpg"

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
B64FLAGS="--input"
else
B64FLAGS="-w0"
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
-H "x-goog-api-key: $GEMINI_API_KEY" \
-H 'Content-Type: application/json' \
-X POST \
-d '{
    "contents": [{\
    "parts":[\
        {\
            "inline_data": {\
            "mime_type":"image/jpeg",\
            "data": "'"$(base64 $B64FLAGS $IMG_PATH)"'"\
            }\
        },\
        {"text": "Caption this image."},\
    ]\
    }]
}' 2> /dev/null
```

You can also fetch an image from a URL, convert it to bytes, and pass it to
`generateContent` as shown in the following examples.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding#rest)More

```
from google import genai
from google.genai import types

import requests

image_path = "https://goo.gle/instrument-img"
image_bytes = requests.get(image_path).content
image = types.Part.from_bytes(
  data=image_bytes, mime_type="image/jpeg"
)

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=["What is this image?", image],
)

print(response.text)
```

```
import { GoogleGenAI } from "@google/genai";

async function main() {
  const ai = new GoogleGenAI({});

  const imageUrl = "https://goo.gle/instrument-img";

  const response = await fetch(imageUrl);
  const imageArrayBuffer = await response.arrayBuffer();
  const base64ImageData = Buffer.from(imageArrayBuffer).toString('base64');

  const result = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: [\
    {\
      inlineData: {\
        mimeType: 'image/jpeg',\
        data: base64ImageData,\
      },\
    },\
    { text: "Caption this image." }\
  ],
  });
  console.log(result.text);
}

main();
```

```
package main

import (
  "context"
  "fmt"
  "os"
  "io"
  "net/http"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  // Download the image.
  imageResp, _ := http.Get("https://goo.gle/instrument-img")

  imageBytes, _ := io.ReadAll(imageResp.Body)

  parts := []*genai.Part{
    genai.NewPartFromBytes(imageBytes, "image/jpeg"),
    genai.NewPartFromText("Caption this image."),
  }

  contents := []*genai.Content{
    genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
    ctx,
    "gemini-3-flash-preview",
    contents,
    nil,
  )

  fmt.Println(result.Text())
}
```

```
IMG_URL="https://goo.gle/instrument-img"

MIME_TYPE=$(curl -sIL "$IMG_URL" | grep -i '^content-type:' | awk -F ': ' '{print $2}' | sed 's/\r$//' | head -n 1)
if [[ -z "$MIME_TYPE" || ! "$MIME_TYPE" == image/* ]]; then
  MIME_TYPE="image/jpeg"
fi

# Check for macOS
if [[ "$(uname)" == "Darwin" ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -b 0)
elif [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64)
else
  IMAGE_B64=$(curl -sL "$IMG_URL" | base64 -w0)
fi

curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
            {\
              "inline_data": {\
                "mime_type":"'"$MIME_TYPE"'",\
                "data": "'"$IMAGE_B64"'"\
              }\
            },\
            {"text": "Caption this image."}\
        ]\
      }]
    }' 2> /dev/null
```

### Uploading images using the File API

For large files or to be able to use the same image file repeatedly, use the
Files API. The following code uploads an image file and then uses the file in a
call to `generateContent`. See the [Files API guide](https://ai.google.dev/gemini-api/docs/files) for
more information and examples.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding#rest)More

```
from google import genai

client = genai.Client()

my_file = client.files.upload(file="path/to/sample.jpg")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[my_file, "Caption this image."],
)

print(response.text)
```

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";

const ai = new GoogleGenAI({});

async function main() {
  const myfile = await ai.files.upload({
    file: "path/to/sample.jpg",
    config: { mimeType: "image/jpeg" },
  });

  const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: createUserContent([\
      createPartFromUri(myfile.uri, myfile.mimeType),\
      "Caption this image.",\
    ]),
  });
  console.log(response.text);
}

await main();
```

```
package main

import (
  "context"
  "fmt"
  "os"
  "google.golang.org/genai"
)

func main() {
  ctx := context.Background()
  client, err := genai.NewClient(ctx, nil)
  if err != nil {
      log.Fatal(err)
  }

  uploadedFile, _ := client.Files.UploadFromPath(ctx, "path/to/sample.jpg", nil)

  parts := []*genai.Part{
      genai.NewPartFromText("Caption this image."),
      genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
  }

  contents := []*genai.Content{
      genai.NewContentFromParts(parts, genai.RoleUser),
  }

  result, _ := client.Models.GenerateContent(
      ctx,
      "gemini-3-flash-preview",
      contents,
      nil,
  )

  fmt.Println(result.Text())
}
```

```
IMAGE_PATH="path/to/sample.jpg"
MIME_TYPE=$(file -b --mime-type "${IMAGE_PATH}")
NUM_BYTES=$(wc -c < "${IMAGE_PATH}")
DISPLAY_NAME=IMAGE

tmp_header_file=upload-header.tmp

# Initial resumable request defining metadata.
# The upload url is in the response headers dump them to a file.
curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME}'}}" 2> /dev/null

upload_url=$(grep -i "x-goog-upload-url: " "${tmp_header_file}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file}"

# Upload the actual bytes.
curl "${upload_url}" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Length: ${NUM_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${IMAGE_PATH}" 2> /dev/null > file_info.json

file_uri=$(jq -r ".file.uri" file_info.json)
echo file_uri=$file_uri

# Now generate content using that file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          {"file_data":{"mime_type": "'"${MIME_TYPE}"'", "file_uri": "'"${file_uri}"'"}},\
          {"text": "Caption this image."}]\
        }]
      }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Prompting with multiple images

You can provide multiple images in a single prompt by including multiple image
`Part` objects in the `contents` array. These can be a mix of inline data
(local files or URLs) and File API references.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding#python)[JavaScript](https://ai.google.dev/gemini-api/docs/image-understanding#javascript)[Go](https://ai.google.dev/gemini-api/docs/image-understanding#go)[REST](https://ai.google.dev/gemini-api/docs/image-understanding#rest)More

```
from google import genai
from google.genai import types

client = genai.Client()

# Upload the first image
image1_path = "path/to/image1.jpg"
uploaded_file = client.files.upload(file=image1_path)

# Prepare the second image as inline data
image2_path = "path/to/image2.png"
with open(image2_path, 'rb') as f:
    img2_bytes = f.read()

# Create the prompt with text and multiple images
response = client.models.generate_content(

    model="gemini-3-flash-preview",
    contents=[\
        "What is different between these two images?",\
        uploaded_file,  # Use the uploaded file reference\
        types.Part.from_bytes(\
            data=img2_bytes,\
            mime_type='image/png'\
        )\
    ]
)

print(response.text)
```

```
import {
  GoogleGenAI,
  createUserContent,
  createPartFromUri,
} from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({});

async function main() {
  // Upload the first image
  const image1_path = "path/to/image1.jpg";
  const uploadedFile = await ai.files.upload({
    file: image1_path,
    config: { mimeType: "image/jpeg" },
  });

  // Prepare the second image as inline data
  const image2_path = "path/to/image2.png";
  const base64Image2File = fs.readFileSync(image2_path, {
    encoding: "base64",
  });

  // Create the prompt with text and multiple images

  const response = await ai.models.generateContent({

    model: "gemini-3-flash-preview",
    contents: createUserContent([\
      "What is different between these two images?",\
      createPartFromUri(uploadedFile.uri, uploadedFile.mimeType),\
      {\
        inlineData: {\
          mimeType: "image/png",\
          data: base64Image2File,\
        },\
      },\
    ]),
  });
  console.log(response.text);
}

await main();
```

```
// Upload the first image
image1Path := "path/to/image1.jpg"
uploadedFile, _ := client.Files.UploadFromPath(ctx, image1Path, nil)

// Prepare the second image as inline data
image2Path := "path/to/image2.jpeg"
imgBytes, _ := os.ReadFile(image2Path)

parts := []*genai.Part{
  genai.NewPartFromText("What is different between these two images?"),
  genai.NewPartFromBytes(imgBytes, "image/jpeg"),
  genai.NewPartFromURI(uploadedFile.URI, uploadedFile.MIMEType),
}

contents := []*genai.Content{
  genai.NewContentFromParts(parts, genai.RoleUser),
}

result, _ := client.Models.GenerateContent(
  ctx,
  "gemini-3-flash-preview",
  contents,
  nil,
)

fmt.Println(result.Text())
```

```
# Upload the first image
IMAGE1_PATH="path/to/image1.jpg"
MIME1_TYPE=$(file -b --mime-type "${IMAGE1_PATH}")
NUM1_BYTES=$(wc -c < "${IMAGE1_PATH}")
DISPLAY_NAME1=IMAGE1

tmp_header_file1=upload-header1.tmp

curl "https://generativelanguage.googleapis.com/upload/v1beta/files" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -D upload-header1.tmp \
  -H "X-Goog-Upload-Protocol: resumable" \
  -H "X-Goog-Upload-Command: start" \
  -H "X-Goog-Upload-Header-Content-Length: ${NUM1_BYTES}" \
  -H "X-Goog-Upload-Header-Content-Type: ${MIME1_TYPE}" \
  -H "Content-Type: application/json" \
  -d "{'file': {'display_name': '${DISPLAY_NAME1}'}}" 2> /dev/null

upload_url1=$(grep -i "x-goog-upload-url: " "${tmp_header_file1}" | cut -d" " -f2 | tr -d "\r")
rm "${tmp_header_file1}"

curl "${upload_url1}" \
  -H "Content-Length: ${NUM1_BYTES}" \
  -H "X-Goog-Upload-Offset: 0" \
  -H "X-Goog-Upload-Command: upload, finalize" \
  --data-binary "@${IMAGE1_PATH}" 2> /dev/null > file_info1.json

file1_uri=$(jq ".file.uri" file_info1.json)
echo file1_uri=$file1_uri

# Prepare the second image (inline)
IMAGE2_PATH="path/to/image2.png"
MIME2_TYPE=$(file -b --mime-type "${IMAGE2_PATH}")

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi
IMAGE2_BASE64=$(base64 $B64FLAGS $IMAGE2_PATH)

# Now generate content using both images
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d '{
      "contents": [{\
        "parts":[\
          {"text": "What is different between these two images?"},\
          {"file_data":{"mime_type": "'"${MIME1_TYPE}"'", "file_uri": '$file1_uri'}},\
          {\
            "inline_data": {\
              "mime_type":"'"${MIME2_TYPE}"'",\
              "data": "'"$IMAGE2_BASE64"'"\
            }\
          }\
        ]\
      }]
    }' 2> /dev/null > response.json

cat response.json
echo

jq ".candidates[].content.parts[].text" response.json
```

## Object detection

Models are trained to detect objects in an
image and get their bounding box coordinates. The coordinates, relative to image
dimensions, scale to \[0, 1000\]. You need to descale these coordinates based on
your original image size.

[Python](https://ai.google.dev/gemini-api/docs/image-understanding#python)More

```
from google import genai
from google.genai import types
from PIL import Image
import json

client = genai.Client()
prompt = "Detect the all of the prominent items in the image. The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000."

image = Image.open("/path/to/image.png")

config = types.GenerateContentConfig(
  response_mime_type="application/json"
  )

response = client.models.generate_content(model="gemini-3-flash-preview",
                                          contents=[image, prompt],
                                          config=config
                                          )

width, height = image.size
bounding_boxes = json.loads(response.text)

converted_bounding_boxes = []
for bounding_box in bounding_boxes:
    abs_y1 = int(bounding_box["box_2d"][0]/1000 * height)
    abs_x1 = int(bounding_box["box_2d"][1]/1000 * width)
    abs_y2 = int(bounding_box["box_2d"][2]/1000 * height)
    abs_x2 = int(bounding_box["box_2d"][3]/1000 * width)
    converted_bounding_boxes.append([abs_x1, abs_y1, abs_x2, abs_y2])

print("Image size: ", width, height)
print("Bounding boxes:", converted_bounding_boxes)
```

For more examples, check following notebooks in the [Gemini Cookbook](https://github.com/google-gemini/cookbook):

- [2D spatial understanding notebook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb)
- [Experimental 3D pointing notebook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/examples/Spatial_understanding_3d.ipynb)

## Segmentation

Starting with Gemini 2.5, models not only detect items but also segment them
and provide their contour masks.

The model predicts a JSON list, where each item represents a segmentation mask.
Each item has a bounding box ("`box_2d`") in the format `[y0, x0, y1, x1]` with
normalized coordinates between 0 and 1000, a label ("`label`") that identifies
the object, and finally the segmentation mask inside the bounding box, as base64
encoded png that is a probability map with values between 0 and 255.
The mask needs to be resized to match the bounding box dimensions, then
binarized at your confidence threshold (127 for the midpoint).

[Python](https://ai.google.dev/gemini-api/docs/image-understanding#python)More

````
from google import genai
from google.genai import types
from PIL import Image, ImageDraw
import io
import base64
import json
import numpy as np
import os

client = genai.Client()

def parse_json(json_output: str):
  # Parsing out the markdown fencing
  lines = json_output.splitlines()
  for i, line in enumerate(lines):
    if line == "```json":
      json_output = "\n".join(lines[i+1:])  # Remove everything before "```json"
      output = json_output.split("```")[0]  # Remove everything after the closing "```"
      break  # Exit the loop once "```json" is found
  return json_output

def extract_segmentation_masks(image_path: str, output_dir: str = "segmentation_outputs"):
  # Load and resize image
  im = Image.open(image_path)
  im.thumbnail([1024, 1024], Image.Resampling.LANCZOS)

  prompt = """
  Give the segmentation masks for the wooden and glass items.
  Output a JSON list of segmentation masks where each entry contains the 2D
  bounding box in the key "box_2d", the segmentation mask in key "mask", and
  the text label in the key "label". Use descriptive labels.
  """

  config = types.GenerateContentConfig(
    thinking_config=types.ThinkingConfig(thinking_budget=0) # set thinking_budget to 0 for better results in object detection
  )

  response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[prompt, im], # Pillow images can be directly passed as inputs (which will be converted by the SDK)
    config=config
  )

  # Parse JSON response
  items = json.loads(parse_json(response.text))

  # Create output directory
  os.makedirs(output_dir, exist_ok=True)

  # Process each mask
  for i, item in enumerate(items):
      # Get bounding box coordinates
      box = item["box_2d"]
      y0 = int(box[0] / 1000 * im.size[1])
      x0 = int(box[1] / 1000 * im.size[0])
      y1 = int(box[2] / 1000 * im.size[1])
      x1 = int(box[3] / 1000 * im.size[0])

      # Skip invalid boxes
      if y0 >= y1 or x0 >= x1:
          continue

      # Process mask
      png_str = item["mask"]
      if not png_str.startswith("data:image/png;base64,"):
          continue

      # Remove prefix
      png_str = png_str.removeprefix("data:image/png;base64,")
      mask_data = base64.b64decode(png_str)
      mask = Image.open(io.BytesIO(mask_data))

      # Resize mask to match bounding box
      mask = mask.resize((x1 - x0, y1 - y0), Image.Resampling.BILINEAR)

      # Convert mask to numpy array for processing
      mask_array = np.array(mask)

      # Create overlay for this mask
      overlay = Image.new('RGBA', im.size, (0, 0, 0, 0))
      overlay_draw = ImageDraw.Draw(overlay)

      # Create overlay for the mask
      color = (255, 255, 255, 200)
      for y in range(y0, y1):
          for x in range(x0, x1):
              if mask_array[y - y0, x - x0] > 128:  # Threshold for mask
                  overlay_draw.point((x, y), fill=color)

      # Save individual mask and its overlay
      mask_filename = f"{item['label']}_{i}_mask.png"
      overlay_filename = f"{item['label']}_{i}_overlay.png"

      mask.save(os.path.join(output_dir, mask_filename))

      # Create and save overlay
      composite = Image.alpha_composite(im.convert('RGBA'), overlay)
      composite.save(os.path.join(output_dir, overlay_filename))
      print(f"Saved mask and overlay for {item['label']} to {output_dir}")

# Example usage
if __name__ == "__main__":
  extract_segmentation_masks("path/to/image.png")
````

Check the
[segmentation example](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Spatial_understanding.ipynb#scrollTo=WQJTJ8wdGOKx)
in the cookbook guide for a more detailed example.

https://ai.google.dev/static/gemini-api/docs/images/segmentation.jpgAn example segmentation output with objects and segmentation masks

## Supported image formats

Gemini supports the following image format MIME types:

- PNG - `image/png`
- JPEG - `image/jpeg`
- WEBP - `image/webp`
- HEIC - `image/heic`
- HEIF - `image/heif`

To learn about other file input methods, see the
[File input methods](https://ai.google.dev/gemini-api/docs/file-input-methods) guide.

## Capabilities

All Gemini model versions are multimodal and can be utilized in a wide range of
image processing and computer vision tasks including but not limited to image captioning,
visual question and answering, image classification, object detection and segmentation.

Gemini can reduce the need to use specialized ML models depending on your quality and performance requirements.

The latest model versions are specifically trained improve accuracy of
specialized tasks in addition to generic capabilities, like enhanced
[object detection](https://ai.google.dev/gemini-api/docs/image-understanding#object-detection) and [segmentation](https://ai.google.dev/gemini-api/docs/image-understanding#segmentation).

## Limitations and key technical information

### File limit

Gemini models support a maximum of 3,600 image files per request.

### Token calculation

- 258 tokens if both dimensions <= 384 pixels.
Larger images are tiled into 768x768 pixel tiles, each costing 258 tokens.

A rough formula for calculating the number of tiles is as follows:

- Calculate the crop unit size which is roughly: floor(min(width, height) / 1.5).
- Divide each dimension by the crop unit size and multiply together to get the
number of tiles.

For example, for an image of dimensions 960x540 would have a crop unit size
of 360. Divide each dimension by 360 and the number of tile is 3 * 2 = 6.

### Media resolution

Gemini 3 introduces granular control over multimodal vision processing with the
`media_resolution` parameter. The `media_resolution` parameter determines the
**maximum number of tokens allocated per input image or video frame.**
Higher resolutions improve the model's ability to
read fine text or identify small details, but increase token usage and latency.

For more details about the parameter and how it can impact token calculations,
see the [media resolution](https://ai.google.dev/gemini-api/docs/media-resolution) guide.

## Tips and best practices

- Verify that images are correctly rotated.
- Use clear, non-blurry images.
- When using a single image with text, place the text prompt _after_ the image part in the `contents` array.

## What's next

This guide shows you how to upload image files and generate text outputs from image
inputs. To learn more, see the following resources:

- [Files API](https://ai.google.dev/gemini-api/docs/files): Learn more about uploading and managing files for use with Gemini.
- [System instructions](https://ai.google.dev/gemini-api/docs/text-generation#system-instructions):
System instructions let you steer the behavior of the model based on your
specific needs and use cases.
- [File prompting strategies](https://ai.google.dev/gemini-api/docs/files#prompt-guide): The
Gemini API supports prompting with text, image, audio, and video data, also
known as multimodal prompting.
- [Safety guidance](https://ai.google.dev/gemini-api/docs/safety-guidance): Sometimes generative
AI models produce unexpected outputs, such as outputs that are inaccurate,
biased, or offensive. Post-processing and human evaluation are essential to
limit the risk of harm from such outputs.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="langgraph-quickstart.md">
<details>
<summary>LangGraph quickstart</summary>

Phase: [EXPLOITATION]

# LangGraph quickstart

**Source URL:** <https://langchain-ai.github.io/langgraph/agents/agents/>

Agents combine language models with [tools](https://docs.langchain.com/oss/python/langchain/tools) to create systems that can reason about tasks, decide which tools to use, and iteratively work towards solutions.[`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) provides a production-ready agent implementation.[An LLM Agent runs tools in a loop to achieve a goal](https://simonwillison.net/2025/Sep/18/agents/).
An agent runs until a stop condition is met - i.e., when the model emits a final output or an iteration limit is reached.

[`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) builds a **graph**-based agent runtime using [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview). A graph consists of nodes (steps) and edges (connections) that define how your agent processes information. The agent moves through this graph, executing nodes like the model node (which calls the model), the tools node (which executes tools), or middleware.Learn more about the [Graph API](https://docs.langchain.com/oss/python/langgraph/graph-api).

## Core components

### Model

The [model](https://docs.langchain.com/oss/python/langchain/models) is the reasoning engine of your agent. It can be specified in multiple ways, supporting both static and dynamic model selection.

#### Static model

Static models are configured once when creating the agent and remain unchanged throughout execution. This is the most common and straightforward approach.To initialize a static model from a model identifier string:

```
from langchain.agents import create_agent

agent = create_agent("openai:gpt-5", tools=tools)
```

Model identifier strings support automatic inference (e.g., `"gpt-5"` will be inferred as `"openai:gpt-5"`). Refer to the [reference](https://reference.langchain.com/python/langchain/chat_models/base/init_chat_model) to see a full list of model identifier string mappings.

For more control over the model configuration, initialize a model instance directly using the provider package. In this example, we use [`ChatOpenAI`](https://reference.langchain.com/python/langchain-openai/chat_models/base/ChatOpenAI). See [Chat models](https://docs.langchain.com/oss/python/integrations/chat) for other available chat model classes.

```
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model="gpt-5",
    temperature=0.1,
    max_tokens=1000,
    timeout=30
    # ... (other params)
)
agent = create_agent(model, tools=tools)
```

Model instances give you complete control over configuration. Use them when you need to set specific [parameters](https://docs.langchain.com/oss/python/langchain/models#parameters) like `temperature`, `max_tokens`, `timeouts`, `base_url`, and other provider-specific settings. Refer to the [reference](https://docs.langchain.com/oss/python/integrations/providers/all_providers) to see available params and methods on your model.

#### Dynamic model

Dynamic models are selected at runtime based on the current state and context. This enables sophisticated routing logic and cost optimization.To use a dynamic model, create middleware using the [`@wrap_model_call`](https://reference.langchain.com/python/langchain/agents/middleware/types/wrap_model_call) decorator that modifies the model in the request:

```
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse

basic_model = ChatOpenAI(model="gpt-4.1-mini")
advanced_model = ChatOpenAI(model="gpt-4.1")

@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model based on conversation complexity."""
    message_count = len(request.state["messages"])

    if message_count > 10:
        # Use an advanced model for longer conversations
        model = advanced_model
    else:
        model = basic_model

    return handler(request.override(model=model))

agent = create_agent(
    model=basic_model,  # Default model
    tools=tools,
    middleware=[dynamic_model_selection]
)
```

Pre-bound models (models with [`bind_tools`](https://reference.langchain.com/python/langchain-core/language_models/chat_models/BaseChatModel/bind_tools) already called) are not supported when using structured output. If you need dynamic model selection with structured output, ensure the models passed to the middleware are not pre-bound.

For model configuration details, see [Models](https://docs.langchain.com/oss/python/langchain/models). For dynamic model selection patterns, see [Dynamic model in middleware](https://docs.langchain.com/oss/python/langchain/middleware#dynamic-model).

### Tools

Tools give agents the ability to take actions. Agents go beyond simple model-only tool binding by facilitating:

- Multiple tool calls in sequence (triggered by a single prompt)
- Parallel tool calls when appropriate
- Dynamic tool selection based on previous results
- Tool retry logic and error handling
- State persistence across tool calls

For more information, see [Tools](https://docs.langchain.com/oss/python/langchain/tools).

#### Static tools

Static tools are defined when creating the agent and remain unchanged throughout execution. This is the most common and straightforward approach.To define an agent with static tools, pass a list of the tools to the agent.

Tools can be specified as plain Python functions or coroutines.The [tool decorator](https://docs.langchain.com/oss/python/langchain/tools#create-tools) can be used to customize tool names, descriptions, argument schemas, and other properties.

```
from langchain.tools import tool
from langchain.agents import create_agent

@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

@tool
def get_weather(location: str) -> str:
    """Get weather information for a location."""
    return f"Weather in {location}: Sunny, 72°F"

agent = create_agent(model, tools=[search, get_weather])
```

If an empty tool list is provided, the agent will consist of a single LLM node without tool-calling capabilities.

#### Dynamic tools

With dynamic tools, the set of tools available to the agent is modified at runtime rather than defined all upfront. Not every tool is appropriate for every situation. Too many tools may overwhelm the model (overload context) and increase errors; too few limit capabilities. Dynamic tool selection enables adapting the available toolset based on authentication state, user permissions, feature flags, or conversation stage.There are two approaches depending on whether tools are known ahead of time:

- Filtering pre-registered tools

- Runtime tool registration


When all possible tools are known at agent creation time, you can pre-register them and dynamically filter which ones are exposed to the model based on state, permissions, or context.

- State

- Store

- Runtime Context


Enable advanced tools only after certain conversation milestones:

```
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from typing import Callable

@wrap_model_call
def state_based_tools(
    request: ModelRequest,
    handler: Callable[[ModelRequest], ModelResponse]
) -> ModelResponse:
    """Filter tools based on conversation State."""
    # Read from State: check if user has authenticated
    state = request.state
    is_authenticated = state.get("authenticated", False)
    message_count = len(state["messages"])

    # Only enable sensitive tools after authentication
    if not is_authenticated:
        tools = [t for t in request.tools if t.name.startswith("public_")]
        request = request.override(tools=tools)
    elif message_count < 5:
        # Limit tools early in conversation
        tools = [t for t in request.tools if t.name != "advanced_search"]
        request = request.override(tools=tools)

    return handler(request)

agent = create_agent(
    model="gpt-4.1",
    tools=[public_search, private_search, advanced_search],
    middleware=[state_based_tools]
)
```

Filter tools based on user preferences or feature flags in Store:

```
from dataclasses import dataclass
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from typing import Callable
from langgraph.store.memory import InMemoryStore

@dataclass
class Context:
    user_id: str

@wrap_model_call
def store_based_tools(
    request: ModelRequest,
    handler: Callable[[ModelRequest], ModelResponse]
) -> ModelResponse:
    """Filter tools based on Store preferences."""
    user_id = request.runtime.context.user_id

    # Read from Store: get user's enabled features
    store = request.runtime.store
    feature_flags = store.get(("features",), user_id)

    if feature_flags:
        enabled_features = feature_flags.value.get("enabled_tools", [])
        # Only include tools that are enabled for this user
        tools = [t for t in request.tools if t.name in enabled_features]
        request = request.override(tools=tools)

    return handler(request)

agent = create_agent(
    model="gpt-4.1",
    tools=[search_tool, analysis_tool, export_tool],
    middleware=[store_based_tools],
    context_schema=Context,
    store=InMemoryStore()
)
```

Filter tools based on user permissions from Runtime Context:

```
from dataclasses import dataclass
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from typing import Callable

@dataclass
class Context:
    user_role: str

@wrap_model_call
def context_based_tools(
    request: ModelRequest,
    handler: Callable[[ModelRequest], ModelResponse]
) -> ModelResponse:
    """Filter tools based on Runtime Context permissions."""
    # Read from Runtime Context: get user role
    if request.runtime is None or request.runtime.context is None:
        # If no context provided, default to viewer (most restrictive)
        user_role = "viewer"
    else:
        user_role = request.runtime.context.user_role

    if user_role == "admin":
        # Admins get all tools
        pass
    elif user_role == "editor":
        # Editors can't delete
        tools = [t for t in request.tools if t.name != "delete_data"]
        request = request.override(tools=tools)
    else:
        # Viewers get read-only tools
        tools = [t for t in request.tools if t.name.startswith("read_")]
        request = request.override(tools=tools)

    return handler(request)

agent = create_agent(
    model="gpt-4.1",
    tools=[read_data, write_data, delete_data],
    middleware=[context_based_tools],
    context_schema=Context
)
```

This approach is best when:

- All possible tools are known at compile/startup time
- You want to filter based on permissions, feature flags, or conversation state
- Tools are static but their availability is dynamic

See [Dynamically selecting tools](https://docs.langchain.com/oss/python/langchain/middleware/custom#dynamically-selecting-tools) for more examples.

When tools are discovered or created at runtime (e.g., loaded from an MCP server, generated based on user data, or fetched from a remote registry), you need to both register the tools and handle their execution dynamically.This requires two middleware hooks:

1. `wrap_model_call` - Add the dynamic tools to the request
2. `wrap_tool_call` - Handle execution of the dynamically added tools

```
from langchain.tools import tool
from langchain.agents import create_agent
from langchain.agents.middleware import AgentMiddleware, ModelRequest, ToolCallRequest

# A tool that will be added dynamically at runtime
@tool
def calculate_tip(bill_amount: float, tip_percentage: float = 20.0) -> str:
    """Calculate the tip amount for a bill."""
    tip = bill_amount * (tip_percentage / 100)
    return f"Tip: ${tip:.2f}, Total: ${bill_amount + tip:.2f}"

class DynamicToolMiddleware(AgentMiddleware):
    """Middleware that registers and handles dynamic tools."""

    def wrap_model_call(self, request: ModelRequest, handler):
        # Add dynamic tool to the request
        # This could be loaded from an MCP server, database, etc.
        updated = request.override(tools=[*request.tools, calculate_tip])
        return handler(updated)

    def wrap_tool_call(self, request: ToolCallRequest, handler):
        # Handle execution of the dynamic tool
        if request.tool_call["name"] == "calculate_tip":
            return handler(request.override(tool=calculate_tip))
        return handler(request)

agent = create_agent(
    model="gpt-4o",
    tools=[get_weather],  # Only static tools registered here
    middleware=[DynamicToolMiddleware()],
)

# The agent can now use both get_weather AND calculate_tip
result = agent.invoke({
    "messages": [{"role": "user", "content": "Calculate a 20% tip on $85"}]
})
```

This approach is best when:

- Tools are discovered at runtime (e.g., from an MCP server)
- Tools are generated dynamically based on user data or configuration
- You’re integrating with external tool registries

The `wrap_tool_call` hook is required for runtime-registered tools because the agent needs to know how to execute tools that weren’t in the original tool list. Without it, the agent won’t know how to invoke the dynamically added tool.

To learn more about tools, see [Tools](https://docs.langchain.com/oss/python/langchain/tools).

#### Tool error handling

To customize how tool errors are handled, use the [`@wrap_tool_call`](https://reference.langchain.com/python/langchain/agents/middleware/types/wrap_tool_call) decorator to create middleware:

```
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_tool_call
from langchain.messages import ToolMessage

@wrap_tool_call
def handle_tool_errors(request, handler):
    """Handle tool execution errors with custom messages."""
    try:
        return handler(request)
    except Exception as e:
        # Return a custom error message to the model
        return ToolMessage(
            content=f"Tool error: Please check your input and try again. ({str(e)})",
            tool_call_id=request.tool_call["id"]
        )

agent = create_agent(
    model="gpt-4.1",
    tools=[search, get_weather],
    middleware=[handle_tool_errors]
)
```

The agent will return a [`ToolMessage`](https://reference.langchain.com/python/langchain-core/messages/tool/ToolMessage) with the custom error message when a tool fails:

```
[\
    ...\
    ToolMessage(\
        content="Tool error: Please check your input and try again. (division by zero)",\
        tool_call_id="..."\
    ),\
    ...\
]
```

#### Tool use in the ReAct loop

Agents follow the ReAct (“Reasoning + Acting”) pattern, alternating between brief reasoning steps with targeted tool calls and feeding the resulting observations into subsequent decisions until they can deliver a final answer.

Example of ReAct loop

**Prompt:** Identify the current most popular wireless headphones and verify availability.

```
================================ Human Message =================================

Find the most popular wireless headphones right now and check if they're in stock
```

- **Reasoning**: “Popularity is time-sensitive, I need to use the provided search tool.”
- **Acting**: Call `search_products("wireless headphones")`

```
================================== Ai Message ==================================
Tool Calls:
  search_products (call_abc123)
 Call ID: call_abc123
  Args:
    query: wireless headphones
```

```
================================= Tool Message =================================

Found 5 products matching "wireless headphones". Top 5 results: WH-1000XM5, ...
```

- **Reasoning**: “I need to confirm availability for the top-ranked item before answering.”
- **Acting**: Call `check_inventory("WH-1000XM5")`

```
================================== Ai Message ==================================
Tool Calls:
  check_inventory (call_def456)
 Call ID: call_def456
  Args:
    product_id: WH-1000XM5
```

```
================================= Tool Message =================================

Product WH-1000XM5: 10 units in stock
```

- **Reasoning**: “I have the most popular model and its stock status. I can now answer the user’s question.”
- **Acting**: Produce final answer

```
================================== Ai Message ==================================

I found wireless headphones (model WH-1000XM5) with 10 units in stock...
```

### System prompt

You can shape how your agent approaches tasks by providing a prompt. The [`system_prompt`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent(system_prompt)) parameter can be provided as a string:

```
agent = create_agent(
    model,
    tools,
    system_prompt="You are a helpful assistant. Be concise and accurate."
)
```

When no [`system_prompt`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent(system_prompt)) is provided, the agent will infer its task from the messages directly.The [`system_prompt`](https://reference.langchain.com/python/langchain/agents/#langchain.agents.create_agent(system_prompt)) parameter accepts either a `str` or a [`SystemMessage`](https://reference.langchain.com/python/langchain-core/messages/system/SystemMessage). Using a `SystemMessage` gives you more control over the prompt structure, which is useful for provider-specific features like [Anthropic’s prompt caching](https://docs.langchain.com/oss/python/integrations/chat/anthropic#prompt-caching):

```
from langchain.agents import create_agent
from langchain.messages import SystemMessage, HumanMessage

literary_agent = create_agent(
    model="anthropic:claude-sonnet-4-5",
    system_prompt=SystemMessage(
        content=[\
            {\
                "type": "text",\
                "text": "You are an AI assistant tasked with analyzing literary works.",\
            },\
            {\
                "type": "text",\
                "text": "<the entire contents of 'Pride and Prejudice'>",\
                "cache_control": {"type": "ephemeral"}\
            }\
        ]
    )
)

result = literary_agent.invoke(
    {"messages": [HumanMessage("Analyze the major themes in 'Pride and Prejudice'.")]}
)
```

The `cache_control` field with `{"type": "ephemeral"}` tells Anthropic to cache that content block, reducing latency and costs for repeated requests that use the same system prompt.

#### Dynamic system prompt

For more advanced use cases where you need to modify the system prompt based on runtime context or agent state, you can use [middleware](https://docs.langchain.com/oss/python/langchain/middleware).The [`@dynamic_prompt`](https://reference.langchain.com/python/langchain/agents/middleware/types/dynamic_prompt) decorator creates middleware that generates system prompts based on the model request:

```
from typing import TypedDict

from langchain.agents import create_agent
from langchain.agents.middleware import dynamic_prompt, ModelRequest

class Context(TypedDict):
    user_role: str

@dynamic_prompt
def user_role_prompt(request: ModelRequest) -> str:
    """Generate system prompt based on user role."""
    user_role = request.runtime.context.get("user_role", "user")
    base_prompt = "You are a helpful assistant."

    if user_role == "expert":
        return f"{base_prompt} Provide detailed technical responses."
    elif user_role == "beginner":
        return f"{base_prompt} Explain concepts simply and avoid jargon."

    return base_prompt

agent = create_agent(
    model="gpt-4.1",
    tools=[web_search],
    middleware=[user_role_prompt],
    context_schema=Context
)

# The system prompt will be set dynamically based on context
result = agent.invoke(
    {"messages": [{"role": "user", "content": "Explain machine learning"}]},
    context={"user_role": "expert"}
)
```

For more details on message types and formatting, see [Messages](https://docs.langchain.com/oss/python/langchain/messages). For comprehensive middleware documentation, see [Middleware](https://docs.langchain.com/oss/python/langchain/middleware).

### Name

Set an optional [`name`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) for the agent. This is used as the node identifier when adding the agent as a subgraph in [multi-agent systems](https://docs.langchain.com/oss/python/langchain/multi-agent):

```
agent = create_agent(
    model,
    tools,
    name="research_assistant"
)
```

Prefer `snake_case` for agent names (e.g., `research_assistant` instead of `Research Assistant`). Some model providers reject names containing spaces or special characters with errors. Using alphanumeric characters, underscores, and hyphens only ensures compatibility across all providers. The same applies to [tool names](https://docs.langchain.com/oss/python/langchain/tools).

## Invocation

You can invoke an agent by passing an update to its [`State`](https://docs.langchain.com/oss/python/langgraph/graph-api#state). All agents include a [sequence of messages](https://docs.langchain.com/oss/python/langgraph/use-graph-api#messagesstate) in their state; to invoke the agent, pass a new message:

```
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)
```

For streaming steps and / or tokens from the agent, refer to the [streaming](https://docs.langchain.com/oss/python/langchain/streaming) guide.Otherwise, the agent follows the LangGraph [Graph API](https://docs.langchain.com/oss/python/langgraph/use-graph-api) and supports all associated methods, such as `stream` and `invoke`.

Use [LangSmith](https://docs.langchain.com/langsmith/home) to trace, debug, and evaluate your agents.

## Advanced concepts

### Structured output

In some situations, you may want the agent to return an output in a specific format. LangChain provides strategies for structured output via the [`response_format`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) parameter.

#### ToolStrategy

`ToolStrategy` uses artificial tool calling to generate structured output. This works with any model that supports tool calling. `ToolStrategy` should be used when provider-native structured output (via [`ProviderStrategy`](https://docs.langchain.com/oss/python/langchain/agents#providerstrategy)) is not available or reliable.

```
from pydantic import BaseModel
from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

class ContactInfo(BaseModel):
    name: str
    email: str
    phone: str

agent = create_agent(
    model="gpt-4.1-mini",
    tools=[search_tool],
    response_format=ToolStrategy(ContactInfo)
)

result = agent.invoke({
    "messages": [{"role": "user", "content": "Extract contact info from: John Doe, john@example.com, (555) 123-4567"}]
})

result["structured_response"]
# ContactInfo(name='John Doe', email='john@example.com', phone='(555) 123-4567')
```

#### ProviderStrategy

`ProviderStrategy` uses the model provider’s native structured output generation. This is more reliable but only works with providers that support native structured output:

```
from langchain.agents.structured_output import ProviderStrategy

agent = create_agent(
    model="gpt-4.1",
    response_format=ProviderStrategy(ContactInfo)
)
```

As of `langchain 1.0`, simply passing a schema (e.g., `response_format=ContactInfo`) will default to `ProviderStrategy` if the model supports native structured output. It will fall back to `ToolStrategy` otherwise.

To learn about structured output, see [Structured output](https://docs.langchain.com/oss/python/langchain/structured-output).

### Memory

Agents maintain conversation history automatically through the message state. You can also configure the agent to use a custom state schema to remember additional information during the conversation.Information stored in the state can be thought of as the [short-term memory](https://docs.langchain.com/oss/python/langchain/short-term-memory) of the agent:Custom state schemas must extend [`AgentState`](https://reference.langchain.com/python/langchain/agents/middleware/types/AgentState) as a `TypedDict`.There are two ways to define custom state:

1. Via [middleware](https://docs.langchain.com/oss/python/langchain/middleware) (preferred)
2. Via [`state_schema`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.AgentMiddleware.state_schema) on [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent)

#### Defining state via middleware

Use middleware to define custom state when your custom state needs to be accessed by specific middleware hooks and tools attached to said middleware.

```
from langchain.agents import AgentState
from langchain.agents.middleware import AgentMiddleware
from typing import Any

class CustomState(AgentState):
    user_preferences: dict

class CustomMiddleware(AgentMiddleware):
    state_schema = CustomState
    tools = [tool1, tool2]

    def before_model(self, state: CustomState, runtime) -> dict[str, Any] | None:
        ...

agent = create_agent(
    model,
    tools=tools,
    middleware=[CustomMiddleware()]
)

# The agent can now track additional state beyond messages
result = agent.invoke({
    "messages": [{"role": "user", "content": "I prefer technical explanations"}],
    "user_preferences": {"style": "technical", "verbosity": "detailed"},
})
```

#### Defining state via `state_schema`

Use the [`state_schema`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.AgentMiddleware.state_schema) parameter as a shortcut to define custom state that is only used in tools.

```
from langchain.agents import AgentState

class CustomState(AgentState):
    user_preferences: dict

agent = create_agent(
    model,
    tools=[tool1, tool2],
    state_schema=CustomState
)
# The agent can now track additional state beyond messages
result = agent.invoke({
    "messages": [{"role": "user", "content": "I prefer technical explanations"}],
    "user_preferences": {"style": "technical", "verbosity": "detailed"},
})
```

As of `langchain 1.0`, custom state schemas **must** be `TypedDict` types. Pydantic models and dataclasses are no longer supported. See the [v1 migration guide](https://docs.langchain.com/oss/python/migrate/langchain-v1#state-type-restrictions) for more details.

Defining custom state via middleware is preferred over defining it via [`state_schema`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.AgentMiddleware.state_schema) on [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent) because it allows you to keep state extensions conceptually scoped to the relevant middleware and tools.[`state_schema`](https://reference.langchain.com/python/langchain/middleware/#langchain.agents.middleware.AgentMiddleware.state_schema) is still supported for backwards compatibility on [`create_agent`](https://reference.langchain.com/python/langchain/agents/factory/create_agent).

To learn more about memory, see [Memory](https://docs.langchain.com/oss/python/concepts/memory). For information on implementing long-term memory that persists across sessions, see [Long-term memory](https://docs.langchain.com/oss/python/langchain/long-term-memory).

### Streaming

We’ve seen how the agent can be called with `invoke` to get a final response. If the agent executes multiple steps, this may take a while. To show intermediate progress, we can stream back messages as they occur.

```
from langchain.messages import AIMessage, HumanMessage

for chunk in agent.stream({
    "messages": [{"role": "user", "content": "Search for AI news and summarize the findings"}]
}, stream_mode="values"):
    # Each chunk contains the full state at that point
    latest_message = chunk["messages"][-1]
    if latest_message.content:
        if isinstance(latest_message, HumanMessage):
            print(f"User: {latest_message.content}")
        elif isinstance(latest_message, AIMessage):
            print(f"Agent: {latest_message.content}")
    elif latest_message.tool_calls:
        print(f"Calling tools: {[tc['name'] for tc in latest_message.tool_calls]}")
```

For more details on streaming, see [Streaming](https://docs.langchain.com/oss/python/langchain/streaming).

### Middleware

[Middleware](https://docs.langchain.com/oss/python/langchain/middleware) provides powerful extensibility for customizing agent behavior at different stages of execution. You can use middleware to:

- Process state before the model is called (e.g., message trimming, context injection)
- Modify or validate the model’s response (e.g., guardrails, content filtering)
- Handle tool execution errors with custom logic
- Implement dynamic model selection based on state or context
- Add custom logging, monitoring, or analytics

Middleware integrates seamlessly into the agent’s execution, allowing you to intercept and modify data flow at key points without changing the core agent logic.

For comprehensive middleware documentation including decorators like [`@before_model`](https://reference.langchain.com/python/langchain/agents/middleware/types/before_model), [`@after_model`](https://reference.langchain.com/python/langchain/agents/middleware/types/after_model), and [`@wrap_tool_call`](https://reference.langchain.com/python/langchain/agents/middleware/types/wrap_tool_call), see [Middleware](https://docs.langchain.com/oss/python/langchain/middleware).

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="multimodal-rag-with-colpali-milvus-and-vlms.md">
<details>
<summary>Multimodal RAG with Colpali, Milvus and VLMs</summary>

Phase: [EXPLOITATION]

# Multimodal RAG with Colpali, Milvus and VLMs

**Source URL:** <https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag>

[Community Article](https://huggingface.co/blog/community) Published
December 10, 2024

In this post, we will see how to do multimodal RAG with [colpali](https://arxiv.org/abs/2407.01449), [milvus](https://milvus.io/) and a visual language model (gemini/gpt-4o).

We will build an application to upload a PDF and then do Q&A queries on it. Q&A can be done on both text and visual elements of the PDF. We will not extract text from the PDF; instead, we will treat it as an image and use colpali to get embeddings for the PDF pages. These embeddings will be indexed to Milvus, and then we will use a VLM to do Q&A queries on the PDF pages.

> If you just want to see the code in action, there is a demo at [https://huggingface.co/spaces/saumitras/colpali-milvus/](https://huggingface.co/spaces/saumitras/colpali-milvus/). Code for the same is [here](https://github.com/saumitras/colpali-milvus-multimodal-rag/).

**TOC**:

1. [Problem](https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag#problem)
2. [Why colpali?](https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag#why-colpali)
3. [Understanding how colpali works](https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag#understanding-how-colpali-works)
4. [Code to upload a PDF, get embedding using colpali, index it to Milvus, then do Q&A queries using a vision language model (gemini/openai)](https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag#code)

## Problem

Let's say a company wants to build a Q&A/search interface for its internal documents, which include PDFs, word files, wikis, images, and text files. The traditional approach involves extracting text and media, detecting layout for structure, and indexing the information in a vector store for semantic search. However, this method often falls short for complex documents containing images, tables, and graphs. Let's look at an example below:

We have a [PDF with stats on covid](https://saumitra.me/2024/covid-slides.pdf) in the form of charts and tables. We want to answer the queries below:

```markdown
1. What is the correlation between the samples tested and the positivity rate?
2. When and what was the highest number of cases and TPR?
3. Which country had the highest omicron cases?
```

These queries can be answered by using data from following 3 pages:

**Page 4: A chart showing stats on samples and positivity rate**

https://saumitra.me/2024/covid-page-4.png

**Page 8: A table showing cases and TPR**

https://saumitra.me/2024/covid-page-8.png

**Page 9: A table showing cases by country**

https://saumitra.me/2024/covid-page-9.png

It would be difficult to extract data from these pages as text in a manner which can be used for querying.
We want to show user the answer and source page(s) from the PDF which contains the answer, like below:

https://saumitra.me/2024/rag-demo-screenshot.png

Let's understand how colpali can help us here.

## Why colpali?

Document retrieval has always been a key component of systems like search engines and information retrieval. Traditional document retrieval methods rely heavily on text-based methods (like OCR and text segmentation), often missing crucial visual cues like layouts, images, and tables.

Colpali addresses this by using Vision-Language Models (VLMs) to understand and retrieve visually rich documents, capturing both textual and visual information. Colpali's architecture allows direct encoding of document images into a common embedding space, eliminating the need for time-consuming text extraction and segmentation.

## Understanding how colpali works

Colpali works in the following steps:

### Step 1: Treating the Document as an Image

Imagine we have a PDF document. Normally, we would extract text from the document using OCR (Optical Character Recognition), segment it into different sections, and then use these segments for searching. colpali simplifies this process by treating the entire document page as an image, bypassing the need for complex text extraction, layout detection, or OCR.

### Step 2: Splitting the Image into Patches

Once colpali has this "image" of the document, it divides the page into small, uniform pieces called patches. Each patch captures a tiny portion of the page. It might contain a few words, a piece of a graph, or part of an image. This division helps the model focus on the document's small, detailed parts rather than trying to understand the whole page at once.

At first glance, it might seem like dividing an image into patches is similar to breaking text into chunks. However, these two methods have several key differences, especially in how they handle and preserve context. Let’s dive deeper into these differences to understand why patch-based processing in colpali is more effective for document retrieval compared to traditional text chunking.

#### Understanding Context Loss in Text Chunking

In traditional text chunking, text is split into smaller chunks based on certain tokens since many models limit the number of tokens they can process at once.

Problem with Context Loss:

- Chunking can split sentences or paragraphs midway, causing crucial context to be lost. It can also result in incomplete information in one chunk and missing context in another.
Chunking doesn't preserve visual or structural information, such as the relationship between headings and their corresponding content or the placement of text in tables or figures.

For example, If you have a document with a heading followed by a table, text chunking might separate the heading and the table, losing the context that the table belongs to that heading.

#### Patch-Based Image Processing in colpali

Colpali divides the document image into patches, much like dividing a photo into small squares. Each patch is a fixed-size portion of the image, like a mini-snapshot of that part of the page.

Patches are more effective due to the following reasons:

- **No Loss of Structure:** The patches retain the document's visual structure, preserving its spatial layout. For instance, if a page has two columns of text or a table with rows and columns, each patch maintains its relative position, ensuring that the model understands the overall arrangement of the elements.
- **Multi-Modal Context:** Patches capture both textual and visual information. This includes both visual features (e.g., font styles, colors, boldness) and non-text elements (e.g., figures and graphs).
- **Positional Awareness:** Each patch has a positional embedding that tells the model where it is located on the page, helping the model understand the overall layout.

### Step 3: Embedding Creation and **Aligning Visual and Textual Information**

Each patch is then passed through a Vision Transformer (ViT), which converts them into unique embeddings. Next, colpali aligns these visual embeddings with the text of the query by transforming the query into its own set of embeddings. colpali uses a process called `alignment` that aligns image path embeddings and text embeddings in the same vector space. Only then can we compare the similarity between query and document embeddings.

### Step 4: Scoring the Relevance - Late Interaction Mechanism

At this point, colpali has embeddings for both the query and the document. The next challenge is to identify the relevant parts of the document. colpali uses a process called the `Late Interaction Mechanism`, where each piece of the query is finely matched against every part of the document, scoring and ranking their relevance.

Colpali highlights the most relevant pieces of the document, focusing on the patches that best match the query. This approach enables colpali to efficiently retrieve relevant information from visually rich documents, capturing both visual and textual data without losing context.

* * *

## Code

Full code at [https://github.com/saumitras/colpali-milvus-rag/](https://github.com/saumitras/colpali-milvus-rag/)

### 1\. Add colpali processor

```python
model_name = "vidore/colpali-v1.2"
device = get_torch_device("cuda")

model = colpali.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map=device,
).eval()

processor = cast(colpaliProcessor, colpaliProcessor.from_pretrained(model_name))
```

### 2\. Use colpali to get embeddings for image (pdf pages)

```python
def process_images(self, image_paths:list[str], batch_size=5):

    print(f"Processing {len(image_paths)} image_paths")

    images = self.get_images(image_paths)

    dataloader = DataLoader(
        dataset=ListDataset[str](images),
        batch_size=batch_size,
        shuffle=False,
        collate_fn=lambda x: processor.process_images(x),
    )

    ds: List[torch.Tensor] = []
    for batch_doc in tqdm(dataloader):
        with torch.no_grad():
            batch_doc = {k: v.to(model.device) for k, v in batch_doc.items()}
            embeddings_doc = model(**batch_doc)
        ds.extend(list(torch.unbind(embeddings_doc.to(device))))

    ds_np = [d.float().cpu().numpy() for d in ds]

    return ds_np
```

### 3\. Use colpali to get embeddings for text (user query)

```python
def process_text(self, texts: list[str]):
    print(f"Processing {len(texts)} texts")

    dataloader = DataLoader(
        dataset=ListDataset[str](texts),
        batch_size=1,
        shuffle=False,
        collate_fn=lambda x: processor.process_queries(x),
    )

    qs: List[torch.Tensor] = []
    for batch_query in dataloader:
        with torch.no_grad():
            batch_query = {k: v.to(model.device) for k, v in batch_query.items()}
            embeddings_query = model(**batch_query)

        qs.extend(list(torch.unbind(embeddings_query.to(device))))

    qs_np = [q.float().cpu().numpy() for q in qs]

    return qs_np
```

### 4\. Code to create collection, index and query in milvus

```python
class MilvusManager:
    def __init__(self, milvus_uri, collection_name, create_collection, dim=128):
        self.client = MilvusClient(uri=milvus_uri)
        self.collection_name = collection_name
        if self.client.has_collection(collection_name=self.collection_name):
            self.client.load_collection(collection_name)
        self.dim = dim

        if create_collection:
            self.create_collection()
            self.create_index()

    def create_collection(self):
        if self.client.has_collection(collection_name=self.collection_name):
            self.client.drop_collection(collection_name=self.collection_name)
        schema = self.client.create_schema(
            auto_id=True,
            enable_dynamic_fields=True,
        )
        schema.add_field(field_name="pk", datatype=DataType.INT64, is_primary=True)
        schema.add_field(
            field_name="vector", datatype=DataType.FLOAT_VECTOR, dim=self.dim
        )
        schema.add_field(field_name="seq_id", datatype=DataType.INT16)
        schema.add_field(field_name="doc_id", datatype=DataType.INT64)
        schema.add_field(field_name="doc", datatype=DataType.VARCHAR, max_length=65535)

        self.client.create_collection(
            collection_name=self.collection_name, schema=schema
        )

    def create_index(self):
        self.client.release_collection(collection_name=self.collection_name)
        self.client.drop_index(
            collection_name=self.collection_name, index_name="vector"
        )
        index_params = self.client.prepare_index_params()
        index_params.add_index(
            field_name="vector",
            index_name="vector_index",
            index_type="HNSW",
            metric_type="IP",
            params={
                "M": 16,
                "efConstruction": 500,
            },
        )

        self.client.create_index(
            collection_name=self.collection_name, index_params=index_params, sync=True
        )

    def create_scalar_index(self):
        self.client.release_collection(collection_name=self.collection_name)

        index_params = self.client.prepare_index_params()
        index_params.add_index(
            field_name="doc_id",
            index_name="int32_index",
            index_type="INVERTED",
        )

        self.client.create_index(
            collection_name=self.collection_name, index_params=index_params, sync=True
        )

    def search(self, data, topk):
        search_params = {"metric_type": "IP", "params": {}}
        results = self.client.search(
            self.collection_name,
            data,
            limit=int(50),
            output_fields=["vector", "seq_id", "doc_id"],
            search_params=search_params,
        )
        doc_ids = set()
        for r_id in range(len(results)):
            for r in range(len(results[r_id])):
                doc_ids.add(results[r_id][r]["entity"]["doc_id"])

        scores = []

        def rerank_single_doc(doc_id, data, client, collection_name):
            doc_colbert_vecs = client.query(
                collection_name=collection_name,
                filter=f"doc_id in [{doc_id}, {doc_id + 1}]",
                output_fields=["seq_id", "vector", "doc"],
                limit=1000,
            )
            doc_vecs = np.vstack(
                [doc_colbert_vecs[i]["vector"] for i in range(len(doc_colbert_vecs))]
            )
            score = np.dot(data, doc_vecs.T).max(1).sum()
            return (score, doc_id)

        with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
            futures = {
                executor.submit(
                    rerank_single_doc, doc_id, data, self.client, self.collection_name
                ): doc_id
                for doc_id in doc_ids
            }
            for future in concurrent.futures.as_completed(futures):
                score, doc_id = future.result()
                scores.append((score, doc_id))

        scores.sort(key=lambda x: x[0], reverse=True)
        if len(scores) >= topk:
            return scores[:topk]
        else:
            return scores

    def insert(self, data):
        colbert_vecs = [vec for vec in data["colbert_vecs"]]
        seq_length = len(colbert_vecs)
        doc_ids = [data["doc_id"] for i in range(seq_length)]
        seq_ids = list(range(seq_length))
        docs = [""] * seq_length
        docs[0] = data["filepath"]

        self.client.insert(
            self.collection_name,
            [\
                {\
                    "vector": colbert_vecs[i],\
                    "seq_id": seq_ids[i],\
                    "doc_id": doc_ids[i],\
                    "doc": docs[i],\
                }\
                for i in range(seq_length)\
            ],
        )

    def get_images_as_doc(self, images_with_vectors:list):

        images_data = []

        for i in range(len(images_with_vectors)):
            data = {
                "colbert_vecs": images_with_vectors[i]["colbert_vecs"],
                "doc_id": i,
                "filepath": images_with_vectors[i]["filepath"],
            }
            images_data.append(data)

        return images_data

    def insert_images_data(self, image_data):
        data = self.get_images_as_doc(image_data)

        for i in range(len(data)):
            self.insert(data[i])
```

### 5\. Save pdf as individual images

```python
class PdfManager:
    def __init__(self):
        pass

    def clear_and_recreate_dir(self, output_folder):
        print(f"Clearing output folder {output_folder}")

        if os.path.exists(output_folder):
            shutil.rmtree(output_folder)

        os.makedirs(output_folder)

    def save_images(self, id, pdf_path, max_pages, pages: list[int] = None) -> list[str]:
        output_folder = f"pages/{id}/"
        images = convert_from_path(pdf_path)

        print(f"Saving images from {pdf_path} to {output_folder}. Max pages: {max_pages}")

        self.clear_and_recreate_dir(output_folder)

        num_page_processed = 0

        for i, image in enumerate(images):
            if max_pages and num_page_processed >= max_pages:
                break

            if pages and i not in pages:
                continue

            full_save_path = f"{output_folder}/page_{i + 1}.png"

            image.save(full_save_path, "PNG")

            num_page_processed += 1

        return [f"{output_folder}/page_{i + 1}.png" for i in range(num_page_processed)]
```

### 6\. Middleware to index and search Milvus for embeddings generated from colpali

```python
class Middleware:
    def __init__(self, id:str, create_collection=True):
        hashed_id = hashlib.md5(id.encode()).hexdigest()[:8]
        milvus_db_name = f"milvus_{hashed_id}.db"
        self.milvus_manager = MilvusManager(milvus_db_name, "colpali", create_collection)

    def index(self, pdf_path: str, id:str, max_pages: int, pages: list[int] = None):

        print(f"Indexing {pdf_path}, id: {id}, max_pages: {max_pages}")

        image_paths = pdf_manager.save_images(id, pdf_path, max_pages)

        print(f"Saved {len(image_paths)} images")

        colbert_vecs = colpali_manager.process_images(image_paths)

        images_data = [{\
            "colbert_vecs": colbert_vecs[i],\
            "filepath": image_paths[i]\
        } for i in range(len(image_paths))]

        print(f"Inserting {len(images_data)} images data to Milvus")

        self.milvus_manager.insert_images_data(images_data)

        print("Indexing completed")

        return image_paths


    def search(self, search_queries: list[str]):
        print(f"Searching for {len(search_queries)} queries")

        final_res = []

        for query in search_queries:
            print(f"Searching for query: {query}")
            query_vec = colpali_manager.process_text([query])[0]
            search_res = self.milvus_manager.search(query_vec, topk=1)
            print(f"Search result: {search_res} for query: {query}")
            final_res.append(search_res)

        return final_res
```

### 7\. Use Gemini or gpt-4o to do Q&A on pdf page(s) matching user query

```python
class Rag:

    def get_answer_from_gemini(self, query, imagePaths):

        print(f"Querying Gemini for query={query}, imagePaths={imagePaths}")

        try:
            genai.configure(api_key=os.environ['GEMINI_API_KEY'])
            model = genai.GenerativeModel('gemini-1.5-flash')

            images = [Image.open(path) for path in imagePaths]

            chat = model.start_chat()

            response = chat.send_message([*images, query])

            answer = response.text

            print(answer)

            return answer

        except Exception as e:
            print(f"An error occurred while querying Gemini: {e}")
            return f"Error: {str(e)}"


    def get_answer_from_openai(self, query, imagesPaths):
        print(f"Querying OpenAI for query={query}, imagesPaths={imagesPaths}")

        try:
            payload = self.__get_openai_api_payload(query, imagesPaths)

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
            }

            response = requests.post(
                url="https://api.openai.com/v1/chat/completions",
                headers=headers,
                json=payload
            )
            response.raise_for_status()  # Raise an HTTPError for bad responses

            answer = response.json()["choices"][0]["message"]["content"]

            print(answer)

            return answer

        except Exception as e:
            print(f"An error occurred while querying OpenAI: {e}")
            return None

    def __get_openai_api_payload(self, query:str, imagesPaths:List[str]):
        image_payload = []

        for imagePath in imagesPaths:
            base64_image = encode_image(imagePath)
            image_payload.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            })

        payload = {
            "model": "gpt-4o",
            "messages": [\
                {\
                    "role": "user",\
                    "content": [\
                        {\
                            "type": "text",\
                            "text": query\
                        },\
                        *image_payload\
                    ]\
                }\
            ],
            "max_tokens": 1024
        }

        return payload

```

In the next post, we will understand the limitations of colpali and a workaround for them.

## References

1. [https://milvus.io/docs/use\_colpali\_with\_milvus.md](https://milvus.io/docs/use_colpali_with_milvus.md)
2. [https://arxiv.org/abs/2407.01449](https://arxiv.org/abs/2407.01449)

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="the-8-best-ai-image-generators-in-2025.md">
<details>
<summary>The 8 best AI image generators in 2025</summary>

Phase: [EXPLOITATION]

# The 8 best AI image generators in 2025

**Source URL:** <https://zapier.com/blog/best-ai-image-generator/>

## Get the best AI-generated images using text-to-image AI.

By Harry Guinness · April 1, 2026

https://images.ctfassets.net/lzny33ho1g45/2olcy4TVSWAjqy5dsxLNZd/e6585308a718ebdcb2d20e2f7f6b8a93/best-ai-image-generators.jpg?fm=jpg&q=31&fit=thumb&w=1520&h=760

AI image generators have been brewing (generating?) up a storm for the last few years. If you've been on social media, watched prime time news shows, or read a magazine, AI-generated images have been impossible to miss. These kinds of AI-generated images are everywhere, and sometimes you won't even realize. If you want to join in the fun, or [add some AI-powered features to your business workflows](https://zapier.com/blog/ai-image-examples-for-business/), the apps on this list will give you what you're looking for.

I've been writing about AI image generators [since Google Deep Dream in 2015](https://photography.tutsplus.com/articles/brave-new-camera-computational-photography--cms-23438). That's about as long as anyone outside of a computer science lab has realistically been thinking about these tools, and I'm really excited by how far they've come.

I'm going to try to avoid the thorny discussions around artistic merit, whether or not these tools are replacing or augmenting artists, and copyright infringement in training data, at least where I can. I'm also going to steer clear of some of the [controversial uses these models have been put to](https://www.theguardian.com/technology/2026/jan/22/grok-ai-generated-millions-sexualised-images-in-month-research-says). You're reading this on the Zapier blog, so I'm going to assume you have a good personal or professional need for an image generator.

While you've probably tested these image generators before, if you haven't tried one in a while, it's worth taking a few hours to play around with one of these newer text-to-image AI apps. Things have improved massively, so it's worth understanding what they can do, even just from a technical perspective. Whether you like it or not, we're all seeing a lot of their output at the moment. And there will only be more to come.

## The best AI image generators

- [ChatGPT](https://zapier.com/blog/best-ai-image-generator/#gpt-4o) for the best AI image generator overall

- [Nano Banana](https://zapier.com/blog/best-ai-image-generator/#nano-banana) for Google users

- [Midjourney](https://zapier.com/blog/best-ai-image-generator/#midjourney) for artistic results

- [Reve](https://zapier.com/blog/best-ai-image-generator/#reve) for overall prompt adherence

- [Ideogram](https://zapier.com/blog/best-ai-image-generator/#ideogram) for accurate text

- [FLUX](https://zapier.com/blog/best-ai-image-generator/#flux) for customization and control of your AI images

- [Adobe Firefly](https://zapier.com/blog/best-ai-image-generator/#firefly) for integrating AI-generated images into photos

- [Recraft](https://zapier.com/blog/best-ai-image-generator/#recraft) for graphic design


## How do AI image generators work?

All these AI image generators take a text prompt and then turn it—as best they can—into a matching image. This opens up some wild possibilities, since your prompt can be anything from "an impressionist oil painting of a Canadian man riding a moose through a forest of maple trees" to "a painting in the style of Vermeer of a large fluffy Irish wolfhound enjoying a pint of beer in a traditional pub" or "a photograph of a donkey on the moon."

https://images.ctfassets.net/lzny33ho1g45/2udOp4paDgOh5HpqG5JRAQ/e3e78a269577deefa2c47c6c743ce4db/image8.png

I made this with Google Gemini using the prompt "an impressionist oil painting of a Canadian man riding a moose through a forest of maple trees"

Seriously, the only real limits are your imagination, the AI image generator's ability to [comprehend your prompt](https://zapier.com/blog/natural-language-processing/), and any content filters put in place to stop plagiarism, copyright infringement, and bad actors flooding the internet with AI-generated violence or other NSFW content.

Most AI image generators work in a pretty similar way. Billions of image-text pairs are used to train a neural network (basically, a very fancy computer algorithm [modeled loosely on the human brain](https://news.mit.edu/2017/explained-neural-networks-deep-learning-0414)) on _what things are_. By allowing it to process near-countless images, it learns what dogs, the color red, Vermeers, and everything else are. Once this is done, you have an AI that can interpret almost any prompt—though [there is a skill in setting things up](https://zapier.com/blog/ai-art-prompts/) so it can do so accurately.

https://images.ctfassets.net/lzny33ho1g45/1LHdvgxMxOKcgWqC2yzoKh/ff7194426828d81a2d8437f4f9c38132/ai-image-generator-dogs.png

A dog-shaped cloud floating in a clear blue sky—from top-left, going clockwise, at 10 steps, 20 steps, 40 steps, and 120 steps.

The next step is to actually render the AI-generated image. There are two primary ways of doing this:

- **Diffusion models** work by starting with a random field of noise, and then editing it in a series of steps to match its understanding of the prompt.

- **Autoregression models** work by generating chunks of the image at a time, predicting the next chunk based on what they've already created. These are the current state-of-the-art models.


## What makes the best AI image generator?

There's a reason that AI image generators have become incredibly popular over the past three or four years: before that, they were pretty bad. The technology underlying them was incredibly cool and impressive, at least to research scientists, but [the images they could output](https://www.theguardian.com/artanddesign/2016/mar/28/google-deep-dream-art) were underwhelming. Even the original DALL·E was more of a fun novelty than a world-shaking revelation [when it launched in 2021](https://openai.com/research/dall-e).

Now that these text-to-image generators have been around for a while, there's some real competition between the different models. They've really increased in quality and can now even generate text with some reliability. If all you care about is the current "best" model, check out [Artificial Analysis's Image Arena](https://artificialanalysis.ai/text-to-image/arena?tab=Leaderboard). But we've reached the stage where the top 50 or so models are all excellent, so other features and usability matter more than they used to.

So, to find the best AI art generators, I set some pretty strict criteria:

- I was looking for apps that allowed you to generate AI images from a text prompt (and to a lesser degree, an image prompt). Tools that have you upload a dozen of your photos and then [spit out AI-generated portraits](https://land.prisma-ai.com/magic-avatars/) are fun, but they aren't the kind of general-purpose image generators I was considering.

- I was looking at the AI image generators themselves, not [tools built on top of them](https://zapier.com/blog/ai-art-generator/). For example, [NightCafe](https://nightcafe.studio/) is an AI picture generator that has a great community and app, but it just enables you to use [open source models](https://zapier.com/blog/open-source-ai/) like FLUX and Stable Diffusion, fine-tuned models based on various versions of them, various APIs for current models, as well as a handful of older [generative models](https://zapier.com/blog/generative-ai). It's worth checking out, but it doesn't meet my criteria for its own entry on this list.


Aside from all that, I also considered how easy each AI image creator is to use, what kinds of controls and customization options it provides (for things like AI image upscale), what pricing model it has, and most important of all: how good were the results? The best AI image generators are now far less likely to create weird or impossible-looking things.

I've been using and writing about text-to-image generators since the original DALL·E launched, and about photography and art for more than a decade, so I'm pretty familiar with how all these tools work—and their various pros, cons, and bonkers behaviors. But writing this article was actually the first time I've put so many AI image generators head-to-head with the _same prompts_. The results were fascinating, and I'm delighted to say all the apps on the list offer genuine reasons to use them.

**How to use AI image generation at work**

Interested in AI, but not quite sure how you'd use it at work? Here are a few of the ways people are turning to AI image generation in their roles:

- Generating hero images for blog posts

- Creating social media posts

- Generating slide decks and storyboards

- Creating personalized images for customers


Learn more about [how to use AI image generation at work](https://zapier.com/blog/ai-image-examples-for-business/).

## The best AI image generators at a glance

|  | **Best for** | **Access options** | **Price** | **Parent company** |
| --- | --- | --- | --- | --- |
| [ChatGPT](https://zapier.com/blog/best-ai-image-generator/#gpt-4o) | Ease of use and overall quality | ChatGPT; API | Free with ChatGPT; fewer restrictions with ChatGPT Plus at $20/month | OpenAI |
| [Nano Banana](https://zapier.com/blog/best-ai-image-generator/#nano-banana) | Google users | Google Gemini; API | Limited availability on free plan; included with Google AI Plus plan at $8/month | Google |
| [Midjourney](https://zapier.com/blog/best-ai-image-generator/#midjourney) | Artistic results | Web app; Discord | From $10/month for ~200 images/month and commercial usage rights | Midjourney |
| [Reve](https://zapier.com/blog/best-ai-image-generator/#reve) | Adhering to prompts | Web app | Limited free plan; Pro plan at $20/month with more generations and private images | Reve |
| [Ideogram](https://zapier.com/blog/best-ai-image-generator/#ideogram) | Accurate text | Web app | Limited free plan; from $20/month for 1,000 monthly priority credits | Ideogram AI |
| [FLUX](https://zapier.com/blog/best-ai-image-generator/#flux) | Customization and control | NightCafe, Tensor.Art, Civitai, and lots of other apps; API; downloading it to a local server | Depends on the platform | Black Forest Labs |
| [Adobe Firefly](https://zapier.com/blog/best-ai-image-generator/#firefly) | Using AI-generated images in photos | firefly.adobe.com, Photoshop, Express, and other Adobe tools | Limited free credits; from $9.99 for 2,000 credits/month | Adobe |
| [Recraft](https://zapier.com/blog/best-ai-image-generator/#recraft) | Graphic design | Web app | Free for 30 credits/day; from $12/month for full features | Recraft |

## The best AI image generator overall

### [ChatGPT](https://chat.com/) (GPT Image 1.5)

https://images.ctfassets.net/lzny33ho1g45/75DSS8gsgXORvalbs3MCyE/170374ed491f2eae0f67d581c7f27594/image11.png

**ChatGPT pros:**

- Incredibly easy to use and a best-in-class model

- Included with ChatGPT plans, so you get a lot of AI for your money

- Integrates with Zapier


**ChatGPT cons:**

- Very slow

- Controls can be hit and miss

- It's pricey if you don't want the rest of ChatGPT with it


After OpenAI's [DALL·E](https://zapier.com/blog/dall-e-3/) model kickstarted the text-to-image boom, it seemed to take a backseat to the company's language models. DALL·E 2 and DALL·E 3 were good when they debuted, but were both quickly overtaken by other models. But since last year, OpenAI has been back with a bang. GPT Image 1.5 is integrated with [ChatGPT](https://zapier.com/blog/how-to-use-chatgpt/), which can now [natively generate images](https://zapier.com/blog/chatgpt-image-generation/).

GPT Image 1 is one of the best image generators available. It's also ridiculously easy to use: tell ChatGPT what you want to see, and it'll create the image. Unfortunately, because it uses an autoregression model instead of diffusion, it's much slower than the other image generators on this list—and it only generates a single image. If you're only occasionally generating a few images, this isn't a big deal, but it's worth noting.

It's really solid across the board: accurate text rendering, easy editing, understanding of numbers and position, the list goes on. Its best feature, though, is what's caused it to go viral a few times. It's great at adhering to image prompts (and it's pretty good at adhering to regular prompts, too). If you upload a photo and direct it to create the image in the style of Picasso, Vermeer, or, yes, Studio Ghibli, it will do an exceptional job. It's also pretty good at incorporating feedback—ask it to change just one element of your image and it generally will.

You get limited access to image creation on ChatGPT's free plan. If you want to use it more, you'll need to subscribe to ChatGPT Plus or Pro.

In addition to image generation through ChatGPT, [OpenAI offers an API](https://zapier.com/blog/openai-api/), which means you can [connect ChatGPT to Zapier](https://zapier.com/apps/chatgpt/integrations) to do things like automatically create images from Google Forms or HubSpot responses—or any other apps you use. Learn more about [how to automate ChatGPT](https://zapier.com/blog/automate-chatgpt/), or get started with a pre-made template.

**ChatGPT pricing:** Free users and ChatGPT Go users ($8/month) can access it, but if you don't want to run into limits, image generation is included as part of ChatGPT Plus at $20/month.

## The best AI image generator for Google users

### [**Nano Banana**](https://gemini.google/overview/image-generation/) **(Gemini 3.1 Flash Image Preview)**

https://images.ctfassets.net/lzny33ho1g45/9GybvN9xhbgxFvSg9YILl/aff748b7bcd4d11abaa4c067c9137711/image1.png

**Nano Banana pros:**

- Excellent at editing existing images

- Available through Google Gemini as well as other apps and tools


**Nano Banana cons:**

- Prompt adherence can be hit and miss

- Visible watermark added to all images


[Nano Banana 2](https://zapier.com/blog/gemini-nano-banana/) (officially Gemini 3.1 Flash, but no one calls it that) is Google's answer to ChatGPT's image generation. Despite the silly name, Nano Banana is a serious contender. It's especially good at editing existing images. If you're a Google user, using it through Gemini is a very easy choice.

While Nano Banana can create incredible results, I found its prompt adherence and direct editing tools lagged a little behind other models. While I was able to change a tennis ball into a chicken, I couldn't get Nano Banana to have the chicken run away from my dog and not toward it. When I asked it to change the moose in the image above into a cow, it managed it perfectly but couldn't change the direction of travel without making a weird two-headed-no-tailed monster. Similarly, in prompts with lots of details, it missed a few. The other big catch is that it watermarks your images.

Google's image models have been solid for the past while, but they've always fallen a little short. Nano Banana fixes that. Prompt adherence aside, it's one of the top models currently available—and here's hoping Google can iron out those last few quirks.

You can even add Nano Banana to the rest of your AI workflows with [Zapier's Gemini integration](https://zapier.com/apps/google-ai-studio/integrations), so you can create images in Gemini based on triggers in all your other apps.

**Nano Banana pricing:** Limited availability on free plan; included with Google AI Plus plan at $8/month and Google AI Pro plan at $20/month.

## The best AI image generator for artistic results

### [**Midjourney**](https://www.midjourney.com/explore?tab=top)

https://images.ctfassets.net/lzny33ho1g45/5c2lxK4vhLWzfata4t1eul/392d5e391b93eab744d3d1476955bb6f/image2.jpg

**Midjourney pros:**

- Consistently produces some of the best-looking AI-generated images

- The community is a great way to get inspiration


**Midjourney cons:**

- Images you generate are public by default

- [Free trials are currently suspended](https://docs.midjourney.com/hc/en-us/articles/27870399340173-Free-Trials)


For a long time, [Midjourney](https://zapier.com/blog/how-to-use-midjourney/) produced my favorite results of all of the image generators on this list. Other apps have finally surpassed it in quality, especially when it comes to adhering exactly to your prompts, but I still feel Midjourney produces some of the most visually appealing and interesting results with great textures and colors. It helps that you now have to fine-tune the model to match your visual preferences.

Best of all, Midjourney's web app is increasingly excellent. It's come a long way since the time you had to access it through Discord.

Still, as you can probably guess, Midjourney isn't totally free of quirks: by default, every image you generate is posted publicly on Midjourney's Explore page and can be viewed on your profile. It gives everything a cool community aspect, but it means that anyone who cares to look can see what you're creating. While not necessarily a problem for artists, this might be a dealbreaker if you're looking to use Midjourney for business purposes. It's also worth noting that Midjourney is in the midst of [a lawsuit with Disney and Universal](https://www.bbc.com/news/articles/cg5vjqdm1ypo); not much has come of it yet, and a lot of these suits have petered out, but it's worth being aware of.

[Midjourney's help docs](https://docs.midjourney.com/docs/quick-start) are really good and walk you through getting started with both the web app and Discord, and they show you how to control all its various features, from selecting model versions and upscaling to using character references and its personalization tools. It's one of the most feature-filled apps on this list, and once you understand the different options, the results you can get are genuinely amazing.

Midjourney's free trials are still suspended, but they're occasionally reinstated for a few days. If you miss a free trial window, the Basic Plan starts at $10/month and comes with 3.3 hours of GPU time per month, or around 200 images. You also get the option to buy additional GPU time, and you can use your images commercially.

**Midjourney pricing:** From $10/month for the Basic Plan that allows you to generate ~200 images/month and provides commercial usage rights.

**Read more:** [Midjourney vs. ChatGPT](https://zapier.com/blog/midjourney-vs-dalle/)

## The best AI image generator for adhering to prompts

### [**Reve**](https://preview.reve.art/)

https://images.ctfassets.net/lzny33ho1g45/1rErUICKuzBtIoT0x1EmHf/1aa12d16da420ae518e18a5a2826c77e/image5.png

**Reve Image pros:**

- Great prompt adherence and editing

- Solid free plan


**Reve Image cons:**

- Model hasn't been updated in a year


Reve Image is an image model that essentially came out of nowhere in March 2025. It instantly jumped to the top of Artificial Analysis's leaderboard—and it's still comfortably in the top tier. It's an incredibly powerful image generator with best-in-class prompt adherence and very effective editing.

In plain English, that means Reve Image is able to stick closely to the prompt you give it. If you ask for, say, an image with a warrior holding a sword and a wizard holding a staff, that's what you'll get—not a warrior with a staff and a wizard with a sword. This kind of adherence has been a struggle for image generators, especially as prompts get longer and more complicated. I was pretty blown away by just how many details Reve Image could manage.

On top of that, Reve Image is great with text, different styles, photorealism, and editing. If you want to make changes, you can add text notes to the areas of the image and it will regenerate everything. It's a great way to work.

Sadly, Reve Image has axed its credit-based pricing. The free plan gets you a limited number of generations; the Pro plan gets you the vague "100x more usage" for $20/month.

**Reve Image pricing:** Free plan; Pro plan at $20/month with more generations and private images.

## Best AI image generator for accurate text

### [Ideogram](https://ideogram.ai/)

https://images.ctfassets.net/lzny33ho1g45/7xaiByWYInfO3qQnxkpn9O/fa576b1cac761d8db9fb9000e8ae5a43/image3.png

**Ideogram pros:**

- Great looking AI-generated images—and among the most accurate text of any app

- There's a free plan


**Ideogram cons:**

- Images you generate are public by default


Although they're getting better, most AI image generators still struggle to generate text correctly—the diffusion process just doesn't lend itself to precisely rendering letters. Ideogram, though, has cracked it. Its latest 3.0 algorithm is able to accurately and reliably include text along with any generated image.

What makes this more impressive is Ideogram is also one of the best image generators overall. It has an intuitive web app and some nice features like an [image editor](https://docs.ideogram.ai/using-ideogram/ideogram-features/ideogram-editor) and the ability to [use any image as the basis for a new one](https://docs.ideogram.ai/using-ideogram/ideogram-features/remix). There's a Batch Generator that allows you to upload a spreadsheet with a list of prompts, a canvas feature that allows for more complex designs, and a Character creator that allows you to put the same person in any scene you can imagine. In my testing, it was up there with Midjourney in terms of quality.

Ideogram even has a free plan. With it, you're limited to 10 credits a week, you have to wait a few minutes for a generation to start, and you only get Ideogram's basic features, but it's still a great way to get a feel for one of the best AI image generators available.

**Ideogram pricing:** Limited free plan; from $20/month for Plus plan with 1,000 monthly priority credits.

## Best AI image generator for customization and control

### [**FLUX**](https://blackforestlabs.ai/)

https://images.ctfassets.net/lzny33ho1g45/5xAzjYy11xVmiruodsWtSo/64a34016fd91e08bcdbe0eba251a59e1/image9.png

**FLUX pros:**

- From the team behind Stable Diffusion—but without the drama

- Powerful and open


**FLUX cons:**

- New and not as widely available as Stable Diffusion


As [Stability.ai](http://stability.ai/), the makers of Stable Diffusion, [started collapsing back in 2024](https://futurism.com/the-byte/stability-ai-collapsing-considering-sale), a significant portion of the team left the company to found [Black Forest Labs](https://blackforestlabs.ai/). Their [FLUX series](https://zapier.com/blog/flux-ai-image/) are now the premier open text-to-image models.

There are a few different versions of FLUX: FLUX.2 Max, FLUX.2 Pro, FLUX.2 Flex, FLUX.2 Klein, as well as older FLUX 1.1 models. They're all excellent and are being widely embraced by the AI art community. They're designed for prompt-based editing.

Right now, if you're looking to get into open AI image generation rather than just using one of the simpler text-to-image tools, I'd suggest experimenting with FLUX. The different models have different licensing terms, so make sure to check them out. You can find out more [over on GitHub](https://github.com/black-forest-labs/flux2).

For non-developers, the simplest way to use FLUX is through online AI art generators like NightCafe, Tensor.Art, and Civitai—though the [FLUX playground](https://playground.bfl.ai/image/generate) is much improved. Sign up for a free account, give it a go, and compare it side by side with some of the other models. But again, be warned that the content on these sites may not be entirely SFW.

**FLUX pricing:** Depends on the platform, but many offer free credits so you can try them out.

## Best AI image generator for integrating AI-generated images into photos

### [Adobe Firefly](https://www.adobe.com/products/firefly/features/text-to-image.html)

https://images.ctfassets.net/lzny33ho1g45/6KPLNbYlvyWTbrmT46ySii/de135d3226837a0639936fad525b4a8a/image10.png

**Adobe Firefly pros:**

- Integrates well with Adobe's apps, especially Photoshop

- Powerful when it's matching an image


**Adobe Firefly cons:**

- Not the best as a pure text-to-image model


Adobe has been building AI tools into its apps for almost two decades, so it should be no surprise that it has one of the most powerful text-to-image generators—at least in terms of how it integrates with other tools. You can try out its AI model, [Firefly](https://zapier.com/blog/adobe-firefly/), on the web for free or through [Adobe Express](https://zapier.com/blog/adobe-express-ai), but it's at its best in the latest version of Photoshop. (It also supports other models now, including Nano Banana and GPT Image 1.5, but I'm going to focus on Firefly.)

Firefly has a few tricks up its sleeve. In addition to being capable of generating new images from a detailed text description, it can create text effects from a written prompt (think, the word "TOAST" written with letters that look like they're made from toast), recolor vector artwork, or add AI-generated elements to your images. You can test all these out through the web app, but it's that last feature where Firefly stands out.

Taken purely as a text-to-image generator, Firefly's results can be pretty hit and miss. It can match the best image generators for some prompts, but for others, I question what it was aiming to do. On the other hand, its integration with Photoshop, the industry standard image editor, is next level.

The two best features are Generative Fill and Generative Expand. With Generative Fill, you use Photoshop's regular tools to select an area of your image, and then, just by clicking a button and typing a prompt, you can replace it with something else. With Generative Expand, you can add to the outside of your image. Crucially, both tools understand the context of your image. In the screenshot above, you can see that Photoshop has matched the depth-of-field-blur for the forest I added using Generative Fill. It looks cohesive.

As much as other tools started the conversation about image-generating AIs, Adobe's Firefly was the first implementation of an AI photo generator that didn't feel like a party trick but a tool. Other apps are now doing similar things, but Firefly is unique in that it's available to the millions of professionals who use Adobe apps every day.

**Firefly pricing:** Limited free credits; from $9.99 for Firefly Standard with 2,000 credits/month; Photoshop is available from $19.99/month as part of the Creative Cloud Photography Plan, which comes with 25 generative credits per month.

## The best AI image generator for graphic design

### [**Recraft**](https://www.recraft.ai/)

https://images.ctfassets.net/lzny33ho1g45/3ZU5phnoABT9vgevnLFlcG/c49b85ee8952e8d8361761dc21426b1c/image7.png

**Recraft pros:**

- One of the most powerful and usable AI image generators

- Graphic design features are second to none


**Recraft cons:**

- More complicated to use than some of the other apps


Recraft is probably the most impressive app on this list. Its model is excellent and able to generate whatever you want, from photorealistic images to interesting logo designs. But it's the tools that Recraft has built around its model that really make it stand out.

Here's one example. Recraft allows you to create image sets that all fit the same style and color panel from a single set of prompts. You have all the style, color, and controls you need to dial things in, and it does an exceptional job right off the bat. Once you're happy with your images, you can export them as JPGs (fine), PNGs (better), or SVGs (amazing). Instead of being limited to small individual images, right from Recraft, you can create matching scalable design elements.

On top of that, you can use Recraft to create product mockups that combine multiple AI elements, in-paint and out-paint to add elements and combine images, adjust images and AI-generated work, remove backgrounds, and so much more. It's got collaboration tools, a great workspace, and you can export your work to other apps like Photoshop or Illustrator. It's a real continuation of what Adobe has done integrating Firefly into Photoshop, and it's also adding additional third-party models.

**Recraft Pricing:** Free for 30 credits/day and limited features. From $12/month for Basic with 1,000 credits/month, commercial rights, and more artistic controls.

## Other AI image generators worth trying out

Over the past year, the overall standard of image generators has really improved. There are now a dozen different models that are almost equivalent in quality. I feel the eight above are the best choices for most people, but there are a handful of other apps that warrant mentioning:

- [Leonardo.Ai](https://leonardo.ai/). In addition to offering FLUX, image creation tool Leonardo.Ai (now owned by Canva) has developed its own Lucid Origin and Phoenix models. It's a solid platform that's aimed at businesses and creators. (Full disclosure: I've worked with them in the past, but I'd recommend it regardless. It only doesn't make the list because it puts so much emphasis on other models.)

- [Generative AI by Getty](https://www.gettyimages.ie/ai). Designed to generate commercially safe images, Generative AI by Getty is...fine. If you need images with zero commercial risk, it's worth a look—but the legal system doesn't seem to care about companies using images from Midjourney or Ideogram at this point.

- [Luma Photon](https://lumalabs.ai/photon). Luma Photon is another great model, though I found the [Dream Machine](https://lumalabs.ai/dream-machine) app that uses it a bit too offbeat.

- [Playground](https://playground.com/design). Playground is great for creating designs, but its reliance on a template system meant I felt it was a little out of scope for the list.

- There are a number of excellent models from Chinese AI companies, including [ByteDance SeedDream 5.0](https://seed.bytedance.com/en/seedream5_0_lite), [Hunyuan Image 3.0 by Tencent](https://hy-image.org/), [KlingAI Image 3.0](https://app.klingai.com/global/text-to-image/new), and [Qwen Image](https://chat.qwen.ai/c/guest). I found they weren't as easy to access or as feature-filled as the apps on the list above, but they're worth checking out if you see them.

- [Grok](https://grok.com/imagine). Grok has a good but very controversial image generator. The issues around its use keep it off the list.


If you want a laundry list of every AI image generator out there, including those that are built on top of all the models I've talked about, I made that too. It includes more than two dozen image generators: some are built into other tools, like [AI writing apps](https://zapier.com/blog/best-ai-writing-generator/), [photo editing apps](https://zapier.com/blog/best-ai-photo-editor/), or [stock photo sites](https://zapier.com/blog/best-free-stock-photos/); some let you [select from multiple models](https://zapier.com/blog/hugging-face/); and each one differs on how it approaches AI image generation. So if none of the apps on this list feel natural to you, check out my list of the [top AI art generators](https://zapier.com/blog/ai-art-generator/), and see if anything stands out.

## How to use an AI image generator

Ok, so you know what the best options are, but...now what? The team at Zapier has put together a bunch of resources to help you understand how to use these tools—and put them to work.

First, tutorials and walkthroughs for some of the best AI image generators:

- [How to use the ChatGPT image generator](https://zapier.com/blog/chatgpt-image-generation/)

- [How to use Midjourney](https://zapier.com/blog/how-to-use-midjourney/)

- [How to use FLUX.1](https://zapier.com/blog/flux-ai-image/)

- [How to use Adobe Firefly](https://zapier.com/blog/adobe-firefly/)


Plus, a guide for [how to write effective AI art prompts](https://zapier.com/blog/ai-art-prompts/), so you can get what you're looking for faster (and better) when generating images.

Once you've got the basics down, it's time to use these tools for more than just creating wacky pictures. Here are some [tips for how to use AI image generators at work](https://zapier.com/blog/ai-image-examples-for-business/).

## The legal and ethical implications of AI-generated images

AI-generated images are everywhere now, but that doesn't mean we shouldn't be asking questions about [how they should (or shouldn't) be used](https://zapier.com/blog/how-to-use-ai-badly/).

There aren't clear laws in place surrounding AI-generated images. And that goes for both sides of the coin: the U.S. Copyright Office [suggests that](https://fortune.com/2023/02/23/no-copyright-images-made-ai-artificial-intelligence/) AI-generated content isn't copyright-protected [without some kind of significant human input to the process](https://petapixel.com/2025/01/30/us-copyright-office-softens-its-stance-toward-registering-ai-generated-artworks/), and there aren't rules to protect artists whose work was scraped for AI training. (That's why Firefly was trained on licensed images and public domain content only.) They've [reaffirmed this stance](https://www.reuters.com/legal/litigation/us-copyright-office-denies-protection-another-ai-created-image-2023-09-06/), and the courts ( [including the Supreme Court](https://www.hklaw.com/en/insights/publications/2026/03/the-final-word-supreme-court-refuses-to-hear-case-on-ai-authorship)) [have sided with their interpretation](https://www.reuters.com/world/us/us-appeals-court-rejects-copyrights-ai-generated-art-lacking-human-creator-2025-03-18/).

You're not likely to get into trouble for using AI-generated images for a few social media posts or blog hero images, but because there's no line drawn in the sand yet, it can be risky to develop an entire strategy around AI-generated art. The results of the Midjourney vs. Disney and Universal case could be enlightening, but it may not affect regular users regardless of how it falls out. (For what it's worth, [Hollywood](https://nofilmschool.com/the-brutalist-ai) and [Netflix](https://www.cnet.com/tech/services-and-software/when-will-you-see-ai-generated-content-on-netflix-its-possible-you-already-have/) seem to already be using AI image generators all the time.)

Then there's the [issue of bias](https://zapier.com/blog/ai-ethics/). As of now, AI has a lot of the same biases as humans, and that can lead to everything from the portrayal of stereotypes to harmful content. I experienced this myself with the outputs I got from some of the apps while testing them, though other tools take deliberate steps to add diversity to the images they generate. It's up to us as humans to avoid it by reviewing AI-generated content for bias and refining our prompts to eliminate that bias as much as possible.

## What's next for AI image generators?

AI image generating is a rapidly evolving space—and more powerful models are available each time I update this article. (I've had to update this article five times over the past 18 months.) It's wild how good text-to-image models like Image 1.5, Reve, Midjourney, Ideogram, and FLUX are getting at rendering tricky concepts repeatedly. While they're still a somewhat niche tool now, if they continue getting better at this pace, they could really shake things up.

_This article was originally published in March 2023. The most recent update was in April 2026._

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="what-are-some-real-world-applications-of-multimodal-ai.md">
<details>
<summary>What are some real-world applications of multimodal AI?</summary>

Phase: [EXPLOITATION]

# What are some real-world applications of multimodal AI?

**Source URL:** <https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai>

Multimodal AI, which processes and combines different data types like text, images, audio, and sensor inputs, has practical applications across industries. By integrating multiple data sources, these systems improve accuracy and functionality in tasks that require contextual understanding. Below are three key areas where multimodal AI is being applied effectively today.

In healthcare, multimodal AI enhances diagnostics and patient care by merging medical imaging, electronic health records (EHRs), and sensor data. For example, a system might analyze a chest X-ray (image), a patient’s symptom descriptions (text), and vital signs from wearables (sensor data) to detect pneumonia. Models like Google’s **Med-PaLM 2** combine vision and language processing to interpret radiology images alongside clinical notes, reducing misdiagnosis risks. Another use case is monitoring postoperative recovery: wearable devices track movement and heart rate, while speech analysis detects pain or fatigue in a patient’s voice, enabling proactive interventions.

Autonomous vehicles rely heavily on multimodal AI to fuse data from cameras, LiDAR, radar, and GPS. A self-driving car processes road signs (visual data), pedestrian movements (video), and proximity sensor readings to navigate safely. Tesla’s Autopilot, for instance, uses neural networks to combine camera feeds with ultrasonic sensors, improving object detection in varied lighting or weather. Similarly, companies like Waymo train models to correlate map data with real-time sensor inputs, ensuring precise localization and path planning. This redundancy across modalities helps address limitations of single-sensor systems, such as camera failures in low light.

Customer service and content moderation also benefit from multimodal approaches. Virtual assistants like Amazon’s Alexa process voice commands while analyzing user history (text) to personalize responses. In moderation, platforms like YouTube use AI to flag harmful content by scanning video frames (images), audio for hate speech, and user comments (text) simultaneously. For example, a post containing violent imagery and threatening text would be detected faster than if each modality were analyzed separately. Tools like **OpenAI’s CLIP** enable cross-modal matching, such as linking inappropriate images to their descriptive captions, improving accuracy in filtering violations. These systems reduce reliance on manual review while scaling to handle large data volumes.

</details>

</research_source>

<research_source type="guideline_exploitation" phase="exploitation" file="what-is-optical-character-recognition-ocr.md">
<details>
<summary>What Is Optical Character Recognition (OCR)?</summary>

Phase: [EXPLOITATION]

# What Is Optical Character Recognition (OCR)?

**Source URL:** <https://blog.roboflow.com/what-is-optical-character-recognition-ocr/>

https://storage.ghost.io/c/2c/8d/2c8d8c0d-1c15-4b6d-825e-02b78d61d40a/content/images/size/w1200/2024/04/image-730.webp

[Petru P.](https://blog.roboflow.com/author/potrimba/)

Published
Nov 21, 2023
•
7 min read


Have you ever wondered how a computer can understand the words on a photo, just like you do? That's where Optical Character Recognition, or [OCR](https://roboflow.com/ocr?ref=blog.roboflow.com), steps in. OCR takes the text you see in images – be it from a book, a receipt, or an old letter – and turns it into something your computer can read, edit, and search.

OCR finds widespread applications in tasks such as automated data entry, document digitization, text extraction from images, invoice processing, form recognition, and enhancing accessibility for visually impaired individuals.

Let's explore the fundamentals of OCR, understanding its workings, the challenges it addresses, and why it remains a crucial component of present and future technology.

## What Is Optical Character Recognition?

Optical Character Recognition (OCR) involves converting both handwritten and typed text from various sources, including images, videos, and scanned documents like PDFs, into a digitally editable format.

The output from OCR can be used by a computer to make decisions. Common use cases of OCR include:

Using OCR to read product identifiers on an assembly line. When each identifier is read, a piece of software can update an inventory tracking system to note the package with the given identifier has arrived.

Using OCR for scanned document recognition. This involves scanning printed documents, after which OCR software converts them into searchable and editable text. This method is widely employed to automate the handling of legal documents, extract data from bank statements and invoices, and streamline tasks like invoice processing and financial record-keeping.

Using OCR for “scene text recognition”, wherein an OCR system recognizes text from natural scenes, such as street signs, storefronts, or license plates.

Using OCR for alphanumeric, printed text, such as text that was written on a typewriter, or text that was printed out. But, you can also use OCR on handwriting. This usually involves using a separate system due to the differences in handwriting compared to printed text.

https://storage.ghost.io/c/2c/8d/2c8d8c0d-1c15-4b6d-825e-02b78d61d40a/content/images/2024/04/image-733.webp_Application of OCR on the text of a book._ [_Source_](https://www.edenai.co/post/optical-character-recognition-ocr-which-solution-to-choose?ref=blog.roboflow.com).

## How Optical Character Recognition Works

Let's discuss the typical steps modern OCR software uses to read text:

1.  **Image pre-processing**: After an image has been collected, the image undergoes pre-processing to enhance image quality, improving recognition. Pre-processing may involve resizing, contrast enhancement, binarization, noise reduction, and other techniques.
2.  **Text Detection**: Using a specialized deep-learning model trained on large datasets of images and text, the computer vision model detects regions in the input image that likely contain text. This process is usually a crucial step.
3.  **Layout Analysis**: After detecting text regions, the computer vision model conducts layout analysis to determine the structure and order of the text in the image. This step ensures the preservation of context and organizes the output for readability, but is not run by all OCR systems.
4.  **Text Recognition**: Detected text regions pass through a deep learning-based text recognition model, utilizing a combination of convolutional neural networks (CNNs) and recurrent neural networks (RNNs). This model recognizes individual characters and words in the input image, converting them into machine-readable text.
5.  **Language Model**: The final output undergoes post-processing to remove noise, correct spelling mistakes, and enhance overall accuracy. The predicted sequence of characters may contain errors, especially for long or uncommon words. Language models, acting as word processors, refine the output by predicting the probability of a sequence of words based on the input image. Statistical models and advanced methods, including deep learning, may be employed for this purpose.


https://storage.ghost.io/c/2c/8d/2c8d8c0d-1c15-4b6d-825e-02b78d61d40a/content/images/2024/04/image-738.webp_An example OCR system pipeline._

Having acquired an understanding of how OCR operates, let's examine its algorithms and investigate their operational mechanisms, covering the old and the new.

## Traditional Approaches to OCR

The first OCR algorithms rooted in image processing were typically rule-based systems. One well-known OCR that uses this approach is [Tesseract](https://github.com/tesseract-ocr/tesseract?ref=blog.roboflow.com). These systems relied on manually crafted features and heuristic rules to identify characters within images. The approach involved segmenting characters into individual units and applying a set of rules for character classification.

However, the accuracy and performance of these algorithms were often constrained due to the intricate process of developing and fine-tuning the necessary handcrafted features and rules for effective recognition.

### Tesseract

[Tesseract](https://roboflow.com/model/tesseract?ref=blog.roboflow.com), an open-source optical character recognition engine, originated at Hewlett-Packard Laboratories in the 1980s and subsequently became open-source in 2005.

Initially designed to recognize English text exclusively, [Tesseract](https://roboflow.com/model/tesseract?ref=blog.roboflow.com) has evolved into a versatile OCR engine. Working from traditional image processing principles, which involves manual logic unlike the deep learning processes in modern systems, [Tesseract](https://roboflow.com/model/tesseract?ref=blog.roboflow.com) analyzes images to identify patterns for character recognition.

First, Tesseract preprocesses the image to enhance input quality, a step which encompasses tasks like contrast improvement and noise removal. Following this, Tesseract employs feature extraction techniques, including edge detection and pattern recognition, to identify and recognize characters.

https://storage.ghost.io/c/2c/8d/2c8d8c0d-1c15-4b6d-825e-02b78d61d40a/content/images/2024/04/image-741.webp_Tesseract OCR engine pipeline._ [_Source_](https://www.researchgate.net/figure/Tesseract-OCR-engine-architecture_fig4_265087843?ref=blog.roboflow.com).

## Deep Learning Approaches to Optical Character Recognition

With the rise of deep learning, the integration of neural networks into OCR systems has gained substantial popularity. In particular, deep learning methodologies like [Convolutional Neural Networks](https://blog.roboflow.com/what-is-a-convolutional-neural-network/) and Long Short-Term Memory networks are leveraged, for precise text recognition. Neural networks regularly achieve better performance than traditional OCR techniques.

In recent years, there has also been a surge in novel approaches that leverage pre-trained image and text [Transformers](https://blog.roboflow.com/what-is-a-transformer/), a deep learning architecture. Transformers are ushering in a new era of end-to-end optical word recognition.

### PaddleOCR

[Paddle OCR](https://arxiv.org/abs/2009.09941?ref=blog.roboflow.com) is an open-source engine developed by Baidu's PaddlePaddle team. Leveraging deep learning techniques, including CNNs and recurrent neural networks, Paddle OCR excels in accurate text recognition. It comprises two key components: the detector and the extractor. The detector is tasked with pinpointing text within an image or document. It employs various algorithms, such as [EAST (Efficient and Accurate Scene Text)](https://paperswithcode.com/paper/east-an-efficient-and-accurate-scene-text?ref=blog.roboflow.com) or [DB (Differentiable Binarization)](https://arxiv.org/abs/1911.08947?ref=blog.roboflow.com) detectors, to identify text regions.

https://storage.ghost.io/c/2c/8d/2c8d8c0d-1c15-4b6d-825e-02b78d61d40a/content/images/2024/04/image-745.webp_DB (Differentiable Binarization) architecture._ [_Source_](https://arxiv.org/pdf/2009.09941.pdf?ref=blog.roboflow.com).

After the detector locates the text, the extractor comes into play, retrieving the text from the image. It employs a blend of Convolutional Neural Networks and Recurrent Neural Networks for precise text recognition. CNNs are utilized to extract features from the text, while RNNs play a crucial role in recognizing the sequence of characters.

https://storage.ghost.io/c/2c/8d/2c8d8c0d-1c15-4b6d-825e-02b78d61d40a/content/images/2024/04/image-748.webp_CRNN Extractor architecture._ [_Source_](https://arxiv.org/pdf/1507.05717.pdf?ref=blog.roboflow.com).

Paddle OCR stands out for its remarkable speed, making it among the swiftest OCR engines. Its efficiency is attributed to the utilization of parallel computing and GPU acceleration. This feature renders it particularly suitable for extensive OCR tasks, including document scanning and image recognition. Moreover, its adaptability shines through as it can be tailored and fine-tuned for specific tasks and datasets, enhancing its versatility and robustness in various OCR applications.

### TrOCR

[Transformer-based Optical Character Recognition (TrOCR)](https://arxiv.org/abs/2109.10282?ref=blog.roboflow.com) is one of many transformer-based [OCR models](https://playground.roboflow.com/models?tasks=ocr&ref=blog.roboflow.com). In contrast to traditional OCR systems, TrOCR adopts a methodology where both input image processing and the generation of corresponding text output occur within a single model.

The encoder segment of TrOCR employs a transformer-based architecture to handle the input image, segmenting it into a grid of patches and extracting visual features from each patch. Simultaneously, the decoder component utilizes a transformer-based model to produce the relevant text output, incorporating the visual features extracted from the image.

https://storage.ghost.io/c/2c/8d/2c8d8c0d-1c15-4b6d-825e-02b78d61d40a/content/images/2024/04/image-752.webp_TrOCR Architecture._ [_Source_](https://arxiv.org/pdf/2109.10282.pdf?ref=blog.roboflow.com).

This comprehensive and transformer-based methodology empowers TrOCR to attain strong performance across diverse OCR benchmarks, establishing the model as a highly dependable and effective tool for text recognition tasks.

## Advantages of Modern OCR Techniques

One of the primary advantages of OCR is its ability to automate the data entry process. Traditional manual data entry is not only time-consuming but also prone to errors. OCR technology streamlines this process by automatically extracting text from images or scanned documents, eliminating the need for human input. This automation significantly reduces the time required for tasks such as transcribing printed or handwritten text into digital formats.

In addition, OCR facilitates the digitization of documents, leading to improved efficiency in document management. By converting physical documents into digital formats, OCR enables easy storage, retrieval, and organization of information.

Digital documents are more accessible and can be quickly searched, eliminating the need for manual sorting through paper files. This advantage is particularly crucial in business settings where quick access to relevant information is essential.

## Limitations of Modern OCR Techniques

OCR systems, while proficient in recognizing printed text, often face challenges when it comes to accurately interpreting handwritten text. Handwriting is inherently diverse, varying in styles, shapes, and legibility. Unlike printed text, which follows standardized fonts and structures, handwritten text can exhibit significant variability, making it difficult for OCR algorithms to consistently and accurately recognize every nuance.

This limitation is particularly pronounced in scenarios where the handwriting is cursive, unconventional, or poorly formed. Overcoming this challenge requires more advanced techniques, such as integrating machine learning [models](https://blog.roboflow.com/best-ocr-models-text-recognition/) specifically trained on diverse handwritten datasets.

Furthermore,OCR systems can be sensitive to the quality of the input image and may struggle with images that have poor resolution, low contrast, or significant noise. Additionally, documents with complex layouts, multiple columns, or irregular text arrangements pose challenges for traditional OCR methods.

The image preprocessing steps performed by OCR engines, such as Tesseract, are crucial for improving recognition accuracy, but they may not always suffice for images with inherent complexities. Complex layouts can disrupt the OCR's ability to accurately segment text regions and extract meaningful content, leading to errors in character recognition.

To mitigate these issues, additional preprocessing techniques or more advanced OCR methods may be necessary, adding complexity to the implementation process.

## Optical Character Recognition

Optical Character Recognition (OCR) is the extraction of text from scanned documents or images, converting it into machine-readable data to enhance information accessibility.

OCR can reduce the time and resources needed for managing non-searchable or elusive data, eliminating manual data input, reducing errors, and boosting productivity. However, challenges such as handwritten text recognition and sensitivity to image quality persist in OCR systems.

Despite these challenges, OCR remains pivotal in present and future technology, automating data entry, improving document management, and enhancing accessibility. Its adaptability and multilingual support position OCR as a fundamental component in shaping technological advancements.

### **Cite this Post**

Use the following entry to cite this post in your research:

_[Petru P.](https://blog.roboflow.com/author/potrimba/). (Nov 21, 2023)._
_What Is Optical Character Recognition (OCR)?. Roboflow Blog: https://blog.roboflow.com/what-is-optical-character-recognition-ocr/_

</details>

</research_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

_No local file sources found._

</golden_source>