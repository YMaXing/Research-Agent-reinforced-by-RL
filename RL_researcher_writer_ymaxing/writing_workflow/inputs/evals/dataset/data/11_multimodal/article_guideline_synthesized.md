## Global Context of the Lesson

### What We Are Planning to Share

We will write a lesson on the fundamentals of working with multimodal data (text, images, and documents) in the context of LLMs, LLM workflows, and AI agents. We begin by highlighting the real-world prevalence of multimodal data in both human activities and enterprise systems, then contrast early normalization approaches (such as OCR converting everything to text) with the superior strategy of native multimodal processing that preserves rich visual and layout information. We provide just enough theory on multimodal LLMs, vision-language alignment, and multimodal embeddings for the reader to build intuition, followed by extensive hands-on examples of calling multimodal LLMs with mixed image/PDF/text inputs. We then cover foundations of multimodal RAG (including contrast with text-only RAG from prior lessons and concepts like vision-based retrieval), implement a working text-image-document RAG pipeline, and extend it into a multimodal AI agent. Throughout we emphasize that once you master text-image RAG, adding native document support is straightforward because documents are processed as images. We close by connecting this skill to the broader AI engineering journey and the course’s upcoming multi-agent project.

### Why We Think It's Valuable

Multimodal data handling is the final core competency needed to build enterprise-grade AI agents and LLM workflows that operate on real organizational data stored in databases, warehouses, and lakes. Traditional OCR-based normalization loses critical spatial, color, geometric, and layout signals present in financial reports, diagrams, research papers, and charts, leading to suboptimal accuracy, higher latency, and brittle systems. Native multimodal processing is faster, cheaper, more intuitive, and more performant because it mirrors how humans consume information. Mastering when to embed natively, when to retrieve visual chunks, and how to orchestrate them inside context windows directly determines whether your agents can deliver production value on complex private data instead of being limited to text.

### Expected Length of the Lesson
**5,200 words**

### Theory / Practice Ratio

30% theory - 70% real-world examples

## Anchoring the Lesson in the Course

### Details About the Course

This piece is part of a broader course on AI agents and LLM workflows. The course consists of 4 parts, each with multiple lessons. 

Thus, it's essential to always anchor this piece into the broader course, understanding where the reader is in its journey. You will be careful to consider the following:
- The points of view
- To not reintroduce concepts already taught in the previous lesson.
- To be careful when talking about concepts introduced only in future lessons
- To always reference previous and future lessons when discussing topics outside the piece's scope.

### Lesson Scope

This is lesson 11 (from part 1) of the course on working with multimodal data, such as text, images, and documents.

The article H1 title must follow the format `# Lesson 11: <Your Creative Subtitle Here>`.

### Point of View
The course is created by a team writing for a single reader, also known as the student. Thus, for voice consistency across the course, we will always use 'we,' 'our,' and 'us' to refer to the team who creates the course, and 'you' or 'your' to address the reader. Avoid singular first person and don't use 'we' to refer to the student.

Examples of correct point of view:
- Instead of "Before we can choose between workflows and agents, we need a clear understanding of what they are." word it as "To choose between workflows and agents, you need a clear understanding of what they are."

### Who Is the Intended Audience

Aspiring AI engineers who are learning about working with multimodal data for the first time.

### Concepts Introduced in Previous Lessons

In previous lessons of the course, we introduced the following concepts:

**Part 1:**

- **Lesson 1 - AI Engineering & Agent Landscape**: Understanding the role, the stack, and why agents matter now
- **Lesson 2 - Workflows vs. Agents**: Grasping the crucial difference between predefined logic and LLM-driven autonomy
- **Lesson 3 - Context Engineering**: The art of managing information flow to LLMs
- **Lesson 4 - Structured Outputs**: Ensuring reliable data extraction from LLM responses
- **Lesson 5 - Basic Workflow Ingredients**: Implementing chaining, routing, parallel and the orchestrator-worker patterns
- **Lesson 6 - Agent Tools & Function Calling**: Giving your LLM the ability to take action
- **Lesson 7 - Planning & Reasoning**: Understanding patterns like ReAct (Reason + Act)
- **Lesson 8 - Implementing ReAct**: Building a reasoning agent from scratch
- **Lesson 9 - Agent Memory & Knowledge**: Short-term vs. long-term memory (procedural, episodic, semantic)
- **Lesson 10 - RAG Deep Dive**: Advanced retrieval techniques for knowledge-augmented agents

As this is only the last lesson of the first part of the course, we introduced most of the required concepts for people to work with LLM workflows and AI agents, except the last piece of the puzzle: multimodal data.

### Concepts That Will Be Introduced in Future Lessons

In future lessons of the course, we will introduce the following concepts:

**Part 1:**

DONE - except the current lesson on multimodal data

**Part 2:**

In this section, you'll move from theory to practice by starting your work on the course's central project: an interconnected research and writing agent system. After a deep dive into agentic design patterns and a comparative look at modern frameworks, we'll focus on LangGraph. You will implement the research agent, equipping it with tools for web scraping and analysis. Then, you'll construct the writing workflow to convert research into polished content. Finally, you'll integrate these components, working on the orchestration of a complete, multi-agent pipeline from start to finish.

Other concepts from Part 2:
- MCP

**Part 3:**

With the agent system built, this section focuses on the engineering practices required for production. You will learn to design and implement robust evaluation frameworks to measure and guarantee agent reliability, moving far beyond simple demos. We will cover AI observability, using specialized tools to trace, debug, and understand complex agent behaviors. Finally, you’ll explore optimization techniques for cost and performance and learn the fundamentals of deploying your agent system, ensuring it is scalable and ready for real-world use.

**Part 4:**

In this final part of the course, you will build and submit your own advanced LLM agent, applying what you've learned throughout the previous sections. We provide a complete project template repository, enabling you to either extend our agent pipeline or build your own novel solution. Your project will be reviewed to ensure functionality, relevance, and adherence to course guidelines for the awarding of your course certification.

### Anchoring the Reader in the Educational Journey

Within the course we are teaching the reader multiple topics and concepts. Thus, understanding where the reader is in their educational journey is critical for this piece. You have to use only previously introduced concepts, while being reluctant about using concepts that haven't been introduced yet.

When discussing the **concepts introduced in previous lessons** listed in the `Concepts Introduced in Previous Lessons` section, avoid reintroducing them to the reader. Especially don't reintroduce the acronyms. Use them as if the reader already knows what they are. 

Avoid using all the **concepts that haven't been introduced in previous lessons** listed in the `Concepts That Will Be Introduced in Future Lessons` subsection. Whenever another concept requires references to these banned concepts, instead of directly using them, use intuitive analogies or explanations that are more general and easier to understand, as you would explain them to a 7-year-old. For example:
- If the "tools" concept wasn't introduced yet and you have to talk about agents, refer to them as "actions".
- If the "routing" concept wasn't introduced yet and you have to talk about it, refer to it as "guiding the workflow between multiple decisions".
You can use the concepts that haven't been introduced in previous lessons listed in the `Concepts That Will Be Introduced in Future Lessons` subsection only if we explicitly specify them. Still, even in that case, as the reader doesn't know how that concept works, you are only allowed to use the term, while keeping the explanation extremely high-level and intuitive, as if you were explaining it to a 7-year-old.
Whenever you use a concept from the `Concepts That Will Be Introduced in Future Lessons` subsection, explicitly specify in what lesson it will be explained in more detail, leveraging the particulars from the subsection. If not explicitly specified in the subsection, simply state that we will cover it in future lessons without providing a concrete lesson number. 

In all use cases avoid using acronyms that aren't explicitly stated in the guidelines. Rather use other more accessible synonyms or descriptions that are easier to understand by non-experts.

## Narrative Flow of the Lesson

Follow the next narrative flow when writing the end-to-end lesson:

- What problem are we learning to solve? Why is it essential to solve it?
    - Start with a personal story where we encountered the problem
- Why other solutions are not working and what's wrong with them.
- At a theoretical level, explain our solution or transformation. Highlight:
    - The theoretical foundations.
    - Why is it better than other solutions?
    - What tools or algorithms can we use?
- Provide some hands-on examples.
- Go deeper into the advanced theory.
- Provide a more complex example supporting the advanced theory.
- Connect our solution to the bigger field of AI Engineering. Add course next steps.

## Lesson Outline

1. Introduction: The need for multimodal AI
2. Limitations of traditional document processing
3. Foundations of multimodal LLMs
4. Applying multimodal LLMs to images and PDFs
5. Foundations of multimodal RAG
6. Implementing multimodal RAG for images, PDFs and text
7. Building multimodal AI agents
8. Conclusion

## Section 1 - Introduction: The need for multimodal AI
- Open with a relatable story from your own AI engineering practice where a text-only system failed on a real enterprise document (e.g., a financial report containing tables, charts, and annotated diagrams) that a human could interpret instantly but the system could not.
- Explain that as humans we constantly consume text, images, documents, and audio together; enterprise data in databases, data warehouses, and data lakes mirrors this reality with mixed modalities.
- Contrast the early days of AI applications (normalizing everything to text via OCR or extraction) with the modern requirement for native multimodal support inside the same context window and tool ecosystem.
- Tie this directly to business value: enterprise-grade AI agents and LLM workflows must manipulate an organization’s private multimodal data to deliver accurate, context-rich results rather than brittle approximations.
- Give a high-level preview of the lesson structure: limitations of traditional OCR pipelines, theoretical foundations of multimodal LLMs and embeddings (just enough for intuition), hands-on examples with images and PDFs, foundations and implementation of multimodal RAG, extension into multimodal agents, and connection to the rest of the course.
- Explicitly reference that this lesson builds on context engineering, RAG deep dive, agent memory, and planning patterns you already know without re-explaining them.
- End by noting that the same native techniques scale to video or audio (mentioned only at high level; those modalities are outside this lesson’s scope).
- Transition to Section 2: Before we can adopt native multimodal processing we must understand exactly where traditional document pipelines break.
-  **Section length:** 300 words

## Section 2: Limitations of traditional document processing
- Detail the traditional pipeline (OCR → text extraction → optional tabular parsing) and illustrate with concrete failure modes: loss of spatial layout, inability to interpret color-coded regions, geometric relationships in diagrams, handwritten annotations, or complex tables that span pages.
- Provide side-by-side contrasts: a financial PDF page with embedded charts versus its OCR-extracted text; show how critical meaning (trend direction conveyed by line slope and color, hierarchical table structure) disappears.
- Discuss information-loss edge cases: sketches, architectural diagrams, scientific figures with callouts, scanned forms with overlapping stamps—scenarios where converting to text is fundamentally lossy because language cannot economically encode visual geometry or color semantics.
- Quantify downsides in production terms: higher error rates on complex documents, increased latency from multi-stage pipelines, brittle maintenance when layouts change, and ultimately lower agent reliability when those extracted texts are fed into context engineering systems you learned about earlier.
- Present real-world enterprise examples (financial reports mixing narrative, tables, and graphs; research papers with captioned figures; internal wikis with screenshots) where OCR-based systems produced hallucinations or missed key insights that a human reader would catch immediately.
- Introduce the plot twist of the lesson: instead of forcing everything into text, modern systems process images and documents in their native format, feeding raw pixels or page images directly to multimodal models.
- Contrast this native approach with OCR along cost, speed, fidelity, and developer experience dimensions using a comparison table rendered in Markdown.
- Highlight that once you adopt native processing for images it becomes trivial to treat document pages the same way, setting up the multimodal RAG discussion later.
- Transition to Section 3: To use native images and documents effectively we first need a working mental model of how multimodal LLMs actually see and reason over visual input.
-  **Section length**: 650 words (don't count the mermaid diagrams or image links)

## Section 3: Foundations of multimodal LLMs
- Define multimodal LLMs (also called vision-language models) as systems that jointly process pixel data and token sequences inside a single unified architecture, contrasting them with the text-only models used in earlier lessons.
- Explain at an intuitive level how a vision encoder transforms raw images into embeddings that live in the same latent space as text tokens, allowing the LLM backbone to attend over both modalities seamlessly.
- Cover the theoretical foundation of contrastive pre-training (using CLIP-style objectives from the literature) that aligns visual concepts with language descriptions without requiring paired captions for every possible image.
- Describe the “image as a sequence of patches” or “image as tokens” mechanism and why this enables the same context-engineering techniques you already know (positioning, repetition of instructions, XML tagging) to apply to visual content.
- Discuss practical implications for context windows: each image consumes a variable number of tokens depending on resolution and patching strategy; provide guidance on trading off resolution versus token budget.
- Illustrate with concrete examples: describing a photograph, answering questions about a chart, extracting structured data from a form, reasoning over a multi-panel research figure.
- Include a simple architecture diagram (described in text or suggested as a Mermaid flowchart) showing vision encoder → projection layer → LLM decoder.
- Address edge cases and failure modes: low-resolution artifacts, cultural visual biases, hallucinations on ambiguous diagrams, and how prompt phrasing (e.g., “describe every element you see” versus “focus on trends”) dramatically changes output quality.
- Connect back to previous concepts: multimodal context is still context; the same optimization questions (minimal relevant slices, compression, isolation) apply, except the “slices” can now be image crops or document pages.
- Emphasize that we are giving only the minimal theory needed for engineering intuition; deeper architectural papers are left for further reading in the golden sources.
- Transition to Section 4: With the foundations in place, let’s move to concrete code that lets you send images and PDF pages to a multimodal LLM today.
-  **Section length**: 1,200 words (don't count the images or mermaid diagrams)

## Section 4: Applying multimodal LLMs to images and PDFs
- Walk through a complete Python example that loads a local image (or image from URL), encodes it appropriately (base64 or direct file upload depending on the API), and sends it together with a text prompt to a multimodal LLM.
- Show progressively more complex prompts: simple captioning, visual question answering, structured extraction using schemas you learned in Lesson 4, and multi-image comparison (“which chart shows higher growth?”).
- Demonstrate PDF handling by converting each page to an image, then either processing pages independently or concatenating a intelligently chosen subset into one call; include code patterns for page selection based on metadata or quick thumbnail analysis.
- Provide three realistic worked examples: (1) analyzing a financial report page containing both narrative text and a bar chart, (2) extracting actionable insights from a handwritten diagram, (3) comparing two versions of a marketing creative.
- Discuss prompt-engineering nuances specific to vision: reference objects by spatial location (“the red line in the upper-left plot”), ask the model to list every visible element before reasoning, and repeat critical instructions at beginning and end of the visual context.
- Cover production pitfalls: token explosion when sending many high-resolution pages, inconsistent formatting of visual observations that later enter agent memory, and how to use structured outputs to force the model to return clean JSON even when describing images.
- Show how to integrate the visual observations into the short-term working memory patterns from Lesson 9 so downstream agent turns can reference them.
- Include code snippets with clear comments, expected input/output shapes, and debugging tips (e.g., printing token counts for the visual part of the prompt).
- Contrast naive “send every page” versus selective retrieval approaches to foreshadow the multimodal RAG section.
- Transition to Section 5: While single-turn multimodal calls are powerful, most production systems need to retrieve relevant images or document pages from a large corpus first; this is where multimodal RAG enters.
-  **Section length**: 950 words (Don't count the code, images or mermaid diagrams)

## Section 5: Foundations of multimodal RAG
- Remind the reader (without re-teaching) of the RAG pipeline from Lesson 10 and show why text-only retrieval fails when the corpus contains charts, screenshots, or layout-heavy PDFs.
- Introduce multimodal embeddings that project both images and text into a shared vector space so a text query can surface relevant visuals and vice versa.
- Explain at high level how models like ColPali adapt vision-language architectures for document retrieval by treating each page as an image and producing late-interaction embeddings that preserve fine-grained token-to-patch matching.
- Contrast ColPali-style vision retrieval with traditional OCR-then-embed pipelines along accuracy, implementation complexity, and preservation of visual semantics.
- Discuss indexing strategies: chunking documents into pages or figures, embedding each visual unit, storing in a vector database that supports multimodal vectors, and optionally adding metadata filters you already know from prior RAG work.
- Cover query-time nuances: embedding the user’s text query with the same multimodal model, retrieving top-k visual chunks, then passing those images directly (not OCR text) into the generator’s context.
- Present failure modes (retrieving visually similar but semantically irrelevant images, resolution mismatches between index and generation, token budget when many images are retrieved) and mitigation patterns (reranking, caption-assisted filtering, adaptive image resolution).
- Include a diagram (Mermaid or textual) showing the end-to-end multimodal RAG flow: multimodal embedder → vector store → multimodal LLM generator.
- Emphasize that the same system works for pure images, scanned PDFs, and born-digital documents because everything is treated as images; once the text-image path is built, documents require almost no extra code.
- Transition to Section 6: Theory is useful, but seeing a minimal working implementation will make the concepts concrete.
-  **Section length**: 750 words (don't count the images or mermaid diagrams)

## Section 6: Implementing multimodal RAG for images, PDFs and text
- Provide a complete, runnable walkthrough (mirroring best practices from the golden sources) that indexes a small corpus containing text snippets, photographs, and PDF pages.
- Step-by-step: (1) load and split documents into image-per-page or figure crops, (2) embed each visual item with a multimodal embedding model, (3) store in a vector index with associated raw image bytes or URLs, (4) implement a retriever that accepts text or image queries, (5) pass retrieved images plus original query to a multimodal LLM for generation.
- Show code structure for embedding, retrieval, and generation phases; highlight how few changes are needed to go from text-image RAG to full document support.
- Include two concrete evaluation examples: a query about “year-over-year revenue trend” that correctly surfaces a bar chart image instead of narrative text, and a visual search query that finds similar diagrams.
- Discuss observability: always log the exact images sent to the model (using the tracing tools you will explore in Part 3), measure retrieval recall on visual relevance, and track end-to-end latency and token usage.
- Present compression and selection techniques (thumbnail reranking, clustering near-duplicate images, time-based or metadata filtering) that keep context small while preserving signal—tying back to context engineering.
- Demonstrate that the same index can serve both standard RAG and agentic use cases because the retrieved images become structured observations inside agent memory.
- End with extensibility notes: swapping the embedder or vector store, adding hybrid text+visual retrieval, and preparing the retriever as a tool for the agent we build next.
- Transition to Section 7: With retrieval working, we can now give an autonomous agent the ability to decide when to fetch and reason over visual documents.
-  **Section length**: 650 words (don't count the code, images or mermaid diagrams)

## Section 7: Building multimodal AI agents
- Show how to wrap the multimodal RAG retriever as a tool that an agent (using the ReAct pattern you implemented in Lesson 8) can call.
- Illustrate an end-to-end agent that receives a user question about organizational data, decides whether to retrieve text or visual chunks, receives the images as observations, reasons over them, and produces a final structured answer.
- Provide a worked example: an agent helping an analyst explore a folder of quarterly reports (some text, some PDF with charts); walk through the thought → tool call → multimodal observation → final synthesis loop.
- Discuss context-engineering adaptations required for agents: formatting visual observations with XML tags, repeating key visual instructions, isolating visual context to worker agents in an orchestrator-worker setup, and compressing long visual histories into semantic summaries.
- Highlight integration points with memory systems: storing episodic visual memories (previously seen charts) in long-term semantic stores and retrieving them when relevant.
- Cover graceful degradation: what the agent should do when an image cannot be processed, how to fall back to text descriptions only when token budgets are exceeded, and how to expose confidence or supporting images in the final answer.
- Connect the complete system back to earlier lessons: the agent uses tools and function calling, structured outputs for observations, context engineering to keep the multimodal window manageable, and RAG for knowledge.
- Emphasize that this pattern is directly applicable to the research and writing agents you will build in Part 2; the multimodal skills learned here become foundational for any real-world project.
-  **Section length**: 500 words (don't count the code, images or mermaid diagrams)

## Section 8: Conclusion
- Summarize the core transformation: move from OCR-based text normalization to native multimodal processing for images, PDFs, and text inside the same pipelines you already know how to build.
- Reiterate the business impact—higher accuracy on complex enterprise documents, simpler code paths, and agents that truly see what humans see.
- Position this lesson as the capstone of Part 1: you now possess the complete foundational stack (context engineering, structured outputs, agents, memory, RAG, and multimodal) required to start the hands-on multi-agent research and writing system in Part 2.
- Tease that Part 3 will show how to evaluate, observe, and productionize these multimodal agents, while Part 4 gives you the opportunity to apply everything in a capstone project.
- End with a forward-looking statement: the ability to fluidly combine text, images, and documents inside context-engineered agents is no longer optional; it is table stakes for any serious AI engineering practice.
-  **Section length**: 150 words

## Article Code

Links to code that will be used to support the article. Always prioritize this code over any other code found in the sources: 

1. [Notebook 1](https://github.com/towardsai/course-ai-agents/blob/dev/lessons/11_multimodal/notebook.ipynb)


## Golden Sources
1. [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms)
2. [Vision Language Models](https://www.nvidia.com/en-us/glossary/vision-language-models/)
3. [Multimodal Embeddings: An Introduction](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/)
4. [Multimodal Embeddings: An Introduction](https://www.youtube.com/watch?v=YOvxh_ma5qE)
5. [Multi-modal ML with OpenAI's CLIP](https://www.pinecone.io/learn/series/image-search/clip/)
6. [ColPali: Efficient Document Retrieval with Vision Language Models](https://arxiv.org/pdf/2407.01449v6)

## Other Sources
1. [Image understanding with Gemini](https://ai.google.dev/gemini-api/docs/image-understanding)
2. [Multimodal RAG with Colpali, Milvus and VLMs](https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag)
3. [Google Generative AI Embeddings (AI Studio & Gemini API)](https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/)
4. [LangGraph quickstart](https://langchain-ai.github.io/langgraph/agents/agents/)
5. [Complex Document Recognition: OCR Doesn’t Work and Here’s How You Fix It](https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it)
6. [What are some real-world applications of multimodal AI?](https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai)
7. [What Is Optical Character Recognition (OCR)?](https://blog.roboflow.com/what-is-optical-character-recognition-ocr/)
8. [The 8 best AI image generators in 2025](https://zapier.com/blog/best-ai-image-generator/)