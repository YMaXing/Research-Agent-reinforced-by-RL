"""
Repair inline citations in article.md for 11_multimodal__preset0.

Problem: Grok generated a full References section but zero inline [[N]](url) citations
in the body text. This script:
1. Removes irrelevant references [1]-[26] (from other lessons)
2. Renumbers references [27]-[40] and adds new research-sourced references
3. Inserts inline citations at factual claims throughout the body
4. Writes repaired article.md and article_002.md
"""
from pathlib import Path
import re
import shutil

EPISODE_DIR = Path(__file__).resolve().parent

# ---------------------------------------------------------------------------
# New reference mapping (clean, multimodal-relevant only)
# ---------------------------------------------------------------------------
REFS = {
    1: ("Understanding Multimodal LLMs", "https://magazine.sebastianraschka.com/p/understanding-multimodal-llms"),
    2: ("Vision Language Models", "https://www.nvidia.com/en-us/glossary/vision-language-models/"),
    3: ("Multimodal Embeddings: An Introduction", "https://towardsdatascience.com/multimodal-embeddings-an-introduction-5dc36975966f"),
    4: ("Multi-modal ML with OpenAI's CLIP", "https://www.pinecone.io/learn/series/image-search/clip/"),
    5: ("ColPali: Efficient Document Retrieval with Vision Language Models", "https://arxiv.org/pdf/2407.01449v6"),
    6: ("Image understanding with Gemini", "https://ai.google.dev/gemini-api/docs/image-understanding"),
    7: ("Multimodal RAG with Colpali, Milvus and VLMs", "https://huggingface.co/blog/saumitras/colpali-milvus-multimodal-rag"),
    8: ("LangGraph Quickstart", "https://langchain-ai.github.io/langgraph/agents/agents/"),
    9: ("Complex Document Recognition: OCR Doesn't Work", "https://hackernoon.com/complex-document-recognition-ocr-doesnt-work-and-heres-how-you-fix-it"),
    10: ("Real-world applications of multimodal AI", "https://milvus.io/ai-quick-reference/what-are-some-realworld-applications-of-multimodal-ai"),
    11: ("What Is Optical Character Recognition (OCR)?", "https://blog.roboflow.com/what-is-optical-character-recognition-ocr/"),
    12: ("OCR Accuracy", "https://www.llamaindex.ai/blog/ocr-accuracy"),
    13: ("Overcoming OCR Errors and Limitations", "https://jiffy.ai/overcoming-ocr-errors-and-limitations-with-intelligent-document-processing/"),
    14: ("ChatGPT Financial Analysis", "https://konfuzio.com/en/chatgpt-financial-analysis/"),
    15: ("Medical Imaging AI", "https://techtoday.lenovo.com/sites/default/files/2025-05/Medical%20Imaging%20White%20Paper%20NVIDIA%20and%20Lenovo.pdf"),
    16: ("Google Generative AI Embeddings", "https://python.langchain.com/docs/integrations/text_embedding/google_generative_ai/"),
    17: ("Multimodal AI Agents", "https://kanerika.com/blogs/multimodal-ai-agents/"),
    18: ("Why Traditional OCR Fails for Complex Business Documents", "https://learn.microsoft.com/en-us/answers/questions/5668164/why-traditional-ocr-fails-for-complex-business-doc"),
    19: ("Snowflake Arctic: Agentic RAG with Multimodal PDF Retrieval", "https://www.snowflake.com/en/engineering-blog/arctic-agentic-rag-multimodal-pdf-retrieval/"),
    20: ("Stop Converting Documents to Text", "https://www.decodingai.com/p/stop-converting-documents-to-text"),
}


def cite(n: int) -> str:
    """Return inline citation string [[N]](url)."""
    _, url = REFS[n]
    return f"[[{n}]]({url})"


def build_references_section() -> str:
    """Build a clean ## References section."""
    lines = ["## References\n"]
    for n in sorted(REFS):
        title, url = REFS[n]
        lines.append(f"- [{n}] {title} ({url})\n")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Inline citation insertions
# Each entry: (unique_old_text, replacement_text)
# The old_text must be unique in the article body.
# ---------------------------------------------------------------------------
INSERTIONS: list[tuple[str, str]] = [
    # ---- Section 1 (Introduction) ----
    # OCR accuracy stats in intro paragraph
    (
        "Enterprise APIs improve the numbers on standard forms yet still degrade sharply on irregular layouts, heavy tables, or mixed handwriting and print.",
        f"Enterprise APIs improve the numbers on standard forms yet still degrade sharply on irregular layouts, heavy tables, or mixed handwriting and print {cite(12)}.",
    ),
    # Financial analysts
    (
        "Financial analysts querying reports lose the meaning carried by charts.",
        f"Financial analysts querying reports lose the meaning carried by charts {cite(14)}.",
    ),
    # Medical teams
    (
        "Medical teams reviewing imaging alongside notes cannot rely on text-only summaries. Technical teams searching documentation with embedded sketches receive incomplete answers.",
        f"Medical teams reviewing imaging alongside notes cannot rely on text-only summaries {cite(15)}. Technical teams searching documentation with embedded sketches receive incomplete answers {cite(9)}.",
    ),
    # Building sketches break OCR (Section 1)
    (
        "Building sketches, X-rays, noisy handwritten forms, and multi-page tables with merged cells all break the assumptions baked into template-driven OCR systems. The pipelines themselves compound the problem.",
        f"Building sketches, X-rays, noisy handwritten forms, and multi-page tables with merged cells all break the assumptions baked into template-driven OCR systems {cite(18)}. The pipelines themselves compound the problem.",
    ),
    # Modern multimodal LLMs (Section 1)
    (
        "Modern multimodal LLMs address the root cause by processing images and documents in their native visual form. A single model ingests text, layout, charts, diagrams, and photographs together, preserving the complete context a human reader would use. The pipeline collapses from many brittle steps into one robust forward pass. Accuracy on visually complex content improves, latency decreases, and maintenance burden shrinks. This lesson shows exactly how to build those systems.",
        f"Modern multimodal LLMs address the root cause by processing images and documents in their native visual form {cite(1)}, {cite(20)}. A single model ingests text, layout, charts, diagrams, and photographs together, preserving the complete context a human reader would use. The pipeline collapses from many brittle steps into one robust forward pass. Accuracy on visually complex content improves, latency decreases, and maintenance burden shrinks. This lesson shows exactly how to build those systems.",
    ),

    # ---- Section 2 (Limitations) ----
    # OCR stats in Section 2 (different paragraph from Section 1)
    (
        "Enterprise APIs improve the numbers on standard forms yet still degrade sharply on irregular layouts, heavy tables, or mixed handwriting and print.\n\nReal enterprise use cases",
        f"Enterprise APIs improve the numbers on standard forms yet still degrade sharply on irregular layouts, heavy tables, or mixed handwriting and print {cite(12)}, {cite(11)}.\n\nReal enterprise use cases",
    ),
    # Text-only summarization of financial reports
    (
        "Text-only summarization of financial reports ignores the very charts and tables that contain the most salient data, producing incomplete or factually inconsistent outputs.",
        f"Text-only summarization of financial reports ignores the very charts and tables that contain the most salient data, producing incomplete or factually inconsistent outputs {cite(14)}.",
    ),
    # Research assistants, medical teams
    (
        "Research assistants processing papers lose the meaning carried by diagrams and spatial layouts. Medical teams reviewing imaging alongside notes cannot rely on text-only summaries.",
        f"Research assistants processing papers lose the meaning carried by diagrams and spatial layouts. Medical teams reviewing imaging alongside notes cannot rely on text-only summaries {cite(15)}.",
    ),
    # Building sketches in Section 2
    (
        "Building sketches, X-rays, noisy handwritten forms, and multi-page tables with merged cells all break the assumptions baked into template-driven OCR systems.\n\n```mermaid\nflowchart TD\n    A[Building Sketch",
        f"Building sketches, X-rays, noisy handwritten forms, and multi-page tables with merged cells all break the assumptions baked into template-driven OCR systems {cite(18)}.\n\n```mermaid\nflowchart TD\n    A[Building Sketch",
    ),
    # Predefined positional rules
    (
        "Most rely on predefined positional rules or templates that work only for fixed layouts. Any change in format requires manual rule updates and ongoing monitoring. The absence of genuine contextual understanding means numbers without units, ambiguous terms, or cross-referenced data are misinterpreted.",
        f"Most rely on predefined positional rules or templates that work only for fixed layouts. Any change in format requires manual rule updates and ongoing monitoring {cite(13)}. The absence of genuine contextual understanding means numbers without units, ambiguous terms, or cross-referenced data are misinterpreted {cite(13)}.",
    ),
    # Modern multimodal LLMs in Section 2 closing
    (
        "Modern multimodal LLMs address the root cause by processing images and documents in their native visual form. A single model ingests text, layout, charts, diagrams, and photographs together, preserving the complete context a human reader would use. The pipeline collapses from many brittle steps into one robust forward pass. Accuracy on visually complex content improves, latency decreases, and maintenance burden shrinks. The next section explains the architectural foundations that make this possible.",
        f"Modern multimodal LLMs address the root cause by processing images and documents in their native visual form {cite(1)}. A single model ingests text, layout, charts, diagrams, and photographs together, preserving the complete context a human reader would use. The pipeline collapses from many brittle steps into one robust forward pass. Accuracy on visually complex content improves, latency decreases, and maintenance burden shrinks. The next section explains the architectural foundations that make this possible.",
    ),

    # ---- Section 3 (Foundations of multimodal LLMs) ----
    # Unified embedding decoder architecture
    (
        "These image tokens are then concatenated with text tokens and fed into the decoder exactly as if they were additional words. The model's self-attention layers learn to reason jointly over both modalities because they occupy the same input sequence.",
        f"These image tokens are then concatenated with text tokens and fed into the decoder exactly as if they were additional words. The model's self-attention layers learn to reason jointly over both modalities because they occupy the same input sequence {cite(1)}.",
    ),
    # Cross-attention architecture
    (
        "Because visual tokens never enter the main context window as additional sequence elements, the approach scales more efficiently to high-resolution images.",
        f"Because visual tokens never enter the main context window as additional sequence elements, the approach scales more efficiently to high-resolution images {cite(1)}.",
    ),
    # CLIP, SigLIP encoders
    (
        "A pretrained model such as CLIP, OpenCLIP, or SigLIP divides the image into fixed-size patches, extracts features from each patch using a vision transformer, and produces embeddings.",
        f"A pretrained model such as CLIP, OpenCLIP, or SigLIP divides the image into fixed-size patches, extracts features from each patch using a vision transformer, and produces embeddings {cite(4)}.",
    ),
    # Image encoders contrastive pretraining
    (
        "Image encoders learn representations in which semantically related images and text descriptions map to nearby vectors. This alignment, achieved through contrastive pretraining on billions of image-text pairs, is what enables zero-shot capabilities such as image classification or visual question answering.",
        f"Image encoders learn representations in which semantically related images and text descriptions map to nearby vectors. This alignment, achieved through contrastive pretraining on billions of image-text pairs, is what enables zero-shot capabilities such as image classification or visual question answering {cite(3)}, {cite(4)}.",
    ),
    # NVLM hybrid
    (
        "NVIDIA's NVLM paper explored exactly this combination and found the hybrid model balanced efficiency and accuracy better than either pure approach.",
        f"NVIDIA's NVLM paper explored exactly this combination and found the hybrid model balanced efficiency and accuracy better than either pure approach {cite(1)}.",
    ),
    # CLIP-style encoders for RAG
    (
        "CLIP-style encoders map both text and images into a shared vector space, which means you can compute similarity between a text query and an image without converting the image to text first. This capability becomes the foundation for multimodal RAG",
        f"CLIP-style encoders map both text and images into a shared vector space, which means you can compute similarity between a text query and an image without converting the image to text first {cite(3)}, {cite(4)}. This capability becomes the foundation for multimodal RAG",
    ),

    # ---- Section 4 (Applying multimodal LLMs) ----
    # Three practical methods
    (
        "Three practical methods exist for supplying visual data to multimodal LLMs: raw bytes, Base64 encoding, and URLs. Each method trades off convenience, storage compatibility, and efficiency.",
        f"Three practical methods exist for supplying visual data to multimodal LLMs: raw bytes, Base64 encoding, and URLs {cite(6)}. Each method trades off convenience, storage compatibility, and efficiency.",
    ),

    # ---- Section 5 (Foundations of multimodal RAG) ----
    # ColPali leading implementation
    (
        "ColPali is the leading implementation of this idea for document retrieval. Its central innovation is to bypass the entire OCR pipeline.",
        f"ColPali is the leading implementation of this idea for document retrieval {cite(5)}. Its central innovation is to bypass the entire OCR pipeline.",
    ),
    # MaxSim late-interaction
    (
        "Retrieval uses a late-interaction mechanism called MaxSim. Each token in the query embedding is compared to every patch embedding from a candidate page.",
        f"Retrieval uses a late-interaction mechanism called MaxSim {cite(5)}. Each token in the query embedding is compared to every patch embedding from a candidate page.",
    ),
    # ViDoRe benchmark
    (
        "ColPali achieves an average nDCG@5 of 81.3 percent, substantially outperforming OCR-based baselines.",
        f"ColPali achieves an average nDCG@5 of 81.3 percent, substantially outperforming OCR-based baselines {cite(5)}.",
    ),
    # Enterprise RAG implications
    (
        "Financial analysts can query reports containing both narrative and charts without losing the meaning carried by the visuals. Technical teams can search documentation that includes schematics and flow diagrams.",
        f"Financial analysts can query reports containing both narrative and charts without losing the meaning carried by the visuals {cite(10)}. Technical teams can search documentation that includes schematics and flow diagrams.",
    ),
    # Production vector databases
    (
        "Milvus, Pinecone, and similar systems support the required similarity operations and can scale to millions of document pages.",
        f"Milvus, Pinecone, and similar systems support the required similarity operations and can scale to millions of document pages {cite(7)}.",
    ),

    # ---- Section 6 (Implementing multimodal RAG) ----
    # ColPali reference in implementation
    (
        "This forces the system to treat every piece of content as an image, exactly as ColPali does.",
        f"This forces the system to treat every piece of content as an image, exactly as ColPali does {cite(5)}, {cite(7)}.",
    ),
    # Voyage Multimodal, Cohere Embed
    (
        "In production the description step would be removed and the image bytes would be embedded directly by a multimodal model such as Voyage Multimodal, Cohere Embed, or Google's embedding endpoint on Vertex AI.",
        f"In production the description step would be removed and the image bytes would be embedded directly by a multimodal model such as Voyage Multimodal, Cohere Embed, or Google's embedding endpoint on Vertex AI {cite(3)}, {cite(16)}.",
    ),

    # ---- Section 7 (Building multimodal AI agents) ----
    # LangGraph create_react_agent
    (
        "The agent is constructed with LangGraph's `create_react_agent`. The system prompt emphasizes that visual queries should trigger the multimodal search tool.",
        f"The agent is constructed with LangGraph's `create_react_agent` {cite(8)}. The system prompt emphasizes that visual queries should trigger the multimodal search tool.",
    ),
]


def apply_insertions(text: str) -> str:
    """Apply all inline citation insertions."""
    for old, new in INSERTIONS:
        count = text.count(old)
        if count == 0:
            print(f"  WARNING: Pattern not found: {old[:80]}...")
            continue
        if count > 1:
            # For patterns that appear multiple times, only replace the first occurrence
            # that hasn't been cited yet (doesn't already have [[)
            idx = text.find(old)
            text = text[:idx] + new + text[idx + len(old):]
        else:
            text = text.replace(old, new)
    return text


def replace_references_section(text: str) -> str:
    """Replace the entire ## References section."""
    ref_pattern = r"## References\n.*"
    new_refs = build_references_section()
    # Find ## References and replace everything after it
    match = re.search(r"^## References\s*$", text, re.MULTILINE)
    if match:
        text = text[:match.start()] + new_refs
    return text


def main():
    article_path = EPISODE_DIR / "article.md"
    article_002_path = EPISODE_DIR / "article_002.md"

    # Back up originals
    for p in [article_path, article_002_path]:
        if p.exists():
            backup = p.with_suffix(".md.bak")
            if not backup.exists():
                shutil.copy2(p, backup)
                print(f"Backed up: {p.name} -> {backup.name}")

    # Read article
    text = article_path.read_text(encoding="utf-8")

    # Count original inline citations
    original_count = len(re.findall(r"\[\[\d+\]\]", text))
    print(f"Original inline citations: {original_count}")

    # Apply insertions
    text = apply_insertions(text)

    # Replace references section
    text = replace_references_section(text)

    # Count new inline citations
    new_count = len(re.findall(r"\[\[\d+\]\]", text))
    print(f"New inline citations: {new_count}")

    # Write repaired files
    article_path.write_text(text, encoding="utf-8")
    article_002_path.write_text(text, encoding="utf-8")
    print(f"Wrote repaired: {article_path.name}, {article_002_path.name}")


if __name__ == "__main__":
    main()
