# HNSW Explained: The Foundation of Modern Vector Search![Hierarchical Navigable Small World (HNSW) graph overview](https://cdn.sanity.io/images/vr8gru94/production/d6e3a660654d9cb55f7ac137a736539e227296b6-1920x1080.png)

Image 1: An overview of a Hierarchical Navigable Small World (HNSW) graph. (Source [Dissecting Faiss: The HNSW Index [7]](https://www.pinecone.io/learn/series/faiss/hnsw/))

Hierarchical Navigable Small World (HNSW) has become the go-to algorithm for approximate nearest neighbor (ANN) search, powering countless production vector databases and retrieval systems. Its popularity stems from its ability to deliver state-of-the-art recall with sub-millisecond query speeds on massive vector collections, outperforming older methods like Inverted File (IVF) or Locality-Sensitive Hashing (LSH) [[1]](https://arxiv.org/abs/1603.09320).

Despite its widespread adoption, the internal mechanics of HNSW remain a black box for many engineers. This article demystifies HNSW, breaking down its theoretical foundations and practical implementation. We will also explore how to implement HNSW using [Faiss](https://www.pinecone.io/learn/series/faiss/) and tune its parameters for optimal performance. Let's begin by examining the two core concepts HNSW combines: probability skip lists and navigable small world graphs.

## Foundations of HNSW

HNSW belongs to the family of graph-based ANN algorithms, specifically proximity graphs, where edges connect vectors that are close to each other in the chosen metric space. While simple proximity graphs can be effective, HNSW introduces a sophisticated hierarchical structure that greatly improves search efficiency. This innovation is built on two fundamental data structures: the probability skip list and the navigable small world graph.

### Probability Skip List

A probability skip list is a data structure that combines the fast search capabilities of a sorted array with the efficient insertion of a linked list [[2]](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf). It achieves this by building multiple layers of linked lists. The bottom layer is a standard sorted list containing all elements. Each subsequent layer acts as an "express lane," containing a random subset of the elements from the layer below. The probability of an element from layer `i` also appearing in layer `i+1` is defined by a parameter `p` (commonly 0.5 or 0.25). On average, each element appears in `1/(1-p)` lists.

To search for an element, you start at the sparsest top layer and traverse forward. If you overshoot the target or reach the end of the list, you drop down to the next, denser layer and continue the search. This process repeats until you reach the bottom layer, where you perform a final, short linear scan. This layered approach reduces the search complexity to `O(log n)` on average, trading a small amount of extra storage for a large gain in search speed. HNSW inherits this core idea of a multi-layered structure to accelerate traversal.![A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for (or we reach the end), we drop to the next layer.](https://cdn.sanity.io/images/vr8gru94/production/9065d31e1b2e33ca697a56082f0ece7eff1c2d9b-1920x500.png)

Image 2: A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for (or we reach the end), we drop to the next layer. (Source [Similarity Search, Part 4: Hierarchical Navigable Small World (HNSW) [6]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37))

### Navigable Small World Graphs

Navigable Small World (NSW) graphs are networks where most connections are short-range, but a few long-range links exist to bridge distant parts of the graph [[3]](https://www.emergentmind.com/topics/navigable-small-world-nsw), [[4]](https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059). This structure enables a greedy routing algorithm to find short paths with (poly-)logarithmic complexity relative to the number of nodes.![The search process through a NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector.](https://cdn.sanity.io/images/vr8gru94/production/5ca4fca27b2a9bf89b06748b39b7b6238fd4548c-1920x1080.png)

Image 3: The search process through a NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector. (Source [Dissecting Faiss: The HNSW Index [7]](https://www.pinecone.io/learn/series/faiss/hnsw/))

The search process in an NSW graph is intuitive. It starts at a designated entry point and, at each step, moves to the neighbor in the current node's "friend list" that is closest to the query vector. This greedy traversal continues until it reaches a local minimum—a node that is closer to the query than any of its neighbors. This local minimum is then returned as the search result.

This search process has two distinct phases. The initial "zoom-out" phase involves traversing long-range links between low-degree nodes, allowing the search to quickly cross large distances in the vector space. These long-range links are often formed by the first elements inserted into the graph, acting as crucial "highways." As the search gets closer to the target region, it enters a "zoom-in" phase, where it moves between high-degree nodes with shorter-range links to refine its position [[5]](https://arxiv.org/abs/1507.06529).

A key challenge with this approach is the risk of getting trapped in a local minimum far from the true nearest neighbor, especially if the graph is not well-connected. This issue, known as early stopping, can reduce recall. To mitigate this, NSW graphs often increase the average number of connections (degree) per vertex. A higher degree provides more paths for the greedy search to explore, but it also creates a trade-off: it improves recall but increases construction time, memory usage, and the number of distance calculations per query. This balance between connectivity and cost is a central tuning axis for graph-based search algorithms.

### Creating HNSW

HNSW’s key innovation is applying the layered structure of a skip list to an NSW graph. Instead of a single graph, HNSW builds a hierarchy of graphs. The top layer contains only the longest-range links, connecting the most distant nodes. Each subsequent layer below it becomes progressively denser, with more nodes and shorter-range links. The bottom layer is a complete NSW graph containing all the vectors.![Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous.](https://cdn.sanity.io/images/vr8gru94/production/42d4a3ffc43e5dc2758ba8e5d2ef29d4c4d78254-1920x1040.png)

Image 4: Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous. (Source [Dissecting Faiss: The HNSW Index [7]](https://www.pinecone.io/learn/series/faiss/hnsw/))

The search process mirrors this hierarchical structure. It begins at a single, deterministic entry point in the top layer, performing a greedy search to find the local minimum. This node then serves as the entry point for the search in the layer below. This descent continues, with each layer refining the search, until the algorithm reaches the bottom layer. The search performed here yields the final set of nearest neighbor candidates [[1]](https://arxiv.org/abs/1603.09320).

This coarse-to-fine approach differs from a flat NSW search, which often relies on multiple random entry points to avoid getting trapped in local minima. In HNSW, the hierarchy itself provides the mechanism for course correction, making the search more efficient by eliminating the need for multiple random starts. While an NSW search starts with a "zoom-out" and ends with a "zoom-in," the process is implicit and depends on the graph's organic structure. HNSW makes this process explicit: the upper layers handle the "zoom-out" by traversing long-range links, and the lower layers handle the "zoom-in" with dense, short-range connections. This separation of links by their characteristic distance scale is what allows HNSW to break the polylogarithmic complexity of NSW and achieve true logarithmic scaling.![The search process through the multi-layer structure of an HNSW graph.](https://cdn.sanity.io/images/vr8gru94/production/e63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png)

Image 5: The search process through the multi-layer structure of an HNSW graph. (Source [Dissecting Faiss: The HNSW Index [7]](https://www.pinecone.io/learn/series/faiss/hnsw/))

With the layered foundations and search behavior clarified, we now turn to the practical iterative algorithm used to construct an HNSW graph one vector at a time.

## Graph Construction

The HNSW graph is built by inserting vectors one by one. The maximum number of layers `L` is a parameter of the index. When a new vector is inserted, it is assigned a random maximum layer `l` (where `l <= L`) based on an exponentially decaying probability distribution. This is calculated using the formula `l = floor(-ln(uniform(0,1)) * mL)`, ensuring that very few nodes are present in the top layers, while the bottom layer contains all nodes [[6]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).![The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it.](https://cdn.sanity.io/images/vr8gru94/production/f105cb148aae44f77fa7e3df7b7f8c0256bcbec4-1920x980.png)

Image 6: The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it. (Source [Dissecting Faiss: The HNSW Index [7]](https://www.pinecone.io/learn/series/faiss/hnsw/))

The probability distribution is controlled by a level multiplier parameter `m_L`, typically set to `1/ln(M)`, where `M` is the number of neighbors for each node. This value is chosen to minimize the overlap of neighbors across different layers, which is key to achieving optimal performance and logarithmic search complexity [[1]](https://arxiv.org/abs/1603.09320).

The insertion process itself occurs in two phases. In the first phase, the algorithm performs a fast greedy search (`ef=1`) from the top layer down to the randomly assigned layer `l`. This descent quickly finds the best entry point in the target layer.

Once layer `l` is reached, the second phase begins. From layer `l` down to the bottom layer (layer 0), the algorithm performs a more thorough search at each level using a construction parameter `efConstruction`. This parameter defines the size of a dynamic candidate list, allowing the algorithm to explore more neighbors. From these candidates, the `M` closest vectors are selected and bidirectionally linked to the new node. These same candidates also serve as the entry points for the search in the next layer down.

The number of connections per node is capped. A parameter `M_max` limits the connections for layers 1 and above, while `M_max0` (typically `2*M`) is used for the dense base layer. This prevents nodes from becoming overly connected, which would increase memory usage and search time [[7]](https://www.pinecone.io/learn/series/faiss/hnsw/).![Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0.](https://cdn.sanity.io/images/vr8gru94/production/dc5cb11ea197ceb4e1f18214066c8c51526b9af5-1920x1080.png)

Image 7: Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0. (Source [Dissecting Faiss: The HNSW Index [7]](https://www.pinecone.io/learn/series/faiss/hnsw/))

Equipped with a clear picture of how the hierarchical graph is built, we now examine the concrete Faiss implementation, index internals, parameter controls, and empirical tradeoffs observed on real workloads.

## Implementation of HNSW

We will implement HNSW using the Facebook AI Similarity Search (Faiss) library and test different construction and search parameters to see how these affect index performance [[7]](https://www.pinecone.io/learn/series/faiss/hnsw/).

1.  We initialize the HNSW index using `IndexHNSWFlat`. The constructor takes the vector dimension `d` and the number of neighbors `M`.
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
    <faiss.swigfaiss_avx2.HNSW; proxy of <Swig Object of type 'faiss::HNSW *' at 0x7f833c8b5c90> >
    ```

2.  The `M` parameter sets the number of neighbors added during insertion. Faiss automatically calls a method `set_default_probas` at initialization, which sets the maximum number of connections `M_max` to `M` and the maximum for the base layer `M_max0` to `2*M` [[7]](https://www.pinecone.io/learn/series/faiss/hnsw/).

3.  Before we add any data, the index has no layers.
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

4.  After building the index by adding our data (`xb`), the layers are populated. We can inspect the maximum level and the distribution of vectors across each layer.
    ```python
    # xb is a numpy array of our dataset vectors
    # index.add(xb)
    
    print(index.hnsw.max_level)
    
    levels = faiss.vector_to_array(index.hnsw.levels)
    print(np.bincount(levels))
    ```
    It outputs:
    ```text
    4
    array([961921,  37123,   1187,     39,      5,      1])
    ```
    This shows our index has 5 layers (0 to 4), with the vast majority of vectors residing in the bottom layer.

5.  The index also has a single entry point, which is the starting node for all searches.
    ```python
    print(index.hnsw.entry_point)
    ```
    It outputs:
    ```text
    118295
    ```

### Graph Structure

The layer assignment in Faiss is probabilistic. When the index is initialized, the `set_default_probas` method is called with `M` and a level multiplier `m_L` equal to `1 / log(M)`. This method calculates the probability for a new vector to be inserted into each layer [[7]](https://www.pinecone.io/learn/series/faiss/hnsw/).

1.  We can replicate this logic in Python to understand how the probabilities are determined.
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
            nn += (2 * M) if level == 0 else M
            cum_nneighbor_per_level.append(nn)
            level += 1
        return assign_probas, cum_nneighbor_per_level
    ```

2.  Calling this function with `M=32` shows the exponentially decaying probabilities for higher layers. The `cum_nneighbor_per_level` list shows the cumulative number of neighbor links stored for an element inserted at a given level.
    ```python
    assign_probas, cum_nneighbor_per_level = set_default_probas(32, 1/np.log(32))
    
    print(assign_probas)
    print(cum_nneighbor_per_level)
    ```
    It outputs:
    ```text
    [0.9118395804153673, 0.0811690084013442, 0.006322479007283431, 0.0004926639535313327, 3.83901924737202e-05, 2.991879038304934e-06, 2.331580972412674e-07, 1.817109591353123e-08, 1.416181958614275e-09]
    [64, 96, 128, 160, 192, 224, 256, 288, 320]
    ```

3.  The `random_level` function uses these probabilities to assign a layer to a new vector. It generates a random number and finds the highest layer whose cumulative probability is not exceeded.
    ```python
    def random_level(assign_probas):
        f = np.random.rand()
        for i, proba in enumerate(assign_probas):
            f -= proba
            if f < 0:
                return i
        return len(assign_probas) - 1
    ```

4.  Simulating this process for 1,000,000 vectors confirms that our Python implementation closely matches the actual layer distribution created by Faiss.
    ```python
    # levels = [random_level(assign_probas) for i in range(1000000)]
    # print(np.bincount(levels))
    ```
    It outputs:
    ```text
    array([911985,  81139,   6300,    492,     37,      2])
    ```![Distribution of vertices across layers in both the Faiss implementation (left) and the Python implementation (right).](https://cdn.sanity.io/images/vr8gru94/production/75658a08c25dabc1405f769c76fd2929c051853b-1920x930.png)

Image 8: Distribution of vertices across layers in both the Faiss implementation (left) and the Python implementation (right). (Source [Dissecting Faiss: The HNSW Index [7]](https://www.pinecone.io/learn/series/faiss/hnsw/))

A key detail is that the Faiss implementation ensures at least one vertex is present at the highest layer, guaranteeing a valid entry point for the graph search.

### HNSW Performance

To understand the performance trade-offs, we can run an empirical parameter sweep on the Sift1M dataset, varying `M`, `efSearch`, and `efConstruction` while measuring recall, search time, and memory usage.

1.  The parameters `efConstruction` and `efSearch` control the depth of the search during index construction and querying, respectively. `efConstruction` must be set before adding vectors, while `efSearch` can be adjusted anytime before searching.
    ```python
    # M is set at initialization
    index = faiss.IndexHNSWFlat(d, M)
    
    # efConstruction must be set before adding vectors
    index.hnsw.efConstruction = efConstruction
    index.add(xb)  # build the index
    
    # efSearch can be set anytime before searching
    index.hnsw.efSearch = efSearch
    index.search(xq[:1000], k=1)
    ```![Recall@1 performance for various M, efConstruction, and efSearch parameters.](https://cdn.sanity.io/images/vr8gru94/production/e8c281c3626226a76389fa344a71eb57f70cf879-1920x980.png)

Image 9: Recall@1 performance for various M, efConstruction, and efSearch parameters. (Source [Dissecting Faiss: The HNSW Index [7]](https://www.pinecone.io/learn/series/faiss/hnsw/))

The results show that higher values for `M` (number of neighbors) and `efSearch` (search-time exploration) improve recall. A sufficiently high `efConstruction` is also necessary for building a high-quality graph. Increasing `efConstruction` can often compensate for lower `M` and `efSearch` values, allowing you to achieve high recall with a smaller, faster index [[7]](https://www.pinecone.io/learn/series/faiss/hnsw/). For instance, with `M=16`, increasing `efConstruction` from 40 to 128 provides a noticeable recall boost across all `efSearch` values. This demonstrates that a better-constructed graph leads to more accurate searches. We also see diminishing returns; the jump from `M=32` to `M=64` yields a smaller recall improvement than the jump from `M=16` to `M=32`, especially at high `efSearch`.![Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is using a log scale.](https://cdn.sanity.io/images/vr8gru94/production/876bf66aba408959042888efe72c55db4d6b3b41-1920x980.png)

Image 10: Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is using a log scale. (Source [Dissecting Faiss: The HNSW Index [7]](https://www.pinecone.io/learn/series/faiss/hnsw/))

There is a clear trade-off between recall and search time. The log scale on the y-axis highlights the exponential increase in search time as parameters are raised. For a batch of 1000 queries, search times can range from around 1ms for 80% recall to over 50ms for near-perfect recall. It is often assumed that `efConstruction` has little impact on search time, but this holds true only for very small query volumes. For larger batches, a higher `efConstruction` leads to a denser, more complex graph that takes longer to traverse because more nodes are visited on average per query.

However, when the query volume is low (e.g., a single query), increasing `efConstruction` is a great way to boost recall with minimal impact on latency, especially at lower `M` values. This confirms that for real-time applications with single-vector queries, `efConstruction` can be increased to improve graph quality and recall without a significant latency penalty.![efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values.](https://cdn.sanity.io/images/vr8gru94/production/ef1a2edd25adb202c0a98a1f33a0e72d1295b554-1720x1080.png)

Image 11: efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values. (Source [Dissecting Faiss: The HNSW Index [7]](https://www.pinecone.io/learn/series/faiss/hnsw/))

Finally, memory usage is solely determined by the `M` parameter. `efConstruction` and `efSearch` have no effect on the final index size. The memory footprint can be substantial, exceeding 0.5GB for `M=2` and approaching 5GB for `M=512` on the Sift1M dataset. The linear growth is clear. For applications with tight memory constraints, `M` is the most important parameter to tune. An index with `M=512` requires nearly 10x the memory of one with `M=32`, a cost that must be justified by a corresponding improvement in performance. This highlights the important three-way trade-off between recall, latency, and memory that engineers must balance based on their application's requirements and infrastructure constraints [[7]](https://www.pinecone.io/learn/series/faiss/hnsw/).![Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage.](https://cdn.sanity.io/images/vr8gru94/production/e04d23ccd76d8bdc568542bebe75a75e7d36a21e-1480x1050.png)

Image 12: Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage. (Source [Dissecting Faiss: The HNSW Index [7]](https://www.pinecone.io/learn/series/faiss/hnsw/))

### Improving Memory Usage and Search Speeds

When the memory consumption of a standard HNSW index becomes prohibitive, two common strategies can be employed. First, you can compress the stored vectors using Product Quantization (PQ), which reduces memory usage at the cost of lower recall and slightly increased search times. Second, you can wrap the HNSW index within an IVF component. This creates a composite index where HNSW is used to quickly identify the most promising IVF cells to search, improving search speed on very large datasets. These composite index strategies are a topic for another day, but you can learn more about them in our article on [composite indexes](https://www.pinecone.io/learn/series/faiss/composite-indexes/).

## References

- [1] Y. A. Malkov, D. A. Yashunin, [Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs](https://arxiv.org/abs/1603.09320)
- [2] W. Pugh, [Skip lists: a probabilistic alternative to balanced trees](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)
- [3] [Navigable Small World Graphs](https://www.emergentmind.com/topics/navigable-small-world-nsw)
- [4] Y. Malkov, A. Ponomarenko, A. Logvinov, V. Krylov, [Approximate nearest neighbor algorithm based on navigable small world graphs](https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059)
- [5] Y. A. Malkov, A. Ponomarenko, [Growing homophilic networks are natural navigable small worlds](https://arxiv.org/abs/1507.06529)
- [6] A. Grigorov, [Similarity Search, Part 4: Hierarchical Navigable Small World (HNSW)](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37)
- [7] J. Briggs, [Dissecting Faiss: The HNSW Index](https://www.pinecone.io/learn/series/faiss/hnsw/)
</article>