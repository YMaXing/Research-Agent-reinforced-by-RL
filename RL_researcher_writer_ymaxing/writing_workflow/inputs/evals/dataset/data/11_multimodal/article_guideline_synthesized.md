## Global Context of the Lesson

### What We Are Planning to Share

A hands-on lesson presenting the fundamentals of working with multimodal data in the context of LLMs, LLM workflows, and AI Agents. When building AI apps in the real world, we rarely work only with text data. As human beings, we work daily with all types of data: text, images, documents, and audio. Thus, having them integrated into our AI systems is a must. This quickly translates to a business problem, where all enterprise-grade AI apps use and require multimodal data (text, images, documents) when manipulating their private data from databases, warehouses, and lakes. 

In the early days, most AI apps tried to normalize everything to text. For example, we used OCR to parse documents and map them to text or tabular data. The plot twist behind this lesson is that instead of translating images or documents to text, when building AI and RAG systems, it's better and recommended to process them directly as native images or documents. This way, we can natively pass all the rich visual information to the model. To understand how to do that, we have to cover a few theoretical aspects such as how multimodal LLMs, embedding models, and RAG systems work. Just enough theory for the reader to have an intuition on how these work. Then, we will implement a few hands-on use cases where we explain how to work with LLMs with text, images, and documents combined. Then we will connect the reader to the bigger picture and show them, first, how to build a simple text-image RAG system, and then an agentic RAG app. We want to highlight that once you build a text-image system, as the documents are processed as images as well, mapping it to a text-images-document modality is a no-brainer.

So this lesson will provide all the knowledge to build enterprise AI agents or LLM workflows that can process your personal or organizational data. Side note: most of these techniques can be translated to video or audio, but that won't be covered here.

### Why We Think It's Valuable

Often, we have to manipulate various types of multimodal data such as text, images, and documents within the same context window and tools. Most of the issues come when we start treating each image or document the same. We cannot do that. An extremely popular example is building AI agents that process various financial PDFs that sometimes contain only text and sometimes tables, diagrams, and graphs from various reports and research. If we translate text-only documents to text, that's fine. But if we try to translate the documents or images with complex layouts to text, we lose a lot of information, resulting in suboptimal solutions. Thus, instead of using OCR-based systems that normalize everything to text, modern AI systems directly process data input in their native format (documents, images, audio), preserving all the rich information made possible by their specific format. For example, if we translate sketches or diagrams to text, it's impossible to grasp all the details, such as the colors and geometrical relationships between the elements, in text. But directly processing the image, as a human would, is easier to implement, faster, cheaper, more intuitive, and usually more performant. That's why AI apps MUST have native support for images and documents to easily process complex data formats and relationships that are natural for a human being to use in their daily workflow.

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

This is lesson 11 (from part 1) of the course on AI agents and LLM workflows.

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
- Open with a personal story from one of our real-world consulting projects where a financial analysis agent kept failing on quarterly reports because charts, graphs, and layout relationships were lost when OCR converted PDFs to plain text.
- Explain that as AI agents and LLM workflows moved from simple chatbots to enterprise systems, the data we needed to reason over became inherently multimodal (text + images + complex documents).
- Highlight why this matters now: enterprises store the majority of their knowledge in PDFs, images, scanned reports, dashboards, and diagrams that contain critical spatial, visual, and relational information that text alone cannot capture.
- Connect to previous lessons by noting that even with sophisticated context engineering, memory systems, and RAG pipelines from Lessons 3, 9, and 10, none of those techniques deliver their full potential if we throw away visual information before it ever reaches the LLM.
- Present the central plot twist of the lesson: instead of forcing every image and document into text through OCR, modern systems process native multimodal inputs directly, preserving colors, layouts, geometric relationships, and visual semantics.
- Tease the journey ahead: light theory on how multimodal LLMs and embedding models actually work, followed by concrete implementations for images, PDFs, text-image RAG, and finally a multimodal agentic RAG system.
- End the section by stating that mastering these techniques completes the last major missing piece for building production enterprise AI agents that can truly understand your organization's private data.
- Transition to Section 2: Before we can adopt native multimodal processing, we must clearly understand why the traditional OCR-first approach so often fails in practice.
-  **Section length:** 300 words

## Section 2: Limitations of traditional document processing
- Detail the historical workflow most teams followed: scan document → run OCR → extract text/tables → embed text → retrieve with classic vector search.
- Explain the core failure modes with concrete examples:
  - Loss of spatial layout (tables where row/column relationships disappear).
  - Destruction of visual semantics (charts where color, trend lines, and annotations carry meaning).
  - Poor performance on complex layouts (research papers with interleaved figures, captions, and multi-column text).
  - Complete failure on handwritten notes, scanned forms, or diagrams without clear text.
- Use the financial PDF example from the brief: a quarterly report containing both pure-text sections and intricate bar charts with overlaid numbers; OCR produces noisy or incomplete text while losing the visual trend that a human (or multimodal model) would instantly grasp.
- Discuss real-world consequences: higher hallucination rates, incorrect numerical reasoning, missed insights, and ultimately agents that cannot be trusted with high-stakes organizational data.
- Reference the "Complex Document Recognition: OCR Doesn’t Work and Here’s How You Fix It" article to support the claim that OCR-based normalization is fundamentally limited for modern document understanding.
- Contrast the old approach with the new philosophy: treat images and PDFs as first-class citizens that can be embedded and reasoned over natively.
- Include a simple before-and-after diagram (text-only vs. native multimodal) to visualize information loss.
- Transition to Section 3: To move beyond these limitations we first need to understand how modern multimodal LLMs are architected and why they can consume raw pixels alongside text tokens.
-  **Section length**: 650 words (don't count the mermaid diagrams or image links)

## Section 3: Foundations of multimodal LLMs
- Provide just enough theory for intuition without turning the lesson into a research paper.
- Explain the core architecture: a vision encoder (transforms image patches into visual tokens), a projection layer that maps visual tokens into the same embedding space as text tokens, and a standard LLM decoder that now attends over both.
- Describe how contrastive pre-training (similar to CLIP from the sources) teaches the model to align images and text descriptions in a shared space.
- Cover how multimodal models handle variable-length visual tokens and interleave them with text in a single context window.
- Discuss token efficiency, context window implications, and why visual tokens are typically more expensive than text tokens.
- Present key training objectives: image-text matching, visual question answering, document understanding, and chart reasoning.
- Include a high-level architecture diagram (vision encoder → projector → LLM) with labeled components; annotate where visual tokens enter the same attention mechanism as text.
- Compare single-modal vs. multimodal embedding spaces and why alignment quality determines downstream performance.
- Reference the golden sources "Understanding Multimodal LLMs", "Vision Language Models", and "Multi-modal ML with OpenAI's CLIP" to ground the explanations.
- Highlight practical implications for context engineering (Lesson 3): visual information now competes for the same limited context window, so strategic selection becomes even more important.
- Transition to Section 4: With this foundation in place, let's see how to call these models on real images and PDFs using concrete code examples.
-  **Section length**: 1,200 words (don't count the images or mermaid diagrams)

## Section 4: Applying multimodal LLMs to images and PDFs
- Shift to 70% practice mode with concrete, runnable examples.
- Walk through calling a multimodal LLM on a single image (describe chart, answer questions about a photo, extract information from a screenshot).
- Show code structure for passing both text prompts and image bytes or URLs in the same request; highlight the message format that combines text and image content.
- Extend to PDFs: explain converting PDF pages to images (one image per page) and passing the full set as a sequence of visual inputs.
- Demonstrate progressive refinement: first ask high-level questions ("What is the overall trend?"), then follow up with detailed numerical extraction on the same images.
- Present a side-by-side comparison table: OCR-based extraction vs. native multimodal extraction on the same financial report, showing accuracy and qualitative insight differences.
- Include error analysis: cases where the model still struggles (tiny text, overlapping elements) and prompt patterns that mitigate them.
- Show how to combine text, image, and previous conversation history in one context window, reinforcing context engineering lessons.
- Provide three progressively complex notebooks-style examples: (1) image description, (2) chart reasoning, (3) multi-page PDF financial analysis.
- Use the "Image understanding with Gemini" source to inform the code patterns without naming specific vendor APIs unless the writer chooses illustrative snippets.
- Transition to Section 5: While direct multimodal prompting works well for single documents, most enterprise use cases require retrieving the right images or pages first; this leads us to multimodal RAG.
-  **Section length**: 950 words (Don't count the code, images or mermaid diagrams)

## Section 5: Foundations of multimodal RAG
- Explain why classic text RAG fails for visual documents and how multimodal embeddings solve the problem.
- Describe two main approaches: (1) embedding entire page images with vision-language models, (2) late-interaction models like ColPali that produce token-level embeddings for fine-grained retrieval.
- Detail ColPali specifically (from the arXiv paper in golden sources): how it uses a vision-language model to generate embeddings for each visual token on a document page, enabling retrieval without any OCR.
- Cover indexing strategy: split documents into pages or logical chunks, embed each page as an image, store in a vector database that supports multimodal vectors.
- Discuss retrieval nuances: similarity is now computed in a joint vision-language space; top-k pages are returned as images rather than text chunks.
- Address re-ranking and fusion when mixing text embeddings and image embeddings in the same index.
- Present a diagram of the multimodal RAG pipeline: PDF → page images → multimodal embedder → vector DB → retrieval → multimodal LLM.
- Compare token cost, accuracy, and latency versus OCR + text RAG using real-world trade-off numbers from the sources.
- Reference "Multimodal Embeddings: An Introduction", "ColPali: Efficient Document Retrieval with Vision Language Models", and the Hugging Face ColPali + Milvus blog.
- Emphasize connection to Lesson 10: all the advanced retrieval techniques you learned there still apply, but the embedding function and stored modality change.
- Transition to Section 6: Theory is useful, but seeing a working implementation that retrieves and reasons over mixed text, images, and PDFs makes the concepts concrete.
-  **Section length**: 750 words (don't count the images or mermaid diagrams)

## Section 6: Implementing multimodal RAG for images, PDFs and text
- Provide a complete end-to-end implementation walkthrough that the reader can follow in a notebook.
- Step 1: ingest a mixed corpus (text files, images, PDFs); convert PDFs to page images.
- Step 2: embed every item using a multimodal embedding model (show code for both image and text paths).
- Step 3: store in a vector database with metadata distinguishing modality.
- Step 4: implement a retriever that accepts a multimodal query (text + optional image) and returns top relevant pages/images.
- Step 5: pass retrieved images directly to a multimodal LLM along with the user question and any conversation history.
- Show code for query expansion, hybrid retrieval (text + image embeddings), and result fusion.
- Include a practical example using a set of financial reports and product images; demonstrate queries like "Compare the revenue trend in these two reports" that require both text and chart understanding.
- Add debugging techniques: visualize retrieved images, show similarity scores, and allow the reader to see which visual features drove retrieval.
- Discuss production considerations: caching embeddings, handling very large documents, cost control when sending many images to the LLM.
- End with a working minimal system the reader can run and extend, reinforcing that once you have text + image RAG, adding full document support is straightforward because documents are already processed as images.
- Transition to Section 7: The final step is to embed this multimodal RAG capability inside an agent that can decide when to retrieve images, when to call tools, and how to orchestrate multi-turn reasoning over visual data.
-  **Section length**: 650 words (don't count the code, images or mermaid diagrams)

## Section 7: Building multimodal AI agents
- Show how to wrap the multimodal RAG system inside an agent loop that uses the planning and reasoning patterns from earlier lessons.
- Demonstrate an agent that can be given a high-level goal ("Analyze last quarter's performance"), autonomously retrieves relevant PDF pages and images, reasons over them, calls additional tools if needed, and produces a structured report.
- Highlight the role of structured outputs (Lesson 4) for forcing the agent to return both text answers and references to specific retrieved images.
- Discuss memory implications: storing conversation history that now includes references to previously seen images.
- Present a high-level control flow diagram showing the agent deciding between text retrieval, image retrieval, direct multimodal LLM calls, or tool use.
- Provide a minimal code skeleton that integrates the retriever from Section 6 with the ReAct-style loop from Lesson 8.
- Give two concrete examples: (1) personal photo library assistant that answers questions about family pictures and documents, (2) enterprise financial analyst agent that navigates multiple reports containing both text and charts.
- Emphasize that the same system can be extended to the research and writing agents the reader will build in Part 2 by simply adding multimodal retrieval tools.
- Connect back to context engineering: the agent's most important job is deciding which visual artifacts actually belong in the limited context window.
-  **Section length**: 500 words (don't count the code, images or mermaid diagrams)

## Section 8: Conclusion
- Summarize the key mindset shift: stop forcing the world into text; give AI native eyes by processing images and documents directly.
- Reiterate that multimodal capabilities complete the foundation built across the first eleven lessons, enabling truly enterprise-ready agents that understand the rich, visual data organizations actually produce.
- Remind the reader that the techniques covered here (native image handling, multimodal embeddings, ColPali-style retrieval, agentic orchestration over visual artifacts) translate naturally to the research and writing agent system they will implement in Part 2 and productionize in Part 3.
- End with an encouraging note that the reader now possesses the complete toolkit to build AI systems that see the world more like humans do.
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