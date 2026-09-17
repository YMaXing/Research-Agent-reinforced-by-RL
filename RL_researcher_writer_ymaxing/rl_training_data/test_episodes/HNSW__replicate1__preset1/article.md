# A Deep Dive into Hierarchical Navigable Small Worlds (HNSW)

Hierarchical Navigable Small World (HNSW) is a leading algorithm for Approximate Nearest Neighbor (ANN) search. It consistently delivers state-of-the-art recall with sub-millisecond speeds on massive vector datasets, outperforming methods like Inverted File (IVF) indexes and Locality-Sensitive Hashing (LSH) in both speed and accuracy for high-recall scenarios. This performance makes it a cornerstone of modern vector databases, powering applications from RAG to multimodal retrieval [[19]](https://www.vldb.org/pvldb/vol15/p850-doshi.pdf), [[45]](https://www.soeasie.com/blog/considerations-for-optimizing-media-retrieval-systems-using-multimodal-embeddings), [[46]](https://www.biorxiv.org/content/10.64898/2026.06.02.729602v1.full-text), [[47]](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf).![Hierarchical Navigable Small World (HNSW) graph overview](https://cdn.sanity.io/images/vr8gru94/production/d6e3a660654d9cb55f7ac137a736539e227296b6-1920x1080.png)

Image 1: An overview of the Hierarchical Navigable Small World (HNSW) graph. (Source: [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

Despite its widespread use, HNSW's internal mechanics remain difficult to grasp. They are a complex blend of probabilistic layering and graph traversal. This article demystifies HNSW, breaking down its theory, construction, and implementation. We will explore how to use it with Faiss and find the optimal parameters for your needs.

Having oriented ourselves on why HNSW matters, we will now examine the two core theoretical pillars that HNSW elegantly combines. These are probability skip lists and navigable small world graphs.

## Foundations of HNSW

Within the landscape of ANN algorithms, HNSW belongs to the category of proximity graphs. In these graphs, each vector is a node, and edges connect nodes that are close to each other in the vector space. HNSW takes this concept a step further by introducing a hierarchical structure, drawing inspiration from two fundamental data structures: the probability skip list and the navigable small world graph.

### Probability Skip List

A probability skip list is a data structure that enables fast search, similar to a sorted array, while also allowing for fast insertions and deletions, like a linked list. It achieves this by building multiple layers of linked lists on top of a base list that contains all elements in sorted order [[25]](https://en.wikipedia.org/wiki/Skip_list).

Each subsequent layer acts as an "express lane," containing a probabilistic subset of the elements from the layer below. The probability of an element from layer `i` also appearing in layer `i+1` is defined by a parameter `p` (usually 0.25 or 0.5). On average, each element appears in `1 / (1 - p)` lists. Higher layers have fewer elements and longer connections, allowing the search algorithm to skip over large portions of the list [[36]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).![A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for (or we reach the end), we drop to the next layer.](https://cdn.sanity.io/images/vr8gru94/production/9065d31e1b2e33ca697a56082f0ece7eff1c2d9b-1920x500.png)

Image 2: A probability skip list structure. The search starts at the top layer and drops down when it overshoots the target. (Source: [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

To search for an element, you start at the sparsest list in the top layer. You traverse horizontally until you find an element greater than your target or reach the end of the list. At that point, you drop down to the next layer and repeat the process. This continues until you reach the bottom layer, where you perform a final, short traversal to find the target element. This layered approach reduces the search complexity from linear, O(n), to logarithmic, O(log n) [[2]](https://en.wikipedia.org/wiki/Skip_list).

HNSW inherits its core hierarchical principle from skip lists, replacing the simple linked lists at each layer with more complex proximity graphs.

### Navigable Small World Graphs

Navigable Small World (NSW) graphs are networks designed for efficient greedy routing. They are characterized by two types of connections: short-range links that connect to nearby neighbors (a "friend list") and long-range links that bridge distant parts of the graph. This combination ensures that any two nodes in the network can be reached in a small number of steps, leading to a (poly-)logarithmic search complexity [[32]](https://arxiv.org/abs/1507.06529), [[34]](https://www.nature.com/articles/nphys1132), [[39]](https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059).![The search process through a NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector.](https://cdn.sanity.io/images/vr8gru94/production/5ca4fca27b2a9bf89b06748b39b7b6238fd4548c-1920x1080.png)

Image 3: The greedy search process through an NSW graph, moving from an entry point toward a query vector. (Source: [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

The search uses a greedy algorithm, starting at an entry point and iteratively moving to the neighbor closest to the query. This process involves a "zoom-out" phase, where the algorithm traverses through low-degree vertices with long-range links to find the query's general vicinity, followed by a "zoom-in" phase that uses high-degree vertices with short-range links for refinement [[5]](https://www.pinecone.io/learn/series/faiss/hnsw).

The algorithm stops when it reaches a local minimum. This is a node where no neighbor is closer to the query than the node itself. While effective, this greedy approach can sometimes get trapped in a local minimum far from the true nearest neighbor, especially if the graph lacks sufficient connectivity. This "early stopping" problem can reduce recall. This issue is most prominent in datasets with highly clustered or low-dimensional structures, where the greedy path can lead into a dense cluster that offers no links pointing toward the true, more distant neighbor [[48]](https://arxiv.org/abs/1603.09320).

To mitigate this, the density of connections, or the average degree of the vertices, can be increased. A higher degree provides more paths for the search to explore, reducing the chance of getting stuck. However, this comes at a cost: it increases the complexity of graph construction and the number of distance calculations required for each step of the search. This trade-off between recall and performance is a central challenge in designing graph-based ANN algorithms.

### Creating HNSW

The key innovation of HNSW is the application of the hierarchical principle of skip lists to NSW graphs. Instead of a single, massive graph, HNSW constructs a multi-layered structure where each layer is a proximity graph [[38]](https://arxiv.org/abs/1603.09320).![Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous.](https://cdn.sanity.io/images/vr8gru94/production/42d4a3ffc43e5dc2758ba8e5d2ef29d4c4d78254-1920x1040.png)

Image 4: The layered graph structure of HNSW, with long-range links at the top and shorter, denser links at the bottom. (Source: [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

The top layers contain a small subset of the vectors and are characterized by long-range links, similar to the "express lanes" in a skip list. As you move down the hierarchy, the layers become progressively denser, with more vectors and shorter-range links. The bottom layer, layer 0, contains all the vectors in the dataset.

The search process in HNSW and NSW shares the same core mechanic: a greedy traversal within a graph layer. However, their overall strategies differ significantly. In NSW, the search operates on a single graph and terminates upon reaching the first local minimum. This can be efficient but risks premature termination.

HNSW refines this process by introducing a hierarchy. The search begins in the sparse top layer and proceeds greedily until a local minimum is found. Instead of stopping, HNSW uses this node as the entry point for a new greedy search in the denser layer below. This descent continues layer by layer, with each step refining the search. This hierarchical approach is HNSW's main advantage, as it transforms the polylogarithmic complexity of NSW into a more efficient logarithmic complexity, O(log n). It allows the search to quickly navigate the vector space at a coarse level before zooming in for a precise search at the bottom, drastically reducing the number of comparisons needed.![The search process through the multi-layer structure of an HNSW graph.](https://cdn.sanity.io/images/vr8gru94/production/e63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png)

Image 5: The search process in HNSW, descending from the top layer to the bottom. (Source: [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

This hierarchical approach provides the best of both worlds. The upper layers allow for fast, coarse-grained navigation across the vector space, while the lower layers enable a precise, fine-grained search. By separating links based on their characteristic distance scales, HNSW avoids the high cost of traversing the entire dense graph from the beginning and achieves a true logarithmic search complexity. This scaling is a direct inheritance from skip lists; with each layer being exponentially sparser, the number of layers grows as O(log n), keeping the search cost logarithmic. However, recent research questions if the hierarchy is necessary for high-dimensional data. Studies suggest a flat NSW graph performs comparably on vectors with more than ~32 dimensions, proposing that a "Hub Highway" of naturally-forming, well-connected nodes makes the explicit hierarchy redundant [[49]](https://arxiv.org/html/2412.01940v2), [[38]](https://arxiv.org/abs/1603.09320), [[51]](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture).

With the layered foundations and search behavior clarified, we now turn to the practical iterative algorithm used to construct an HNSW graph one vector at a time.

## Graph Construction

The HNSW graph is built iteratively by inserting vectors one by one. The maximum number of layers in the graph is denoted by `L`. When a new vector is inserted, it is first assigned a random layer height, `l`, drawn from an exponentially decaying probability distribution. This means that most vectors will only exist in the lower layers, while a few will be promoted to the higher, sparser layers [[27]](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW).![The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it.](https://cdn.sanity.io/images/vr8gru94/production/f105cb148aae44f77fa7e3df7b7f8c0256bcbec4-1920x980.png)

Image 6: The probabilistic assignment of a vector to layers. (Source: [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

The probability distribution is controlled by a level multiplier parameter, `m_L`. Research has shown that the best performance is achieved when the overlap of shared neighbors between layers is minimized. An `m_L` value of approximately `1/ln(M)` (where `M` is the number of neighbors for each vertex) provides a good balance, ensuring the total number of traversals during search remains logarithmic [[38]](https://arxiv.org/abs/1603.09320).

The insertion process itself has two phases. First, the algorithm performs a greedy search starting from the top layer down to the randomly assigned layer `l`. In this phase, the search parameter `ef` is set to 1, meaning it only tracks the single best candidate at each step. This quickly identifies the right region for insertion.

Once layer `l` is reached, the second phase begins. The algorithm repeats the search process from layer `l` down to layer 0. However, this time, the search is more thorough. The `efConstruction` parameter is used to define the size of the dynamic candidate list, allowing the algorithm to explore more potential neighbors. From this candidate set, the algorithm selects `M` neighbors to connect to the new vector. Instead of just picking the `M` closest candidates, a heuristic is used to promote diverse connections. This heuristic favors candidates that are not only close to the new vector but also distant from already selected neighbors, which helps maintain global connectivity and prevents the search from getting trapped in isolated clusters [[38]](https://arxiv.org/abs/1603.09320).

This link creation is subject to caps. For all layers above 0, a vertex can have a maximum of `M_max` connections. For the base layer (layer 0), this cap is typically doubled to `M_max0` to ensure a high degree of connectivity where the final search happens. If adding new links exceeds these caps, the algorithm prunes the connections, keeping only the closest neighbors.![Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0.](https://cdn.sanity.io/images/vr8gru94/production/dc5cb11ea197ceb4e1f18214066c8c51526b9af5-1920x1080.png)

Image 7: The rules for assigning links to vertices, governed by the parameters M, M_max, and M_max0. (Source: [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

The construction process effectively mirrors the search procedure. The candidates found at each layer serve as the entry points for the search in the layer below, ensuring the graph remains navigable as it grows.

Equipped with a clear picture of how the hierarchical graph is built, we now examine the concrete Faiss implementation, index internals, parameter controls, and empirical tradeoffs observed on real workloads.

## Implementation of HNSW

We will implement HNSW using the Facebook AI Similarity Search (Faiss) library and test different construction and search parameters to see how they affect index performance.

1.  We start by initializing a basic HNSW index.
    ```python
    import faiss
    import numpy as np
    
    d = 128  # vector size
    M = 32   # number of neighbors
    
    index = faiss.IndexHNSWFlat(d, M)
    print(index.hnsw)
    ```
    It outputs:
    ```text
    <faiss.impl.HNSW.HNSW; proxy of <Swig Object of type 'faiss::HNSW *' at 0x137604e10> >
    ```

2.  The parameter `M` sets the number of neighbors to add during insertion. However, the `M_max` (max neighbors for upper layers) and `M_max0` (max neighbors for layer 0) parameters are set automatically by Faiss's `set_default_probas` method, which is called during initialization. It sets `M_max` to `M` and `M_max0` to `M*2`. Before we add any data, the index has no layers [[15]](https://www.pinecone.io/learn/series/faiss/hnsw).
    ```python
    # the HNSW index starts with no levels
    print(index.hnsw.max_level)
    
    # and levels (or layers) are empty too
    levels = faiss.vector_to_array(index.hnsw.levels)
    print(np.bincount(levels))
    ```
    It outputs:
    ```text
    -1
    array([], dtype=int64)
    ```

3.  After we build the index by adding our data (`xb`), the structure is populated.
    ```python
    # Sift1M dataset
    # xb contains 1M 128-dimensional vectors
    # xq contains 10k 128-dimensional query vectors
    
    index.add(xb)
    
    print(index.hnsw.max_level)
    
    levels = faiss.vector_to_array(index.hnsw.levels)
    print(np.bincount(levels))
    ```
    It outputs:
    ```text
    4
    array([     0, 968746,  30276,    951,     26,      1], dtype=int64)
    ```
    We now have 5 layers (0 through 4), and we can see the distribution of the 1 million vectors across them. Most vectors reside in layer 0, with exponentially fewer in the higher layers.

4.  The index also has a single entry point, which is the starting node for all searches.
    ```python
    print(index.hnsw.entry_point)
    ```
    It outputs:
    ```text
    118295
    ```

### Graph Structure

The logic for assigning layers and connections is handled by the `set_default_probas` method in Faiss. When we initialize the index, Faiss calls this method, passing `M` and a level multiplier `m_L` (calculated as `1 / log(M)`). This sets up the probability distribution for layer assignment.

1.  We can replicate this logic in Python to understand how it works. The function calculates the probability of a new vector being assigned to each level and the cumulative number of neighbors a vertex will have based on its insertion level.
    ```python
    def set_default_probas(M: int, m_L: float):
        nn = 0
        cum_nneighbor_per_level = []
        level = 0
        assign_probas = []
        while True:
            proba = np.exp(-level / m_L) * (1 - np.exp(-1 / m_L))
            if proba < 1e-9: break
            assign_probas.append(proba)
            nn += M * 2 if level == 0 else M
            cum_nneighbor_per_level.append(nn)
            level += 1
        return assign_probas, cum_nneighbor_per_level
    ```
    The core of this function is the probability calculation: `np.exp(-level / m_L) * (1 - np.exp(-1 / m_L))`. This formula creates an exponentially decaying probability for each successive layer. The loop continues to generate probabilities for new layers until the probability becomes negligibly small (less than 1e-9), at which point it stops.

2.  Calling this function with our parameters shows the probability distribution and the cumulative neighbor counts.
    ```python
    assign_probas, cum_nneighbor_per_level = set_default_probas(32, 1/np.log(32))
    print(assign_probas)
    print(cum_nneighbor_per_level)
    ```
    It outputs:
    ```text
    ([0.96875, 0.0302734375, 0.000946044921875, 2.956390380859375e-05, 9.238719940185547e-07, 2.8870999813079834e-08],
    [64, 96, 128, 160, 192, 224])
    ```
    The output shows a high probability (96.8%) of assigning a vector to layer 0, with probabilities decaying exponentially for higher layers. The cumulative neighbor count shows that a vector inserted at layer 0 will have 64 connections, while one inserted at layer 1 will have 96 total connections (64 at layer 0, 32 at layer 1), and so on.

3.  The `random_level` function then uses these probabilities to assign a layer to each new vector. It generates a random number and iterates through the `assign_probas` list, subtracting each level's probability until the random number falls within the range of a specific level's probability.
    ```python
    def random_level(assign_probas, rng):
        f = rng.random()
        for level in range(len(assign_probas)):
            if f < assign_probas[level]:
                return level
            f -= assign_probas[level]
        return len(assign_probas) - 1
    ```

4.  We can simulate this process for 1 million vectors to see if our Python implementation matches the distribution produced by Faiss.
    ```python
    rng = np.random.default_rng(12345)
    lvls = [random_level(assign_probas, rng) for i in range(1000000)]
    print(np.bincount(lvls))
    ```
    It outputs:
    ```text
    array([968821,  30170,    985,     23,       1])
    ```
    ![Distribution of vertices across layers in both the Faiss implementation (left) and the Python implementation (right).](https://cdn.sanity.io/images/vr8gru94/production/75658a08c25dabc1405f769c76fd2929c051853b-1920x930.png)

    Image 8: A comparison of vertex distribution across layers in the Faiss and Python implementations, showing a close match. (Source: [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

The distributions are very similar. The Faiss implementation includes a small but important detail: it ensures at least one vector is present in the highest layer to serve as the graph's entry point [[15]](https://www.pinecone.io/learn/series/faiss/hnsw).

### HNSW Performance

To understand the practical trade-offs, we can perform a parameter sweep on the Sift1M dataset, varying `M`, `efConstruction`, and `efSearch` to measure their impact on recall, search time, and memory usage.

The parameters `efConstruction` and `efSearch` control the depth of the search during index construction and querying, respectively. A higher value means a more thorough (and more expensive) search. `efConstruction` must be set before building the index, while `efSearch` can be adjusted any time before a search.

```python
# M is set at initialization
index = faiss.IndexHNSWFlat(d, M)

# efConstruction must be set before we build the index
index.hnsw.efConstruction = efConstruction
index.add(xb)

# efSearch can be set anytime before searching
index.hnsw.efSearch = efSearch
D, I = index.search(xq[:1000], k=1)
```

**Recall**![Recall@1 performance for various M, efConstruction, and efSearch parameters.](https://cdn.sanity.io/images/vr8gru94/production/e8c281c3626226a76389fa344a71eb57f70cf879-1920x980.png)

Image 9: Recall@1 performance for different parameter settings on the Sift1M dataset. (Source: [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

As expected, higher values for `M` and `efSearch` significantly improve recall. A reasonably high `efConstruction` value is also necessary to build a high-quality graph. Increasing `efConstruction` allows you to achieve high recall even with lower `M` and `efSearch` values, as it creates a more robust graph structure from the start. This is because a higher `efConstruction` allows the algorithm to find more optimal connections during index creation, leading to a higher-quality graph that improves recall during search [[18]](https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall).

**Search Time**![Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is on a log scale.](https://cdn.sanity.io/images/vr8gru94/production/876bf66aba408959042888efe72c55db4d6b3b41-1920x980.png)

Image 10: Search time for 1000 queries with various parameter settings. The y-axis is on a log scale. (Source: [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

The trade-off between recall and search time is clear. Achieving near-perfect recall can increase search times substantially. It's often assumed that `efConstruction` has little impact on search time, but our tests on a batch of 1000 queries show otherwise. For larger query volumes, a higher `efConstruction` leads to longer search times because a denser, more complex graph requires more traversal.

However, for low query volumes (e.g., a single query), the impact of `efConstruction` on search time is much less pronounced, especially at lower `M` values. This makes `efConstruction` an excellent parameter to increase when you need higher recall without a significant latency penalty for single-shot queries.![efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values.](https://cdn.sanity.io/images/vr8gru94/production/ef1a2edd25adb202c0a98a1f33a0e72d1295b554-1720x1080.png)

Image 11: The effect of efConstruction on search time for a single query. (Source: [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

**Memory Usage**![Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage.](https://cdn.sanity.io/images/vr8gru94/production/e04d23ccd76d8bdc568542bebe75a75e7d36a21e-1480x1050.png)

Image 12: Memory usage as a function of the parameter M. (Source: [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

Memory usage is affected only by the `M` parameter. Both `efConstruction` and `efSearch` have no impact on the final index size. The memory footprint grows substantially with `M`. For the Sift1M dataset, the index size starts at over 0.5GB for a small `M` of 2 and balloons to nearly 5GB for an `M` of 512. This highlights the critical three-way trade-off between recall, latency, and memory, which has direct implications for infrastructure costs.

Echoing the research on the hierarchy's diminishing returns in high dimensions, building a flat graph can offer significant memory savings. One study found that a "flattened" HNSW implementation reduced peak memory consumption by 18-39% on large-scale (100M vector) benchmarks compared to the standard hierarchical build, without a discernible loss in performance. This suggests that for memory-constrained applications with high-dimensional data, omitting the hierarchy could be a practical optimization [[49]](https://arxiv.org/html/2412.01940v2).

### Improving Memory Usage and Search Speeds

When the memory requirements of a standard HNSW index become prohibitive, there are several strategies to mitigate the issue. One common approach is to compress the stored vectors using Product Quantization (PQ). PQ works by splitting each vector into sub-vectors and quantizing each sub-vector independently. This significantly reduces the memory footprint, though it typically comes at the cost of lower recall and slightly increased search times as the original vectors are not stored.

Another strategy is to combine HNSW with an Inverted File (IVF) component. In this setup, the dataset is first partitioned into a set of cells, or Voronoi partitions. HNSW is then used as a coarse quantizer to quickly identify the most relevant partitions to search, rather than performing an exhaustive scan of all partition centroids. This is particularly effective when dealing with a very large number of partitions (e.g., thousands), as HNSW can find the nearest centroids much faster than a brute-force search. The final search is then confined to the vectors within these selected partitions, which can improve overall search speed.

These techniques for creating composite indexes are powerful but add another layer of complexity. For a deeper dive, we recommend exploring how to combine IVF, PQ, and HNSW [[44]](https://www.pinecone.io/learn/series/faiss/composite-indexes/).

## Conclusion

HNSW has established itself as a top-tier algorithm for approximate nearest neighbor search, delivering an exceptional balance of speed and accuracy. Its hierarchical structure, combining principles from skip lists and navigable small world graphs, enables efficient, logarithmic-time searching in massive, high-dimensional datasets. We have explored its theoretical underpinnings, dissected its construction algorithm, and analyzed its implementation in Faiss.

The parameter sweeps reveal the fundamental trade-offs between recall, search latency, and memory usage, providing the knowledge to tune the index for specific application needs. While HNSW's memory consumption can be a challenge, techniques like Product Quantization and IVF integration offer practical solutions. Understanding HNSW is a key skill for engineers building production-grade AI systems that rely on high-performance similarity search.

## References

- [1] S. Arya, D. M. Mount, N. S. Netanyahu, R. Silverman, and A. Y. Wu. An Optimal Algorithm for Approximate Nearest Neighbor Searching Fixed Dimensions. *Journal of the ACM*, 45(6), 891-923, 1998.
- [2] Skip list - Wikipedia. https://en.wikipedia.org/wiki/Skip_list
- [3] A. Gionis, P. Indyk, and R. Motwani. Similarity Search in High Dimensions via Hashing. *Proceedings of the 25th International Conference on Very Large Data Bases*, 518-529, 1999.
- [4] Y. A. Malkov and D. A. Yashunin. Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs. *IEEE Transactions on Pattern Analysis and Machine Intelligence*, 42(4), 824-836, 2018.
- [5] How does greedy routing function in navigable small world graphs?. https://www.pinecone.io/learn/series/faiss/hnsw
- [6] Understading HNSW — Hierarchical Navigable Small World. https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605
- [7] Similarity Search, Part 4: Hierarchical Navigable Small World (HNSW). https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37
- [8] Approximate nearest neighbor algorithm based on navigable small world graphs. https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf
- [9] What are core innovations in Malkov HNSW paper?. https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf
- [10] What are core innovations in Malkov HNSW paper?. https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf
- [11] E. Chávez, G. Navarro, R. Baeza-Yates, and J. L. Marroquín. Searching in Metric Spaces. *ACM Computing Surveys*, 33(3), 273-321, 2001.
- [12] What are core innovations in Malkov HNSW paper?. https://openreview.net/pdf/9d557864b10a646d79ecf63772864cc3c168091f.pdf
- [13] IVFPQ+HNSW for Billion-scale Similarity Search. https://towardsdatascience.com/ivfpq-hnsw-for-billion-scale-similarity-search-89ff2f89d90e
- [14] How does Faiss implement HNSW with parameters M efConstruction efSearch?. https://www.pinecone.io/learn/series/faiss/hnsw
- [15] How does Faiss implement HNSW with parameters M efConstruction efSearch?. https://www.pinecone.io/learn/series/faiss/hnsw
- [16] How does Faiss implement HNSW with parameters M efConstruction efSearch?. https://www.youtube.com/watch?v=QvKMwLjdK-s
- [17] M. Muja and D. G. Lowe. Fast Approximate Nearest Neighbors with Automatic Algorithm Configuration. *International Conference on Computer Vision Theory and Application*, 2, 331-340, 2009.
- [18] What are the key configuration parameters for an HNSW index, such as M and efConstruction/efSearch, and how does each influence the tradeoff between index size, build time, query speed, and recall?. https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall
- [19] LANNS: A Web-Scale Approximate Nearest Neighbor Lookup System. https://www.vldb.org/pvldb/vol15/p850-doshi.pdf
- [20] What empirical tradeoffs does HNSW show on Sift1M for M ef parameters?. https://www.pinecone.io/learn/series/faiss/hnsw
- [21] Indexing 1M vectors. https://github.com/facebookresearch/faiss/wiki/Indexing-1M-vectors
- [22] J. L. Bentley. Multidimensional binary search trees used for associative searching. *Communications of the ACM*, 18(9), 509-517, 1975.
- [23] What empirical tradeoffs does HNSW show on Sift1M for M ef parameters?. https://www.youtube.com/watch?v=QvKMwLjdK-s
- [24] How does HNSW assign random layer heights using exponential probability distribution?. https://arxiv.org/html/2412.01940v2
- [25] Hierarchical Navigable Small World (HNSW) for Vector Search. https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world
- [26] The Shortcut Through Space: Hierarchical Navigable Small Worlds (HNSW) in Vector Search. https://medium.com/@adnanmasood/the-shortcut-through-space-hierarchical-navigable-small-worlds-hnsw-in-vector-search-4df5aa755100
- [27] Hierarchical Navigable Small Worlds (HNSW). https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW
- [28] How does HNSW assign random layer heights using exponential probability distribution?. https://www.youtube.com/watch?v=QvKMwLjdK-s
- [29] What two-phase construction search does HNSW use with ef=1 and efConstruction?. https://www.pinecone.io/learn/series/faiss/hnsw
- [30] P. Indyk and R. Motwani. Approximate Nearest Neighbors: Towards Removing the Curse of Dimensionality. *Proceedings of the 30th Annual ACM Symposium on Theory of Computing*, 604-613, 1998.
- [31] How does Faiss set_default_probas compute level probabilities and M_max for HNSW?. https://www.pinecone.io/learn/series/faiss/hnsw
- [32] faiss/HNSW.h at main · efficient/faiss-learned-termination. https://github.com/efficient/faiss-learned-termination/blob/master/HNSW.h
- [33] How does Faiss set_default_probas compute level probabilities and M_max for HNSW?. https://www.youtube.com/watch?v=QvKMwLjdK-s
- [34] struct faiss::HNSW. https://faiss.ai/cpp_api/struct/structfaiss_1_1HNSW.html
- [35] Similarity Search, Part 4: Hierarchical Navigable Small World (HNSW). https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37
- [36] Similarity Search, Part 4: Hierarchical Navigable Small World (HNSW). https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37
- [37] What role does L play in HNSW insertion?. https://www.pinecone.io/learn/series/faiss/hnsw
- [38] Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs. https://arxiv.org/abs/1603.09320
- [39] Approximate nearest neighbor algorithm based on navigable small world graphs. https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059
- [40] Growing homophilic networks are natural navigable small worlds. https://arxiv.org/abs/1507.06529
- [41] Navigability of complex networks. https://arxiv.org/abs/0709.0303
- [42] G. Navarro. Searching in metric spaces by spatial approximation. *The VLDB Journal*, 11(1), 28-46, 2002.
- [43] W. Pugh. Skip lists: a probabilistic alternative to balanced trees. *Communications of the ACM*, 33(6), 668-676, 1990.
- [44] Facebook AI and the Index Factory. https://www.pinecone.io/learn/series/faiss/composite-indexes/
- [45] Considerations for Optimizing Media Retrieval Systems Using Multimodal Embeddings. https://www.soeasie.com/blog/considerations-for-optimizing-media-retrieval-systems-using-multimodal-embeddings
- [46] HNSW-MS: A Scalable and Accurate Mass Spectral Similarity Search for Real-Time Metabolomics. https://www.biorxiv.org/content/10.64898/2026.06.02.729602v1.full-text
- [47] Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs. https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf
- [48] Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs. https://arxiv.org/abs/1603.09320
- [49] Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”. https://arxiv.org/html/2412.01940v2
- [50] M. S. Charikar. Similarity Estimation Techniques from Rounding Algorithms. *Proceedings of the 34th Annual ACM Symposium on Theory of Computing*, 380-388, 2002.
- [51] HNSW: The Architecture of the Vector Search Index. https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture
</article>