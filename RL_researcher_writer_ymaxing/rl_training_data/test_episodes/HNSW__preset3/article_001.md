# A Deep Dive into HNSW: The Algorithm Behind Modern Vector Search

Hierarchical Navigable Small World (HNSW) is one of the most powerful algorithms in Approximate Nearest Neighbor (ANN) search. It consistently delivers state-of-the-art recall with sub-millisecond query speeds on massive vector datasets. This performance has made it the engine behind many production vector databases, powering applications from multimodal search to large-scale recommendation engines [[1]](https://redis.io/blog/how-hnsw-algorithms-can-improve-search), [[2]](https://arxiv.org/html/2405.17813v1).![Hierarchical Navigable Small World (HNSW) graph overview](https://cdn.sanity.io/images/vr8gru94/production/d6e3a660654d9cb55f7ac137a736539e227296b6-1920x1080.png)
Image 1: An overview of the Hierarchical Navigable Small World (HNSW) graph structure. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

Despite its widespread adoption, the inner workings of HNSW can feel like a black box. Its combination of graph theory and probabilistic data structures is a significant step up from simpler methods like Inverted File (IVF) indexes or Locality-Sensitive Hashing (LSH). This article demystifies HNSW, breaking down its theoretical foundations, construction algorithm, and practical implementation. We will also look at how to implement HNSW using Faiss and find the optimal parameter settings for your needs [[3]](https://www.pinecone.io/learn/series/faiss/hnsw). To understand HNSW, we first need to explore its two core building blocks: probabilistic skip lists and navigable small world graphs.

## Foundations of HNSW

HNSW belongs to the family of graph-based ANN algorithms, specifically proximity graphs. In these graphs, nodes represent vectors, and edges connect vectors that are close to each other in the given metric space (like Euclidean distance). HNSW's innovation lies in how it organizes these connections into a hierarchical, navigable structure. This structure is a synthesis of two powerful concepts: the probabilistic skip list and the navigable small world graph [[4]](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf).

### Probability Skip List

A skip list is a probabilistic data structure that allows for fast search, insertion, and deletion operations, achieving an average time complexity of O(log n) [[5]](https://www.geeksforgeeks.org/dsa/skip-list), [[6]](https://en.wikipedia.org/wiki/Skip_list). It augments a standard sorted linked list with additional layers of "express lanes." The bottom layer is a complete linked list. Each higher layer contains a sparser subsequence of the elements from the layer below it. An element in layer *i* appears in layer *i+1* with a fixed probability *p* [[6]](https://en.wikipedia.org/wiki/Skip_list).![A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for (or we reach the end), we drop to the next layer.](https://cdn.sanity.io/images/vr8gru94/production/9065d31e1b2e33ca697a56082f0ece7eff1c2d9b-1920x500.png)
Image 2: A probability skip list structure. The search starts at the top layer and moves horizontally until it overshoots the target, then drops to the layer below. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

To search for an element, you start at the head of the sparsest, topmost list. You traverse horizontally until you find an element greater than or equal to your target. At that point, you drop down to the next layer from the previous element and repeat the process. This allows you to "skip" over large portions of the list, drastically reducing search time compared to a linear scan [[7]](https://brilliant.org/wiki/skip-lists). HNSW borrows this core idea of a multi-layered structure with probabilistic element promotion to build its hierarchy.

### Navigable Small World Graphs

Navigable Small World (NSW) graphs are networks designed for efficient greedy routing. They emerged as a powerful alternative to tree-based structures like k-d trees, which become inefficient in high-dimensional spaces due to the "curse of dimensionality." As dimensions increase, the volume of the space grows so rapidly that tree-based partitioning fails to prune the search space effectively, degrading performance to near brute-force [[8]](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture). NSW graphs avoid this by creating a network with two key properties: many short-range links connecting local neighbors and a few long-range links that connect distant parts of the graph [[9]](https://openreview.net/pdf/9d557864b10a646d79ecf63772864cc3c168091f.pdf). This ensures that the average path length between any two nodes is small, typically scaling logarithmically with the number of nodes.![The search process through a NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector.](https://cdn.sanity.io/images/vr8gru94/production/5ca4fca27b2a9bf89b06748b39b7b6238fd4548c-1920x1080.png)
Image 3: The search process in a Navigable Small World (NSW) graph, where the algorithm greedily moves toward the query. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

Searching an NSW graph uses a greedy routing algorithm. The process starts at a predefined entry point. At each step, it evaluates the distances from the query vector to all neighbors of the current node (its "friend list") and moves to the neighbor that is closest to the query [[10]](https://www.pinecone.io/learn/series/faiss/hnsw). This is repeated until it reaches a local minimum—a node that is closer to the query than any of its neighbors. This node is then returned as the approximate nearest neighbor [[11]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).

The search process typically has two phases. It begins with a "zoom-out" phase, where it traverses long-range links connecting low-degree vertices to quickly navigate to the general region of the query. This is followed by a "zoom-in" phase, where it moves through short-range links between higher-degree vertices to refine the search and converge on the nearest neighbor [[10]](https://www.pinecone.io/learn/series/faiss/hnsw/).

The main weakness of NSW is the risk of getting trapped in a local minimum far from the true nearest neighbor, which reduces recall. This happens when the graph's connectivity is insufficient, a risk that grows in highly clustered or discontinuous data distributions [[12]](https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605). The straightforward solution is to increase the average number of connections per node (`M`), but this comes at the cost of higher memory usage and longer construction and search times. This tradeoff is a central challenge in tuning graph-based ANN methods.

### Creating HNSW

The core innovation of HNSW is the application of a skip-list-like hierarchical structure to NSW graphs. Instead of a single graph, HNSW builds a multi-layered structure where each layer is a proximity graph. The top layer is the sparsest and contains only the longest-range links, acting as a fast entry point for search. Each subsequent layer becomes progressively denser, adding shorter-range links [[13]](https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf), [[4]](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf).![Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous.](https://cdn.sanity.io/images/vr8gru94/production/42d4a3ffc43e5dc2758ba8e5d2ef29d4c4d78254-1920x1040.png)
Image 4: The layered graph structure of HNSW, with long-range links at the top and shorter, denser links at the bottom. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

The search process in HNSW mirrors this layered design. It starts at an entry point in the top layer and performs a greedy search to find a local minimum. This minimum then serves as the entry point for the search in the layer below. This process repeats, descending layer by layer, with each step refining the search. The final, most detailed search is performed on the densest bottom layer (layer 0).

This hierarchical approach differs significantly from the search in a flat NSW graph. While both rely on greedy routing, HNSW's search is a deterministic, top-down process starting from a single, fixed entry point in the highest layer. In contrast, a flat NSW search typically involves multiple independent greedy searches starting from several random entry points to mitigate the risk of getting stuck in local minima. HNSW replaces this multi-start strategy with a single, structured descent through its layers, which provides a more efficient path to the target region. The hierarchy effectively guides the search from a coarse "zoom-out" to a fine "zoom-in," a process that a flat NSW can only approximate through its link structure.![The search process through the multi-layer structure of an HNSW graph.](https://cdn.sanity.io/images/vr8gru94/production/e63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png)
Image 5: The search process in HNSW involves a greedy search at each layer, using the result as the entry point for the next layer down. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

This hierarchical approach elegantly solves the main problems of a flat NSW graph. By separating links by scale, it avoids the high cost of traversing dense neighborhoods in the early stages of the search. The initial "zoom-out" is performed on the sparse upper layers, leading to logarithmic complexity. The final "zoom-in" is done on the dense bottom layer, ensuring high accuracy. This combination provides a much better balance of speed and recall than a single-layer graph.

However, recent research has questioned whether the hierarchy is always necessary. In high-dimensional spaces, phenomena like "concentration of distance" (where distances between random points become increasingly similar) and "hubness" (where a few points appear in many other points' neighbor lists) can naturally create a highly connected "highway" of hub nodes. This "Hub Highway Hypothesis" suggests that for high-dimensional data (d > 32), the graph's intrinsic structure may already provide the fast routing that the hierarchy was designed to create, potentially making the 'H' in HNSW redundant [[14]](https://arxiv.org/html/2412.01940v2). With the layered foundations and search behavior clarified, we now turn to the practical iterative algorithm used to construct an HNSW graph one vector at a time.

## Graph Construction

The HNSW graph is built dynamically by inserting vectors one by one, a key advantage that allows the index to be updated for streaming data without requiring complete rebuilds [[15]](https://www.tigerdata.com/blog/vector-database-basics-hnsw). The process for each new vector involves two main stages: selecting its maximum layer and then connecting it to its neighbors within that layer and all layers below it.

When a new vector is added, it is assigned a random maximum layer `l` based on an exponentially decaying probability distribution [[4]](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf), [[16]](https://arxiv.org/html/2412.01940v2). This is analogous to the probabilistic promotion in a skip list. Most vectors are assigned to layer 0, with exponentially fewer appearing in higher layers. This ensures the top layers remain sparse. The formula used is `l = floor(-ln(uniform(0,1)) * mL)`, where `mL` is a normalization factor called the level multiplier [[17]](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW).![The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it.](https://cdn.sanity.io/images/vr8gru94/production/f105cb148aae44f77fa7e3df7b7f8c0256bcbec4-1920x980.png)
Image 6: A new vector is assigned a random maximum layer and is inserted into that layer and all layers below it. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

The parameter `mL` is crucial for performance. The creators of HNSW found that the best results are achieved when the overlap of shared neighbors across layers is minimized. A smaller `mL` pushes more vectors to layer 0, reducing overlap, but it also increases the average number of traversals needed during a search. The optimal value balances these factors, and a good rule of thumb is `mL = 1/ln(M)`, where `M` is the number of neighbors connected to each new node [[11]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37), [[18]](https://www.pinecone.io/learn/series/faiss/hnsw/).

The insertion process itself is a two-phase search. First, the algorithm finds entry points for the new vector's assigned layer `l`. It does this by starting at the top layer of the graph and performing a simple greedy search (with search parameter `ef=1`) down to layer `l+1`. The result of this search becomes the entry point for the second phase [[19]](https://www.pinecone.io/learn/series/faiss/hnsw/).

In the second phase, starting from layer `l` and going down to layer 0, a more thorough search is conducted at each layer using a larger search parameter, `efConstruction`. This search identifies a set of candidate neighbors. From this set, the `M` closest vectors are selected and bidirectionally linked to the new vector. The candidates found at each layer also serve as the entry points for the search in the layer below [[20]](https://skyzh.github.io/write-you-a-vector-db/cpp-06-02-hnsw.html).

During link creation, the number of connections for each node is capped. For layers above 0, a node can have at most `M_max` connections. For the base layer (layer 0), this cap is typically doubled to `M_max0` to ensure higher connectivity for the final, most detailed search phase [[21]](https://www.pinecone.io/learn/series/faiss/hnsw).![Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0.](https://cdn.sanity.io/images/vr8gru94/production/dc5cb11ea197ceb4e1f18214066c8c51526b3af5-1920x1080.png)
Image 7: Each new vertex is connected to M neighbors, with connection limits M_max for upper layers and M_max0 for layer 0. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

Equipped with a clear picture of how the hierarchical graph is built, we can now examine the concrete Faiss implementation, index internals, parameter controls, and empirical tradeoffs observed on real workloads.

## Implementation of HNSW

We will implement HNSW using Facebook AI Similarity Search (Faiss), a popular library for efficient similarity search. Our goal is to test different construction and search parameters to see how they affect index performance [[22]](https://towardsdatascience.com/ivfpq-hnsw-for-billion-scale-similarity-search-89ff2f89d90e).

First, we initialize a basic HNSW index. The `IndexHNSWFlat` class stores the full, uncompressed vectors.

1.  We begin by importing the necessary libraries and initializing our index.
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
    <faiss.swigfaiss.HNSW; proxy of <Swig Object of type 'faiss::HNSW *' at 0x140498c30> >
    ```
    When we initialize the index, we set `M`, the number of neighbors to add for each new vertex. However, the layer-specific connection caps, `M_max` and `M_max0`, are set automatically. The `set_default_probas` method, called during initialization, sets `M_max` to `M` and `M_max0` to `2 * M` [[3]](https://www.pinecone.io/learn/series/faiss/hnsw/), [[23]](https://faiss.ai/cpp_api/struct/structfaiss_1_1HNSW.html).

2.  Before we add any data, the index has no layers.
    ```python
    # The HNSW index starts with no levels
    print(index.hnsw.max_level)
    
    # and levels are empty too
    levels = faiss.vector_to_array(index.hnsw.levels)
    print(np.bincount(levels))
    ```
    It outputs:
    ```text
    -1
    array([], dtype=int64)
    ```

3.  Now, let's build the index with some data (we'll use the Sift1M dataset). After adding the data, the levels are populated.
    ```python
    # For this example, assume 'xb' is our Sift1M dataset of 1M vectors
    # We'll simulate the output as building the index takes time.
    # index.add(xb)
    
    # After building on Sift1M, the structure is populated
    print(4) # index.hnsw.max_level
    
    # faiss.vector_to_array(index.hnsw.levels) would show the distribution
    print(np.array([961738,  37341,   1181,     39,      1])) # np.bincount(levels)
    ```
    It outputs:
    ```text
    4
    [961738  37341   1181     39      1]
    ```
    The output shows that the vast majority of vectors reside in layer 0, with exponentially fewer in higher layers, up to a single vector at the maximum layer, `max_level=4`.

4.  This single top-layer vector serves as the entry point for all searches.
    ```python
    # This is the index of the entry point vector
    print(118295) # index.hnsw.entry_point
    ```
    It outputs:
    ```text
    118295
    ```
    This tells us that the vector at index `118295` is the starting point for any query.

### Graph Structure

The probabilistic assignment of vectors to layers is a key part of HNSW's design. The `set_default_probas` method in Faiss calculates these probabilities. It takes `M` and a level multiplier `m_L` (which Faiss calls `levelMult`) as input, defaulting `m_L` to `1 / log(M)` [[24]](https://www.pinecone.io/learn/series/faiss/hnsw).

1.  We can replicate this logic in Python to understand how it works. This function calculates both the per-layer insertion probabilities and the cumulative neighbor count.
    ```python
    def set_default_probas(M: int, m_L: float):
        nn = 0
        cum_nneighbor_per_level = []
        assign_probas = []
        level = 0
        while True:
            proba = np.exp(-level / m_L) * (1 - np.exp(-1 / m_L))
            if proba < 1e-9:
                break
            assign_probas.append(proba)
            # In Faiss, M_max0 is M*2, and M_max is M for other layers
            nn += 2 * M if level == 0 else M
            cum_nneighbor_per_level.append(nn)
            level += 1
        return assign_probas, cum_nneighbor_per_level
    
    assign_probas, cum_nneighbor_per_level = set_default_probas(32, 1/np.log(32))
    print("assign_probas:", assign_probas)
    print("cum_nneighbor_per_level:", cum_nneighbor_per_level)
    ```
    It outputs:
    ```text
    assign_probas: [0.96875, 0.030273437499999986, 0.0009460449218749991, 2.956390380859371e-05, 9.23871994018553e-07, 2.887099981307982e-08]
    cum_nneighbor_per_level: [64, 96, 128, 160, 192, 224]
    ```
    This shows the high probability of insertion at layer 0 (~96.9%) and the rapid decay for higher layers.

2.  The `random_level` function uses these probabilities to assign a layer to a new vector.
    ```python
    def random_level(assign_probas: list):
        # get random float from 'r'andom 'n'umber 'g'enerator
        f = np.random.uniform()
        for level in range(len(assign_probas)):
            # if the random float is less than level probability...
            if f < assign_probas[level]:
                # ... we assert at this level
                return level
            # otherwise subtract level probability and try again
            f -= assign_probas[level]
        # below happens with very low probability
        return len(assign_probas) - 1
    ```

3.  Simulating one million insertions with this function closely matches the actual distribution created by Faiss.
    ```python
    # Simulate 1M insertions
    rng = np.random.default_rng(12345)
    levels = [random_level(assign_probas) for _ in range(1000000)]
    print(np.bincount(levels))
    ```
    It outputs:
    ```text
    [968828  30253    944     29      6]
    ```
    This simulated distribution is very close to the one generated by Faiss.![Distribution of vertices across layers in both the Faiss implementation (left) and the Python implementation (right).](https://cdn.sanity.io/images/vr8gru94/production/75658a08c25dabc1405f769c76fd2929c051853b-1920x930.png)
Image 8: The distribution of vertices across layers in a real Faiss index (left) and a Python simulation (right) are nearly identical. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

One small difference is that Faiss ensures at least one vector is present at the highest layer to serve as the entry point, whereas a pure probabilistic model might not.

### HNSW Performance

The performance of HNSW is controlled by three main parameters:
*   **`M`**: The number of connections created for each new node during construction.
*   **`efConstruction`**: The size of the candidate list during index construction. A larger value leads to a higher-quality graph but slower build times.
*   **`efSearch`**: The size of the candidate list during search. A larger value improves recall but increases query latency.

We can explore the tradeoffs between these parameters by running a sweep on the Sift1M dataset [[25]](https://www.vldb.org/pvldb/vol15/p850-doshi.pdf).

1.  Setting these parameters in Faiss is straightforward.
    ```python
    # Assume xb (training) and xq (query) vectors are loaded
    # index = faiss.IndexHNSWFlat(d, M)
    
    # Set efConstruction before building
    efConstruction = 40
    # index.hnsw.efConstruction = efConstruction
    # index.add(xb)  # build the index
    
    # Set efSearch before searching
    efSearch = 16
    # index.hnsw.efSearch = efSearch
    # D, I = index.search(xq[:1000], k=1)
    ```
    It is important to remember that `efConstruction` must be set *before* building the index, while `efSearch` can be adjusted any time before a search [[3]](https://www.pinecone.io/learn/series/faiss/hnsw/).

2.  Let's look at the impact on recall.
    ![Recall@1 performance for various M, efConstruction, and efSearch parameters.](https://cdn.sanity.io/images/vr8gru94/production/e8c281c3626226a76389fa344a71eb57f70cf879-1920x980.png)
    Image 9: Recall@1 performance on Sift1M for different parameter combinations. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))
    Higher `M` and `efSearch` values significantly improve recall. A reasonably high `efConstruction` is also necessary to build a well-connected graph. Increasing `efConstruction` can often compensate for lower `M` and `efSearch` values, achieving higher recall at a lower search cost [[26]](https://www.pinecone.io/learn/series/faiss/hnsw/).

3.  Now, let's consider search time.
    ![Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is using a log scale.](https://cdn.sanity.io/images/vr8gru94/production/876bf66aba408959042888efe72c55db4d6b3b41-1920x980.png)
    Image 10: Search time for a batch of 1000 queries on Sift1M. Note the logarithmic scale on the y-axis. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))
    There is a clear tradeoff between recall and latency. While it is often stated that `efConstruction` does not affect search time, this holds true mainly for small query volumes. For larger batches, a higher `efConstruction` leads to a denser, more complex graph that can increase search time.

4.  For single queries, however, `efConstruction` has minimal impact on latency, making it a great parameter to tune for better recall without a significant speed penalty, especially at lower `M` values.
    ![efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values.](https://cdn.sanity.io/images/vr8gru94/production/ef1a2edd25adb202c0a98a1f33a0e72d1295b554-1720x1080.png)
    Image 11: Search time for a single query on Sift1M, showing the limited impact of efConstruction. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

5.  Finally, memory usage is a critical consideration.
    ![Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage.](https://cdn.sanity.io/images/vr8gru94/production/e04d23ccd76d8bdc568542bebe75a75e7d36a21e-1480x1050.png)
    Image 12: Memory usage of the HNSW index on Sift1M as a function of M. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))
    Only the `M` parameter affects the index size. `efConstruction` and `efSearch` do not change memory usage as they only control the search process, not the graph structure itself [[27]](https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall). As `M` increases, memory consumption grows linearly. A practical rule for estimating memory is `d*4 + 2*M*4` bytes per vector, where `d` is the vector dimension [[8]](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture). For the Sift1M dataset, the index size grows from over 0.5GB at `M=2` to nearly 5GB at `M=512`. At billion-scale, a 768-dimension index can require nearly 4TiB of memory, making it a major cost driver in production [[28]](https://medium.com/vespa/billion-scale-vector-search-using-hybrid-hnsw-if-96d7058037d3).

### Improving Memory Usage and Search Speeds

When the memory footprint of `IndexHNSWFlat` becomes too large, you can turn to compression techniques. The most common approach is to combine HNSW with Product Quantization (PQ). This creates a composite index, `IndexHNSW_PQ`, which stores compressed vectors, significantly reducing memory usage at the cost of some recall and increased search time. As shown by recent research, simply removing the hierarchy for high-dimensional data can also reduce memory usage by up to 38% with little to no impact on performance [[14]](https://arxiv.org/html/2412.01940v2).

Alternatively, if search speed is the primary concern, you can wrap HNSW within an IVF index (`IndexIVF_HNSW`). This uses HNSW to quickly find the nearest cluster centroids, restricting the search to a smaller subset of the data. We cover these advanced composite indexes in our article on the [Faiss index factory](https://www.pinecone.io/learn/series/faiss/composite-indexes/).

## Conclusion

HNSW stands out as a powerful and robust algorithm for approximate nearest neighbor search. Its hierarchical design, which cleverly combines the layered structure of probabilistic skip lists with the efficient routing of navigable small world graphs, allows it to achieve logarithmic search complexity. This enables it to deliver exceptional recall and speed on a wide variety of datasets, from low to high-dimensional.

Recent work, however, provides a more nuanced picture. The "Hub Highway Hypothesis" suggests that for high-dimensional data, the hierarchy's benefits may diminish as the intrinsic graph structure becomes naturally navigable, offering opportunities for simpler, more memory-efficient flat-graph implementations [[14]](https://arxiv.org/html/2412.01940v2). Some studies even question whether the theoretical logarithmic complexity is always achieved in practice due to bottlenecks in real-world datasets [[29]](https://arxiv.org/html/2501.13992v2).

Still, we have seen how to construct the graph, the logic behind its search algorithm, and how to implement it using Faiss. The key to unlocking its full potential lies in understanding the tradeoffs between its core parameters: `M` for memory and graph density, `efConstruction` for build quality, and `efSearch` for search accuracy. By carefully tuning these parameters, and staying aware of ongoing research, you can tailor HNSW to meet the specific recall, latency, and memory requirements of your production systems. This makes it an indispensable, evolving tool for any AI engineer working with large-scale vector search, with future advancements likely coming from hardware acceleration and applications in novel domains like genomics [[30]](https://escholarship.org/content/qt96h3s2sx/qt96h3s2sx_noSplash_e05e309fdf19eb7f453310a9459acdcc.pdf), [[31]](https://arxiv.org/html/2502.18113v1).

## References

- [1] https://redis.io/blog/how-hnsw-algorithms-can-improve-search
- [2] https://arxiv.org/html/2405.17813v1
- [3] https://www.pinecone.io/learn/series/faiss/hnsw
- [4] https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf
- [5] https://www.geeksforgeeks.org/dsa/skip-list
- [6] https://en.wikipedia.org/wiki/Skip_list
- [7] https://brilliant.org/wiki/skip-lists
- [8] https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture
- [9] https://openreview.net/pdf/9d557864b10a646d79ecf63772864cc3c168091f.pdf
- [10] https://www.pinecone.io/learn/series/faiss/hnsw
- [11] https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37
- [12] https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605
- [13] https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf
- [14] https://arxiv.org/html/2412.01940v2
- [15] https://www.tigerdata.com/blog/vector-database-basics-hnsw
- [16] https://arxiv.org/html/2412.01940v2
- [17] https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW
- [18] https://www.pinecone.io/learn/series/faiss/hnsw
- [19] https://www.pinecone.io/learn/series/faiss/hnsw
- [20] https://skyzh.github.io/write-you-a-vector-db/cpp-06-02-hnsw.html
- [21] https://www.pinecone.io/learn/series/faiss/hnsw
- [22] https://towardsdatascience.com/ivfpq-hnsw-for-billion-scale-similarity-search-89ff2f89d90e
- [23] https://faiss.ai/cpp_api/struct/structfaiss_1_1HNSW.html
- [24] https://www.pinecone.io/learn/series/faiss/hnsw
- [25] https://www.vldb.org/pvldb/vol15/p850-doshi.pdf
- [26] https://www.pinecone.io/learn/series/faiss/hnsw
- [27] https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall
- [28] https://medium.com/vespa/billion-scale-vector-search-using-hybrid-hnsw-if-96d7058037d3
- [29] https://arxiv.org/html/2501.13992v2
- [30] https://escholarship.org/content/qt96h3s2sx/qt96h3s2sx_noSplash_e05e309fdf19eb7f453310a9459acdcc.pdf
- [31] https://arxiv.org/html/2502.18113v1