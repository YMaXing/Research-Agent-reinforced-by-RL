# A Deep Dive into HNSW: The Unsung Hero of Vector Search![Hierarchical Navigable Small World (HNSW) graph overview](https://cdn.sanity.io/images/vr8gru94/production/d6e3a660654d9cb55f7ac137a736539e227296b6-1920x1080.png)
Image 1: Hierarchical Navigable Small World (HNSW) graph overview

Hierarchical Navigable Small World (HNSW) has become the engine behind many high-performance vector databases and retrieval systems. It consistently delivers state-of-the-art recall with sub-millisecond search speeds on massive vector collections, outperforming older methods like Inverted File (IVF) indexes or Locality-Sensitive Hashing (LSH) [[1]](https://arxiv.org/abs/1603.09320).

Despite its widespread adoption, HNSW’s internal mechanics remain a black box for many engineers. Its blend of graph theory and probabilistic data structures can be difficult to grasp. This article demystifies HNSW, breaking down its core principles, construction, and implementation. Towards the end, we’ll look at how to implement HNSW using Faiss and find the parameter settings that give us the performance we need.

Having oriented ourselves on why HNSW matters, we will now examine the two theoretical pillars it combines: probability skip lists and navigable small world graphs.

## Foundations of HNSW

HNSW belongs to the family of graph-based Approximate Nearest Neighbor (ANN) search algorithms, specifically proximity graphs. In these graphs, nodes represent vectors, and edges connect vectors that are close to each other in the given metric space (like Euclidean distance). HNSW represents a significant leap in complexity from a simple proximity graph, primarily by integrating two powerful concepts: the probability skip list and navigable small world graphs.

### Probability Skip List

A probability skip list is a data structure that enables fast search, like a sorted array, while also allowing for fast insertions, a feature of linked lists [[2]](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf). It achieves this by building multiple layers of linked lists. The bottom layer is a standard sorted linked list containing all elements. Each subsequent layer acts as an "express lane," containing a random subset of the elements from the layer below.

Searching a skip list begins at the sparsest, highest layer. You traverse the list until you find an element greater than your target or reach the end. At that point, you drop down to the next layer and continue the search. This process repeats until you find the target element in the bottom layer. This layered approach allows the search to skip over large numbers of elements, achieving an average search complexity of O(log n).![A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for (or we reach the end), we drop to the next layer.](https://cdn.sanity.io/images/vr8gru94/production/9065d31e1b2e33ca697a56082f0ece7eff1c2d9b-1920x500.png)
Image 2: A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for (or we reach the end), we drop to the next layer.

HNSW inherits the core idea of a multi-layered structure from skip lists. Instead of simple linked lists, HNSW uses proximity graphs at each layer, but the principle of starting coarse and getting finer remains the same.

### Navigable Small World Graphs

Navigable Small World (NSW) graphs are networks where most nodes can be reached from any other node in a small number of steps [[3]](https://www.emergentmind.com/topics/navigable-small-world-nsw). They combine two types of connections: short-range links that connect a node to its immediate neighbors (its "friend list") and long-range links that act as shortcuts across the graph. This structure allows for a greedy routing search algorithm to find paths with a complexity that scales polylogarithmically with the number of nodes [[4]](https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059).![The search process through a NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector.](https://cdn.sanity.io/images/vr8gru94/production/5ca4fca27b2a9bf89b06748b39b7b6238fd4548c-1920x1080.png)
Image 3: The search process through a NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector. (Source https://www.pinecone.io/learn/series/faiss/hnsw)

Greedy routing in an NSW graph starts at a predefined entry point. At each step, the algorithm evaluates the distances from the query vector to the neighbors of the current node and moves to the neighbor that is closest to the query. This process repeats until it reaches a local minimum—a node where none of its neighbors are closer to the query.

The search process typically has two phases. It begins with a "zoom-out" phase, where it traverses long-range links between low-degree nodes to quickly cross large distances in the vector space. As it gets closer to the target region, it enters a "zoom-in" phase, navigating through more densely connected, high-degree nodes to refine the search.

The main weakness of this approach is the risk of getting trapped in a local minimum far from the true nearest neighbor, especially if the graph lacks sufficient connectivity. This "early stopping" can reduce recall. To mitigate this, NSW graphs often increase the average number of connections (degree) per node. However, a higher degree increases the graph's construction complexity, memory footprint, and the cost of each search traversal, creating a fundamental trade-off between recall and performance.

### Creating HNSW

The key innovation of HNSW is the application of the skip list's hierarchical structure to an NSW graph [[1]](https://arxiv.org/abs/1603.09320). Instead of a single, massive graph, HNSW builds a series of nested graphs in layers. The top layer is the sparsest, containing only a few nodes connected by long-range links. Each subsequent layer becomes progressively denser, with the bottom layer containing all the vectors connected by short-range links.![Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous.](https://cdn.sanity.io/images/vr8gru94/production/42d4a3ffc43e5dc2758ba8e5d2ef29d4c4d78254-1920x1040.png)
Image 4: Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous. (Source https://www.pinecone.io/learn/series/faiss/hnsw/)

The search process in HNSW mirrors that of a skip list. It starts at an entry point in the top layer and performs a greedy search to find the local minimum. This node then serves as the entry point for the search in the layer below. This process repeats, descending layer by layer, with each step refining the search. The final greedy search is performed on the dense bottom layer (layer 0) to find the nearest neighbors to the query.![The search process through the multi-layer structure of an HNSW graph.](https://cdn.sanity.io/images/vr8gru94/production/e63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png)
Image 5: The search process through the multi-layer structure of an HNSW graph. (Source https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37)

This hierarchical approach allows HNSW to achieve logarithmic search complexity. The top layers enable fast, coarse-grained navigation across the vector space, while the bottom layers provide the density needed for a precise, fine-grained search. This avoids the high cost of traversing the entire dense graph from the start, which is a limitation of a flat NSW.

With the layered foundations and search behavior clarified, we now turn to the practical iterative algorithm used to construct an HNSW graph one vector at a time.

## Graph Construction

The HNSW graph is built by inserting vectors one by one. The process has a maximum number of layers, `L`. When a new vector is inserted, it is assigned a random maximum layer height, `l`, drawn from an exponentially decaying probability distribution. This means most vectors will only exist in the bottom layers, while very few will be present in the top layers, creating the hierarchical pyramid structure [[1]](https://arxiv.org/abs/1603.09320). The new vector is then inserted into the graph on all layers from `l` down to 0.![The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it.](https://cdn.sanity.io/images/vr8gru94/production/f105cb148aae44f77fa7e3df7b7f8c0256bcbec4-1920x980.png)
Image 6: The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it. (Source https://www.pinecone.io/learn/series/faiss/hnsw/)

The shape of this probability distribution is controlled by a level multiplier parameter, `m_L`. Research has shown that performance is best when the overlap of shared neighbors between layers is minimized. A good rule of thumb for `m_L` is `1/ln(M)`, where `M` is the number of neighbors connected to each new node. This value balances the need for sparse upper layers with the efficiency of traversals during search [[5]](https://www.pinecone.io/learn/series/faiss/hnsw), [[6]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).

The insertion process itself has two phases. First, the algorithm finds the best entry points for the new vector. It starts at the top layer of the graph and performs a simple greedy search (with a candidate list size of `ef=1`) to find the nearest node to the new vector. This node becomes the entry point for the search in the layer below. This continues until it reaches the randomly assigned layer `l`.

In the second phase, starting from layer `l` and going down to layer 0, the algorithm performs a more thorough search. The candidate list size is increased to a construction-time parameter, `efConstruction`. This search identifies the nearest neighbors to the new vector at each layer. From this set of candidates, `M` neighbors are selected and bidirectionally linked to the new node. The maximum number of links per node is capped by `M_max` for the upper layers and `M_max0` (typically `2*M`) for the more dense bottom layer. The neighbors found at each layer then serve as the entry points for the search in the layer below, continuing until the process is complete at layer 0.![Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0.](https://cdn.sanity.io/images/vr8gru94/production/dc5cb11ea197ceb4e1f18214066c8c51526b9af5-1920x1080.png)
Image 7: Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0. (Source https://www.pinecone.io/learn/series/faiss/hnsw/)

Equipped with a clear picture of how the hierarchical graph is built, we now examine the concrete Faiss implementation, index internals, parameter controls, and empirical tradeoffs observed on real workloads.

## Implementation of HNSW

We will implement HNSW using the Facebook AI Similarity Search (Faiss) library and test different construction and search parameters to see how they affect index performance [[7]](https://www.pinecone.io/learn/series/faiss/composite-indexes/).

1.  First, we initialize the HNSW index. We need to specify the vector dimensionality `d` and the number of neighbors `M` for each vertex.
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
    <faiss.impl.HNSW.HNSW; proxy of <Swig Object of type 'faiss::HNSW *' at 0x137568570> >
    ```

2.  Initializing the index sets our `M` parameter, but the maximum number of links per layer, `M_max` (for upper layers) and `M_max0` (for layer 0), are set automatically. Faiss calls a method called `set_default_probas` during initialization, which sets `M_max` to `M` and `M_max0` to `2*M` [[5]](https://www.pinecone.io/learn/series/faiss/hnsw).

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

4.  After we build the index by adding our data (`xb`), the layers are created and populated.
    ```python
    # Sift1M dataset
    # xb contains 1,000,000 128-dimensional vectors
    # xq contains 1,000 128-dimensional query vectors
    
    index.add(xb)
    
    print(f"Maximum layer: {index.hnsw.max_level}")
    levels = faiss.vector_to_array(index.hnsw.levels)
    print(f"Distribution of levels: {np.bincount(levels)}")
    ```
    It outputs:
    ```text
    Maximum layer: 4
    Distribution of levels: [908953  82103   8115    820     98      1]
    ```
    This shows the distribution of the 1 million vectors across the 5 layers (0 to 4).

5.  The index also has a designated entry point, which is always a node in the highest layer.
    ```python
    print(f"Entry point: {index.hnsw.entry_point}")
    ```
    It outputs:
    ```text
    Entry point: 118295
    ```

### Graph Structure

The `set_default_probas` method in Faiss determines the probability of a new vector being assigned to each layer. It takes `M` and a level multiplier `levelMult` (equivalent to `m_L`, which defaults to `1 / log(M)`) as input. It then calculates the probability for each layer until the probability becomes negligibly small [[5]](https://www.pinecone.io/learn/series/faiss/hnsw).

1.  We can replicate this logic in Python to understand how the layer probabilities are determined.
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
            # M2 is M*2
            nn += (M * 2) if level == 0 else M
            cum_nneighbor_per_level.append(nn)
            level += 1
        return assign_probas, cum_nneighbor_per_level
    ```

2.  With `M=32`, we can see the calculated probabilities.
    ```python
    m_L = 1 / np.log(32)
    assign_probas, cum_nneighbor_per_level = set_default_probas(32, m_L)
    
    print(f"assign_probas: {assign_probas}")
    print(f"cum_nneighbor_per_level: {cum_nneighbor_per_level}")
    ```
    It outputs:
    ```text
    assign_probas: [0.9118748365942065, 0.08141003461440816, 0.00632616229381711, 0.0003889664975681146, 1.493923055171738e-05, 3.655938099852021e-07, 5.922033324659438e-09]
    cum_nneighbor_per_level: [64, 96, 128, 160, 192, 224, 256]
    ```
    As expected, the probability of being inserted into layer 0 is very high (over 91%), and it drops exponentially for higher layers.

3.  The `random_level` function uses these probabilities to assign a layer to a new vector.
    ```python
    def random_level(assign_probas):
        # draw random value from [0, 1)
        f = np.random.rand()
        # find the first level whose cumulative probability is > f
        for level in range(len(assign_probas)):
            if f < assign_probas[level]:
                return level
            f -= assign_probas[level]
        # if f is not consumed, return the highest level
        return len(assign_probas) - 1
    ```

4.  Simulating this process for 1 million vectors gives a distribution very similar to what Faiss produced.
    ```python
    levels = [random_level(assign_probas) for _ in range(1_000_000)]
    print(np.bincount(levels))
    ```
    It outputs:
    ```text
    [911760  81467   6391    366     16      0]
    ```![Distribution of vertices across layers in both the Faiss implementation (left) and the Python implementation (right).](https://cdn.sanity.io/images/vr8gru94/production/75658a08c25dabc1405f769c76fd2929c051853b-1920x930.png)
Image 8: Distribution of vertices across layers in both the Faiss implementation (left) and the Python implementation (right). (Source https://www.pinecone.io/learn/series/faiss/hnsw/)

The distributions are nearly identical. The only minor difference is that Faiss guarantees at least one vector is placed in the highest layer to serve as the graph's entry point.

### HNSW Performance

To understand the performance trade-offs, we can sweep through different values for `M`, `efSearch`, and `efConstruction` on the Sift1M dataset.

1.  The `efConstruction` parameter must be set before building the index, while `efSearch` can be adjusted any time before searching.
    ```python
    # M, efConstruction, efSearch are parameters we modify
    
    index = faiss.IndexHNSWFlat(d, M)
    
    index.hnsw.efConstruction = efConstruction
    index.add(xb)  # build the index
    
    index.hnsw.efSearch = efSearch  # and now we can search
    index.search(xq[:1000], k=1)
    ```

2.  The recall performance is highly sensitive to these parameters.
    ![Recall@1 performance for various M, efConstruction, and efSearch parameters.](https://cdn.sanity.io/images/vr8gru94/production/e8c281c3626226a76389fa344a71eb57f70cf879-1920x980.png)
    Image 9: Recall@1 performance for various M, efConstruction, and efSearch parameters. (Source https://www.pinecone.io/learn/series/faiss/hnsw/)

    Higher values for `M` and `efSearch` significantly improve recall. A reasonably high `efConstruction` is also necessary for good performance, and increasing it can often compensate for lower `M` and `efSearch` values, allowing you to achieve high recall with a smaller, faster index.

3.  Search time also increases with these parameters.
    ![Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is using a log scale.](https://cdn.sanity.io/images/vr8gru94/production/876bf66aba408959042888efe72c55db4d6b3b41-1920x980.png)
    Image 10: Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is using a log scale. (Source https://www.pinecone.io/learn/series/faiss/hnsw/)

    There is a clear trade-off between recall and search time. For our batch of 1000 queries, search times ranged from around 1ms for 80% recall to 50ms for near-100% recall. It is often assumed that `efConstruction` has little impact on search time, but this only holds true for very small query volumes. For larger batches, a higher `efConstruction` leads to a better-structured graph that can actually speed up search.

4.  When the query volume is low (e.g., a single query), increasing `efConstruction` is an excellent way to boost recall with almost no added search-time cost, especially at lower `M` values.
    ![efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values.](https://cdn.sanity.io/images/vr8gru94/production/ef1a2edd25adb202c0a98a1f33a0e72d1295b554-1720x1080.png)
    Image 11: efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values. (Source https://www.pinecone.io/learn/series/faiss/hnsw/)

5.  Memory usage is another critical factor. Only `M` affects the index size; `efConstruction` and `efSearch` do not.
    ![Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage.](https://cdn.sanity.io/images/vr8gru94/production/e04d23ccd76d8bdc568542bebe75a75e7d36a21e-1480x1050.png)
    Image 12: Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage. (Source https://www.pinecone.io/learn/series/faiss/hnsw/)

    The memory cost of HNSW can be substantial. Even with a small `M=2`, the index for Sift1M is over 0.5GB. At `M=512`, it approaches 5GB. This highlights the three-way trade-off between recall, latency, and memory that engineers must balance based on their specific application and infrastructure constraints.

### Improving Memory Usage and Search Speeds

When the memory footprint of HNSW becomes too large, there are several strategies to mitigate it. The most common is to compress the stored vectors using Product Quantization (PQ). This significantly reduces memory usage but comes at the cost of lower recall and potentially slower search times due to the overhead of decoding vectors.

Another approach is to wrap HNSW within an IVF component. In this setup, HNSW is used as a coarse quantizer to quickly identify the most promising IVF cells to search, which can improve search speed. These composite index strategies offer more advanced ways to tune the performance of your vector search system.

## Conclusion

HNSW stands out as a powerful and versatile algorithm for approximate nearest neighbor search. By combining the layered structure of skip lists with the efficient routing of navigable small world graphs, it achieves an excellent balance of speed and accuracy on large-scale, high-dimensional datasets.

However, its performance is not a given. It depends on a careful tuning of its parameters—`M`, `efConstruction`, and `efSearch`—to navigate the complex trade-offs between recall, latency, and memory usage. As we have seen with Faiss, understanding how these parameters influence the graph's structure and the search process is key to unlocking HNSW's full potential. For engineers building modern AI applications, mastering HNSW is no longer optional; it is a fundamental skill for creating fast, accurate, and scalable retrieval systems.

## References

- [1] [Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs](https://arxiv.org/abs/1603.09320)
- [2] [Skip Lists: A Probabilistic Alternative to Balanced Trees](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)
- [3] [Navigable Small World Graphs](https://www.emergentmind.com/topics/navigable-small-world-nsw)
- [4] [Approximate nearest neighbor algorithm based on navigable small world graphs](https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059)
- [5] [Facebook AI and HNSW](https://www.pinecone.io/learn/series/faiss/hnsw)
- [6] [Similarity Search, Part 4: Hierarchical Navigable Small World (HNSW)](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37)
- [7] [Facebook AI and the Index Factory](https://www.pinecone.io/learn/series/faiss/composite-indexes/)
- [8] [Faiss HNSW Implementation](https://github.com/facebookresearch/faiss/blob/main/faiss/impl/HNSW.cpp)