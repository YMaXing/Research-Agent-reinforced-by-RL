# A Deep Dive into HNSW: The Unsung Hero of Vector Search![Hierarchical Navigable Small World (HNSW) graph overview](https://cdn.sanity.io/images/vr8gru94/production/d6e3a660654d9cb55f7ac137a736539e227296b6-1920x1080.png)
Image 1: An overview of a Hierarchical Navigable Small World (HNSW) graph. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

Hierarchical Navigable Small World (HNSW) has become a cornerstone of modern AI, powering the vector databases behind production Retrieval-Augmented Generation (RAG) and multimodal applications using embeddings from models like CLIP (Contrastive Language–Image Pre-training) [[2]](https://arxiv.org/html/2405.17813v1). It consistently delivers state-of-the-art recall with sub-millisecond search speeds on massive vector collections, outperforming older methods like Inverted File (IVF) or Locality-Sensitive Hashing (LSH) [[1]](https://www.vldb.org/pvldb/vol15/p850-doshi.pdf).

Despite its widespread adoption, HNSW’s internals often remain a black box. Its effectiveness comes from a sophisticated blend of probabilistic data structures and graph theory, making it difficult to grasp intuitively.

This article demystifies HNSW's theory, construction, and implementation. Using Faiss, we will explore the parameter settings that deliver optimal performance [[3]](https://www.pinecone.io/learn/series/faiss/). We will begin by examining the two core concepts HNSW combines: probability skip lists and navigable small world graphs.

## Foundations of HNSW

In the landscape of Approximate Nearest Neighbor (ANN) search algorithms, HNSW belongs to the category of proximity graphs. In these graphs, nodes represent vectors, and edges connect vectors that are close to each other based on a chosen distance metric [[1]](https://www.vldb.org/pvldb/vol15/p850-doshi.pdf). HNSW takes this a step further by introducing a hierarchy, drawing inspiration from two powerful concepts: the probability skip list and the navigable small world graph.

### Probability Skip List

A probability skip list is a data structure that achieves the fast search capabilities of a sorted array while maintaining the fast insertion of a linked list. It is built in layers, where the bottom layer is an ordinary ordered linked list. Each higher layer acts as an "express lane," containing a random subset of the nodes from the layer below it [[4]](https://www.geeksforgeeks.org/dsa/skip-list), [[5]](https://en.wikipedia.org/wiki/Skip_list). The probability `p` (typically 0.25 or 0.5) determines if a node from layer `i` also appears in layer `i+1`. On average, each element appears in `1 / (1 - p)` lists, ensuring that higher layers are progressively sparser [[10]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).![A probability skip list structure. We start on the top layer. If our current key is greater than the key we are searching for (or we reach the end), we drop to the next layer.](https://cdn.sanity.io/images/vr8gru94/production/9065d31e1b2e33ca697a56082f0ece7eff1c2d9b-1920x500.png)
Image 2: A probability skip list structure. We start on the top layer and drop down when we overshoot the target key. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

To search for an element, you start at the sparsest top layer and traverse horizontally until you find an element greater than your target. You then drop down to the next layer from the previous node and repeat the process. This allows you to "skip" large portions of the list, achieving an average search and insertion complexity of O(log n) [[5]](https://en.wikipedia.org/wiki/Skip_list), [[22]](https://brilliant.org/wiki/skip-lists).

HNSW inherits its core hierarchical structure from skip lists. The idea of using multiple layers to speed up traversal is central to HNSW's design, but instead of simple linked lists, HNSW uses complex graphs at each layer [[7]](https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf).

### Navigable Small World Graphs

Navigable Small World (NSW) graphs are networks that enable efficient routing with only local information. They are defined by two key properties: they contain short-range links connecting nearby nodes (friends) and long-range links that connect distant parts of the graph [[8]](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf). This combination allows a greedy search algorithm to navigate the graph with (poly)logarithmic complexity [[6]](https://www.pinecone.io/learn/series/faiss/hnsw/), [[10]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).

The NSW graph is constructed by inserting points sequentially and connecting each new node to its `M` nearest neighbors among the existing nodes. The long-range links, which are crucial for efficient navigation, are often formed during the early stages of construction. These initial connections act as bridges between what will later become network hubs, allowing the search to quickly traverse different regions of the graph [[10]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).![The search process through a NSW graph. Starting at a pre-defined entry point, the algorithm greedily traverses to connected vertices that are nearer to the query vector.](https://cdn.sanity.io/images/vr8gru94/production/5ca4fca27b2a9bf89b06748b39b7b6238fd4548c-1920x1080.png)
Image 3: The search process through an NSW graph. The algorithm greedily moves to the neighbor closest to the query vector. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

Greedy routing is the primary search mechanism in NSW graphs. The search starts at a designated entry point and iteratively moves to the neighbor of the current node that is closest to the query vector. This process continues until it reaches a local minimum. A local minimum is a node that is closer to the query than any of its neighbors [[6]](https://www.pinecone.io/learn/series/faiss/hnsw/).

The search process typically has two phases. It begins with a "zoom-out" phase, traversing long-range links between low-degree nodes to quickly cross the graph. As it gets closer to the target region, it enters a "zoom-in" phase, using short-range links between high-degree nodes to refine the search [[10]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).

However, this greedy approach can get trapped in a local minimum that is not the global optimum, which hurts recall [[9]](https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605). This risk of early stopping highlights a fundamental tradeoff in NSW graphs: connectivity versus performance. To improve recall, one can increase the average degree (number of connections) of each vertex. A denser graph provides more potential paths, reducing the likelihood of the greedy search getting trapped. However, this increased connectivity comes at a cost. A higher average degree increases the memory footprint, lengthens construction time, and adds to the number of distance calculations at each step, which can slow down search latency. Tuning an NSW-based system involves finding the right balance between graph density for high recall and sparsity for speed and low memory usage [[6]](https://www.pinecone.io/learn/series/faiss/hnsw/).

This challenge is also amplified by the "curse of dimensionality." As dimensions increase, the distance between any two random points tends to converge, making it difficult for distance-based algorithms to distinguish between near and far neighbors [[11]](https://arxiv.org/html/2412.01940v2). This phenomenon, known as the concentration of measure, can reduce the effectiveness of proximity-based routing [[9]](https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605).

### Creating HNSW

HNSW's key innovation is applying the layered structure of a skip list to an NSW graph. This creates a hierarchy of proximity graphs, where each layer is a subset of the one below it. The top layer contains only a few nodes with long-range links, while the bottom layer contains all nodes and their short-range connections [[7]](https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf), [[8]](https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf).

Interestingly, recent research has questioned whether this hierarchy is necessary for the high-dimensional data common in modern AI. This work suggests that in high-dimensional spaces, a phenomenon called "hubness" naturally emerges, where a small number of nodes become highly connected and act as "highways" for routing. This "Hub Highway Hypothesis" posits that these intrinsic hubs serve the same function as HNSW's explicit upper layers, potentially making the hierarchy redundant [[11]](https://arxiv.org/html/2412.01940v2).![Layered graph of HNSW. The top layer is our entry point and contains only the longest links. As we move down the layers, the link lengths become shorter and more numerous.](https://cdn.sanity.io/images/vr8gru94/production/42d4a3ffc43e5dc2758ba8e5d2ef29d4c4d78254-1920x1040.png)
Image 4: A layered HNSW graph. Higher layers have fewer nodes and longer links, while lower layers are denser with shorter links. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

The search process in HNSW mirrors that of a skip list. It starts at an entry point in the top layer and performs a greedy search to find the local minimum. Once found, that node becomes the entry point for the search in the layer below. This process repeats, descending through the hierarchy until it completes the search on the bottom layer (layer 0). The original HNSW paper claims this layered approach achieves an overall search complexity of O(log n) [[10]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37). While theoretically efficient, some studies suggest this structure does not always achieve its promised logarithmic complexity in practice [[12]](https://arxiv.org/html/2501.13992v2).![The search process through the multi-layer structure of an HNSW graph.](https://cdn.sanity.io/images/vr8gru94/production/e63ca5c638bc3cd61cc1cd2ab33b101d82170426-1920x1080.png)
Image 5: The search process in an HNSW graph, descending layer by layer. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

This hierarchical approach is more efficient than a flat NSW search. By starting with long-range links, the algorithm quickly navigates to the right region of the vector space. The subsequent searches in lower, denser layers refine the result, ensuring high accuracy. To improve search quality, instead of finding only one nearest neighbor at each layer, HNSW can find the `efSearch` closest neighbors and use each of them as an entry point for the next layer down [[10]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37). This avoids the high cost of a full greedy search on the entire dense graph from the start.

With the layered foundations and search behavior clarified, we now turn to the practical iterative algorithm used to construct an HNSW graph one vector at a time.

## Graph Construction

A key advantage of HNSW is its dynamic nature; the graph can be built incrementally and updated with new vectors or deletions without a full rebuild, making it suitable for evolving datasets [[14]](https://www.tigerdata.com/blog/vector-database-basics-hnsw). The graph is built by inserting vectors one by one. For each new vector, the algorithm first determines its maximum layer, `l`, using a probabilistic function. This function is an exponentially decaying probability distribution, meaning that most vectors will be assigned to the lower layers, while only a few will appear in the upper layers [[13]](https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world), [[10]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37). This creates the sparse-to-dense hierarchical structure.![The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it.](https://cdn.sanity.io/images/vr8gru94/production/f105cb148aae44f77fa7e3df7b7f8c0256bcbec4-1920x980.png)
Image 6: The probability distribution for layer assignment in HNSW ensures higher layers are sparser. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

The parameter `mL` (level multiplier) controls this distribution. The optimal value is typically set to `1/ln(M)`, which helps minimize the overlap of shared neighbors between layers. This balance is important: too much overlap makes the upper layers redundant, while too little increases the number of traversals needed during a search [[6]](https://www.pinecone.io/learn/series/faiss/hnsw/).

The insertion process involves two phases [[6]](https://www.pinecone.io/learn/series/faiss/hnsw/). First, the algorithm descends from the top layer, performing a simple greedy search (`ef=1`) at each level to find the best entry point for the target insertion layer, `l`.

Once at layer `l`, the second phase begins. From this layer down to layer 0, a more thorough search, controlled by the `efConstruction` parameter, finds candidate neighbors. The `M` closest candidates are connected to the new vector, respecting per-layer connection limits: `M_max` for upper layers and `M_max0` (typically `2*M`) for the denser base layer [[6]](https://www.pinecone.io/learn/series/faiss/hnsw/).

However, simply selecting the `M` closest candidates is not always optimal. To build a more robust graph, HNSW employs a heuristic that prioritizes diverse connections. It ensures that the selected neighbors are not all clustered together, instead favoring links that connect to different regions of the graph. This improves navigability by creating better long-range connections, even on the lower layers [[10]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).![Explanation of the number of links assigned to each vertex and the effect of M, M_max, and M_max0.](https://cdn.sanity.io/images/vr8gru94/production/dc5cb11ea197ceb4e1f18214066c8c51526b9af5-1920x1080.png)
Image 7: Link capping rules in HNSW construction, where layer 0 has more connections (`M_max0`) than upper layers (`M_max`). (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

This construction process mirrors the search algorithm, and the sequence of data insertion can influence the final graph's structure and search performance [[2]](https://arxiv.org/html/2405.17813v1). The candidates found at each layer serve as the entry points for the next, ensuring the graph remains navigable as it grows. Equipped with a clear picture of how the hierarchical graph is built, we now examine the concrete Faiss implementation, index internals, and parameter tradeoffs.

## Implementation of HNSW

We will implement HNSW using the Facebook AI Similarity Search (Faiss) library and test different construction and search parameters to see how they affect performance [[3]](https://www.pinecone.io/learn/series/faiss/).

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
2.  The parameter `M` sets the number of neighbors to add to each vertex during insertion. However, the `M_max` (max connections for upper layers) and `M_max0` (max connections for layer 0) parameters are set automatically by Faiss's `set_default_probas` method, which is called during initialization. It sets `M_max` to `M` and `M_max0` to `2*M` [[6]](https://www.pinecone.io/learn/series/faiss/hnsw/), [[10]](https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37).

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

The `set_default_probas` method is key to how Faiss builds the graph's structure. It takes `M` and a `levelMult` parameter (equivalent to `m_L`, which defaults to `1 / log(M)`) to calculate the probability of assigning a new vector to each layer [[15]](https://github.com/facebookresearch/faiss/blob/main/faiss/impl/HNSW.cpp).

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

3.  The `random_level` function uses these probabilities to assign a layer to a new vector. It generates a random float and iterates through the `assign_probas` list. It assigns the vector to the first level `i` where the random float is less than the cumulative probability up to that level.
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
Image 8: Distribution of vertices across layers in the Faiss (left) and Python (right) implementations, showing a near-identical structure. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

One small detail is that the Faiss implementation ensures at least one vector is present in the highest layer to serve as the entry point, which our simulation doesn't account for but is a minor difference [[6]](https://www.pinecone.io/learn/series/faiss/hnsw/).

### HNSW Performance

Now, let's explore the performance tradeoffs by adjusting the key parameters: `M`, `efConstruction`, and `efSearch`. We will run these tests on the Sift1M dataset [[6]](https://www.pinecone.io/learn/series/faiss/hnsw/).

-   `M`: The number of connections made for each new vertex during construction. A higher `M` increases the graph's connectivity, improving recall by providing more paths and reducing the chance of getting stuck in local minima. However, this comes at the cost of a larger memory footprint and longer build times, as more comparisons are needed to establish links [[16]](https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall).
-   `efConstruction`: The number of candidate neighbors explored when inserting a node. A higher value allows the algorithm to find more optimal connections, resulting in a higher-quality graph and better recall. The tradeoff is a significant increase in build time, as each insertion requires more distance computations. This parameter does not affect the final index size [[16]](https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall).
-   `efSearch`: The size of the dynamic candidate list during a query. This is a critical tuning parameter for balancing recall and query speed. A higher `efSearch` explores more neighbors, increasing the probability of finding the true nearest neighbors and thus improving recall. The downside is increased latency due to the additional distance calculations [[16]](https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall).

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
Image 9: Recall@1 performance across different parameter settings for HNSW on Sift1M. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

As shown in Image 9, higher values for `M` and `efSearch` substantially improve recall. A reasonably high `efConstruction` is also necessary, as a higher value can compensate for lower `M` and `efSearch` settings, leading to a higher-quality graph [[16]](https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall). For example, a high-recall setup for offline batch processing might use `M=24`, `efConstruction=400`, and `efSearch=500`, while a real-time system might prioritize speed with `M=12`, `efConstruction=200`, and `efSearch=100` [[16]](https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall).![Search time in µs for various M, efConstruction, and efSearch parameters when searching for 1000 queries. Note that the y-axis is using a log scale.](https://cdn.sanity.io/images/vr8gru94/production/876bf66aba408959042888efe72c55db4d6b4b41-1920x980.png)
Image 10: Search time for 1000 queries with different HNSW parameters. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

There is a clear tradeoff between recall and search time. The logarithmic y-axis in Image 10 shows that search time increases exponentially as we tune parameters for higher recall. Searching 1000 queries can range from around 1ms for ~80% recall to over 50ms for near-100% recall. It is often assumed that `efConstruction` has a minimal impact on search time, but our tests show this is only true for small query volumes. For a batch of 1000 queries, a higher `efConstruction` does increase search latency.

However, when query volume is low, increasing `efConstruction` is an excellent way to boost recall with little to no extra search time cost, especially at lower `M` values. This makes it a "free" recall boost for applications that handle single queries rather than large batches.![efConstruction and search time when searching for only one query. When using lower M values, the search time remains almost unchanged for different efConstruction values.](https://cdn.sanity.io/images/vr8gru94/production/ef1a2edd25adb202c0a98a1f33a0e72d1295b554-1720x1080.png)
Image 11: The impact of `efConstruction` on search time for a single query is negligible at lower `M` values. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))![Memory usage with increasing values of M using our Sift1M dataset. efSearch and efConstruction have no effect on the memory usage.](https://cdn.sanity.io/images/vr8gru94/production/e04d23ccd76d8bdc568542bebe75a75e7d36a21e-1480x1050.png)
Image 12: Memory usage increases linearly with M, while `efSearch` and `efConstruction` have no impact. (Source [Pinecone](https://www.pinecone.io/learn/series/faiss/hnsw/))

Finally, memory usage is solely dependent on `M`. `efConstruction` and `efSearch` have no effect on the index size [[6]](https://www.pinecone.io/learn/series/faiss/hnsw/). A simple rule of thumb for estimating memory is `d*4 + 2*M*4` bytes per vector [[17]](https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture). As `M` increases, so does the memory footprint, from over 0.5GB at `M=2` to nearly 5GB at `M=512` for the Sift1M dataset. This highlights the critical three-way tradeoff between recall, latency, and memory costs, which has direct implications for infrastructure planning and operational expenses.

For high-dimensional data, recent benchmarks show that a flat NSW graph (HNSW with a single layer) can achieve nearly identical recall and latency with significant memory savings—up to 38% less peak memory during construction on large datasets. This suggests the hierarchy's overhead may not be justified for all use cases [[11]](https://arxiv.org/html/2412.01940v2).

### Improving Memory Usage and Search Speeds

When the memory footprint of an HNSW index becomes too large, you have a few options. One common strategy is to compress the stored vectors using Product Quantization (PQ). This technique works by splitting each vector into sub-vectors and then quantizing each sub-vector separately, which significantly reduces memory usage. However, this compression is lossy and typically comes at the cost of lower recall and increased search times.

Another approach is to combine HNSW with an IVF component. In this setup, the dataset is partitioned into Voronoi cells, and HNSW is used as a coarse quantizer to quickly identify the most promising cells to search. This limits the search space and can improve search speeds, especially for very large datasets. A third option is to partition the dataset based on metadata, creating smaller, independent HNSW indexes that can be managed more easily [[18]](https://lantern.dev/blog/calculator). We cover combining IVF and PQ with HNSW in our article on composite indexes [[19]](https://www.pinecone.io/learn/series/faiss/composite-indexes/).

## Conclusion

HNSW has established itself as a top-performing ANN algorithm by cleverly combining the layered efficiency of skip lists with the powerful routing capabilities of navigable small world graphs. Its hierarchical structure allows for a search that is both fast and accurate, starting broad and progressively refining the results.

We have seen how to build and inspect an HNSW index using Faiss and explored the critical tradeoffs between `M`, `efConstruction`, and `efSearch`. Mastering these is key to optimizing HNSW for your specific use case. However, emerging research suggests that for high-dimensional data, the hierarchy itself may be an unnecessary overhead, with flat graphs offering comparable performance and lower memory costs due to the natural "hub" structures in the data [[11]](https://arxiv.org/html/2412.01940v2).

This highlights that HNSW is not a static solution. Its principles are being adapted to new domains like genomics with non-metric distances [[20]](https://escholarship.org/content/qt96h3s2sx/qt96h3s2sx_noSplash_e05e309fdf19eb7f453310a9459acdcc.pdf) and optimized for new hardware like edge devices [[21]](https://pmc.ncbi.nlm.nih.gov/articles/PMC12568237). Understanding HNSW’s internals empowers you to move beyond black-box usage and build truly high-performance vector search applications.

## References

- [1] https://www.vldb.org/pvldb/vol15/p850-doshi.pdf
- [2] https://arxiv.org/html/2405.17813v1
- [3] https://www.pinecone.io/learn/series/faiss/
- [4] https://www.geeksforgeeks.org/dsa/skip-list
- [5] https://en.wikipedia.org/wiki/Skip_list
- [6] https://www.pinecone.io/learn/series/faiss/hnsw/
- [7] https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf
- [8] https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf
- [9] https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605
- [10] https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37
- [11] https://arxiv.org/html/2412.01940v2
- [12] https://arxiv.org/html/2501.13992v2
- [13] https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world
- [14] https://www.tigerdata.com/blog/vector-database-basics-hnsw
- [15] https://github.com/facebookresearch/faiss/blob/main/faiss/impl/HNSW.cpp
- [16] https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall
- [17] https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture
- [18] https://lantern.dev/blog/calculator
- [19] https://www.pinecone.io/learn/series/faiss/composite-indexes/
- [20] https://escholarship.org/content/qt96h3s2sx/qt96h3s2sx_noSplash_e05e309fdf19eb7f453310a9459acdcc.pdf
- [21] https://pmc.ncbi.nlm.nih.gov/articles/PMC12568237
- [22] https://brilliant.org/wiki/skip-lists
- [23] https://openreview.net/pdf/9d557864b10a646d79ecf63772864cc3c168091f.pdf
- [24] https://towardsdatascience.com/ivfpq-hnsw-for-billion-scale-similarity-search-89ff2f89d90e
- [25] https://github.com/facebookresearch/faiss/wiki/Indexing-1M-vectors
- [26] https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW
- [27] https://github.com/efficient/faiss-learned-termination/blob/master/HNSW.h
- [28] https://faiss.ai/cpp_api/struct/structfaiss_1_1HNSW.html
- [29] https://skyzh.github.io/write-you-a-vector-db/cpp-06-02-hnsw.html
- [30] https://www.elastic.co/search-labs/blog/hnsw-graph
- [31] https://docs.vespa.ai/en/querying/approximate-nn-hnsw.html
- [32] https://medium.com/vespa/billion-scale-vector-search-using-hybrid-hnsw-if-96d7058037d3
- [33] https://arxiv.org/html/2607.02338v1
- [34] https://redis.io/blog/how-hnsw-algorithms-can-improve-search
- [35] https://www.researchgate.net/publication/262334462_Scalable_Distributed_Algorithm_for_Approximate_Nearest_Neighbor_Search_Problem_in_High_Dimensional_General_Metric_Spaces
- [36] https://publications.hse.ru/mirror/pubs/share/folder/x5p6h7thif/direct/128296059
- [37] https://15721.courses.cs.cmu.edu/spring2018/papers/08-oltpindexes1/pugh-skiplists-cacm1990.pdf
- [38] https://arxiv.org/abs/1603.09320
- [39] https://www.iiis.org/CDs2011/CD2011IDI/ICTA_2011/PapersPdf/CT175ON.pdf
- [40] https://arxiv.org/abs/1507.06529
- [41] https://arxiv.org/abs/0709.0303
</article>