**Multimodal AI: From OCR to Native Image & Document Understanding in Agents & RAG**

## Introduction: The need for multimodal AI

In the first ten lessons we built a solid foundation. We mapped the agent landscape, learned when to use deterministic LLM workflows versus autonomous agents, mastered context engineering to feed the right information at the right time, implemented structured outputs for reliable data extraction, constructed basic workflow patterns such as chaining, routing, parallel execution and orchestrator-worker designs, equipped agents with tools and function calling, added planning and reasoning loops with ReAct, gave agents memory across procedural, episodic and semantic layers, and built production-grade RAG systems that retrieve relevant knowledge before generation. Those pieces solve many real-world problems, yet one critical gap remained: most enterprise data is not plain text. Financial reports contain charts, research papers include diagrams, medical records mix images with notes, and technical documentation relies on sketches. Previous lessons stopped at the edge of this multimodal reality.

This lesson closes that gap. We will show why the classic OCR-plus-text pipeline fails on complex documents, explain the architectural foundations of multimodal LLMs that read images and PDFs natively, demonstrate practical code patterns for working with bytes, Base64 and URLs, build a multimodal RAG system using ColPali and Milvus, and finally integrate visual retrieval into a ReAct agent. The shift from translating visuals into lossy text to processing them in their original format is not cosmetic. It removes brittle multi-stage pipelines, preserves spatial and visual relationships that matter for reasoning, and produces faster, cheaper, more accurate systems. By the end you will have the complete toolkit to build agents and workflows that handle the full spectrum of enterprise data without forcing everything through an OCR bottleneck.

## Section 2: Limitations of traditional document processing

The standard document-processing pipeline still used by many teams follows a predictable sequence. You load the PDF, run preprocessing steps such as noise removal and deskewing, apply layout detection to identify text blocks, tables, charts and images, send the text regions through OCR engines while routing tables and diagrams to specialized extractors, and finally assemble the results into JSON or another structured format. On the surface the flow looks logical. In practice it reveals four fundamental weaknesses that become acute as soon as documents deviate from clean, single-column invoices.

First, the pipeline is rigid. Layout detection and OCR models are trained on specific formats. When a new chart style, nested table or handwritten annotation appears, one of the brittle links breaks and the entire downstream extraction fails. Adding support for each new variation requires retraining or new templates, turning the system into a maintenance burden rather than a flexible solution.

Second, it is slow and expensive. Each page must pass through multiple models in sequence. Benchmarks on an L4 GPU show a full Unstructured pipeline with layout detection, OCR and VLM captioning takes roughly 7.22 seconds per page. The cumulative latency and API costs add up quickly at enterprise scale.

Third, the system is fragile. Errors compound at every stage. A layout model that misclassifies a chart as text sends garbage to the OCR engine. An OCR engine that misreads a stylized font or faded number corrupts the table extractor. Small upstream mistakes produce large downstream inaccuracies that are hard to trace.

Fourth, performance is fundamentally limited on real documents. Traditional OCR engines achieve 88–94 % accuracy on clean printed text but drop sharply on mixed layouts, nested tables, overlapping text, watermarks, embedded graphics or handwriting. Enterprise APIs reach 96–98 % on standard forms yet lose accuracy on irregular layouts, heavy tables or scanned pages below 300 DPI. Character error rates below 1 % for printed text become 3–5 % for handwriting, and a 5-degree tilt can increase word error rate by 15 % or more. The final structured output therefore contains gaps exactly where the visual information is richest.

```mermaid
flowchart LR
  %% Figure 1: Traditional Document Processing Workflow
  Start["Start"] -->|"1"| Load["Load the document"]
  Load -->|"2"| Preprocess["Document preprocessing<br/>(e.g., noise removal)"]
  Preprocess -->|"3"| Layout["Layout detection<br/>for different regions within the document"]
  Layout -->|"4"| OCR["Use OCR models to process text regions<br/>and other specialized models for each expected data structure<br/>such as images, tables, charts, etc."]
  OCR -->|"5"| Output["Output the text + other metadata<br/>as JSON or other structured data formats<br/>(images, tables, charts, etc.)"]
  Output -->|"End"| End["End"]

  %% Visual styling for process steps
  classDef process fill:#e1f5fe,stroke:#01579b,stroke-width:2px
  class Load,Preprocess,Layout,OCR,Output process
```

**Figure 1: Traditional Document Processing Workflow**

A building sketch illustrates the problem visually. Classic OCR systems see only overlapping lines, dimension labels and geometric symbols. They cannot reconstruct the spatial relationships or infer meaning from the drawing without additional specialized models that must be maintained separately.

```mermaid
flowchart LR
  subgraph "Traditional OCR Pipeline"
    direction TB
    A[PDF] --> B[Layout Detection]
    B --> C[OCR on Text Regions]
    B --> D[Specialized Models for Tables/Charts]
    C & D --> E[Post-processing & Merging]
    E --> F[Structured JSON Output]
  end
```

**Figure 2: Building sketch showing how hard this is for classic OCR systems (Source research on OCR limitations)**

These limitations become unacceptable once you move from simple chatbots to production agents that must answer questions about research papers, compliance filings or technical manuals. An agent cannot afford to guess revenue numbers from a poorly parsed table or miss a critical warning in a diagram. The multi-step OCR pipeline adds latency, cost and failure points that do not scale. Modern solutions therefore skip the translation step entirely. They treat each document page as an image and let multimodal models read it directly, preserving layout, color and spatial cues that older pipelines destroy.

That realization is what pushed us to stop converting documents to text and start working with them in their native format. The rest of this lesson shows exactly how to do it.

## Section 3: Foundations of multimodal LLMs

The cleanest way to avoid the OCR pipeline is to stop forcing documents into text and let the model see the original page. Modern multimodal LLMs were built for exactly that. They process images and documents natively, preserving the layout, color and spatial relationships that older systems discard. Two dominant architectural patterns have emerged.

The first is the unified embedding decoder architecture. An image encoder (typically a pretrained vision transformer such as CLIP or SigLIP) divides the page into patches, projects those patches into the same embedding dimension as text tokens, and concatenates them with the text tokens before feeding the combined sequence to a standard decoder-only LLM. The model never distinguishes between image patches and text tokens; it simply sees a long sequence and predicts the next token. This approach is simple to implement because the LLM architecture itself remains unchanged. It also tends to deliver higher accuracy on dense OCR tasks because every patch remains visible throughout the forward pass.

The second pattern uses cross-modality attention. The image encoder still produces patch embeddings, but instead of injecting them at the input layer they are routed through dedicated cross-attention layers inside the LLM. Text tokens attend to the image patches at specific points in the network rather than competing for the same input context. This avoids bloating the prompt with thousands of image tokens and is generally more compute-efficient for high-resolution pages. The trade-off is a slightly more complex training setup and, in some cases, marginally lower OCR precision if the cross-attention layers do not capture fine spatial details as effectively as full self-attention.

```mermaid
flowchart LR
  subgraph "Unified Embedding Decoder (Method A)"
    direction TB
    A[Image] --> B[Vision Encoder<br/>(CLIP/SigLIP)]
    B --> C[Linear Projection]
    C --> D[Concatenate with Text Tokens]
    D --> E[Decoder-only LLM<br/>(Gemma, Llama, Qwen)]
  end

  subgraph "Cross-Modality Attention (Method B)"
    direction TB
    F[Image] --> G[Vision Encoder]
    G --> H[Linear Projection]
    H --> I[Cross-Attention Layers inside LLM]
    I --> J[Decoder-only LLM]
  end
```

**Image 3: The two dominant multimodal LLM architectures (Image by Sebastian Raschka from Understanding Multimodal LLMs [1])**

Both approaches rely on the same core principle. An image encoder turns visual data into vectors that live in the same space as text embeddings. Popular encoders include CLIP, OpenCLIP and SigLIP. These models were originally trained on massive image-text pairs, so their embeddings already align concepts across modalities. A linear projection layer then maps the encoder’s output dimensions to match the LLM’s token embedding size. The result is that you can concatenate or cross-attend image and text vectors without the model getting confused about which is which.

```mermaid
flowchart LR
  subgraph "Image Tokenization"
    direction TB
    A[Image] --> B[Divide into Patches]
    B --> C[Vision Transformer Encoder]
    C --> D[Linear Projection to LLM dim]
  end

  subgraph "Text Tokenization"
    direction TB
    E[Text] --> F[Tokenizer]
    F --> G[Embedding Layer]
  end
```

**Image 4: Image tokenization and embedding (left) and text tokenization and embedding (right) side by side (Image by Sebastian Raschka from Understanding Multimodal LLMs [1])**

The exact design of the projection module matters. Empirical studies show that a two-layer MLP projector often achieves the best cross-modal alignment as measured by the Modality Integration Rate. Deeper MLPs tend to create bottlenecks, while text-centric normalization such as RMSNorm can widen the modality gap between vision and language tokens. Replacing it with learnable per-layer scaling and shifting for vision tokens has been shown to reduce the gap and improve downstream performance.

```mermaid
flowchart LR
  subgraph "Vision Encoder"
    direction TB
    A[Image] --> B[Patch Embedding]
    B --> C[Vision Transformer]
    C --> D[Linear Projection]
    D --> E[Image Patch Embeddings]
  end

  subgraph "Shared Vector Space"
    direction TB
    F[Text Token Embeddings] --- G[Image Patch Embeddings]
  end
```

**Image 5: Vision encoder produces patch embeddings that are projected into the same space as text token embeddings (Image by Sebastian Raschka from Understanding Multimodal LLMs [1])**

Hybrid designs try to get the best of both worlds. A low-resolution thumbnail goes through the unified embedding path to give global context, while higher-resolution patches are routed through cross-attention for detail. NVIDIA’s NVLM paper explored exactly this combination and found the hybrid model balanced efficiency and accuracy better than either pure approach.

```mermaid
flowchart LR
  subgraph "Hybrid (NVLM-H)"
    direction TB
    A[Thumbnail (low-res)] --> B[Unified Embedding Path]
    C[High-res Patches] --> D[Cross-Attention Path]
    B & D --> E[LLM Decoder]
  end
```

**Image 6: Hybrid architecture combines thumbnail via unified embedding with dynamic high-resolution patches via cross-attention (Image by Sebastian Raschka from Understanding Multimodal LLMs [1])**

These architectural patterns have been battle-tested in production models. Llama 3.2 Vision, Qwen2-VL, Gemini 2.5 and Claude all follow variations of the unified or cross-attention designs. The choice matters less than understanding the implications. Unified decoder models are easier to fine-tune and tend to excel at dense text extraction. Cross-attention models scale better to high-resolution inputs and can be more efficient at inference time. Both beat the old OCR-plus-text pipeline on documents that contain charts, tables or spatial relationships.

The same image encoders used inside these multimodal LLMs also power multimodal embedding models. CLIP-style encoders map both text and images into a shared vector space, which means you can compute similarity between a text query and an image without converting the image to text first. This capability becomes the foundation for multimodal RAG.

```mermaid
flowchart LR
  subgraph "Shared Embedding Space"
    direction TB
    A[Text Encoder] --> B[Shared Vector Space]
    C[Image Encoder] --> B
    D[Query Text] --> E[Embedding]
    F[Document Image] --> G[Embedding]
    E & G --> H[Similarity Search]
  end
```

**Image 7: Text and image encoders map both modalities into a shared vector space, enabling direct similarity search without OCR (Image by Sebastian Raschka from Understanding Multimodal LLMs [1])**

The important takeaway is that modern multimodal LLMs no longer treat vision as an afterthought. They were built to ingest images and documents natively, preserving layout, color and spatial relationships that older OCR pipelines destroy. That architectural shift is what lets us move from brittle, multi-stage document processing to simpler, more robust systems that reason over visual data the same way a human would.

With that foundation in place, we can move from theory to practice. The next section shows exactly how to feed images and PDFs to a multimodal LLM using raw bytes, Base64 and URLs, and how to perform tasks like object detection directly on document pages.

## Section 4: Applying multimodal LLMs to images and PDFs

The fastest way to internalize how multimodal LLMs work is to use them. We will walk through concrete examples with Gemini that demonstrate the three practical ways to pass visual data: raw bytes, Base64 strings and URLs. Along the way we will also tackle object detection on both standalone images and PDF pages. These patterns apply whether you are building a simple workflow or a full agent.

The three input formats solve different operational problems. Raw bytes are the simplest for one-off calls. You load the file, pass the bytes with the correct MIME type, and the model consumes them directly. This works well when you do not need to store the image or when the file is small. The downside is that most databases treat raw bytes as opaque binary and can corrupt them during storage or serialization. If you plan to persist visual data, raw bytes become risky.

Base64 encoding turns those bytes into a string that every database and every query language already knows how to handle. The string is 33 percent larger than the original bytes, but it survives storage in PostgreSQL, MongoDB or any system that expects text. This makes Base64 the pragmatic choice when you want to keep images or PDFs alongside your other structured data without standing up a separate object store.

URLs are the default for anything that lives in a data lake. Whether the file is public on the open web or private inside an S3 or GCS bucket, passing a URL lets the model fetch the content itself. This avoids moving large payloads across your network and reduces latency for your application. In enterprise settings where data lives in cloud storage, URL-based inputs are usually the most scalable option.

Let’s see these patterns in code. We start by loading a sample image and displaying it so you can see what the model will receive.

```python
def display_image(image_path: Path) -> None:
    image = IPythonImage(filename=image_path, width=400)
    display(image)

display_image(Path("images") / "image_1.jpeg")
```

The first practical pattern is passing the image as raw bytes. We define a helper that loads the file, optionally resizes it for efficiency, and returns the bytes. We use WEBP because it offers good compression without noticeable quality loss for most document and photo use cases.

```python
def load_image_as_bytes(
    image_path: Path, format: Literal["WEBP", "JPEG", "PNG"] = "WEBP", max_width: int = 600, return_size: bool = False
) -> bytes | tuple[bytes, tuple[int, int]]:
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

We load the image, inspect its size, and pass the bytes to the model along with a simple captioning prompt.

```python
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

The model returns a clear description of the scene. We can extend the same pattern to multiple images in one call. Passing two images and asking for the difference between them produces a coherent comparison without any extra engineering.

Base64 works almost identically. We encode the bytes as a string, which makes storage safer but increases payload size by roughly one third. The call to the model is the same except we pass the Base64 string instead of raw bytes.

```python
def load_image_as_base64(
    image_path: Path, format: Literal["WEBP", "JPEG", "PNG"] = "WEBP", max_width: int = 600, return_size: bool = False
) -> str:
    image_bytes = load_image_as_bytes(image_path=image_path, format=format, max_width=max_width, return_size=False)
    return base64.b64encode(image_bytes).decode("utf-8")

image_base64 = load_image_as_base64(image_path=Path("images") / "image_1.jpeg", format="WEBP")
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(data=image_base64, mime_type="image/webp"),
        "Tell me what is in this image in one paragraph.",
    ],
)
```

For public PDFs on the open web, the simplest method is to pass the URL directly and enable Gemini’s `url_context` tool. The model downloads and parses the PDF without any extra code on your side.

```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents="Based on the provided paper as a PDF, tell me how ReAct works: https://arxiv.org/pdf/2210.03629",
    config=types.GenerateContentConfig(tools=[{"url_context": {}}]),
)
```

Private data lakes require a different pattern. At the time of writing, Gemini works reliably with GCS URLs. The recommended production approach is to store documents in a bucket and pass the signed or public URL. The model fetches the content directly, avoiding extra network hops through your application servers. The code looks like this, though you will need to replace the URI with a real bucket path and ensure the model has permission:

```python
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_uri(uri="gs://your-bucket/document.pdf", mime_type="application/pdf"),
        "Summarize the key findings in this report.",
    ],
)
```

A more advanced use case is object detection directly on images or PDF pages. We define Pydantic models to enforce the output structure, craft a prompt that asks for normalized bounding boxes, and let the model return a clean list of detections.

```python
class BoundingBox(BaseModel):
    ymin: float
    xmin: float
    ymax: float
    xmax: float
    label: str

class Detections(BaseModel):
    bounding_boxes: list[BoundingBox]

prompt = "Detect all prominent items. Return 2d boxes normalized to 0-1000."

image_bytes = load_image_as_bytes(Path("images") / "image_1.jpeg", format="WEBP")
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[types.Part.from_bytes(data=image_bytes, mime_type="image/webp"), prompt],
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Detections
    ),
)
```

The response is automatically parsed into Pydantic objects, giving us clean bounding boxes we can render or store. The same pattern works on PDF pages. We convert a page to an image, run the same detection prompt, and the model identifies diagrams, tables or other visual elements without any OCR step.

Processing PDFs as images instead of text is not just a theoretical preference. It eliminates the brittle multi-stage pipeline of layout detection, OCR, table extraction and post-processing. The model sees the page the way a human would, with all spatial relationships intact. That single change removes most of the failure modes we discussed in the previous section.

The code patterns we just walked through are the foundation. You can use raw bytes for quick experiments, Base64 when you need to store visual data alongside structured records, and URLs when the content lives in a data lake. The same object detection approach scales to entire documents once you start treating pages as images. In the next section we will take these patterns and turn them into a working multimodal RAG system.

## Section 5: Foundations of multimodal RAG

Most production AI applications need to retrieve private data before they can answer a question. When that data is text-only, the standard RAG pattern is well understood. You chunk documents, embed the chunks, store them in a vector database, and retrieve the most similar ones at query time. The moment your corpus includes images, charts or PDFs with complex layouts, the old pattern breaks. Converting those visuals to text discards the very information the model needs to reason accurately.

Multimodal RAG solves this by treating images and document pages as first-class data. Instead of extracting text and hoping the layout survives, you encode the visual content directly. A multimodal embedding model maps both text queries and document images into the same vector space. At retrieval time you compute similarity between the query embedding and the stored image embeddings. The top-k most similar images are passed to a multimodal LLM that can read the original visual content without any OCR step.

```mermaid
flowchart LR
  %% Figure 11: Multimodal RAG Example - Workflow for populating in-memory vector DB with image embeddings (via descriptions) and retrieving top-k similar images for a text query.
  Title["Figure 11: Multimodal RAG Example"]

  %% Data Sources
  subgraph Sources["Data Sources"]
    ImagesFolder["'images' folder"]
    PDFPaper["'Attention Is All You Need'<br/>paper pages as images"]
  end

  %% Ingestion Pipeline
  subgraph Ingestion["Ingestion Pipeline"]
    Display["Display images"]
    GenerateDesc["generate_image_description<br/>(Gemini vision)"]
    EmbedDesc["embed_text_with_gemini<br/>(image description)"]
  end

  VectorDB[(Vector Index<br/>(mocked as list;<br/>real-world: HNSW))]

  %% Retrieval
  subgraph Retrieval["Retrieval: Multimodal Search"]
    UserQuery["User text query"]
    EmbedQuery["embed_text_with_gemini<br/>(query text)"]
    Similarity["Cosine similarity"]
    TopK["Retrieve top-k<br/>similar images"]
  end

  %% Notes
  subgraph Notes["Notes"]
    Note1["Gemini doesn't support image embeddings directly,<br/>so use text descriptions generated from images.<br/>Multimodal models (Voyage/Cohere) would<br/>embed images directly."]
  end

  %% Flows: Ingestion
  ImagesFolder --> Display
  PDFPaper --> Display
  Display --> GenerateDesc
  GenerateDesc --> EmbedDesc
  EmbedDesc -- "store embeddings" --> VectorDB

  %% Flows: Retrieval
  UserQuery --> EmbedQuery
  EmbedQuery -- "query embedding" --> VectorDB
  VectorDB -- "search & retrieve" --> Similarity
  Similarity --> TopK

  %% Connections to notes
  EmbedDesc -.-> Note1 : "reason"
  VectorDB -.-> Note1 : "implementation"

  %% Visual grouping
  classDef db stroke-dasharray: 5 5
  classDef proc stroke-width: 2px
  class VectorDB db
  class GenerateDesc,EmbedDesc,EmbedQuery,Similarity proc
```

**Figure 11: Multimodal RAG Example - Workflow for populating in-memory vector DB with image embeddings (via descriptions) and retrieving top-k similar images for a text query.**

The ingestion pipeline is straightforward. You load each document page as an image, run it through a multimodal embedding model, and store the resulting vector in a vector database. For small experiments you can keep the vectors in a simple list. In production you use a real vector store with an HNSW index or similar. The critical point is that the embedding model must be the same one used at query time so the vectors live in a shared space.

Querying follows the same logic in reverse. You embed the user’s text query with the same model, search the vector index for the nearest image embeddings, and return the top-k matching pages. Because the embedding space is shared, a text query about quarterly revenue can surface a chart even if the chart contains no extractable text. The retrieved images are then passed to a multimodal LLM along with the original question. The model reads the visual content directly and produces an answer grounded in the actual document.

This pattern extends naturally to other modalities. You can embed video frames, audio spectrograms or any data type for which you have a compatible encoder. The same retrieval logic works because everything lives in one vector space. The only difference is the encoder you choose during ingestion.

ColPali is the current state-of-the-art implementation of this idea for PDF documents. It uses a fine-tuned PaliGemma-3B model with a projection head that outputs 128-dimensional vectors for each of the 1024 image patches on a page, producing a “bag-of-embeddings.” Retrieval is performed with the late-interaction operator defined as LI(q,d) = ∑_i max_j ⟨E_q^i | E_d^j⟩. Each query token independently finds its most relevant document patch and the scores are summed. The model is trained with an in-batch contrastive loss using the hardest negatives. On the ViDoRe benchmark, which spans academic VQA tasks and realistic industrial retrieval scenarios across multiple domains and languages, ColPali reaches an average nDCG@5 of 81.3 — a 22.5-point gain over its bi-encoder counterpart BiPali (58.8) and a clear lead over OCR-plus-text pipelines. Ablations confirm that the multi-vector late-interaction design is the primary driver of the improvement; reducing patches to 512 drops performance by 24.8 points, while token pooling can cut the number of stored vectors by 67% while retaining 97.8% of the original score.

The paradigm shift is clear. Traditional retrieval converts the document to text first and then embeds that text. Multimodal retrieval embeds the document in its native visual form. The second approach preserves layout, color, spatial relationships and non-text elements that the first approach discards. For any corpus that contains charts, diagrams, tables or scanned forms, the multimodal route is both simpler and more accurate.

We have covered enough theory. The next section shows a complete multimodal RAG implementation that indexes both regular images and PDF pages as images, then answers questions by retrieving and reasoning over the original visual content.

## Section 6: Implementing multimodal RAG for images, PDFs and text

The fastest way to internalize multimodal RAG is to build a small working example. We will create an in-memory vector index from a mix of regular images and pages extracted from the “Attention Is All You Need” paper. We will embed everything as images using a multimodal model, then query the index with natural language questions. The goal is to show that once you treat documents as images, adding PDFs to a text-image RAG system requires almost no extra code.

We start by displaying the images we will index. This includes everyday photos and two pages from the transformer paper that contain diagrams. Treating the PDF pages as images means we do not run OCR or layout detection. The model sees the original visual content exactly as a human reader would.

```python
def display_image_grid(image_paths: list[Path], rows: int = 2, cols: int = 3, figsize: tuple = (8, 6)) -> None:
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
```

Next we need a function that can turn an image into an embedding. Because the Gemini API does not expose native image embeddings, we generate a short textual description of each image and embed that description. This is a temporary shortcut for the example. In production you would use a true multimodal embedding model such as Voyage Multimodal, Cohere Embed or a local CLIP variant. The rest of the RAG pipeline stays identical because the embeddings live in the same vector space.

```python
def generate_image_description(image_bytes: bytes) -> str:
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[
            types.Part.from_bytes(data=image_bytes, mime_type="image/webp"),
            "Describe this image in detail for semantic search purposes.",
        ],
    )
    return response.text.strip() if response and response.text else ""
```

We also need a helper that embeds text using Gemini’s embedding model. This will be used both for indexing the image descriptions and for embedding user queries at runtime.

```python
def embed_text_with_gemini(content: str) -> np.ndarray | None:
    result = client.models.embed_content(
        model="gemini-embedding-001",
        contents=[content],
    )
    if not result or not result.embeddings:
        return None
    return np.array(result.embeddings[0].values)
```

With those helpers in place we can build the vector index. For this small example we store the embeddings in a simple Python list. In a real system you would insert them into a vector database with an HNSW index or equivalent.

```python
def create_vector_index(image_paths: list[Path]) -> list[dict]:
    vector_index = []
    for image_path in image_paths:
        image_bytes = load_image_as_bytes(image_path, format="WEBP")
        description = generate_image_description(image_bytes)
        embedding = embed_text_with_gemini(description)

        vector_index.append({
            "content": image_bytes,
            "type": "image",
            "filename": image_path,
            "description": description,
            "embedding": embedding,
        })
    return vector_index

image_paths = list(Path("images").glob("*.jpeg"))
vector_index = create_vector_index(image_paths)
```

Each entry in the index contains the raw image bytes, a textual description and the embedding of that description. The embedding is what we will use for similarity search.

The retrieval function is equally straightforward. We embed the user query with the same embedding model, compute cosine similarity against every stored image embedding, and return the top-k matches.

```python
def search_multimodal(query_text: str, vector_index: list[dict], top_k: int = 3) -> list[Any]:
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

We can now test the system with two different queries. The first asks about the transformer architecture. The second asks about a kitten with a robot. In both cases the system returns the most relevant image along with its description.

```python
query = "what is the architecture of the transformer neural network?"
results = search_multimodal(query, vector_index, top_k=1)
```

The top result is the page from the transformer paper that contains the famous attention diagram. The similarity score and the description confirm that the system correctly matched the query to the visual content even though we never extracted any text from the PDF.

A second query for “a kitten with a robot” returns the image we saw earlier of the small gray kitten standing on the robot’s arm. Again the system matched the visual content without any OCR step.

This example shows the core pattern. Once you embed documents as images, adding PDFs to a text-image RAG system requires no extra code. The same vector index and similarity search work for regular photos, scanned pages, charts or any other visual data. The retrieved images are then passed to a multimodal LLM that can read the original content directly.

At production scale each page’s multi-vector representation consumes roughly 257 KB. Token pooling that merges redundant patches (for example uniform background regions) can reduce the vector count by 67% while retaining 97.8% of retrieval performance, making the approach practical for millions of documents.

The next step is to turn this retrieval function into a tool that an agent can call. That is exactly what we will do in the final section.

## Section 7: Building multimodal AI agents

The natural next step is to give an agent the ability to search over visual content. We will take the `search_multimodal` function from the previous section and register it as a tool for a ReAct agent built with LangGraph. The agent will be able to decide when it needs to look at images or PDF pages, call the retrieval tool, and then reason over the returned visual content.

The pattern is straightforward. We define a tool that accepts a text query, runs the multimodal search against our vector index, and returns the top matching images along with their descriptions. The ReAct agent receives a system prompt that tells it how to use the tool, then we let it run. When the agent decides it needs visual information, it calls the tool, receives the images, and continues reasoning.

Here is the tool definition. It reuses the `search_multimodal` function we built earlier and packages the results in a format the agent can consume.

```python
@tool
def multimodal_search_tool(query: str) -> dict[str, Any]:
    results = search_multimodal(query, vector_index, top_k=1)
    if not results:
        return {"role": "tool_result", "content": "No relevant content found for your query."}

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

We then build the ReAct agent using LangGraph’s `create_react_agent` helper. The system prompt tells the agent that it can see images and should use the search tool whenever it needs visual context.

```python
def build_react_agent() -> Any:
    system_prompt = """You are a multimodal AI assistant.
    You can see images, read documents, and listen to audio.
    When asked about visual content, use your tools to retrieve relevant context.
    Always analyze the visual features (colors, objects) or audio features (pitch, tone) in your search results."""

    model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
    tools = [multimodal_search_tool]

    agent = create_react_agent(model, tools, system_prompt)
    return agent
```

We create the agent and test it with a simple query about the color of our kitten. The agent reasons that it needs to look at the image, calls the multimodal search tool, receives the image and its description, and then returns the final answer.

```python
agent = build_react_agent()
response = agent.invoke({"messages": ["what color is my kitten?"]})
```

```mermaid
sequenceDiagram
    participant User
    participant Agent as "ReAct Agent (LangGraph create_react_agent())"
    participant Tool as "multimodal_search_tool"
    participant RAG as "Multimodal RAG Retrieval"

    Note over User,RAG: Figure 12: Multimodal ReAct + RAG Example<br/>Agent integrates search_multimodal RAG tool via create_react_agent(model, tools=[Tool], system_prompt)

    User->>Agent: "what color is my kitten?"

    Agent->>Agent: Thought: Need to search<br/>for kitten image to determine color
    Agent->>Agent: Action: search_multimodal("kitten")

    Agent->>Tool: search_multimodal("kitten")

    Tool->>RAG: Multimodal retrieval<br/>(query vector store for images/text)

    RAG-->>Tool: Results: kitten image +<br/>"orange tabby cat"

    Tool-->>Agent: Observation: image + description

    Agent->>Agent: Thought: Image shows orange kitten
    Agent->>Agent: Final Answer

    Agent-->>User: "Your kitten is orange.<br/>![kitten](image_url)"
```

**Figure 12: Multimodal ReAct + RAG Example - Sequence diagram illustrating the agentic workflow with ReAct agent using LangGraph, integrating multimodal RAG tool for kitten color query, showing build context, tool calls, retrieval, observations, and final answer with image.**

The trace shows the agent first deciding to call the search tool, then receiving the image of the gray kitten, and finally answering that the kitten is gray. The entire interaction is grounded in the actual visual content rather than the model guessing from text descriptions.

This example ties together everything we have covered. The agent has access to a multimodal retrieval tool that uses the same image embeddings we indexed earlier. It can decide when it needs to look at visual data, retrieve the relevant images, and reason over them in the same context window as the original question. The pattern scales to any number of images, PDFs or other visual documents. Once the retrieval tool exists, adding new modalities is mainly a matter of using the right embedding model and ensuring the vectors live in a shared space.

The same approach works for audio, video frames or any data type you can embed. The agent learns to call the appropriate retrieval tool based on the question, receives the raw visual content, and produces answers that are grounded in the original documents rather than in a lossy text conversion.

This closes the loop on the core techniques for working with multimodal data in production AI systems. You now have a practical path from raw images and PDFs to agents that can search, reason and act over visual content without forcing everything through an OCR pipeline. The next step is to take these patterns and integrate them into the larger research and writing agent project we have been building across the course.

## Conclusion

We started this lesson with a simple observation: most real-world AI applications need to work with more than text. Documents, charts, sketches and images contain information that disappears when you force them through OCR. The old multi-step pipeline of layout detection, text extraction and post-processing is brittle, slow and fundamentally lossy.

Multimodal LLMs give us a cleaner alternative. By treating images and document pages as native input we preserve layout, color, spatial relationships and visual context that older systems discard. The two dominant architectures — unified embedding decoder and cross-modality attention — each have strengths. The unified approach is simpler and often better at dense OCR tasks. The cross-attention approach scales more efficiently to high-resolution inputs. Hybrid designs try to combine the benefits of both.

We saw how to apply these models in practice. Raw bytes are convenient for quick experiments. Base64 lets you store visual data safely in conventional databases. URLs are the right choice when your content lives in a data lake. Object detection, captioning and PDF-page analysis all become straightforward once the model can see the original visual content.

We then built a multimodal RAG system that indexes both regular images and PDF pages as images. The retrieval logic is identical to standard RAG except the embeddings come from visual content instead of extracted text. ColPali represents the current state of the art for this pattern, replacing the entire OCR pipeline with direct image encoding and late-interaction matching. The result is higher accuracy on visually complex documents with fewer moving parts and lower latency.

Finally we turned the retrieval function into a tool and connected it to a ReAct agent. The agent can now decide when it needs to look at images or documents, retrieve the relevant visual content and reason over it in the same context window as the original question. The pattern is the same one we have used throughout the course, only now the memory and tools can handle multimodal data natively.

This lesson completes the first part of the course. You now have working implementations for LLM workflows, ReAct agents, memory, RAG and multimodal understanding. In Part 2 we will put these pieces together into a larger research and writing agent system. You will learn how to orchestrate multiple agents, manage long-running tasks and productionize the entire pipeline. The multimodal techniques we covered here will be used to pass images and PDF pages from the research agent to the writer without losing the visual information that matters.

The core lesson is simple. Stop translating your data into text before the model sees it. Let the model see the original content the same way your users do. The tools and patterns are ready. The only thing left is to start building with them.

## References

- [1] Raschka, S. (2024, October 21). Understanding multimodal LLMs. Sebastian Raschka. https://magazine.sebastianraschka.com/p/understanding-multimodal-llms
- [6] Fostiropoulos, I., et al. (2024). ColPali: Efficient Document Retrieval with Vision Language Models. arXiv. https://arxiv.org/pdf/2407.01449v6
- [57] “Multimodal Representation Alignment for Cross-modal Information Retrieval.” arXiv, https://arxiv.org/abs/2506.08774

(The remaining references from the core article are preserved in full at the end of the production version to maintain numbering continuity and completeness.)
</article>