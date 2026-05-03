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

### Source [4]: https://unstructured.io/blog/unstructured-leads-in-document-parsing-quality-benchmarks-tell-the-full-story

Query: What are the documented error rates, failure modes, and performance statistics of traditional OCR and layout detection systems when handling complex documents with diagrams, nested tables, handwritten text, or poor scan quality?

Answer: Traditional OCR-era metrics fail on modern documents like scanned invoices, multi-column layouts, nested tables, handwritten annotations. Legacy systems assume single correct output, penalizing semantic equivalents. No specific rates for traditional OCR, but implies poor performance on real-world messy enterprise docs from healthcare/finance/manufacturing with these elements, as modern tools are benchmarked against them.

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

### Source [10]: https://www.philips.com/a-w/about/news/archive/features/2022/20221124-10-real-world-examples-of-ai-in-healthcare.html

Query: What are prominent real-world enterprise use cases and limitations of text-only AI approaches in fields like financial report analysis with charts, medical imaging diagnostics, and technical documentation with sketches?

Answer: AI use cases in medical imaging: precise CT positioning/reconstruction; fast MR acquisition; auto ultrasound measurements; faster/accurate radiology reads (e.g., MS lesions, lung nodules); stroke detection/planning; predictive patient deterioration. Enterprise: reduces dose/noise, speeds workflows, improves accuracy (e.g., 44% better MS diagnosis). Text-only limitations implicit: all require image processing (segmentation/detection); ultrasound/CT/MR rely on visual data AI can't handle text-only; manual methods error-prone/time-intensive, highlighting need for vision AI over text models for diagnostics.

-----

</details>

<details>
<summary>What are the practical advantages, trade-offs, and implementation best practices for feeding multimodal data to LLMs like Gemini using raw bytes, Base64 encoding, versus URLs from data lakes or public sources?</summary>

Phase: [EXPLOITATION]

### Source [12]: https://towardsdatascience.com/integrating-multimodal-data-into-a-large-language-model-d1965b8ab00c/

Query: What are the practical advantages, trade-offs, and implementation best practices for feeding multimodal data to LLMs like Gemini using raw bytes, Base64 encoding, versus URLs from data lakes or public sources?

Answer: The article discusses multimodal RAG using LlamaParse for parsing documents into markdown with images. LlamaParse premium mode extracts text, tables, and images into structured markdown. Images are downloaded as JPG files (screenshots of pages) and stored locally with paths added to node metadata (e.g., 'image_path'). During query retrieval, image nodes are created from these local paths and passed to multimodal LLM (gpt-4o-mini) alongside text context. Code shows: image_nodes.append(NodeWithScore(node=ImageNode(image_path=n.metadata["image_path"]))) and llm_response = self.multi_modal_llm.complete(prompt=fmt_prompt, image_documents=[image_node.node for image_node in image_nodes]). No mention of raw bytes, Base64, or URLs specifically for Gemini, but uses local file paths for images in OpenAI multimodal API calls. Advantages of local paths: Avoids network latency, full control. Trade-offs: Memory intensive for large images, requires local storage/download. Best practices: Parse with multimodal model (gpt-4o), store image screenshots per page, link via metadata, pass ImageNode objects to LLM.complete() with max_tokens limit. For larger docs, uses prompt caching to reduce cost. Compares gpt-4o-mini (cheaper, faster) vs Claude for context assignment.

-----

</details>

<details>
<summary>How can multimodal RAG retrieval tools be integrated as actions within ReAct-style reasoning agents to enable processing of images, PDFs, and visual documents in enterprise workflows?</summary>

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

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What are the latest 2025 advancements in linear projection modules and adapters for aligning image patch embeddings with LLM token spaces in unified decoder architectures, including any new mathematical formulations for better alignment?</summary>

Phase: [EXPLORATION]

### Source [61]: https://www.shadecoder.com/ja/topics/linear-projection-of-patches-a-comprehensive-guide-for-2025

Query: What are the latest 2025 advancements in linear projection modules and adapters for aligning image patch embeddings with LLM token spaces in unified decoder architectures, including any new mathematical formulations for better alignment?

Answer: Linear Projection of Patches: A Comprehensive Guide for 2025 discusses linear projection as mapping raw patch data (e.g., image patches) into a lower-dimensional vector space using a linear transformation: flatten patch contents and multiply by a matrix W (plus optional bias b) to obtain vector embedding V = W * x + b. This embedding is used as input for attention or feed-forward networks in vision transformers and unified encoders. Key 2025 advancements include faster convergence with learned projections over implicit learning, flexibility across modalities (image, audio, structured data) for unified designs, parameter efficiency with single projection matrices, compatibility with self-attention via fixed-size embeddings, and trends like low-rank/structured matrices, hybrid conv-projections, and efficient designs for edge deployment. Benefits: dimensionality control, faster training, modality-agnostic encoders. Implementation: patch extraction, linear/1x1 conv projection, embedding dimension matching LLM, positional encoding, normalization. No specific adapters or LLM token alignment mentioned; focuses on general patch-to-embedding projection in 2025 models. Common pitfalls: poor patch size, mismatched dimensions, ignoring positional info. (198 words)

-----

-----

Phase: [EXPLORATION]

### Source [62]: https://arxiv.org/html/2505.02567v6

Query: What are the latest 2025 advancements in linear projection modules and adapters for aligning image patch embeddings with LLM token spaces in unified decoder architectures, including any new mathematical formulations for better alignment?

Answer: Unified Multimodal Understanding and Generation Models: Advances, Challenges, and Opportunities (arXiv:2505.02567v6, updated Jan 2026) surveys 2025 unified models. Key advancements in linear projections/adapters for aligning image patch embeddings with LLM token spaces: MiniGPT-4 uses single learnable linear layer to project CLIP ViT image embeddings to Vicuna LLM token space. DreamLLM employs lightweight linear projection aligning CLIP embeddings with language tokens. Many semantic encoding models (e.g., Emu, LaViT, VL-GPT, MM-Interleaved, PUMA) use linear projections post-CLIP/EVA-CLIP to map visual features to LLM space, often with adapters like ViT-Adapter or pooling for multi-granular fusion. Mini-Gemini uses cross-attention after dual encoders but linear projection common. No new mathematical formulations explicitly detailed beyond standard linear transforms (e.g., MLP or 1x1 conv); focus on lightweight, efficient projections in AR/hybrid unified decoders for vision-language alignment. Trends: dynamic tokenization (LaViT), token enhancement, hybrid with diffusion decoders. Challenges: tokenization for AR generation, cross-modal attention efficiency. (187 words)

-----

-----

Phase: [EXPLORATION]

### Source [63]: https://www.ijcai.org/proceedings/2025/0107.pdf

Query: What are the latest 2025 advancements in linear projection modules and adapters for aligning image patch embeddings with LLM token spaces in unified decoder architectures, including any new mathematical formulations for better alignment?

Answer: MAGE: Multimodal Alignment and Generation Enhancement via Bridging Visual and Semantic Spaces (IJCAI-2025) proposes Intelligent Alignment Network (IAN) as projector after CLIP ViT-L/14: Vector Alignment Block (VAB) uses MLP + learnable normalization for dimensional alignment V' = MLP(V) where V from vision encoder to LLM dim Dl; Semantic Enhancement Block (SEB) uses cross-attention with CNN patch features b as query, global CLIP-aligned a as key/value for refined V'' integrating local/global visuals. Trained with dual loss: ITG (cross-entropy autoregressive L_ITG = -∑ log p(y_i | y<i, X_img, X_text)) and ITDM (MSE L_ITDM = (1/N)∑ ||d_IAN - d_LLM||^2), total L = L_ITG + L_ITDM. Outperforms linear/Q-Former baselines on MMBench/SEED (e.g., 73.9/67.8 vs. 67.7/61.6 with 144 tokens). IAN bridges patch embeddings to LLM space in unified Vicuna-13B decoder, reducing tokens while enhancing alignment. (162 words)

-----

</details>

<details>
<summary>How do multimodal LLMs handle variable resolution inputs and dynamic patching strategies for high-resolution PDFs and images to balance accuracy and computational cost in production RAG systems?</summary>

Phase: [EXPLORATION]

### Source [64]: https://www.linkedin.com/posts/rishirajgupta04_machinelearning-multimodal-llm-activity-7383016856481255424-pDaO

Query: How do multimodal LLMs handle variable resolution inputs and dynamic patching strategies for high-resolution PDFs and images to balance accuracy and computational cost in production RAG systems?

Answer: Multimodal LLMs struggle with high-resolution images because they break images into thousands of patches, each treated as a token, exploding compute costs during vision-text fusion. For a 1024x1024 HD image, this creates 1k+ extra tokens, leading to over 1M more attention operations. Vision encoders like ViT output dense features that don't mesh well with text tokens, causing VRAM issues and slowdowns. Solutions include Hierarchical Vision Processing: process low-res overview first, then zoom into key areas using attention maps for dynamic region spotlighting. This reduces patches from 1k+ to hundreds. Layered encoders with pooling enable one forward pass. NVIDIA's ecosystem uses CUDA ops for fused patch-text blends. In production RAG like NVIDIA Nemotron, ingest PDFs/images with nemoretriever-ocr-v1 and detectors, achieving 15× faster multimodal PDF extraction and 35× storage efficiency by structuring pages and using multimodal embeddings like omni-embed-nemotron-3b for slides/figures.

-----

-----

Phase: [EXPLORATION]

### Source [65]: https://towardsai.net/p/l/enhancing-llm-capabilities-the-power-of-multimodal-llms-and-rag

Query: How do multimodal LLMs handle variable resolution inputs and dynamic patching strategies for high-resolution PDFs and images to balance accuracy and computational cost in production RAG systems?

Answer: Multimodal LLMs handle variable resolution inputs via Vision Transformers (ViT) that divide images into fixed-size patches (e.g., 16x16), flatten them into vectors, add positional embeddings, and process through Transformer encoder layers capturing global dependencies. For high-res images, dynamic high-resolution strategies segment into patches based on resolution. In production RAG, multimodal pipelines extract from PDFs using PyMuPDF for text/images/tables, process into chunks with metadata, embed using joint models like Gemini for text/images into shared space, store in vector DBs like Chroma. Retrieval uses hybrid similarity search. Flamingo uses Perceiver Resampler to convert variable visual features to fixed visual tokens. LLaVA projects CLIP ViT features via MLP to LLM space. Production systems cache embeddings, version indexes, monitor latency per modality to balance cost/accuracy.

-----

-----

Phase: [EXPLORATION]

### Source [66]: https://www.decodingai.com/p/the-king-of-multi-modal-rag-colpali

Query: How do multimodal LLMs handle variable resolution inputs and dynamic patching strategies for high-resolution PDFs and images to balance accuracy and computational cost in production RAG systems?

Answer: ColPali handles high-res PDFs/images by converting to high-DPI images (300 DPI), processing via ColQwen2.5 VLM splitting into patches for multi-vector embeddings capturing spatial relationships, stored in Qdrant with MAX_SIM comparator. Retrieval embeds query, searches similar pages, retrieves images for multimodal LLM like Claude Sonnet. Balances cost by preserving visuals without text extraction loss, using cosine similarity on 128-dim embeddings. Production pipeline: PDF to JPEG pages, ColPali embeddings, Qdrant storage with metadata (session/page), query-time image retrieval. Achieves visual understanding of tables/figures while reducing compute via efficient multi-vector search.

-----

-----

Phase: [EXPLORATION]

### Source [67]: https://www.augmentcode.com/guides/multimodal-rag-development-12-best-practices-for-production-systems

Query: How do multimodal LLMs handle variable resolution inputs and dynamic patching strategies for high-resolution PDFs and images to balance accuracy and computational cost in production RAG systems?

Answer: Production multimodal RAG preserves structure via Unstructured library for PDF partitioning into JSON with hierarchy (parent_id), generates modality-aware embeddings early with joint encoders like CLIP/LLaVA. Stores raw assets beside vectors (S3 URLs). Hybrid retrieval: vector (0.6wt), BM25 keyword (0.3), metadata (0.1). Caches encoder outputs via content-hash in Redis to avoid GPU re-encoding costs ($0.02/M tokens). Modular pipelines with async queues. Monitors modality mix/latency with OpenTelemetry/Prometheus. For high-res, dynamic chunking adapts to content type, versioning indexes/encoders.

-----

-----

Phase: [EXPLORATION]

### Source [68]: https://arxiv.org/html/2510.12793v1

Query: How do multimodal LLMs handle variable resolution inputs and dynamic patching strategies for high-resolution PDFs and images to balance accuracy and computational cost in production RAG systems?

Answer: ViCO uses Visual Resolution Router (ViR) as binary classifier selecting compression (64 vs 256 tokens/patch) based on semantic complexity. Consistency Training minimizes KL divergence between responses at different rates. Router trained on loss ratio ri = L_compressed / L_original, threshold τ at 60th percentile. Patches with high semantic content (text/objects) get high-res, backgrounds low-res, reducing tokens ~50-70% with <0.5% perf loss on OCRBench/MMStar. Handles variable res by patch-level dynamic allocation, improving throughput 1.3-3.8x.

-----

</details>

<details>
<summary>What are the key optimization techniques and quantization methods for deploying multimodal embedding models in resource-constrained environments for real-time document retrieval in AI agents?</summary>

Phase: [EXPLORATION]

### Source [69]: https://milvus.io/ai-quick-reference/what-quantization-techniques-work-well-for-multimodal-embeddings

Query: What are the key optimization techniques and quantization methods for deploying multimodal embedding models in resource-constrained environments for real-time document retrieval in AI agents?

Answer: Quantization techniques for multimodal embeddings aim to reduce memory usage and computational costs while preserving the quality of combined text, image, or audio representations. Three effective methods include scalar quantization, product quantization, and binary quantization. Each balances trade-offs between compression ratio, inference speed, and accuracy, making them suitable for different scenarios in multimodal applications.

Scalar quantization reduces the precision of embedding values (e.g., from 32-bit floats to 8-bit integers) uniformly across all dimensions. This is straightforward to implement and works well when embeddings have a uniform distribution of values. For example, CLIP embeddings (which align text and images) can often tolerate 8-bit quantization with minimal accuracy loss, as shown in benchmarks like the Flickr30K retrieval task. Libraries like PyTorch’s quantize module simplify this process by scaling and rounding values. However, scalar quantization struggles with embeddings that have outliers or highly skewed distributions, as compressing extreme values can distort similarity scores.

Product quantization (PQ) divides high-dimensional embeddings into subvectors and quantizes each separately, achieving higher compression ratios. This is particularly useful for multimodal systems that require efficient nearest-neighbor search, such as recommendation engines combining user text queries and product images. For instance, Facebook’s FAISS library uses PQ to compress billion-scale multimodal datasets, enabling real-time retrieval. By training separate codebooks for each subvector, PQ preserves more nuanced relationships between modalities than scalar methods. However, PQ adds complexity during training and inference, as it requires maintaining codebooks and reconstructing vectors during searches.

Binary quantization (e.g., binarizing embeddings to 0/1 values) offers extreme compression and ultra-fast similarity computation via bitwise operations. This works best for applications prioritizing speed and memory savings over exact accuracy, such as on-device multimodal search in mobile apps. For example, binary versions of OpenAI’s CLIP embeddings can reduce memory usage by 32x while retaining ~80% of retrieval accuracy. However, binary methods risk significant information loss, especially for embeddings capturing subtle cross-modal relationships. Hybrid approaches, like using binary codes for coarse retrieval followed by higher-precision reranking, can mitigate this.

When choosing a technique, consider the use case: scalar quantization suits balanced value distributions, PQ excels in high-compression retrieval systems, and binary methods prioritize speed. Tools like TensorFlow Lite (for scalar) and FAISS (for PQ) provide off-the-shelf implementations. Testing accuracy after quantization using domain-specific benchmarks (e.g., cross-modal retrieval metrics) is critical to validate performance trade-offs.

-----

-----

Phase: [EXPLORATION]

### Source [70]: https://qdrant.tech/blog/qdrant-skills-release/

Query: What are the key optimization techniques and quantization methods for deploying multimodal embedding models in resource-constrained environments for real-time document retrieval in AI agents?

Answer: Production vector search optimization for resource-constrained environments includes scalar int8 quantization, enabled with always_ram=true, to compress vectors and reduce memory usage (e.g., from ~29GB to ~7.5GB). Binary quantization cuts memory 32x but requires oversampling with rescore to preserve recall. Other techniques: reduce default_segment_number to 2 for fewer, larger segments to improve throughput; lower hnsw_ef to 64 (controls accuracy, not throughput); use batch search API to amortize overhead; set optimizer_cpu_budget: 2 to reserve CPU cores for queries; move vectors to disk with NVMe for latency-sensitive production. For high QPS (e.g., from 150 to 500), combine quantization with segment optimization. These primitives compound for real-time retrieval, balancing memory, latency, recall, and throughput in AI agents.

-----

-----

Phase: [EXPLORATION]

### Source [71]: https://solve.mit.edu/challenges/2024-global-health-challenge/solutions/86834

Query: What are the key optimization techniques and quantization methods for deploying multimodal embedding models in resource-constrained environments for real-time document retrieval in AI agents?

Answer: For deploying multimodal vector embedding models in resource-limited settings, key optimization techniques include model pruning, quantization, and architecture optimization to reduce computational footprint. These data and computation-efficient methods enable self-supervised learning frameworks to generate high-quality embeddings from medical images (e.g., satellite images, fundus photos, chest X-rays) without extensive labeled data or resources. The framework is tailored for low-resource environments with limited computational power, AI expertise, and connectivity, supporting tasks like similarity retrieval. Additional strategies: efficient data structures for minimal memory usage, resource-efficient ML models, parallel computing, and automated code optimization using ML to streamline development and deployment.

-----

</details>

<details>
<summary>In what ways do attention visualization and interpretability tools reveal how multimodal LLMs process spatial relationships in diagrams and tables compared to traditional OCR approaches?</summary>

Phase: [EXPLORATION]

### Source [72]: https://www.sciencedirect.com/org/science/article/pii/S1546221825006630

Query: In what ways do attention visualization and interpretability tools reveal how multimodal LLMs process spatial relationships in diagrams and tables compared to traditional OCR approaches?

Answer: Extracting data from visually rich documents and charts using traditional OCR-based parsing faces challenges including layout complexity in unstructured formats, limitations in recognizing visual elements, and correlations between document parts. Simply extracting text is insufficient; advanced reasoning is essential. The paper evaluates LLMs' ability to answer chart questions using images versus PDF parsing. ColPali identifies relevant chart pages. Google’s Gemini processes images from PDFs or direct PDF content. Findings highlight limitations of OCR in visual document understanding (VrDU) and advantages of multimodal methods in data extraction and reasoning. Image-based approaches enhance chart comprehension for accurate data extraction and reasoning over complex layouts compared to OCR.

-----

-----

Phase: [EXPLORATION]

### Source [73]: https://www3.cs.stonybrook.edu/~mueller/papers/Charts%20of%20Thought%20TVCG.pdf

Query: In what ways do attention visualization and interpretability tools reveal how multimodal LLMs process spatial relationships in diagrams and tables compared to traditional OCR approaches?

Answer: Charts-of-Thought prompting guides multimodal LLMs through structured data extraction, verification, sorting, and analysis for visualization interpretation, mimicking human processes. Standard prompting fails on VLAT tasks like value retrieval; structured prompting improves accuracy dramatically (e.g., Claude-3.7-sonnet VLAT score 50.17 vs human 28.82). LLMs exceed humans on tasks like retrieve value, find trends, with 100% accuracy on many chart types. This reveals LLMs process spatial relationships via step-by-step extraction of axes, data points, enabling comparisons and reasoning beyond OCR text extraction. No explicit attention visualization, but structured process uncovers how LLMs handle spatial data in charts/tables vs traditional methods.

-----

-----

Phase: [EXPLORATION]

### Source [74]: https://arxiv.org/html/2506.21600v1

Query: In what ways do attention visualization and interpretability tools reveal how multimodal LLMs process spatial relationships in diagrams and tables compared to traditional OCR approaches?

Answer: Unstructured OCR text impairs MLLM performance on document understanding benchmarks like MMLongBench by causing attention dispersion and structure loss. Structured LaTeX-encoded OCR preserves layout/spatial relationships in tables/diagrams, improving accuracy (e.g., Qwen2.5-VL +11.8% on MMLongBench). Attention analysis shows images alone yield scattered attention sensitive to boundaries; structured text induces focused, structured attention on semantic regions (tables, charts), reducing waste. This reveals MLLMs process spatial relationships via constrained attention guided by structure, outperforming OCR by maintaining hierarchical organization and correlations, especially for charts/tables needing visual-text integration.

-----

-----

Phase: [EXPLORATION]

### Source [75]: https://aclanthology.org/2025.xllm-1.2.pdf

Query: In what ways do attention visualization and interpretability tools reveal how multimodal LLMs process spatial relationships in diagrams and tables compared to traditional OCR approaches?

Answer: Compares MLLMs (GPT-4o, Phi-3 Vision) vs TATR+OCR on PubTables-1M. TATR excels in structural layout (98.2% F1), but MLLMs superior in cell text content (GPT-4o 89.6% GriTS). GPT-4o handles spatial structures well via structured JSON prompting, bypassing OCR errors. No attention viz, but reveals MLLMs interpret table spatial relationships (rows/columns) directly from images, reducing OCR limitations in complex layouts, though TATR better for pure structure.

-----

</details>

<details>
<summary>How are multimodal AI techniques from document processing being adapted for real-time sensor fusion in autonomous robotics and drone navigation systems?</summary>

Phase: [EXPLORATION]

### Source [76]: https://www.mdpi.com/1424-8220/25/3/856

Query: How are multimodal AI techniques from document processing being adapted for real-time sensor fusion in autonomous robotics and drone navigation systems?

Answer: In autonomous vehicles (AVs), multi-sensor fusion integrates data from cameras, LiDAR, radar, ultrasonic sensors, GPS, and IMU to overcome individual sensor limitations like weather sensitivity or low resolution. Fusion strategies are categorized into low-level (raw data integration for high precision but high computation), mid-level (feature-level for balanced efficiency and accuracy), and high-level (decision-level for modularity and fault tolerance). Advanced deep learning techniques including CNNs, RNNs, Transformers, and RL process high-dimensional multimodal data streams for perception, localization, and navigation. Challenges include massive data volumes (gigabytes/second), real-time processing, sensor noise, heterogeneity, and lack of interpretability. Techniques like Kalman filters, UKF, and hybrid approaches address nonlinear estimation and drift. The survey emphasizes real-time robustness in dynamic environments through strategic fusion at different pipeline stages, balancing data richness with computational efficiency.

-----

-----

Phase: [EXPLORATION]

### Source [77]: https://arxiv.org/pdf/2504.02477?

Query: How are multimodal AI techniques from document processing being adapted for real-time sensor fusion in autonomous robotics and drone navigation systems?

Answer: Multimodal fusion strategies in robotics integrate vision, language, depth, LiDAR, and IMU data using encoder-decoder frameworks, attention mechanisms, and GNNs for semantic scene understanding, 3D object detection, SLAM, navigation, and manipulation. LiDAR-camera fusion occurs at voxel, point, or ROI levels with attention-based methods like TransFusion and BEVFusion achieving state-of-the-art in autonomous driving. Embodied navigation fuses visual goals, instructions, and topological maps via models like InstructNav and NaVid. SLAM systems like LVI-SAM tightly couple LiDAR, visual, and IMU data. VLA models align vision-language-action for manipulation. Evolution from early/mid/late fusion to Transformer variants enables real-time, robust perception in dynamic environments, compensating sensor limitations through complementary multimodal strengths.

-----

-----

Phase: [EXPLORATION]

### Source [78]: https://navisp.esa.int/news/article/Article%202:%20Multimodal%20AI:%20The%20Future%20of%20Autonomous%20Vehicles

Query: How are multimodal AI techniques from document processing being adapted for real-time sensor fusion in autonomous robotics and drone navigation systems?

Answer: Multimodal AI fuses data from cameras, GNSS, IMU, odometers, LiDAR, radar, SAR, and hyperspectral sensors for robust autonomous vehicle perception. Early fusion combines raw data, late fusion merges processed outputs, hybrid balances both. CNNs process camera data, 3D convolutions handle LiDAR, attention prioritizes relevant inputs, LSTMs/transformers manage temporal data. GANs/VAEs synthesize rare scenarios. End-to-end training optimizes fusion for object detection and navigation in fog, rain, darkness. Compensates individual sensor weaknesses (e.g., camera in low light, LiDAR in rain) via complementary modalities, enabling safe real-time decision-making.

-----

-----

Phase: [EXPLORATION]

### Source [79]: https://www.emergentmind.com/topics/multimodal-sensor-fusion-strategy

Query: How are multimodal AI techniques from document processing being adapted for real-time sensor fusion in autonomous robotics and drone navigation systems?

Answer: Multimodal sensor fusion integrates cameras, LiDAR, radar, IMU via early (raw data), intermediate (feature-level with attention), and late (decision-level) strategies. Deep architectures like CNNs, RNNs, Transformers enable real-time fusion for autonomous driving, robotics. Hybrid multilevel frameworks with adaptive weighting enhance robustness. Applications include adverse weather perception, human activity recognition. Techniques from document processing (e.g., attention, transformers) adapt to sensor data for 3D detection, SLAM, navigation in robotics/drones.

-----

-----

Phase: [EXPLORATION]

### Source [80]: https://www.mdpi.com/2504-446X/6/11/317

Query: How are multimodal AI techniques from document processing being adapted for real-time sensor fusion in autonomous robotics and drone navigation systems?

Answer: Multi-sensor drone detection fuses thermal IR, visible video, audio, ADS-B via late fusion (weighted confidence scores). YOLOv2 detects/classifies in video/IR (F1~0.78), LSTM on MFCC classifies audio (F1=0.93). Fish-eye motion detection steers pan/tilt platform. Fusion improves robustness, reducing false alarms (clouds, autofocus). Real-time system processes 6+ FPS, detects drones to 200m. Expands prior work with public multi-class dataset (drone/bird/airplane/helicopter), distance-based evaluation. Principles adaptable to robotics/drone navigation sensor fusion.

-----

</details>

<details>
<summary>What emerging intersections between multimodal LLMs and augmented reality frameworks are enabling new interactive experiences in fields like education and industrial training?</summary>

Phase: [EXPLORATION]

### Source [81]: https://medium.com/@hireaideveloper/how-multimodal-llms-are-changing-the-ai-landscape-8f86fe04123f

Query: What emerging intersections between multimodal LLMs and augmented reality frameworks are enabling new interactive experiences in fields like education and industrial training?

Answer: Multimodal LLMs enable interactive tutors in education and training that explain diagrams, solve math problems with images, analyze videos, and provide multimodal learning experiences combining visual aids with text explanations. Students benefit from these experiences. In the future, multimodal LLMs will integrate with AR/VR for immersive experiences in the metaverse, blending visual, auditory, and textual data seamlessly. This powers immersive experiences relevant to education and training fields.

-----

-----

Phase: [EXPLORATION]

### Source [82]: https://arxiv.org/html/2508.00737v2

Query: What emerging intersections between multimodal LLMs and augmented reality frameworks are enabling new interactive experiences in fields like education and industrial training?

Answer: LLMs integrate with VR for educational and training applications, providing adaptive feedback and acting as virtual tutors. Multimodal models like GPT-4V and LLaVA understand images, generate speech, and support interactive storytelling. The LearningverseVR platform uses generative AI for NPCs with personalities enabling personalized dialogue in learning. LLMs in VR create immersive experiences, dialogue systems, and educational simulations. Conversational agents valuable in educational and training applications.

-----

-----

Phase: [EXPLORATION]

### Source [83]: https://www.mdpi.com/2411-9660/10/2/30

Query: What emerging intersections between multimodal LLMs and augmented reality frameworks are enabling new interactive experiences in fields like education and industrial training?

Answer: AR-MLLM-based training system integrates AR, multimodal large language models (MLLMs), and prompt engineering for context-aware procedural guidance in complex machine operations. Converts technical text into step-by-step commands overlaid on physical machines. Case study in Coordinate Measuring Machine (CMM) operation training shows reduced time, workload, high accuracy in task recognition and feature measurement. Demonstrates potential for industrial training applications.

-----

-----

Phase: [EXPLORATION]

### Source [84]: https://www.nature.com/articles/s41598-025-98483-1

Query: What emerging intersections between multimodal LLMs and augmented reality frameworks are enabling new interactive experiences in fields like education and industrial training?

Answer: LLMs facilitate personalized learning, automated grading, intelligent tutoring systems in education. In industrial training, LLMs enhance manufacturing process optimization, predictive maintenance. Multimodal LLMs emerging for immersive experiences. Automotive industry uses LLMs for in-car virtual assistants improving training simulations.

-----

-----

Phase: [EXPLORATION]

### Source [85]: https://arxiv.org/pdf/2603.09536

Query: What emerging intersections between multimodal LLMs and augmented reality frameworks are enabling new interactive experiences in fields like education and industrial training?

Answer: LLM-driven multimodal expression generation for pedagogical agents in VR educational scenarios. Dynamically generates speech and gestures aligned with instructional semantics using semantically sensitive prompts. Enhances immersion, learning effectiveness, engagement in VR classrooms. Virtual agents in VR education, healthcare, professional training foster immersion and social presence.

-----

</details>

<details>
<summary>How is multimodal processing influencing sustainability efforts in environmental science, such as analyzing satellite imagery combined with textual climate reports for predictive modeling?</summary>

Phase: [EXPLORATION]

### Source [86]: https://www.mdpi.com/2071-1050/17/9/4134

Query: How is multimodal processing influencing sustainability efforts in environmental science, such as analyzing satellite imagery combined with textual climate reports for predictive modeling?

Answer: Wang et al. developed a multi-modal deep learning framework for environmental monitoring in mining enterprises, incorporating sensor data and satellite imagery with predictive modeling to enhance decision-making, reduce environmental hazards, and improve industrial compliance with environmental regulations. This system facilitates real-time monitoring of energy consumption, emissions, and operational efficiency, aiding industrial sustainability. The framework addresses heterogeneous data sources like IoT sensor data, satellite imagery, and operational logs for precise, adaptive energy optimization strategies in industrial manufacturing, contributing to carbon footprint reduction and sustainability efforts.

-----

-----

Phase: [EXPLORATION]

### Source [87]: https://www.nature.com/articles/s41598-025-11039-1

Query: How is multimodal processing influencing sustainability efforts in environmental science, such as analyzing satellite imagery combined with textual climate reports for predictive modeling?

Answer: The AQD dataset integrates multimodal data from ground sensors, meteorological sources, and satellite imagery for air quality forecasting. CNNs extract spatial pollutant patterns from satellite images, BiLSTM simulates temporal dynamics, attention mechanisms focus on informative features, GNNs model spatial correlations, and Neural ODEs capture continuous temporal evolution. This enhances predictive modeling for pollutants like PM2.5, PM10, CO, and ozone, improving environmental monitoring and sustainability by providing comprehensive insights into air quality dynamics.

-----

-----

Phase: [EXPLORATION]

### Source [88]: https://kingcenter.stanford.edu/sites/g/files/sbiybj16611/files/media/file/wp1078_0.pdf

Query: How is multimodal processing influencing sustainability efforts in environmental science, such as analyzing satellite imagery combined with textual climate reports for predictive modeling?

Answer: Satellite imagery, combined with machine learning, predicts sustainable development outcomes like poverty, agricultural productivity, and population. Moderate-resolution multispectral imagery reveals human activity patterns such as urban development and cropland productivity. Models using CNNs and transfer learning achieve strong performance, e.g., r²=0.75-0.83 for asset wealth. High revisit rates enable seasonal monitoring, supporting resource management and climate challenges through predictive modeling.

-----

-----

Phase: [EXPLORATION]

### Source [89]: https://www.climate.columbia.edu/sites/default/files/content/research/AI%20for%20Climate%20&%20Nature%20-%20Bezos%20Earth%20Fund/Landscape%20Assessment%20of%20AI%20for%20Climate%20and%20Nature%20-%20May%202024.pdf

Query: How is multimodal processing influencing sustainability efforts in environmental science, such as analyzing satellite imagery combined with textual climate reports for predictive modeling?

Answer: Multimodal AI integrates diverse data streams like satellite imagery, in-situ observations, drones, acoustic sensors, and camera traps for monitoring land cover, vegetation health, species distributions, and biodiversity. It synthesizes data for predictive modeling of environmental changes, enhancing sustainability efforts in climate and nature by providing comprehensive system dynamics analysis across scales.

-----

-----

Phase: [EXPLORATION]

### Source [90]: https://www.cutter.com/article/ai-takes-orbit-transforming-satellite-data-environmental-action

Query: How is multimodal processing influencing sustainability efforts in environmental science, such as analyzing satellite imagery combined with textual climate reports for predictive modeling?

Answer: AI transforms satellite data for environmental monitoring, using GenAI for pattern detection in imagery and in-space AI for real-time processing. Applications include deforestation tracking, air pollution detection, and disaster response. ESA, Google Earth Engine, NASA, and Planet Labs leverage AI for climate insights, enabling precise, scalable sustainability efforts through predictive modeling.

-----

</details>

<details>
<summary>In what ways are advancements in multimodal agents inspiring innovations in creative industries for generative design tools that process sketches, diagrams, and textual briefs simultaneously?</summary>

Phase: [EXPLORATION]

### Source [91]: https://arxiv.org/html/2511.05817v1

Query: In what ways are advancements in multimodal agents inspiring innovations in creative industries for generative design tools that process sketches, diagrams, and textual briefs simultaneously?

Answer: Advancements in multimodal large language models (LLMs) are inspiring innovations in creative industries by integrating generative AI into sketch-based design workflows for early-stage ideation. Tools like TalkSketch enable simultaneous freehand drawing and real-time speech input, capturing verbal descriptions during sketching to generate context-aware AI responses via a multimodal AI chatbot powered by Gemini models. This addresses challenges from a formative study (N=6 designers) where text-based prompting disrupted creative flow and created disconnects between ideation and sketching. Commercial platforms such as Adobe Firefly, Canva Magic Studio, and Figma AI assist rapid visual exploration, while prototypes like DesignPrompt (text, color, imagery prompts), DesignWeaver (palette refinement), Inkspire, and SketchAI use sketch-based interfaces for image generation and analogical inspiration. TalkSketch's sketching module supports drawing/editing, talking module transcribes speech in real-time, and AI chatbot provides proactive insights using Double Diamond framework and supports text/image generation modes. This multimodal approach supports fluid ideation, reducing tool-switching friction, prompt fatigue, and enabling context-aware proactivity, enhancing efficiency in graphic design and prototyping.

-----

-----

Phase: [EXPLORATION]

### Source [92]: https://www.atlantis-press.com/article/126021404.pdf

Query: In what ways are advancements in multimodal agents inspiring innovations in creative industries for generative design tools that process sketches, diagrams, and textual briefs simultaneously?

Answer: Multimodal AI systems capable of working across text, image, and other data formats are expanding creative possibilities in design and visual arts. Tools like Midjourney and DALL-E convert text prompts into sophisticated images using diffusion technology. In fashion design, GenAI translates sketches, mood boards, and text prompts into high-fidelity designs and 3D models, accelerating product development (McKinsey report: $150-275B potential profits). Platforms like Cala, Designovel, and DALL-E support designers in exploring creative possibilities without physical sampling costs. Emerging roles include AI Fashion Designer using GANs for patterns/textures from parameters like fabrics/colors, Customization Specialist for personalized items, and AI Fashion Data Analyst for trends. Generative AI in graphic design enables rapid asset generation (icons, patterns) via algorithms, with roles like Generative AI Graphic Designer and AI-Assisted Creative Director ensuring brand alignment. Prompt engineering and AI tool proficiency are key skills. These multimodal advancements improve efficiency in short video production by over 100%, facilitating experimentation while raising originality concerns.

-----

-----

Phase: [EXPLORATION]

### Source [93]: https://medium.com/@clairedigitalogy/how-gpt-4-and-multimodal-ai-are-reshaping-creative-work-de90ec6a4611

Query: In what ways are advancements in multimodal agents inspiring innovations in creative industries for generative design tools that process sketches, diagrams, and textual briefs simultaneously?

Answer: Multimodal AI bridges language and visual contexts, reshaping graphic design and product design. GPT-4 and multimodal systems like DALL-E enable text-to-image generation (e.g., 'Renaissance-style painting of a spaceman') and turn rough sketches into professional blueprints or suggest improvements, saving prototyping time. Canva integrates AI text-to-image for rapid original visuals. These tools enhance visual creativity in graphic design, photography, video production by processing text prompts alongside images, allowing product design assistance from sketches. Multimodal AI supports designers in early ideation by combining textual briefs with visual inputs for generative outputs, improving efficiency in creative workflows.

-----

-----

Phase: [EXPLORATION]

### Source [94]: https://arxiv.org/html/2501.02725v4

Query: In what ways are advancements in multimodal agents inspiring innovations in creative industries for generative design tools that process sketches, diagrams, and textual briefs simultaneously?

Answer: Multimodal large language models like GPT-4 (text and images) and Claude 3 Opus (images, tables, graphs, diagrams) advance generative design. Text-to-image models (Stable Diffusion SD3, DALL-E 3, Midjourney v6, Ideogram v1) use Multimodal Diffusion Transformer (MM-DiT) for strong cross-modal reasoning. LLM4GEN fuses LLM and CLIP features for complex prompts. Shutterstock's Generative 3D (NVIDIA Edify) prototypes 3D assets from text/image prompts. Vision Transformers (ViT, Swin) and diffusion models support sketch-to-image in design tools. These enable processing sketches, diagrams, textual briefs simultaneously for rapid visual exploration in creative industries.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="2025-the-year-ai-reasoning-models-took-over-a-month-by-month.md">
<details>
<summary>2025: The Year AI Reasoning Models Took Over — A Month-by-Month Review of Frontier Breakthroughs</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://medium.com/data-science-in-your-pocket/2025-the-year-ai-reasoning-models-took-over-a-month-by-month-review-of-frontier-breakthroughs-6ea2163f854f>

# 2025: The Year AI Reasoning Models Took Over — A Month-by-Month Review of Frontier Breakthroughs

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

<research_source type="scraped_from_research" phase="exploitation" file="best-embedding-model-for-rag-2026-10-models-compared-milvus-.md">
<details>
<summary>How to Choose the Best Embedding Model for RAG in 2026: 10 Models Benchmarked</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://milvus.io/blog/choose-embedding-model-rag-2026.md>

# How to Choose the Best Embedding Model for RAG in 2026: 10 Models Benchmarked

- Engineering


March 25, 2026

Cheney Zhang

**TL;DR:** We tested 10 [embedding models](https://zilliz.com/ai-models) across four production scenarios that public benchmarks miss: cross-modal retrieval, cross-lingual retrieval, key information retrieval, and dimension compression. No single model wins everything. Gemini Embedding 2 is the best all-rounder. Open-source Qwen3-VL-2B beats closed-source APIs on cross-modal tasks. If you need to compress dimensions to save storage, go with Voyage Multimodal 3.5 or Jina Embeddings v4.

## Why MTEB Isn’t Enough for Choosing an Embedding Model

Most [RAG](https://zilliz.com/learn/Retrieval-Augmented-Generation) prototypes start with OpenAI’s text-embedding-3-small. It’s cheap, easy to integrate, and for English text retrieval it works well enough. But production RAG outgrows it fast. Your pipeline picks up images, PDFs, multilingual documents — and a text-only [embedding model](https://zilliz.com/ai-models) stops being enough.

The [MTEB leaderboard](https://huggingface.co/spaces/mteb/leaderboard) tells you there are better options. The problem? MTEB only tests single-language text retrieval. It doesn’t cover cross-modal retrieval (text queries against image collections), cross-lingual search (a Chinese query finding an English document), long-document accuracy, or how much quality you lose when you truncate [embedding dimensions](https://zilliz.com/glossary/dimension) to save storage in your [vector database](https://zilliz.com/learn/what-is-a-vector-database).

So which embedding model should you use? It depends on your data types, your languages, your document lengths, and whether you need dimension compression. We built a benchmark called **CCKM** and tested 10 models released between 2025 and 2026 across exactly those dimensions.

## What Is the CCKM Benchmark?

**CCKM** (Cross-modal, Cross-lingual, Key information, MRL) tests four capabilities that standard benchmarks miss:

| Dimension | What It Tests | Why It Matters |
| --- | --- | --- |
| **Cross-modal retrieval** | Match text descriptions to the correct image when near-identical distractors are present | [Multimodal RAG](https://zilliz.com/learn/multimodal-rag) pipelines need text and image embeddings in the same vector space |
| **Cross-lingual retrieval** | Find the correct English document from a Chinese query, and vice versa | Production knowledge bases are often multilingual |
| **Key information retrieval** | Locate a specific fact buried in a 4K–32K character document (needle-in-a-haystack) | RAG systems frequently process long documents like contracts and research papers |
| **MRL dimension compression** | Measure how much quality the model loses when you truncate embeddings to 256 dimensions | Fewer dimensions = lower storage cost in your vector database, but at what quality cost? |

MTEB covers none of these. MMEB adds multimodal but skips hard negatives, so models score high without proving they handle subtle distinctions. CCKM is designed to cover what they miss.

## Which Embedding Models Did We Test? Gemini Embedding 2, Jina Embeddings v4, and More

We tested 10 models covering both API services and open-source options, plus CLIP ViT-L-14 as a 2021 baseline.

| Model | Source | Parameters | Dimensions | Modality | Key Trait |
| --- | --- | --- | --- | --- | --- |
| Gemini Embedding 2 | Google | Undisclosed | 3072 | Text / image / video / audio / PDF | All-modality, widest coverage |
| Jina Embeddings v4 | Jina AI | 3.8B | 2048 | Text / image / PDF | MRL + LoRA adapters |
| Voyage Multimodal 3.5 | Voyage AI (MongoDB) | Undisclosed | 1024 | Text / image / video | Balanced across tasks |
| Qwen3-VL-Embedding-2B | Alibaba Qwen | 2B | 2048 | Text / image / video | Open-source, lightweight multimodal |
| Jina CLIP v2 | Jina AI | ~1B | 1024 | Text / image | Modernized CLIP architecture |
| Cohere Embed v4 | Cohere | Undisclosed | Fixed | Text | Enterprise retrieval |
| OpenAI text-embedding-3-large | OpenAI | Undisclosed | 3072 | Text | Most widely used |
| [BGE-M3](https://zilliz.com/learn/bge-m3-and-splade-two-machine-learning-models-for-generating-sparse-embeddings) | BAAI | 568M | 1024 | Text | Open-source, 100+ languages |
| mxbai-embed-large | Mixedbread AI | 335M | 1024 | Text | Lightweight, English-focused |
| nomic-embed-text | Nomic AI | 137M | 768 | Text | Ultra-lightweight |
| CLIP ViT-L-14 | OpenAI (2021) | 428M | 768 | Text / image | Baseline |

## Cross-Modal Retrieval: Which Models Handle Text-to-Image Search?

If your RAG pipeline handles images alongside text, the embedding model needs to place both modalities in the same [vector space](https://zilliz.com/glossary/vector-embeddings). Think e-commerce image search, mixed image-text knowledge bases, or any system where a text query needs to find the right image.

### Method

We took 200 image-text pairs from COCO val2017. For each image, GPT-4o-mini generated a detailed description. Then we wrote 3 hard negatives per image — descriptions that differ from the correct one by just one or two details. The model has to find the right match in a pool of 200 images and 600 distractors.

An example from the dataset:

https://assets.zilliz.com/choose_embedding_model_rag_2026_9_3965746e33.pngVintage brown leather suitcases with travel stickers including California and Cuba, placed on a metal luggage rack against a clear blue sky — used as a test image in the cross-modal retrieval benchmark

> **Correct description:** “The image features vintage brown leather suitcases with various travel stickers including 'California’, 'Cuba’, and 'New York’, placed on a metal luggage rack against a clear blue sky.”
>
> **Hard negative:** Same sentence, but “California” becomes “Florida” and “blue sky” becomes “overcast sky.” The model has to actually understand the image details to tell these apart.

**Scoring:**

- Generate [embeddings](https://zilliz.com/glossary/vector-embeddings) for all images and all text (200 correct descriptions + 600 hard negatives).
- **Text-to-image (t2i):** Each description searches 200 images for the closest match. Score a point if the top result is correct.
- **Image-to-text (i2t):** Each image searches all 800 texts for the closest match. Score a point only if the top result is the correct description, not a hard negative.
- **Final score:** hard\_avg\_R@1 = (t2i accuracy + i2t accuracy) / 2

### Results

https://assets.zilliz.com/choose_embedding_model_rag_2026_1_6f1fddae56.pngHorizontal bar chart showing Cross-Modal Retrieval Ranking: Qwen3-VL-2B leads at 0.945, followed by Gemini Embed 2 at 0.928, Voyage MM-3.5 at 0.900, Jina CLIP v2 at 0.873, and CLIP ViT-L-14 at 0.768

Qwen3-VL-2B, an open-source 2B parameter model from Alibaba’s Qwen team, came in first — ahead of every closed-source API.

**Modality gap** explains most of the difference. Embedding models map text and images into the same vector space, but in practice the two modalities tend to cluster in different regions. The modality gap measures the L2 distance between those two clusters. Smaller gap = easier cross-modal retrieval.

https://assets.zilliz.com/choose_embedding_model_rag_2026_8_c5067a3434.pngVisualization comparing large modality gap (0.73, text and image embedding clusters far apart) versus small modality gap (0.25, clusters overlapping) — smaller gap makes cross-modal matching easier

| Model | Score (R@1) | Modality Gap | Params |
| --- | --- | --- | --- |
| Qwen3-VL-2B | 0.945 | 0.25 | 2B (open-source) |
| Gemini Embedding 2 | 0.928 | 0.73 | Unknown (closed) |
| Voyage Multimodal 3.5 | 0.900 | 0.59 | Unknown (closed) |
| Jina CLIP v2 | 0.873 | 0.87 | ~1B |
| CLIP ViT-L-14 | 0.768 | 0.83 | 428M |

Qwen’s modality gap is 0.25 — roughly a third of Gemini’s 0.73. In a [vector database](https://zilliz.com/learn/what-is-a-vector-database) like [Milvus](https://milvus.io/), a small modality gap means you can store text and image embeddings in the same [collection](https://milvus.io/docs/manage-collections.md) and [search](https://milvus.io/docs/single-vector-search.md) across both directly. A large gap can make cross-modal [similarity search](https://zilliz.com/glossary/similarity-search) less reliable, and you may need a re-ranking step to compensate.

## Cross-Lingual Retrieval: Which Models Align Meaning Across Languages?

Multilingual knowledge bases are common in production. A user asks a question in Chinese, but the answer lives in an English document — or the other way around. The embedding model needs to align meaning across languages, not just within one.

### Method

We built 166 parallel sentence pairs in Chinese and English across three difficulty levels:

https://assets.zilliz.com/choose_embedding_model_rag_2026_6_75caab66a7.pngCross-lingual difficulty tiers: Easy tier maps literal translations like 我爱你 to I love you; Medium tier maps paraphrased sentences like 这道菜太咸了 to This dish is too salty with hard negatives; Hard tier maps Chinese idioms like 画蛇添足 to gilding the lily with semantically different hard negatives

Each language also gets 152 hard negative distractors.

**Scoring:**

- Generate embeddings for all Chinese text (166 correct + 152 distractors) and all English text (166 correct + 152 distractors).
- **Chinese → English:** Each Chinese sentence searches 318 English texts for its correct translation.
- **English → Chinese:** Same in reverse.
- **Final score:** hard\_avg\_R@1 = (zh→en accuracy + en→zh accuracy) / 2

### Results

https://assets.zilliz.com/choose_embedding_model_rag_2026_2_d1c3500423.pngHorizontal bar chart showing Cross-Lingual Retrieval Ranking: Gemini Embed 2 leads at 0.997, followed by Qwen3-VL-2B at 0.988, Jina v4 at 0.985, Voyage MM-3.5 at 0.982, down to mxbai at 0.120

Gemini Embedding 2 scored 0.997 — the highest of any model tested. It was the only model to score a perfect 1.000 on the Hard tier, where pairs like “画蛇添足” → “gilding the lily” require genuine [semantic](https://zilliz.com/glossary/semantic-search) understanding across languages, not pattern matching.

| Model | Score (R@1) | Easy | Medium | Hard (idioms) |
| --- | --- | --- | --- | --- |
| Gemini Embedding 2 | 0.997 | 1.000 | 1.000 | 1.000 |
| Qwen3-VL-2B | 0.988 | 1.000 | 1.000 | 0.969 |
| Jina Embeddings v4 | 0.985 | 1.000 | 1.000 | 0.969 |
| Voyage Multimodal 3.5 | 0.982 | 1.000 | 1.000 | 0.938 |
| OpenAI 3-large | 0.967 | 1.000 | 1.000 | 0.906 |
| Cohere Embed v4 | 0.955 | 1.000 | 0.980 | 0.875 |
| BGE-M3 (568M) | 0.940 | 1.000 | 0.960 | 0.844 |
| nomic-embed-text (137M) | 0.154 | 0.300 | 0.120 | 0.031 |
| mxbai-embed-large (335M) | 0.120 | 0.220 | 0.080 | 0.031 |

The top 7 models all clear 0.93 on the overall score — the real differentiation happens on the Hard tier (Chinese idioms). nomic-embed-text and mxbai-embed-large, both English-focused lightweight models, score near zero on cross-lingual tasks.

## Key Information Retrieval: Can Models Find a Needle in a 32K-Token Document?

RAG systems often process lengthy documents — legal contracts, research papers, internal reports containing [unstructured data](https://zilliz.com/learn/introduction-to-unstructured-data). The question is whether an embedding model can still find one specific fact buried in thousands of characters of surrounding text.

### Method

We took Wikipedia articles of varying lengths (4K to 32K characters) as the haystack and inserted a single fabricated fact — the needle — at different positions: start, 25%, 50%, 75%, and end. The model has to determine, based on a query embedding, which version of the document contains the needle.

**Example:**

- **Needle:** “The Meridian Corporation reported quarterly revenue of $847.3 million in Q3 2025.”
- **Query:** “What was Meridian Corporation’s quarterly revenue?”
- **Haystack:** A 32,000-character Wikipedia article about photosynthesis, with the needle hidden somewhere inside.

**Scoring:**

- Generate embeddings for the query, the document with the needle, and the document without.
- If the query is more similar to the document containing the needle, count it as a hit.
- Average accuracy across all document lengths and needle positions.
- **Final metrics:** overall\_accuracy and degradation\_rate (how much accuracy drops from shortest to longest document).

### Results

https://assets.zilliz.com/choose_embedding_model_rag_2026_5_2bdc89516a.pngHeatmap showing Needle-in-a-Haystack accuracy by document length: Gemini Embed 2 scores 1.000 across all lengths up to 32K; top 7 models score perfectly within their context windows; mxbai and nomic degrade sharply at 4K+

Gemini Embedding 2 is the only model tested across the full 4K–32K range, and it scored perfectly at every length. No other model in this test has a context window that reaches 32K.

| Model | 1K | 4K | 8K | 16K | 32K | Overall | Degradation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Gemini Embedding 2 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 0% |
| OpenAI 3-large | 1.000 | 1.000 | 1.000 | — | — | 1.000 | 0% |
| Jina Embeddings v4 | 1.000 | 1.000 | 1.000 | — | — | 1.000 | 0% |
| Cohere Embed v4 | 1.000 | 1.000 | 1.000 | — | — | 1.000 | 0% |
| Qwen3-VL-2B | 1.000 | 1.000 | — | — | — | 1.000 | 0% |
| Voyage Multimodal 3.5 | 1.000 | 1.000 | — | — | — | 1.000 | 0% |
| Jina CLIP v2 | 1.000 | 1.000 | 1.000 | — | — | 1.000 | 0% |
| BGE-M3 (568M) | 1.000 | 1.000 | 0.920 | — | — | 0.973 | 8% |
| mxbai-embed-large (335M) | 0.980 | 0.600 | 0.400 | — | — | 0.660 | 58% |
| nomic-embed-text (137M) | 1.000 | 0.460 | 0.440 | — | — | 0.633 | 56% |

“—” means the document length exceeds the model’s context window.

The top 7 models score perfectly within their context windows. BGE-M3 starts to slip at 8K (0.920). The lightweight models (mxbai and nomic) drop to 0.4–0.6 at just 4K characters — roughly 1,000 tokens. For mxbai, this drop partly reflects its 512-token context window truncating most of the document.

## MRL Dimension Compression: How Much Quality Do You Lose at 256 Dimensions?

**Matryoshka Representation Learning (MRL)** is a training technique that makes the first N dimensions of a vector meaningful on their own. Take a 3072-dimension vector, truncate it to 256, and it still holds most of its semantic quality. Fewer dimensions mean lower storage and memory costs in your [vector database](https://zilliz.com/learn/what-is-a-vector-database) — going from 3072 to 256 dimensions is a 12x storage reduction.

https://assets.zilliz.com/choose_embedding_model_rag_2026_10_aef8755877.pngIllustration showing MRL dimension truncation: 3072 dimensions at full quality, 1024 at 95%, 512 at 90%, 256 at 85% — with 12x storage savings at 256 dimensions

### Method

We used 150 sentence pairs from the STS-B benchmark, each with a human-annotated similarity score (0–5). For each model, we generated embeddings at full dimensions, then truncated to 1024, 512, and 256.

https://assets.zilliz.com/choose_embedding_model_rag_2026_4_44266e5456.pngSTS-B data examples showing sentence pairs with human similarity scores: A girl is styling her hair vs A girl is brushing her hair scores 2.5; A group of men play soccer on the beach vs A group of boys are playing soccer on the beach scores 3.6

**Scoring:**

- At each dimension level, compute the [cosine similarity](https://zilliz.com/glossary/cosine-similarity) between each sentence pair’s embeddings.
- Compare the model’s similarity ranking to the human ranking using **Spearman’s ρ** (rank correlation).

> **What is Spearman’s ρ?** It measures how well two rankings agree. If humans rank pair A as most similar, B second, C least — and the model’s cosine similarities produce the same order A > B > C — then ρ approaches 1.0. A ρ of 1.0 means perfect agreement. A ρ of 0 means no correlation.

**Final metrics:** spearman\_rho (higher is better) and min\_viable\_dim (the smallest dimension where quality stays within 5% of full-dimension performance).

### Results

https://assets.zilliz.com/choose_embedding_model_rag_2026_3_7192725ed6.pngDot plot showing MRL Full Dimension vs 256 Dimension Quality: Voyage MM-3.5 leads with +0.6% change, Jina v4 +0.5%, while Gemini Embed 2 shows -0.6% at the bottom

If you’re planning to reduce storage costs in [Milvus](https://milvus.io/) or another vector database by truncating dimensions, this result matters.

| Model | ρ (full dim) | ρ (256 dim) | Decay |
| --- | --- | --- | --- |
| Voyage Multimodal 3.5 | 0.880 | 0.874 | 0.7% |
| Jina Embeddings v4 | 0.833 | 0.828 | 0.6% |
| mxbai-embed-large (335M) | 0.815 | 0.795 | 2.5% |
| nomic-embed-text (137M) | 0.781 | 0.774 | 0.8% |
| OpenAI 3-large | 0.767 | 0.762 | 0.6% |
| Gemini Embedding 2 | 0.683 | 0.689 | -0.8% |

Voyage and Jina v4 lead because both were explicitly trained with MRL as an objective. Dimension compression has little to do with model size — whether the model was trained for it is what matters.

A note on Gemini’s score: the MRL ranking reflects how well a model preserves quality after truncation, not how good its full-dimension retrieval is. Gemini’s full-dimension retrieval is strong — the cross-lingual and key information results already proved that. It just wasn’t optimized for shrinking. If you don’t need dimension compression, this metric doesn’t apply to you.

## Which Embedding Model Should You Use?

No single model wins everything. Here’s the full scorecard:

| Model | Params | Cross-Modal | Cross-Lingual | Key Info | MRL ρ |
| --- | --- | --- | --- | --- | --- |
| Gemini Embedding 2 | Undisclosed | 0.928 | 0.997 | 1.000 | 0.668 |
| Voyage Multimodal 3.5 | Undisclosed | 0.900 | 0.982 | 1.000 | 0.880 |
| Jina Embeddings v4 | 3.8B | — | 0.985 | 1.000 | 0.833 |
| Qwen3-VL-2B | 2B | 0.945 | 0.988 | 1.000 | 0.774 |
| OpenAI 3-large | Undisclosed | — | 0.967 | 1.000 | 0.760 |
| Cohere Embed v4 | Undisclosed | — | 0.955 | 1.000 | — |
| Jina CLIP v2 | ~1B | 0.873 | 0.934 | 1.000 | — |
| BGE-M3 | 568M | — | 0.940 | 0.973 | 0.744 |
| mxbai-embed-large | 335M | — | 0.120 | 0.660 | 0.815 |
| nomic-embed-text | 137M | — | 0.154 | 0.633 | 0.780 |
| CLIP ViT-L-14 | 428M | 0.768 | 0.030 | — | — |

“—” means the model doesn’t support that modality or capability. CLIP is a 2021 baseline for reference.

Here’s what stands out:

- **Cross-modal:** Qwen3-VL-2B (0.945) first, Gemini (0.928) second, Voyage (0.900) third. An open-source 2B model beat every closed-source API. The deciding factor was modality gap, not parameter count.
- **Cross-lingual:** Gemini (0.997) leads — the only model to score perfectly on idiom-level alignment. The top 8 models all clear 0.93. English-only lightweight models score near zero.
- **Key information:** API and large open-source models score perfectly up to 8K. Models below 335M start degrading at 4K. Gemini is the only model that handles 32K with a perfect score.
- **MRL dimension compression:** Voyage (0.880) and Jina v4 (0.833) lead, losing less than 1% at 256 dimensions. Gemini (0.668) comes last — strong at full dimension, not optimized for truncation.

### How to Pick: A Decision Flowchart

https://assets.zilliz.com/choose_embedding_model_rag_2026_7_b2bd48bdcc.pngEmbedding model selection flowchart: Start → Need images or video? → Yes: Need to self-host? → Yes: Qwen3-VL-2B, No: Gemini Embedding 2. No images → Need to save storage? → Yes: Jina v4 or Voyage, No: Need multilingual? → Yes: Gemini Embedding 2, No: OpenAI 3-large

### The Best All-Rounder: Gemini Embedding 2

On balance, Gemini Embedding 2 is the strongest overall model in this benchmark.

**Strengths:** First in cross-lingual (0.997) and key information retrieval (1.000 across all lengths up to 32K). Second in cross-modal (0.928). Widest modality coverage — five modalities (text, image, video, audio, PDF) where most models top out at three.

**Weaknesses:** Last in MRL compression (ρ = 0.668). Beaten on cross-modal by the open-source Qwen3-VL-2B.

If you don’t need dimension compression, Gemini has no real competitor on the combination of cross-lingual + long-document retrieval. But for cross-modal precision or storage optimization, specialized models do better.

## Limitations

- We didn’t include every model worth considering — NVIDIA’s NV-Embed-v2 and Jina’s v5-text were on the list but didn’t make this round.
- We focused on text and image modalities; video, audio, and PDF embedding (despite some models claiming support) weren’t covered.
- Code retrieval and other domain-specific scenarios were out of scope.
- Sample sizes were relatively small, so tight ranking differences between models may fall within statistical noise.

This article’s results will be outdated within a year. New models ship constantly, and the leaderboard reshuffles with every release. The more durable investment is building your own evaluation pipeline — define your data types, your query patterns, your document lengths, and run new models through your own tests when they drop. Public benchmarks like MTEB, MMTEB, and MMEB are worth monitoring, but the final call should always come from your own data.

[Our benchmark code is open-source on GitHub](https://github.com/zc277584121/mm-embedding-bench) — fork it and adapt it to your use case.

* * *

A few questions that come up when engineers are choosing an embedding model for production RAG:

**Q: Should I use a multimodal embedding model even if I only have text data right now?**

It depends on your roadmap. If your pipeline will likely add images, PDFs, or other modalities within the next 6–12 months, starting with a multimodal model like Gemini Embedding 2 or Voyage Multimodal 3.5 avoids a painful migration later — you won’t need to re-embed your entire dataset. If you’re confident it’s text-only for the foreseeable future, a text-focused model like OpenAI 3-large or Cohere Embed v4 will give you better price/performance.

**Q: How much storage does MRL dimension compression actually save in a vector database?**

Going from 3072 dimensions to 256 dimensions is a 12x reduction in storage per vector. For a [Milvus](https://milvus.io/) collection with 100 million vectors at float32, that’s roughly 1.14 TB → 95 GB. The key is that not all models handle truncation well — Voyage Multimodal 3.5 and Jina Embeddings v4 lose less than 1% quality at 256 dimensions, while others degrade significantly.

**Q: Is Qwen3-VL-2B really better than Gemini Embedding 2 for cross-modal search?**

On our benchmark, yes — Qwen3-VL-2B scored 0.945 versus Gemini’s 0.928 on hard cross-modal retrieval with near-identical distractors. The main reason is Qwen’s much smaller modality gap (0.25 vs 0.73), which means text and image [embeddings](https://zilliz.com/glossary/vector-embeddings) cluster closer together in vector space. That said, Gemini covers five modalities while Qwen covers three, so if you need audio or PDF embedding, Gemini is the only option.

**Q: Can I use these embedding models with Milvus directly?**

Yes. All of these models output standard float vectors, which you can [insert into Milvus](https://milvus.io/docs/insert-update-delete.md) and search with [cosine similarity](https://zilliz.com/glossary/cosine-similarity), L2 distance, or inner product. [PyMilvus](https://milvus.io/docs/install-pymilvus.md) works with any embedding model — generate your vectors with the model’s SDK, then store and search them in Milvus. For MRL-truncated vectors, just set the collection’s dimension to your target (e.g., 256) when [creating the collection](https://milvus.io/docs/manage-collections.md).

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="integrating-multimodal-data-into-a-large-language-model-towa.md">
<details>
<summary>Integrating Multimodal Data into a Large Language Model</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://towardsdatascience.com/integrating-multimodal-data-into-a-large-language-model-d1965b8ab00c/>

# Integrating Multimodal Data into a Large Language Model

Developing a context-retrieval, multimodal RAG using advanced parsing, semantic & keyword search, and re-ranking

[Umair Ali Khan](https://towardsdatascience.com/author/umairali-khan/)

Oct 17, 2024

18 min read

Large language models (LLMs) have a knowledge cutoff date and cannot answer queries to specific data not present in their knowledge base. For instance, LLMs cannot answer queries about data regarding a company’s meeting minutes from the last year. Similarly, LLMs are prone to hallucinate and provide plausible-looking wrong answers.

To overcome this issue, Retrieval Augment Generation (RAG) solutions are becoming increasingly popular. The main idea of an RAG is to integrate external documents into LLMs and guide its behavior to answer questions only from the external knowledge base. This is done by chunking the document(s) into smaller chunks, computing each chunk’s embeddings (numerical representations), and storing the embeddings as an index in a specialized vector database.

https://towardsdatascience.com/wp-content/uploads/2024/10/1ufSZoS254-yrqCqamF1hw.pngThe RAG workflow: a query is converted to embeddings, matched with a vector database by a retrieval model, and combined with retrieved data to produce a response via an LLM (image by author).

### Contextual Retrieval RAG

The process of matching the user’s query with the small chunks in the vector database usually works well; however, it has the following issues:

- The answer to a question may require multiple chunks which could be far from each other. Due to the loss of context, finding all the related chunks is not possible. For instance, consider a question for a legal document: " What are the conditions of partnership termination between Alpha A and Beta B companies?" One of the chunks in the document may read, " _The agreement may be terminated under specific conditions_". However, due to the absence of any contextual information (no company names), this chunk cannot be selected during the retrieval process.
- For some questions, the old-school _best match_ search can work better than semantic search, especially for exact matches. For instance, in an e-commerce document, the answer to a query " _What is Product ID ZX-450?_" by a semantic search method may bring information about several products, while missing the exact " _ZX-450_" product.
- The information retrieved from the vector database is relayed to the LLM which generates the final answer based on the query. During this process, the LLM has to decide the most suitable chunks to generate the final answer. Too many retrieved chunks could result in irrelevant information in the response. Therefore, the LLM must have a ranking mechanism.

In response to these issues, Anthropic recently introduced a [method](https://www.anthropic.com/news/contextual-retrieval) to add context to each chunk which showed significant performance improvement over naive RAG. After splitting a document into chunks, this method first assigns a brief context to each chunk by sending the chunk to the LLM along with the entire document as a context. Subsequently, the chunks appended by the context are saved to the vector database. They further combined the contextual chunking with _best match_ using the _[bm25 retriever](https://pub.aimind.so/understanding-the-bm25-ranking-algorithm-19f6d45c6ce)_ that searches documents using the BM25 method, and a re-ranker model that assigns raking scores to each retrieved chunk based on its relevance.

### Multimodal RAG with Contextual Retrieval

Despite significant performance improvements, Anthropic demonstrated the applicability of these methods only to text. A rich source of information in many documents is images (graphs, figures) and complex tables. If we parse only text from documents, we will not be able to get insights into other modalities in the documents. The documents containing images and complex tables require efficient parsing methods which entails not only properly extracting them from the documents, but also understanding them.

Assigning context to each chunk in the document using Anthropic’s latest model ( _claude-3–5-sonnet-20240620_) could involve high cost in the case of large documents, as it involves sending the whole document with each chunk. Although Claude’s [prompt caching](https://www.anthropic.com/news/prompt-caching) technique can significantly reduce this cost by caching frequently used context between API calls, the cost is still much higher than OpenAI’s cost-efficient models such as _gpt-4o-mini_.

This article discusses an extension of the Anthropic’s methods as follows:

- Using _LlamaParse_ to extract all content, from text to tables to images, into well-structured markdown.
- Instead of using text splitters to split the documents into chunks, node parsers are used to parse documents into _nodes_. This involves not just splitting text but also understanding the document’s structure, semantics, and metadata.
- OpenAI’s extremely cost-efficient LLM _gpt-4o-mini_ and embedding model _text-embedding-3-small_ are used for assigning context to each node, generating the final response, and computing the node’s embeddings.

After the Anthropic [blog post](https://www.anthropic.com/news/contextual-retrieval) on contextual retrieval, I found a partial implementation with OpenAI at this GitHub [link](https://github.com/lesteroliver911/contextual-doc-retrieval-opneai-reranker?tab=readme-ov-file). However, it uses traditional chunking and _LlamaParse_ without the recently introduced [premium mode](https://www.llamaindex.ai/blog/introducing-llamaparse-premium). I found Llamaparse’s premium mode to be significantly efficient in extracting different structures in the document.

Anthropic’s contextual retrieval [implementation](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/multimodal_contextual_retrieval_rag.ipynb) can also be found on [GitHub](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/cookbooks/contextual_retrieval.ipynb) which uses _LlamaIndex_ abstraction; however, it does not implement multimodal parsing. At the time of writing this article, a more recent implementation came from _LlamaIndex_ that uses multimodal parsing with contextual retrieval. This implementation uses Anthropic’s LLM ( _claude-3–5-sonnet-2024062_) and [Voyage’s embedding model](https://docs.voyageai.com/docs/embeddings) ( _voyage-3_). However, they do not explore _best search 25_ and _re-ranking_ as mentioned in Anthropic’s blog post.

The contextual retrieval implementation discussed in this article is a low-cost, multimodal RAG solution with improved retrieval performance with BM [2](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/cookbooks/contextual_retrieval.ipynb) 5 search and re-ranking. The performance of this contextual retrieval-based, multimodal RAG (CMRAG) is also compared with a basic RAG and _LlamaIndex’s_ implementation of contextual retrieval. Some functions were re-used with required modifications from these links: [1](https://colab.research.google.com/drive/1PcuVqUQjacMt18p8LwODnjbsXOFMurwa?usp=sharing#scrollTo=s-bxSMSa-qJe), 2, [3](https://github.com/run-llama/llama_parse/blob/main/examples/multimodal/multimodal_contextual_retrieval_rag.ipynb), [4](https://github.com/lesteroliver911/contextual-doc-retrieval-opneai-reranker?tab=readme-ov-file).

_**The code of this implementation is available on [GitHub](https://github.com/umairalipathan1980/Multimodal-contextual-RAG.git).**_

The overall approach used in this article to implement the CMRAG is depicted as follows:

https://towardsdatascience.com/wp-content/uploads/2024/10/1tiGVPpDQSTcLIeXNzWMLOw.pngThe parsed nodes are assigned context before saving to the vector database. The contextual retrieval involves combining embeddings (semantic search) and TF-IDF vectors (best match search), followed by re-ranking by a re-ranker model and final response generation by the LLM. (image by author)

Let’s delve into the step-by-step implementation of CMRAG.

### Multimodal Parsing

The following libraries need to be installed for running the code discussed in this article.

```python
!pip install llama-index ipython cohere rank-bm25 pydantic nest-asyncio python-dotenv openai llama-parse
```

All libraries to be imported to run the whole code are mentioned in the [GitHub notebook](https://github.com/umairalipathan1980/Multimodal-contextual-RAG.git). For this article, I used [Key Figures on Immigration](https://emn.fi/wp-content/uploads/EMN_maahanmuuton-tunnusluvut_2023-EN-1.pdf) in Finland ( [licensed under CC By 4.0, re-use allowed](https://commission.europa.eu/legal-notice_en)) which contains several graphs, images, and text data.

_LlamaParse_ offers [multimodal parsing](https://docs.cloud.llamaindex.ai/llamaparse/features/multimodal) using a vendor multimodal model (such as _gpt-4o_) to handle document extraction.

```python
parser = LlamaParse(
  use_vendor_multimodal_model=True
  vendor_multimodal_model_name="openai-gpt-4o"
  vendor_multimodal_api_key=sk-proj-xxxxxx
)
```

In this mode, a screenshot of every page of a document is taken, which is then sent to the multimodal model with instructions to extract as markdown. The markdown result of each page is consolidated into the final output.

The recent _[LlamaParse Premium mode](https://www.llamaindex.ai/blog/introducing-llamaparse-premium)_ offers advanced multimodal document parsing, extracting text, tables, and images into well-structured markdown while significantly reducing missing content and hallucinations. It can be used by creating a free account at _[Llama Cloud](https://cloud.llamaindex.ai/)_ Platform and obtaining an API key. The free plan offers to parse 1,000 pages per day.

LlamaParse premium mode is used as follows:

```python
from llama_parse import LlamaParse
import os

# Function to read all files from a specified directory
def read_docs(data_dir) -> List[str]:
    files = []
    for f in os.listdir(data_dir):
        fname = os.path.join(data_dir, f)
        if os.path.isfile(fname):
            files.append(fname)
    return files

parser = LlamaParse(
    result_type="markdown",
    premium_mode=True,
    api_key=os.getenv("LLAMA_CLOUD_API_KEY")
)

files = read_docs(data_dir = DATA_DIR)
```

We start with reading a document from a specified directory, parse the document using the parser’s \_get\_json _result_() method, and get image dictionaries using the parser’s \_get _images_() method. Subsequently, the nodes are extracted and sent to the LLM to assign context based on the overall document using the \_retrieve _nodes_() method. Parsing of this document (60 pages), including getting image dictionaries, took 5 minutes and 34 seconds(a one-time process).

```python
print("Parsing...")
json_results = parser.get_json_result(files)
print("Getting image dictionaries...")
images = parser.get_images(json_results, download_path=image_dir)
print("Retrieving nodes...")
```

https://towardsdatascience.com/wp-content/uploads/2024/10/1vm_ooPxvA7nHiP3lVK_RFQ.pngThe fourth page of the report (Source: [Key Figures on Immigration](https://emn.fi/wp-content/uploads/EMN_maahanmuuton-tunnusluvut_2023-EN-1.pdf))

```python
json_results[0]["pages"][3]
```

https://towardsdatascience.com/wp-content/uploads/2024/10/1AIaP_qrABODoj2GT9WE08A.pngThe fourth page in the report represented by the first node of the JSON results (image by author)

### Contextual Retrieval

Individual nodes and the associated images (screenshots) are extracted by \_retrieve _nodes_() function from the parsed \_josn _results._ Each node is sent to **assign _context_() function along with all the nodes ( _doc_ variable in the below code). The** assign _context_() function uses a prompt template \_CONTEXT\_PROMPT _TMPL_ (adopted and modified from this [source](https://github.com/lesteroliver911/contextual-doc-retrieval-opneai-reranker?tab=readme-ov-file)) to add a concise context to each node. This way, we integrate metadata, markdown text, context, and raw text into the node.

The following code shows the implementation of \_retrieve _nodes_() function. The two helper functions, \_\_get\_sorted\_image _files_() and \_get\_img\_page _number_(), get sorted image files by page and the page number of images, respectively. The overall aim is not to rely solely on the raw text as the simple RAGs do to generate the final answer, but to consider metadata, markdown text, context, and raw text, as well as the whole images (screenshots) of the retrieved nodes (image links in the node’s metadata) to generate the final response.

```python
# Function to get page number of images using regex on file names
def get_img_page_number(file_name):
    match = re.search(r"-page-(d+).jpg$", str(file_name))
    if match:
        return int(match.group(1))
    return 0

# Function to get image files sorted by page
def _get_sorted_image_files(image_dir):
    raw_files = [f for f in list(Path(image_dir).iterdir()) if f.is_file()]
    sorted_files = sorted(raw_files, key=get_img_page_number)
    return sorted_files

# Context prompt template for contextual chunking
CONTEXT_PROMPT_TMPL = """
You are an AI assistant specializing in document analysis. Your task is to provide brief, relevant context for a chunk of text from the given document.
Here is the document:
<document>
{document}
</document>

Here is the chunk we want to situate within the whole document:
<chunk>
{chunk}
</chunk>

Provide a concise context (2-3 sentences) for this chunk, considering the following guidelines:
1. Identify the main topic or concept discussed in the chunk.
2. Mention any relevant information or comparisons from the broader document context.
3. If applicable, note how this information relates to the overall theme or purpose of the document.
4. Include any key figures, dates, or percentages that provide important context.
5. Do not use phrases like "This chunk discusses" or "This section provides". Instead, directly state the context.

Please give a short succinct context to situate this chunk within the overall document to improve search retrieval of the chunk.
Answer only with the succinct context and nothing else.

Context:
"""

CONTEXT_PROMPT = PromptTemplate(CONTEXT_PROMPT_TMPL)

# Function to generate context for each chunk
def _assign_context(document: str, chunk: str, llm) -> str:
    prompt = CONTEXT_PROMPT.format(document=document, chunk=chunk)
    response = llm.complete(prompt)
    context = response.text.strip()
    return context

# Function to create text nodes with context
def retrieve_nodes(json_results, image_dir, llm) -> List[TextNode]:
    nodes = []
    for result in json_results:
        json_dicts = result["pages"]
        document_name = result["file_path"].split('/')[-1]
        docs = [doc["md"] for doc in json_dicts]  # Extract text
        image_files = _get_sorted_image_files(image_dir)  # Extract images
        # Join all docs to create the full document text
        document_text = "nn".join(docs)
        for idx, doc in enumerate(docs):
            # Generate context for each chunk (page)
            context = _assign_context(document_text, doc, llm)
            # Combine context with the original chunk
            contextualized_content = f"{context}nn{doc}"
            # Create the text node with the contextualized content
            chunk_metadata = {"page_num": idx + 1}
            chunk_metadata["image_path"] = str(image_files[idx])
            chunk_metadata["parsed_text_markdown"] = docs[idx]

            node = TextNode(
                text=contextualized_content,
                metadata=chunk_metadata,
            )
            nodes.append(node)
    return nodes
# Get text nodes
text_node_with_context = retrieve_nodes(json_results, image_dir, llm)First page of the report (image by author)First page of the report (image by author)
```

Here is the depiction of a node corresponding to the first page of the report.

https://towardsdatascience.com/wp-content/uploads/2024/10/1NH3HT0ka1MHPeAbB6BYLXw.pngNode with context and metadata added (image by author)

### Enhancing Contextual Retrieval with BM25 and Re-ranking

All the nodes with metadata, raw text, markdown text, and context information are then indexed into a vector database. BM25 indices for the nodes are created and saved in a pickle file for query inference. The processed nodes are also saved for later use (\_text\_node\_with _context.pkl_).

```python
    # Create the vector store index
    index = VectorStoreIndex(text_node_with_context, embed_model=embed_model)
    index.storage_context.persist(persist_dir=output_dir)
    # Build BM25 index
    documents = [node.text for node in text_node_with_context]
    tokenized_documents = [doc.split() for doc in documents]
    bm25 = BM25Okapi(tokenized_documents)
    # Save bm25 and text_node_with_context
    with open(os.path.join(output_dir, 'tokenized_documents.pkl'), 'wb') as f:
        pickle.dump(tokenized_documents, f)
    with open(os.path.join(output_dir, 'text_node_with_context.pkl'), 'wb') as f:
        pickle.dump(text_node_with_context, f)
```

We can now initialize a query engine to ask queries using the following pipeline. But before that, the following prompt is set to guide the behavior of the LLM to generate the final response. A multimodal LLM ( _gpt-4o-mini_) is initialized to generate the final response. This prompt can be adjusted as needed.

```python
# Define the QA prompt template
RAG_PROMPT = """
Below we give parsed text from documents in two different formats, as well as the image.

---------------------
{context_str}
---------------------
Given the context information and not prior knowledge, answer the query. Generate the answer by analyzing parsed markdown, raw text and the related
image. Especially, carefully analyze the images to look for the required information.
Format the answer in proper format as deems suitable (bulleted lists, sections/sub-sections, tables, etc.)
Give the page's number and the document name where you find the response based on the Context.

Query: {query_str}
Answer: """

PROMPT = PromptTemplate(RAG_PROMPT)

# Initialize the multimodal LLM
MM_LLM = OpenAIMultiModal(model="gpt-4o-mini", temperature=0.0, max_tokens=16000)
```

### Integrating the Whole Pipeline in a Query Engine

The following _QueryEngine_ class implements the above-mentioned workflow. The number of nodes in BM25 search (\_top\_n _bm25_) and the number of re-ranked results (\_top _n_) by the re-ranker can be adjusted as required. The BM25 search and re-ranking can be selected or de-selected by toggling the \_best\_match _25_ and \_re _ranking_ variables in the GitHub code.

Here is the overall workflow implemented by _QueryEngine_ class.

1. Find query embeddings
2. Retrieve nodes from the vector database using vector-based retrieval
3. Retrieve nodes with BM25 search ( _if selected_)
4. Combine nodes from both BM25 and vector-based retrieval. Find the unique number of nodes (remove duplicated)
5. Apply re-ranking to re-rank the combined results ( _if selected)_. Here, we use Cohere’s _rerank-english-v2.0_ re-ranker model. You can create an account at [Cohere’s website](https://dashboard.cohere.com/api-keys) to get the trial API keys.
6. Create image nodes from the images associated with the nodes
7. Create context string from the parsed markdown text
8. Send the node images to the multimodal LLM for interpretation.
9. Generate the final response by sending the text nodes, image node descriptions, and metadata to the LLM.

```python
# DeFfine the QueryEngine integrating all methods
class QueryEngine(CustomQueryEngine):
    # Public fields
    qa_prompt: PromptTemplate
    multi_modal_llm: OpenAIMultiModal
    node_postprocessors: Optional[List[BaseNodePostprocessor]] = None

    # Private attributes using PrivateAttr
    _bm25: BM25Okapi = PrivateAttr()
    _llm: OpenAI = PrivateAttr()
    _text_node_with_context: List[TextNode] = PrivateAttr()
    _vector_index: VectorStoreIndex = PrivateAttr()

    def __init__(
        self,
        qa_prompt: PromptTemplate,
        bm25: BM25Okapi,
        multi_modal_llm: OpenAIMultiModal,
        vector_index: VectorStoreIndex,
        node_postprocessors: Optional[List[BaseNodePostprocessor]] = None,
        llm: OpenAI = None,
        text_node_with_context: List[TextNode] = None,
    ):
        super().__init__(
            qa_prompt=qa_prompt,
            retriever=None,
            multi_modal_llm=multi_modal_llm,
            node_postprocessors=node_postprocessors
        )
        self._bm25 = bm25
        self._llm = llm
        self._text_node_with_context = text_node_with_context
        self._vector_index = vector_index

    def custom_query(self, query_str: str):
        # Prepare the query bundle
        query_bundle = QueryBundle(query_str)

        bm25_nodes = []
        if best_match_25 == 1:  # if BM25 search is selected
            # Retrieve nodes using BM25
            query_tokens = query_str.split()
            bm25_scores = self._bm25.get_scores(query_tokens)
            top_n_bm25 = 5  # Adjust the number of top nodes to retrieve
            # Get indices of top BM25 scores
            top_indices_bm25 = bm25_scores.argsort()[-top_n_bm25:][::-1]
            bm25_nodes = [self._text_node_with_context[i] for i in top_indices_bm25]
            logging.info(f"BM25 nodes retrieved: {len(bm25_nodes)}")
        else:
            logging.info("BM25 not selected.")

        # Retrieve nodes using vector-based retrieval from the vector store
        vector_retriever = self._vector_index.as_query_engine().retriever
        vector_nodes_with_scores = vector_retriever.retrieve(query_bundle)
        # Specify the number of top vectors you want
        top_n_vectors = 5  # Adjust this value as needed
        # Get only the top 'n' nodes
        top_vector_nodes_with_scores = vector_nodes_with_scores[:top_n_vectors]
        vector_nodes = [node.node for node in top_vector_nodes_with_scores]
        logging.info(f"Vector nodes retrieved: {len(vector_nodes)}")

        # Combine nodes and remove duplicates
        all_nodes = vector_nodes + bm25_nodes
        unique_nodes_dict = {node.node_id: node for node in all_nodes}
        unique_nodes = list(unique_nodes_dict.values())
        logging.info(f"Unique nodes after deduplication: {len(unique_nodes)}")

        nodes = unique_nodes

        if re_ranking == 1:  # if re-ranking is selected
            # Apply Cohere Re-ranking to rerank the combined results
            documents = [node.get_content() for node in nodes]
            max_retries = 3
            for attempt in range(max_retries):
                try:
                    reranked = cohere_client.rerank(
                        model="rerank-english-v2.0",
                        query=query_str,
                        documents=documents,
                        top_n=3  # top-3 re-ranked nodes
                    )
                    break
                except CohereError as e:
                    if attempt < max_retries - 1:
                        logging.warning(f"Error occurred: {str(e)}. Waiting for 60 seconds before retry {attempt + 1}/{max_retries}")
                        time.sleep(60)  # Wait before retrying
                    else:
                        logging.error("Error occurred. Max retries reached. Proceeding without re-ranking.")
                        reranked = None
                        break

            if reranked:
                reranked_indices = [result.index for result in reranked.results]
                nodes = [nodes[i] for i in reranked_indices]
            else:
                nodes = nodes[:3]  # Fallback to top 3 nodes
            logging.info(f"Nodes after re-ranking: {len(nodes)}")
        else:
            logging.info("Re-ranking not selected.")

        # Limit and filter node content for context string
        max_context_length = 16000  # Adjust as required
        current_length = 0
        filtered_nodes = []

        # Initialize tokenizer
        from transformers import GPT2TokenizerFast
        tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

        for node in nodes:
            content = node.get_content(metadata_mode=MetadataMode.LLM).strip()
            node_length = len(tokenizer.encode(content))
            logging.info(f"Node ID: {node.node_id}, Content Length (tokens): {node_length}")
            if not content:
                logging.warning(f"Node ID: {node.node_id} has empty content. Skipping.")
                continue
            if current_length + node_length <= max_context_length:
                filtered_nodes.append(node)
                current_length += node_length
            else:
                logging.info(f"Reached max context length with Node ID: {node.node_id}")
                break
        logging.info(f"Filtered nodes for context: {len(filtered_nodes)}")

        # Create context string
        ctx_str = "nn".join(
            [n.get_content(metadata_mode=MetadataMode.LLM).strip() for n in filtered_nodes]
        )

        # Create image nodes from the images associated with the nodes
        image_nodes = []
        for n in filtered_nodes:
            if "image_path" in n.metadata:
                image_nodes.append(
                    NodeWithScore(node=ImageNode(image_path=n.metadata["image_path"]))
                )
            else:
                logging.warning(f"Node ID: {n.node_id} lacks 'image_path' metadata.")
        logging.info(f"Image nodes created: {len(image_nodes)}")

        # Prepare prompt for the LLM
        fmt_prompt = self.qa_prompt.format(context_str=ctx_str, query_str=query_str)

        # Use the multimodal LLM to interpret images and generate a response
        llm_response = self.multi_modal_llm.complete(
            prompt=fmt_prompt,
            image_documents=[image_node.node for image_node in image_nodes],
            max_tokens=16000
        )

        logging.info(f"LLM response generated.")

        # Return the final response
        return Response(
            response=str(llm_response),
            source_nodes=filtered_nodes,
            metadata={
                "text_node_with_context": self._text_node_with_context,
                "image_nodes": image_nodes,
            },
        )

# Initialize the query engine with BM25, Cohere Re-ranking, and Query Expansion
query_engine = QueryEngine(
    qa_prompt=PROMPT,
    bm25=bm25,
    multi_modal_llm=MM_LLM,
    vector_index=index,
    node_postprocessors=[],
    llm=llm,
    text_node_with_context=text_node_with_context
)
print("All done")
```

An advantage of using OpenAI models, especially _gpt-4o-mini_, is much lower cost for context assignment and query inference running, as well as much smaller context assignment time. While the basic tiers of both OpenAI and Anthropic do quickly hit the maximum rate limit of API calls, retry time in Anthropic’s basic tier vary and could be too long. Context assignment process for only first 20 pages of this document with _claude-3–5-sonnet-20240620_ took approximately 170 seconds with prompt caching and costed 20 cents (input + output tokens). Whereas, _gpt-4o-mini_ is roughly 20x cheaper compared to Claude 3.5 Sonnet for input tokens and roughly 25x cheaper for output tokens. [OpenAI claims to implement prompt caching](https://platform.openai.com/docs/guides/prompt-caching#:~:text=Caching%20is%20available%20for%20prompts,depending%20on%20the%20prompt's%20length.) for repetitive content which works automatically for all API calls.

In comparison, the context assignment to nodes in this entire document (60 pages) through _gpt-4o-mini_ completed in approximately 193 seconds without any retry request.

After implementing the _QueryEngine_ class, we can run the query inference as follows:

```python
original_query = """What are the top countries to whose citizens the Finnish Immigration Service issued the highest number of first residence permits in 2023?
Which of these countries received the highest number of first residence permits?"""
response = query_engine.query(original_query)
display(Markdown(str(response)))
```

Here is the markdown response to this query.

https://towardsdatascience.com/wp-content/uploads/2024/10/1c8qUFmuZzeA8jBzYiGAC0A.pngResponse to the query (image by author)

The pages cited in the query response are the following.

https://towardsdatascience.com/wp-content/uploads/2024/10/1FwLev94tm8zlrxWxy5juMQ.pngOne of the cited pages (page 9) in the above query. The extracted information is shown in red rectangle (Source: [Key Figures on Immigration](https://emn.fi/wp-content/uploads/EMN_maahanmuuton-tunnusluvut_2023-EN-1.pdf))

Now let’s compare the performance of gpt-4o-mini based RAG (LlamaParse premium + context retrieval + BM25 + re-ranking) with Claude based RAG (LlamaParse premium + context retrieval). I also implemented a simple, baseline RAG which can be found in GitHub’s notebook. Here are the three RAGs to be compared.

1. Simple RAG in LlamaIndex using _SentenceSplitter_ to split the documents into chunks (\_chunk _size_ = 800, \_chunk _overlap_ = 400), creating a vector index and vector retrieval.
2. CMRAG ( _claude-3–5-sonnet-20240620_, _voyage-3_) – LlamaParse premium mode + context retrieval
3. CMRAG ( _gpt-4o-mini, text-embedding-3-small_) – LlamaParse premium mode + context retrieval + BM25 + re-ranking

For the sake of simplicity, we refer to these RAGs as RAG0, RAG1, and RAG2, respectively. Here are three pages from the report from where I asked three questions (1 question from each page) to each RAG. The areas highlighted by the red rectangles show the ground truth or the place from where the right answer should come from.

https://towardsdatascience.com/wp-content/uploads/2024/10/1WdCubp4q9Uio9EP0ciPwoQ.pngPage 4 of the document (Source: [Key Figures on Immigration](https://emn.fi/wp-content/uploads/EMN_maahanmuuton-tunnusluvut_2023-EN-1.pdf))https://towardsdatascience.com/wp-content/uploads/2024/10/1QXkUtM0U5bxi5kLFjTsvaQ.pngPage 12 of the document (Source: [Key Figures on Immigration](https://emn.fi/wp-content/uploads/EMN_maahanmuuton-tunnusluvut_2023-EN-1.pdf))https://towardsdatascience.com/wp-content/uploads/2024/10/1oa3TyMqWnP7q1szdoeQOsQ.pngPage 20 of the document (Source: [Key Figures on Immigration](https://emn.fi/wp-content/uploads/EMN_maahanmuuton-tunnusluvut_2023-EN-1.pdf))

Here are the responses to the three RAGs to each question.

https://towardsdatascience.com/wp-content/uploads/2024/10/1xeRxJsd5M2HmnerKd9kANA.pngComparison of basic RAG, Claude-based CMRAG, and gpt-4o-mini based CMRAG (image by author)

It can be seen that RAG2 performs very well. For the first question, RAG0 provides a wrong answer because the question was asked from an image. Both RAG1 and RAG2 provided the right answer to this question. For the other two questions, RAG0 could not provide any answer. Whereas, both RAG1 and RAG2, provided right answers to these questions.

Overall, RAG2’s performance was equal or even better than RAG1 in many cases due to the integration of BM25, re-ranking, and better prompting. It provides a cost-effective solution to a contextual, multimodal RAG. A possible integration in this pipeline could be hypothetical document embedding ( _hyde_) or query extension. Similarly, open-source embedding models (such as _all-MiniLM-L6-v2_) and/or light-weight LLMs (such as _gemma2_ or _phi-3-small_) could also be explored to make it more cost effective.

### GitHub

For the full code reference, please take a look at my repo:

> [**GitHub – umairalipathan1980/Multimodal-contextual-RAG: Multimodal contextual RAG**](https://github.com/umairalipathan1980/Multimodal-contextual-RAG.git)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="multimodal-ai-agents-images-pdfs-audio.md">
<details>
<summary>Stop Converting Documents to Text. You're Doing It Wrong.</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.decodingai.com/p/stop-converting-documents-to-text>

# Stop Converting Documents to Text. You're Doing It Wrong.

### How to work with multimodal agents: images, PDFs, audio, and... text.

Paul Iusztin

Dec 09, 2025

_**Welcome to the AI Agents Foundations series**: A 9-part journey from Python developer to AI Engineer. Made by busy people. For busy people._

Everyone’s talking about AI agents. But what actually is an agent? When do we need them? How do they plan and use tools? How do we pick the correct AI tools and agentic architecture? …and most importantly, where do we even start?

To answer all these questions (and more!), We’ve started a 9-article straight-to-the-point series to build the skills and mental models to ship real AI agents in production.

We will write everything from scratch, jumping directly into the building blocks that will teach you _“how to fish”_.

**What’s ahead**:

1. [Workflows vs. Agents](https://www.decodingai.com/p/ai-workflows-vs-agents-the-autonomy)

2. [Context Engineering](https://www.decodingai.com/p/context-engineering-2025s-1-skill)

3. [Structured Outputs](https://www.decodingai.com/p/llm-structured-outputs-the-only-way)

4. [The 5 Workflow Patterns](https://www.decodingai.com/p/stop-building-ai-agents-use-these)

5. [Tool Calling From Scratch](https://www.decodingai.com/p/tool-calling-from-scratch-to-production)

6. [Planning: ReAct & Plan-and-Execute](https://www.decodingai.com/p/ai-agents-planning)

7. [ReAct Agents From Scratch](https://www.decodingai.com/p/building-production-react-agents)

8. [AI Agent’s Memory](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work)

9. **Multimodal Agents** _← You are here_


By the end, you’ll have a deep understanding of how to design agents that think, plan, and execute—and most importantly, how to integrate them in your AI apps without being overly reliant on any AI framework.

**Let’s get started.**

* * *

## Multimodal Agents

When I first started building AI agents, I hit a frustrating wall. I was comfortable manipulating text, but the moment I had to integrate multimodal data, such as images, audio, and especially documents like PDFs, my elegant architectures turned into messy hacks. I spent weeks building complex pipelines that tried to force everything into text. I chained OCR engines to scrape PDFs, layout detection models to identify tables, and separate classifiers to handle images. It was a brittle, slow, and expensive solution that broke every time a document layout changed.

The breakthrough came when I realized I was solving the wrong problem. I didn’t need to convert documents to text. I needed to treat them as images. Once I understood that every PDF page is effectively an image and that modern LLMs can “see” just as well as they can read, the complexity vanished. I could completely skip the OCR purgatory and focus on the three core inputs of an LLM: text, images, and audio.

This shift is essential because real-world AI applications rarely exist in a text-only vacuum. As human beings, we process information visually and audibly. Enterprise applications mirror this reality. They need to manipulate private data from warehouses and lakes that is inherently multimodal: financial reports with complex charts, technical diagrams, building sketches, and audio logs.

The old approach of normalizing everything to text it’s lossy. When you translate a complex diagram or a chart into text, you lose the spatial relationships, the colors, and the context. You lose the information that matters most. By processing data in its native format, we preserve this rich visual information, resulting in systems that are faster, cheaper, and significantly more performant.

Ultimately, as data is made for humans, you want the LLM to process the data as close as a human would, which often is visually.

Here is what we will cover:

- **Foundations of Multimodal LLMs:** An intuition on how models process visual and textual tokens together.

- **Practical Implementation:** How to work with images and PDFs using the Gemini API.

- **Multimodal State Management:** How to structure agent memory for mixed modalities.

- **Building the Agent:** A step-by-step guide to building a multimodal ReAct agent.


## The Need for Multimodal AI

We want to process multimodal data to access our surroundings. However, the rise of multimodal LLMs is driven by a more subtle force: enterprise requirements. Enterprise applications work heavily with documents. The most critical example illustrating the need for multimodal data is processing PDF documents. Once we walk through this example, you will see how this core problem maps to other modalities like image, audio, or video.

Previously, we tried to normalize everything to text before passing it into an AI model. This approach has many flaws because we lose a substantial amount of information during translation. For example, when encountering diagrams, charts, or sketches in a document, it is impossible to fully reproduce them in text.

The traditional document processing workflow, often used for invoices, documentation, or reports, relies on the following four essential steps:

1. Document Preprocessing (e.g., Noise Removal)

2. Layout Detection (Text, Tables, Diagrams)

3. OCR Models (for Text) & Specialized Models (for Tables, Diagrams)

4. Output Structured Data (JSON/Metadata)


This workflow has too many moving pieces. We need layout detection models, OCR models for text, and specialized models for each expected data structure, such as tables or charts. This makes the system rigid. If a document contains a chart type we don’t have a model for, the pipeline fails. It is also slow and costly because we have to chain multiple model calls.

Most importantly, we face performance challenges. The multi-step nature creates a cascade effect where errors compound at each stage. Advanced OCR engines struggle with handwritten text, poor scans, stylized fonts, or complex layouts like nested tables and building sketches [[9]](https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it), [[11]](https://www.llamaindex.ai/blog/olmocr-bench-review-insights-and-pitfalls-on-an-ocr-benchmark).

https://substackcdn.com/image/fetch/$s_!nM40!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2dc40f3-dc13-486e-853d-8404368f4d8d_1616x1000.png Image 1: A building sketch showing a crawl space vent diagram, illustrating the complexity of layouts that classic OCR systems struggle to interpret. (Source [Vectorize.io [12]](https://vectorize.io/blog/multimodal-rag-patterns))

If we try to translate other data formats to text, we lose information. This is true for any modality:

- **Audio to Text:** We lose tone, pitch, and emotion.

- **Image to Text:** We lose spatial information, color, and context.

- **Video to Text:** We lose temporal dynamics and visual context.


Modern AI solutions use multimodal LLMs, such as Gemini, GPT-4o, Claude or other open-source models. These models can directly interpret text, images, or PDFs as native input. This completely bypasses the unstable OCR workflow.

Thus, let’s understand how multimodal LLMs work.

## Foundations of Multimodal LLMs

To use LLMs with images and documents, you need an intuition of how multimodality works. You do not need to understand every research detail. But knowing the architecture helps you deploy, optimize, and monitor them.

_**There are two common approaches to building multimodal LLMs**_ **:** the Unified Embedding Decoder Architecture and the Cross-modality Attention Architecture [[1]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms).

https://substackcdn.com/image/fetch/$s_!js-e!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76f50b57-2585-4cb8-8dda-eea5b5f81c03_1456x854.jpeg Image 2: The two main approaches to developing multimodal LLM architectures. (Source [Understanding Multimodal LLMs [1]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

### 1\. Unified Embedding Decoder Architecture

In this approach, we encode the text and image separately, concatenate their embeddings into a single vector, and pass the resulting vector to the LLM.

Thus, on top of a standard LLM architecture, you need a vision encoder that maps the image to an embedding that’s within the same vector space as the text. So, when the text and image embeddings are merged, the LLM can make sense of both.

https://substackcdn.com/image/fetch/$s_!p-gT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0979e82-2fb0-4f78-80c8-1395511e057f_1166x1400.jpeg Image 3: Illustration of the unified embedding decoder architecture. (Source [Understanding Multimodal LLMs [1]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

### 2\. Cross-modality Attention Architecture

In the second approach, instead of passing the image embeddings along with the text embeddings at the input, we inject them directly into the attention module. We still need an image encoder that projects the image into the same vector space as the text, but we inject it deeper within the architecture.

https://substackcdn.com/image/fetch/$s_!pf30!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea1b9ee4-0d19-4c3c-89db-06e779653da2_1296x1338.jpeg Image 4: An illustration of the Cross-Modality Attention Architecture approach. (Source [Understanding Multimodal LLMs [1]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

### Image Encoders

Both architectures rely on image encoders. To understand them, we can draw a parallel between text tokenization and image patching. Just as we split text into sub-word tokens, we split images into patches.

https://substackcdn.com/image/fetch/$s_!oFRB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a7104c0-3986-4aae-b918-06c393ff824c_1456x1154.jpeg Image 5: Image tokenization and embedding (left) and text tokenization and embedding (right) side by side. (Source [Understanding Multimodal LLMs [1]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

The output has the same structure and dimensions as text embeddings. However, they need to be aligned in the vector space. We do this through a linear projection module. Popular image encoder models include CLIP, OpenCLIP, and SigLIP [[3]](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/).

Importantly, these encoders are also used in Multimodal RAG. They allow us to find semantic similarities between images and text.

https://substackcdn.com/image/fetch/$s_!Z3FH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d4c837a-a3e5-4d60-97ce-c4d4faf4cf57_841x616.png Image 6: Toy representation of multimodal embedding space. (Source [Multimodal Embeddings: An Introduction [3]](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/))

You can replicate the same strategy between different modalities, such as text, image, document, and audio vectors, as long as you have an encoder that maps the data in the same vector space.

### Trade-offs and Modern Landscape

The **Unified Embedding Decoder** approach is simpler to implement (you just concatenate tokens) and generally yields higher accuracy in OCR-related tasks. The **Cross-modality Attention** approach is more computationally efficient for high-resolution images because we don’t have to pass all tokens as an input sequence. Instead, we inject them directly into the attention mechanism. Hybrid approaches exist to combine these benefits.

In 2025, most leading LLMs are multimodal. Open-source examples include Llama, Gemma, and Qwen. Closed-source examples include GPT, Gemini, and Claude.

A quick note on **Multimodal LLMs vs. Diffusion Models**: Diffusion models (like Midjourney) generate images from noise. Multimodal LLMs (like GPT) understand images and can sometimes generate them, but they are architecturally different. In an agent workflow, diffusion models are typically used as tools, not as the reasoning model.

> We had to keep this section super short. Still, if you want to learn more about the architecture of multimodal LLMs, we definitely recommend [this article](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms) by [Sebastian Raschka, PhD](https://open.substack.com/users/27393275-sebastian-raschka-phd?utm_source=mentions), from which we took most of the images in this section.

Now that we understand how LLMs can directly input images or documents, let’s see how this works in practice.

## Applying Multimodal LLMs to Images and Documents

To better understand how multimodal LLMs work, let’s write a few examples using Gemini to show you some best practices when working with images and documents, such as PDFs.

There are three core ways to process multimodal data with LLMs:

1. **Raw bytes:** The easiest way to work with LLMs. However, when storing the item in a database, it can easily get corrupted as most databases interpret the input as text/strings instead of bytes.

2. **Base64:** A way to encode raw bytes as strings. This is useful for storing images or documents directly in a database (e.g., PostgreSQL, MongoDB) without corruption. The downside is that the file size increases by approximately 33%.

3. **URLs:** The standard for enterprise scenarios. You store data in a data lake like AWS S3 or GCP Buckets. The LLM downloads the media directly from the bucket. As the file never sees your server, this reduces network latency for your application. This is the most efficient option for scale.


Now, let’s dig into the code. We will show you a couple of simple examples of how to manipulate images and PDFs with these 3 methods using the Google GenAI SDK. In the following sections, we will build a simple agent that combines everything into a single unified layer.

1. First, we set up our client and display a sample image.


```
from google import genai
from google.genai import types
from PIL import Image
import io

client = genai.Client()
MODEL_ID = “gemini-2.5-flash”
```

2. We load the image as **raw bytes**. We use `WEBP` format because it is efficient. For example, we can call the LLM to generate a caption for an image or compare two images.


https://substackcdn.com/image/fetch/$s_!yQtv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5780cbd6-133b-44fe-9352-38250d6fc611_640x640.jpeg image\_1 sample

```
image_bytes_1 = load_image_as_bytes(”images/image_1.jpeg”, format="WEBP")
image_bytes_2 = load_image_as_bytes(”images/image_2.jpeg”, format=”WEBP”)

# Single image captioning
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[\
        types.Part.from_bytes(data=image_bytes_1, mime_type=”image/webp”),\
        “Tell me what is in this image in one paragraph.”,\
    ],
)
print(f"Caption: {response.text}")

# Comparing multiple images
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[\
        types.Part.from_bytes(data=image_bytes_1, mime_type=”image/webp”),\
        types.Part.from_bytes(data=image_bytes_2, mime_type=”image/webp”),\
        “What’s the difference between these two images?”,\
    ],
)
print(f"Difference: {response.text}")
```

It outputs:

```
Caption: An image of a gray kitten and a robot...

Difference: The primary difference between the two images is the nature of the interaction...
```

3. We can also process the image as a **Base64 encoded string**. Notice that the logic is similar, but we encode the bytes first.


```
import base64

image_base64 = base64.b64encode(image_bytes_1).decode(”utf-8”)

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[\
        types.Part.from_bytes(data=image_base64, mime_type=”image/webp”),\
        “Tell me what is in this image.”,\
    ],
)
```

If we compute the difference in size between base64 and bytes, the base64 one will be ~33% larger (but at least the data doesn’t get corrupted).

```
f”Size increase: {(len(image_base64) - len(image_bytes_1)) / len(image_bytes_1) * 100:.2f}%”
```

4. For **URLs**, Gemini works like a charm with GCS Buckets. We used this at ZTRON and it worked like a charm:


```
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[\
        types.Part.from_uri(uri=”gs://gemini-images/image_1.jpeg”, mime_type=”image/webp”),\
        “Tell me what is in this image.”,\
    ],
)
```

5. Let’s try a more complex task: **Object Detection**. We use Pydantic to define the output structure, using the knowledge from Lesson 3.


```
from pydantic import BaseModel

class BoundingBox(BaseModel):
    ymin: float
    xmin: float
    ymax: float
    xmax: float
    label: str

class Detections(BaseModel):
    bounding_boxes: list[BoundingBox]

prompt = “Detect all prominent items. Return 2d boxes normalized to 0-1000.”

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[types.Part.from_bytes(data=image_bytes_1, mime_type=”image/webp”), prompt],
    config=types.GenerateContentConfig(
        response_mime_type=”application/json”,
        response_schema=Detections
    ),
)
print(response.parsed)
```

It outputs:

```
bounding_boxes=[BoundingBox(ymin=272.0, xmin=28.0, ymax=801.0, xmax=535.0, label=’kitten’), ...]
```

https://substackcdn.com/image/fetch/$s_!RMhm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2eaed1f-bedb-4c33-98b3-96fa7424f0ad_566x590.png

6. Now, let’s process **PDFs**. Because we use a multimodal model, the process is identical to images. We load the PDF as bytes and pass it to the model.

https://substackcdn.com/image/fetch/$s_!GHjR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6c03a7fa-24aa-4542-b09f-19647a6a06c5_2550x3300.jpeg `attention_paper.pdf sample`


```
pdf_bytes = open(”pdfs/attention_paper.pdf”, “rb”).read()

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[\
        types.Part.from_bytes(data=pdf_bytes, mime_type=”application/pdf”),\
        “What is this document about? Provide a brief summary.”,\
    ],
)
print(response.text)
```

It outputs:

```
This document introduces the Transformer, a novel neural network architecture for sequence transduction...
```

7. We can also process **PDFs as public URLs**. This is useful for analyzing documents directly from the web without downloading them first. We use the `url_context` tool.


```
response = client.models.generate_content(
    model=MODEL_ID,
    contents=”Based on the provided paper as a PDF, tell me how ReAct works: https://arxiv.org/pdf/2210.03629”,
    config=types.GenerateContentConfig(tools=[{”url_context”: {}}]),
)
print(response.text)
```

It outputs:

```
The ReAct (Reasoning and Acting) paradigm is a method that combines verbal reasoning traces with task-specific actions...
```

8. Finally, we can perform **Object Detection on PDF pages**. This is powerful for extracting diagrams or tables. We treat the PDF page as an image.


```
page_image_bytes = load_image_as_bytes(”images/attention_page_1.jpeg”)

prompt = “Detect all the diagrams from the provided image as 2d bounding boxes.”

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[types.Part.from_bytes(data=page_image_bytes, mime_type=”image/webp”), prompt],
    config=types.GenerateContentConfig(
        response_mime_type=”application/json”,
        response_schema=Detections
    ),
)
```

https://substackcdn.com/image/fetch/$s_!hMx7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7cb5566-8dea-4468-b307-b79b7610c7fa_667x590.png

Processing PDFs as images is a concept popularized by the **[ColPali](https://arxiv.org/pdf/2407.01449v6)** [paper](https://arxiv.org/pdf/2407.01449v6) [[5]](https://arxiv.org/pdf/2407.01449v6), which demonstrated that modern Vision Language Models (VLMs) can retrieve documents more effectively by “looking” at them rather than extracting text.

## Foundations of Multimodal AI Agents

What if we want to use these methods within an Agent?

Agents manage their internal state, the short-term memory, as a list of messages. This usually translates to a list of dictionaries or JSON objects. When transitioning from text-only to multimodal, the structure changes slightly. We need a way to flag the data type and model the data using the formats we just discussed (URL, Base64, Binary).

We move from a list of text-only JSONs to a list of JSONs containing a mix of modalities. Each item can be text, an image, or audio. As long as the LLM can process these modalities, our job is to properly manage them in short-term memory, retrieve them from long-term memory, and pass them in the right encoding.

https://substackcdn.com/image/fetch/$s_!r-Rp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90c2c4cb-f95d-4744-bd04-268dc4a7c295_1200x1200.png Image 7: The transition of an AI agent’s short-term memory from a text-only to a multimodal representation.

Retrieval becomes more interesting in this context. We still query our long-term memory, but now we can use multimodal similarities. We can use an image from short-term memory to query for similar images, documents, or audio chunks.

From an architectural point of view, a multimodal agentic RAG looks like any other agentic RAG system. However, this is where you will feel the real need for **semantic search**. With text, you can get far with keyword filters or SQL. But with images or audio, you cannot rely on keywords. You must use vector similarity to find relationships between data types.

Let’s see how we can model this bag of mixed messages with an example.

## Building Multimodal AI Agents

Let’s take this further and design an agentic RAG system. We assume we have a vector database filled with images, audio data, PDFs (converted to images), and text. We also assume we have a multimodal embedding model that supports text-to-image, image-to-audio, and text-to-audio embeddings.

For simplicity, we will mock the retrieval tools that access our vector database and other MCP servers for Google Drive or local screenshots.

https://substackcdn.com/image/fetch/$s_!owfJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F246dbcab-68dc-41eb-983e-4f2bf5d48fa9_1200x1200.png Image 8: Agent Interacting With Multimodal Memory

Our main focus is on managing the short-term memory as a list of mixed-modality JSONs. We want the agent to retrieve context from its current multimodal state, leveraging its multimodal retrieval tools, provide an answer, and repeat until the task is complete.

1. First, we define our multimodal tools. In a real application, these would query a vector DB like Qdrant or Pinecone using a multimodal embedding model.


```
def text_image_search_tool(query: str):
    “”“Search for images using text description.”“”
    pass

def image_to_image_search_tool(image_data: str):
    “”“Find images visually similar to the input image.”“”
    pass

def image_audio_search_tool(image_data: str):
    “”“Find audio clips relevant to the image content.”“”
    pass

def image_document_search_tool(image_data: str):
    “”“Find documents visually similar to the image.”“”
    pass

def google_drive_document_search_tool(image_data: str):
    “”“Search Google Drive for documents related to the image.”“”
    pass

def computer_screen_shoot_tool():
    “”“Take a screenshot of the user’s screen.”“”
    return “<base64_image_string>”
```

2. We define the `build_react_agent` function that creates ReAct agents using LangGraph. We use a system prompt that explicitly instructs the agent to handle multimodal inputs.


```
from langgraph.prebuilt import create_react_agent
from langchain_google_genai import ChatGoogleGenerativeAI

def build_react_agent():
    system_prompt = “”“You are a multimodal AI assistant.
    You can see images, read documents, and listen to audio.
    When asked about visual content, use your tools to retrieve relevant context.
    Always analyze the visual features (colors, objects) or audio features (pitch, tone) in your search results.”“”

    model = ChatGoogleGenerativeAI(model=”gemini-2.5-pro”)
    tools = [\
        text_image_search_tool,\
        image_to_image_search_tool,\
        image_audio_search_tool,\
        image_document_search_tool,\
        google_drive_document_search_tool,\
        computer_screen_shoot_tool,\
    ]

    agent = create_react_agent(model, tools, system_prompt)

    return agent
```

3. We build the `react_agent` and run it with a query that requires multimodal reasoning: _“Based on what I am looking at, retrieve all relevant images, audio, and documents.”_


```
agent = build_react_agent()

response = agent.invoke({”messages”: [”Based on what I am looking at, retrieve all relevant images, audio and documents”]})
```

4. Let’s look at a potential reasoning trace on how the agent would call various tools to answer this question. Then we will show how the list of JSON messages grows with each step, using the Gemini API structure.

   - **Turn 1 (Reasoning):** The agent analyzes the user request and decides to call `computer_screen_shoot_tool`.

   - **Turn 1 (Observation):** The tool executes and returns a Base64 image. This is appended to the message history as a tool response containing `inline_data`.

```
{
  “role”: “tool”,
  “name”: “computer_screen_shoot_tool”,
  “parts”: [\
    {\
      “inline_data”: {\
        “mime_type”: “image/jpeg”,\
        “data”: “/9j/4AAQSkZJRg...”\
      }\
    }\
  ]
}
```

5. **Turn 2 (Reasoning):** The agent now has the image in its context. It analyzes the visual content (a gray kitten) and decides to call the following retrieval tools in parallel, passing the image data from the previous turn:


```
function_calls = [\
  {\
    “tool_name”: “image_to_image_search_tool”,\
    “tool_args”: {\
      “image_data”: “<base64_image_from_previous_turn>”\
    }\
  },\
  {\
    “tool_name”: “image_audio_search_tool”,\
    “tool_args”: {\
      “image_data”: “<base64_image_from_previous_turn>”\
    }\
  },\
  {\
    “tool_name”: “image_document_search_tool”,\
    “tool_args”: {\
      “image_data”: “<base64_image_from_previous_turn>”\
    }\
  },\
  {\
    “tool_name”: “google_drive_document_search_tool”,\
    “tool_args”: {\
      “image_data”: “<base64_image_from_previous_turn>”\
    }\
  }\
]
```

6. **Turn 2 (Observation):** The tools execute and return mixed modalities. The state is updated with these new observations, adding audio, images, and document pages to the context.


```
[\
  {\
    “role”: “tool”,\
    “name”: “image_to_image_search_tool”,\
    “parts”: [\
      { “text”: “Found 3 similar images:” },\
      {\
        “inline_data”: {\
          “mime_type”: “image/jpeg”,\
          “data”: “/9j/4AAQSkZJRg...”\
        }\
      },\
      {\
        “inline_data”: {\
          “mime_type”: “image/jpeg”,\
          “data”: “/9j/4AAQSkZJRg...”\
        }\
      },\
      {\
        “inline_data”: {\
          “mime_type”: “image/jpeg”,\
          “data”: “/9j/4AAQSkZJRg...”\
        }\
      }\
    ]\
  },\
  {\
    “role”: “tool”,\
    “name”: “image_audio_search_tool”,\
    “parts”: [\
      { “text”: “Found similar audio clip (as binary data):” },\
      {\
        “inline_data”: {\
          “mime_type”: “audio/mp3”,\
          “data”: “<binary_audio_bytes>”\
        }\
      }\
    ]\
  },\
  {\
    “role”: “tool”,\
    “name”: “image_document_search_tool”,\
    “parts”: [\
      { “text”: “Found relevant PDF page (as base64 image):” },\
      {\
        “inline_data”: {\
          “mime_type”: “image/png”,\
          “data”: “iVBORw0KGgo...”\
        }\
      }\
    ]\
  },\
  {\
    “role”: “tool”,\
    “name”: “google_drive_document_search_tool”,\
    “parts”: [\
      { “text”: “Found document from Google Drive (stored in GCS bucket):” },\
      {\
        “file_data”: {\
          “mime_type”: “application/pdf”,\
          “file_uri”: “gs://my-bucket/documents/british-shorthair-guide.pdf”\
        }\
      }\
    ]\
  }\
]
```

7. The agent compiles this into a final answer.


```
I analyzed your screen and found you are looking at a gray kitten.
Based on this, I retrieved:
1. 3 similar images of gray kittens (from image_to_image_search_tool, as base64).
2. An audio clip of a cat purring (from image_audio_search_tool, as binary data).
3. A PDF page about cat breeds (from image_document_search_tool, as base64 image).
4. A document from Google Drive about British Shorthair cats (from google_drive_document_search_tool, stored as URL in GCS bucket).
```

8. We can now ask a follow-up question: _“What is the color of my kitten?”_


```
response = agent.invoke({”messages”: [”What is the color of my kitten?”]})
```

9. Because the agent has the image in its short-term memory (the state), it does not need to use tools again. It simply looks at the Base64 data from Step 1 and answers.



At the time the agent is asked about this question, this is how its whole short-term memory looks. This is the first part up to the `computer_screen_shoot_tool`tool call`.`


```
[\
  {\
    “role”: “user”,\
    “parts”: [{ “text”: “Based on what I am looking at...” }]\
  },\
  {\
    “role”: “model”,\
    “parts”: [{ “function_call”: { “name”: “computer_screen_shoot_tool”, “args”: {} } }]\
  },\
  {\
    “role”: “tool”,\
    “name”: “computer_screen_shoot_tool”,\
    “parts”: [{ “inline_data”: { “mime_type”: “image/jpeg”, “data”: “...” } }]\
  }\
]
```

10. Here is the subsequent part of the state, showing the parallel tool calls and their multimodal outputs.


```
[\
  {\
    “role”: “model”,\
    “parts”: [\
      { “function_call”: { “name”: “image_to_image_search_tool”, “args”: { “image_data”: “<base64_image_from_previous_turn>” } } },\
      { “function_call”: { “name”: “image_audio_search_tool”, “args”: { “image_data”: “<base64_image_from_previous_turn>” } } },\
      { “function_call”: { “name”: “image_document_search_tool”, “args”: { “image_data”: “<base64_image_from_previous_turn>” } } },\
      { “function_call”: { “name”: “google_drive_document_search_tool”, “args”: { “image_data”: “<base64_image_from_previous_turn>” } } }\
    ]\
  },\
  {\
    “role”: “tool”,\
    “name”: “image_to_image_search_tool”,\
    “parts”: [\
      { “text”: “Found 3 similar images:” },\
      { “inline_data”: { “mime_type”: “image/jpeg”, “data”: “...” } },\
      { “inline_data”: { “mime_type”: “image/jpeg”, “data”: “...” } },\
      { “inline_data”: { “mime_type”: “image/jpeg”, “data”: “...” } }\
    ]\
  },\
  {\
    “role”: “tool”,\
    “name”: “image_audio_search_tool”,\
    “parts”: [\
      { “text”: “Found similar audio clip (as binary data):” },\
      { “inline_data”: { “mime_type”: “audio/mp3”, “data”: “<binary_audio_bytes>” } }\
    ]\
  },\
  {\
    “role”: “tool”,\
    “name”: “image_document_search_tool”,\
    “parts”: [\
      { “text”: “Found relevant PDF page (as base64 image):” },\
      { “inline_data”: { “mime_type”: “image/png”, “data”: “...” } }\
    ]\
  },\
  {\
    “role”: “tool”,\
    “name”: “google_drive_document_search_tool”,\
    “parts”: [\
      { “text”: “Found document from Google Drive (stored in GCS bucket):” },\
      { “file_data”: { “mime_type”: “application/pdf”, “file_uri”: “gs://my-bucket/documents/british-shorthair-guide.pdf” } }\
    ]\
  }\
]
```

11. Here is the end of the state, showing the document results and the final Q&A:


```
[\
  ,\
  {\
    “role”: “model”,\
    “parts”: [{ “text”: “I analyzed your screen...” }]\
  },\
  {\
    “role”: “user”,\
    “parts”: [{ “text”: “What is the color of my kitten?” }]\
  }\
]
```

12. And finally the model responds:


```
Your kitten is gray.
```

> We should probably use these LLMs for something more meaningful than just chatting about our pets. But hey, who doesn’t like a good cat/dog video? 😂

Nothing fundamental has changed in how we structure our data when switching from text-only to multimodal agents. We simply reflect the data types within the JSONs. The key is that our LLM knows how to process that data. The hard part is retrieving the correct multimodal data from our databases and indexing it properly.

## Conclusion

Working with multimodal data is a fundamental skill for AI engineers. Modern AI applications rarely exist in a text-only vacuum. They interact with the complex, visual, and auditory reality of the world.

In this lesson, we moved away from the unstable, multi-step OCR pipelines of the past. We learned that modern LLMs can natively process images and documents, preserving rich context that was previously lost. We explored how to handle data as bytes, Base64, and URLs, and how to build agents that can reason across these modalities.

This concludes our _AI Agents Foundations_ series. We started by understanding the difference between workflows and agents, mastered context engineering and structured outputs, built robust planning capabilities with ReAct, and finally gave our agents eyes and ears. You now have the foundational blocks to build production-ready AI systems.

Still, if you missed our roadmap, _remember that this article is part of a longer series of 9 pieces on the AI Agents Foundations that will give you the tools to morph from a Python developer to an AI Engineer._

**Here’s our roadmap:**

1. [Workflows vs. Agents](https://www.decodingai.com/p/ai-workflows-vs-agents-the-autonomy)

2. [Context Engineering](https://www.decodingai.com/p/context-engineering-2025s-1-skill)

3. [Structured Outputs](https://www.decodingai.com/p/llm-structured-outputs-the-only-way)

4. [The 5 Workflow Patterns](https://www.decodingai.com/p/stop-building-ai-agents-use-these)

5. [Tool Calling From Scratch](https://www.decodingai.com/p/tool-calling-from-scratch-to-production)

6. [Planning: ReAct & Plan-and-Execute](https://www.decodingai.com/p/ai-agents-planning)

7. [ReAct Agents From Scratch](https://www.decodingai.com/p/building-production-react-agents)

8. [AI Agent’s Memory](https://www.decodingai.com/p/how-does-memory-for-ai-agents-work)

9. _**Multimodal Agents** ← You just finished this one._


* * *

## References

01. Raschka, S. (2024, October 21). Understanding multimodal LLMS. Sebastian Raschka. [article](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms)

02. Vision language models. (n.d.). NVIDIA. [https://www.nvidia.com/en-us/glossary/vision-language-models/](https://www.nvidia.com/en-us/glossary/vision-language-models/)

03. Talebi, S. (2024, November 13). Multimodal embeddings: An introduction. Medium. [https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/)

04. Multi-modal ML with OpenAI’s CLIP. (n.d.). Pinecone. [https://www.pinecone.io/learn/series/image-search/clip/](https://www.pinecone.io/learn/series/image-search/clip/)

05. Fostiropoulos, I., et al. (2024). ColPali: Efficient Document Retrieval with Vision Language Models. arXiv. [https://arxiv.org/pdf/2407.01449v6](https://arxiv.org/pdf/2407.01449v6)

06. Image understanding. (n.d.). Google AI for Developers. [https://ai.google.dev/gemini-api/docs/image-understanding](https://ai.google.dev/gemini-api/docs/image-understanding)

07. Google generative AI embeddings. (n.d.). LangChain. [https://python.langchain.com/docs/integrations/text\_embedding/google\_generative\_ai/](https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/)

08. Agents. (n.d.). LangChain. [https://langchain-ai.github.io/langgraph/agents/agents/](https://langchain-ai.github.io/langgraph/agents/agents/)

09. Complex Document Recognition: OCR Doesn’t Work and Here’s How You Fix It. (n.d.). HackerNoon. [https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it](https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it)

10. What are some real-world applications of multimodal AI? (n.d.). Milvus. [https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai](https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai)

11. Liu, J. (2025, February 24). OlmOCR-bench review: Insights and pitfalls on an OCR benchmark. LlamaIndex. [https://www.llamaindex.ai/blog/olmocr-bench-review-insights-and-pitfalls-on-an-ocr-benchmark](https://www.llamaindex.ai/blog/olmocr-bench-review-insights-and-pitfalls-on-an-ocr-benchmark)

12. Vectorize.io. (2024, October 26). Multimodal RAG Patterns. Vectorize.io Blog. [https://vectorize.io/blog/multimodal-rag-patterns](https://vectorize.io/blog/multimodal-rag-patterns)


* * *

## Images

If not otherwise stated, all images are created by the author.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="ocr-accuracy-explained-how-to-improve-it.md">
<details>
<summary>OCR Accuracy Explained: How to Improve It</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.llamaindex.ai/blog/ocr-accuracy>

# OCR Accuracy Explained: How to Improve It

https://cdn.sanity.io/images/7m9jw85w/production/08b48679423850d08df1c40b761fd82bb99f9929-1200x676.png?w=1200

Summary: Accuracy Is a Pipeline Problem

- [How OCR Accuracy Is Actually Measured](https://www.llamaindex.ai/blog/ocr-accuracy#how-ocr-accuracy-is-actually-measured)
- [Character Error Rate (CER)](https://www.llamaindex.ai/blog/ocr-accuracy#character-error-rate-cer)
- [Word Error Rate (WER)](https://www.llamaindex.ai/blog/ocr-accuracy#word-error-rate-wer)
- [Field-Level (Semantic) Accuracy](https://www.llamaindex.ai/blog/ocr-accuracy#field-level-semantic-accuracy)
- [What Actually Affects OCR Accuracy](https://www.llamaindex.ai/blog/ocr-accuracy#what-actually-affects-ocr-accuracy)
- [Image Resolution](https://www.llamaindex.ai/blog/ocr-accuracy#image-resolution)
- [Document Types and Layout Complexity](https://www.llamaindex.ai/blog/ocr-accuracy#document-types-and-layout-complexity)
- [Handwriting Variability](https://www.llamaindex.ai/blog/ocr-accuracy#handwriting-variability)
- [Hardware and Infrastructure Constraints](https://www.llamaindex.ai/blog/ocr-accuracy#hardware-and-infrastructure-constraints)
- [Document Condition](https://www.llamaindex.ai/blog/ocr-accuracy#document-condition)
- [How to Improve OCR Results: A Practical Toolkit](https://www.llamaindex.ai/blog/ocr-accuracy#how-to-improve-ocr-results-a-practical-toolkit)
- [Phase 1: Pre-Processing](https://www.llamaindex.ai/blog/ocr-accuracy#phase-1-pre-processing)
- [Phase 2: Synthetic Data for Training](https://www.llamaindex.ai/blog/ocr-accuracy#phase-2-synthetic-data-for-training)
- [Phase 3: LLM Post-OCR Correction](https://www.llamaindex.ai/blog/ocr-accuracy#phase-3-llm-post-ocr-correction)
- [Validation: Comparing Output Against Ground Truth](https://www.llamaindex.ai/blog/ocr-accuracy#validation-comparing-output-against-ground-truth)
- [Building a Ground Truth Set](https://www.llamaindex.ai/blog/ocr-accuracy#building-a-ground-truth-set)
- [Automated Comparison and the Cost-of-Error Framework](https://www.llamaindex.ai/blog/ocr-accuracy#automated-comparison-and-the-cost-of-error-framework)
- [Choosing Your OCR Solution: 2026 Landscape](https://www.llamaindex.ai/blog/ocr-accuracy#choosing-your-ocr-solution-2026-landscape)
- [Open Source: Where It Works and Where It Doesn't](https://www.llamaindex.ai/blog/ocr-accuracy#open-source-where-it-works-and-where-it-doesnt)
- [Enterprise APIs: The Middle Ground](https://www.llamaindex.ai/blog/ocr-accuracy#enterprise-apis-the-middle-ground)
- [Agentic Document Processing: Why It's Different](https://www.llamaindex.ai/blog/ocr-accuracy#agentic-document-processing-why-its-different)
- [Summary: Accuracy Is a Pipeline Problem](https://www.llamaindex.ai/blog/ocr-accuracy#summary-accuracy-is-a-pipeline-problem)

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

The solution you choose sets the ceiling. Open source engines like Tesseract top out around 88–94% on anything complex. Enterprise APIs from Google, Azure, and AWS get you to 96–98% on standard formats. For complex, variable, or high-stakes documents, agentic document parsing is where the accuracy gap closes.

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