# A Deep Dive into HNSW: The Algorithm Behind Modern Vector Search

Hierarchical Navigable Small World (HNSW) is one of the most powerful algorithms for Approximate Nearest Neighbor (ANN) search. It consistently delivers state-of-the-art recall with sub-millisecond query speeds, even on billion-scale vector datasets. Its balance of speed and accuracy has made it the engine behind countless vector databases, recommendation systems, and multimodal retrieval systems for image and audio search [[53]](https://milvus.io/ai-quick-reference/what-is-hnsw-and-why-is-it-popular-for-vector-search).![Image 1: An overview of the Hierarchical Navigable Small World (HNSW) graph structure.](https://cdn.sanity.io/images/vr8gru94/production/d6e3a660654d9cb55f7ac137a736539e227296b6-1920x1080.png)

Image 1: An overview of the Hierarchical Navigable Small World (HNSW) graph structure. (Source [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw))

While methods like Inverted File (IVF) indexes or Locality-Sensitive Hashing (LSH) have their place, HNSW often provides a superior trade-off between speed and accuracy [[31]](https://www.vldb.org/pvldb/vol15/p850-doshi.pdf). Yet, despite its widespread adoption, its internal mechanics remain a black box for many engineers.

This article demystifies HNSW, breaking down its theoretical foundations, graph construction, and performance trade-offs. Towards the end, we’ll look at how to implement HNSW using Facebook AI Similarity Search (Faiss) and find the parameter settings that give us the performance we need. Let's examine the two core theoretical pillars it combines: probability skip lists and navigable small world graphs.

## Foundations of HNSW

HNSW belongs to the category of graph-based ANN algorithms, specifically proximity graphs. In these graphs, nodes represent vectors, and edges connect vectors that are close to each other in the given metric space (like Euclidean distance). HNSW's innovation was to combine two powerful concepts to create a hierarchical proximity graph: the probability skip list and the navigable small world graph.

### Probability Skip List

A probability skip list is a data structure that achieves the fast search capabilities of a sorted array while retaining the efficient insertion of a linked list [[46]](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf). It accomplishes this with a layered structure. The bottom layer is an ordinary sorted linked list containing all elements. Each subsequent layer above it acts as an "express lane," containing a random subset of the elements from the layer below.![Image 2: A probability skip list structure. The search starts on the top layer. If the current key is greater than the key being searched for, or the end of the list is reached, the search drops to the next layer.](https://cdn.sanity.io/images/vr8gru94/production/9065d31e1b2e33ca697a56082f0ece7eff1c2d9b-1920x500.png)

Image 2: A probability skip list structure. The search starts on the top layer. If the current key is greater than the key being searched for, or the end of the list is reached, the search drops to the next layer. (Source [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw))

To search for an element, you start at the sparsest top layer. You traverse horizontally until you find an element greater than your target or reach the end of the list. At that point, you drop down to the next layer and continue the process. This allows the search to skip over large numbers of elements in the upper layers, achieving an average search complexity of O(log n) [[45]](https://en.wikipedia.org/wiki/Skip_list). HNSW inherits this multi-layered search strategy, but instead of simple linked lists, it uses graphs.

### Navigable Small World Graphs

Navigable Small World (NSW) graphs are networks where most nodes can be reached from any other node in a small number of steps [[47]](https://arxiv.org/abs/1507.06529). They are defined by having a high clustering coefficient (your friends are likely to be friends with each other) and a short average path length. This structure is achieved by combining short-range links, which connect nearby nodes, with long-range links that bridge distant parts of the graph [[50]](https://arxiv.org/abs/0709.0303).![Image 3: The search process through an NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector.](https://cdn.sanity.io/images/vr8gru94/production/5ca4fca27b2a9bf89b06748b39b7b6238fd4548c-1920x1080.png)

Image 3: The search process through an NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector. (Source [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw))

Searching an NSW graph uses a greedy routing algorithm. Starting from a pre-defined entry point, the algorithm evaluates the "friend list" of the current node and moves to the neighbor closest to the query vector. This process is repeated until it reaches a local minimum—a node where no neighbor is closer to the query [[5]](https://www.pinecone.io/learn/series/faiss/hnsw).

This routing process has two phases. It starts with a "zoom-out" phase, traversing long-range links between low-degree nodes to quickly cross the graph. As it gets closer to the target region, it enters a "zoom-in" phase, using short-range links between high-degree nodes for fine-grained searching [[32]](https://arxiv.org/abs/1603.09320).

The main weakness of this approach is the risk of getting trapped in a local minimum far from the true nearest neighbor, especially if the graph's connectivity is poor [[6]](https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605). This problem is most prominent for low-dimensional or highly clustered data, where the greedy search can fail to find a path to the global optimum [[32]](https://arxiv.org/abs/1603.09320). The algorithm's effectiveness relies on metric properties like the triangle inequality; non-metric similarity measures can violate the assumptions that make greedy routing work, leading to degraded performance [[55]](https://keyurramoliya.com/posts/Understading-HNSW-Hierarchical-Navigable-Small-World). Increasing the number of connections per node (its degree) improves recall but also increases construction time and search latency. This trade-off is a central challenge that HNSW aims to solve.

### Creating HNSW

The key innovation of HNSW is applying the hierarchical structure of a skip list to an NSW graph. Instead of a single, flat graph, HNSW separates links into multiple layers based on their characteristic distance scale [[32]](https://arxiv.org/abs/1603.09320). The top layers contain only the longest-range links, creating a sparse but globally connected graph. Each subsequent layer becomes progressively denser, adding shorter-range links.![Image 4: The layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous.](https://cdn.sanity.io/images/vr8gru94/production/42d4a3ffc43e5dc2758ba8e5d2ef29d4c4d78254-1920x1040.png)

Image 4: The layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous. (Source [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw))

The search process mirrors that of a skip list. It begins at an entry point in the topmost layer and performs a greedy search. When a local minimum is found, the algorithm uses that node as the entry point to search the next layer down. This process repeats until it reaches the bottom layer (layer 0), which contains all the elements and the shortest-range links. The result from this final search is returned as the answer.![Image 5: The search process through the multi-layer structure of an HNSW graph.](https://cdn.sanity.io/images/vr8gru94/production/e63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png)

Image 5: The search process through the multi-layer structure of an HNSW graph. (Source [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw))

However, recent research has questioned the necessity of the hierarchy for high-dimensional data. The "Hub Highway Hypothesis" suggests that in high-dimensional spaces, proximity graphs naturally form a well-connected "highway" of hub nodes that serve the same purpose as the upper layers, allowing for efficient routing without an explicit hierarchy. According to this view, a flat NSW graph can achieve nearly identical performance to HNSW on high-dimensional embeddings, but with lower memory overhead, while the hierarchy remains beneficial primarily for low-dimensional data (d < 32) [[54]](https://arxiv.org/html/2412.01940v2).

This hierarchical approach allows HNSW to achieve logarithmic search complexity, where the number of layers grows as O(log n). The upper layers enable fast, coarse-grained navigation across the vector space, while the lower layers provide the density needed for precise, fine-grained search without the high cost of traversing the entire dense graph from the start [[32]](https://arxiv.org/abs/1603.09320). The total search cost scales logarithmically with the number of vectors, dominated by the beam search on the final layer [[56]](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture).

With the layered foundations and search behavior clarified, we now turn to the practical iterative algorithm used to construct an HNSW graph one vector at a time.

## Graph Construction

The HNSW graph is built by inserting vectors one by one. For each new vector, the algorithm first assigns it a random maximum layer level, `l`, based on an exponentially decaying probability distribution. This ensures that very few elements make it to the top layers, keeping them sparse, while the bottom layer contains every element [[27]](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW).![Image 6: The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it.](https://cdn.sanity.io/images/vr8gru94/production/f105cb148aae44f77fa7e3df7b7f8c0256bcbec4-1920x980.png)

Image 6: The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it. (Source [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw))

The probability distribution is controlled by a level multiplier parameter, `m_L`, which is typically set to `1/ln(M)`, where `M` is the number of neighbors for each node. This value is chosen to minimize the overlap of neighbors between layers, which is key to achieving optimal performance [[37]](https://www.pinecone.io/learn/series/faiss/hnsw).

The insertion process itself has two phases. First, the algorithm starts at the top layer of the existing graph and performs a greedy search to find the nearest element to the new vector. This element becomes the entry point for the next layer down. This continues until it reaches the target insertion layer `l` [[29]](https://www.pinecone.io/learn/series/faiss/hnsw).

In the second phase, starting from layer `l` and moving down to layer 0, the algorithm finds the `efConstruction` nearest neighbors to the new vector. From this set of candidates, it selects `M` neighbors to form bidirectional links with the new vector. These candidates also serve as the entry points for the search in the next layer down.

To control the graph's density, the number of links per node is capped. A parameter `M_max` limits the connections for nodes in the upper layers, while `M_max0` (usually `2*M`) sets a higher limit for the denser base layer (layer 0). If adding a new connection exceeds this limit for a node, the algorithm prunes its connections to keep only the closest ones [[40]](https://www.pinecone.io/learn/series/faiss/hnsw).![Image 7: Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0.](https://cdn.sanity.io/images/vr8gru94/production/dc5cb11ea197ceb4e1f18214066c8c51526b9af5-1920x1080.png)

Image 7: Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0. (Source [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw))

Equipped with a clear picture of how the hierarchical graph is built, we now examine the concrete Faiss implementation, index internals, parameter controls, and empirical tradeoffs observed on real workloads.

## Implementation of HNSW

We will implement HNSW using the Facebook AI Similarity Search (Faiss) library and test different construction and search parameters to see how they affect performance.

1.  First, we initialize the HNSW index. We will use `IndexHNSWFlat`, which means the actual vectors are stored as-is without compression.
    ```python
    import faiss
    import numpy as np
    
    d = 128  # vector dimension
    M = 32   # number of neighbors for each vertex
    
    index = faiss.IndexHNSWFlat(d, M)
    print(index.hnsw)
    ```
    It outputs:
    ```text
    <faiss.impl.HNSW.HNSW; proxy of <Swig Object of type 'faiss::HNSW *' at 0x13758b5a0> >
    ```
2.  When we initialize the index, we set `M`, the number of neighbors added to each vertex during insertion. The parameters `M_max` (max neighbors for upper layers) and `M_max0` (max neighbors for layer 0) are set automatically by a method called `set_default_probas`. In Faiss, this method sets `M_max = M` and `M_max0 = 2 * M` [[33]](https://www.youtube.com/watch?v=QvKMwLjdK-s).
3.  Before we add any data, the index has no layers.
    ```python
    # The HNSW index starts with no levels
    print(index.hnsw.max_level)
    
    # And levels are empty too
    levels = faiss.vector_to_array(index.hnsw.levels)
    print(np.bincount(levels))
    ```
    It outputs:
    ```text
    -1
    array([], dtype=int64)
    ```
4.  Now, let's add our data (we'll use the Sift1M dataset) and see how the structure gets populated.
    ```python
    # For this example, assume `xb` contains the 1M Sift1M vectors
    # index.add(xb)
    
    # After adding data, the max_level is set (output will vary)
    # print(index.hnsw.max_level) -> e.g., 4
    
    # And we can see the distribution of vectors across layers
    # levels = faiss.vector_to_array(index.hnsw.levels)
    # print(np.bincount(levels)) -> e.g., array([961778,  37286,   1187,     47,      2])
    ```
5.  The index also has a designated entry point, which is the starting node for all searches.
    ```python
    # print(index.hnsw.entry_point) -> e.g., 118295
    ```

### Graph Structure

The layered structure of the graph is determined by the `set_default_probas` method, which is called during initialization. This method calculates the probability of a new vector being assigned to each layer, using `M` and the level multiplier `m_L` (which defaults to `1 / log(M)`).

1.  We can replicate this logic in Python to understand how it works. The function calculates `assign_probas`, the probability for each layer, and `cum_nneighbor_per_level`, the cumulative number of neighbors.
    ```python
    def set_default_probas(M: int, m_L: float):
        nn = 0
        cum_nneighbor_per_level = []
        level = 0
        assign_probas = []
        while True:
            proba = np.exp(-level / m_L) * (1 - np.exp(-1 / m_L))
            if proba < 1e-9:
                break
            assign_probas.append(proba)
            # In Faiss, M_max0 is M*2, and M_max is M for other layers
            nn += (M * 2) if level == 0 else M
            cum_nneighbor_per_level.append(nn)
            level += 1
        return assign_probas, cum_nneighbor_per_level
    
    assign_probas, cum_nneighbor_per_level = set_default_probas(32, 1/np.log(32))
    print(f"assign_probas: {assign_probas}")
    print(f"cum_nneighbor_per_level: {cum_nneighbor_per_level}")
    ```
    It outputs:
    ```text
    assign_probas: [0.9163381363456339, 0.0768913697046166, 0.00645229568939546, 0.0005414381395318029, 4.543304128039987e-05, 3.81245035323908e-06, 3.199195932593452e-07, 2.684497559218227e-08]
    cum_nneighbor_per_level: [64, 96, 128, 160, 192, 224, 256, 288]
    ```
    As we can see, the probability of being inserted into layer 0 is over 91%, and it drops exponentially for higher layers.
2.  During insertion, the `random_level` function uses these probabilities to assign a max level to each new vector.
    ```python
    def random_level(assign_probas, m_L):
        f = np.random.rand()
        for i, proba in enumerate(assign_probas):
            if f < proba:
                return i
            f -= proba
        return len(assign_probas) - 1
    ```
3.  We can simulate this to see how closely our Python version matches the actual Faiss distribution.
    ```python
    # Simulating 1,000,000 insertions
    # levels_py = [random_level(assign_probas, 1/np.log(32)) for _ in range(1000000)]
    # print(np.bincount(levels_py))
    # -> e.g., array([916428,  76865,   6415,    541,     46,      5])
    ```
    The distribution is very similar to what Faiss produces internally.![Image 8: Distribution of vertices across layers in the Faiss implementation (left) and the Python simulation (right).](https://cdn.sanity.io/images/vr8gru94/production/75658a08c25dabc1405f769c76fd2929c051853b-1920x930.png)

Image 8: Distribution of vertices across layers in the Faiss implementation (left) and the Python simulation (right). (Source [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw))

One small detail is that Faiss guarantees that at least one vertex is present at the highest layer, which serves as the graph's entry point [[15]](https://www.pinecone.io/learn/series/faiss/hnsw).

### HNSW Performance

To understand the practical trade-offs, we can sweep through the key parameters—`M`, `efConstruction`, and `efSearch`—on the Sift1M dataset.

1.  The parameters `efConstruction` and `efSearch` control the size of the dynamic candidate list during construction and search, respectively. `efConstruction` must be set before building the index, while `efSearch` can be adjusted anytime before searching.
    ```python
    # M, efConstruction, efSearch are parameters we vary
    # index = faiss.IndexHNSWFlat(d, M)
    # index.hnsw.efConstruction = efConstruction
    # index.add(xb) # build the index
    
    # index.hnsw.efSearch = efSearch # set search-time parameter
    # D, I = index.search(xq[:1000], k=1) # search
    ```![Image 9: Recall@1 performance for various M, efConstruction, and efSearch parameters on Sift1M.](https://cdn.sanity.io/images/vr8gru94/production/e8c281c3626226a76389fa344a71eb57f70cf879-1920x980.png)

Image 9: Recall@1 performance for various M, efConstruction, and efSearch parameters on Sift1M. (Source [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw))

The results show that higher `M` and `efSearch` values significantly increase recall. A reasonably high `efConstruction` is also necessary for a well-structured graph. Increasing `efConstruction` allows you to achieve higher recall with lower `M` and `efSearch` values, giving you another lever to tune performance [[20]](https://www.pinecone.io/learn/series/faiss/hnsw).![Image 10: Search time in µs for various M, efConstruction, and efSearch parameters when searching 1000 queries. The y-axis uses a log scale.](https://cdn.sanity.io/images/vr8gru94/production/876bf66aba408959042888efe72c55db4d6b3b41-1920x980.png)

Image 10: Search time in µs for various M, efConstruction, and efSearch parameters when searching 1000 queries. The y-axis uses a log scale. (Source [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw))

This brings us to the core trade-off: recall vs. search time. Achieving near-perfect recall comes at the cost of higher latency. It's often assumed that `efConstruction` has little impact on search time, but this only holds true for very low query volumes. For a batch of 1000 queries, a higher `efConstruction` clearly increases search time.

However, when the query volume is low (e.g., a single query), increasing `efConstruction` is an excellent way to boost recall with minimal impact on latency, especially at lower `M` values.![Image 11: efConstruction and search time when searching for only one query. At lower M values, search time remains almost unchanged for different efConstruction values.](https://cdn.sanity.io/images/vr8gru94/production/ef1a2edd25adb202c0a98a1f33a0e72d1295b554-1720x1080.png)

Image 11: efConstruction and search time when searching for only one query. At lower M values, search time remains almost unchanged for different efConstruction values. (Source [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw))

Finally, memory usage is a critical factor. In HNSW, only the `M` parameter affects the index size. `efConstruction` and `efSearch` are purely search-time parameters and have no impact on memory.![Image 12: Memory usage with increasing values of M on the Sift1M dataset. efSearch and efConstruction have no effect on memory usage.](https://cdn.sanity.io/images/vr8gru94/production/e04d23ccd76d8bdc568542bebe75a75e7d36a21e-1480x1050.png)

Image 12: Memory usage with increasing values of M on the Sift1M dataset. efSearch and efConstruction have no effect on memory usage. (Source [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw))

The memory footprint grows quickly with `M`. On the Sift1M dataset, the index size exceeds 0.5GB with just `M=2` and balloons to nearly 5GB at `M=512`. This highlights the three-way trade-off between recall, latency, and memory costs that engineers must navigate when deploying HNSW in production.

This memory cost is a key point of contention. For high-dimensional datasets like Sift1M, some studies suggest that the hierarchy itself provides little to no performance benefit over a flat NSW graph. Benchmarks have shown that a single-layer graph can match HNSW's recall and latency but with up to 38% less peak memory consumption during construction, challenging the conventional wisdom that the hierarchy's memory cost is a necessary trade-off for speed [[54]](https://arxiv.org/html/2412.01940v2).

### Improving Memory Usage and Search Speeds

When the memory requirements of HNSW become too high, you can turn to other techniques. One common approach is to compress the stored vectors using Product Quantization (PQ), which dramatically reduces memory usage at the cost of some recall and speed. Another strategy is to wrap HNSW with an Inverted File (IVF) component, which can improve search speed by partitioning the dataset. These composite indexes combine the strengths of multiple methods to find the optimal balance for a given application.

## Conclusion

HNSW stands as a testament to the power of combining simple, elegant ideas—probabilistic skip lists and navigable small world graphs—to solve a complex problem. Its hierarchical structure enables an efficient search that starts broad and progressively narrows, achieving state-of-the-art performance in approximate nearest neighbor search. By understanding its construction, the role of its key parameters, and the fundamental trade-offs between recall, latency, and memory, you are now equipped to build and tune high-performance vector search systems. While HNSW is powerful on its own, its true potential in production is often unlocked when combined with other techniques like IVF and PQ, a topic we explore further in our article on composite indexes. Its applications extend far beyond typical semantic search, powering fields like computational biology, where it has achieved speedups of over 500x in searching massive spectral data repositories [[57]](https://www.biorxiv.org/content/10.64898/2026.06.02.729602v1.full-text).

## References

- [1] Y. Malkov, A. Ponomarenko, A. Logvinov, V. Krylov. (2011). Approximate Nearest Neighbor Search Small World Approach. [https://www.iiis.org/CDs2011/CD2011IDI/ICTA_2011/PapersPdf/CT175ON.pdf](https://www.iiis.org/CDs2011/CD2011IDI/ICTA_2011/PapersPdf/CT175ON.pdf)
- [2] Y. Malkov, A. Ponomarenko, A. Logvinov, V. Krylov. (2012). Scalable Distributed Algorithm for Approximate Nearest Neighbor Search Problem in High Dimensional General Metric Spaces. [https://www.researchgate.net/publication/262334462_Scalable_Distributed_Algorithm_for_Approximate_Nearest_Neighbor_Search_Problem_in_High_Dimensional_General_Metric_Spaces](https://www.researchgate.net/publication/262334462_Scalable_Distributed_Algorithm_for_Approximate_Nearest_Neighbor_Search_Problem_in_High_Dimensional_General_Metric_Spaces)
- [3] Y. Malkov, A. Ponomarenko, A. Logvinov, V. Krylov. (2014). Approximate nearest neighbor algorithm based on navigable small world graphs. [https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059](https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059)
- [4] LANNS: A Web-Scale Approximate Nearest Neighbor Lookup System. (2022). [https://www.vldb.org/pvldb/vol15/p850-doshi.pdf](https://www.vldb.org/pvldb/vol15/p850-doshi.pdf)
- [5] J. P. Ramos. (n.d.). Faiss Part 4: HNSW. Pinecone. [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw)
- [6] K. Notes. (2023). Understading HNSW — Hierarchical Navigable Small World. Medium. [https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605](https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605)
- [7] A. Fish. (2023). Similarity Search, Part 4: Hierarchical Navigable Small World (HNSW). Towards Data Science. [https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37)
- [8] Y. Malkov, D. Yashunin. (2016). Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs. [https://arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320)
- [9] E. Bern. (2021). Paper review: Efficient and robust approximate nearest neighbor search using hierarchical navigable. Medium. [https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf](https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf)
- [10] Y. Malkov, D. Yashunin. (2016). Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs. [https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf)
- [11] J. P. Ramos. (n.d.). Facebook AI and the Index Factory. Pinecone. [https://www.pinecone.io/learn/series/faiss/composite-indexes/](https://www.pinecone.io/learn/series/faiss/composite-indexes/)
- [12] M. Doshi. (2022). HNSW: The need for speed. OpenReview. [https://openreview.net/pdf/9d557864b10a646d79ecf63772864cc3c168091f.pdf](https://openreview.net/pdf/9d557864b10a646d79ecf63772864cc3c168091f.pdf)
- [13] W. G. (2021). IVFPQ + HNSW for Billion-Scale Similarity Search. Towards Data Science. [https://towardsdatascience.com/ivfpq-hnsw-for-billion-scale-similarity-search-89ff2f89d90e](https://towardsdatascience.com/ivfpq-hnsw-for-billion-scale-similarity-search-89ff2f89d90e)
- [14] J. P. Ramos. (2021). HNSW. Pinecone. [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw)
- [15] J. P. Ramos. (2021). Faiss HNSW Implementation. YouTube. [https://www.youtube.com/watch?v=QvKMwLjdK-s](https://www.youtube.com/watch?v=QvKMwLjdK-s)
- [16] Milvus. (n.d.). What are the key configuration parameters for an HNSW index. Milvus. [https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall](https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall)
- [17] Github. (n.d.). Indexing 1M vectors. [https://github.com/facebookresearch/faiss/wiki/Indexing-1M-vectors](https://github.com/facebookresearch/faiss/wiki/Indexing-1M-vectors)
- [18] Y. Chen, Y. Tian. (2024). A Comprehensive Survey on HNSW for Real-World Applications. arXiv. [https://arxiv.org/html/2412.01940v2](https://arxiv.org/html/2412.01940v2)
- [19] MongoDB. (n.d.). Hierarchical Navigable Small World (HNSW). [https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world](https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world)
- [20] A. Masood. (2023). The Shortcut Through Space: Hierarchical Navigable Small Worlds (HNSW) in Vector Search. Medium. [https://medium.com/@adnanmasood/the-shortcut-through-space-hierarchical-navigable-small-worlds-hnsw-in-vector-search-4df5aa755100](https://medium.com/@adnanmasood/the-shortcut-through-space-hierarchical-navigable-small-worlds-hnsw-in-vector-search-4df5aa755100)
- [21] Zilliz. (n.d.). What is HNSW?. [https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW)
- [22] Faiss. (n.d.). HNSW.h. [https://github.com/efficient/faiss-learned-termination/blob/master/HNSW.h](https://github.com/efficient/faiss-learned-termination/blob/master/HNSW.h)
- [23] Faiss. (n.d.). Faiss HNSW Struct Reference. [https://faiss.ai/cpp_api/struct/structfaiss_1_1HNSW.html](https://faiss.ai/cpp_api/struct/structfaiss_1_1HNSW.html)
- [24] S. Zhang. (2023). Write You a Vector DB, Part 6 Chapter 2: HNSW Index. [https://skyzh.github.io/write-you-a-vector-db/cpp-06-02-hnsw.html](https://skyzh.github.io/write-you-a-vector-db/cpp-06-02-hnsw.html)
- [25] M. Watson. (2021). HNSW Graph. Elastic. [https://www.elastic.co/search-labs/blog/hnsw-graph](https://www.elastic.co/search-labs/blog/hnsw-graph)
- [26] Vespa. (n.d.). Approximate Nearest Neighbor Search (ANN) using HNSW. [https://docs.vespa.ai/en/querying/approximate-nn-hnsw.html](https://docs.vespa.ai/en/querying/approximate-nn-hnsw.html)
- [27] GeeksforGeeks. (n.d.). Skip List. [https://www.geeksforgeeks.org/dsa/skip-list](https://www.geeksforgeeks.org/dsa/skip-list)
- [28] Wikipedia. (n.d.). Skip list. [https://en.wikipedia.org/wiki/Skip_list](https://en.wikipedia.org/wiki/Skip_list)
- [29] Brilliant. (n.d.). Skip Lists. [https://brilliant.org/wiki/skip-lists](https://brilliant.org/wiki/skip-lists)
- [30] W. Pugh. (1990). Skip Lists: A Probabilistic Alternative to Balanced Trees. [https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)
- [31] I. Doshi, et al. (2022). LANNS: A Web-Scale Approximate Nearest Neighbor Lookup System. [https://www.vldb.org/pvldb/vol15/p850-doshi.pdf](https://www.vldb.org/pvldb/vol15/p850-doshi.pdf)
- [32] Y. Malkov, D. Yashunin. (2016). Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs. [https://arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320)
- [33] J. P. Ramos. (2021). Faiss HNSW Implementation. YouTube. [https://www.youtube.com/watch?v=QvKMwLjdK-s](https://www.youtube.com/watch?v=QvKMwLjdK-s)
- [34] A. Fish. (2023). Similarity Search, Part 4: Hierarchical Navigable Small World (HNSW). Towards Data Science. [https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37)
- [35] Y. Malkov, et al. (2012). Scalable Distributed Algorithm for Approximate Nearest Neighbor Search Problem in High Dimensional General Metric Spaces. [https://www.researchgate.net/publication/262334462_Scalable_Distributed_Algorithm_for_Approximate_Nearest_Neighbor_Search_Problem_in_High_Dimensional_General_Metric_Spaces](https://www.researchgate.net/publication/262334462_Scalable_Distributed_Algorithm_for_Approximate_Nearest_Neighbor_Search_Problem_in_High_Dimensional_General_Metric_Spaces)
- [36] Y. Malkov, et al. (2014). Approximate nearest neighbor algorithm based on navigable small world graphs. [https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059](https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059)
- [37] J. P. Ramos. (2021). Faiss HNSW. Pinecone. [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw)
- [38] A. Ponomarenko, et al. (2011). Approximate Nearest Neighbor Search Small World Approach. [https://www.iiis.org/CDs2011/CD2011IDI/ICTA_2011/PapersPdf/CT175ON.pdf](https://www.iiis.org/CDs2011/CD2011IDI/ICTA_2011/PapersPdf/CT175ON.pdf)
- [39] Y. Malkov, A. Ponomarenko. (2015). Growing homophilic networks are natural navigable small worlds. [https://arxiv.org/abs/1507.06529](https://arxiv.org/abs/1507.06529)
- [40] J. P. Ramos. (2021). Faiss HNSW. Pinecone. [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw)
- [41] M. Boguñá, D. Krioukov, kc claffy. (2009). Navigability of complex networks. [https://arxiv.org/abs/0709.0303](https://arxiv.org/abs/0709.0303)
- [42] W. Pugh. (1990). Skip Lists: A Probabilistic Alternative to Balanced Trees. [https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)
- [43] Y. Malkov, D. Yashunin. (2016). Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs. [https://arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320)
- [44] Y. Malkov, et al. (2014). Approximate nearest neighbor algorithm based on navigable small world graphs. [https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059](https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059)
- [45] Wikipedia. (n.d.). Skip list. [https://en.wikipedia.org/wiki/Skip_list](https://en.wikipedia.org/wiki/Skip_list)
- [46] W. Pugh. (1990). Skip Lists: A Probabilistic Alternative to Balanced Trees. [https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)
- [47] Y. Malkov, A. Ponomarenko. (2015). Growing homophilic networks are natural navigable small worlds. [https://arxiv.org/abs/1507.06529](https://arxiv.org/abs/1507.06529)
- [48] M. Boguñá, D. Krioukov, kc claffy. (2009). Navigability of complex networks. [https://arxiv.org/abs/0709.0303](https://arxiv.org/abs/0709.0303)
- [49] A. Ponomarenko, et al. (2011). Approximate Nearest Neighbor Search Small World Approach. [https://www.iiis.org/CDs2011/CD2011IDI/ICTA_2011/PapersPdf/CT175ON.pdf](https://www.iiis.org/CDs2011/CD2011IDI/ICTA_2011/PapersPdf/CT175ON.pdf)
- [50] M. Boguñá, D. Krioukov, kc claffy. (2009). Navigability of complex networks. [https://arxiv.org/abs/0709.0303](https://arxiv.org/abs/0709.0303)
- [51] Faiss. (n.d.). HNSW.cpp. [https://github.com/facebookresearch/faiss/blob/main/faiss/impl/HNSW.cpp](https://github.com/facebookresearch/faiss/blob/main/faiss/impl/HNSW.cpp)
- [52] J. P. Ramos. (n.d.). Faiss. [https://www.pinecone.io/learn/series/faiss/](https://www.pinecone.io/learn/series/faiss/)
- [53] Milvus. (n.d.). What is HNSW and why is it popular for vector search? [https://milvus.io/ai-quick-reference/what-is-hnsw-and-why-is-it-popular-for-vector-search](https://milvus.io/ai-quick-reference/what-is-hnsw-and-why-is-it-popular-for-vector-search)
- [54] B. Munyampirwa, V. Lakshman, B. Coleman. (2024). Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”. [https://arxiv.org/html/2412.01940v2](https://arxiv.org/html/2412.01940v2)
- [55] K. Ramoliya. (n.d.). Understading HNSW — Hierarchical Navigable Small World. [https://keyurramoliya.com/posts/Understading-HNSW-Hierarchical-Navigable-Small-World](https://keyurramoliya.com/posts/Understading-HNSW-Hierarchical-Navigable-Small-World)
- [56] M. Brenndörfer. (n.d.). HNSW Index: The Architecture of Vector Search. [https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture)
- [57] S. J. T. et al. (2024). HNSW-MS: Accelerating mass spectral similarity search with approximate nearest neighbor indexing. [https://www.biorxiv.org/content/10.64898/2026.06.02.729602v1.full-text](https://www.biorxiv.org/content/10.64898/2026.06.02.729602v1.full-text)