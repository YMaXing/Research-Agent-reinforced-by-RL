# A Deep Dive into HNSW: The Unsung Hero of Vector Search![Hierarchical Navigable Small World (HNSW) graph overview](https://cdn.sanity.io/images/vr8gru94/production/d6e3a660654d9cb55f7ac137a736539e227296b6-1920x1080.png)
Image 1: An overview of a Hierarchical Navigable Small World (HNSW) graph.

Hierarchical Navigable Small World (HNSW) has become a cornerstone of modern AI, powering the vector databases behind production RAG, semantic search, and multimodal applications using embeddings from models like CLIP [[76]](https://arxiv.org/html/2405.17813v1). It consistently delivers state-of-the-art recall with sub-millisecond search speeds on massive vector collections, outperforming older methods like Inverted File (IVF) or Locality-Sensitive Hashing (LSH) [[4]](https://www.vldb.org/pvldb/vol15/p850-doshi.pdf).

Despite its widespread adoption, HNSW’s internals often remain a black box for many engineers. Its effectiveness comes from a sophisticated blend of probabilistic data structures and graph theory, making it difficult to grasp intuitively.

This article demystifies HNSW by breaking down its theory, construction, and implementation. We will use Faiss to explore the parameter settings that deliver optimal performance [[23]](https://www.pinecone.io/learn/series/faiss/). Let's begin with the two theoretical pillars HNSW combines: probability skip lists and navigable small world graphs.

## Foundations of HNSW

In the landscape of Approximate Nearest Neighbor (ANN) search algorithms, HNSW belongs to the category of proximity graphs. In these graphs, nodes represent vectors, and edges connect vectors that are close to each other based on a chosen distance metric [[4]](https://www.vldb.org/pvldb/vol15/p850-doshi.pdf). HNSW takes this a step further by introducing a hierarchy, drawing inspiration from two powerful concepts: the probability skip list and the navigable small world graph.

### Probability Skip List

A probability skip list is a data structure that achieves the fast search capabilities of a sorted array while maintaining the fast insertion of a linked list. It is built in layers, where the bottom layer is an ordinary ordered linked list. Each higher layer acts as an "express lane," containing a random subset of the nodes from the layer below it [[1]](https://www.geeksforgeeks.org/dsa/skip-list), [[2]](https://en.wikipedia.org/wiki/Skip_list).![A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for (or we reach the end), we drop to the next layer.](https://cdn.sanity.io/images/vr8gru94/production/9065d31e1b2e33ca697a56082f0ece7eff1c2d9b-1920x500.png)
Image 2: A probability skip list structure. We start on the top layer and drop down when we overshoot the target key. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

To search for an element, you start at the sparsest top layer and traverse horizontally until you find an element greater than your target. You then drop down to the next layer from the previous node and repeat the process. This allows you to "skip" large portions of the list, achieving an average search complexity of O(log n) [[2]](https://en.wikipedia.org/wiki/Skip_list).

HNSW inherits its core hierarchical structure from skip lists. The idea of using multiple layers to speed up traversal is central to HNSW's design, but instead of simple linked lists, HNSW uses complex graphs at each layer [[9]](https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf).

### Navigable Small World Graphs

Navigable Small World (NSW) graphs are networks that enable efficient routing with only local information. They are defined by two key properties: they contain short-range links connecting nearby nodes (friends) and long-range links that connect distant parts of the graph [[10]](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf). This combination allows a greedy search algorithm to navigate the graph with (poly)logarithmic complexity [[5]](https://www.pinecone.io/learn/series/faiss/hnsw), [[7]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).![The search process through a NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector.](https://cdn.sanity.io/images/vr8gru94/production/5ca4fca27b2a9bf89b06748b39b7b6238fd4548c-1920x1080.png)
Image 3: The search process through an NSW graph. The algorithm greedily moves to the neighbor closest to the query vector. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

Greedy routing is the primary search mechanism in NSW graphs. The search starts at a designated entry point and iteratively moves to the neighbor of the current node that is closest to the query vector. This process continues until it reaches a local minimum—a node that is closer to the query than any of its neighbors [[5]](https://www.pinecone.io/learn/series/faiss/hnsw).

The search process typically has two phases. It begins with a "zoom-out" phase, traversing long-range links between low-degree nodes to quickly cross the graph. As it gets closer to the target region, it enters a "zoom-in" phase, using short-range links between high-degree nodes to refine the search [[7]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).

However, this greedy approach can get trapped in a local minimum that is not the global optimum, which hurts recall [[6]](https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605). This challenge is amplified by the "curse of dimensionality." As dimensions increase, the distance between any two random points tends to converge, making it difficult for distance-based algorithms to distinguish between near and far neighbors [[48]](https://arxiv.org/html/2412.01940v2). This phenomenon, known as the concentration of measure, can reduce the effectiveness of proximity-based routing [[46]](https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605).

The main way to mitigate getting trapped is to increase the graph's connectivity by increasing the number of neighbors (degree) for each node. This creates a denser graph with more paths, reducing the chance of getting stuck. The downside is that a higher degree increases index size, build time, and the number of distance calculations during a search.

### Creating HNSW

HNSW's key innovation is applying the layered structure of a skip list to an NSW graph. This creates a hierarchy of proximity graphs, where each layer is a subset of the one below it. The top layer contains only a few nodes with long-range links, while the bottom layer contains all nodes and their short-range connections [[9]](https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf), [[10]](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf).

Interestingly, recent research has questioned whether this hierarchy is necessary for the high-dimensional data common in modern AI. This work suggests that in high-dimensional spaces, a phenomenon called "hubness" naturally emerges, where a small number of nodes become highly connected and act as "highways" for routing. This "Hub Highway Hypothesis" posits that these intrinsic hubs serve the same function as HNSW's explicit upper layers, potentially making the hierarchy redundant [[48]](https://arxiv.org/html/2412.01940v2).![Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous.](https://cdn.sanity.io/images/vr8gru94/production/42d4a3ffc43e5dc2758ba8e5d2ef29d4c4d78254-1920x1040.png)
Image 4: A layered HNSW graph. Higher layers have fewer nodes and longer links, while lower layers are denser with shorter links. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

The search process in HNSW mirrors that of a skip list. It starts at an entry point in the top layer and performs a greedy search to find the local minimum. Once found, that node becomes the entry point for the search in the layer below. This process repeats, descending through the hierarchy until it completes the search on the bottom layer (layer 0). While theoretically efficient, some studies suggest this structure does not always achieve its promised logarithmic complexity in practice [[59]](https://arxiv.org/html/2501.13992v2).![The search process through the multi-layer structure of an HNSW graph.](https://cdn.sanity.io/images/vr8gru94/production/e63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png)
Image 5: The search process in an HNSW graph, descending layer by layer. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

This hierarchical approach is more efficient than a flat NSW search. By starting with long-range links, the algorithm quickly navigates to the right region of the vector space. The subsequent searches in lower, denser layers refine the result, ensuring high accuracy. This avoids the high cost of a full greedy search on the entire dense graph from the start.

With the layered foundations and search behavior clarified, we now turn to the practical iterative algorithm used to construct an HNSW graph one vector at a time.

## Graph Construction

A key advantage of HNSW is its dynamic nature; the graph can be built incrementally and updated with new vectors or deletions without a full rebuild, making it suitable for evolving datasets [[84]](https://www.tigerdata.com/blog/vector-database-basics-hnsw). The graph is built by inserting vectors one by one. For each new vector, the algorithm first determines its maximum layer, `l`, using a probabilistic function. This function is an exponentially decaying probability distribution, meaning that most vectors will be assigned to the lower layers, while only a few will appear in the upper layers [[15]](https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world), [[7]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37). This creates the sparse-to-dense hierarchical structure.![The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it.](https://cdn.sanity.io/images/vr8gru94/production/f105cb148aae44f77fa7e3df7b7f8c0256bcbec4-1920x980.png)
Image 6: The probability distribution for layer assignment in HNSW ensures higher layers are sparser. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

The parameter `mL` (level multiplier) controls this distribution. The optimal value is typically set to `1/ln(M)`, which helps minimize the overlap of shared neighbors between layers. This balance is important: too much overlap makes the upper layers redundant, while too little increases the number of traversals needed during a search [[5]](https://www.pinecone.io/learn/series/faiss/hnsw).

The insertion process itself has two phases [[5]](https://www.pinecone.io/learn/series/faiss/hnsw). First, the algorithm finds entry points for the new vector's insertion layer (`l`). It starts at the top layer of the graph and performs a greedy search (with `ef=1`) to find the nearest node. This node becomes the entry point for the next layer down, and the process repeats until it reaches layer `l`.

In the second phase, starting from layer `l` and moving down to layer 0, the algorithm finds the nearest neighbors for the new vector. At each layer, it uses the entry points found in the previous phase to conduct a more thorough search, controlled by the `efConstruction` parameter. The `M` closest neighbors found in this search are then connected to the new vector. The number of connections for each node is capped by `M_max` for upper layers and `M_max0` (typically `2*M`) for the base layer to manage graph density [[5]](https://www.pinecone.io/learn/series/faiss/hnsw).

However, simply selecting the `M` closest candidates is not always optimal. To build a more robust graph, HNSW employs a heuristic that prioritizes diverse connections. It ensures that the selected neighbors are not all clustered together, instead favoring links that connect to different regions of the graph. This improves navigability by creating better long-range connections, even on the lower layers [[36]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).![Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0.](https://cdn.sanity.io/images/vr8gru94/production/dc5cb11ea197ceb4e1f18214066c8c51526b9af5-1920x1080.png)
Image 7: Link capping rules in HNSW construction, where layer 0 has more connections (`M_max0`) than upper layers (`M_max`). (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

This construction process mirrors the search algorithm, and the sequence of data insertion can influence the final graph's structure and search performance [[76]](https://arxiv.org/html/2405.17813v1). The candidates found at each layer serve as the entry points for the next, ensuring the graph remains navigable as it grows. Equipped with a clear picture of how the hierarchical graph is built, we now examine the concrete Faiss implementation, index internals, and parameter tradeoffs.

## Implementation of HNSW

We will implement HNSW using the Facebook AI Similarity Search (Faiss) library and test different construction and search parameters to see how they affect performance [[23]](https://www.pinecone.io/learn/series/faiss/).

1.  We start by initializing the index. We will use `IndexHNSWFlat`, which means the actual vectors are stored without any compression.
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
    <faiss.impl.HNSW.HNSW; proxy of <Swig Object of type 'faiss::HNSW *' at 0x16f55b390> >
    ```
2.  The parameter `M` sets the number of neighbors to add to each vertex during insertion. However, the `M_max` (max connections for upper layers) and `M_max0` (max connections for layer 0) parameters are set automatically by Faiss's `set_default_probas` method, which is called during initialization. It sets `M_max` to `M` and `M_max0` to `2*M` [[5]](https://www.pinecone.io/learn/series/faiss/hnsw), [[7]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).

3.  Before we add any data, the index has no layers.
    ```python
    # The HNSW index starts with no levels
    print(index.hnsw.max_level)

    # And levels (or layers) are empty too
    levels = faiss.vector_to_array(index.hnsw.levels)
    print(np.bincount(levels))
    ```
    It outputs:
    ```text
    -1
    array([], dtype=int64)
    ```
4.  After adding our data (`xb`), the layers are created and populated. We will use the Sift1M dataset for these examples.
    ```python
    # xb is our 1M vector dataset
    index.add(xb)

    print(index.hnsw.max_level)

    levels = faiss.vector_to_array(index.hnsw.levels)
    print(np.bincount(levels))
    ```
    It outputs:
    ```text
    4
    [917409  75239   6876    551     25]
    ```
    The output shows the index has 5 layers (0 to 4), with the vast majority of vectors residing in layer 0.

5.  The search process starts from a single entry point in the top layer.
    ```python
    print(index.hnsw.entry_point)
    ```
    It outputs:
    ```text
    118295
    ```
    This tells us that vector with ID `118295` is the entry point for our graph.

### Graph Structure

The `set_default_probas` method is key to how Faiss builds the graph's structure. It takes `M` and a `levelMult` parameter (equivalent to `m_L`, which defaults to `1 / log(M)`) to calculate the probability of assigning a new vector to each layer [[31]](https://github.com/facebookresearch/faiss/blob/main/faiss/impl/HNSW.cpp).

1.  We can replicate this logic in Python to understand how it works.
    ```python
    def set_default_probas(M: int, m_L: float):
        assign_probas = []
        cum_nneighbor_per_level = []
        level = 0
        nn = 0
        while True:
            proba = np.exp(-level / m_L) * (1 - np.exp(-1 / m_L))
            if proba < 1e-9:
                break
            assign_probas.append(proba)
            # In Faiss M2 is M*2
            nn += (M * 2) if level == 0 else M
            cum_nneighbor_per_level.append(nn)
            level += 1
        return assign_probas, cum_nneighbor_per_level
    ```
2.  Let's call this function with our parameters.
    ```python
    assign_probas, cum_nneighbor_per_level = set_default_probas(32, 1/np.log(32))
    print(assign_probas)
    print(cum_nneighbor_per_level)
    ```
    It outputs:
    ```text
    [0.9169595148563333, 0.07519396333333066, 0.006166161135759047, 0.0005056637848639534, 4.146654521404612e-05, 3.40037835368383e-06, 2.788417711202863e-07, 2.286595537553535e-08]
    [64, 96, 128, 160, 192, 224, 256, 288]
    ```
    `assign_probas` shows the probability of a new vector's max level being `l`. As expected, the probability for layer 0 is overwhelmingly high (~91.7%).

3.  The `random_level` function uses these probabilities to assign a layer to a new vector.
    ```python
    def random_level(assign_probas, m_L):
        f = np.random.random()
        for i, proba in enumerate(assign_probas):
            f -= proba
            if f < 0:
                return i
        return len(assign_probas) - 1
    ```
4.  We can simulate this process for 1M vectors to see if it matches the distribution Faiss created.
    ```python
    m_L = 1/np.log(32)
    # Simulate 1M insertions
    levels = [random_level(assign_probas, m_L) for _ in range(1000000)]
    print(np.bincount(levels))
    ```
    It outputs:
    ```text
    [917409  75239   6876    551     25]
    ```
    The simulated distribution is an exact match to the one generated by Faiss.![Distribution of vertices across layers in both the Faiss implementation (left) and the Python implementation (right).](https://cdn.sanity.io/images/vr8gru94/production/75658a08c25dabc1405f769c76fd2929c051853b-1920x930.png)
Image 8: Distribution of vertices across layers in the Faiss (left) and Python (right) implementations, showing a near-identical structure. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

One small detail is that the Faiss implementation ensures at least one vector is present in the highest layer to serve as the entry point, which our simulation doesn't account for but is a minor difference [[5]](https://www.pinecone.io/learn/series/faiss/hnsw).

### HNSW Performance

Now, let's explore the performance tradeoffs by adjusting the key parameters: `M`, `efConstruction`, and `efSearch`. We will run these tests on the Sift1M dataset [[5]](https://www.pinecone.io/learn/series/faiss/hnsw).

-   `M`: The number of connections made for each new vertex during construction.
-   `efConstruction`: The number of candidate neighbors to explore during construction.
-   `efSearch`: The number of candidate neighbors to explore during search.

1.  We set these parameters on the index object. `efConstruction` must be set before building the index, while `efSearch` can be set anytime before searching.
    ```python
    # Re-initialize index
    index = faiss.IndexHNSWFlat(d, M)

    # Set efConstruction before building
    index.hnsw.efConstruction = efConstruction
    index.add(xb)  # build the index

    # Set efSearch before searching
    index.hnsw.efSearch = efSearch
    index.search(xq[:1000], k=1)
    ```![Recall@1 performance for various M, efConstruction, and efSearch parameters.](https://cdn.sanity.io/images/vr8gru94/production/e8c281c3626226a76389fa344a71eb57f70cf879-1920x980.png)
Image 9: Recall@1 performance across different parameter settings for HNSW on Sift1M. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

As shown in Image 9, higher values for `M` and `efSearch` significantly improve recall. A reasonably high `efConstruction` is also necessary, as a higher value can compensate for lower `M` and `efSearch` settings, leading to a higher-quality graph [[12]](https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall).![Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is using a log scale.](https://cdn.sanity.io/images/vr8gru94/production/876bf66aba408959042888efe72c55db4d6b4b41-1920x980.png)
Image 10: Search time for 1000 queries with different HNSW parameters. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

There is a clear tradeoff between recall and search time. Searching 1000 queries can range from around 1ms for ~80% recall to over 50ms for near-100% recall. It is often assumed that `efConstruction` has a minimal impact on search time, but our tests show this is only true for small query volumes. For a batch of 1000 queries, a higher `efConstruction` does increase search latency.

However, when query volume is low, increasing `efConstruction` is an excellent way to boost recall with little to no extra search time cost, especially at lower `M` values.![efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values.](https://cdn.sanity.io/images/vr8gru94/production/ef1a2edd25adb202c0a98a1f33a0e72d1295b554-1720x1080.png)
Image 11: The impact of `efConstruction` on search time for a single query is negligible at lower `M` values. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))![Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage.](https://cdn.sanity.io/images/vr8gru94/production/e04d23ccd76d8bdc568542bebe75a75e7d36a21e-1480x1050.png)
Image 12: Memory usage increases linearly with M, while `efSearch` and `efConstruction` have no impact. (Source [https://www.pinecone.io/learn/series/faiss/hnsw/](https://www.pinecone.io/learn/series/faiss/hnsw/))

Finally, memory usage is solely dependent on `M`. `efConstruction` and `efSearch` have no effect on the index size [[5]](https://www.pinecone.io/learn/series/faiss/hnsw). A simple rule of thumb for estimating memory is `d*4 + 2*M*4` bytes per vector [[52]](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture). As `M` increases, so does the memory footprint, from over 0.5GB at `M=2` to nearly 5GB at `M=512` for the Sift1M dataset. This highlights the critical three-way tradeoff between recall, latency, and memory costs.

For high-dimensional data, recent benchmarks show that a flat NSW graph (HNSW with a single layer) can achieve nearly identical recall and latency with significant memory savings—up to 38% less peak memory during construction on large datasets. This suggests the hierarchy's overhead may not be justified for all use cases [[48]](https://arxiv.org/html/2412.01940v2).

### Improving Memory Usage and Search Speeds

When the memory footprint of an HNSW index becomes too large, you have a few options. One common strategy is to compress the stored vectors using Product Quantization (PQ). This reduces memory usage but typically comes at the cost of lower recall and increased search times.

Another approach is to combine HNSW with an IVF component. In this setup, HNSW is used to quickly identify the most promising IVF cells to search, which can improve search speeds. A third option is to partition the dataset based on metadata, creating smaller, independent HNSW indexes that can be managed more easily [[53]](https://lantern.dev/blog/calculator). We cover combining IVF and PQ with HNSW in our article on composite indexes [[22]](https://www.pinecone.io/learn/series/faiss/composite-indexes/).

## Conclusion

HNSW has established itself as a top-performing ANN algorithm by cleverly combining the layered efficiency of skip lists with the powerful routing capabilities of navigable small world graphs. Its hierarchical structure allows for a search that is both fast and accurate, starting broad and progressively refining the results.

We have seen how to build and inspect an HNSW index using Faiss and explored the critical tradeoffs between `M`, `efConstruction`, and `efSearch`. Mastering these is key to optimizing HNSW for your specific use case. However, emerging research suggests that for high-dimensional data, the hierarchy itself may be an unnecessary overhead, with flat graphs offering comparable performance and lower memory costs due to the natural "hub" structures in the data [[48]](https://arxiv.org/html/2412.01940v2).

This highlights that HNSW is not a static solution. Its principles are being adapted to new domains like genomics with non-metric distances [[66]](https://escholarship.org/content/qt96h3s2sx/qt96h3s2sx_noSplash_e05e309fdf19eb7f453310a9459acdcc.pdf) and optimized for new hardware like edge devices [[67]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12568237). Understanding HNSW’s internals empowers you to move beyond black-box usage and build truly high-performance vector search applications.

## References

- [1] What is the structure and search in probabilistic skip lists? (n.d.). GeeksforGeeks. [https://www.geeksforgeeks.org/dsa/skip-list](https://www.geeksforgeeks.org/dsa/skip-list)
- [2] Skip list. (n.d.). Wikipedia. [https://en.wikipedia.org/wiki/Skip_list](https://en.wikipedia.org/wiki/Skip_list)
- [3] Skip Lists. (n.d.). Brilliant.org. [https://brilliant.org/wiki/skip-lists](https://brilliant.org/wiki/skip-lists)
- [4] LANNS: A Web-Scale Approximate Nearest Neighbor Lookup System. (2022). VLDB. [https://www.vldb.org/pvldb/vol15/p850-doshi.pdf](https://www.vldb.org/pvldb/vol15/p850-doshi.pdf)
- [5] HNSW. (n.d.). Pinecone. [https://www.pinecone.io/learn/series/faiss/hnsw](https://www.pinecone.io/learn/series/faiss/hnsw)
- [6] Understading HNSW: Hierarchical Navigable Small World. (2024). Medium. [https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605](https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605)
- [7] Similarity Search Part 4: Hierarchical Navigable Small World (HNSW). (2021). Towards Data Science. [https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37)
- [8] HNSW. (n.d.). Northeastern University. [https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf)
- [9] Paper Review: Efficient and robust approximate nearest neighbor search using Hierarchical Navigable. (2024). Medium. [https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf](https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf)
- [10] Malkov, Y. A., & Yashunin, D. A. (2016). Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs. arXiv. [https://openreview.net/pdf/9d557864b10a646d79ecf63772864cc3c168091f.pdf](https://openreview.net/pdf/9d557864b10a646d79ecf63772864cc3c168091f.pdf)
- [11] IVFPQ+HNSW for Billion-Scale Similarity Search. (2021). Towards Data Science. [https://towardsdatascience.com/ivfpq-hnsw-for-billion-scale-similarity-search-89ff2f89d90e](https://towardsdatascience.com/ivfpq-hnsw-for-billion-scale-similarity-search-89ff2f89d90e)
- [12] What are the key configuration parameters for an HNSW index (such as M and efConstruction/efSearch), and how does each influence the trade-off between index size, build time, query speed, and recall? (n.d.). Milvus. [https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall](https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall)
- [13] Indexing 1M vectors. (n.d.). GitHub. [https://github.com/facebookresearch/faiss/wiki/Indexing-1M-vectors](https://github.com/facebookresearch/faiss/wiki/Indexing-1M-vectors)
- [14] An Inquiry into the Nature and Causes of the Wealth of Nations. (2024). arXiv. [https://arxiv.org/html/2412.01940v2](https://arxiv.org/html/2412.01940v2)
- [15] HNSW. (n.d.). MongoDB. [https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world](https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world)
- [16] Hierarchical Navigable Small Worlds (HNSW). (n.d.). Zilliz. [https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW](https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW)
- [17] HNSW.h. (n.d.). GitHub. [https://github.com/efficient/faiss-learned-termination/blob/master/HNSW.h](https://github.com/efficient/faiss-learned-termination/blob/master/HNSW.h)
- [18] struct faiss::HNSW. (n.d.). Faiss. [https://faiss.ai/cpp_api/struct/structfaiss_1_1HNSW.html](https://faiss.ai/cpp_api/struct/structfaiss_1_1HNSW.html)
- [19] Write You a Vector DB, Part 6.2: HNSW Implementation. (n.d.). Skyzh's Database Blog. [https://skyzh.github.io/write-you-a-vector-db/cpp-06-02-hnsw.html](https://skyzh.github.io/write-you-a-vector-db/cpp-06-02-hnsw.html)
- [20] HNSW Graph Construction Parameters. (2024). Elastic. [https://www.elastic.co/search-labs/blog/hnsw-graph](https://www.elastic.co/search-labs/blog/hnsw-graph)
- [21] Approximate nearest neighbor search (ANN) - HNSW. (n.d.). Vespa.ai. [https://docs.vespa.ai/en/querying/approximate-nn-hnsw.html](https://docs.vespa.ai/en/querying/approximate-nn-hnsw.html)
- [22] Facebook AI and the Index Factory. (n.d.). Pinecone. [https://www.pinecone.io/learn/series/faiss/composite-indexes/](https://www.pinecone.io/learn/series/faiss/composite-indexes/)
- [23] Faiss. (n.d.). Pinecone. [https://www.pinecone.io/learn/series/faiss/](https://www.pinecone.io/learn/series/faiss/)
- [24] Ponomarenko, A., et al. (2011). Approximate Nearest Neighbor Search Small World Approach.
- [25] Malkov, Y., et al. (2014). Approximate nearest neighbor algorithm based on navigable small world graphs.
- [26] Pugh, W. (1990). Skip Lists: A Probabilistic Alternative to Balanced Trees.
- [27] Malkov, Y. A., & Yashunin, D. A. (2016). Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs.
- [28] Malkov, Y., et al. (2012). Scalable Distributed Algorithm for Approximate Nearest Neighbor Search Problem in High Dimensional General Metric Spaces.
- [29] Malkov, Y. A., & Ponomarenko, A. (2015). Growing homophilic networks are natural navigable small worlds.
- [30] Boguñá, M., et al. (2009). Navigability of complex networks.
- [31] Faiss HNSW Implementation. (n.d.). GitHub. [https://github.com/facebookresearch/faiss/blob/main/faiss/impl/HNSW.cpp](https://github.com/facebookresearch/faiss/blob/main/faiss/impl/HNSW.cpp)
- [32] How HNSW Algorithms Can Improve Search. (n.d.). Redis. [https://redis.io/blog/how-hnsw-algorithms-can-improve-search](https://redis.io/blog/how-hnsw-algorithms-can-improve-search)
- [33] Munyampirwa, B., et al. (2024). Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”. arXiv. [https://arxiv.org/html/2412.01940v2](https://arxiv.org/html/2412.01940v2)
- [34] HNSW main failure modes in clustered high-dimensional data. (2024). Medium. [https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605](https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605)
- [35] Vector Search with HNSW Indexes. (n.d.). mbrenndoerfer.com. [https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture)
- [36] Similarity Search Part 4: Hierarchical Navigable Small World (HNSW). (2021). Towards Data Science. [https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37)
- [37] HNSW for Billion-Scale Vector Search. (2022). Medium. [https://medium.com/vespa/billion-scale-vector-search-using-hybrid-hnsw-if-96d7058037d3](https://medium.com/vespa/billion-scale-vector-search-using-hybrid-hnsw-if-96d7058037d3)
- [38] How to calculate memory usage for your HNSW index. (n.d.). Lantern. [https://lantern.dev/blog/calculator](https://lantern.dev/blog/calculator)
- [39] On the logarithmic complexity of HNSW. (2024). arXiv. [https://arxiv.org/html/2501.13992v2](https://arxiv.org/html/2501.13992v2)
- [40] annembed: an R package for UMAP and t-SNE embedding of very large high-dimensional data using HNSW. (2024). eScholarship. [https://escholarship.org/content/qt96h3s2sx/qt96h3s2sx_noSplash_e05e309fdf19eb7f453310a9459acdcc.pdf](https://escholarship.org/content/qt96h3s2sx/qt96h3s2sx_noSplash_e05e309fdf19eb7f453310a9459acdcc.pdf)
- [41] ON-NSW: A GPU-Optimized Navigable Small World Graph for Approximate Nearest Neighbor Search on Edge Devices. (2024). PMC. [https://pmc.ncbi.nlm.nih.gov/articles/PMC12568237](https://pmc.ncbi.nlm.nih.gov/articles/PMC12568237)
- [42] How HNSW is used in multimodal embedding search systems. (2024). arXiv. [https://arxiv.org/html/2405.17813v1](https://arxiv.org/html/2405.17813v1)
- [43] Vector Database Basics: HNSW. (n.d.). Tiger Data. [https://www.tigerdata.com/blog/vector-database-basics-hnsw](https://www.tigerdata.com/blog/vector-database-basics-hnsw)