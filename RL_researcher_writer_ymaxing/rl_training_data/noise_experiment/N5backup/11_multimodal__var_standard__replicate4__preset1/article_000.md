# Stop Converting Documents to Text. You're Doing It Wrong.

When I first started building AI agents, I hit a frustrating wall. I was comfortable manipulating text, but the moment I had to integrate multimodal data, such as images, audio, and especially documents like PDFs, my elegant architectures turned into messy hacks. I spent weeks building complex pipelines that tried to force everything into text. I chained OCR engines to scrape PDFs, layout detection models to identify tables, and separate classifiers to handle images. It was a brittle, slow, and expensive solution that broke every time a document layout changed.

The breakthrough came when I realized I was solving the wrong problem. I didn’t need to convert documents to text. I needed to treat them as images. Once I understood that every PDF page is effectively an image and that modern LLMs can “see” just as well as they can read, the complexity vanished. I could completely skip the OCR purgatory and focus on the three core inputs of an LLM: text, images, and audio.

This shift is essential because real-world AI applications rarely exist in a text-only vacuum. As human beings, we process information visually and audibly. Enterprise applications mirror this reality. They need to manipulate private data from warehouses and lakes that is inherently multimodal: financial reports with complex charts, technical diagrams, building sketches, and audio logs.

The old approach of normalizing everything to text is lossy. When you translate a complex diagram or a chart into text, you lose the spatial relationships, the colors, and the context. You lose the information that matters most. By processing data in its native format, we preserve this rich visual information, resulting in systems that are faster, cheaper, and significantly more performant.

Ultimately, as data is made for humans, you want the LLM to process the data as close as a human would, which often is visually.

Here is what we will cover:
- **Foundations of Multimodal LLMs:** An intuition on how models process visual and textual tokens together.
- **Practical Implementation:** How to work with images and PDFs using the Gemini API.
- **Multimodal State Management:** How to structure agent memory for mixed modalities.
- **Building the Agent:** A step-by-step guide to building a multimodal ReAct agent.

## The Need for Multimodal AI

We want to process multimodal data to access our surroundings. However, the rise of multimodal LLMs is driven by a more subtle force: enterprise requirements. Enterprise applications work heavily with documents. The most critical example illustrating the need for multimodal data is processing PDF documents. Once we walk through this example, you will see how this core problem maps to other modalities like image, audio, or video.

Previously, we tried to normalize everything to text before passing it into an AI model. This approach has many flaws because we lose a substantial amount of information during translation. For example, when encountering diagrams, charts, or sketches in a document, it is impossible to fully reproduce them in text.

Text-only approaches have significant limitations in various enterprise use cases. In financial analysis, models that cannot process charts miss crucial trends in reports. Similarly, a research assistant that ignores diagrams in scientific papers fails to grasp the core concepts. In healthcare, text-only systems cannot interpret medical imagery like X-rays, and in engineering, they are useless for understanding technical documentation filled with sketches and diagrams [[10]](https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai), [[25]](https://rasa.com/blog/multimodal-ai-use-cases), [[30]](https://www.nature.com/articles/s41598-025-98483-1).

The traditional document processing workflow, often used for invoices, documentation, or reports, relies on the following four essential steps:
1.  Document Preprocessing (e.g., Noise Removal)
2.  Layout Detection (Text, Tables, Diagrams)
3.  OCR Models (for Text) & Specialized Models (for Tables, Diagrams)
4.  Output Structured Data (JSON/Metadata)

This workflow has too many moving pieces. We need layout detection models, OCR models for text, and specialized models for each expected data structure, such as tables or charts. This makes the system rigid. If a document contains a chart type we do not have a model for, the pipeline fails. It is also slow and costly because we have to chain multiple model calls.

Most importantly, we face performance challenges. The multi-step nature creates a cascade effect where errors compound at each stage. Advanced OCR engines struggle with handwritten text, poor scans, stylized fonts, or complex layouts like nested tables and building sketches [[44]](https://conexiom.com/blog/the-6-biggest-ocr-problems-and-how-to-overcome-them), [[45]](https://unstructured.io/blog/unstructured-leads-in-document-parsing-quality-benchmarks-tell-the-full-story). Even with high-quality scanners, OCR-based solutions can have an accuracy as low as 60%, requiring significant manual correction [[46]](https://netfira.com/why-ocr-technology-fails-on-real-world-documents-and-how-intelligent-document-processing-can-help/).![A building sketch showing a crawl space vent diagram, illustrating the complexity of layouts that classic OCR systems struggle to interpret.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2dc40f3-dc13-486e-853d-8404368f4d8d_1616x1000.png)
Image 1: A building sketch showing a crawl space vent diagram, illustrating the complexity of layouts that classic OCR systems struggle to interpret. (Source [Vectorize.io](https://vectorize.io/blog/multimodal-rag-patterns) [[12]](https://vectorize.io/blog/multimodal-rag-patterns))

If we try to translate other data formats to text, we lose information. This is true for any modality:
- **Audio to Text:** We lose tone, pitch, and emotion.
- **Image to Text:** We lose spatial information, color, and context.
- **Video to Text:** We lose temporal dynamics and visual context.

Modern AI solutions use multimodal LLMs, such as Gemini, GPT-4o, or Claude. These models can directly interpret text, images, or PDFs as native input. This completely bypasses the unstable OCR workflow.

Thus, let’s understand how multimodal LLMs work.

## Foundations of Multimodal LLMs

To use LLMs with images and documents, you need an intuition of how multimodality works. You do not need to understand every research detail. But knowing the architecture helps you deploy, optimize, and monitor them.

There are two common approaches to building multimodal LLMs: the Unified Embedding Decoder Architecture and the Cross-modality Attention Architecture [[1]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms).![The two main approaches to developing multimodal LLM architectures.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76f50b57-2585-4cb8-8dda-eea5b5f81c03_1456x854.jpeg)
Image 2: The two main approaches to developing multimodal LLM architectures. (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms) [[1]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

### Unified Embedding Decoder Architecture

In this approach, we encode the text and image separately, concatenate their embeddings into a single vector, and pass the resulting vector to the LLM.

Thus, on top of a standard LLM architecture, you need a vision encoder that maps the image to an embedding that’s within the same vector space as the text. So, when the text and image embeddings are merged, the LLM can make sense of both.![Illustration of the unified embedding decoder architecture.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0979e82-2fb0-4f78-80c8-1395511e057f_1166x1400.jpeg)
Image 3: Illustration of the unified embedding decoder architecture. (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms) [[1]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

### Cross-modality Attention Architecture

In the second approach, instead of passing the image embeddings along with the text embeddings at the input, we inject them directly into the attention module. We still need an image encoder that projects the image into the same vector space as the text, but we inject it deeper within the architecture.![An illustration of the Cross-Modality Attention Architecture approach.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fea1b9ee4-0d19-4c3c-89db-06e779653da2_1296x1338.jpeg)
Image 4: An illustration of the Cross-Modality Attention Architecture approach. (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms) [[1]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

### Image Encoders

Both architectures rely on image encoders. To understand them, we can draw a parallel between text tokenization and image patching. Just as we split text into sub-word tokens, we split images into patches.![Image tokenization and embedding (left) and text tokenization and embedding (right) side by side.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a7104c0-3986-4aae-b918-06c393ff824c_1456x1154.jpeg)
Image 5: Image tokenization and embedding (left) and text tokenization and embedding (right) side by side. (Source [Understanding Multimodal LLMs](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms) [[1]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms))

The output has the same structure and dimensions as text embeddings. However, they need to be aligned in the vector space. We do this through a linear projection module. Popular image encoder models include CLIP, OpenCLIP, and SigLIP [[3]](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/).

Importantly, these encoders are also used in Multimodal RAG. They allow us to find semantic similarities between images and text.![Toy representation of multimodal embedding space.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d4c837a-a3e5-4d60-97ce-c4d4faf4cf57_841x616.png)
Image 6: Toy representation of multimodal embedding space. (Source [Multimodal Embeddings: An Introduction](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/) [[3]](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/))

You can replicate the same strategy between different modalities, such as text, image, document, and audio vectors, as long as you have an encoder that maps the data in the same vector space.

### Trade-offs and Modern Landscape

The **Unified Embedding Decoder** approach is simpler to implement and generally yields higher accuracy in OCR-related tasks. The **Cross-modality Attention** approach is more computationally efficient for high-resolution images because we do not have to pass all tokens as an input sequence. Instead, we inject them directly into the attention mechanism. Hybrid approaches exist to combine these benefits [[1]](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms), [[26]](https://github.com/cognitivetech/llm-research-summaries/blob/main/models-review/A-Comprehensive-Survey-and-Guide-to-Multimodal-Large-Language-Models-in-Vision-Language-Tasks.md).

In 2025, most leading LLMs are multimodal. Open-source examples include Llama, Gemma, and Qwen. Closed-source examples include GPT, Gemini, and Claude [[54]](https://medium.com/data-science-in-your-pocket/2025-the-year-ai-reasoning-models-took-over-a-month-by-month-review-of-frontier-breakthroughs-6ea2163f854f), [[57]](https://www.promptitude.io/post/ultimate-2025-ai-language-models-comparison-gpt5-gpt-4-claude-gemini-sonar-more).

A quick note on **Multimodal LLMs vs. Diffusion Models**: Diffusion models like Midjourney generate images from noise. Multimodal LLMs like GPT understand images and are architecturally different. In an agent workflow, diffusion models are typically used as tools, not as the reasoning model [[13]](https://arxiv.org/html/2409.14993v3).

Now that we understand how LLMs can directly input images or documents, let’s see how this works in practice.

## Applying Multimodal LLMs to Images and Documents

To better understand how multimodal LLMs work, let’s write a few examples using Gemini to show you some best practices when working with images and documents, such as PDFs.

There are three core ways to process multimodal data with LLMs:

1.  **Raw bytes:** The easiest way to work with LLMs. However, when storing the item in a database, it can easily get corrupted as most databases interpret the input as text/strings instead of bytes.
2.  **Base64:** A way to encode raw bytes as strings. This is useful for storing images or documents directly in a database (e.g., PostgreSQL, MongoDB) without corruption. The downside is that the file size increases by approximately 33%.
3.  **URLs:** The standard for enterprise scenarios. You store data in a data lake like AWS S3 or GCP Buckets. The LLM downloads the media directly from the bucket. As the file never sees your server, this reduces network latency for your application. This is the most efficient option for scale.

Now, let’s dig into the code. We will show you a couple of simple examples of how to manipulate images and PDFs with these 3 methods using the Google GenAI SDK. In the following sections, we will build a simple agent that combines everything into a single unified layer.

1. First, we set up our client and display a sample image.
   ```python
   from google import genai
   from google.genai import types
   from PIL import Image
   import io
   
   client = genai.Client()
   MODEL_ID = “gemini-2.5-flash”
   ```

2. We load the image as **raw bytes**. We use `WEBP` format because it is efficient. For example, we can call the LLM to generate a caption for an image or compare two images.
   ```python
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
   ```text
   Caption: This striking image features a massive, dark metallic robot, its powerful form detailed with intricate circuit patterns on its head and piercing red glowing eyes. Perched playfully on its right arm is a small, fluffy grey tabby kitten, its front paw raised as if exploring or batting at the robot's armored limb, while its gaze is directed slightly off-frame. The robot's large, segmented hand is visible beneath the kitten. The background suggests an industrial or workshop environment, with hints of metal structures and natural light filtering in from an unseen window, creating a dramatic contrast between the soft, vulnerable kitten and the formidable, mechanical sentinel.
   
   Difference: The primary difference between the two images lies in the nature of the interaction depicted and their respective settings. In the first image, a small, grey kitten is shown curiously interacting with a large, metallic robot, gently perched on its arm within what appears to be a clean, well-lit workshop or industrial space. Conversely, the second image portrays a tense and aggressive confrontation between a fluffy white dog and a sleek black robot, both in combative stances, amidst a cluttered and grimy urban alleyway filled with trash and graffiti.
   ```

3. We can also process the image as a **Base64 encoded string**. Notice that the logic is similar, but we encode the bytes first.
   ```python
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
   If we compute the difference in size between base64 and bytes, the base64 one will be ~33% larger.
   ```python
   f”Size increase: {(len(image_base64) - len(image_bytes_1)) / len(image_bytes_1) * 100:.2f}%”
   ```

4. For **URLs**, Gemini works like a charm with GCS Buckets.
   ```python
   response = client.models.generate_content(
       model=MODEL_ID,
       contents=[\
           types.Part.from_uri(uri=”gs://gemini-images/image_1.jpeg”, mime_type=”image/webp”),\
           “Tell me what is in this image.”,\
       ],
   )
   ```

5. Let’s try a more complex task: **Object Detection**. We use Pydantic to define the output structure, using the knowledge from Lesson 3.
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
   ```text
   bounding_boxes=[BoundingBox(ymin=1.0, xmin=450.0, ymax=997.0, xmax=1000.0, label='robot'), BoundingBox(ymin=269.0, xmin=39.0, ymax=782.0, xmax=530.0, label='kitten')]
   ```
   ![Object detection results for the image with the kitten and the robot.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2eaed1f-bedb-4c33-98b3-96fa7424f0ad_566x590.png)
   Image 7: Object detection results for the image with the kitten and the robot.

6. Now, let’s process **PDFs**. Because we use a multimodal model, the process is identical to images. We load the PDF as bytes and pass it to the model.
   ```python
   pdf_bytes = open(”pdfs/attention_is_all_you_need_paper.pdf”, “rb”).read()
   
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
   ```text
   This document introduces the Transformer, a novel neural network architecture for sequence transduction models, primarily applied to machine translation.
   ```

7. We can also process **PDFs as public URLs**. This is useful for analyzing documents directly from the web without downloading them first. We use the `url_context` tool.
   ```python
   response = client.models.generate_content(
       model=MODEL_ID,
       contents=”Based on the provided paper as a PDF, tell me how ReAct works: https://arxiv.org/pdf/2210.03629”,
       config=types.GenerateContentConfig(tools=[{”url_context”: {}}]),
   )
   print(response.text)
   ```
   It outputs:
   ```text
   ReAct is a novel paradigm for large language models (LLMs) that combines reasoning (Thought) and acting (Action) in an interleaved manner to solve diverse language and decision-making tasks.
   ```

8. Finally, we can perform **Object Detection on PDF pages**. This is powerful for extracting diagrams or tables. We treat the PDF page as an image.
   ```python
   page_image_bytes = load_image_as_bytes(”images/attention_is_all_you_need_1.jpeg”)
   
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
   ![Object detection results for a page from the "Attention Is All You Need" paper.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7cb5566-8dea-4468-b307-b79b7610c7fa_667x590.png)
   Image 8: Object detection results for a page from the "Attention Is All You Need" paper.

Processing PDFs as images is a concept popularized by the ColPali paper, which demonstrated that modern Vision Language Models (VLMs) can retrieve documents more effectively by “looking” at them rather than extracting text [[5]](https://arxiv.org/pdf/2407.01449v6). This ability to 'see' documents opens up powerful new possibilities for AI agents, which need to manage and reason over diverse data types. Let's explore how we can build an agent that leverages these multimodal foundations.

## Foundations of Multimodal AI Agents

What if we want to use these methods within an Agent?

Agents manage their internal state, the short-term memory, as a list of messages. This usually translates to a list of dictionaries or JSON objects. When transitioning from text-only to multimodal, the structure changes slightly. We need a way to flag the data type and model the data using the formats we just discussed (URL, Base64, Binary).

We move from a list of text-only JSONs to a list of JSONs containing a mix of modalities. Each item can be text, an image, or audio. As long as the LLM can process these modalities, our job is to properly manage them in short-term memory, retrieve them from long-term memory, and pass them in the right encoding.![The transition of an AI agent’s short-term memory from a text-only to a multimodal representation.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90c2c4cb-f95d-4744-bd04-268dc4a7c295_1200x1200.png)
Image 9: The transition of an AI agent’s short-term memory from a text-only to a multimodal representation.

Retrieval becomes more interesting in this context. We still query our long-term memory, but now we can use multimodal similarities. We can use an image from short-term memory to query for similar images, documents, or audio chunks.

From an architectural point of view, a multimodal agentic RAG looks like any other agentic RAG system. However, this is where you will feel the real need for **semantic search**. With text, you can get far with keyword filters or SQL. But with images or audio, you cannot rely on keywords. You must use vector similarity to find relationships between data types.

Let’s see how we can model this bag of mixed messages with an example.

## Building Multimodal AI Agents

Let’s take this further and design an agentic RAG system. We assume we have a vector database filled with images, audio data, PDFs (converted to images), and text. We also assume we have a multimodal embedding model that supports text-to-image, image-to-audio, and text-to-audio embeddings.

For simplicity, we will mock the retrieval tools that access our vector database and other servers for Google Drive or local screenshots.![Agent Interacting With Multimodal Memory](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F246dbcab-68dc-41eb-983e-4f2bf5d48fa9_1200x1200.png)
Image 10: Agent Interacting With Multimodal Memory

Our main focus is on managing the short-term memory as a list of mixed-modality JSONs. We want the agent to retrieve context from its current multimodal state, leveraging its multimodal retrieval tools, provide an answer, and repeat until the task is complete.

1. First, we define our multimodal tools. In a real application, these would query a vector DB like Qdrant or Pinecone using a multimodal embedding model.
   ```python
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
   ```python
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

3. We build the `react_agent` and run it with a query that requires multimodal reasoning: `“Based on what I am looking at, retrieve all relevant images, audio, and documents.”`
   ```python
   agent = build_react_agent()
   
   response = agent.invoke({”messages”: [”Based on what I am looking at, retrieve all relevant images, audio and documents”]})
   ```

4. Let’s look at a potential reasoning trace. The agent first calls `computer_screen_shoot_tool`, which returns a Base64 image. This is appended to the message history.
   ```json
   {
     "role": "tool",
     "name": "computer_screen_shoot_tool",
     "parts": [\
       {\
         "inline_data": {\
           "mime_type": "image/jpeg",\
           "data": "/9j/4AAQSkZJRg..."\
         }\
       }\
     ]
   }
   ```

5. The agent now has the image in its context. It analyzes the visual content and decides to call retrieval tools in parallel, passing the image data from the previous turn.
   ```python
   function_calls = [\
     {\
       "tool_name": "image_to_image_search_tool",\
       "tool_args": {\
         "image_data": "<base64_image_from_previous_turn>"\
       }\
     },\
     {\
       "tool_name": "image_audio_search_tool",\
       "tool_args": {\
         "image_data": "<base64_image_from_previous_turn>"\
       }\
     },\
   ]
   ```

6. The tools execute and return mixed modalities. The state is updated with these new observations, adding audio, images, and document pages to the context.
   ```json
   [\
     {\
       "role": "tool",\
       "name": "image_to_image_search_tool",\
       "parts": [\
         { "text": "Found 3 similar images:" },\
         {\
           "inline_data": {\
             "mime_type": "image/jpeg",\
             "data": "..."\
           }\
         }\
       ]\
     },\
     {\
       "role": "tool",\
       "name": "google_drive_document_search_tool",\
       "parts": [\
         { "text": "Found document from Google Drive (stored in GCS bucket):" },\
         {\
           "file_data": {\
             "mime_type": "application/pdf",\
             "file_uri": "gs://my-bucket/documents/british-shorthair-guide.pdf"\
           }\
         }\
       ]\
     }\
   ]
   ```

7. The agent compiles this into a final answer.
   ```text
   I analyzed your screen and found you are looking at a gray kitten.
   Based on this, I retrieved:
   1. 3 similar images of gray kittens (from image_to_image_search_tool, as base64).
   2. An audio clip of a cat purring (from image_audio_search_tool, as binary data).
   3. A PDF page about cat breeds (from image_document_search_tool, as base64 image).
   4. A document from Google Drive about British Shorthair cats (from google_drive_document_search_tool, stored as URL in GCS bucket).
   ```

8. We can now ask a follow-up question: `“What is the color of my kitten?”`
   ```python
   response = agent.invoke({”messages”: [”What is the color of my kitten?”]})
   ```
   Because the agent has the image in its short-term memory, it does not need to use tools again. It simply looks at the Base64 data from the first step and answers:
   ```text
   Your kitten is gray.
   ```

Nothing fundamental has changed in how we structure our data when switching from text-only to multimodal agents. We simply reflect the data types within the JSONs. The key is that our LLM knows how to process that data. The hard part is retrieving the correct multimodal data from our databases and indexing it properly.

## Conclusion

Working with multimodal data is a fundamental skill for AI engineers. Modern AI applications rarely exist in a text-only vacuum. They interact with the complex, visual, and auditory reality of the world.

In this lesson, we moved away from the unstable, multi-step OCR pipelines of the past. We learned that modern LLMs can natively process images and documents, preserving rich context that was previously lost. We explored how to handle data as bytes, Base64, and URLs, and how to build agents that can reason across these modalities.

The principles you learned for images and documents extend to other formats like audio and video. Instead of relying on text transcripts, which lose nuance, agentic workflows can perform visual searches on video frames—for example, finding a clip of a "person wearing a hard hat"—or analyze audio for specific events, creating richer context [[62]](https://www.ragie.ai/blog/how-we-built-multimodal-rag-for-audio-and-video), [[63]](https://aimagazine.com/articles/multimodal-rag-agentic-finastra-data-scientist-talk-2025).

This concludes our *AI Agents Foundations* series. We started by understanding the difference between workflows and agents, mastered context engineering and structured outputs, built robust planning capabilities with ReAct, and finally gave our agents eyes and ears. You now have the foundational blocks to build production-ready AI systems.

## References

- [1] Raschka, S. (2024, October 21). Understanding multimodal LLMS. *Sebastian Raschka*. [https://magazine.sebastianraschka.com/p/understanding-multimodal-llms](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms)
- [2] Vision language models. (n.d.). NVIDIA. [https://www.nvidia.com/en-us/glossary/vision-language-models/](https://www.nvidia.com/en-us/glossary/vision-language-models/)
- [3] Talebi, S. (2024, November 13). Multimodal embeddings: An introduction. *Medium*. [https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/](https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f/)
- [4] Multi-modal ML with OpenAI’s CLIP. (n.d.). Pinecone. [https://www.pinecone.io/learn/series/image-search/clip/](https://www.pinecone.io/learn/series/image-search/clip/)
- [5] Fostiropoulos, I., et al. (2024). ColPali: Efficient Document Retrieval with Vision Language Models. *arXiv*. [https://arxiv.org/pdf/2407.01449v6](https://arxiv.org/pdf/2407.01449v6)
- [6] Image understanding. (n.d.). Google AI for Developers. [https://ai.google.dev/gemini-api/docs/image-understanding](https://ai.google.dev/gemini-api/docs/image-understanding)
- [7] Google generative AI embeddings. (n.d.). LangChain. [https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/](https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/)
- [8] Agents. (n.d.). LangChain. [https://langchain-ai.github.io/langgraph/agents/agents/](https://langchain-ai.github.io/langgraph/agents/agents/)
- [9] Complex Document Recognition: OCR Doesn’t Work and Here’s How You Fix It. (n.d.). *HackerNoon*. [https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it](https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it)
- [10] What are some real-world applications of multimodal AI? (n.d.). Milvus. [https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai](https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai)
- [11] Liu, J. (2025, February 24). OlmOCR-bench review: Insights and pitfalls on an OCR benchmark. *LlamaIndex*. [https://www.llamaindex.ai/blog/olmocr-bench-review-insights-and-pitfalls-on-an-ocr-benchmark](https://www.llamaindex.ai/blog/olmocr-bench-review-insights-and-pitfalls-on-an-ocr-benchmark)
- [12] Vectorize.io. (2024, October 26). Multimodal RAG Patterns. *Vectorize.io Blog*. [https://vectorize.io/blog/multimodal-rag-patterns](https://vectorize.io/blog/multimodal-rag-patterns)
- [13] Wang, X., et al. (2025). Multi-modal Generative AI: Multi-modal LLMs, Diffusions, and the Unification. *arXiv*. [https://arxiv.org/html/2409.14993v3](https://arxiv.org/html/2409.14993v3)
- [14] Dey, S. (2024, June 14). Multimodal RAG architecture. *LinkedIn*. [https://www.linkedin.com/posts/sayandey01_generativeai-llm-rag-activity-7412381316106760192-nFx3](https://www.linkedin.com/posts/sayandey01_generativeai-llm-rag-activity-7412381316106760192-nFx3)
- [15] Evaluating Multimodal vs. Text-Based Retrieval for RAG with Snowflake Cortex. (2025, April 21). *Snowflake*. [https://www.snowflake.com/en/engineering-blog/arctic-agentic-rag-multimodal-pdf-retrieval/](https://www.snowflake.com/en/engineering-blog/arctic-agentic-rag-multimodal-pdf-retrieval/)
- [16] Pathway. (n.d.). Multimodal RAG. [https://pathway.com/developers/templates/rag/multimodal-rag](https://pathway.com/developers/templates/rag/multimodal-rag)
- [17] Aggarwal, G. (2024, June 17). MMCTAgent. *LinkedIn*. [https://www.linkedin.com/posts/gauravagg_mmctagent-enables-multimodal-reasoning-over-activity-7413983881181339648--PyD](https://www.linkedin.com/posts/gauravagg_mmctagent-enables-multimodal-reasoning-over-activity-7413983881181339648--PyD)
- [18] Multimodal RAG Explained: From Text to Images and Beyond. (2024, July 24). *USAII*. [https://www.usaii.org/ai-insights/multimodal-rag-explained-from-text-to-images-and-beyond](https://www.usaii.org/ai-insights/multimodal-rag-explained-from-text-to-images-and-beyond)
- [19] LLMs on Anyscale. (n.d.). *Anyscale*. [https://docs.anyscale.com/llm](https://docs.anyscale.com/llm)
- [20] Zhang, C. (2026, March 25). How to Choose the Best Embedding Model for RAG in 2026. *Milvus*. [https://milvus.io/blog/choose-embedding-model-rag-2026.md](https://milvus.io/blog/choose-embedding-model-rag-2026.md)
- [21] Fostiropoulos, I. (2024, November 11). eager-embed-v1. *eagerworks*. [https://eagerworks.com/blog/best-embedding-model-for-rag](https://eagerworks.com/blog/best-embedding-model-for-rag)
- [22] Top Embedding Models in 2025. (2024, December 1). *ArtSmart.ai*. [https://artsmart.ai/blog/top-embedding-models-in-2025/](https://artsmart.ai/blog/top-embedding-models-in-2025/)
- [23] Kanerika. (2024, November 15). Multimodal AI Agents. *Kanerika*. [https://kanerika.com/blogs/multimodal-ai-agents/](https://kanerika.com/blogs/multimodal-ai-agents/)
- [24] Multimodal Enterprise AI. (2024, October 29). *Invisible Technologies*. [https://invisibletech.ai/blog/multimodal-enterprise-ai](https://invisibletech.ai/blog/multimodal-enterprise-ai)
- [25] Multimodal AI Use Cases. (2024, July 10). *Rasa*. [https://rasa.com/blog/multimodal-ai-use-cases](https://rasa.com/blog/multimodal-ai-use-cases)
- [26] A Comprehensive Survey and Guide to Multimodal Large Language Models in Vision-Language Tasks. (2024, July 1). *GitHub*. [https://github.com/cognitivetech/llm-research-summaries/blob/main/models-review/A-Comprehensive-Survey-and-Guide-to-Multimodal-Large-Language-Models-in-Vision-Language-Tasks.md](https://github.com/cognitivetech/llm-research-summaries/blob/main/models-review/A-Comprehensive-Survey-and-Guide-to-Multimodal-Large-Language-Models-in-Vision-Language-Tasks.md)
- [27] Multimodal AI Examples: How It Works, Real-World Applications, and Future Trends. (2024, November 25). *SmartDev*. [https://smartdev.com/multimodal-ai-examples-how-it-works-real-world-applications-and-future-trends/](https://smartdev.com/multimodal-ai-examples-how-it-works-real-world-applications-and-future-trends/)
- [28] What is a multimodal LLM? (n.d.). *IBM*. [https://www.ibm.com/think/topics/multimodal-llm](https://www.ibm.com/think/topics/multimodal-llm)
- [29] Wu, C., et al. (2025). A survey on multimodal large language models for medical applications. *PMC*. [https://pmc.ncbi.nlm.nih.gov/articles/PMC12479233/](https://pmc.ncbi.nlm.nih.gov/articles/PMC12479233/)
- [30] Multimodal AI in Healthcare. (2025, May 15). *Nature*. [https://www.nature.com/articles/s41598-025-98483-1](https://www.nature.com/articles/s41598-025-98483-1)
- [31] Why traditional OCR fails for complex business documents. (2024, May 22). *Microsoft Learn*. [https://learn.microsoft.com/en-us/answers/questions/5668164/why-traditional-ocr-fails-for-complex-business-doc?page=1](https://learn.microsoft.com/en-us/answers/questions/5668164/why-traditional-ocr-fails-for-complex-business-doc?page=1)
- [32] Document Processing Automation Guide. (2024, July 29). *Parseur*. [https://parseur.com/blog/document-processing-automation-guide](https://parseur.com/blog/document-processing-automation-guide)
- [33] AI-Powered PDF Data Extraction in Clinical Research. (2024, June 12). *Intuition Labs*. [https://intuitionlabs.ai/articles/ai-pdf-data-extraction-clinical-research](https://intuitionlabs.ai/articles/ai-pdf-data-extraction-clinical-research)
- [34] Gemini consistently producing valid Pydantic responses. (2024, August 15). *Google AI Community*. [https://discuss.ai.google.dev/t/gemini-consistently-producing-valid-pydantic-responses/98992](https://discuss.ai.google.dev/t/gemini-consistently-producing-valid-pydantic-responses/98992)
- [35] Iusztin, P. (2025, December 9). Stop Converting Documents to Text. You're Doing It Wrong. *Decoding AI*. [https://www.decodingai.com/p/stop-converting-documents-to-text](https://www.decodingai.com/p/stop-converting-documents-to-text)
- [36] LLM Output Parsing and Structured Generation with Pydantic. (2024, September 5). *Tetrate*. [https://tetrate.io/learn/ai/llm-output-parsing-structured-generation](https://tetrate.io/learn/ai/llm-output-parsing-structured-generation)
- [37] Structured Outputs with Multimodal Gemini. (2024, October 23). *Instructor*. [https://python.useinstructor.com/blog/2024/10/23/structured-outputs-with-multimodal-gemini/](https://python.useinstructor.com/blog/2024/10/23/structured-outputs-with-multimodal-gemini/)
- [38] Steering Large Language Models with Pydantic. (2024, November 1). *Pydantic*. [https://pydantic.dev/articles/llm-intro](https://pydantic.dev/articles/llm-intro)
- [39] Multimodal Semantic Search. (2024, August 20). *OpenSearch*. [https://opensearch.org/blog/multimodal-semantic-search/](https://opensearch.org/blog/multimodal-semantic-search/)
- [40] Joint Visual-Textual Embedding for Multimodal Style Search. (2017). *Amazon Science*. [https://assets.amazon.science/89/bf/661d950d4059930c8f1d2e449ac6/joint-visual-textual-embedding-for-multimodal-style-search.pdf](https://assets.amazon.science/89/bf/661d950d4059930c8f1d2e449ac6/joint-visual-textual-embedding-for-multimodal-style-search.pdf)
- [41] Combine Image and Text: How Multimodal Retrieval Transforms Search. (2024, September 10). *Zilliz*. [https://zilliz.com/blog/combine-image-and-text-how-multimodal-retrieval-transforms-search](https://zilliz.com/blog/combine-image-and-text-how-multimodal-retrieval-transforms-search)
- [42] Multimodal Sentence Transformers. (2024, October 15). *Hugging Face*. [https://huggingface.co/blog/multimodal-sentence-transformers](https://huggingface.co/blog/multimodal-sentence-transformers)
- [43] OCR Accuracy Explained: How to Improve It. (2024, November 5). *LlamaIndex*. [https://www.llamaindex.ai/blog/ocr-accuracy](https://www.llamaindex.ai/blog/ocr-accuracy)
- [44] The 6 Biggest OCR Problems and How to Overcome Them. (2023, August 8). *Conexiom*. [https://conexiom.com/blog/the-6-biggest-ocr-problems-and-how-to-overcome-them](https://conexiom.com/blog/the-6-biggest-ocr-problems-and-how-to-overcome-them)
- [45] Unstructured Leads in Document Parsing Quality. (2024, March 14). *Unstructured.io*. [https://unstructured.io/blog/unstructured-leads-in-document-parsing-quality-benchmarks-tell-the-full-story](https://unstructured.io/blog/unstructured-leads-in-document-parsing-quality-benchmarks-tell-the-full-story)
- [46] Why OCR Technology Fails on Real-World Documents. (2023, November 21). *Netfira*. [https://netfira.com/why-ocr-technology-fails-on-real-world-documents-and-how-intelligent-document-processing-can-help/](https://netfira.com/why-ocr-technology-fails-on-real-world-documents-and-how-intelligent-document-processing-can-help/)
- [47] Financial Summarization with USTT. (2023). *IJCAI*. [https://www.ijcai.org/proceedings/2023/0581.pdf](https://www.ijcai.org/proceedings/2023/0581.pdf)
- [48] EPOCH framework for AI in finance. (2025). *arXiv*. [https://arxiv.org/html/2503.22035v1](https://arxiv.org/html/2503.22035v1)
- [49] 10 real-world examples of AI in healthcare. (2022, November 24). *Philips*. [https://www.philips.com/a-w/about/news/archive/features/2022/20221124-10-real-world-examples-of-ai-in-healthcare.html](https://www.philips.com/a-w/about/news/archive/features/2022/20221124-10-real-world-examples-of-ai-in-healthcare.html)
- [50] Exploring Multimodal LLMs. (2024, June 5). *SparkCognition*. [https://sparkco.ai/blog/exploring-multimodal-llms-text-image-and-video-integration](https://sparkco.ai/blog/exploring-multimodal-llms-text-image-and-video-integration)
- [51] Multimodal LLMs. (n.d.). *Emergent Mind*. [https://www.emergentmind.com/topics/multimodal-llms](https://www.emergentmind.com/topics/multimodal-llms)
- [52] Enhancing LLM Capabilities: The Power of Multimodal LLMs and RAG. (2024, May 1). *Towards AI*. [https://towardsai.net/p/l/enhancing-llm-capabilities-the-power-of-multimodal-llms-and-rag](https://towardsai.net/p/l/enhancing-llm-capabilities-the-power-of-multimodal-llms-and-rag)
- [53] Evolution from LLMs to MLLMs. (2024, November 11). *arXiv*. [https://arxiv.org/html/2411.06284v3](https://arxiv.org/html/2411.06284v3)
- [54] 2025: The Year AI Reasoning Models Took Over. (2025, May 29). *Medium*. [https://medium.com/data-science-in-your-pocket/2025-the-year-ai-reasoning-models-took-over-a-month-by-month-review-of-frontier-breakthroughs-6ea2163f854f](https://medium.com/data-science-in-your-pocket/2025-the-year-ai-reasoning-models-took-over-a-month-by-month-review-of-frontier-breakthroughs-6ea2163f854f)
- [55] Breakdown of 2025 Flagship LLM Architectures. (2025, July 21). *LinkedIn*. [https://www.linkedin.com/posts/progressivethinker_this-is-the-most-essential-breakdown-of-2025-activity-7376654335319117825-a5aD](https://www.linkedin.com/posts/progressivethinker_this-is-the-most-essential-breakdown-of-2025-activity-7376654335319117825-a5aD)
- [56] Comparison of Coding LLMs. (2025, August 1). *Preprints.org*. [https://www.preprints.org/manuscript/202508.1904](https://www.preprints.org/manuscript/202508.1904)
- [57] Ultimate 2025 AI Language Models Comparison. (2025, June 10). *Promptitude*. [https://www.promptitude.io/post/ultimate-2025-ai-language-models-comparison-gpt5-gpt-4-claude-gemini-sonar-more](https://www.promptitude.io/post/ultimate-2025-ai-language-models-comparison-gpt5-gpt-4-claude-gemini-sonar-more)
- [58] Vaswani, A., et al. (2017). Attention Is All You Need. *arXiv*. [https://arxiv.org/abs/1706.03762](https://arxiv.org/abs/1706.03762)
- [59] What Is Optical Character Recognition (OCR)?. (2023, November 21). *Roboflow Blog*. [https://blog.roboflow.com/what-is-optical-character-recognition-ocr/](https://blog.roboflow.com/what-is-optical-character-recognition-ocr/)
- [60] Multimodal RAG with Colpali, Milvus and VLMs. (2024, December 10). *Hugging Face*. [https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag](https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag)
- [61] The 8 best AI image generators in 2025. (2026, April 1). *Zapier*. [https://zapier.com/blog/best-ai-image-generator/](https://zapier.com/blog/best-ai-image-generator/)
- [62] How We Built Multimodal RAG for Audio and Video. (2024). *RAGIE AI*. [https://www.ragie.ai/blog/how-we-built-multimodal-rag-for-audio-and-video](https://www.ragie.ai/blog/how-we-built-multimodal-rag-for-audio-and-video)
- [63] Multimodal RAG and Agentic AI. (2025). *AI Magazine*. [https://aimagazine.com/articles/multimodal-rag-agentic-finastra-data-scientist-talk-2025](https://aimagazine.com/articles/multimodal-rag-agentic-finastra-data-scientist-talk-2025)