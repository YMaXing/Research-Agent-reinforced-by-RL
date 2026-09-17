## Context of the Article

### What We Are Planning to Share

- Comprehensive breakdown of Hierarchical Navigable Small Worlds (HNSW) as a leading graph-based ANN method that achieves state-of-the-art recall and sub-millisecond query speeds on large-scale vector datasets.
- Theoretical foundations combining probabilistic skip lists (for fast layered traversal and insertion) with navigable small world graphs (for logarithmic greedy routing via long-range and short-range links).
- The core hierarchical innovation that applies skip-list layering to NSW graphs, enabling searches to start with coarse long-range links at the top and progressively refine to precise short-range links at the bottom.
- Iterative one-by-one graph construction algorithm, including probabilistic layer assignment, candidate selection, and link capping rules.
- Deep dive into the Faiss implementation, index inspection methods, exact roles of parameters M, efConstruction, and efSearch, empirical tradeoffs measured on Sift1M, and mitigation approaches using PQ compression or IVF clustering.
- Concrete diagrams, parameter-sweep heatmaps, histograms, and tradeoff curves that make the layered mechanics and performance impacts explicit for AI engineers.

### Why We Think It's Valuable

- HNSW powers high-performance vector databases and retrieval systems in production RAG and semantic search applications; mastering its layered proximity-graph mechanics and parameter sensitivities lets engineers choose indexes wisely, optimize the recall-latency-memory frontier, and debug or extend ANN pipelines.
- By focusing on greedy routing pitfalls, hierarchy benefits, and Faiss-specific behaviors, the article equips experienced vector-search developers to move beyond black-box usage and make informed implementation decisions.

### Expected Length of the Article
**2,550 words**

### Theory / Practice Ratio
70% theory - 30% practice

## Article Outline

1. Introduction
2. Foundations of HNSW
3. Graph Construction
4. Implementation of HNSW

## Section 1 - Introduction

- First, insert a graph with the following online URL syntax:
![Hierarchical Navigable Small World (HNSW) graph overview](https://cdn.sanity.io/images/vr8gru94/production/d6e3a660654d9cb55f7ac137a736539e227296b6-1920x1080.png)
- Highlight HNSW popularity drivers by citing its consistent delivery of state-of-the-art recall paired with sub-millisecond search speeds on large vector collections, contrasting this with slower or lower-recall methods such as IVF or LSH.
- Explain briefly why HNSW internals remain difficult to understand despite widespread adoption in vector databases.
- State that this article aims to dymistify HNSW, and towards the end of the article, we’ll look at how to implement HNSW using [Faiss](https://www.pinecone.io/learn/series/faiss/) and which parameter settings give us the performance we need.
- Transition to Section 2: Having oriented the reader on why HNSW matters and where the article is headed, we now examine the two core theoretical pillars—probability skip lists and navigable small world graphs—that HNSW elegantly combines.

- **Section length:** 120 words

## Section 2 - Foundations of HNSW

- Position HNSW inside the ANN landscape as a member of the graph category, specifically proximity graphs in which edges are created only between vectors that are close under Euclidean (or chosen) distance. Acknowledge the significant leap in complexity from the proximity-graph to hierarchical-navigable-small-world-graph, and thus naturally introduce the two fundamental technicals that contributed the most to HNSW - the probability skip list, and navigable small world graphs.

### Probability Skip List

- Detail probability skip lists as a layered linked-list structure that enables both fast search like a sorted array and fast insertion of new elements using a linked list structure which is impossible with mere sorted arrays: describe the structure of layers of linked lists, starting from the first layer and then moving down the layers; explain concisely how to search a skip list.
- Insert a graph with the following online URL syntax:
![A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for (or we reach the end), we drop to the next layer.](https://cdn.sanity.io/images/vr8gru94/production/9065d31e1b2e33ca697a56082f0ece7eff1c2d9b-1920x500.png)
- Briefly state what HNSW inherits from skip list.

### Navigable Small World Graphs

- Describe navigable small world (NSW) graphs as networks that combine long-range links (for rapid global movement) with short-range “friend-list” links (for local refinement), producing greedy-routing complexity that scales (poly-)logarithmically with graph size. 
- Insert a graph with the following online URL syntax:
![The search process through a NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector.](https://cdn.sanity.io/images/vr8gru94/production/5ca4fca27b2a9bf89b06748b39b7b6238fd4548c-1920x1080.png)
- Explain greedy routing mechanics in detail: the algorithm begins at an entry point and repeatedly moves to the nearest neighbor in the current vertex’s friend list; contrast the early “zoom-out” phase (low-degree vertices with long-range links that cover large distances) against the later “zoom-in” phase (high-degree vertices that refine position) during routing; note the local-minima stopping condition and the risk of early stopping that reduces recall when the graph lacks sufficient connectivity;
- Analyze the degree-versus-performance tradeoff: higher average vertex degree improves recall by lowering the probability of premature local-minima traps, yet simultaneously raises both construction complexity and per-query network traversal cost, creating a central tuning axis that later sections quantify.

### Creating HNSW

- Insert a graph with the following online URL syntax:
![Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous.](https://cdn.sanity.io/images/vr8gru94/production/42d4a3ffc43e5dc2758ba8e5d2ef29d4c4d78254-1920x1040.png)
- Present hierarchy as the key innovation of HNSW and the search process in HNSW: skip-list-style layering is applied to an NSW graph so that search starts at the top layer with only long-range links, descends layer by layer upon reaching a local minimum, and thereby progressively increases accuracy while avoiding the high cost of searching the entire dense bottom layer. Stress both the similarities and differences between the search process in HSNW and that in NSW.
- Insert a graph with the following online URL syntax:
![The search process through the multi-layer structure of an HNSW graph.](https://cdn.sanity.io/images/vr8gru94/production/e63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png)
- Transition to Section 3: With the layered foundations and search behavior clarified, we now turn to the practical iterative algorithm used to construct an HNSW graph one vector at a time.

- **Section length:** 900 words

## Section 3 - Graph Construction

- Describe the iterative one-by-one vector insertion process and the role of L (maximum number of layers), where each new vector is assigned a random layer height drawn from an exponentially decaying probability distribution.
- Insert a graph with the following online URL syntax:
![The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it.](https://cdn.sanity.io/images/vr8gru94/production/f105cb148aae44f77fa7e3df7b7f8c0256bcbec4-1920x980.png)
- Emphasize that the finding that minizing the overlap of shared neighbors across layers enables the best performance. Explain the level multiplier m_L (approximately 1/ln(M)) and how it controls the expected number of layers while minimizing neighbor overlap across layers, thereby keeping the total number of traversals during search logarithmic.
- Break down the two-phase construction search: an initial ef=1 greedy traversal to discover the insertion layer, followed by a richer efConstruction-parameterized search repeated layer-by-layer down to layer 0 for candidate gathering and link creation.
- Detail link selection from the candidate set: the M nearest candidates are chosen as neighbors while respecting per-layer caps M_max for upper layers and the doubled M_max0 for the base layer (layer 0), which directly determines final vertex degrees.
- Show how construction mirrors the search procedure, with each layer's efConstruction candidates doubling as entry points into the next layer, so link creation continues down to layer 0's local-minimum stop, keeping the graph navigable.
- Insert a graph with the following online URL syntax:
![Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0.](https://cdn.sanity.io/images/vr8gru94/production/dc5cb11ea197ceb4e1f18214066c8c51526b9af5-1920x1080.png)
- Transition to Section 4: Equipped with a clear picture of how the hierarchical graph is built, we now examine the concrete Faiss implementation, index internals, parameter controls, and empirical tradeoffs observed on real workloads.

- **Section length:** 350 words

## Section 4 - Implementation of HNSW

- Introduce implementing HNSW with the Facebook AI Similarity Search (Faiss) library, framing the goal of testing different construction and search parameters to see how they affect index performance.
- Include a code block initializing the HNSW index (`import faiss`, `d = 128`, `M = 32`, `index = faiss.IndexHNSWFlat(d, M)`, `print(index.hnsw)`) together with its output showing the raw Faiss HNSW proxy object.
- Explain that `M` sets the number of neighbors added to each vertex on insertion, but M_max and M_max0 are still missing, and detail how Faiss's `set_default_probas` method (called automatically at index initialization) sets M_max = `M` and M_max0 = `M*2`.
- Include a code block showing that before calling `index.add(xb)`, `index.hnsw.max_level` is unset (output `-1`) and `levels` (via `faiss.vector_to_array(index.hnsw.levels)` and `np.bincount`) is an empty array.
- Include a code block calling `index.add(xb)` to build the index, then re-checking `index.hnsw.max_level` (now `4`) and the populated `levels` bincount output, showing the vertex distribution across layers 0-4.
- Include a code block retrieving `index.hnsw.entry_point` (output `118295`), explaining that this identifies which vector serves as the graph's entry point.

### Graph Structure

- Explain that initializing the index with `d` and `M` calls `set_default_probas`, passing `M` and `1 / log(M)` in place of `levelMult` (equivalent to m_L), and that this method can be reproduced in Python.
- Include a code block with the Python equivalent of `set_default_probas`, building `assign_probas` (the per-layer insertion probability) and `cum_nneighbor_per_level` (the cumulative neighbor count per insertion level).
- Include a code block calling `set_default_probas(32, 1/np.log(32))` together with its output values for `assign_probas` and `cum_nneighbor_per_level`, highlighting the much higher probability of inserting at layer 0 and the increasing sparsity of higher layers.
- Detail the `random_level` function: it draws a random float and walks through `assign_probas`, assigning the vertex to the first level whose cumulative probability threshold isn't exceeded, defaulting to the highest level if none satisfy the condition.
- Include a code block with the Python `random_level` implementation.
- Include a code block simulating 1,000,000 insertions with `random_level` and `np.bincount`, comparing the resulting distribution against the true Faiss level distribution and noting the close match.
- Insert a graph with the following online URL syntax:
![Distribution of vertices across layers in both the Faiss implementation (left) and the Python implementation (right).](https://cdn.sanity.io/images/vr8gru94/production/75658a08c25dabc1405f769c76fd2929c051853b-1920x930.png)
- Note that the Faiss implementation always guarantees at least one vertex at the highest layer, ensuring it can serve as the graph's entry point.

### HNSW Performance

- Introduce the empirical parameter sweep across `M`, `efSearch`, and `efConstruction` on the Sift1M dataset, measuring recall, search/build time, and memory usage.
- Include a code block re-initializing the index (`index = faiss.IndexHNSWFlat(d, M)`), then setting `index.hnsw.efConstruction` before `index.add(xb)` and `index.hnsw.efSearch` before calling `index.search(xq[:1000], k=1)`, noting that `efConstruction` must be set before construction while `efSearch` can be set any time before searching.
- Insert a graph with the following online URL syntax:
![Recall@1 performance for various M, efConstruction, and efSearch parameters.](https://cdn.sanity.io/images/vr8gru94/production/e8c281c3626226a76389fa344a71eb57f70cf879-1920x980.png)
- Report that high M and efSearch values substantially raise recall, that a reasonable efConstruction value is also needed, and that increasing efConstruction can compensate for lower M and efSearch values.
- Insert a graph with the following online URL syntax:
![Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is using a log scale.](https://cdn.sanity.io/images/vr8gru94/production/876bf66aba408959042888efe72c55db4d6b3b41-1920x980.png)
- Explain the recall/search-time balancing act (ranging roughly 80%-1ms to 100%-50ms across 1000 queries), and correct the common assumption that efConstruction has a negligible effect on search time — clarifying this only holds for small query volumes, not the 1000-query batch tested here.
- State that when query volume is low, efConstruction is a great parameter to raise for extra recall with little added search-time cost, particularly at lower M values.
- Insert a graph with the following online URL syntax:
![efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values.](https://cdn.sanity.io/images/vr8gru94/production/ef1a2edd25adb202c0a98a1f33a0e72d1295b554-1720x1080.png)
- Insert a graph with the following online URL syntax:
![Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage.](https://cdn.sanity.io/images/vr8gru94/production/e04d23ccd76d8bdc568542bebe75a75e7d36a21e-1480x1050.png)
- Report that only M affects index memory usage (efConstruction and efSearch have no effect), with index size already exceeding 0.5GB at M=2 and reaching almost 5GB at M=512, underscoring the recall/latency/memory tradeoff and its infrastructure cost implications.

### Improving Memory Usage and Search Speeds

- Outline mitigation strategies when HNSW memory becomes prohibitive: compress stored vectors with product quantization (PQ), which reduces memory at the cost of recall and search time, or wrap HNSW with an IVF component to improve search speed.
- Close the article by noting that combining IVF and PQ with HNSW is covered in another article on composite indexes with the URL - (https://www.pinecone.io/learn/series/faiss/composite-indexes/).

- **Section length:** 1180 words

## Golden Sources

<!-- [Skip lists: a probabilistic alternative to balanced trees](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf) -->
"pugh-skiplists-cacm1990.md"

<!-- [Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs](https://arxiv.org/abs/1603.09320) -->
"Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs.md"

<!-- [Approximate Nearest Neighbor Search Small World Approach](https://www.iiis.org/CDs2011/CD2011IDI/ICTA_2011/PapersPdf/CT175ON.pdf) -->
"Approximate Nearest Neighbor Search Small World Approach.md"

<!-- [Scalable Distributed Algorithm for Approximate Nearest Neighbor Search Problem in High Dimensional General Metric Spaces](https://www.researchgate.net/publication/262334462_Scalable_Distributed_Algorithm_for_Approximate_Nearest_Neighbor_Search_Problem_in_High_Dimensional_General_Metric_Spaces) -->
"Scalable Distributed Algorithm for Approximate Nearest.md"

<!-- [Approximate nearest neighbor algorithm based on navigable small world graphs](https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059) -->
"Approximate nearest neighbor algorithm based on navigable small world graphs.md"

<!-- [Growing homophilic networks are natural navigable small worlds](https://arxiv.org/abs/1507.06529) -->
"Growing homophilic networks are natural navigable small worlds.md"

# Other Sources

[Faiss HNSW Implementation](https://github.com/facebookresearch/faiss/blob/main/faiss/impl/HNSW.cpp)

<!-- [Navigability of complex networks](https://arxiv.org/abs/0709.0303) -->
"Navigability of complex networks.md"