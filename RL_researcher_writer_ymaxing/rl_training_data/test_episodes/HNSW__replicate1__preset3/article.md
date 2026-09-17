# Hierarchical Navigable Small World (HNSW)![Hierarchical Navigable Small World (HNSW) graph overview](https://cdn.sanity.io/images/vr8gru94/production/d6e3a660654d9cb55f7ac137a736539e227296b6-1920x1080.png)
Image 1: An overview of the Hierarchical Navigable Small World (HNSW) graph structure. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

Hierarchical Navigable Small World (HNSW) has become a cornerstone of modern Approximate Nearest Neighbor (ANN) search. It consistently delivers state-of-the-art recall with sub-millisecond query speeds, even on massive vector datasets, outperforming older methods like Inverted File (IVF) indexes or Locality-Sensitive Hashing (LSH) [[1]](https://www.vldb.org/pvldb/vol15/p850-doshi.pdf). Despite its widespread adoption in vector databases and retrieval systems, its internal mechanics often remain a black box for many engineers. This article aims to demystify HNSW, breaking down its theoretical foundations and walking through its construction algorithm. Towards the end, we’ll look at how to implement HNSW using Faiss and explore which parameter settings give us the performance we need [[2]](https://towardsdatascience.com/ivfpq-hnsw-for-billion-scale-similarity-search-89ff2f89d90e). Now that we understand why HNSW is important, let's examine its two theoretical foundations: probabilistic skip lists and navigable small world graphs.

## Foundations of HNSW

Within the ANN landscape, HNSW belongs to the category of proximity graphs. In these graphs, nodes represent vectors, and edges connect vectors that are close to each other in the given metric space (like Euclidean distance). HNSW represents a notable leap in complexity from a simple proximity graph by integrating two powerful concepts: the probabilistic skip list and the navigable small world graph [[3]](https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf).

### Probability Skip List

A skip list is a probabilistic data structure that enables fast search, similar to a sorted array, while also allowing for fast insertions and deletions, like a linked list [[4]](https://www.geeksforgeeks.org/dsa/skip-list). It achieves this by building multiple layers of linked lists on top of a base list. The bottom layer is a standard sorted linked list containing all elements. Each subsequent layer acts as an "express lane," containing a random subset of the elements from the layer below it. An element in layer `i` has a fixed probability `p` of also appearing in layer `i+1` [[5]](https://en.wikipedia.org/wiki/Skip_list). On average, this structure contains `log(n)` lists and allows for search, insertion, and deletion operations with an average complexity of O(log n) [[6]](https://brilliant.org/wiki/skip-lists).![A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for (or we reach the end), we drop to the next layer.](https://cdn.sanity.io/images/vr8gru94/production/9065d31e1b2e33ca697a56082f0ece7eff1c2d9b-1920x500.png)
Image 2: A probability skip list structure. The search starts on the top layer and drops down when it overshoots the target. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

To search for an element, you start at the head of the sparsest, topmost list. You traverse horizontally until you find an element greater than your target or reach the end of the list. At that point, you drop down to the next layer from the previous element and repeat the process. This allows you to skip large portions of the list, resulting in an average search complexity of O(log n) [[6]](https://brilliant.org/wiki/skip-lists). HNSW inherits this core idea of a multi-layered structure with probabilistic placement, which allows for a coarse-to-fine search strategy.

### Navigable Small World Graphs

Navigable Small World (NSW) graphs are networks designed for efficient greedy routing, achieving a (poly)logarithmic search complexity relative to the number of nodes [[7]](https://www.pinecone.io/learn/series/faiss/hnsw). They are characterized by a combination of short-range links, connecting nearby nodes (friends), and long-range links, which act as bridges between distant parts of the graph [[8]](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf).![The search process through a NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector.](https://cdn.sanity.io/images/vr8gru94/production/5ca4fca27b2a9bf89b06748b39b7b6238fd4548c-1920x1080.png)
Image 3: The greedy search process in a Navigable Small World (NSW) graph. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

The search process, known as greedy routing, begins at a designated entry point. At each step, the algorithm evaluates the neighbors of the current node and moves to the one closest to the query vector. This process is repeated until it reaches a local minimum. A local minimum is a node where none of its neighbors are closer to the query [[9]](https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605).

Routing in an NSW graph typically involves two phases. The initial "zoom-out" phase uses long-range links connecting low-degree vertices to quickly traverse large distances across the graph. This allows the search to rapidly approach the general vicinity of the target. As the search gets closer, it enters a "zoom-in" phase, where it navigates through higher-degree vertices with shorter-range links to refine its position and find the nearest neighbor [[10]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).

However, this greedy approach can get trapped in a local minimum if the graph's connectivity is insufficient, leading to a suboptimal result and reduced recall. This problem is especially prevalent in the "zoom-out" phase, where low-degree nodes offer fewer paths forward. If none of the few available neighbors are closer to the query, the search stops prematurely. This creates a fundamental trade-off. Increasing the average degree of vertices (the number of links per node) reduces the chance of getting stuck, thereby improving recall. However, a denser graph increases network complexity, which in turn raises both the construction time and the search time per query. This balance between vertex degree and performance is a central tuning axis in graph-based ANN methods.

This challenge is amplified in high-dimensional spaces due to a phenomenon known as the "curse of dimensionality." As dimensions increase, the distances between points become less meaningful, making it difficult to distinguish between near and far neighbors [[11]](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture). This can weaken the greedy search's directional progress. Consequently, while NSW aims for logarithmic complexity, some studies note this is not always achieved in practice, as random graph construction can create disconnected regions that trap the search in local optima [[12]](https://arxiv.org/html/2501.13992v2).

### Creating HNSW

The key innovation of HNSW is the application of the probabilistic, layered structure of a skip list to an NSW graph. This creates a hierarchy of proximity graphs, where each layer is a sparser-than-the-last subset of the graph [[13]](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf). The top layers contain only the longest-range links, providing a coarse view of the data space, while the bottom layers contain dense, short-range links for fine-grained search.![Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous.](https://cdn.sanity.io/images/vr8gru94/production/42d4a3ffc43e5dc2758ba8e5d2ef29d4c4d78254-1920x1040.png)
Image 4: The hierarchical structure of an HNSW graph, separating links by scale into different layers. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

The search process in HNSW mirrors that of a skip list. It starts at an entry point in the top layer and performs a greedy search. When a local minimum is found, the search drops down to the layer below, using the found minimum as the new entry point. This process is repeated, descending layer by layer, until the search is completed on the bottom-most layer (layer 0).![The search process through the multi-layer structure of an HNSW graph.](https://cdn.sanity.io/images/vr8gru94/production/e63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png)
Image 5: The search process in HNSW descends through layers, refining the search at each step. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

This hierarchical approach provides a clear advantage over a flat NSW graph. By starting with only long-range links, the algorithm quickly navigates to the right region of the graph. As it descends, the density of links increases, allowing for a more precise search. This avoids the high cost of traversing the dense base layer from the beginning, leading to a logarithmic time complexity. With the layered foundations and search behavior clarified, we now turn to the practical iterative algorithm used to construct an HNSW graph one vector at a time.

## Graph Construction

The HNSW graph is built by inserting vectors one-by-one. Each new vector is assigned a random maximum layer `l` based on an exponentially decaying probability distribution [[14]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37). This ensures most vectors reside in lower layers, with a few promoted to higher, sparser layers. The vector is then inserted into all layers from `l` down to 0.![The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it.](https://cdn.sanity.io/images/vr8gru94/production/f105cb148aae44f77fa7e3df7b7f8c0256bcbec4-1920x980.png)
Image 6: The probabilistic layer assignment for a new vector during HNSW graph construction. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

The probability distribution is controlled by a level multiplier, `m_L`. Performance is optimal when the overlap of shared neighbors between layers is minimized. The authors of HNSW propose an optimal value of `m_L` ≈ `1/ln(M)`, where `M` is the number of neighbors for each vertex. This value balances neighbor overlap and search efficiency, helping to keep the number of traversals logarithmic [[15]](https://www.pinecone.io/learn/series/faiss/hnsw).

The insertion process for a new vector involves two phases [[16]](https://www.pinecone.io/learn/series/faiss/hnsw). First, starting from the top layer, the algorithm performs a greedy search (with search parameter `ef=1`) to find the single nearest neighbor to the new vector. This neighbor becomes the entry point for the layer below. This is repeated until the randomly assigned insertion layer `l` is reached.

In the second phase, starting from layer `l`, the search becomes more thorough. The `ef` parameter is increased to a user-defined construction parameter, `efConstruction`. A greedy search is performed to find the `efConstruction` nearest neighbors. These neighbors serve as the candidate set from which `M` links will be created to the new vector. The `M` links are not simply the closest candidates. A selection heuristic is used to promote diverse connections, which helps link distant regions of the graph and improve navigability [[14]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37). After connecting the new vector, the algorithm drops to the layer below, using the found candidates as entry points, and repeats the process until it reaches layer 0.![Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0.](https://cdn.sanity.io/images/vr8gru94/production/dc5cb11ea197ceb4e1f18214066c8c51526b9af5-1920x1080.png)
Image 7: A new vertex is connected to M neighbors, but existing vertices may have their links trimmed to not exceed M_max (or M_max0 on layer 0). (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

The number of connections per vertex is capped. For layers greater than 0, a vertex can have at most `M_max` connections. For the dense base layer (layer 0), this limit is `M_max0`. In the Faiss implementation, `M_max` is typically set to `M`, while `M_max0` is set to `2*M` to ensure dense connectivity at the bottom for a precise final search [[17]](https://www.pinecone.io/learn/series/faiss/hnsw). If adding a new connection to an existing node exceeds its limit, the node's neighbor list is pruned to keep only the closest ones. Equipped with a clear picture of how the hierarchical graph is built, we now examine the concrete Faiss implementation, index internals, parameter controls, and empirical tradeoffs observed on real workloads.

## Implementation of HNSW

We will implement HNSW using the Facebook AI Similarity Search (Faiss) library and test different construction and search parameters to see how they affect index performance.

1.  First, let's set up our HNSW parameters and initialize the index. We will use a vector size `d` of 128 and set `M`, the number of neighbors to add for each vertex, to 32.
    ```python
    import faiss
    import numpy as np
    
    # setup our HNSW parameters
    d = 128  # vector size
    M = 32
    
    index = faiss.IndexHNSWFlat(d, M)
    print(index.hnsw)
    ```
    It outputs:
    ```text
    >
    ```
    This initializes a flat HNSW index. The `M` parameter controls the number of bidirectional links created for each new node [[18]](https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall). However, the per-layer caps, `M_max` and `M_max0`, are set automatically by Faiss's `set_default_probas` method, which is called during initialization. This method sets `M_max` to `M` and `M_max0` to `2*M` [[15]](https://www.pinecone.io/learn/series/faiss/hnsw).

2.  Before we add data, the index has no layers.
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

3.  Now, let's build the index with some data. We will use the Sift1M dataset. After adding the data, we can inspect the graph structure.
    ```python
    # 'xb' is the Sift1M dataset base vectors
    index.add(xb)
    
    print(f"Maximum layer: {index.hnsw.max_level}")
    
    levels = faiss.vector_to_array(index.hnsw.levels)
    print(f"Distribution of levels: {np.bincount(levels)}")
    ```
    It outputs:
    ```text
    Maximum layer: 4
    Distribution of levels: [916422  75463   7320    721     74]
    ```
    The index now has a `max_level` of 4, and the `bincount` shows the distribution of the 1 million vectors across the 5 layers (0 through 4), with the vast majority residing in the bottom layer.

4.  The graph also has a designated entry point, which is the starting node for all searches.
    ```python
    print(f"Entry point: {index.hnsw.entry_point}")
    ```
    It outputs:
    ```text
    Entry point: 118295
    ```

### Graph Structure

The layer assignment in Faiss is determined by the `set_default_probas` method. It takes `M` and a level multiplier `m_L` (called `levelMult` in Faiss), which is set to `1 / log(M)` by default. This method calculates the probability of a new node being assigned to each layer [[19]](https://www.pinecone.io/learn/series/faiss/hnsw).

1.  Here is a Python equivalent of that Faiss method. It calculates `assign_probas`, the probability of insertion at a given layer, and `cum_nneighbor_per_level`, the cumulative total of neighbors for a vertex at different insertion levels. The formula `proba = np.exp(-level / m_L) * (1 - np.exp(-1 / m_L))` implements the exponentially decaying probability distribution, ensuring higher layers are progressively sparser.
    ```python
    def set_default_probas(M: int, m_L: float):
        nn = 0
        cum_nneighbor_per_level = []
        assign_probas = []
        level = 0
        M2 = M * 2
        while True:
            proba = np.exp(-level / m_L) * (1 - np.exp(-1 / m_L))
            if proba < 1e-9:
                break
            assign_probas.append(proba)
            nn += M2 if level == 0 else M
            cum_nneighbor_per_level.append(nn)
            level += 1
        return assign_probas, cum_nneighbor_per_level
    ```

2.  Let's see the probabilities and cumulative neighbor counts for our configuration. The `cum_nneighbor_per_level` output shows the total number of neighbors a node would have if it were inserted at that level (e.g., 64 for layer 0, 96 for layer 1, etc.).
    ```python
    assign_probas, cum_nneighbor_per_level = set_default_probas(32, 1/np.log(32))
    print(f"assign_probas: {assign_probas}")
    print(f"cum_nneighbor_per_level: {cum_nneighbor_per_level}")
    ```
    It outputs:
    ```text
    assign_probas: [0.96875, 0.030273437499999986, 0.0009460449218749991, 2.956390380859371e-05, 9.23871994018553e-07, 2.887099981307982e-08]
    cum_nneighbor_per_level: [64, 96, 128, 160, 192, 224]
    ```
    As expected, the probability of being assigned to layer 0 is extremely high (≈97%), and it drops exponentially for higher layers.

3.  The `random_level` function uses these probabilities to assign a layer to a new vector. It generates a random number and finds which probability bucket it falls into.
    ```python
    def random_level(assign_probas):
        f = np.random.random()
        for i in range(len(assign_probas)):
            if f < assign_probas[i]:
                return i
            f -= assign_probas[i]
        return len(assign_probas) - 1
    ```

4.  We can simulate this process to see if it matches the distribution we observed from Faiss. We first normalize the probabilities to ensure they sum to 1 for the simulation.
    ```python
    # we need to normalize the probabilities first
    assign_probas_norm = np.array(assign_probas) / np.sum(assign_probas)
    
    # simulate 1M insertions
    lvls = [random_level(assign_probas_norm) for i in range(1000000)]
    print(np.bincount(lvls))
    ```
    It outputs:
    ```text
    [969713  29375    891     21]
    ```
    The simulated distribution is remarkably close to the actual distribution generated by Faiss. The Faiss implementation also ensures there is always at least one element in the highest layer to serve as the entry point for searches.![Distribution of vertices across layers in both the Faiss implementation (left) and the Python implementation (right).](https://cdn.sanity.io/images/vr8gru94/production/75658a08c25dabc1405f769c76fd2929c051853b-1920x930.png)
Image 8: Distribution of vertices across layers in the Faiss (left) and Python (right) implementations shows a close match. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

### HNSW Performance

The performance of HNSW is a trade-off between recall, search speed, and memory usage, primarily controlled by three parameters:
*   **M**: The number of connections for each new vertex during construction. Affects memory and recall.
*   **efConstruction**: The size of the candidate list during construction. Affects index build time and quality.
*   **efSearch**: The size of the candidate list during search. Affects search time and recall.

Let's empirically test these parameters on the Sift1M dataset.

1.  We can modify `efConstruction` and `efSearch` after initializing the index. `efConstruction` must be set before building the index, while `efSearch` can be set anytime before searching.
    ```python
    # M, efSearch, and efConstruction are varied in a loop for testing
    index = faiss.IndexHNSWFlat(d, M)
    index.hnsw.efConstruction = efConstruction
    index.add(xb)  # build the index
    index.hnsw.efSearch = efSearch  # and now we can search
    index.search(xq[:1000], k=1)
    ```

2.  The results show that higher `M` and `efSearch` values substantially improve recall. A reasonably high `efConstruction` is also necessary for good performance, and it can help compensate for lower `M` and `efSearch` values. For instance, at `M=16`, increasing `efSearch` from 16 to 128 provides a large boost in recall, while the same increase at `M=64` yields a smaller marginal gain. A high `efConstruction` value like 400 consistently provides the highest recall ceiling for any given `M` and `efSearch` combination.![Recall@1 performance for various M, efConstruction, and efSearch parameters.](https://cdn.sanity.io/images/vr8gru94/production/e8c281c3626226a76389fa344a71eb57f70cf879-1920x980.png)
Image 9: Recall@1 performance for various M, efConstruction, and efSearch parameters on Sift1M. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

3.  Search time, naturally, increases as we raise these parameters. The plot below shows the search time for a batch of 1000 queries. It is often stated that `efConstruction` has little effect on search time, but this is only true for small query volumes. For larger batches, a higher `efConstruction` leads to a better-quality graph that can actually speed up batched searches by enabling more efficient traversal paths.![Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is using a log scale.](https://cdn.sanity.io/images/vr8gru94/production/876bf66aba408959042888efe72c55db4d6b3b41-1920x980.png)
Image 10: Search time for 1000 queries with varying parameters. The y-axis is on a log scale. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

4.  When the query volume is low (e.g., a single query), increasing `efConstruction` provides a boost in recall with almost no added latency, especially at lower values of `M`. This makes it an excellent parameter to tune for high-recall, low-latency applications where queries are handled individually rather than in large batches.![efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values.](https://cdn.sanity.io/images/vr8gru94/production/ef1a2edd25adb202c0a98a1f33a0e72d1295b554-1720x1080.png)
Image 11: For a single query, search time is less sensitive to efConstruction, especially with smaller M. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

5.  Finally, memory usage is solely dependent on `M`. Neither `efConstruction` nor `efSearch` impacts the final index size. The memory footprint grows substantially with `M`, from over 0.5 GB at `M=2` to nearly 5 GB at `M=512` for the Sift1M dataset. The memory cost per vector can be approximated as `d*4` bytes for the vector plus `2*M*4` bytes for the connections on layer 0, where most links reside. For a 768-dimension vector with M=16, this is about 3.2 KB per vector, or 3.2 GB per million vectors [[11]](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture). At a billion-vector scale, this can translate to terabytes of RAM, making memory a primary constraint in system design [[20]](https://medium.com/vespa/billion-scale-vector-search-using-hybrid-hnsw-if-96d7058037d3). This highlights the critical trade-off between recall, latency, and the infrastructure cost required to host the index.![Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage.](https://cdn.sanity.io/images/vr8gru94/production/e04d23ccd76d8bdc568542bebe75a75e7d36a21e-1480x1050.png)
Image 12: Memory usage increases linearly with M, while efSearch and efConstruction have no impact. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

### Improving Memory Usage and Search Speeds

When the memory requirements of a standard HNSW index become prohibitive, there are two common strategies to mitigate this. First, you can compress the stored vectors using Product Quantization (PQ), which greatly reduces memory usage at the cost of some recall and increased search time. Second, you can wrap the HNSW index within an Inverted File (IVF) structure. This partitions the data into cells and uses HNSW to quickly find the most promising cells to search, improving search speed on very large datasets. These techniques create composite indexes, a topic explored in more detail in our article on that subject (https://www.pinecone.io/learn/series/faiss/composite-indexes/).

## Conclusion

HNSW is a notable ANN search method that integrates the layered, probabilistic nature of skip lists with the efficient greedy routing of navigable small world graphs. This hierarchical design allows it to achieve state-of-the-art performance, quickly navigating to the correct region of the vector space in its upper layers before refining the search in the dense lower layers.

Through our exploration of the Faiss implementation, we have seen how the graph is constructed and how its performance is a direct result of the trade-offs between key parameters. `M` controls the graph's connectivity and memory footprint, `efConstruction` dictates the quality of the index build, and `efSearch` tunes the balance between search accuracy and speed. Understanding these levers is not just academic; it is essential for any AI engineer tasked with building high-performance RAG pipelines, semantic search engines, or any system that relies on fast and accurate vector retrieval.

Beyond its core mechanics, HNSW is a versatile tool applied in domains ranging from recommendation engines and collaborative filtering to genomics, where it has been adapted for sequence similarity search using non-Euclidean distances [[21]](https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world)[[22]](https://escholarship.org/content/qt96h3s2sx/qt96h3s2sx_noSplash_e05e309fdf19eb7f453310a9459acdcc.pdf). As vector search becomes ubiquitous, research continues to push boundaries. Emerging hardware accelerations are optimizing HNSW for edge devices [[23]](https://arxiv.org/html/2502.18113v1). Furthermore, recent studies question if the hierarchy is needed at all for high-dimensional data, proposing a "Hub Highway Hypothesis" where naturally forming hub nodes provide fast traversal without explicit layers, paving the way for simpler, more memory-efficient models [[24]](https://arxiv.org/html/2412.01940v2).

## References

- [1] [LANNS: A Web-Scale Approximate Nearest Neighbor Lookup System](https://www.vldb.org/pvldb/vol15/p850-doshi.pdf)
- [2] [IVFPQ + HNSW for Billion-Scale Similarity Search](https://towardsdatascience.com/ivfpq-hnsw-for-billion-scale-similarity-search-89ff2f89d90e)
- [3] [Paper Review: Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World](https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf)
- [4] [Skip List](https://www.geeksforgeeks.org/dsa/skip-list)
- [5] [Skip list - Wikipedia](https://en.wikipedia.org/wiki/Skip_list)
- [6] [Skip Lists](https://brilliant.org/wiki/skip-lists)
- [7] [Implementing HNSW](https://www.pinecone.io/learn/series/faiss/hnsw)
- [8] [Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf)
- [9] [Understading HNSW (Hierarchical Navigable Small World)](https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605)
- [10] [Similarity Search, Part 4: Hierarchical Navigable Small World (HNSW)](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37)
- [11] [HNSW Index for Vector Search: An Architecture Overview](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture)
- [12] [Hierarchical Navigable Small World Graph for Scalable and Efficient Approximate Nearest Neighbor Search](https://arxiv.org/html/2501.13992v2)
- [13] [Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf)
- [14] [Similarity Search, Part 4: Hierarchical Navigable Small World (HNSW)](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37)
- [15] [Implementing HNSW](https://www.pinecone.io/learn/series/faiss/hnsw)
- [16] [Implementing HNSW](https://www.pinecone.io/learn/series/faiss/hnsw)
- [17] [Implementing HNSW](https://www.pinecone.io/learn/series/faiss/hnsw)
- [18] [What are the key configuration parameters for an HNSW index (such as M and efConstruction/efSearch), and how does each influence the trade-off between index size, build time, query speed, and recall?](https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall)
- [19] [Implementing HNSW](https://www.pinecone.io/learn/series/faiss/hnsw)
- [20] [Billion-scale vector search with Vespa — part two](https://medium.com/vespa/billion-scale-vector-search-using-hybrid-hnsw-if-96d7058037d3)
- [21] [Hierarchical Navigable Small World (HNSW) Explained](https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world)
- [22] [Annembed: a Rust library for scalable approximate nearest neighbor embedding](https://escholarship.org/content/qt96h3s2sx/qt96h3s2sx_noSplash_e05e309fdf19eb7f453310a9459acdcc.pdf)
- [23] [A Survey of Hardware-Software Co-Design for Graph-Based Approximate Nearest Neighbor Search](https://arxiv.org/html/2502.18113v1)
- [24] [Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”](https://arxiv.org/html/2412.01940v2)