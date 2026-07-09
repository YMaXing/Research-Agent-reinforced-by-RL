# A Deep Dive into HNSW: The Unsung Hero of Vector Search

Hierarchical Navigable Small World (HNSW) is one of the most powerful algorithms in modern AI. It consistently delivers state-of-the-art recall with sub-millisecond search speeds on massive vector collections, powering high-performance vector databases and retrieval systems everywhere. This performance has made it a cornerstone of production RAG and semantic search applications, outclassing older methods like Inverted File (IVF) or Locality-Sensitive Hashing (LSH). Its effectiveness extends to complex, high-stakes domains like multimodal retrieval, where for corpora under a few million vectors, HNSW is often the default starting point [[9]](https://www.soeasie.com/blog/considerations-for-optimizing-media-retrieval-systems-using-multimodal-embeddings).![Image 1: An overview of a Hierarchical Navigable Small World (HNSW) graph.](https://cdn.sanity.io/images/vr8gru94/production/d6e3a660654d9cb55f7ac137a736539e227296b6-1920x1080.png)

Image 1: An overview of a Hierarchical Navigable Small World (HNSW) graph. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/composite-indexes/))

Despite its widespread adoption, the internal mechanics of HNSW remain a black box for many engineers. Its name alone—a mouthful of technical jargon—can be intimidating. This article demystifies HNSW, breaking down its theoretical foundations and practical implementation. We will explore how it works, why it is so effective, and how to tune it for optimal performance. Towards the end, we’ll look at how to implement HNSW using Faiss and find the parameter settings that give us the performance we need.

Having oriented ourselves on why HNSW matters, we will now examine the two core theoretical pillars it elegantly combines: probability skip lists and navigable small world graphs.

## Foundations of HNSW

Approximate Nearest Neighbor (ANN) search algorithms are broadly categorized into tree-based, hashing-based, and graph-based methods. HNSW falls into the last category, specifically as a *proximity graph*. In these graphs, nodes represent vectors, and edges connect vectors that are close to each other based on a chosen distance metric, like Euclidean or cosine distance.

HNSW represents a significant leap from simple proximity graphs by integrating two powerful concepts: the probabilistic structure of skip lists and the efficient routing of navigable small world graphs.

### Probability Skip List

A skip list is a probabilistic data structure that offers the best of both worlds: the fast search capabilities of a sorted array and the efficient insertion of a linked list [[1]](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf). It is built with multiple layers of linked lists. The bottom layer is a standard sorted list containing all elements. Each subsequent layer above it acts as an "express lane," containing a random subset of the elements from the layer below.![Image 2: A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for, or we reach the end, we drop to the next layer.](https://cdn.sanity.io/images/vr8gru94/production/9065d31e1b2e33ca697a56082f0ece7eff1c2d9b-1920x500.png)

Image 2: A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for, or we reach the end, we drop to the next layer. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

To search for an element, you start at the sparsest top layer and traverse forward. If you find an element greater than your target or reach the end of the list, you drop down to the next layer and continue the search. This process allows you to skip over large chunks of elements, achieving an average search complexity of O(log n) [[2]](https://en.wikipedia.org/wiki/Skip_list). HNSW inherits this layered, probabilistic structure to build its hierarchy, replacing simple linked lists with complex graphs.

### Navigable Small World Graphs

Navigable Small World (NSW) graphs are networks designed for efficient routing [[3]](https://www.iiis.org/CDs2011/CD2011IDI/ICTA_2011/PapersPdf/CT175ON.pdf), [[4]](https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059). They exhibit the "small-world" property, where most nodes can be reached from any other node in a small number of steps. They achieve this by combining two types of connections: short-range links to immediate neighbors and long-range links that act as highways across the graph. This structure enables a greedy search algorithm to navigate the graph with (poly-)logarithmic complexity.![Image 3: The search process through a NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector.](https://cdn.sanity.io/images/vr8gru94/production/5ca4fca27b2a9bf89b06748b39b7b6238fd4548c-1920x1080.png)

Image 3: The search process through a NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

Greedy routing in an NSW graph starts at a designated entry point. At each step, it evaluates the "friend list" of the current node and moves to the neighbor closest to the query vector. This process is often described in two phases. The search begins with a "zoom-out" phase, traversing long-range links between low-degree nodes to quickly cross the vector space. As it gets closer to the target region, it enters a "zoom-in" phase, navigating short-range links between high-degree nodes for fine-grained refinement [[5]](https://arxiv.org/abs/1507.06529). The search terminates when it reaches a local minimum—a node that is closer to the query than any of its neighbors.

However, this greedy approach has a critical weakness: it can get trapped in a local minimum far from the true nearest neighbor, especially if the graph has poor connectivity. This "early stopping" problem reduces recall. Performance can also degrade significantly in highly clustered or low-dimensional data, where the graph structure may not provide enough pathways to escape a local optimum [[10]](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf). Furthermore, the algorithm's effectiveness relies on the distance metric satisfying properties like the triangle inequality; non-metric similarity measures can violate these assumptions and lead to poor routing decisions [[11]](https://keyurramoliya.com/posts/Understading-HNSW-Hierarchical-Navigable-Small-World).

The straightforward solution is to increase the average degree (number of neighbors) of each node, but this comes at a cost. A higher degree improves recall by creating a more connected graph, but it also increases construction time, memory usage, and the number of distance calculations during search. This tradeoff is a central challenge in designing graph-based ANN indexes.

### Creating HNSW

The core innovation of HNSW is its hierarchical structure, which applies the layering principle of skip lists to NSW graphs [[6]](https://arxiv.org/abs/1603.09320). Instead of a single, flat graph, HNSW builds a multi-layered hierarchy of graphs. The top layers contain a sparse subset of vectors with only long-range links, acting as a fast entry point for search. Each subsequent layer becomes progressively denser, adding more vectors and shorter-range links.![Image 4: Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous.](https://cdn.sanity.io/images/vr8gru94/production/42d4a3ffc43e5dc2758ba8e5d2ef29d4c4d78254-1920x1040.png)

Image 4: Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

However, the necessity of this hierarchy has become a topic of debate. Recent research suggests that for high-dimensional data (d > 32), the hierarchy may not provide a significant benefit. The "Hub Highway Hypothesis" posits that in high-dimensional spaces, proximity graphs naturally form a well-connected "highway" of hub nodes that serve the same routing function as the hierarchical layers, making a flat graph just as efficient [[13]](https://arxiv.org/html/2412.01940v2). While the hierarchy is crucial for low-dimensional data, its value diminishes as dimensionality increases.

The search process in HNSW mirrors its structure. It begins at an entry point in the topmost layer, performing a greedy search to find the nearest neighbor in that sparse graph. This neighbor then serves as the entry point for the search in the next layer down. This process repeats, descending layer by layer, with each step refining the search with greater precision. The final search is performed on the bottom layer (layer 0), which contains all the vectors.![Image 5: The search process through the multi-layer structure of an HNSW graph.](https://cdn.sanity.io/images/vr8gru94/production/e63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png)

Image 5: The search process through the multi-layer structure of an HNSW graph. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

This hierarchical approach elegantly solves the main problem of NSW. By separating links by scale, it allows the search to start with a coarse, long-range "zoom-out" and progressively transition to a fine-grained "zoom-in," all while keeping the number of connections at each layer manageable. This exponential thinning of nodes layer-by-layer is what gives HNSW its logarithmic search complexity; the number of layers grows as O(log_M n), and since each layer requires a bounded number of steps, the total cost scales logarithmically [[12]](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture). The search is guaranteed to explore the densest graph at the final stage, preserving high recall.

With the layered foundations and search behavior clarified, we now turn to the practical iterative algorithm used to construct an HNSW graph one vector at a time.

## Graph Construction

The HNSW graph is built by inserting vectors one by one. The maximum number of layers, `L`, is not fixed but grows dynamically. When a new vector is inserted, it is assigned a random maximum layer level, `l`, based on an exponentially decaying probability distribution. This means most vectors will only exist in the bottom layers, while a few will be promoted to the higher, sparser layers [[6]](https://arxiv.org/abs/1603.09320).![Image 6: The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it.](https://cdn.sanity.io/images/vr8gru94/production/f105cb148aae44f77fa7e3df7b7f8c0256bcbec4-1920x980.png)

Image 6: The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

The probability distribution is controlled by a level multiplier parameter, `m_L`, which is typically set to `1/ln(M)`, where `M` is the number of neighbors for each vertex. This value is chosen to minimize the overlap of shared neighbors between layers, which is key to achieving optimal performance. A smaller `m_L` creates more separation but increases the average number of traversals during search [[6]](https://arxiv.org/abs/1603.09320).

The insertion process itself has two phases. First, the algorithm performs a greedy search starting from the top layer down to the assigned layer `l`. In this phase, the search parameter `ef` (which controls the size of the candidate list) is set to 1. The goal is simply to find the best entry point in each layer.

Once layer `l` is reached, the second phase begins. The algorithm performs another search, this time with a larger candidate list size defined by the `efConstruction` parameter. This richer search is repeated from layer `l` down to layer 0. The nearest neighbors found at each layer become candidates for the new vector's connections. From this candidate set, `M` neighbors are selected and linked to the new vector. The number of connections is capped by `M_max` for upper layers and `M_max0` for the base layer, which is typically `2*M` to ensure high connectivity at the densest level. These candidates also serve as the entry points for the search in the next layer down, ensuring the graph remains navigable.![Image 7: An explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0.](https://cdn.sanity.io/images/vr8gru94/production/dc5cb11ea197ceb4e1f18214066c8c51526b9af5-1920x1080.png)

Image 7: An explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

Equipped with a clear picture of how the hierarchical graph is built, we now examine the concrete Faiss implementation, index internals, parameter controls, and empirical tradeoffs observed on real workloads.

## Implementation of HNSW

We will implement HNSW using Facebook AI Similarity Search (Faiss), a popular library for efficient similarity search. Our goal is to test different construction and search parameters to see how they affect index performance.

1.  We start by initializing a basic HNSW index. We will use `IndexHNSWFlat`, which means the actual vectors are stored as is without compression.
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
    <faiss.impl.HNSW.HNSW; proxy of <Swig Object of type 'faiss::HNSW *' at 0x13753b870> >
    ```
2.  The parameter `M` sets the number of neighbors added to each vertex during insertion. However, the maximum number of connections, `M_max` and `M_max0`, are set automatically by Faiss's `set_default_probas` method, which is called during initialization. This method sets `M_max` to `M` and `M_max0` to `2 * M` [[7]](https://www.pinecone.io/learn/series/faiss/hnsw).

3.  Before we add any data, the index is empty. It has no layers and no entry point.
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
4.  Let's add some data. We will use the Sift1M dataset, which contains one million 128-dimensional vectors.
    ```python
    # For this example, assume 'xb' is our Sift1M dataset of 1M vectors
    # xb = ...
    
    index.add(xb)
    
    print(index.hnsw.max_level)
    levels = faiss.vector_to_array(index.hnsw.levels)
    print(np.bincount(levels))
    ```
    After adding the data, the index is built. The `max_level` is now set, and we can see the distribution of vectors across the different layers. The vast majority of vectors reside in layer 0.
    It outputs:
    ```text
    4
    array([990176,   9731,     85,      7,      1])
    ```
5.  The index also has a designated entry point, which is the starting node for all searches.
    ```python
    print(index.hnsw.entry_point)
    ```
    It outputs:
    ```text
    118295
    ```

### Graph Structure

The layered structure of the HNSW graph is determined probabilistically. When we initialize the index, the `set_default_probas` method is called. It takes `M` and a level multiplier `m_L` (called `levelMult` in Faiss), which defaults to `1 / log(M)`. This method calculates the probability of a new vector being inserted into each layer.

1.  We can replicate this logic in Python to understand how it works.
    ```python
    def set_default_probas(M: int, m_L: float):
        assign_probas = []
        level = 0
        while True:
            proba = np.exp(-level / m_L) * (1 - np.exp(-1 / m_L))
            if proba < 1e-9:
                break
            assign_probas.append(proba)
            level += 1
        return assign_probas
    
    assign_probas = set_default_probas(32, 1/np.log(32))
    print(assign_probas)
    ```
    The output shows the probability for each layer, with layer 0 having by far the highest probability.
    It outputs:
    ```text
    [0.9118398436248912, 0.0811601563751088, 0.006763351996551832, 0.0002366480034481309, 8.27961916377751e-06, 2.896791444589255e-07, 1.0134444535359142e-08]
    ```
2.  During insertion, the `random_level` function uses these probabilities to assign a max layer to each vector. It generates a random number and iterates through the cumulative probabilities to select a level.
    ```python
    def random_level(assign_probas, rng):
        f = rng.random()
        for i, proba in enumerate(assign_probas):
            f -= proba
            if f < 0:
                return i
        return len(assign_probas) - 1
    
    # Simulate 1M insertions
    rng = np.random.RandomState(42)
    levels_py = [random_level(assign_probas, rng) for _ in range(1000000)]
    print(np.bincount(levels_py))
    ```
    Simulating this process for 1 million vectors gives us a distribution that closely matches the one generated by Faiss.
    It outputs:
    ```text
    array([911931,  81119,   6717,    227,      6])
    ```
    ![Image 8: Distribution of vertices across layers in both the Faiss implementation (left) and the Python simulation (right).](https://cdn.sanity.io/images/vr8gru94/production/75658a08c25dabc1405f769c76fd2929c051853b-1920x930.png)

    Image 8: Distribution of vertices across layers in both the Faiss implementation (left) and the Python simulation (right). (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

    A small difference is that the Faiss implementation guarantees at least one vertex at the highest layer, which serves as the graph's entry point.

### HNSW Performance

The performance of an HNSW index is controlled by three key parameters: `M`, `efConstruction`, and `efSearch`. We can sweep through different values for these parameters on the Sift1M dataset to measure their impact on recall, search time, build time, and memory.

1.  The parameters `efConstruction` and `efSearch` control the size of the dynamic candidate list during index construction and search, respectively. `efConstruction` must be set before building the index, while `efSearch` can be adjusted any time before searching.
    ```python
    # M is set at initialization
    index = faiss.IndexHNSWFlat(d, M)
    
    # efConstruction must be set before adding data
    index.hnsw.efConstruction = 64
    index.add(xb)
    
    # efSearch can be set before searching
    index.hnsw.efSearch = 32
    # Assume xq is our query set
    # D, I = index.search(xq[:1000], k=1)
    ```
2.  Our experiments show that higher values for `M` and `efSearch` significantly improve recall. `efConstruction` also plays a vital role; a higher value can produce a higher-quality graph, which in turn allows you to achieve high recall with lower `M` and `efSearch` values.

    ![Image 9: Recall@1 performance for various M, efConstruction, and efSearch parameters.](https://cdn.sanity.io/images/vr8gru94/production/e8c281c3626226a76389fa344a71eb57f70cf879-1920x980.png)

    Image 9: Recall@1 performance for various M, efConstruction, and efSearch parameters. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

3.  Of course, higher recall comes at the cost of increased search time. There is a clear trade-off between speed and accuracy. For our batch of 1000 queries, search times ranged from around 1ms for 80% recall to over 50ms for near-perfect recall. It is often assumed that `efConstruction` has little impact on search time, but our tests show this is only true for very small query volumes. For larger batches, a higher `efConstruction` leads to a denser, more complex graph that takes longer to traverse.

    ![Image 10: Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is using a log scale.](https://cdn.sanity.io/images/vr8gru94/production/876bf66aba408959042888efe72c55db4d6b3b41-1920x980.png)

    Image 10: Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is using a log scale. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

    If your application involves single, low-latency queries, increasing `efConstruction` is a great way to boost recall with minimal impact on search time, especially at lower `M` values.

    ![Image 11: efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values.](https://cdn.sanity.io/images/vr8gru94/production/ef1a2edd25adb202c0a98a1f33a0e72d1295b554-1720x1080.png)

    Image 11: efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

4.  Finally, memory usage is a critical consideration. Of the three parameters, only `M` affects the size of the index. `efConstruction` and `efSearch` have no impact on memory. The memory footprint of HNSW can be substantial. For the Sift1M dataset, the index size starts at over 0.5GB for `M=2` and grows to nearly 5GB for `M=512`. This highlights the three-way tradeoff between recall, latency, and memory cost that engineers must navigate when deploying HNSW in production.

    ![Image 12: Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage.](https://cdn.sanity.io/images/vr8gru94/production/e04d23ccd76d8bdc568542bebe75a75e7d36a21e-1480x1050.png)

    Image 12: Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw))

### Improving Memory Usage and Search Speeds

When the memory consumption of `IndexHNSWFlat` becomes prohibitive, there are strategies to mitigate it. One common approach is to compress the stored vectors using Product Quantization (PQ). This significantly reduces memory usage, but it comes at the cost of lower recall and slightly slower search times due to the overhead of decoding vectors.

Another strategy is to combine HNSW with an IVF index. In this setup, HNSW is used as a coarse quantizer to quickly identify the most promising IVF cells to search, which can improve search speed, especially on very large datasets. A third approach, particularly for high-dimensional data, is to forgo the hierarchy altogether. Recent benchmarks show that a flat NSW graph can achieve performance nearly identical to HNSW with considerable memory savings, potentially reducing peak memory consumption by 18-39% on large datasets [[13]](https://arxiv.org/html/2412.01940v2).

These composite indexes and alternative structures offer more knobs to tune the performance-memory trade-off, a topic explored in more detail in our article on composite indexes [[8]](https://www.pinecone.io/learn/series/faiss/composite-indexes/).

## Conclusion

HNSW stands as a testament to elegant algorithmic design, combining the probabilistic layering of skip lists with the efficient routing of navigable small world graphs to create a state-of-the-art solution for approximate nearest neighbor search. Its ability to deliver high recall at logarithmic complexity has made it an indispensable tool for building modern, large-scale similarity search systems, with applications ranging from RAG to computational biology, where it has achieved up to a 560-fold acceleration over linear scans on massive datasets [[14]](https://www.biorxiv.org/content/10.64898/2026.06.02.729602v1.full-text).

Through this deep dive, we have unpacked the theoretical principles, the construction algorithm, and the practical implementation details in Faiss. We have seen how parameters like `M`, `efConstruction`, and `efSearch` are not just arbitrary knobs but powerful levers for navigating the critical trade-offs between recall, latency, and memory. Understanding these relationships is the key to moving beyond black-box usage and building truly optimized, production-ready AI applications.

## References

- [1] [Skip Lists: A Probabilistic Alternative to Balanced Trees](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)
- [2] [Skip list - Wikipedia](https://en.wikipedia.org/wiki/Skip_list)
- [3] [Approximate Nearest Neighbor Search Small World Approach](https://www.iiis.org/CDs2011/CD2011IDI/ICTA_2011/PapersPdf/CT175ON.pdf)
- [4] [Approximate nearest neighbor algorithm based on navigable small world graphs](https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059)
- [5] [Growing homophilic networks are natural navigable small worlds](https://arxiv.org/abs/1507.06529)
- [6] [Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs](https://arxiv.org/abs/1603.09320)
- [7] [HNSW](https://www.pinecone.io/learn/series/faiss/hnsw)
- [8] [Facebook AI and the Index Factory](https://www.pinecone.io/learn/series/faiss/composite-indexes/)
- [9] [Considerations for Optimizing Media Retrieval Systems Using Multimodal Embeddings](https://www.soeasie.com/blog/considerations-for-optimizing-media-retrieval-systems-using-multimodal-embeddings)
- [10] [Performance of proximity graph-based ANN algorithms on high dimensional and clustered data](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf)
- [11] [Understanding HNSW: Hierarchical Navigable Small World](https://keyurramoliya.com/posts/Understading-HNSW-Hierarchical-Navigable-Small-World)
- [12] [HNSW Index for Vector Search: Architecture and Performance](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture)
- [13] [Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”](https://arxiv.org/html/2412.01940v2)
- [14] [HNSW-MS: A High-Performance Mass Spectral Similarity Search Algorithm for Million-Scale Metabolomics](https://www.biorxiv.org/content/10.64898/2026.06.02.729602v1.full-text)