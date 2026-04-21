**Lesson 11: Multimodal AI - From Images and Documents to Agentic RAG**

In the first ten lessons we covered the core building blocks of AI engineering: from understanding the agent landscape and choosing between workflows and agents, through context engineering, structured outputs, workflow patterns, tool use, planning with ReAct, memory systems, and advanced RAG techniques. Those lessons equipped you to design reliable systems that reason, act, remember, and retrieve knowledge. This final lesson of Part 1 addresses the missing piece that appears in nearly every real enterprise application: working natively with images, documents, and other visual data instead of forcing everything through text translation layers.

We learned this lesson the hard way while building an agent that analyzed financial reports. Our initial pipeline ran OCR on every page, extracted tables with specialized detectors, generated captions for charts, and fed the resulting text into the model. The system was slow, brittle, and frequently missed the very insights locked inside diagrams and spatial layouts. That experience showed us the core problem: when you translate visually rich content to text you lose the colors, geometric relationships, and contextual cues that humans rely on. Modern multimodal models solve this by processing images and PDFs in their native format. The result is faster, cheaper, and more accurate systems that see documents the same way a person does.

This lesson shows you exactly how to build those systems. We begin with the practical failures of traditional OCR-heavy pipelines on complex financial reports, medical records, and technical documentation. We then explain the architectural foundations of multimodal LLMs so you understand why they outperform older approaches. From there we demonstrate how to work directly with images and PDFs using Gemini, covering raw bytes, Base64, and URLs. Next we construct a multimodal RAG system that indexes both photographs and PDF pages as images. Finally we integrate that retrieval capability into a ReAct agent, creating a complete multimodal agentic RAG example you can adapt to your own data. By the end you will have the complete toolkit to stop translating visual information to text and start building agents that reason over the same rich formats your organization already uses.

**What we will cover in this lesson:**
- Why traditional multi-step OCR pipelines fail on real enterprise documents and the specific performance numbers behind those failures.
- The two primary architectures for multimodal LLMs and the practical trade-offs between them.
- How to process images and PDFs natively with Gemini using bytes, Base64, and URLs, including object detection on both photographs and document pages.
- The core architecture of multimodal RAG and why treating PDF pages as images eliminates the error cascade of OCR-based systems.
- A complete working implementation of multimodal RAG that indexes images and PDF pages into a vector store and retrieves them based on text queries.
- How to wrap that retrieval system as a tool inside a ReAct agent, creating a production-ready multimodal agent that can reason over visual content.

The techniques you learn here extend naturally to video frames and audio spectrograms, but we focus on the image and document patterns that solve the most common enterprise problems today. Let's start by examining exactly where and why the old OCR approach collapses in practice.

## Limitations of Traditional Document Processing

The traditional document processing pipeline that most organizations still rely on follows a predictable sequence. You load a PDF, run preprocessing to remove noise, apply layout detection to identify text blocks, tables, and images, feed text regions through OCR engines, use specialized models for tables or charts, and finally assemble everything into structured JSON or Markdown. On paper the flow looks logical. In production it reveals itself as rigid, slow, expensive, and surprisingly fragile.

The rigidity appears first. Most pipelines depend on templates or fixed rules for specific layouts. When a new report arrives with an unexpected table structure, a novel diagram style, or mixed handwriting on printed forms, the system fails. You either add another specialized model or accept lower accuracy. Maintenance becomes constant as document formats evolve across departments or vendors.

Errors compound at every stage. A layout detector might misclassify a chart as text. An OCR engine could transpose numbers in a financial table. A captioning model might describe a graph inaccurately. By the time the data reaches the LLM the original meaning has been distorted through multiple imperfect transformations. Research shows traditional OCR engines reach only 88–94 percent accuracy on complex layouts, with error rates climbing sharply on nested tables, mixed handwriting, or poor scan quality. One study found that even high-end enterprise OCR systems drop below 60 percent accuracy on semi-structured business documents when layout variations or handwriting appear. When PowerPoint slides containing architecture diagrams, tables, and calendars were evaluated, multimodal models like Gemini 1.5 Pro achieved 76 percent recall and 99 percent precision. Traditional OCR managed only 26 percent recall and 61 percent precision.

The operational cost is substantial. Running layout detection, multiple OCR calls, table extraction, and captioning for every page adds significant latency and compute expense. A single PDF with mixed content might require half a dozen model inferences before retrieval even begins. This becomes unsustainable at enterprise scale where thousands of documents arrive daily.

These problems appear across industries. Financial reports lose critical insights locked inside charts that text extraction cannot faithfully reproduce. Medical imaging diagnostics discard spatial context when scans are reduced to text descriptions. Technical documentation with sketches becomes nearly unusable when diagrams are flattened into crude textual approximations. The fundamental assumption that all information can be faithfully represented as text is simply false. Visual relationships, color coding, spatial arrangement, and graphical elements carry meaning that text alone cannot capture.

This realization drives the modern approach. Instead of converting documents to text and accepting the inevitable information loss, current systems process pages directly as images. Multimodal LLMs can see the complete visual context, including layout, color, and spatial relationships that OCR pipelines destroy. The rest of this lesson shows exactly how this works, beginning with the core architecture of multimodal LLMs themselves.

**Figure 1: Traditional multi-step PDF processing pipeline (load → preprocess → layout detection → OCR/specialized models → structured output).**  
(The diagram shows the sequential steps with error propagation arrows between each stage, highlighting how failures in layout detection or OCR cascade through the entire pipeline.)

**Figure 2: Building sketch example demonstrating OCR failure on complex layouts.**  
(The image shows a detailed architectural sketch with overlapping lines, annotations, and geometric relationships that traditional OCR engines misinterpret or completely miss.)

## Foundations of Multimodal LLMs

Before examining code it helps to have a clear mental model of how multimodal LLMs function. Two primary architectural patterns have emerged for combining visual and textual understanding.

The first pattern, the unified embedding decoder architecture, keeps the core LLM unchanged. An image encoder converts the visual input into a sequence of patch embeddings that match the dimensionality of text token embeddings. These image patches are concatenated directly with the text tokens and fed into the decoder-only transformer. The model processes everything in a single unified sequence, allowing seamless cross-modal reasoning. This approach is simpler to implement because it requires no modifications to the LLM's attention mechanism.

The second pattern, the cross-modality attention architecture, injects visual information deeper into the model. The image encoder still produces patch embeddings, but instead of adding them to the input sequence these embeddings are processed through dedicated cross-attention layers within the transformer blocks. The LLM's self-attention handles the text tokens normally while cross-attention allows the model to attend to image features at specific points in the computation. This design is more computationally efficient for high-resolution images because it avoids creating extremely long input sequences.

Both approaches rely on the same fundamental components. A vision encoder, typically based on a Vision Transformer or CLIP-style model, breaks images into patches and converts them into embeddings. A linear projection layer then aligns these visual embeddings with the text embedding space so the LLM can process them together. The choice between architectures involves clear trade-offs. The unified decoder approach tends to achieve higher accuracy on OCR-related tasks because all tokens participate fully in the self-attention mechanism. The cross-attention approach scales better with high-resolution inputs since it does not force every image patch into the main sequence.

Training the projection layer while the LLM remains frozen during pretraining comes with practical difficulties. The projector's small size makes it sensitive to learning rates and other hyperparameters, often resulting in poor convergence on complex alignments. Consequently, most pipelines unfreeze the LLM during instruction tuning. Different image tokenization strategies also affect downstream performance on document layouts. Fixed patching can break semantic objects into disconnected fragments. Approaches that produce semantically complete tokens through clustering or similarity-based filtering help the model reason more effectively over charts, diagrams, and tables.

Most leading models in 2025 follow one of these patterns or a hybrid variant. Open-source examples include Llama 4, Gemma 2, Qwen3, and DeepSeek variants, while closed models like GPT-5, Gemini 2.5, and Claude all support native multimodal input. The same principles extend beyond images to other modalities. Different encoders can be added for audio, video, or PDF pages treated as images. The core idea remains consistent: transform each data type into embeddings that can be aligned and processed together with text.

It is worth noting the distinction between multimodal LLMs and diffusion-based generation models like Stable Diffusion. Diffusion models excel at creating images from text but are architecturally separate from LLMs. In agent systems, diffusion models typically appear as specialized tools rather than the core reasoning engine. The multimodal LLMs we focus on here handle understanding across modalities while maintaining strong text performance.

These architectural innovations explain why directly processing documents as images outperforms traditional OCR pipelines. The model sees the complete visual context, including layout, color, spatial relationships, and graphical elements that text extraction inevitably loses. Different tokenization strategies further influence reasoning quality on complex layouts. Patch-based methods can fragment semantic objects, while approaches that cluster patches into semantically complete units or filter tokens using text similarity preserve more coherent visual meaning. Experiments on ScienceQA showed measurable gains when unimportant image tokens were masked using cross-modal similarity, demonstrating that selective token retention directly improves complex visual reasoning.

With this foundation in place, let's examine how these models work with concrete inputs.

**Figure 3: The two main approaches to multimodal LLM architectures (unified embedding decoder and cross-modality attention).** (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

**Figure 4: Unified embedding decoder architecture showing image patches concatenated with text tokens.** (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

**Figure 5: Cross-modality attention architecture injecting image features directly into transformer attention layers.** (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

**Figure 6: Image tokenization and embedding (left) versus text tokenization and embedding (right).** (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

**Figure 7: Vision Transformer (ViT) setup used as the image encoder.** (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

**Figure 8: Text and image embeddings aligned in the same vector space, enabling direct cross-modal similarity search.** (Source [Multimodal Embeddings: An Introduction](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/))

**Figure 9: Comparison of large modality gap (hard to match) versus small modality gap (easy to match) in cross-modal retrieval.** (Source [How to Choose the Best Embedding Model for RAG in 2026](https://milvus.io/blog/choose-embedding-model-rag-2026.md))

## Applying Multimodal LLMs to Images and PDFs

The practical advantage of multimodal LLMs becomes clear once you start working with them directly. Instead of building complex OCR pipelines, you can pass images and PDFs in their native format and receive structured responses. The Google Generative AI SDK makes this straightforward through three main input methods: raw bytes, base64 encoding, and URLs.

Raw bytes represent the simplest approach for one-off API calls. You load an image file, convert it to bytes, and pass it directly to the model. This method works well when you do not need to store the image persistently. The following code shows how to load an image as WEBP bytes and generate a caption.

```python
def load_image_as_bytes(image_path, format="WEBP", max_width=600):
    image = PILImage.open(image_path)
    if image.width > max_width:
        ratio = max_width / image.width
        new_size = (max_width, int(image.height * ratio))
        image = image.resize(new_size)
    byte_stream = io.BytesIO()
    image.save(byte_stream, format=format)
    return byte_stream.getvalue()

image_bytes = load_image_as_bytes("images/image_1.jpeg", format="WEBP")
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type="image/webp"),
        "Tell me what is in this image in one paragraph.",
    ],
)
```

The model returns a detailed description of the image contents. You can extend this pattern to compare multiple images by passing several byte objects in the same request. The LLM analyzes both images and describes their differences in a single coherent response.

Base64 encoding solves the storage problem. Many databases interpret raw bytes as text and can corrupt binary data. Base64 converts the bytes into a safe string format that survives storage and transmission. The encoded string is about 33 percent larger than the original bytes, but the trade-off is worth it for persistence. The process mirrors the byte approach except you encode the data first.

```python
def load_image_as_base64(image_path, format="WEBP", max_width=600):
    image_bytes = load_image_as_bytes(image_path, format=format, max_width=max_width)
    return base64.b64encode(image_bytes).decode("utf-8")

image_base64 = load_image_as_base64("images/image_1.jpeg", format="WEBP")
response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(data=image_base64, mime_type="image/webp"),
        "Tell me what is in this image in one paragraph.",
    ],
)
```

URLs provide the most scalable solution for production systems. When images or PDFs live in cloud storage like S3 or GCS, the model can fetch them directly rather than routing large binary payloads through your application servers. This reduces network overhead and simplifies architecture. For public web content, you can pass the URL with the appropriate context tool enabled.

Object detection demonstrates more advanced usage. You define a Pydantic model to specify the expected output structure, craft a precise detection prompt, and let the model return normalized bounding boxes with labels. The response parses automatically into clean Python objects.

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

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(data=image_bytes, mime_type="image/webp"),
        prompt,
    ],
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=Detections,
    ),
)

print(response.parsed)
```

PDF processing follows the same patterns. Since the model treats PDF pages as images, you can pass entire documents as byte streams, base64 strings, or cloud storage URLs. The model extracts meaning directly from the visual layout, including tables, charts, and diagrams that traditional OCR would distort. For object detection on PDF pages, you simply load the page as an image and run the same detection prompt used for regular images.

These examples demonstrate a fundamental shift. Instead of building brittle multi-stage pipelines that convert documents to text and lose critical visual context, you let the model see the content natively. The approach scales naturally to other modalities. The same principles apply to video frames or audio spectrograms. With this foundation established, we can now connect these capabilities to retrieval systems that power production applications.

**Shared setup code used throughout the examples in this section (from the lesson notebook):**

```python
from google import genai
from google.genai import types
from PIL import Image as PILImage
import io
import base64
from pathlib import Path

client = genai.Client()
MODEL_ID = "gemini-2.5-flash"
```

## Foundations of Multimodal RAG

Multimodal RAG extends the core retrieval-augmented generation pattern to handle images, documents, and other visual content alongside text. The central insight is that you no longer need to force everything into text before retrieval. Instead, you embed the visual content directly and retrieve the most relevant images or document pages based on semantic similarity.

The architecture follows the same basic flow as standard RAG but operates in a unified embedding space. During ingestion, you process each image or PDF page through a multimodal embedding model that converts visual content into vectors. These vectors are stored in a vector database alongside any associated metadata like captions or document identifiers. The key requirement is that the embedding model maps both text queries and visual content into the same vector space, enabling direct similarity comparisons regardless of the original modality.

At query time, the user's text question is embedded using the same model. The system then performs a similarity search against the stored image and document vectors. The top-k most relevant visual items are retrieved and passed to a multimodal LLM along with the original question. The LLM can now reason over both the text query and the actual visual content of the retrieved pages.

This approach solves several problems inherent in traditional document RAG. OCR errors disappear because no text extraction occurs during indexing. Layout and visual relationships remain intact since the model sees the complete page image. Charts, diagrams, and tables that would be lost or poorly represented in text become first-class citizens in the retrieval process.

ColPali represents the current state-of-the-art implementation for document-focused multimodal RAG. Rather than treating documents as text, ColPali processes each page as an image and generates multiple embeddings per page using a vision-language model. The model splits each page into patches, encodes them, and produces what is effectively a bag of embeddings that capture both textual and visual information. During retrieval, a late interaction mechanism computes fine-grained similarities between query tokens and document patches, allowing precise matching even for complex layouts.

The advantages become clear when you compare this to conventional pipelines. Traditional systems require layout detection, OCR, table extraction, captioning, chunking, and multiple embedding steps. Each stage introduces potential errors and adds latency. ColPali replaces this entire chain with a single forward pass through a vision-language model. The result is not only higher accuracy on visually complex documents but also significantly faster indexing and simpler system architecture.

Real-world applications demonstrate the practical value. Financial analysis systems can retrieve specific charts or tables from quarterly reports without losing the visual context that text extraction would destroy. Technical documentation platforms can surface diagrams and schematics alongside textual explanations. Research assistants can find relevant figures from academic papers by describing what they need to see rather than hoping the accompanying text captures the essential details.

**Figure 10: Multimodal RAG Ingestion & Retrieval Pipelines + Vector Database.**  
(The diagram shows the unified embedding space where both images and text are indexed, query modalities (text-to-image, image-to-image), and hybrid search options using captions and metadata.)

That said, scaling ColPali to large collections of multi-page documents, especially inside ReAct agent loops that may issue repeated queries, surfaces memory and latency issues. Each page produces hundreds of embedding vectors, and late-interaction scoring requires many pairwise computations. Research continues on compression, dynamic pruning, and hybrid indexing strategies to make these systems production-ready at scale.

The embedding space itself deserves attention. When text and images map to the same vector space, any combination of modalities becomes possible. You can index images and query with text, index text and query with images, or mix both approaches within the same collection. This flexibility proves especially valuable for enterprise systems that must handle diverse document types containing text, charts, photographs, and handwritten annotations.

With these foundations in place, we can now implement a working multimodal RAG system that demonstrates these principles in practice.

## Implementing Multimodal RAG for Images, PDFs and Text

The most effective way to internalize these concepts is to build a working system. We will create a multimodal RAG pipeline that indexes both regular images and PDF pages treated as images, then answers questions by retrieving the most relevant visual content.

The implementation follows the architecture we just discussed. We use ColPali-style embeddings to convert images and PDF pages into vectors, store them in a vector database, and retrieve based on semantic similarity to text queries. For this demonstration we mock the vector index as an in-memory list to keep the example self-contained. In production you would use a proper vector database with optimized indexes.

**Shared setup code used throughout the examples in this section (from the lesson notebook):**

```python
from google import genai
from google.genai import types
from PIL import Image as PILImage
import io
import base64
from pathlib import Path
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from tqdm import tqdm
from torch.utils.data import DataLoader

client = genai.Client()
MODEL_ID = "gemini-2.5-flash"
```

First we need a way to display the images we will index. The following code loads images from a directory and shows them in a grid so we can verify the content before embedding.

```python
def display_image_grid(image_paths, rows=2, cols=2, figsize=(8, 6)):
    fig, axes = plt.subplots(rows, cols, figsize=figsize)
    axes = axes.ravel()
    for idx, img_path in enumerate(image_paths[:rows*cols]):
        img = PILImage.open(img_path)
        axes[idx].imshow(img)
        axes[idx].axis('off')
    plt.tight_layout()
    plt.show()

display_image_grid([
    Path("images") / "image_1.jpeg",
    Path("images") / "image_2.jpeg",
    Path("images") / "image_3.jpeg",
    Path("images") / "image_4.jpeg",
    Path("images") / "attention_is_all_you_need_1.jpeg",
    Path("images") / "attention_is_all_you_need_2.jpeg",
], rows=2, cols=3)
```

Next we create the vector index. The `create_vector_index` function generates descriptions for each image using Gemini, then embeds those descriptions with a text embedding model. In a production system you would use a true multimodal embedding model that can process the images directly. The current implementation uses text descriptions as a practical workaround since the Gemini API does not expose image embeddings in the same way.

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

vector_index = create_vector_index(image_paths)
```

The `generate_image_description` function uses Gemini to create rich textual descriptions optimized for semantic search. The `embed_text_with_gemini` function converts those descriptions into embedding vectors using the Gemini embedding model. Each entry in the vector index contains the original image bytes, the generated description, and the corresponding embedding.

With the index populated, we can implement the search functionality. The `search_multimodal` function embeds a text query and finds the most similar images using cosine similarity.

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

Testing this with a query about transformer architecture returns the correct PDF page containing the model diagram. A follow-up query about a kitten with a robot correctly identifies the relevant image. These results demonstrate that the same vector index works for both standard photographs and PDF pages because we normalized everything to image format during ingestion.

This implementation shows the core pattern. You embed visual content directly, store the vectors, and retrieve based on semantic similarity. The same approach extends naturally to other modalities. Video frames can be sampled and embedded as images. Audio can be converted to spectrograms. The unified embedding space makes cross-modal retrieval straightforward once you have the right embedding model.

The next logical step is to connect this retrieval capability to an agent that can reason about when and how to use it.

**Figure 11: Multimodal RAG Example Workflow.**  
(The diagram shows data preparation from images and PDF pages, indexing with descriptions embedded as text, a mock vector database, and multimodal search using cosine similarity to retrieve top-k matching images or pages.)

## Building Multimodal AI Agents

The final step is to integrate our multimodal RAG system into a ReAct agent. This combines the retrieval capabilities we built with the reasoning patterns from earlier lessons, creating an agent that can decide when to search for visual information and how to interpret what it finds.

The implementation uses LangGraph's `create_react_agent` function with a custom tool that wraps our `search_multimodal` function. The system prompt explicitly instructs the agent to use visual search when questions involve images or documents it cannot answer from internal knowledge alone.

```python
def build_react_agent():
    system_prompt = """You are a multimodal AI assistant.
    You can see images, read documents, and reason about visual content.
    When asked about images, diagrams, or document content, use the multimodal_search_tool
    to find relevant visual information before answering."""
    
    model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")
    tools = [multimodal_search_tool]
    
    agent = create_react_agent(model, tools, system_prompt)
    return agent
```

The `multimodal_search_tool` takes a text query, calls our RAG search function, and returns the most relevant images along with their descriptions. The agent can then reason about the retrieved visual content and formulate its final response.

Testing the agent with a simple question about the color of a kitten demonstrates the complete flow. The agent first recognizes that it needs visual information, calls the search tool, receives the relevant image and description, and then provides a direct answer based on what it observes.

This pattern generalizes to any multimodal scenario. The agent can search through company documents, analyze screenshots, interpret charts from financial reports, or reason about images uploaded by users. The same retrieval mechanism works for any visual content once it has been embedded into the vector database.

The combination of multimodal retrieval and agentic reasoning creates systems that can work with the same types of information that humans naturally use. Instead of forcing everything through text translation layers that lose critical details, the agent sees the actual visual content and makes decisions based on complete information.

**Figure 12: Multimodal ReAct + RAG Agent Architecture.**  
(The diagram shows the setup of a ReAct agent with a multimodal search tool and the example execution loop for the kitten color query, including thought, action, observation, and final answer steps.)

## Conclusion

This lesson completes the foundational section of the course by showing how to work with multimodal data in LLM workflows and AI agents. You now understand why traditional OCR pipelines often fail on complex documents, how multimodal LLMs process images and PDFs natively, and how to build retrieval systems that work directly with visual content.

The key insight is that you should stop converting documents to text whenever possible. Modern vision-language models can understand page layouts, charts, diagrams, and spatial relationships that text extraction inevitably destroys. By treating images and PDFs in their native format, you create systems that are faster, cheaper, and more accurate than multi-stage OCR pipelines.

The techniques you learned here extend naturally to other modalities. The same patterns apply to video frames, audio spectrograms, or any data type that can be represented visually. The core principles of multimodal embedding, unified vector spaces, and direct visual processing remain consistent across different media types.

In Part 2 of the course we will apply these concepts to our capstone project. The research agent will use multimodal RAG to process both textual documents and visual content from web pages, while the writing agent will receive complete visual context from the research phase. This eliminates the information loss that occurs when complex diagrams and charts are forced into text descriptions.

The journey from simple text chatbots to sophisticated multimodal agents represents a fundamental shift in how we build AI systems. Context engineering, structured outputs, tool use, memory management, and multimodal understanding form the complete toolkit. You now have all the essential building blocks. The remaining lessons will show you how to combine them into production-ready AI applications that solve real business problems at scale.

The next part of the course moves from individual components to complete agent systems. You will learn advanced agentic patterns, compare different frameworks, and ultimately build a production-grade research and writing agent that demonstrates everything we have covered. The foundation is in place. The real engineering begins now.

## References

- [1] Raschka, S. (2024). Understanding Multimodal LLMs. Sebastian Raschka's Magazine. https://magazine.sebastianraschka.com/p/understanding-multimodal-llms
- [2] NVIDIA. (n.d.). Vision Language Models. NVIDIA Glossary. https://www.nvidia.com/en-us/glossary/vision-language-models/
- [3] Talebi, S. (2024). Multimodal Embeddings: An Introduction. Towards Data Science. https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/
- [4] Pinecone. (n.d.). Multi-modal ML with OpenAI's CLIP. Pinecone Learn. https://www.pinecone.io/learn/series/image-search/clip/
- [5] Fostiropoulos, I. et al. (2024). ColPali: Efficient Document Retrieval with Vision Language Models. arXiv. https://arxiv.org/pdf/2407.01449v6
- [6] Google AI for Developers. (n.d.). Image understanding with Gemini. https://ai.google.dev/gemini-api/docs/image-understanding
- [7] LangChain. (n.d.). Google Generative AI Embeddings. https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/
- [8] LangChain. (n.d.). LangGraph Quickstart. https://langchain-ai.github.io/langgraph/agents/agents/
- [9] Kokorin, O. (2023). Complex Document Recognition: OCR Doesn’t Work and Here’s How You Fix It. HackerNoon. https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it
- [10] Milvus. (n.d.). What are some real-world applications of multimodal AI? https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai
- [11] Roboflow. (2023). What Is Optical Character Recognition (OCR)? Roboflow Blog. https://blog.roboflow.com/what-is-optical-character-recognition-ocr/
- [12] Guinness, H. (2026). The 8 best AI image generators in 2025. Zapier. https://zapier.com/blog/best-ai-image-generator/
- [13] Capgemini Invent Lab. (n.d.). From OCR to Multimodal: A New Era in Image-to-Text Technology. https://medium.com/capgemini-invent-lab/from-ocr-to-multimodal-a-new-era-in-image-to-text-technology-8d45d7559f01
- [14] ICLR. (2025). Towards Semantic Equivalence of Tokenization in Multimodal LLM. https://iclr.cc/media/iclr-2025/Slides/28428.pdf
- [15] LearnOpenCV. (2024). Multimodal RAG with ColPali. https://learnopencv.com/multimodal-rag-with-colpali/
- [16] arXiv. (2026). Scaling ColPali-style multi-vector embeddings. https://arxiv.org/html/2602.12510v1

**Figure 1: Traditional multi-step PDF processing pipeline (load → preprocess → layout detection → OCR/specialized models → structured output).**  
(The diagram shows the sequential steps with error propagation arrows between each stage, highlighting how failures in layout detection or OCR cascade through the entire pipeline.)

**Figure 2: Building sketch example demonstrating OCR failure on complex layouts.**  
(The image shows a detailed architectural sketch with overlapping lines, annotations, and geometric relationships that traditional OCR engines misinterpret or completely miss.)

**Figure 3: The two main approaches to multimodal LLM architectures (unified embedding decoder and cross-modality attention).** (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

**Figure 4: Unified embedding decoder architecture showing image patches concatenated with text tokens.** (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

**Figure 5: Cross-modality attention architecture injecting image features directly into transformer attention layers.** (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

**Figure 6: Image tokenization and embedding (left) versus text tokenization and embedding (right).** (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

**Figure 7: Vision Transformer (ViT) setup used as the image encoder.** (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

**Figure 8: Text and image embeddings aligned in the same vector space, enabling direct cross-modal similarity search.** (Source [Multimodal Embeddings: An Introduction](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/))

**Figure 9: Comparison of large modality gap (hard to match) versus small modality gap (easy to match) in cross-modal retrieval.** (Source [How to Choose the Best Embedding Model for RAG in 2026](https://milvus.io/blog/choose-embedding-model-rag-2026.md))

**Figure 10: Multimodal RAG Ingestion & Retrieval Pipelines + Vector Database.**  
(The diagram shows the unified embedding space where both images and text are indexed, query modalities (text-to-image, image-to-image), and hybrid search options using captions and metadata.)

**Figure 11: Multimodal RAG Example Workflow.**  
(The diagram shows data preparation from images and PDF pages, indexing with descriptions embedded as text, a mock vector database, and multimodal search using cosine similarity to retrieve top-k matching images or pages.)

**Figure 12: Multimodal ReAct + RAG Agent Architecture.**  
(The diagram shows the setup of a ReAct agent with a multimodal search tool and the example execution loop for the kitten color query, including thought, action, observation, and final answer steps.)
</article>