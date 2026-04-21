**Multimodal AI Engineering: From OCR to Native Image & Document Processing in 2025**

We spent years building AI systems that treated everything as text. Documents were OCR'd, diagrams were described in words, and images were captioned before feeding them into models. It felt logical at the time. After all, our LLMs spoke text, so why not translate everything into their native language?

The results were never quite right. Financial reports lost meaning when charts became bullet points. Technical manuals became brittle when sketches turned into vague descriptions. Medical imaging workflows required constant human correction because a caption could never capture what a radiologist sees in a single glance. We accepted these compromises because the alternative seemed too complex.

I remember one project where we processed thousands of technical drawings. The OCR pipeline worked on clean text but failed on anything with symbols, rotated annotations, or complex layouts. We layered on specialized models for tables, another for diagrams, and spent weeks maintaining the brittle chain of components. The system was slow, expensive, and still required manual review for anything important.

That experience changed how I think about multimodal data. Instead of forcing images and documents into text, modern systems process them natively. The shift isn't just technical convenience. It represents a fundamental improvement in what our AI applications can understand and do.

In this lesson, we'll move beyond the OCR-first mindset that dominated early AI workflows. You'll see why translating visual information to text creates unnecessary loss, how multimodal LLMs handle images and PDFs directly, and how to build retrieval systems that work with native formats. We'll implement practical examples using Gemini, then connect these techniques to RAG and agent systems. By the end, you'll have the foundation to build AI applications that process your organization's real data, not just its text.

We'll start by examining why traditional document processing fails on complex content, explore how multimodal LLMs work under the hood, apply these models to images and PDFs, build a multimodal RAG system, and finally create an agent that leverages these capabilities. The journey moves from understanding the problems with our old approaches to implementing systems that work with data in its natural form.

## Limitations of Traditional Document Processing

The problems with traditional document processing become obvious once you move beyond simple invoices or clean text documents. Most enterprise content doesn't fit the neat templates that OCR systems expect. Financial reports contain charts that carry critical meaning. Technical manuals include diagrams that explain concepts text alone cannot convey. Research papers mix tables, figures, and annotations in ways that break when forced into linear text.

Traditional pipelines follow a predictable but fragile sequence. First, the document loads. Then comes preprocessing to remove noise and correct orientation. Layout detection identifies different regions, attempting to separate text from tables, charts, and images. OCR models process the text regions while specialized models handle other structures. The final step assembles everything into JSON or another structured format.

This multi-step approach creates multiple failure points. Each component must work perfectly for the system to succeed. Layout detection fails on irregular formats. OCR accuracy drops on poor scans, handwritten notes, or complex fonts. Specialized models for tables or charts introduce their own errors and maintenance burden. When one piece breaks, the entire pipeline suffers.

Research shows the scale of these problems. Traditional OCR engines achieve 88-94% accuracy on simple layouts but struggle with multi-column formats, nested tables, overlapping text, faded watermarks, and embedded graphics. Handwriting recognition typically reaches 3-5% character error rate, considered good but still requiring human review for critical applications. Poor scan quality below 300 DPI causes accuracy drops of 20% or more. A 5-degree tilt can increase word error rate by 15%.

Enterprise use cases reveal even clearer limitations. Text-only approaches to financial report analysis miss critical information in charts and tables. Summarization models that ignore visual elements produce incomplete or factually incorrect outputs. Medical imaging diagnostics require vision capabilities that pure text systems cannot provide. Technical documentation with sketches loses essential spatial relationships when converted to text.

The rigidity of template-based systems makes them particularly problematic. They work for fixed formats but break when documents vary. A slight change in layout requires manual rule updates. The lack of contextual understanding means numbers without units or ambiguous terms get misinterpreted. These systems scale poorly with document variety and volume.

The fundamental issue runs deeper than accuracy metrics. Traditional approaches force visual information into text, losing the rich context that diagrams, charts, and spatial relationships provide. A table's structure, a chart's trends, a diagram's component relationships, these elements carry meaning that text descriptions cannot fully capture. When we normalize everything to text, we accept information loss as inevitable.

This realization led to the current shift toward native multimodal processing. Modern systems treat images and documents in their original format rather than translating them to text first. Multimodal LLMs can process these inputs directly, preserving layout, visual relationships, and contextual information that OCR pipelines destroy. The approach is simpler, faster, and usually more accurate for complex content.

The contrast becomes clear when comparing traditional pipelines to native multimodal approaches. Instead of multiple specialized models and brittle handoffs, a single multimodal model handles text, images, and document structure together. The system becomes more robust because it avoids the error cascade that occurs when one component fails. Performance improves because visual information remains intact rather than being approximated in text.

This shift matters for anyone building AI systems that work with real organizational data. Most enterprise content contains visual elements that carry essential meaning. Technical documentation, financial reports, medical records, research papers, these documents lose critical context when forced through OCR pipelines. Native multimodal processing preserves that context, enabling AI applications that actually understand the materials they process.

The theoretical foundations for this approach come from advances in vision-language models. These systems learn to align visual and textual representations in shared embedding spaces. The same techniques that power image captioning and visual question answering now extend to document understanding. Rather than treating documents as text with occasional images, modern models process the complete visual document as a unified input.

This foundation enables practical applications that were difficult or impossible with traditional methods. Research assistants can now analyze papers with complex figures. Financial analysts can query reports containing both text and charts. Technical teams can search documentation that includes diagrams and schematics. The capabilities extend beyond simple text extraction to genuine multimodal understanding.

The transition from OCR-centric to native multimodal processing represents more than a technical improvement. It changes how we think about document intelligence. Instead of forcing visual content into text representations, we build systems that work with data in its natural form. This approach scales better, performs better on complex content, and requires fewer moving parts to maintain.

The practical benefits become clear when implementing these systems. Processing times decrease because we eliminate multiple model calls and post-processing steps. Accuracy improves on visually complex documents because layout and visual relationships remain intact. Development effort decreases because we replace brittle pipelines with unified models that handle multiple data types.

This sets the stage for understanding how multimodal LLMs actually work. The architectures that enable native processing of images and documents build on the same transformer foundations as text-only models, but with specific adaptations for visual inputs. The next section explores these foundations, providing the technical intuition needed to use these models effectively in your own applications.

## Foundations of Multimodal LLMs

Understanding how multimodal LLMs work provides the foundation for using them effectively. You don't need to implement these architectures from scratch, but you need enough technical intuition to make good decisions about model selection, prompt design, and system architecture. The two primary approaches differ significantly in their design choices and trade-offs.

The unified embedding decoder architecture represents the simpler approach. An image gets converted into embedding vectors that match the dimension of text token embeddings. These image tokens then concatenate with text tokens and pass through a standard decoder-only LLM. The model processes both modalities through the same self-attention mechanism without architectural changes to the underlying transformer.

This method's strength lies in its implementation simplicity. You don't modify the LLM architecture. The image encoder, typically a pretrained vision transformer like CLIP or SigLIP, extracts features from image patches. A linear projection layer aligns these visual features with the text embedding space. The resulting tokens feed directly into the LLM alongside text tokens.

The cross-modality attention architecture takes a different approach. Instead of converting images into input tokens, this method uses cross-attention layers within the LLM to integrate visual information. The image encoder still processes the input, but rather than concatenating tokens at the input level, the model attends to visual features through dedicated cross-attention mechanisms at specific layers.

This approach offers computational advantages for high-resolution images. The model doesn't need to process every image token through all transformer layers. Visual information gets introduced later through cross-attention, reducing the sequence length the self-attention mechanism must handle. The original LLM parameters can remain frozen, preserving text-only performance while adding multimodal capabilities.

Both approaches share common components. A vision encoder, typically based on CLIP or similar contrastive models, processes the image. These encoders divide images into patches, similar to how text gets tokenized. Each patch becomes an embedding vector. The key difference lies in how these visual embeddings integrate with the language model.

The linear projection that often follows the vision encoder serves a specific purpose. Vision transformers typically output embeddings with different dimensions than text transformers. The projection layer maps visual features into the same dimensional space as text token embeddings. This alignment enables the LLM to process both modalities through its standard mechanisms.

Image encoders like CLIP, OpenCLIP, or SigLIP learn representations where semantically similar images and text descriptions map to nearby vectors. This alignment in embedding space enables the multimodal capabilities we see in practice. The same techniques that power image search and zero-shot classification also support document understanding when applied to PDF pages treated as images.

Trade-offs between these architectures matter for practical applications. The unified embedding approach proves simpler to implement and often achieves higher accuracy on OCR-related tasks. Processing all tokens through the full transformer stack gives the model maximum opportunity to integrate visual and textual information. However, this comes at the cost of computational efficiency, especially with high-resolution images that generate many tokens.

The cross-attention approach offers better computational characteristics for high-resolution inputs. By introducing visual information through cross-attention rather than input concatenation, the model avoids long sequences in its self-attention layers. This efficiency becomes important when processing detailed documents or multiple images. The ability to keep the original LLM frozen during training also helps maintain text-only performance.

Hybrid approaches attempt to combine the strengths of both methods. A low-resolution thumbnail provides global context through the unified embedding path, while high-resolution patches contribute fine details through cross-attention. This balances computational efficiency with the accuracy benefits of detailed visual processing.

Recent models demonstrate these architectures in practice. Open-source options include Llama 4, Gemma 2, Qwen3, and DeepSeek variants with multimodal capabilities. Closed-source models like GPT-5, Gemini 2.5, and Claude also support native multimodal inputs. The specific architecture matters less than understanding the general principles of how visual information integrates with language models.

These same techniques extend to other modalities. Different encoders handle audio, video, or specialized data types. The core principle remains consistent: learn representations that align across modalities in a shared embedding space. This alignment enables the model to reason about relationships between different types of information.

The distinction between multimodal LLMs and diffusion models for generation deserves clarification. Diffusion models like Stable Diffusion focus on creating images from text descriptions. They excel at generation but don't provide the understanding capabilities needed for document analysis or visual question answering. Multimodal LLMs focus on understanding and reasoning across modalities, though some can generate images as well.

In agent systems and LLM workflows, diffusion models can serve as specialized tools. An agent might use a multimodal LLM to understand a document, then call a diffusion model to generate a diagram illustrating a concept from that document. The separation of concerns works well, with understanding and generation handled by models optimized for each task.

These architectural foundations explain why multimodal LLMs outperform traditional OCR pipelines on complex documents. Rather than losing information through text conversion, the models process visual content directly. Layout, spatial relationships, color, and other visual cues remain available for reasoning. This native processing enables capabilities that text-only approaches cannot match.

The practical implications become clear when implementing these systems. Processing documents as images simplifies the pipeline. You avoid maintaining separate models for text, tables, charts, and diagrams. The single multimodal model handles all content types, reducing complexity and potential failure points. Performance typically improves because the model sees the complete document rather than a degraded text representation.

This understanding of multimodal LLM foundations prepares us for practical implementation. The next section demonstrates how to apply these models to images and PDFs using different input formats. These examples show the flexibility of modern APIs and provide patterns you can adapt to your own applications.

## Applying Multimodal LLMs to Images and PDFs

Working with multimodal LLMs requires understanding the different ways to provide visual inputs. The three primary methods, raw bytes, Base64 encoding, and URLs, each serve different use cases depending on your storage strategy and application architecture. Choosing the right approach affects both performance and system design.

Raw bytes represent the most direct method. You load the image or PDF as binary data and pass it directly to the model. This approach works well for one-off API calls where you don't need to store the media long-term. The main limitation appears when persisting data in databases. Most databases expect text or structured data, and storing raw bytes can lead to corruption or compatibility issues.

Base64 encoding solves the storage problem by converting binary data into text strings. This format works reliably across databases, APIs, and web applications. The trade-off is size. Base64 encoding increases data size by approximately 33% compared to raw bytes. For applications that store many images or documents, this overhead becomes significant. However, the universal compatibility often outweighs the storage cost.

URLs provide the most efficient option for applications using data lakes or cloud storage. Rather than moving large files through your application code and API calls, you provide a reference that the model can fetch directly. This approach minimizes network traffic and memory usage in your application. Public URLs work for internet data, while private URLs from services like AWS S3 or Google Cloud Storage work for enterprise data lakes. The model needs appropriate permissions to access private storage.

The choice between these methods depends on your architecture. Applications that process media once and discard it can use raw bytes for simplicity. Systems that store and reuse media benefit from Base64 for database compatibility. Large-scale applications with dedicated storage layers should use URLs to minimize data movement.

Let's examine these approaches through practical examples using Gemini. We'll start with image processing, then extend the same patterns to PDFs. The code demonstrates both simple captioning and more complex tasks like object detection.

Consider this sample image of a robot and kitten. We can process it using raw bytes with a function that loads, optionally resizes, and converts the image to the desired format. WEBP provides the most efficient compression for this use case.

```python
def load_image_as_bytes(image_path, format="WEBP", max_width=600, return_size=False):
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
```

Loading our sample image produces 44,392 bytes. We can pass this directly to the model along with a prompt to generate a caption. The response provides a detailed description that captures both the robot's technical appearance and the kitten's playful interaction.

The same image processed as Base64 produces a string 59,192 characters long, demonstrating the expected 33% size increase. Despite the larger size, Base64 offers advantages for database storage since all database systems handle text reliably. The caption generation works identically to the raw bytes approach.

Public URLs enable the simplest integration for internet content. Gemini's `url_context` tool allows direct processing of publicly accessible PDFs and images by providing the URL. This eliminates the need to download and pass data through your application code.

For private data lakes, the pattern involves providing storage URLs that the model can access directly. While current Gemini implementations work best with Google Cloud Storage, the general principle applies to any storage system where the model has appropriate access permissions. This approach minimizes data movement and leverages the storage system's existing infrastructure.

Object detection demonstrates more sophisticated multimodal capabilities. We define Pydantic models to specify the expected output structure for bounding boxes and labels. The prompt instructs the model to detect prominent objects and return normalized coordinates along with descriptive labels.

```python
class BoundingBox(BaseModel):
    ymin: float
    xmin: float
    ymax: float
    xmax: float
    label: str

class Detections(BaseModel):
    bounding_boxes: list[BoundingBox]
```

The model processes the image and returns structured detections. For our robot and kitten image, it identifies both objects with appropriate bounding boxes. Visualizing these detections on the original image confirms the accuracy of the predictions. The robot receives a large bounding box covering most of the right side of the image, while the kitten gets a smaller, precisely positioned box.

PDF processing follows similar patterns to image processing. We can treat PDF pages as images or process the PDF document directly. The `attention_is_all_you_need_paper.pdf` serves as our example. Displaying the first page shows the familiar transformer architecture diagram that launched the current era of large language models.

Processing the PDF as raw bytes produces a comprehensive summary of the document's content. The model correctly identifies the paper's focus on the transformer architecture, its departure from recurrent and convolutional networks, and its superior performance on machine translation tasks. The same PDF processed as Base64 yields identical results, demonstrating that the input format doesn't affect the model's understanding when properly handled.

Object detection on PDF pages treated as images reveals the power of native multimodal processing. The model successfully identifies the transformer architecture diagram on one of the paper's pages and provides accurate bounding box coordinates. This capability would be difficult to achieve with traditional OCR approaches that would struggle to understand the diagram's structure and components.

These examples demonstrate why native multimodal processing outperforms traditional OCR pipelines. The model sees the complete visual document, including layout, spatial relationships, and graphical elements that text conversion would lose. The unified approach simplifies the system architecture while improving accuracy on complex content.

The patterns established here extend naturally to multimodal RAG systems. Rather than converting documents to text before embedding, we can embed the native visual representations. This preserves information that would be lost in translation and enables more accurate retrieval for visually complex documents. The next section explores these foundations in detail.

## Foundations of Multimodal RAG

The limitations of context windows make retrieval essential when working with large collections of multimodal data. Even models with million-token contexts cannot efficiently process thousands of document pages or hundreds of images in a single call. Multimodal RAG addresses this by retrieving only the most relevant visual and textual content for each query.

A basic multimodal RAG system for text and images follows a straightforward pattern. During ingestion, we embed images using a text-image embedding model and store these embeddings in a vector database. At query time, we embed the user's text query with the same model and retrieve the most similar images based on embedding similarity. Since both text and image embeddings occupy the same vector space, this approach works bidirectionally. You can query with text to find images, query with images to find text, or search within a single modality.

This pattern extends naturally to documents when we treat PDF pages as images. Rather than extracting text through OCR and losing visual information, we embed the complete page images. The retrieval system finds pages containing relevant visual and textual content based on the semantic similarity of their embeddings to the query.

ColPali represents the current state-of-the-art approach for document-focused multimodal RAG. The key innovation involves bypassing traditional OCR pipelines entirely. Instead of extracting text, detecting layout, chunking content, and embedding text segments, ColPali processes document pages as images using vision-language models.

The architecture builds on the multimodal LLM concepts we explored earlier. A vision encoder processes document pages as images, dividing them into patches and generating embeddings for each patch. Unlike single-vector embeddings that compress an entire document into one representation, ColPali produces multi-vector embeddings, essentially a "bag of embeddings" that preserves detailed information from different regions of the page.

This multi-vector approach enables the late interaction mechanism that gives ColPali its power. During retrieval, each token in the query embedding gets compared to every patch embedding from the document. The system calculates maximum similarity scores for each query token across all document patches, then sums these scores to rank documents. This fine-grained matching captures both textual content and visual layout information that single-vector approaches miss.

The advantages over traditional pipelines become clear when examining real performance metrics. ColPali achieves 81.3% average nDCG@5 across the ViDoRe benchmark, substantially outperforming OCR-based systems. The improvement is most dramatic on visually complex tasks like infographics, scientific figures, and tables. Processing times decrease because the system eliminates multiple model calls for layout detection, OCR, table extraction, and captioning.

The computational benefits extend beyond accuracy. Traditional pipelines require sequential processing through multiple specialized models, creating latency bottlenecks and maintenance complexity. ColPali processes each document page in a single forward pass through the vision-language model. The resulting embeddings can be indexed efficiently, and queries execute quickly using standard vector similarity operations.

Real-world applications demonstrate these advantages clearly. Financial document analysis benefits enormously from preserving chart and table information that OCR systems cannot represent accurately in text. Technical documentation with diagrams and schematics becomes searchable in ways that text-only systems cannot achieve. Research paper analysis can incorporate figures and their relationship to surrounding text without losing critical visual context.

The paradigm shift extends beyond performance metrics. Traditional approaches force all document content into text representations, accepting information loss as inevitable. Multimodal RAG treats documents in their native visual form, preserving the complete context that human readers use. This philosophical change leads to systems that better match how people actually understand documents.

Implementing multimodal RAG requires understanding both the theoretical foundations and practical considerations. The embedding model choice affects both accuracy and computational cost. Vector database selection must support efficient storage and retrieval of multi-vector embeddings. Query processing needs to handle the different characteristics of text queries versus visual queries.

The next section demonstrates these concepts through a concrete implementation. We will build a multimodal RAG system that indexes both standard images and PDF pages treated as images. The example uses an in-memory vector store for simplicity while maintaining the core patterns that scale to production vector databases. This hands-on approach will make the theoretical concepts concrete and provide a foundation for adapting these techniques to your own applications.

## Implementing Multimodal RAG for Images, PDFs and Text

Building a practical multimodal RAG system demonstrates how the concepts from previous sections combine into a working application. Our example indexes both standard images and PDF pages treated as images, then enables text queries that retrieve the most relevant visual content. This approach mirrors production patterns while remaining simple enough to understand completely.

The implementation uses our existing knowledge of multimodal processing. We treat PDF pages as images, generate descriptions for each image using Gemini, and create embeddings from those descriptions. In a production system, you would use a native multimodal embedding model to skip the description step entirely. The core RAG pattern remains identical regardless of whether you embed descriptions or the images directly.

The vector index for this example uses a simple in-memory list rather than a full vector database. Each entry contains the image bytes, filename, generated description, and embedding vector. This structure mirrors what you would store in a production vector database, though real implementations would use efficient indexing structures like HNSW for fast similarity search.

Let's examine the key functions that make this system work. The `create_vector_index` function processes a list of image paths and builds our searchable index. For each image, it generates a description using Gemini, creates an embedding from that description, and stores everything in a structured format.

```python
def create_vector_index(image_paths):
    vector_index = []
    for image_path in image_paths:
        image_bytes = load_image_as_bytes(image_path, format="WEBP")
        
        image_description = generate_image_description(image_bytes)
        image_embedding = embed_text_with_gemini(image_description)
        
        vector_index.append({
            "content": image_bytes,
            "type": "image",
            "filename": image_path,
            "description": image_description,
            "embedding": image_embedding,
        })
    return vector_index
```

The description generation step deserves special attention. In this example, we use Gemini to create text descriptions of each image, then embed those descriptions. This approach works for our demonstration but represents the exact pattern we criticized in earlier sections. Converting visual information to text loses important details that a native multimodal embedding would preserve.

The real-world implementation would replace the description step with direct multimodal embedding. Modern embedding models from Voyage, Cohere, Google, and OpenAI can process images directly. The code change would be minimal. Instead of generating and embedding a description, you would embed the image bytes directly. The rest of the RAG system, including similarity search and result presentation, would work identically because all embeddings exist in the same vector space.

The embedding function for text queries uses Gemini's text embedding capabilities. This creates query vectors that can be compared directly against our image embeddings.

```python
def embed_text_with_gemini(content):
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=[content],
    )
    return np.array(result.embeddings[0].values)
```

The search function implements the retrieval logic. It embeds the query, calculates cosine similarity against all indexed embeddings, and returns the top results. This demonstrates the core RAG pattern where semantic similarity in the shared embedding space drives retrieval.

```python
def search_multimodal(query_text, vector_index, top_k=3):
    query_embedding = embed_text_with_gemini(query_text)
    
    embeddings = [doc["embedding"] for doc in vector_index]
    similarities = cosine_similarity([query_embedding], embeddings).flatten()
    
    top_indices = np.argsort(similarities)[::-1][:top_k]
    
    results = []
    for idx in top_indices:
        results.append({**vector_index[idx], "similarity": similarities[idx]})
    
    return results
```

Testing this system with different queries reveals its capabilities. Asking about "the architecture of the transformer neural network" correctly retrieves pages from the "Attention Is All You Need" paper. The system finds the relevant technical content even though our index mixes standard images with document pages.

Querying for "a kitten with a robot" successfully retrieves the image of a robot and kitten from our test set. The multimodal nature of the embeddings enables this cross-modal retrieval where a text description finds a matching image.

These examples demonstrate the power of treating all content as images in a unified embedding space. Adding new document types becomes trivial since everything processes as images. The same index that holds photographs can contain technical diagrams, charts, tables, and text-heavy pages. The retrieval system doesn't need to know the difference.

This implementation, while simplified, captures the essential patterns of production multimodal RAG systems. The vector database would be replaced with Milvus, Pinecone, or a similar system optimized for large-scale similarity search. The description step would be eliminated in favor of native multimodal embeddings. The core principle of embedding visual content directly and retrieving based on semantic similarity would remain unchanged.

The natural next step involves connecting this retrieval capability to an agent system. Rather than manually calling the search function, we can expose it as a tool that an agent can use autonomously. This creates a multimodal agentic RAG system that combines the reasoning capabilities of ReAct agents with the visual understanding of multimodal embeddings.

## Building Multimodal AI Agents

The RAG system from the previous section provides a foundation for more sophisticated applications. By exposing the multimodal search functionality as a tool, we can integrate it into agent systems that reason about when and how to use visual information. This creates agents that can work with images, documents, and text in a unified way.

Multimodal capabilities enhance agents in several ways. The reasoning LLM behind the agent can accept multimodal inputs and outputs directly. Retrieval tools can search across images, documents, and text using the same embedding space. Additional tools might access external multimodal resources like company documents, screenshots, audio files, or video content.

Our example demonstrates the first two capabilities. We create a ReAct agent using LangGraph's `create_react_agent()` function and connect our `search_multimodal` RAG tool. The agent can reason about visual queries and use the retrieval tool to find relevant images or document pages.

The system prompt guides the agent's behavior, emphasizing the importance of using multimodal search for queries involving visual elements. This helps the agent understand when to call the search tool versus relying on its internal knowledge.

```python
def build_react_agent():
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
```

Testing this agent with the query "what color is my kitten?" demonstrates the complete system working together. The agent reasons that it needs to search for visual information, calls the multimodal search tool, receives the relevant image and description, and provides a final answer identifying the kitten as a gray tabby.

The intermediate steps show the ReAct pattern in action. The agent first thinks about the visual nature of the query, then acts by calling the search tool, observes the results, and finally reasons to produce the answer. This demonstrates how multimodal retrieval integrates naturally into agent workflows.

The LangGraph implementation provides the agent infrastructure that we will explore in much greater detail in Part 2 of this course. For now, the important concept is that our RAG tool becomes just another capability that the agent can use when appropriate. The same patterns extend to other multimodal tools, whether for deep research, accessing company documents through MCP servers, analyzing screenshots, or processing audio and video content.

This example completes the foundation we have built throughout Part 1 of the course. We started with understanding the difference between workflows and agents, explored context engineering and structured outputs, examined tool use and reasoning patterns, and now we have added multimodal capabilities to the mix. These concepts work together to create AI systems that can process and reason about the rich, multimodal data that exists in real organizations.

The techniques you have learned apply far beyond this simple demonstration. Production systems combine these approaches in sophisticated ways. Agents use multimodal retrieval to access company documents, analyze images and screenshots, process audio recordings, and integrate information across all these modalities. The same principles scale to video understanding, audio processing, and other data types.

This foundation prepares you for Part 2 of the course, where we will build a complete research and writing agent system. The multimodal capabilities you learned here will play a crucial role in that project. The research agent will need to process various document types, including PDFs with complex layouts, while the writing agent will benefit from seeing the original visual context rather than text-only summaries.

The complete picture of modern AI engineering includes all these elements working together. Context engineering ensures the right information reaches each component. Structured outputs enable reliable data flow between steps. Tools and actions allow agents to interact with external systems. Memory provides continuity across interactions. Multimodal processing handles the rich data types that exist in the real world.

As you continue through the course, these concepts will connect and reinforce each other. The simple examples from early lessons become building blocks for the sophisticated systems we will construct later. Each new capability builds upon the foundations established in previous lessons.

The journey from basic LLM calls to production AI systems requires mastering all these techniques. Context engineering, structured outputs, tool use, reasoning patterns, memory management, retrieval systems, and multimodal processing work together to create applications that solve real problems reliably and efficiently.

The next part of the course will put these concepts into practice through a substantial project. You will build interconnected agents that research topics, analyze information across multiple modalities, and produce high-quality written content. The multimodal techniques from this lesson will prove essential for handling the diverse data types that real research involves.

The skills you develop throughout this course will serve you well beyond any specific project or framework. Understanding these fundamental patterns enables you to design AI systems that work with the complexity of real-world data and requirements. Whether you build research agents, document analysis systems, customer service applications, or entirely new categories of AI products, the principles remain the same.

The field continues evolving rapidly. New models, architectures, and techniques emerge regularly. The foundational understanding you build here will help you evaluate and adopt these advances effectively. Context engineering, in particular, will remain relevant even as specific models and tools change. The challenge of providing the right information to AI systems in the right format persists across technological generations.

Your ability to build reliable, efficient, and capable AI systems depends on mastering these core concepts. The combination of theoretical understanding and practical implementation experience creates the foundation for success in AI engineering. As you continue through the course and apply these concepts to increasingly complex projects, you will develop the intuition and skills necessary to tackle real-world AI challenges with confidence.

The journey from understanding individual components to building complete AI systems requires practice, experimentation, and careful attention to how different pieces interact. Each lesson builds upon the previous ones, creating a comprehensive toolkit for modern AI development. The multimodal capabilities you learned in this lesson complete the foundation established in the first ten lessons, preparing you for the more advanced topics and substantial project work that follows.

## Conclusion

This lesson completes the foundational portion of our course on AI agents and LLM workflows. We have covered the essential concepts that enable building sophisticated AI systems, from understanding the fundamental differences between workflows and agents to mastering context engineering, structured outputs, tool use, reasoning patterns, memory management, retrieval systems, and now multimodal processing.

The journey began with recognizing that AI applications have evolved beyond simple chatbots and basic RAG systems. Modern applications require sophisticated orchestration of multiple components working together. The choice between rigid workflows and autonomous agents depends on the specific requirements of each use case. Context engineering provides the framework for managing the complex information flows that these systems require.

Structured outputs create the essential bridge between the probabilistic world of LLMs and the deterministic requirements of software applications. Without reliable methods for extracting structured data from LLM responses, building production systems becomes significantly more difficult. The techniques we explored, from manual JSON parsing to native API integration with Pydantic models, provide the foundation for robust data flow throughout your AI applications.

The progression through tool use, reasoning patterns like ReAct, memory management, and retrieval systems built upon these foundations. Each new capability addressed specific limitations of simpler approaches. Tools enable agents to interact with external systems. Reasoning patterns provide systematic approaches to problem-solving. Memory creates continuity across interactions. Retrieval systems connect agents to domain-specific knowledge.

Multimodal processing completes this foundation by addressing the reality that most organizational data exists in formats beyond plain text. The shift from OCR-based approaches that normalize everything to text toward native multimodal processing preserves the rich information contained in images, documents, charts, and diagrams. This capability proves essential for applications that work with real enterprise content.

The practical examples throughout this lesson demonstrated these concepts in action. From simple image captioning and object detection to multimodal RAG systems and agent integration, we saw how theoretical concepts translate into working code. The progression from understanding limitations of traditional approaches to implementing sophisticated multimodal systems provides a template you can adapt to your own applications.

This foundation prepares you for the substantial project work in Part 2 of the course. You will build a complete research and writing agent system that leverages many of the techniques covered in these first eleven lessons. The research agent will need to process various document types, including PDFs with complex layouts and visual elements. The writing agent will benefit from seeing original visual context rather than text-only summaries. The multimodal capabilities you developed here will play a crucial role in making that system effective.

The concepts you have learned extend far beyond this specific course project. Context engineering, structured outputs, tool use, reasoning patterns, memory management, retrieval systems, and multimodal processing represent fundamental skills for modern AI engineering. As the field continues evolving, these core principles will remain relevant even as specific models and frameworks change.

The most successful AI applications combine these techniques thoughtfully rather than treating them as isolated capabilities. Context engineering ensures the right information reaches each component. Structured outputs enable reliable data flow between steps. Tools and actions allow interaction with external systems. Memory provides continuity and personalization. Retrieval connects to organizational knowledge. Multimodal processing handles the rich data types that exist in the real world.

Your ability to combine these capabilities effectively will determine your success as an AI engineer. The hands-on experience you gain throughout this course, implementing these concepts in working code and applying them to increasingly complex projects, will prove more valuable than theoretical knowledge alone. Each lesson builds upon the previous ones, creating a comprehensive toolkit for building production AI systems.

The path from understanding individual components to architecting complete AI solutions requires practice, experimentation, and careful attention to how different pieces interact. The course structure reflects this progression, moving from fundamental concepts to practical implementation to advanced project work. By the time you complete the capstone project in Part 4, you will have built multiple AI systems of increasing sophistication.

The AI engineering field rewards engineers who understand both the theoretical foundations and practical realities of building with these technologies. The combination of technical depth and system-level thinking that you develop through this course will serve you well regardless of which specific models or frameworks dominate in the future. The principles of effective context management, reliable data extraction, thoughtful tool design, systematic reasoning, memory architecture, retrieval optimization, and multimodal processing transcend any particular implementation.

As you continue through the remaining lessons, keep the complete picture in mind. Each new concept builds upon the foundation established in these first eleven lessons. The skills you develop here will compound as you tackle more complex challenges. The investment in understanding these fundamentals will pay dividends throughout your career as an AI engineer.

The most important lesson extends beyond any specific technique or model. Building effective AI systems requires thinking in terms of complete architectures rather than isolated components. The most successful applications combine multiple approaches thoughtfully, using workflows where predictability matters, agents where flexibility is essential, and hybrid approaches that leverage the strengths of both. Context engineering, structured outputs, and multimodal processing provide the foundation that makes these sophisticated systems possible.

Your journey through this course represents more than learning specific techniques. You are developing the architectural thinking and practical skills necessary to build AI systems that work reliably in production environments. The combination of theoretical understanding and hands-on implementation experience creates the foundation for success in this rapidly evolving field.

The next part of the course will put these concepts into practice through a substantial project. The research and writing agent system you will build incorporates many of the techniques covered in these foundational lessons. The experience of implementing these concepts in a realistic application will solidify your understanding and prepare you for the evaluation, observability, optimization, and deployment topics that follow in Part 3.

The complete set of skills developed across all four parts of this course will equip you to tackle real-world AI engineering challenges with confidence. From initial design decisions through production deployment and monitoring, you will understand how to build systems that are not only powerful but also reliable, efficient, and maintainable. This comprehensive approach distinguishes professional AI engineers from those who focus on individual components in isolation.

The field of AI engineering continues evolving at a remarkable pace. New models, architectures, and techniques emerge regularly. The foundational understanding you build here will help you evaluate these advances critically and adopt them effectively. Context engineering, in particular, will remain a crucial skill even as models become more capable and context windows expand. The challenge of providing the right information to AI systems in the right format at the right time persists across technological generations.

The investment you make in mastering these concepts will compound over time. Each new project builds upon the skills developed in previous work. The patterns you learn here will appear repeatedly as you tackle different applications and domains. The ability to design effective context management systems, implement reliable structured output pipelines, build sophisticated agent architectures, and process multimodal data effectively represents a powerful combination of capabilities for any AI engineer.

As artificial intelligence becomes increasingly integrated into organizational workflows and decision-making processes, the demand for engineers who can build reliable, production-ready AI systems continues to grow. The skills developed through this course position you to meet that demand effectively. Whether you build internal tools for your organization, develop customer-facing AI applications, or create entirely new categories of AI products, the principles and practices covered here will serve as your foundation.

The journey from understanding basic LLM calls to architecting sophisticated multi-agent systems requires dedication, practice, and systematic learning. This course provides the structure and hands-on experience necessary to make that journey successfully. Each lesson builds upon the previous ones, creating a comprehensive framework for modern AI development.

The most valuable outcome extends beyond any specific technique or implementation detail. You are developing the architectural thinking, practical skills, and systematic approach necessary to tackle complex AI engineering challenges with confidence. This combination of capabilities will serve you well throughout your career as the field continues to evolve and new opportunities emerge.

The foundation is now in place. The remaining lessons will build upon it, taking you from fundamental concepts to complete production systems. The journey continues, but you now possess the essential understanding required to navigate the complex landscape of modern AI engineering successfully.

## References

- [1] Ntinopoulos, V., Biefer, H. R. C., Tudorache, I., Papadopoulos, N., Odavic, D., Risteski, P., Haeussler, A., & Dzemali, O. (2025). Large language models for data extraction from unstructured and semi-structured electronic health records: a multiple model performance evaluation. BMJ Health & Care Informatics, 32(1), e101139. https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/

- [2] Evaluation of LLM-based Strategies for the Extraction of Food Product Information from Online Shops. arXiv. https://arxiv.org/html/2506.21585v1

- [3] Team, S. (2024, August 29). Type Safety in Python: Pydantic vs. Data Classes vs. Annotations vs. TypedDicts. Speakeasy. https://www.speakeasy.com/blog/pydantic-vs-dataclasses

- [4] Validators approach in Python - Pydantic vs. Dataclasses. Codetain. https://codetain.com/blog/validators-approach-in-python-pydantic-vs-dataclasses/

- [5] Automating Knowledge Graphs with LLM Outputs. Prompts.ai. https://www.prompts.ai/en/blog-details/automating-knowledge-graphs-with-llm-outputs

- [6] Kelly, C. (2025, February 13). Structured Outputs: everything you should know. Humanloop. https://humanloop.com/blog/structured-outputs

- [7] Structured Outputs in vLLM: Guiding AI Responses. Red Hat Developer. https://developers.redhat.com/articles/2025/06/03/structured-outputs-vllm-guiding-ai-responses

- [8] Best practices for prompt engineering with the OpenAI API. OpenAI Help Center. https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api

- [9] Structured data response with Amazon Bedrock: Prompt Engineering and Tool Use. AWS Machine Learning Blog. https://aws.amazon.com/blogs/machine-learning/structured-data-response-with-amazon-bedrock-prompt-engineering-and-tool-use/

- [10] Structured output. Google AI for Developers. https://ai.google.dev/gemini-api/docs/structured-output

- [11] Solomon, M. (2020, March 27). TypedDict vs dataclasses in Python — Epic typing BATTLE! DEV Community. https://dev.to/meeshkan/typeddict-vs-dataclasses-in-python-epic-typing-battle-onb

- [12] AI Agents for Product Managers: Tools that work for you. Product School. https://productschool.com/blog/artificial-intelligence/ai-agents-product-managers

- [13] Performance. Pydantic. https://docs.pydantic.dev/latest/concepts/performance/

- [14] Sharma, A. (2024, October 10). When should I use function calling, structured outputs or JSON mode? Vellum AI Blog. https://www.vellum.ai/blog/when-should-i-use-function-calling-structured-outputs-or-json-mode

- [15] Structured Output in vertexAI BatchPredictionJob. Google Cloud Community. https://www.googlecloudcommunity.com/gc/AI-ML/Structured-Output-in-vertexAI-BatchPredictionJob/m-p/866640

- [16] Hacker News Discussion on Structured Output. https://news.ycombinator.com/item?id=41173223

- [17] Lost-in-the-Middle effect. Promptmetheus. https://promptmetheus.com/resources/llm-knowledge-base/lost-in-the-middle-effect

- [18] Accounts, L. (2025, July 28). Context engineering. LangChain Blog. https://blog.langchain.com/context-engineering-for-agents/

- [19] Context Engineering - What it is, and techniques to consider. LlamaIndex. https://www.llamaindex.ai/blog/context-engineering-what-it-is-and-techniques-to-consider

- [20] Chase, H. (2025, June 23). The rise of "context engineering". LangChain Blog. https://blog.langchain.com/the-rise-of-context-engineering/

- [21] Context Engineering. DataCamp. https://www.datacamp.com/blog/context-engineering

- [22] Mei, L., Yao, J., Ge, Y., Wang, Y., Bi, B., Cai, Y., Liu, J., Li, M., Li, Z., Zhang, D., Zhou, C., Mao, J., Xia, T., Guo, J., & Liu, S. (2025, July 17). A survey of context engineering for large language models. arXiv. https://arxiv.org/pdf/2507.13334

- [23] karpathy. (n.d.). X. https://x.com/karpathy/status/1937902205765607626

- [24] lenadroid. (n.d.). X. https://x.com/lenadroid/status/1943685060785524824

- [25] Elvis. (2025, July 5). Context Engineering Guide. AI Newsletter. https://nlp.elvissaravia.com/p/context-engineering-guide

- [26] What is Context Engineering? Pinecone. https://www.pinecone.io/learn/context-engineering/

- [27] Understanding Multimodal LLMs. Sebastian Raschka's Magazine. https://magazine.sebastianraschka.com/p/understanding-multimodal-llms

- [28] Vision Language Models. NVIDIA Glossary. https://www.nvidia.com/en-us/glossary/vision-language-models/

- [29] Multimodal Embeddings: An Introduction. Towards Data Science. https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f

- [30] Multi-modal ML with OpenAI's CLIP. Pinecone. https://www.pinecone.io/learn/series/image-search/clip/

- [31] ColPali: Efficient Document Retrieval with Vision Language Models. arXiv. https://arxiv.org/pdf/2407.01449v6

- [32] Image understanding with Gemini. Google AI for Developers. https://ai.google.dev/gemini-api/docs/image-understanding

- [33] Multimodal RAG with Colpali, Milvus and VLMs. Hugging Face Blog. https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag

- [34] Google Generative AI Embeddings. LangChain Documentation. https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/

- [35] LangGraph Quickstart. LangGraph Documentation. https://langchain-ai.github.io/langgraph/agents/agents/

- [36] Complex Document Recognition: OCR Doesn’t Work and Here’s How You Fix It. Hackernoon. https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it

- [37] What are some real-world applications of multimodal AI? Milvus AI Quick Reference. https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai

- [38] What Is Optical Character Recognition (OCR)? Roboflow Blog. https://blog.roboflow.com/what-is-optical-character-recognition-ocr/

- [39] The 8 best AI image generators in 2025. Zapier. https://zapier.com/blog/best-ai-image-generator/