## Exploration Integration Example: Depth Enrichment (Technical Nuance)

This example demonstrates integrating an exploration source that adds genuine technical depth — a
specific implementation trade-off that the core article's exploitation sources did not cover.

---

### Exploration Source

```xml
<research_source phase="exploration" type="tavily" url="https://www.pinecone.io/learn/series/faiss/vector-indexes/">
Vector index selection is one of the most consequential decisions when deploying a RAG system at scale.
While exact search (flat indexes) guarantees perfect recall but scales O(n) with dataset size,
approximate nearest neighbor (ANN) methods trade a small amount of recall for dramatically faster queries.

The two most widely adopted ANN structures are IVFFlat and HNSW. IVFFlat partitions the embedding space
into Voronoi cells at training time using k-means clustering, then at query time searches only the cells
closest to the query vector (controlled by the `nprobe` parameter). HNSW constructs a multi-layer graph
where edges connect similar vectors, enabling logarithmic-time search.

HNSW consistently delivers lower latency — typically achieving 95–99% recall at 5–10× the query speed
of IVFFlat — but requires significantly more memory (roughly 100 bytes per vector for M=16 compared to
~8 bytes for a flat index) and a longer index build time. For production systems processing millions of
documents, the choice matters: HNSW is the default when memory is available; IVFFlat is preferable
under memory constraints.
</research_source>
```

### Assessment

**Qualifies — Depth.** The core article explains semantic search conceptually and mentions FAISS. This
source adds concrete, implementer-relevant detail (IVFFlat vs. HNSW trade-offs: recall, latency, memory
footprint) that the exploitation sources did not cover. A practitioner reading the article will benefit
from knowing *which* index type to pick and *why*.

---

### Core Section (Before Integration)

**Semantic Retrieval**

When a user query arrives, the retrieval layer converts it into a dense vector using the same embedding
model that indexed the knowledge base. FAISS then computes cosine similarity between the query vector
and all stored document vectors and returns the top-k most similar chunks. These retrieved chunks become
the context injected into the prompt.

Choosing the right chunk size and top-k value requires experimentation. Chunks that are too long dilute
relevance; chunks that are too short lose coherent context. In practice, chunks of 256–512 tokens with a
10–15% overlap and k=5–10 retrieved chunks balance precision and recall for most production workloads.

---

### Integrated Section (After Integration)

**Semantic Retrieval**

When a user query arrives, the retrieval layer converts it into a dense vector using the same embedding
model that indexed the knowledge base. FAISS then computes cosine similarity between the query vector
and all stored document vectors and returns the top-k most similar chunks. These retrieved chunks become
the context injected into the prompt.

For datasets with millions of documents, exact search does not scale: it requires O(n) comparisons per
query. Approximate nearest neighbor (ANN) indexes solve this by trading a small amount of recall for
substantially faster queries. The two most common options are HNSW and IVFFlat. HNSW achieves 95–99%
recall at 5–10× the query speed of IVFFlat but uses roughly 10× more memory per vector. For datasets
that fit in GPU memory HNSW is the default choice; IVFFlat is preferable when memory is constrained.

Choosing the right chunk size and top-k value requires experimentation. Chunks that are too long dilute
relevance; chunks that are too short lose coherent context. In practice, chunks of 256–512 tokens with a
10–15% overlap and k=5–10 retrieved chunks balance precision and recall for most production workloads.

---

### Explanation

The ANN trade-off paragraph was inserted **after** the first paragraph (which establishes *what*
retrieval does conceptually) and **before** the chunk-size paragraph (which covers a separate
implementation decision). This follows the natural decision sequence: understand what retrieval does →
how to scale it → how to tune it. The existing paragraphs are unchanged and the section's core
narrative about semantic retrieval remains primary.
