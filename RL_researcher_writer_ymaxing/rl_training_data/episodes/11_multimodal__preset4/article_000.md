# Stop Converting Documents to Text. You're Doing It Wrong.

In the previous lessons, we built a solid foundation in AI Engineering. We learned the difference between LLM workflows and autonomous agents, mastered context engineering and structured outputs, and implemented core agentic patterns like ReAct, memory, and Retrieval-Augmented Generation (RAG). You now have the skills to build AI systems that can reason, remember, and retrieve information.

This lesson adds the final piece to the puzzle: multimodality. In the real world, we rarely work only with text. We process information visually and audibly through images, documents, and audio. Enterprise AI applications mirror this reality, needing to manipulate private data from warehouses and lakes that is inherently multimodal: financial reports with complex charts, technical diagrams with intricate sketches, and audio logs with subtle tonal cues. The applications extend beyond corporate documents, transforming creative industries by enabling AI-powered film post-production, interactive storytelling, and digital art generation [[74]](https://www.tvtechnology.com/opinion/reshaping-media-workflows-how-multimodal-and-generative-ai-impact-video-storytelling).

Early AI applications tried to normalize everything to text. We used Optical Character Recognition (OCR) to scrape PDFs and complex layout detection models to parse tables. The plot twist is that this approach is often wrong. Instead of translating images or documents to text, it is better to process them directly in their native format. This way, we preserve the rich visual information that gets lost in translation. We will show you how this approach is not only more performant but also simpler, faster, and cheaper to implement.

This lesson will give you the knowledge to build enterprise AI agents that can process your personal or organizational data in any format. We will cover:

-   The limitations of traditional document processing.
-   The foundations of how multimodal LLMs, embeddings, and RAG systems work.
-   Hands-on examples of working with images and PDFs using Gemini.
-   How to build a multimodal RAG system and a ReAct agent from scratch.

## Limitations of Traditional Document Processing

To understand why a multimodal-native approach is better, we need to look at the flaws of traditional document processing. When building AI systems for tasks like invoice parsing or report analysis, the old way was to force everything into a text format before the AI model ever saw it. This is a lossy and brittle process. When you encounter diagrams, charts, or sketches in a document, it is impossible to fully reproduce their meaning in text alone.

A typical OCR-based workflow involves a complex, multi-step pipeline to process a PDF containing mixed text, tables, and diagrams.

Image 1: A flowchart illustrating the traditional document processing workflow.

This pipeline has too many moving pieces. You need layout detection models, OCR models for text, and specialized models for each expected data structure, like tables or charts. This makes the system rigid and fragile. If a document contains a chart type you do not have a model for, the pipeline fails. It is also slow and costly because you have to chain multiple model calls.

Most importantly, this approach has serious performance challenges. The multi-step nature creates a cascade effect where errors compound at each stage. Even the best OCR engines struggle with handwritten text, poor-quality scans, or complex layouts like nested tables and building sketches [[9]](https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it), [[50]](https://intuitionlabs.ai/articles/ai-pdf-data-extraction-clinical-research). Studies show that while engines like Tesseract can reach 88-94% accuracy on simple layouts, this can drop significantly on real-world messy documents [[1]](https://www.llamaindex.ai/blog/ocr-accuracy). A 5-degree tilt alone can increase word error rates by 15% or more [[1]](https://www.llamaindex.ai/blog/ocr-accuracy). This performance gap becomes even more stark on visually rich content. In a direct comparison on PowerPoint slides containing complex layouts like lists, tables, and architecture diagrams, multimodal models like Gemini 1.5 Pro achieved a recall of 76% and precision of 99%, while a traditional OCR engine like Tesseract scored only 26% and 61%, respectively [[75]](https://medium.com/capgemini-invent-lab/from-ocr-to-multimodal-a-new-era-in-image-to-text-technology-8d45d7559f01). Multimodal models correctly interpret the spatial relationships and visual structures that OCR simply cannot process.

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2dc40f3-dc13-486e-853d-8404368f4d8d_1616x1000.png
Image 2: A building sketch showing a crawl space vent diagram, illustrating the complexity of layouts that classic OCR systems struggle to interpret. (Source [Vectorize.io](https://vectorize.io/blog/multimodal-rag-patterns))

While this might work for highly specialized applications, it does not scale in a world where AI agents need to be flexible and fast. Modern AI solutions use multimodal LLMs, such as Gemini, GPT-4o, or Claude, which can directly interpret text, images, and PDFs as native input. This approach completely bypasses the fragile OCR workflow.

To understand how, let’s explore how these models work.

## Foundations of Multimodal LLMs

To use LLMs with images and documents, you need an intuition of how multimodality works. You do not need to understand every research detail, but knowing the architecture helps you deploy, optimize, and monitor them.

There are two common approaches to building multimodal LLMs: the Unified Embedding Decoder Architecture and the Cross-modality Attention Architecture [[36]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms).

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76f50b57-2585-4cb8-8dda-eea5b5f81c03_1456x854.jpeg
Image 3: The two main approaches to developing multimodal LLM architectures. (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

### Unified Embedding Decoder Architecture

In this approach, we encode the text and image separately, concatenate their embeddings into a single vector, and pass the resulting vector to the LLM. On top of a standard LLM, you need a vision encoder that maps the image to an embedding in the same vector space as the text. When the text and image embeddings are merged, the LLM can make sense of both.

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0979e82-2fb0-4f78-80c8-1395511e057f_1166x1400.jpeg
Image 4: Illustration of the unified embedding decoder architecture. (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

### Cross-modality Attention Architecture

In the second approach, instead of passing the image embeddings along with the text embeddings at the input, we inject them directly into the attention module. We still need an image encoder that projects the image into the same vector space as the text, but we inject it deeper within the architecture.

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea1b9ee4-0d19-4c3c-89db-06e779653da2_1296x1338.jpeg
Image 5: An illustration of the Cross-Modality Attention Architecture approach. (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

### Image Encoders

Both architectures rely on image encoders, which function similarly to text tokenizers. Just as we split text into sub-word tokens, we split images into patches. These patches are then processed to create embeddings.

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a7104c0-3986-4aae-b918-06c393ff824c_1456x1154.jpeg
Image 6: Image tokenization and embedding (left) and text tokenization and embedding (right) side by side. (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

The image encoder, typically a pretrained Vision Transformer (ViT), processes these patches [[36]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms). The output has the same structure and dimensions as text embeddings. However, this fixed-grid patching is a relatively simple approach to image tokenization and has its own limitations. It can fragment objects across multiple patches, disrupting their semantic integrity. Emerging research focuses on more advanced techniques like semantic-equivalent tokenizers, which aim to group patches into complete semantic units that better align with linguistic concepts, improving the model's reasoning capabilities [[76]](https://iclr.cc/media/iclr-2025/Slides/28428.pdf).

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffef5f8cb-c76c-4c97-9771-7fdb87d7d8cd_1600x1135.png
Image 7: Illustration of a classic vision transformer (ViT) setup, similar to the model proposed in the original ViT paper from 2020. (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

However, for the LLM to understand them together, the image and text embeddings must be aligned in the same vector space. This alignment is achieved through a linear projection module, which ensures that similar concepts from different modalities are mapped to nearby points in the vector space. Popular image encoders that use this technique, often based on the core CLIP architecture, include OpenCLIP and SigLIP [[31]](https://milvus.io/blog/choose-embedding-model-rag-2026.md), [[35]](https://artsmart.ai/blog/top-embedding-models-in-2025/). These encoders are also used in multimodal RAG to find semantic similarities between images and text, allowing you to run similarity metrics across different data types.

https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d4c837a-a3e5-4d60-97ce-c4d4faf4cf57_841x616.png
Image 8: Toy representation of a shared multimodal embedding space where text and images are aligned. (Source [Multimodal Embeddings: An Introduction](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/))

### Trade-offs and Modern Landscape

The **Unified Embedding Decoder** approach is simpler to implement and generally yields higher accuracy in OCR-related tasks [[37]](https://arxiv.org/abs/2409.11402). The **Cross-modality Attention** approach is more computationally efficient for high-resolution images because it injects image tokens directly into the attention mechanism rather than passing them all through the input sequence [[37]](https://arxiv.org/abs/2409.11402). Hybrid approaches also exist to combine these benefits. Another emerging direction is neuro-symbolic AI, which combines neural pattern recognition with symbolic logic. In this paradigm, a neural model creates an object-based representation of an image, which a symbolic engine then uses for structured reasoning. This approach can enhance interpretability on complex visual documents [[77]](https://ajithp.com/2025/07/27/neuro-symbolic-ai-multimodal-reasoning/).

Training these models efficiently presents its own challenges. The projector layer, which aligns the vision and language embeddings, has a limited learning capacity. While training only this small component with the main LLM frozen is computationally cheap, it can struggle to learn complex multimodal alignments. Consequently, the LLM is often unfrozen during the later instruction-tuning phase to allow for more comprehensive updates [[36]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms).

In 2025, most leading LLMs are multimodal. Open-source examples include Llama 4, Gemma 2, Qwen3, and DeepSeek, while closed-source leaders include GPT-5, Gemini 2.5, and Claude models [[22]](https://medium.com/data-science-in-your-pocket/2025-the-year-ai-reasoning-models-took-over-a-month-by-month-review-of-frontier-breakthroughs-6ea2163f854f). These architectures can be extended to other modalities like PDFs, audio, or video by integrating specialized encoders for each data type [[28]](https://www.emergentmind.com/topics/multimodal-llms).

It is also important to distinguish multimodal LLMs from diffusion models like Midjourney or Stable Diffusion. Diffusion models generate images from noise and are architecturally different from LLMs [[19]](https://arxiv.org/html/2409.14993v3). In an agentic workflow, diffusion models are typically used as tools for image creation, not as the core reasoning engine.

Now that we have an intuition of how LLMs can directly process images and documents, let’s see this in practice.

## Applying Multimodal LLMs to Images and PDFs

To understand how multimodal LLMs work in practice, let’s write a few examples using Gemini to demonstrate some best practices for working with images and PDFs.

There are three primary ways to process multimodal data with LLMs: as raw bytes, as Base64-encoded strings, or as URLs.

-   **Raw bytes:** This is the easiest method for one-off API calls. However, storing raw bytes in a database can lead to data corruption, as many databases interpret the input as text strings.
-   **Base64:** This method encodes raw bytes as strings, making it safe to store images or documents directly in a database like PostgreSQL or MongoDB. The main downside is a file size increase of approximately 33%.
-   **URLs:** This is the standard for enterprise scenarios. Data is stored in a data lake like AWS S3 or Google Cloud Storage. The LLM downloads the media directly from the bucket, which reduces network latency for your application as the file never passes through your server. This is the most efficient option for large-scale applications.

For one-off LLM calls without storage, raw bytes work well. For storing data directly in a database, Base64 prevents corruption. For large-scale enterprise applications, URLs offer the most efficient and scalable solution.

Now, let's dig into the code.

1.  First, we display our sample image.

    ```python
    from pathlib import Path
    from IPython.display import Image as IPythonImage

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
    ```

    It outputs:

    ```text
    <IPython.core.display.Image object>
    ```

    ![A photorealistic image of a small, fluffy grey kitten playfully perched on the arm of a large, dark metallic robot with glowing red eyes.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5780cbd6-133b-44fe-9352-38250d6fc611_640x640.jpeg)

2.  We will process the image as raw bytes. We start by defining a helper function to load an image and convert it to bytes. We use the `WEBP` format because it is highly efficient.

    ```python
    import io
    from typing import Literal

    from PIL import Image as PILImage

    def load_image_as_bytes(
        image_path: Path, format: Literal["WEBP", "JPEG", "PNG"] = "WEBP", max_width: int = 600, return_size: bool = False
    ) -> bytes | tuple[bytes, tuple[int, int]]:
        """
        Load an image from file path and convert it to bytes with optional resizing.
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

    image_bytes = load_image_as_bytes(image_path=Path("images") / "image_1.jpeg", format="WEBP")
    ```

    Now we can call the LLM to generate a caption or even compare multiple images.

    ```python
    from google import genai
    from google.genai import types

    client = genai.Client()
    MODEL_ID = "gemini-2.5-flash"

    # Single image captioning
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

    # Comparing multiple images
    response_comparison = client.models.generate_content(
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
    ```

    It outputs:

    ```text
    Caption: This striking image features a massive, dark metallic robot...
    Comparison: The primary difference between the two images lies in the nature of the interaction depicted...
    ```

3.  Next, we process the image as a Base64-encoded string. Notice that the logic is similar, but we encode the bytes first.

    ```python
    import base64
    from typing import cast

    def load_image_as_base64(
        image_path: Path, format: Literal["WEBP", "JPEG", "PNG"] = "WEBP", max_width: int = 600, return_size: bool = False
    ) -> str:
        """
        Load an image and convert it to base64 encoded string.
        """

        image_bytes = load_image_as_bytes(image_path=image_path, format=format, max_width=max_width, return_size=False)

        return base64.b64encode(cast(bytes, image_bytes)).decode("utf-8")

    image_base64 = load_image_as_base64(image_path=Path("images") / "image_1.jpeg", format="WEBP")

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[
            types.Part.from_bytes(data=image_base64, mime_type="image/webp"),
            "Tell me what is in this image in one paragraph.",
        ],
    )
    ```

    As you can see, the Base64 version is about 33% larger than the raw bytes.

    ```python
    print(f"Image as Base64 is {(len(image_base64) - len(image_bytes)) / len(image_bytes) * 100:.2f}% larger than as bytes")
    ```

    It outputs:

    ```text
    Image as Base64 is 33.34% larger than as bytes
    ```

4.  For public URLs, Gemini's `url_context` tool allows the model to automatically parse webpages, PDFs, and images. You simply provide the URL in the prompt and configure the tool.

    ```python
    response = client.models.generate_content(
        model=MODEL_ID,
        contents="Based on the provided paper as a PDF, tell me how ReAct works: https://arxiv.org/pdf/2210.03629",
        config=types.GenerateContentConfig(tools=[{"url_context": {}}]),
    )
    ```

    It outputs:

    ```text
    ReAct is a novel paradigm for large language models (LLMs) that combines reasoning (Thought) and acting (Action) in an interleaved manner to solve diverse language and decision-making tasks...
    ```

5.  For URLs from private data lakes, Gemini integrates well with Google Cloud Storage. While we will not run it here for simplicity, the code would look like this, assuming the LLM has the necessary permissions.

    ```python
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[
            types.Part.from_uri(uri="gs://gemini-images/image_1.jpeg", mime_type="image/webp"),
            "Tell me what is in this image in one paragraph.",
        ],
    )
    ```

6.  Let's try a more complex task: object detection. We use Pydantic to define the output structure, leveraging what we learned in Lesson 4.

    ```python
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

    prompt = """
    Detect all of the prominent items in the image.
    The box_2d should be [ymin, xmin, ymax, xmax] normalized to 0-1000.
    Also, output the label of the object found within the bounding box.
    """

    image_bytes, image_size = load_image_as_bytes(
        image_path=Path("images") / "image_1.jpeg", format="WEBP", return_size=True
    )

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
    ```

    It outputs:

    ```text
    ymin=1.0 xmin=450.0 ymax=997.0 xmax=1000.0 label='robot'
    ymin=269.0 xmin=39.0 ymax=782.0 xmax=530.0 label='kitten'
    ```

7.  Now, let's process PDFs. Because we use a multimodal model, the process is identical to working with images. We will use the famous "Attention Is All You Need" paper as an example.

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
    This document introduces the Transformer, a novel neural network architecture designed for sequence transduction tasks (like machine translation)...
    ```

8.  Finally, we can perform object detection on PDF pages by treating them as images. This is powerful for extracting diagrams, tables, or other visual elements.

    ```python
    image_bytes, image_size = load_image_as_bytes(
        image_path=Path("images") / "attention_is_all_you_need_1.jpeg", format="WEBP", return_size=True
    )

    prompt = """
    Detect all the diagrams from the provided image as 2d bounding boxes...
    """

    #... same config and model call as before
    ```

    This technique of processing PDFs as images was popularized by the ColPali paper, which demonstrated that modern Vision Language Models (VLMs) can retrieve documents more effectively by "looking" at them rather than just reading extracted text [[5]](https://arxiv.org/pdf/2407.01449v6). This powerful idea of using vision models for retrieval is the foundation of modern multimodal RAG systems.

## Foundations of Multimodal RAG

One of the most common use cases for multimodal data is RAG, a concept we explored in Lesson 10. When building custom AI applications, you will almost always need to retrieve private company data. For large formats like images or PDFs, RAG is essential. Stuffing a thousand-page PDF into an LLM's context window is unfeasible due to the direct correlation between context size and increased latency, cost, and decreased performance.

Let's explore a generic multimodal RAG architecture using images and text as an example. The workflow consists of two main pipelines:

-   **Ingestion:** Images are embedded using a text-image embedding model, and these embeddings are stored in a vector database.
-   **Retrieval:** A user's text query is embedded using the same model. The vector database is then queried to retrieve the `top-k` most similar images based on the distance between the query embedding and the image embeddings.

Because the text and image embeddings exist in the same vector space, this approach also works for image-to-text or image-to-image search. This technique is heavily used in image search engines like Google or Apple Photos. Beyond document analysis, these techniques are used in industrial settings where technicians query manuals with diagrams or search real-time sensor data [[78]](https://www.elixirclaw.ai/blog/building-multimodal-rag-systems). Studies have confirmed that a multimodal approach in these scenarios achieves significantly higher performance than text-only or image-only RAG systems [[79]](https://www.ibm.com/think/topics/multimodal-rag).

Image 9: A Mermaid diagram illustrating a generic multimodal RAG architecture with Ingestion and Retrieval pipelines connected by a Vector Database.

For enterprise document RAG, one of the most popular architectures as of 2025 is ColPali [[5]](https://arxiv.org/pdf/2407.01449v6). Its key innovation is bypassing the entire OCR pipeline. ColPali, developed by Illuin Technology, achieves this by combining two key components: PaliGemma, a vision-language model, and ColBERT's late-interaction mechanism. Instead of compressing a query into a single vector, ColBERT allows every token in the query to interact with all the document patch embeddings, preserving granular detail and improving retrieval accuracy [[80]](colpali-redefining-multimodal-rag-with-gemini.md). Instead of extracting text, detecting layouts, and chunking, ColPali processes document images directly. It divides each page image into patches, creates a "bag-of-embeddings" for these patches, and uses a late interaction mechanism (MaxSim) to compute fine-grained similarities between query tokens and document patches. This makes it highly effective for documents with complex visual layouts.![The ColPali architecture, showing an offline ingestion pipeline where a Vision LLM processes documents, and an online pipeline where a query is processed by an LLM and matched against the document embeddings using a MaxSim similarity score.](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98194488-ddb1-4f93-b6d8-1937f374ed22_1508x686.png)
Image 10: The ColPali architecture simplifies document retrieval by using a Vision LLM for both offline indexing and online querying, outperforming traditional methods. (Source [ColPali Paper](https://arxiv.org/pdf/2407.01449v6))

ColPali is based on PaliGemma (3B parameters) with a SigLIP vision encoder. It offers 2-10x faster query latency and has fewer failure points compared to traditional OCR pipelines. On the ViDoRe benchmark, it outperforms all baseline systems with an 81.3% average nDCG@5 score [[5]](https://arxiv.org/pdf/2407.01449v6).

Despite its strengths, the ColPali approach has scaling challenges. The multi-vector representation and late-interaction mechanism are computationally expensive and create a significant memory and storage footprint, storing 10x-100x more data than dense embeddings [[81]](https://zilliz.com/blog/colpali-enhanced-doc-retrieval-with-vision-language-models-and-colbert-strategy). Another practical limitation is that it retrieves entire pages rather than smaller, more relevant chunks, which can increase token consumption and API costs for the downstream LLM. Furthermore, native support for ColBERT-style embeddings is still not common across all vector databases, which can add engineering overhead [[80]](colpali-redefining-multimodal-rag-with-gemini.md).

Now, let's implement a simplified multimodal RAG system from scratch.

## Implementing Multimodal RAG for Images, PDFs and Text

Let's connect the dots with a coding example where we combine what we have learned in this lesson and Lesson 10 into a multimodal RAG system. We will build a simple RAG pipeline that populates an in-memory vector database with images and PDF pages, and then query it with text questions. To keep it simple, we will not patch the images or use a late-interaction mechanism like ColPali.

Image 11: A Mermaid diagram illustrating the multimodal RAG example, showing the process of populating an in-memory vector database with images and then querying it with text questions.

1.  First, we define a function to generate a text description for each image using Gemini.

    <aside>
    💡

    The Gemini Dev API does not currently support direct image embedding. To keep this example simple, we will generate a description for each image and embed that description using a text embedding model. In a production system with a true multimodal embedding model (like Voyage AI, Cohere, or Google's models on Vertex AI), you would skip the description step and embed the image bytes directly. The rest of the RAG system architecture would remain the same.

    </aside>

    ```python
    from io import BytesIO

    def generate_image_description(image_bytes: bytes) -> str:
        """
        Generate a detailed description of an image using Gemini Vision model.
        """
        try:
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
            return response.text.strip() if response and response.text else ""
        except Exception as e:
            print(f"❌ Failed to generate image description: {e}")
            return ""
    ```

2.  Next, we define a function to create text embeddings using `gemini-embedding-001`.

    ```python
    import numpy as np

    def embed_text_with_gemini(content: str) -> np.ndarray | None:
        """
        Embed text content using Gemini's text embedding model.
        """
        try:
            result = client.models.embed_content(
                model="gemini-embedding-001",
                contents=[content],
            )
            return np.array(result.embeddings[0].values) if result and result.embeddings else None
        except Exception as e:
            print(f"❌ Failed to embed text: {e}")
            return None
    ```

3.  Now, we create our vector index. Since we only have a few images, we will mock the index as a Python list. In a real-world application, you would use a dedicated vector database with an efficient index like HNSW.

    ```python
    def create_vector_index(image_paths: list[Path]) -> list[dict]:
        """
        Create embeddings for images by generating descriptions and embedding them.
        """
        vector_index = []
        for image_path in image_paths:
            image_bytes = cast(bytes, load_image_as_bytes(image_path, format="WEBP", return_size=False))
            image_description = generate_image_description(image_bytes)
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

    image_paths = list(Path("images").glob("*.jpeg"))
    vector_index = create_vector_index(image_paths)
    ```

4.  We define a search function that finds the `top_k` most similar items from our vector index based on a user's text query.

    ```python
    from sklearn.metrics.pairwise import cosine_similarity
    from typing import Any

    def search_multimodal(query_text: str, vector_index: list[dict], top_k: int = 3) -> list[Any]:
        """
        Search for most similar documents to query using direct Gemini client.
        """
        query_embedding = embed_text_with_gemini(query_text)
        if query_embedding is None:
            return []

        embeddings = [doc["embedding"] for doc in vector_index]
        similarities = cosine_similarity([query_embedding], embeddings).flatten()
        top_indices = np.argsort(similarities)[::-1][:top_k]

        return [{**vector_index[idx], "similarity": similarities[idx]} for idx in top_indices]
    ```

5.  Let's test it with a query about the Transformer architecture.

    ```python
    query = "what is the architecture of the transformer neural network?"
    results = search_multimodal(query, vector_index, top_k=1)
    ```

    It correctly retrieves the page from the "Attention Is All You Need" paper with a similarity score of 0.744.

    ![A page from the 'Attention Is All You Need' paper showing the Transformer model architecture diagram.](https://substackcdn.com/image/fetch/w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f63e7c8-0d17-4835-985e-d82054c25f6e_600x776.jpeg)

6.  Here is another example with a query about a kitten and a robot.

    ```python
    query = "a kitten with a robot"
    results = search_multimodal(query, vector_index, top_k=1)
    ```

    It retrieves the correct image with a similarity score of 0.811.

    ![A photorealistic image of a small, fluffy grey kitten playfully perched on the arm of a large, dark metallic robot with glowing red eyes.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5780cbd6-133b-44fe-9352-38250d6fc611_640x640.jpeg)

    By treating all visual content as images, we used the same vector index to search for both standard images and PDF pages. This flexible approach could easily be extended to other visual data, like video frames or audio spectrograms. Now that we have a functional multimodal retrieval pipeline, the next logical step is to give it to an agent as a tool, allowing it to autonomously search and reason about visual information.

## Building Multimodal AI Agents

Now, let's take our RAG system a step further by integrating it into a ReAct agent as a tool. This will consolidate most of the skills you have learned so far in Part 1.

Multimodal capabilities can be added to AI agents in several ways:

1.  **Multimodal Inputs/Outputs:** The reasoning LLM behind the agent can natively accept and process multimodal data.
2.  **Multimodal Tools:** The agent can leverage tools that perform multimodal tasks, such as our RAG retriever.
3.  **External Resources:** The agent can interact with tools that access external resources like company PDFs, computer screenshots, or media files.

In this example, we will focus on the first two techniques. We will create a ReAct agent using LangGraph and connect our `search_multimodal` function as a tool. The agent will use this tool to find relevant images from our vector database and then use its native vision capabilities to answer questions about them.

Image 12: A Mermaid diagram illustrating the multimodal ReAct + RAG example.

1.  First, we define the `multimodal_search_tool` using LangGraph's `@tool` decorator. This tool will serve as our RAG function within the agent.

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

2.  Next, we create the ReAct agent. We will use LangGraph's `create_react_agent` function, which we will explore in more detail in Part 2 of the course. For now, think of it as a drop-in replacement for building a ReAct agent.

    ```python
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langgraph.prebuilt import create_react_agent

    def build_react_agent() -> Any:
        """
        Build a ReAct agent with multimodal search capabilities.
        """
        tools = [multimodal_search_tool]
        system_prompt = """You are a helpful AI assistant that can search through images and text to answer questions..."""

        agent = create_react_agent(
            model=ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0.1),
            tools=tools,
            prompt=system_prompt,
        )
        return agent

    react_agent = build_react_agent()
    ```

3.  Now, let's ask the agent about the color of our kitten.

    ```python
    test_question = "what color is my kitten?"
    response = react_agent.invoke(input={"messages": test_question})
    ```

    The agent first reasons that it needs to search for an image of a kitten. It calls the `multimodal_search_tool` with the query "my kitten". The tool retrieves the correct image and its description from our vector index. The agent then analyzes this retrieved content and formulates the final answer.

    It outputs:

    ```text
    Based on the image, your kitten is a gray tabby. It has soft, short gray fur with darker tabby stripe patterns.
    ```

    ![A photorealistic image of a small, fluffy grey kitten playfully perched on the arm of a large, dark metallic robot with glowing red eyes.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5780cbd6-133b-44fe-9352-38250d6fc611_640x640.jpeg)

    In this lesson, we combined structured outputs, tools, ReAct, RAG, and multimodal capabilities to create a functional multimodal agentic RAG proof of concept.

## Conclusion

Working with multimodal data is a fundamental skill for AI engineers. Modern AI applications rarely exist in a text-only vacuum; they interact with the complex, visual, and auditory reality of the world. By embracing a multimodal-native approach, we can build systems that are not only more powerful but also simpler and more robust.

As you build these systems, it is also important to consider their environmental impact. The growing computational demand of multimodal models intersects with sustainable computing practices. Optimizing energy consumption through techniques like quantization, pruning, and deploying smaller, efficient models on edge devices will become increasingly important for building responsible and scalable AI applications [[82]](https://mlsysbook.ai/book/contents/core/sustainable_ai/sustainable_ai.html).

This was the last lesson of Part 1, where we covered the fundamentals of AI Engineering. In Part 2 of the course, you will move from theory to practice by building a complete, interconnected research and writing agent system. We will dive deep into agentic design patterns, explore modern frameworks like LangGraph, and construct a multi-agent pipeline from start to finish.

## References

-   [1] OCR Accuracy Explained: How to Improve It. (2026, March 25). LlamaIndex. [https://www.llamaindex.ai/blog/ocr-accuracy](https://www.llamaindex.ai/blog/ocr-accuracy)
-   [2] The 6 Biggest OCR Problems and How to Overcome Them. (n.d.). Conexiom. [https://conexiom.com/blog/the-6-biggest-ocr-problems-and-how-to-overcome-them](https://conexiom.com/blog/the-6-biggest-ocr-problems-and-how-to-overcome-them)
-   [3] Overcoming OCR Errors and Limitations with Intelligent Document Processing. (n.d.). Jiffy.ai. [https://jiffy.ai/overcoming-ocr-errors-and-limitations-with-intelligent-document-processing/](https://jiffy.ai/overcoming-ocr-errors-and-limitations-with-intelligent-document-processing/)
-   [4] Unstructured Leads in Document Parsing Quality: Benchmarks Tell the Full Story. (n.d.). Unstructured.io. [https://unstructured.io/blog/unstructured-leads-in-document-parsing-quality-benchmarks-tell-the-full-story](https://unstructured.io/blog/unstructured-leads-in-document-parsing-quality-benchmarks-tell-the-full-story)
-   [5] Fostiropoulos, I., et al. (2024). ColPali: Efficient Document Retrieval with Vision Language Models. arXiv. [https://arxiv.org/pdf/2407.01449v6](https://arxiv.org/pdf/2407.01449v6)
-   [6] ChatGPT for Financial Analysis. (n.d.). Konfuzio. [https://konfuzio.com/en/chatgpt-financial-analysis/](https://konfuzio.com/en/chatgpt-financial-analysis/)
-   [7] Medical Imaging White Paper. (n.d.). Lenovo. [https://techtoday.lenovo.com/sites/default/files/2025-05/Medical%20Imaging%20White%20Paper%20NVIDIA%20and%20Lenovo.pdf](https://techtoday.lenovo.com/sites/default/files/2025-05/Medical%20Imaging%20White%20Paper%20NVIDIA%20and%20Lenovo.pdf)
-   [8] Wang, Z., et al. (2023). Beyond Pure Text: Summarizing Financial Reports Based on Both Textual and Tabular Data. IJCAI. [https://www.ijcai.org/proceedings/2023/0581.pdf](https://www.ijcai.org/proceedings/2023/0581.pdf)
-   [9] Complex Document Recognition: OCR Doesn’t Work and Here’s How You Fix It. (n.d.). HackerNoon. [https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it](https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it)
-   [10] What are some real-world applications of multimodal AI? (n.d.). Milvus. [https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai](https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai)
-   [11] What Is Optical Character Recognition (OCR)? (2023, November 21). Roboflow Blog. [https://blog.roboflow.com/what-is-optical-character-recognition-ocr/](https://blog.roboflow.com/what-is-optical-character-recognition-ocr/)
-   [12] The 8 best AI image generators in 2025. (2026, April 1). Zapier. [https://zapier.com/blog/best-ai-image-generator/](https://zapier.com/blog/best-ai-image-generator/)
-   [13] How to use an LLM to create data schemas in BigQuery. (n.d.). Google Cloud Blog. [https://cloud.google.com/blog/products/data-analytics/how-to-use-an-llm-to-create-data-schemas-in-bigquery](https://cloud.google.com/blog/products/data-analytics/how-to-use-an-llm-to-create-data-schemas-in-bigquery)
-   [14] Integrating Multimodal Data into a Large Language Model. (n.d.). Towards Data Science. [https://towardsdatascience.com/integrating-multimodal-data-into-a-large-language-model-d1965b8ab00c](https://towardsdatascience.com/integrating-multimodal-data-into-a-large-language-model-d1965b8ab00c)
-   [15] A Survey of Data Management in Multimodal LLMs. (2025). arXiv. [https://arxiv.org/html/2505.18458v1](https://arxiv.org/html/2505.18458v1)
-   [16] Multimodal RAG architecture for complex PDFs. (2025). LinkedIn. [https://www.linkedin.com/posts/sayandey01_generativeai-llm-rag-activity-7412381316106760192-nFx3](https://www.linkedin.com/posts/sayandey01_generativeai-llm-rag-activity-7412381316106760192-nFx3)
-   [17] Evaluating Multimodal vs. Text-Based Retrieval for RAG with Snowflake Cortex. (2025, April 21). Snowflake. [https://www.snowflake.com/en/engineering-blog/arctic-agentic-rag-multimodal-pdf-retrieval/](https://www.snowflake.com/en/engineering-blog/arctic-agentic-rag-multimodal-pdf-retrieval/)
-   [18] Multimodal RAG template for PDFs. (n.d.). Pathway. [https://pathway.com/developers/templates/rag/multimodal-rag](https://pathway.com/developers/templates/rag/multimodal-rag)
-   [19] Wang, X., et al. (2025). Multi-modal Generative AI: Multi-modal LLMs, Diffusions, and the Unification. arXiv. [https://arxiv.org/html/2409.14993v3](https://arxiv.org/html/2409.14993v3)
-   [20] Multimodal Pipelines. (n.d.). Anyscale. [https://docs.anyscale.com/llm](https://docs.anyscale.com/llm)
-   [21] Understanding Multimodal LLMs. (2024, November 3). Sebastian Raschka's Magazine. [https://magazine.sebastianraschka.com/p/understanding-multimodal-llms](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms)
-   [22] 2025: The Year AI Reasoning Models Took Over. (2025). Medium. [https://medium.com/data-science-in-your-pocket/2025-the-year-ai-reasoning-models-took-over-a-month-by-month-review-of-frontier-breakthroughs-6ea2163f854f](https://medium.com/data-science-in-your-pocket/2025-the-year-ai-reasoning-models-took-over-a-month-by-month-review-of-frontier-breakthroughs-6ea2163f854f)
-   [23] The Ultimate Guide to the Top Large Language Models in 2025. (n.d.). CodeDesign.ai. [https://codedesign.ai/blog/the-ultimate-guide-to-the-top-large-language-models-in-2025/](https://codedesign.ai/blog/the-ultimate-guide-to-the-top-large-language-models-in-2025/)
-   [24] Breakdown of 2025 Flagship LLM Architectures. (2025). LinkedIn. [https://www.linkedin.com/posts/progressivethinker_this-is-the-most-essential-breakdown-of-2025-activity-7376654335319117825-a5aD](https://www.linkedin.com/posts/progressivethinker_this-is-the-most-essential-breakdown-of-2025-activity-7376654335319117825-a5aD)
-   [25] Comparison of Coding LLMs. (2025). Preprints.org. [https://www.preprints.org/manuscript/202508.1904](https://www.preprints.org/manuscript/202508.1904)
-   [26] Ultimate 2025 AI Language Models Comparison. (n.d.). Promptitude. [https://www.promptitude.io/post/ultimate-2025-ai-language-models-comparison-gpt5-gpt-4-claude-gemini-sonar-more](https://www.promptitude.io/post/ultimate-2025-ai-language-models-comparison-gpt5-gpt-4-claude-gemini-sonar-more)
-   [27] Exploring Multimodal LLMs: Text, Image, and Video Integration. (n.d.). Sparkcognition. [https://sparkco.ai/blog/exploring-multimodal-llms-text-image-and-video-integration](https://sparkco.ai/blog/exploring-multimodal-llms-text-image-and-video-integration)
-   [28] Multimodal LLMs. (n.d.). Emergent Mind. [https://www.emergentmind.com/topics/multimodal-llms](https://www.emergentmind.com/topics/multimodal-llms)
-   [29] Enhancing LLM Capabilities: The Power of Multimodal LLMs and RAG. (n.d.). Towards AI. [https://towardsai.net/p/l/enhancing-llm-capabilities-the-power-of-multimodal-llms-and-rag](https://towardsai.net/p/l/enhancing-llm-capabilities-the-power-of-multimodal-llms-and-rag)
-   [30] From LLMs to MLLMs: A Survey. (2024). arXiv. [https://arxiv.org/html/2411.06284v3](https://arxiv.org/html/2411.06284v3)
-   [31] How to Choose the Best Embedding Model for RAG in 2026: 10 Models Benchmarked. (2026, March 25). Milvus. [https://milvus.io/blog/choose-embedding-model-rag-2026.md](https://milvus.io/blog/choose-embedding-model-rag-2026.md)
-   [32] What's the best embedding model for RAG in 2026? (2025). Reddit. [https://www.reddit.com/r/Rag/comments/1rcba6y/whats_the_best_embedding_model_for_rag_in_2026_my/](https://www.reddit.com/r/Rag/comments/1rcba6y/whats_the_best_embedding_model_for_rag_in_2026_my/)
-   [33] Best Embedding Models for RAG. (n.d.). Greennode. [https://greennode.ai/blog/best-embedding-models-for-rag](https://greennode.ai/blog/best-embedding-models-for-rag)
-   [34] Best Embedding Model for RAG. (n.d.). EagerWorks. [https://eagerworks.com/blog/best-embedding-model-for-rag](https://eagerworks.com/blog/best-embedding-model-for-rag)
-   [35] Top Embedding Models in 2025. (n.d.). ArtSmart.ai. [https://artsmart.ai/blog/top-embedding-models-in-2025/](https://artsmart.ai/blog/top-embedding-models-in-2025/)
-   [36] Raschka, S. (2024, November 3). Understanding Multimodal LLMs. Sebastian Raschka's Magazine. [https://magazine.sebastianraschka.com/p/understanding-multimodal-llms](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms)
-   [37] NVLM: Open Frontier-Class Multimodal LLMs. (2024). arXiv. [https://arxiv.org/abs/2409.11402](https://arxiv.org/abs/2409.11402)
-   [38] Multimodal AI Agents. (n.d.). Kanerika. [https://kanerika.com/blogs/multimodal-ai-agents/](https://kanerika.com/blogs/multimodal-ai-agents/)
-   [39] Multimodal Enterprise AI. (n.d.). Invisible Technologies. [https://invisibletech.ai/blog/multimodal-enterprise-ai](https://invisibletech.ai/blog/multimodal-enterprise-ai)
-   [40] Multimodal AI Use Cases. (n.d.). Rasa. [https://rasa.com/blog/multimodal-ai-use-cases](https://rasa.com/blog/multimodal-ai-use-cases)
-   [41] A Comprehensive Survey and Guide to Multimodal Large Language Models in Vision-Language Tasks. (n.d.). GitHub. [https://github.com/cognitivetech/llm-research-summaries/blob/main/models-review/A-Comprehensive-Survey-and-Guide-to-Multimodal-Large-Language-Models-in-Vision-Language-Tasks.md](https://github.com/cognitivetech/llm-research-summaries/blob/main/models-review/A-Comprehensive-Survey-and-Guide-to-Multimodal-Large-Language-Models-in-Vision-Language-Tasks.md)
-   [42] Multimodal AI Examples. (n.d.). SmartDev. [https://smartdev.com/multimodal-ai-examples-how-it-works-real-world-applications-and-future-trends/](https://smartdev.com/multimodal-ai-examples-how-it-works-real-world-applications-and-future-trends/)
-   [43] Multimodal LLM. (n.d.). IBM. [https://www.ibm.com/think/topics/multimodal-llm](https://www.ibm.com/think/topics/multimodal-llm)
-   [44] Multimodal Large Language Models for Heterogeneous Medical Data. (2025). PMC. [https://pmc.ncbi.nlm.nih.gov/articles/PMC12479233/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12479233/)
-   [45] Multimodal LLMs in Healthcare. (2025). Nature. [https://www.nature.com/articles/s41598-025-98483-1](https://www.nature.com/articles/s41598-025-98483-1)
-   [46] End-to-End Distributed PDF Processing Pipeline. (n.d.). Daft. [https://www.daft.ai/blog/end-to-end-distributed-pdf-processing-pipeline](https://www.daft.ai/blog/end-to-end-distributed-pdf-processing-pipeline)
-   [47] Why traditional OCR fails for complex business documents. (n.d.). Microsoft Learn. [https://learn.microsoft.com/en-us/answers/questions/5668164/why-traditional-ocr-fails-for-complex-business-doc?page=1](https://learn.microsoft.com/en-us/answers/questions/5668164/why-traditional-ocr-fails-for-complex-business-doc?page=1)
-   [48] Document Processing Automation Guide. (n.d.). Parseur. [https://parseur.com/blog/document-processing-automation-guide](https://parseur.com/blog/document-processing-automation-guide)
-   [49] OCR for Tables. (n.d.). LlamaIndex. [https://www.llamaindex.ai/blog/ocr-for-tables](https://www.llamaindex.ai/blog/ocr-for-tables)
-   [50] AI PDF Data Extraction in Clinical Research. (n.d.). Intuition Labs. [https://intuitionlabs.ai/articles/ai-pdf-data-extraction-clinical-research](https://intuitionlabs.ai/articles/ai-pdf-data-extraction-clinical-research)
-   [51] Gemini consistently producing valid Pydantic responses. (n.d.). Google AI Community. [https://discuss.ai.google.dev/t/gemini-consistently-producing-valid-pydantic-responses/98992](https://discuss.ai.google.dev/t/gemini-consistently-producing-valid-pydantic-responses/98992)
-   [52] Stop Converting Documents to Text. You're Doing It Wrong. (n.d.). Decoding AI. [https://www.decodingai.com/p/stop-converting-documents-to-text](https://www.decodingai.com/p/stop-converting-documents-to-text)
-   [53] LLM Output Parsing & Structured Generation. (n.d.). Tetrate. [https://tetrate.io/learn/ai/llm-output-parsing-structured-generation](https://tetrate.io/learn/ai/llm-output-parsing-structured-generation)
-   [54] Structured Outputs with Multimodal Gemini. (2024, October 23). Instructor. [https://python.useinstructor.com/blog/2024/10/23/structured-outputs-with-multimodal-gemini/](https://python.useinstructor.com/blog/2024/10/23/structured-outputs-with-multimodal-gemini/)
-   [55] Steering Large Language Models with Pydantic. (n.d.). Pydantic. [https://pydantic.dev/articles/llm-intro](https://pydantic.dev/articles/llm-intro)
-   [56] Multimodal Semantic Search. (n.d.). OpenSearch. [https://opensearch.org/blog/multimodal-semantic-search/](https://opensearch.org/blog/multimodal-semantic-search/)
-   [57] Multimodal AI Search for Business Applications. (n.d.). Towards Data Science. [https://towardsdatascience.com/multimodal-ai-search-for-business-applications-65356d011009/](https://towardsdatascience.com/multimodal-ai-search-for-business-applications-65356d011009/)
-   [58] Joint Visual-Textual Embedding for Multimodal Style Search. (n.d.). Amazon Science. [https://assets.amazon.science/89/bf/661d950d4059930c8f1d2e449ac6/joint-visual-textual-embedding-for-multimodal-style-search.pdf](https://assets.amazon.science/89/bf/661d950d4059930c8f1d2e449ac6/joint-visual-textual-embedding-for-multimodal-style-search.pdf)
-   [59] Combine Image and Text: How Multimodal Retrieval Transforms Search. (n.d.). Zilliz. [https://zilliz.com/blog/combine-image-and-text-how-multimodal-retrieval-transforms-search](https://zilliz.com/blog/combine-image-and-text-how-multimodal-retrieval-transforms-search)
-   [60] Multimodal Sentence Transformers. (n.d.). Hugging Face. [https://huggingface.co/blog/multimodal-sentence-transformers](https://huggingface.co/blog/multimodal-sentence-transformers)
-   [61] Vision Language Models. (n.d.). NVIDIA. [https://www.nvidia.com/en-us/glossary/vision-language-models/](https://www.nvidia.com/en-us/glossary/vision-language-models/)
-   [62] Multimodal Embeddings: An Introduction. (2024, November 29). Towards Data Science. [https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/)
-   [63] Multimodal Embeddings: An Introduction. (2024, November 29). YouTube. [https://www.youtube.com/watch?v=YOvxh_ma5qE](https://www.youtube.com/watch?v=YOvxh_ma5qE)
-   [64] Multi-modal ML with OpenAI's CLIP. (n.d.). Pinecone. [https://www.pinecone.io/learn/series/image-search/clip/](https://www.pinecone.io/learn/series/image-search/clip/)
-   [65] Image understanding with Gemini. (n.d.). Google AI for Developers. [https://ai.google.dev/gemini-api/docs/image-understanding](https://ai.google.dev/gemini-api/docs/image-understanding)
-   [66] Multimodal RAG with Colpali, Milvus and VLMs. (2024, December 10). Hugging Face. [https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag](https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag)
-   [67] Google Generative AI Embeddings (AI Studio & Gemini API). (n.d.). LangChain. [https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/](https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/)
-   [68] LangGraph quickstart. (n.d.). LangChain. [https://langchain-ai.github.io/langgraph/agents/agents/](https://langchain-ai.github.io/langgraph/agents/agents/)
-   [69] Why OCR technology fails on real-world documents and how intelligent document processing can help. (n.d.). netfira. [https://netfira.com/why-ocr-technology-fails-on-real-world-documents-and-how-intelligent-document-processing-can-help/](https://netfira.com/why-ocr-technology-fails-on-real-world-documents-and-how-intelligent-document-processing-can-help/)
-   [70] EPOCH framework for AI in financial services. (2025). arXiv. [https://arxiv.org/html/2503.22035v1](https://arxiv.org/html/2503.22035v1)
-   [71] 10 real-world examples of AI in healthcare. (2022, November 24). Philips. [https://www.philips.com/a-w/about/news/archive/features/2022/20221124-10-real-world-examples-of-ai-in-healthcare.html](https://www.philips.com/a-w/about/news/archive/features/2022/20221124-10-real-world-examples-of-ai-in-healthcare.html)
-   [72] MMCTAgent for multimodal reasoning. (2025). LinkedIn. [https://www.linkedin.com/posts/gauravagg_mmctagent-enables-multimodal-reasoning-over-activity-7413983881181339648--PyD](https://www.linkedin.com/posts/gauravagg_mmctagent-enables-multimodal-reasoning-over-activity-7413983881181339648--PyD)
-   [73] Multimodal RAG Explained. (n.d.). USAII. [https://www.usaii.org/ai-insights/multimodal-rag-explained-from-text-to-images-and-beyond](https://www.usaii.org/ai-insights/multimodal-rag-explained-from-text-to-images-and-beyond)
-   [74] Reshaping Media Workflows: How Multimodal and Generative AI Impact Video Storytelling. (2024, November 11). TV Technology. [https://www.tvtechnology.com/opinion/reshaping-media-workflows-how-multimodal-and-generative-ai-impact-video-storytelling](https://www.tvtechnology.com/opinion/reshaping-media-workflows-how-multimodal-and-generative-ai-impact-video-storytelling)
-   [75] From OCR to Multimodal: A New Era in Image-to-Text Technology. (2024, December 3). Medium. [https://medium.com/capgemini-invent-lab/from-ocr-to-multimodal-a-new-era-in-image-to-text-technology-8d45d7559f01](https://medium.com/capgemini-invent-lab/from-ocr-to-multimodal-a-new-era-in-image-to-text-technology-8d45d7559f01)
-   [76] Towards Semantic Equivalence of Tokenization in Multimodal LLM. (2025). ICLR. [https://iclr.cc/media/iclr-2025/Slides/28428.pdf](https://iclr.cc/media/iclr-2025/Slides/28428.pdf)
-   [77] Neuro-Symbolic AI and Multimodal Reasoning. (2025, July 27). Ajith P.com. [https://ajithp.com/2025/07/27/neuro-symbolic-ai-multimodal-reasoning/](https://ajithp.com/2025/07/27/neuro-symbolic-ai-multimodal-reasoning/)
-   [78] Building Multimodal RAG Systems. (n.d.). Elixir.ai. [https://www.elixirclaw.ai/blog/building-multimodal-rag-systems](https://www.elixirclaw.ai/blog/building-multimodal-rag-systems)
-   [79] What is multimodal RAG? (n.d.). IBM. [https://www.ibm.com/think/topics/multimodal-rag](https://www.ibm.com/think/topics/multimodal-rag)
-   [80] ColPali: Enhancing Financial Report Analysis with Multimodal RAG and Gemini. (2024, September 17). LearnOpenCV. [colpali-redefining-multimodal-rag-with-gemini.md](colpali-redefining-multimodal-rag-with-gemini.md)
-   [81] ColPali: Enhanced Document Retrieval with Vision-Language Models and ColBERT Strategy. (n.d.). Zilliz. [https://zilliz.com/blog/colpali-enhanced-doc-retrieval-with-vision-language-models-and-colbert-strategy](https://zilliz.com/blog/colpali-enhanced-doc-retrieval-with-vision-language-models-and-colbert-strategy)
-   [82] Sustainable AI. (n.d.). MLSysBook. [https://mlsysbook.ai/book/contents/core/sustainable_ai/sustainable_ai.html](https://mlsysbook.ai/book/contents/core/sustainable_ai/sustainable_ai.html)