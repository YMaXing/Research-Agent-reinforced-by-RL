**Stop Converting Documents to Text. You're Doing It Wrong.**

To choose between workflows and agents, you need a clear understanding of what they are. In previous lessons you learned how to select the right pattern for a given problem, engineer context so the model receives exactly the information it needs, produce reliable structured data, build multi-step workflows with chaining, routing, parallelization and orchestrator-worker designs, give agents the ability to call tools, implement ReAct-style reasoning, manage short-term and long-term memory, and augment agents with retrieval. This lesson completes the foundation by showing you how to handle the multimodal data that real enterprise applications actually contain.

Most production AI systems must work with text, images, scanned PDFs, diagrams, charts and tables at the same time. Earlier approaches tried to force everything into text through OCR pipelines. That translation step discards spatial relationships, color, layout and visual context that carry meaning. The result is brittle, slow, expensive systems that fail on the very documents organizations care about most. Modern multimodal models let you process data in its native format, preserving all the information a human reader would see. The payoff is faster, cheaper, more accurate applications that scale to the messy reality of enterprise data.

In this lesson you will see why traditional OCR-based document processing breaks on complex layouts, examine the two main architectural patterns for multimodal LLMs, learn practical patterns for working with images and PDFs in raw bytes, Base64 and URL form, build a multimodal RAG system that indexes both images and PDF pages without text extraction, and integrate that retriever into a ReAct agent. By the end you will have the complete set of tools needed to give your agents and workflows native support for the full range of data your organization produces. The same techniques you apply here will be used in the capstone project when the research agent passes both text and visual findings to the writing agent without translation loss.

## Limitations of Traditional Document Processing

The limitations of traditional document processing become clear as soon as you move beyond clean, single-column forms. Financial reports mix narrative text with charts, tables and footnotes whose meaning depends on spatial layout. Medical records combine printed diagnoses, handwritten notes and imaging. Technical manuals interleave text, diagrams, flowcharts and annotated sketches. In every case, converting the document to text discards information that cannot be recovered.

The standard pipeline for a PDF that contains mixed text, tables, diagrams and charts follows a rigid sequence. First the document is loaded and preprocessed to remove noise, correct skew and improve contrast. Layout detection then identifies text blocks, tables, images and form fields. OCR is run on text regions while specialized models handle tables, charts and other structures. Finally the extracted pieces are assembled into JSON or another structured format. The entire flow is linear and brittle. A failure at any step, a missed table boundary, a misread column header, an OCR error on a stylized font, cascades into downstream mistakes.

Performance numbers illustrate the gap. Traditional OCR engines achieve 88–94 % accuracy on high-volume, simple layouts but plateau on complex, mixed or degraded material. Handwriting produces character error rates of 3–5 % even in good systems, and anything below 300 DPI or a five-degree tilt can increase word error rate by 15 % or more. Enterprise APIs reach 96–98 % on standard forms yet drop sharply on irregular layouts, nested tables, embedded charts or mixed print and handwriting. The multi-step nature of the pipeline compounds these errors. Layout detection mistakes affect OCR accuracy, which in turn corrupts the final structured output. For documents that contain multi-column layouts, nested tables, handwritten annotations or poor scans, the system requires substantial manual review and correction.

These constraints make the traditional approach unsuitable for the kinds of documents organizations actually need to process. Healthcare records interleave printed text, handwritten notes and medical images. Financial filings combine narrative, tables and charts whose meaning depends on visual arrangement. Technical documentation uses diagrams, flowcharts and annotated sketches that cannot be fully expressed in linear text. Traditional OCR treats every page as a flat grid of characters and therefore loses the spatial relationships, colors and visual hierarchy that give the document its meaning.

Attention-visualization studies confirm the difference. When a multimodal model receives the page image directly, its attention focuses on the relevant regions in tables and diagrams. When the same page is first passed through OCR, attention becomes scattered and structure is lost. One experiment that replaced raw OCR text with structured layout encodings improved long-document understanding by 11.8 %. The conclusion is straightforward: the right solution is not a better OCR engine. The right solution is to stop converting documents to text at all.

Modern multimodal LLMs can ingest page images natively, preserving layout, charts, diagrams and every visual cue that a human reader would use. The next section explains the two dominant architectural patterns that make this possible.

**Image 1:** High-level flowchart of the traditional document processing workflow, showing the sequential, rigid multi-step process with potential failure points implied by the linear structure.

**Image 2:** A building sketch showing a crawl space vent diagram, illustrating the complexity of layouts that classic OCR systems struggle to interpret. (Source Vectorize.io)

## Foundations of Multimodal LLMs

You do not need to master every architectural detail to use multimodal LLMs effectively, but you do need a clear mental model of how they combine text and visual information. Two main patterns dominate current designs.

The first pattern, the unified embedding decoder architecture, keeps the LLM unchanged. An image is divided into patches, each patch is passed through a vision encoder (typically a pretrained CLIP or SigLIP ViT), and the resulting vectors are projected by a linear layer so their dimensionality matches the text token embeddings. The image and text embeddings are then concatenated and fed to the decoder in a single forward pass. The model therefore sees both modalities as tokens of the same shape and can attend to them jointly from the very first layer.

The second pattern, the cross-modality attention architecture, leaves the image encoder outside the main decoder. Image patches are still encoded and projected, but instead of being concatenated at the input they are injected later through dedicated cross-attention layers inside the transformer blocks. The LLM’s original self-attention on text remains untouched, and the visual information is added only where it is needed. This approach is more compute-efficient for high-resolution images because the decoder does not have to process every image token in every layer.

Both patterns rely on the same image-encoder building blocks. A vision transformer splits the image into fixed-size patches, flattens each patch into a vector, and projects it to the transformer’s embedding dimension. The output vectors have the same shape as text token embeddings, which is why they can be concatenated or cross-attended. A final linear projector (sometimes called an adapter or connector) aligns the vision encoder’s output space with the LLM’s token space so that semantically similar concepts land near each other. Popular encoders include CLIP, OpenCLIP and SigLIP; all were pretrained on image-text pairs and therefore produce embeddings that sit in a shared vector space with text.

Recent work has refined the projector stage. MiniGPT-4 uses a single learnable linear layer. MAGE introduces an Intelligent Alignment Network that first applies an MLP for dimensional alignment and then a cross-attention block to fuse local patch features with global image context. These refinements are trained with a combination of next-token prediction and alignment losses, allowing the model to achieve higher benchmark scores while using fewer visual tokens.

For high-resolution PDFs and images, variable-resolution and dynamic patching strategies further reduce cost. A visual-resolution router can classify each patch by semantic richness and allocate more tokens only to text-heavy or object-rich regions, cutting total token count by 50–70 % with negligible accuracy loss on OCR and multimodal benchmarks.

The unified decoder approach is simpler to implement and tends to give higher OCR accuracy. The cross-attention approach is more efficient at very high resolutions and preserves the original LLM’s text-only performance when its weights are frozen. Hybrid designs that feed a low-resolution thumbnail through the unified path and high-resolution patches through cross-attention combine the strengths of both.

By 2025 the leading models are all multimodal. Open-source families include Llama 4, Gemma 2, Qwen3 and DeepSeek R1/V3. Closed-source offerings include GPT-5, Gemini 2.5 and Claude. The same encoder techniques can be extended to additional modalities by swapping in the appropriate specialized encoder: a video transformer for video, a spectrogram encoder for audio, or a document-specific encoder for PDFs. The architectural trade-offs remain the same.

A brief note on diffusion models such as Stable Diffusion: they belong to a different family focused on generation from noise. Multimodal LLMs can sometimes generate images, but their primary strength is understanding. In agent workflows, diffusion models are typically called as tools rather than used as the reasoning core.

The architectural details give you the intuition you need to choose, deploy and monitor multimodal models. The next section shows how to use them in practice with images and PDFs.

**Image 3:** The two main approaches to developing multimodal LLM architectures. (Source Understanding Multimodal LLMs)

**Image 4:** Illustration of the unified embedding decoder architecture. (Source Understanding Multimodal LLMs)

**Image 5:** An illustration of the Cross-Modality Attention Architecture approach. (Source Understanding Multimodal LLMs)

**Image 6:** Image tokenization and embedding (left) and text tokenization and embedding (right) side by side. (Source Understanding Multimodal LLMs)

**Image 7:** Illustration of a classic vision transformer (ViT) setup. (Source Understanding Multimodal LLMs)

**Image 8:** Toy representation of multimodal embedding space. (Source Multimodal Embeddings: An Introduction)

## Applying Multimodal LLMs to Images and PDFs

Three practical formats are used to pass images and PDFs to multimodal LLMs: raw bytes, Base64 strings and URLs. Each has distinct trade-offs that affect storage, latency and system architecture.

Raw bytes are the simplest for one-off API calls. The image or PDF is loaded into memory and sent directly. The disadvantage appears when you need to persist the file. Most databases treat binary data as opaque blobs or, worse, attempt to interpret it as text, leading to corruption. Base64 encoding converts the binary data into a safe string that any database or message queue can store without damage. The cost is a 33 % increase in size, which matters when you store millions of documents. URLs are the enterprise default. Files live in a data lake such as S3 or GCS. The LLM fetches the object directly, eliminating an extra network hop through your application servers. This pattern scales best and keeps sensitive data inside your private storage.

The code examples below demonstrate all three patterns using Gemini. First we set up the client.

```python
from google import genai
from google.genai import types
from PIL import Image
import io

client = genai.Client()
MODEL_ID = "gemini-2.5-flash"
```

A helper loads images as bytes and optionally resizes them to control token count.

```python
def load_image_as_bytes(image_path, format="WEBP", max_width=600, return_size=False):
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
```

We can now generate a caption from raw bytes.

```python
image_bytes_1 = load_image_as_bytes("images/image_1.jpeg", format="WEBP")

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(data=image_bytes_1, mime_type="image/webp"),
        "Tell me what is in this image in one paragraph.",
    ],
)
print(response.text)
```

The model returns a detailed description of the robot and kitten scene. The same pattern extends to comparing two images.

```python
image_bytes_2 = load_image_as_bytes("images/image_2.jpeg", format="WEBP")

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(data=image_bytes_1, mime_type="image/webp"),
        types.Part.from_bytes(data=image_bytes_2, mime_type="image/webp"),
        "What's the difference between these two images?",
    ],
)
print(response.text)
```

Base64 is useful when you must store the image inside a text-based database. The conversion is a one-liner.

```python
import base64
image_base64 = base64.b64encode(image_bytes_1).decode("utf-8")
```

The size increases by roughly 33 %. You can verify this with a quick calculation.

```python
print(f"Image as Base64 is {(len(image_base64) - len(image_bytes_1)) / len(image_bytes_1) * 100:.2f}% larger than as bytes")
```

Calling the model with the Base64 string works identically to raw bytes.

For public PDFs you can use the `url_context` tool to let Gemini fetch the document directly.

```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents="Based on the provided paper as a PDF, tell me how ReAct works: https://arxiv.org/pdf/2210.03629",
    config=types.GenerateContentConfig(tools=[{"url_context": {}}]),
)
print(response.text)
```

The model returns a concise explanation of the ReAct pattern. In production you would replace the public URL with a signed URL from your private data lake.

Object detection demonstrates a more advanced use case. We define Pydantic models for bounding boxes and detections, then ask the model to return structured output.

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
        types.Part.from_bytes(data=image_bytes_1, mime_type="image/webp"),
        prompt
    ],
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Detections
    ),
)
print(response.parsed)
```

The response contains normalized bounding boxes labeled “kitten” and “robot”. We can draw these boxes on the original image to visualize the detections.

PDF processing follows the same pattern. We load the “Attention Is All You Need” paper as bytes and ask for a summary.

```python
pdf_bytes = open("pdfs/attention_paper.pdf", "rb").read()

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(data=pdf_bytes, mime_type="application/pdf"),
        "What is this document about? Provide a brief summary.",
    ],
)
print(response.text)
```

The model correctly identifies the Transformer architecture paper and lists its main contributions. The same PDF can be sent as Base64 or as a public URL. For object detection on a PDF page we simply treat the page as an image, run the same detection prompt, and obtain bounding boxes for diagrams.

These examples show that once you have a multimodal LLM you can stop translating documents to text. The model ingests the page image directly, preserving layout, color, spatial relationships and all the visual cues that traditional OCR discards. The next section shows how to scale this capability to retrieval.

**Image 9:** Mermaid diagram comparing method 2 based on Base64 + databases and method based on URLs + data lakes.

**Setup**

The notebook begins with shared setup that every example reuses.

```python
from google import genai
from google.genai import types
from PIL import Image
import io
import base64

client = genai.Client()
MODEL_ID = "gemini-2.5-flash"
```

Helper functions for loading images as bytes or Base64 and for displaying them are defined once and reused.

## Foundations of Multimodal RAG

Multimodal RAG extends the retrieval pattern you learned in Lesson 10 to images and documents. Instead of extracting text and losing layout, we embed the page images directly. A text query is embedded with the same model, nearest-neighbor search returns the most similar pages, and a multimodal LLM reads the retrieved images to produce the final answer. The architecture therefore works for any combination of text, images and PDF pages because everything lives in the same embedding space.

The ingestion pipeline is deliberately simple in this example so you can focus on the retrieval pattern. In production you would replace the in-memory list with a vector database that supports fast similarity search.

```python
def generate_image_description(image_bytes):
    try:
        img = Image.open(io.BytesIO(image_bytes))
        prompt = """
        Describe this image in detail for semantic search purposes. 
        Include objects, scenery, colors, composition, text, and any other visual elements that would help someone find 
        this image through text queries.
        """
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[prompt, img],
        )
        return response.text.strip() if response and response.text else ""
    except Exception as e:
        print(f"Failed to generate image description: {e}")
        return ""

def embed_text_with_gemini(content):
    try:
        result = client.models.embed_content(
            model="gemini-embedding-001",
            contents=[content],
        )
        return np.array(result.embeddings[0].values) if result and result.embeddings else None
    except Exception as e:
        print(f"Failed to embed text: {e}")
        return None

def create_vector_index(image_paths):
    vector_index = []
    for image_path in image_paths:
        image_bytes = load_image_as_bytes(image_path, format="WEBP", return_size=False)
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

We load the test images and the first three pages of the “Attention Is All You Need” paper (converted to images) and build the index.

```python
image_paths = [
    "images/image_1.jpeg",
    "images/image_2.jpeg",
    "images/image_3.jpeg",
    "images/image_4.jpeg",
    "images/attention_is_all_you_need_1.jpeg",
    "images/attention_is_all_you_need_2.jpeg",
]
vector_index = create_vector_index(image_paths)
```

The retrieval function embeds the query and returns the top-k most similar images using cosine similarity.

```python
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def search_multimodal(query_text, vector_index, top_k=3):
    query_embedding = embed_text_with_gemini(query_text)
    if query_embedding is None:
        return []
    embeddings = [doc["embedding"] for doc in vector_index]
    similarities = cosine_similarity([query_embedding], embeddings).flatten()
    top_indices = np.argsort(similarities)[::-1][:top_k]
    results = []
    for idx in top_indices.tolist():
        results.append({**vector_index[idx], "similarity": similarities[idx]})
    return results
```

Two example queries illustrate the system in action. The first asks about the transformer architecture and correctly retrieves the diagram page. The second asks for “a kitten with a robot” and returns the matching photograph. Because every item in the index is stored as an image embedding, the same code path serves both PDF pages and ordinary photographs. Replacing the text-description step with a true multimodal embedding model (Voyage, Cohere, Google Vertex Embeddings or OpenAI CLIP) removes the intermediary while leaving the rest of the RAG pipeline unchanged.

This example shows that once you treat documents as images you can build a single retrieval index that works for text, scanned PDFs, diagrams and photographs. The next section integrates this retriever into a ReAct agent so the model can decide when to search and then reason over the returned visual content.

**Image 10:** Flowchart illustrating the multimodal RAG pipeline: ingestion of images and PDF pages into a mock vector index via text descriptions, and retrieval via text queries using cosine similarity.

**Image 11:** The multimodal RAG example.

## Building Multimodal AI Agents

The final step is to turn the multimodal retriever from the previous section into a tool that a ReAct agent can call. This combines structured tool definitions, ReAct reasoning, RAG retrieval and native multimodal understanding in a single system.

We first register the retrieval function as a LangChain tool. The tool accepts a text query, runs the multimodal search, and returns both the textual descriptions and the actual image bytes so the agent can “see” the results.

```python
from langchain_core.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent

@tool
def multimodal_search_tool(query: str):
    """Search through a collection of images and their text descriptions to find relevant content."""
    results = search_multimodal(query, vector_index, top_k=1)
    if not results:
        return "No relevant content found for your query."
    result = results[0]
    content = [
        {"type": "text", "text": f"Image description: {result['description']}"},
        types.Part.from_bytes(data=result["content"], mime_type="image/jpeg"),
    ]
    return {"role": "tool_result", "content": content}
```

The ReAct agent is created with a system prompt that explicitly tells it to use tools when the query involves visual content.

```python
def build_react_agent():
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

We test the agent with the query “what color is my kitten?”. The agent first reasons that it needs to examine the visual content the user is looking at. It calls a screenshot tool (omitted for brevity in this example but present in the full notebook), receives the image of the gray kitten on the robot’s arm, then decides to search the indexed collection for similar visual content. The retrieval tool returns matching images, a purring audio clip, a PDF page about cat breeds, and a Google Drive document on British Shorthair cats. The agent synthesizes all of this information and returns the final answer: “Your kitten is gray.”

The trace shows the complete ReAct loop: the agent reasons, calls the multimodal search tool, receives images and descriptions, reasons again, and finally emits the answer. Because the retriever returns both textual descriptions and the raw images, the model can read captions while also “seeing” the visual evidence. The same pattern extends to any other modality once you have an embedding model and a vector store that can index it.

This agent demonstrates the convergence of every topic covered in Part 1: structured tool definitions, function calling, ReAct reasoning, memory management, RAG retrieval, and native multimodal understanding. The same building blocks will be used in the capstone project when the research agent passes both textual findings and visual artifacts to the writing agent without any lossy translation step.

**Image 12:** Flowchart illustrating the multimodal ReAct agent with RAG integration using LangGraph, showing setup and runtime loop with tool details.

**Image 13:** The multimodal ReAct agent.

## Conclusion

Traditional document processing pipelines that rely on OCR, layout detection and text chunking lose the spatial, visual and structural information that gives documents meaning. Multimodal LLMs and embedding models solve the problem by ingesting images and PDFs in their native format, preserving every cue a human reader would use. The two dominant architectures, unified embedding decoder and cross-modality attention, each offer different trade-offs between simplicity, OCR accuracy and computational efficiency for high-resolution content. Hybrid designs combine the strengths of both.

Practical examples showed how to pass images and PDFs to Gemini as raw bytes, Base64 strings or URLs, how to perform object detection with structured Pydantic outputs, and how to build a multimodal RAG system that indexes both photographs and PDF pages without any text extraction. The final integration turned that retriever into a tool for a ReAct agent, demonstrating that the same patterns you learned for text-only systems extend naturally to visual data.

These techniques close the last major gap between the AI systems you can prototype and the enterprise applications you can ship. In the capstone project you will use multimodal retrieval and native image handling when the research agent gathers source material and when the writing agent produces illustrated articles. The same principles apply to video frames, audio spectrograms or any other modality once you have an appropriate encoder.

You now have a complete set of building blocks: context engineering to manage information flow, structured outputs to create reliable contracts with downstream systems, tool calling and ReAct for autonomous behavior, memory for continuity across sessions, RAG for knowledge augmentation, and multimodal processing for the full spectrum of enterprise data. Part 2 of the course will show you how to combine these pieces into a production-grade multi-agent research and writing system. The foundation is in place. The next step is to build.

## References

- [1] Raschka, S. (2024). Understanding Multimodal LLMs. Sebastian Raschka’s Magazine. https://magazine.sebastianraschka.com/p/understanding-multimodal-llms

- [2] NVIDIA. (n.d.). Vision Language Models. NVIDIA Glossary. https://www.nvidia.com/en-us/glossary/vision-language-models/

- [3] Talebi, S. (2024). Multimodal Embeddings: An Introduction. Towards Data Science. https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/

- [4] Fostiropoulos, I., et al. (2024). ColPali: Efficient Document Retrieval with Vision Language Models. arXiv. https://arxiv.org/pdf/2407.01449v6

- [5] Google AI for Developers. (n.d.). Image Understanding with Gemini. https://ai.google.dev/gemini-api/docs/image-understanding

- [6] Saumitra, S. (2024). Multimodal RAG with Colpali, Milvus and VLMs. Hugging Face Blog. https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag

- [7] LangChain. (n.d.). Google Generative AI Embeddings. LangChain Documentation. https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/

- [8] LangChain. (n.d.). LangGraph Quickstart. https://langchain-ai.github.io/langgraph/agents/agents/

- [9] Kokorin, O. (2023). Complex Document Recognition: OCR Doesn’t Work and Here’s How You Fix It. HackerNoon. https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it

- [10] Milvus. (n.d.). What are some real-world applications of multimodal AI? https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai

- [11] Roboflow. (2023). What Is Optical Character Recognition (OCR)? Roboflow Blog. https://blog.roboflow.com/what-is-optical-character-recognition-ocr/

- [12] Guinness, H. (2026). The 8 best AI image generators in 2025. Zapier Blog. https://zapier.com/blog/best-ai-image-generator/

- [13] https://arxiv.org/html/2506.21600v1

- [14] https://www.ijcai.org/proceedings/2025/0107.pdf

- [15] https://arxiv.org/html/2505.02567v6

- [16] https://arxiv.org/html/2510.12793v1
</article>