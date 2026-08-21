# Stop Converting Documents to Text. You're Doing It Wrong.

When I first started building AI agents, I hit a frustrating wall. I was comfortable manipulating text, but the moment I had to integrate multimodal data, such as images, audio, and especially documents like PDFs, my elegant architectures turned into messy hacks. I spent weeks building complex pipelines that tried to force everything into text. I chained OCR engines to scrape PDFs, layout detection models to identify tables, and separate classifiers to handle images. It was a brittle, slow, and expensive solution that broke every time a document layout changed.

The breakthrough came when I realized I was solving the wrong problem. I did not need to convert documents to text. I needed to treat them as images. Once I understood that every PDF page is effectively an image and that modern LLMs can “see” just as well as they can read, the complexity vanished.

This shift is essential because real-world AI applications rarely exist in a text-only vacuum. Enterprise applications need to manipulate private data from warehouses and lakes that is inherently multimodal: financial reports with complex charts, technical diagrams, and building sketches. The old approach of normalizing everything to text is lossy. When you translate a complex diagram into text, you lose the spatial relationships, the colors, and the context. By processing data in its native format, we preserve this rich visual information, resulting in systems that are faster, cheaper, and significantly more performant.

Here is what we will cover:
- The limitations of traditional document processing.
- The foundations of how multimodal LLMs work.
- How to apply multimodal LLMs to images and PDFs.
- The basics of building multimodal RAG systems.
- A hands-on implementation of a multimodal RAG system.
- How to build a simple multimodal AI agent.

## Limitations of Traditional Document Processing

To understand the problem, let’s look at the limitations of traditional document processing for invoices, documentation, or reports. Previous approaches tried to normalize everything to text before passing it to an AI model. This has many flaws, as we lose a substantial amount of information during translation. For example, when encountering diagrams, charts, or sketches in a document, it is impossible to fully reproduce them in text.

The traditional workflow relies on a multi-step pipeline involving layout detection and Optical Character Recognition (OCR). This process typically includes loading the document, preprocessing it to remove noise, detecting the layout of different regions, and then using OCR for text and specialized models for other data structures like tables or charts.

```mermaid
flowchart LR
  %% Input Stage
  subgraph "Input"
    A["Load Document"]
  end

  %% Core Processing Stages
  subgraph "Core Processing"
    B["Document Preprocessing<br/>(e.g., noise removal)"]
    C["Layout Detection<br/>(text, diagrams, tables)"]
    D["OCR Models<br/>(text regions)"]
    E["Specialized Models<br/>(images, tables, charts)"]
  end

  %% Output Stage
  subgraph "Output"
    F["Output Structured Data<br/>(JSON/metadata)"]
  end

  %% Flow connections
  A --> B
  B --> C
  C -- "processes text regions" --> D
  C -- "processes non-text regions" --> E
  D -- "generates" --> F
  E -- "generates" --> F

  %% Visual grouping
  classDef boundary stroke-dasharray:3,3
  classDef process stroke-width:2px
  class A,F boundary
  class B,C,D,E process
```
Image 1: A flowchart illustrating the traditional document processing workflow.

This workflow has too many moving pieces, making the system rigid, slow, and fragile. If a document contains a chart type we do not have a model for, the pipeline fails. Performance is also a major challenge. Errors compound at each stage, and even advanced OCR engines struggle with handwritten text, poor scans, or complex layouts like nested tables and building sketches [[9]](https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it), [[11]](https://www.llamaindex.ai/blog/olmocr-bench-review-insights-and-pitfalls-on-an-ocr-benchmark). Traditional OCR accuracy, which can be 88-94% on simple layouts, drops significantly on complex documents or degraded scans [[1]](https://www.llamaindex.ai/blog/ocr-accuracy).

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2dc40f3-dc13-486e-853d-8404368f4d8d_1616x1000.png
Image 2: A building sketch showing a crawl space vent diagram, illustrating the complexity of layouts that classic OCR systems struggle to interpret. (Source [Vectorize.io](https://vectorize.io/blog/multimodal-rag-patterns))

This approach might work for highly specialized applications, but it does not scale in a world of flexible and fast AI agents. Modern AI solutions use multimodal LLMs that can directly interpret text, images, or PDFs as native input, completely bypassing this brittle OCR workflow. Thus, let’s understand how they work.

## Foundations of Multimodal LLMs

To use LLMs with images and documents, you need an intuition of how multimodality works. You do not need to understand every research detail, but knowing the architecture helps you deploy, optimize, and monitor them. There are two common approaches to building multimodal LLMs: the Unified Embedding Decoder Architecture and the Cross-modality Attention Architecture [[1]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms).

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76f50b57-2585-4cb8-8dda-eea5b5f81c03_1456x854.jpeg
Image 3: The two main approaches to developing multimodal LLM architectures. (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

### Unified Embedding Decoder Architecture

In this approach, we encode the text and image separately, concatenate their embeddings into a single vector, and pass the resulting vector to the LLM. This requires a vision encoder to map the image into the same vector space as the text so the LLM can process both modalities together [[1]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms).

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0979e82-2fb0-4f78-80c8-1395511e057f_1166x1400.jpeg
Image 4: Illustration of the unified embedding decoder architecture. (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

### Cross-modality Attention Architecture

In the second approach, instead of passing image embeddings with the text at the input, we inject them directly into the attention module of the LLM. We still need an image encoder to project the image into the same vector space as the text, but it is integrated deeper within the architecture [[1]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms).

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea1b9ee4-0d19-4c3c-89db-06e779653da2_1296x1338.jpeg
Image 5: An illustration of the Cross-Modality Attention Architecture approach. (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

### Image Encoders

Both architectures rely on image encoders. We can draw a parallel between text tokenization and image patching. Just as we split text into sub-word tokens, we split images into patches. These patches are then processed to create embeddings.

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a7104c0-3986-4aae-b918-06c393ff824c_1456x1154.jpeg
Image 6: Image tokenization and embedding (left) and text tokenization and embedding (right) side by side. (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

The output has the same structure as text embeddings, but the two must be aligned in the same vector space. This is achieved through a linear projection module. Popular image encoders like CLIP, OpenCLIP, and SigLIP use contrastive learning to align image and text representations, allowing for semantic comparisons between them [[3]](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/). This alignment is also what powers multimodal RAG.

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d4c837a-a3e5-4d60-97ce-c4d4faf4cf57_841x616.png
Image 7: Toy representation of multimodal embedding space. (Source [Multimodal Embeddings: An Introduction](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/))

### Trade-offs and Modern Landscape

The **Unified Embedding Decoder** is simpler to implement and often yields higher accuracy on OCR-related tasks. The **Cross-modality Attention** approach is more computationally efficient for high-resolution images. Hybrid approaches also exist to combine these benefits [[36]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms).

In 2025, most leading LLMs are multimodal, including open-source models like Llama 4 and Qwen3, and closed-source options like GPT-5 and Gemini 2.5 [[22]](https://medium.com/data-science-in-your-pocket/2025-the-year-ai-reasoning-models-took-over-a-month-by-month-review-of-frontier-breakthroughs-6ea2163f854f). It is also important to distinguish multimodal LLMs from diffusion models like Midjourney or Stable Diffusion. Diffusion models generate images from noise, while multimodal LLMs understand and can sometimes generate images but are architecturally different. In an agent workflow, diffusion models are typically used as tools, not as the reasoning model [[19]](https://arxiv.org/html/2409.14993v3).

Now that we understand how LLMs can directly process images or documents, let’s see how this works in practice.

## Applying Multimodal LLMs to Images and PDFs

Let’s write a few examples using Gemini to show some best practices when working with images and PDFs. There are three core ways to process multimodal data with LLMs:

1.  **Raw bytes:** The easiest way to work with LLMs, but data can be corrupted when stored in most databases, which interpret the input as text instead of bytes. This method is best for one-off API calls without storage.
2.  **Base64:** Encodes raw bytes as strings, allowing you to store images or documents in a database without corruption. The downside is a file size increase of approximately 33%.
3.  **URLs:** The standard for enterprise scenarios where data is stored in a data lake like AWS S3 or GCP Buckets. The LLM downloads the media directly, reducing network latency for your application.

Now, let's dig into the code.

1.  First, we display a sample image.

    https://github.com/towardsai/course-ai-agents/raw/dev/lessons/11_multimodal/images/image_1.jpeg
    Image 8: The sample image of a robot and a kitten used in the code examples.

2.  We can process the image as **raw bytes**. We use the `WEBP` format because it is efficient. The following code loads the image and asks the LLM to generate a caption.
    ```python
    def load_image_as_bytes(
        image_path: Path, format: Literal["WEBP", "JPEG", "PNG"] = "WEBP", max_width: int = 600, return_size: bool = False
    ) -> bytes | tuple[bytes, tuple[int, int]]:
        """
        Load an image from file path and convert it to bytes with optional resizing.
        """
        # ... (implementation from notebook)
    
    image_bytes = load_image_as_bytes(image_path=Path("images") / "image_1.jpeg", format="WEBP")
    
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
    ```
    It outputs:
    ```text
    This striking image features a massive, dark metallic robot, its powerful form detailed with intricate circuit patterns on its head and piercing red glowing eyes...
    ```

3.  We can also process the image as a **Base64 encoded string**. The logic is similar, but we encode the bytes first.
    ```python
    def load_image_as_base64(
        image_path: Path, format: Literal["WEBP", "JPEG", "PNG"] = "WEBP", max_width: int = 600, return_size: bool = False
    ) -> str:
        """
        Load an image and convert it to base64 encoded string.
        """
        # ... (implementation from notebook)
    
    image_base64 = load_image_as_base64(image_path=Path("images") / "image_1.jpeg", format="WEBP")
    
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[
            types.Part.from_bytes(data=image_base64, mime_type="image/webp"),
            "Tell me what is in this image in one paragraph.",
        ],
    )
    ```
    The Base64 string is about 33% larger than the raw bytes, but it prevents data corruption in databases.

4.  For **public URLs**, Gemini's `url_context` tool can automatically parse web pages, PDFs, and images.
    ```python
    response = client.models.generate_content(
        model=MODEL_ID,
        contents="Based on the provided paper as a PDF, tell me how ReAct works: https://arxiv.org/pdf/2210.03629",
        config=types.GenerateContentConfig(tools=[{"url_context": {}}]),
    )
    ```
    It outputs:
    ```text
    ReAct is a novel paradigm for large language models (LLMs) that combines reasoning (Thought) and acting (Action) in an interleaved manner...
    ```

5.  For **private URLs** from data lakes like GCS, you can pass the URI directly, assuming the LLM has the correct permissions.
    ```python
    # Mocked example
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[
            types.Part.from_uri(uri="gs://gemini-images/image_1.jpeg", mime_type="image/webp"),
            "Tell me what is in this image in one paragraph.",
        ],
    )
    ```

6.  Let's try a more complex task: **Object Detection**. We use Pydantic to define the output structure, a concept we covered in Lesson 4.
    ```python
    from pydantic import BaseModel, Field
    
    class BoundingBox(BaseModel):
        ymin: float
        xmin: float
        ymax: float
        xmax: float
        label: str = Field(...)
    
    class Detections(BaseModel):
        bounding_boxes: list[BoundingBox]
    
    prompt = """
    Detect all of the prominent items in the image. 
    The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000.
    Also, output the label of the object found within the bounding box.
    """
    
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Detections,
    )
    
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[
            types.Part.from_bytes(data=image_bytes, mime_type="image/webp"),
            prompt,
        ],
        config=config,
    )
    ```
    The model returns structured JSON with bounding box coordinates, which can then be visualized on the image.

    https://github.com/towardsai/course-ai-agents/raw/dev/lessons/11_multimodal/images/image_1_detection.png
    Image 9: The output of the object detection call, with bounding boxes for the kitten and robot.

7.  The process for **PDFs** is nearly identical. We can load a PDF as bytes and ask the model for a summary.
    ```python
    pdf_bytes = (Path("pdfs") / "attention_is_all_you_need_paper.pdf").read_bytes()
    
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[
            types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf"),
            "What is this document about? Provide a brief summary of the main topics.",
        ],
    )
    ```
    It outputs:
    ```text
    This document introduces the **Transformer**, a novel neural network architecture designed for **sequence transduction tasks** (like machine translation).
    ```

8.  Finally, we can perform **Object Detection on PDF pages** by treating the page as an image. This is powerful for extracting diagrams or tables without traditional OCR. This concept was popularized by the ColPali paper, which demonstrated that modern Vision Language Models (VLMs) can retrieve documents more effectively by “looking” at them [[5]](https://arxiv.org/pdf/2407.01449v6).

    https://github.com/towardsai/course-ai-agents/raw/dev/lessons/11_multimodal/images/attention_is_all_you_need_1_detection.png
    Image 10: Object detection applied to a page of the "Attention Is All You Need" paper to extract the main diagram.

## Foundations of Multimodal RAG

One of the most common use cases for multimodal data is RAG. When working with large documents or images, stuffing everything into the context window is unfeasible due to increased latency, cost, and decreased performance. RAG becomes essential.

Let's explore a generic multimodal RAG architecture using images and text. The workflow involves an ingestion pipeline, where images are embedded and stored in a vector database, and a retrieval pipeline, where a user's text query is embedded to find the most similar images.

```mermaid
flowchart LR
  %% Ingestion Pipeline
  subgraph "Ingestion Pipeline"
    A["Embed Images<br/>(Text-Image Embedding Model)"]
    B["Load Embeddings to Vector Database"]
  end

  %% Retrieval Pipeline
  subgraph "Retrieval Pipeline"
    D["Embed User Text Query<br/>(Text-Image Embedding Model)"]
    E["Query Vector Database<br/>(Image Vector Index)"]
    F["Retrieve Top-K Similar Images<br/>(Cosine Distance)"]
  end

  %% Central Component
  C[(Vector Database)]

  %% Ingestion Flow
  A -- "generates image embeddings" --> B
  B -- "stores embeddings" --> C

  %% Retrieval Flow
  D -- "generates query embedding" --> E
  E -- "queries" --> C
  C -- "returns image vectors" --> E
  E -- "processes results" --> F

  %% Visual grouping
  classDef process stroke-width:2px
  classDef store stroke-dasharray:3,3
  class A,B,D,E,F process
  class C store
```
Image 11: A flowchart illustrating a generic multimodal RAG architecture using images and text.

For enterprise document RAG, a popular architecture as of 2025 is ColPali [[5]](https://arxiv.org/pdf/2407.01449v6). It bypasses the entire OCR pipeline by processing document pages directly as images. It uses a "bag-of-embeddings" approach, where each document image is broken into patches, and each patch gets its own embedding vector. At query time, a late interaction mechanism computes similarities between query tokens and document patches, allowing for fine-grained matching. This method is significantly faster and more accurate than traditional OCR pipelines, especially for documents with complex visual layouts [[5]](https://arxiv.org/pdf/2407.01449v6).

## Implementing Multimodal RAG

Let's implement a simple multimodal RAG system. We will populate an in-memory vector index with several images, including pages from the "Attention Is All You Need" paper treated as images. To keep it simple, we will not patch the images or use a late interaction mechanism.

```mermaid
flowchart LR
  %% Ingestion Process
  subgraph Ingestion
    A["Load Images/PDF Pages as Images"]
    B["Generate Image Descriptions<br/>(Gemini)"]
    C["Embed Descriptions<br/>(Text Embedding Model)"]
    D["Create In-Memory Vector Index"]
  end

  %% Retrieval Process
  subgraph Retrieval
    E["User Text Query"]
    F["Embed Query<br/>(Text Embedding Model)"]
    G["Search Vector Index<br/>(Cosine Similarity)"]
    H["Retrieve Top-K Results<br/>(Images/PDF Pages)"]
  end

  %% Data Flow
  A -- "images/pages" --> B
  B -- "descriptions" --> C
  C -- "embeddings" --> D

  E -- "text query" --> F
  F -- "query embedding" --> G
  G -- "retrieved items" --> H

  %% Relationship between Ingestion and Retrieval
  D -. "provides index for" .-> G

  %% Visual grouping
  classDef process stroke-width:2px
  classDef storage stroke-dasharray:3,3
  class A,B,C,E,F,G,H process
  class D storage
```
Image 12: A flowchart illustrating the multimodal RAG example, showing both the ingestion and retrieval processes.

1.  First, we define a function to create our vector index. Since the Gemini API used in this notebook does not support direct image embedding, we will use a workaround: generate a text description for each image with Gemini and then embed that description using a text embedding model. In a production system with a true multimodal embedding model (like Voyage, Cohere, or Google's models on Vertex AI), you would embed the image bytes directly.
    ```python
    def create_vector_index(image_paths: list[Path]) -> list[dict]:
        """
        Create embeddings for images by generating descriptions and embedding them.
        """
        vector_index = []
        for image_path in image_paths:
            image_bytes = load_image_as_bytes(image_path, format="WEBP", return_size=False)
            image_description = generate_image_description(image_bytes)
    
            # In production, you would embed image_bytes directly with a multimodal model
            image_embedding = embed_text_with_gemini(image_description)
    
            vector_index.append(
                {
                    "content": image_bytes,
                    "filename": image_path,
                    "description": image_description,
                    "embedding": image_embedding,
                }
            )
        return vector_index
    ```

2.  Next, we define a search function that takes a text query, embeds it, and finds the most similar images in our index using cosine similarity.
    ```python
    from sklearn.metrics.pairwise import cosine_similarity
    
    def search_multimodal(query_text: str, vector_index: list[dict], top_k: int = 3) -> list[Any]:
        """
        Search for most similar documents to query.
        """
        query_embedding = embed_text_with_gemini(query_text)
        if query_embedding is None:
            return []
    
        embeddings = [doc["embedding"] for doc in vector_index]
        similarities = cosine_similarity([query_embedding], embeddings).flatten()
    
        top_indices = np.argsort(similarities)[::-1][:top_k]
        results = [{**vector_index[idx], "similarity": similarities[idx]} for idx in top_indices]
        return results
    ```

3.  Let's test it with a query about the Transformer architecture.
    ```python
    query = "what is the architecture of the transformer neural network?"
    results = search_multimodal(query, vector_index, top_k=1)
    ```
    The system correctly retrieves the image of the Transformer model architecture from the paper, demonstrating its ability to connect a text query to a relevant visual diagram.

    https://github.com/towardsai/course-ai-agents/raw/dev/lessons/11_multimodal/images/attention_is_all_you_need_1.jpeg
    Image 13: The retrieved image for the query "what is the architecture of the transformer neural network?".

## Building Multimodal AI Agents

To take this a step further, we can integrate our RAG function into a ReAct agent as a tool. This combines many of the skills we have learned so far, including structured outputs, tools, ReAct, and RAG. The agent will use the `multimodal_search_tool` to find relevant images based on a user's question and then reason about the retrieved content to provide an answer.

```mermaid
flowchart LR
  %% User interaction
  UserQuery["User Query"]

  %% Agent Core
  subgraph Agent["ReAct Agent (LangGraph)"]
    Reasoning["Reasoning"]
    Act["Act"]
    FinalAnswer["Final Answer"]
  end

  %% Search & Retrieval
  subgraph SearchRetrieval["Search & Retrieval"]
    MultimodalSearchTool["Multimodal Search Tool"]
    EmbedsQuery["Embeds Query"]
    SearchesVectorDatabase["Searches Vector Database"]
    RetrieveMultimodalContent["Retrieve Multimodal Content<br/>(images, PDF pages, text)"]
  end

  %% Data Store
  subgraph DataStore["Data Store"]
    VectorDatabase["Vector Database<br/>(persistent store for multimodal embeddings)"]
  end

  %% Primary data flows
  UserQuery -- "initiates" --> Reasoning
  Reasoning -- "decides" --> Act
  Act -- "calls (if search needed)" --> MultimodalSearchTool
  MultimodalSearchTool -- "processes" --> EmbedsQuery
  EmbedsQuery -- "queries" --> SearchesVectorDatabase
  SearchesVectorDatabase -- "retrieves from" --> VectorDatabase
  VectorDatabase -- "provides content to" --> SearchesVectorDatabase
  SearchesVectorDatabase -- "returns" --> RetrieveMultimodalContent
  RetrieveMultimodalContent -- "as Observation" --> Reasoning
  Reasoning -- "produces" --> FinalAnswer

  %% Indirect / supporting relationships
  VectorDatabase -. "stores embeddings" .-> EmbedsQuery

  %% Visual grouping
  classDef store stroke-dasharray:3,3
  classDef exec stroke-width:2px
  class VectorDatabase store
  class Reasoning,Act,MultimodalSearchTool,EmbedsQuery,SearchesVectorDatabase,RetrieveMultimodalContent,FinalAnswer exec
```
Image 14: A flowchart illustrating a multimodal ReAct Agent with RAG functionality.

1.  We define the `multimodal_search_tool` using LangChain's `@tool` decorator, which wraps our `search_multimodal` function.
    ```python
    from langchain_core.tools import tool
    
    @tool
    def multimodal_search_tool(query: str) -> dict[str, Any]:
        """
        Search through a collection of images and their text descriptions to find relevant content.
        """
        results = search_multimodal(query, vector_index, top_k=1)
        if not results:
            return {"role": "tool_result", "content": "No relevant content found."}
        
        result = results[0]
        content = [
            {"type": "text", "text": f"Image description: {result['description']}"},
            types.Part.from_bytes(data=result["content"], mime_type="image/jpeg"),
        ]
        return {"role": "tool_result", "content": content}
    ```

2.  We create a ReAct agent using LangGraph's `create_react_agent`, providing it with our new tool and a system prompt that guides its behavior.
    ```python
    from langgraph.prebuilt import create_react_agent
    from langchain_google_genai import ChatGoogleGenerativeAI
    
    def build_react_agent() -> Any:
        system_prompt = """You are a helpful AI assistant that can search through images and text to answer questions..."""
        agent = create_react_agent(
            model=ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.1),
            tools=[multimodal_search_tool],
            prompt=system_prompt,
        )
        return agent
    
    react_agent = build_react_agent()
    ```

3.  Finally, we invoke the agent with a question. The agent reasons that it needs to use the search tool, calls it with a relevant query ("my kitten"), receives the image and its description, and then uses that context to answer the user's question.
    ```python
    test_question = "what color is my kitten?"
    response = react_agent.invoke(input={"messages": test_question})
    ```
    It outputs:
    ```text
    Based on the image, your kitten is a gray tabby. It has soft, short gray fur with darker tabby stripe patterns.
    ```

## Conclusion

Working with multimodal data is a fundamental skill for AI engineers. Modern AI applications rarely exist in a text-only vacuum; they must interact with the complex, visual, and auditory reality of the world. In this lesson, we moved away from the unstable, multi-step OCR pipelines of the past and learned that modern LLMs can natively process images and documents, preserving rich context that was previously lost.

This concludes the first part of our course on the foundations of AI Engineering. You now have the foundational blocks to build production-ready AI systems. In Part 2, we will move from theory to practice and begin building our central course project: an interconnected research and writing agent system. We will start with a deep dive into agentic design patterns and a look at modern frameworks like LangGraph.

## References

- [1] Raschka, S. (2024, October 21). Understanding multimodal LLMS. *Sebastian Raschka*. [https://magazine.sebastianraschka.com/p/understanding-multimodal-llms](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms)
- [2] Vision language models. (n.d.). *NVIDIA*. [https://www.nvidia.com/en-us/glossary/vision-language-models/](https://www.nvidia.com/en-us/glossary/vision-language-models/)
- [3] Talebi, S. (2024, November 13). Multimodal embeddings: An introduction. *Medium*. [https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/)
- [4] Multi-modal ML with OpenAI’s CLIP. (n.d.). *Pinecone*. [https://www.pinecone.io/learn/series/image-search/clip/](https://www.pinecone.io/learn/series/image-search/clip/)
- [5] Fostiropoulos, I., et al. (2024). ColPali: Efficient Document Retrieval with Vision Language Models. *arXiv*. [https://arxiv.org/pdf/2407.01449v6](https://arxiv.org/pdf/2407.01449v6)
- [6] Image understanding. (n.d.). *Google AI for Developers*. [https://ai.google.dev/gemini-api/docs/image-understanding](https://ai.google.dev/gemini-api/docs/image-understanding)
- [7] Multimodal RAG with Colpali, Milvus and VLMs. (n.d.). *Hugging Face*. [https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag](https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag)
- [8] Google Generative AI Embeddings. (n.d.). *LangChain*. [https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/](https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/)
- [9] Complex Document Recognition: OCR Doesn’t Work and Here’s How You Fix It. (n.d.). *HackerNoon*. [https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it](https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it)
- [10] What are some real-world applications of multimodal AI? (n.d.). *Milvus*. [https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai](https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai)
- [11] Liu, J. (2025, February 24). OlmOCR-bench review: Insights and pitfalls on an OCR benchmark. *LlamaIndex*. [https://www.llamaindex.ai/blog/olmocr-bench-review-insights-and-pitfalls-on-an-ocr-benchmark](https://www.llamaindex.ai/blog/olmocr-bench-review-insights-and-pitfalls-on-an-ocr-benchmark)
- [12] Vectorize.io. (2024, October 26). Multimodal RAG Patterns. *Vectorize.io Blog*. [https://vectorize.io/blog/multimodal-rag-patterns](https://vectorize.io/blog/multimodal-rag-patterns)
- [13] What Is Optical Character Recognition (OCR)?. (n.d.). *Roboflow*. [https://blog.roboflow.com/what-is-optical-character-recognition-ocr/](https://blog.roboflow.com/what-is-optical-character-recognition-ocr/)
- [14] The 8 best AI image generators in 2025. (n.d.). *Zapier*. [https://zapier.com/blog/best-ai-image-generator/](https://zapier.com/blog/best-ai-image-generator/)
- [15] Multimodal Embeddings: An Introduction. (n.d.). *YouTube*. [https://www.youtube.com/watch?v=YOvxh_ma5qE](https://www.youtube.com/watch?v=YOvxh_ma5qE)
- [16] LangGraph quickstart. (n.d.). *LangChain*. [https://langchain-ai.github.io/langgraph/agents/agents/](https://langchain-ai.github.io/langgraph/agents/agents/)
- [17] Wang, X., et al. (2025). Multi-modal Generative AI: Multi-modal LLMs, Diffusions, and the Unification. *arXiv*. [https://arxiv.org/html/2409.14993v3](https://arxiv.org/html/2409.14993v3)
- [18] Fostiropoulos, I., et al. (2024). ColPali: Efficient Document Retrieval with Vision Language Models. *arXiv*. [https://arxiv.org/pdf/2407.01449v6](https://arxiv.org/pdf/2407.01449v6)
- [19] Wang, X., et al. (2025). Multi-modal Generative AI: Multi-modal LLMs, Diffusions, and the Unification. *arXiv*. [https://arxiv.org/html/2409.14993v3](https://arxiv.org/html/2409.14993v3)
- [20] Evaluating Multimodal vs. Text-Based Retrieval for RAG with Snowflake Cortex. (n.d.). *Snowflake*. [https://www.snowflake.com/en/engineering-blog/arctic-agentic-rag-multimodal-pdf-retrieval/](https://www.snowflake.com/en/engineering-blog/arctic-agentic-rag-multimodal-pdf-retrieval/)
- [21] Financial analysis with ChatGPT: possibilities and limitations. (n.d.). *Konfuzio*. [https://konfuzio.com/en/chatgpt-financial-analysis/](https://konfuzio.com/en/chatgpt-financial-analysis/)
- [22] 2025: The Year AI Reasoning Models Took Over — A Month-by-Month Review of Frontier Breakthroughs. (n.d.). *Medium*. [https://medium.com/data-science-in-your-pocket/2025-the-year-ai-reasoning-models-took-over-a-month-by-month-review-of-frontier-breakthroughs-6ea2163f854f](https://medium.com/data-science-in-your-pocket/2025-the-year-ai-reasoning-models-took-over-a-month-by-month-review-of-frontier-breakthroughs-6ea2163f854f)
- [23] How to Choose the Best Embedding Model for RAG in 2026: 10 Models Benchmarked. (n.d.). *Milvus*. [https://milvus.io/blog/choose-embedding-model-rag-2026.md](https://milvus.io/blog/choose-embedding-model-rag-2026.md)
- [24] OCR Accuracy Explained: How to Improve It. (n.d.). *LlamaIndex*. [https://www.llamaindex.ai/blog/ocr-accuracy](https://www.llamaindex.ai/blog/ocr-accuracy)
- [25] Why traditional OCR fails for complex business documents. (n.d.). *Microsoft Learn*. [https://learn.microsoft.com/en-us/answers/questions/5668164/why-traditional-ocr-fails-for-complex-business-doc?page=1](https://learn.microsoft.com/en-us/answers/questions/5668164/why-traditional-ocr-fails-for-complex-business-doc?page=1)
- [26] OCR for Tables. (n.d.). *LlamaIndex*. [https://www.llamaindex.ai/blog/ocr-for-tables](https://www.llamaindex.ai/blog/ocr-for-tables)
- [27] Gemini consistently producing valid Pydantic responses. (n.d.). *Google AI*. [https://discuss.ai.google.dev/t/gemini-consistently-producing-valid-pydantic-responses/98992](https://discuss.ai.google.dev/t/gemini-consistently-producing-valid-pydantic-responses/98992)
- [28] Stop Converting Documents to Text. You're Doing It Wrong.. (n.d.). *Decoding AI*. [https://www.decodingai.com/p/stop-converting-documents-to-text](https://www.decodingai.com/p/stop-converting-documents-to-text)
- [29] LLM Output Parsing and Structured Generation with Pydantic. (n.d.). *Tetrate*. [https://tetrate.io/learn/ai/llm-output-parsing-structured-generation](https://tetrate.io/learn/ai/llm-output-parsing-structured-generation)
- [30] Structured Outputs with Multimodal Gemini. (n.d.). *Instructor*. [https://python.useinstructor.com/blog/2024/10/23/structured-outputs-with-multimodal-gemini/](https://python.useinstructor.com/blog/2024/10/23/structured-outputs-with-multimodal-gemini/)
- [31] Steering Large Language Models with Pydantic. (n.d.). *Pydantic*. [https://pydantic.dev/articles/llm-intro](https://pydantic.dev/articles/llm-intro)
- [32] Multimodal Semantic Search. (n.d.). *OpenSearch*. [https://opensearch.org/blog/multimodal-semantic-search/](https://opensearch.org/blog/multimodal-semantic-search/)
- [33] Multimodal AI Search for Business Applications. (n.d.). *Towards Data Science*. [https://towardsdatascience.com/multimodal-ai-search-for-business-applications-65356d011009/](https://towardsdatascience.com/multimodal-ai-search-for-business-applications-65356d011009/)
- [34] Joint Visual-Textual Embedding for Multimodal Style Search. (n.d.). *Amazon Science*. [https://assets.amazon.science/89/bf/661d950d4059930c8f1d2e449ac6/joint-visual-textual-embedding-for-multimodal-style-search.pdf](https://assets.amazon.science/89/bf/661d950d4059930c8f1d2e449ac6/joint-visual-textual-embedding-for-multimodal-style-search.pdf)
- [35] Combine Image and Text: How Multimodal Retrieval Transforms Search. (n.d.). *Zilliz*. [https://zilliz.com/blog/combine-image-and-text-how-multimodal-retrieval-transforms-search](https://zilliz.com/blog/combine-image-and-text-how-multimodal-retrieval-transforms-search)
- [36] NVLM: Open Frontier-Class Multimodal LLMs. (n.d.). *arXiv*. [https://arxiv.org/abs/2409.11402](https://arxiv.org/abs/2409.11402)
- [37] A Comprehensive Survey and Guide to Multimodal Large Language Models in Vision Language Tasks. (n.d.). *GitHub*. [https://github.com/cognitivetech/llm-research-summaries/blob/main/models-review/A-Comprehensive-Survey-and-Guide-to-Multimodal-Large-Language-Models-in-Vision-Language-Tasks.md](https://github.com/cognitivetech/llm-research-summaries/blob/main/models-review/A-Comprehensive-Survey-and-Guide-to-Multimodal-Large-Language-Models-in-Vision-Language-Tasks.md)
- [38] Multimodal AI Examples: How It Works, Real-World Applications, and Future Trends. (n.d.). *SmartDev*. [https://smartdev.com/multimodal-ai-examples-how-it-works-real-world-applications-and-future-trends/](https://smartdev.com/multimodal-ai-examples-how-it-works-real-world-applications-and-future-trends/)
- [39] What is a multimodal LLM?. (n.d.). *IBM*. [https://www.ibm.com/think/topics/multimodal-llm](https://www.ibm.com/think/topics/multimodal-llm)
- [40] Multimodal large language models for radiology. (n.d.). *PMC*. [https://pmc.ncbi.nlm.nih.gov/articles/PMC12479233/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12479233/)
- [41] The rise of multimodal large language models in healthcare. (n.d.). *Nature*. [https://www.nature.com/articles/s41598-025-98483-1](https://www.nature.com/articles/s41598-025-98483-1)
- [42] Exploring Multimodal LLMs: Text, Image, and Video Integration. (n.d.). *Spark*. [https://sparkco.ai/blog/exploring-multimodal-llms-text-image-and-video-integration](https://sparkco.ai/blog/exploring-multimodal-llms-text-image-and-video-integration)
- [43] Multimodal LLMs. (n.d.). *Emergent Mind*. [https://www.emergentmind.com/topics/multimodal-llms](https://www.emergentmind.com/topics/multimodal-llms)
- [44] Enhancing LLM Capabilities: The Power of Multimodal LLMs and RAG. (n.d.). *Towards AI*. [https://towardsai.net/p/l/enhancing-llm-capabilities-the-power-of-multimodal-llms-and-rag](https://towardsai.net/p/l/enhancing-llm-capabilities-the-power-of-multimodal-llms-and-rag)
- [45] Cross-Modal Transformers: Integrating Vision and Language in AI. (n.d.). *arXiv*. [https://arxiv.org/html/2411.06284v3](https://arxiv.org/html/2411.06284v3)
- [46] Multimodal Sentence Transformers. (n.d.). *Hugging Face*. [https://huggingface.co/blog/multimodal-sentence-transformers](https://huggingface.co/blog/multimodal-sentence-transformers)
- [47] Medical Imaging White Paper. (n.d.). *Lenovo*. [https://techtoday.lenovo.com/sites/default/files/2025-05/Medical%20Imaging%20White%20Paper%20NVIDIA%20and%20Lenovo.pdf](https://techtoday.lenovo.com/sites/default/files/2025-05/Medical%20Imaging%20White%20Paper%20NVIDIA%20and%20Lenovo.pdf)
- [48] Summarizing Text with Tables using Unified Text-to-Text Model. (n.d.). *IJCAI*. [https://www.ijcai.org/proceedings/2023/0581.pdf](https://www.ijcai.org/proceedings/2023/0581.pdf)
- [49] 10 real-world examples of AI in healthcare. (n.d.). *Philips*. [https://www.philips.com/a-w/about/news/archive/features/2022/20221124-10-real-world-examples-of-ai-in-healthcare.html](https://www.philips.com/a-w/about/news/archive/features/2022/20221124-10-real-world-examples-of-ai-in-healthcare.html)
- [50] Multimodal RAG with unstructured library and Multi-Vector retrieval. (n.d.). *LinkedIn*. [https://www.linkedin.com/posts/sayandey01_generativeai-llm-rag-activity-7412381316106760192-nFx3](https://www.linkedin.com/posts/sayandey01_generativeai-llm-rag-activity-7412381316106760192-nFx3)
- [51] Multimodal RAG template for PDFs. (n.d.). *Pathway*. [https://pathway.com/developers/templates/rag/multimodal-rag](https://pathway.com/developers/templates/rag/multimodal-rag)
- [52] MMCTAgent for multimodal reasoning over video/image collections. (n.d.). *LinkedIn*. [https://www.linkedin.com/posts/gauravagg_mmctagent-enables-multimodal-reasoning-over-activity-7413983881181339648--PyD](https://www.linkedin.com/posts/gauravagg_mmctagent-enables-multimodal-reasoning-over-activity-7413983881181339648--PyD)
- [53] Multimodal RAG Explained: From Text to Images and Beyond. (n.d.). *USAII*. [https://www.usaii.org/ai-insights/multimodal-rag-explained-from-text-to-images-and-beyond](https://www.usaii.org/ai-insights/multimodal-rag-explained-from-text-to-images-and-beyond)
- [54] Multimodal LLMs on Anyscale. (n.d.). *Anyscale*. [https://docs.anyscale.com/llm](https://docs.anyscale.com/llm)
- [55] The ultimate guide to the top large language models in 2025. (n.d.). *CodeDesign.ai*. [https://codedesign.ai/blog/the-ultimate-guide-to-the-top-large-language-models-in-2025/](https://codedesign.ai/blog/the-ultimate-guide-to-the-top-large-language-models-in-2025/)
- [56] Breakdown of 2025 flagship LLM architectures. (n.d.). *LinkedIn*. [https://www.linkedin.com/posts/progressivethinker_this-is-the-most-essential-breakdown-of-2025-activity-7376654335319117825-a5aD](https://www.linkedin.com/posts/progressivethinker_this-is-the-most-essential-breakdown-of-2025-activity-7376654335319117825-a5aD)
- [57] A Comparative Analysis of Flagship Open-Weight Coding LLMs. (n.d.). *Preprints.org*. [https://www.preprints.org/manuscript/202508.1904](https://www.preprints.org/manuscript/202508.1904)
- [58] Ultimate 2025 AI Language Models Comparison. (n.d.). *Promptitude*. [https://www.promptitude.io/post/ultimate-2025-ai-language-models-comparison-gpt5-gpt-4-claude-gemini-sonar-more](https://www.promptitude.io/post/ultimate-2025-ai-language-models-comparison-gpt5-gpt-4-claude-gemini-sonar-more)
- [59] Best Embedding Models for RAG. (n.d.). *GreenNode*. [https://greennode.ai/blog/best-embedding-models-for-rag](https://greennode.ai/blog/best-embedding-models-for-rag)
- [60] Best Embedding Model for RAG. (n.d.). *EagerWorks*. [https://eagerworks.com/blog/best-embedding-model-for-rag](https://eagerworks.com/blog/best-embedding-model-for-rag)
- [61] Top Embedding Models in 2025. (n.d.). *ArtSmart.ai*. [https://artsmart.ai/blog/top-embedding-models-in-2025/](https://artsmart.ai/blog/top-embedding-models-in-2025/)