# A Deep Dive into HNSW: The Unbeatable Algorithm for Vector Search

Hierarchical Navigable Small World (HNSW) is a powerful vector search algorithm, delivering state-of-the-art recall with sub-millisecond query speeds on massive datasets. This performance has made it the engine behind countless production RAG and semantic search applications, and the default index in most vector databases [[41]](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture). While methods like Inverted File (IVF) indexes or Locality-Sensitive Hashing (LSH) have their place, HNSW often provides a superior trade-off between speed and accuracy [[19]](https://www.vldb.org/pvldb/vol15/p850-doshi.pdf).![Hierarchical Navigable Small World (HNSW) graph overview](https://cdn.sanity.io/images/vr8gru94/production/d6e3a660654d9cb55f7ac137a736539e227296b6-1920x1080.png)
Image 1: An overview of the Hierarchical Navigable Small World (HNSW) graph structure.

Despite its widespread adoption in vector databases, the internal mechanics of HNSW can be difficult to grasp. This article demystifies the algorithm, breaking down its theoretical foundations and construction process. Towards the end, we’ll look at how to implement HNSW using Faiss and find the parameter settings that give us the performance we need [[15]](https://www.pinecone.io/learn/series/faiss/hnsw).

To understand HNSW, we first need to examine the two core pillars it combines: probabilistic skip lists and navigable small world graphs.

## Foundations of HNSW

HNSW belongs to the category of proximity-based graph algorithms for Approximate Nearest Neighbor (ANN) search. In these graphs, nodes represent vectors, and edges connect vectors that are close to each other in the given distance metric (like Euclidean or cosine distance). HNSW takes this a step further by introducing a hierarchy, drawing inspiration from two powerful data structures.

### Probability Skip List

A skip list is a probabilistic data structure that allows for fast search and insertion, achieving an average time complexity of O(log n) [[1]](https://www.geeksforgeeks.org/dsa/skip-list). It improves upon a standard sorted linked list by adding multiple layers of "express lanes." The bottom layer is a complete, sorted linked list containing all elements. Each subsequent layer above it contains a sparser subsequence of the elements from the layer below.

Searching a skip list starts at the highest, most sparse layer. The algorithm traverses forward until it finds an element greater than the target or reaches the end of the list. At that point, it drops down to the next layer and resumes the search from the previous position. This process continues until the target element is found in the bottom layer. This layered approach allows the search to "skip" over large portions of the list, making it significantly faster than a linear scan [[2]](https://en.wikipedia.org/wiki/Skip_list).![A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for (or we reach the end), we drop to the next layer.](https://cdn.sanity.io/images/vr8gru94/production/9065d31e1b2e33ca697a56082f0ece7eff1c2d9b-1920x500.png)
Image 2: A probability skip list structure. The search starts on the top layer and descends when it overshoots the target key.

The key idea HNSW borrows from skip lists is this multi-layered structure. Instead of linked lists, HNSW uses graphs at each layer, but the principle of starting coarse and getting finer remains the same.

### Navigable Small World Graphs

A Navigable Small World (NSW) graph is a network that enables efficient decentralized greedy routing [[4]](https://www.emergentmind.com/topics/navigable-small-world-nsw). A small-world network is defined by two key properties: a high clustering coefficient, meaning friends of a node are likely to be friends with each other, and a low average path length, meaning any two nodes can be connected by a short chain of connections [[42]](https://en.wikipedia.org/wiki/Small-world_network). These networks also tend to have an over-abundance of *hubs*—nodes with a very high number of connections that mediate the short paths between other nodes [[42]](https://en.wikipedia.org/wiki/Small-world_network). This is achieved by combining short-range links, which connect a node to its immediate neighbors, and long-range links, which act as bridges between distant parts of the graph.![The search process through a NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector.](https://cdn.sanity.io/images/vr8gru94/production/5ca4fca27b2a9bf89b06748b39b7b6238fd4548c-1920x1080.png)
Image 3: The search process through an NSW graph. Starting at an entry point, the algorithm greedily moves to the neighbor closest to the query vector.

Searching an NSW graph uses a greedy routing algorithm. The search begins at a predefined entry point. At each step, the algorithm evaluates the distances from the query vector to all neighbors (its "friend list") of the current node. It then moves to the neighbor that is closest to the query. This process repeats until the algorithm reaches a local minimum—a node where no neighbor is closer to the query than the node itself [[5]](https://www.pinecone.io/learn/series/faiss/hnsw).

This search process has two distinct phases. It begins with a "zoom-out" phase, where the algorithm traverses long-range links between low-degree vertices to quickly navigate to the general region of the target. As it gets closer, it enters a "zoom-in" phase, where it moves between higher-degree vertices with shorter-range links to refine the search [[7]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).

The main weakness of this approach is the risk of getting trapped in a local minimum far from the true nearest neighbor. This "early stopping" problem is more likely to occur if the graph's connectivity is poor. To mitigate this, one can increase the average degree of the vertices (the number of friends each node has). However, this increases both the complexity of building the graph and the number of distance calculations required at each step of the search, creating a fundamental trade-off between recall and performance.

### Creating HNSW

The key innovation of HNSW is applying the hierarchical structure of a skip list to an NSW graph. This creates a multi-layered graph where each layer is a progressively denser proximity graph. The top layer contains only the longest-range links, acting as express "highways" for quick navigation, connecting a sparse subset of nodes [[43]](https://www.tigerdata.com/blog/vector-database-basics-hnsw). Each layer below adds more nodes and shorter-range links, with the bottom layer (layer 0) containing all nodes and the densest connections.![Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous.](https://cdn.sanity.io/images/vr8gru94/production/42d4a3ffc43e5dc2758ba8e5d2ef29d4c4d78254-1920x1040.png)
Image 4: The layered graph structure of HNSW. Higher layers have fewer nodes and longer links, while lower layers are denser.

The search process in HNSW elegantly combines the strengths of both its predecessors. It begins at an entry point in the highest layer. The algorithm performs a greedy search on this layer, just as in an NSW graph, until it finds a local minimum. This node then serves as the entry point for the search on the layer below. This descent continues layer by layer, with the search becoming progressively more granular. The final greedy search on the bottom layer yields the approximate nearest neighbors [[9]](https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf).![The search process through the multi-layer structure of an HNSW graph.](https://cdn.sanity.io/images/vr8gru94/production/e63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png)
Image 5: The search process in an HNSW graph starts at the top layer and descends, using the local minimum from one layer as the entry point for the next.

This hierarchical approach provides a significant performance boost over a flat NSW graph. By starting with long-range links, the algorithm quickly navigates to the correct region of the vector space. The subsequent searches in denser, lower layers refine this position without the high computational cost of traversing a massive, dense graph from a random starting point. This separation of links by scale allows HNSW to achieve logarithmic search complexity [[10]](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf).

However, recent research has questioned whether this hierarchy is necessary for modern, high-dimensional datasets. The "curse of dimensionality" can lead to a phenomenon called *hubness*, where a small subset of vectors act as "hubs" that are nearest neighbors to a disproportionately large number of other points [[44]](https://arxiv.org/html/2412.01940v2). These hubs can naturally form a well-connected "highway" through the graph, providing the same fast-routing function as the explicit upper layers. In such cases, a flat NSW graph may perform just as well as HNSW but with lower memory overhead [[24]](https://arxiv.org/html/2412.01940v2).

With the layered foundations and search behavior clarified, we now turn to the practical iterative algorithm used to construct an HNSW graph one vector at a time.

## Graph Construction

The HNSW graph is built by inserting vectors one by one. This incremental construction is a significant advantage for dynamic applications, as new vectors can be added to an existing index without rebuilding the entire structure [[45]](https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605). When a new vector is added, it is assigned a random maximum layer height, `l`, drawn from an exponentially decaying probability distribution. This means most vectors will only exist in the bottom layers, while a few will be present in the higher, sparser layers [[24]](https://arxiv.org/html/2412.01940v2). The vector is then inserted into the graph at every layer from `l` down to 0.![The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it.](https://cdn.sanity.io/images/vr8gru94/production/f105cb148aae44f77fa7e3df7b7f8c0256bcbec4-1920x980.png)
Image 6: Each new vector is assigned a random maximum layer and is present in all layers up to that maximum.

The probability distribution is controlled by a level multiplier parameter, `m_L`. The creators of HNSW found that performance is best when the overlap of shared neighbors between layers is minimized. A smaller `m_L` pushes more vectors to lower layers, reducing overlap but increasing the number of traversals needed during a search. An optimal balance is typically found with `m_L` set to `1/ln(M)`, where `M` is the number of neighbors connected to each new node [[37]](https://www.pinecone.io/learn/series/faiss/hnsw).

The insertion process for a new vector involves two phases [[29]](https://www.pinecone.io/learn/series/faiss/hnsw).
1.  **Finding entry points:** Starting from the top layer of the graph, the algorithm performs a simple greedy search (`ef=1`) to find the single nearest neighbor to the new vector. This neighbor becomes the entry point for the search in the layer below. This process repeats until the algorithm reaches the randomly assigned insertion layer `l`.
2.  **Connecting to neighbors:** From layer `l` downwards, the search becomes more thorough. The algorithm uses a parameter `efConstruction` to define the size of a dynamic candidate list for neighbors. At each layer, it finds the `efConstruction` nearest neighbors. From this candidate set, `M` neighbors are selected and bidirectionally linked to the new vector. These `efConstruction` candidates also serve as the entry points for the search in the next layer down.

The number of links per vertex is capped. For all layers above the base layer, a vertex can have at most `M_max` connections. For the base layer (layer 0), this limit is typically doubled to `M_max0` to ensure high connectivity for the final, most detailed search phase [[40]](https://www.pinecone.io/learn/series/faiss/hnsw).![Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0.](https://cdn.sanity.io/images/vr8gru94/production/dc5cb11ea197ceb4e1f18214066c8c51526b9af5-1920x1080.png)
Image 7: A vertex's connections are capped by `M_max` on upper layers and `M_max0` on the base layer.

This construction process mirrors the search procedure, ensuring the graph remains navigable as it grows. By using a richer search during construction (`efConstruction` > 1), the algorithm builds a higher-quality graph with more optimal connections, which in turn improves search recall later on.

Equipped with a clear picture of how the hierarchical graph is built, we now examine the concrete Faiss implementation, index internals, parameter controls, and empirical tradeoffs observed on real workloads.

## Implementation of HNSW

We will implement HNSW using the Facebook AI Similarity Search (Faiss) library and test how different construction and search parameters affect index performance.

1.  First, we initialize a basic HNSW index. We will use `IndexHNSWFlat`, which means the actual vectors are stored in the index without any compression.
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
    <faiss.impl.HNSW.HNSW; proxy of <Swig Object of type 'faiss::HNSW *' at 0x1404e4c30> >
    ```
2.  When we initialize the index, we set `M`, the number of neighbors added to each vertex on insertion. However, the `M_max` and `M_max0` parameters, which cap the number of connections, are set automatically by Faiss's internal `set_default_probas` method. This method is called at initialization and sets `M_max` to `M` and `M_max0` to `2 * M` [[33]](https://www.youtube.com/watch?v=QvKMwLjdK-s).
3.  Before we build the index by adding data, the HNSW structure is empty. The maximum level is not set, and there is no distribution of vectors across layers.
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
4.  Now, let's build the index using the Sift1M dataset, which contains 1 million 128-dimensional vectors. After adding the data, the index is populated.
    ```python
    # Sift1M data can be downloaded from https://gist.github.com/mdouze/04646174a7f3e4b47644
    # xb contains the 1M database vectors, xq contains 10k query vectors
    
    index.add(xb)
    
    print(f"Maximum layer: {index.hnsw.max_level}")
    
    levels = faiss.vector_to_array(index.hnsw.levels)
    print(f"Distribution of levels: {np.bincount(levels)}")
    ```
    It outputs:
    ```text
    Maximum layer: 4
    Distribution of levels: [917591  75971   6139    294      5]
    ```
    We can see that the index now has a maximum layer of 4, and the vast majority of vectors reside in layer 0, with exponentially fewer vectors in higher layers.
5.  The index also has a designated entry point, which is the starting node for all searches.
    ```python
    print(f"Entry point: {index.hnsw.entry_point}")
    ```
    It outputs:
    ```text
    Entry point: 118295
    ```

### Graph Structure

The logic for assigning layers in Faiss is handled by the `set_default_probas` method. When we initialize the index, this method is called with `M` and a `levelMult` parameter (our `m_L`), which defaults to `1 / log(M)` [[31]](https://www.pinecone.io/learn/series/faiss/hnsw).

1.  We can replicate this logic in Python to understand how the layer assignment probabilities are calculated. The function creates new levels until the probability of assigning a vector to that level drops below a small threshold.
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
            nn += 2 * M if level == 0 else M
            cum_nneighbor_per_level.append(nn)
            level += 1
        return assign_probas, cum_nneighbor_per_level
    ```
2.  Running this with our parameters (`M=32`) shows the probability distribution for layer assignment. The probability of being assigned to layer 0 is very high (over 70%), and it drops off quickly for higher layers.
    ```python
    assign_probas, _ = set_default_probas(32, 1/np.log(32))
    print(assign_probas)
    ```
    It outputs:
    ```text
    [0.7126167634625149, 0.20450333890412434, 0.0587024349340059, 0.01684784437207439, 0.004836018318182243, 0.0013881452427814392, 0.0003985147551061809, 0.00011440625341258673, 3.284245233158098e-05, 9.427771746452271e-06, 2.705886659771144e-06, 7.76612450337854e-07, 2.228965825310659e-07, 6.397554904221764e-08, 1.836066228224097e-08, 5.269098197779775e-09, 1.512411333390013e-09]
    ```
3.  The `random_level` function uses these probabilities to assign a layer to each new vector. It generates a random number and iterates through the cumulative probabilities to select a layer.
    ```python
    def random_level(assign_probas):
        rng = np.random.default_rng()
        f = rng.random()
        for i, proba in enumerate(assign_probas):
            f -= proba
            if f < 0:
                return i
        return len(assign_probas) - 1
    ```
4.  We can simulate the insertion of 1 million vectors to verify that our Python implementation closely matches the actual distribution produced by Faiss.
    ```python
    # run simulation
    rng = np.random.default_rng(12345)
    lvls = [random_level(assign_probas) for _ in range(1_000_000)]
    
    # plot distributions
    print(np.bincount(lvls))
    ```
    It outputs:
    ```text
    [917480  76092   6111    295      5      0      0      0      0      0      0
          0      0      0      0      0     17]
    ```
    The simulated distribution is nearly identical to the one from our actual Faiss index, confirming our understanding of the layer assignment mechanism. Faiss also ensures that at least one vertex is placed at the highest level to serve as the graph's entry point.![Distribution of vertices across layers in both the Faiss implementation (left) and the Python implementation (right).](https://cdn.sanity.io/images/vr8gru94/production/75658a08c25dabc1405f769c76fd2929c051853b-1920x930.png)
Image 8: The distribution of vertices across layers is nearly identical between the actual Faiss index and our Python simulation.

### HNSW Performance

Now, let's analyze the performance trade-offs by tuning the core HNSW parameters: `M`, `efConstruction`, and `efSearch`.
*   `M`: The number of neighbors connected to each new vertex during construction. Affects graph density, memory usage, and recall.
*   `efConstruction`: The size of the candidate list during graph construction. A higher value leads to a better-quality graph and higher recall but increases build time.
*   `efSearch`: The size of the candidate list during search. A higher value increases recall at the cost of search latency.

1.  We set these parameters on the Faiss index object. `efConstruction` must be set before building the index with `index.add()`, while `efSearch` can be adjusted any time before calling `index.search()`.
    ```python
    # re-initialize index
    index = faiss.IndexHNSWFlat(d, M)
    
    # set efConstruction before building
    index.hnsw.efConstruction = efConstruction
    index.add(xb)  # build the index
    
    # set efSearch before searching
    index.hnsw.efSearch = efSearch
    # now we can search
    index.search(xq[:1000], k=1)
    ```
2.  Our experiments on Sift1M show that higher `M` and `efSearch` values significantly improve recall. A reasonably high `efConstruction` is also necessary, as it can help achieve higher recall even with lower `M` and `efSearch` values [[20]](https://www.pinecone.io/learn/series/faiss/hnsw).

    ![Recall@1 performance for various M, efConstruction, and efSearch parameters.](https://cdn.sanity.io/images/vr8gru94/production/e8c281c3626226a76389fa344a71eb57f70cf879-1920x980.png)
    Image 9: Recall@1 performance for various `M`, `efConstruction`, and `efSearch` parameters on the Sift1M dataset.
3.  As expected, increasing these parameters also increases search time. The chart below shows search time for 1000 queries on a log scale. There is a clear trade-off: achieving near-perfect recall can take 50 times longer than achieving 80% recall. It is often assumed that `efConstruction` does not affect search time, but our tests with a batch of 1000 queries show this is not the case. The effect is simply less pronounced than that of `M` or `efSearch` [[16]](https://www.youtube.com/watch?v=QvKMwLjdK-s).

    ![Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is using a log scale.](https://cdn.sanity.io/images/vr8gru94/production/876bf66aba408959042888efe72c55db4d6b3b41-1920x980.png)
    Image 10: Search time in µs for 1000 queries across different parameter settings. Note the logarithmic y-axis.
4.  However, when the query volume is low (e.g., a single query), the impact of `efConstruction` on search time becomes negligible, especially at lower `M` values. This makes `efConstruction` an excellent parameter to increase when you need a boost in recall without a significant latency penalty for single-shot queries.

    ![efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values.](https://cdn.sanity.io/images/vr8gru94/production/ef1a2edd25adb202c0a98a1f33a0e72d1295b554-1720x1080.png)
    Image 11: For a single query, increasing `efConstruction` has little impact on search time, especially with smaller `M` values.

It is important to note that HNSW's performance can degrade in very high-dimensional spaces (e.g., >1024 dimensions). As dimensionality increases, the distance between any two points becomes less meaningful due to the "curse of dimensionality." This can trap the greedy search algorithm in local minima, reducing recall in ways that simply increasing `efSearch` cannot fix [[46]](https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605)[[47]](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture). Another performance consideration is hardware. While GPUs can accelerate vector search, HNSW's sequential, increment-based construction process is not inherently well-suited for the massive parallelization of GPUs, posing challenges for index building at scale [[48]](https://arxiv.org/html/2508.08744v2).
5.  Finally, memory usage is a critical consideration. Of the three parameters, only `M` affects the index size. `efConstruction` and `efSearch` are search-time parameters and do not impact memory. The memory footprint grows linearly with `M`. For the Sift1M dataset, the index size starts at over 0.5 GB for a small `M=2` and grows to nearly 5 GB for `M=512`. This highlights the three-way trade-off between recall, latency, and memory, which has direct implications for infrastructure costs [[23]](https://www.youtube.com/watch?v=QvKMwLjdK-s).

    ![Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage.](https://cdn.sanity.io/images/vr8gru94/production/e04d23ccd76d8bdc568542bebe75a75e7d36a21e-1480x1050.png)
    Image 12: Memory usage increases with `M`. `efSearch` and `efConstruction` have no effect on index size.

### Improving Memory Usage and Search Speeds

The high memory consumption of HNSW can be a significant challenge in production. If memory becomes a bottleneck, there are two primary strategies to mitigate it.

First, you can compress the stored vectors using techniques like Product Quantization (PQ). This dramatically reduces the memory footprint, but it comes at the cost of lower recall. Applying quantization to HNSW is also less straightforward than with IVF indexes. HNSW's random memory access patterns are incompatible with optimizations like vector packing that make PQ fast, leading to less effective compression trade-offs [[49]](https://blog.vectorchord.ai/why-hnsw-is-not-the-answer). Furthermore, HNSW's memory usage can grow over time in production systems due to its complex process for managing deletions, which often involves marking nodes as deleted rather than immediately reclaiming space [[41]](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture)[[50]](https://gsitechnology.com/not-all-hnsw-indices-are-made-equally).

Second, you can wrap the HNSW index with an Inverted File (IVF) component. In this setup, HNSW is used as a coarse quantizer to quickly identify a small subset of database partitions (Voronoi cells) to search, rather than searching the entire dataset. This can significantly improve search speed, especially for very large datasets.

These advanced techniques for building composite indexes are covered in more detail in our article on [composite indexes in Faiss](https://www.pinecone.io/learn/series/faiss/composite-indexes/).

## Conclusion

HNSW is a sophisticated and highly effective algorithm for approximate nearest neighbor search. By combining the layered structure of skip lists with the greedy routing of navigable small world graphs, it achieves state-of-the-art performance in recall and latency. However, this power comes with complexity. Mastering HNSW requires a deep understanding of its construction process and the intricate trade-offs between its key parameters—`M`, `efConstruction`, and `efSearch`. As we have seen, tuning these parameters allows you to navigate the critical balance between accuracy, query speed, and memory consumption. This enables you to build powerful and efficient vector search systems, with ongoing research exploring adaptive methods like Dynamic HNSW to tune these parameters automatically based on data characteristics [[51]](https://ieeexplore.ieee.org/document/10992903).

## References

- [1] https://www.geeksforgeeks.org/dsa/skip-list
- [2] https://en.wikipedia.org/wiki/Skip_list
- [4] https://www.emergentmind.com/topics/navigable-small-world-nsw
- [5] https://www.pinecone.io/learn/series/faiss/hnsw
- [7] https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37
- [9] https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf
- [10] https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf
- [15] https://www.pinecone.io/learn/series/faiss/hnsw
- [16] https://www.youtube.com/watch?v=QvKMwLjdK-s
- [19] https://www.vldb.org/pvldb/vol15/p850-doshi.pdf
- [20] https://www.pinecone.io/learn/series/faiss/hnsw
- [23] https://www.youtube.com/watch?v=QvKMwLjdK-s
- [24] https://arxiv.org/html/2412.01940v2
- [29] https://www.pinecone.io/learn/series/faiss/hnsw
- [31] https://www.pinecone.io/learn/series/faiss/hnsw
- [33] https://www.youtube.com/watch?v=QvKMwLjdK-s
- [37] https://www.pinecone.io/learn/series/faiss/hnsw
- [40] https://www.pinecone.io/learn/series/faiss/hnsw
- [41] https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture
- [42] https://en.wikipedia.org/wiki/Small-world_network
- [43] https://www.tigerdata.com/blog/vector-database-basics-hnsw
- [44] https://arxiv.org/html/2412.01940v2
- [45] https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605
- [46] https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605
- [47] https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture
- [48] https://arxiv.org/html/2508.08744v2
- [49] https://blog.vectorchord.ai/why-hnsw-is-not-the-answer
- [50] https://gsitechnology.com/not-all-hnsw-indices-are-made-equally
- [51] https://ieeexplore.ieee.org/document/10992903