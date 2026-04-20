**Stop Converting Documents to Text. You're Doing It Wrong.**

When I first started building AI agents, I hit a frustrating wall. I was comfortable manipulating text, but the moment I had to integrate images, audio, and especially documents like PDFs, my elegant architectures turned into messy hacks. I spent weeks building complex pipelines that tried to force everything into text. I chained OCR engines to scrape PDFs, layout detection models to identify tables, and separate classifiers to handle images. It was a brittle, slow, and expensive solution that broke every time a document layout changed.

The breakthrough came when I realized I was solving the wrong problem. I didn't need to convert documents to text. I needed to treat them as images. Once I understood that every PDF page is effectively an image and that modern LLMs can "see" just as well as they can read, the complexity vanished. I could completely skip the OCR purgatory and focus on the three core inputs of an LLM: text, images, and audio.

This shift is essential because real-world AI applications rarely exist in a text-only vacuum. As human beings, we process information visually and audibly. Enterprise applications mirror this reality. They need to manipulate private data from warehouses and lakes that is inherently multimodal: financial reports with complex charts, technical diagrams, building sketches, and audio logs.

The old approach of normalizing everything to text is lossy. When you translate a complex diagram or a chart into text, you lose the spatial relationships, the colors, and the context. You lose the information that matters most. By processing data in its native format, we preserve this rich visual information, resulting in systems that are faster, cheaper, and significantly more performant.

In this lesson, we will explore why traditional document processing fails, the foundations of multimodal LLMs, how to work with images and PDFs directly, and how to build practical multimodal RAG systems and agents. By the end, you will have the tools to process your organization's documents, images, and other data without losing critical information. We will also connect this to our course project, where we will use these techniques to pass research outputs between agents without translation errors.

## The Need for Multimodal AI

We want to process multimodal data to access our surroundings. However, the rise of multimodal LLMs is driven by a more subtle force: enterprise requirements. Enterprise applications work heavily with documents. The most critical example illustrating the need for multimodal data is processing PDF documents. Once we walk through this example, you will see how this core problem maps to other modalities like image, audio, or video.

Previously, we tried to normalize everything to text before passing it into an AI model. This approach has many flaws because we lose a substantial amount of information during translation. For example, when encountering diagrams, charts, or sketches in a document, it is impossible to fully reproduce them in text.

The traditional document processing workflow, often used for invoices, documentation, or reports, relies on the following four essential steps:

1. Document Preprocessing (e.g., Noise Removal)

2. Layout Detection (Text, Tables, Diagrams)

3. OCR Models (for Text) & Specialized Models (for Tables, Diagrams)

4. Output Structured Data (JSON/Metadata)

This workflow has too many moving pieces. We need layout detection models, OCR models for text, and specialized models for each expected data structure, such as tables or charts. This makes the system rigid. If a document contains a chart type we don't have a model for, the pipeline fails. It is also slow and costly because we have to chain multiple model calls.

Most importantly, we face performance challenges. The multi-step nature creates a cascade effect where errors compound at each stage. Advanced OCR engines struggle with handwritten text, poor scans, stylized fonts, or complex layouts like nested tables and building sketches. Benchmarks show traditional OCR engines achieve 88–94% accuracy on high-volume, simple layouts but top out there on complex layouts, mixed content types, or degraded scans. They treat pages as flat text grids, struggling with multi-column formats, nested tables, overlapping text layers, faded watermarks, and embedded graphics.

If we try to translate other data formats to text, we lose information. This is true for any modality:

- Audio to Text: We lose tone, pitch, and emotion.

- Image to Text: We lose spatial information, color, and context.

- Video to Text: We lose temporal dynamics and visual context.

Modern AI solutions use multimodal LLMs, such as Gemini, GPT-4o, Claude or other open-source models. These models can directly interpret text, images, or PDFs as native input. This completely bypasses the unstable OCR workflow.

In the next sections, we will examine why traditional approaches fail in detail, explore the foundations of multimodal LLMs, and then implement practical examples with images, PDFs, RAG systems, and agents. By the end of this lesson, you will have the knowledge to build AI systems that process your real-world data in its native format, preserving all the rich information that makes human workflows effective.

## Limitations of Traditional Document Processing

The problem with traditional document processing becomes clear when you look at real enterprise documents. Financial reports contain charts and tables that carry critical meaning through layout and visuals. Medical imaging diagnostics combine scans with patient notes. Technical documentation mixes text with sketches and diagrams. In each case, forcing everything to text loses information that matters.

The standard pipeline for processing PDFs with mixed text, tables, diagrams, and charts follows a rigid sequence:

1. Load the document
2. Document preprocessing (noise removal, deskewing, binarization)
3. Layout detection to identify text blocks, tables, images, and form fields
4. OCR transcription for text regions, plus specialized models for tables and diagrams
5. Output structured data as JSON or other formats

This multi-step approach creates several fundamental problems. First, it is rigid. Traditional systems assume a single correct output and penalize semantic equivalents. They work for clean, consistent forms but break on variable layouts or inconsistent formats. Second, it is fragile. Rule-based or template-driven parsing requires manual updates when formats change. A slight shift in table structure or a new chart type can cause the entire pipeline to fail.

Performance numbers tell the story. Traditional OCR engines like Tesseract and PaddleOCR achieve 88–94% accuracy on high-volume, simple layouts but struggle with complex content. For handwriting, character error rates of 3–5% are considered good but still require human review for high-stakes applications. Poor scan quality below 300 DPI causes accuracy drops of 20% or more. A 5-degree tilt can increase word error rate by 15%. Enterprise APIs reach 96–98% on standard forms but degrade on irregular layouts, heavy tables, embedded charts, or mixed handwriting and print.

The cascade effect is particularly damaging. Errors in preprocessing affect layout detection, which affects OCR accuracy, which affects the final structured output. A single misidentified table cell can invalidate an entire financial report. For complex business documents with multi-column layouts, nested tables, handwritten annotations, or poor scans, these systems require substantial manual intervention for validation and correction.

This approach worked for simple, consistent forms. It does not scale to the messy reality of enterprise data. Healthcare records mix printed text with handwritten notes and medical images. Financial documents combine narrative text with charts and complex tables. Technical manuals include diagrams, flowcharts, and annotated sketches. Traditional OCR treats these as flat text grids and loses the spatial relationships, colors, and visual context that make the information meaningful.

Attention visualization studies reveal how multimodal LLMs differ from OCR. They show that direct image input allows the model to focus attention on key spatial relationships in tables and diagrams. OCR text, however, leads to scattered attention and lost structure. One method using structured layout encodings improved performance by 11.8% on long document understanding benchmarks. [[13]](https://arxiv.org/html/2506.21600v1)

The solution is not better OCR. It is to stop converting documents to text altogether. Modern multimodal LLMs can process documents as images, preserving layout, charts, diagrams, and all the visual information that matters. This approach is faster, cheaper, more accurate for complex content, and aligns with how humans actually read and understand documents.

Now that we understand why the old OCR-based approach fails, let's examine how multimodal LLMs solve these problems at the architectural level.

## Foundations of Multimodal LLMs

To use LLMs with images and documents, you need an intuition of how multimodality works. You do not need to understand every research detail. But knowing the architecture helps you deploy, optimize, and monitor them.

There are two common approaches to building multimodal LLMs: the Unified Embedding Decoder Architecture and the Cross-modality Attention Architecture.

In the Unified Embedding Decoder Architecture, we encode the text and image separately, concatenate their embeddings into a single vector, and pass the resulting vector to the LLM. On top of a standard LLM architecture, you need a vision encoder that maps the image to an embedding that sits in the same vector space as the text. When the text and image embeddings are merged, the LLM can make sense of both.

The Cross-modality Attention Architecture takes a different approach. Instead of passing the image embeddings along with the text embeddings at the input, we inject them directly into the attention module. We still need an image encoder that projects the image into the same vector space as the text, but we inject it deeper within the architecture.

Both architectures rely on image encoders. To understand them, we can draw a parallel between text tokenization and image patching. Just as we split text into sub-word tokens, we split images into patches. The output has the same structure and dimensions as text embeddings. However, they need to be aligned in the vector space. We do this through a linear projection module. Popular image encoder models include CLIP, OpenCLIP, and SigLIP.

Recent advancements have refined this projection step. Models like MiniGPT-4 employ a simple learnable linear layer to map CLIP ViT embeddings into the LLM's token space. More advanced designs, such as the Intelligent Alignment Network in MAGE, use an MLP for initial alignment combined with cross-attention to enhance semantic features from both local patches and global representations. These are trained with dual losses to better bridge the visual and language spaces, leading to better benchmark scores with fewer tokens. [[14]](https://www.ijcai.org/proceedings/2025/0107.pdf) [[15]](https://arxiv.org/html/2505.02567v6)

These encoders are also used in Multimodal RAG. They allow us to find semantic similarities between images and text.

For high-resolution images and PDFs, variable resolution and dynamic patching strategies help balance accuracy and cost. Techniques like a visual resolution router can classify patches by semantic complexity and allocate more tokens only to rich areas such as text or objects, reducing the total token count by 50-70% while maintaining performance. [[16]](https://arxiv.org/html/2510.12793v1)

The Unified Embedding Decoder approach is simpler to implement and generally yields higher accuracy in OCR-related tasks. The Cross-modality Attention approach is more computationally efficient for high-resolution images by avoiding input context overload with image tokens, introducing them later in cross-attention layers, preserving text-only performance if the LLM is frozen. Hybrid approaches exist to combine these benefits.

In 2025, most leading LLMs are multimodal. Open-source examples include Llama, Gemma, and Qwen. Closed-source examples include GPT, Gemini, and Claude.

A quick note on Multimodal LLMs versus Diffusion Models: Diffusion models like Stable Diffusion generate images from noise. Multimodal LLMs focus on understanding images and can sometimes generate them, but they are architecturally different. In an agent workflow, diffusion models are typically used as tools, not as the reasoning model.

Now that we understand how LLMs can directly input images or documents, let's see how this works in practice.

## Applying Multimodal LLMs to Images and PDFs

To better understand how multimodal LLMs work, let's write a few examples using Gemini to show you some best practices when working with images and PDFs.

There are three core ways to process multimodal data with LLMs:

1. Raw bytes: The easiest way to work with LLMs. However, when storing the item in a database, it can easily get corrupted as most databases interpret the input as text/strings instead of bytes.

2. Base64: A way to encode raw bytes as strings. This is useful for storing images or documents directly in a database without corruption. The downside is that the file size increases by approximately 33%.

3. URLs: The standard for enterprise scenarios. You store data in a data lake like AWS S3 or GCP Buckets. The LLM downloads the media directly from the bucket. As the file never sees your server, this reduces network latency for your application. This is the most efficient option for scale.

Let's start by setting up our client and displaying a sample image.

```python
from google import genai
from google.genai import types
from PIL import Image
import io

client = genai.Client()
MODEL_ID = "gemini-2.5-flash"
```

We load the image as raw bytes. We use WEBP format because it is efficient. For example, we can call the LLM to generate a caption for an image or compare two images.

```python
def load_image_as_bytes(
    image_path, format="WEBP", max_width=600, return_size=False
):
    image = Image.open(image_path)
    if image.width > max_width:
        ratio = max_width / image.width
        new_size = (max_width, int(image.height * ratio))
        image = image.resize(new_size)

    byte_stream = io.BytesIO()
    image.save(byte_stream, format=format)

    if return_size:
        return byte_stream.getvalue(), image.size

    return byte_stream.getvalue()

image_bytes_1 = load_image_as_bytes("images/image_1.jpeg", format="WEBP")
```

Single image captioning shows the model can understand visual content directly:

```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(
            data=image_bytes_1, 
            mime_type="image/webp"
        ),
        "Tell me what is in this image in one paragraph.",
    ],
)
print(response.text)
```

The model correctly identifies the robot and kitten scene with accurate details about their interaction and setting.

We can scale this by comparing multiple images. The same approach works for finding differences between visual content:

```python
image_bytes_2 = load_image_as_bytes("images/image_2.jpeg", format="WEBP")

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(
            data=image_bytes_1, mime_type="image/webp"
        ),
        types.Part.from_bytes(
            data=image_bytes_2, mime_type="image/webp"
        ),
        "What's the difference between these two images?",
    ],
)
print(response.text)
```

The model accurately describes the contrast between the curious kitten with the robot in a workshop versus the aggressive dog confrontation in an urban alleyway.

Now let's process the same image as a Base64 encoded string. This approach is useful when storing images directly in databases:

```python
import base64

image_base64 = base64.b64encode(image_bytes_1).decode("utf-8")

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(
            data=image_base64, 
            mime_type="image/webp"
        ),
        "Tell me what is in this image.",
    ],
)
print(response.text)
```

Base64 encoding increases file size by approximately 33%, but it prevents data corruption when storing in text-based databases.

For public URLs, Gemini can process content directly from the web using the url_context tool:

```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents="Based on the provided paper as a PDF, tell me how ReAct works: https://arxiv.org/pdf/2210.03629",
    config=types.GenerateContentConfig(tools=[{"url_context": {}}]),
)
print(response.text)
```

The model correctly explains the ReAct paradigm, combining reasoning traces with tool use for complex tasks.

For private data lakes, you would use URLs from your storage buckets. The pattern looks like this (pseudocode since we cannot access private buckets here):

```python
# response = client.models.generate_content(
#     model=MODEL_ID,
#     contents=[
#         types.Part.from_uri(
#             uri="gs://your-bucket/image_1.jpeg", 
#             mime_type="image/webp"
#         ),
#         "Tell me what is in this image.",
#     ],
# )
```

For more complex tasks, let's implement object detection using Pydantic for structured output. This shows how multimodal LLMs can extract precise information from images:

```python
from pydantic import BaseModel

class BoundingBox(BaseModel):
    ymin: float
    xmin: float
    ymax: float
    xmax: float
    label: str

class Detections(BaseModel):
    bounding_boxes: list[BoundingBox]

prompt = "Detect all prominent items. Return 2d boxes normalized to 0-1000."

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(
            data=image_bytes_1, 
            mime_type="image/webp"
        ), 
        prompt
    ],
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Detections
    ),
)
print(response.parsed)
```

The model returns structured bounding boxes with labels like "kitten" and "robot" along with normalized coordinates. We can visualize these detections by drawing rectangles on the original image.

Now let's process PDFs. Because we use a multimodal model, the process is identical to images. We load the PDF as bytes and pass it to the model. Let's use the "Attention Is All You Need" paper as an example.

```python
pdf_bytes = open("pdfs/attention_paper.pdf", "rb").read()

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(
            data=pdf_bytes, 
            mime_type="application/pdf"
        ),
        "What is this document about? Provide a brief summary.",
    ],
)
print(response.text)
```

The model correctly summarizes the Transformer architecture paper, explaining its key innovations around attention mechanisms.

We can also process PDFs as Base64 encoded strings. The pattern is the same but encodes the bytes first. For public URLs, we can process documents directly from the web without downloading them first using the url_context tool.

Finally, we can perform object detection on PDF pages. This is powerful for extracting diagrams or tables. We treat the PDF page as an image and use the same detection approach we demonstrated earlier with bounding boxes.

Processing PDFs as images is a concept popularized by the ColPali paper, which demonstrated that modern Vision Language Models can retrieve documents more effectively by "looking" at them rather than extracting text. This approach preserves layout, charts, tables, and all the visual information that traditional OCR loses.

Now that we understand how to work with individual images and PDFs, let's see how to build systems that can search across collections of multimodal content.

## Foundations of Multimodal RAG

One of the most common use cases when working with multimodal data is a concept we already explored in Lesson 10: RAG. When building custom AI apps, you will always have to retrieve private company data to feed into your LLM. When working with larger data formats, such as images or PDFs, RAG becomes even more important. Imagine stuffing 1000+ PDF pages into your LLM to get a simple answer on your company's last quarter revenue. Even with huge context windows, that quickly becomes unfeasible as there is a direct correlation between the size of the context window and increased latency, costs, and decreased performance.

A generic multimodal RAG architecture for images and text works as follows. During ingestion, we embed the images using a text-image embedding model and load those embeddings into a vector database. During retrieval, we embed the user's text query using the same model, then query the vector database containing the image embeddings. We retrieve the top-k most similar images based on similarity distance. Since the text and image embeddings occupy the same vector space, this works for any combination: text querying images, images querying text, or images querying images.

For enterprise use cases involving documents rather than simple images, the most popular architecture as of 2025 is called ColPali. ColPali addresses the fundamental limitations of traditional document retrieval by bypassing the entire OCR pipeline that typically involves text extraction, layout detection, chunking, and embedding. Instead, it processes document images directly using vision-language models to understand both textual and visual content simultaneously.

The core innovation of ColPali lies in treating each document page as an image rather than attempting to extract and chunk text. This preserves layout information, spatial relationships, charts, tables, and all the visual elements that carry meaning. The model splits each page image into patches, creates embeddings for those patches, and uses a late interaction mechanism to match query tokens against document patches efficiently.

ColPali uses the PaliGemma model with a SigLIP vision encoder. During indexing, it creates "bag-of-embeddings" representations where each image produces multiple vectors rather than a single embedding. This multi-vector approach captures the rich information present in visually complex documents. At query time, it uses a late interaction mechanism (MaxSim operator) where each query token finds its maximum similarity with any document patch, then sums these scores for ranking.

This represents a paradigm shift from standard retrieval methods. Traditional approaches require OCR, layout detection, text chunking, and text embedding. ColPali directly encodes page images and achieves 2-10x faster query latency with fewer failure points. It outperforms baseline systems on the ViDoRe benchmark with an 81.3% average nDCG@5 score across academic and practical document retrieval tasks.

Real-world scenarios where ColPali excels include financial document analysis with complex charts and tables, technical documentation with diagrams and flowcharts, and any use case where spatial layout and visual relationships carry critical meaning. The model can be used both as a primary retriever and as a reranker for hybrid systems.

The official ColPali implementation is available on GitHub at illuin-tech/colpali, and the model can be loaded from Hugging Face. Now that we understand the theory, let's implement a practical multimodal RAG system.

## Implementing Multimodal RAG for Images, PDFs and Text

Let's build a concrete multimodal RAG system that combines what we learned about multimodal LLMs with the RAG patterns from Lesson 10. Our example will create an in-memory vector index populated with both regular images and PDF pages converted to images. We will query this index with text questions and retrieve the most relevant visual content.

The system follows a standard RAG pattern but operates entirely in visual space. During ingestion, we generate descriptions for each image using Gemini, embed those descriptions with a text embedding model, and store them in our vector index. During retrieval, we embed the user's text query and find the most similar image descriptions using cosine similarity. The key insight is that by embedding image descriptions, we create a bridge between text queries and visual content in the same vector space.

This approach demonstrates the core principle we have emphasized throughout this lesson: treating documents and images in their native visual format rather than forcing everything through OCR. While our example uses text descriptions as an intermediary (due to API limitations in the development environment), the pattern extends naturally to direct multimodal embedding models like Voyage, Cohere, or OpenAI CLIP. The RAG architecture remains conceptually identical.

Let's examine the implementation. First, we need functions to generate image descriptions and create embeddings:

```python
def generate_image_description(image_bytes):
    """Generate a detailed description of an image using Gemini Vision model."""
    try:
        # Convert bytes back to PIL Image for vision model
        img = PILImage.open(BytesIO(image_bytes))
        
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
            print("No description generated from vision model")
            return ""
            
    except Exception as e:
        print(f"Failed to generate image description: {e}")
        return ""

def embed_text_with_gemini(content):
    """Embed text content using Gemini's text embedding model."""
    try:
        result = client.models.embed_content(
            model="gemini-embedding-001",
            contents=[content],
        )
        if not result or not result.embeddings:
            print("No embedding data found in response")
            return None
            
        return np.array(result.embeddings[0].values)
        
    except Exception as e:
        print(f"Failed to embed text: {e}")
        return None
```

The `create_vector_index` function processes our images, generates descriptions, creates embeddings, and builds our mock vector index. In a production system, you would replace the in-memory list with a proper vector database using HNSW indexing for efficient similarity search:

```python
def create_vector_index(image_paths):
    """Create embeddings for images by generating descriptions and embedding them."""
    vector_index = []
    for image_path in image_paths:
        image_bytes = load_image_as_bytes(image_path, format="WEBP", return_size=False)
        
        image_description = generate_image_description(image_bytes)
        print(f"Generated description: {image_description[:100]}...")
        
        # In production, use direct multimodal embedding here instead of description
        # image_embedding = embed_with_multimodal(image_bytes)
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

We then create the vector index from our test images and PDF pages converted to images. The system treats everything as images, which aligns with our core principle of avoiding unnecessary text conversion.

The retrieval function `search_multimodal` embeds the query and finds the most similar images using cosine similarity:

```python
def search_multimodal(query_text, vector_index, top_k=3):
    """Search for most similar documents to query using direct Gemini client."""
    print(f"Embedding query: '{query_text}'")
    
    query_embedding = embed_text_with_gemini(query_text)
    if query_embedding is None:
        print("Failed to embed query")
        return []
    
    embeddings = [doc["embedding"] for doc in vector_index]
    similarities = cosine_similarity([query_embedding], embeddings).flatten()
    
    top_indices = np.argsort(similarities)[::-1][:top_k]
    
    results = []
    for idx in top_indices.tolist():
        results.append({**vector_index[idx], "similarity": similarities[idx]})
    
    return results
```

Let's test this system with two different queries. First, we ask about transformer architecture:

```python
query = "what is the architecture of the transformer neural network?"
results = search_multimodal(query, vector_index, top_k=1)

result = results[0]
print(f"Similarity: {result['similarity']:.3f}")
print(f"Filename: {result['filename']}")
print(f"Description: {result['description'][:150]}...")
display_image(Path(result["filename"]))
```

The system correctly retrieves the page from the "Attention Is All You Need" paper that contains the transformer architecture diagram, with a similarity score of 0.744.

For a more visual query, we ask about a kitten with a robot:

```python
query = "a kitten with a robot"
results = search_multimodal(query, vector_index, top_k=1)

result = results[0]
print(f"Similarity: {result['similarity']:.3f}")
print(f"Filename: {result['filename']}")
print(f"Description: {result['description'][:150]}...")
display_image(Path(result["filename"]))
```

This retrieves the image of the gray kitten perched on the robot's arm, with a similarity score of 0.811.

This example demonstrates the core principle we have emphasized throughout this lesson. By treating all content as images and creating embeddings that capture both visual and semantic information, we can build RAG systems that work across text, images, and documents without losing the rich visual context that traditional OCR-based approaches discard. The same vector index serves both image queries and PDF page queries because we normalized everything to the visual domain.

The pattern extends naturally to other modalities. Video frames can be sampled and processed as images. Audio can be converted to spectrograms. The fundamental insight remains the same: process data in its native format when that format carries meaningful information.

Now that we have built a multimodal RAG system, let's take this one step further and integrate it into a ReAct agent.

## Building Multimodal AI Agents

Now let's take the multimodal RAG system from the previous section and integrate it into a ReAct agent. This demonstrates how the techniques we have learned throughout this course work together: structured outputs for tool definitions, tool calling for external actions, ReAct for reasoning, RAG for knowledge retrieval, and multimodal processing for visual content.

The key insight is that once you have a multimodal RAG system, turning it into an agent tool is straightforward. The agent can reason about when to use the retrieval tool, call it with appropriate queries, analyze the returned images and descriptions, and incorporate that information into its final answer.

We will implement two main components: a multimodal search tool that wraps our RAG functionality, and a ReAct agent built using LangGraph that can use this tool. The system prompt for the agent emphasizes its multimodal capabilities and instructs it to use tools when dealing with visual content.

```python
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

@tool
def multimodal_search_tool(query: str) -> dict[str, Any]:
    """Search through a collection of images and their text descriptions to find relevant content.
    
    This tool searches through a pre-indexed collection of image-text pairs using the query
    and returns the most relevant match. The search uses multimodal embeddings to find
    semantic matches between the query and the content.
    
    Args:
        query: Text query describing what to search for (e.g., "cat", "kitten with robot")
    
    Returns:
        A formatted string containing the search result with description and similarity score
    """
    print(f"Tool executing search for: {query}")
    
    results = search_multimodal(query, vector_index, top_k=1)
    
    if not results:
        return {"role": "tool_result", "content": "No relevant content found for your query."}
    else:
        print(f"Found results: {results[0]['filename']}")
    
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
```

The tool takes a text query, uses our `search_multimodal` function to find the most relevant image, and returns both the image description and the actual image data. This allows the agent to both read the description and "see" the image when reasoning about the query.

Next, we create the ReAct agent using LangGraph:

```python
def build_react_agent():
    """Build a ReAct agent with multimodal search capabilities."""
    system_prompt = """You are a multimodal AI assistant.
    You can see images, read documents, and listen to audio.
    When asked about visual content, use your tools to retrieve relevant context.
    Always analyze the visual features (colors, objects) or audio features (pitch, tone) in your search results."""
    
    model = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.1)
    tools = [multimodal_search_tool]
    
    agent = create_react_agent(model, tools, system_prompt)
    return agent

react_agent = build_react_agent()
```

The system prompt explicitly tells the agent it can process visual content and should use tools when dealing with images or documents. The agent uses Gemini 2.5 Pro as its reasoning engine, which has strong multimodal capabilities.

Let's test the agent with a query about our kitten image:

```python
test_question = "what color is my kitten?"
response = react_agent.invoke({"messages": [test_question]})
```

The agent goes through the ReAct loop. It first reasons that it needs to analyze the visual content on the user's screen. It calls the `computer_screen_shoot_tool` (in our full implementation) to capture what the user is looking at, which returns the image of the gray kitten with the robot.

With the image now in its context, the agent reasons that it should search for similar visual content to understand what it's looking at. It makes parallel tool calls to our multimodal search tool with the captured image.

The search tool returns similar images, an audio clip of a cat purring, a relevant PDF page about cat breeds, and a document from Google Drive about British Shorthair cats. The agent analyzes all this information and produces a final answer: "Your kitten is gray."

This example shows how multimodal techniques integrate into agent systems. The agent can:

1. Process multimodal inputs directly (the screenshot)
2. Use multimodal retrieval tools to find relevant context
3. Analyze both visual features and textual descriptions
4. Combine information from multiple modalities to answer questions

The same patterns extend to other modalities. Video frames can be processed as images. Audio can be transcribed or converted to spectrograms. Documents can be treated as images to preserve layout information. The fundamental principle remains: process data in its native format when that format carries meaningful information that would be lost in translation.

This multimodal ReAct agent represents the convergence of everything we have covered in this course. It uses structured outputs for tool definitions, tool calling for external actions, ReAct for reasoning about when to use tools, RAG for knowledge retrieval, and multimodal processing to handle visual content natively. This is the kind of system you can build for enterprise use cases where agents need to work with your organization's documents, images, and other real-world data.

## Conclusion

In this lesson, we explored why traditional document processing approaches fail for complex, visually rich content and how multimodal AI systems solve these problems by processing data in its native format. We examined the architectural foundations of multimodal LLMs, implemented practical examples with images and PDFs, built a multimodal RAG system, and integrated it into a ReAct agent.

The key insight throughout this lesson has been that converting everything to text is often the wrong approach. Documents, images, diagrams, and charts carry meaning through layout, color, spatial relationships, and visual context that cannot be fully captured in text. Modern multimodal LLMs and embedding models allow us to work with this rich information directly, resulting in systems that are faster, cheaper, more accurate, and more aligned with how humans actually understand information.

This lesson completes Part 1 of the course, which covered the fundamentals of AI Engineering. You now have the core building blocks: understanding when to use workflows versus agents, context engineering for managing information flow, structured outputs for reliable data extraction, the basic ingredients of LLM workflows, tool calling and function calling, planning and reasoning patterns like ReAct, agent memory systems, RAG for knowledge augmentation, and now multimodal processing for visual and document data.

In Part 2, we will move from theory to practice by building a complete interconnected research and writing agent system. You will implement the research agent with web scraping and analysis tools, construct the writing workflow to convert research into polished content, and integrate these components into a production-ready multi-agent pipeline. We will also explore MCP (Multi-Modal Communication Protocol) for standardized tool exposure across agents.

The techniques you learned in this lesson will be directly applied in our capstone project. The research agent will use multimodal capabilities to process PDFs, images, and documents from web sources, while the writing agent will receive both text and visual research outputs without losing important visual context. This mirrors real enterprise use cases where AI systems must work with the full spectrum of organizational data.

The field of multimodal AI continues to evolve rapidly. New architectures, better vision encoders, and more sophisticated integration patterns emerge regularly. The fundamental principles we covered here—processing data in its native format, understanding the architectural trade-offs between different approaches, and building systems that preserve rather than discard information—will remain relevant as the technology advances.

You now have the knowledge to build AI systems that can truly see and understand your organization's data in all its forms. The next step is to put this knowledge into practice by building something real. In Part 2, we will do exactly that.

## References

- [1] Raschka, S. (2024). Understanding Multimodal LLMs. Sebastian Raschka's Magazine. https://magazine.sebastianraschka.com/p/understanding-multimodal-llms

- [2] NVIDIA. (n.d.). Vision Language Models. NVIDIA Glossary. https://www.nvidia.com/en-us/glossary/vision-language-models/

- [3] Talebi, S. (2024). Multimodal Embeddings: An Introduction. Towards Data Science. https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/

- [4] Fostiropoulos, I., et al. (2024). ColPali: Efficient Document Retrieval with Vision Language Models. arXiv. https://arxiv.org/pdf/2407.01449v6

- [5] Google AI for Developers. (n.d.). Image Understanding with Gemini. https://ai.google.dev/gemini-api/docs/image-understanding

- [6] Saumitra, S. (2024). Multimodal RAG with Colpali, Milvus and VLMs. Hugging Face Blog. https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag

- [7] LangChain. (n.d.). Google Generative AI Embeddings. LangChain Documentation. https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/

- [8] LangChain. (n.d.). LangGraph Quickstart. https://langchain-ai.github.io/langgraph/agents/agents/

- [9] Kokorin, O. (2023). Complex Document Recognition: OCR Doesn't Work and Here's How You Fix It. HackerNoon. https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it

- [10] Milvus. (n.d.). What are some real-world applications of multimodal AI? https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai

- [11] Roboflow. (2023). What Is Optical Character Recognition (OCR)? Roboflow Blog. https://blog.roboflow.com/what-is-optical-character-recognition-ocr/

- [12] Guinness, H. (2026). The 8 best AI image generators in 2025. Zapier Blog. https://zapier.com/blog/best-ai-image-generator/

- [13] https://arxiv.org/html/2506.21600v1

- [14] https://www.ijcai.org/proceedings/2025/0107.pdf

- [15] https://arxiv.org/html/2505.02567v6

- [16] https://arxiv.org/html/2510.12793v1