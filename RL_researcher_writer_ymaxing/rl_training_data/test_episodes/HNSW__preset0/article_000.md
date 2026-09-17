# HNSW: The Backbone of Modern Vector Search![Hierarchical Navigable Small World (HNSW) graph overview](https://cdn.sanity.io/images/vr8gru94/production/d6e3a660654d9cb55f7ac137a736539e227296b6-1920x1080.png)
Image 1: An overview of a Hierarchical Navigable Small World (HNSW) graph.

Hierarchical Navigable Small World (HNSW) is one of the most powerful algorithms in the world of Approximate Nearest Neighbor (ANN) search. It consistently delivers state-of-the-art recall with sub-millisecond query speeds, even on massive vector datasets. This performance puts it ahead of many other methods, like Inverted File (IVF) indexes or Locality-Sensitive Hashing (LSH), which often trade more accuracy for speed.

Despite its widespread adoption in vector databases and retrieval systems, the internal mechanics of HNSW remain a black box for many engineers. This article aims to demystify HNSW, breaking down its theoretical foundations and practical implementation. Towards the end, we’ll look at how to implement HNSW using Faiss and find the parameter settings that give us the performance we need.

Having oriented ourselves on why HNSW matters, we will now examine the two core theoretical pillars it combines: probability skip lists and navigable small world graphs.

## Foundations of HNSW

HNSW belongs to the category of graph-based ANN algorithms, specifically proximity graphs. In these graphs, nodes represent vectors, and edges connect vectors that are close to each other in the given metric space, such as Euclidean distance. While the concept of a proximity graph is straightforward, HNSW introduces a sophisticated hierarchical structure that makes it far more complex and efficient. This innovation is built on two fundamental data structures: the probability skip list and the navigable small world graph.

### Probability Skip List

A probability skip list is a data structure that combines the fast search capabilities of a sorted array with the efficient insertion of a linked list [[2]](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf), [1](https://en.wikipedia.org/wiki/Skip_list). It achieves this by building multiple layers of linked lists. The bottom layer is a standard sorted linked list containing all elements. Each subsequent layer acts as an "express lane," containing a random subset of the elements from the layer below. This structure allows searches to start at the sparsest top layer, quickly skipping over large portions of the list before dropping down to more granular layers to pinpoint the target element.![A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for (or we reach the end), we drop to the next layer.](https://cdn.sanity.io/images/vr8gru94/production/9065d31e1b2e33ca697a56082f0ece7eff1c2d9b-1920x500.png)
Image 2: A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for (or we reach the end), we drop to the next layer.

This layered approach allows for an average search and insertion complexity of O(log n). HNSW inherits this core idea of a multi-layered structure to enable fast traversal, but it applies this concept to graphs instead of simple linked lists.

### Navigable Small World Graphs

Navigable Small World (NSW) graphs are networks where most nodes can be reached from any other node in a small number of steps [[4]](https://arxiv.org/abs/1507.06529), [5](https://www.emergentmind.com/topics/navigable-small-world-nsw). They achieve this by combining two types of connections: short-range links that connect nearby nodes (the "friend list") and long-range links that act as bridges between distant parts of the graph. This structure allows a search algorithm to navigate the graph with (poly-)logarithmic complexity relative to its size [[3]](https://www.iiis.org/CDs2011/CD2011IDI/ICTA_2011/PapersPdf/CT175ON.pdf).![The search process through a NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector.](https://cdn.sanity.io/images/vr8gru94/production/5ca4fca27b2a9bf89b06748b39b7b6238fd4548c-1920x1080.png)
Image 3: The search process through an NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector.

Searching an NSW graph is done using a greedy routing algorithm. The process begins at a designated entry point and, at each step, moves to the neighbor in the current node's friend list that is closest to the query vector. This continues until the algorithm reaches a local minimum—a node where no neighbor is closer to the query than the node itself [[3]](https://www.iiis.org/CDs2011/CD2011IDI/ICTA_2011/PapersPdf/CT175ON.pdf).

This routing process has two distinct phases. The "zoom-out" phase occurs early in the search, where the algorithm traverses long-range links between low-degree nodes to quickly cover large distances and approach the general vicinity of the query. The subsequent "zoom-in" phase involves traversing short-range links between high-degree nodes to refine the search and locate the nearest neighbor [[6]](https://arxiv.org/abs/1603.09320).

However, this greedy approach has a notable weakness: it can get trapped in a local minimum far from the true nearest neighbor, especially if the graph lacks sufficient connectivity. This "early stopping" problem can reduce recall. To mitigate this, the average degree of the graph can be increased, which creates a denser network with more paths to the target. This, however, comes at the cost of higher construction complexity, increased memory usage, and more distance calculations during each query. This trade-off between recall and performance is a central challenge in designing graph-based indexes.

### Creating HNSW

The key innovation of HNSW is its hierarchical structure, which applies the layering concept of skip lists to an NSW graph. Instead of a single graph, HNSW builds a multi-layered graph where the top layer contains only the longest-range links, and each subsequent layer becomes progressively denser with shorter-range links. The bottom layer contains all the nodes and the most granular connections [[6]](https://arxiv.org/abs/1603.09320).![Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous.](https://cdn.sanity.io/images/vr8gru94/production/42d4a3ffc43e5dc2758ba8e5d2ef29d4c4d78254-1920x1040.png)
Image 4: Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous.

The search process in HNSW mirrors this layered design. It starts at an entry point in the top layer and uses a greedy algorithm to find the nearest neighbor within that layer. Once it reaches a local minimum, it uses that node as the entry point to descend to the layer below. This process repeats, with the search becoming progressively finer at each level, until it completes the search on the dense bottom layer (layer 0).![The search process through the multi-layer structure of an HNSW graph.](https://cdn.sanity.io/images/vr8gru94/production/e63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png)
Image 5: The search process through the multi-layer structure of an HNSW graph.

This hierarchical approach elegantly solves the main performance bottleneck of a flat NSW graph. By starting with a coarse search and refining it layer by layer, HNSW avoids the high cost of traversing the entire dense graph from the beginning. It combines the rapid, long-distance navigation of the "zoom-out" phase with the precise, local refinement of the "zoom-in" phase in a structured and efficient manner, achieving logarithmic search complexity [[6]](https://arxiv.org/abs/1603.09320).

With the layered foundations and search behavior clarified, we now turn to the practical iterative algorithm used to construct an HNSW graph one vector at a time.

## Graph Construction

The HNSW graph is built iteratively by inserting vectors one by one. A key parameter in this process is `L`, the maximum number of layers in the graph. When a new vector is inserted, it is randomly assigned a layer height, `l`, drawn from an exponentially decaying probability distribution. This ensures that most vectors exist only in the lower, denser layers, while a few are promoted to the upper, sparser layers to serve as long-range "express lane" connections [[6]](https://arxiv.org/abs/1603.09320).![The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it.](https://cdn.sanity.io/images/vr8gru94/production/f105cb148aae44f77fa7e3df7b7f8c0256bcbec4-1920x980.png)
Image 6: The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it. (Source [7](https://www.pinecone.io/learn/series/faiss/hnsw/))

The probability distribution is controlled by a level multiplier parameter, `m_L`, typically set to `1/ln(M)`. This value is chosen to balance two competing factors: minimizing the overlap of shared neighbors across layers, which improves search efficiency, while ensuring enough connections exist at each layer to prevent the search from taking too many steps [[7]](https://www.pinecone.io/learn/series/faiss/hnsw/). This balance is what helps HNSW maintain its logarithmic search complexity.

The insertion process itself occurs in two phases. First, a greedy search with a small candidate list size (`ef=1`) is performed from the top layer down to the assigned insertion layer `l`. This quickly identifies the right neighborhood for the new vector. In the second phase, a more thorough search, parameterized by `efConstruction`, is conducted from layer `l` down to layer 0. At each of these layers, the algorithm finds the `efConstruction` nearest neighbors to the new vector. From this candidate set, `M` neighbors are selected and bidirectionally linked to the new vector [[6]](https://arxiv.org/abs/1603.09320).

The number of connections per node is capped at each layer. For all layers above the base layer, the maximum number of links is `M_max`. For the base layer (layer 0), this cap is doubled to `M_max0` to ensure high connectivity for the final, most detailed part of the search [[7]](https://www.pinecone.io/learn/series/faiss/hnsw/). The candidates found at each layer during this second phase also serve as the entry points for the search in the layer below, ensuring the graph remains navigable as it is constructed.![Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0.](https://cdn.sanity.io/images/vr8gru94/production/dc5cb11ea197ceb4e1f18214066c8c51526b9af5-1920x1080.png)
Image 7: Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0. (Source [7](https://www.pinecone.io/learn/series/faiss/hnsw/))

Equipped with a clear picture of how the hierarchical graph is built, we now examine the concrete Faiss implementation, index internals, parameter controls, and empirical tradeoffs observed on real workloads.

## Implementation of HNSW

We will implement HNSW using the Facebook AI Similarity Search (Faiss) library and test how different construction and search parameters affect index performance [[10]](https://github.com/facebookresearch/faiss/wiki/Indexing-1M-vectors).

1.  We start by initializing a basic HNSW index. We will use `IndexHNSWFlat`, which means the actual vectors are stored as-is without compression. We need to define the vector dimensionality `d` and the number of neighbors `M` to connect for each vertex.
    ```python
    import faiss
    import numpy as np
    
    # setup our HNSW parameters
    d = 128 # vector size
    M = 32
    
    index = faiss.IndexHNSWFlat(d, M)
    print(index.hnsw)
    ```
    It outputs:
    ```text
    <faiss.impl.HNSW.HNSW; proxy of <Swig Object of type 'faiss::HNSW *' at 0x137532390> >
    ```
    The parameter `M` sets the number of neighbors added during insertion. However, the `M_max` (max connections for upper layers) and `M_max0` (max connections for layer 0) parameters are set automatically by Faiss's `set_default_probas` method, which is called during initialization. It sets `M_max = M` and `M_max0 = M * 2` [[7]](https://www.pinecone.io/learn/series/faiss/hnsw/).

2.  Before we add any data, the index is empty. The maximum level is not set, and there are no vectors distributed across layers.
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

3.  Now, let's build the index by adding our data vectors (`xb`). After adding the data, we can see that the `max_level` has been set, and the `levels` array shows how many vectors are assigned to each layer.
    ```python
    # For this example, we'll use the Sift1M dataset
    # xb contains 1,000,000 128-dimensional vectors
    index.add(xb)
    
    print(index.hnsw.max_level)
    
    levels = faiss.vector_to_array(index.hnsw.levels)
    print(np.bincount(levels))
    ```
    It outputs:
    ```text
    4
    [969443  30046    501      9      1]
    ```
    This output shows that the index has 5 layers (0 to 4). The vast majority of vectors (969,443) are in the base layer (layer 0), with exponentially fewer vectors in the upper layers, which is exactly what we expect from the probabilistic layer assignment.

4.  The index also has a single entry point, which is the starting node for all searches.
    ```python
    print(index.hnsw.entry_point)
    ```
    It outputs:
    ```text
    118295
    ```

### Graph Structure

The layered structure of the graph is determined by the `set_default_probas` method in Faiss. When we initialize the index, this method is called with `M` and a level multiplier `m_L` (called `levelMult` in Faiss) set to `1 / log(M)`. This method calculates the probability of a new vector being inserted at each layer [[7]](https://www.pinecone.io/learn/series/faiss/hnsw/).

1.  We can replicate this logic in Python to understand how it works. The function calculates `assign_probas`, the probability for each layer, and `cum_nneighbor_per_level`, the cumulative neighbor count.
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

2.  Let's run this with our `M=32`.
    ```python
    assign_probas, cum_nneighbor_per_level = set_default_probas(32, 1/np.log(32))
    print(assign_probas)
    print(cum_nneighbor_per_level)
    ```
    It outputs:
    ```text
    [0.969485455940933, 0.03002931535792945, 0.0004851287011375375, 7.83693175416246e-06, 1.2659345229415865e-07, 2.0448144033785237e-09]
    [64, 96, 128, 160, 192, 224]
    ```
    The `assign_probas` list shows a very high probability (96.9%) of inserting a vector at layer 0, with probabilities decaying exponentially for higher layers.

3.  The actual layer for a new vector is chosen by the `random_level` function. It generates a random number and compares it against the cumulative probabilities derived from `assign_probas`.
    ```python
    def random_level(assign_probas):
        f = np.random.rand()
        for i, proba in enumerate(assign_probas):
            f -= proba
            if f < 0:
                return i
        return len(assign_probas) - 1
    ```

4.  We can simulate the insertion of 1,000,000 vectors to see if our Python logic matches the actual Faiss distribution.
    ```python
    # Simulate with our python implementation
    py_levels = np.array([random_level(assign_probas) for _ in range(1000000)])
    print(np.bincount(py_levels))
    
    # Get true levels from Faiss
    faiss_levels = faiss.vector_to_array(index.hnsw.levels)
    print(np.bincount(faiss_levels))
    ```
    It outputs:
    ```text
    [969544  29953    494      9      0      0]
    [969443  30046    501      9      1]
    ```
    The distributions are nearly identical, confirming our understanding of the layer assignment mechanism.![Distribution of vertices across layers in both the Faiss implementation (left) and the Python implementation (right).](https://cdn.sanity.io/images/vr8gru94/production/75658a08c25dabc1405f769c76fd2929c051853b-1920x930.png)
Image 8: Distribution of vertices across layers in both the Faiss implementation (left) and the Python implementation (right). (Source [7](https://www.pinecone.io/learn/series/faiss/hnsw/))

One small detail is that the Faiss implementation guarantees that at least one vector is present in the highest layer, which serves as the entry point for the graph [[7]](https://www.pinecone.io/learn/series/faiss/hnsw/).

### HNSW Performance

Now, let's analyze the performance trade-offs by adjusting the three key parameters: `M`, `efConstruction`, and `efSearch`, using the Sift1M dataset.

1.  These parameters are set on the index object. `efConstruction` must be configured before building the index with `index.add()`, while `efSearch` can be adjusted any time before a search.
    ```python
    # Re-initialize index
    index = faiss.IndexHNSWFlat(d, M)
    
    # Set construction and search parameters
    efConstruction = 40
    efSearch = 16
    
    index.hnsw.efConstruction = efConstruction
    index.add(xb) # build the index
    
    index.hnsw.efSearch = efSearch
    # and now we can search
    D, I = index.search(xq[:1000], k=1)
    ```

2.  **Recall:** Higher values for `M` and `efSearch` significantly improve recall. A reasonably high `efConstruction` is also necessary to build a high-quality graph. Increasing `efConstruction` can often compensate for lower `M` and `efSearch` values, allowing you to achieve high recall with a smaller, faster index [[7]](https://www.pinecone.io/learn/series/faiss/hnsw/).

    ![Recall@1 performance for various M, efConstruction, and efSearch parameters.](https://cdn.sanity.io/images/vr8gru94/production/e8c281c3626226a76389fa344a71eb57f70cf879-1920x980.png)
    Image 9: Recall@1 performance for various M, efConstruction, and efSearch parameters. (Source [7](https://www.pinecone.io/learn/series/faiss/hnsw/))

3.  **Search Time:** There is a clear trade-off between recall and search time. As you increase `M`, `efSearch`, and `efConstruction` to get better accuracy, the search latency increases. A common assumption is that `efConstruction` has little impact on search time, but this is only true for a very low volume of queries. For larger batches, a higher `efConstruction` leads to a denser, more complex graph that takes longer to traverse [[7]](https://www.pinecone.io/learn/series/faiss/hnsw/).

    ![Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is using a log scale.](https://cdn.sanity.io/images/vr8gru94/production/876bf66aba408959042888efe72c55db4d6b3b41-1920x980.png)
    Image 10: Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is using a log scale. (Source [7](https://www.pinecone.io/learn/series/faiss/hnsw/))

    However, if your application handles queries one by one, increasing `efConstruction` is an excellent way to boost recall with minimal impact on search latency, especially at lower `M` values.

    ![efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values.](https://cdn.sanity.io/images/vr8gru94/production/ef1a2edd25adb202c0a98a1f33a0e72d1295b554-1720x1080.png)
    Image 11: efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values. (Source [7](https://www.pinecone.io/learn/series/faiss/hnsw/))

4.  **Memory Usage:** Of the three parameters, only `M` affects the memory footprint of the index. `efConstruction` and `efSearch` are search-time parameters that do not change the size of the stored graph. The memory usage grows linearly with `M`, and it can become substantial. For the Sift1M dataset, the index size starts at over 0.5 GB for `M=2` and grows to nearly 5 GB for `M=512` [[7]](https://www.pinecone.io/learn/series/faiss/hnsw/). This highlights the critical three-way trade-off between recall, latency, and memory that engineers must balance based on their specific application requirements and infrastructure constraints.

    ![Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage.](https://cdn.sanity.io/images/vr8gru94/production/e04d23ccd76d8bdc568542bebe75a75e7d36a21e-1480x1050.png)
    Image 12: Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage. (Source [7](https://www.pinecone.io/learn/series/faiss/hnsw/))

### Improving Memory Usage and Search Speeds

The high memory consumption of HNSW can be a significant challenge in production environments. When memory becomes a bottleneck, there are two common strategies to mitigate it. First, you can compress the stored vectors using Product Quantization (PQ). This drastically reduces memory usage but comes at the cost of lower recall and slightly increased search times. Second, you can wrap the HNSW index within an IVF component. This combination uses HNSW to quickly identify the most promising IVF cells to search, improving search speed, especially for very large datasets.

We cover how to combine IVF and PQ with HNSW in our article on composite indexes.

## References

- [1] Skip list - Wikipedia. (n.d.). [https://en.wikipedia.org/wiki/Skip_list](https://en.wikipedia.org/wiki/Skip_list)
- [2] Pugh, W. (1990). Skip Lists: A Probabilistic Alternative to Balanced Trees. Communications of the ACM. [https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf](https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf)
- [3] Ponomarenko, A., Mal'kov, Y., Logvinov, A., & Krylov, V. (2011). Approximate Nearest Neighbor Search Small World Approach. [https://www.iiis.org/CDs2011/CD2011IDI/ICTA_2011/PapersPdf/CT175ON.pdf](https://www.iiis.org/CDs2011/CD2011IDI/ICTA_2011/PapersPdf/CT175ON.pdf)
- [4] Malkov, Y. A., & Ponomarenko, A. (2015). Growing homophilic networks are natural navigable small worlds. [https://arxiv.org/abs/1507.06529](https://arxiv.org/abs/1507.06529)
- [5] Navigable Small World Graphs. (2025, December 14). Emergent Mind. [https://www.emergentmind.com/topics/navigable-small-world-nsw](https://www.emergentmind.com/topics/navigable-small-world-nsw)
- [6] Malkov, Y. A., & Yashunin, D. A. (2016). Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs. [https://arxiv.org/abs/1603.09320](https://arxiv.org/abs/1603.09320)
- [7] HNSW | Faiss. (n.d.). Pinecone. [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/)
- [8] Malkov, Y., Ponomarenko, A., Logvinov, A., & Krylov, V. (2012). Scalable Distributed Algorithm for Approximate Nearest Neighbor Search Problem in High Dimensional General Metric Spaces. [https://www.researchgate.net/publication/262334462_Scalable_Distributed_Algorithm_for_Approximate_Nearest_Neighbor_Search_Problem_in_High_Dimensional_General_Metric_Spaces](https://www.researchgate.net/publication/262334462_Scalable_Distributed_Algorithm_for_Approximate_Nearest_Neighbor_Search_Problem_in_High_Dimensional_General_Metric_Spaces)
- [9] Malkov, Y., Ponomarenko, A., Logvinov, A., & Krylov, V. (2014). Approximate nearest neighbor algorithm based on navigable small world graphs. Information Systems. [https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059](https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059)
- [10] Indexing 1M vectors. (2022, January 11). Faiss Wiki. [https://github.com/facebookresearch/faiss/wiki/Indexing-1M-vectors](https://github.com/facebookresearch/faiss/wiki/Indexing-1M-vectors)
- [11] Boguñá, M., Krioukov, D., & claffy, kc. (2007). Navigability of complex networks. [https://arxiv.org/abs/0709.0303](https://arxiv.org/abs/0709.0303)
- [12] Faiss C++ implementation of HNSW. (n.d.). GitHub. [https://github.com/facebookresearch/faiss/blob/main/faiss/impl/HNSW.cpp](https://github.com/facebookresearch/faiss/blob/main/faiss/impl/HNSW.cpp)
- [13] Facebook AI and the Index Factory. (n.d.). Pinecone. [https://www.pinecone.io/learn/series/faiss/composite-indexes/](https://www.pinecone.io/learn/series/faiss/composite-indexes/)
- [14] Faiss. (n.d.). Pinecone. [https://www.pinecone.io/learn/series/faiss/](https://www.pinecone.io/learn/series/faiss/)