# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>What is the structure and search in probabilistic skip lists?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://www.geeksforgeeks.org/dsa/skip-list

Query: What is the structure and search in probabilistic skip lists?

Answer: A skip list is a data structure that allows for efficient search, insertion and deletion of elements in a sorted list. It is a probabilistic data structure, meaning that its average time complexity is determined through a probabilistic analysis. In a skip list, elements are organized in layers, with each layer having a smaller number of elements than the one below it. The bottom layer is a regular linked list, while the layers above it contain "skipping" links that allow for fast navigation to elements that are far apart in the bottom layer. The idea behind this is to allow for quick traversal to the desired element, reducing the average number of steps needed to reach it.

-----

Phase: [EXPLOITATION]

### Source [2]: https://en.wikipedia.org/wiki/Skip_list

Query: What is the structure and search in probabilistic skip lists?

Answer: In computer science, a skip list (or skiplist) is a probabilistic data structure that allows [...] To quote the author: Skip lists are a probabilistic data structure that seem likely to supplant balanced trees as the implementation method of choice for many applications. Skip list algorithms have the same asymptotic expected time bounds as balanced trees and are simpler, faster and use less space. — William Pugh, Concurrent Maintenance of Skip Lists (1989) Fast search is made possible by maintaining a linked hierarchy of subsequences, with each successive subsequence skipping over fewer elements than the previous one (see the picture below). Searching starts in the sparsest subsequence until two consecutive elements have been found, one smaller and one larger than or equal to the element searched for. Via the linked hierarchy, these two elements link to elements of the next sparsest subsequence, where searching is continued until finally searching in the full sequence. The elements that are skipped over may be chosen probabilistically

-----

Phase: [EXPLOITATION]

### Source [3]: https://brilliant.org/wiki/skip-lists

Query: What is the structure and search in probabilistic skip lists?

Answer: The skip list is a probabilisitc data structure that is built upon the general idea of a linked list. The skip list uses probability to build subsequent layers of linked lists upon an original linked list. Each additional layer of links contains fewer elements, but no new elements. [...] Each element in the skip list has four pointers. It points to the node to its left, its right, its top, and its bottom. These quad-nodes will allow us to efficiently search through the skip list. Time The complexity of a skip list is complicated due to its probabilistic nature. We will prove its time complexity below, but for now we will just look at the results. It is important to note, though, that these bounds are expected or average-case bounds. This is because we use randomization in this data structure: Insertion - O(log(n)), Deletion - O(log(n)), Indexing - O(log(n)), Search - O(log(n)). Search There are two nested `while` loops in this function. There is the outer loop that is akin to "scanning down" the skip list, and there is the inner loop which is like "scanning forward" in the skip list.

-----

</details>

<details>
<summary>How does greedy routing function in navigable small world graphs?</summary>

Phase: [EXPLOITATION]

### Source [5]: https://www.pinecone.io/learn/series/faiss/hnsw

Query: How does greedy routing function in navigable small world graphs?

Answer: Navigable small world models are defined as any network with (poly/)logarithmic complexity using greedy routing. The efficiency of greedy routing breaks down for larger networks (1-10K+ vertices) when a graph is not navigable. The routing consists of two phases: a “zoom-out” phase passing through low-degree vertices and a later “zoom-in” phase passing through higher-degree vertices. When searching an NSW graph, we begin at a pre-defined entry-point. This entry point connects to several nearby vertices. We identify which of these vertices is the closest to our query vector and move there. The search process through a NSW graph greedily traverses to connected vertices that are nearer to the query vector. We repeat the greedy-routing search process of moving from vertex to vertex by identifying the nearest neighboring vertices in each friend list. Eventually, we will find no nearer vertices than our current vertex — this is a local minimum and acts as our stopping condition.

-----

Phase: [EXPLOITATION]

### Source [6]: https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605

Query: How does greedy routing function in navigable small world graphs?

Answer: The routing process in NSW graphs follows a greedy strategy where each step moves to the neighbor closest to the query target. The effectiveness of this approach depends on the graph’s ability to provide good local routing choices at each step. The proximity-based construction ensures that local neighborhoods contain progressively closer neighbors as the search approaches the target region, enabling effective convergence in most cases. The greedy routing strategy that underlies HNSW’s search algorithm can become trapped in local minima when the graph structure fails to provide adequate routing options toward the global optimum. While the multi-layer hierarchy and beam search with ef > 1 mitigate this issue significantly, pathological cases can still occur, particularly in highly clustered or discontinuous data distributions.

-----

Phase: [EXPLOITATION]

### Source [7]: https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37

Query: How does greedy routing function in navigable small world graphs?

Answer: Navigable small world is a graph with polylogarithmic T = O(logᵋn) search complexity which uses greedy routing. Routing refers to the process of starting the search process from low-degree vertices and ending with high-degree vertices. Since low-degree vertices have very few connections, the algorithm can rapidly move between them to efficiently navigate to the region where the nearest neighbour is likely to be located. Then the algorithm gradually zooms in and switches to high-degree vertices to find the nearest neighbour among the vertices in that region. Greedy search process in a navigable small world: Node A is used as an entry point. It has two neighbours B and D. Node D is closer to the query than B. As a result, we move to D. Node D has three neighbours C, E and F. E is the closest neighbour to the query, so we move to E. Finally, the search process will lead to node L. Since all neighbours of L are located further from the query than L itself, we stop the algorithm and return L as the answer to the query.

-----

Phase: [EXPLOITATION]

### Source [8]: https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf

Query: How does greedy routing function in navigable small world graphs?

Answer: Networks with logarithmic or polylogarithmic scaling of the greedy graph routing are known as the navigable small world networks. Such networks are an important topic of complex network theory aiming at understanding of the underlying mechanisms of real-life networks formation in order to apply them for applications of scalable routing and distributed similarity search. An NSW graph is constructed via consecutive insertion of elements in random order by bidirectionally connecting them to the M closest neighbors from the previously inserted elements. The M closest neighbors are found using a variant of a greedy search from multiple random enter-point nodes. Links to the closest neighbors of the elements inserted at the beginning of the construction later become bridges between the network hubs that keep the overall graph connectivity and allow the logarithmic scaling of the number of hops during greedy routing.

-----

</details>

<details>
<summary>What are core innovations in Malkov HNSW paper?</summary>

Phase: [EXPLOITATION]

### Source [9]: https://medium.com/@EleventhHourEnthusiast/paper-review-efficient-and-robust-approximate-nearest-neighbor-search-using-hierarchical-navigable-07f7241a0baf

Query: What are core innovations in Malkov HNSW paper?

Answer: Core innovations in Malkov HNSW paper include a hierarchical set of navigable small world graphs and a heuristic neighbor selection strategy for efficient search. HNSW leverages navigable small world graphs, which combine local clustering and long-range connections to enable efficient navigation between nodes. HNSW’s key innovation lies in its hierarchical set of such graphs, each representing a different scale of similarity. The paper attributes HNSW’s strengths to its innovative hierarchical structure, which enables efficient navigation across different scales of similarity, and its heuristic neighbor selection strategy, which promotes robust and diverse connections within the graph.

-----

Phase: [EXPLOITATION]

### Source [10]: https://khoury.northeastern.edu/home/pandey/courses/cs7270/fall25/papers/vectordb/HNSW.pdf

Query: What are core innovations in Malkov HNSW paper?

Answer: The main contributions are: explicit selection of the graph’s enter-point node, separation of links by different scales and use of an advanced heuristic to select the neighbors. Hierarchical NSW incrementally builds a multi-layer structure consisting of a hierarchical set of proximity graphs (layers) for nested subsets of the stored elements. The maximum layer in which an element is present is selected randomly with an exponentially decaying probability distribution.

-----

Phase: [EXPLOITATION]

### Source [13]: https://openreview.net/pdf/9d557864b10a646d79ecf63772864cc3c168091f.pdf

Query: What are core innovations in Malkov HNSW paper?

Answer: HNSW builds off of prior work in navigable small world graph indexes. Small world graphs are a well-studied phenomenon in both computing and the social sciences and are primarily defined by the fact that the average length of a shortest path between two vertices is small (typically scaling logarithmically with the number of nodes in the network).

-----

</details>

<details>
<summary>How does Faiss implement HNSW with parameters M efConstruction efSearch?</summary>

Phase: [EXPLOITATION]

### Source [14]: https://towardsdatascience.com/ivfpq-hnsw-for-billion-scale-similarity-search-89ff2f89d90e

Query: How does Faiss implement HNSW with parameters M efConstruction efSearch?

Answer: In Faiss, HNSW is implemented with `IndexHNSWFlat`. An index in Faiss is a data structure, an object where one can use the `add` method to add vectors to the index, and the `search` method to perform a nearest neighbor search given some query vectors. A flat index typically means an index that is without any compression or encoding, where the actual vectors are stored as is. `IndexHNSWFlat` `add` `search` ### Effect of M, efConstruction, and efSearch In this section, we will plot out and examine the effect of `M`, `efConstruction`, and `efSearch` on HNSW. `M` `efConstruction` `efSearch` [...] `M` `efConstruction` `efSearch` To recapitulate, `M` is the number of connections that would be made for each new vertex during construction. `efConstruction` is the number of candidate neighbors to explore during construction time, while `efSearch` is the number of candidate neighbors to explore during search time. `M` `efConstruction` `efSearch` To generate these plots, 3 million 128-dimensional vectors are added to `IndexHNSWFlat`, and search is performed using 1,000 query vectors. These are synthetic vectors generated using the Faiss datasets module. `IndexHNSWFlat` [...] The bubble charts below summarize the effect of `M`, `efConstruction`, and `efSearch` on the search speed and accuracy of HNSW, as well as on the index size and construction time. `M` `efConstruction` `efSearch` If memory is not a concern, HNSW is a great choice for providing fast and superb-quality searches. ## 6. Implementation with Faiss: IndexIVFPQ + HNSW Awesome! We’ve learned how to implement HNSW with Faiss. But how do we use HNSW with IVFPQ? In Faiss, IVFPQ is implemented with `IndexIVFPQ`. `IndexIVFPQ` The `IndexHNSWFlat` we saw earlier now works as the coarse quantizer for `IndexIVFPQ`. `IndexHNSWFlat` `IndexIVFPQ`

-----

Phase: [EXPLOITATION]

### Source [15]: https://www.pinecone.io/learn/series/faiss/hnsw

Query: How does Faiss implement HNSW with parameters M efConstruction efSearch?

Answer: We will be modifying three parameters: `M`, `efSearch`, and `efConstruction`. And we will be indexing the Sift1M dataset, which you can download and prepare using this script. As we did before, we initialize our index like so: ``` index = faiss.IndexHNSWFlat(d, M) ``` The two other parameters, `efConstruction` and `efSearch` can be modified after we have initialized our `index`. ``` index.hnsw.efConstruction = efConstruction index.add(xb) # build the index index.hnsw.efSearch = efSearch # and now we can search index.search(xq[:1000], k=1) ``` Our `efConstruction` value must be set before we construct the index via `index.add(xb)`, but `efSearch` can be set anytime before searching. Let’s take a look at the recall performance first. [...] Explanation of the number of links assigned to each vertex and the effect of M, M\_max, and M\_max0. The stopping condition for insertion is reaching the local minimum in layer 0. ## Implementation of HNSW We will implement HNSW using the Facebook AI Similarity Search (Faiss) library, and test different construction and search parameters and see how these affect index performance. To initialize the HNSW index we write: In: ``` # setup our HNSW parameters d = 128 # vector size M = 32 index = faiss.IndexHNSWFlat(d, M) print(index.hnsw) ``` Out: ``` > ``` With this, we have set our `M` parameter — the number of neighbors we add to each vertex on insertion, but we’re missing M\_max and M\_max0. [...] In Faiss, these two parameters are set automatically in the `set_default_probas` method, called at index initialization. The M\_max value is set to `M`, and M\_max0 set to `M2` (find further detail in the notebook). Before building our `index` with `index.add(xb)`, we will find that the number of layers (or levels in Faiss) are not set: In: ``` # the HNSW index starts with no levels index.hnsw.max_level ``` Out: ``` -1 ``` In: ``` # and levels (or layers) are empty too levels = faiss.vector_to_array(index.hnsw.levels) np.bincount(levels) ``` Out: ``` array([], dtype=int64) ``` If we go ahead and build the index, we’ll find that both of these parameters are now set. In: ``` index.add(xb) ``` In:

-----

Phase: [EXPLOITATION]

### Source [18]: https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall

Query: How does Faiss implement HNSW with parameters M efConstruction efSearch?

Answer: M determines the number of bidirectional links each node maintains in the graph layers of HNSW. A higher M (e.g., 24 vs. 12) increases the graph’s connectivity, improving recall by reducing the chance of search getting trapped in local minima. However, more connections also expand the index size (memory usage) and slow down build time, as each insertion requires more comparisons to establish links. For example, doubling M from 12 to 24 might quadruple build time in some cases. During queries, a higher M can speed up search by enabling faster traversal through the graph’s “shortcuts,” but this depends on how well the graph is structured during construction. Developers often tune M based on dataset size and memory constraints—larger datasets may require higher M for acceptable recall but [...] efSearch (Query-Time Search Depth): efSearch determines the size of the dynamic candidate list during querying. A higher efSearch (e.g., 500 vs. 100) increases recall by exploring more neighbors, but it slows down queries due to additional distance calculations. For example, in a 10-million-vector dataset, efSearch=500 might achieve 98% recall but take 5ms per query, while efSearch=100 might drop to 85% recall with 1ms latency. This parameter is often adjusted dynamically: a large efSearch is used for accuracy-critical tasks (e.g., medical image retrieval), while smaller values suit real-time applications (e.g., autocomplete suggestions). Importantly, efSearch must be set ≥ the desired number of nearest neighbors (k) to return meaningful results. [...] efConstruction controls the number of candidate neighbors explored when inserting a node into the graph. A higher efConstruction (e.g., 400 vs. 200) allows the algorithm to find more optimal connections during index creation, leading to a higher-quality graph and better recall. However, this significantly increases build time, as each insertion requires more distance computations. For instance, setting efConstruction=400 might double build time compared to efConstruction=200. The parameter does not affect index size, as it only influences how links are selected. Developers often prioritize higher efConstruction for critical applications like recommendation systems where recall is paramount, even if it means waiting longer for the index to build.

-----

</details>

<details>
<summary>What empirical tradeoffs does HNSW show on Sift1M for M ef parameters?</summary>

Phase: [EXPLOITATION]

### Source [19]: https://www.vldb.org/pvldb/vol15/p850-doshi.pdf

Query: What empirical tradeoffs does HNSW show on Sift1M for M ef parameters?

Answer: HNSW tends to outperform competitors considering QPS vs recall tradeoff on SIFT1M. The recall is generally traded off for the query latency or throughput. Figure 1 shows compromise between various algorithms including HNSW on SIFT1M dataset for 10 and 100 nearest neighbors. HNSW is a graph-based technique with polylogarithmic time complexity, highly competitive on real-world datasets, with tuning parameters to adjust accuracy vs speed and space vs speed trade-offs.

-----

Phase: [EXPLOITATION]

### Source [20]: https://www.pinecone.io/learn/series/faiss/hnsw

Query: What empirical tradeoffs does HNSW show on Sift1M for M ef parameters?

Answer: On Sift1M, memory usage increases with M (from >0.5GB at M=2 to ~5GB at M=512); efSearch and efConstruction have no effect on memory. High M and efSearch improve recall@1, with reasonable efConstruction needed; higher efConstruction achieves higher recall at lower M/efSearch. Search time increases with parameters (log scale shown). Tradeoff between recall and search time; M controls connectivity/memory/recall, efConstruction for build quality, efSearch for search accuracy.

-----

Phase: [EXPLOITATION]

### Source [21]: https://github.com/facebookresearch/faiss/wiki/Indexing-1M-vectors

Query: What empirical tradeoffs does HNSW show on Sift1M for M ef parameters?

Answer: On SIFT1M, HNSW obtains better speed/precision than IVFFlat (0.020ms vs 0.140ms for >0.9 recall@1) at higher memory cost. HNSW with scalar quantizer better than classical HNSW. Various HNSW uses evaluated with benchs/bench_hnsw.py. HNSW has best operating points in high-accuracy regime.

-----

</details>

<details>
<summary>How does HNSW assign random layer heights using exponential probability distribution?</summary>

Phase: [EXPLOITATION]

### Source [24]: https://arxiv.org/html/2412.01940v2

Query: How does HNSW assign random layer heights using exponential probability distribution?

Answer: HNSW assigns random layer heights using an exponentially decaying probability distribution, ensuring fewer elements at higher layers. The layer assignment follows a formula based on the natural logarithm of a random number. This method balances the structure for efficient querying. Specifically, the HNSW index is constructed in an iterative fashion. For a newly inserted element x, the algorithm will randomly select a maximum layer l and then insert the new point into every layer up to l. This randomized process is executed with an exponentially decaying probability distribution such that, in expectation, each subsequent layer has exponentially more nodes than its predecessor.

-----

Phase: [EXPLOITATION]

### Source [25]: https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world

Query: How does HNSW assign random layer heights using exponential probability distribution?

Answer: Elements are randomly assigned levels, with fewer elements at higher levels. The level distribution follows an exponentially decaying probability. This randomization ensures a balanced structure that can handle dynamic datasets efficiently. The probabilistic tiering in HNSW, where nodes distribute across different layers like skip lists, is governed by a parameter typically denoted as mL. This parameter determines the likelihood of a node appearing in successive layers, with the probability decreasing exponentially as the layers ascend.

-----

Phase: [EXPLOITATION]

### Source [27]: https://zilliz.com/learn/hierarchical-navigable-small-worlds-HNSW

Query: How does HNSW assign random layer heights using exponential probability distribution?

Answer: As with the skip list, the query vector will appear in upper layers with exponentially decreasing probability. Specifically, the HNSW paper uses the equation `floor(-ln(rand(0, 1)))`, where `rand(0, 1)` is a random number sampled from a uniform distribution between (0, 1]. The uppermost layer has the lowest probability, increasing probability as we move down in layers. The general rule is that any element in a layer will appear in layer above it with some pre-defined probability `p`. Therefore, if an element first appears in some layer `l`, it will also get added to layers `l-1`, `l-2`, and so on. l = -int(np.log(np.random.random()) * self._mL)

-----

</details>

<details>
<summary>What two-phase construction search does HNSW use with ef=1 and efConstruction?</summary>

Phase: [EXPLOITATION]

### Source [29]: https://www.pinecone.io/learn/series/faiss/hnsw

Query: What two-phase construction search does HNSW use with ef=1 and efConstruction?

Answer: HNSW uses two-phase construction: first, ef=1 for initial layer connections; second, efConstruction for thorough neighbor exploration. Graph construction starts at the top layer. After entering the graph the algorithm greedily traverse across edges, finding the ef nearest neighbors to our inserted vector q — at this point ef = 1. After finding the local minimum, it moves down to the next layer (just as is done during search). This process is repeated until reaching our chosen insertion layer. Here begins phase two of construction. The ef value is increased to efConstruction (a parameter we set), meaning more nearest neighbors will be returned. In phase two, these nearest neighbors are candidates for the links to the new inserted element q and as entry points to the next layer. M neighbors are added as links from these candidates — the most straightforward selection criteria are to choose the closest vectors.

-----

</details>

<details>
<summary>How does Faiss set_default_probas compute level probabilities and M_max for HNSW?</summary>

Phase: [EXPLOITATION]

### Source [31]: https://www.pinecone.io/learn/series/faiss/hnsw

Query: How does Faiss set_default_probas compute level probabilities and M_max for HNSW?

Answer: In Faiss, these two parameters are set automatically in the `set_default_probas` method, called at index initialization. The M_max value is set to `M`, and M_max0 set to `M2` (find further detail in the notebook). When we initialize our index we pass our vector dimensionality `d` and number of neighbors for each vertex `M`. This calls the method ‘`set_default_probas`’, passing `M` and `1 / log(M)` in the place of `levelMult` (equivalent to m_L above). A Python equivalent of this method looks like: def set_default_probas(M: int, m_L: float): nn = 0 cum_nneighbor_per_level = [] level = 0 assign_probas = [] while True: proba = np.exp(-level / m_L) * (1 - np.exp(-1 / m_L)) if proba < 1e-9: break assign_probas.append(proba) nn += M2 if level == 0 else M cum_nneighbor_per_level.append(nn) level += 1 return assign_probas, cum_nneighbor_per_level. The method stops creating new levels when a low probability threshold is reached.

-----

Phase: [EXPLOITATION]

### Source [32]: https://github.com/efficient/faiss-learned-termination/blob/master/HNSW.h

Query: How does Faiss set_default_probas compute level probabilities and M_max for HNSW?

Answer: void set_default_probas(int M, float levelMult); void set_nb_neighbors(int level_no, int n); int nb_neighbors(int layer_no) const; int cum_nb_neighbors(int layer_no) const; explicit HNSW(int M = 32); int random_level(); void fill_with_random_links(size_t n); void set_default_probas(int M, float levelMult); std::vector<double> assign_probas; std::vector<int> cum_nneighbor_per_level;

-----

Phase: [EXPLOITATION]

### Source [34]: https://faiss.ai/cpp_api/struct/structfaiss_1_1HNSW.html

Query: How does Faiss set_default_probas compute level probabilities and M_max for HNSW?

Answer: initialize the assign_probas and cum_nneighbor_per_level to have 2\M links on level 0 and M links on levels > 0 set nb of neighbors for this level (before adding anything) nb of neighbors for this level cumumlative nb up to (and excluding) this level range of entries in the neighbors table of vertex no at layer_no only mandatory parameter: nb of neighbors pick a random level for a new point add n random levels to table (for debugging…) assignment probability to each layer (sum=1) number of neighbors stored per layer (cumulative), should not be changed after first add

-----

Phase: [EXPLOITATION]

### Source [35]: https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37

Query: How does Faiss set_default_probas compute level probabilities and M_max for HNSW?

Answer: Faiss implementation of IndexHNSWFlat IndexHNSWFlat sets values for M₀ = M and M₀0 = 2 \ M. IndexHNSWFlat + IndexIVFPQ IndexHNSWFlat can be combined with other indexes as well. One of the examples is IndexIVFPQ described in the previous part. Creation of this composite index proceeds in two steps: Training and adding can be done by using different or the same data. FAISS implementation of IndexHNSWFlat + IndexIVFPQ Conclusion Faiss (Facebook AI Search Similarity) is a Python library written in C++ used for optimised similarity search. This library presents different types of indexes which are data structures used to efficiently store the data and perform queries. Based on the information from the Faiss documentation, we will see how HNSW can be utilized and merged together with inverted file index and product quantization. FAISS has a class IndexHNSWFlat implementing the HNSW structure. As usual, the suffix "Flat" indicates that dataset vectors are fully stored in index. The constructor accepts 2 parameters: Additionally, via thr hnsw field, IndexHNSWFlat provides several useful attributes (which can be modified) and methods: Construction Choosing the maximum layer Nodes in HNSW are inserted sequentially one by one. Every node is randomly assigned an integer l indicating the maximum layer at which this node can present in the graph. For example, if l = 1, then the node can only be found on layers 0 and 1. The authors select l randomly for each node with an exponentially decaying probability distribution normalized by the non-zero multiplier mL (mL = 0 results in a single layer in HNSW and non-optimized search complexity). Normally, the majority of l values should be equal to 0, so most of the nodes are present only on the lowest level. The larger values of mL increase the probability of a node appearing on higher layers.

-----

</details>

<details>
<summary>What role does L play in HNSW insertion?</summary>

Phase: [EXPLOITATION]

### Source [36]: https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37

Query: What role does L play in HNSW insertion?

Answer: Nodes in HNSW are inserted sequentially one by one. Every node is randomly assigned an integer l indicating the maximum layer at which this node can present in the graph. For example, if l = 1, then the node can only be found on layers 0 and 1. The authors select l randomly for each node with an exponentially decaying probability distribution normalized by the non-zero multiplier mL (mL = 0 results in a single layer in HNSW and non-optimized search complexity). Normally, the majority of l values should be equal to 0, so most of the nodes are present only on the lowest level. The larger values of mL increase the probability of a node appearing on higher layers. [...] One of the ways to decrease the overlap is to decrease mL. But it is important to keep in mind that reducing mL also leads on average to more traversals during a greedy search on each layer. That is why it is essential to choose such a value of mL that will balance both the overlap and the number of traversals. The authors of the paper propose choosing the optimal value of mL which is equal to 1 / ln(M). This value corresponds to the parameter p = 1 / M of the skip list being an average single element overlap between the layers.

-----

Phase: [EXPLOITATION]

### Source [37]: https://www.pinecone.io/learn/series/faiss/hnsw

Query: What role does L play in HNSW insertion?

Answer: During graph construction, vectors are iteratively inserted one-by-one. The number of layers is represented by parameter L. The probability of a vector insertion at a given layer is given by a probability function normalized by the ‘level multiplier’ m_L, where m_L = ~0 means vectors are inserted at layer 0 only. The probability function is repeated for each layer (other than layer 0). The vector is added to its insertion layer and every layer below it. The creators of HNSW found that the best performance is achieved when we minimize the overlap of shared neighbors across layers. Decreasing m_L can help minimize overlap (pushing more vectors to layer 0), but this increases the average number of traversals during search. So, we use an m_L value which balances both. A rule of thumb for this optimal value is `1/ln(M)`.

-----

Phase: [EXPLOITATION]

### Source [38]: https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world

Query: What role does L play in HNSW insertion?

Answer: When a new node is added for the graph construction, the algorithm first determines its position in the hierarchical structure depending on where the node appears and the maximum number of nodes. This process involves identifying the pre-defined entry point for the node based on the probabilistic tiering governed by the parameter mL. Upon introducing a new node to the graph, the algorithm orchestrates its placement within the hierarchical structure. This involves identifying the entry layer for the node through a probabilistic tiering mechanism governed by the parameter mL. Commencing from that layer, the insertion process establishes connections for the new node with the M closest neighbors within that layer.

-----

Phase: [EXPLOITATION]

### Source [39]: https://skyzh.github.io/write-you-a-vector-db/cpp-06-02-hnsw.html

Query: What role does L play in HNSW insertion?

Answer: Before inserting, we will need to decide which layer and below levels to insert the vector. From the HNSW paper, this is computed by \( \text{level} = \lfloor - \ln (\text{unif} (0 \ldots 1)) \times m\_L \rfloor \). ep = upper-most level entry point target_level = generate random level based on m_L for go down one level until target_level + 1 ep <- layers[level].search(ep=ep, limit=1, search_target) for go down one level until level 0 ep <- layers[level].search(ep=ep, limit=ef_construction, search_target) neighbors <- m-nearest neighbor in ep connect neighbors with search_target purge edges of neighbors if larger than m_max of that layer

-----

</details>

<details>
<summary>What link capping rules use M_max in HNSW?</summary>

Phase: [EXPLOITATION]

### Source [40]: https://www.pinecone.io/learn/series/faiss/hnsw

Query: What link capping rules use M_max in HNSW?

Answer: In HNSW, M_max limits the maximum number of links per vertex to control graph density. It helps balance recall and search speed. Higher values increase recall but also memory usage and indexing cost. After working through multiple iterations, there are two more parameters that are considered when adding links. M_max, which defines the maximum number of links a vertex can have, and M_max0, which defines the same but for vertices in layer 0. In Faiss, these two parameters are set automatically in the set_default_probas method, called at index initialization. The M_max value is set to M, and M_max0 set to M2 (find further detail in the notebook). With an m value of three we would add three neighbors to that vertex both on layer one and also on layer zero now we can also have a m max value and an m max zero value which is what we have down here and basically as more vertices are added we may find that this vertex ends up with more than three friends and maybe that that's fine but what we essentially do is use m match to say okay if we have any vertices with more than this number of friends we need to trim it and we need to just keep the closest like three in this example and then m max zero is another value and that is the same so it's the maximum number of friends of vertex you have but for layer 0 which is i think always a higher number than the other layers. On every level we will assign m neighbors as our is our m max it's set from level zero where we will assign uh 2 m okay so this is this m times y 2. so for for our use case we have 32 we have m set to 32 so that means in all of our layers set from layer 0 will have each vertex will have 32 neighbors or friends and on layer or level 0 it will have 64 friends.

-----

Phase: [EXPLOITATION]

### Source [42]: https://www.elastic.co/search-labs/blog/hnsw-graph

Query: What link capping rules use M_max in HNSW?

Answer: To summarize, the two parameters used to construct an HNSW graph are M (the maximum number of links a node can have) and ef_construction (how many nodes to search for neighbours when adding a new vector). Because each layer has fewer vectors than the layer below it, but the maximum number of links is the same, vectors in higher layers have longer-range links than those in lower layers, aiding fast traversal across the vector space from the initial entry point at the start of the search.

-----

Phase: [EXPLOITATION]

### Source [44]: https://docs.vespa.ai/en/querying/approximate-nn-hnsw.html

Query: What link capping rules use M_max in HNSW?

Answer: max-links-per-node - a higher value increases recall accuracy, but also memory usage, indexing and search cost. neighbors-to-explore-at-insert - a higher value increases recall accuracy, but also indexing cost. Choosing the value of these parameters affects both accuracy, search performance, memory usage and indexing performance. See Billion-scale vector search with Vespa - part two for a detailed description of these tradeoffs. See HNSW index reference for details on the index parameters. The HNSW settings impacts indexing throughput. Higher values of max-links-per-node and neighbors-to-explore-at-insert reduces indexing throughput. Example from Billion-scale vector search with Vespa - part two.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What are HNSW main failure modes in clustered high-dimensional data?</summary>

Phase: [EXPLORATION]

### Source [46]: https://medium.com/thedeephub/understading-hnsw-hierarchical-navigable-small-world-ff1a72d98605

Query: What are HNSW main failure modes in clustered high-dimensional data?

Answer: The greedy routing strategy that underlies HNSW’s search algorithm can become trapped in local minima when the graph structure fails to provide adequate routing options toward the global optimum. While the multi-layer hierarchy and beam search with ef > 1 mitigate this issue significantly, pathological cases can still occur, particularly in highly clustered or discontinuous data distributions. These limitations manifest as reduced recall rates that cannot be overcome simply by increasing search effort. High-dimensional data presents fundamental challenges that affect all proximity-based search methods, including HNSW. As dimensionality increases, the relative differences between distances to different points become smaller due to concentration of measure effects. This phenomenon can make it difficult to distinguish between truly similar and dissimilar items, reducing the effectiveness of any distance-based search strategy. High-dimensional datasets present more complex scaling behavior due to the intrinsic properties of high-dimensional spaces and the limitations of proximity-based routing. While HNSW maintains significant advantages over competing methods, the logarithmic scaling may become less pronounced in very high dimensions where the concept of nearest neighbors becomes less meaningful due to concentration of measure phenomena.

-----

Phase: [EXPLORATION]

### Source [47]: https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture

Query: What are HNSW main failure modes in clustered high-dimensional data?

Answer: The problem is the curse of dimensionality. In high dimensions, the volumes of hyperspheres and hyperrectangles become so large relative to the data that almost no pruning is possible. For 512-dimensional embeddings, a KD-tree query degrades to nearly brute-force performance: the tree structure provides no benefit. This makes tree-based methods completely impractical for modern NLP embeddings. Low M (4-8): Compact index, faster construction, but lower recall, especially for high-dimensional data. The graph is sparse, meaning fewer alternative paths exist between any two nodes. This can work well for low-dimensional data or applications where modest recall is acceptable. Medium M (12-24): The sweet spot for most applications. M=16 is a common default. At this level, the graph is dense enough to provide excellent navigability without excessive memory overhead. Most nodes have enough connections that the greedy search rarely gets stuck. For very high-dimensional embeddings (above 1024 dimensions), HNSW's performance can degrade. In these spaces, all vectors are roughly equidistant from any query (the curse of dimensionality), making it hard for the greedy search to make directional progress. Increasing M helps, but at the cost of proportionally higher memory and construction time. Dimensionality reduction via PCA before indexing can mitigate this, though it introduces a small additional approximation. In practice, most sentence embedding models produce vectors in the 384 to 1536 dimensional range, where HNSW performs well without special treatment.

-----

Phase: [EXPLORATION]

### Source [48]: https://arxiv.org/html/2412.01940v2

Query: What are HNSW main failure modes in clustered high-dimensional data?

Answer: A related, but slightly different, notion of hubness that has been at the center of theoretical analysis is concentration of distances in high-dimensional spaces. It has been shown that, in expectation, the ℓ 2 distance between independent and identically distributed (i.i.d) vectors grows with d while the variance tends to a constant as d approaches infinity (Talagrand, 1994). As a result, the ℓ 2 distance loses its discriminative power as d increases. In fact, this concentration phenomenon is not only constrained to ℓ 2 Why does hierarchy not help? We hypothesize that the hierarchy benefits decrease in high-dimensions due to hubness. Hubness is a high-dimensional phenomenon that causes a skewed distribution in the near-neighbor lists of search queries (Radovanovic et al., 2010). We hypothesize that hubness leads to preferential attachment in the similarity search graph, inducing the formation of easily-traversed highways that connect disparate regions of the graph. Concentration of distances: Under many data-generating distributions, the expected distances between randomly-drawn points converge to a constant value as dimension increases (Beyer et al., 1999). This suggests that in sufficiently high-dimensional spaces, we do not need to explicitly encourage the formation of “long-range” connections. Since all distances are approximately equal, all connections have similar length and a few edge traversals should span the graph of a high-dimensional dataset.

-----

Phase: [EXPLORATION]

### Source [49]: https://www.pinecone.io/learn/series/faiss/hnsw

Query: What are HNSW main failure modes in clustered high-dimensional data?

Answer: High-degree vertices have many links, whereas low-degree vertices have very few links. Our stopping condition is finding no nearer vertices in our current vertex’s friend list. Because of this, we are more likely to hit a local minimum and stop too early when in the zoom-out phase (fewer links, less likely to find a nearer vertex). To minimize the probability of stopping early (and increase recall), we can increase the average degree of vertices, but this increases network complexity (and search time). So we need to balance the average degree of vertices between recall and search speed.

-----

Phase: [EXPLORATION]

### Source [50]: https://www.tigerdata.com/blog/vector-database-basics-hnsw

Query: What are HNSW main failure modes in clustered high-dimensional data?

Answer: Traditional graph indexing techniques often struggle with the curse of dimensionality, where the distance between data points becomes less meaningful in high-dimensional spaces. This makes it challenging to organize and search the data efficiently. They also suffer from poor scalability and difficulty updating the index as new data points are added or removed. HNSW addresses these issues through its multi-layered, hierarchical approach. It allows for efficient search by reducing the dimensionality at each layer and dynamically adjusting the graph's structure without needing complete rebuilds. ANN can be divided into three primary categories, each defined by its foundational data structures: trees, hashes, and graphs. Trees hierarchically organize data, allowing for binary decisions at each node to navigate closer to the query point. Hashes convert data points into codes in a lower-dimensional space, grouping similar items into the same buckets for faster retrieval. Graphs, which HNSW utilizes, create a network of points where edges connect neighbors based on similarity measures. Among these, HNSW stands out for its use of a multi-layered graph structure that efficiently tackles the "curse of dimensionality"—an issue that impacts high-dimensional data spaces by making traditional search methodologies inefficient and often infeasible.

-----

</details>

<details>
<summary>How does HNSW memory scale for billion-vector datasets versus theory?</summary>

Phase: [EXPLORATION]

### Source [51]: https://medium.com/vespa/billion-scale-vector-search-using-hybrid-hnsw-if-96d7058037d3

Query: How does HNSW memory scale for billion-vector datasets versus theory?

Answer: For a billion scale vector dataset using 768 dimensions with float precision requires close to 3TiB of memory. In addition, the HNSW graph data structure needs to be in-memory, which adds 20-40% in addition to the vector data. Given this, indexing a 1B vector dataset using HNSW will need about 4TiB of memory. In 2022, many cloud providers offer cloud instance types with large amounts of memory, but these instance types also come with many v-CPUs, which drives production deployment costs. These high-memory and high-compute instance types support massive queries per second and might be the optimal instance type for applications needing to support large query throughput with high recall. However, many real-world applications using vector search do not need enormous query throughput but still need to search large billion-scale vector datasets with relatively low latency with high accuracy. Therefore, large cloud instance types with thousands of GiB of memory and hundreds of v-CPUs are not cost-efficient for those low query volume use cases.

-----

Phase: [EXPLORATION]

### Source [52]: https://mbrenndoerfer.com/writing/hnsw-index-vector-search-architecture

Query: How does HNSW memory scale for billion-vector datasets versus theory?

Answer: The most significant limitation is memory consumption. HNSW requires storing the entire graph structure in RAM, including all vectors and their neighbor lists. For a billion-vector index with 768-dimensional embeddings, the vectors alone require about 3 TB of storage (at 4 bytes per float), and the graph adds substantial overhead on top of that. This makes pure HNSW impractical for very large-scale deployments without compression techniques like Product Quantization or dimensionality reduction. The total memory per vector in an HNSW index is approximately d×4 bytes (for the raw float32 vector) plus 2M×4 bytes (for the layer 0 connections) plus a small overhead for the upper layers. With d=768 and M=16, this works out to about 3200 bytes per vector, or roughly 3.2 GB per million vectors.

-----

Phase: [EXPLORATION]

### Source [53]: https://lantern.dev/blog/calculator

Query: How does HNSW memory scale for billion-vector datasets versus theory?

Answer: There usually are natural ways to partition a huge dataset via metadata fields, so the above optimization is applicible in theory. For example, when indexing a large scientific libraries such as Arxiv or OpenAlex, one can partition the index by year of publication, topic, etc. Postgres has great support for partial indexes, constrained by values of non-indexed columns, all of which Lantern inherits. So, this kind of partitioning is possible and painless in Lantern! Though we have not yet implemented neighbor id compression as described above, this is on our roadmap for supporting billion-scale datasets off of a single node. Hopefully, the graphs above convince you that even for billion-vector datasets, a single database node is likely enough to store your index. HNSW stores our dataset of vectors in a hierarchical graph structure. The majority of the vectors are stored at the lowest level. At typical values of M (M >= 10), over 90% of all vectors are at the lowest level. There are exponentially fewer vectors at each higher level. At the lowest level, nodes have 2 \ M neighbors. So, the vast majority of nodes have 2 \ M neighbors and this is very close to average number of neighbors per node in the graph.

-----

Phase: [EXPLORATION]

### Source [54]: https://arxiv.org/html/2412.01940v2

Query: How does HNSW memory scale for billion-vector datasets versus theory?

Answer: We utilize the benchmark datasets released through the popular leaderboards ANN Benchmarks (Aumüller et al., 2018) and Big ANN Benchmarks (Simhadri et al., 2022). The specific datasets and their associated statistics are presented in Table 1. For the Big ANN Benchmark datasets, we consider both the 10M and 100M collection of vectors for which the ground truth near neighbors have previously been computed and released. We did not experiment with the largest Big ANN datasets with 1 billion vectors since constructing HNSW indexes at this scale requires over 1.5TB of RAM, which exceeded our compute resources. Below, we include our benchmarking results for the four 100M-scale datasets available through Big ANN Benchmarks. We see that our flat HNSW implementation achieves performance parity with

-----

Phase: [EXPLORATION]

### Source [55]: https://www.tigerdata.com/blog/vector-database-basics-hnsw

Query: How does HNSW memory scale for billion-vector datasets versus theory?

Answer: 1. Memory-intensive: HNSW's performance relies heavily on storing the index entirely in memory. While beneficial for speed, this architecture choice makes HNSW more suitable for systems with substantial RAM availability. The memory requirement can become a limiting factor as the dataset grows, especially into the tens of millions of high-dimensional vectors. 2. Scales with memory, not disk: Unlike other data storage and indexing methods that efficiently utilize disk space, HNSW's design necessitates that the entire index fit within the available memory. This characteristic can pose challenges in scaling the system for extensive datasets or in environments where memory resources are constrained. While HNSW is the preferred index in vector databases, its memory-intensive nature can be a hurdle for developers working with large datasets. This is where pgvectorscale stands out, delivering high performance without eating away at your disk space and memory.

-----

</details>

<details>
<summary>What key HNSW theoretical proofs support logarithmic complexity?</summary>

Phase: [EXPLORATION]

### Source [56]: https://keyurramoliya.com/posts/Understading-HNSW-Hierarchical-Navigable-Small-World

Query: What key HNSW theoretical proofs support logarithmic complexity?

Answer: The scalability analysis demonstrates HNSW’s logarithmic search complexity through systematic evaluation across datasets of varying sizes. The experiments measure both the number of distance computations and actual query times as functions of dataset size, revealing the algorithmic efficiency gains relative to linear search and competing methods. These results validate the theoretical complexity analysis while highlighting practical performance characteristics. The Hierarchical Navigable Small World algorithm represents a fundamental advancement in approximate nearest neighbor search that has transformed the landscape of similarity search applications. By combining insights from small world network theory with the hierarchical structure of skip lists, HNSW achieves logarithmic search complexity while maintaining practical efficiency and implementation simplicity. The algorithm’s robust performance across diverse datasets, dimensionalities, and distance metrics has established it as the foundation for modern vector databases and large-scale similarity search systems. The construction time complexity of HNSW exhibits favorable scaling properties that make it practical for building indexes on large datasets. Theoretical analysis suggests O(N log N) complexity for construction on relatively low-dimensional data, where N represents the number of elements. This scaling behavior arises because each element insertion requires searching through the existing structure, which takes logarithmic time on average, and this process must be repeated for all N elements.

-----

Phase: [EXPLORATION]

### Source [57]: https://arxiv.org/html/2607.02338v1

Query: What key HNSW theoretical proofs support logarithmic complexity?

Answer: The HNSW index is a hierarchical graph structure approximating the proximity of points in . It consists of a series of layers , where layer contains all data points, and each subsequent layer contains a subset of the points from layer , forming a hierarchy. Formally, an HNSW structure is a tuple of graphs . Each graph is defined such that . The edges connect points within the same layer based on proximity heuristics. The hierarchy allows for logarithmic search complexity by initiating the search at the top layer (coarse granularity) and progressively refining the search region as traversal moves down to layer (fine granularity). Hierarchical Navigable Small World (HNSW) graphs serve as the industry standard due to their logarithmic complexity and strong empirical performance.

-----

Phase: [EXPLORATION]

### Source [58]: https://www.pinecone.io/learn/series/faiss/hnsw

Query: What key HNSW theoretical proofs support logarithmic complexity?

Answer: Navigable small world models are defined as any network with (poly/)logarithmic complexity using greedy routing. The efficiency of greedy routing breaks down for larger networks (1-10K+ vertices) when a graph is not navigable . The routing (literally the route we take through the graph) consists of two phases. We start with the “zoom-out” phase where we pass through low-degree vertices (degree is the number of links a vertex has) — and the later “zoom-in” phase where we pass through higher-degree vertices . HNSW inherits the same layered format with longer edges in the highest layers (for fast search) and shorter edges in the lower layers (for accurate search). Vector search using Navigable Small World (NSW) graphs was introduced over the course of several papers from 2011-14 [4, 5, 6]. The idea is that if we take a proximity graph but build it so that we have both long-range and short-range links, then search times are reduced to (poly/)logarithmic complexity. There is a significant leap in complexity from a ‘proximity’ graph to ‘hierarchical navigable small world’ graph. We will describe two fundamental techniques that contributed most heavily to HNSW: the probability skip list, and navigable small world graphs. The probability skip list was introduced way back in 1990 by William Pugh . It allows fast search like a sorted array, while using a linked list structure for easy (and fast) insertion of new elements (something that is not possible with sorted arrays). Skip lists work by building several layers of linked lists. On the first layer, we find links that skip many intermediate nodes/vertices. As we move down the layers, the number of ‘skips’ by each link is decreased.

-----

Phase: [EXPLORATION]

### Source [59]: https://arxiv.org/html/2501.13992v2

Query: What key HNSW theoretical proofs support logarithmic complexity?

Answer: (Lin & Zhao, 2019) also observed that the hierarchical structure of HNSW fails to achieve the expected logarithmic complexity. Instead, the exhaustive traversal of each layer becomes a bottleneck. As a result, HNSW encounters several inherent problems: (1) a high likelihood of local minima, which grows with the size of the data; (2) weak connectivity between clusters; and (3) slower search times, construction time, making it difficult to achieve logarithmic complexity in practice. Despite its success, HNSW faces several limitations. The first drawback relates to local optimum during the search process. This issue arises from the node insertion mechanism, which inserts nodes into the HNSW graph randomly. Random insertion can result in disconnected regions and weaker inter-cluster connectivity, increasing the likelihood of the search process becoming trapped in local optimum. The second drawback is that the logarithmic complexity 𝒪⁢(n⁢log⁡n)𝒪⁢n⁢log⁡n proposed in the original HNSW paper (Malkov & Yashunin, 2018) is not always achieved in practice. To further accelerate the search and approximate logarithmic complexity in practice, we introduce a method for creating additional skip bridges between upper layers and bottom layer (layer 0) based on LID thresholds (see Fig. 3).

-----

Phase: [EXPLORATION]

### Source [60]: https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world

Query: What key HNSW theoretical proofs support logarithmic complexity?

Answer: Elements are randomly assigned levels, with fewer elements at higher levels. The level distribution follows an exponentially decaying probability. This randomization ensures a balanced structure that can handle dynamic datasets efficiently. The probabilistic tiering in HNSW, where nodes distribute across different layers like skip lists, is governed by a parameter typically denoted as mL. This parameter determines the likelihood of a node appearing in successive layers, with the probability decreasing exponentially as the layers ascend. Each layer is a proximity graph of elements at that level, allowing logarithmic complexity scaling. Higher layers provide a broader overview, while lower layers offer finer details. HNSW operates by creating a multi-layered graph structure where each layer is a simplified, navigable, small world network. This structure allows for remarkably quick and accurate searches, even in vast, high-dimensional data spaces, mainly by use of skip lists. Its foundations relate to approximate nearest neighbors (ANN). ANNs are often used in vector similarity search and can be split into three distinct categories: trees, hashes, and graphs. HNSW can be more specifically categorized as a proximity graph, in which two vertices are linked based on their proximity (closer vertices are linked).

-----

</details>

<details>
<summary>What recent HNSW variants address original 2016 limitations?</summary>

Phase: [EXPLORATION]

### Source [63]: https://redis.io/blog/how-hnsw-algorithms-can-improve-search

Query: What recent HNSW variants address original 2016 limitations?

Answer: HNSW has advantages over many other approaches, but it’s not without its tradeoffs, and some use cases will benefit from other techniques. ### High memory consumption HNSW, due to its graph-based structure, requires much more memory than other ANN methods. With larger amounts of connections per node, HNSW can get even more memory-intensive. Tuning parameter M can help find a balance, and using lower-dimensional embeddings can make functions more efficient, but there still tends to be a practical limit on graph size. ### Index construction overhead

-----

Phase: [EXPLORATION]

### Source [64]: https://www.pinecone.io/learn/series/faiss/hnsw

Query: What recent HNSW variants address original 2016 limitations?

Answer: Y. Malkov, D. Yashunin, Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs (2016), IEEE Transactions on Pattern Analysis and Machine Intelligence Y. Malkov et al., Approximate Nearest Neighbor Search Small World Approach (2011), International Conference on Information and Communication Technologies & Applications Y. Malkov et al., Scalable Distributed Algorithm for Approximate Nearest Neighbor Search Problem in High Dimensional General Metric Spaces (2012), Similarity Search and Applications, pp. 132-147 Y. Malkov et al., Approximate nearest neighbor algorithm based on navigable small world graphs (2014), Information Systems, vol. 45, pp. 61-68

-----

</details>

<details>
<summary>How is HNSW applied in genomics for DNA sequence similarity search?</summary>

Phase: [EXPLORATION]

### Source [65]: https://dfrws.org/wp-content/uploads/2025/05/An-extensible-and-scalable-system-for-hash-lookup-and-approximate-similarity-search-with-similarity-digest-algorithms.pdf

Query: How is HNSW applied in genomics for DNA sequence similarity search?

Answer: The system works in two phases: indexing and querying. During indexing, similarity digests are extracted using a modular SDA interface and stored in the radix tree for exact searches. At the same time, digests are inserted into the HNSW graph, where edges to similar nodes are created based on the calculated similarity scores. The query phase first checks the radix tree for exact matches. If no exact match is found, an approximate similarity search is performed using HNSW, retrieving the K nearest neighbors based on the SDA similarity scores. This combined approach ensures high-speed retrieval of similar files, improving forensic efficiency in identifying duplicate or related artifacts in diverse datasets, from textual documents to binary executables. [...] The radix tree is used to store similarity digests and efficiently retrieve exact matches. Unlike hash tables, it allows for prefix-based searches, making it well suited for detecting partial or hierarchical similarities within structured forensic data. In parallel, HNSW is used for approximate similarity searches, offering a trade-off between speed and accuracy on large-scale datasets. However, existing HNSW implementations assume continuous vector spaces and rely on distance metrics such as Euclidean or cosine similarity. Since SDAs generate discrete hash values with algorithm-specific scoring functions, APOTHEOSIS adapts HNSW to use SDA-derived similarity scores instead of traditional distance-based metrics. [...] As described earlier, APOTHEOSIS leverages two data structures that work together: a custom implementation of radix tree and HNSW. These data structures are combined with similarity digests to enable efficient approximate similarity searches. The APOTHEOSIS database stores all hashes and associated extended information for each hash. By keeping this information separate from the HNSW structure, we maintain a low space complexity for the HNSW graph.

-----

Phase: [EXPLORATION]

### Source [66]: https://escholarship.org/content/qt96h3s2sx/qt96h3s2sx_noSplash_e05e309fdf19eb7f453310a9459acdcc.pdf

Query: How is HNSW applied in genomics for DNA sequence similarity search?

Answer: computed via hashing-like algorithms ( 53–56 ), making the idea of combining them with HNSW even more attractive for various applications that required these other distance metrics (e.g., strings, vectors and text / document). We provide an example in which we used order MinHash to approximate Edit distance for DNA sequences of single genes and visualize them via annembed. This application helps to identify mislabeled taxonomic information in widely used reference sequence databases such as the 16S rRNA gene databases. However, when distance of interest is not a metric distance, HNSW is limited in terms of accuracy, and UMAP based on NN-Descent will be a better option (NN-Descent works for non-metric distance) until recent efforts to generalize HNSW to non-metric distances become more [...] provided that an appropriate distance metric is available. Accordingly, the annembed library is also applied in GSearch ( 26 ), a computer program that uses annembed as a dependency to perform HNSW graph building for millions of microbial genomes, in addition to standalone implementations. Annembed is written in Rust and it is fully parallelized for almost all steps. Materials and methods Overall, our implementation is a mixture of HNSW with previously described embedding algorithms such as UMAP and t-SNE. First, the graph is initialized by the HNSW algorithm (Figure 1 A), which provides sub-sampling of the data to be embedded by considering only less densely occupied layers (i.e., the upper layers). This corresponds generally to a sub-sampling of 2–4% of the total data but the small [...] to a sub-sampling of 2–4% of the total data but the small fraction of data used is not problematic as the distance between the points left out by the subsampling and their nearest sampled neighbor are known in the complete HWSW graph. The HNSW NAR Genomics and Bioinformatics , 2024, Vol. 6, No. 4 3 A B D C Figure 1. Overall description of annembed algorithm’s key steps and functionalities. ( A ) Build a HNSW graph from scratch by gradually adding points in the database in a recursive way with random initialization. When maximum number of allowed neighbors in the graph is reached (M) for each existing point, a representative will be chosen as new point in new layers (above) by collapsing the neighbors. Finding neighbors for a newly added point involves inserting the point into the graph

-----

</details>

<details>
<summary>What emerging hardware accelerations optimize HNSW for edge computing devices?</summary>

Phase: [EXPLORATION]

### Source [67]: https://pmc.ncbi.nlm.nih.gov/articles/PMC12568237

Query: What emerging hardware accelerations optimize HNSW for edge computing devices?

Answer: ON-NSW redesigns HNSW for GPU on edge devices, with a focus on parallelism and memory hierarchy optimization. ON-NSW employs a flat graph structure derived from HNSW to fully exploit GPU parallelism. In addition, it carefully places HNSW components in the unified memory. The original HNSW was designed for high-end CPUs and discrete GPUs, and therefore does not fully exploit the architectural characteristics of edge devices. In particular, NVIDIA Jetson devices employ a unified memory hierarchy in which CPUs and GPUs share the same DRAM space. This feature requires careful design of data placement and memory access policies to fully exploit the device’s performance. These limitations of the original HNSW motivate our GPU-optimized redesign for edge devices.

-----

Phase: [EXPLORATION]

### Source [68]: https://arxiv.org/html/2502.18113v1

Query: What emerging hardware accelerations optimize HNSW for edge computing devices?

Answer: Specialized hardware like GPUs (Zhao et al., 2020), FPGAs (Jiang et al., 2024; Zeng et al., 2023; Peng et al., 2021), Compute Express Link (CXL) (Jang et al., 2023), Non-Volatile Memory (NVM) (Ren et al., 2020), NVMe SSDs (Wang et al., 2024b), and SmartSSDs (Tian et al., 2024) accelerate distance computation and optimize the HNSW index layout, achieving superior performance through software-hardware collaboration.

-----

Phase: [EXPLORATION]

### Source [69]: https://www.usenix.org/system/files/hotedge20_paper_zhou-xingyu.pdf

Query: What emerging hardware accelerations optimize HNSW for edge computing devices?

Answer: For the hardware devices used, FPGAs show both highest absolute computation power and highest energy efficiency. This makes it a good option for flexible acceleration tasks at the edge. However, for relatively low pressure scenarios, the device costs could be dominant and FPGAs are harder to program. For machine learning inference tasks, server-side GPUs can have the most computation power and higher energy efficiency than CPUs and some lightweight edge devices. Thus, embedded GPUs like Jetson Nano could have much potential for more general.

-----

Phase: [EXPLORATION]

### Source [70]: https://www.dre.vanderbilt.edu/~gokhale/WWW/papers/HotEdge20_HWAccelReco.pdf

Query: What emerging hardware accelerations optimize HNSW for edge computing devices?

Answer: To that end, hardware acceleration technologies, such as field programmable gate arrays (FPGAs), graphical processing units (GPUs) and application specific integrated circuits(ASICs) among others, have shown significant promise for edge computing. For the hardware devices used, FPGAs show both highest absolute computation power and highest energy efficiency. This makes it a good option for flexible acceleration tasks at the edge.

-----

Phase: [EXPLORATION]

### Source [71]: https://www.vldb.org/pvldb/vol18/p3797-jiang.pdf

Query: What emerging hardware accelerations optimize HNSW for edge computing devices?

Answer: While previous research has explored hardware accelerator designs for GVS based on FPGA prototyping [80, 103], these approaches have three main limitations. Firstly, they only support the Hierarchical Navigable Small World (HNSW) graph. While HNSW is widely used today, more efficient graph construction algorithms are emerging that offer improved recall [28, 70, 72, 73, 81, 107, 111]. Two recent studies [80, 103] implemented HNSW, a popular GVS algorithm, on FPGAs. Peng et al. presented the first FPGA-based implementation, while Zeng et al. further optimized the design by introducing data prefetching and enabling multi-FPGA search.

-----

</details>

<details>
<summary>How do small world principles from HNSW apply to social media recommendation algorithms?</summary>

Phase: [EXPLORATION]

### Source [72]: https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world

Query: How do small world principles from HNSW apply to social media recommendation algorithms?

Answer: HNSW has been utilized in collaborative filtering algorithms to efficiently find similar users or items based on their features or rating vectors. By constructing an HNSW graph, similarity-based recommendations can be generated with sub-linear time complexity, enabling real-time personalized recommendations in large-scale systems. This application of HNSW enhances the accuracy and scalability of recommendation systems. HNSW has been successfully employed in music recommendation systems, where the goal is to suggest songs or playlists based on user preferences. By representing songs as feature vectors capturing their audio characteristics, HNSW enables fast retrieval of similar songs. With its efficient vector database and multi-layer structure, HNSW can handle large music collections and quickly provide recommendations based on users' listening history or preferences.

-----

Phase: [EXPLORATION]

### Source [73]: https://redis.io/blog/how-hnsw-algorithms-can-improve-search

Query: How do small world principles from HNSW apply to social media recommendation algorithms?

Answer: Think of the "six degrees of Kevin Bacon" game: everyone is connected by just a few people. That same principle powers hierarchical navigable small world (HNSW) algorithms, which link data points so queries can reach the right match in far fewer hops. HNSW combines a hierarchy of layers with networks of navigable small worlds, allowing for scalable, high-performant search. HNSW has emerged as the leading ANN approach for high-dimensional vector search—whether you’re building similarity search, recommendation engines, or AI applications—because it balances speed, accuracy, and scalability better than alternatives. By organizing data into layered graphs, HNSW dramatically reduces search complexity while maintaining high recall, making it the go-to choice for enterprise-scale workloads.

-----

Phase: [EXPLORATION]

### Source [74]: https://www.velodb.io/glossary/the-backbone-of-approximate-nearest-neighbor-search

Query: How do small world principles from HNSW apply to social media recommendation algorithms?

Answer: HNSW is rooted in the Small-World Network model—a special type of graph characterized by having a short distance between any two nodes, much like the "six degrees of separation" idea. Navigable Small World (NSW): The precursor to HNSW creates a graph where vectors are nodes and edges connect close neighbors. The search is a greedy process: from any starting point, the search moves to the neighbor that is closest to the query vector, effectively finding a short path toward the target. This structure ensures a small number of "hops" is often sufficient to reach the target region. HNSW's genius lies in its ability to navigate vast, high-dimensional spaces efficiently, borrowing ideas from graph theory and probabilistic data structures.

-----

</details>

<details>
<summary>What role does HNSW play in the shift toward multimodal embedding search systems?</summary>

Phase: [EXPLORATION]

### Source [76]: https://arxiv.org/html/2405.17813v1

Query: What role does HNSW play in the shift toward multimodal embedding search systems?

Answer: To bridge the gap between benchmarks and contemporary applications, our research studies the behaviour of HNSW search across vector spaces produced with various methods including synthetic data, popular retrieval benchmarks with popular text embedding models, and real-world e-commerce data with multimodal embeddings from CLIP models. Vector search systems, pivotal in AI applications, often rely on the Hierarchical Navigable Small Worlds (HNSW) algorithm. However, the behaviour of HNSW under real-world scenarios using vectors generated with deep learning models remains under-explored. Existing Approximate Nearest Neighbours (ANN) benchmarks and research typically has an over-reliance on simplistic datasets like MNIST or SIFT1M and fail to reflect the complexity of current use-cases. Our investigation focuses on HNSW’s efficacy across a spectrum of datasets, including synthetic vectors tailored to mimic specific intrinsic dimensionalities, widely-used retrieval benchmarks with popular embedding models, and proprietary e-commerce image data with CLIP models. We survey the most popular HNSW vector databases and collate We discover that the recall of approximate HNSW search, in comparison to exact K Nearest Neighbours (KNN) search, is linked to the vector space’s intrinsic dimensionality and significantly influenced by the data insertion sequence. Our methodology highlights how insertion order, informed by measurable properties such as the pointwise Local Intrinsic Dimensionality (LID) or known categories, can shift recall by up to 12 percentage points. We also observe that running popular benchmark datasets with HNSW instead of KNN can shift rankings by up to three positions for some models. This work underscores the need for more nuanced benchmarks and design considerations in developing robust vector search systems using approximate vector search algorithms. This study presents a number of scenarios

-----

Phase: [EXPLORATION]

### Source [78]: https://redis.io/blog/how-hnsw-algorithms-can-improve-search

Query: What role does HNSW play in the shift toward multimodal embedding search systems?

Answer: ## What is a hierarchical navigable small world (HNSW)?

Hierarchical navigable small world, or HNSW, is a graph-based ANN algorithm that combines navigable small worlds (networks of points where each point is connected to its nearest neighbors) and hierarchy (layers that refine search to support speed). Researchers Yu A. Malkov and D. A. Yashunin introduced the idea in the 2016 paper, “Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs.” [...] June 10, 202511 minute read

Image

Jim Allen Wallace

Think of the "six degrees of Kevin Bacon" game: everyone is connected by just a few people. That same principle powers hierarchical navigable small world (HNSW) algorithms, which link data points so queries can reach the right match in far fewer hops.

Modern applications frequently deal with high-dimensional data—embeddings of images, text, and more. A brute-force k-Nearest Neighbors (KNN) search becomes impractical as dimensionality increases, which is why approximate nearest neighbors (ANN) algorithms trade slight accuracy for much better speed. But not all ANN algorithms are created equal. Many introduce latency issues and scalability bottlenecks that limit their usefulness. [...] Image recognition and retrieval, where search functions have to search across high-dimensional vectors.
 Natural language processing (NLP), where it can support semantic and similarity search functions.
 Recommendation engines, where it can suggest a relevant product for a shopper or highlight the best paragraph from a help center to assist a user with troubleshooting.
 Anomaly detection, where it can support search across large datasets to detect fraud and monitor networks.

HNSW is growing in popularity because it’s better than most other ANN algorithms at supporting high-dimensional vector searches—a broad use case that’s only becoming more high-priority with the rise of AI.

## How Does HNSW Work?

-----

Phase: [EXPLORATION]

### Source [79]: https://www.tigerdata.com/blog/vector-database-basics-hnsw

Query: What role does HNSW play in the shift toward multimodal embedding search systems?

Answer: Despite its memory-intensive nature and challenges in scaling large datasets, HNSW's benefits in facilitating rapid and accurate searches are undeniable. For those ready to integrate HNSW into their projects, whether through SQL commands or the Python-based Timescale library, the process is straightforward yet powerful. With just a line of code, you can unlock the potential of your vector data, enhancing your applications' search capabilities.

Working with scaling datasets? Install the pgvectorscale PostgreSQL extension and start building more scalable AI applications with higher-performance embedding search and cost-efficient storage.

For production hybrid search combining pgvector with BM25 see Tiger Data Search.

// Related posts

Great Models Aren't Enough for Physical AI [...] 3. Configurability for high recall and speed: HNSW offers exceptional configurability, allowing it to be tuned for high recall—the ability to retrieve the most relevant results—without significantly compromising search speed. This balance is particularly valuable in scenarios where the accuracy of search results is paramount, and results need to be obtained quickly. [...] TimescaleDB, an extension of PostgreSQL designed to handle time-series data, events, and analytics, also extends its functionality to support vector operations through pgvector. Implementing HNSW indexing for your vector data stored in a PostgreSQL database can significantly enhance search performance.

Here's how you can create an HNSW index on a table's embedding column in SQL:

`CREATE INDEX document_embedding_idx ON document_embedding USING hnsw(embedding vector_cosine_ops);`

This command creates an HNSW index named `document_embedding_idx` for the `document_embedding` table on the `embedding` column using cosine similarity operations (`vector_cosine_ops`). This index facilitates efficient nearest-neighbor searches using the HNSW algorithm's speed and accuracy.

-----

</details>

<details>
<summary>What mathematical proofs validate HNSW probabilistic layer assignment minimizing overlap?</summary>

Phase: [EXPLORATION]

### Source [80]: https://www.pinecone.io/learn/series/faiss/hnsw

Query: What mathematical proofs validate HNSW probabilistic layer assignment minimizing overlap?

Answer: The creators of HNSW found that the best performance is achieved when we minimize the overlap of shared neighbors across layers. Decreasing m_L can help minimize overlap (pushing more vectors to layer 0), but this increases the average number of traversals during search. So, we use an m_L value which balances both. A rule of thumb for this optimal value is `1/ln(M)` . Graph construction starts at the top layer. After entering the graph the algorithm greedily traverse across edges, finding the ef nearest neighbors to our inserted vector q — at this point ef = 1. After finding the local minimum, it moves down to the next layer (just as is done during search). This process is repeated until reaching our chosen insertion layer. Here begins phase two of construction. [...] Here we are building two vectors — `assign_probas`, the probability of insertion at a given layer, and `cum_nneighbor_per_level`, the cumulative total of nearest neighbors assigned to a vertex at different insertion levels. In: ``` assign_probas, cum_nneighbor_per_level = set_default_probas( 32, 1/np.log(32) ) assign_probas, cum_nneighbor_per_level ``` Out: ``` ([0.96875, 0.030273437499999986, 0.0009460449218749991, 2.956390380859371e-05, 9.23871994018553e-07, 2.887099981307982e-08], [64, 96, 128, 160, 192, 224]) ``` [...] ``` def random_level(assign_probas: list, rng): # get random float from 'r'andom 'n'umber 'g'enerator f = rng.uniform() for level in range(len(assign_probas)): # if the random float is less than level probability... if f < assign_probas[level]: # ... we assert at this level return level # otherwise subtract level probability and try again f -= assign_probas[level] # below happens with very low probability return len(assign_probas) - 1 ``` We generate a random float using Numpy’s random number generator `rng` (initialized below) in `f`. For each `level`, we check if `f` is less than the assigned probability for that level in `assign_probas` — if so, that is our insertion layer.

-----

Phase: [EXPLORATION]

### Source [81]: https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37

Query: What mathematical proofs validate HNSW probabilistic layer assignment minimizing overlap?

Answer: The number of layers l for every node is chosen randomly with exponentially decaying probability distribution. Distribution of the number of layers based on normalization factor mL. The horizontal axis represents values of the uniform(0, 1) distribution. To achieve the optimum performance advantage of the controllable hierarchy, the overlap between neighbors on different layers (i.e. percent of element neighbors that are also belong to other layers) has to be small. – Yu. A. Malkov, D. A. Yashunin. [...] One of the ways to decrease the overlap is to decrease mL. But it is important to keep in mind that reducing mL also leads on average to more traversals during a greedy search on each layer. That is why it is essential to choose such a value of mL that will balance both the overlap and the number of traversals. The authors of the paper propose choosing the optimal value of mL which is equal to 1 / ln(M). This value corresponds to the parameter p = 1 / M of the skip list being an average single element overlap between the layers. ### Insertion After a node is assigned the value l, there are two phases of its insertion: [...] ## Construction ### Choosing the maximum layer Nodes in HNSW are inserted sequentially one by one. Every node is randomly assigned an integer l indicating the maximum layer at which this node can present in the graph. For example, if l = 1, then the node can only be found on layers 0 and 1. The authors select l randomly for each node with an exponentially decaying probability distribution normalized by the non-zero multiplier mL (mL = 0 results in a single layer in HNSW and non-optimized search complexity). Normally, the majority of l values should be equal to 0, so most of the nodes are present only on the lowest level. The larger values of mL increase the probability of a node appearing on higher layers.

-----

</details>

<details>
<summary>How should HNSW entry points be dynamically updated for streaming data insertions?</summary>

Phase: [EXPLORATION]

### Source [82]: https://www.mongodb.com/resources/basics/hierarchical-navigable-small-world

Query: How should HNSW entry points be dynamically updated for streaming data insertions?

Answer: Insertions and deletions in the HNSW graph ensure its dynamic adaptability and robustness in handling high-dimensional datasets based on entry points and distance metrics. When a new node is added for the graph construction, the algorithm first determines its position in the hierarchical structure depending on where the node appears and the maximum number of nodes. This process involves identifying the pre-defined entry point for the node based on the probabilistic tiering governed by the parameter mL. Insertions and deletions play pivotal roles in maintaining the dynamic adaptability and robustness of the graph, particularly when dealing with high-dimensional datasets, given their memory consumption. Leveraging cosine similarity as a metric for measuring distances between nodes, the HNSW creates efficient insertions and deletions among top layer and next layer to find the optimal value, reinforcing its capability for dynamic and accurate nearest neighbor searches in high-dimensional datasets as well as considering memory usage or memory footprint. In HNSW, each point is connected to others within its level and to higher levels, creating a hierarchical structure. This graph stores connections and metadata like nearest neighbors and distances, aiding in pattern analysis. Additional data structures, such as priority queues or hash tables, help streamline tasks like insertion and deletion.

-----

Phase: [EXPLORATION]

### Source [83]: https://arxiv.org/html/2407.07871v2

Query: How should HNSW entry points be dynamically updated for streaming data insertions?

Answer: The above-described processes are implemented within the HNSW source code, particularly encompassing the functions addPoint, updatePoint, and repairConnectionsForUpdate. The significance of the replaced_update method lies in its ability to manage the index efficiently. Without it, inserting new data points would leave deleted entries in the index, wasting storage and causing unnecessary expansion. By using replaced_update, deleted points’ storage is reused for new insertions, preventing the index from growing excessively and maintaining efficient space utilization. Insertion. Algorithms 2 and 3, collectively called Mutual Neighbor Replaced Update (MN-RU), update the HNSW index when a new point replaces a deleted one. First, Algorithm 2 repairs the graph’s connectivity, then Algorithm 3 inserts the new point to the index. Unlike the conventional approach of adding new points, the Algorithm 3 enables the new point to inherit the layer level of the deleted point. Subsequent to this inheritance, the new point undergoes insertion using the standard HNSW insert process. Algorithm 3 starts by identifying the top layer of the HNSW index and the maximum layer of the deleted point, establishing an initial entry point for the search. From the top layer to the layer above the deleted point’s maximum layer, it iteratively searches for the nearest point as the

-----

Phase: [EXPLORATION]

### Source [84]: https://www.tigerdata.com/blog/vector-database-basics-hnsw

Query: How should HNSW entry points be dynamically updated for streaming data insertions?

Answer: This design improves search efficiency in high-dimensional spaces and supports incremental updates, making HNSW particularly well-suited for dynamic datasets where data points frequently change. In summary, HNSW's optimized approach to organizing and searching high-dimensional data leverages the principles of navigable small-world networks and skip lists, introducing long edges to facilitate rapid navigation. This structure significantly overcomes the limitations of traditional graph indexing techniques, offering a scalable, dynamic, and efficient solution for approximate nearest-neighbor search. HNSW's adaptability to dynamic datasets—it efficiently manages inserts and deletes without necessitating a complete rebuild of the index. This dynamic nature is pivotal for continuously evolving applications, requiring the index to be as fluid as the data it represents. HNSW addresses these issues through its multi-layered, hierarchical approach. It allows for efficient search by reducing the dimensionality at each layer and dynamically adjusting the graph's structure without needing complete rebuilds.

-----

Phase: [EXPLORATION]

### Source [85]: https://www.pinecone.io/learn/series/faiss/hnsw

Query: How should HNSW entry points be dynamically updated for streaming data insertions?

Answer: To initialize the HNSW index we write: # setup our HNSW parameters d = 128 # vector size M = 32 index = faiss.IndexHNSWFlat(d, M) With this, we have set our M parameter — the number of neighbors we add to each vertex on insertion, but we’re missing M_max and M_max0. M In Faiss, these two parameters are set automatically in the set_default_probas method, called at index initialization. The M_max value is set to M, and M_max0 set to M2 (find further detail in the notebook). set_default_probas M M2 Before building our index with index.add(xb), we will find that the number of layers (or levels in Faiss) are not set: After finding the local minimum, it moves down to the next layer (just as is done during search). This process is repeated until reaching our chosen insertion layer. Here begins phase two of construction. The ef value is increased to efConstruction (a parameter we set), meaning more nearest neighbors will be returned. In phase two, these nearest neighbors are candidates for the links to the new inserted element q and as entry points to the next layer. efConstruction M neighbors are added as links from these candidates — the most straightforward selection criteria are to choose the closest vectors. We will be modifying three parameters: M, efSearch, and efConstruction. And we will be indexing the Sift1M dataset, which you can download and prepare using this script. M efSearch efConstruction As we did before, we initialize our index like so: index = faiss.IndexHNSWFlat(d, M) The two other parameters, efConstruction and efSearch can be modified after we have initialized our index. efConstruction efSearch index index.hnsw.efConstruction = efConstruction index.add(xb) # build the index index.hnsw.efSearch = efSearch # and now we can search index.search(xq[:1000], k=1) Our efConstruction value must be set before we construct the index via index.add(xb), but efSearch can be set anytime before searching. efConstruction index.add(xb) efSearch

-----

Phase: [EXPLORATION]

### Source [86]: https://redis.io/blog/how-hnsw-algorithms-can-improve-search

Query: How should HNSW entry points be dynamically updated for streaming data insertions?

Answer: HNSW, due to the hierarchy it requires, can be computationally expensive, and the queries run using it can be time-consuming. For every new point, HNSW performs a greedy search to find the best neighbors and updates the graph by inserting connections—a process that it has to repeat for every new point. Tuning efConstruction, which controls the thoroughness of the search, can allow you to dial in the best balance of indexing time vs. accuracy. Similarly, using parallel index construction, which allows you to use multi-threading, can make the work less intensive. As a result, database products that offer parallelized index construction, incremental updates, and easily configurable efConstruction can be best for companies looking to reduce indexing time. There will never be a balance that’s perfect for all contexts. Instead, finding the right balance will require looking closely at the use case at hand. Generally speaking, you can tune to the right balance by starting with the defaults, measuring recall and latency on a validation data set, increasing efSearch if recall is low, and increasing M and efConstruction if recall remains too low. Incremental tuning allows you to find the right level of recall without overburdening performance. Database products that offer dynamic search tuning, optimized query execution, and adaptive indexing strategies can help you further balance recall and response times. Unlike other ANN algorithms, which tend to require an exhaustive and often slow search, HNSW provides a graph that minimizes hops from point to point and a hierarchy that doesn’t require many distance computations. The combination of the two is what makes HNSW stand apart from other ANN algorithms: One study found that, in comparison to other ANN algorithms, “Over all recall values, HNSW is fastest.” HNSW algorithms also tend to outcompete ANN algorithms in practical terms. Many ANN methods require a training phase, but HNSW doesn’t, meaning teams can build the HNSW incrementally and update it over time.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="down-with-the-hierarchy-the-h-in-hnsw-stands-for-hubs.md">
<details>
<summary>Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”</summary>

Phase: [EXPLORATION]

**Source URL:** <https://arxiv.org/html/2412.01940v2>

# Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”

Blaise Munyampirwa
Independent ResearcherMountain ViewCA[blaisemunyampirwa@gmail.com](mailto:blaisemunyampirwa@gmail.com), Vihan Lakshman
MIT CSAILCambridgeMA[vihan@mit.edu](mailto:vihan@mit.edu) and Benjamin Coleman
Google DeepMindMountain ViewCA[colemanben@google.com](mailto:colemanben@google.com)

###### Abstract.

Driven by recent breakthrough advances in neural representation learning, approximate near-neighbor (ANN) search over vector embeddings has emerged as
a critical computational workload. With the introduction of the seminal Hierarchical Navigable Small World (HNSW) algorithm, graph-based indexes have established themselves as the overwhelmingly dominant paradigm for efficient and scalable ANN search. As the name suggests, HNSW searches a layered hierarchical graph to quickly identify neighborhoods of similar points to a given query vector. But is this hierarchy even necessary? A rigorous experimental analysis to answer this question would provide valuable insights into the nature of algorithm design for ANN search and motivate directions for future work in this increasingly crucial domain. To that end, we conduct an extensive benchmarking study covering more large-scale datasets than prior investigations of this question. We ultimately find that a flat navigable small world graph graph retains all of the benefits of HNSW on high-dimensional datasets, with latency and recall performance essentially _identical_ to the original algorithm but with less memory overhead. Furthermore, we go a step further and study _why_ the hierarchy of HNSW provides no benefit in high dimensions, hypothesizing that navigable small world graphs contain a well-connected, frequently traversed “highway” of hub nodes that maintain the same purported function as the hierarchical layers. We present compelling empirical evidence that the _Hub Highway Hypothesis_ holds for real datasets and investigate the mechanisms by which the highway forms. The implications of this hypothesis may also provide future research directions in developing enhancements to graph-based ANN search.

## 1\. Introduction

Near neighbor search is a fundamental problem in computational geometry that lies at the heart of countless practical applications. From industrial-scale recommendation (Feng et al., [2022](https://arxiv.org/html/2412.01940v2#bib.bib15 "")) to retrieval-augmented generation (Lewis et al., [2020](https://arxiv.org/html/2412.01940v2#bib.bib28 "")) and even to computational biology (Zhao et al., [2024](https://arxiv.org/html/2412.01940v2#bib.bib51 "")), numerous data-intensive tasks utilize similarity search at some location in the stack.
As a result, similarity indexes are very well-studied
(Guo et al., [2019](https://arxiv.org/html/2412.01940v2#bib.bib18 ""); Malkov and Yashunin, [2016](https://arxiv.org/html/2412.01940v2#bib.bib33 ""); Johnson et al., [2017](https://arxiv.org/html/2412.01940v2#bib.bib26 ""); Aguerrebere et al., [2023](https://arxiv.org/html/2412.01940v2#bib.bib2 ""); Jayaram Subramanya et al., [2019](https://arxiv.org/html/2412.01940v2#bib.bib24 "")) with multiple large-scale benchmarks and leaderboards to compare techniques
(Aumüller et al., [2018](https://arxiv.org/html/2412.01940v2#bib.bib4 ""); Simhadri et al., [2022](https://arxiv.org/html/2412.01940v2#bib.bib43 "")).

Historically, the state-of-the-art for near neighbor search involved constructing sophisticated tree-based data structures, such as k⁢d𝑘𝑑kditalic\_k italic\_d-trees (Bentley, [1975](https://arxiv.org/html/2412.01940v2#bib.bib5 "")) and cover trees (Beygelzimer et al., [2006](https://arxiv.org/html/2412.01940v2#bib.bib7 "")), that guaranteed exact solutions while avoiding a brute-force examination of all points. However, the recent advent of large-scale neural representation learning, including large language models (LLMs), places a significant strain on these classical methods that were developed to target a much lower-dimensional search space. In response, the community has turned to approximate search methods. While alternative approximate indexing methods such as locality-sensitive hashing (Indyk and Motwani, [1998](https://arxiv.org/html/2412.01940v2#bib.bib19 "")) and product quantization (Jegou et al., [2010](https://arxiv.org/html/2412.01940v2#bib.bib25 "")), have garnered significant interest, graph-based approaches generally achieve the strongest performance on established ANN benchmarks (Aumüller et al., [2018](https://arxiv.org/html/2412.01940v2#bib.bib4 ""); Simhadri et al., [2022](https://arxiv.org/html/2412.01940v2#bib.bib43 "")). Introduced in 2016, the Hierarchical Navigable Small World (HNSW) algorithm (Malkov and Yashunin, [2016](https://arxiv.org/html/2412.01940v2#bib.bib33 "")), emerged as one of the first high-performance graph-based search indexes at scale and still enjoys immense popularity to this day with over 4300 Github stars111 [https://github.com/nmslib/hnswlib](https://github.com/nmslib/hnswlib "").

As the name implies, a core feature of the HNSW index is its hierarchically layered graph akin to a skip list (Pugh, [1990](https://arxiv.org/html/2412.01940v2#bib.bib39 "")) where the search process iteratively traverses through graphs of increasing density before converging to a neighborhood of similar points in the final graph layer. By drawing intuition from skip lists, the HNSW authors argue that the initial coarse graph layers allow for efficiently identifying the neighborhood of similar points in the collection through fewer overall comparisons.

Despite the immense popularity of HNSW, however, the algorithm suffers from multiple scalability bottlenecks. For instance, the hierarchical layers introduce a hefty memory overhead. Moreover, Malkov and Yashunin ( [2016](https://arxiv.org/html/2412.01940v2#bib.bib33 "")) also note in Section 6 of their paper that the hierarchy can reduce the overall system throughput in distributed settings when compared to a flat NSW graph.

While the high cost of this hierarchy in HNSW is traditionally justified by the low latency of graph-based indexes, we ask the question of whether the hierarchy is even necessary in the first place. A growing body of results suggest that the hierarchy may be a vestigial artifact left behind by the lower-dimensional problems of the past. For example, Lin and Zhao ( [2019](https://arxiv.org/html/2412.01940v2#bib.bib29 "")) published a set of experiments suggesting that the hierarchical component of HNSW is only beneficial for low-dimensional inputs (d<32𝑑32d<32italic\_d < 32). Other recent works have observed similar problems with the hierarchy. For example, Coleman et al. ( [2022](https://arxiv.org/html/2412.01940v2#bib.bib9 "")) present an ablation study showing the same behavior in the appendix of their paper. This behavior seems to be an increasingly well-known “folklore” of the similarity search community, but there is currently an absence of a thorough investigation and analysis of this phenomenon.

An exhaustive benchmark comparison on the utility of the HNSW hierarchy would go a long way towards improving our understanding of graph-based similarity search in high-dimensional space and inform future research directions in developing improvements. However, there are several key difficulties with executing such a benchmarking study. The first issue is that running a meaningful ablation study requires first engineering a similarity search implementation over a flat NSW graph that reaches performance parity with HNSW and other state of the art approaches (Douze et al., [2024](https://arxiv.org/html/2412.01940v2#bib.bib13 ""); Sun et al., [2024](https://arxiv.org/html/2412.01940v2#bib.bib44 ""); Jayaram Subramanya et al., [2019](https://arxiv.org/html/2412.01940v2#bib.bib24 "")). This is an increasingly nontrivial task, as the community has invested significant performance engineering efforts into these codebases such that a non-expert implementation has little hope of being competitive.

The second challenge is designing benchmarking experiments in a manner that avoids the confounding effect of the performance of a particular software _implementation_ when making conclusions about the efficacy of the _algorithm_.
Finally, benchmarking near-neighbor search can be highly nuanced. For example, it is possible that hierarchical structures are strongly beneficial for isolated slices of the input. These may sharply reduce the 99th percentile latency while not affecting the median.

Perhaps most importantly, we still have no satisfactory understanding of _why hierarchy does not help_.
Hierarchical structures are a mainstay of algorithm design, where a common trick is to reduce an O⁢(n)𝑂𝑛O(n)italic\_O ( italic\_n ) search process to a sublinear one by traversing a (balanced) hierarchy (Pugh, [1990](https://arxiv.org/html/2412.01940v2#bib.bib39 ""); Guibas and Sedgewick, [1978](https://arxiv.org/html/2412.01940v2#bib.bib17 ""); Mikolov et al., [2013](https://arxiv.org/html/2412.01940v2#bib.bib35 ""); Cormen et al., [2022](https://arxiv.org/html/2412.01940v2#bib.bib10 "")). Arguably, it is counterintuitive for this idea to fail to hold in the context of high-dimensional similarity search – especially when we have strong positive results that hierarchy _helps_ in low dimensions (Beygelzimer et al., [2006](https://arxiv.org/html/2412.01940v2#bib.bib7 ""); Dolatshah et al., [2015](https://arxiv.org/html/2412.01940v2#bib.bib12 ""); Ram and Sinha, [2019](https://arxiv.org/html/2412.01940v2#bib.bib41 ""); Lin and Zhao, [2019](https://arxiv.org/html/2412.01940v2#bib.bib29 "")). Thus, an exhaustive benchmark and deeper analysis into the necessity of the hierarchy in HNSW would shed further light on the nature of algorithm design in high-dimensional spaces and thus may be of independent interest to the community as well.

https://arxiv.org/html/2412.01940v2/extracted/6171912/images/hub_highway_hypothesis.png

Figure 1. We hypothesize that in high dimensions, graph-based ANN indexes naturally form a “highway-feeder” structure, where a small subset of nodes and edges are easily reached, well-connected, and heavily traversed.

### 1.1. Contributions

In this paper, we address the question of whether the hierarchical component of HNSW is truly necessary. Our central research question is, “Can we achieve the same performance on large-scale benchmarks with simply a flat navigable small world graph?” In summary, we make the following contributions:

Benchmarking the hierarchy: We rigorously benchmark HNSW to understand whether the hierarchy is necessary. To do so, we reproduce and extend the hierarchy ablations of previous studies, finding that, on high-dimensional vector datasets, it is indeed beneficial to remove the ‘H’ from HNSW.

Why does hierarchy not help? We hypothesize that the hierarchy benefits decrease in high-dimensions due to hubness.
Hubness is a high-dimensional phenomenon that causes a skewed distribution in the near-neighbor lists of search queries (Radovanovic et al., [2010](https://arxiv.org/html/2412.01940v2#bib.bib40 "")).
We hypothesize that hubness leads to preferential attachment in the similarity search graph, inducing the formation of _easily-traversed highways_ that connect disparate regions of the graph.
This hypothesis, which we call the Hub Highway Hypothesis, explains why we no longer need the hierarchy in high dimensions; we can simply traverse the intrinsic highway structure that naturally forms in high-dimensional spaces. To that end, we conduct a series of experiments to investigate the hub-highway hypothesis. Our results ultimately support this hypothesis, showing that hubness is responsible for driving the connectivity of similarity search graphs.
This insight opens up exciting new research directions in graph construction, link pruning, and graph traversal.

Our specific contributions are as follows.

- •

We release an implementation for a flattened version of HNSW222 [https://github.com/nmslib/hnswlib](https://github.com/nmslib/hnswlib ""), called FlatNav333 [https://github.com/BlaiseMuhirwa/flatnav](https://github.com/BlaiseMuhirwa/flatnav ""), that reaches performance parity with the original version with considerable memory savings.

- •

We demonstrate that hierarchy does not improve performance in either the median or tail latency case by building HNSW and FlatNav indexes over 13 popular benchmark datasets ranging in size from 1 million to 100 million vectors.

- •

We conduct an analysis of hubness phenomena in high-dimensional metric spaces and the resulting HNSW graphs, finding strong empirical support for the hub-highway hypothesis.

Practical implications: Our benchmarks reveal that HNSW can be significantly optimized for modern high-dimensional embedding workloads. For instance, our implementation saves roughly 38%percent3838\\%38 % and 39%percent3939\\%39 % of peak memory consumption on two Big-ANN benchmark datasets compared to hnswlib (and sizable further headroom is likely). Our results confirm the folklore of the similarity search community, conclusively demonstrating that we can remove the hierarchy on high-dimensional inputs with impunity.

## 2\. Background: Similarity Search & HNSW

In the similarity search (or k𝑘kitalic\_k-NNS) problem, we are interested in retrieving k𝑘kitalic\_k elements from a dataset 𝒟={𝕩i,…,𝕩n}⊂ℝd𝒟subscript𝕩𝑖…subscript𝕩𝑛superscriptℝ𝑑\\mathcal{D}=\\{\\mathbb{x}\_{i},\\ldots,\\mathbb{x}\_{n}\\}\\subset\\mathbb{R}^{d}caligraphic\_D = { blackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT , … , blackboard\_x start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT } ⊂ blackboard\_R start\_POSTSUPERSCRIPT italic\_d end\_POSTSUPERSCRIPT that minimize the distance to a given query q∈ℝd𝑞superscriptℝ𝑑q\\in\\mathbb{R}^{d}italic\_q ∈ blackboard\_R start\_POSTSUPERSCRIPT italic\_d end\_POSTSUPERSCRIPT (or, equivalently, maximize the vector similarity). More precisely, given a similarity function ϕ:ℝd×ℝd→ℝ,:italic-ϕ→superscriptℝ𝑑superscriptℝ𝑑ℝ\\phi:\\mathbb{R}^{d}\\times\\mathbb{R}^{d}\\to\\mathbb{R},italic\_ϕ : blackboard\_R start\_POSTSUPERSCRIPT italic\_d end\_POSTSUPERSCRIPT × blackboard\_R start\_POSTSUPERSCRIPT italic\_d end\_POSTSUPERSCRIPT → blackboard\_R , the nearest neighbor 𝕩∗∈𝒳superscript𝕩𝒳\\mathbb{x}^{\*}\\in\\mathcal{X}blackboard\_x start\_POSTSUPERSCRIPT ∗ end\_POSTSUPERSCRIPT ∈ caligraphic\_X of q𝑞qitalic\_q is defined as

| | | |
| --- | --- | --- |
| | 𝕩∗≔arg⁢max𝕩i∈𝒟⁡ϕ⁢(𝕩i,q)≔superscript𝕩subscriptargmaxsubscript𝕩𝑖𝒟italic-ϕsubscript𝕩𝑖𝑞\\mathbb{x}^{\*}\\coloneqq\\operatorname\*{arg\\,max}\_{\\mathbb{x}\_{i}\\in\\mathcal{D}}%<br>\\phi(\\mathbb{x}\_{i},q)blackboard\_x start\_POSTSUPERSCRIPT ∗ end\_POSTSUPERSCRIPT ≔ start\_OPERATOR roman\_arg roman\_max end\_OPERATOR start\_POSTSUBSCRIPT blackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ∈ caligraphic\_D end\_POSTSUBSCRIPT italic\_ϕ ( blackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT , italic\_q ) | |

where ϕitalic-ϕ\\phiitalic\_ϕ is usually the ℓ2subscriptℓ2\\ell\_{2}roman\_ℓ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT or cosine similarity. With the enormity of modern data workloads and the underlying vector dimensionality, it becomes computationally infeasible to exhaustively search for the true top-k𝑘kitalic\_k neighbors for any query q.𝑞q.italic\_q . Thus, approximate search algorithms trade-off quality of the search for lower latency.

In the approximate nearest neighbor search (ANNS) regime, we evaluate the quality of the search procedure typically by the Recall@⁢k@𝑘@k@ italic\_k metric. More formally, suppose a given ANNS search algorithm outputs a subset 𝒪⊆𝒟,\|𝒪\|=k,formulae-sequence𝒪𝒟𝒪𝑘\\mathcal{O}\\subseteq\\mathcal{D},\|\\mathcal{O}\|=k,caligraphic\_O ⊆ caligraphic\_D , \| caligraphic\_O \| = italic\_k , and let G⊆𝒟𝐺𝒟G\\subseteq\\mathcal{D}italic\_G ⊆ caligraphic\_D be the true k𝑘kitalic\_k nearest neighbors of a query q.𝑞q.italic\_q . We define Recall@⁢k@𝑘@k@ italic\_k by \|𝒪∩G\|k𝒪𝐺𝑘\\frac{\|\\mathcal{O}\\cap G\|}{k}divide start\_ARG \| caligraphic\_O ∩ italic\_G \| end\_ARG start\_ARG italic\_k end\_ARG. ANNS algorithms seek to maximize this metric while retrieving results as quickly as possible.

### 2.1. HNSW Overview

With this formalization of the ANNS problem, we will now briefly review the key elements of the HNSW algorithm, which is the central focus of our benchmarking study. As we alluded to previously, HNSW builds off of prior work in _navigable small world graph_ indexes introduced in (Malkov et al., [2014](https://arxiv.org/html/2412.01940v2#bib.bib32 "")). Small world graphs are a well-studied phenomenon in both computing and the social sciences and are primarily defined by the fact that the average length of a shortest path between two vertices is small (typically scaling logarithmically with the number of nodes in the network) (Travers and Milgram, [1977](https://arxiv.org/html/2412.01940v2#bib.bib47 ""); Watts and Strogatz, [1998](https://arxiv.org/html/2412.01940v2#bib.bib49 ""); Kleinberg, [2000](https://arxiv.org/html/2412.01940v2#bib.bib27 "")). Small world graphs are also often characterized by the presence of well-connected _hub nodes_ which we discuss further in the next section.

Algorithm 1 HNSW Construction

1:Input: Set of data points D𝐷Ditalic\_D, max layer Lm⁢a⁢xsubscript𝐿𝑚𝑎𝑥L\_{max}italic\_L start\_POSTSUBSCRIPT italic\_m italic\_a italic\_x end\_POSTSUBSCRIPT, max connections per layer M𝑀Mitalic\_M, layer insertion probability mlsubscript𝑚𝑙m\_{l}italic\_m start\_POSTSUBSCRIPT italic\_l end\_POSTSUBSCRIPT, size of dynamic candidate list e⁢f⁢c𝑒𝑓𝑐efcitalic\_e italic\_f italic\_c

2:Output: HNSW graph with hierarchical layers

3:procedureConstruct(D,Lm⁢a⁢x,M,ml,e⁢f⁢c𝐷subscript𝐿𝑚𝑎𝑥𝑀subscript𝑚𝑙𝑒𝑓𝑐D,L\_{max},M,m\_{l},efcitalic\_D , italic\_L start\_POSTSUBSCRIPT italic\_m italic\_a italic\_x end\_POSTSUBSCRIPT , italic\_M , italic\_m start\_POSTSUBSCRIPT italic\_l end\_POSTSUBSCRIPT , italic\_e italic\_f italic\_c)

4:     Initialize empty hierarchical graph G𝐺Gitalic\_G

5:     Initialize entry point e⁢p←None←𝑒𝑝Noneep\\leftarrow\\text{None}italic\_e italic\_p ← None

6:for each p∈D𝑝𝐷p\\in Ditalic\_p ∈ italic\_Ddo

7:Lp←←subscript𝐿𝑝absentL\_{p}\\leftarrowitalic\_L start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT ← GeometricDistribution(mlsubscript𝑚𝑙m\_{l}italic\_m start\_POSTSUBSCRIPT italic\_l end\_POSTSUBSCRIPT)

8:ife⁢p=None𝑒𝑝Noneep=\\text{None}italic\_e italic\_p = Nonethen

9:              Set p𝑝pitalic\_p as entry point e⁢p𝑒𝑝epitalic\_e italic\_p

10:              Insert p𝑝pitalic\_p into all levels ≤Lpabsentsubscript𝐿𝑝\\leq L\_{p}≤ italic\_L start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT

11:endif

12:forl=Lm⁢a⁢x𝑙subscript𝐿𝑚𝑎𝑥l=L\_{max}italic\_l = italic\_L start\_POSTSUBSCRIPT italic\_m italic\_a italic\_x end\_POSTSUBSCRIPT to Lpsubscript𝐿𝑝L\_{p}italic\_L start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPTdo

13:e⁢p←←𝑒𝑝absentep\\leftarrowitalic\_e italic\_p ← SearchLayer(G,l,p,e⁢p,e⁢f⁢c𝐺𝑙𝑝𝑒𝑝𝑒𝑓𝑐G,l,p,ep,efcitalic\_G , italic\_l , italic\_p , italic\_e italic\_p , italic\_e italic\_f italic\_c) ▷▷\\triangleright▷ Algorithm [2](https://arxiv.org/html/2412.01940v2#alg2 "Algorithm 2 ‣ 2.2. HNSW Search Algorithm ‣ 2. Background: Similarity Search & HNSW ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”")

14:endfor

15:forl=0𝑙0l=0italic\_l = 0 to Lpsubscript𝐿𝑝L\_{p}italic\_L start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPTdo

16:N←←𝑁absentN\\leftarrowitalic\_N ← SelectNeighbors(p,G,l,M𝑝𝐺𝑙𝑀p,G,l,Mitalic\_p , italic\_G , italic\_l , italic\_M)

17:              Add edges from q𝑞qitalic\_q to each neighbor n∈N𝑛𝑁n\\in Nitalic\_n ∈ italic\_N at layer l𝑙litalic\_l

18:ifn∈N𝑛𝑁n\\in Nitalic\_n ∈ italic\_N has <Mabsent𝑀<M< italic\_M edges then

19:                  Add back-connections to q𝑞qitalic\_q to node n𝑛nitalic\_n.

20:else

21:                  Run SelectNeighbors on {q,\\{q,{ italic\_q , edges of n}n\\}italic\_n }.

22:endif

23:endfor

24:endfor

25:ifLp>Le⁢psubscript𝐿𝑝subscript𝐿𝑒𝑝L\_{p}>L\_{ep}italic\_L start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT > italic\_L start\_POSTSUBSCRIPT italic\_e italic\_p end\_POSTSUBSCRIPTthen

26:e⁢p←p←𝑒𝑝𝑝ep\\leftarrow pitalic\_e italic\_p ← italic\_p

27:endif

28:endprocedure

29:

30:functionSelectNeighbors(p,G,l,M𝑝𝐺𝑙𝑀p,G,l,Mitalic\_p , italic\_G , italic\_l , italic\_M)

31:     Compute distances from p𝑝pitalic\_p to all nodes in G⁢\[l\]𝐺delimited-\[\]𝑙G\[l\]italic\_G \[ italic\_l \]

32:     Return M𝑀Mitalic\_M nodes based on selection heuristic in  (Arya and Mount, [1993](https://arxiv.org/html/2412.01940v2#bib.bib3 ""))

33:endfunction

### 2.2. HNSW Search Algorithm

Algorithm 2 HNSW Query

1:Input: Graph G𝐺Gitalic\_G, layer l𝑙litalic\_l, query q𝑞qitalic\_q, starting point p𝑝pitalic\_p, number of nearest neighbors to return e⁢f⁢s𝑒𝑓𝑠efsitalic\_e italic\_f italic\_s

2:procedureSearchLayer(G,l,q,p,e⁢f⁢s𝐺𝑙𝑞𝑝𝑒𝑓𝑠G,l,q,p,efsitalic\_G , italic\_l , italic\_q , italic\_p , italic\_e italic\_f italic\_s)

3:     Candidate queue C=p𝐶𝑝C={p}italic\_C = italic\_p, currently top
results queue T=p𝑇𝑝T={p}italic\_T = italic\_p, visited list V=p𝑉𝑝V={p}italic\_V = italic\_p

4:whileC𝐶Citalic\_C is not empty do

5:c←nearest element from⁢C⁢to⁢q←𝑐nearest element from𝐶to𝑞c\\leftarrow\\text{nearest element from}~{}C~{}\\text{to}~{}qitalic\_c ← nearest element from italic\_C to italic\_q

6:f←furthest element from⁢T⁢to⁢q←𝑓furthest element from𝑇to𝑞f\\leftarrow\\text{furthest element from}~{}T~{}\\text{to}~{}qitalic\_f ← furthest element from italic\_T to italic\_q

7:if dist(c, q) ¿ dist(f, q) thenreturn T

8:endif

9:fore∈neighbourhood⁢(c)⁢at layer⁢l𝑒neighbourhood𝑐at layer𝑙e\\in\\text{neighbourhood}(c)~{}\\text{at layer}~{}litalic\_e ∈ neighbourhood ( italic\_c ) at layer italic\_ldo

10:ife∈V𝑒𝑉e\\in Vitalic\_e ∈ italic\_Vthen

11:                  continue

12:endif

13:V.a⁢d⁢d⁢(e)formulae-sequence𝑉𝑎𝑑𝑑𝑒V.add(e)italic\_V . italic\_a italic\_d italic\_d ( italic\_e )

14:ifd⁢i⁢s⁢t⁢(e,q)≤d⁢i⁢s⁢t⁢(f,q)⁢or⁢\|T\|≤e⁢f⁢s𝑑𝑖𝑠𝑡𝑒𝑞𝑑𝑖𝑠𝑡𝑓𝑞or𝑇𝑒𝑓𝑠dist(e,q)\\leq dist(f,q)~{}\\text{or}~{}\|T\|\\leq efsitalic\_d italic\_i italic\_s italic\_t ( italic\_e , italic\_q ) ≤ italic\_d italic\_i italic\_s italic\_t ( italic\_f , italic\_q ) or \| italic\_T \| ≤ italic\_e italic\_f italic\_sthen

15:C.a⁢d⁢d⁢(e)formulae-sequence𝐶𝑎𝑑𝑑𝑒C.add(e)italic\_C . italic\_a italic\_d italic\_d ( italic\_e )

16:T.a⁢d⁢d⁢(e)formulae-sequence𝑇𝑎𝑑𝑑𝑒T.add(e)italic\_T . italic\_a italic\_d italic\_d ( italic\_e )

17:endif

18:if\|T\|≥e⁢f⁢s𝑇𝑒𝑓𝑠\|T\|\\geq efs\| italic\_T \| ≥ italic\_e italic\_f italic\_sthen

19:                  Remove furthest point to q from T

20:endif

21:f←furthest element from⁢T⁢to⁢q←𝑓furthest element from𝑇to𝑞f\\leftarrow\\text{furthest element from}~{}T~{}\\text{to}~{}qitalic\_f ← furthest element from italic\_T to italic\_q

22:endforreturn T

23:endwhile

24:endprocedure

While small world graphs are, by construction, suited for efficient greedy graph traversal, the HNSW authors argue that the polylogarithmic scaling of the search process is still too inefficient for the demands of near neighbor search on large datasets. This claim motivates the design of HNSW where the hierarchy allows for computing a fixed number of distances in each graph layer independent of the network size.

Specifically, the HNSW index is constructed in an iterative fashion. For a newly inserted element x𝑥xitalic\_x, the algorithm will randomly select a maximum layer l𝑙litalic\_l and then insert the new point into every layer up to l𝑙litalic\_l. This randomized process is executed with an exponentially decaying probability distribution such that, in expectation, each subsequent layer has exponentially more nodes than its predecessor. Within a layer, HNSW greedily adds edges between x𝑥xitalic\_x and its M𝑀Mitalic\_M closest neighbors (where M𝑀Mitalic\_M is a hyperparameter) where the neighbors consist of previously inserted points. This process then repeats in the subsequent layer below using the closest neighbors found in the prior graph as entry points. Through this process, the top layer of the hierarchy will be the coarsest directed graph, consisting of the fewest nodes and edges, and the bottom layer will be the densest and contain all of the nodes, each with connections to (up to) M𝑀Mitalic\_M neighbors. As an additional, and important, optimization, HNSW also implements the pruning heuristic of (Arya and Mount, [1993](https://arxiv.org/html/2412.01940v2#bib.bib3 "")) that will prune an edge from u𝑢uitalic\_u to v𝑣vitalic\_v if there exists another edge from u𝑢uitalic\_u to a neighbor w𝑤witalic\_w of v𝑣vitalic\_v such that the distance from u𝑢uitalic\_u to w𝑤witalic\_w is less than that of u𝑢uitalic\_u to v𝑣vitalic\_v.

The search procedure of HNSW, described in Algorithm [2](https://arxiv.org/html/2412.01940v2#alg2 "Algorithm 2 ‣ 2.2. HNSW Search Algorithm ‣ 2. Background: Similarity Search & HNSW ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”") also executes iteratively where the algorithm maintains a list of candidate points at each layer of the hierarchical graph before returning the final list k𝑘kitalic\_k nearest neighbor candidates after traversing the base graph layer.

https://arxiv.org/html/2412.01940v2/extracted/6171912/images/hnsw_graphic.png

Figure 2. Visualization of the HNSW search index. We benchmark the full hierarchical graph search procedure against simply searching in the bottom base layer.

## 3\. Related Work

### 3.1. Near-Neighbor Benchmarks

Due to the importance of the k𝑘kitalic\_k-NNS problem, there have been several large-scale near-neighbor benchmarks in recent years. The original ANN Benchmarks  (Aumüller et al., [2018](https://arxiv.org/html/2412.01940v2#bib.bib4 "")) made significant impact because it provided the first standard evaluation of near-neigh3bor search algorithms. Since its inception, the benchmark has grown in scope from a handful of algorithms to include over 30 methods on 9 datasets.
However, most of the datasets included in ANN Benchmarks are relatively small by modern standards at around one million points. To reflect the growing need for high-dimensional, large-scale embedding search, NeurIPS hosted a competition track known as Big ANN Benchmarks (Simhadri et al., [2022](https://arxiv.org/html/2412.01940v2#bib.bib43 "")), which evaluates algorithms on five billion-scale datasets. Graph-based indexes easily and consistently place among the top three algorithms in each benchmark. However, these benchmarks are not sufficient for our purposes because they focus exclusively on overall throughput metrics and do not report tail latency numbers such as the 99th percentile, which is important in our case for teasing apart the impact of hierarchy in HNSW.

Hierarchy Studies: Hierarchical structures are considered a fundamental component of graph-based near-neighbor algorithms.
As a result, numerous high-performing algorithms use some form of hierarchy including HNSW (Malkov and Yashunin, [2016](https://arxiv.org/html/2412.01940v2#bib.bib33 "")), ONNG (Iwasaki and Miyazaki, [2018](https://arxiv.org/html/2412.01940v2#bib.bib22 "")) PANNG (Iwasaki, [2016](https://arxiv.org/html/2412.01940v2#bib.bib21 "")), and HCNNG (Munoz et al., [2019](https://arxiv.org/html/2412.01940v2#bib.bib36 "")).
However, this practice has recently come under scrutiny. Dobson et al. ( [2023](https://arxiv.org/html/2412.01940v2#bib.bib11 "")) show that the hierarchy may be unnecessary for some workloads, based on the observation that HNSW under-performs both HCNNG (which uses a shallower hierarchy) and DiskANN (Jayaram Subramanya et al., [2019](https://arxiv.org/html/2412.01940v2#bib.bib24 "")) (which does not use a hierarchy). Lin and Zhao ( [2019](https://arxiv.org/html/2412.01940v2#bib.bib29 "")) present results on synthetic data showing that the hierarchy is only beneficial for low-dimensional data (d<32𝑑32d<32italic\_d < 32), but analyze only a limited number of small real-world datasets and – most importantly – do not explain why the hierarchy fails to provide value. In this work, we aim to address these gaps in the literature through more comprehensive benchmarks coupled with an analysis of why hierarchical structures in high-dimensional space may not add value. In the following section, we aim to reproduce the results of both Malkov and Yashunin ( [2016](https://arxiv.org/html/2412.01940v2#bib.bib33 "")) and Lin and Zhao ( [2019](https://arxiv.org/html/2412.01940v2#bib.bib29 "")) to confirm that we can independently replicate their findings with our own software implementation before proceeding to new experiments on larger-scale benchmark datasets.

### 3.2. Hubness in High Dimensional Spaces

Astute readers might observe that the HNSW graph construction algorithm described above does not explicitly enforce the small world property and instead adds edges between nodes based on their proximity in the metric space. The connection between proximity and the small world property arises due to _hubness_.

Specifically, hubness is a property of high-dimensional metric spaces where a small subset of points (the “hubs”) occur a disproportionate number of times in the near-neighbor lists of other points in the dataset (Radovanovic et al., [2010](https://arxiv.org/html/2412.01940v2#bib.bib40 "")). In other words, a small fraction of nodes are highly connected to other points.

A related, but slightly different, notion of hubness that has been at the center of theoretical analysis is concentration of distances in high-dimensional spaces. It has been shown that, in expectation, the ℓ2subscriptℓ2\\ell\_{2}roman\_ℓ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT distance between independent and identically distributed (i.i.d) vectors grows with d𝑑\\sqrt{d}square-root start\_ARG italic\_d end\_ARG while the variance tends to a constant as d𝑑ditalic\_d approaches infinity (Talagrand, [1994](https://arxiv.org/html/2412.01940v2#bib.bib46 "")). As a result, the ℓ2subscriptℓ2\\ell\_{2}roman\_ℓ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT distance loses its discriminative power as d𝑑ditalic\_d increases. In fact, this concentration phenomenon is not only constrained to ℓ2subscriptℓ2\\ell\_{2}roman\_ℓ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT but also applies to other ℓpsubscriptℓ𝑝\\ell\_{p}roman\_ℓ start\_POSTSUBSCRIPT italic\_p end\_POSTSUBSCRIPT and even fractional norms (François et al., [2007](https://arxiv.org/html/2412.01940v2#bib.bib16 "")).

Due to undesirable consequences of the hubness phenomenon, such as poor clustering quality, a large body of work has focused on hubness reduction strategies. For instance, (Zelnik-Manor and Perona, [2004](https://arxiv.org/html/2412.01940v2#bib.bib50 "")) introduced local scaling which scales distances d⁢(𝕩,𝕪)𝑑𝕩𝕪d(\\mathbb{x},\\mathbb{y})italic\_d ( blackboard\_x , blackboard\_y ) by accounting for local neighborhood information. Interestingly, our work stands in contrast to this literature on hubness reduction by presenting a case study where hubs provide tangible value in an algorithmic setting, namely in accelerating greedy traversal in near neighbor proximity graphs. This result may be of independent interest to machine learning and algorithms researchers as well.

## 4\. Reproduction of Prior Studies

In this section, we present a replicability study using four flatnav NSW implementation. In particular, we revisit the experimental design of two prior works in the literature: the original 2016 HNSW paper of Malkov and Yashunin ( [2016](https://arxiv.org/html/2412.01940v2#bib.bib33 "")) and a subsequent 2019 paper from Lin and Zhao ( [2019](https://arxiv.org/html/2412.01940v2#bib.bib29 "")) that found limitations with the hierarchical component of HNSW. As we discussed in the previous section, these prior works possess limitations in experimental design, scope of benchmarking datasets, and a lack of analysis into understanding the results, which motivates our work in this paper. Nevertheless, we use these prior studies as a starting point to see if we can independently replicate these results via our own FlatNav implementation. Such a reproduction would both further validate the soundness of these previous experiments over the test of time as well as provide confirmation of the correctness of FlatNav before we proceed to new, larger-scale benchmarks.

Following the same setups as Malkov and Yashunin ( [2016](https://arxiv.org/html/2412.01940v2#bib.bib33 "")) and Lin and Zhao ( [2019](https://arxiv.org/html/2412.01940v2#bib.bib29 "")) we generate a series of random vector datasets of varying dimensionality where each vector component is sampled uniformly at random from the range \[0,1)01\[0,1)\[ 0 , 1 ). In particular, we consider dimensionalities of d=4,8,16𝑑4816d=4,8,16italic\_d = 4 , 8 , 16 and 32. As in (Lin and Zhao, [2019](https://arxiv.org/html/2412.01940v2#bib.bib29 "")), we set the number of near neighbors to retrieve to k=1𝑘1k=1italic\_k = 1 (departing from the default of k=100𝑘100k=100italic\_k = 100 we use elsewhere in this paper). We also tried including the sw-graph NSW baseline (Boytsov and Naidan, [2013](https://arxiv.org/html/2412.01940v2#bib.bib8 "")) that Malkov and Yashunin ( [2016](https://arxiv.org/html/2412.01940v2#bib.bib33 "")) used in their evaluation to benchmark against HNSW, but we were not able to run this older library successfully. However, we were able to replicate these prior findings using our own flatnav implementation which is conceptually identical to sw-graph but with more software optimizations to achieve engineering parity with hnswlib (detailed in Section [5.1](https://arxiv.org/html/2412.01940v2#S5.SS1 "5.1. Software Performance Optimizations ‣ 5. FlatNav Benchmarking Experiments ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”")).

https://arxiv.org/html/2412.01940v2/extracted/6171912/images/linzhao/linzhao_all.png

Figure 3. Median Latency vs. Recall of HNSW and FlatNav across dimensions d=4,8,16,32𝑑481632d=4,8,16,32italic\_d = 4 , 8 , 16 , 32. We observe that the hierarchical structure accelerates search only when d<32𝑑32d<32italic\_d < 32, matching the findings of Lin and Zhao ( [2019](https://arxiv.org/html/2412.01940v2#bib.bib29 "")). Our results demonstrating a significant advantage with HNSW on synthetic datasets with dimensionality d=4𝑑4d=4italic\_d = 4 and d=8𝑑8d=8italic\_d = 8 also match the findings of the original HNSW paper Malkov and Yashunin ( [2016](https://arxiv.org/html/2412.01940v2#bib.bib33 "")).

As shown in Figure [3](https://arxiv.org/html/2412.01940v2#S4.F3 "Figure 3 ‣ 4. Reproduction of Prior Studies ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”"), we successfully replicated the experiments benchmarking HNSW versus a flat NSW graph from two prior research papers. Notably, both of these previous works primarily experiment with randomly generated vector data with very low dimensionality by the standards of modern machine learning. Coupled with our findings in the next section where we find no discernible difference between HSNW and a flat graph index on high-dimensional datasets, our results suggest a simple decision criterion for selecting a search index: For dimensionality d<32𝑑32d<32italic\_d < 32, HNSW and the hierarchy provide a speedup. Otherwise, the simplicity and memory savings of a flat NSW index provide more benefit.

We also had the opportunity to discuss our findings with the lead author of (Malkov and Yashunin, [2016](https://arxiv.org/html/2412.01940v2#bib.bib33 "")) who confirmed that the hierarchy provides a robust speedup on these low-dimensional datasets but noted the performance on higher dimensional vectors remained less clear, which further motivated us to take up the benchmarking study in the next section.

## 5\. FlatNav Benchmarking Experiments

In this section, we report the results of our benchmarking study comparing the performance of flat HNSW search to hierarchical search on a suite of standard high-dimensional benchmark datasets drawn from real machine learning models.

A challenge in designing such benchmarking experiments is separating the confounding impact of performance engineering in the implementation of an approach from any purely algorithmic advantages of a method. We argue that this is a pitfall that has clouded several past benchmarking studies in ANN search. To circumvent this challenge, we fix the implementation in our experimental design such that the _same code_ is used in constructing the base navigable small world graph. In particular, we use the popular hnswlib library as our baseline HNSW implementation. To benchmark the flat NSW index performance, we extract the bottom graph layer from hnswlib and reimplement the HNSW’s greedy search heuristic over this flat graph. To the best of our knowledge, we provide the first benchmarking study on the utility of HNSW’s hierarchy that makes an effort to achieve parity in the implementations of the two techniques to center the focus on the central algorithmic question.

### 5.1. Software Performance Optimizations

One major challenge in prior near neighbor benchmarking studies is the confounding effect of software performance optimizations when making conclusions about algorithmic efficacy. To address this issue, our implementation of a flat similarity search graph in flatnav closely follows the performance optimizations native to hnswlib. We use SIMD vector instructions to efficiently compute the distance between any two vectors, which is the key operation underpinning similarity search. Depending on the hardware type, we provide distance computations using SSE, AVX and AVX-512 intrinsics for float, uint8\_t and int8\_t data types. The choice of which intrinsics family to use is a compile-time choice, which is determined based on the dataset dimensionality and hardware support, similar to hnswlib. For all benchmark experiments, we use the float data type.

Furthermore, one common problem in constructing and querying graph-based indexes is the random data access pattern which can hamper latency and throughput. To improve search throughput, hnswlib implements prefetching using the \_mm\_prefetch intrinsic which reduces memory access latency by prefetching data into the L1 cache. Since caching can significantly affect latency metrics, we control for this performance optimization by leveraging the same intrinsic in the flatnav implementation so that our benchmarks strictly adhere to algorithmic differences.

### 5.2. Datasets and Compute

We utilize the benchmark datasets released through the popular leaderboards ANN Benchmarks (Aumüller et al., [2018](https://arxiv.org/html/2412.01940v2#bib.bib4 "")) and Big ANN Benchmarks (Simhadri et al., [2022](https://arxiv.org/html/2412.01940v2#bib.bib43 "")). The specific datasets and their associated statistics are presented in Table [1](https://arxiv.org/html/2412.01940v2#S5.T1 "Table 1 ‣ 5.2. Datasets and Compute ‣ 5. FlatNav Benchmarking Experiments ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”"). For the Big ANN Benchmark datasets, we consider both the 10M and 100M collection of vectors for which the ground truth near neighbors have previously been computed and released. We did not experiment with the largest Big ANN datasets with 1 billion vectors since constructing HNSW indexes at this scale requires over 1.5TB of RAM, which exceeded our compute resources. Below, we include our benchmarking results for the four 100M-scale datasets available through Big ANN Benchmarks. We see that our flat HNSW implementation achieves performance parity with the hierarchical HNSW implementation.

| Dataset | Dimensionality | \# Points | \# Queries |
| --- | --- | --- | --- |
| BigANN† | 128 | 100M | 10K |
| Microsoft SpaceV† | 100 | 100M | 29.3K |
| Yandex DEEP† | 96 | 100M | 10K |
| Yandex Text-to-Image† | 200 | 100M | 100K |
| GloVe | {25, 50, 100, 200} | 1.2M | 10K |
| NYTimes | 256 | 290K | 10K |
| GIST | 960 | 1M | 1K |
| SIFT | 128 | 1M | 10K |
| MNIST | 784 | 60K | 10K |
| DEEP1B | 96 | 10M | 10K |

Table 1. Dataset Statistics. The datasets marked by ††\\dagger† are from the BigANN benchmarks (Simhadri et al., [2022](https://arxiv.org/html/2412.01940v2#bib.bib43 "")). The remaining are taken from ANN Benchmarks (Aumüller et al., [2018](https://arxiv.org/html/2412.01940v2#bib.bib4 "")).

For our benchmarks on datasets consisting of fewer than 100M vectors in the collection, we use an AWS c6i.8xlarge instance with an Intel Ice Lake processor and 64GB of RAM. We selected this particular public cloud instance to facilitate accessible reproducibility of our experiments. For the 100M-sized large-scale experiments, we use a cloud server equipped with an M. EPYC 9J14 96-Core Processor and 1 TB of RAM.

### 5.3. Latency Results

#### 5.3.1. BigANN Benchmarks (Simhadri et al., [2022](https://arxiv.org/html/2412.01940v2#bib.bib43 ""))

In Figures [4](https://arxiv.org/html/2412.01940v2#S5.F4 "Figure 4 ‣ 5.3.1. BigANN Benchmarks (Simhadri et al., 2022) ‣ 5.3. Latency Results ‣ 5. FlatNav Benchmarking Experiments ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”") and [5](https://arxiv.org/html/2412.01940v2#S5.F5 "Figure 5 ‣ 5.3.1. BigANN Benchmarks (Simhadri et al., 2022) ‣ 5.3. Latency Results ‣ 5. FlatNav Benchmarking Experiments ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”"), we compare latency metrics for HNSW and FlatNav at the 50th and 99th percentile for the four 100M datasets from BigANN benchmarks listed in Table [1](https://arxiv.org/html/2412.01940v2#S5.T1 "Table 1 ‣ 5.2. Datasets and Compute ‣ 5. FlatNav Benchmarking Experiments ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”"). All of our results support the conclusion that flatnav achieves nearly identical performance to hnswlib.

From the results in Figures [4](https://arxiv.org/html/2412.01940v2#S5.F4 "Figure 4 ‣ 5.3.1. BigANN Benchmarks (Simhadri et al., 2022) ‣ 5.3. Latency Results ‣ 5. FlatNav Benchmarking Experiments ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”") and [5](https://arxiv.org/html/2412.01940v2#S5.F5 "Figure 5 ‣ 5.3.1. BigANN Benchmarks (Simhadri et al., 2022) ‣ 5.3. Latency Results ‣ 5. FlatNav Benchmarking Experiments ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”"), we observe that there is no consistent and discernable gap between FlatNav and HNSW in both the median and tail latency cases. These results suggest that the hierarchical structure of HNSW provides no tangible benefit on practical high-dimensional embedding datasets.

https://arxiv.org/html/2412.01940v2/extracted/6171912/images/bigann-100m/100m_all_p50.pngFigure 4. p50 Latency vs. Recall for HNSW and FlatNav over four 100M-scale benchmark datasets with dimensionality between 96 and 200. We observe that the flat NSW index achieves essentially identical performance to the hierarchical HNSW index.
https://arxiv.org/html/2412.01940v2/extracted/6171912/images/bigann-100m/100m_all_p99.pngFigure 5. p99 Latency vs. Recall for HNSW and FlatNav over four 100M-scale benchmark datasets with dimensionality between 96 and 200. As with the median case, we observe nearly identical performance between the two indexes.

#### 5.3.2. ANN Benchmarks (Aumüller et al., [2018](https://arxiv.org/html/2412.01940v2#bib.bib4 ""))

Moreover, we repeat the same experimental setup comparing HNSW and FlatNav on the ANN Benchmark datasets listed in Table [1](https://arxiv.org/html/2412.01940v2#S5.T1 "Table 1 ‣ 5.2. Datasets and Compute ‣ 5. FlatNav Benchmarking Experiments ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”"). In Figures [6](https://arxiv.org/html/2412.01940v2#S5.F6 "Figure 6 ‣ 5.3.2. ANN Benchmarks (Aumüller et al., 2018) ‣ 5.3. Latency Results ‣ 5. FlatNav Benchmarking Experiments ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”") and [7](https://arxiv.org/html/2412.01940v2#S5.F7 "Figure 7 ‣ 5.3.2. ANN Benchmarks (Aumüller et al., 2018) ‣ 5.3. Latency Results ‣ 5. FlatNav Benchmarking Experiments ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”"), we report the p50 and p99 latency of all of the non-GloVe ANN Benchmarks. Although these datasets are smaller in scale than the BigANN Benchmarks, we still see no discernible difference in latency between HNSW and FlatNav which supports our hypothesis that the vector dimensionality and not the size of the collection is the main driver of eliminating the need for hierarchical search in small world graphs. We see further evidence of this idea in Table [8](https://arxiv.org/html/2412.01940v2#S5.F8 "Figure 8 ‣ 5.3.2. ANN Benchmarks (Aumüller et al., 2018) ‣ 5.3. Latency Results ‣ 5. FlatNav Benchmarking Experiments ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”"), where we plot the median latency versus recall on the four GloVe benchmark datasets ranging in dimensionality from 25 to 200. Ultimately, these results, coupled with our reproducibility studies in the previous section, provide compelling evidence that for high-dimensional datasets, which are the standard in modern similarity search workloads, there is no apparent performance benefit to the hierarchical layers of HNSW.

https://arxiv.org/html/2412.01940v2/extracted/6171912/images/ann-benchmarks/ann_bench_p50.pngFigure 6. p50 Latency vs. Recall for HNSW and FlatNav over five ANN Benchmark datasets ranging in dimensionality from 96 to 960. The flat NSW index again achieves practically indistinguishable performance from the hierarchical graph index.
https://arxiv.org/html/2412.01940v2/extracted/6171912/images/ann-benchmarks/ann_bench_p99.pngFigure 7. p99 Latency vs. Recall for HNSW and FlatNav over five ANN Benchmark datasets ranging in dimensionality from 96 to 960.
https://arxiv.org/html/2412.01940v2/extracted/6171912/images/ann-benchmarks/glove_results.pngFigure 8. p50 and p99 Latency vs. Recall for HNSW and FlatNav over the GloVe ANN Benchmark datasets with respective dimensionalities 25, 50, 100, and 200. We observe that HNSW has a minor advantage in low dimensions and that FlatNav has a minor advantage in high dimensions, but also that there is no clear difference in performance.

### 5.4. Memory

| Dataset | \# Data | hnswlib Memory | flatnav Memory |
| --- | --- | --- | --- |
| BigANN | 100M | 183 | 113 |
| Microsoft SpaceV | 100M | 104 | 85.5 |
| Yandex DEEP | 100M | 100 | 60.7 |

Table 2. Peak Index Construction Memory in GBs. We observe that flatnav requires considerably less memory during construction compared to hnswlib.

In this section we measure the memory savings from removing the hierarchy by running a memory profiler during index construction. In terms of memory allocation, similarly to flatnav, hnswlib allocates static memory during index construction comprising base layer node allocation, a visited node list and a list of mutexes in the multi-threaded setting. Additionally, it also incurs memory cost attributable to the hierarchy, particularly maintaning the dynamically allocated links between nodes at each layer.

We benchmarked both libraries against a subset of the BigANN benchmarks. Table [2](https://arxiv.org/html/2412.01940v2#S5.T2 "Table 2 ‣ 5.4. Memory ‣ 5. FlatNav Benchmarking Experiments ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”") shows the peak memory allocated by the two implementations during index construction for the BigANN, Microsoft SpaceV and Yandex DEEP benchmarks. Since multithreading has a runtime overhead, we fix the number of cores to 32 in each one of the stated benchmark. For BigANN, we observe a 38%percent3838\\%38 % reduction in peak memory, a 39%percent3939\\%39 % reduction for Yandex DEEP, and an 18%percent1818\\%18 % reduction for the Microsoft SpaceV benchmark. This shows that we are able to save significant memory by removing the hierarchy, and it is likely that we can optimize flatnav implementation to save memory further.

One caveat of these reported memory savings is that we are comparing different two software implementations in hnswlib and flatnav. Since hnswlib is a mature library widely used by practitioners as well as researchers, it supports more features than flatnav and thus must maintain additional complexity whereas our implementation, while performant, is more of a research prototype. Therefore, differences in code may account for a significant part of the peak memory usage differences. Nevertheless, we believe our findings are relevant and still noteworthy given that hnswlib is so widely adopted. By demonstrating that we can considerably reduce the memory overhead of hnswlib without sacrificing performance, we hope to bring the community’s attention to the opportunities for further optimization in this direction.

## 6\. The Hub Highway Hypothesis

In the previous section, we established through a series of careful benchmarking experiments that there appears to be no discernible difference in performance between HNSW and its flat counterpart with no hierarchical graph structure. We now turn our attention to studying why the hierarchy appears to provide no benefit in the search process.

In our experiments, we observed that a small fraction of nodes appear in the set of near neighbors for a disproportionate number of other vectors. We thus conjecture that the hub structure prevalent in high-dimensional data performs the same functional role as the hierarchy.

###### Hypothesis 0 (Hub Highways).

In high-dimensional metric spaces, k𝑘kitalic\_k-NN proximity graphs form a highway routing structure where a small subset of nodes are well-connected and heavily traversed, particularly in the early stages of graph search.

We remark that the existence of hub nodes in high-dimensional space is not a new observation (Radovanovic et al., [2010](https://arxiv.org/html/2412.01940v2#bib.bib40 "")). The novelty of our hypothesis lies in connecting the idea of hubness to the notion of accelerating near neighbor search in ANN proximity graphs. In particular, we conjecture that near neighbor queries over proximity graphs in high dimensions often spend the majority of their time visiting hub nodes early on in the search process before converging to a local neighborhood of near neighbors. This procedure succeeds because hub nodes are very well connected to other parts of the graph and thereby efficiently route queries to the appropriate neighborhood in much the same manner that the layered hierarchy purports to do.

In many applications, such as clustering, hubness is considered an undesirable property that harms algorithmic performance, motivating the need for hubness reduction techniques (Zelnik-Manor and Perona, [2004](https://arxiv.org/html/2412.01940v2#bib.bib50 "")). On the contrary, our Hub Highway Hypothesis presents a case where hubness offers a distinct advantage in a practical algorithmic setting.

In the remainder of this section, we present an experimental design and a series of results that provide empirical evidence in the affirmative for the existence of such a highway routing mechanism amongst hubs in navigable small world graphs.

### 6.1. Intuition:

The formation of a hub highway can be understood through concentration of measure phenomena.

Concentration of distances: Under many data-generating distributions, the expected distances between randomly-drawn points converge to a constant value as dimension increases (Beyer et al., [1999](https://arxiv.org/html/2412.01940v2#bib.bib6 "")). This suggests that in sufficiently high-dimensional spaces, we do not need to explicitly encourage the formation of “long-range” connections. Since all distances are approximately equal, all connections have similar length and a few edge traversals should span the graph of a high-dimensional dataset.

Concentration of measure: A well-known fact about high-dimensional geometry is that volume concentrates at the extrema of a shape (e.g., the surface of a ball or the faces of a hypercube). These portions of the distribution contain a disproportionate number of points and frequently contain the hubs of the metric space.
For example, Low et. al. demonstrate that the the hubs of a uniform hypercube distribution are located at the corners (Low et al., [2013](https://arxiv.org/html/2412.01940v2#bib.bib30 "")), which are exactly the points we would wish to connect via long-range connections in a hierarchical graph.

### 6.2. Methodology

Argument sketch: We will demonstrate the Hub Highway Hypothesis by providing empirical evidence for the following claims.

1. (1)

Some nodes are visited by queries much more frequently than others. The relative popularity of these hub nodes is explained by the hubness phenomena that arises in high-dimensional datasets.

2. (2)

The hub nodes tend to be connected to each other, forming a well-connected subgraph of hubs.

3. (3)

Queries visit many hub nodes early in the search process, before visiting less well-traversed neighborhoods.

Empirical measures of hubness: To support the first part of our argument, we will need a formal definition and characterization of hubness.

Following (Radovanovic et al., [2010](https://arxiv.org/html/2412.01940v2#bib.bib40 "")), let 𝕩,𝕩1,…,𝕩n𝕩subscript𝕩1…subscript𝕩𝑛\\mathbb{x},\\mathbb{x}\_{1},\\ldots,\\mathbb{x}\_{n}blackboard\_x , blackboard\_x start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , … , blackboard\_x start\_POSTSUBSCRIPT italic\_n end\_POSTSUBSCRIPT be a collection of vectors drawn from the same probability distribution with support 𝒮⊆ℝd𝒮superscriptℝ𝑑\\mathcal{S}\\subseteq\\mathbb{R}^{d}caligraphic\_S ⊆ blackboard\_R start\_POSTSUPERSCRIPT italic\_d end\_POSTSUPERSCRIPT, and let ϕ:𝒮×𝒮→ℝ:italic-ϕ→𝒮𝒮ℝ\\phi:\\mathcal{S}\\times\\mathcal{S}\\to\\mathbb{R}italic\_ϕ : caligraphic\_S × caligraphic\_S → blackboard\_R be a distance function.

Furthermore, for 1≤i,k≤nformulae-sequence1𝑖𝑘𝑛1\\leq i,k\\leq n1 ≤ italic\_i , italic\_k ≤ italic\_n, let pi,ksubscript𝑝𝑖𝑘p\_{i,k}italic\_p start\_POSTSUBSCRIPT italic\_i , italic\_k end\_POSTSUBSCRIPT be defined by

| | | |
| --- | --- | --- |
| | pi,k⁢(𝕩)={1if 𝕩 is among the k-NN set of 𝕩i under ϕ0otherwise subscript𝑝𝑖𝑘𝕩cases1if 𝕩 is among the k-NN set of 𝕩i under ϕ0otherwise p\_{i,k}(\\mathbb{x})=\\begin{cases}1&\\text{if $\\mathbb{x}$ is among the $k$-NN %<br>set of $\\mathbb{x}\_{i}$ under $\\phi$}\\\<br>0&\\text{otherwise }\\end{cases}italic\_p start\_POSTSUBSCRIPT italic\_i , italic\_k end\_POSTSUBSCRIPT ( blackboard\_x ) = { start\_ROW start\_CELL 1 end\_CELL start\_CELL if blackboard\_x is among the italic\_k -NN set of blackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT under italic\_ϕ end\_CELL end\_ROW start\_ROW start\_CELL 0 end\_CELL start\_CELL otherwise end\_CELL end\_ROW | |

Now let N⁢(𝕩)𝑁𝕩N(\\mathbb{x})italic\_N ( blackboard\_x ) be the random variable defined by

| | | |
| --- | --- | --- |
| | N⁢(𝕩)≔∑i=1npi,k⁢(𝕩)≔𝑁𝕩superscriptsubscript𝑖1𝑛subscript𝑝𝑖𝑘𝕩N(\\mathbb{x})\\coloneqq\\sum\_{i=1}^{n}p\_{i,k}(\\mathbb{x})italic\_N ( blackboard\_x ) ≔ ∑ start\_POSTSUBSCRIPT italic\_i = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_n end\_POSTSUPERSCRIPT italic\_p start\_POSTSUBSCRIPT italic\_i , italic\_k end\_POSTSUBSCRIPT ( blackboard\_x ) | |

which represents the number of vectors that have 𝕩𝕩\\mathbb{x}blackboard\_x included in their k𝑘kitalic\_k-nearest neighbors.

For any dataset 𝒟𝒟\\mathcal{D}caligraphic\_D, we can compute N⁢(𝕩),𝕩∈𝒟𝑁𝕩𝕩𝒟N(\\mathbb{x}),\\mathbb{x}\\in\\mathcal{D}italic\_N ( blackboard\_x ) , blackboard\_x ∈ caligraphic\_D, which yields a discrete distribution Nksubscript𝑁𝑘N\_{k}italic\_N start\_POSTSUBSCRIPT italic\_k end\_POSTSUBSCRIPT. We are interested in the skewness of this distribution, given by

| | | |
| --- | --- | --- |
| | SNk=𝔼⁢\[(Nk−μNk)3\]σNk3subscript𝑆subscript𝑁𝑘𝔼delimited-\[\]superscriptsubscript𝑁𝑘subscript𝜇subscript𝑁𝑘3subscriptsuperscript𝜎3subscript𝑁𝑘S\_{N\_{k}}=\\frac{\\mathbb{E}\\left\[\\left(N\_{k}-\\mu\_{N\_{k}}\\right)^{3}\\right\]}{%<br>\\sigma^{3}\_{N\_{k}}}italic\_S start\_POSTSUBSCRIPT italic\_N start\_POSTSUBSCRIPT italic\_k end\_POSTSUBSCRIPT end\_POSTSUBSCRIPT = divide start\_ARG blackboard\_E \[ ( italic\_N start\_POSTSUBSCRIPT italic\_k end\_POSTSUBSCRIPT - italic\_μ start\_POSTSUBSCRIPT italic\_N start\_POSTSUBSCRIPT italic\_k end\_POSTSUBSCRIPT end\_POSTSUBSCRIPT ) start\_POSTSUPERSCRIPT 3 end\_POSTSUPERSCRIPT \] end\_ARG start\_ARG italic\_σ start\_POSTSUPERSCRIPT 3 end\_POSTSUPERSCRIPT start\_POSTSUBSCRIPT italic\_N start\_POSTSUBSCRIPT italic\_k end\_POSTSUBSCRIPT end\_POSTSUBSCRIPT end\_ARG | |

This measure characterizes the asymmetry of the k𝑘kitalic\_k-occurrence distribution Nksubscript𝑁𝑘N\_{k}italic\_N start\_POSTSUBSCRIPT italic\_k end\_POSTSUBSCRIPT, and it is the metric most often used to estimate the presence of hubs. Thus, in our experiments we use SNksubscript𝑆subscript𝑁𝑘S\_{N\_{k}}italic\_S start\_POSTSUBSCRIPT italic\_N start\_POSTSUBSCRIPT italic\_k end\_POSTSUBSCRIPT end\_POSTSUBSCRIPT to quantify the presence of hubness in a particular dataset. The more skewed the distribution of Nksubscript𝑁𝑘N\_{k}italic\_N start\_POSTSUBSCRIPT italic\_k end\_POSTSUBSCRIPT, the more dataset 𝒟𝒟\\mathcal{D}caligraphic\_D tends to have clusters of vectors (hubs) that keep regularly occurring in the k𝑘kitalic\_k-NN sets of other vectors.

Table 3. Datasets

| Dataset | Dimensionality | \# Data | \# Queries |
| --- | --- | --- | --- |
| GIST | 960 | 1M | 1k |
| GloVe | 100 | 1.2M | 10k |
| NYTimes | 256 | 290K | 10k |
| Yandex-DEEP | 96 | 10M | 10k |
| Microsoft-SpaceV | 100 | 10M | 29.3k |
| IID Normal | {16, 32, 64, 128, 256, 1024, 1536} | 1M | 10k |
| IID Normal | {16, 32, 64, 128, 256, 1024, 1536} | 1M | 10k |

Synthetic and ANN Benchmark Datasets: To illustrate evidence for the Hub Highway Hypothesis, we experiment with both real and synthetic datasets as shown in Table [3](https://arxiv.org/html/2412.01940v2#S6.T3 "Table 3 ‣ 6.2. Methodology ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”"). In addition to a subset of ANN Benchmark datasets, we generate synthetic datasets by drawing vectors from the standard normal distribution. The choice of the normal distribution is important because, as (Low et al., [2013](https://arxiv.org/html/2412.01940v2#bib.bib30 ""))
observe, data sampled from the normal distribution exhibit a stronger hubness phenomenon due to strong density gradient than other distributions, such as sampling uniformly from a d𝑑ditalic\_d-dimensional hypercube. Furthermore, since the hubness phenomenon is accentuated in high-dimensional spaces, we generate random data with increasing dimensionality which allows us to study the effect of these intrinsic highway structures that form as d𝑑ditalic\_d
increases.

In the following three experiments we show empirical evidence supporting the Hub Highway Hypothesis. We start by examining the distribution of the number of times each node in the similarity search index is visited during search given a fixed number of queries, which we denote by Pm⁢(𝕩i)subscript𝑃𝑚subscript𝕩𝑖P\_{m}(\\mathbb{x}\_{i})italic\_P start\_POSTSUBSCRIPT italic\_m end\_POSTSUBSCRIPT ( blackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) to indicate that node 𝕩isubscript𝕩𝑖\\mathbb{x}\_{i}blackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT is visited exactly m𝑚mitalic\_m times during a fixed number of k𝑘kitalic\_k-NN queries for each one of the datasets in Table [3](https://arxiv.org/html/2412.01940v2#S6.T3 "Table 3 ‣ 6.2. Methodology ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”"). We show that this distribution is skewed to the right, thus confirming that certain nodes (highway nodes) are visited a disproportionate number of times. Next, using this distribution, we selectively choose the most visited nodes in the similarity search graph to be the hub node clusters and show evidence that these nodes are more connected to each other than random nodes using hypothesis tests. In the last experiment, we show that not only are these highway nodes more connected, they also allow for faster graph traversals for queries, hence supporting the claim that we no longer need hierarchy in high dimensional vector search where fast query times evolve as a result of the presence of the hub-highways.

### 6.3. Skewness of the Node Access Distribution

As described above, for this study we consider the discrete distribution Pm⁢(𝕩i)subscript𝑃𝑚subscript𝕩𝑖P\_{m}(\\mathbb{x}\_{i})italic\_P start\_POSTSUBSCRIPT italic\_m end\_POSTSUBSCRIPT ( blackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ), 𝕩i∈𝒟subscript𝕩𝑖𝒟\\mathbb{x}\_{i}\\in\\mathcal{D}blackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ∈ caligraphic\_D, where 𝒟𝒟\\mathcal{D}caligraphic\_D is one of the datasets in Table [3](https://arxiv.org/html/2412.01940v2#S6.T3 "Table 3 ‣ 6.2. Methodology ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”"). For all these experiments we construct a HNSW index with parameters listed in Table [4](https://arxiv.org/html/2412.01940v2#S6.T4 "Table 4 ‣ 6.3. Skewness of the Node Access Distribution ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”") and import the base layer of the graph into FlatNav to construct a flat NSW index.

Table 4. Similarity search index parameters

| m𝑚mitalic\_m | e⁢f𝑒𝑓efitalic\_e italic\_f-construction | e⁢f𝑒𝑓efitalic\_e italic\_f-search | k𝑘kitalic\_k |
| --- | --- | --- | --- |
| 32 | 100 | 200 | 100 |

https://arxiv.org/html/2412.01940v2/extracted/6171912/images/node-access-distribution/node_access_2.pngFigure 9. Log-normalized node access count distribution Pm⁢(𝕩i)subscript𝑃𝑚subscript𝕩𝑖P\_{m}(\\mathbb{x}\_{i})italic\_P start\_POSTSUBSCRIPT italic\_m end\_POSTSUBSCRIPT ( blackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) for datasets using angular distance (left) and ℓ2subscriptℓ2\\ell\_{2}roman\_ℓ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT distance (right). Note that the x-axis is also log-normalized, so all histograms are skewed to the left – but the ℓ2subscriptℓ2\\ell\_{2}roman\_ℓ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT datasets have a much greater skew.

Figure [9](https://arxiv.org/html/2412.01940v2#S6.F9 "Figure 9 ‣ 6.3. Skewness of the Node Access Distribution ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”") shows the log-normalized node access count distribution for different datasets. We observe that as the dimension d𝑑ditalic\_d increases, this distribution becomes more skewed to the right for ℓ2subscriptℓ2\\ell\_{2}roman\_ℓ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT distance-based datasets, indicating that a subset of nodes are visited much more often than the rest of the nodes in the graph. The cosine distance, on the other hand, is known to have anti-hub properties that prevent such a dramatic skew even for d∈{1024,1536}𝑑10241536d\\in\\{1024,1536\\}italic\_d ∈ { 1024 , 1536 }. This is consistent with the results observed by (Radovanovic et al., [2010](https://arxiv.org/html/2412.01940v2#bib.bib40 "")). The increased skewness of the Pm⁢(𝕩i)subscript𝑃𝑚subscript𝕩𝑖P\_{m}(\\mathbb{x}\_{i})italic\_P start\_POSTSUBSCRIPT italic\_m end\_POSTSUBSCRIPT ( blackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) distribution as d𝑑ditalic\_d increases suggests that highway nodes occur as a result of the intrinsic dimensionality of the datasets.

Confounding mechanisms: While Figure [9](https://arxiv.org/html/2412.01940v2#S6.F9 "Figure 9 ‣ 6.3. Skewness of the Node Access Distribution ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”") confirms the existence of hub nodes in the dataset, it does not distinguish between hubs that arise from the properties of the underlying metric space and hubs that form through some other mechanism. It is possible that preferential attachment explains the formation of hubs, since NSW graphs are built incrementally by sequentially adding points to an existing graph. Nodes that are added early in graph construction may become hubs by accumulating a greater-than-average share of inbound graph links, rather than by being popular neighbors in the metric space.

To investigate the effects of preferential attachment, we computed the variance (R2superscript𝑅2R^{2}italic\_R start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT of a linear model) in the empirical node access distribution explained by the insertion ordering(Table [5](https://arxiv.org/html/2412.01940v2#S6.T5 "Table 5 ‣ 6.3. Skewness of the Node Access Distribution ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”")). We log-transformed both the node access count and the insertion order before running the linear model and confirmed that the residuals are approximately normal by visually examining the QQ plots (p<10−6𝑝superscript106p<10^{-6}italic\_p < 10 start\_POSTSUPERSCRIPT - 6 end\_POSTSUPERSCRIPT for all models).

We observe a modest effect from the node insertion order in our synthetic data. This is particularly true for the angular datasets, which we believe to be due to the weaker hubness phenomena produced by the angular distance metric. Preferential attachment may account for a relatively greater share of the node access distribution when metric hubs are not present to heavily skew the distribution.

Ideally, we would repeat this analysis using the K𝐾Kitalic\_K-occurrence distribution, to show that the hubness of the metric space is more strongly predictive of the node acccess count than the insertion order. Unfortunately, it is not feasible to compute the K𝐾Kitalic\_K-occurrence distribution due to the O⁢(n2)𝑂superscript𝑛2O(n^{2})italic\_O ( italic\_n start\_POSTSUPERSCRIPT 2 end\_POSTSUPERSCRIPT ) brute-force computation cost. However, we believe that the results in Table [5](https://arxiv.org/html/2412.01940v2#S6.T5 "Table 5 ‣ 6.3. Skewness of the Node Access Distribution ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”") still support the idea that the dimensionality of the metric space strongly contributes to the formation of hubs in the Hub-Highway Hypothesis, especially when combined with the evidence in Figure [9](https://arxiv.org/html/2412.01940v2#S6.F9 "Figure 9 ‣ 6.3. Skewness of the Node Access Distribution ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”")).

Table 5. Correlation analysis for node insertion order and node access count, to determine effects of preferential attachment.

| Dataset | Dimension | Explained Variance (%) |
| :----------------------- | :-------- | :-------------------- |
| IID Normal (Angular)     | 16        | 3.0                   |
| IID Normal (Angular)     | 32        | 8.7                   |
| IID Normal (Angular)     | 64        | 16.6                  |
| IID Normal (Angular)     | 128       | 23.3                  |
| IID Normal (Angular)     | 256       | 24.6                  |
| IID Normal (Angular)     | 1024      | 24.1                  |
| IID Normal (Angular)     | 1536      | 23.9                  |
| IID Normal (L2)          | 16        | <0.1                  |
| IID Normal (L2)          | 32        | 3.1                   |
| IID Normal (L2)          | 64        | 7.6                   |
| IID Normal (L2)          | 128       | 8.7                   |
| IID Normal (L2)          | 256       | 7.1                   |
| IID Normal (L2)          | 1024      | 7.1                   |
| IID Normal (L2)          | 1536      | 6.6                   |
| GloVe (Angular)          | 100       | 0.2                   |
| NYTimes (Angular)        | 256       | 0.3                   |
| GIST (L2)                | 960       | <0.1                  |
| Yandex-DEEP (L2)         | 96        | 0.3                   |
| Microsoft-SpaceV (L2)    | 100       | 0.5                   |

### 6.4. Subgraph Connectivity of the Hub-Highway Nodes

Having demonstrated the occurrence of highway nodes, in the next set of experiments we present empirical evidence confirming that these nodes exhibit strong connectivity in the graph. One reasonable approach could be to identify hub nodes by thresholding the node access distribution (e.g., to the top 5% by access frequency) and determining whether these nodes form a connected component. However, this is strongly influenced by the threshold probability, and in any case the hubs need not form a single subgraph to support the Hub Highway Hypothesis.

Instead, we rely on statistical hypothesis testing to determine whether hub nodes are likely to connect to other hub nodes. We begin by explaining our procedure to identify hubs. Let 𝕩i,1≤i≤nsubscript𝕩𝑖1𝑖𝑛\\mathbb{x}\_{i},1\\leq i\\leq nblackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT , 1 ≤ italic\_i ≤ italic\_n, be the vectors in a similarity search index for any dataset 𝒟𝒟\\mathcal{D}caligraphic\_D under consideration.

- •

Using the empirical node access distribution Pm⁢(𝕩i)subscript𝑃𝑚subscript𝕩𝑖P\_{m}(\\mathbb{x}\_{i})italic\_P start\_POSTSUBSCRIPT italic\_m end\_POSTSUBSCRIPT ( blackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ), we identify hub nodes as those that fall into either the 95thth{}^{\\text{th}}start\_FLOATSUPERSCRIPT th end\_FLOATSUPERSCRIPT or 99thth{}^{\\text{th}}start\_FLOATSUPERSCRIPT th end\_FLOATSUPERSCRIPT percentile of node access counts. We assign a binary label to each node to indicate whether it is a hub. Let h:𝒟→{0,1}:ℎ→𝒟01h:\\mathcal{D}\\to\\{0,1\\}italic\_h : caligraphic\_D → { 0 , 1 } be this assignment function with h⁢(𝕩i)=1ℎsubscript𝕩𝑖1h(\\mathbb{x}\_{i})=1italic\_h ( blackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) = 1 for nodes identified as hubs.

- •

We wish to estimate the likelihood that a randomly-chosen out-neighbor of a hub node is, itself, a hub. To do so, we examine the 1-hop out-degree expansion of each hub and count the number of adjacent hub nodes. By repeating this process for each hub node, we obtain a discrete distribution for the number of hubs to which each hub node is connected.

- •

Similarly, we select a set of random non-hub nodes from V≔𝒟∖⋃i=1nh⁢(𝕩i)=1≔𝑉𝒟superscriptsubscript𝑖1𝑛ℎsubscript𝕩𝑖1V\\coloneqq\\mathcal{D}\\setminus\\bigcup\_{i=1}^{n}h(\\mathbb{x}\_{i})=1italic\_V ≔ caligraphic\_D ∖ ⋃ start\_POSTSUBSCRIPT italic\_i = 1 end\_POSTSUBSCRIPT start\_POSTSUPERSCRIPT italic\_n end\_POSTSUPERSCRIPT italic\_h ( blackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) = 1. For each node 𝕩i∈Vsubscript𝕩𝑖𝑉\\mathbb{x}\_{i}\\in Vblackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ∈ italic\_V, we compute the same quantity to find the number of hubs with which non-hubs are connected, allowing us to construct the equivalent distribution for non-hubs.

Our hypothesis test investigates whether these two distributions differ. The null hypothesis is that hubs and non-hubs are equally likely to attach to hubs, and the alternative hypothesis is that hubs display different connectivity behavior than the rest of the graph. A finding that hubs are statistically more likely to attach to other hubs will support the Hub Highway Hypothesis.

We measure statistical significance using the standard two-sample parametric t𝑡titalic\_t-test as well as the non-parametric Mann-Whitney U-test (Mann and Whitney, [1947](https://arxiv.org/html/2412.01940v2#bib.bib34 "")), which is particularly suitable for ANN datasets because it does not require the normality assumption.
Note that we consider dataset sizes larger than those often encountered in hypothesis testing (n>103𝑛superscript103n>10^{3}italic\_n > 10 start\_POSTSUPERSCRIPT 3 end\_POSTSUPERSCRIPT).
A well-known consequence of the Central Limit Theorem (CLT) (Durrett, [2019](https://arxiv.org/html/2412.01940v2#bib.bib14 "")) is that the U-statistic used in non-parametric tests such as the Mann-Whitney test will converge to a normal distribution as the sample size increases. This, in turn, leads to p𝑝pitalic\_p-values that approach 0 whenever there is a true difference between any two populations under consideration. For this reason, we also consider the effect size in our test and constrain the sample size to be 1000 for both populations.

Table [6](https://arxiv.org/html/2412.01940v2#S6.T6 "Table 6 ‣ 6.4. Subgraph Connectivity of the Hub-Highway Nodes ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”") shows the results when we use the top-5% threshold to select hub nodes. Assuming the regular 0.05 threshold for rejecting the null hypothesis, note that in all by five cases we reject the null hypothesis under the Mann-Whitney U𝑈Uitalic\_U-test (and all by six cases using the two-sample t𝑡titalic\_t-test). Unsurprisingly, the effect size is much higher in the synthetic ℓ2subscriptℓ2\\ell\_{2}roman\_ℓ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT datasets, likely because this metric and distribution induce strong metric hubness properties in the dataset and thus a more connected subgraph.

Notably, the Yandex-DEEP benchmark does not exhibit the subgraph connectivity observed in most other benchmarks.
Unlike the other embeddings in our collection, Yandex-DEEP was obtained by applying PCA and ℓ2subscriptℓ2\\ell\_{2}roman\_ℓ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT normalization to the last fully-connected layer of GoogleNet (Szegedy et al., [2014](https://arxiv.org/html/2412.01940v2#bib.bib45 "")). Theoretically, ℓ2subscriptℓ2\\ell\_{2}roman\_ℓ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT normalization should reduce the prevalence of hubs by restricting the distribution to the surface of the unit sphere. Yandex-DEEP also has the most uniform node access distribution of the ℓ2subscriptℓ2\\ell\_{2}roman\_ℓ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT datasets in Figure [9](https://arxiv.org/html/2412.01940v2#S6.F9 "Figure 9 ‣ 6.3. Skewness of the Node Access Distribution ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”"). We believe that this may explain why Yandex-DEEP hubs are not as well-connected.

Table [7](https://arxiv.org/html/2412.01940v2#S6.T7 "Table 7 ‣ 6.4. Subgraph Connectivity of the Hub-Highway Nodes ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”") shows the results when hubs are identified using the top-1% threshold. Here, we are able to reject the null hypothesis (p<0.05𝑝0.05p<0.05italic\_p < 0.05) in all but one case for both the Mann-Whitney U𝑈Uitalic\_U-test and the two-sample t𝑡titalic\_t-test. We also observe much larger effect sizes with the top-1% selection criterion, demonstrating that the strongest hubs cluster tightly in the graph. Taken together, these two statistical tests support the idea that hub nodes are often connected to other hubs.

Table 6. Two-sample t𝑡titalic\_t-test and Mann-Whitney U-test results. Hub nodes are selected using the P95 threshold of the node access distribution.

| Dataset                   | Dim  | Mann-Whitney                             | Two-Sample t𝑡titalic\_t-Test                            | Effect Size |
| :------------------------ | :--- | :--------------------------------------- | :--------------------------------------- | :---------- |
| IID Normal (Angular)      | 16   | 0​.3629                                  | 0.3090                                   | 0.0267      |
| IID Normal (L2)           | 16   | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.3737      |
| IID Normal (Angular)      | 32   | 0.0335                                   | 0.0516                                   | 0.0872      |
| IID Normal (L2)           | 32   | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.4275      |
| IID Normal (Angular)      | 64   | 0.0216                                   | 0.0148                                   | 0.1165      |
| IID Normal (L2)           | 64   | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.3965      |
| IID Normal (Angular)      | 128  | 0.0083                                   | 0.0083                                   | 0.1284      |
| IID Normal (L2)           | 128  | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.3773      |
| IID Normal (Angular)      | 256  | 0.0009                                   | 0.0007                                   | 0.1723      |
| IID Normal (L2)           | 256  | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.2620      |
| IID Normal (Angular)      | 1024 | 0.1000                                   | 0.1114                                   | 0.0652      |
| IID Normal (L2)           | 1024 | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.2361      |
| IID Normal (Angular)      | 1536 | 0.0957                                   | 0.1141                                   | 0.0645      |
| IID Normal (L2)           | 1536 | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.2512      |
| GloVe                     | 100  | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.2550      |
| NYTimes                   | 256  | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.4488      |
| GIST                      | 960  | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.3645      |
| Yandex-DEEP               | 96   | 0.5002                                   | 0.5000                                   | 0.0000      |
| Microsoft-SpaceV          | 100  | 0.1586                                   | 0.1585                                   | 0.0535      |

Table 7. Two-sample t𝑡titalic\_t-test and Mann-Whitney U-test results. Hub nodes are selected using the P99 threshold of the node access distribution.

| Dataset                | Dim  | Mann-Whitney                             | Two-Sample t𝑡titalic\_t-Test                            | Effect Size |
| :--------------------- | :--- | :--------------------------------------- | :--------------------------------------- | :---------- |
| IID Normal (Angular)   | 16   | 0.0006                                   | 0.0006                                   | 0.1745      |
| IID Normal (L2)        | 16   | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.6621      |
| IID Normal (Angular)   | 32   | 0.0347                                   | 0.0347                                   | 0.0972      |
| IID Normal (L2)        | 32   | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.8173      |
| IID Normal (Angular)   | 64   | 0.0359                                   | 0.0417                                   | 0.0927      |
| IID Normal (L2)        | 64   | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.8725      |
| IID Normal (Angular)   | 128  | 0.0093                                   | 0.0070                                   | 0.1316      |
| IID Normal (L2)        | 128  | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.8428      |
| IID Normal (Angular)   | 256  | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.3110      |
| IID Normal (L2)        | 256  | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.8582      |
| IID Normal (Angular)   | 1024 | 0.1472                                   | 0.1318                                   | 0.0598      |
| IID Normal (L2)        | 1024 | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.8314      |
| IID Normal (Angular)   | 1536 | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.2356      |
| IID Normal (L2)        | 1536 | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.8568      |
| GloVe                  | 100  | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.7642      |
| NYTimes                | 256  | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.9305      |
| GIST                   | 960  | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | <10−5absentsuperscript105\\!<\\!10^{-5}< 10 start\_POSTSUPERSCRIPT - 5 end\_POSTSUPERSCRIPT | 0.6829      |
| Yandex-DEEP            | 96   | 0.0013                                   | 0.0013                                   | 0.1614      |
| Microsoft-SpaceV       | 100  | 0.0011                                   | 0.0011                                   | 0.1644      |

### 6.5. Hub-Highway Nodes Enable Fast Traversal

In this section, we show that not only are highway nodes strongly connected to each other, they also allow queries to quickly traverse the similarity search graph.
While it is not surprising that a well-connected subgraph of frequently visited nodes would enable this behavior, it is not immediately clear that queries use the highway in the way predicted by our hypothesis – to quickly identify a neighborhood for deep exploration.
To investigate this question, we track the sequence of nodes visited during beam search. We examine thousands of queries to determine the fraction of time spent on hub nodes in different phases of search.

Since beam search takes a variable number of steps for each query, we normalize by the total search length when presenting the results. More formally, suppose that 𝕩1,𝕩2,…,𝕩lsubscript𝕩1subscript𝕩2…subscript𝕩𝑙\\mathbb{x}\_{1},\\mathbb{x}\_{2},\\ldots,\\mathbb{x}\_{l}blackboard\_x start\_POSTSUBSCRIPT 1 end\_POSTSUBSCRIPT , blackboard\_x start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT , … , blackboard\_x start\_POSTSUBSCRIPT italic\_l end\_POSTSUBSCRIPT is a length-l𝑙litalic\_l sequence of such nodes visited by a query. We use the hub node assignment heuristic discussed in section [6.4](https://arxiv.org/html/2412.01940v2#S6.SS4 "6.4. Subgraph Connectivity of the Hub-Highway Nodes ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”") to label h⁢(𝕩i)ℎsubscript𝕩𝑖h(\\mathbb{x}\_{i})italic\_h ( blackboard\_x start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT ) each of these nodes as hubs / non-hubs. Then, we then split the sequence into bins and compute the prevalence of hubs in each bin. For bin Bisubscript𝐵𝑖B\_{i}italic\_B start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT, this is given by

| | | |
| --- | --- | --- |
| | (1\|Bi\|)⁢∑𝕩j∈Bih⁢(𝕩j)1subscript𝐵𝑖subscriptsubscript𝕩𝑗subscript𝐵𝑖ℎsubscript𝕩𝑗\\left(\\frac{1}{\|B\_{i}\|}\\right)\\sum\_{\\mathbb{x}\_{j}\\in B\_{i}}h(\\mathbb{x}\_{j})( divide start\_ARG 1 end\_ARG start\_ARG \| italic\_B start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT \| end\_ARG ) ∑ start\_POSTSUBSCRIPT blackboard\_x start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT ∈ italic\_B start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT end\_POSTSUBSCRIPT italic\_h ( blackboard\_x start\_POSTSUBSCRIPT italic\_j end\_POSTSUBSCRIPT ) | |

where \|Bi\|subscript𝐵𝑖\|B\_{i}\|\| italic\_B start\_POSTSUBSCRIPT italic\_i end\_POSTSUBSCRIPT \| is the bin size (fixed to 30303030 in our analysis). By averaging this value over all queries, we can plot the likelihood of visiting a hub as the search progresses.

Figure [10](https://arxiv.org/html/2412.01940v2#S6.F10 "Figure 10 ‣ 6.5. Hub-Highway Nodes Enable Fast Traversal ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”") shows results for the Gist, GloVe, Microsoft SpaceV and Yandex-DEEP benchmark datasets. We observe that queries tend to concentrate in the highway structures early in search, shown by the high percentage of hub nodes visited in the first 5-10% of the search steps. This result suggests that the highway allows queries to quickly navigate the similarity search graph until they find the region of the graph best suited for deep exploration. The propensity of the query to visit hubs appears to be tied to the hubness properties of the dataset. For example, the GloVe dataset uses the angular distance and has less pronounced hubs (Figure [9](https://arxiv.org/html/2412.01940v2#S6.F9 "Figure 9 ‣ 6.3. Skewness of the Node Access Distribution ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”")), and queries spend a lower percentage of their time in hub nodes in this dataset (Figure [10(b)](https://arxiv.org/html/2412.01940v2#S6.F10.sf2 "In Figure 10 ‣ 6.5. Hub-Highway Nodes Enable Fast Traversal ‣ 6. The Hub Highway Hypothesis ‣ Down with the Hierarchy: The ‘H’ in HNSW Stands for “Hubs”")). On the other hand, the GIST dataset has some of the highest rates of highway utilization and is also our highest-dimensional ℓ2subscriptℓ2\\ell\_{2}roman\_ℓ start\_POSTSUBSCRIPT 2 end\_POSTSUBSCRIPT dataset.

https://arxiv.org/html/2412.01940v2/x1.png(a)Gist
https://arxiv.org/html/2412.01940v2/x2.png(b)GloVe
https://arxiv.org/html/2412.01940v2/x3.png(c)Microsoft SpaceV
https://arxiv.org/html/2412.01940v2/x4.png(d)Yandex Deep

Figure 10. Highway nodes allow queries to traverse the graph faster. We observe that early in search,

### 6.6. Discussion

We observe substantial evidence from the above sequence of experiments supporting the Hub Highway Hypothesis. Although it has long been established that the hubness phenomenon negatively affect common applications, such as clustering and even near neighbor search recall, existing ANNS methods, such as HNSW and NSG (Zhao et al., [2023](https://arxiv.org/html/2412.01940v2#bib.bib52 "")) mostly emphasize algorithmic improvements and performance optimizations only. We have shown that leveraging the inherent structures in the data, particularly hub-highway occurrences, should be central to the design of new scalable similarity search indexes.

As discussed earlier, the skewness of the k𝑘kitalic\_k-occurrence distribution Nksubscript𝑁𝑘N\_{k}italic\_N start\_POSTSUBSCRIPT italic\_k end\_POSTSUBSCRIPT directly affects the quality of search in terms of recall. Given our empirical results showing that hub-highways allow queries to traverse the graph faster, interesting future research directions might consider leveraging this distribution to improve edge pruning heuristics or judiciously choose which edges to explore during beam search over proximity graphs.

Small-World Graphs: The network science research community has known for decades that long-range connections and hubs induce the formation of “small-world” graphs that are easily traversed (Watts and Strogatz, [1998](https://arxiv.org/html/2412.01940v2#bib.bib49 "")).
This idea has been enormously influential in ANNS, providing the motivation for both NSW and HNSW (Malkov et al., [2012](https://arxiv.org/html/2412.01940v2#bib.bib31 ""), [2014](https://arxiv.org/html/2412.01940v2#bib.bib32 "")), but our results suggest that ANN graphs constructed over low-dimensional datasets may not in fact exhibit small-world properties.
Because the k𝑘kitalic\_k-occurrence distribution is near-uniform for intrinsically low-dimensional data distributions, a pure k𝑘kitalic\_kNN graph (without pruning or long-range links) will not create hubs with a high in-degree.
We believe that hierarchical structures are helpful in low dimensions because they help to induce hub behavior, by ensuring that search always begins from a small set of nodes.
However, this is not necessary to produce hubs and induce small-world properties in high dimensions. The k𝑘kitalic\_kNN graph construction process is sufficient on its own, because the hub highway emerges in high dimensions.

Scientific Implications:
Our work reveals that the hub highway is an intrinsic and naturally-forming structure in high-dimensional proximity graphs. We believe this observation is both novel and has important implications for the scaling potential of many traversal heuristics.
Specifically, we expect the benefits of sophisticated search initialization methods to decay under hub-style preferential attachment.

Initialization is a recurring and popular research direction for graph-based near-neighbor search, and leading algorithms vary greatly in their initialization techniques.
The research question dates back to the seminal 1993 paper by Arya and Mount (Arya and Mount, [1993](https://arxiv.org/html/2412.01940v2#bib.bib3 "")), which conjectured that clever search initialization – in their case, via k⁢d𝑘𝑑kditalic\_k italic\_d-tree – could improve performance over random initialization.
Over the following three decades, the research community has investigated diverse stratified sampling based on clusters (Sebastian and Kimia, [2002](https://arxiv.org/html/2412.01940v2#bib.bib42 "")), vantage-point trees (Iwasaki, [2010](https://arxiv.org/html/2412.01940v2#bib.bib20 "")), seeds formed from the graph expansion of k⁢d𝑘𝑑kditalic\_k italic\_d-trees (Iwasaki and Miyazaki, [2018](https://arxiv.org/html/2412.01940v2#bib.bib22 "")) and previously-visited nodes (Wang and Li, [2012](https://arxiv.org/html/2412.01940v2#bib.bib48 "")), hierarchical graphs (Malkov and Yashunin, [2016](https://arxiv.org/html/2412.01940v2#bib.bib33 "")), hierarchical clustering (Munoz et al., [2019](https://arxiv.org/html/2412.01940v2#bib.bib36 "")), dataset medoids (Jayaram Subramanya et al., [2019](https://arxiv.org/html/2412.01940v2#bib.bib24 "")), and several other methods before finally returning to cluster-stratified candidates (Oguri and Matsui, [2024](https://arxiv.org/html/2412.01940v2#bib.bib38 ""); Ni et al., [2023](https://arxiv.org/html/2412.01940v2#bib.bib37 "")) and random entry nodes (Jaiswal et al., [2022](https://arxiv.org/html/2412.01940v2#bib.bib23 "")).

How is it that these early papers on graph search show performance gains, even as today’s best vector databases return to simple initializations without performance loss? Our hub highway hypothesis offers a clear explanation for this apparent contradiction: In the early 2000s and 2010s, datasets were low-dimensional and initialization was important to avoid local minima and long graph detours. However, modern vector databases contain data that is sufficiently high-dimensional to naturally form a fast-routing structure, explaining why initialization no longer drives performance. Based on our results, we conjecture that the largest algorithmic improvements to graph-based ANNS should come from optimizations that affect the connectivity and cost of traversal in the base graph, such as link pruning and search algorithm design.

## 7\. Conclusion

Approximate near neighbor search has become an increasingly crucial computational workload in recent years with the seminal Hierarchical Navigable Small World (HNSW) algorithm continuing to garner significant interest and adoption from practitioners. To that end, this paper presents the first comprehensive study on the utility of the hierarchical component of HNSW over numerous large-scale datasets and performance metrics. Ultimately, we find that the hierarchy of HNSW provides no clear benefit on high-dimensional datasets and can be removed without any discernible loss in performance while providing memory savings.

While similar observations have been made before in the literature (Lin and Zhao, [2019](https://arxiv.org/html/2412.01940v2#bib.bib29 ""); Coleman et al., [2022](https://arxiv.org/html/2412.01940v2#bib.bib9 ""); Dobson et al., [2023](https://arxiv.org/html/2412.01940v2#bib.bib11 "")), we are, to our knowledge, the first to conduct an exhaustive study over modern benchmark datasets and taking extensive care to compare implementations with performance engineering parity. Furthermore, we go beyond prior works and study _why_ the hierarchy does not help, culminating in our introduction of the _Hub Highway Hypothesis_, an empirical result on how proximity graphs built over high-dimensional metric spaces leverage a small subset of well-connected nodes to traverse the network quickly, akin to highways and exits in transportation systems.

As part of our benchmarking study and analysis, we also release an open-source, high-performance flat navigable small world implementation, called flatnav, that we hope will serve as an additional resource to both researchers and industry practitioners. We also hope that our work can inspire future directions in algorithm design for ANN search, such as in better strategies for exploiting the hub highway structure we observed or even designing new algorithms that do manage to leverage the idea of hierarchy effectively. In the short term, we believe that our results provide immediate implications for practitioners seeking to save memory or simplify their vector database implementations and we look forward to further partnering with the community on these endeavors.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="lanns-a-web-scale-approximate-nearest-neighbor-lookup-system.md">
<details>
<summary>LANNS: A Web-Scale Approximate Nearest Neighbor Lookup System</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.vldb.org/pvldb/vol15/p850-doshi.pdf>

# LANNS: A Web-Scale Approximate Nearest Neighbor Lookup System 

# Ishita Doshi 

LinkedIn idoshi@linkedin.com 

# Dhritiman Das 

LinkedIn dhdas@linkedin.com 

# Ashish Bhutani 

Uber abhutani@uber.com 

# Rajeev Kumar 

LinkedIn rkumar6@linkedin.com 

# Rushi Bhatt 

Compass rushi.bhatt@compass.com 

# Niranjan Balasubramanian 

LinkedIn nbalasubramanian@linkedin.com 

## ABSTRACT 

Nearest neighbor search (NNS) has a wide range of applications in information retrieval, computer vision, machine learning, databases, and other areas. Existing state-of-the-art algorithm for nearest neighbor search, Hierarchical Navigable Small World Networks (HNSW), is unable to scale to large datasets of 100M records in high dimensions. In this paper, we propose LANNS, an end-to-end platform for Approximate Nearest Neighbor Search, which scales for web-scale datasets. Library for Large Scale Approximate Nearest Neighbor Search (LANNS) is deployed in multiple produc-tion systems for identifying top-K (100 ≤ k ≤ 200) approximate nearest neighbors with a latency of a few milliseconds per query, high throughput of ∼2.5k Queries Per Second (QPS) on a single node, on large (e.g., ∼ 180M data points) high dimensional (50-2048 dimensional) datasets. 

PVLDB Reference Format: 

Ishita Doshi, Dhritiman Das, Ashish Bhutani, Rajeev Kumar, Rushi Bhatt, and Niranjan Balasubramanian. LANNS: A Web-Scale Approximate Nearest Neighbor Lookup System. PVLDB, 15(4): 850 - 858, 2022. doi:10.14778/3503585.3503594 

## 1 INTRODUCTION 

Nearest-neighbor search (NNS) is an effective technique for infor-mation retrieval and several machine learning applications. Despite its simplicity and wide-ranging utility, efficiently building and serv-ing k-nearest neighbor data structures to web-scale has remained a challenge. In this paper, we describe LANNS (Large Scale Approxi-mate Nearest Neighbor Search), a system designed and deployed in a web-scale environment at LinkedIn. LANNS has been deployed in a production environment for identifying top-K (with k ranging from 100-200) approximate nearest neighbors with very low latency (few milliseconds per query), very high throughput (roughly 2.5K Queries Per Second (QPS) on a single node), on large (e.g., 180M data points) high dimensional (e.g., 128, 256, or 2048 dimensional) data sets. 

> This work is licensed under the Creative Commons BY-NC-ND 4.0 International License. Visit https://creativecommons.org/licenses/by-nc-nd/4.0/ to view a copy of this license. For any use beyond those covered by this license, obtain permission by emailing info@vldb.org. Copyright is held by the owner/author(s). Publication rights licensed to the VLDB Endowment. Proceedings of the VLDB Endowment, Vol. 15, No. 4 ISSN 2150-8097. doi:10.14778/3503585.3503594

Broadly, nearest neighbor search approaches fall into four cate-gories. They can be tree-based[ 6, 9, 21 , 25 ], product quantization-based[ 11 , 12 , 16 , 17 ], Locality Sensitive Hashing (LSH) based[ 1, 2, 5,13 , 29 ], or graph-based[ 10 , 14 , 19 , 20 ]. Most of the scalable methods return approximate nearest neighbors (i.e., miss out on some of the k-nearest neighbors in the results) in order to speed up the search. The recall, measured as the fraction of true 𝑘 -nearest neighbors returned in a result set of size 𝑘 , is generally traded off for the query latency or throughput. Figure 1[ 4], shows such a compromise be-tween various state of the art algorithms (Annoy[ 25 ], BallTree[ 7], Faiss-IVF[ 15 , 16 ], FLANN[ 24 ], Hierarchical Navigable Small World (HNSW) graph[ 20 ], KGraph[ 10 ], PANNG[ 14 ], PyNNDescent[ 22 ]and SWGraph [ 19 ]) on the SIFT1M dataset. It is evident from Fig-ure 1, and other offline benchmarks conducted by us, that HNSW tends to outperform competitors considering QPS vs recall tradeoff. We have used HNSW as the core approximate nearest neighbor (ANN) algorithm. However, LANNS has been built to be extensible to support other ANN algorithms with a bounded drop in recall. Despite the favorable performance characteristics and popularity of HNSW[ 20 ], building the HNSW data structure does not scale well for production system with large, high dimensional datasets. For example, building the HNSW index on a real dataset of size 

2.7𝑀 with 256 dimensions takes about 2 hours 20 minutes on a single machine. At LinkedIn, we often have to serve 𝑘 -NN queries on datasets containing 100M-500M records with dimensionality of 50-2048 . This renders the default single-machine HNSW index build methods impractical. Furthermore, beyond a certain index size, procurement and maintenance cost of high memory servers also increases compared to commodity hardware. It is therefore necessary to be able to split up the dataset into multiple shards. In this paper, we present LANNS, our end-to-end platform cur-rently in production at LinkedIn, which enables web-scale nearest neighbor search in a variety of applications. As part of LANNS, we propose a two-level data partitioning strategy that allows us to scale the HNSW algorithm to web-scale datasets at index build time, as well as for online serving. We show that using this parallel building of separate HNSW indices, one for each data partition, and flexible data segmentation, we achieve fast index build and online serving. Our proposed data segmentation techniques also bound the drop in recall as compared to the HNSW algorithm. These segmentation techniques have theoretical guarantees on the recall as a function of the tuneable partitioning parameters that are on similar lines as [ 9]. We demonstrate the empirical performance of our proposed strategy on two open-source and four real-world datasets. 

850 Figure 1: Recall v/s QPS on SIFT1M. Left: 10 nearest neighbors, Right: 100 nearest neighbors 

## 1.1 Our Contributions 

Our contributions in this paper are as follows: (1) We propose a two-level data partitioning strategy that al-lows us to scale HNSW indexing to web-scale datasets. (2) We propose a flexible data segmentation framework within each partition which allows further scaling. We propose two segmentation strategies with guarantees for a bounded drop in recall as a function of data size. (3) We show, through extensive benchmarking, that for a ma-jority of queries, high recall is achieved while querying only one or a few segments, and our partitioning and seg-mentation framework performs and scales well. (4) We demonstrate the performance of our end-to-end sys-tem on various open-source and real datasets and show its favorable scalability properties. The paper is organized as follows. We discuss related work in Section 2. In Section 3, we motivate two-level data partitioning, followed by the partitioning strategies. In Section 4, we describe the Spark framework for LANNS. In Section 5, we present our ex-periments on open source and real datasets, with a brief discussion on design choices. We present our online framework in Section 6, and conclude and discuss future work in Section 7. 

## 2 RELATED WORK 

In this section, we will discuss techniques and algorithms used for nearest neighbor search, as well as some works similar to LANNS. 

Locality Sensitive Hashing (LSH) [13 ] – LSH is a hashing based technique where points are assigned to buckets such that, with high probability, similar points are found within the same bucket, while points far from each other are likely to be in different buckets. Variants of LSH can be data dependent[ 1, 2, 5, 29 ] or data independent. This method builds the index in linear time and has good theoretical guarantees of sub-linear query time, however, for adversarial data, this algorithm might run as slow as a linear scan. 

Tree-based methods [ 9, 21 , 25 ] – These tree based methods build one or a set of trees by recursively splitting the dataset. In [25 ], a set of trees are built where each tree is constructed by picking two points at random and splitting the dataset using a hyperplane separating the two points. In [ 21 ] the authors propose Approximate Principal Direction Trees, which recursively splits the data points using approximate eigenvectors. They claim that the method re-duces average diameter at the same rate as PCA Trees [ 28 ] with lower runtime. In [ 9], a tree is built by randomly partitioning the data using random hyperplanes. They also propose spills, i.e., route data points or queries to multiple partitions based on their distance to the splitting hyperplane. These algorithms give low recall when queries are near the boundaries of splitting hyperplanes. 

Product Quantization (PQ) [ 11 , 12 , 16 , 17 ] – PQ is a compres-sion based ANN search method. The main motivation behind PQ is to compress the space into a product of lower dimension spaces and to quantize each of these subspaces separately. The dataset is split into multiple smaller, tall datasets based on their dimensions, and each of these sub-datasets are clustered into 𝑘 clusters. One advantage is the compression of datasets, which results in signif-icant speedup. However, in this approach as well, exact nearest neighbors might lie in other clusters. 

Sparsest Cut and Eigenvectors [ 27 ] – Sparsest cut aims to partition the vertices of a graph in a way that the weights of the edges cut during this partitioning are as small as possible. This is typically done by using the Laplacian of the adjacency matrix of the graph and using the second smallest eigenvector of the same. [ 27 ]shows that using the second smallest eigenvector of the Laplacian has some proven theoretical guarantees. 

Hierarchical Navigable Small World(HNSW) [ 20 ] – A graph-based technique built on the idea of Small Worlds (SW). Suppose you build a hierarchy of SW graphs that separate links according to their lengths. At earlier stages of the search, you traverse long edges and zoom into a local minima for the query, and at later stages, you search the neighborhood of the local minima to find the nearest neighbors to the query. This method has the benefit of tuning parameters to adjust the accuracy v/s speed trade-off, and the space v/s speed trade-off. It has a polylogarithmic time complexity and is highly competitive on real-world datasets[ 4 ]. However, the HNSW indexing is not scalable for large datasets in production. We extend this work to scale to large datasets with an implementation in Apache Spark[ 30 ] and employing various techniques motivated by Random Projection Trees[ 9], Approximate Principal Direction Trees[21] and Sparsest Cuts[27]. Another related work, SONG[ 31 ] leverages GPUs to scale NNS. It might not always be feasible to provison GPUs for all practical use cases. With LANNS, we propose leveraging a shared Spark cluster for NNS. Another type of ANNS is where there is a trade-off between RAM and the query time or QPS[ 3, 26 ]. This may not be suitable for time sensitive (e.g., search) applications or use cases, where a decrease in QPS could cause a loss in trust of the users. 

## 3 TWO-LEVEL PARTITIONING 

In many real use cases, we often require the algorithm to scale to datasets of size 100M-500M. The state-of-the-art, HNSW algorithm, takes about 2 hours 20 minutes to index a dataset of 2.7M records. This becomes infeasible in real-world scenarios. Often these indices are used in production systems that do not have the capacity to support such large datasets. We propose a horizontal, two-level partitioning of the data such that each partition represents a subset of the dataset. We attain acceptable indexing times by building a separate HNSW index within each partition, and we host one, or a few, partitions on each online server node. The two-levels of partitioning, sharding and 

851 segmentation , are two different dimensions that help in solving two aspects of the scaling problem. 

## 3.1 Sharding 

Sharding, our first level of partitioning, is necessary for a very large dataset where the memory requirements for keeping the entire dataset is large and cannot be accommodated in a single node. For example, a dataset with 50M records in a 500-dimensional space would require approximately 93G storage. In addition to this 93G, we also need to consider the memory requirements of building a graph. Assuming that the total storage required would be about 128G, an index of this size would not fit in a production node with a standard memory configuration of 64G. Building customized production nodes with higher memory is not feasible since the cost per GB increases super-linearly with total machine memory due to the higher cost of compatible components, higher failure rates, etc. Thus, we propose our first level of partitioning as sharding .When a point is inserted, it is hashed to one particular shard using the key of the data point. This partitioning does not exploit any locality information and each query is routed to all shards of the LANNS index. The response is generated by merging all shard level candidates and picking the topK best candidates. 

Sharding allows us to scale horizontally by partitioning the dataset. Each shard is hosted on a separate server node, which in turn enables us to keep the memory requirement of a single server node under control, and allows us to use standard configuration server nodes with 64G memory. Let us consider a use case where the server node has enough memory but the indexing time is unacceptable. In such scenarios, with only one level of partitioning, we would create more shards. There is additional merge cost involved at the master/broker or the system which makes calls to the shards. Higher the number of shards, higher is the merge cost. The master, a system with low memory of 2G-4G, would need to merge the results from these shards and give the final topK responses. Considering the build time, one may use a large number of shards which could mean an in-creased merge cost, and possibly higher memory for use cases with a large number of shards. Having large number of shards also comes with an additional undesirable operational cost of maintaining a large number of systems in production, and increased hardware footprint in terms of the cluster (collection of server nodes) size. 

## 3.2 Segmentation 

Segmentation, our second level of partitioning aims at reducing the disadvantages of sharding. Each shard is further split into smaller partitions called segments. This segmentation can be done using same techniques as sharding, or smarter segmentation techniques that allow queries to be routed to one or only a few segments. Routing to a single segment during query retrieval may have a neg-ative impact on the topK recall, but smarter segmentation strategies can be employed to keep this impact bounded. We propose two "smarter" segmentation strategies learnt using the indexing data in Section 3.3. Employing these same techniques in sharding becomes complicated as the online service employs an external broker in front of the shards, which are not co-located. Another added advantage of segmentation is that segmentation provides the same scalability as sharding for offline ingestion 1,which is useful for cases where the dataset is small enough to fit into a single server node, but it is large enough to render the HNSW indexing time unacceptable. This helps to avoid setting up a multi-sharded setup till the time the dataset becomes large enough. For a large dataset, this also enables us to keep the number of shards under control. Each partition, i.e., each segment is built separately and in parallel. Thus, segmentation does not hamper the scalability of indexing. Since multiple segments are hosted within the same server node, it also reduces the online hardware footprint. As mentioned earlier, routing to one or a few segments can cause a drop in the recall. We propose segmentation techniques that bounds this drop in the recall. Another point to note is that in cases where a query is routed to multiple segments, there is an additional merge cost. For our online serving systems, this merge happens within the shard and does not require additional network I/O to send results from each shard to the broker node. 

## 3.3 Segmentation Strategies 

In this section, we describe three types of segmenters, the Random Segmenter (RS), Random Hyperplane Segmenter (RH), and Approx-imate Principal Direction Hyperplane Segmenters (APD). RS is a data-independent segmenter, whereas RH and APD segmenters are data-dependent. 

3.3.1 Random Segmenter (RS). In this particular segmenter, no type of learning from data is required. At indexing time, for each document, it randomly selects a segment where it should be routed. Since this type of segmenter has no guarantees about the locality of the data, a query vector would be routed to all segments. 

3.3.2 Random Hyperplane Segmenters(RH). Random Hyperplane Segmenters, motivated by Randomized Projection Trees[ 9 ], builds a short tree of hyperplanes. The motivation behind this work is the following– if two points are similar, they would be close in the space, and it is highly unlikely that a randomly chosen hyperplane would split the two. However, if two points are far, there would be a high probability that the two points would be split. This enforces a sense of locality. With high probability, points similar to each other would lie in the same partition. We exploit this intuition to design our segmenters as– at each internal node of our segmenter, we first generate a random hyperplane from the unit sphere and project all points on this generated hyperplane. We then perform a median split based on these projected values. However, with a low probability, this method faces the problem of missing nearest neighbors that lie across the boundary in the other partition. We employ the method of “virtual“ spill, where we maintain a left and right boundary around the splitting point. When a query point arrives and it lies within these left and right boundaries, we route the queries to both partitions. 2

We briefly describe the insertion and querying process and state the theoretical bounds provided in [ 9] which are directly applicable to RH segmenter. Let the dataset be represented by a matrix D of 

> 1It is worthwhile to note that indexing is done offline for online serving as well.
> 2Note that instead of using a virtual spill, we can also perform data side spill during ingestion, where data points lying within the left and right boundaries are routed to both partitions.

852 (a) Virtual Spill when query point (Q) is near the splitting hyper-plane (b) Probability of failure with increasing depth 

Figure 2: Spills and failure probability of Segmentation 

size 𝑛 × 𝑑 , where 𝑛 is the number of points and 𝑑 is the number of dimensions, and 𝛼 be the amount of spill. Let 𝑥 .ℎ refer to the projection of 𝑥 on ℎ, and 𝑈 denote the 𝑛 dimensional vector of projections, 𝑈 = D.ℎ . For insertion of a point 𝑥 , if 𝑥 .ℎ < 𝑚𝑒𝑑𝑖𝑎𝑛 (𝑈 )

route to the left partition, else route to the right. For query of a point 𝑞 , let 𝑙 = 0.5 − 𝛼 fractile point in 𝑈 , and 𝑟 = 0.5 + 𝛼 fractile point in 𝑈 . If 𝑞.ℎ < 𝑙 , route to the left, if 𝑞.ℎ > 𝑟 , route to the right, else route to both sides. . 

Definition 3.1. For query 𝑞 , data points 𝑥 1, . . . 𝑥 𝑛 , let 𝑥 (1) , . . . , 𝑥 (𝑛 )

denote the reordering of points by increasing distance from 𝑞 . Let us consider the potential function for the 𝑘 -NN. 

Φ𝑘,𝑚 (𝑞, 𝑥 1, . . . 𝑥 𝑛 ) = 1

𝑚 

> 𝑛

∑︁ 

> 𝑖 =𝑘 +1

Í𝑘 𝑗 =1 || 𝑞 − 𝑥 ( 𝑗 ) ||/ 𝑘 

|| 𝑞 − 𝑥 (𝑖 ) || (1) 

Theorem 3.2. From [ 9], Suppose we build a tree on data points 

𝑥 1, . . . 𝑥 𝑛 of depth L, with 𝛼 spill. If this tree is used to find the nearest neighbors of query 𝑞 , then the probability that it fails to return 𝑥 (1) , . . . , 𝑥 (𝑘 ) is 

𝑘 𝛼 

> L

∑︁ 

> 𝑖 =0

Φ(𝑘, (0.5+𝛼 )𝑖 𝑛 ) (𝑞, 𝑥 1, . . . , 𝑥 𝑛 ) (2) As we increase the depth of the tree, the number of hyperplanes used also increases. As more hyperplanes are used, there is a higher probability of two close points being separated by the segmentation algorithm. In Figure 2b, we approximate the probability that our segmentation algorithm fails to return 𝑥 ( 1).For the ease of demonstration, let 𝑛 = 10000 . As we use more levels, there is a higher probability of missing out on the exact nearest neighbor. Note that, in practice, we only a few levels of segmentation with about 1-8 segments per shard. Inside each of the leaves, we build an HNSW graph which is known to give high recall[4]. 

3.3.3 Approximate Principal Direction Hyperplane Segmenters(APD). 

Approximate Principal Hyperplane Segmenters, are motivated by Approximate Principal Directions[ 21 ] and Spectral Clustering[ 27 ]. Since we would like to minimize the number of queries being routed to multiple segments, we propose using a spectral clustering instead of random hyperplanes. To speed up the process, we also make use a core principle from APD Trees[ 21 ]– with a few steps of the power iteration, one can get reasonably close to the eigenvector. Let the dataset be denoted by D of dimensions 𝑛 × 𝑑 . Let 𝐴 𝑛 ×𝑛 

denote the adjacency matrix of a similarity graph, 𝐺 constructed on D. Let 𝐷 be the degree matrix of 𝐴 such that 𝐷 𝑖𝑖 = Í𝑗 𝐴 𝑖 𝑗 , and 

𝐶 = 𝐷 −1/2𝐴𝐷 −1/2. It is well-known that the largest eigenvalue of 

𝐶 is 1, and the second-largest eigenvalue and the corresponding eigenvector approximate the sparsest cut [ 27 ]. However, for large datasets, it is difficult to compute to the matrices 𝐴 and 𝐶 since they are of the order 𝑂 (𝑛 × 𝑛 ). Along with these restrictions, we also have the added requirement of having a “queryable“ hyperplane which not only partitions the data, but allows us to route a new point (query) to the right partition. To make this method work in practice, we assume 𝐴 = DD 𝑇 

and D is almost regular, which allows us to apply the Cheeger inequality described above. The second-largest eigenvector of 𝐴 

can be found using the second largest left singular vector of D.Since D = 𝑈 Σ𝑉 𝑇 where 𝑈 and 𝑉 are the left and right singular vectors, we approximate the right singular vectors, as 𝑈 = D.𝑉 .Thus, we use ℎ which is the second-largest right singular vectors of D, and let 𝑢 = D.ℎ .This method also has the drawback of near points being across the splitting hyperplane. Again, we employ methods of spill, in-sertion, and querying as described in Section 3.3.2. Note that the theoretical guarantees from Section 3.3.2 are also applicable to the APD Segmenters. This bound is loose since APD is a data-dependent partitioning technique which boosts the performance in practice. Consider a LANNS system which leverages these strategies, and Theorem 3.2, we can state the following. 

Corollary 3.3. Suppose we build a tree of depth L, with 𝛼 spill, and the leaves of this tree are segments of the LANNS index. Let method A be used to perform an ANN-search within each segment. If for a query 𝑞 , A fails to return 𝑥 (1) , . . . , 𝑥 (𝑘 ) with probability 𝑝 𝐴 ,then LANNS fails to return 𝑥 (1) , . . . , 𝑥 (𝑘 ) with probability 

𝑘𝑝 𝐴 

𝛼 

> L

∑︁ 

> 𝑖 =0

Φ(𝑘, (0.5+𝛼 )𝑖 𝑛 ) (𝑞, 𝑥 1, . . . , 𝑥 𝑛 ) (3) 

## 4 OFFLINE FRAMEWORK 

In this section, we describe the various components of LANNS. We propose pre-learning our learnable segmenters and feeding them as input to the indexing algorithm. The indexing algorithm stores the index on HDFS which can be fed into the querying algorithm, or can be exported to an online serving system (see Section 6). 

## 4.1 Learning a Segmenter 

Since the data distribution in our shards is uniform, we propose to pre-learn a segmenter and employ the same segmenter across all shards. This has a two-fold advantage– (i) avoiding unneces-sary computations to learn a segmenter for each shard on the fly; (ii) storing segmenters for each shard in the offline system. Since the segmenter is shared, only one copy is stored. Given the input dataset, we subsample the dataset uniformly at random. This sam-pled dataset, say, D, is fed to the segmenter learning algorithm, which is one of RH or APD. These techniques learn a tree of separat-ing hyperplanes. At each internal node of this tree, a hyperplane is generated using RH or APD, that is used to further split the dataset into two partitions. For the APD Segmenter, we use the Spark Ma-chine Learning library[ 23 ] implementation for distributed Singular Value Decomposition. Once this tree of hyperplanes is learnt, we 

853 store the tree consisting of the hyperplane, the split points, and the left and right boundaries for each of the internal nodes. This learnt segmenter is fed to the ingestion algorithm. 

## 4.2 Indexing 

In Figure 3a, we show the process of scaling indexing for web-scale datasets. Along with the input dataset, we optionally input a pre-learnt segmenter that is loaded within each Spark executor and is used to generate the two-level partitioning. This pre-learnt segmenter is shared across shards. Each document is tagged with a shardID and one or more segmentIDs. The partition tagged dataset is repartitioned based on segmentID and shardIDs. One particular (shard, segment) pair is loaded in an executor and the HNSW Index is built on this subset. The HNSW Index is built inside an executor and hence, all HNSW indexing can happen in parallel. The serialized index inside each executor is stored in the HDFS from the executor itself and the associated metadata and segmenter information is coupled with the index and written from the driver. 

## 4.3 Querying 

For our offline use cases, it is of utmost importance to scale not only to big datasets but also to big query sets. To scale our query process, we make use of partitioned query sets. We demonstrate our process of querying with our two-level partitioned index in Figure 3b. We take a large query set and partition them into smaller batches, which are written to the HDFS. We also read the metadata of the index and prepare a ‘ SearchExecutorContext ‘ which informs each executor of which segment of which shard, and which query partition to load within it. This SearchExecutorContext is sent to the executors, the respective HNSW Indices and query partitions are loaded inside the executor. Partial search occurs inside each of these executors. The partial results go through a two-level merging as follows– in the first level, partial results are returned to the driver along with the shard and segmentIDs they come from. These partial results are repartitioned on the basis of the queryID and the shardID to perform a segment level merging to obtain shard results. The shard results are repartitioned again based on the queryID for the final merge. This is analogous to how merging would occur in an online system, where segment results would first get merged within the server node containing the shard. These merged shard level responses are further merged within the searcher master/broker node. 

4.3.1 Preventing Time-Out Errors. Spark occasionally suffers from time-out errors which could prove to be catastrophic in some large-scale systems. Since a spark cluster is shared among many users and applications, there is heavy load in the cluster, and some nodes which are freed up while waiting for other tasks to finish. These get allocated to other applications, and “die“ Consider a scenario where you have 100 (query, shard, segment) -partitions, and only 8 execu-tors. After the partitioned search, before segment-level merging is triggered, some executors die and become unreachable. In these scenarios, the results become unavailable and search for those parti-tions is restarted. While waiting for these recomputed results, some other executors may die, and so on. This leads to cascading failures which may cause catastrophic damages for applications. This is what we refer to as “time-out“ errors. In order to prevent such scenarios from happening, we write partial results to a temporary path on the HDFS. After searching and the first phase of merging, the results are written to a temporary path on the HDFS and are loaded from the temporary path for further processing. As soon as our two-level merging finishes, this temporary directory is cleaned. This works well since Spark ensures that for write operations, as soon as an executor finishes processing its task, instead of waiting for other executors to finish execution, it can write to the HDFS. This is in contrast to the repartitioning where the executor keeps the results and waits for all tasks of the stage to finish executing. 

4.3.2 Per shard TopK. Some recommender systems require search-ing for a very large number of nearest neighbors, of the order of 1000s, with further post-processing to prune candidates. Sending the same "k" or "topK" to each shard can prove to be wasteful since each shard would then return topK responses. These topK responses would use up network I/O bandwidth and also increase the merge cost at the searcher or broker. In order to avoid such cases, we employ a "perShardTopK", which uses the Normal Approximation Interval[ 8] to reduce the number of nearest neighbors fetched from each randomly partitioned shard. Let 𝑆 be the number of shards, and 𝑝 be the confidence (or topK.confidence), and 𝑠 ′ = 1 

> 𝑆

, and 𝑐𝐼 =

𝑠 ′ + 𝑓 (𝑝 ) ∗ √︃ 𝑠 ′ (1−𝑠 ′) 

> 𝑡𝑜𝑝𝐾

then, 𝑝𝑒𝑟𝑆ℎ𝑎𝑟𝑑𝑇𝑜𝑝𝐾 = 𝑚𝑖𝑛 (𝑡𝑜𝑝𝐾, ⌈𝑐𝐼 ∗𝑡𝑜𝑝𝐾 ⌉) ,where 𝑓 (𝑝 ) is the (1 − 𝑝 /2) quantile of the standard normal distri-bution (the probit). Note that since hyperplane based segmenters may query only a few segments, it is undesirable to apply the concept of a "per segment topK". Employing a per segment topK could lead to fewer than topK results as the final output. Thus, we do not optimize the topK for segments, instead we propagate the shard level perShard-TopK to the associated segments. In the online system, querying using the perShardTopK at the segment level does not hamper the network I/O drastically. The merging occurs within a node and only a final perShardTopK are sent over the network. While c-ANNS[ 18 ]may also be applied to reduce the number of results, this may not be desirable in all use cases. Some applications may need to generate candidates when the query point is very far from all indexed data (i.e., recommendations for new or inactive users). 

## 5 EXPERIMENTS 5.1 Open Source Evaluation 

For our evaluations on open-source data, we use two datasets– (i) 

SIFT1M , the SIFT1M dataset with the indexing dataset of 1𝑀 records and a query set of 10 𝑘 records. Each of these has dimension, 𝑑 = 128 ,and (ii) GIST1M , the GIST1M dataset with the indexing dataset of 1𝑀 

records and query set of 1𝑘 records. Each of these have dimension, 

𝑑 = 960 . For both these datasets, we consider 𝑡𝑜𝑝𝐾 = 100 near-est neighbors with the distance function to be Euclidean Distance. For both, SIFT1M and GIST1M , we compare our performance with the HNSW algorithm. We build (𝑛, 𝑚 )-partitioned indices, where 𝑛 

is the number of shards and 𝑚 is the number of segments, using Random Segmenters (RS), Random Hyperplane Segmenters (RH), and APD Segmenters (APD). For the SIFT1M dataset, we experi-ment with (1, 8)-partitioned and (2, 4)-partitioned indices. For the 

GIST1M dataset, we limit ourselves to (1, 8)-partitioned indices. For all experiments, 𝛼 = 0.15 , i.e., we route about 30% queries to both partitions at any level. We set the 𝑡𝑜𝑝𝐾 .𝑐𝑜𝑛𝑓 𝑖𝑑𝑒𝑛𝑐𝑒 = 0.95 to limit 

854 (a) Indexing multi-million datasets (b) Querying with large query sets on multi-million datasets 

Figure 3: Indexing and Querying within LANNS 

the number of results obtained from each shard. For all experiments, the building times, query times, and recall are averaged over 5 runs. 

5.1.1 Results. In Tables 1,2 and 3, we present the Recall, Build Times and Query Times comparisons with the HNSW algorithm for 

SIFT1M and GIST1M datasets. For Build and Query Times, we vary the number of executors for our LANNS indices. For both datasets, we observe a ∼ 4.5 × − 5× speed-up in build time using 2 executors, and a ∼ 10 × − 11 × speed-up in build time using 8 executors. For the RS segmenter, we see comparable query times with respect to HNSW and 2 executors. However, we see a speedup of 2 × − 2.5×

when we increase the number of executors to 8. This comes with comparable recall. With RH segmenter for both datasets, we see a significant drop of about ∼ 15% in recall for (1, 8)-partitioning, and this comes with a speed up of ∼ 2 × − 2.5× on the query time using 2 executors, and ∼ 3 × − 4× using 8 executors. For the APD segmenter, for SIFT1M , we observe a loss of 2% in recall with a 

(1, 8)-partitioning and a 1% drop (2, 4)-partitioning. For GIST1M ,we observe 7% loss in recall with the (1, 8)-partitioning. However, for both datasets, the (1, 8)-partitioning this comes with a ∼ 2×− 3×

speedup in query time with 2 executors and ∼ 5× speedup in query time with 8 executors.It is worthwhile to note that while both datasets contain 1M points, GIST1M has a lower recall with APD. This can be attributed to the difference in dimensionality, SIFT1M is in 128 dimensions while GIST1M is in 960 dimensions. Theorem 3.2 and Theorem 3.3 also indicates that higher dimensionality and a deeper segmentation tree leads to a higher loss in recall. Build times do not change across (1, 8)-partitioning and the 

(2, 4)-partitioning and across segmenters. This is because we pre-learn the segmenters and feed them to the ingestion setup. While RS doesn’t require any pre-learning, for the SIFT1M dataset, RH segmenter takes 2.1 minutes and 1.8 minutes for (1, 8)-partitioning and (2, 4)-partitioning respectively on a subsample of 250k data points, and APD segmenter takes 3 minutes and 2.6 minutes for 

(1, 8)-partitioning and (2, 4)-partitioning respectively on a subsam-ple of 250k data points. For the GIST1M dataset, RH segmenter takes 6.3 minutes on a subsample of 250k data points, and APD segmenter takes 18 minutes on a subsample of 250k data points. For all segmenter learning on GIST1M , we use 30 executors. 

## 5.2 Real-World Datasets 

We use four large-scale datasets for real-world use cases: (1) Groups Search: Groups is a dataset of ∼ 2.7M groups on LinkedIn. Each group is embedded in a 256-dimensional space. We evaluate the offline performance on 10k queries. (2) People You May Know: ( PYMK ) is a database of 100M users of the platform. Each record is an embedding in 50 dimensions. We evaluate the offline recall performance on a subset of 1M queries, and offline query latency on 372M queries. (3) People Search: ( People ) is a database of 180M users of the LinkedIn platform, represented as an embedding in 50 dimensions. This use case leverages LANNS for people search. We evaluate the offline performance on 20k queries. (4) Near-Duplicates: ( NearDupe ) consists of embeddings of im-ages posted on the LinkedIn feed. The training set has 148k records in 2048 dimensions with a query set of 500k records. 

Groups , People and NearDupe use-cases were first tested using our offline platform and then onboarded to the online platform (See Section 6). PYMK use case, one of our biggest use-cases employs our offline platform for an in-production system. We first provide benchmarking results on the Groups dataset. We evaluate the following alternatives– (i) Physical Spill: A data point close to the splitting plane is routed to both children or segments, (ii) Virtual Spill: A query close to the splitting plane is routed to both children or segments. The physical spill uses data side duplication and uses a higher memory footprint as compared to the virtual spill. However, the Queries per Second (QPS) in case of a physical spill is slightly higher than the virtual spill since the query is routed to only one segment in case of a physical spill. The results with both types of spill are presented in Table 4. For both of these, we see that the recall values are comparable with only a slight difference in the QPS values. For virtual spills, since queries are being routed to multiple segments, the number of unique queries that can be 

855 Table 1: Recall for SIFT1M and GIST1M datasets. R@k refers to Recall at topK = k. Method suffix (𝑛, 𝑚 ) refers to (𝑛, 𝑚 )-partitioning. 

SIFT1M GIST1M 

Method R@1 R@5 R@10 R@15 R@50 R@100 R@1 R@5 R@10 R@15 R@50 R@100 HNSW 0.991 0.996 0.997 0.998 0.998 0.998 0.994 0.995 0.995 0.995 0.993 0.989 

RS(1,8) 0.979 0.986 0.986 0.986 0.98 0.98 0.995 0.998 0.999 0.999 0.999 0.999 RH(1,8) 0.841 0.818 0.804 0.798 0.776 0.762 0.872 0.858 0.851 0.843 0.827 0.812 

APD(1,8) 0.977 0.977 0.975 0.973 0.966 0.961 0.931 0.919 0.912 0.91 0.908 0.905 

RS(2,4) 0.989 0.994 0.995 0.995 0.996 0.996 - - - - - -

RH(2,4) 0.916 0.913 0.906 0.903 0.892 0.885 - - - - - -

APD(2,4) 0.989 0.995 0.994 0.994 0.992 0.991 - - - - - -

Table 2: Build times for SIFT1M and GIST1M datasets with vary-ing number of executors ( E). Time is in minutes for total 1𝑀 

data points. 

SIFT1M GIST1M 

E HNSW RS RH APD HNSW RS RH APD 2 40 8.2 8.1 8.4 577 132 128 140 

4 - 6.6 6.8 6.3 - 96 108 106 

8 - 4.3 4.4 4.1 - 48 54 52 Table 3: Query times for SIFT1M and GIST1M dataset with vary-ing number of executors ( E). Time is in milliseconds per query for total 10 𝑘 query points for SIFT1M and 1𝑘 query points for GIST1M .

SIFT1M GIST1M 

(1,8)- (2,4)- (1,8)-HN partitioning partitioning HN partitioning 

E SW RS RH APD RS RH APD SW RS RH APD 2 50 58 21 16 49 46 44 336 330 156 144 

4 - 46 16 12 38 25 25 - 222 132 108 

8 - 25 13 10 33 17 17 - 132 96 66 

served is lower, leading to slight degradation in the QPS. Since LANNS indices are used in production systems, it is undesirable to have a high memory footprint. Employing physical spills for large datasets such as PYMK would increase the memory footprint by 30% ( 30M records), which increases the number of server nodes required. Thus, we use virtual spill with 𝛼 = 0.15 .In Table 5, we present our building and querying times 34 for our real-world datasets. We include the improvements in the build time for the dataset mentioned in the Introduction. For the Groups 

dataset, a (2,2)-partitioned index reduces build time to 38 minutes. For People and the PYMK use cases, owing to the large size of the data, it is infeasible to compare with HNSW. For the NearDupe use cases, we essentially use the HNSW index with distributed querying. We present results on real datasets with the parameters reflecting the optimal trade-off for our in-production services. We also present our recall evaluations in Table 6. For each dataset, we obtain a high recall of over 95% , evaluated on query sets of 

> 3Note that these times are inclusive of the times required for requesting a cluster and assigning executors.
> 4The building and querying time presented here are averaged over 5 runs.

Table 4: Recall on Groups dataset with (1,m)-partitioning using APD Segmentation. R@k refers to the recall for k-nearest neighbors, m refers to the number of segments Physical Spill Virtual Spill 

m Spill R@15 QPS R@15 QPS 1 0% 0.9458 863.29 0.9458 863.29 

4 10% 0.8400 2619.02 0.8526 2186.93 4 20% 0.8861 2432.23 0.8853 2010.44 

4 30% 0.9268 2392.42 0.9272 1984.21 8 30% 0.9105 2710.24 0.9112 2573 16 30% 0.8836 2797.42 0.892 2985.34 Table 5: Build and Query Times for Real-World datsets. dim refers to dimensions, 𝑛 to number of Shards, and 𝑚 to number of Segments. Indexing Querying Dataset n m dim Size Time Size Time 

PYMK 20 1 50 100M 480m 370M 10h People 32 1 50 180M 520m 20k 10m NearDupe 1 1 2048 148k 80m 500k 5m Groups 1 1 256 2.7M 133m 20k 7m Groups 2 2 256 2.7M 38m 20k 3m 

Table 6: Recall for Real-World datasets. dim refers to dimen-sions, and R@K refers to the Recall at topK = K. Dataset n dim Index Size Query Size K R@K 

People 32 50 180M 20k 50 97% 

PYMK 20 50 100M 1M 100 95% 

NearDupe 1 2048 148k 0.5M 100 97% 

Groups 1 256 2.7M 20k 100 96.9% reasonable sizes. For large datasets, we employ an in-house Spark implementation of distributed brute-force search. 

## 5.3 Choice of Parameters 

As demonstrated in Table 1, for both open source datasets, we observe that the RH segmenter has a significant loss in the recall as compared to the APD segmenter, with comparable query time. This comes with a trade-off on the time to learn a segmenter. RH might be a good fit for certain time sensitive applications with highly dynamic datasets where a trade-off between indexing time 

856 and recall is acceptable. For use cases where the dataset is not very dynamic, APD allows a better trade-off with respect to indexing time and recall. Other factors to consider in these scenarios is the 

(𝑛, 𝑚 ) configuration. While the spark indexing time is the same for 

(1, 8) and (2, 4), the choice can depend on a large number of factors. The 𝑛 = 1 case requires only one node in the online setup, whereas, the 𝑛 = 2 case would require two nodes and a broker node to merge the results. The query times for both cases would vary as well. For the 𝑛 = 2 case, each query would perform ANN on two shards, and for 𝑛 = 1, it would be on one shard, and recall loss for 𝑚 = 4 v/s 

𝑚 = 8 varies with the dimensionality. Another interesting trade-off could be the physical v/s virtual spill. For cases where there are enough resources to allow for a physical spill, but the application is highly time sensitive and requires high parallelization of the queries, one may decide to use physical spill described in [ 9 ], and in Table 4. In this case, each query would be routed to only one segment, and queries which are routed to different segments can be served in parallel. In cases where data duplication across segments is not tolerable, virtual spill gives similar results with a small drop in QPS. For any use case, the choice would be dependent not only on the nature of the use case, the indexing time, query time, and recall quality but also on the dimensionality, the cost budget and available resources. 

## 6 ONLINE SERVING 

Figure 4: Online Service Architecture 

Throughout the paper, we discuss the offline implementations evaluations of our proposed method for scaling HNSW builds. In this section, we will discuss our online service architecture, as shown in Figure 4. To enable nearest neighbor search capability in an online environment, we build the index offline on our Spark cluster and ship the serialized HNSW index (as Avro datasets) to online searcher nodes. The serialized index consists of the graph index, the embeddings (vectors) and additional metadata (like the segmenter, distance function used during index build, etc). The searcher nodes, when starting up, deserialize the index to native Java data-structures optimized for online serving using persisted metadata with minimal additional configuration. This ensures that the platform doesn’t allow accidental differences in algorithm con-figuration between offline build and online serving. The majority of storage needed in the online node comes from the vector represen-tations of entities in the index, the index itself is quite small. Fast lookup access to the embeddings for a document is critical for low latency online serving as most of the search time is spent on doing <query, document> distance comparisons. The difference in the online architecture is that each shard is hosted on a different node. The first stage of the two-step merging, i.e., the shard level merging, happens on the node where the shard is hosted (called a "searcher"), and the final merge happens at the broker or client. The broker is also responsible for calculating and passing the 𝑝𝑒𝑟𝑆ℎ𝑎𝑟𝑑𝑇𝑜𝑝𝐾 to each shard. We also built additional constructs to support use cases hosting different indices in the same searcher for online A/B tests between different embedding representations of the documents. For one of our large use cases with 180M documents and embeddings of dimension 128 , we benchmarked the online searcher to achieve a 2.5K QPS at a p99 latency of 20ms .Our production systems make use of both, online and offline approaches. Some use cases perform nearest neighbor search of-fline, using Spark, at a fixed cadence and send the results to online services for further processing. Three in-production use cases are hosted online with each shard hosted on a separate searcher node. 

Offline v/s Online Serving – For applications with very large datasets and fixed query sets (for example, connections of members of a social network), we suggest offline search and sending results to online services. For very large datasets, the number of shards could be high and require several dedicated host machines, whereas, in offline mode, the processing is done once and a cluster could be shared with various applications. Thus, if the use case is not latency sensitive, or if precomputation of nearest neighbors or recommedations is feasible, it is preferred to use the offline service. Much of the cost of offline processing can be delegated to the offline grid infrastructure. However, this cannot be done for applications where the query set is dynamic and the results are required instantly. For cases such as a search application or nearline spam detection, the offline service would have delays and an unacceptable latency and the online service is the only option. 

## 7 CONCLUSION 

In this work, we propose LANNS, an end-to-end platform for Ap-proximate Nearest Neighbor Search. We enable scaling HNSW to web-scale datasets through a two-level partitioning scheme us-ing the Spark framework. We demonstrate the excellent empirical performance on LinkedIn’s production use-cases, and through ex-tensive offline evaluations on various datasets. We demonstrate our scalable and highly competitive performance. We also briefly dis-cuss the design choices and the trade-off between using an offline pipeline or an online, deployable service. As future work, our approach of using segments can be explored for other purposes as well. For example, for context-based searches, we can build a segment per context and perform search in one or a few segments based on the contexts selected at query time.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="similarity-search-part-4-hierarchical-navigable-small-world-.md">
<details>
<summary>Similarity Search, Part 4: Hierarchical Navigable Small World (HNSW)</summary>

Phase: [EXPLORATION]

**Source URL:** <https://towardsdatascience.com/similarity-search-part-4-hierarchical-navigable-small-world-hnsw-2aad4fe87d37>

# Similarity Search, Part 4: Hierarchical Navigable Small World (HNSW)

Hierarchical Navigable Small World (HNSW) is a state-of-the-art algorithm used for an approximate search of nearest neighbours. Under the…

### Discover how to construct efficient multi-layered graphs to boost search speed in massive volumes of data

https://towardsdatascience.com/wp-content/uploads/2023/06/1Qz7AjCqkO7SYm5XHhn3uzw.png

**Similarity search** is a problem where given a query the goal is to find the most similar documents to it among all the database documents.

## Introduction

In data science, similarity search often appears in the NLP domain, search engines or recommender systems where the most relevant documents or items need to be retrieved for a query. There exists a large variety of different ways to improve search performance in massive volumes of data.

**[Hierarchical Navigable Small World](https://arxiv.org/pdf/1603.09320.pdf)** (HNSW) is a state-of-the-art algorithm used for an approximate search of nearest neighbours. Under the hood, HNSW constructs optimized graph structures making it very different from other approaches that were discussed in previous parts of this article series.

> The main idea of HNSW is to construct such a graph where a path between any pair of vertices could be traversed in a small number of steps.

A well-known analogy on the famous [six handshakes rule](https://en.wikipedia.org/wiki/Six_degrees_of_separation) is related to this method:

> All people are six or fewer social connections away from each other.

Before proceeding to inner workings of HNSW let us first discuss skip lists and navigable small words – crucial data structures used inside the HNSW implementation.

## Skip lists

[Skip list](https://en.wikipedia.org/wiki/Skip_list) is a probabilistic data structure that allows inserting and searching elements within a sorted list for _O(logn)_ on average. A skip list is constructed by several layers of linked lists. The lowest layer has the original linked list with all the elements in it. When moving to higher levels, the number of skipped elements increases, thus decreasing the number of connections.

https://towardsdatascience.com/wp-content/uploads/2023/06/1-8oKDoFp-jiYOF4-z3EdCw.pngFinding element 20 in skip list

The search procedure for a certain value starts from the highest level and compares its next element with the value. If the value is less or equal to the element, then the algorithm proceeds to its next element. Otherwise, the search procedure descends to the lower layer with more connections and repeats the same process. At the end, the algorithm descends to the lowest layer and finds the desired node.

Based on the information from [Wikipedia](https://en.wikipedia.org/wiki/Skip_list), a skip list has the main parameter _p_ which defines the probability of an element appearing in several lists. If an element appears in layer _i_, then the probability that it will appear in layer _i + 1_ is equal to _p (p_ is usually set to 0.5 or 0.25 _)_. On average, each element is presented in _1 / (1 – p)_ lists.

As we can see, this process is much faster than the normal linear search in the linked list. In fact, HNSW inherits the same idea but instead of linked lists, it uses graphs.

## Navigable Small World

**[Navigable small world](https://en.wikipedia.org/wiki/Small-world_network)** is a graph with polylogarithmic _T = O(logᵏn)_ search complexity which uses greedy routing. **Routing** refers to the process of starting the search process from low-degree vertices and ending with high-degree vertices. Since low-degree vertices have very few connections, the algorithm can rapidly move between them to efficiently navigate to the region where the nearest neighbour is likely to be located. Then the algorithm gradually zooms in and switches to high-degree vertices to find the nearest neighbour among the vertices in that region.

> Vertex is sometimes also referred to as a **node**.

### Search

In the first place, search is proceeded by choosing an entry point. To determine the next vertex (or vertices) to which the algorithm makes a move, it calculates the distances from the query vector to the current vertex’s neighbours and moves to the closest one. At some point, the algorithm terminates the search procedure when it cannot find a neighbour node that is closer to the query than the current node itself. This node is returned as the response to the query.

https://towardsdatascience.com/wp-content/uploads/2023/06/1FqFiylcO1IsqcqLcybOmpA.pngGreedy search process in a navigable small world. Node A is used as an entry point. It has two neighbours B and D. Node D is closer to the query than B. As a result, we move to D. Node D has three neighbours C, E and F. E is the closest neighbour to the query, so we move to E. Finally, the search process will lead to node L. Since all neighbours of L are located further from the query than L itself, we stop the algorithm and return L as the answer to the query.

This greedy strategy does not guarantee that it will find the exact nearest neighbour as the method uses only local information at the current step to take decisions. **Early stopping** is one of the problems of the algorithm. It occurs especially at the beginning of the search procedure when there are no better neighbour nodes than the current one. For the most part, this might happen when the starting region has too many low-degree vertices.

https://towardsdatascience.com/wp-content/uploads/2023/06/1JRJeFUA013z7tNNWEY83Ug.pngEarly stopping. Both neighbours of the current node are further away from the query. Thus, the algorithm returns the current node as the response, though there exist much closer nodes to the query.

The search accuracy can be improved by using several entry points.

### Construction

The NSW graph is built by shuffling dataset points and inserting them one by one in the current graph. When a new node is inserted, it is then linked by edges to the _M_ nearest vertices to it.

https://towardsdatascience.com/wp-content/uploads/2023/06/1vzPqZFdw3uxZMJJa1X7IqQ.pngSequential insertion of nodes (from left to right) with M = 2. At each iteration, a new vertex is added to the graph and linked to its M = 2 nearest neighbours. Blue lines represent the connected edges to a newly inserted node.

In most scenarios, long-range edges will likely be created at the beginning phase of the graph construction. They play an important role in graph navigation.

> Links to the closest neighbors of the elements inserted in the beginning of the construction later become bridges between the network hubs that keep the overall graph connectivity and allow the logarithmic scaling of the number of hops during greedy routing. – Yu. A. Malkov, D. A. Yashunin

From the example in the figure above, we can see the importance of the long-range edge _AB_ that was added in the beginning. Imagine a query requiring the traverse of a path from the relatively far-located nodes _A_ and I. Having the edge _AB_ allows doing it rapidly by directly navigating from one side of the graph to the opposite one.

As the number of vertices in the graph increases, it increases the probability that the lengths of newly connected edges to a new node will be smaller.

## HNSW

**[HNSW](https://arxiv.org/pdf/1603.09320.pdf)** is based on the same principles as skip list and navigable small world. Its structure represents a multi-layered graph with fewer connections on the top layers and more dense regions on the bottom layers.

## Search

The search starts from the highest layer and proceeds to one level below every time the local nearest neighbour is greedily found among the layer nodes. Ultimately, the found nearest neighbour on the lowest layer is the answer to the query.

https://towardsdatascience.com/wp-content/uploads/2023/06/1ziU6_KIDqfmaDXKA1cMa8w.pngSearch in HNSW

Similarly to NSW, the search quality of HNSW can be improved by using several entry points. Instead of finding only one nearest neighbour on each layer, the _efSearch_ (a hyperparameter) \_\_ closest nearest neighbours to the query vector are found and each of these neighbours is used as the entry point on the next layer.

### Complexity

The authors of the [original paper](https://arxiv.org/pdf/1603.09320.pdf) claim that the number of operations required to find the nearest neighbour on any layer is bounded by a constant. Taking into consideration that the number of all layers in a graph is logarithmic, we get the total search complexity which is _O(logn)_.

## Construction

### Choosing the maximum layer

Nodes in HNSW are inserted sequentially one by one. Every node is randomly assigned an integer _l_ indicating the maximum layer at which this node can present in the graph. For example, if _l = 1_, then the node can only be found on layers 0 and 1. The authors select _l_ randomly for each node with an _exponentially decaying probability distribution_ normalized by the non-zero multiplier _mL (mL = 0_ results in a single layer in HNSW and non-optimized search complexity _)_. Normally, the majority of _l_ values should be equal to 0, so most of the nodes are present only on the lowest level. The larger values of _mL_ increase the probability of a node appearing on higher layers.

https://towardsdatascience.com/wp-content/uploads/2023/06/1dlGxLpWZdNMcIiMrLymwQg.pngThe number of layers l for every node is chosen randomly with _exponentially decaying probability distribution._https://towardsdatascience.com/wp-content/uploads/2023/06/1Nl_BPedx-nIkBVMOuxqGPQ.pngDistribution of the number of layers based on normalization factor mL. The horizontal axis represents values of the uniform(0, 1) distribution.

> To achieve the optimum performance advantage of the controllable hierarchy, the overlap between neighbors on different layers (i.e. percent of element neighbors that are also belong to other layers) has to be small. – Yu. A. Malkov, D. A. Yashunin.

One of the ways to decrease the overlap is to decrease _mL_. But it is important to keep in mind that reducing _mL_ also leads on average to more traversals during a greedy search on each layer. That is why it is essential to choose such a value of _mL_ that will balance both the overlap and the number of traversals.

The authors of the paper propose choosing the optimal value of _mL_ which is equal to _1 / ln(M)_. This value corresponds to the parameter _p = 1 / M_ of the skip list being an average single element overlap between the layers.

### Insertion

After a node is assigned the value _l_, there are two phases of its insertion:

1. The algorithm starts from the upper layer and greedily finds the nearest node. The found node is then used as an entry point to the next layer and the search process continues. Once the layer _l_ is reached _,_ the insertion proceeds to the second step.
2. Starting from layer _l_ the algorithm inserts the new node at the current layer. Then it acts the same as before at step 1 but instead of finding only one nearest neighbour, it greedily searches for _efConstruction_ (hyperparameter) nearest neighbours. Then _M_ out of _efConstruction_ neighbours are chosen and edges from the inserted node to them are built. After that, the algorithm descends to the next layer and each of found _efConstruction_ nodes acts as an entry point. The algorithm terminates after the new node and its edges are inserted on the lowest layer 0.

https://towardsdatascience.com/wp-content/uploads/2023/06/1jEGA6ZXYR0qwgrtIEJ9vWg.pngInsertion of a node (in blue) in HNSW. The maximum layer for a new node was randomly chosen as l = 2. Therefore, the node will be inserted on layers 2, 1 and 0. On each of these layers, the node will be connected to its M = 2 nearest neighbours.

### Choosing values for construction parameters

The original paper provides several useful insights on how to choose hyperparameters:

- According to simulations, good values for _M_ lie between 5 and 48. Smaller values of _M_ tend to be better for lower recalls or low-dimensional data while higher values of M are suited better for high recalls or high-dimensional data.
- Higher values of _efConstruction_ imply a more profound search as more candidates are explored. However, it requires more computations. Authors recommend choosing such an _efConstruction_ value that results at recall being close to _0.95–1_ during training.
- Additionally, there is another important parameter _Mₘₐₓ_ – the maximum number of edges a vertex can have. Apart from it, there exists the same parameter _Mₘₐₓ₀_ but separately for the lowest layer. It is recommended to choose a value for _Mₘₐₓ_ close to _2 \* M_. Values greater than _2 \* M_ can lead to performance degradation and excessive memory usage. At the same time, _Mₘₐₓ = M_ results in poor performance at high recall.

### Candidate selection heuristic

It was noted above that during node insertion, _M_ out of _efConstruction_ candidates are chosen to build edges to them. Let us discuss possible ways of choosing these _M_ nodes.

The naïve approach takes _M_ closest candidates. Nevertheless, it is not always the optimal choice. Below is an example demonstrating it.

Imagine a graph with the structure in the figure below. As you can see, there are three regions with two of them not being connected to each other (on the left and on the top). As a result, getting, for example, from point _A_ to _B_ requires a long path through another region. It would be logical to somehow connect these two regions for better navigation.

https://towardsdatascience.com/wp-content/uploads/2023/06/1sRZY7WzZXjT7jhyPLmHOIQ.pngNode X is inserted into the graph. The objective is to optimally connect it to other M = 2 points.

Then a node _X_ is inserted into the graph and needs to be linked to _M_ _= 2_ other \_\_ vertices.

In this case, the naïve approach directly takes the _M = 2_ nearest neighbours ( _B_ and _C_) and connects _X_ to them. Though _X_ is connected to its real nearest neighbours, it does not solve the problem. Let us look at the heuristical approach invented by the authors.

> The heuristic considers not only the closest distances between nodes but also the connectivity of different regions on the graph.

The heuristic chooses the first nearest neighbour ( _B_ in our case) and connects the inserted node ( _X_) to it. Then the algorithm sequentially takes another most closest nearest neighbour in the sorted order ( _C_) and builds an edge to it only if the distance from this neighbour to the new node ( _X_) is smaller than any distance from this neighbour to all already connected vertices ( _B_) to the new node ( _X_). After that, the algorithm proceeds to the next closest neighbour until _M_ edges are built.

Getting back to the example, the heuristical procedure is illustrated in the figure below. The heuristic chooses _B_ as the closest nearest neighbour for X and builds the edge _BX_. Then the algorithm chooses _C_ as the next closest nearest neighbour. However, this time _BC < CX_. This indicates that adding the edge _CX_ to the graph is not optimal because there already exists the edge _BX_ and the nodes _B_ and _C_ are very close to each other. The same analogy proceeds with the nodes _D_ and _E_. After that, the algorithm examines the node _A_. This time, it satisfies the condition since _BA_ _\> AX_. As a result, the new edge _AX_ and both initial regions become connected to each other.

https://towardsdatascience.com/wp-content/uploads/2023/06/1_2N0HYxF27wMHGrdQRWqTQ.pngThe example on the left uses the naïve approach. The example on the right uses the selection heuristic which results in two initial disjoint regions being connected to each other.

### Complexity

The insertion process works very similarly, compared to the search procedure, without any significant differences which could require a non-constant number of operations. Thus, the insertion of a single vertex imposes _O(logn)_ of time. To estimate the total complexity, the number of all inserted nodes _n_ in a given dataset should be considered. Ultimately, HNSW construction requires _O(n \* logn)_ time.

## Combining HNSW with other methods

HNSW can be used together with other similarity search methods to provide better performance. One of the most popular ways to do it is to combine it with an inverted file index and product quantization ( _IndexIVFPQ_) which were described in other parts of this article series.

> [**Similarity Search, Part 3: Blending Inverted File Index and Product Quantization**](https://towardsdatascience.com/similarity-search-blending-inverted-file-index-and-product-quantization-a8e508c765fa)

Within this paradigm, HNSW plays the role of a **coarse quantizer** for _IndexIVFPQ_ meaning that it will be responsible for finding the nearest Voronoi partition, so the search scope can be reduced. To do it, an HNSW index has to be built on all Voronoi centroids. When given a query, HNSW is used to find the nearest Voronoi centroid (instead of brute-force search as it was previously by comparing distances to every centroid). After that, the query vector is quantized within a respective Voronoi partition and distances are calculated by using PQ codes.

https://towardsdatascience.com/wp-content/uploads/2023/06/13Mm9lL73jscwxvDNe8_WzA.pngChoosing the nearest Voronoi centroid by finding the nearest neighbour in HNSW built on top of Voronoi centroids.

When using only an inverted file index, it is better to set the number of Voronoi partitions not too large (256 or 1024, for instance) because brute-force search is performed to find the nearest centroids. By choosing a small number of Voronoi partitions, the number of candidates inside each partition becomes relatively large. Therefore, the algorithm rapidly identifies the nearest centroid for a query and most of its runtime is concentrated on finding the nearest neighbour inside a Voronoi partition.

However, introducing HNSW into the workflow requires an adjustment. Consider running HNSW only on a small number of centroids (256 or 1024): HNSW would not bring any significant benefits because, with a small number of vectors, HNSW performs relatively the same in terms of execution time as naïve brute-force search. Moreover, HNSW would require more memory to store the graph structure.

> That is why when merging HNSW and inverted file index, it is recommended to set the number of Voronoi centroids much bigger than usual. By doing so, the number of candidates inside each Voronoi partition becomes much smaller.

This shift in paradigm results in the following settings:

- HNSW rapidly identifies the nearest Voronoi centroids in logarithmic time.
- After that, an exhaustive search inside respective Voronoi partitions is performed. It should not be a trouble because the number of potential candidates is small.

## Faiss implementation

> **[Faiss](https://github.com/facebookresearch/faiss)** (Facebook AI Search Similarity) is a Python library written in C++ used for optimised similarity search. This library presents different types of indexes which are data structures used to efficiently store the data and perform queries.

Based on the information from the [Faiss documentation](https://faiss.ai/), we will see how HNSW can be utilized and merged together with inverted file index and product quantization.

### IndexHNSWFlat

FAISS has a class _IndexHNSWFlat_ implementing the HNSW structure. As usual, the suffix " _Flat_" indicates that dataset vectors are fully stored in index. The constructor accepts 2 parameters:

- **d**: data dimensionality.
- **M**: the number of edges that need to be added to every new node during insertion.

Additionally, via thr **hnsw** field, _IndexHNSWFlat_ provides several useful attributes (which can be modified) and methods:

- **hnsw.efConstruction**: number of nearest neighbours to explore during construction.
- **hnsw.efSearch**: number of nearest neighbours to explore during search.
- **hnsw.max\_level**: returns the maximum layer.
- **hnsw.entry\_point**: returns the entry point.
- **faiss.vector\_to\_array(index.hnsw.levels)**: returns a list of maximum layers for each vector
- **hnsw.set\_default\_probas(M: int, level\_mult: float)**: allows setting _M_ and _mL_ values respectively. By default, \_level _mult_ is set to _1 / ln(M)_.

https://towardsdatascience.com/wp-content/uploads/2023/06/1g7ca4NhG0CZBuQCWEOCB2g.pngFaiss implementation of IndexHNSWFlat

_IndexHNSWFlat_ sets values for _Mₘₐₓ = M_ and _Mₘₐₓ₀ = 2 \* M._

### IndexHNSWFlat + IndexIVFPQ

_IndexHNSWFlat_ can be combined with other indexes as well. One of the examples is _IndexIVFPQ_ described in the previous part. Creation of this composite index proceeds in two steps:

1. _IndexHNSWFlat_ is initialized as a coarse quantizer.
2. The quantizer is passed as a parameter to the constructor of _IndexIVFPQ_.

Training and adding can be done by using different or the same data.

https://towardsdatascience.com/wp-content/uploads/2023/06/1HWCUhn8z8ub7tOja1Rgxsw.pngFAISS implementation of IndexHNSWFlat + IndexIVFPQ

## Conclusion

In this article, we have studied a robust algorithm which works especially well for large dataset vectors. By using multi-layer graph representations and the candidate selection heuristic its search speed scales efficiently while maintaining a decent prediction accuracy. It is also worth noting that HNSW can be used in combination with other similarity search algorithms making it very flexible.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="skip-list-wikipedia.md">
<details>
<summary>Skip list - Wikipedia</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://en.wikipedia.org/wiki/Skip_list>

# Skip list - Wikipedia

Probabilistic data structure

| Skip list |
| --- |
| [Type](https://en.wikipedia.org/wiki/List_of_data_structures "List of data structures") | List |
| Invented | 1989 |
| Invented by | [W. Pugh](https://en.wikipedia.org/wiki/William_Pugh_(computer_scientist) "William Pugh (computer scientist)") |
| | [Time complexity](https://en.wikipedia.org/wiki/Time_complexity "Time complexity") in [big O notation](https://en.wikipedia.org/wiki/Big_O_notation "Big O notation") |
| --- |
| Operation | **Average** | **Worst case** |
| Search | O(log⁡n){\\displaystyle {\\mathcal {O}}(\\log n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/74a9dfea91c47d1c6563e89bbcd891771b91acfa | O(n){\\displaystyle {\\mathcal {O}}(n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/3c7bbe0124ae81792773344bc8709fc2f9c9910d[\[1\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-cs.uwaterloo-1) |
| Insert | O(log⁡n){\\displaystyle {\\mathcal {O}}(\\log n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/74a9dfea91c47d1c6563e89bbcd891771b91acfa | O(n){\\displaystyle {\\mathcal {O}}(n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/3c7bbe0124ae81792773344bc8709fc2f9c9910d |
| Delete | O(log⁡n){\\displaystyle {\\mathcal {O}}(\\log n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/74a9dfea91c47d1c6563e89bbcd891771b91acfa | O(n){\\displaystyle {\\mathcal {O}}(n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/3c7bbe0124ae81792773344bc8709fc2f9c9910d |
| [Space complexity](https://en.wikipedia.org/wiki/Space_complexity "Space complexity") |
| Space | O(n){\\displaystyle {\\mathcal {O}}(n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/3c7bbe0124ae81792773344bc8709fc2f9c9910d | O(nlog⁡n){\\displaystyle {\\mathcal {O}}(n\\log n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/9981ede263cbf28215d3a70bf30f55db41a6e692[\[1\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-cs.uwaterloo-1) | |

In [computer science](https://en.wikipedia.org/wiki/Computer_science "Computer science"), a **skip list** (or **skiplist**) is a [probabilistic](https://en.wikipedia.org/wiki/Randomized_algorithm "Randomized algorithm") [data structure](https://en.wikipedia.org/wiki/Data_structure "Data structure") that allows O(log⁡n){\\displaystyle {\\mathcal {O}}(\\log n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/74a9dfea91c47d1c6563e89bbcd891771b91acfa[average complexity](https://en.wikipedia.org/wiki/Average-case_complexity "Average-case complexity") for search as well as O(log⁡n){\\displaystyle {\\mathcal {O}}(\\log n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/74a9dfea91c47d1c6563e89bbcd891771b91acfa average complexity for insertion within an [ordered sequence](https://en.wikipedia.org/wiki/Ordered_sequence "Ordered sequence") of n{\\displaystyle n}https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b elements. Thus it can get the best features of a sorted [array](https://en.wikipedia.org/wiki/Array_data_structure "Array data structure") (for searching) while maintaining a [linked list](https://en.wikipedia.org/wiki/Linked_list "Linked list")-like structure that allows insertion, which is not possible with a static array. Fast search is made possible by maintaining a linked hierarchy of subsequences, with each successive subsequence skipping over fewer elements than the previous one _(see the picture below)_. Searching starts in the sparsest subsequence until two consecutive elements have been found, one smaller and one larger than or equal to the element searched for. Via the linked hierarchy, these two elements link to elements of the next sparsest subsequence, where searching is continued until finally searching in the full sequence. The elements that are skipped over may be chosen probabilistically[\[2\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-pugh-2) or deterministically,[\[3\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-3) with the former being more common.

## Description

https://en.wikipedia.org/wiki/File:Skip_list.svg A schematic picture of the skip list data structure. Each box with an arrow represents a pointer and a row is a [linked list](https://en.wikipedia.org/wiki/Linked_list "Linked list") giving a sparse subsequence; the numbered boxes (in yellow) at the bottom represent the ordered data sequence. Searching proceeds downwards from the sparsest subsequence at the top until consecutive elements bracketing the search element are found.

A skip list is built in layers. The bottom layer 1{\\displaystyle 1}https://wikimedia.org/api/rest_v1/media/math/render/svg/92d98b82a3778f043108d4e20960a9193df57cbf is an ordinary ordered [linked list](https://en.wikipedia.org/wiki/Linked_list "Linked list"). Each higher layer acts as an "express lane" for the lists below, where an element in layer i{\\displaystyle i}https://wikimedia.org/api/rest_v1/media/math/render/svg/add78d8608ad86e54951b8c8bd6c8d8416533d20 appears in layer i+1{\\displaystyle i+1}https://wikimedia.org/api/rest_v1/media/math/render/svg/2fe1bfc8314922e4c3fdb4e8eceb20a00b4f011d with some fixed probability p{\\displaystyle p}https://wikimedia.org/api/rest_v1/media/math/render/svg/81eac1e205430d1f40810df36a0edffdc367af36 (two commonly used values for p{\\displaystyle p}https://wikimedia.org/api/rest_v1/media/math/render/svg/81eac1e205430d1f40810df36a0edffdc367af36 are 1/2{\\displaystyle 1/2}https://wikimedia.org/api/rest_v1/media/math/render/svg/e308a3a46b7fdce07cc09dcab9e8d8f73e37d935 or 1/4{\\displaystyle 1/4}https://wikimedia.org/api/rest_v1/media/math/render/svg/4d3cf1ef33695c3d98cb09f01e5700f927ce928c). On average, each element appears in 1/(1−p){\\displaystyle 1/(1-p)}https://wikimedia.org/api/rest_v1/media/math/render/svg/212e9859c8d055e32c9a1b32fd6d3490a4bb84db lists, and the tallest element (usually a special head element at the front of the skip list) appears in all the lists. The skip list contains log1/p⁡n{\\displaystyle \\log \_{1/p}n\\,}https://wikimedia.org/api/rest_v1/media/math/render/svg/909fb0d0b25ebd96ecfab41e93ce5ee2c1e2df79 (i.e. logarithm base 1/p{\\displaystyle 1/p}https://wikimedia.org/api/rest_v1/media/math/render/svg/2cdfd6eb8d2c6f424b698d06aa99d31895c47e91 of n{\\displaystyle n}https://wikimedia.org/api/rest_v1/media/math/render/svg/a601995d55609f2d9f5e233e36fbe9ea26011b3b) lists.

A search for a target element begins at the head element in the top list, and proceeds horizontally until the current element is greater than or equal to the target. If the current element is equal to the target, it has been found. If the current element is greater than the target, or the search reaches the end of the linked list, the procedure is repeated after returning to the previous element and dropping down vertically to the next lower list. The expected number of steps in each linked list is at most 1/p{\\displaystyle 1/p}https://wikimedia.org/api/rest_v1/media/math/render/svg/2cdfd6eb8d2c6f424b698d06aa99d31895c47e91, which can be seen by tracing the search path backwards from the target until reaching an element that appears in the next higher list or reaching the beginning of the current list. Therefore, the total _expected_ cost of a search is 1plog1/p⁡n{\\displaystyle {\\tfrac {1}{p}}\\log \_{1/p}n}https://wikimedia.org/api/rest_v1/media/math/render/svg/c963a559c75713f6b587853c9f6bce09683debc2 which is O(log⁡n){\\displaystyle {\\mathcal {O}}(\\log n)\\,}https://wikimedia.org/api/rest_v1/media/math/render/svg/0d4564f8652da4d6bc379228c67a2e1f86214ae8, when p{\\displaystyle p}https://wikimedia.org/api/rest_v1/media/math/render/svg/81eac1e205430d1f40810df36a0edffdc367af36 is a constant. By choosing different values of p{\\displaystyle p}https://wikimedia.org/api/rest_v1/media/math/render/svg/81eac1e205430d1f40810df36a0edffdc367af36, it is possible to trade search costs against storage costs. For example, the value p=1/e{\\displaystyle p=1/e}https://wikimedia.org/api/rest_v1/media/math/render/svg/383f81e1ab5142d1678b7198b15a658bad6d2de2 minimizes the average search time of skip lists, whereas the value p=1/2{\\displaystyle p=1/2}https://wikimedia.org/api/rest_v1/media/math/render/svg/c4a77b7a2e96414f0214f2d6ee49e462ccf33af0 simplifies their implementation.

### Implementation details

https://en.wikipedia.org/wiki/File:Skip_list_add_element-en.gif Inserting elements into a skip list

The elements used for a skip list can contain more than one pointer since they can participate in more than one list.

Insertions and deletions are implemented much like the corresponding linked-list operations, except that "tall" elements must be inserted into or deleted from more than one linked list.

O(n){\\displaystyle {\\mathcal {O}}(n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/3c7bbe0124ae81792773344bc8709fc2f9c9910d operations, which force us to visit every node in ascending order (such as printing the entire list), provide the opportunity to perform a behind-the-scenes derandomization of the level structure of the skip-list in an optimal way, bringing the skip list to O(log⁡n){\\displaystyle {\\mathcal {O}}(\\log n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/74a9dfea91c47d1c6563e89bbcd891771b91acfa search time. (Choose the level of the i'th finite node to be 1 plus the number of times it is possible to repeatedly divide i by 2 before it becomes odd. Also, i=0 for the negative infinity header as there is the usual special case of choosing the highest possible level for negative and/or positive infinite nodes.) However this also allows someone to know where all of the higher-than-level 1 nodes are and delete them.

Alternatively, the level structure could be made quasi-random in the following way:

```
make all nodes level 1
j ← 1
while the number of nodes at level j > 1 do
    for each i'th node at level j do
        if i is odd and i is not the last node at level j
            randomly choose whether to promote it to level j+1
        else if i is even and node i-1 was not promoted
            promote it to level j+1
        end if
    repeat
    j ← j + 1
repeat
```

Like the derandomized version, quasi-randomization is only done when there is some other reason to be running an O(n){\\displaystyle {\\mathcal {O}}(n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/3c7bbe0124ae81792773344bc8709fc2f9c9910d operation (which visits every node).

The advantage of this quasi-randomness is that it doesn't give away nearly as much level-structure related information to an [adversarial user](https://en.wikipedia.org/wiki/Adversary_(online_algorithm) "Adversary (online algorithm)") as the de-randomized one. This is desirable because an adversarial user who is able to tell which nodes are not at the lowest level can pessimize performance by simply deleting higher-level nodes. (Bethea and Reiter however argue that nonetheless an adversary can use probabilistic and timing methods to force performance degradation.[\[4\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-4)) The search performance is still guaranteed to be logarithmic.

It would be tempting to make the following "optimization": In the part which says "Next, for each _i_ th...", forget about doing a coin-flip for each even-odd pair. Just flip a coin once to decide whether to promote only the even ones or only the odd ones. Instead of O(nlog⁡n){\\displaystyle {\\mathcal {O}}(n\\log n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/9981ede263cbf28215d3a70bf30f55db41a6e692 coin flips, there would only be O(log⁡n){\\displaystyle {\\mathcal {O}}(\\log n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/74a9dfea91c47d1c6563e89bbcd891771b91acfa of them. Unfortunately, this gives the adversarial user a 50/50 chance of being correct upon guessing that all of the even numbered nodes (among the ones at level 1 or higher) are higher than level one. This is despite the property that there is a very low probability of guessing that a particular node is at level _N_ for some integer _N_.

A skip list does not provide the same absolute worst-case performance guarantees as more traditional [balanced tree](https://en.wikipedia.org/wiki/Balanced_tree "Balanced tree") data structures, because it is always possible (though with very low probability[\[5\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-5)) that the coin-flips used to build the skip list will produce a badly balanced structure. However, they work well in practice, and the randomized balancing scheme has been argued to be easier to implement than the deterministic balancing schemes used in balanced binary search trees. Skip lists are also useful in [parallel computing](https://en.wikipedia.org/wiki/Parallel_computing "Parallel computing"), where insertions can be done in different parts of the skip list in parallel without any global rebalancing of the data structure. Such parallelism can be especially advantageous for resource discovery in an ad-hoc [wireless network](https://en.wikipedia.org/wiki/Wireless_network "Wireless network") because a randomized skip list can be made robust to the loss of any single node.[\[6\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-6)

### Indexable skiplist

As described above, a skip list is capable of fast O(log⁡n){\\displaystyle {\\mathcal {O}}(\\log n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/74a9dfea91c47d1c6563e89bbcd891771b91acfa insertion and removal of values from a sorted sequence, but it has only slow O(n){\\displaystyle {\\mathcal {O}}(n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/3c7bbe0124ae81792773344bc8709fc2f9c9910d lookups of values at a given position in the sequence (i.e. return the 500th value); however, with a minor modification the speed of [random access](https://en.wikipedia.org/wiki/Random_access "Random access") indexed lookups can be improved to O(log⁡n){\\displaystyle {\\mathcal {O}}(\\log n)}https://wikimedia.org/api/rest_v1/media/math/render/svg/74a9dfea91c47d1c6563e89bbcd891771b91acfa.

For every link, also store the width of the link. The width is defined as the number of bottom layer links being traversed by each of the higher layer "express lane" links.

For example, here are the widths of the links in the example at the top of the page:

```
   1                               10
 o---> o---------------------------------------------------------> o    Top level
   1           3              2                    5
 o---> o---------------> o---------> o---------------------------> o    Level 3
   1        2        1        2              3              2
 o---> o---------> o---> o---------> o---------------> o---------> o    Level 2
   1     1     1     1     1     1     1     1     1     1     1
 o---> o---> o---> o---> o---> o---> o---> o---> o---> o---> o---> o    Bottom level
Head  1st   2nd   3rd   4th   5th   6th   7th   8th   9th   10th  NIL
      Node  Node  Node  Node  Node  Node  Node  Node  Node  Node
```

Notice that the width of a higher level link is the sum of the component links below it (i.e. the width 10 link spans the links of widths 3, 2 and 5 immediately below it). Consequently, the sum of all widths is the same on every level (10 + 1 = 1 + 3 + 2 + 5 = 1 + 2 + 1 + 2 + 3 + 2).

To index the skip list and find the i'th value, traverse the skip list while counting down the widths of each traversed link. Descend a level whenever the upcoming width would be too large.

For example, to find the node in the fifth position (Node 5), traverse a link of width 1 at the top level. Now four more steps are needed but the next width on this level is ten which is too large, so drop one level. Traverse one link of width 3. Since another step of width 2 would be too far, drop down to the bottom level. Now traverse the final link of width 1 to reach the target running total of 5 (1+3+1).

```
function lookupByPositionIndex(i)
    node ← head
    i ← i + 1                           # don't count the head as a step
    for level from top to bottom do
        while i ≥ node.width[level] do # if next step is not too far
            i ← i - node.width[level]  # subtract the current width
            node ← node.next[level]    # traverse forward at the current level
        repeat
    repeat
    return node.value
end function
```

This method of implementing indexing is detailed in _"A skip list cookbook"_ by William Pugh[\[7\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-7)

## History

Skip lists were first described in 1989 by [William Pugh](https://en.wikipedia.org/wiki/William_Pugh_(computer_scientist) "William Pugh (computer scientist)").[\[8\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-8)

To quote the author:

> _Skip lists are a probabilistic data structure that seem likely to supplant balanced trees as the implementation method of choice for many applications. Skip list algorithms have the same asymptotic expected time bounds as balanced trees and are simpler, faster and use less space._

—William Pugh, _Concurrent Maintenance of Skip Lists_ (1989)

## Usages

List of applications and frameworks that use skip lists:

- [Apache Portable Runtime](https://en.wikipedia.org/wiki/Apache_Portable_Runtime "Apache Portable Runtime") implements skip lists.[\[9\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-9)
- [MemSQL](https://en.wikipedia.org/wiki/MemSQL "MemSQL") uses lock-free skip lists as its prime indexing structure for its database technology.
- [MuQSS](https://en.wikipedia.org/wiki/MuQSS "MuQSS"), for the [Linux kernel](https://en.wikipedia.org/wiki/Linux_kernel "Linux kernel"), is a [CPU scheduler](https://en.wikipedia.org/wiki/Scheduling_(computing)#SHORT-TERM "Scheduling (computing)") built on skip lists.[\[10\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-10)[\[11\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-11)
- [Cyrus IMAP server](https://en.wikipedia.org/wiki/Cyrus_IMAP_server "Cyrus IMAP server") offers a "skiplist" backend DB implementation[\[12\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-12)
- IBM [DOORS](https://en.wikipedia.org/wiki/DOORS "DOORS") offers skip lists as a data type in its DOORS/DXL (DOORS eXtension Language) scripting language
- [Lucene](https://en.wikipedia.org/wiki/Lucene "Lucene") uses skip lists to search delta-encoded posting lists in logarithmic time.\[ _[citation needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")_\]
- The "QMap" key/value dictionary (up to Qt 4) template class of [Qt](https://en.wikipedia.org/wiki/Qt_(framework) "Qt (framework)") is implemented with skip lists.[\[13\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-13)
- [Redis](https://en.wikipedia.org/wiki/Redis "Redis"), an ANSI-C open-source persistent key/value store for Posix systems, uses skip lists in its implementation of ordered sets.[\[14\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-14)
- [Discord](https://en.wikipedia.org/wiki/Discord "Discord") uses skip lists to handle storing and updating the list of members in a [server](https://en.wikipedia.org/wiki/Discord#Servers "Discord").[\[15\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-15)
- [RocksDB](https://en.wikipedia.org/wiki/RocksDB "RocksDB") uses skip lists for its default Memtable implementation.[\[16\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-16)
- [Java](https://en.wikipedia.org/wiki/Java_(programming_language) "Java (programming language)") uses skip lists for its [ConcurrentSkipListSet](https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/concurrent/ConcurrentSkipListSet.html) and [ConcurrentSkipListMap](https://docs.oracle.com/en/java/javase/24/docs/api/java.base/java/util/concurrent/ConcurrentSkipListMap.html).

Skip lists are also used in distributed applications (where the nodes represent physical computers, and pointers represent network connections) and for implementing highly scalable concurrent [priority queues](https://en.wikipedia.org/wiki/Priority_queue "Priority queue") with less lock contention,[\[17\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-17) or even [without locking](https://en.wikipedia.org/wiki/Non-blocking_algorithm "Non-blocking algorithm"),[\[18\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-18)[\[19\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-19)[\[20\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-20) as well as [lock-free](https://en.wikipedia.org/wiki/Lock-free "Lock-free") concurrent dictionaries.[\[21\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-21) There are also several US patents for using skip lists to implement (lockless) priority queues and concurrent dictionaries.[\[22\]](https://en.wikipedia.org/wiki/Skip_list#cite_note-22)

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="what-are-the-key-configuration-parameters-for-an-hnsw-index-.md">
<details>
<summary>What are the key configuration parameters for an HNSW index (such as M and efConstruction/efSearch), and how does each influence the trade-off between index size, build time, query speed, and recall?</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://milvus.io/ai-quick-reference/what-are-the-key-configuration-parameters-for-an-hnsw-index-such-as-m-and-efconstructionefsearch-and-how-does-each-influence-the-tradeoff-between-index-size-build-time-query-speed-and-recall>

# What are the key configuration parameters for an HNSW index (such as M and efConstruction/efSearch), and how does each influence the trade-off between index size, build time, query speed, and recall?

The key configuration parameters for an HNSW (Hierarchical Navigable Small World) index are **M**, **efConstruction**, and **efSearch**. These parameters directly influence the balance between index size, build time, query speed, and recall. Here’s how each works and their trade-offs:

**M (Maximum Connections per Node):**
M determines the number of bidirectional links each node maintains in the graph layers of HNSW. A higher M (e.g., 24 vs. 12) increases the graph’s connectivity, improving recall by reducing the chance of search getting trapped in local minima. However, more connections also expand the index size (memory usage) and slow down build time, as each insertion requires more comparisons to establish links. For example, doubling M from 12 to 24 might quadruple build time in some cases. During queries, a higher M can speed up search by enabling faster traversal through the graph’s “shortcuts,” but this depends on how well the graph is structured during construction. Developers often tune M based on dataset size and memory constraints—larger datasets may require higher M for acceptable recall but will incur higher memory costs.

**efConstruction (Construction-Time Search Depth):**
efConstruction controls the number of candidate neighbors explored when inserting a node into the graph. A higher efConstruction (e.g., 400 vs. 200) allows the algorithm to find more optimal connections during index creation, leading to a higher-quality graph and better recall. However, this significantly increases build time, as each insertion requires more distance computations. For instance, setting efConstruction=400 might double build time compared to efConstruction=200. The parameter does not affect index size, as it only influences how links are selected. Developers often prioritize higher efConstruction for critical applications like recommendation systems where recall is paramount, even if it means waiting longer for the index to build.

**efSearch (Query-Time Search Depth):**
efSearch determines the size of the dynamic candidate list during querying. A higher efSearch (e.g., 500 vs. 100) increases recall by exploring more neighbors, but it slows down queries due to additional distance calculations. For example, in a 10-million-vector dataset, efSearch=500 might achieve 98% recall but take 5ms per query, while efSearch=100 might drop to 85% recall with 1ms latency. This parameter is often adjusted dynamically: a large efSearch is used for accuracy-critical tasks (e.g., medical image retrieval), while smaller values suit real-time applications (e.g., autocomplete suggestions). Importantly, efSearch must be set ≥ the desired number of nearest neighbors (k) to return meaningful results.

**Practical Trade-offs and Use Cases:**
Tuning these parameters requires balancing priorities. For example, a high-recall setup (M=24, efConstruction=400, efSearch=500) suits offline batch processing but demands significant memory and build time. In contrast, a real-time system might use M=12, efConstruction=200, and efSearch=100 to prioritize speed and resource efficiency. Experimentation is key: start with default values (e.g., M=16, efConstruction=200) and adjust incrementally while monitoring recall, latency, and resource usage. Tools like ANN benchmarks can help quantify trade-offs for specific datasets and hardware.

</details>

</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

<details>
<summary>Faiss HNSW Implementation</summary>

# Faiss HNSW Implementation

## Summary
Repository: facebookresearch/faiss
Commit: 42dc2862c293b7c7f788be686cf6c9ac93abf6cf
Subpath: /faiss/impl
Files analyzed: 160

Estimated tokens: 412.9k

## File tree
```Directory structure:
└── impl/
    ├── AdditiveQuantizer.cpp
    ├── AdditiveQuantizer.h
    ├── AdSampling.cpp
    ├── AdSampling.h
    ├── AuxIndexStructures.cpp
    ├── AuxIndexStructures.h
    ├── ClusteringHelpers.cpp
    ├── ClusteringHelpers.h
    ├── ClusteringInitialization.cpp
    ├── ClusteringInitialization.h
    ├── CodePacker.cpp
    ├── CodePacker.h
    ├── CodePackerRaBitQ.cpp
    ├── CodePackerRaBitQ.h
    ├── DistanceComputer.h
    ├── expanded_scanners.h
    ├── FaissAssert.h
    ├── FaissException.cpp
    ├── FaissException.h
    ├── HNSW.cpp
    ├── HNSW.h
    ├── IDSelector.cpp
    ├── IDSelector.h
    ├── index_read.cpp
    ├── index_read_utils.h
    ├── index_write.cpp
    ├── InvertedListScannerStats.h
    ├── io.cpp
    ├── io.h
    ├── io_macros.h
    ├── kmeans1d.cpp
    ├── kmeans1d.h
    ├── lattice_Zn.cpp
    ├── lattice_Zn.h
    ├── LocalSearchQuantizer.cpp
    ├── LocalSearchQuantizer.h
    ├── mapped_io.cpp
    ├── mapped_io.h
    ├── maybe_owned_vector.h
    ├── NNDescent.cpp
    ├── NNDescent.h
    ├── NSG.cpp
    ├── NSG.h
    ├── Panorama.cpp
    ├── Panorama.h
    ├── PanoramaStats.cpp
    ├── PanoramaStats.h
    ├── PdxLayout.cpp
    ├── PdxLayout.h
    ├── platform_macros.h
    ├── PolysemousTraining.cpp
    ├── PolysemousTraining.h
    ├── ProductAdditiveQuantizer.cpp
    ├── ProductAdditiveQuantizer.h
    ├── ProductQuantizer-inl.h
    ├── ProductQuantizer.cpp
    ├── ProductQuantizer.h
    ├── Quantizer.h
    ├── RaBitQuantizer.cpp
    ├── RaBitQuantizer.h
    ├── RaBitQuantizerMultiBit.cpp
    ├── RaBitQuantizerMultiBit.h
    ├── RaBitQUtils.cpp
    ├── RaBitQUtils.h
    ├── residual_quantizer_encode_steps.cpp
    ├── residual_quantizer_encode_steps.h
    ├── ResidualQuantizer.cpp
    ├── ResidualQuantizer.h
    ├── ResultHandler.h
    ├── ScalarQuantizer.cpp
    ├── ScalarQuantizer.h
    ├── simd_dispatch.h
    ├── svs_io.cpp
    ├── svs_io.h
    ├── ThreadedIndex-inl.h
    ├── ThreadedIndex.h
    ├── VisitedTable.cpp
    ├── VisitedTable.h
    ├── zerocopy_io.cpp
    ├── zerocopy_io.h
    ├── approx_topk/
    │   ├── approx_topk.h
    │   ├── avx2.cpp
    │   ├── generic.h
    │   ├── neon.cpp
    │   ├── rq_beam_search_tab-inl.h
    │   ├── rq_beam_search_tab.h
    │   └── simdlib256-inl.h
    ├── binary_hamming/
    │   ├── avx2.cpp
    │   ├── avx512.cpp
    │   ├── dispatch.h
    │   ├── IndexBinaryHash_impl.h
    │   ├── IndexBinaryHNSW_impl.h
    │   ├── IndexBinaryIVF_impl.h
    │   ├── IndexIVFSpectralHash_impl.h
    │   ├── IndexPQ_impl.h
    │   ├── neon.cpp
    │   └── rvv.cpp
    ├── fast_scan/
    │   ├── accumulate_loops.h
    │   ├── accumulate_loops_512.h
    │   ├── decompose_qbs.h
    │   ├── dispatching.h
    │   ├── fast_scan.cpp
    │   ├── fast_scan.h
    │   ├── FastScanDistancePostProcessing.h
    │   ├── impl-avx2.cpp
    │   ├── impl-avx512.cpp
    │   ├── impl-neon.cpp
    │   ├── impl-riscv.cpp
    │   ├── kernels_simd256.h
    │   ├── kernels_simd512.h
    │   ├── LookupTableScaler.h
    │   ├── rabitq_dispatching.h
    │   ├── rabitq_result_handler.h
    │   └── simd_result_handlers.h
    ├── hnsw/
    │   ├── avx2.cpp
    │   ├── avx512.cpp
    │   ├── LockVector.cpp
    │   ├── LockVector.h
    │   ├── MinimaxHeap.cpp
    │   ├── MinimaxHeap.h
    │   └── .nobuck
    ├── pq_code_distance/
    │   ├── avx2.cpp
    │   ├── avx512.cpp
    │   ├── IVFPQ_QueryTables.cpp
    │   ├── IVFPQ_QueryTables.h
    │   ├── IVFPQScanner_impl.h
    │   ├── neon.cpp
    │   ├── pq_code_distance-avx2.h
    │   ├── pq_code_distance-avx512.h
    │   ├── pq_code_distance-generic.cpp
    │   ├── pq_code_distance-generic.h
    │   ├── pq_code_distance-inl.h
    │   ├── pq_code_distance-sve.cpp
    │   ├── pq_scan_impl.h
    │   ├── PQDistanceComputer_impl.h
    │   └── rvv.cpp
    ├── result_handler/
    │   ├── avx2.cpp
    │   ├── avx512.cpp
    │   └── ResultHandler.cpp
    ├── scalar_quantizer/
    │   ├── codecs.h
    │   ├── distance_computers.h
    │   ├── quantizers.h
    │   ├── scanners.h
    │   ├── similarities.h
    │   ├── sq-avx2.cpp
    │   ├── sq-avx512-impl.h
    │   ├── sq-avx512-spr.cpp
    │   ├── sq-avx512.cpp
    │   ├── sq-dispatch.h
    │   ├── sq-neon.cpp
    │   ├── sq-rvv.cpp
    │   ├── training.cpp
    │   └── training.h
    └── simdlib/
        ├── simdlib.h
        ├── simdlib_avx2.h
        ├── simdlib_avx512.h
        ├── simdlib_dispatch.h
        ├── simdlib_emulated.h
        ├── simdlib_neon.h
        └── simdlib_ppc64.h

```

## Extracted content
================================================
FILE: faiss/impl/AdditiveQuantizer.cpp
================================================
/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// -*- c++ -*-

#include <faiss/impl/AdditiveQuantizer.h>

#include <cstddef>
#include <cstdio>
#include <cstring>
#include <memory>
#include <random>

#include <algorithm>

#include <faiss/Clustering.h>
#include <faiss/impl/FaissAssert.h>
#include <faiss/impl/LocalSearchQuantizer.h>
#include <faiss/impl/ResidualQuantizer.h>
#include <faiss/impl/simd_dispatch.h>
#include <faiss/utils/Heap.h>
#include <faiss/utils/distances.h>
#include <faiss/utils/hamming.h>

extern "C" {

// general matrix multiplication
int sgemm_(
        const char* transa,
        const char* transb,
        FINTEGER* m,
        FINTEGER* n,
        FINTEGER* k,
        const float* alpha,
        const float* a,
        FINTEGER* lda,
        const float* b,
        FINTEGER* ldb,
        float* beta,
        float* c,
        FINTEGER* ldc);
}

namespace faiss {

AdditiveQuantizer::AdditiveQuantizer(
        size_t d_in,
        const std::vector<size_t>& nbits_in,
        Search_type_t search_type_in)
        : Quantizer(d_in),
          M(nbits_in.size()),
          nbits(nbits_in),
          search_type(search_type_in) {
    set_derived_values();
}

AdditiveQuantizer::AdditiveQuantizer()
        : AdditiveQuantizer(0, std::vector<size_t>()) {}

void AdditiveQuantizer::set_derived_values() {
    tot_bits = 0;
    only_8bit = true;
    codebook_offsets.resize(M + 1, 0);
    for (size_t i = 0; i < M; i++) {
        int nbit = nbits[i];
        FAISS_CHECK_RANGE(nbit, 0, 31);
        size_t k = (size_t)1 << nbit;
        codebook_offsets[i + 1] =
                add_no_overflow(codebook_offsets[i], k, "codebook_offsets");
        tot_bits += nbit;
        if (nbit != 0) {
            only_8bit = false;
        }
    }
    total_codebook_size = codebook_offsets[M];
    switch (search_type) {
        case ST_norm_float:
            norm_bits = 32;
            break;
        case ST_norm_qint8:
        case ST_norm_cqint8:
        case ST_norm_lsq2x4:
        case ST_norm_rq2x4:
            norm_bits = 8;
            break;
        case ST_norm_qint4:
        case ST_norm_cqint4:
            norm_bits = 4;
            break;
        case ST_decompress:
        case ST_LUT_nonorm:
        case ST_norm_from_LUT:
        default:
            norm_bits = 0;
            break;
    }
    tot_bits += norm_bits;

    // convert bits to bytes
    code_size = (tot_bits + 7) / 8;
}

void AdditiveQuantizer::train_norm(size_t n, const float* norms) {
    norm_min = HUGE_VALF;
    norm_max = -HUGE_VALF;
    for (size_t i = 0; i < n; i++) {
        if (norms[i] < norm_min) {
            norm_min = norms[i];
        }
        if (norms[i] > norm_max) {
            norm_max = norms[i];
        }
    }

    if (search_type == ST_norm_cqint8 || search_type == ST_norm_cqint4) {
        size_t k = (1 << 8);
        if (search_type == ST_norm_cqint4) {
            k = (1 << 4);
        }
        Clustering1D clus(k);
        clus.train_exact(n, norms);
        qnorm.add(clus.k, clus.centroids.data());
    } else if (search_type == ST_norm_lsq2x4 || search_type == ST_norm_rq2x4) {
        std::unique_ptr<AdditiveQuantizer> aq;
        if (search_type == ST_norm_lsq2x4) {
            aq.reset(new LocalSearchQuantizer(1, 2, 4));
        } else {
            aq.reset(new ResidualQuantizer(1, 2, 4));
        }

        aq->train(n, norms);
        // flatten aq codebooks
        std::vector<float> flat_codebooks(1 << 8);
        FAISS_THROW_IF_NOT(aq->codebooks.size() == 32);

        // save norm tables for 4-bit fastscan search
        norm_tabs = aq->codebooks;

        // assume big endian
        const float* c = norm_tabs.data();
        for (size_t i = 0; i < 16; i++) {
            for (size_t j = 0; j < 16; j++) {
                flat_codebooks[i * 16 + j] = c[j] + c[16 + i];
            }
        }

        qnorm.reset();
        qnorm.add(1 << 8, flat_codebooks.data());
        FAISS_THROW_IF_NOT(qnorm.ntotal == (1 << 8));
    }
}

void AdditiveQuantizer::compute_codebook_tables() {
    centroid_norms.resize(total_codebook_size);
    FAISS_THROW_IF_NOT_FMT(
            codebooks.size() >=
                    mul_no_overflow(
                            total_codebook_size, d, "codebooks validation"),
            "codebooks size %zd too small for total_codebook_size=%zd * d=%zd",
            codebooks.size(),
            total_codebook_size,
            d);
    fvec_norms_L2sqr(
            centroid_norms.data(), codebooks.data(), d, total_codebook_size);
    size_t cross_table_size = 0;
    for (size_t m = 0; m < M; m++) {
        FAISS_CHECK_RANGE(nbits[m], 0, 31);
        size_t K = (size_t)1 << nbits[m];
        size_t product =
                mul_no_overflow(K, codebook_offsets[m], "cross_table_size");
        cross_table_size = add_no_overflow(
                cross_table_size, product, "cross_table_size accumulation");
    }
    codebook_cross_products.resize(cross_table_size);
    size_t ofs = 0;
    for (size_t m = 1; m < M; m++) {
        FINTEGER ki = (size_t)1 << nbits[m];
        FINTEGER kk = codebook_offsets[m];
        FINTEGER di = d;
        float zero = 0, one = 1;
        size_t step_size = (size_t)ki * (size_t)kk;
        FAISS_THROW_IF_NOT_FMT(
                add_no_overflow(ofs, step_size, "cross product table offset") <=
                        cross_table_size,
                "cross product table overflow at step %zd: "
                "%zd + %zd > %zd",
                m,
                ofs,
                step_size,
                cross_table_size);
        sgemm_("Transposed",
               "Not transposed",
               &ki,
               &kk,
               &di,
               &one,
               codebooks.data() + d * kk,
               &di,
               codebooks.data(),
               &di,
               &zero,
               codebook_cross_products.data() + ofs,
               &ki);
        ofs += step_size;
    }
}

namespace {

// TODO
// https://stackoverflow.com/questions/31631224/hacks-for-clamping-integer-to-0-255-and-doubles-to-0-0-1-0

uint8_t encode_qint8(float x, float amin, float amax) {
    float x1 = (x - amin) / (amax - amin) * 256;
    int32_t xi = int32_t(floor(x1));

    return xi < 0 ? 0 : xi > 255 ? 255 : xi;
}

uint8_t encode_qint4(float x, float amin, float amax) {
    float x1 = (x - amin) / (amax - amin) * 16;
    int32_t xi = int32_t(floor(x1));

    return xi < 0 ? 0 : xi > 15 ? 15 : xi;
}

float decode_qint8(uint8_t i, float amin, float amax) {
    return (i + 0.5) / 256 * (amax - amin) + amin;
}

float decode_qint4(uint8_t i, float amin, float amax) {
    return (i + 0.5) / 16 * (amax - amin) + amin;
}

} // anonymous namespace

uint32_t AdditiveQuantizer::encode_qcint(float x) const {
    idx_t id;
    qnorm.assign(1, &x, &id, 1);
    return uint32_t(id);
}

float AdditiveQuantizer::decode_qcint(uint32_t c) const {
    return qnorm.get_xb()[c];
}

uint64_t AdditiveQuantizer::encode_norm(float norm) const {
    switch (search_type) {
        case ST_norm_float:
            uint32_t inorm;
            memcpy(&inorm, &norm, 4);
            return inorm;
        case ST_norm_qint8:
            return encode_qint8(norm, norm_min, norm_max);
        case ST_norm_qint4:
            return encode_qint4(norm, norm_min, norm_max);
        case ST_norm_lsq2x4:
        case ST_norm_rq2x4:
        case ST_norm_cqint8:
            return encode_qcint(norm);
        case ST_norm_cqint4:
            return encode_qcint(norm);
        case ST_decompress:
        case ST_LUT_nonorm:
        case ST_norm_from_LUT:
        default:
            return 0;
    }
}

void AdditiveQuantizer::pack_codes(
        size_t n,
        const int32_t* codes,
        uint8_t* packed_codes,
        int64_t ld_codes,
        const float* norms,
        const float* centroids) const {
    if (ld_codes == -1) {
        ld_codes = M;
    }
    std::vector<float> norm_buf;
    if (search_type == ST_norm_float || search_type == ST_norm_qint4 ||
        search_type == ST_norm_qint8 || search_type == ST_norm_cqint8 ||
        search_type == ST_norm_cqint4 || search_type == ST_norm_lsq2x4 ||
        search_type == ST_norm_rq2x4) {
        if (centroids != nullptr || !norms) {
            norm_buf.resize(n);
            std::vector<float> x_recons(n * d);
            decode_unpacked(codes, x_recons.data(), n, ld_codes);

            if (centroids != nullptr) {
                // x = x + c
                fvec_add(n * d, x_recons.data(), centroids, x_recons.data());
            }
            fvec_norms_L2sqr(norm_buf.data(), x_recons.data(), d, n);
            norms = norm_buf.data();
        }
    }
    int64_t n_signed = n;
#pragma omp parallel for if (n > 1000)
    for (int64_t i = 0; i < n_signed; i++) {
        const int32_t* codes1 = codes + i * ld_codes;
        BitstringWriter bsw(packed_codes + i * code_size, code_size);
        for (size_t m = 0; m < M; m++) {
            bsw.write(codes1[m], nbits[m]);
        }
        if (norm_bits != 0) {
            bsw.write(encode_norm(norms[i]), norm_bits);
        }
    }
}

void AdditiveQuantizer::decode(const uint8_t* code, float* x, size_t n) const {
    FAISS_THROW_IF_NOT_MSG(
            is_trained, "The additive quantizer is not trained yet.");

    int64_t n_signed = n;
    // standard additive quantizer decoding
#pragma omp parallel for if (n > 100)
    for (int64_t i = 0; i < n_signed; i++) {
        BitstringReader bsr(code + i * code_size, code_size);
        float* xi = x + i * d;
        for (size_t m = 0; m < M; m++) {
            int idx = bsr.read(nbits[m]);
            const float* c = codebooks.data() + d * (codebook_offsets[m] + idx);
            if (m == 0) {
                memcpy(xi, c, sizeof(*x) * d);
            } else {
                fvec_add(d, xi, c, xi);
            }
        }
    }
}

void AdditiveQuantizer::decode_unpacked(
        const int32_t* code,
        float* x,
        size_t n,
        int64_t ld_codes) const {
    FAISS_THROW_IF_NOT_MSG(
            is_trained, "The additive quantizer is not trained yet.");

    if (ld_codes == -1) {
        ld_codes = M;
    }

    int64_t n_signed = n;
    // standard additive quantizer decoding
#pragma omp parallel for if (n > 1000)
    for (int64_t i = 0; i < n_signed; i++) {
        const int32_t* codesi = code + i * ld_codes;
        float* xi = x + i * d;
        for (size_t m = 0; m < M; m++) {
            int idx = codesi[m];
            const float* c = codebooks.data() + d * (codebook_offsets[m] + idx);
            if (m == 0) {
                memcpy(xi, c, sizeof(*x) * d);
            } else {
                fvec_add(d, xi, c, xi);
            }
        }
    }
}

AdditiveQuantizer::~AdditiveQuantizer() {}

/****************************************************************************
 * Support for fast distance computations in centroids
 ****************************************************************************/

void AdditiveQuantizer::compute_centroid_norms(float* norms) const {
    size_t ntotal = (size_t)1 << tot_bits;
    int64_t ntotal_signed = ntotal;
    // TODO: make tree of partial sums
    with_simd_level([&]<SIMDLevel SL>() {
#pragma omp parallel
        {
            std::vector<float> tmp(d);
#pragma omp for
            for (int64_t i = 0; i < ntotal_signed; i++) {
                decode_64bit(i, tmp.data());
                norms[i] = fvec_norm_L2sqr<SL>(tmp.data(), d);
            }
        }
    });
}

void AdditiveQuantizer::decode_64bit(idx_t bits, float* xi) const {
    for (size_t m = 0; m < M; m++) {
        idx_t idx = bits & (((size_t)1 << nbits[m]) - 1);
        bits >>= nbits[m];
        const float* c = codebooks.data() + d * (codebook_offsets[m] + idx);
        if (m == 0) {
            memcpy(xi, c, sizeof(*xi) * d);
        } else {
            fvec_add(d, xi, c, xi);
        }
    }
}

void AdditiveQuantizer::compute_LUT(
        size_t n,
        const float* xq,
        float* LUT,
        float alpha,
        long ld_lut) const {
    // in all cases, it is large matrix multiplication

    FINTEGER ncenti = total_codebook_size;
    FINTEGER di = d;
    FINTEGER nqi = n;
    FINTEGER ldc = ld_lut > 0 ? ld_lut : ncenti;
    float zero = 0;

    sgemm_("Transposed",
           "Not transposed",
           &ncenti,
           &nqi,
           &di,
           &alpha,
           codebooks.data(),
           &di,
           xq,
           &di,
           &zero,
           LUT,
           &ldc);
}

namespace {

/* compute inner products of one query with all centroids, given a look-up
 * table of all inner products with codebook entries */
void compute_inner_prod_with_LUT(
        const AdditiveQuantizer& aq,
        const float* LUT,
        float* ips) {
    size_t prev_size = 1;
    for (size_t m = 0; m < aq.M; m++) {
        const float* LUTm = LUT + aq.codebook_offsets[m];
        int nb = aq.nbits[m];
        size_t nc = (size_t)1 << nb;

        if (m == 0) {
            memcpy(ips, LUT, sizeof(*ips) * nc);
        } else {
            for (int64_t i = nc - 1; i >= 0; i--) {
                float v = LUTm[i];
                fvec_add(prev_size, ips, v, ips + i * prev_size);
            }
        }
        prev_size *= nc;
    }
}

} // anonymous namespace

void AdditiveQuantizer::knn_centroids_inner_product(
        idx_t n,
        const float* xq,
        idx_t k,
        float* distances,
        idx_t* labels) const {
    std::unique_ptr<float[]> LUT(new float[n * total_codebook_size]);
    compute_LUT(n, xq, LUT.get());
    size_t ntotal = (size_t)1 << tot_bits;

#pragma omp parallel if (n > 100)
    {
        std::vector<float> dis(ntotal);
#pragma omp for
        for (idx_t i = 0; i < n; i++) {
            const float* LUTi = LUT.get() + i * total_codebook_size;
            compute_inner_prod_with_LUT(*this, LUTi, dis.data());
            float* distances_i = distances + i * k;
            idx_t* labels_i = labels + i * k;
            minheap_heapify(k, distances_i, labels_i);
            minheap_addn(k, distances_i, labels_i, dis.data(), nullptr, ntotal);
            minheap_reorder(k, distances_i, labels_i);
        }
    }
}

void AdditiveQuantizer::knn_centroids_L2(
        idx_t n,
        const float* xq,
        idx_t k,
        float* distances,
        idx_t* labels,
        const float* norms) const {
    std::unique_ptr<float[]> LUT(new float[n * total_codebook_size]);
    compute_LUT(n, xq, LUT.get());
    std::unique_ptr<float[]> q_norms(new float[n]);
    fvec_norms_L2sqr(q_norms.get(), xq, d, n);
    size_t ntotal = (size_t)1 << tot_bits;

#pragma omp parallel if (n > 100)
    {
        std::vector<float> dis(ntotal);
#pragma omp for
        for (idx_t i = 0; i < n; i++) {
            const float* LUTi = LUT.get() + i * total_codebook_size;
            float* distances_i = distances + i * k;
            idx_t* labels_i = labels + i * k;

            compute_inner_prod_with_LUT(*this, LUTi, dis.data());

            // update distances using
            // ||x - y||^2 = ||x||^2 + ||y||^2 - 2 * <x,y>

            maxheap_heapify(k, distances_i, labels_i);
            for (size_t j = 0; j < ntotal; j++) {
                float disj = q_norms[i] + norms[j] - 2 * dis[j];
                if (disj < distances_i[0]) {
                    heap_replace_top<CMax<float, int64_t>>(
                            k, distances_i, labels_i, disj, j);
                }
            }
            maxheap_reorder(k, distances_i, labels_i);
        }
    }
}

/****************************************************************************
 * Support for fast distance computations in codes
 ****************************************************************************/

namespace {

float accumulate_IPs(
        const AdditiveQuantizer& aq,
        BitstringReader& bs,
        const float* LUT) {
    float accu = 0;
    for (size_t m = 0; m < aq.M; m++) {
        size_t nbit = aq.nbits[m];
        int idx = bs.read(nbit);
        accu += LUT[idx];
        LUT += (uint64_t)1 << nbit;
    }
    return accu;
}

float compute_norm_from_LUT(const AdditiveQuantizer& aq, BitstringReader& bs) {
    float accu = 0;
    std::vector<int> idx(aq.M);
    const float* c = aq.codebook_cross_products.data();
    for (size_t m = 0; m < aq.M; m++) {
        size_t nbit = aq.nbits[m];
        int i = bs.read(nbit);
        size_t K = 1 << nbit;
        idx[m] = i;

        accu += aq.centroid_norms[aq.codebook_offsets[m] + i];

        for (size_t l = 0; l < m; l++) {
            int j = idx[l];
            accu += 2 * c[j * K + i];
            c += (1 << aq.nbits[l]) * K;
        }
    }
    // FAISS_THROW_IF_NOT(c == aq.codebook_cross_products.data() +
    // aq.codebook_cross_products.size());
    return accu;
}

} // anonymous namespace

template <>
float AdditiveQuantizer::
        compute_1_distance_LUT<true, AdditiveQuantizer::ST_LUT_nonorm>(
                const uint8_t* codes,
                const float* LUT) const {
    BitstringReader bs(codes, code_size);
    return accumulate_IPs(*this, bs, LUT);
}

template <>
float AdditiveQuantizer::
        compute_1_distance_LUT<false, AdditiveQuantizer::ST_LUT_nonorm>(
                const uint8_t* codes,
                const float* LUT) const {
    BitstringReader bs(codes, code_size);
    return -accumulate_IPs(*this, bs, LUT);
}

template <>
float AdditiveQuantizer::
        compute_1_distance_LUT<false, AdditiveQuantizer::ST_norm_float>(
                const uint8_t* codes,
                const float* LUT) const {
    BitstringReader bs(codes, code_size);
    float accu = accumulate_IPs(*this, bs, LUT);
    uint32_t norm_i = bs.read(32);
    float norm2;
    memcpy(&norm2, &norm_i, 4);
    return norm2 - 2 * accu;
}

template <>
float AdditiveQuantizer::
        compute_1_distance_LUT<false, AdditiveQuantizer::ST_norm_cqint8>(
                const uint8_t* codes,
                const float* LUT) const {
    BitstringReader bs(codes, code_size);
    float accu = accumulate_IPs(*this, bs, LUT);
    uint32_t norm_i = bs.read(8);
    float norm2 = decode_qcint(norm_i);
    return norm2 - 2 * accu;
}

template <>
float AdditiveQuantizer::
        compute_1_distance_LUT<false, AdditiveQuantizer::ST_norm_cqint4>(
                const uint8_t* codes,
                const float* LUT) const {
    BitstringReader bs(codes, code_size);
    float accu = accumulate_IPs(*this, bs, LUT);
    uint32_t norm_i = bs.read(4);
    float norm2 = decode_qcint(norm_i);
    return norm2 - 2 * accu;
}

template <>
float AdditiveQuantizer::
        compute_1_distance_LUT<false, AdditiveQuantizer::ST_norm_qint8>(
                const uint8_t* codes,
                const float* LUT) const {
    BitstringReader bs(codes, code_size);
    float accu = accumulate_IPs(*this, bs, LUT);
    uint32_t norm_i = bs.read(8);
    float norm2 = decode_qint8(norm_i, norm_min, norm_max);
    return norm2 - 2 * accu;
}

template <>
float AdditiveQuantizer::
        compute_1_distance_LUT<false, AdditiveQuantizer::ST_norm_qint4>(
                const uint8_t* codes,
                const float* LUT) const {
    BitstringReader bs(codes, code_size);
    float accu = accumulate_IPs(*this, bs, LUT);
    uint32_t norm_i = bs.read(4);
    float norm2 = decode_qint4(norm_i, norm_min, norm_max);
    return norm2 - 2 * accu;
}

template <>
float AdditiveQuantizer::
        compute_1_distance_LUT<false, AdditiveQuantizer::ST_norm_from_LUT>(
                const uint8_t* codes,
                const float* LUT) const {
    FAISS_THROW_IF_NOT(codebook_cross_products.size() > 0);
    BitstringReader bs(codes, code_size);
    float accu = accumulate_IPs(*this, bs, LUT);
    BitstringReader bs2(codes, code_size);
    float norm2 = compute_norm_from_LUT(*this, bs2);
    return norm2 - 2 * accu;
}

} // namespace faiss



================================================
FILE: faiss/impl/AdditiveQuantizer.h
================================================
/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

#pragma once

#include <cmath>
#include <cstdint>
#include <vector>

#include <faiss/Index.h>
#include <faiss/IndexFlat.h>
#include <faiss/impl/Quantizer.h>

namespace faiss {

/** Abstract structure for additive quantizers
 *
 * Different from the product quantizer in which the decoded vector is the
 * concatenation of M sub-vectors, additive quantizers sum M sub-vectors
 * to get the decoded vector.
 */
struct AdditiveQuantizer : Quantizer {
    size_t M;                     ///< number of codebooks
    std::vector<size_t> nbits;    ///< bits for each step
    std::vector<float> codebooks; ///< codebooks

    // derived values
    /// codebook #1 is stored in rows codebook_offsets[i]:codebook_offsets[i+1]
    /// in the codebooks table of size total_codebook_size by d
    std::vector<uint64_t> codebook_offsets;
    size_t tot_bits = 0;            ///< total number of bits (indexes + norms)
    size_t norm_bits = 0;           ///< bits allocated for the norms
    size_t total_codebook_size = 0; ///< size of the codebook in vectors
    bool only_8bit = false;         ///< are all nbits = 8 (use faster decoder)

    bool verbose = false;    ///< verbose during training?
    bool is_trained = false; ///< is trained or not

    /// auxiliary data for ST_norm_lsq2x4 and ST_norm_rq2x4
    /// store norms of codebook entries for 4-bit fastscan
    std::vector<float> norm_tabs;
    IndexFlat1D qnorm; ///< store and search norms

    void compute_codebook_tables();

    /// norms of all codebook entries (size total_codebook_size)
    std::vector<float> centroid_norms;

    /// dot products of all codebook entries with the previous codebooks
    /// size sum(codebook_offsets[m] * 2^nbits[m], m=0..M-1)
    std::vector<float> codebook_cross_products;

    /// norms and distance matrixes with beam search can get large, so use this
    /// to control for the amount of memory that can be allocated
    size_t max_mem_distances = 5 * (size_t(1) << 30);

    /// encode a norm into norm_bits bits
    uint64_t encode_norm(float norm) const;

    /// encode norm by non-uniform scalar quantization
    uint32_t encode_qcint(float x) const;

    /// decode norm by non-uniform scalar quantization
    float decode_qcint(uint32_t c) const;

    /// Encodes how search is performed and how vectors are encoded
    enum Search_type_t {
        ST_decompress,    ///< decompress database vector
        ST_LUT_nonorm,    ///< use a LUT, don't include norms (OK for IP or
                          ///< normalized vectors)
        ST_norm_from_LUT, ///< compute the norms from the look-up tables (cost
                          ///< is in O(M^2))
        ST_norm_float, ///< use a LUT, and store float32 norm with the vectors
        ST_norm_qint8, ///< use a LUT, and store 8bit-quantized norm
        ST_norm_qint4,
        ST_norm_cqint8, ///< use a LUT, and store non-uniform quantized norm
        ST_norm_cqint4,

        ST_norm_lsq2x4, ///< use a 2x4 bits lsq as norm quantizer (for fast
                        ///< scan)
        ST_norm_rq2x4,  ///< use a 2x4 bits rq as norm quantizer (for fast scan)
        ST_count
    };

    AdditiveQuantizer(
            size_t d,
            const std::vector<size_t>& nbits,
            Search_type_t search_type = ST_decompress);

    AdditiveQuantizer();

    ///< compute derived values when d, M and nbits have been set
    void set_derived_values();

    ///< Train the norm quantizer
    void train_norm(size_t n, const float* norms);

    void compute_codes(const float* x, uint8_t* codes, size_t n)
            const override {
        compute_codes_add_centroids(x, codes, n);
    }

    /** Encode a set of vectors
     *
     * @param x      vectors to encode, size n * d
     * @param codes  output codes, size n * code_size
     * @param centroids  centroids to be added to x, size n * d
     */
    virtual void compute_codes_add_centroids(
            const float* x,
            uint8_t* codes,
            size_t n,
            const float* centroids = nullptr) const = 0;

    /** pack a series of code to bit-compact format
     *
     * @param codes        codes to be packed, size n * code_size
     * @param packed_codes output bit-compact codes
     * @param ld_codes     leading dimension of codes
     * @param norms        norms of the vectors (size n). Will be computed if
     *                     needed but not provided
     * @param centroids    centroids to be added to x, size n * d
     */
    void pack_codes(
            size_t n,
            const int32_t* codes,
            uint8_t* packed_codes,
            int64_t ld_codes = -1,
            const float* norms = nullptr,
            const float* centroids = nullptr) const;

    /** Decode a set of vectors
     *
     * @param codes  codes to decode, size n * code_size
     * @param x      output vectors, size n * d
     */
    void decode(const uint8_t* codes, float* x, size_t n) const override;

    /** Decode a set of vectors in non-packed format
     *
     * @param codes  codes to decode, size n * ld_codes
     * @param x      output vectors, size n * d
     */
    virtual void decode_unpacked(
            const int32_t* codes,
            float* x,
            size_t n,
            int64_t ld_codes = -1) const;

    /****************************************************************************
     * Search functions in an external set of codes.
     ****************************************************************************/

    /// Also determines what's in the codes
    Search_type_t search_type;

    /// min/max for quantization of norms
    float norm_min = NAN, norm_max = NAN;

    template <bool is_IP, Search_type_t effective_search_type>
    float compute_1_distance_LUT(const uint8_t* codes, const float* LUT) const;

    /*
        float compute_1_L2sqr(const uint8_t* codes, const float* LUT);
    */
    /****************************************************************************
     * Support for exhaustive distance computations with all the centroids.
     * Hence, the number of these centroids should not be too large.
     ****************************************************************************/

    /// decoding function for a code in a 64-bit word
    void decode_64bit(idx_t n, float* x) const;

    /** Compute inner-product look-up tables. Used in the centroid search
     * functions.
     *
     * @param xq     query vector, size (n, d)
     * @param LUT    look-up table, size (n, total_codebook_size)
     * @param alpha  compute alpha * inner-product
     * @param ld_lut  leading dimension of LUT
     */
    virtual void compute_LUT(
            size_t n,
            const float* xq,
            float* LUT,
            float alpha = 1.0f,
            long ld_lut = -1) const;

    /// exact IP search
    void knn_centroids_inner_product(
            idx_t n,
            const float* xq,
            idx_t k,
            float* distances,
            idx_t* labels) const;

    /** For L2 search we need the L2 norms of the centroids
     *
     * @param norms    output norms table, size total_codebook_size
     */
    void compute_centroid_norms(float* norms) const;

    /** Exact L2 search, with precomputed norms */
    void knn_centroids_L2(
            idx_t n,
            const float* xq,
            idx_t k,
            float* distances,
            idx_t* labels,
            const float* centroid_norms) const;

    virtual ~AdditiveQuantizer() override;
};

} // namespace faiss



================================================
FILE: faiss/impl/AdSampling.cpp
================================================
/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

#include <faiss/impl/AdSampling.h>

#include <cmath>

#include <faiss/impl/FaissAssert.h>

namespace faiss {
namespace detail {

double normal_quantile(double p) {
    // Three-branch rational polynomial; branch breakpoint p_low = 0.02425.
    static constexpr double a[] = {
            -3.969683028665376e+01,
            2.209460984245205e+02,
            -2.759285104469687e+02,
            1.383577518672690e+02,
            -3.066479806614716e+01,
            2.506628277459239e+00,
    };
    static constexpr double b[] = {
            -5.447609879822406e+01,
            1.615858368580409e+02,
            -1.556989798598866e+02,
            6.680131188771972e+01,
            -1.328068155288572e+01,
    };
    static constexpr double c[] = {
            -7.784894002430293e-03,
            -3.223964580411365e-01,
            -2.400758277161838e+00,
            -2.549732539343734e+00,
            4.374664141464968e+00,
            2.938163982698783e+00,
    };
    static constexpr double d[] = {
            7.784695709041462e-03,
            3.224671290700398e-01,
            2.445134137142996e+00,
            3.754408661907416e+00,
    };
    constexpr double p_low = 0.02425;
    constexpr double p_high = 1.0 - p_low;
    if (p < p_low) {
        const double q = std::sqrt(-2.0 * std::log(p));
        return (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q +
                c[5]) /
                ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1.0);
    } else if (p <= p_high) {
        const double q = p - 0.5;
        const double r = q * q;
        return (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r +
                a[5]) *
                q /
                (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r +
                 1.0);
    } else {
        const double q = std::sqrt(-2.0 * std::log(1.0 - p));
        return -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q +
                 c[5]) /
                ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1.0);
    }
}

double chi2_quantile_wh(int p, double alpha) {
    FAISS_THROW_IF_NOT(p > 0);
    // Wilson-Hilferty cube-root approximation:
    //   ((X/p)^(1/3) - (1 - 2/(9p))) / sqrt(2/(9p)) ~ N(0,1)
    // inverted into a quantile formula.
    //
    // Domain constraint: for very small alpha (< ~0.001) and small p
    // (< 4), t can go negative, producing a negative chi-squared quantile
    // (physically impossible). In practice this cannot happen here:
    // precompute_ad_thresholds calls with alpha = 1 - epsilon where
    // epsilon = ad_epsilon_factor / d, and d_prime_min >= 16, so
    // p >= 16 and alpha >= 1 - 1/16 = 0.9375 — well inside the accurate
    // region of the approximation.
    const double z = normal_quantile(alpha);
    const double t = 1.0 - 2.0 / (9.0 * p) + z * std::sqrt(2.0 / (9.0 * p));
    return p * t * t * t;
}

std::vector<float> precompute_ad_thresholds(int d, double epsilon) {
    FAISS_THROW_IF_NOT_MSG(
            epsilon > 0.0 && epsilon < 1.0,
            "precompute_ad_thresholds: epsilon must be in (0, 1)");
    FAISS_THROW_IF_NOT_MSG(
            d > 0, "precompute_ad_thresholds: d must be positive");
    std::vector<float> coeff(d + 1);
    for (int p = 1; p <= d; p++) {
        coeff[p] = static_cast<float>(chi2_quantile_wh(p, 1.0 - epsilon) / d);
    }
    return coeff;
}

} // namespace detail
} // namespace faiss



================================================
FILE: faiss/impl/AdSampling.h
================================================
/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

#pragma once

#include <vector>

namespace faiss {
namespace detail {

/** Inverse standard normal CDF. Three-branch rational polynomial,
 * absolute error < 1.15e-9 over `p in (0, 1)`. Behavior at the boundaries
 * (p <= 0 or p >= 1) is unspecified — returns NaN or +/-inf. */
double normal_quantile(double p);

/** Chi-squared quantile via cube-root approximation. Validated to within
 * 2% of scipy for `p in [16, d]` and `alpha <= 1 - 1e-6`. Accuracy
 * degrades for smaller `p` or for `alpha` near 1. */
double chi2_quantile_wh(int p, double alpha);

/** Build ADSampling threshold table of size `d + 1`:
 *   coeff[p] = chi2_quantile_wh(p, 1 - epsilon) / d.
 *
 * Indexing: coeff[0] is reserved (left at 0.0f). coeff[1..15] are
 * computed but NOT accuracy-bounded — callers requiring the 2% scipy
 * tolerance must consume only coeff[16..d]. SuperKMeans enforces
 * this via its `d_prime_min = 16` parameter. */
std::vector<float> precompute_ad_thresholds(int d, double epsilon);

} // namespace detail
} // namespace faiss



================================================
FILE: faiss/impl/AuxIndexStructures.cpp
================================================
/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// -*- c++ -*-

#include <algorithm>
#include <cstring>

#include <faiss/impl/AuxIndexStructures.h>

#include <faiss/impl/FaissAssert.h>

namespace faiss {

/***********************************************************************
 * RangeSearchResult
 ***********************************************************************/

RangeSearchResult::RangeSearchResult(size_t nq_in, bool alloc_lims)
        : nq(nq_in) {
    if (alloc_lims) {
        lims = new size_t[nq_in + 1];
        memset(lims, 0, sizeof(*lims) * (nq_in + 1));
    } else {
        lims = nullptr;
    }
    labels = nullptr;
    distances = nullptr;
    buffer_size = 1024 * 256;
}

/// called when lims contains the nb of elements result entries
/// for each query
void RangeSearchResult::do_allocation() {
    // works only if all the partial results are aggregated
    // simultaneously
    FAISS_THROW_IF_NOT(labels == nullptr && distances == nullptr);
    size_t ofs = 0;
    for (size_t i = 0; i < nq; i++) {
        size_t n = lims[i];
        lims[i] = ofs;
        ofs += n;
    }
    lims[nq] = ofs;
    labels = new idx_t[ofs];
    distances = new float[ofs];
}

RangeSearchResult::~RangeSearchResult() {
    delete[] labels;
    delete[] distances;
    delete[] lims;
}

/***********************************************************************
 * BufferList
 ***********************************************************************/

BufferList::BufferList(size_t buffer_size_in) : buffer_size(buffer_size_in) {
    wp = buffer_size_in;
}

BufferList::~BufferList() {
    for (size_t i = 0; i < buffers.size(); i++) {
        delete[] buffers[i].ids;
        delete[] buffers[i].dis;
    }
}

void BufferList::add(idx_t id, float dis) {
    if (wp == buffer_size) { // need new buffer
        append_buffer();
    }
    Buffer& buf = buffers.back();
    buf.ids[wp] = id;
    buf.dis[wp] = dis;
    wp++;
}

void BufferList::append_buffer() {
    Buffer buf = {new idx_t[buffer_size], new float[buffer_size]};
    buffers.push_back(buf);
    wp = 0;
}

/// copy elements ofs:ofs+n-1 seen as linear data in the buffers to
/// tables dest_ids, dest_dis
void BufferList::copy_range(
        size_t ofs,
        size_t n,
        idx_t* dest_ids,
        float* dest_dis) {
    size_t bno = ofs / buffer_size;
    ofs -= bno * buffer_size;
    while (n > 0) {
        size_t ncopy = ofs + n < buffer_size ? n : buffer_size - ofs;
        Buffer buf = buffers[bno];
        memcpy(dest_ids, buf.ids + ofs, ncopy * sizeof(*dest_ids));
        memcpy(dest_dis, buf.dis + ofs, ncopy * sizeof(*dest_dis));
        dest_ids += ncopy;
        dest_dis += ncopy;
        ofs = 0;
        bno++;
        n -= ncopy;
    }
}

/***********************************************************************
 * RangeSearchPartialResult
 ***********************************************************************/

void RangeQueryResult::add(float dis, idx_t id) {
    nres++;
    pres->add(id, dis);
}

RangeSearchPartialResult::RangeSearchPartialResult(RangeSearchResult* res_in)
        : BufferList(res_in->buffer_size), res(res_in) {}

/// begin a new result
RangeQueryResult& RangeSearchPartialResult::new_result(idx_t qno) {
    RangeQueryResult qres = {qno, 0, this};
    queries.push_back(qres);
    return queries.back();
}

void RangeSearchPartialResult::finalize() {
    set_lims();
#pragma omp barrier

#pragma omp single
    res->do_allocation();

#pragma omp barrier
    copy_result();
}

/// called by range_search before do_allocation
void RangeSearchPartialResult::set_lims() {
    for (size_t i = 0; i < queries.size(); i++) {
        RangeQueryResult& qres = queries[i];
        res->lims[qres.qno] = qres.nres;
    }
}

/// called by range_search after do_allocation
void RangeSearchPartialResult::copy_result(bool incremental) {
    size_t ofs = 0;
    for (size_t i = 0; i < queries.size(); i++) {
        RangeQueryResult& qres = queries[i];

        copy_range(
                ofs,
                qres.nres,
                res->labels + res->lims[qres.qno],
                res->distances + res->lims[qres.qno]);
        if (incremental) {
            res->lims[qres.qno] += qres.nres;
        }
        ofs += qres.nres;
    }
}

void RangeSearchPartialResult::merge(
        std::vector<RangeSearchPartialResult*>& partial_results,
        bool do_delete) {
    int npres = partial_results.size();
    if (npres == 0) {
        return;
    }
    RangeSearchResult* result = partial_results[0]->res;
    size_t nx = result->nq;

    // count
    for (const RangeSearchPartialResult* pres : partial_results) {
        if (!pres) {
            continue;
        }
        for (const RangeQueryResult& qres : pres->queries) {
            result->lims[qres.qno] += qres.nres;
        }
    }
    result->do_allocation();
    for (int j = 0; j < npres; j++) {
        if (!partial_results[j]) {
            continue;
        }
        partial_results[j]->copy_result(true);
        if (do_delete) {
            delete partial_results[j];
            partial_results[j] = nullptr;
        }
    }

    // reset the limits
    for (size_t i = nx; i > 0; i--) {
        result->lims[i] = result->lims[i - 1];
    }
    result->lims[0] = 0;
}

/***********************************************************
 * Interrupt callback
 ***********************************************************/

std::unique_ptr<InterruptCallback> InterruptCallback::instance;

std::mutex InterruptCallback::lock;

void InterruptCallback::clear_instance() {
    delete instance.release();
}

void InterruptCallback::check() {
    if (!instance.get()) {
        return;
    }
    if (instance->want_interrupt()) {
        FAISS_THROW_MSG("computation interrupted");
    }
}

bool InterruptCallback::is_interrupted() {
    if (!instance.get()) {
        return false;
    }
    std::lock_guard<std::mutex> guard(lock);
    return instance->want_interrupt();
}

size_t InterruptCallback::get_period_hint(size_t flops) {
    if (!instance.get()) {
        return (size_t)1 << 30; // never check
    }
    // for 10M flops, it is reasonable to check once every 10 iterations
    return std::max((size_t)10 * 10 * 1000 * 1000 / (flops + 1), (size_t)1);
}

void TimeoutCallback::set_timeout(double timeout_in_seconds) {
    timeout = timeout_in_seconds;
    start = std::chrono::steady_clock::now();
}

bool TimeoutCallback::want_interrupt() {
    if (timeout == 0) {
        return false;
    }
    auto end = std::chrono::steady_clock::now();
    std::chrono::duration<float, std::milli> duration = end - start;
    float elapsed_in_seconds = duration.count() / 1000.0;
    if (elapsed_in_seconds > timeout) {
        timeout = 0;
        return true;
    }
    return false;
}

void TimeoutCallback::reset(double timeout_in_seconds) {
    auto tc(new faiss::TimeoutCallback());
    faiss::InterruptCallback::instance.reset(tc);
    tc->set_timeout(timeout_in_seconds);
}

} // namespace faiss



================================================
FILE: faiss/impl/AuxIndexStructures.h
================================================
/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

// Auxiliary index structures, that are used in indexes but that can
// be forward-declared

#ifndef FAISS_AUX_INDEX_STRUCTURES_H
#define FAISS_AUX_INDEX_STRUCTURES_H

#include <stdint.h>

#include <cstring>
#include <memory>
#include <mutex>
#include <vector>

#include <faiss/impl/InvertedListScannerStats.h>

#include <faiss/MetricType.h>
#include <faiss/impl/platform_macros.h>

namespace faiss {

/** The objective is to have a simple result structure while
 *  minimizing the number of mem copies in the result. The method
 *  do_allocation can be overloaded to allocate the result tables in
 *  the matrix type of a scripting language like Lua or Python. */
struct RangeSearchResult {
    size_t nq;    ///< nb of queries
    size_t* lims; ///< size (nq + 1)

    idx_t* labels;    ///< result for query i is labels[lims[i]:lims[i+1]]
    float* distances; ///< corresponding distances (not sorted)

    size_t buffer_size; ///< size of the result buffers used

    /// lims must be allocated on input to range_search.
    explicit RangeSearchResult(size_t nq, bool alloc_lims = true);

    /// called when lims contains the nb of elements result entries
    /// for each query
    virtual void do_allocation();

    virtual ~RangeSearchResult();
};

/****************************************************************
 * Result structures for range search.
 *
 * The main constraint here is that we want to support parallel
 * queries from different threads in various ways: 1 thread per query,
 * several threads per query. We store the actual results in blocks of
 * fixed size rather than exponentially increasing memory. At the end,
 * we copy the block content to a linear result array.
 *****************************************************************/

/** List of temporary buffers used to store results before they are
 *  copied to the RangeSearchResult object. */
struct BufferList {
    // buffer sizes in # entries
    size_t buffer_size;

    struct Buffer {
        idx_t* ids;
        float* dis;
    };

    std::vector<Buffer> buffers;
    size_t wp; ///< write pointer in the last buffer.

    explicit BufferList(size_t buffer_size);

    ~BufferList();

    /// create a new buffer
    void append_buffer();

    /// add one result, possibly appending a new buffer if needed
    void add(idx_t id, float dis);

    /// copy elements ofs:ofs+n-1 seen as linear data in the buffers to
    /// tables dest_ids, dest_dis
    void copy_range(size_t ofs, size_t n, idx_t* dest_ids, float* dest_dis);
};

struct RangeSearchPartialResult;

/// result structure for a single query
struct RangeQueryResult {
    idx_t qno;   //< id of the query
    size_t nres; //< nb of results for this query
    RangeSearchPartialResult* pres;
    InvertedListScannerStats stats;

    /// called by search function to report a new result
    void add(float dis, idx_t id);
};

/// the entries in the buffers are split per query
struct RangeSearchPartialResult : BufferList {
    RangeSearchResult* res;

    /// eventually the result will be stored in res_in
    explicit RangeSearchPartialResult(RangeSearchResult* res_in);

    /// query ids + nb of results per query.
    std::vector<RangeQueryResult> queries;

    /// begin a new result
    RangeQueryResult& new_result(idx_t qno);

    /*****************************************
     * functions used at the end of the search to merge the result
     * lists */
    void finalize();

    /// called by range_search before do_allocation
    void set_lims();

    /// called by range_search after do_allocation
    void copy_result(bool incremental = false);

    /// merge a set of PartialResult's into one RangeSearchResult
    /// on output the partialresults are empty!
    static void merge(
            std::vector<RangeSearchPartialResult*>& partial_results,
            bool do_delete = true);
};

/***********************************************************
 * Interrupt callback
 ***********************************************************/

struct FAISS_API InterruptCallback {
    virtual bool want_interrupt() = 0;
    virtual ~InterruptCallback() {}

    // lock that protects concurrent calls to is_interrupted
    static std::mutex lock;

    static std::unique_ptr<InterruptCallback> instance;

    static void clear_instance();

    /** check if:
     * - an interrupt callback is set
     * - the callback returns true
     * if this is the case, then throw an exception. Should not be called
     * from multiple threads.
     */
    static void check();

    /// same as check() but return true if is interrupted instead of
    /// throwing. Can be called from multiple threads.
    static bool is_interrupted();

    /** assuming each iteration takes a certain number of flops, what
     * is a reasonable interval to check for interrupts?
     */
    static size_t get_period_hint(size_t flops);
};

struct TimeoutCallback : InterruptCallback {
    std::chrono::time_point<std::chrono::steady_clock> start;
    double timeout;
    bool want_interrupt() override;
    void set_timeout(double timeout_in_seconds);
    static void reset(double timeout_in_seconds);
};

} // namespace faiss

#endif



================================================
FILE: faiss/impl/ClusteringHelpers.cpp
================================================
/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

#include <faiss/impl/ClusteringHelpers.h>

#include <cassert>
#include <chrono>
#include <cinttypes>
#include <cstdint>
#include <cstdio>
#include <cstring>
#include <limits>
#include <vector>

#include <omp.h>

#include <faiss/Index.h>
#include <faiss/impl/FaissAssert.h>
#include <faiss/utils/random.h>

namespace faiss {
namespace detail {

uint64_t get_actual_rng_seed(const int seed) {
    return (seed >= 0)
            ? seed
            : static_cast<uint64_t>(std::chrono::high_resolution_clock::now()
                                            .time_since_epoch()
                                            .count());
}

idx_t subsample_training_set(
        const Clustering& clus,
        idx_t nx,
        const uint8_t* x,
        size_t line_size,
        const float* weights,
        uint8_t** x_out,
        float** weights_out) {
    FAISS_THROW_IF_NOT(clus.k > 0 && clus.max_points_per_centroid > 0);
    if (clus.verbose) {
        printf("Sampling a subset of %zd / %" PRId64 " for training\n",
               clus.k * clus.max_points_per_centroid,
               nx);
    }

    const uint64_t actual_seed = get_actual_rng_seed(clus.seed);

    std::vector<idx_t> perm;
    if (clus.use_faster_subsampling) {
        SplitMix64RandomGenerator rng(actual_seed);

        const idx_t new_nx = clus.k * clus.max_points_per_centroid;
        perm.resize(new_nx);
        assert(!perm.empty());
        for (idx_t i = 0; i < new_nx; i++) {
            perm[i] = rng.rand_int64() % nx;
        }
    } else {
        FAISS_THROW_IF_NOT_FMT(
                nx <= static_cast<idx_t>(std::numeric_limits<int>::max()),
                "Dataset too large (%" PRId64
                ") for standard subsampling; "
                "set use_faster_subsampling=true",
                nx);
        std::vector<int> int_perm(nx);
        rand_perm(int_perm.data(), nx, actual_seed);
        perm.assign(int_perm.begin(), int_perm.end());
    }

    nx = clus.k * clus.max_points_per_centroid;
    FAISS_THROW_IF_NOT_FMT(
            perm.size() >= static_cast<size_t>(nx),
            "subsample_training_set: perm size %zu < required nx %" PRId64,
            perm.size(),
            nx);
    assert(!perm.empty());

    uint8_t* x_new = new uint8_t[nx * line_size];
    *x_out = x_new;

    for (idx_t i = 0; i < nx; i++) {
        memcpy(x_new + i * line_size, x + perm[i] * line_size, line_size);
    }
    if (weights) {
        float* weights_new = new float[nx];
        for (idx_t i = 0; i < nx; i++) {
            weights_new[i] = weights[perm[i]];
        }
        *weights_out = weights_new;
    } else {
        *weights_out = nullptr;
    }
    return nx;
}

void compute_centroids(
        size_t d,
        size_t k,
        size_t n,
        size_t k_frozen,
        const uint8_t* x,
        const Index* codec,
        const int64_t* assign,
        const float* weights,
        float* hassign,
        float* centroids) {
    k -= k_frozen;
    centroids += k_frozen * d;

    memset(centroids, 0, sizeof(*centroids) * d * k);

    size_t line_size = codec ? codec->sa_code_size() : d * sizeof(float);

#pragma omp parallel
    {
        int nt = omp_get_num_threads();
        int rank = omp_get_thread_num();

        // this thread is taking care of centroids c0:c1
        size_t c0 = (k * rank) / nt;
        size_t c1 = (k * (rank + 1)) / nt;
        std::vector<float> decode_buffer(d);

        for (size_t i = 0; i < n; i++) {
            int64_t ci = assign[i];
            FAISS_THROW_IF_NOT_MSG(
                    ci >= 0 && ci < k + k_frozen, "invalid cluster assignment");
            ci -= k_frozen;
            if (ci >= static_cast<int64_t>(c0) &&
                ci < static_cast<int64_t>(c1)) {
                float* c = centroids + ci * d;
                const float* xi;
                if (!codec) {
                    xi = reinterpret_cast<const float*>(x + i * line_size);
                } else {
                    float* xif = decode_buffer.data();
                    codec->sa_decode(1, x + i * line_size, xif);
                    xi = xif;
                }
                if (weights) {
                    float w = weights[i];
                    hassign[ci] += w;
                    for (size_t j = 0; j < d; j++) {
                        c[j] += xi[j] * w;
                    }
                } else {
                    hassign[ci] += 1.0;
                    for (size_t j = 0; j < d; j++) {
                        c[j] += xi[j];
                    }
                }
            }
        }
    }

#pragma omp parallel for
    for (idx_t ci = 0; ci < static_cast<idx_t>(k); ci++) {
        if (hassign[ci] == 0) {
            continue;
        }
        float norm = 1 / hassign[ci];
        float* c = centroids + ci * d;
        for (size_t j = 0; j < d; j++) {
            c[j] *= norm;
        }
    }
}

// a bit above machine epsilon for float16
static constexpr float EPS = 1.f / 1024.f;

int split_clusters(
        size_t d,
        size_t k,
        size_t n,
        size_t k_frozen,
        float* hassign,
        float* centroids) {
    k -= k_frozen;
    centroids += k_frozen * d;
    FAISS_THROW_IF_NOT_MSG(
            n > k,
            "split_clusters: n must exceed k to find a non-empty donor centroid");

    size_t nsplit = 0;
    RandomGenerator rng(1234);
    for (size_t ci = 0; ci < k; ci++) {
        if (hassign[ci] == 0) {
            // Probabilistic donor pick weighted by hassign; deterministic
            // fallback to the largest cluster if too many iterations pass.
            size_t cj;
            size_t max_tries = 10 * k;
            size_t n_tries = 0;
            bool found = false;
            for (cj = 0; n_tries < max_tries; cj = (cj + 1) % k) {
                float p = (hassign[cj] - 1.0) / (float)(n - k);
                float r = rng.rand_float();
                if (r < p) {
                    found = true;
                    break;
                }
                n_tries++;
            }
            if (!found) {
                // Deterministic fallback: split the largest cluster.
                cj = 0;
                for (size_t j = 1; j < k; j++) {
                    if (hassign[j] > hassign[cj]) {
                        cj = j;
                    }
                }
            }
            memcpy(centroids + ci * d,
                   centroids + cj * d,
                   sizeof(*centroids) * d);

            /* small symmetric perturbation */
            for (size_t j = 0; j < d; j++) {
                if (j % 2 == 0) {
                    centroids[ci * d + j] *= 1 + EPS;
                    centroids[cj * d + j] *= 1 - EPS;
                } else {
                    centroids[ci * d + j] *= 1 - EPS;
                    centroids[cj * d + j] *= 1 + EPS;
                }
            }

            /* assume even split of the cluster */
            hassign[ci] = hassign[cj] / 2;
            hassign[cj] -= hassign[ci];
            nsplit++;
        }
    }

    return static_cast<int>(nsplit);
}

} // namespace detail
} // namespace faiss



================================================
FILE: faiss/impl/ClusteringHelpers.h
================================================
/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

#pragma once

#include <cstddef>
#include <cstdint>

#include <faiss/Clustering.h>
#include <faiss/Index.h>

namespace faiss {
namespace detail {

/** Resolve the actual RNG seed for clustering helpers.
 *
 * If `seed >= 0`, returns `seed`. Otherwise returns a high-resolution
 * timestamp so that callers get a non-deterministic seed.
 *
 * @param seed  user-provided seed; negative values request a time-based seed
 * @return      the resolved seed
 */
uint64_t get_actual_rng_seed(const int seed);

/** Subsample a training set down to `clus.k * clus.max_points_per_centroid`
 * rows.
 *
 * Allocates `*x_out` (and `*weights_out` when `weights` is non-null) with
 * `new[]`; ownership is transferred to the caller.
 *
 * @param clus        clustering parameters (reads `k`,
 * `max_points_per_centroid`, `use_faster_subsampling`, `seed`, `verbose`)
 * @param nx          number of input training rows
 * @param x           input training data, row-major, `nx * line_size` bytes
 * @param line_size   bytes per training row
 * @param weights     optional per-row weights (length `nx`), or null
 * @param x_out       output: newly allocated subsampled rows
 * @param weights_out output: newly allocated subsampled weights, or null
 * @return            number of rows in the subsampled set
 */
idx_t subsample_training_set(
        const Clustering& clus,
        idx_t nx,
        const uint8_t* x,
        size_t line_size,
        const float* weights,
        uint8_t** x_out,
        float** weights_out);

/** compute centroids as (weighted) sum of training points
 *
 * @param x            training vectors, size n * code_size (from codec)
 * @param codec        how to decode the vectors (if NULL then cast to float*)
 * @param weights      per-training vector weight, size n (or NULL)
 * @param assign       nearest centroid for each training vector, size n
 * @param k_frozen     do not update the k_frozen first centroids
 * @param centroids    centroid vectors (output only), size k * d
 * @param hassign      histogram of assignments per centroid (size k),
 *                     should be 0 on input
 *
 */
void compute_centroids(
        size_t d,
        size_t k,
        size_t n,
        size_t k_frozen,
        const uint8_t* x,
        const Index* codec,
        const int64_t* assign,
        const float* weights,
        float* hassign,
        float* centroids);

/** Handle empty clusters by splitting larger ones.
 *
 * It works by slightly changing the centroids to make 2 clusters from
 * a single one. Takes the same arguments as compute_centroids.
 *
 * @return           nb of splitting operations (larger is worse)
 */
int split_clusters(
        size_t d,
        size_t k,
        size_t n,
        size_t k_frozen,
        float* hassign,
        float* centroids);

} // namespace detail
} // namespace faiss



================================================
FILE: faiss/impl/ClusteringInitialization.cpp
================================================
/*
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

#include <faiss/impl/ClusteringInitialization.h>

#include <algorithm>
#include <chrono>
#include <cstring>
#include <limits>
#include <random>
#include <unordered_set>
#include <vector>

#include <faiss/impl/FaissAssert.h>
#include <faiss/utils/distances_dispatch.h>
#include <faiss/utils/random.h>

namespace faiss {

namespace {

uint64_t get_seed(int64_t seed) {
    if (seed >= 0) {
        return static_cast<uint64_t>(seed);
    }
    return static_cast<uint64_t>(std::chrono::high_resolution_clock::now()
                                         .time_since_epoch()
                                         .count());
}

/// Compute distance from point idx to its nearest centroid.
/// Optionally checks both primary and secondary centroid sets.
float distance_to_nearest_centroid(
        size_t d,
        size_t n_centroids,
        const float* x,
        size_t idx,
        const float* centroids,
        size_t n_existing_centroids = 0,
        const float* existing_centroids = nullptr) {
    if (n_centroids == 0 && n_existing_centroids == 0) {
        return std::numeric_limits<float>::infinity();
    }

    const float* point = x + idx * d;
    float min_dist = std::numeric_limits<float>::max();

    auto check_centroids = [&]<SIMDLevel SL>() {
        // Check primary centroids
        for (size_t c = 0; c < n_centroids; c++) {
            float dist = fvec_L2sqr<SL>(point, centroids + c * d, d);
            min_dist = std::min(min_dist, dist);
        }

        // Check existing centroids if provided
        for (size_t c = 0; c < n_existing_centroids; c++) {
            float dist = fvec_L2sqr<SL>(point, existing_centroids + c * d, d);
            min_dist = std::min(min_dist, dist);
        }
    };
    with_simd_level(check_centroids);
    return min_dist;
}

/// Result of initializing distances for D² sampling
struct InitDistancesResult {
    size_t first_new_centroid_idx;
    double sum_d2;
    size_t first_selected_idx; // Only valid when first_new_centroid_idx == 1
};

/// Initialize distance array for D² sampling.
/// If existing centroids are provided, computes distances to them.
/// Otherwise, selects first centroid randomly and computes distances to it.
/// Returns first_new_centroid_idx (0 if existing, 1 if random first),
/// sum of squared distances, and the first selected index (if applicable).
InitDistancesResult init_distances_for_d2_sampling(
        size_t d,
        size_t n,
        const float* x,
        float* centroids,
        size_t n_existing_centroids,
        const float* existing_centroids,
        std::vector<double>& distances,
        std::mt19937_64& rng) {
    double sum_d2 = 0.0;
    size_t first_selected_idx = 0;

    if (n_existing_centroids > 0 && existing_centroids != nullptr) {
        // Compute distances to nearest existing centroid
        for (size_t i = 0; i < n; i++) {
            distances[i] = distance_to_nearest_centroid(
                    d, n_existing_centroids, x, i, existing_centroids);
            sum_d2 += distances[i];
        }
        return {0, sum_d2, 0};
    } else {
        // Select first centroid randomly
        std::uniform_int_distribution<size_t> uniform_dist(0, n - 1);
        first_selected_idx = uniform_dist(rng);
        std::memcpy(centroids, x + first_selected_idx * d, d * sizeof(float));

        // Compute distances to first centro

[... Content truncated due to length ...]

</details>

</golden_source>

<golden_source type="guideline_youtube">
## YouTube Video Transcripts (from Article Guidelines)

_No guideline YouTube video transcripts found._

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

<details>
<summary>Facebook AI and the Index Factory</summary>

**Source URL:** <https://www.pinecone.io/learn/series/faiss/composite-indexes/>

# Facebook AI and the Index Factory

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2F066c44f15fc4b2241e65d4af3c16264a174b5f81-1920x1080.png&w=3840&q=75

In the world of [vector search](https://www.pinecone.io/learn/what-is-similarity-search/), there are many indexing methods and vector processing techniques that allow us to prioritize between recall, latency, and memory usage.

Using specific methods such as IVF, [PQ](https://www.pinecone.io/learn/series/faiss/product-quantization/), or [HNSW](https://www.pinecone.io/learn/series/faiss/hnsw/), we can often return good results. But for _best performance_ we will usually want to use _composite indexes_.

We can view a composite index as a step-by-step process of vector transformations and one or more indexing methods. Allowing us to place multiple indexes and/or processing steps together to create our ‘ideal’ index.

For example, we can use an inverted file (IVF) index to reduce the scope of our search (increasing search speed), and then add a compression technique such as [product quantization (PQ)](https://www.pinecone.io/learn/series/faiss/product-quantization/) to keep larger indexes within a reasonable size limit.

Where there is the ability to customize indexes, there is the risk of producing indexes with unnecessarily poor recall, latency, or memory usage.

We must know how composite indexes work if we want to build robust and high-performance vector similarity search applications. It is essential to understand where different indexes or vector transformations can be used — and when they are not needed.

In this article, we will learn how to build high-performance composite indexes using [Facebook AI Similarity Search (Faiss)](https://www.pinecone.io/learn/series/faiss/) — a powerful library used by many for building fast and accurate vector similarity search indexes. We will also introduce the Faiss `index_factory` which allows us to build composite indexes with clearer, more elegant code.

## What are Composite Indexes

Composite indexes are akin to _lego blocks_; we place one on top of another. We will find that most blocks fit together — but different combinations can produce anything from an artistic masterpiece to an unrecognizable mess.

The same applies to Faiss. Most components _can_ be placed together — but that does not mean they _should_ be placed together.

A composite index is built from any combination of:

- **Vector transform** — a pre-processing step applied to vectors before indexing (PCA, OPQ).
- **Coarse quantizer** — _rough_ organization of vectors to sub-domains (for restricting search scope, includes IVF, IMI, and HNSW).
- **Fine quantizer** — a _finer_ compression of vectors into smaller domains (for compressing index size, such as PQ).
- **Refinement** — a final step at search-time which re-orders results using distance calculations on the original flat vectors. Alternatively, another index (non-flat) index can be used.

Note that coarse quantization refers to the ‘clustering’ of vectors (such as inverted indexing with IVF). By using coarse quantization, we enable _non-exhaustive_ search by limiting the search scope.

Fine quantization describes the compression of vectors into _codes_ (as with PQ) \[1\]\[2\]\[3\]. The purpose of this is to reduce the memory usage of the index.

### Index Components

We can build a composite index using the following components:

| Vector transform | Coarse quantizer | Fine quantizer | Refinement |
| --- | --- | --- | --- |
| PCA, OPQ, RR, L2norm, ITQ, Pad | IVF,Flat, IMI, IVF,HNSW, IVF,PQ, IVF,RCQ, HNSW,Flat, HNSW,SQ, HNSW,PQ | Flat _, PQ, SQ, Residual_, RQ, LSQ, ZnLattice, LSH | RFlat, Refine\* |

For example, we could build an index where we:

- Transform incoming vectors using `OPQ`.
- Perform coarse quantization of vectors by storing them in an inverted file list `IVF`, enabling non-exhaustive search.
- Compress vectors, reducing memory usage with `PQ` within each IVF cell _(the vectors are quantized, but their cell assignment does not change)_.
- After the search, re-order results based on their original flat vectors `RFlat`.

When building these indexes, it can get messy to use a list of the different Faiss classes — so it is often clearer to build our indexes using the Faiss `index_factory`.

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2F409e12bad9ca16b82d685bf6c203ea9c0d282b59-1920x1080.png&w=3840&q=75

We can merge IVF and PQ indexes to store quantized PQ vectors in an IVF structure.

## Faiss Index Factory

The Faiss `index_factory` function allows us to build composite indexes using little more than a string. It allows us to switch:

```python

```

For this:

```python

```

_We haven’t specified the L2 distance in our_ _`index_factory`_ _example because the_ _`index_factory`_ _uses L2 by default. If we’d like to use_ _`IndexFlatIP`_ _we add_ _`faiss.METRIC_INNER_PRODUCT`_ _to our_ _`index_factory`_ _parameters._

We can confirm that both methods produce the same composite index by comparing their performance. First, do they return the same nearest neighbors?

In\[4\]:

```python

```

In\[5\]:

```python

```

In\[6\]:

```python

```

Out\[6\]:

```
True
```

Identical results, and how do they compare for search speed and memory usage?

In\[7\]:

```python

```

Out\[7\]:

```
153 µs ± 7.47 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```

In\[8\]:

```python

```

Out\[8\]:

```
148 µs ± 5.79 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```

In\[9\]:

```python

```

Out\[9\]:

```
520133259
```

In\[10\]:

```python

```

Out\[10\]:

```
520133259
```

The `get_memory` function returns an exact match for memory usage. Search speeds are incredibly close, with the `index_factory` version 5µs faster — a negligible difference.

_We calculate recall as the percentage of matches from the top-`k`_ _between a flat L2 index and the tested index._

_The more commonly used metric in literature is recall@k; this is_ **_not_** _the recall calculated here. Recall@k is the percentage of queries that returned its nearest neighbor in the top_ _`k`_ _returned records._

_If we returned the ground-truth nearest neighbor 50% of the time when using a_ _`k`_ _value of_ _`100`, we would say the recall@100 performance is 0.5._

### Why Use the Index Factory

Judging from our tests, we can be confident that these two index-building methods are nothing more than separate paths to the same destination.

With that in mind — why should we care to learn how we use `index_factory`? First, it can depend on personal preference. If you prefer the class-based index building approach, stick with it.

However, through using the `index_factory` we can greatly improve the elegance and clarity of our code. We will see that five lines of complicated code can be represented in a single — more readable — line of code when using the `index_factory`.

Let’s put together a composite index where we pre-process vectors with OPQ, cluster with IVF, quantize using PQ, then re-order with a flat index.

```python

```

This code demonstrates the complexity that adding several components to our index can create. If we rewrite this using the `index_factory`, we get much simpler code:

```python

```

Both approaches produce the exact same index. The performance for each:

|  | Recall | Search Time | Memory Usage |
| --- | --- | --- | --- |
| Without index\_factory | 31% | 181µs | 552MB |
| With index\_factory | 31% | 174µs | 552MB |

Search time does tend to be slightly faster when using the `index_factory` — but otherwise, there are no performance differences between equivalent indexes built with or without the `index_factory`.

## Popular Composite Indexes

Now that we know how to quickly build composite indexes using the `index_factory`, let’s explore a few popular and high-performance combinations.

### IVFADC

We have covered a modified **IVFADC** index above — the `IVF256,PQ32` portion of our previous examples make up the core of IVFADC. Let’s dive into it in a little more detail.

The index was introduced alongside product quantization in 2010 \[4\]. Since then, it has remained one of the most popular indexes — thanks to being an easy-to-use index that produces reasonable recall, fast speeds, and _incredible_ memory usage.

IVFADC is ideal when our main priority is to minimize memory usage while maintaining fast search speeds. This comes at the cost of _okay_ — but not _good_ recall performance.

There are two steps to indexing with IVFADC:

1. Vectors are assigned to different lists ( _or_ Voronoi cells) in the IVF structure.
2. The vectors are compressed using PQ.

![Indexing process for IVFADC, adapted from [4].](https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2F0b9d996a8476e1bbe0ceea54ea7703f304125ffd-1920x980.png&w=3840&q=75)

Indexing process for IVFADC, adapted from \[4\].

After indexing vectors, an **A** symmetric **D** istance **C** omputation (ADC) is performed between query vectors `xq` and our indexed, quantized vectors.

The search is referred to as being _asymmetric_ because it compares `xq` — which is not compressed, against compressed PQ vectors (that we previously indexed).

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fe6008652a7306c91155c9dd1b95a8e934a2ffefa-1920x1000.png&w=3840&q=75

With symmetric distance computation (SDC, left) we quantize xq before comparing it to our previously quantized xb vectors. ADC (right) skips the quantization of xq and compares it directly to the quantized xb vectors.

To implement the index using the `index_factory` we can write:

In\[40\]:

```python

```

Out\[40\]:

```
30
```

With this, we create an IVFADC index with `256` IVF cells; each vector is compressed with PQ using `m` and `nbits` values of `32` and `8`, respectively. PQ uses `nbits == 8` by default so we can also write `"IVF256,PQ32"`.

_`m`: number of subvectors that original vectors are split into_

_`nbits`: number of bits used by each subquantizer, we can calculate the number of centroids used by each subquantizer as_ _`2**nbits`_

We can decrease `nbits` to reduce index memory usage or increase to improve recall and search speed. However, the current version of Faiss does restrict `nbits` to `>= 8` for `IVF,PQ`.

It is also possible to increase the `index.nprobe` value to search more IVF cells — by default, this value is `1`.

In\[42\]:

```python

```

Out\[42\]:

```
74
```

Here we have our index performance for various `nbits` and `nprobe` values:

| Index | nprobe | Recall | Search Time | Memory |
| --- | --- | --- | --- | --- |
| IVF256,PQ32x4 | 1 | 27% | 329µs | 25MB |
| IVF256,PQ32x4 | 6 | 45% | 975µs | 25MB |
| IVF256,PQ32x8 | 1 | 30% | 136µs | 40MB |
| IVF256,PQ32x8 | 8 | 74% | 729µs | 40MB |

#### Optimized Product Quantization

**IVFADC** and other indexes using PQ can benefit from **O** ptimized **P** roduct **Q** uantization (OPQ).

OPQ works by rotating vectors to flatten the distribution of values across the subvectors used in PQ. This is particularly beneficial for unbalanced vectors with uneven data distributions.

In Faiss, we add OPQ as a pre-processing step. For IVFADC, the OPQ index string looks like `" OPQ32,IVF256,PQ32"` where the `32` in `OPQ32` _and_`PQ32` refers to the number of bytes `m` in the PQ generated codes.

_The OPQ matrix in Faiss is_ **_not_** _the whole rotation and PQ process. It is only the rotation. A PQ step must be included downstream for OPQ to be implemented._

As before, we will need to `train` the index on initialization.

In\[45\]:

```python

```

Out\[45\]:

```
31
```

In\[46\]:

```python

```

Out\[46\]:

```
142 µs ± 2.25 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```

The data distribution of the Sift1M dataset is already well balanced, so OPQ gives us only a minor increase in recall performance. With an `nprobe == 1` we have increased recall from 30% -> 31%.

We can increase our `nprobe` value to improve recall (at the cost of speed). However, because we added a pre-processing step to our index, we cannot access `nprobe` directly with `index.nprobe` as this `index` no longer refers to the IVF portion of our index.

Instead, we must _extract_ the IVF index before modifying the `nprobe` value — we can do this using the `extract_index_ivf` function.

In\[47\]:

```python

```

Out\[47\]:

```
74
```

In\[48\]:

```python

```

Out\[48\]:

```
1.08 ms ± 21.1 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

With a higher `nprobe` value of `14` — we return a recall of 74%. A similar recall result to PQ alone, alongside an increased search time from 729µs -> 1060µs.

| Index | nprobe | Recall | Search Time | Memory |
| --- | --- | --- | --- | --- |
| IVF256,PQ32x4 | 1 | 30% | 136µs | 40.2MB |
| IVF256,PQ32x4 | 1 | 31% | 143µs | 40.3MB |
| IVF256,PQ32x8 | 8 | 74% | 729µs | 40.2MB |
| IVF256,PQ32x8 | 13 | 74% | 1060µs | 40.3MB |

We will see later in the article that OPQ can be used to improve performance, but as we can see here, that is not _always_ the case.

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2F2f8651fdfc87169f2b088c95d37a8a033701ad7a-1920x1080.png&w=3840&q=75

Search time (top) and recall (bottom) for various nprobe values. We have included "IVF256,Flat" for comparison. The flat index has much higher memory usage at 520MB.

OPQ can also be used to reduce the dimensionality of our vectors in this pre-processing step. This dimensionality `D` must be a multiple of `M`, preferably `D == 4M`. To reduce dimensionality to `64`, we could use `"OPQ16_64,IVF256,PQ16"`.

### Multi-D-ADC

Multi-D-ADC refers to **multi-d** imensional indexing, alongside a PQ step which produces an **a** symmetric **d** istance **c** omputation at search time (as we discussed previously) \[5\].

The **multi-D-ADC** index is based on the inverted multi-index (IMI), an extension of IVF.

IMI can outperform IVF in both recall and search speed but does increase memory usage \[7\]. This makes IMI indexes (such as multi-D-ADC) ideal in cases where IVFADC doesn’t quite reach the recall and speed required, and you can spare more memory usage. The IMI index works in a very similar way to IVF, but Voronoi cells are split across vector dimensions. What this produces is akin to a multi-level Voronoi cell structure.

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fce81a066f489fe38b681d4fd7111f9cb5e4c804e-1920x1020.png&w=3840&q=75

Voronoi cells split across multiple vector subspaces. Given a query vector xq, we would compare each xq subvector to its respective subspace cells.

When we add a vector compression to IMI using PQ, we produce the **multi-D-ADC** index. Where ADC refers to the asymmetric distance computation that is made when comparing query vectors to PQ vectors.

Putting all of this together, we can create a multi-D-ADC index using the index factory string `" IMI2x8,PQ32"`.

In\[50\]:

```python

```

In\[53\]:

```python

```

Out\[53\]:

```
72
```

In\[54\]:

```python

```

Out\[54\]:

```
1.35 ms ± 60.2 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

To return a similar recall to our IVFADC equivalent, we increased search time to 1.3ms, which is very slow. However, if we add OPQ to our index, we will return much better results.

In\[56\]:

```python

```

In\[59\]:

```python

```

Out\[59\]:

```
74
```

In\[60\]:

```python

```

Out\[60\]:

```
461 µs ± 30 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

For a recall of 74%, our OPQ multi-D-ADC index is fastest at an average search time of just 461µs.

| Index | Recall | Search Time | Memory |
| --- | --- | --- | --- |
| IVF256,PQ32 | 74% | 729µs | 40.2MB |
| IMI2x8,PQ32 | 72% | 1350µs | 40.8MB |
| OPQ32,IMI2x8,PQ32 | 74% | 461µs | 40.7MB |

As before, we can fine-tune the index to prioritize recall or speed using `nprobe`.

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2F3500949c3274050f2c7bcc970dd74e24c46a7e95-1920x1080.png&w=3840&q=75

Search time (top) and recall (bottom) for various nprobe values. We have included "IMI2x8,Flat" for comparison. The flat index has much higher memory usage at 520MB.

`"OPQ32,IMI2x8,PQ32"` is one of our best indexes in terms of recall and speed at low memory. However, we’ll see that we can improve these metrics even further with the following index.

### HNSW Indexes

IVF with **H** ierarchical **N** avigable **S** mall- **W** orld (HNSW) graphs is our final composite index. This index splits our indexed vectors into cells as per usual with IVF, but this time we will optimize the process using HNSW.

Compared to our previous two indexes, IVF with HNSW produces comparable or better speed and significantly higher recall — at the cost of _much_ higher memory usage.

At a high level, HNSW is based on the _small-world graph theory_ that all vertices ( _nodes_) in a network — no matter how large — can be traversed in a small number of steps.

Example of a navigable small-world graph, all nodes within the graph are connected by a small number of edge traversals. Small world graph theory assumes the same to be true even for huge networks with billions of vertices.

In this small world graph, we see both short-range and long-range links. When traversing across long-range links, we move more quickly across the graph.

HNSW takes advantage of this by splitting graph links into multiple layers. At the higher entry layers, we find only long-range links. As we move down the layers, shorter-range links are added.

When searching, we start at these higher layers with long-range links. Meaning our first traversals are across long-range links. As we move down the layers, our search becomes finer as we traverse across more short-range links.

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2F0b4b19e673df19f684dbfe5ed91f80f283cda10c-1920x1080.png&w=3840&q=75

HNSW graphs break the typical graph containing both long-range and short-range links into multiple layers (hierarchies). During the search, we begin at the highest layer, which consists of long-range links. As we move down through each layer, the links become more granular.

This approach should minimize the number of traversals (speeding up search) while still performing a very fine search in the lower layers (maintaining high recall).

That is HNSW, but how can we merge HNSW with IVF?

Using vanilla IVF, we introduce our query vector and compare it to every cell centroid, identifying the nearest centroids for restricting our search scope.

To pair this process with HNSW, we produce an HNSW graph of all of these cell centroids, making the exhaustive centroid search _approximate_.

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2F0c94d256ebe92cf3ffea7429f54ede89477a6513-1920x1080.png&w=3840&q=75

HNSW can be used to quickly find the approximate nearest neighbor using IVF cell centroids.

Previously, we have been using IVF indexes with 256 cell centroids. An exhaustive search of 256 is fast, and there is no reason to use an approximate search with so few centroids.

And because we have so few cells, each cell must contain many vectors - which will still be searched using an exhaustive search. In this case, IVF+HNSW on the cell centroids does not help.

With IVF+HNSW indexes, we need to swap _' few centroids and large cells'_ for _' many centroids and small cells'_.

For our 1M index, an `nlist` value of `65536` is recommended \[8\]. However, we should provide _at least_`30*nlist == 1.97M` vectors to `index.train`, which we do not have. So a smaller `nlist` of `16384` or less is more suitable. For this dataset, `nlist == 4096` returned the highest recall (at slower speeds).

Using IVF+HNSW, we quickly identify the approximate nearest cell centroids using HNSW, then restrict our _exhaustive_ search to those nearest cells.

The standard IVF+HNSW index can be built with `"IVF4096_HNSW32,Flat"`. Using this, we have:

- `4096` IVF cells.
- Cell centroids are stored in an HNSW graph. Each centroid is linked to `32` other centroids.
- The vectors themselves have not been changed. They are `Flat` vectors.

In\[62\]:

```python

```

In\[63\]:

```python

```

Out\[63\]:

```
25
```

In\[64\]:

```python

```

Out\[64\]:

```
58.9 µs ± 3.25 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
```

In\[65\]:

```python

```

Out\[65\]:

```
100
```

In\[66\]:

```python

```

Out\[66\]:

```
916 µs ± 9.23 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```

With this index, we can produce incredible performance ranging from 25% -> 100% recall at search times of 58.9µs -> 916µs.

https://www.pinecone.io/_next/image/?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fvr8gru94%2Fproduction%2Fae39ade8751b67c4acdc7f960c9a0ee9e565ff95-1920x1080.png&w=3840&q=75

Search time (top) and recall (bottom) for various nprobe values. At the cost of longer search times, we can increase recall by decreasing nlist.

However, the IVF+HNSW index is not without its flaws. Although we have incredible recall and fast search speeds, the memory usage of this index is _huge_. Our 1M 128-dimensional vectors produce an index size of 523MB+.

As we have done before, we can reduce this using PQ and OPQ, but this will reduce recall and increase search times.

| Index | Recall | Search Time | Memory |
| --- | --- | --- | --- |
| IVF4096\_HNSW,Flat | 90% | 550µs | 523MB |
| IVF4096\_HNSW,PQ32 (PQ) | 69% | 550µs | 43MB |
| OPQ32,IVF4096\_HNSW,PQ32 (OPQ) | 74% | 364µs | 43MB |

If a lower recall is acceptable for minimizing search time and memory usage, the IVF+HNSW index with OPQ is ideal. On the other hand, IVF+HNSW with PQ offers no benefit over our previous _IVFADC_ and _Multi-D-ADC_ indexes.

| Name | Index String | Recall | Search Time | Memory |
| --- | --- | --- | --- | --- |
| IVFADC | IVF256,PQ32 | 74% | 729µs | 40MB |
| Multi-D-ADC | OPQ32,IMI2x8,PQ32 | 74% | 461µs | 41MB |

That’s it for this article! We introduced composite indexes and how to build them using the Faiss `index_factory`. We explored several of the most popular composite indexes, including:

- IVFADC
- Multi-D-ADC
- IVF-HNSW

By indexing and searching the Sift1M dataset, we learned how to modify each index’s parameters to prioritize recall, speed, and memory usage.

With what we have covered here, you will be able to design and test a variety of composite indexes and better decide on an index structure that best suits your needs.

## References

\[1\] Y.Chen, et al., [Approximate Nearest Neighbor Search by Residual Vector Quantization](https://www.researchgate.net/publication/51873001_Approximate_Nearest_Neighbor_Search_by_Residual_Vector_Quantization) (2010), _Sensors_

\[2\] Y. Matsui, et al., [A Survey of Product Quantization](https://www.jstage.jst.go.jp/article/mta/6/1/6_2/_pdf) (2018), _ITE Trans. on MTA_

\[3\] T. Ge, et. al., [Optimized Product Quantization](http://kaiminghe.com/publications/pami13opq.pdf) (2014), _TPAMI_

\[4\] H. Jégou, et al., [Product quantization for nearest neighbor search](https://lear.inrialpes.fr/pubs/2011/JDS11/jegou_searching_with_quantization.pdf) (2010), _TPAMI_

\[5\] A. Babenko, V. Lempitsky, [The Inverted Multi-Index](http://sites.skoltech.ru/app/data/uploads/sites/25/2014/12/TPAMI14.pdf) (2012), _CVPR_

\[6\] H. Jégou, et al., [Searching in One Billion Vectors: Re-rank with Source Coding](https://arxiv.org/pdf/1102.3828.pdf) (2011), _ICASSP_

\[7\] D. Baranchuk, et al., [Revisiting the Inverted Indices for Billion-Scale Approximate Nearest Neighbors](https://arxiv.org/pdf/1802.02422.pdf) (2018), _ECCV_

\[8\] [Guidelines to choose an index](https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index), Faiss wiki

\[9\] [The Index Factory](https://github.com/facebookresearch/faiss/wiki/The-index-factory), Faiss wiki

</details>

<details>
<summary>Faiss</summary>

# Faiss

**Source URL:** <https://www.pinecone.io/learn/series/faiss/>

Facebook AI Similarity Search (Faiss) is one of the best open source options for similarity search. In this ebook, you will learn the essentials of vector search and how to apply them in Faiss to build powerful vector indexes.

## Introduction

Vector search has been used by tech giants like Google and Amazon for decades. It has been claimed to be a significant driver in clicks, views, and sales across several platforms. Yet, it was only with Faiss that this technology became more accessible.

In the past few years, vector search exploded in popularity. It has driven ecommerce sales, powered music and podcast search, and even recommended your next favorite shows on streaming platforms. Vector search is everywhere and in the following chapters you will discover why it has found such great success and how to apply it yourself using the Facebook AI Similarity Search (Faiss) library.

</details>

</golden_source>

<research_source type="guideline_exploitation" phase="exploitation">
## Exploitation Sources (from Article Guidelines — Other Sources)

_No exploitation guideline sources found._

</research_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

<details>
<summary>**Approximate Nearest Neighbor Search Small World Approach**</summary>

# **Approximate Nearest Neighbor Search Small World Approach**

**Alexander Ponomarenko, Yury Mal'kov, Andrey Logvinov, Vladimir Krylov MERA Labs LLC, Nizhny Novgorod, Russia**

[aponom@meralabs.com,](mailto:aponom@meralabs.com) [ymalkov@meralabs.com,](mailto:ymalkov@meralabs.com) [alogvinov@meralabs.com,](mailto:alogvinov@meralabs.com) vkrylov@meralabs.com

# **ABSTRACT**

In this paper we propose a novel approach to solving the nearest neighbor search problem. We propose to build a data structure where the greedy search algorithm can be applied which is known to have logarithmic complexity in structures with navigable small world properties. The distinctive feature of our approach is that we build a non-hierarchical structure with possibility of local minimums which are circumvented by performing a series of searches starting from arbitrary elements of the structure. The performed simulation shows that the structure built using the proposed algorithms has navigable small world properties with logarithmic search complexity which is retained even for high-dimensional data.

**Keywords**: Similarity Search, Small World, Distributed Data Structure

## **1. INTRODUCTION**

We present a new approach for solving nearest neighbor search problem in general metric space. This problem appears when we need to find a closest object from finite set of objects to given query , where is the set of all possible objects (data domain). Closeness or proximity of two objects is defined as distance function .

In general, the search problem can be described as follows: Let be a domain, d a distance measure on , and ( a metric space. Given a set of elements, preprocess or structure the data, so that proximity queries are answered efficiently.

The nearest neighbor search problem is relevant to many applications such as pattern recognition and classification [**[1](#page-4-0)**], [content-based](http://en.wikipedia.org/wiki/Content-based_image_retrieval) image retrieval [**[2](#page-4-1)**], machine learning [**[3](#page-4-2)**], [Recommendation](http://en.wikipedia.org/wiki/Recommender_system) systems [**[4](#page-4-3)**], searching similar DNA sequence [**[5](#page-4-4)**], semantic document retrieval [**[6](#page-4-5)**].

In a trivial case data structure is a simple linear list. The complexity of addition operation is , but searching for closest object for requires evaluation of the metric function for every element from the set of objects . This amounts to complexity , where is the number of objects in .

General way to reduce amount of distance measure calculations consists of building a set of equivalence classes, discarding some classes, and exhaustively searching the rest [**[7](#page-5-0)**]. Authors also showed that two main techniques based on equivalence

relations, namely, pivoting and compact partitions encompass all the existing methods. Pivot technique relies on taking pivots and mapping the metric space onto using the distance and they can outperform a compact partitioning index if it has enough memory. Methods based on compact partition are more efficient for spaces with high dimensionality.

However, methods from both classes generally use either data structures with tree topology (GNAT, GHT, SAT, BST, VT, MT) or, in some cases, distance matrix (ALAESA, LAESA)

We suggest using for solving nearest neighbor problem a data structure with small word network topology presented by graph , where every object from is [uniquely](http://lingvo.yandex.ru/unequivocally/%D1%81%20%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE/LingvoUniversal/) associated with vertex from . Thereby searching for the closest element to query from the data set will take the form of searching for a vertex in the graph .

Application of that approach is based on follows:

- There exist algorithms for building small world networks that have the ability to perform nearest neighbor and addition of a new object to the structure with complexity of [**[8](#page-5-1)**].
- Small world networks have no root element.
- All operations (addition and search) use only local information and can be initiated from any element that has been added to the structure.

This gives opportunity for building decentralized similarity search oriented storage systems where physical data location doesn't depend on the content because every data object can be placed on the arbitrary physical machine and can be connected with other by links like in p2p systems. Such storage systems can provide simultaneous access to large numbers of users for performing data search and addition), have good fault tolerance and have unlimited scalability in terms of performance and capacity.

One of the basic vertex search algorithms in graphs is greedy search. This algorithm has simple implementation on the structure that has small world network topology and can be initiated from every vertex.

In order for the result of the algorithm to be the exact nearest element to the query, the network should contain th[e Delaunay](http://en.wikipedia.org/wiki/Delaunay_triangulation) graph as its subgraph, which is dual to the Voronoi tessellation [**9**].

However, the requirement of search in for the exact nearest neighbor can be excessive (optional) for the applications

described above. So the problem for finding the exact nearest neighbor can be substituted for the approximate nearest neighbor search, since we don't need to support whole/exact Delaunay graph.

For the search algorithm to be logarithmically scalable, the small world network should have navigation property that was already discussed in [8]

In this paper we present the algorithm for data structure construction based on small world network topology with graph G(V, E) which uses greedy search algorithm for finding approximate nearest neighbor. Graph G(V, E) contains approximate Delaunay graph and has navigation property. Search algorithm has the ability to change accuracy of search without modification of the structure. Presented algorithms do not use the coordinate representation and do not presume the properties of linear spaces, because they are based only on the metric computation between objects, and therefore is applicable to data from general metric spaces.

#### 2. RELATED WORKS

Kd-tree [10] and quadra trees [11] were among the first structures for solving exact nearest neighbor search problem. They perform well in 2-3 dimensions (search complexity is close to  $O(\log n)$ ), but analysis of the worst case for that structures [12] indicates  $O(d*N^{1-1/d})$  search complexity, where d is dimensionality.

Other structures which have tree topology such as variants of kd-trees, R-trees and structures based on space-filling curves are surveyed in [13]. They also have good performance when searching in a low-dimension (d < 4) metric space, but they quickly lose their effectiveness with increasing number of dimensions [14]. A more effective data structure for exact nearest neighbor search in  $\Re^d$  with search complexity  $O(2^d \log n)$  has been described in [15]. But as can be seen, search complexity has exponential dependence from the number of dimensions.

Structures such as mvp-tree [16], vp<sup>s</sup>-tree and vp<sup>sb</sup>-tree [17] use "vantage point" technique, but no analysis has been provided for search complexity in spaces with high number of dimensions.

In general, presently there are no methods for effective exact nearest neighbor search in high-dimensionality metric space. The reason behind it lies in the "curse" of dimensionality [7].

To avoid the curse of dimensionality while retaining the logarithmic scaling of the number of elements, it was proposed to reduce the requirements for finding the nearest neighbor, making it approximate.

Thus a large number of papers appeared which proposed to search for nearest neighbor with  $\epsilon$  accuracy ( $\epsilon$ -NNS). For example, Arya and Mount proposed methods with search

complexity  $O(\log^3 n)$ , but preprocessing requires  $O(n^2)$  and algorithm was applicable only to data from  $E^d$  [18].

Kleinberg proposed two methods [19] for solving  $\varepsilon$ -NNS. First method requires  $O(n \log d)^{2d}$  preprocessing time and query time polynomial in d,  $\varepsilon$  and  $\log n$ . Another method with preprocessing polynomial in d,  $\varepsilon$  and n, but with query time  $O(n + d \log^3 n)$ . Also both methods are applicable only to data from  $E^d$ 

The first algorithms with search complexity polynomial in d,  $\log n$ ,  $\varepsilon^{-1}$  and polynomial preprocessing time for fixed  $\varepsilon$  were proposed by Indyk and Motwani in [20] and Kushilevitz, Ostrovsky and Rabani in [21]. Indyk and Motwani were the first ones to relax  $\varepsilon$ -ANN problem to approximate point location in equal balls ( $\varepsilon$ -PLEB). For the formulation of the problem in  $\varepsilon$ -PLEB points in metric space expand to the balls with center at this point and radius  $(1+\varepsilon)r$ , it is necessary to determine which ball belongs to the query q. Also in [20] proposed a second method, which uses the concept of locality-sensitive hashing regarding formulation of the problem  $\varepsilon$ -PLEB, with search time  $O(n^{1/(1+\varepsilon)})$ ,

however requires near quadratic memory (for small  $\epsilon$ ). In addition, the first method is applicable only for  $E^d$ , and the second for the Hamming space.

In general, the concept of locality-sensitive hashing has become popular in the last decade to solve the ANN problem. Other works using the concept of locality-sensitive hashing are [22], [23]. But they all have the same major drawback: each algorithm is focused on a narrow class of metrics such as Hamming distance, Jakarta or  $l_s$  norms for Euclidean space. Thus it is necessary to create digests in order to decide which method to choose.

The first structure for solving ANN in  $E^d$  with topology of small world networks is Raynet [24]. It is an extension of earlier work by the same authors Voronet [25], which solved the problem of the exact NN in  $E^2$ . Originally Voronet was envisioned as a p2p network, where every node has coordinates in  $E^2$ . In Raynet every node has the coordinates in  $E^d$ . The system supports two levels of links - short for correct work of the greedy search algorithm and long - for logarithmic search. Short links correspond to edges of Delaunay graph, i.e. each object has references to objects that are neighbors of its Voronoi region. The main difference of Raynet from Voronet is that in Raynet every object doesn't know all of its Voronoi neighbors, i.e. Raynet obtains neighborhood with approximately using the Monte Carlo method.

Raynet is the closest work to ours in terms of general concept. But unlike Raynet, we propose a structure that works with objects from arbitrary metric spaces.

### 3. STRUCTURE OVERVIEW

We solve the problem of approximate nearest neighbor search formulated as follows: given objects from domain  $\mathcal D$  with

distance function . For finite set an effective probability search method is required to find which is closest to . Effective method means that search complexity must scale logarithmically with the number of elements in . The exact search is not guaranteed, i.e. the result of the algorithm may be an element that is not true nearest neighbor, nevertheless structure and algorithms are designed to minimize the probability of this and there is a possibility to adjust it by varying the parameter of the search algorithm without changing the structure**.**

The structure of is constructed as a small world network described by a graph , where the objects from the set are uniquely mapped to the vertices from the set . The set of edges is determined by the structure construction algorithm, so as to ensure correct operation of the greedy search algorithm.

Since in the proposed structure each vertex is uniquely mapped to an element from the set , we will use the terms "vertex", "element" or "object" interchangeably. We will use the term "friends" for vertices that share an edge. List of vertices that share a common edge with the vertex is called the friend list of vertex .

# **4. SEARCH ALGORITHM**

#### **Greedy Search**

The basic search algorithm traverses the edges of the graph from one vertex to another. The algorithm takes two parameters: query and the vertex which is the starting point of search (the entry point). Starting from the entry point at each vertex the algorithm computes the metric value from query q to each vertex from the friend list of the current vertex and then selects the vertex with minimal value of the metric. If the metric value between the query and the selected vertex is smaller than between the query and the current element, then the algorithm moves to that vertex. After that the algorithm repeats. The algorithm stops at the vertex whose friend list doesn't contain a vertex that is closer to the query than the vertex itself. That vertex is a local minimum.

```
Greedy_Search(q: object, venter_point: object)
1 vcurr ← venter_point; 
2 dmin ← d(q, vcurr); vnext ← NIL;
3 foreach vfriend vcurr.getFriends() do
4 if d(query, vfriend) < dmin then
5 dmin ← d(q, vfriend);
6 vnext ← vfriend;
7 if vnext = Nil then return vcurr;
8 else return Greedy_Search(q, vnext);
```

The element which is a local minimum with respect to query q, can be either the true closest element to the query q from the entire set of elements of , or a false closest..

If every element in the structure had in their friend list all of its Voronoi neighbors, then this would exclude the existence of false local minimums. Maintaining this condition is equivalent to constructing Delaunay graph, which is dual to the Voronoi diagram.

Because it is impossible to determine exact Delaunay graph [**[26](#page-5-4)**] (excluding the variant of the complete graph) we cannot avoid the existence of local minimums.

But for the problem of approximate searching as defined above it is not an obstacle since approximate search does not require the entire Delaunay graph [**[24](#page-5-2)**]. As shown below, the probability of finding the true nearest element tends exponentially towards 1 with increase of the average number of edges in the approximated Delaunay graph.

#### **Multi Search**

In order to be able to find the true closest element in a network with local minimums, we propose the following modification of the search algorithm. We propose to use a series of m searches initiated from random vertices and choose the result element that is closest to the query from the set of found elements. Since the greedy search

Greedy\_Search(q, venterPoint ϵ V)is deterministic for each entry point venterPoint ϵ V it either results in a success finding the true nearest neigbor, or with a failure - finding the element that is not the nearest neighbor of *q*.

Thus search of the closest element to the same query may result in finding of the true nearest neighbor or a false nearest neigbor depending on the entry point from which the search algorithm started.

Since we can choose the entry point at random, there is a probability of finding the true closest to the particular element q (but not to all elements). Moreover, this probability is always nonzero, because it is always possible to choose the exact nearest neighbor as the entry point, which subsequently will be returned by the greedy search algorithm.

If probability to find true closest in one search attempt is p then probability to find the same element in search attempts is , so failure probability decreases exponentially with the number of search attempts. Thus, we can improve search precision, increasing the parameter - number independent searches.

```
Multi_Search(object q, integer: m)
1 results: SET[objects];
2 for (i 0; i < m; i++) do
3 enter_point getRandomEnterPoint();
4 local_min Greedy_Search(query, 
enter_point)
5 if local_min results then
6 results.add(result);
7 return results;
```

![](_page_3_Figure_0.jpeg)

**Fig 1**

If , where is the number of elements in the structure, the algorithm becomes [exhaustive search.](http://lingvo.yandex.ru/exchaustive%20search/%D1%81%20%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%BE%D0%B3%D0%BE/LingvoScience/)

If the graph of the network has small-world properties, then it is possible tp choose a random vertex in a number of random steps proportional to , which doesn't affect overall logarithmic search complexity.

Therefore the overall complexity of the search will increase no more than times.

# **5. DATA ADDITION ALGORITHM**

Since we build an approximation of the Delaunay graph, there is much freedom in the choice of construction algorithm. For example in [**[24](#page-5-2)**] it is proposed to build approximate Delaunay graph which minimizes the volume of Voronoi region for a fixed number of edges for each vertex in the graph. In [**27**] it is proposed to connect new element with k closest objects which are already in the structure. It is based on the idea that intersection of the set of elements which are Voronoi neighbors and the k closest elements is large. In [**27**], [**[28](#page-5-5)**] authors also have shown theoretically and confirmed by experimental results that graph which constructed by proposed algorithm has properties of small world network if elements arrive in random order.

We propose a modified variant of this algorithm which is distinguished by the fact that that the search for k nearest elements uses a series of searches.

The algorithm takes three parameters: the object to be added to the structure and two positive integers k and init\_attempts. First, the algorithm determines a set of local minima, using the procedure Multi\_Search, which

produces a series of independent searches on init\_attempts of randomly selected elements from the set of objects that already have been added to the structure. After that algorithm determines neighborhood u, which contains all neighbors of each found local minimums. Set u is sorted in ascending order by distance from the object new\_object to be added. After that new\_object is connected with the first K nearest elements from the set of u.

```
Nearest_Neighbor_Add(object: new_object,
integer: k, integer: init_attempts)
1 SET[object]: localMins 
MultiAttempts_Search(new_object, 
init_attempts);
2 SET[object]: u ; //neighborhood;
3 foreach object: local_min localMins 
do
4 u u local_min.getFriends();
6 sort the set u so to satisfy the 
condition d(u[i], new_object) < d(u[i+1], 
new_object)
7 for (i 0; i < k; i++) do
8 u[i].connect(new_object);
9 new_object.connect(u[i]);
```

Fig 1 shows the structure which is constructed by Nearest\_Neighbor\_Add algorithm for points from E2. Circles denote the elements. The numbers near thems correspond to the addition order. Solid lines show the links (edges) between elements. Dotted lines correspond to the borders of Voronoi tessellation. Delaunay graph edges between elements 0 and 10, 1 and 9 are missing. The structure obtained by the algorithm with parameters m = 3 and attemptsNumber = 5. Element with number 0 is a local minimum, which is not the closest to queries that fall into the

shaded area "A", respectively 10 for the "B", 9 for D and 1 for the region"C". Hatched lines show the paths of the two search algorithm runs for query q in the region "B". The algorithm run which starts from vertex 7 stops on the element 10 which is local minimum, but not the closest to the query q. However, the algorithm run which starts from vertex 5 finds the true closest vertex to the query q.

### 6. EXPERIMENT RESULTS

![](_page_4_Figure_2.jpeg)

Fig 2

We have implemented the algorithms presented above in order to validate our assumptions about the logarithmic search complexity dependence of the total number of elements.

We used randomly selected points from the  $E^D$  as test dataset.  $L_2$  (Euclidean distance) was selected as proximity function

n elements were added to the structure. We chose the number of search attempts m so that the probability of finding the true closest element to the query was not less than 95%. The number of metric calculations was measured. The graph shows the percent of scanned elements (vertical) with an increase in the number of added elements in the structure (horizontal).

The graph (**Fig 2**) shows that with the increase of number of elements in the structure, the percentage of visited elements decreases, and the curve becomes a straight line with angle 45 degrees. This gives us grounds to speak of logarithmic complexity of the search on the number of scanned elements.

The graph shows that the curve for higher dimensions behaves similarly. From this we can make the

assumption that there is no exponential dependence from the dimension of space. But it requires more careful study.

#### 7. CONCLUSION

We have proposed a method of organizing data into a small world topology data structure suited for approximate nearest neighbor search in metric space.

We have created a modified k nearest neighbor connection algorithm which is one of the possible algorithms for construction of small world data structures with navigation properties.

Simulation results confirm logarithmic dependency of search complexity from the number of elements in the structure.

All proposed algorithms use only local information on each step and can be initiated from any vertex.

All elements in the structure are of the same type, there is no central or root element.

Thus, all mentioned structure properties are a basis for using the structure for building totally decentralized data storage systems.

</details>

<details>
<summary>Approximate nearest neighbor algorithm based on navigable small world graphs</summary>

# Approximate nearest neighbor algorithm based on navigable small world graphs

![](_page_0_Picture_7.jpeg)

Yury Malkov <sup>a,b,\*</sup>, Alexander Ponomarenko <sup>b,c</sup>, Andrey Logvinov <sup>b</sup>, Vladimir Krylov <sup>b,d</sup>

- <sup>a</sup> The Institute of Applied Physics of the Russian Academy of Sciences, 46 Ulyanov Street, 603950 Nizhny Novgorod, Russia
- <sup>b</sup> MERA Labs LLC, 13, Delovaya St., Nizhny Novgorod 603163, Russia
- <sup>c</sup> National Research University Higher School of Economics, Laboratory of Algorithms and Technologies for Network Analysis, 136 Rodionova, Nizhny Novgorod 603093, Russia
- <sup>d</sup> Nizhny Novgorod State Technical University, Nizhny Novgorod, Russia

#### ARTICLE INFO

#### Available online 4 November 2013

Keywords: Similarity search k-Nearest neighbor Approximate nearest neighbor Navigable small world Distributed data structure

#### ABSTRACT

We propose a novel approach to solving the approximate *k*-nearest neighbor search problem in metric spaces. The search structure is based on a navigable small world graph with vertices corresponding to the stored elements, edges to links between them, and a variation of greedy algorithm for searching. The navigable small world is created simply by keeping old Delaunay graph approximation links produced at the start of construction. The approach is very universal, defined in terms of arbitrary metric spaces and at the same time it is very simple. The algorithm handles insertions in the same way as queries: by finding approximate neighbors for the inserted element and connecting it to them. Both search and insertion can be done in parallel requiring only local information from the structure. The structure can be made distributed. The accuracy of the probabilistic k-nearest neighbor queries can be adjusted without rebuilding the structure.

The performed simulation for data in the Euclidean spaces shows that the structure built using the proposed algorithm has small world navigation properties with  $\log^2(n)$  insertion and search complexity at fixed accuracy, and performs well at high dimensionality. Simulation on a CoPHiR dataset revealed its high efficiency in case of large datasets (more than an order of magnitude less metric computations at fixed recall) compared to permutation indexes. Only 0.03% of the 10 million 208-dimensional vector dataset is needed to be evaluated to achieve 0.999 recall (virtually exact search). For recall 0.93 processing speed 2800 queries/s can be achieved on a dual Intel X5675 Xenon server node with Java implementation.

© 2013 Elsevier Ltd. All rights reserved.

#### 1. Introduction

The scalability of any software system is limited by the scalability of its data structures. Massively distributed systems like BitTorrent or Skype are based on distributed

E-mail address: yurymalkov@mail.ru (Y. Malkov).

hash tables. While the latter structures have good scalability, their search functionality is limited to the exact matching. This limitation arises because small changes in an element value lead to large and chaotic changes in the hash value, making the hash-based approach inapplicable to the range search and the similarity search problems.

However, there are many applications (such as pattern recognition and classification [1], content-based image retrieval [2], machine learning [3], recommendation systems [4], searching similar DNA sequence [5], semantic

<sup>\*</sup>Corresponding author at: The Institute of Applied Physics of the Russian Academy of Sciences, 46 Ul'yanov Street, 603950 Nizhny Novgorod, Russia.

document retrieval [6]) that require the similarity search rather than just exact matching. The k-nearest neighbor search (k-NNS) problem is a mathematical formalization for similarity search. It is defined as follows: we need to find the set of k closest objects  $P \subseteq X$  from a finite set of objects  $X \subseteq \mathcal{D}$  to a given query  $q \in \mathcal{D}$ , where  $\mathcal{D}$  is the set of all possible objects (the data domain). Closeness or proximity of two objects  $o', o'' \in \mathcal{D}$  is defined as a distance function  $\delta(o', o'')$ .

A naïve solution for the k-NNS problem is to calculate the distance function  $\delta$  between q and every element from X. This leads to linear search time complexity, which is much worse than the scalability of structures for exact match search, and makes the naïve version of k-NNS almost impossible to use for large size datasets.

We suggest a solution for the nearest neighbor search problem: a data structure represented by a graph G(V, E), where every object  $o_i$  from X is uniquely associated with a vertex  $v_i$  from V. Searching for the closest elements to the query q from the data set X takes the form of searching for a vertices in the graph G.

This gives an opportunity for building decentralized similarity search oriented storage systems where physical data location does not depend on the content because every data object can be placed on an arbitrary physical machine and can be connected with others by links like in p2p systems.

One of the basic vertex search algorithms in graphs with metric objects is the greedy search algorithm. It has a simple implementation and can be initiated from any vertex. In order for the algorithm to work correctly (always return precise results), the network must contain the Delaunay graph as its subgraph, which is dual to the Voronoi tessellation [7]. However, there are major drawbacks associated with the Delaunay graph: it requires some knowledge of metric space internal structure [8] and it suffers from the curse of dimensionality [7]. Moreover, for the applications described above, the precise exactness of the search is not required. So the problem of finding the exact nearest neighbors can be substituted by the approximate nearest neighbor search, and thus we do not need to support the whole/exact Delaunay graph.

Graphs with logarithmic scalability of the greedy search algorithm are called navigable small world graphs, they are well known in Euclidean spaces [9]. Note that the small world models (not *navigable* small world) like [10] do not have this feature. Even though there are short paths in the graph, the greedy algorithm do no tend to find them, in the end having a power law search complexity. Solutions for constructing a navigational small world graphs were proposed for general spaces but they are usually more complex, requiring sampling, iterations, rewiring etc. [11–14]. We show that the small world navigation property can be achieved with a much simpler technique even without prior knowledge of internal structure of a metric space (e.g. dimensionality or data density distribution).

In this paper we present a simple algorithm for the data structure construction based on a navigable small world network topology with a graph G(V, E), which uses the greedy search algorithm for the approximate k-nearest neighbor search problem. The graph G(V, E) contains an

approximation of the Delaunay graph and has long-range links together with the small-world navigation property. The search algorithm we propose has the ability to choose the accuracy of search without modification of the structure. Presented algorithms do not use the coordinate representation and do not presume the properties of Euclidean spaces, because they are based only on comparing distances between the objects and the query, and therefore in principle are applicable to data from general metric (or even non-metric) spaces. Simulations revealed weak dimensionality dependence for Euclidean data.

#### 2. Related work

Kd-tree [15] and quadra trees [16] were among the first works on the kNN problem. They perform well in 2–3 dimensions (search complexity is close to  $O(\log n)$  in practice), but the analysis of the worst case for these structures [17] indicates  $O(d^*N^{1-1/d})$  search complexity, where d is the dimensionality.

In Ref. [8] was proposed an exact-proximity search structure that uses the Delaunay graph with the greedy search algorithm. Authors showed the impossibility of finding the exact Delaunay graph in a general metric space, and to keep the search exact they resort to backtracking. Proposed data structure has construction time  $O(n \log^2 n / \log \log n)$  and search time  $O(n^{1-\Theta(1/\log \log n)})$  in high dimensions and  $O(n^{\alpha})$ ,  $(0 < \alpha < 1)$  in low dimensions.

In general, currently there are no methods for effective exact NNS in high-dimensionality metric spaces. The reason behind this lies in the "curse" of dimensionality [18]. To avoid the curse of dimensionality while retaining the logarithmic cost on the number of elements, it was proposed to reduce the requirements for the kNN problem solution, making it approximate (Approximate kNN).

There are two commonly used definitions of the approximate neighbor search. One class of methods proposed to search with predefined accuracy  $\varepsilon$  ( $\varepsilon$ -NNS). It means that the distance between the query and any element in the result is no more than  $1+\varepsilon$  times the distance from query to its true k-th nearest neighbor. Such methods have been described in [19–23]. Another class gives probability guarantee of finding true k closest point to the query [24–31], using "recall" (the fraction of true k nearest elements found).

Some structures [19–23] can be applied only to Euclidean space. Other methods [24–31] are applicable to the general metric space. More can be found in reviews [32,33].

Permutation indexes (PI) [25,34] is an efficient nondistributed algorithm suitable for general metric spaces. The idea behind PI is to represent each database object with the permutation of a set of references, called the permutants, sorted by distance to the object. The distance between objects is hinted by the distance between their respective permutations. PI is known to have high precision and recall even for datasets with high intrinsic dimensionality.

The work by Houle and Sakuma [26] features a probabilistic tree-like structure for the approximate nearest neighbor search in general metric spaces, based on selection of the nearest neighbors. The algorithm was simulated

<span id="page-2-0"></span>on real-life data. The work by Chávez and Tellez [\[27\]](#page-7-0) also uses determination of nearest neighbors in its construction algorithm, with the greedy algorithm used for searching. The main drawback of the algorithm is poor (linear) scalability with the size of the dataset. Both algorithms offer high recall in return for evaluation of only a tiny portion of the dataset.

Kleinberg's work [\[9\]](#page-7-0) has shown the possibility of using navigable small world networks for finding the nearest neighbor with the greedy search algorithm. The algorithm relied on random long-range links following the power law of link length probability r <sup>γ</sup> , γ for navigation and 2-dimensional lattice for correctness of the results. To have navigable small world properties, the link length distribution has to have a specific value of γ. In Voronet [\[35\]](#page-7-0), Kleinberg's approach was extended to arbitrary 2 dimensional data by building a two-dimensional Delaunay tessellation instead of a regular lattice. In their next work [\[13\]](#page-7-0) they have weakened the requirements on the exactness of the search in order to avoid the curse of dimensionality for the d-dimension Euclidean space. The algorithm approximates the Delaunay graph by selecting 3dþ1 neighbors that minimize the volume of the corresponding Voronoi cell. The algorithm relies heavily on the quality of the Delaunay graph approximation, it has to be repeated iteratively to reach acceptable accuracy, and in principle works only in the Euclidean space. The work, together with the others [\[11](#page-7-0)–14], also presented some sophisticated algorithms for supporting the Kleinberg's power law link length distribution with a specific exponent value.

# 3. Core idea

The structure S is constructed as a navigable small world network represented by a graph GðV; EÞ, where objects from the set X are uniquely mapped to vertices from the set V. The set of edges E is determined by the structure construction algorithm. Since each vertex is uniquely mapped to an element from the set X, we will use the terms "vertex", "element" and "object" interchangeably. We will use the term "friends" for vertices that share an edge. The list of vertices that share a common edge with the vertex vi is called the friend list of the vertex vi.

We use a variation of the greedy search algorithm as a base algorithm for the k-NN search. It traverses the graph from an element to another element each time selecting an unvisited friend closest to the query until it reaches a stop condition. See a detailed description of the algorithms in [Section 4.2.](#page-3-0)

It is important to note that links (edges) in the graph serve two distinct purposes:

- 1) There is a subset of short-range links, which are used as an approximation of the Delaunay graph [\[7\]](#page-7-0) required by the greedy search algorithm.
- 2) Another subset is the long-range links, which are used for logarithmic scaling of the greedy search. Long-range links are responsible for the navigation small world properties of the constructed graph [\[9\]](#page-7-0).

![](_page_2_Figure_10.jpeg)

Fig. 1. Graph representation of the structure. Circles (vertices) are the data in metric space, black edges are the approximation of the Delaunay graph, and red edges are long range links for logarithmic scaling. Arrows show a sample path of the greedy algorithm from the entry point to the query (shown green). (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

The structure performance is illustrated in Fig. 1.

The construction of the structure is based on the consecutive insertion of all elements. For every new incoming element, we find the set of its closest neighbors (Delaunay graph approximation) from the structure. The set is connected to the element and vice versa. As more and more elements are inserted into the structure, links that previously served as short-range links now become long-range links (for details see [Section 5\)](#page-3-0) making a navigable small world. All queries in the structure are independent; they can be done in parallel, and if the elements are placed randomly on physical computer nodes, then the processing query load can be shared across physical nodes.

#### 4. Search algorithm

#### 4.1. Basic greedy search algorithm

The basic single nearest neighbor search algorithm traverses the edges of the graph GðV; EÞ from one vertex to another. The algorithm takes two parameters: query and the vertex Ventry\_point AV½G which is the starting point of a search (the entry point). Starting from the entry point, the algorithm computes a distance from the query q to each vertex from the friend list of the current vertex, and then selects a vertex with the minimal distance. If the distance between the query and the selected vertex is smaller than the one between the query and the current element, then the algorithm moves to the selected vertex, and it becomes new current vertex. The algorithm stops when it reaches a local minimum: a vertex whose friend list does not contain a vertex that is closer to the query than the vertex itself. The algorithm

```
Greedy_Search(q: object, ventry_point: object)
1 vcurr←ventry_point;
2 δmin←δ(q, vcurr); vnext←NIL;
3 foreach vfriendAvcurr.getFriends() do
4 δ fr←d (query, vfriend)
5 if δ froδ min then
6 δ min←δ fr;
7 vnext←vfriend;
8 if vnext¼NIL then return vcurr;
9 else return Greedy_Search(q, vnext);
```

The element which is a local minimum with respect to the query qAD can be either the true closest element to the <span id="page-3-0"></span>query q from all elements in the set X, or a false closest (an error).

If every element in the structure had in their friend list all of its Voronoi neighbors, then this would preclude the existence of false global minima. Maintaining this condition is equivalent to constructing the Delaunay graph, which is dual to the Voronoi diagram.

It turns out that it is impossible to determine exact Delaunay graph for an unknown metric space [\[8\]](#page-7-0) (excluding the variant of the complete graph), so we cannot avoid the existence of false global minima. For the problem of approximate search as defined above it is not an obstacle, since approximate search does not require the entire Delaunay graph [\[13\]](#page-7-0).

Note that there is a distinction from the ANN problem defined in the works [19–[23\]](#page-7-0) where it is expressed in terms of ε-neighborhood. Like in [\[24](#page-7-0)–31] in our structure there are no constrains on the absolute value of the distance between the algorithm NN results and true NN results. The result guaranties are probabilistic, meaning that only the probability of finding the true nearest neighbor is guaranteed. It may be more convenient to use such definition of the search effectiveness when the data distribution is highly skewed and it is hard to define one value ε for all regions at the same time.

#### 4.2. k-NN search modification

In our previous work [\[36\]](#page-7-0) we have used a simple algorithm for k-NN search based on a series of m searches and returns the best results of these. With each subsequent search, the probability of not finding the nearest neighbors decreases exponentially, allowing boosting the accuracy of the structure without the need for reconstruction.

In this work we present a more sophisticated version of the k-NN algorithm with two key modifications:

- 1) We use different stop condition. The algorithm iterates on not previously visited elements (i.e. those for which the link list has not been read) closest to the queries. It stops when at the next iteration, k closest results to the query do not change. Simply put, the algorithm keeps exploring the neighborhood of the closest elements in a greedy manner as long as it can improve the known k closest elements on each step.
- 2) The list of previously visited elements visitedSet is shared across the series of searches preventing useless repeated extractions.

```
K-NNSearch(object q, integer: m, k)
1 TreeSet [object] tempRes, candidates, visitedSet,
 result
2 for (i←0; iom; iþ þ) do:
3 put random entry point in candidates
4 tempRes←null
5 repeat:
6 get element c closest from candidates
      to q
7 remove c from candidates
8 //check stop condition:
9 if c is further than k-th element from result
```

```
10 than break repeat
11 //update list of candidates:
12 for every element e from friends of c do:
13 if e is not in visitedSet than
14 add e to visitedSet, candidates, tempRes
15
16 end repeat
17 //aggregate the results:
18 add objects from tempRes to result
19 end for
20 return best k elements from result
```

The use of TreeSet ordered lists allows storing evaluated elements in the order of proximity to the query, thus easily extracting closest elements from the set, which is required on steps 6, 9 and 20.

If m is big enough, the algorithm becomes an exhaustive search, assuming that entry points are never reused. If the graph of the network has the small-world property, then it is possible to choose a random vertex without any metric calculations in a number of random steps proportional to the logarithm of the dataset size, which does not yield the overall logarithmic search complexity.

#### 5. Data insertion algorithm

Since we build an approximation of the Delaunay graph, there is a great freedom in the details of the construction algorithm. The main goal is to minimize the probability of false global minima while keeping the number of links as small possible. Some approaches are based on knowledge of topology of the metric space being used. For example, in [\[13\]](#page-7-0) it is proposed to build an approximate Delaunay graph which would minimize the volume of a Voronoi region (computed by the Monte-Carlo method) for a fixed number of edges for each vertex in the graph (achieved by iterating a selection of neighbors of every node in the graph several times). We propose to assemble the structure by inserting elements one by one and connecting them on each step with the f closest objects which are already in the structure. Our approach is based on the idea that intersection of the set of elements which are Voronoi neighbors and the f closest elements should be large.

The graph can be constructed by sequential insertion of all elements. For every new coming element, we find the set of its closest neighbors (Delaunay graph approximation) from the structure. The set is connected to the element and vice versa. One of the advantages of this approach (already shown empirically for one-dimensional data [\[37\]\)](#page-7-0) is that a graph created by such algorithm with general metric data arriving in random order has small world navigation properties without any additional arrangements.

To determine the set of f closest elements, we use approximate kNN search algorithm (see Section 4.2). The algorithm takes three parameters: the object to be inserted in the structure, and two positive integer numbers: f (number of nearest neighbors to connect) and w (number of multi-searches).

First, the algorithm determines a set neighbors containing f local closest elements using the procedure <span id="page-4-0"></span>k-NNSearch (see Section 4.2). After that new\_object is connected to every object in a set and vice versa.

```
Nearest_Neighbor_Insert(object: new_object, integer:
   f, integer: w)
1   SET[object]: neighbors \( \times \) + NNSearch (new_object, w,
   f);
2   for (I \( \times 0 \); i \( < f; i + + ) \) do
3   neighbors [i].connect(new_object);
4   new_object.connect(neighbors [i]);</pre>
```

#### 5.1. Choice of parameters

The parameter w affects how accurate is determination (recall) of nearest neighbors in the construction algorithm [36]. Like in Section 4.2, setting w to a big number is equivalent to exhaustive search of the closest elements in the structure resulting in a perfect recall. The idea is to set w big enough to have the recall close to unity (e.g. 0.95-0.99). Smaller recall will create a fraction of wrong links which solely increase complexity of the algorithm, while our experiments indicate that increasing recall at insertion higher than 0.99 have no measurable effect on the search quality. Test have also shown that w for optimal recall changes slowly (logarithmically) with the dataset size, so if we already know the approximate wo for a good recall, we can run random query tests, firstly with much larger m (e.g. m=2\*w0+10), assuming that m is large enough for the results of the search to be true k nearest neighbors, and then increase w, repeating the tests until we have a high recall (e.g. 0.95-0.99). The complexity of the operation is logarithmic to the size of the dataset so it does not affect the overall construction complexity.

The tests indicate [36] that at least for Euclid data with d=1...20, the optimal value for number of neighbors to connect (£) is about 3d, making memory consumption linear with the dimensionality. Lesser values of £ can be used to reduce the complexity of a single search, sacrificing its recall quality.

### 6. Test results and discussion

#### 6.1. Test data

We have implemented the algorithms presented above in order to validate our assumptions about the scalability of the structure, and to evaluate its performance. In our tests we have used a workstation based on two Intel Xeon X5675 six core processors with 192 Gb of RAM. The algorithm was written in Java using the Oracle Java Platform.

We have used the following test datasets:

- Uniformly distributed random points with  $L_2$  (Euclidean distance) distance function (up to  $5 \times 10^7$  elements, up to 50 dimensions).
- A subset of the CoPHiR [38] dataset for comparison with other works. 208-dimensional feature vectors were extracted from the database. L<sub>1</sub>-metric was used as a distance function. 30 approximate nearest neighbors are found during a search.

![](_page_4_Figure_13.jpeg)

Fig. 2. The average hop count induced by a greedy search algorithm for different dimensionality Euclidean data (k=10, w=20). The navigable small world properties are evident from the logarithmic scaling.

#### 6.2. Small world navigation properties

To verify the small world navigation properties of the proposed structure, we have measured the average path length induced by the greedy search algorithm (see Section 4.1) for the points in different dimensionality Euclidean spaces (see Fig. 2). The values of f were set to 3d. The plot clearly shows logarithmic dependence of the greedy search path length on the dataset size, proving that the proposed structure is a navigable small world. Note that for bigger dimensionalities dependence is weaker. This is not due to different values of f (they do not affect the length of the path significantly), but possibly due shortening of the set's "topological diameter". When greedy algorithm encounters long range links, it selects the elements in the direction close to the query and disregards other directions, making the search quasi onedimensional.

The logarithmic complexity corrupts if we add elements that gradually expand the volume of the set (i.e. non-random insertion) or update the links of elements deleting links that do not connect to a one of the closest f elements. These facts allow concluding that the navigable small world feature of the graph is based on keeping longrange links of Delaunay approximation links, created in the beginning of construction.

## 6.3. Parallel and distributed operation

One of the key features of the proposed approach is that the structure is expressed in terms of independent objects connected only by links. The elements can be located on different computers sharing the load. A distributed prototype based on Apache Tomcat was developed. The communication between the servers was based on a client-server model. A client (which may be any server) performs the algorithm described in Section 4.2 with an exclusion of step 12 which requires getting link list from other servers. To improve the performance (but in expense of memory requirements) of the prototype the

link list of each element also contains a copy of the object for every link in the list. This allows saving about 6d data requests between the servers at each step of the algorithm

Our earlier tests for d=1 with on a 4-node computer cluster show that this approach leads to almost linear scalability of total throughput with the respect to the number of processing cores in the system. Future test are required to demonstrate the work of the distributed prototype for different data.

We have also performed experiments with parallel insertion of the elements. For d=10 the first 1000 elements in the database where inserted serially. After that the insertion was done by 16 parallel threads. In spite of the very small database size and potentially many assembling errors, we found no measurable decrease of search accuracy in the tests, allowing massive parallel construction without any additional synchronization means.

#### 6.4. k-Nearest neighbor search complexity scaling

Our primary quality measure is the **recall**: the ratio between relevant results and the objects obtained by the approximate search. We calculate recall by dividing the average number of true results within a search by k, the number of neighbors to find (so it ranges from zero to one). We also measure the fraction of visited elements to evaluate the complexity of search. This fraction is calculated by dividing the overall metric calculations during a single search by the total number of elements.

We have run tests on random Euclidean data with a fixed recall 0.999 for different dimensionalities (from 3 to 50). The fixed value of a search recall was controlled by adjusting the parameter  $\mathfrak{m}$ . Construction parameter  $\mathfrak{f}$  was set to 3d for all trials (optimum value for high recall) and  $\mathfrak{w}$  was updated to get high recall (0.99) of test data in the construction algorithm. We have used 20,000 random elements with different seed number as queries, and found  $\mathfrak{k}=10$  closest neighbors during the search. The plot on Fig. 3 presents the result in a log–log scale for different dimensionalities. It shows that with the increase of the number of elements in the structure, the percentage of

![](_page_5_Figure_8.jpeg)

**Fig. 3.** Average fraction of visited elements within a single 10-NN-search with 0.999 recall versus the size of the dataset for different dimensionality.

![](_page_5_Figure_10.jpeg)

**Fig. 4.** Distance calculations and the value of m to get a 0.999 recall versus the size of the dataset for d=20. The metric calculation count has  $C \log^2(n)$  complexity scaling.

![](_page_5_Figure_12.jpeg)

**Fig. 5.** Average fraction of visited elements within a single 10-NN-search with 0.999 recall for about 22 million elements dataset.

visited elements decreases, and the curves become close to straight lines (corresponding to power law of decay). This means that that for a fixed accuracy search complexity does not change significantly with the size of the dataset. The overall complexity of a fixed recall search together with the value m to get the desired recall is depicted in Fig. 4. The complexity scales as  $C \log^2(n)$ , just as it might be expected. One "log" comes from the average path length of the navigable small world (see Fig. 2), and the other comes from the number of multi-searches (Fig. 4).

#### 6.5. Dimensionality scaling

To test the dimensionality scaling we have plotted in Fig. 5 the average fraction of visited elements within a single 10-NN-search with 0.999 recall for about 22 million elements dataset versus dimensionality. A plateau with an "optimal" value of the dimensionality is clearly seen from the plot. The position of the "optimum" value of dimensionality slowly shifts with increasing dataset size, which may be attributed to shorter greedy paths at higher dimensionality (see Section 6.2).

#### 6.6. CoPHiR, comparison with other works

To get an idea about how the algorithm performs compared to previous k-NN algorithms, we have run a test from [\[25\],](#page-7-0) a 10 million entries subset of CoPHiR collection [\[38\]](#page-7-0). We have used the same L1 distance on 208 dimensional features extracted from xml documents. k¼30 nearest neighbors were found during a search. 100 thousands different (other) elements from the dataset were used as queries. Construction of the structure was done in parallel by 16 threads and took about 2 h.

Since for optimal f30–40 (effective dimensionality 10–13) the algorithm achieves high recall even at a single search, we have compared the recall error (one minus recall) instead of recall (see in Fig. 6 the recall error versus fraction of the visited elements in a logarithmic scale). The achieved results are even slightly better than the expected exponential decrease. Only 0.031% of the database needed to be evaluated to get 0.999 recall, which makes the search virtually exact. In terms of throughput, at m¼1 with recall

![](_page_6_Figure_5.jpeg)

Fig. 6. Average fraction of visited elements within a single k-NN-search vs recall error for 10 M 208 dimensional vectors from CoPHiR database. The inset shows logarithmic rise of distance calculations to get 0.999 recall (vertical) with the dataset size (horizontal).

![](_page_6_Figure_7.jpeg)

Fig. 7. Average fraction of visited elements within a single k-NN-search vs recall error for 10 million CoPHiR objects.

0.92 about 2800 searches per second can be done in parallel on our 12-core test system. The inset of the Fig. 6 shows logarithmic rise of number of evaluated elements for a single 0.999 recall search with the growth of the dataset size.

See the Fig. 7 for the comparison with the data for NAPP, with K¼7 the parameter [\[25\].](#page-7-0) Values of s in NAPP were selected to get best recall at fixed fraction of visited elements. Our algorithm is very effective at big dataset size, especially in case of high recall, requiring more that hundred time less metric computation at a recall of 0.999.

The comparison to Ordering Permutation index [\[34\]](#page-7-0) at low(10<sup>4</sup> ) number of points but high dimensionality (d¼1024), which means that the small world navigation properties do not play a critical role, showed that our algorithm yields in performance(about 65% database elements visited for our algorithm get 0.9 recall versus 42% for the OP).

#### 7. Conclusions and open problems

We have proposed a method of organizing data into a navigable small world graph structure suited for the distributed approximate k-nearest neighbor search in metric spaces. The algorithm uses no information about inner topology of the data and space (i.e. relying only on relative distances between the objects from a set and query), and thus in principle is applicable to arbitrary metric data. The search is approximate from the probabilistic point of view.

The algorithm is very simple and easy to understand. The navigable small world feature of the graph is due to keeping long-range links of Delaunay approximation links, created in the beginning of construction, it does not use the metric space structure. All elements in the structure are of the same type, there is no central or root element. The algorithm handles insertions the same way as queries, by finding approximate neighbors for the inserted element and connecting it to them. The algorithm uses only local information on each step and can be initiated from any vertex.

Accuracy of the approximate search can be raised by using multiple searches with a random initial vertex, and the recall error decreases exponentially with the number of visited elements. Very high recall (better than 0.999) can be obtained at low complexity, making our approach a strong rival for exact search structures. Both logarithmic search and construction complexity at fixed accuracy can be achieved, and they both can be done in parallel without special care. It is shown experimentally that the dimensionality dependence is weak for Euclidean data.

Comparison with other algorithms based on permutation indexes has shown that on a big dataset there are scenarios where the proposed approach can offer much higher efficiency (up to more than an order of magnitude at fixed recall) in the number of metric computations. Only 0.03% percent of the 10 million 208-dimensional CoPHiR dataset is needed to be evaluated to achieve 0.999 recall (virtually exact search). For recall 0.93 processing speed 2800 queries/s can achieved on a single server node.

<span id="page-7-0"></span>The proposed modified k-NN search algorithm provides very high efficiency and good scalability at large datasets. However, still there are several ways to optimize the structure in order to get lower complexity and/or better accuracy constants, such as

- More sophisticated algorithms for node friends selection (see [Section 5\)](#page-3-0). It is quite evident that selecting nearest neighbors as friends is not the best way to approximate Delaunay graph, since this approach takes into account only distances between the new element and candidates, and disregards distances between the candidates. Knowledge of internal structure of the metric space can boost search performance. In [13] is was shown that for Euclidean space the accuracy of a single search can be significantly increased while keeping the number of friends per node fixed.
- More sophisticated algorithms for navigable small world creation.
- More efficient management of multiple searches.

Even though the algorithm in principle can be applied for arbitrary metric spaces and its performance is shown experimentally in vector spaces and CoPHiR it is not clear what is the actual the range of applicability of the algorithm. Further investigations are required to clarify this point.

To sum up, simplicity, effectiveness, high scalability both in size and data dimensionality, and the distributed nature of the algorithm are a good base for building many real-world similarity search applications.

</details>

<details>
<summary>Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs</summary>

# Efficient and robust approximate nearest neighbor search using Hierarchical Navigable Small World graphs

Yu. A. Malkov, D. A. Yashunin

Abstract — We present a new approach for the approximate K-nearest neighbor search based on navigable small world graphs with controllable hierarchy (Hierarchical NSW, HNSW). The proposed solution is fully graph-based, without any need for additional search structures, which are typically used at the coarse search stage of the most proximity graph techniques. Hierarchical NSW incrementally builds a multi-layer structure consisting from hierarchical set of proximity graphs (layers) for nested subsets of the stored elements. The maximum layer in which an element is present is selected randomly with an exponentially decaying probability distribution. This allows producing graphs similar to the previously studied Navigable Small World (NSW) structures while additionally having the links separated by their characteristic distance scales. Starting search from the upper layer together with utilizing the scale separation boosts the performance compared to NSW and allows a logarithmic complexity scaling. Additional employment of a heuristic for selecting proximity graph neighbors significantly increases performance at high recall and in case of highly clustered data. Performance evaluation has demonstrated that the proposed general metric space search index is able to strongly outperform previous opensource state-of-the-art vector-only approaches. Similarity of the algorithm to the skip list structure allows straightforward balanced distributed implementation.

Index Terms — Graph and tree search strategies, Artificial Intelligence, Information Search and Retrieval, Information Storage and Retrieval, Information Technology and Systems, Search process, Graphs and networks, Data Structures, Nearest neighbor search, Big data, Approximate search, Similarity search

#### 1 Introduction

Constantly growing amount of the available information resources has led to high demand in scalable and efficient similarity search data structures. One of the generally used approaches for information search is the K-Nearest Neighbor Search (K-NNS). The K-NNS assumes you have a defined distance function between the data elements and aims at finding the K elements from the dataset which minimize the distance to a given query. Such algorithms are used in many applications, such as non-parametric machine learning algorithms, image features matching in large scale databases [1] and semantic document retrieval [2]. A naïve approach to K-NNS is to compute the distances between the query and every element in the dataset and select the elements with minimal distance. Unfortunately, the complexity of the naïve approach scales linearly with the number of stored elements making it infeasible for large-scale datasets. This has led to a high interest in development of fast and scalable K-NNS algorithms.

Exact solutions for K-NNS [3-5] may offer a substantial search speedup only in case of relatively low dimensional data due to "curse of dimensionality". To overcome this problem a concept of Approximate Nearest Neighbors Search (K-ANNS) was proposed, which relaxes the condition of the exact search by allowing a small number of

errors. The quality of an inexact search (the recall) is defined as the ratio between the number of found true nearest neighbors and *K*. The most popular K-ANNS solutions are based on approximated versions of tree algorithms [6, 7], locality-sensitive hashing (LSH) [8, 9] and product quantization (PQ) [10-17]. Proximity graph K-ANNS algorithms [10, 18-26] have recently gained popularity offering a better performance on high dimensional datasets. However, the power-law scaling of the proximity graph routing causes extreme performance degradation in case of low dimensional or clustered data.

In this paper we propose the Hierarchical Navigable Small World (Hierarchical NSW, HNSW), a new fully graph based incremental K-ANNS structure, which can offer a much better logarithmic complexity scaling. The main contributions are: explicit selection of the graph's enter-point node, separation of links by different scales and use of an advanced heuristic to select the neighbors. Alternatively, Hierarchical NSW algorithm can be seen as an extension of the probabilistic skip list structure [27] with proximity graphs instead of the linked lists. Performance evaluation has demonstrated that the proposed general metric space method is able to strongly outperform previous opensource state-of-the-art approaches suitable only for vector spaces.

Y. Malkov is with the Federal state budgetary institution of science Institute of Applied Physics of the Russian Academy of Sciences, 46 Ul'yanov Street, 603950 Nizhny Novgorod, Russia. E-mail: yurymalkov@mail.ru.

D. Yashunin. Addres: 31-33 ul. Krasnozvezdnaya, 603104 Nizhny Novgorod, Russia. E-mail: yashuninda@yandex.ru

#### 2 RELATED WORKS

# 2.1 Proximity graph techniques

In the vast majority of studied graph algorithms searching takes a form of greedy routing in k-Nearest Neighbor (k-NN) graphs [10, 18-26]. For a given proximity graph, we start the search at some enter point (it can be random or supplied by a separate algorithm) and iteratively traverse the graph. At each step of the traversal the algorithm examines the distances from a query to the neighbors of a current base node and then selects as the next base node the adjacent node that minimizes the distance, while constantly keeping track of the best discovered neighbors. The search is terminated when some stopping condition is met (e.g. the number of distance calculations). Links to the closest neighbors in a k-NN graph serve as a simple approximation of the Delaunay graph [25, 26] (a graph which guranties that the result of a basic greedy graph traversal is always the nearest neighbor). Unfortunately, Delaunay graph cannot be efficiently constructed without prior information about the structure of a space [4], but its approximation by the nearest neighbors can be done by using only distances between the stored elements. It was shown that proximity graph approaches with such approximation perform competitive to other k-ANNS thechniques, such as kd-trees or LSH [18-26].

The main drawbacks of the k-NN graph approaches are: 1) the power law scaling of the number of steps with the dataset size during the routing process [28, 29]; 2) a possible loss of global connectivity which leads to poor search results on clusetered data. To overcome these problems many hybrid approaches have been proposed that use auxiliary algorithms applicable only for vector data (such as kd-trees [18, 19] and product quantization [10]) to find better candidates for the enter nodes by doing a coarse search.

In [25, 26, 30] authors proposed a proximity graph K-ANNS algorithm called Navigable Small World (NSW, also known as Metricized Small World, MSW), which utilized navigable graphs, i.e. graphs with logarithmic or polylogarithmic scaling of the number of hops during the greedy traversal with the respect of the network size [31, 32]. The NSW graph is constructed via consecutive insertion of elements in random order by bidirectionally connecting them to the M closest neighbors from the previously inserted elements. The *M* closest neighbors are found using the structure's search procedure (a variant of a greedy search from multiple random enter nodes). Links to the closest neighbors of the elements inserted in the beginning of the construction later become bridges between the network hubs that keep the overall graph connectivity and allow the logarithmic scaling of the number of hops during greedy routing.

Construction phase of the NSW structure can be efficiently parallelized without global synchronization and without mesuarable effect on accuracy [26], being a good choice for distributed search systems. The NSW approach delivered the state-of-the-art performance on some datasets [33, 34], however, due to the overall polylogarithmic complexity scaling, the algorithm was still prone to

severe performance degradation on low dimensional datasets (on which NSW could lose to tree-based algorithms by several orders of magnitude [34]).

# 2.2 Navigable small world models

Networks with logarithmic or polylogarithmic scaling of the greedy graph routing are known as the navigable small world networks [31, 32]. Such networks are an important topic of complex network theory aiming at understanding of underlying mechanisms of real-life networks formation in order to apply them for applications of scalable routing [32, 35, 36] and distributed similarity search [25, 26, 30, 37-40].

The first works to consider spatial models of navigable networks were done by J. Kleinberg [31, 41] as social network models for the famous Milgram experiment [42]. Kleinberg studied a variant of random Watts-Strogatz networks [43], using a regular lattice graph in ddimensional vector space together with augmentation of long-range links following a specific long link length distribution  $r^{\alpha}$ . For  $\alpha$ =d the number of hops to get to the target by greedy routing scales polylogarithmically (instead of a power law for any other value of  $\alpha$ ). This idea has inspired development of many K-NNS and K-ANNS algorithms based on the navigation effect [37-40]. But even though the Kleinberg's navigability criterion in principle can be extended for more general spaces, in order to build such a navigable network one has to know the data distribution beforehand. In addition, greedy routing in Kleinberg's graphs suffers from polylogarithmic complexity scalability at best.

Another well-known class of navigable networks are the scale-free models [32, 35, 36], which can reproduce several features of real-life networks and advertised for routing applications [35]. However, networks produced by such models have even worse power law complexity scaling of the greedy search [44] and, just like the Kleinberg's model, scale-free models require global knowledge of the data distribution, making them unusable for search applications.

The above-described NSW algorithm uses a simpler, previously unknown model of navigable networks, allowing decentralized graph construction and suitable for data in arbitrary spaces. It was suggested [44] that the NSW network formation mechanism may be responsible for navigability of large-scale biological neural networks (presence of which is disputable): similar models were able to describe growth of small brain networks, while the model predicts several high-level features observed in large scale neural networks. However, the NSW model also suffers from the polylogarithmic search complexity of the routing process.

### **3 MOTIVATION**

The ways of improving the NSW search complexity can be identified through the analysis of the routing process, which was studied in detail in [32, 44]. The routing can be divided into two phases: "zoom-out" and "zoom-in" [32]. The greedy algorithm starts in the "zoom-out" phase

from a low degree node and traverses the graph simultaneously increasing the node's degree until the characteristic radius of the node links length reaches the scale of the distance to the query. Before the latter happens, the average degree of a node can stay relatively small, which leads to an increased probability of being stuck in a distant false local minimum.

One can avoid the described problem in NSW by starting the search from a node with the maximum degree (good candidates are the first nodes inserted in the NSW structure [44]), directly going to the "zoom-in" phase of the search. Tests show that setting hubs as starting points substantially increases probability of successful routing in the structure and provides significantly better performance at low dimensional data. However, it still has only a polylogarithmic complexity scalability of a single greedy search at best, and performs worse on high dimensional data compared to Hierarchical NSW.

The reason for the polylogarithmic complexity scaling of a single greedy search in NSW is that the overall number of distance computations is roughly proportional to a product of the average number of greedy algorithm hops by the average degree of the nodes on the greedy path. The average number of hops scales logarithmically [26, 44], while the average degree of the nodes on the greedy path also scales logarithmically due to the facts that: 1) the greedy search tends to go through the same hubs as the network grows [32, 44]; 2) the average number of hub connections grows logarithmically with an increase of the network size. Thus we get an overall polylogarithmic dependence of the resulting complexity.

The idea of Hierarchical NSW algorithm is to separate the links according to their length scale into different layers and then search in a multilayer graph. In this case we can evaluate only a needed fixed portion of the connections for each element independently of the networks size, thus allowing a logarithmic scalability. In such structure the search starts from the upper layer which has only

![](_page_2_Figure_5.jpeg)

Fig. 1. Illustration of the Hierarchical NSW idea. The search starts from an element from the top layer (shown red). Red arrows show direction of the greedy algorithm from the entry point to the query (shown green).

the longest links (the "zoom-in" phase). The algorithm greedily traverses through the elements from the upper layer until a local minimum is reached (see Fig. 1 for illustration). After that, the search switches to the lower layer (which has shorter links), restarts from the element which was the local minimum in the previous layer and the process repeats. The maximum number of connections per element in all layers can be made constant, thus allowing a logarithmic complexity scaling of routing in a navigable small world network.

One way to form such a layered structure is to explicitly set links with different length scales by introducing layers. For every element we select an integer level l which defines the maximum layer for which the element belongs to. For all elements in a layer a proximity graph (i.e. graph containing only "short" links that approximate Delaunay graph) is built incrementally. If we set an exponentially decaying probability of l (i.e. following a geometric distribution) we get a logarithmic scaling of the expected number of layers in the structure. The search procedure is an iterative greedy search starting from the top layer and finishing at the zero layer.

In case we merge connections from all layers, the structure becomes similar to the NSW graph (in this case the l can be put in correspondence to the node degree in NSW). In contrast to NSW, Hierarchical NSW construction algorithm does not require the elements to be shuffled before the insertion - the stochasticity is achieved by using level randomization, thus allowing truly incremental indexing even in case of temporarily alterating data distribution (though changing the order of the insertion slightly alters the performace due to only partially determenistic construction procedure).

The Hierarchical NSW idea is also very similar to a well-known 1D probabilistic skip list structure [27] and can be described using its terms. The major difference to skip list is that we generalize the structure by replacing the linked list with proximity graphs. The Hierarchical

![](_page_2_Figure_11.jpeg)

Fig. 2. Illustration of the heuristic used to select the graph neighbors for two isolated clusters. A new element is inserted on the boundary of Cluster 1. All of the closest neighbors of the element belong to the Cluster 1, thus missing the edges of Delaunay graph between the clusters. The heuristic, however, selects element *e<sup>2</sup>* from Cluster 2, thus, maintaining the global connectivity in case the inserted element is the closest to *e<sup>2</sup>* compared to any other element from Cluster 1.

NSW approach thus can utilize the same methods for making the distributed approximate search/overlay structures [45].

For the selection of the proximity graph connections during the element insertion we utilize a heuristic that takes into account the distances between the candidate elements to create diverse connections (a similar algorithm was utilized in the spatial approximation tree [4] to select the tree children) instead of just selecting the closest neighbors. The heuristic examines the candidates starting from the nearest (with respect to the inserted element) and creates a connection to a candidate only if it is closer to the base (inserted) element compared to any of the already connected candidates (see Section 4 for the details).

When the number of candidates is large enough the heuristic allows getting the exact relative neighborhood graph [46] as a subgraph, a minimal subgraph of the Delaunay graph deducible by using only the distances between the nodes. The relative neighborhood graph allows easily keeping the global connected component, even in case of highly clustered data (see Fig. 2 for illustration). Note that the heuristic creates extra edges compared to the exact relative neighborhood graphs, allowing controlling the number of the connections which is important for search performance. For the case of 1D data the heuristic allows getting the exact Delaunay subgraph (which in this case coincides with the relative neighborhood graph) by using only information about the distances between the elements, thus making a direct transition from Hierarchical NSW to the 1D probabilistic skip list algorithm.

Base variant of the Hierarchical NSW proximity graphs was also used in ref. [18] (called 'sparse neighborhood graphs') for proximity graph searching. Similar heuristic was also a focus of the FANNG algorithm [47]

#### Algorithm 1

INSERT(*hnsw, q*, *M*, *Mmax, efConstruction*, *mL*)

**Input**: multilayer graph *hnsw*, new element *q*, number of established connections *M*, maximum number of connections for each element per layer *Mmax*, size of the dynamic candidate list *efConstruction*, normalization factor for level generation *m<sup>L</sup>*

**Output**: update *hnsw* inserting element *q*

19 set enter point for *hnsw* to *q*

```
1 W ← ∅ // list for the currently found nearest elements
2 ep ← get enter point for hnsw
3 L ← level of ep // top layer for hnsw
4 l ← ⌊-ln(unif(0..1))∙mL⌋ // new element's level
5 for lc ← L … l+1
6 W ← SEARCH-LAYER(q, ep, ef=1, lc)
7 ep ← get the nearest element from W to q
8 for lc ← min(L, l) … 0
9 W ← SEARCH-LAYER(q, ep, efConstruction, lc)
10 neighbors ← SELECT-NEIGHBORS(q, W, M, lc) // alg. 3 or alg. 4
11 add bidirectionall connectionts from neighbors to q at layer lc
12 for each e ∈ neighbors // shrink connections if needed
13 eConn ← neighbourhood(e) at layer lc 
14 if │eConn│ > Mmax // shrink connections of e
 // if lc = 0 then Mmax = Mmax0
15 eNewConn ← SELECT-NEIGHBORS(e, eConn, Mmax, lc)
 // alg. 3 or alg. 4
16 set neighbourhood(e) at layer lc to eNewConn
17 ep ← W
18 if l > L
```

(published shortly after the first versions of the current manuscript were posted online) with a slightly different interpretation, based on the sparse neighborhood graph's property of the exact routing [18].

# **4 ALGORITHM DESCRIPTION**

Network construction algorithm (alg. 1) is organized via consecutive insertions of the stored elements into the graph structure. For every inserted element an integer maximum layer l is randomly selected with an exponentially decaying probability distribution (normalized by the <sup>m</sup><sup>L</sup> parameter, see line 4 in alg. 1).

The first phase of the insertion process starts from the top layer by greedily traversing the graph in order to find the ef closest neighbors to the inserted element q in the layer. After that, the algorithm continues the search from the next layer using the found closest neighbors from the previous layer as enter points, and the process repeats. Closest neighbors at each layer are found by a variant of the greedy search algorithm described in alg. 2, which is an updated version of the algorithm from [26]. To obtain the approximate ef nearest neighbors in some layer <sup>l</sup> *<sup>с</sup>* , a dynamic list W of ef closest found elements (initially filled with enter points) is kept during the search. The list is updated at each step by evaluating the neighborhood of the closest previously non-evaluated element in the list until the neighborhood of every element from the list is evaluated. Compared to limiting the number of distance calculations, Hierarchical NSW stop condition has an advantage - it allows discarding candidates for evalution that are further from the query than the furthest element in the list, thus avoiding bloating of search structures. As in NSW, the list is emulated via two priority queues for better performance. The distinctions from NSW (along with some queue optimizations) are: 1) the enter point is a fixed parameter; 2) instead of changing the number of multi-searches, the quality of the search is controlled by a different parameter ef (which was set to <sup>K</sup> in NSW [26]).

#### Algorithm 2

18 **return** *W*

```
SEARCH-LAYER(q, ep, ef, lc)
```

**Input**: query element *q*, enter points *ep*, number of nearest to *q* elements to return *ef*, layer number *l<sup>c</sup>*

```
Output: ef closest neighbors to q
1 v ← ep // set of visited elements
2 C ← ep // set of candidates
3 W ← ep // dynamic list of found nearest neighbors
4 while │C│ > 0
5 c ← extract nearest element from C to q
6 f ← get furthest element from W to q
7 if distance(c, q) > distance(f, q)
8 break // all elements in W are evaluated
9 for each e ∈ neighbourhood(c) at layer lc // update C and W
10 if e ∉ v
11 v ← v ⋃ e
12 f ← get furthest element from W to q
13 if distance(e, q) < distance(f, q) or │W│ < ef
14 C ← C ⋃ e
15 W ← W ⋃ e
16 if │W│ > ef
17 remove furthest element from W to q
```

#### **Algorithm 3**

SELECT-NEIGHBORS-SIMPLE(*q*, *C*, *M*)

**Input**: base element *q*, candidate elements *C*, number of neighbors to return *M*

**Output**: *M* nearest elements to *q* **return** *M* nearest elements from *C* to *q*

#### **Algorithm 5**

K-NN-SEARCH(*hnsw, q*, *K*, *ef*)

**Input**: multilayer graph *hnsw*, query element *q*, number of nearest neighbors to return *K,* size of the dynamic candidate list *ef*

**Output**: *K* nearest elements to *q*

1 *W* ← ∅ *//* set for the current nearest elements

2 *ep* ← get enter point for *hnsw*

*3 L* ← level of *ep //* top layer for *hnsw*

4 **for** *l<sup>c</sup>* ← *L* … 1

5 *W* ← SEARCH-LAYER(*q*, *ep*, *ef*=1, *lc*)

6 *ep* ← get nearest element from *W* to *q*

7 *W* ← SEARCH-LAYER(*q*, *ep*, *ef*, *l<sup>c</sup>* =0)

8 **return** *K* nearest elements from *W* to *q*

During the first phase of the search the ef parameter is set to 1 (simple greedy search) to avoid introduction of additional parameters.

When the search reaches the layer that is equal or less than l, the second phase of the construction algorithm is initiated. The second phase differs in two points: 1) the ef parameter is increased from 1 to efConstruction in order to control the recall of the greedy search procedure; 2) the found closest neighbors on each layer are also used as candidates for the connections of the inserted element.

Two methods for the selection of M neighbors from the candidates were considered: simple connection to the closest elements (alg. 3) and the heuristic that accounts for the distances between the candidate elements to create connections in diverse directions (alg. 4), described in the Section 3. The heuristic has two additional parameters: extendCandidates (set to false by default) which extends the candidate set and useful only for extremely clustered data, and keepPrunedConnections which allows getting fixed number of connection per element. The maximum number of connections that an element can have per layer is defined by the parameter Mmax for every layer higher than zero (a special parameter Mmax0 is used for the ground layer separately). If a node is already full at the moment of making of a new connection, then its extended connection list gets shrunk by the same algorithm that used for the neighbors selection (algs. 3 or 4).

The insertion procedure terminates when the connections of the inserted elements are established on the zero layer.

The K-ANNS search algorithm used in Hierarchical NSW is presented in alg. 5. It is roughly equivalent to the insertion algorithm for an item with layer l=0. The difference is that the closest neighbors found at the ground layer which are used as candidates for the connections are now returned as the search result. The quality of the search is controlled by the ef parameter (corresponding to efConstruction in the construction algorithm).

#### **Algorithm 4**

SELECT-NEIGHBORS-HEURISTIC(*q*, *C*, *M, lc, extendCandidates, keep-PrunedConnections*)

**Input**: base element *q*, candidate elements *C*, number of neighbors to return *M,* layer number *lc,* flag indicating whether or not to extend candidate list *extendCandidates*, flag indicating whether or not to add discarded elements *keepPrunedConnections*

**Output**: *M* elements selected by the heuristic

```
1 R ← ∅
```

2 *W* ← *C //* working queue for the candidates

3**if** *extendCandidates //* extend candidates by their neighbors

4 **for** each *e* ∈ *C*

5 **for** each *eadj* ∈ *neighbourhood*(*e*) *at layer l<sup>c</sup>*

6 **if** *eadj* ∉ *W*

7 *W* ← *W* ⋃ *eadj*

8 *W<sup>d</sup>* ← ∅ *//* queue for the discarded candidates

9 **while** │*W*│ *> 0* and │*R*│< *M*

10 *e* ← extract nearest element from *W* to *q*

11 **if** *e* is closer to *q* compared to any element from *R*

12 *R* ← *R* ⋃ *e*

13 **else**

14 *W<sup>d</sup>* ← *W<sup>d</sup>* ⋃ *e*

15 **if** *keepPrunedConnections //* add some of the discarded *//* connections from *W<sup>d</sup>*

16 **while** │*Wd*│*> 0 and* │*R*│< *M*

17 *R ← R* ⋃ extract nearest element from *W<sup>d</sup>* to *q*

18 **return** *R*

# **4.1 Influence of the construction parameters**

Algorithm construction parameters <sup>m</sup><sup>L</sup> and Mmax0 are responsible for maintaining the small world navigability in the constructed graphs. Setting <sup>m</sup><sup>L</sup> to zero (this corresponds to a single layer in the graph) and Mmax0 to M leads to production of directed k-NN graphs with a power-law search complexity well studied before [21, 29] (assuming using the alg. 3 for neighbor selection). Setting <sup>m</sup><sup>L</sup> to zero and Mmax0 to infinity leads to production of NSW graphs with polylogarithmic complexity [25, 26]. Finally, setting <sup>m</sup><sup>L</sup> to some non-zero value leads to emergence of controllable hierarchy graphs which allow logarithmic search complexity by introduction of layers (see the Section 3).

To achieve the optimum performance advantage of the controllable hierarchy, the overlap between neighbors on different layers (i.e. percent of element neighbors that are also belong to other layers) has to be small. In order to decrease the overlap we need to decrease the <sup>m</sup><sup>L</sup> . However, at the same time, decreasing <sup>m</sup><sup>L</sup> leads to an increase of average hop number during a greedy search on each layer, which negatively affects the performance. This leads to existence of the optimal value for the <sup>m</sup><sup>L</sup> parameter.

A simple choice for the optimal <sup>m</sup><sup>L</sup> is 1/ln(M), this corresponds to the skip list parameter p=1/M with an average single element overlap between the layers. Simulations done on an Intel Core i7 5930K CPU show that the proposed selection of <sup>m</sup><sup>L</sup> is a reasonable choice (see Fig. 3 for data on 10M random d=4 vectors). In addition, the plot demonstrates a massive speedup on low dimensional data when increasing the <sup>m</sup><sup>L</sup> from zero and the effect of using the heuristic for selection of the graph connections. It is hard to expect the same behavior for high dimensional data since in this case the k-NN graph already has

![](_page_5_Figure_2.jpeg)

Fig. 3. Plots for query time vs  $m_L$  parameter for 10M random vectors with d=4. The autoselected value  $1/\ln(M)$  for  $m_L$  is shown by an arrow

![](_page_5_Figure_4.jpeg)

Fig. 4. Plots for query time vs  $m_L$  parameter for 100k random vectors with d=1024. The autoselected value  $1/\ln(M)$  for  $m_L$  is shown by an arrow.

![](_page_5_Figure_6.jpeg)

Fig. 5. Plots for query time vs  $m_L$  parameter for 5M SIFT learn dataset. The autoselected value  $1/\ln(M)$  for  $m_L$  is shown by an arrow.

very short greedy algorithm paths [28]. Surprisingly, increasing the  $m_L$  from zero leads to a measurable increase in speed on very high dimensional data (100k dense random d=1024 vectors, see plot in Fig. 4), and does not introduce any penalty for the Hierarchical NSW approach. For real data such as SIFT vectors [1] (which have complex mixed structure), the performance improvement by increasing the  $m_L$  is higher, but less prominent at current settings compared to improvement from the heuristic (see Fig. 5 for 1-NN search performance on 5 million 128-dimensional SIFT vectors from the learning set of BIGANN [13]).

Selection of the  $M_{max0}$  (the maximum number of connections that an element can have in the zero layer) also has a strong influence on the search performance, especially in case of high quality (high recall) search. Simulations show that setting  $M_{max0}$  to M (this corresponds to k-NN graphs on each layer if the neighbors selection heuristic is not used) leads to a very strong performance penalty at high recall. Simulations also suggest that  $2 \cdot M$  is a good choice for  $M_{max0}$ ; setting the parameter higher leads to performance degradation and excessive memory usage. In Fig. 6 there are presented results of search performance for the 5M SIFT learn dataset depending on the  $M_{max0}$  parameter (done on an Intel Core i5 2400 CPU). The suggested value gives performance close to optimal at different recalls.

In all of the considered cases, use of the heuristic for proximity graph neighbors selection (alg. 4) leads to a higher or similar search performance compared to the

naïve connection to the nearest neighbors (alg. 3). The effect is the most prominent for low dimensional data, at high recall for mid-dimensional data and for the case of highly clustered data (ideologically discontinuity can be regarded as a local low dimensional feature), see the comparison in Fig. 7 (Core i5 2400 CPU). When using the closest neighbors as connections for the proximity graph, the Hierarchical NSW algorithm fails to achieve a high recall for clustered data because the search stucks at the clusters boundaries. Contrary, when the heuristic is used (together with candidates' extension, line 3 in Alg. 4), clustering leads to even higher performance. For uniform and very high dimensional data there is a little difference between the neighbors selecting methods (see Fig. 4), possibly due to the fact that in this case almost all of the nearest neighbors are selected by the heuristic.

The only meaningful construction parameter left for the user is M. A reasonable range of M is from 5 to 48. Simulations show that smaller M generally produces better results for lower recalls and/or lower dimensional data, while bigger M is better for high recall and/or high dimensional data (see Fig. 8 for illustration, Core i5 2400 CPU). The parameter also defines the memory consumption of the algorithm (which is proportional to M), so it should be selected with care.

Selection of the *efConstruction* parameter is straightforward. As it was suggested in [26] it has to be large enough to produce K-ANNS recall close to unity during the construction process (0.95 is enough for the most usecases). And just like in [26], this parameter can possibly

![](_page_5_Figure_14.jpeg)

Fig. 6. Plots for query time vs  $M_{max0}$  parameter for 5M SIFT learn dataset. The autoselected value  $2 \cdot M$  for  $M_{max0}$  is shown by an arrow.

![](_page_5_Figure_16.jpeg)

Fig. 7. Effect of the method of neighbor selections (baseline corresponds to alg. 3, heuristic to alg. 4) on clustered (100 random isolated clusters) and non-clustered d=10 random vector data.

![](_page_5_Figure_18.jpeg)

Fig. 8. Plots for recall error vs query time for different parameters of *M* for Hierarchical NSW on 5M SIFT learn dataset.

![](_page_6_Figure_1.jpeg)

Fig. 9. Construction time for Hierarchical NSW on 10M SIFT dataset for different numbers of threads on two CPUs.

![](_page_6_Figure_3.jpeg)

Fig. 10. Plots of the query time vs construction time tradeoff for Hierarchical NSW on 10M SIFT dataset.

![](_page_6_Figure_5.jpeg)

Fig. 11. Plots of the *ef* parameter required to get fixed accuracies vs the dataset size for d=4 random vector data.

be auto-configured by using sample data.

The construction process can be easily and efficiently parallelized with only few synchronization points (as demonstrated in Fig. 9) and no measurable effect on index quality. Construction speed/index quality tradeoff is controlled via the *efConstruction* parameter. The tradeoff between the search time and the index construction time is presented in Fig. 10 for a 10M SIFT dataset and shows that a reasonable quality index can be constructed for *efConstruction*=100 on a 4X 2.4 GHz 10-core Xeon E5-4650 v2 CPU server in just 3 minutes. Further increase of the *efConstruction* leads to little extra performance but in exchange of significantly longer construction time.

# 4.2 Complexity analysis

# 4.2.1 Search complexity

The complexity scaling of a single search can be strictly analyzed under the assumption that we build exact Delaunay graphs instead of the approximate ones. Suppose we have found the closest element on some layer (this is guaranteed by having the Delaunay graph) and then descended to the next layer. One can show that the average number of steps before we find the closest element in the layer is bounded by a constant.

Indeed, the layers are not correlated with the spatial positions of the data elements and, thus, when we traverse the graph there is a fixed probability  $p=\exp(-m_L)$  that the next node belongs to the upper layer. However, the search on the layer always terminates before it reaches the element which belongs to the higher layer (otherwise the search on the upper layer would have stopped on a different element), so the probability of not reaching the target on s-th step is bounded by  $\exp(-s \cdot m_L)$ . Thus the expected number of steps in a layer is bounded by a sum of geometric progression  $S=1/(1-\exp(-m_L))$ , which is independent of the dataset size.

If we assume that the average degree of a node in the Delaunay graph is capped by a constant C in the limit of the large dataset (this is the case for random Euclid data [48], but can be in principle violated in exotic spaces), then the overall average number of distance evaluations in a layer is bounded by a constant  $C \cdot S$ , independently of the dataset size.

And since the expectation of the maximum layer index

by the construction scales as  $O(\log(N))$ , the overall complexity scaling is  $O(\log(N))$ , in agreement with the simulations on low dimensional datasets.

The inital assumption of having the exact Delaunay graph violates in Hierarchical NSW due to usage of approximate edge selection heuristic with a fixed number of neighbors per element. Thus, to avoid stucking into a local minimum the greedy search algorithm employs a backtracking procedure on the zero layer. Simulations show that at least for low dimensional data (Fig. 11, d=4) the dependence of the required *ef* parameter (which determines the complexity via the minimal number of hops during the backtracking) to get a fixed recall saturates with the rise of the dataset size. The backtracking complexity is an additive term in respect to the final complexity, thus, as follows from the empirical data, inaccuracies of the Delaunay graph approximation do not alter the scaling.

Such empirical investigation of the Delaunay graph approximation resilience requires having the average number of Delaunay graph edges independent of the dataset to evidence how well the edges are approximated with a constant number of connections in Hierarchical NSW. However, the average degree of Delaunay graph scales exponentially with the dimensionality [39]), thus for high dimensional data (e.g. d=128) the aforementioned condition requires having extremely large datasets, making such empricial investigation unfeasible. Further analitical evidence is required to confirm whether the resilience of Delaunay graph aproximations generalizes to higher dimensional spaces.

# 4.2.2 Construction complexity

The construction is done by iterative insertions of all elements, while the insertion of an element is merely a sequence of K-ANN-searches at different layers with a subsequent use of heuristic (which has fixed complexity at fixed *efConstruction*). The average number of layers for an element to be added in is a constant that depends on  $m_i$ :

$$E[l+1] = E[-\ln(unif(0,1)) \cdot m_L] + 1 = m_L + 1 \tag{1}$$

Thus, the insertion complexiy scaling is the same as the one for the search, meaning that at least for relatively low dimensional datasets the construction time scales as  $O(N \log(N))$ .

#### 4.2.3 Memory cost

The memory consumption of the Hierarchical NSW is mostly defined by the storage of graph connections. The number of connections per element is  $M_{max,0}$  for the zero layer and  $M_{max}$  for all other layers. Thus, the average memory consumption element per  $(M_{max0}+m_L\cdot M_{max})\cdot bytes\_per\_link$ . If we limit the maximum total number of elements by approximately four billions, we can use four-byte unsigned integers to store the connections. Tests suggest that typical close to optimal M values usually lie in a range between 6 and 48. This means that the typical memory requirements for the index (excluding the size of the data) are about 60-450 bytes per object, which is in a good agreement with the simulations.

#### **5 Performance Evaluation**

The Hierarchical NSW algorithm was implemented in C++ on top of the Non Metric Space Library (nmslib) [49]<sup>1</sup>, which already had a functional NSW implementation (under name "sw-graph"). Due to several limitations posed by the library, to achieve a better performance, the Hierarchical NSW implementation uses custom distance functions together with C-style memory management, which avoids unnecessary implicit addressing and allows efficient hardware and software prefetching during the graph traversal.

Comparing the performance of K-ANNS algorithms is a nontrivial task since the state-of-the-art is constantly changing as new algorithms and implementations are emerging. In this work we concentrated on comparison with the best algorithms in Euclid spaces that have open source implementations. An implementation of the Hierarchical NSW algorithm presented in this paper is also distributed as a part of the open source nmslib library¹ together with an external C++ memory-efficient header-only version with support for incremental index construction².

The comparison section consists of four parts: comparison to the baseline NSW (5.1), comparison to the state-of-the-art algorithms in Euclid spaces (5.2), rerun of the sub-

set of tests [34] in general metric spaces in which NSW failed (5.3) and comparison to state-of-the-art PQ-algorithms on a large 200M SIFT dataset (5.4).

### 5.1 Comparison with baseline NSW

For the baseline NSW algorithm implementation, we used the "sw-graph" from nmslib 1.1 (which is slightly updated compared to the implementation tested in [33, 34]) to demonstrate the improvements in speed and algorithmic complexity (measured by the number of distance computations).

Fig. 12(a) presents a comparison of Hierarchical NSW to the basic NSW algorithm for d=4 random hypercube data made on a Core i5 2400 CPU (10-NN search). Hierarchical NSW uses much less distance computations during a search on the dataset, especially at high recalls.

The scalings of the algorithms on a d=8 random hypercube dataset for a 10-NN search with a fixed recall of 0.95 are presented in Fig. 12(b). It clearly demostrates that Hierarchical NSW has a complexity scaling for this setting not worse than logarithmic and outperforms NSW at any dataset size. The performance advantage in absolute time (Fig. 12(c)) is even higher due to improved algorithm implementaion.

#### 5.2 Comparison in Euclid spaces

The main part of the comparison was carried out on vector datasets with use of the popular K-ANNS benchmark ann-benchmark<sup>3</sup> as a testbed. The testing system utilizes python bindings of the algorithms – it consequentially runs the K-ANN search for one thousand queries (randomly extracted from the initial dataset) with preset algorithm parameters producing an output containing recall and average time of a single search. The considered algorithms are:

- 1. Baseline NSW algorithm from nmslib 1.1 ("sw-graph").
- 2. FLANN 1.8.4 [6]. A popular library<sup>4</sup> containing several algorithms, built-in in OpenCV<sup>5</sup>. We used the available auto-tuning procedure with several reruns to infer the best parameters.
- 3. Annoy6, 02.02.2016 build. A popular algorithm

![](_page_7_Figure_18.jpeg)

Fig. 12. Comparison between NSW and Hierarchical NSW: (a) distance calculation number vs accuracy tradeoff for a 10 million 4-dimensional random vectors dataset; (b-c) performance scaling in terms of number of distance calculations (b) and raw query(c) time on a 8-dimensional random vectors dataset.

<sup>1</sup> https://github.com/searchivarius/nmslib

<sup>&</sup>lt;sup>2</sup> https://github.com/nmslib/hnsw

<sup>&</sup>lt;sup>3</sup> https://github.com/erikbern/ann-benchmarks

<sup>&</sup>lt;sup>4</sup> https://github.com/mariusmuja/flann <sup>5</sup> https://github.com/opencv/opencv

<sup>6</sup> https://github.com/spotify/annoy

TABLE 1 Parameters of the used datasets on vector spaces benchmark.

| Dataset | Description                                       | Size     | d   | BF time Space |        |
|---------|---------------------------------------------------|----------|-----|---------------|--------|
| SIFT    | Image feature vectors [13]                        | 1M       | 128 | 94 ms         | L2     |
| GloVe   | Word embeddings trained on tweets [52]            | 1.2M 100 |     | 95 ms         | cosine |
| CoPhIR  | MPEG-7 features extracted from the images [53] 2M |          | 272 | 370 ms        | L2     |
|         | Random vectors Random vectors in hypercube        | 30M      | 4   | 590 ms        | L2     |
| DEEP    | One million subset of the billion deep image      | 1M       | 96  | 60 ms         | L2     |
|         | features dataset [14]                             |          |     |               |        |
| MNIST   | Handwritten digit images [54]                     | 60k      | 784 | 22 ms         | L2     |

based on random projection tree forest.

- 4. VP-tree. A general metric space algorithm with metric pruning [50] implemented as a part of nmslib 1.1.
- 5. FALCONN<sup>7</sup> , version 1.2. A new efficient LSH algorithm for cosine similarity data [51].

The comparison was done on a 4X Xeon E5-4650 v2 Debian OS system with 128 Gb of RAM. For every algorithm we carefully chose the best results at every recall range to evaluate the best possible performance (with initial values from the testbed defaults). All tests were done in a single thread regime. Hierarchical NSW was compiled using the GCC 5.3 with -Ofast optimization flag.

The parameters and description of the used datasets are outlined in Table 1. For all of the datasets except GloVe we used the L<sup>2</sup> distance. For GloVe we used the cosine similarity which is equivalent to L<sup>2</sup> after vector normalization. The brute-force (BF) time is measured by the nmslib library.

Results for the vector data are presented in Fig. 13. For SIFT, GloVE, DEEP and CoPhIR datasets Hierarchical NSW clearly outperforms the rivals by a large margin. For low dimensional data (d=4) Hierarchical NSW is

TABLE 2. Used datasets for repetition of the Non-Metric data tests subset.

| Dataset     | Description                                                                                                    | Size | d   |            | BF time Distance                      |  |
|-------------|----------------------------------------------------------------------------------------------------------------|------|-----|------------|---------------------------------------|--|
| Wiki-sparse | TF-IDF (term frequency–inverse document<br>frequency) vectors (created via GENSIM [58])                        | 4M   | 105 | 5.9 s      | Sparse cosine                         |  |
| Wiki-8      | Topic histograms created from sparse TF-IDF<br>vectors of the wiki-sparse dataset (created via<br>GENSIM [58]) | 2M   | 8   | -          | Jensen–<br>Shannon (JS)<br>divergence |  |
| Wiki-128    | Topic histograms created from sparse TF-IDF<br>vectors of the wiki-sparse dataset (created via<br>GENSIM [58]) | 2M   |     | 128 1.17 s | Jensen–<br>Shannon (JS)<br>divergence |  |
| ImageNet    | Signatures extracted from LSVRC-2014 with<br>SQFD (signature quadratic form) distance [59]                     | 1M   |     | 272 18.3 s | SQFD                                  |  |
| DNA         | DNA (deoxyribonucleic acid) dataset sampled<br>from the Human Genome 5 [34].                                   | 1M   | -   | 2.4 s      | Levenshtein                           |  |

slightly faster at high recall compared to the Annoy while strongly outperforms the other algorithms.

# **5.3 Comparison in general spaces**

A recent comparison of algorithms [34] in general spaces (i.e. non-symmetric or with violation of triangle inequality) showed that the baseline NSW algorithm has severe problems on low dimensional datasets. To test the performance of the Hierarchical NSW algorithm we have repeated a subset of tests from [34] on which NSW performed poorly or suboptimal. For that purpose we used a built-in nmslib testing system which had scripts to run tests from [34]. The evaluated algorithms included the VP-tree, permutation techniques (NAPP and bruteforce filtering) [49, 55-57], the basic NSW algorithm and NNDescent-produced proximity graphs [29] (both in pair with the NSW graph search algorithm). As in the original tests, for every dataset the test includes the results of either NSW or NNDescent, depending on which structure performed better. No custom distance functions or special

![](_page_8_Figure_14.jpeg)

Fig. 13. Results of the comparison of Hierarchical NSW with open source implementations of K-ANNS algorithms on five datasets for 10- NN searches. The time of a brute-force search is denoted as the BF.

<sup>7</sup> <https://github.com/FALCONN-LIB/FALCONN>

![](_page_9_Figure_2.jpeg)

Fig. 14. Results of the comparison of Hierarchical NSW with general space K-ANNS algorithms from the Non Metric Space Library on five datasets for 10-NN searches. The time of a brute-force search is denoted as the BF.

TABLE 3.

Parameters for comparison between Hierarchical NSW and Faiss on a 200M subset of 1B SIFT dataset.

| Algorithm        | Build time | Peak memory (runtime) | Parameters                   |
|------------------|------------|-----------------------|------------------------------|
| Hierarchical NSW | 5.6 hours  | 64 Gb                 | M=16, efConstruction=500 (1) |
| Hierarchical NSW | 42 minutes | 64 Gb                 | M=16, efConstruction=40 (2)  |
| Faiss            | 12 hours   | 30 Gb                 | OPQ64, IMI2x14, PQ64 (1)     |
| Faiss            | 11 hours   | 23.5 Gb               | OPQ32, IMI2x14, PQ32 (2)     |

memory management were used in this case for Hierarchical NSW leading to some performance loss.

The datasets are summarized in Table 2. Further details of the datasets, spaces and algorithm parameter selection can be found in the original work [34]. The bruteforce (BF) time is measured by the nmslib library.

The results are presented in Fig. 14. Hierarchical NSW significantly improves the performance of NSW and is a leader for any of the tested datasets. The strongest enhancement over NSW, almost by 3 orders of magnitude is observed for the dataset with the lowest dimensionality, the wiki-8 with JS-divergence. This is an important result that demonstrates the robustness of Hierarchical NSW, as for the original NSW this dataset was a stumbling block. Note that for the wiki-8 to nullify the effect of implementation results are presented for the distance computations number instead of the CPU time.

# 5.4 Comparison with product quantization based algorithms.

Product quantization K-ANNS algorithms [10-17] are considered as the state-of-the-art on billion scale datasets since they can efficiently compress stored data, allowing modest RAM usage while achieving millisecond search times on modern CPUs.

To compare the performance of Hierarchical NSW

![](_page_9_Figure_12.jpeg)

Fig. 15 Results of comparison with Faiss library on the 200M SIFT dataset from [13]. The inset shows the scaling of the query time vs the dataset size for Hierarchical NSW.

against PQ algorithms we used the facebook Faiss library<sup>8</sup> as the baseline (a new library with state-of-the-art PQ algorithms [12, 15] implementations, released after the current manuscript was submitted) compiled with the OpenBLAS backend. The tests where done for a 200M subset of 1B SIFT dataset [13] on a 4X Xeon E5-4650 v2 server with 128Gb of RAM. The ann-benchmark testbed was not feasible for these experiments because of its reliance on 32-bit floating point format (requiring more than 100 Gb just to store the data). To get the results for Faiss PQ algorithms we have utilized built-in scripts with the parameters from Faiss wiki<sup>9</sup>. For the Hierarchical NSW algorithm we used a special build outside of the nmslib with a small memory footprint, simple non-vectorized

<sup>8</sup> https://github.com/facebookresearch/faiss 2017 May build. From 2018 Faiss library has its own implementation of Hierarchical NSW.

https://github.com/facebookresearch/faiss/wiki/Indexing-1G-vectors

integer distance functions and support for incremental index construction<sup>10</sup> .

The results are presented in Fig. 15 with summarization of the parameters in Table 3. The peak memory consumption was measured by using linux "time –v" tool in separate test runs after index construction for both of the algorithms. Even though Hierarchical NSW requires significantly more RAM, it can achieve much higher accuracy, while offering a massive advance in search speed and much faster index construction.

The inset in Fig. 15 presents the scaling of the query time vs the dataset size for Hierarchical NSW. Note that the scaling deviates from the pure logarithm, possibly due to relatively high dimensionality of the dataset.

# **6 DISCUSSION**

By using structure decomposition of navigable small world graphs together with the smart neighbor selection heuristic the proposed Hierarchical NSW approach overcomes several important problems of the basic NSW structure advancing the state-of–the-art in K-ANN search. Hierarchical NSW offers an excellent performance and is a clear leader on a large variety of the datasets, surpassing the opensource rivals by a large margin in case of high dimensional data. Even for the datasets where the previous algorithm (NSW) has lost by orders of magnitude, Hierarchical NSW was able to come first. Hierarchical NSW supports continuous incremental indexing and can also be used as an efficient method for getting approximations of the k-NN and relative neighborhood graphs, which are byproducts of the index construction.

Robustness of the approach is a strong feature which makes it very attractive for practical applications. The algorithm is applicable in generalized metric spaces performing the best on any of the datasets tested in this paper, and thus eliminating the need for complicated selection of the best algorithm for a specific problem. We stress the importance of the algorithm's robustness since the data may have a complex structure with different effective dimensionality across the scales. For instance, a dataset can consist of points lying on a curve that randomly fills a high dimensional cube, thus being high dimensional at large scale and low dimensional at small scale. In order to perform efficient search in such datasets an approximate nearest neighbor algorithm has to work well for both cases of high and low dimensionality.

There are several ways to further increase the efficiency and applicability of the Hierarchical NSW approach. There is still one meaningful parameter left which strongly affects the construction of the index – the number of added connections per layer M. Potentially, this parameter can be inferred directly by using different heuristics [4]. It would also be interesting to compare Hierarchical NSW on the full 1B SIFT and 1B DEEP datasets [10-14] and add support for element updates and removal.

One of the apparent shortcomings of the proposed ap-

proach compared to the basic NSW is the loss of the possibility of distributed search. The search in the Hierarchical NSW structure always starts from the top layer, thus the structure cannot be made distributed by using the same techniques as described in [26] due to cognestion of the higher layer elements. Simple workarounds can be used to distribute the structure, such as partitioning the data across cluster nodes studied in [6], however in this case, the total parallel throughput of the system does not scale well with the number of computer nodes.

Still, there are other possible known ways to make this particular structure distributed. Hierarchical NSW is ideologically very similar to the well-known onedimensional exact search probabilistic skip list structure, and thus can use the same techniques to make the structure distributed [45]. Potentially this can lead to even better distributed performance compared to the base NSW due to logarithmic scalability and ideally uniform load on the nodes.

</details>

<details>
<summary>**Growing homophilic networks are natural navigable small worlds**</summary>

# **Growing homophilic networks are natural navigable small worlds**

Yury A. Malkov<sup>1</sup> , Alexander Ponomarenko<sup>2</sup>

- 1. Federal state budgetary institution of science Institute of Applied Physics of the Russian Academy of Sciences, 46 Ul'yanov Street, 603950 Nizhny Novgorod, Russia
- 2. National Research University Higher School of Economics, Nizhny Novgorod, Russia

Correspondence: yurymalkov@mail.ru

**Abstract.** Navigability, an ability to find a logarithmically short path between elements using only local information, is one of the most fascinating properties of real-life networks. However, the exact mechanism responsible for the formation of navigation properties remained unknown. We show that navigability can be achieved by using only two ingredients present in the majority of networks: network growth and local homophily, giving a persuasive answer how the navigation appears in real-life networks. A very simple algorithm produces hierarchical self-similar optimally wired navigable small world networks with exponential degree distribution by using only local information. Adding preferential attachment produces a scale-free network which has shorter greedy paths, but worse (power law) scaling of the information extraction locality (algorithmic complexity of a search). Introducing saturation of the preferential attachment leads to truncated scale-free degree distribution that offers a good tradeoff between these parameters and can be useful for practical applications. Several features of the model are observed in real-life networks, in particular in the brain neural networks, supporting the earlier suggestions that they are navigable.

## **Introduction**

Large scale networks are ubiquitous in many domains of science and technology. They influence numerous aspects of daily human life, and their importance is rising with the advances in the information technology. Even human's ability to think is governed by a large-scale brain network containing more than 100 billion neurons[1]. One of the most fascinating features found in the real-life networks is the navigability, an ability to find a logarithmically short path between two arbitrary nodes using only local information, without global knowledge of the network.

In the late 1960's Stanley Milgram and his collaborators conducted a series of experiments in which individuals from the USA were asked to get letters delivered to an unknown recipient in Boston[2]. Participants forwarded the letter to an acquaintance that was more likely to know the target. As a result about 20% of the letters arrived to the target on the average in less than six hops. In addition to revealing the existence of short paths in real-world acquaintance networks, the small-world experiments showed that these networks are navigable: a short path was discovered through using only local information. Later, the navigation feature was discovered in other types of networks[3]. The first algorithmic navigation model with a local greedy routing was proposed by J. Kleinberg[4, 5], inspiring many other studies and applications of the effect (see the recent review in [3]). However, the exact mechanism that is responsible for formation of navigation properties in real-life networks remained unknown. It was recently suggested that the navigation properties can rise due to various optimization schemes, such as optimization of network's entropy[6], optimization of network transport[7-11], game theory models[12, 13] or due to internal hyperbolicity of a hidden metric space[14]. In [15] a realistic model based on random heterogeneous networks was proposed to describe navigation processes in real networks. Authors argued that to achieve a high probability of successful routing in the large network limit the network has to have a scale-free degree distribution with <2.5. Later, hyperbolicity of hidden metric space was proposed as a possible reason of forming such navigable structures in real-life networks [13, 14, 16]. However it is unclear whether hyperbolicity and other aforementioned complex schemes are related to processes in real-life networks. In this work we show that the navigation property can be directly achieved by using only two ingredients that are present in the majority of reallife networks: network growth and local homophily[17], giving a simple and persuasive answer to the question of the nature of navigability in real-life systems.

One of the natural byproducts of the navigation studies is emergence of new efficient algorithms for distributed data similarity search (namely, the K-Nearest Neighbor Search, K-NN) which is a keen problem for many applications[18]. Several network structures inspired by the Kleinberg's idea were proposed[19-21]; their realization, however, was far from practical applications. In refs. [22-24] an efficient approximate KNN algorithm was introduced for general metric data utilizing incremental insertion and connection of newcoming elements to their closest neighbors in order to construct a navigable small world graph. By simulations the authors show that the algorithm can produce networks with short greedy paths and achieves a polylogarithmic complexity for both search and insertion firmly outperforming rival algorithms for a wide selection of datasets[24-26]. However, the scope of the works[22-24] was limited to the approximate nearest neighbors problem.

Based on these ideas we propose Growing Homophilic (GH) networks as the origin of small world navigation in real-life systems. We analyze the network properties using simulations and theoretical consideration, confirming navigation properties and demonstrating that the scale-free navigation models[15, 27] considered earlier are not truly local in terms of information extraction locality (algorithmic complexity of a search), while the proposed model is. We also show that the GH network features can be found in real-life networks, with an emphasis on functional brain networks.

Functional brain networks are studied in vivo using MRI techniques[28] and are usually modeled by generalizations of random models[29-31] requiring global network knowledge. It was suggested that the brain networks are navigable through utilizing the rich club (a densely interconnected high degree subgraph[32]) and that the navigation plays a major role in brain's function[33]. In the recent work[13] it was demonstrated that the functional brain networks have a navigation skeleton that allows greedy searching with low errors. Both growth and homophily[30, 34] are usually considered to be important factors influencing the brain network structure. Local connection to nearby neurons together with network growth are considered as a plausible mechanism for formation of long range connections in small nervous networks[35, 36], similarly to the proposed model. Our study shows that the GH networks have high level features that are found in the functional brain networks, indicating that the GH mechanism is not suppressed and plays a significant role in brain network formation, thus supporting the earlier suggestions that the brain networks are naturally navigable.

GH networks can also be viewed as a substantial generalization of a complex growing spatial 1D OHO model introduced in [37], which was used to deterministically produce networks with high clustering and short average path. Recently, another generalization of this model for the multidimensional case was proposed as a possible mechanism for formation of neural networks[38]. However, formation of navigation properties was not a subject of studies of the OHO model. GH network in the case of 1D circle data can be also considered as a degenerated version of growth models studied in [16] with an exclusion of popularity term (which also makes it similar to the OHO model). It was demonstrated that the hyperbolic model from [16], which is a growing model in a hyperbolic space, adequately describes evolution of many scale-free real networks. However, the properties for the case without hyperbolicity (popularity) which leads to exponential degree distribution were studied poorly. As follows from the navigation models in refs. [14, 15], without the scale-free degree distribution such networks were not expected to be navigable.

## **Results**

**Construction and navigation properties**. To construct a GH network we use a set of elements *S* from a metric space and a single construction parameter *M*. We start building network by inserting a random element from *S*. Then we iteratively insert randomly selected remaining elements *e* by connecting to *M* the previously inserted elements that have minimal distance to *e*, until all elements from *S* are inserted. Unlike the models from refs. [4, 5, 7, 8, 15, 16, 37-40] and the Watts-Strogatz model [41] (which all require global network knowledge at construction), the GH algorithm insertions can be done approximately using only local information by selecting the approximate nearest neighbors through a help of network navigation feature (see Methods section for details). This has a clear interpretation: new nodes in many real networks do not have global knowledge, so they have to navigate the network in order to find their place and adapt. The tests showed that under appropriate parameters there is no measurable difference in network metrics whether the construction had exact or inexact neighbors selection, while the network assembly process was drastically faster in the approximated neighbors case.

Because the elements from *S* are not placed on a regular lattice, the greedy search algorithm can be trapped in a local minimum before reaching the target. The generalization of the regular lattice for this case is the Delaunay graph, which is dual to the Voronoi partition. If we have a Delaunay graph subset in the network, the greedy search always ends at an element from *S* which is closest to any target element *t* [42] (note that this condition is more general than the one studied in [13]). It is easy to construct a Delaunay graph for low dimensional Euclidian spaces, especially in 1D case where it is a simple liked list, however it was shown that constructing the graph using only distances between the set elements is impossible for general metric spaces[42]. Still, it was demonstrated that connecting to *M* nearest neighbors acts as a good enough approximation of the Delaunay graph, so that by increasing *M* or using a slightly modified versions of the greedy algorithm these effects can be made negligible[23, 24]. The average greedy algorithm hop count of a GH network for different input data is presented in fig. 1(a). The graph shows a clear logarithmic scaling for all data used, including a non-trivial case of edit distance for English words. At the parameters used the probability of a success navigation was higher than 0.92 for all the data and higher than 0.999 for vector data with d<5.

The definition of navigability in [15] requires also that the greedy search success probability does not tend to zero in the limit of infinite network size. This restriction has led to a conclusion that the navigability should be expected only for the power law degree distribution networks with <2.5. However for the 1D data case (which was the only one considered by the authors of [15]) the success probability can be fixed to unity by a very simple realistic heuristics, thus questioning such a conjecture.

Networks produced by a GH model are also navigable by the aforementioned definition at least at small dimensionality (d≤6), as tests indicate that the recall converges to a constant value (see Supporting information for details), thus demonstrating existence of a new class of navigable models.

![](_page_3_Figure_0.jpeg)

Fig. 1. (a) Average hop count during a greedy search for different dimensionality Euclidian data and English words database with edit distance showing logarithmic scaling. (b) Degree distribution for the GH algorithm networks with PA for different degree cutoffs ( $k_c$ ).

**Degree distribution and information extraction locality.** A GH network has an exponential degree distribution (see in fig. 1(b)). The scale in the exponent is determined by the *M* parameter, similar analysis can be done as in [37, 38]. The exponential degree distribution is present in the real-life networks such as power grids, air traffic networks, and collaboration networks of company directors[43]. Studies of the functional brain network degree distribution yielded ambiguous results: some investigations have shown exponential degree distribution, while others exhibited scale-free or truncated scale-free distribution[44].

Most of the studied real-life networks, however, have a power law degree distribution. The GH algorithm can be slightly modified by adding a preferential attachment (PA)[45] to produce a scale-free (power law) degree distribution (which makes it similar to the growing models in a hyperbolic plane[16]). To achieve that, the distances to the elements are normalized by  $k^{1/d}$  during the network construction for uniform data in Euclidean space (see the Methods section for the details), leading to a power law degree distribution with  $\gamma$  close to 3. With the addition of a cutoff  $k_c$ , the degree distribution transforms into a power law with an exponential cutoff (see fig. 1(b)). As expected for scale-free networks[15], adding the preferential attachment does not suppress the network navigability (see fig. S1(b) in Supporting information for the comparison).

Exponential degree distribution is usually attributed to limited capacity of a node or to absence of PA mechanisms<sup>41</sup>. However, there is another critical distinction between scale-free and exponential degree distributions in terms of locality of information extraction which arises in virtual computer networks having practically no limit on node capacity. We define the locality as the number of distance computations during a greedy search, which also corresponds to algorithmic complexity of a search algorithm. Our simulations show that, for the scale-free networks (both in GH networks with PA and scale-free networks studied in [15]), the number of distance computations has a *power law* scaling with the number of network elements, in contrast to GH networks without PA and Kleinberg's networks which have a *polylogarithmic* scaling[24](see fig. S1 and fig. S2 in Supporting information). This happens because the greedy algorithm prefers nodes with the highest degrees (which have monopoly on long range links)[15] while the maximum degree in scale-free network has power law scaling  $N^{1/(\gamma-1)}$  with the number of elements[46] leading to  $N^{1/(\gamma-1)}$  search complexity. The authors in [14] argued that the best choice for optimal navigation is when  $\gamma$  is close to 2; this, however, leads to almost linear scaling of greedy search distance computations number. Such scaling makes using scale-free networks impractical

for greedy routing in large-scale networks where high locality of information extraction matters, which is the case of K-NN algorithms and is likely to be the case for the brain networks.

The importance of employing the locality of information extraction as a measure for network navigation studies can be underpinned by considering a star graph (a graph where every node is connected to a single central hub) with a modified greedy search algorithm that uses effective distance *ak e* (where *k* is degree of a candidate node, *a* is a parameter, is initial metric distance between the candidate and the target). The parameter *a* can be always set large enough, so that every greedy path will go through the hub reaching the target in two steps regardless of the network size. This network is ideal in all navigation measures defined in [14, 15], having short path, ideal success ratio and low average degree. However, to find these paths the greedy search algorithm has to utilize the hub's global view of the network and to compare distances to every network node thus having a bad linear algorithmic complexity scaling.

At the same time, the scale-free networks offer less greedy algorithm hops compared to the base GH algorithm which is beneficial. A power law degree distribution with an exponential cutoff seems to be a good tradeoff between low number of hops and low complexity of a search. Slightly increasing the cutoff *k<sup>c</sup>* above *M* in GH algorithm with PA sharply decreases the number of greedy algorithm hops (see fig. S1(b)), while having almost no impact on the number of distance computations (fig. S1(a)). This finding can be used for constructing artificial networks optimized for best navigability both in terms of complexity and number of hops.

**Link length distribution and optimal wiring.** For uniformly distributed bounded *d*-dimensional Euclidian data, the average distance between the nearest neighbors scales as 1/ ( ) ~ *<sup>d</sup> r N N* (1) with the total number of elements *N* in the network. It means that every characteristic scale of link length in a final network can be put in correspondence to some specific time of construction. That allows deducing the link length distribution by differencing the equation (1). By doing this we get a power law link length density *dN r dr* <sup>~</sup> with *d* 1 exponent (confirmed by the simulations). It was recently shown[7, 8] that *d* 1 is the optimal value for the shortest path length and greedy navigation path in case of constraint on total length of all connections in the network. Thus, GH networks are naturally close to optimal in terms of the wiring cost.

Power law link length distributions with *d* 1 are encountered in real-life networks like airport connections networks[47] and functional brain networks[48, 49]. It was speculated in refs. [7, 8] that such behavior arises due to global optimization schemes, while GH networks provide a much more simple and natural explanation for the exponent value.

**Self-similarity and hierarchical modular structure**. Construction of a GH network is an iterative process: at each step we have as an input a navigable small world network and we insert new elements and links preserving its properties. A part of a uniform data GH network covered by a ball is also a navigable small world with few outer connections. Thus, the GH networks have self-similar structure. Analysis of selfsimilarity identical to [27] is presented in the Supporting Information in fig. S3, demonstrating a selfsimilar structure of network's clustering coefficient.

The hierarchical self-similarity property is found in many real-life networks[27, 50, 51]. Studies have shown that the functional brain networks form a hierarchically modular community structure[48, 52] consisting of highly interconnected specialized modules, only loosely connected to each other. This may seem to contradict the small world feature which is usually modeled by random networks[48]. GH networks can easily model both small world navigation and modular structure simultaneously by introducing clusters. In this case, coordinates of the cluster centers may correspond to different neuron specialties in a generalized underlying metric space. A 2D GH network for clustered data is presented in fig. 3 demonstrating highly modular and at the same time navigable network structure containing only 30 intermodular links (0.03% of the total number) between the first elements in the network (which form a rich club). By using a simple modification of the greedy algorithm with preference of high degree nodes (see Methods section) short paths between different module elements can be efficiently found using only local information.

![](_page_5_Figure_1.jpeg)

Fig. 2. 2D network constructed by the GH algorithm with M=5 for clustered d=2 Euclidian data. The inset shows scaling of the modified greedy algorithm average hop count.

Rich club and greedy hops upper bounds. Simulations show that probability of a connection between the network elements grows exponentially with the element degree, thus demonstrating the presence of a rich club (see fig. S5 in Supporting Information). Due to incremental construction and self-similarity of the GH networks every preceding instance of a GH network acts as a rich club to any subsequent instance. To achieve a well-defined rich club, the self-similarity symmetry has to be broken by introducing non-fractality in data, such as a fixed number of clusters in fig. 2.

Universally, the rich club is composed of the first elements inserted by the GH algorithm, which is also the case for the brain networks. Studies have shown that the rich club in human brain is formed before the 30<sup>th</sup> week of gestation with almost no changes of its inner connections until birth[53]. Moreover, the investigations of C. elegans worms neural network have shown that the rich club neurons are among the first neurons to be born[54, 55]. Thus, together with [35], the GH model offers a plausible explanation of how the rich clubs are formed in brain networks.

Due to presence of rich clubs in GH networks a general navigation analysis similar to the scale-free networks from [15] can be done. At the beginning of a greedy search the algorithm "zooms-out" preferring high degree nodes with a higher characteristic link radius until it reaches a node for which the

characteristic radius of the connections is comparable with the distance to the target node. Next, a reverse "zoom-in" procedure takes place until the target node is reached, see [15] for details.

We offer a slightly different perspective. It can be shown that in GH networks the rich club is also *navigable*, meaning that a greedy search between two rich hub nodes is very likely to select only the rich club nodes at each step. This is illustrated by the simulations results in fig. 3(a) showing that the average hop count for the first  $10^4$  elements selected as start and targets nodes does not depend on the dataset size, i.e. the greedy search algorithm ignores newly added links. Figure 3(b) shows a schematic Voronoi partition of rich club element connections for a greedy algorithm step with another rich club element as a target. In the case of a good Delaunay graph approximation (high enough M) the Voronoi partition alters only locally as is shown in fig. 3(b), thus having no impact on the greedy search between the rich club elements.

Self-similarity and navigability of the rich club in GH networks play a crucial role in the navigation process. Under the conditions of a perfect Delaunay graph and rich club navigability one can show that there is an upper greedy algorithm hop bound  $2\log_2(N)$  (see Supporting Information for details), thus proving a logarithmic greedy search hops scaling.

![](_page_6_Figure_3.jpeg)

Fig. 3 (a) Average number of greedy algorithm hops scaling for the first  $10^4$  elements given as start and target nodes (red) and all elements used for search (black). The first  $10^4$  elements form a rich club that ignores more newly added elements. The results are presented for Euclidian data with d=2, M=20. (b) Cartoon of Voronoi partition for connections of a single greedy search step. Newly added elements (green) cause only local changes in Voronoi partitioning, so if the target element lies outside the current element connections, it falls into Voronoi partition of rich club's elements (blue), thus ignoring local connections at greedy search.

#### Discussion

Using simulations and theoretical studies we have demonstrated that two ingredients that are present in the majority of networks, namely network growth and local homophily, are sufficient to produce a navigable small world network, giving a simple and persuasive answer how the navigation feature appears in real-life networks. In contrast to the generally used models, a simple local GH model without central regulation by using only local information produces hierarchical self-similar optimally wired navigable networks, which offers a simple explanation why these features are found in real-life networks without a need of employing hyperbolicity or other complex schemes. Self-similarity and rich clubs navigation of the GH networks lead to emergence of logarithmic scaling of the greedy algorithm hops in GH networks.

By adding PA with saturation the degree distribution can be tuned from exponential to scale-free with or without exponential cutoff. We have shown that in case of pure scale-free degree distribution (as well as for the scale-free networks studied in [15] and hyperbolic networks), the true logarithmic local routing cannot be achieved due to a power law scaling of information extraction locality (algorithmic complexity of a search). Truncated scale-free degree distribution offers a reasonable tradeoff between the path length and the algorithmic complexity and can be used for practical applications.

Thus, every network that has both growth and homophily is a potential navigable small-world network. This is an important finding for real-life networks, as real life is full of examples of growth and homophily shaping the network. Scientific papers form a growing navigable citation network (navigability of which is actively utilized by researchers) just by citing existing related works. Big city passenger airports were among the first to open and later became big network hubs which play an important role in spatial navigation in airport networks[15]. Neural brain networks are formed utilizing both growth and homophily, producing hierarchical structures with rich clubs consisting of early born neurons. The proposed GH model offers a conclusive explanation of navigability in these networks. Still, the evolution of some networks including social structures incorporate other factors, such as node moving and departure. For these networks, a sudden departure of a major node (say, a key manager in a company or rich club neurons[56]) can seriously hurt the performance. However, some of these networks can be resilient to the above-mentioned processes, thus preserving navigation. For example, there are quite a few top-level deputies in big companies, and when a manager quits, he/she has to pass his/her contacts to a newcomer.

There is evidence that in real-life networks such as an airport and brain networks, the GH model is not suppressed by other mechanisms. In addition to the aforementioned growth and homophily, several other high level features of the GH model are observed in brain networks, such as low diameter, high clustering, presence of navigation skeleton, hierarchical self-similar modular structure, power law link length distribution with exact d+1 exponent, and emergence of a rich club from the first elements in the network. This indicates that the model plays a significant role in the formation of brain networks and that they are likely to be navigable, supporting the earlier suggestions[13, 33].

The proposed GH model can be used as a guide for building artificial optimally wired navigable structures using only local information.

#### Methods

**Construction.** The GH network was constructed through iteratively inserting the elements into the network in random order by adding bidirectional links to the *M* closest elements. To find the connections we applied approximate K-NN graph algorithms[24] (C++ implementations of the K-NN algorithms are available in the Non-Metric Space Library[57]) which had utilized the navigation in the constructed graph. To obtain approximate *M* nearest neighbors, a dynamic list of *M* closest of the found elements (initially filled with a random enter point node) was kept during the search. The list was updated at each step by evaluating the neighborhood of the closest previously non-evaluated element in the list until the neighborhood of every element from the list was evaluated. For *M*=1, this method is equivalent to a basic greedy search. The best *M* results from several trials were used as approximate closest elements. The number of trials was adjusted so that the recall (the ratio between the found and the true *M* nearest neighbors) was higher than 0.95, producing results almost indistinguishable from what you get from the exact search. The construction procedure has a polylogarithmic complexity[24].

For the simulations with PA (fig. 1(a)), effective distances to the elements  $(\Delta_{eff}(e1,e2) = \Delta_{Euclid}(e1,e2)/(k_c)^{1/d})$  if  $k_2 < k_c$ ,  $\Delta_{new}(e1,e2) = \Delta_{Euclid}(e1,e2)/(k_c)^{1/d}$  otherwise, k is the degree of a

node) were used to select the neighbors. Changing the seed of the algorithm random data generators, connecting to the *M* exact neighbors and/or construction in many parallel threads had a very slight effect on the evaluated network metrics.

**Datasets.** Random Euclidian data with coordinates distributed uniformly in [0,1] range with L<sup>2</sup> distance was used to model the vectors. For testing the Damerau–Levenshtein distance, about 700k English words from the Scowl Debain database were used as the dataset. In order to unambiguously select the next node during a greedy search, a small random value was added to the Damerau–Levenshtein distance. For fig. 1(a) parameter *M* was set to be 9, 12, 20, 25, 150 and 40 for Euclidian vectors with *d*=1, 2, 3, 5, 50 and English word dataset, respectively. The success ratio for the vectors was higher than 0.999 for *d*≤5, higher than 0.92 for *d*=50 and English words data. On the average, only 760 distance computations were needed to find the path between two arbitrary words in 700k database and only about 1280 distance computations were required to find the path for 20 million *d=*5 Euclidian vectors.

**Network metrics.** To evaluate the average number of hops, we used up to 10<sup>4</sup>randomly selected nodes as start and target elements. The greedy algorithm selects at each step a neighbor that is closest to the target as an input for the next step, until it reaches the element which is closer to the target than its neighbors. The success ratio is the ratio of the number of successful searches to the total number of searches. The search is considered failed if the result is not the target element.

The information extraction locality metric was evaluated by counting the average number of distance calculations during a single greedy search.

To get a high recall (>0.95) for the tests with clustered 2D data and for the e we used a modification of the greedy search algorithm[39] that minimized the normalized distance (*norm(target,e2)=Euclid(target,e2)/(k2) 1/2*) .

### **Acknowledgements**

We are grateful to I. Malkova, L. Boytsov, D. Yashunin, N. Krivatkina and V. Nekorkin for the discussions. The reported study was funded by RFBR, according to the research project No. 16-31-60104 mol\_а\_dk.

## **References**

- 1. Arbib MA. The handbook of brain theory and neural networks: MIT press; 2003.
- 2. Travers J, Milgram S. An experimental study of the small world problem. Sociometry. 1969:425- 43.
- 3. Huang W, Chen S, Wang W. Navigation in spatial networks: A survey. Physica A: Statistical Mechanics and its Applications. 2014;393:132-54.
- 4. Kleinberg JM. Navigation in a small world. Nature. 2000;406(6798):845-.
- 5. Kleinberg J, editor The small-world phenomenon: An algorithmic perspective. Proceedings of the thirty-second annual ACM symposium on Theory of computing; 2000 2000: ACM.
- 6. Hu Y, Wang Y, Li D, Havlin S, Di Z. Possible origin of efficient navigation in small worlds. Physical Review Letters. 2011;106(10):108701.
- 7. Li G, Reis S, Moreira A, Havlin S, Stanley H, Andrade Jr J. Optimal transport exponent in spatially embedded networks. Physical Review E. 2013;87(4):042810.
- 8. Li G, Reis S, Moreira A, Havlin S, Stanley H, Andrade Jr J. Towards design principles for optimal transport networks. Physical Review Letters. 2010;104(1):018701.
- 9. Chaintreau A, Fraigniaud P, Lebhar E. Networks become navigable as nodes move and forget. Automata, Languages and Programming: Springer; 2008. p. 133-44.
- 10. Clarke I, Sandberg O, Wiley B, Hong TW, editors. Freenet: A distributed anonymous information storage and retrieval system. Designing Privacy Enhancing Technologies; 2001: Springer.
- 11. Sandberg O, Clarke I. The evolution of navigable small-world networks. arXiv preprint cs/0607025. 2006.

- 12. Yang Z, Chen W, editors. A Game Theoretic Model for the Formation of Navigable Small-World Networks. Proceedings of the 24th International Conference on World Wide Web; 2015: International World Wide Web Conferences Steering Committee.
- 13. Gulyás A, Bíró JJ, Kőrösi A, Rétvári G, Krioukov D. Navigable networks as Nash equilibria of navigation games. Nature Communications. 2015;6:7651.
- 14. Krioukov D, Papadopoulos F, Kitsak M, Vahdat A, Boguná M. Hyperbolic geometry of complex networks. Physical Review E. 2010;82(3):036106.
- 15. Boguna M, Krioukov D, Claffy KC. Navigability of complex networks. Nature Physics. 2009;5(1):74-80.
- 16. Papadopoulos F, Kitsak M, Serrano MÁ, Boguñá M, Krioukov D. Popularity versus similarity in growing networks. Nature. 2012;489(7417):537-40.
- 17. McPherson M, Smith-Lovin L, Cook JM. Birds of a feather: Homophily in social networks. Annual Review of Sociology. 2001:415-44.
- 18. Chávez E, Navarro G, Baeza-Yates R, Marroquín JL. Searching in metric spaces. ACM computing surveys (CSUR). 2001;33(3):273-321.
- 19. Beaumont O, Kermarrec A-M, Marchal L, Rivière É, editors. VoroNet: A scalable object network based on Voronoi tessellations. Parallel and Distributed Processing Symposium, 2007 IPDPS 2007 IEEE International; 2007: IEEE.
- 20. Beaumont O, Kermarrec A-M, Rivière É. Peer to peer multidimensional overlays: Approximating complex structures. Principles of Distributed Systems: Springer; 2007. p. 315-28.
- 21. Lifshits Y, Zhang S, editors. Combinatorial algorithms for nearest neighbors, near-duplicates and small-world design. Proceedings of the Twentieth Annual ACM-SIAM Symposium on Discrete Algorithms; 2009: Society for Industrial and Applied Mathematics.
- 22. Ponomarenko A, Mal'kov Y, Logvinov A, Krylov V, editors. Approximate Nearest Neighbor Search Small World Approach. International Conference on Information and Communication Technologies & Applications; 2011; Orlando, Florida, USA.
- 23. Malkov Y, Ponomarenko A, Logvinov A, Krylov V. Scalable distributed algorithm for approximate nearest neighbor search problem in high dimensional general metric spaces. Similarity Search and Applications: Springer Berlin Heidelberg; 2012. p. 132-47.
- 24. Malkov Y, Ponomarenko A, Logvinov A, Krylov V. Approximate nearest neighbor algorithm based on navigable small world graphs. Information Systems. 2014;45:61-8.
- 25. Ponomarenko A, Avrelin N, Naidan B, Boytsov L. Comparative Analysis of Data Structures for Approximate Nearest Neighbor Search. In Proceedings of The Third International Conference on Data Analytics. 2014.
- 26. Naidan B, Boytsov L, Nyberg E. Permutation search methods are efficient, yet faster search is possible. VLDB Procedings. 2015;8(12):1618-29.
- 27. Serrano MA, Krioukov D, Boguná M. Self-similarity of complex networks and hidden metric spaces. Physical Review Letters. 2008;100(7):078701.
- 28. Bullmore E, Sporns O. Complex brain networks: graph theoretical analysis of structural and functional systems. Nature Reviews Neuroscience. 2009;10(3):186-98.
- 29. Vértes PE, Alexander-Bloch A, Bullmore ET. Generative models of rich clubs in Hebbian neuronal networks and large-scale human brain networks. Philosophical Transactions of the Royal Society of London B: Biological Sciences. 2014;369(1653):20130531.
- 30. Betzel RF, Avena-Koenigsberger A, Goñi J, He Y, de Reus MA, Griffa A, et al. Generative models of the human connectome. NeuroImage. 2015.
- 31. Vértes PE, Alexander-Bloch AF, Gogtay N, Giedd JN, Rapoport JL, Bullmore ET. Simple models of human brain functional networks. Proceedings of the National Academy of Sciences. 2012;109(15):5868- 73.
- 32. Colizza V, Flammini A, Serrano MA, Vespignani A. Detecting rich-club ordering in complex networks. Nature Physics. 2006;2(2):110-5.
- 33. van den Heuvel MP, Kahn RS, Goñi J, Sporns O. High-cost, high-capacity backbone for global brain communication. Proceedings of the National Academy of Sciences. 2012;109(28):11372-7.
- 34. Bullmore E, Sporns O. The economy of brain network organization. Nature Reviews Neuroscience. 2012;13(5):336-49.

- 35. Lim S, Kaiser M. Developmental time windows for axon growth influence neuronal network topology. Biological cybernetics. 2015;109(2):275-86.
- 36. Nicosia V, Vértes PE, Schafer WR, Latora V, Bullmore ET. Phase transition in the economically modeled growth of a cellular nervous system. Proceedings of the National Academy of Sciences. 2013;110(19):7880-5.
- 37. Ozik J, Hunt BR, Ott E. Growing networks with geographical attachment preference: Emergence of small worlds. Physical Review E. 2004;69(2):026108.
- 38. Zitin A, Gorowara A, Squires S, Herrera M, Antonsen TM, Girvan M, et al. Spatially embedded growing small-world networks. Scientific Reports. 2014;4.
- 39. Thadakamalla H, Albert R, Kumara S. Search in spatial scale-free networks. New Journal of Physics. 2007;9(6):190.
- 40. Zuev K, Boguñá M, Bianconi G, Krioukov D. Emergence of Soft Communities from Geometric Preferential Attachment. Scientific Reports. 2015;5.
- 41. Watts DJ, Strogatz SH. Collective dynamics of 'small-world'networks. Nature. 1998;393(6684):440-2.
- 42. Navarro G. Searching in metric spaces by spatial approximation. The VLDB Journal. 2002;11(1):28-46.
- 43. Newman M, Barabasi A-L, Watts DJ. The structure and dynamics of networks: Princeton University Press; 2006.
- 44. Qi S, Meesters S, Nicolay K, Romeny BMtH, Ossenblok P. The influence of construction methodology on structural brain network measures: A review. Journal of Neuroscience Methods. (0). doi[: http://dx.doi.org/10.1016/j.jneumeth.2015.06.016.](http://dx.doi.org/10.1016/j.jneumeth.2015.06.016)
- 45. Barabási A-L, Albert R. Emergence of scaling in random networks. Science. 1999;286(5439):509- 12.
- 46. Boguná M, Pastor-Satorras R, Vespignani A. Cut-offs and finite size effects in scale-free networks. The European Physical Journal B-Condensed Matter and Complex Systems. 2004;38(2):205-9.
- 47. Bianconi G, Pin P, Marsili M. Assessing the relevance of node features for network structure. Proceedings of the National Academy of Sciences. 2009;106(28):11433-8.
- 48. Gallos LK, Makse HA, Sigman M. A small world of weak ties provides optimal global integration of self-similar modules in functional brain networks. Proceedings of the National Academy of Sciences. 2012;109(8):2825-30.
- 49. Eguiluz VM, Chialvo DR, Cecchi GA, Baliki M, Apkarian AV. Scale-free brain functional networks. Physical Review Letters. 2005;94(1):018102.
- 50. Song C, Havlin S, Makse HA. Self-similarity of complex networks. Nature. 2005;433(7024):392-5.
- 51. Colomer-de-Simón P, Serrano MÁ, Beiró MG, Alvarez-Hamelin JI, Boguñá M. Deciphering the global organization of clustering in real complex networks. Scientific Reports. 2013;3.
- 52. Meunier D, Lambiotte R, Bullmore ET. Modular and hierarchically modular organization of brain networks. Frontiers in neuroscience. 2010;4.
- 53. Ball G, Aljabar P, Zebari S, Tusor N, Arichi T, Merchant N, et al. Rich-club organization of the newborn human brain. Proceedings of the National Academy of Sciences. 2014;111(20):7456-61.
- 54. Towlson EK, Vértes PE, Ahnert SE, Schafer WR, Bullmore ET. The rich club of the C. elegans neuronal connectome. The Journal of Neuroscience. 2013;33(15):6380-7.
- 55. Varier S, Kaiser M. Neural development features: Spatio-temporal development of the Caenorhabditis elegans neuronal network. PLOS Computational Biology. 2011.
- 56. Rubinov M. Schizophrenia and abnormal brain network hubs. Dialogues in Clinical Neuroscience. 2013;15(3):339.
- 57. Boytsov L, Naidan B. Engineering Efficient and Effective Non-metric Space Library. Similarity Search and Applications: Springer; 2013. p. 280-93. https://github.com/searchivarius/nmslib

# **Supporting Information for**

# "Growing homophilic networks are natural navigable small worlds" by Yu. A. Malkov and A. Ponomarenko

1. Comparison of the basic GH model to the GH model with PA and to the scale-free networks from ref. [1] (Boguna, M., Krioukov, D., & Claffy, K. C. (2009). *Nature Physics*, 5(1), 74-80).

To evaluate the locality of information extraction we determined an average number of distance computations during a single greedy search, a measure which is usually adopted to practically determine the efficiency of similarity search algorithms. Our simulations show that for the scale-free networks produced by GH with PA the number of distance computations has a power law scaling with the number of network elements, in contrast to the GH networks without PA which have a polylogarithmic scaling (see fig. S1(a)).

At the same time, the scale-free networks offer less greedy algorithm hops compared to the base GH algorithm which is beneficial. A power law degree distribution with an exponential cutoff seems to be a good tradeoff between low number of hops and low complexity of a search. Slightly increasing the cutoff  $k_c$  above M in GH algorithm with PA sharply decreases the number of greedy algorithm hops (see fig. S1(b)), while having almost no impact on the number of distance computations (fig. S1(a)). This finding can be used for constructing artificial networks optimized for best navigability both in terms of complexity and number of hops.

![](_page_11_Figure_5.jpeg)

Fig. S1. Comparison of the GH model to the GH model with PA.

(a) Number of distance computations per a greedy search for GH network with PA for different degree cutoffs ( $k_c$ ). (b) Average hop count during a greedy search for GH network with PA for different degree cutoffs. The inset shows the decay of greedy hop slope with an increase of the degree cutoff. Both plots are presented for Euclid data with d=2, M=12.

The scale-free networks from [1] were modeled with the parameters  $\gamma$ =5,  $\alpha$ =2.5 as advised in the paper, for 1D uniformly distributed data in Euclidian distance. The characteristic scale parameter was adjusted to produce a success probability close to 0.92, resulting in an average node degree close to 12. The parameter M of the GH algorithm was set to 5, thus the network had an average degree of 10. The comparison was done only for the 1D case, because for the higher dimensions we were not able to simultaneously get high success probability and the low average degree for the scale-free networks from [1]. The maximum data size in the comparison was limited by the algorithm from [1] which had a high  $N^2 \ln(N)$  complexity to establish the scaling (compared to  $^{\sim}N\cdot\ln^2(N)$  complexity for the GH algorithm case). Both for the GH networks and for the scale-free networks the plots were smoothed over 8-12

trials. An averaged success probability of a greedy search does not decrease with the number of elements in the network for both models (see fig. S2(b)).

Smoothed greedy search success probability scaling is plotted in fig. S2(d) for a case of GH networks with higher dimensional data (d=4, 6). The plot shows almost no changes in the success probability as the networks grows by several orders of magnitude thus demonstrating the GH networks are also navigable by the definition from ref. [1]. This shows the existence of a new class of navigable models with exponential degree distribution. Navigability in this case was not expected from the results of ref. [1], where a scale-free degree distribution was required for the navigability.

![](_page_12_Figure_2.jpeg)

Fig S2. Comparison of the GH algorithm to the navigable scale-free networks from [1] on 1D data (a-c). (a) Average number of distance computations during a greedy search. (b) Average success probability of a greedy search. (c) Average greedy algorithm hops.

(d) The scaling of greedy search success probability in GH networks on higher dimensional random data.

While the considered scale-free networks offer significantly less hops (fig. S2(c)), the number of distance computations for the scale-free network has a scaling close to  $N^{1/1.5}$  (fig. S2(a)) which corresponds to a  $N^{1/(\gamma-1)}$  scaling of the maximum degree in the network. The GH networks instead have a polylogarithmic scaling. So despite the small number of hops the greedy search can hardly be called local for the scale-free networks, especially in the case of the  $\gamma$  close to 2. The observed polynomial scaling should also be valid for hyperbolic geometric graphs[2] which share basic properties with networks, studied in [1].

## 2. Self-similarity in clustering coefficient distribution

The plot in fig. S3 demonstrates a self-similar structure of the network's average clustering coefficient distribution obtained using the same procedure as in [3]. All nodes with degree less than  $k_{thr}$  are

removed from the network and degrees of the nodes are normalized by the mean degree. Finally, a distribution of normalized average clustering coefficient is calculated for different  $k_{thr}$ .

Alternating the  $k_{thr}$  in a wide range does not change the normalized average clustering coefficient distribution, which means that the network has a self-similar structure.

![](_page_13_Figure_2.jpeg)

**Fig. S3.** Normalized average clustering coefficient distribution in the network for different values of  $k_{thr}$  and dimensionality.

## 3. Average nearest neighbor degree

The plot shows average nearest neighbor degree distribution demonstrating that GH networks have assortative degree mixing.

![](_page_13_Figure_6.jpeg)

Fig. S4. Nearest neighbors degree distribution for vectors with different dimensionality.

## 4. Rich club coefficient

Figure S5 shows an exponential rise of the rich club coefficient  $\phi(k) = 2E_{>k} / (N_{>k}(N_{>k}-1))$  together with a rich club coefficient of a random network with the same degree distribution (for the case of d=8), which demonstrates that GH networks have rich clubs.

![](_page_14_Figure_0.jpeg)

Fig. S5. Rich club coefficient of GH networks for vector data of different dimensionality

## 5. Upper bounds of average greedy algorithm hops for the GH model

Suppose we have a GH network which contains a perfect Delaunay graph at every step, rich club navigation feature and has an average greedy algorithm hop count *H*. We can show that by doubling the number of the elements the average greedy path increases no more than by adding a constant.

If the start and target nodes are from the rich club (first half of the network), the average hop count does not increase as it has been shown in the manuscript. If the greedy algorithm starts a search for a distant target from a newly added element it has at least 1/2 probability that the next selected element is from the rich club (since a half of the elements is from the rich club), thus reaching the rich club on average in two steps. Next, the greedy algorithm needs on average no more than H steps to get to a rich club element for which the Voronoi region has the query. For a case when the destination node is from the rich club the average number of hops is thus H+2. In the opposite case the search ends on average in two additional steps, because the probability that next node is from the rich club is at least 1/2 and since we have already visited the rich club node that is closest to the query, this cannot happen. Thus the average number of hops in this case is H+4. By concerning the last case (the target – newly added element and start element is from the rich club) we get an average H+2 hops. Thus the upper hop bound scales as  $2\log_2(N)$  proving GH networks have a logarithmic scaling of the greedy search hops.

</details>

<details>
<summary>Navigability of complex networks</summary>

# Navigability of complex networks

Mari´an Bogu˜n´a,<sup>1</sup> Dmitri Krioukov,<sup>2</sup> and kc claffy<sup>2</sup>

<sup>1</sup>Departament de F´ısica Fonamental, Universitat de Barcelona, Mart´ı i Franqu`es 1, 08028 Barcelona, Spain <sup>2</sup>Cooperative Association for Internet Data Analysis (CAIDA), University of California, San Diego (UCSD), 9500 Gilman Drive, La Jolla, CA 92093, USA

Routing information through networks is a universal phenomenon in both natural and manmade complex systems. When each node has full knowledge of the global network connectivity, finding short communication paths is merely a matter of distributed computation. However, in many real networks nodes communicate efficiently even without such global intelligence. Here we show that the peculiar structural characteristics of many complex networks support efficient communication without global knowledge. We also describe a general mechanism that explains this connection between network structure and function. This mechanism relies on the presence of a metric space hidden behind an observable network. Our findings suggest that real networks in nature have underlying metric spaces that remain undiscovered. Their discovery would have practical applications ranging from routing in the Internet and searching social networks, to studying information flows in neural, gene regulatory networks, or signaling pathways.

## I. INTRODUCTION

Networks are ubiquitous in all domains of science and technology, and permeate many aspects of daily human life [\[1,](#page-11-0) [2,](#page-11-1) [3,](#page-11-2) [4\]](#page-11-3), especially upon the rise of the information technology society [\[5,](#page-11-4) [6\]](#page-11-5). Our growing dependence on them has inspired a burst of activity in the new field of network science, keeping researchers motivated to solve the difficult challenges that networks offer. Among these, the relation between network structure and function is perhaps the most important and fundamental. Transport is one of the most common functions of networked systems. Examples can be found in many domains: transport of energy in metabolic networks, of mass in food webs, of people in transportation systems, of information in cell signalling processes, or of bytes across the Internet.

In many of these examples, routing –or signalling of information propagation paths through a complex network maze– plays a determinant role in the transport properties of the system, in particular in such systems as the Internet or airport networks that have transport as their primary function. The observed efficiency of this routing process in real networks poses an intriguing question: how is this efficiency achieved? When each element of the system has a full view of the global network topology, finding short routes to target destinations is a well-understood computational process. However, in many networks observed in nature, including those in society and biology (signalling pathways, neural networks, etc.), nodes efficiently find intended communication targets even though they do not possess any global view of the system. For example, neural networks would not function so well if they could not route specific signals to appropriate organs or muscles in the body, although no neurone has a full view of global inter-neurone connectivity in the brain.

In this work, we identify a general mechanism that explains routing conductivity, or navigability of real networks based on the concept of similarity between nodes [\[7,](#page-11-6) [8,](#page-11-7) [9,](#page-11-8) [10,](#page-11-9) [11,](#page-11-10) [12\]](#page-11-11). Specifically, intrinsic characteristics of nodes define a measure of similarity between them, which we abstract as a hidden distance. Taken together, hidden distances define a hidden metric space for a given network. Our recent work shows that these spaces explain the observed structural peculiarities of several real networks, in particular social and technological ones [\[13\]](#page-11-12). Here we show that this underlying metric structure can be used to guide the routing process, leading to efficient communication without global information in arbitrarily large networks. Our analysis reveals that, remarkably, real networks satisfy the topological conditions that maximise their navigability within this framework. Therefore, hidden metric spaces offer explanations of two open problems in complex networks science: the communication efficiency networks so often exhibit, and their unique structural characteristics.

## II. NODE SIMILARITY AND HIDDEN METRIC SPACES

Our work is inspired by the seminal work of sociologist Stanley Milgram on the small world problem. The small world paradigm refers to the existence of short chains of acquaintances among individuals in societies [\[14\]](#page-11-13). At Milgram's time, direct proof of such a paradigm was impossible due to the lack of large databases of social contacts, so Milgram conceived an experiment to analyse the small world phenomenon in human social networks. Randomly chosen individuals in the United States were asked to route a letter to an unknown recipient using only friends or acquaintances that, according to their judgement, seemed most likely to know the intended recipient. The outcome of the experiment revealed that, without any global network knowledge, letters reached the target recipient using, on average, 5.2 intermediate people, demonstrating that social acquaintance networks were indeed small worlds.

The small world property can be easily induced by

![](_page_1_Picture_1.jpeg)

FIG. 1: How hidden metric spaces influence the structure and function of complex networks. The smaller the distance between two nodes in the hidden metric space, the more likely they are connected in the observable network topology. If node A is close to node B, and B is close to C, then A and C are necessarily close because of the triangle inequality in the metric space. Therefore, triangle ABC exists in the network topology with high probability, which explains the strong clustering observed in real complex networks. The hidden space also guides the greedy routing process: if node A wants to reach node F, it checks the hidden distances between F and its two neighbours B and C. Distance CF (green dashed line) is smaller than BF (red dashed line), therefore A forwards information to C. Node C then performs similar calculations and selects its neighbour D as the next hop on the path to F. Node D is directly connected to F. The result is path A → C → D → F shown by green edges in the observable topology.

<span id="page-1-0"></span>adding a small number of random connections to a "large world" network [\[15\]](#page-11-14). More striking is the fact that social networks are navigable without global information. Indeed, the only information that people used to make their routing decisions in Milgram's experiment was a set of descriptive attributes of the destined recipient, such as place of living and occupation. People then determined who among their contacts was "socially closest" to the target. The success of the experiment indicates that social distances among individuals –even though they may be difficult to define mathematically– play a role in shaping the network architecture and that, at the same time, these distances can be used to navigate the network. However, it is not clear how this coupling between the structure and function of the network leads to efficiency of the search process, or what the minimum structural requirements are to facilitate such efficiency [\[16\]](#page-11-15).

In this work, we show how network navigability depends on the structural parameters characterising the two most prominent and common properties of real complex networks: (1) scale-free (power-law) node degree distributions characterising the heterogeneity in the number of connections that different nodes have, and (2) clustering, a measure of the number of triangles in the network topology. We assume the existence of a hidden metric space, an underlying geometric frame that contains all nodes of the network, shapes its topology, and guides routing decisions, as illustrated in Fig. [1.](#page-1-0) Nodes are connected in the observable topology, but a full view of their global connectivity is not available at any node. Nodes are also positioned in the hidden metric space and identified by their co-ordinates in it. Distances between nodes in this space abstract their similarity [\[7,](#page-11-6) [8,](#page-11-7) [9,](#page-11-8) [10,](#page-11-9) [11,](#page-11-10) [12\]](#page-11-11). These distances influence both the observable topology and routing function: (1) the smaller the distance between two nodes in the hidden space, i.e., the more similar the two nodes, the more likely they are connected in the observable topology; (2) nodes also use hidden distances to select, as the next hop, the neighbour closest to the destination in the hidden space. Kleinberg introduced the term greedy routing to describe this forwarding process [\[16\]](#page-11-15). Greedy routing and its modifications have been studied extensively in recent computer science literature [\[17,](#page-11-16) [18,](#page-11-17) [19,](#page-12-0) [20,](#page-12-1) [21,](#page-12-2) [22,](#page-12-3) [23,](#page-12-4) [24,](#page-12-5) [25,](#page-12-6) [26,](#page-12-7) [27,](#page-12-8) [28,](#page-12-9) [29\]](#page-12-10) (see also Kleinberg's review [\[30\]](#page-12-11) and references therein). However, most of these works do not study greedy routing on scale-free topologies, which are known as the common signature of many large-scale self-evolving complex networks [\[1,](#page-11-0) [2,](#page-11-1) [3\]](#page-11-2).

We use the class of network models developed in recent work [\[13\]](#page-11-12). They generate networks with topologies similar to those of real networks –small-world, scale-free, and with strong clustering– and, simultaneously, with hidden metric spaces lying underneath. The simplest model in this class (the details are in Appendix [A\)](#page-6-0) uses a one-dimensional circle as the underlying metric space, in which nodes are uniformly distributed. The model first assigns to each node its expected degree k, drawn from a power-law degree distribution P(k) ∼ k −γ , with γ > 2, and then connects each pair of nodes with connection probability r(d; k, k<sup>0</sup> ) that depends both on the distance d between the two nodes in the circle and their assigned degrees k and k 0 ,

<span id="page-2-0"></span>
$$r(d; k, k') \equiv r(d/d_c) = (1 + d/d_c)^{-\alpha},$$
 (1)  
where  $\alpha > 1$  and  $d_c \sim kk',$ 

which means that the probability of link connection between two nodes in the network decreases with the hidden distance between them (as ∼ d <sup>−</sup>α) and increases with their degrees (as ∼ (kk<sup>0</sup> ) <sup>α</sup>).

These two properties have a clear interpretation. The connection cost increases with hidden distance, thus discouraging long-range links. However, in making connections, rich (well-connected, high-degree) nodes care less about distances (connection costs) than poor nodes. Further, the characteristic distance scale d<sup>c</sup> provides a coupling between node degrees and hidden distances, and ensures the following three topological characteristics that we commonly see in real networks. First, pairs of richly connected, high-degree nodes –hubs– are connected with high probability regardless of the hidden distance between them because their characteristic distance d<sup>c</sup> is so large that any actual distance d between them will be short in comparison: regardless of d, connection probability r in Eq. [\(1\)](#page-2-0) is close to 1 if d<sup>c</sup> is large. Second, pairs of low-degree nodes will not be connected unless the hidden distance d between them is short enough to compare with the small value of their characteristic distance dc. Third, following similar arguments, pairs composed of hubs and low-degree nodes are connected only if they are located at moderate hidden distances.

The parameter α in Eq. [\(1\)](#page-2-0) determines the importance of hidden distances for node connections. The larger α, the more preferred are connections between nodes close in the hidden space. Consequently, the triangle inequality in the metric space leads to stronger clustering in the network, cf. Fig. [1.](#page-1-0) Clustering has a clear interpretation in our approach as a reflection of the network's metric strength: the more powerful is the influence of the network's underlying metric space on the observable topology, the more strongly it is clustered.

Although our toy model is not designed to exactly match any specific real network, it generates graphs that are surprisingly similar to some real networks, such as the Internet at the autonomous system level or the USA airport network. See Appendix [D](#page-7-0) for details.

![](_page_2_Figure_8.jpeg)

<span id="page-2-1"></span>FIG. 2: Average length of greedy-routing paths. The left plot shows the average hop length of successful paths, τ , as a function of the network size N for different values of γ and α. Results for values of γ > 2.5 look similar but with longer paths and are omitted for clarity. In all cases, the path length grows polylogarithmically with the network size: the observed values of τ are fit well by τ (N) = A[log N] ν (solid lines), where A and ν are some constants. The right plot shows τ as a function of γ and α for networks of fixed size N ≈ 10<sup>5</sup> . The effect of the two parameters on average path length is straightforward: paths are shorter for smaller exponents γ and stronger clustering (larger α's).

## III. NAVIGABILITY OF MODELLED NETWORKS

We use the model to generate scale-free networks with different values of power-law degree distribution exponent γ and clustering strength α, covering the observed values in a vast majority of documented complex networks [\[1,](#page-11-0) [2,](#page-11-1) [3\]](#page-11-2). We then simulate greedy routing for a large sample of paths on all generated networks, and compare the following two navigability parameters: 1) the average hop length τ from source to destination of successful greedy-routing paths, and 2) the success ratio ps, defined as the percentage of successful paths. Unsuccessful paths are paths that get stuck at nodes without neighbours closer to the destination in the hidden space than themselves. These nodes usually have small degrees. See Appendix [B](#page-7-1) for simulation details.

Fig. [2](#page-2-1) shows the impact of the network's degree distribution and clustering on the average length τ of greedy routing paths. We observe a straightforward dependency: paths are shorter for smaller exponents γ and stronger clustering (larger α's). The dependency of the success ratio (the fraction of successful paths) p<sup>s</sup> on the two topology parameters γ and α is more intertwined. Fig. [3](#page-3-0) shows that the effect of one parameter, γ, on the success ratio depends on the other parameter, the level of clustering. If clustering is weak (low α), the percentage of successful paths decays with network size N regardless of the value of γ (Fig. [3](#page-3-0) top-left). However, with strong clustering (large α), the percentage of successful paths increases with N and attains a maximum for large networks if γ . 2.6, whereas it degrades for large networks if γ > 2.6 (Fig. [3](#page-3-0) bottom-left). Fig. [3](#page-3-0) top-right shows this effect for networks of the same size (N = 10<sup>5</sup> ) with different γ and α. The value of γ = 2.6 ± 0.1 maximises

![](_page_3_Figure_1.jpeg)

<span id="page-3-0"></span>FIG. 3: Success probability of greedy routing. Left plots: success probability  $p_s$  as a function of network size N for different values of  $\gamma$  with weak (top) and strong (bottom) clustering. The top-right plot shows  $p_s$  as a function of  $\gamma$ and  $\alpha$  for networks of fixed size  $N \approx 10^5$ . In the bottomright plot, parameter  $\alpha$  is mapped to clustering coefficient C [15] by computing C for each network with given  $\gamma$  and  $\alpha$ . For each value of C, there is a critical value of  $\gamma = \gamma_c(C)$ such that the success ratio in networks with this C and  $\gamma$  >  $\gamma_c(C)$  decreases with the network size  $(p_s(N) \xrightarrow[N \to \infty]{} 0)$ , while  $p_s(N)$  reaches a constant value for large N in networks with  $\gamma < \gamma_c(C)$ . The solid line in the plot shows these critical values  $\gamma_c(C)$ , separating the low- $\gamma$ , high-C navigable region, in which greedy routing remains efficient in the large-graph limit, from the high- $\gamma$ , low-C non-navigable region, where the efficiency of greedy routing degrades for large networks. The plot labels measured values of  $\gamma$  and C for several real complex networks. *Internet* is the global Internet topology of autonomous systems as seen by the Border Gateway Protocol (BGP) [31]; Web of trust is the Pretty Good Privacy (PGP) social network of mutual trust relationships [32]; Metabolic is the network of metabolic reactions of E. coli [33]; and Airports is the network of the public air transportation system [34].

the number of successful paths once clustering is above a threshold,  $\alpha \geq 1.5$ . These observations mean that for a fixed clustering strength, there is a critical value of the exponent  $\gamma$  (Fig. 3 bottom-right) below which networks remain navigable as their size increases, but above which their navigability deteriorates with their size.

In summary, strong clustering improves both navigability metrics. We also find a delicate trade-off between values of  $\gamma$  close to 2 minimising path lengths, and higher values – not exceeding  $\gamma \approx 2.6$  – maximising the percentage of successful paths. We explain these findings in the next section, but we note here that qualitatively, this navigable parameter region contains a majority of complex networks observed in reality [1, 2, 3], as confirmed in Fig. 3 (bottom-right), where we juxtapose few paradigmatic examples of communication, social, biological, and transportation networks vs. the identified nav-

igable region of clustering and degree distribution exponent. Interestingly, power grids, which propagate electricity rather than route information, are neither scale-free nor clustered [15, 35].

## IV. AIR TRAVEL BY GREEDY ROUTING AS AN EXPLANATION

We illustrate the greedy routing function, and the structure of networks conductive to such routing, with an example of passenger air travel. Suppose we want to travel from Toksook Bay, Alaska, to Ibiza, Spain, by the public air transportation network. Nodes in this network are airports, and two airports are connected if there is at least one flight between them. We travel according to the greedy routing strategy using geography as the underlying metric space. At each airport we choose the next-hop airport geographically closest to the destination. Under these settings, our journey goes first to Bethel, then to Anchorage, to Detroit, over the Atlantic to Paris, then to Valencia and finally to Ibiza, see Fig. 4. The sequence and sizes of airport hops reveal the structure of our greedy-routing path. The path proceeds from a small airport to a local hub at a small distance, from there to a larger hub at a larger distance, and so on until we reach Paris. At that point, when the distance to the destination becomes sufficiently small, greedy routing leads us closer to our final destination by choosing not another hub, but a less connected neighbouring airport.

We observe that the navigation process has two, somewhat symmetric phases. The first phase is a coarse-grained search, travelling longer and longer distances per hop toward hubs, thus "zooming out" from the starting point. The second phase corresponds to a fine-grained search, "zooming in" onto the destination. The turning point between the two phases appears naturally: once we are in a hub near the destination, the probability that it is connected to a bigger hub closer to the destination sharply decreases, but at this point we do not need hubs anyway, and greedy routing directs us to smaller airports at shorter distances next to the destination.

This zoom out/zoom in mechanism works efficiently only if the coupling between the airport network topology and the underlying geography satisfies the following two conditions: the sufficient hubs condition and the sufficient clustering condition. The first condition ensures that a network has enough hub airports (high-degree nodes) to provide an increasing sequence during the zoom out phase. This condition is fulfilled by the real airport network and by other scale-free networks with small values of degree distribution exponent  $\gamma$ , because the smaller the  $\gamma$ , the larger the proportion of hubs in the network.

However, the presence of many hubs does not ensure that greedy routing will use them. Unlike humans, who can use their knowledge of airport size to selectively travel via hub airports, greedy routing uses only one con-

![](_page_4_Figure_1.jpeg)

<span id="page-4-0"></span>FIG. 4: Greedy routing in the airport network. Top: the structure of the single greedy-routing path from Toksook Bay to Ibiza. At each intermediate airport, the next hop is the airport closest to Ibiza geographically. Sizes of symbols representing the airports are proportional to the logarithm of their degrees. The bottom left figure shows the changing distance to Ibiza (in the x axis) vs. the degree of the visited airports (y axis, in logarithmic scale). Bottom right: the structure of greedy-routing paths between a collection of airports in the USA [\[36\]](#page-12-17). We include an airport pair in the collection if the distance between the airports is between 3900 and 4100 kilometers. The number of airport pairs in this collection is 7620. We use colour to indicate how often paths in the collection go through an airport of a given degree located at a given geographical distance from the destination: blue/red indicates exponentially less/more visits to those airports, or more specifically, the color is the logarithm of the normalised density of visited airports.

straint at each hop: minimise distance to the destination. Therefore, the network topology must satisfy the second condition, which ensures that Bethel is larger than Toksook Bay, Anchorage larger than Bethel, and so on. More generally, this condition is that the next greedy hop from a remote low-degree node likely has a higher degree, so that greedy paths typically head first toward the highly connected network core. But the network metric strength is exactly the required property: preference for connections between nodes nearby in the hidden space means that low-degree nodes are less likely to have connectivity to distant low-degree nodes; only high-degree nodes can have long-range connection that greedy routing will effectively select. The stronger this coupling between the metric space and topology (the higher α in Eq. [\(1\)](#page-2-0)), the stronger the clustering in the network.

To illustrate, imagine an airport network without sufficient clustering, one where the airport closest to our

![](_page_5_Figure_1.jpeg)

<span id="page-5-0"></span>FIG. 5: Probability that greedy routing travels to higher-degree nodes. More precisely, the probability  $P_{up}(k,d)$  that the greedy-routing next hop after a node of degree k located at distance d from a destination has higher degree  $k' \geq k$  and is closer to the destination. The distance legend in the right-bottom plot applies to all the plots. The results are for the large-graph limit  $N \to \infty$ .

destination (Ibiza) among all airports connected to our current node (Toksook Bay, Alaska) is not Bethel, which is bigger than Toksook Bay, but Nightmute, Alaska, a nearby airport of comparable size to Toksook Bay. As greedy routing first leads us to Nightmute, then to another small nearby airport, and then to another, we can no longer get to Ibiza in few hops. Worse, travelling via these numerous small airports, we could reach one with no connecting flights heading closer to Ibiza. Our greedy routing would be stuck at this airport with an unsuccessful path.

These factors explain why the most navigable topologies correspond to scale-free networks with small exponents of the degree distribution, i.e., a large number of hubs, and with strong clustering, i.e., strong coupling between the hidden geometry and the observed topology.

## V. THE STRUCTURE OF GREEDY-ROUTING PATHS

We observe the discussed zoom-out/zoom-in mechanism in analytical calculations and numerical simulations. Specifically, we calculate (in Appendix F) the

![](_page_5_Figure_7.jpeg)

<span id="page-5-1"></span>The structure of greedy-routing paths. We visualise the results of our simulation of greedy routing in modelled networks with different values of  $\gamma$  and  $\alpha$  observed in real complex networks. The hidden distance between the starting point and the destination is always approximately  $10^4$ , and the network size N and number of attempted paths is always  $10^5$  for each  $(\gamma, \alpha)$  combination, but the number of successful paths and path hop-lengths vary, cf. Figs. 2,3. All paths start and end at low-degree nodes located, respectively, in the left- and right-bottom corners of the diagrams (see top left plot). For each  $(\gamma, \alpha)$  we depict a single typical path in black and, as in Fig. 4, use colour to indicate how often paths included a node of a given degree located at a given distance from the destination. The simulations confirm that only when  $\gamma$  is small and  $\alpha$  is large does the average path structure follow the zoom-out/zoom-in pattern that characterises successful greedy routing in real networks, e.g., in the airport network in Fig. 4.

probability that the next hop from a node of degree k located at hidden distance d from the destination has a larger degree k' > k, in which case the path moves toward the high-degree network core, see Fig. 5. In the most navigable case, with small degree-distribution exponent and strong clustering, the probability of increasing the node degree along the path is high at low-degree nodes,

and sharply decreases to zero after reaching a node of a critical degree value, which increases with distance d. This observation implies that greedy-routing paths first propagate up to higher-degree nodes in the network core and then exit the core toward low-degree destinations in the periphery. In contrast, with low clustering, paths are less likely to find higher-degree nodes regardless of the distance to the destination. This path structure violates the zoom-out/zoom-in pattern required for efficient navigation.

Fig. 6 shows the structure of greedy-routing paths in simulations, further confirming our analysis. We again see that for small degree-distribution exponents and strong clustering (upper left and middle left), the routing process quickly finds a way to the high-degree core, makes a few hops there, and then descends to a low-degree destination. In the other, non-navigable cases, the process can almost never get to the core of high-degree nodes. Instead, it wanders in the low-degree periphery increasing the probability of getting lost at low-degree nodes.

## VI. DISCUSSION

Our main motivation for this work comes from longstanding scalability problems with the Internet routing architecture [37]. To route information packets to a given destination, Internet routers must communicate to maintain a coherent view of the global Internet topology. The constantly increasing size and dynamics of the Internet thus leads to immense and quickly growing communication and information processing overhead, a major bottleneck in routing scalability [38] causing concerns among Internet experts that the existing Internet routing architecture may not sustain even another decade [37]. Discovery of the Internet's hidden metric space would remove this bottleneck, eliminating the need for the inherently unscalable communication of topology changes. Instead routers would be able to just forward packets greedily to the destination based on hidden distances.

In a similar manner, reconstruction of hidden metric spaces underlying other real networks may prove practically useful. For example, in social or communication networks (e.g., the Web, overlay, or online social networks) hidden spaces would yield efficient strategies for searching specific individuals or content based only on local knowledge. The metric spaces hidden under some biological networks (such as neural, gene regulatory networks, signalling or even protein folding [39] pathways) can become a powerful tool in studying the structure of information or signal flows in these networks, enabling investigation of such processes without detailed global knowledge of the network structure or organisation.

The natural question we thus face is how to proceed toward discovery of the explicit structure of hidden metric spaces underlying real networks. We do not expect spaces underlying different networks to be exactly the same. For example, the similarity spaces of Web pages [9] and Wikipedia editors [11] likely differ. However, the main contribution of this work establishes the *general* mechanisms behind navigability of scale-free, strongly clustered topologies that characterise many different real networks. The next step is to find the common properties of hidden spaces that render them congruent with these mechanisms. Specifically, we are interested in what geometries of hidden spaces lead to such congruency [40].

In general, we believe that the present and future work on hidden metric spaces and network navigability will deepen our understanding of the fundamental laws describing relationships between structure and function of complex networks.

## Acknowledgments

We thank M. Ángeles Serrano for useful comments and discussions. This work was supported in part by DGES grant FIS2007-66485-C02-02, Generalitat de Catalunya grant No. SGR00889, the Ramón y Cajal program of the Spanish Ministry of Science, by NSF CNS-0434996 and CNS-0722070, by DHS N66001-08-C-2029, and by Cisco Systems.

# <span id="page-6-0"></span>APPENDIX A: A MODEL WITH THE CIRCLE AS A HIDDEN METRIC SPACE.

In our model we place all nodes on a circle by assigning them a random variable  $\theta$ , i.e., their polar angle, distributed uniformly in  $[0,2\pi)$ . The circle radius R grows linearly with the total number of nodes N,  $2\pi R = N$ , in order to keep the average density of nodes on the circle fixed to 1. We next assign to each node its expected degree  $\kappa$  drawn from some distribution  $\rho(\kappa)$ . The connection probability between two nodes with hidden coordinates  $(\theta, \kappa)$  and  $(\theta', \kappa')$  takes the form

$$r(\theta, \kappa; \theta', \kappa') = \left(1 + \frac{d(\theta, \theta')}{\mu \kappa \kappa'}\right)^{-\alpha}, \quad \mu = \frac{(\alpha - 1)}{2\langle k \rangle}, \text{ (A1)}$$

where  $d(\theta, \theta')$  is the geodesic distance between the two node on the circle, while  $\langle k \rangle$  is the average degree. One can show that the average degree of nodes with hidden variable  $\kappa$ ,  $\bar{k}(\kappa)$ , is proportional to  $\kappa$ .[41] This proportionality guarantees that the shape of the node degree distribution P(k) in generated networks is approximately the same as the shape of  $\rho(\kappa)$ . The choice of  $\rho(\kappa) = (\gamma - 1)\kappa_0^{\gamma - 1}\kappa^{-\gamma}$ ,  $\kappa > \kappa_0 \equiv (\gamma - 2)\langle k \rangle/(\gamma - 1)$ ,  $\gamma > 2$ , generates random networks with a power-law degree distribution of the form  $P(k) \sim k^{-\gamma}$ , where  $\gamma$  is a model parameter that regulates the heterogeneity of the degree distribution in the network. This parameter abstracts the heterogeneity of node degrees in real networks, where degree distributions may not perfectly

follow power laws, or may exhibit various forms of highdegree cut-offs [\[31,](#page-12-12) [42\]](#page-12-23). The specific effects are less important than the overall measure of heterogenity. We note that instead of a circle in our model we could use any isotropic space of any dimension [\[13\]](#page-11-12).

## <span id="page-7-1"></span>APPENDIX B: NUMERICAL SIMULATIONS.

Our model has three independent parameters: exponent γ of power-law degree distributions, clustering strength α, and average degree hki. We fix the latter to 6, which is roughly equal to the average degree of some real networks of interest [\[31,](#page-12-12) [32\]](#page-12-13), and vary γ ∈ [2.1, 3] and α ∈ [1.1, 5], covering their observed ranges in documented complex networks [\[1,](#page-11-0) [2,](#page-11-1) [3\]](#page-11-2). For each (γ, α) pair, we produce networks of different sizes N ∈ [10<sup>3</sup> , 10<sup>5</sup> ] generating, for each (γ, α, N), a number of different network instances—from 40 for large N to 4000 for small N. In each network instance G, we randomly select 10<sup>6</sup> sourcedestination pairs (a, b) and execute the greedy-routing process for them starting at a and selecting, at each hop h, the next hop as the h's neighbour in G closest to b in the circle. If for a given (a, b), this process visits the same node twice, then the corresponding path leads to a loop and is unsuccessful. We then average the measured values of path hop lengths τ and percentage of successful paths p<sup>s</sup> across all pairs (a, b) and networks G for the same (γ, α, N). Note that we are not concerned with the absolute values of the success ratio ps. Instead we use it as a measure of navigability to compare networks with different (γ, α, N). For this purpose we could use the success ratio of any (improved) modification of standard greedy routing.

#### APPENDIX C: SHORTEST PATH VS. SHORTEST TIME.

All results derived in the present paper are about finding short paths across a network topology. The total physical time from source to destination is implicitly assumed to be proportional to the number of hops. In real transportation systems, e.g. the Internet or the airport network, the finite capacity of nodes implies that the end-to-end path latency may be longer when intermediate nodes are congested. While our results most cleanly apply to uncongested systems, there are obvious modifications, such as choosing the second or third nearest rather than the nearest neighbor, that could still find nearly shortest paths while reducing and balancing load on the system.

## <span id="page-7-0"></span>APPENDIX D: THE MODEL VS. REAL NETWORKS: THE AUTONOMOUS SYSTEM LEVEL MAP OF THE INTERNET AND THE US AIRPORT NETWORK

The model we use in this work is not meant to reproduce any particular system but to generate a set of general properties, like heterogeneous degree distributions, high clustering, and a metric structure lying underneath. Yet, despite its simplistic assumptions, the model generates graphs that are surprisingly close to some real networks of interest, in particular the Internet at the Autonomous System level (AS) [\[31,](#page-12-12) [43\]](#page-12-24) and the network of airline connections among airports within the United States during 2006 (USAN) [\[36\]](#page-12-17). In the case of the Internet, we use two different data sets, the Internet as viewed by the Border Gateway Protocol (BGP) [\[31\]](#page-12-12) and the DIMES project [\[43\]](#page-12-24). The BGP (DIMES) network has a size of N ∼ 17446 (N = 19499) ASs, average degree hki = 4.7 (hki = 5), and average clustering C = 0.41 (C = 0.6). The US Airport Network is composed of US airports connected by regular flights (with more than 1000 passengers per year) during the year 2006. This results in a network of N = 599 airports, average degree hki ∼ 10.8 and average clustering coefficient C = 0.72.

Figs. [7](#page-8-0) and [8](#page-8-1) show a comparison of the basic topological properties of these networks with graphs generated with the model. In the case of the AS map, we use a truncated power law distribution ρ(κ) ∼ κ −γ , κ < κ<sup>c</sup> with exponent γ = 2.1 and κ<sup>c</sup> such that the maximum degree of the network is k<sup>c</sup> = 2400. For the USAN, we use γ = 1.6 and a maximum degree k<sup>c</sup> = 180, as observed in the real network. As it can be appreciated in both figures, the matching of the model with the empirical data is surprisingly good except for very low degree vertices. This is particularly interesting since we are not enforcing any mechanism to reproduce higher order statistics like the average nearest neighbours degree ¯knn(k) or the degree-dependent clustering coefficient ¯c(k). This can be understood as a consequence of the high heterogeneity of the degree distribution that introduces structural constraints in the network [\[44,](#page-12-25) [45\]](#page-12-26).

The airport network differs in several ways from our modelled networks: the distribution of airports in the geographic space is far from uniform; the airport degree distribution does not perfectly follow a power law; and it exhibits a sharp high-degree cut-off. However, the structure of greedy paths is surprisingly similar to that in our modelled networks in Fig. [6.](#page-5-1) The success ratio p<sup>s</sup> ≈ 0.64 and average length of successful paths τ ≈ 2.1 are also similar to those in our modelled networks of the corresponding size, clustering, and degree distribution exponent. These similarities indicate that the network navigability characteristics depend on clustering and heterogeneity of the airport degree distribution, and less so on how perfectly it follows a power law.

![](_page_8_Figure_1.jpeg)

<span id="page-8-0"></span>FIG. 7: Degree distribution P(k), average nearest neighbours' degree  $\bar{k}_{nn}(k)$ , and degree-dependent clustering coefficient  $\bar{c}(k)$  generated by our model with  $\gamma=2.1$  and  $\alpha=2$  compared to the same metrics for the real Internet map as seen by BGP data and the DIMES project.

<span id="page-8-1"></span>FIG. 8: Degree distribution P(k), average nearest neighbours' degree  $\bar{k}_{nn}(k)$ , and degree-dependent clustering coefficient  $\bar{c}(k)$  generated by our model with  $\gamma = 1.6$ ,  $\alpha = 5$  and a cut-off at  $k_c = 180$  compared to the same metrics for the real US airport network.

## APPENDIX E: HIERARCHICAL ORGANIZATION OF MODELED NETWORKS

The routing process in our framework resembles guided searching for a specific object in a complex collection of objects. Perhaps the simplest and most general way to make a complex collection of heterogenous objects searchable is to classify them in a hierarchical fashion. By "hierarchical," we mean that the whole collection is split into categories (i.e., sets), sub-categories, sub-sub-categories, and so on. Relationships between categories form (almost) a tree, whose leaves are individual objects in the collection [7, 8, 12, 40]. Finding an object reduces to the simpler task of navigating this tree.

k-core decomposition [47, 48] is possibly the most suitable generic tool to expose hierarchy within our modeled networks. The k-core of a network is its maximal subgraph such that all the nodes in the subgraph have k or more connections to other nodes in the subgraph. A node's coreness is the maximum k such that the k-core

contains the node but the k+1-core does not. The k-core structure of a network is a form of hierarchy since a k+1-core is a subset of a k-core. One can estimate the quality of this hierarchy using properties of the k-core spectrum, i.e., the distribution of k-core sizes. If the maximum node coreness is large and if there is a rich collection of comparably-sized k-cores with a wide spectrum of k's, then this hierarchy is deep and well-developed, making it potentially more navigable. It is poor, non-navigable otherwise.

In Fig. 9 we feed real and modeled networks to the Large Network visualization tool (LaNet-vi) [46] which utilizes node coreness to visualize the network. Fig. 9 shows that networks with stronger clustering and smaller exponents of degree distribution possess stronger k-core hierarchies. These hierarchies are directly related to how networks are constructed in our model, since nodes with higher  $\kappa$  and, consequently, higher degrees have generally higher coreness, as we can partially see in Fig. 9.

![](_page_9_Figure_1.jpeg)

<span id="page-9-1"></span>FIG. 9: k-core decompositions of real and modeled networks. The first two rows show LaNet-vi [46] network visualizations. All nodes are color-coded based on their coreness (right legends) and size-coded based on their degrees (left legends). Higher-coreness nodes are closer to circle centers. The third row shows the k-core spectrum, i.e., the distribution  $\mathcal{S}(k)$  of sizes of node sets with coreness k. The first column depicts two real networks: the AS-level Internet as seen by the Border Gateway Protocol (BGP) in [31] and the Pretty Good Privacy (PGP) social network from [32]. The rest of the columns show modeled networks for different values of power-law exponent  $\gamma$  in cases with weak ( $\alpha = 1.1$ ) and strong ( $\alpha = 5.0$ ) clustering. The network size N for all real and modeled cases is approximately  $10^4$ . Similarity between real networks and modeled networks with low  $\gamma$  and high  $\alpha$  is remarkable.

#### <span id="page-9-0"></span>APPENDIX F: THE ONE-HOP PROPAGATOR OF GREEDY ROUTING

To derive the greedy-routing propagator in this appendix, we adopt a slightly more general formalism than in the main text. Specifically, we assume that nodes live in a generic metric space  $\mathcal{H}$  and, at the same time, have intrinsic attributes unrelated to  $\mathcal{H}$ . Contrary to normed spaces or Riemannian manifolds, generic metric spaces do not admit any coordinates, but we still use the coordinate-based notations here to simplify the exposition below, and denote by  $\mathbf{x}$  nodes' coordinates in  $\mathcal{H}$ and by  $\omega$  all their other, non-geometric attributes, such as their expected degree  $\kappa$ . In other words, hidden variables  $\mathbf{x}$  and  $\omega$  in this general formalism represent some collections of nodes' geometric and non-geometric hidden attributes, not just a pair of scalar quantities. Therefore, integrations over  $\mathbf{x}$  and  $\omega$  in what follows stand merely to denote an appropriate form of summation in each concrete case

As in the main text, we assume that  $\mathbf{x}$  and  $\omega$  are independent random variables so that the probability density

to find a node with hidden variables  $(\mathbf{x}, \omega)$  is

$$\rho(\mathbf{x}, \omega) = \delta(\mathbf{x})\rho(\omega)/N, \tag{F1}$$

where  $\rho(\omega)$  is the probability density of the  $\omega$  variables and  $\delta(\mathbf{x})$  is the concentration of nodes in  $\mathcal{H}$ . The total number of nodes is

$$N = \int_{\mathcal{H}} \delta(\mathbf{x}) d\mathbf{x},\tag{F2}$$

and the connection probability between two nodes is an integrable decreasing function of the hidden distance between them,

$$r(\mathbf{x}, \omega; \mathbf{x}', \omega') = r[d(\mathbf{x}, \mathbf{x}')/d_c(\omega, \omega')],$$
 (F3)

where  $d_c(\omega, \omega')$  a characteristic distance scale that depends on  $\omega$  and  $\omega'$ .

We define the one-step propagator of greedy routing as the probability  $G(\mathbf{x}', \omega' | \mathbf{x}, \omega; \mathbf{x}_t)$  that the next hop after a node with hidden variables  $(\mathbf{x}, \omega)$  is a node with hidden variables  $(\mathbf{x}', \omega')$ , given that the final destination is located at  $\mathbf{x}_t$ .

To further simplify the notations below, we label the set of variables (x, ω) as a generic hidden variable h and undo this notation change at the end of the calculations according to the following rules:

$$\begin{array}{ccc}
(\mathbf{x},\omega) & \longrightarrow & h \\
\rho(\mathbf{x},\omega) & \longrightarrow & \rho(h) \\
d\mathbf{x}d\omega & \longrightarrow & dh \\
r(\mathbf{x},\omega;\mathbf{x}',\omega') & \longrightarrow & r(h,h').
\end{array}$$
(F4)

We begin the propagator derivation assuming that a

particular network instance has a configuration given by {h, ht, h1, · · · , hN−2} ≡ {h, ht; {hj}} with j = 1, · · · , N − 2, where h and h<sup>t</sup> denote the hidden variables of the current hop and the destination, respectively. In this particular network configuration, the probability that the current node's next hop is a particular node i with hidden variable h<sup>i</sup> is the probability that the current node is connected to i but disconnected to all nodes that are closer to the destination than i,

$$Prob(i|h, h_t; \{h_j\}) = r(h, h_i) \prod_{j(\neq i)=1}^{N-2} [1 - r(h, h_j)]^{\Theta[d(h_i, h_t) - d(h_j, h_t)]},$$
 (F5)

where Θ(·) is the Heaviside step function. Taking the average over all possible configurations {h1, · · · , hi−1, hi+1, · · · , hN−2} excluding node i, we obtain

$$Prob(i|h, h_t; h_i) = r(h, h_i) \left( 1 - \frac{1}{N-3} \bar{k}(h|h_i, h_t) \right)^{N-3},$$
(F6)

where

$$\bar{k}(h|h_i, h_t) = (N-3) \int_{d(h_i, h_t) < d(h', h_t)} \rho(h') r(h, h') dh'$$
(F7)

is the average number of connections between the current node and nodes closer to the destination than node i, excluding i and t.

The probability that the next hop has hidden variable h 0 , regardless of its label, i.e., index i, is

$$Prob(h'|h, h_t) = \sum_{i=1}^{N-2} \rho(h') Prob(i|h, h_t; h').$$
 (F8)

In the case of sparse networks, ¯k(h|h 0 , ht) is a finite quantity. Taking the limit of large N, the above expression simplifies to

$$Prob(h'|h, h_t) = N\rho(h')r(h, h')e^{-\bar{k}(h|h', h_t)}.$$
 (F9)

Yet, this equation is not a properly normalized probability density function for the variable h 0 since node h can have degree zero with some probability. If we consider only nodes with degrees greater than zero, then the normalization factor is given by 1 − e −k¯(h) . Therefore, the properly normalized propagator is finally

$$G(h'|h, h_t) = \frac{N\rho(h')r(h, h')e^{-\bar{k}(h|h', h_t)}}{1 - e^{-\bar{k}(h)}}.$$
 (F10)

We now undo the notation change and express this propagator in terms of our mixed coordinates:

$$G(\mathbf{x}', \omega' | \mathbf{x}, \omega; \mathbf{x}_t) = \frac{\delta(\mathbf{x}')\rho(\omega')}{1 - e^{-\bar{k}(\mathbf{x}, \omega)}} r \left[ \frac{d(\mathbf{x}, \mathbf{x}')}{d_c(\omega, \omega')} \right] e^{-\bar{k}(\mathbf{x}, \omega | \mathbf{x}', \mathbf{x}_t)},$$
(F11)

with

$$\bar{k}(\mathbf{x}, \omega | \mathbf{x}', \mathbf{x}_t) = \int_{d(\mathbf{x}', \mathbf{x}_t) > d(\mathbf{y}, \mathbf{x}_t)} d\mathbf{y} \int d\omega' \delta(\mathbf{y}) \rho(\omega') r \left[ \frac{d(\mathbf{x}, \mathbf{y})}{d_c(\omega, \omega')} \right].$$
 (F12)

In the particular case of the S <sup>1</sup> model, we can express this propagator in terms of relative hidden distances instead of absolute coordinates. Namely, G(d 0 , ω<sup>0</sup> |d, ω) is the probability that an ω-labeled node, e.g., a node with

expected degree κ = ω, at hidden distance d from the destination has as the next hop an ω 0 -labeled node at hidden distance d 0 from the destination. After tedious calculations, the resulting expression reads:

$$G(d', \omega'|d, \omega) = \begin{cases} \frac{(\gamma - 1)}{\omega'^{\gamma}} \left[ \frac{1}{(1 + \frac{d - d'}{\mu \omega \omega'})^{\alpha}} + \frac{1}{(1 + \frac{d + d'}{\mu \omega \omega'})^{\alpha}} \right] \exp\left\{ \frac{(1 - \gamma)\mu\omega}{\alpha - 1} \left[ \mathcal{B}(\frac{d - d'}{\mu \omega}, \gamma - 2, 2 - \alpha) - \mathcal{B}(\frac{d + d'}{\mu \omega}, \gamma - 2, 2 - \alpha) \right] \right\} & ; d' \leq d \\ \frac{(\gamma - 1)}{\omega'^{\gamma}} \left[ \frac{1}{(1 + \frac{d' - d}{\mu \omega \omega'})^{\alpha}} + \frac{1}{(1 + \frac{d + d'}{\mu \omega \omega'})^{\alpha}} \right] \exp\left\{ \frac{(1 - \gamma)\mu\omega}{\alpha - 1} \left[ \frac{2}{\gamma - 2} - \mathcal{B}(\frac{d' - d}{\mu \omega}, \gamma - 2, 2 - \alpha) - \mathcal{B}(\frac{d + d'}{\mu \omega}, \gamma - 2, 2 - \alpha) \right] \right\} & ; d' > d \end{cases}$$
(F13)

![](_page_11_Figure_2.jpeg)

<span id="page-11-18"></span>FIG. 10: Probability  $P_{up}(\omega/d^{1/2}, d)$ .

where we have defined function

$$\mathcal{B}(z,a,b) \equiv z^{-a} \int_0^z t^{a-1} (1+t)^{b-1} dt,$$
 (F14)

which is somewhat similar to the incomplete beta function  $B(z, a, b) = \int_0^z t^{a-1} (1-t)^{b-1} dt$ .

One of the informative quantities elucidating the structure of greedy-routing paths is the probability  $P_{up}(\omega, d)$  that the next hop after an  $\omega$ -labeled node at distance d from the destination has a higher value of  $\omega$ . The greedy-routing propagator defines this probability as

$$P_{up}(\omega, d) = \int_{\omega' > \omega} d\omega' \int_{d' < d} dd' G(d', \omega' | d, \omega), \quad (F15)$$

and we show  $P_{up}(\omega/d^{1/2},d)$  in Fig. 10. We see that the proper scaling of  $\omega_c \sim d^{1/2}$ , where  $\omega_c$  is the critical value of  $\omega$  above which  $P_{up}(\omega,d)$  quickly drops to zero, is present only when clustering is strong. Furthermore,  $P_{up}(\omega,d)$  is an increasing function of  $\omega$  for small  $\omega$ 's only when the degree distribution exponent  $\gamma$  is close to 2. A combination of these two effects guarantees that the layout of greedy routes properly adapts to increasing distances or graph sizes, thus making networks with strong clustering and  $\gamma$ 's greater than but close to 2 navigable.

</details>

<details>
<summary>**Scalable Distributed Algorithm for Approximate Nearest Neighbor Search Problem in High Dimensional General Metric Spaces**</summary>

# **Scalable Distributed Algorithm for Approximate Nearest Neighbor Search Problem in High Dimensional General Metric Spaces**

Yury Malkov, Alexander Ponomarenko, Andrey Logvinov, and Vladimir Krylov

MERA Labs LLC, Nizhny Novgorod, Russia {ymalkov,aponom,alogvinov,vkrylov}@meralabs.com

**Abstract.** We propose a novel approach for solving the approximate nearest neighbor search problem in arbitrary metric spaces. The distinctive feature of our approach is that we can incrementally build a non-hierarchical distributed structure for given metric space data with a logarithmic complexity scaling on the size of the structure and adjustable accuracy probabilistic nearest neighbor queries. The structure is based on a small world graph with vertices corresponding to the stored elements, edges for links between them and the greedy algorithm as base algorithm for searching. Both search and addition algorithms require only local information from the structure. The performed simulation for data in the Euclidian space shows that the structure built using the proposed algorithm has navigable small world properties with logarithmic search complexity at fixed accuracy and has weak (power law) scalability with the dimensionality of the stored data.

**Keywords:** Similarity Search, Nearest Neighbor, Approximate Nearest Neighbor, Small World, Distributed Data Structure, Metric space.

### **1 Introduction**

The scalability of any software system is limited by the scalability of its data structures. Massively distributed systems like BitTorrent or Skype are based on the distributed hash tables. While the latter have good scalability, their search functionality is limited to the exact element hash value matching. This limitation arises because small changes in an element value lead to large and chaotic changes in the hash value, making the hash-based approach inapplicable to the range search and the similarity search problems.

However, there are many applications (such as pattern recognition and classification [1], content-based image retrieval [2], machine learning [3], recommendation systems [4], searching similar DNA sequence [5], semantic document retrieval [6]) that require the similarity search rather than just exact matching. The nearest neighbor search (NNS) problem is a mathematical formalization for the similarity search. It is defined as follows: we need to find the closest object *p X* ∈ from a finite set of objects *X* ⊆ to a given query *q* ∈ , where is a set of all possible objects (the

G. Navarro and V. Pestov (Eds.): SISAP 2012, LNCS 7404, pp. 132–[147,](#page-15-0) 2012.

data domain). Closeness or proximity of two objects ' '' *o o*, ∈ is defined as a distance function ' <sup>σ</sup>( , '') *o o* .

A naïve solution for the NNS problem is to calculate the distance function <sup>σ</sup> between q and every element from X. This leads to linear search time complexity scalability with the number of elements which is much worse than the scalability of structures with the exact value search and makes it almost impossible to use the NNS for extreme size datasets.

We suggest a solution for the nearest neighbor search problem, a data structure with a small world network topology represented by a graph*GVE* ( ) , , where every object *<sup>i</sup> o* from *X* is uniquely associated with a vertex *<sup>i</sup> v* from *V* . Searching for the closest element to the query *q* from the data set *X* takes a form of searching for a vertex in the graph *G* .

We chose this approach based on the following:

- There are many existing well-developed algorithms for building small world networks for some special cases [7].
- Small world networks principally have no root element.
- All operations (addition and search) use only local information and can be initiated from any element that was previously added to the structure.

This gives an opportunity for building decentralized similarity search oriented storage systems where physical data location doesn't depend on the content because every data object can be placed on an arbitrary physical machine and can be connected with others by links like in p2p systems. Such storage systems can provide a simultaneous access to large numbers of users performing data search and addition, have good fault tolerance and are highly scalable in terms of performance and capacity.

One of the basic vertex search algorithms in graphs with metric objects is the greedy search algorithm. It has a simple implementation and can be initiated from any vertex. In order for a result of the algorithm to be always the exact nearest neighbor to any query, the network must contain the Delaunay graph as its subgraph, which is dual to the Voronoi tessellation [8]. However, there are major drawbacks associated with the Delaunay graph, it requires some knowledge of metric space internal structures [9] and it suffers from the curse of dimensionality [8]. Moreover the requirement of the search for the exact nearest neighbor can be not necessary (optional) for the applications described above. So the problem of finding the exact nearest neighbor can be substituted by the approximate nearest neighbor search, and thus we don't need to support the whole/exact Delaunay graph.

For the greedy search algorithm to be logarithmically scalable, the small world network should have the navigation property [7].

In this paper we present a very simple algorithm for the data structure construction based on a small world network topology with a graph *GV E* (, ) which uses the greedy search algorithm for the approximate nearest neighbor search problem. The graph *GVE* ( ) , contains an approximation of the Delaunay graph and has long-range links together with the small-world navigation property. The search algorithm has an ability to adjust the accuracy of search without modification of the structure. Presented algorithms do not use the coordinate representation and do not presume the properties of linear spaces, because they are based only on the metric computation between the objects, and therefore are applicable to data from general metric spaces. It is shown experimentally that the dimensionality dependence is polynomial for a vector data.

### **2 Related Works**

All papers that are dedicated to the nearest neighbor search problem can be divided into four categories: centralized nearest neighbor search structures; centralized approximate exact nearest neighbor search structures, distributed exact nearest neighbor search structures and distributed approximate nearest neighbor search structures.

#### **2.1 Centralized Exact Nearest Neighbor Search Structures**

Kd-tree[10] and quadra trees[11] were among the first works on the NNS problem. They perform well in 2-3 dimensions (search complexity is close to *O n* (log ) ), but the analysis of the worst case for that structures[12] indicates 1 1/ (\* ) *<sup>d</sup> Od N* <sup>−</sup> search complexity, where *d* is the dimensionality.

Other structures which have a tree topology such as variants of kd-trees, R-trees and structures based on space-filling curves are surveyed in [13]. They also have good performance when searching in a low-dimension ( *d* < 4 ) metric space, but they quickly lose their effectiveness with the increasing number of dimensions [14].

In general, presently there are no methods for effective exact NNS in high-dimensionality metric space. The reason behind this lies in the "curse" of dimensionality [15]. To avoid the curse of dimensionality while retaining the logarithmic scaling on the number of elements, it was proposed to reduce the requirements for the NNS problem solution, making it approximate (ANN).

#### **2.2 Centralized Approximate Nearest Neighbor Search Structures**

Thus a large number of papers appeared which proposed to search for the nearest neighbor with predefined accuracy ε (ε-NNS). For example, Arya and Mount proposed methods with search complexity <sup>3</sup> *O n* (log ), but preprocessing requires <sup>2</sup> *O n*( ) and the algorithm was applicable only to data from *E<sup>d</sup>* [16] .

Kleinberg proposed two methods [17] for solving ε-NNS. First method requires <sup>2</sup> (n log ) *<sup>d</sup> O d* preprocessing time and query time polynomial in *d*, ε , and log *n* . The other method with preprocessing time polynomial in *d*, ε , and *n*, but with query time <sup>3</sup> *On d n* ( log ) + . Also both methods are applicable only to data from *E<sup>d</sup>* .

The first algorithms with search complexity polynomial in *d* , log *n* , *ε* -1 and polynomial preprocessing time for fixed *ε* were proposed by Indyk and Motwani in [18] and Kushilevitz, Ostrovsky and Rabani in [19]. Indyk and Motwani were the first ones to relax ε-ANN problem to approximate point location in equal balls (ε-PLEB). For the formulation of the problem in ε-PLEB points in metric space expand to the balls with center at this point and radius (1+ *ε*)*r,* it is necessary to determine which ball belongs to the query *q* . Also in [18] proposed a second method, which uses the concept of locality-sensitive hashing in regard to formulation of the problem ε-PLEB, with search time 1/(1 <sup>ε</sup>) O(n ) <sup>+</sup> . This method however requires near quadratic memory (for small ε). In addition, the first method is applicable only for <sup>d</sup> E , and the second for the Hamming space.

In general, the concept of locality-sensitive hashing has become popular in the last decade to solve the ANN problem. Other works using the concept of locality-sensitive hashing are [20], [21]. But they all have the same major drawback: each algorithm is focused on a narrow class of metrics such as Hamming distance, Jakarta or *sl* norms for Euclidean space.

In [22,23] there were proposed non-distributed algorithms for the approximate k-NN problem suitable in general spaces performing well even in case of high dimensionality. The drawback for the ordering permutations index [23] is that it has a part of search algorithm with a CPU time linear dataset size scaling, and [22] is an essentially static index.

### **2.3 Distributed Exact Nearest Neighbor Search Structures**

There are a number of distributed structures that doesn't support nearest neighbor search in general metric spaces but provide search for interval queries in attributebased (vector) data or simple Euclidian space. MAAN [24], SCRAP[25] , Mercury [26] support multi-dimensional range queries and Voronet [27] is p2p network oriented to search nearest neighbor in E<sup>2</sup> based on Voronoi tessellation [8]. Every peer has coordinates in E2 and has links to all neighbors of its Voronoi region. For the logarithmic navigation Voronet supports long-range links.

The only metric-based distributed structures are M-Chord [28], GHT [29] and MCAN[25]. MCAN uses a pivot-based technique to map the high dimensional metric data to an N-dimensional vector space, and then uses CAN protocol as its underlying structured P2P system, however they all suffer from the curse of dimensionality.

#### **2.4 Distributed Approximate Nearest Neighbor Search Structures**

Authors in [30] explain how to use locality-sensitive hashing scheme for building the structure in a distributed environment. They suggest using a two-level mapping from a d-dimensional space to the peer identifier space. However the lack of versatility inherent to all LSH schemes remains as its main drawback.

Kleinberg's work [7] has shown the possibility of using navigable small world networks for finding the nearest neighbor with the greedy search algorithm. The algorithm relied on long-range links following power-law length distribution for navigation and 2-dimensional lattice for correctness of the results. In Voronet[27] the approach was extended to arbitrary 2-dimensional data by building a two dimensional Delaunay tessellation instead of a regular lattice. In their next work [31] they have weakened the requirements on the exactness of the search in order to avoid the curse of dimensionality for the d-dimension Euclidian space. The algorithm approximates the Delaunay graph by selecting 2 1 *d* + neighbors that minimize the volume of the corresponding Voronoi cell. The algorithm is rather complicated; it relies heavily on the quality of the Delaunay graph approximation, it has to be repeated iteratively to reach acceptable accuracy and in principle works only in the Euclidian space. The work also presented some sophisticated algorithms for managing the long range links.

### **3 Structure Definition**

The structure *S* is constructed as a small world network represented by a graph *GV E* (, ) , where objects from the set *X* are uniquely mapped to vertices from the set *V* . The set of edges *E* is determined by the structure construction algorithm. Since each vertex is uniquely mapped to an element from the set *X* , we will use the terms "vertex", "element" and "object" interchangeably. We will use the term "friends" for vertices that share an edge. The list of vertices that share a common edge with the vertex *<sup>i</sup> v* is called the friend list of the vertex *<sup>i</sup> v* .

We use a variant of the greedy search algorithm as a base algorithm for the NNS. It traverses the graph from an element to an element each time selecting the friend closest to the query until it reaches a local minimum. See a detailed description of the algorithm in the section 4.

Links (edges) in the graph serve two distinct purposes. There is a subset of shortrange links, which are used as an approximation of the Delaunay graph[8] required by the Greedy Search algorithm. Another subset is the long-range links, which are used for logarithmic scaling of the Greedy Search, they are responsible for the navigation small world properties of the constructed graph similar to the ones in Kleinberg's [7] work. The structure is illustrated on the Fig. 1.

In our work we focus on the approximation of the Delaunay graph and ways to nullify the errors rising from of the approximation. It can be studied independently because there is a very simple and strict way to create long range links for a predefined data set (see the section 5).

All queries in the structure are independent, they can be done in parallel and if the elements are placed randomly on physical computer nodes the processing query load is shared evenly across physical nodes. And the performance of the system (parallel queries per second) is limited only by the number of the nodes.

![](_page_5_Figure_2.jpeg)

**Fig. 1.** Graph representation of the structure. Circles (vertices) are the data in metric space, **black** edges are the approximation of the Delaunay graph, and **red** edges are long range links for logarithmic scaling. Arrows show a sample path of the greedy algorithm from an enter point to a query (shown green).

## **4 Search Algorithm**

#### **4.1 Greedy Search**

The basic search algorithm traverses the edges of the graph *GV E* (, ) from one vertex to another. The algorithm takes two parameters: query and the vertex \_ [ ] *V VG enter point* ∈ which is the starting point of a search (the entry point). Starting from the entry point at each vertex the algorithm computes a metric value from the query q to each vertex from the friend list of the current vertex and then selects a vertex with the minimal metric value. If the metric value between the query and the selected vertex is smaller than the one between the query and the current element, then the algorithm moves to that (new) vertex. The algorithm stops when it reaches a local minimum, a vertex whose friend list doesn't contain a vertex that is closer to the query than the vertex itself. The algorithm:

```
Greedy_Search(q: object, venter_point: object) 
1 vcurr ← venter_point; 
2 σmin ← σ(q, vcurr); vnext ← NIL; 
3 foreach vfriend ∈ vcurr.getFriends() do
4 if σfr ← σ(query, vfriend) < σmin then
5 σmin ← σfr; 
6 vnext ← vfriend;
7 if vnext = Nil then return vcurr; 
8 else return Greedy_Search(q, vnext);
```

The element which is a local minimum with respect to the query *q* ∈ can be either the true closest element to the query *q* from the entire set of elements of *X* , or a false closest.

If every element in the structure had in their friend list all of its Voronoi neighbors, then this would preclude the existence of false local minima. Maintaining this condition is equivalent to constructing the Delaunay graph, which is dual to the Voronoi diagram.

It turns out that it is impossible to determine exact Delaunay graph for an unknown metric space [9] (excluding the variant of the complete graph) so we cannot avoid the existence of local minima. For the problem of approximate searching as defined above it is not an obstacle since approximate search does not require the entire Delaunay graph [31].

Note that there is a distinction from the ANN problem defined in the works [16], [17] where it is expressed in terms of ε-neighborhood for which if there are several elements within the ε of the true nearest neighbor the result of the query can be any of these elements with comparable probabilities. There are no constrains on an absolute value of the distance between the false NN result and true NN result in our structure. Inaccuracy of the algorithm is «topological» in our case, meaning that the most likely result (e.g. with probability 0.95) is the true nearest neighbor, if not, the most likely it will be the second closest and so on with sharply decreasing probability. It may be more convenient to use such definition when the data distribution is highly skewed and it is hard to define one ε for all regions at the same time.

#### **4.2 Multi-search**

In order to diminish search errors arising in a network with local minima, we propose a following modification of the search algorithm. We use a series of *m* searches initiated from random vertices and choose a result element that is closest to the query from the set of found elements. Since the greedy search Greedy\_Search(q, venter-Point ϵ V)is unambiguous, for each entry point venterPoint ϵ V it either results in a success, finding the true nearest neighbor, or in a failure, finding an element that is not the nearest neighbor of *q*.

Thus a search of the closest element to a fixed query *q* may result in finding the true nearest neighbor (a global minimum) or a false nearest neighbor depending on the entry point from which the search algorithm started (see Fig. 2).

Since we can choose an entry point at random, there is a probability *p* of finding the true closest element to a particular element q. Moreover, this probability is always nonzero, because it is always possible to choose the exact nearest neighbor as an entry point, which subsequently will be returned by the greedy search algorithm. As an example the probability of finding query element in Fig. 2 is about 73% since there are 8 elements for which taken as the entry point the algorithm will succeed and 3 elements for which he will not (3/8 results in 73%).

If for a fixed query element probability of finding the true closest in a single search attempt is *p* then probability of finding the true closest element in at least one of m attempts is 1 (1 )*<sup>m</sup>* − − *p* , thus failure probability decreases exponentially with the number of search attempts. Thus we can improve the search precision, increasing the parameter m - the number of searches from random entry points. For example in the Fig. 2 for m =5 the result probability is 99.985%, which is more than sufficient for the most applications.

The modified greedy search algorithm:

```
Multi_Search(object q, integer: m) 
1 results: SET[objects]; 
2 for (i ← 0; i < m; i++) do 
3 entry_point ← getRandomEntryPoint(); 
4 local_min ← Greedy_Search(query, entry_point) 
5 if local_min ∉ results then
6 results.add(result); 
7 return results;
```

By selecting the closest element from the results we get an answer to the query.

If m is comparable to the number of elements in the structure, the algorithm becomes an exhaustive search, assuming that entry points are never reused. If the graph of the network has the small-world properties, then it is possible to choose a random vertex in a number of random steps proportional to log *n* , which doesn't affect the overall logarithmic search complexity. Therefore the overall complexity of a search will increase in no more than m times.

![](_page_7_Picture_7.jpeg)

**Fig. 2.** An illustration of the multisearch approach. **Blue** circles represent metric space elements for which taken as entry points for the greedy algorithm it will succeed finding the true NN for a query (**green** circle). **Red** circles represent elements for which taken as entry points the algorithm will stuck in a local minimum. **Arrows** represent gradients direction of the greedy search algorithm. The probability of finding the query in a single search is about 73%. For the multisearch algorithm with m =5 it is 99.985%.

### **5 Data Addition Algorithm**

Since we build an approximation of the Delaunay graph, there is a great freedom of choice of the construction algorithm. The main goal of all the works is to minimize the probability of the false local minima while the keeping number of links small. Some approaches are based on knowledge of topology of a metric space being used. For example in [31] it is proposed to build an approximate Delaunay graph which would minimize a volume of a Voronoi region (computed by the Monte-Carlo method) for a fixed number of edges for each vertex in the graph, this was done by iterating a selection of neighbors of every node in the graph several times. We propose to assemble the structure by adding elements one by one and connecting them on each step with the k closest objects which are already in the structure. It is based on the idea that intersection of the set of elements which are Voronoi neighbors and the k closest elements should be large. Another advantage of this approach was shown empirically in for one-dimensional data[32]. A graph created by such algorithm with data arriving in random order has small world navigation properties without any additional algorithms. That allows us to fully concentrate on the short-range links which approximate the Delaunay graph.

In this work we use a variant of the algorithm which is distinguished by the fact that the search for the k nearest elements uses a series of searches (an analogy to the multi-search, see 4.2).The algorithm takes three parameters: an object to be added to the structure and two positive integer numbers k and w. First, the algorithm determines a set of local minima using the procedure Multi\_Search (see 4.2), which produces a series of w searches using random enter points. After that the algorithm determines a neighborhood u which contains all neighbors of the each found local minima. The set u is sorted in ascending order by distance from the object new\_object to be added. After that new\_object is connected with first k nearest elements from the set u.

```
Nearest_Neighbor_Add(object: new_object, integer: k, integer: w) 
1 SET[object]: localMins ← Multi_Search (new_object, w); 
2 SET[object]: u ← ∅ ; //neighborhood; 
3 foreach object: local_min ∈ localMins do
4 u ← u ∪ local_min.getFriends(); 
6 sort the set u so to satisfy the condition σ (u[i], 
new_object) < σ (u[i+1], new_object) 
7 for (I ← 0; i < k; i++) do 
8 u[i].connect(new_object); 
9 new_object.connect(u[i]);
```

The choice of the parameter k is not clear, it depends on the space, but it can be evaluated automatically for an unknown space with a distributed algorithm; we are planning to describe it in our next works. Note that as in 4.2 setting w to a big number is equivalent to an exhaustive search of the closest elements in the structure. More on the choice of w and k see in the next section.

### **6 Test Results and Discussion**

#### *Test Data*

We have implemented the algorithms presented above in order to validate our assumptions about the scalability of the structure and to evaluate its performance. For a test dataset we have used:

- Uniformly distributed random points with a L2 (Euclidean distance) proximity function (up to 10<sup>6</sup> elements).
- To test our algorithm in a general metric space we have used a database of chemical compounds [33] with a Tanimoto [34] distance function. We have randomly selected 105 elements from the database to test the algorithm.
- A subset of the TREC-3 documents collection containing 24276 documents[23] for comparison with other works.

#### *Small World*

To verify the small world properties of the proposed structure we have measured the average path length induced by the greedy search algorithm for the vectors and chemical compounds (see Fig. 3). The plot clearly shows a logarithmic dependence on the dataset size proving it is a navigable small world. Thus the complexity of a single search scales logarithmically. It can be shown that the small world properties retain at any size (we are going to focus on it in one of our next works). Note that for bigger dimensionalities dependence is weaker due to smaller diameter of a set at a fixed number of elements.

#### *Construction Parameters*

We adjusted the number of search attempts m, so that the probability of finding the true closest element to the query was not less than a fixed value (we took 95% as a reference).

To test the scaling of the search algorithm with the number of elements *n* we have plotted (see Fig. 4) the number of multi-searches m required to get the 95% true nearest neighbor rate versus the size of the dataset for *d*=10 and different w parameters of the construction algorithm. For w=20 the dependence is clearly logarithmic up to 106 elements. For low values of w the algorithm complexity dependence deviates from the expected. Arrows denote the point where the dependence deviates from the logarithmic for w=1..4. One can see that the points are almost equidistant in the logarithmic scale.

So, if we need to get the logarithmic scaling up to *n* elements we have to have w > ×*A n* log ;(6.1) ( ) , where *A* is a constant value. And the overall complexity of both the search and the construction algorithms can be made logarithmic at the same time. Such dependence on the construction parameters can be easily understood. For the low w parameters the probability of finding the true nearest neighbor to a new element is low and the algorithm cannot choose the closest neighbors links correctly. The number of searches required to get *P* close to unity scales logarithmically with the

size of the dataset, leading to equation (6.1). We can set w high enough for any reasonable size of the dataset (like  $10^{100}$ ) while keeping acceptable construction complexity or if the size of the dataset is known (or evaluated dynamically) we can always set the parameters optimal and maintain an overall logarithmic scaling.

![](_page_10_Figure_3.jpeg)

![](_page_10_Figure_4.jpeg)

**Fig. 3.** The average hop count induced by a greedy search algorithm for different dimensionality Euclid data and for a chemical compounds dataset (k=10, w=20). The navigable small world properties are evident from the logarithmic scaling.

**Fig. 4.** The number of multi-searches required to get the 95% true nearest neighbor rate versus the size of the dataset for different w parameters of the construction algorithm. Arrows denote points where the dependence deviates from the logarithmic. The points are almost equidistant in the log scale.

Fig. 5 presents the number of multi-searches m for the same parameters as in Fig. 4 setting  $w = [A \times \log(n) - c]$  for A = 1.5, 2, 2.5, 3. For any value of A the scaling stays logarithmic but at expense of worse complexities for the small values of A. Setting A higher than 2.5 does not affect the complexity of the search.

To define the best choice of the parameter k we have plotted the probability of failing finding the true nearest neighbor versus the fraction of visited elements (metric calculations) for d=10 and different parameters k (see Fig. 6). For k smaller than 2...3·d there is a significant fall of performance, while for bigger values of k there is a very slow decay with the rise of the parameter. For d=2...50 it was verified that the optimal value for k is close to  $3 \cdot d$ . Also one can see that the probability of a wrong NN result falls exponentially with the fraction of visited elements confirming assumptions from section 4.

The bottom line is that the optimal value for k is  $3 \cdot d$ ; the value of w has to be dynamically changed  $A \times \log(n_{current})$  with a constant A or set fixed to  $A \times \log(n)$ , where n is the maximum database size.

![](_page_11_Figure_2.jpeg)

**Fig. 5.** The number of multi-searches required **Fig. 6.** Probability of failing finding the true to get the 95% true nearest neighbor rate versus nearest neighbor versus fraction of visited the size of the dataset for a logarithmic scaling elements for d=10,  $n=2.6\cdot10^5$  of w (A=1.5, 2, 2.5, 3)

#### Absolute Speedup and Scaling

The graph (Fig. 7) shows the percent of visited (extracted) elements (vertical) versus the dataset size (horizontal) in a log-log scale for different dimensionalities. k was fixed to  $3 \cdot d$  for all trials and w was fixed to a big number. The plot shows that with the increase of the number of elements in the structure, the percentage of visited elements decreases, and the curves become close to straight lines with an angle of 45 degrees (corresponding to the 1/n law of decay). This means that the single search complexity does not change significantly with the size of the dataset. From the graphs the overall scaling for complexity of the search can be extracted. It turns out that it scales as  $\log^2(n)$ , just as it might be expected. One "log" coming from the average path length and the other is from the number of multi-searches.

We have also plotted the average fraction of visited elements for  $n=2.6 \cdot 10^5$  in a log-log scale to check the dimensionality dependence (see Fig. 8), it can be approximated by a  $d^{1.7}$  power law. Judging on the Fig. 7 it seems that for low d with rise of n at some size the difference in performance between the dimensionalities diminishes. It might be suspected that such behavior will be the same for bigger dimensionalities but it requires further study.

Overall, the measured search complexity scaling for  $n>10^5$  and d=5..100 is not worse than  $d^{1.7}\times \ln^2(n)\times \ln(1/P_{fail})$  and the construction complexity (deduced from the search complexity) is  $d^{1.7}\times n\ln^2(n)$ , where  $P_{fail}$  is an acceptable probability of failing finding the true nearest neighbor.

To get an idea about how the algorithm performs compared to the other k-NN algorithms we have run a test from [23], a subset of collection TREC-3 documents containing 24276 documents. For a k-NN algorithm we have used a part of the construction algorithm from section 5. To get the averaged 90% recall of 9 documents

from the database it required visiting 5% of the database compared to about 2% from the [23]. We believe it is a good result for such a simplified algorithm. We have also made a slight modification of the k-NN search algorithm, changing the stop condition (the algorithm continues to travel the graph while it can improve distance for the k-th element) yielding about 2.5% extraction of the database at the same recall, very close to the state of art.

![](_page_12_Figure_3.jpeg)

![](_page_12_Figure_4.jpeg)

Fig. 7. Average fraction of visited elements Fig. 8. Average fraction of visited elements within a single NN-search versus the size of within a single Nearest Neighbor search the dataset for different dimensionality and versus the dimensionality of the dataset for ndata types

= 262k with a power-law fit

#### 7 Conclusions and Future Work

We have proposed a method of organizing data into a distributed small world graph structure suited for the distributed approximate nearest neighbor search in a metric space. The algorithm uses no information about inner topology of the data and space, thus it is applicable to arbitrary metric data. The algorithm is very simple and easy to understand. All elements in the structure are of the same type, there is no central or root element. There is no dedicated algorithm for managing the small world properties, they arise automatically. The algorithm uses only local information on each step and can be initiated from any vertex. The search is approximate from the topological point of view. An unsuccessful Nearest Neighbor query typically results in the second

Accuracy of the approximate search can be tuned by using multiple searches with a random initial vertex and the probability of finding a false nearest neighbor decreases exponentially with the number of multi-searches.

The performed simulation for data in the Euclidian space shows that the structure built using the proposed algorithm has the navigable small world property. Both logarithmic search and construction complexity at fixed accuracy can be achieved with appropriate algorithm parameters. There are reasons to believe such behavior will be retained for any dataset size. The algorithm also shows a power law scalability of metric calculation count with dimensionality of the stored data. Simulations for chemical compounds and documents have shown the effectiveness of the approach for non-Euclidian spaces comparable to best algorithms.

The proposed structure was intentionally slimmed-down to demonstrate its scalability over the dataset size and dimensionality. There are several ways to optimize the structure in order to get lower complexity or/and better accuracy constants, such as:

- More complicated algorithms for node friends selection (see sec. 5). It is obvious that selecting nearest neighbors as friends is not the best way to approximate Delaunay graph since it takes into account only distances between the new element and candidates and neglects distances between the candidates. Knowledge of internal structure of the metric space can boost up search performance. In [31] is was shown that for Euclidean space the accuracy of a single search can be significantly increase while keeping the number of friends per node fixed.
- More complicated search algorithms can be used. Excluding already visited elements in consequent searches or/and changing the stop parameters in search algorithm can potentially reduce the number of metric computations several times at the same accuracy.
- More complicated algorithms for navigable small world creation suitable for correlated (non-random) data.

As a future work, we are going to enhance the performance of the structure while keeping good scalability and distributed nature and to make a detail comparison with the state of art algorithms from the area.

Summing up, simplicity, high scalability both with size and data dimensionality and the distributed nature of the algorithm are a good base for building many realworld extreme dataset size high dimensionality similarity search applications.

</details>

<details>
<summary>Skip Lists: A Probabilistic Alternative to Balanced Trees</summary>

# Skip Lists: A Probabilistic Alternative to Balanced Trees

Skip lists are a data structure that can be used in place of balanced trees. Skip lists use probabilistic balancing rather than strictly enforced balancing and as a result the algorithms for insertion and deletion in skip lists are much simpler and significantly faster than equivalent algorithms for balanced trees.

# William Pugh

Binary trees can be used for representing abstract data types such as dictionaries and ordered lists. They work well when the elements are inserted in a random order. Some sequences of operations, such as inserting the elements in order, produce degenerate data structures that give very poor performance. If it were possible to randomly permute the list of items to be inserted, trees would work well with high probability for any input sequence. In most cases queries must be answered on-line, so randomly permuting the input is impractical. *Balanced* tree algorithms re-arrange the tree as operations are performed to maintain certain balance conditions and assure good performance.

Skip lists are a probabilistic alternative to balanced trees. Skip lists are balanced by consulting a random number generator. Although skip lists have bad worst-case performance, no input sequence consistently produces the worst-case performance (much like quicksort when the pivot element is chosen randomly). It is very unlikely a skip list data structure will be significantly unbalanced (e.g., for a dictionary of more than 250 elements, the chance that a search will take more than 3 times the expected time is less than one in a million). Skip lists have balance properties similar to that of search trees built by random insertions, yet do not require insertions to be random.

Balancing a data structure probabilistically is easier than explicitly maintaining the balance. For many applications, skip lists are a more natural representation than trees, also leading to simpler algorithms. The simplicity of skip list algorithms makes them easier to implement and provides significant constant factor speed improvements over balanced tree and self-adjusting tree algorithms. Skip lists are also very space efficient. They can easily be configured to require an average of  $1^{-1}/_{3}$  pointers per element (or even less) and do not require balance or priority information to be stored with each node.

#### SKIP LISTS

We might need to examine every node of the list when searching a linked list (*Figure 1a*). If the list is stored in sorted order and every other node of the list also has a pointer to the node two ahead it in the list (*Figure 1b*), we have to examine no more than  $\lceil n/2 \rceil + 1$  nodes (where n is the length of the list).

Also giving every fourth node a pointer four ahead (*Figure* 1c) requires that no more than  $\lceil n/4 \rceil + 2$  nodes be examined. If every  $(2^i)^{\text{th}}$  node has a pointer  $2^i$  nodes ahead (*Figure* 1d), the number of nodes that must be examined can be reduced to  $\lceil \log_2 n \rceil$  while only doubling the number of pointers. This data structure could be used for fast searching, but insertion and deletion would be impractical.

A node that has k forward pointers is called a *level* k node. If every  $(2^i)^{th}$  node has a pointer  $2^i$  nodes ahead, then levels of nodes are distributed in a simple pattern: 50% are level 1, 25% are level 2, 12.5% are level 3 and so on. What would happen if the levels of nodes were chosen randomly, but in the same proportions (e.g., as in Figure 1e)? A node's  $i^{th}$  forward pointer, instead of pointing  $2^{i-1}$  nodes ahead, points to the next node of level i or higher. Insertions or deletions would require only local modifications; the level of a node, chosen randomly when the node is inserted, need never change. Some arrangements of levels would give poor execution times, but we will see that such arrangements are rare. Because these data structures are linked lists with extra pointers that skip over intermediate nodes, I named them  $skip\ lists$ .

## SKIP LIST ALGORITHMS

This section gives algorithms to search for, insert and delete elements in a dictionary or symbol table. The *Search* operation returns the contents of the value associated with the desired key or *failure* if the key is not present. The *Insert* operation associates a specified key with a new value (inserting the key if it had not already been present). The *Delete* operation deletes the specified key. It is easy to support additional operations such as "find the minimum key" or "find the next key".

Each element is represented by a node, the level of which is chosen randomly when the node is inserted without regard for the number of elements in the data structure. A *level i* node has *i forward* pointers, indexed 1 through *i*. We do not need to store the level of a node in the node. Levels are capped at some appropriate constant *MaxLevel*. The *level* of a list is the maximum level currently in the list (or 1 if the list is empty). The *header* of a list has forward pointers at levels one through *MaxLevel*. The forward pointers of the header at levels higher than the current maximum level of the list point to NIL.

![](_page_1_Figure_0.jpeg)

FIGURE 1 - Linked lists with additional pointers

# **Initialization**

An element NIL is allocated and given a key greater than any legal key. All levels of all skip lists are terminated with NIL. A new list is initialized so that the the *level* of the list is equal to 1 and all forward pointers of the list's header point to NIL. **Search Algorithm**

We search for an element by traversing forward pointers that do not overshoot the node containing the element being searched for (Figure 2). When no more progress can be made at the current level of forward pointers, the search moves down to the next level. When we can make no more progress at level 1, we must be immediately in front of the node that

## **Insertion and Deletion Algorithms**

contains the desired element (if it is in the list).

To insert or delete a node, we simply search and splice, as shown in Figure 3. Figure 4 gives algorithms for insertion and deletion. A vector *update* is maintained so that when the search is complete (and we are ready to perform the splice), *update*[*i*] contains a pointer to the rightmost node of level *i* or higher that is to the left of the location of the insertion/deletion.

If an insertion generates a node with a level greater than

```
Search(list, searchKey)
   x := list→header
   -- loop invariant: x→key < searchKey
   for i := list→level downto 1 do
      while x→forward[i]→key < searchKey do
           x := x→forward[i]
   -- x→key < searchKey ≤ x→forward[1]→key
   x := x→forward[1]
   if x→key = searchKey then return x→value
      else return failure
```

FIGURE 2 - Skip list search algorithm

the previous maximum level of the list, we update the maximum level of the list and initialize the appropriate portions of the update vector. After each deletion, we check if we have deleted the maximum element of the list and if so, decrease the maximum level of the list.

## **Choosing a Random Level**

Initially, we discussed a probability distribution where half of the nodes that have level *i* pointers also have level *i*+1 pointers. To get away from magic constants, we say that a fraction *p* of the nodes with level *i* pointers also have level *i*+1 pointers. (for our original discussion, *p* = 1/2). Levels are generated randomly by an algorithm equivalent to the one in Figure 5. Levels are generated without reference to the number of elements in the list.

# **At what level do we start a search? Defining** *L***(***n***)**

In a skip list of 16 elements generated with *p* = 1/2, we might happen to have 9 elements of level 1, 3 elements of level 2, 3 elements of level 3 and 1 element of level 14 (this would be very unlikely, but it could happen). How should we handle this? If we use the standard algorithm and start our search at level 14, we will do a lot of useless work.

Where should we start the search? Our analysis suggests that ideally we would start a search at the level *L* where we expect 1/*p* nodes. This happens when *L* = log1/*<sup>p</sup> n*. Since we will be referring frequently to this formula, we will use *L*(*n*) to denote log1/*<sup>p</sup> n.*

There are a number of solutions to the problem of deciding how to handle the case where there is an element with an unusually large level in the list.

• *Don't worry, be happy.* Simply start a search at the highest level present in the list. As we will see in our analysis, the probability that the maximum level in a list of *n* elements is significantly larger than *L*(*n*) is very small. Starting a search at the maximum level in the list does not add more than a small constant to the expected search time. This is the approach used in the algorithms described in this paper.

![](_page_2_Figure_0.jpeg)

FIGURE 3 - Pictorial description of steps involved in performing an insertion

- *Use less than you are given*. Although an element may contain room for 14 pointers, we don't need to use all 14. We can choose to utilize only *L*(*n*) levels. There are a number of ways to implement this, but they all complicate the algorithms and do not noticeably improve performance, so this approach is not recommended.
- Fix the dice. If we generate a random level that is more than one greater than the current maximum level in the list, we simply use one plus the current maximum level in the list as the level of the new node. In practice and intuitively, this change seems to work well. However, it totally destroys our ability to analyze the resulting algorithms, since the level of a node is no longer completely random. Programmers should probably feel free to implement this, purists should avoid it.

## **Determining** MaxLevel

Since we can safely cap levels at L(n), we should choose MaxLevel = L(N) (where N is an upper bound on the number of elements in a skip list). If p = 1/2, using MaxLevel = 16 is appropriate for data structures containing up to  $2^{16}$  elements.

## ANALYSIS OF SKIP LIST ALGORITHMS

The time required to execute the *Search, Delete* and *Insert* operations is dominated by the time required to search for the appropriate element. For the *Insert* and *Delete* operations, there is an additional cost proportional to the level of the node being inserted or deleted. The time required to find an element is proportional to the length of the search path, which is determined by the pattern in which elements with different levels appear as we traverse the list.

## **Probabilistic Philosophy**

The structure of a skip list is determined only by the number

```
randomLevel()

| Ivl := 1
| -- random() that returns a random value in [0...1)
| while random() < p and |vl < MaxLevel do

| | | | | | | 1
| return |vl
```

FIGURE 5 - Algorithm to calculate a random level

```
Insert(list, searchKey, newValue)
    local update[1..MaxLevel]
    x := list→header
    for i := list→level downto 1 do
        while x\rightarrowforward[i]\rightarrowkey < searchKey do
              x := x \rightarrow forward[i]
        --x \rightarrow key < searchKey \le x \rightarrow forward[i] \rightarrow key
        update[i] := x
    x := x \rightarrow forward[1]
    if x \rightarrow key = searchKey then x \rightarrow value := newValue
        lvl := randomLevel()
        if IvI > list→level then
              for i := list \rightarrow level + 1 to |v| do
                   update[i] := list→header
              list→level := lvl
        x := makeNode(lvl, searchKey, value)
        for i := 1 to level do
              x \rightarrow forward[i] := update[i] \rightarrow forward[i]
              update[i] \rightarrow forward[i] := x
Delete(list, searchKey)
    local update[1..MaxLevel]
    x := list→header
    for i := list→level downto 1 do
        while x→forward[i]→key < searchKey do
              x := x \rightarrow forward[i]
        update[i] := x
    x := x \rightarrow forward[1]
    if x \rightarrow key = searchKey then
        for i := 1 to list\rightarrowlevel do
           if update[i]\rightarrowforward[i] \neq x then break
           update[i]\rightarrowforward[i] := x\rightarrowforward[i]
        free(x)
        while list→level > 1 and
              list→header→forward[list→level] = NIL do
           list \rightarrow level := list \rightarrow level - 1
```

FIGURE 4 - Skip List insertion and deletion algorithms

elements in the skip list and the results of consulting the random number generator. The sequence of operations that produced the current skip list does not matter. We assume an adversarial user does not have access to the levels of nodes; otherwise, he could create situations with worst-case running times by deleting all nodes that were not level 1.

The probabilities of poor running times for successive operations on the same data structure are NOT independent; two successive searches for the same element will both take exactly the same time. More will be said about this later.

## **Analysis of expected search cost**

We analyze the search path backwards, travelling up and to the left. Although the levels of nodes in the list are known and fixed when the search is performed, we act as if the level of a node is being determined only when it is observed while backtracking the search path.

At any particular point in the climb, we are at a situation similar to situation *a* in Figure 6 – we are at the *i* th forward pointer of a node *x* and we have no knowledge about the levels of nodes to the left of *x* or about the level of *x*, other than that the level of *x* must be at least *i*. Assume the *x* is not the header (the is equivalent to assuming the list extends infinitely to the left). If the level of *x* is equal to *i*, then we are in situation *b*. If the level of *x* is greater than *i*, then we are in situation *c*. The probability that we are in situation *c* is *p*. Each time we are in situation *c*, we climb up a level. Let *C*(*k*) = the expected cost (i.e, length) of a search path that climbs up *k* levels in an infinite list:

$$C(0) = 0$$

*C*(*k*) = (1–*p*) (cost in situation *b*) + *p* (cost in situation *c*)

By substituting and simplifying, we get:

$$C(k) = (1-p)(1 + C(k)) + p(1 + C(k-1))$$

$$C(k) = 1/p + C(k-1)$$

$$C(k) = k/p$$

Our assumption that the list is infinite is a pessimistic assumption. When we bump into the header in our backwards climb, we simply climb up it, without performing any leftward movements. This gives us an upper bound of (*L*(*n*)–1)/*p* on the expected length of the path that climbs from level 1 to level *L*(*n*) in a list of *n* elements.

We use this analysis go up to level *L*(*n*) and use a different analysis technique for the rest of the journey. The number of leftward movements remaining is bounded by the number of elements of level *L*(*n*) or higher in the entire list, which has an expected value of 1/*p*.

We also move upwards from level *L*(*n*) to the maximum level in the list. The probability that the maximum level of the list is a greater than *k* is equal to 1–(1–*pk*) *<sup>n</sup>*, which is at most *npk*. We can calculate the expected maximum level is at most *L*(*n*) + 1/(1–*p*). Putting our results together, we find

Total expected cost to climb out of a list of *n* elements ≤ *L*(*n*)/*p* + 1/(1–*p*)

which is *O*(log *n*).

## **Number of comparisons**

Our result is an analysis of the "length" of the search path. The number of comparisons required is one plus the length of the search path (a comparison is performed for each position in the search path, the "length" of the search path is the number of hops between positions in the search path).

## **Probabilistic Analysis**

It is also possible to analyze the probability distribution of search costs. The probabilistic analysis is somewhat more complicated (see box). From the probabilistic analysis, we can calculate an upper bound on the probability that the actual cost of a search exceeds the expected cost by more than a specified ratio. Some results of this analysis are shown in Figure 8.

## **Choosing** *p*

Table 1 gives the relative times and space requirements for different values of *p.* Decreasing *p* also increases the variabil-

![](_page_3_Picture_22.jpeg)

FIGURE 6 - Possible situations in backwards traversal of the search path

ity of running times. If 1/p is a power of 2, it will be easy to generate a random level from a stream of random bits (it requires an average of  $(\log_2 1/p)/(1-p)$  random bits to generate a random level). Since some of the constant overheads are related to L(n) (rather than L(n)/p), choosing p = 1/4 (rather than 1/2) slightly improves the constant factors of the speed of the algorithms as well. I suggest that a value of 1/4 be used for p unless the variability of running times is a primary concern, in which case p should be 1/2.

#### **Sequences of operations**

The expected total time for a sequence of operations is equal to the sum of the expected times of each of the operations in the sequence. Thus, the expected time for any sequence of m searches in a data structure that contains n elements is  $O(m \log n)$ . However, the pattern of searches affects the probability distribution of the actual time to perform the entire sequence of operations.

If we search for the same item twice in the same data structure, both searches will take exactly the same amount of time. Thus the variance of the total time will be four times the variance of a single search. If the search times for two elements are independent, the variance of the total time is equal to the sum of the variances of the individual searches. Searching for the same element over and over again maximizes the variance.

#### ALTERNATIVE DATA STRUCTURES

Balanced trees (e.g., AVL trees [Knu73] [Wir76]) and self-adjusting trees [ST85] can be used for the same problems as skip lists. All three techniques have performance bounds of the same order. A choice among these schemes involves several factors: the difficulty of implementing the algorithms, constant factors, type of bound (amortized, probabilistic or worst-case) and performance on a non-uniform distribution of queries.

# **Implementation difficulty**

For most applications, implementers generally agree skip lists are significantly easier to implement than either balanced tree algorithms or self-adjusting tree algorithms.

| p    | Normalized search times ( <i>i.e.</i> , normalized $L(n)/p$ ) | Avg. # of pointers per node $(i.e., 1/(1-p))$ |
|------|---------------------------------------------------------------|-----------------------------------------------|
| 1/2  | 1                                                             | 2                                             |
| 1/e  | 0.94                                                          | 1.58                                          |
| 1/4  | 1                                                             | 1.33                                          |
| 1/8  | 1.33                                                          | 1.14                                          |
| 1/16 | 2                                                             | 1.07                                          |

TABLE 1 – Relative search speed and space requirements, depending on the value of p.

#### **Constant factors**

Constant factors can make a significant difference in the practical application of an algorithm. This is particularly true for sub-linear algorithms. For example, assume that algorithms A and B both require  $O(\log n)$  time to process a query, but that B is twice as fast as A: in the time algorithm A takes to process a query on a data set of size n, algorithm B can process a query on a data set of size  $n^2$ .

There are two important but qualitatively different contributions to the constant factors of an algorithm. First, the inherent complexity of the algorithm places a lower bound on any implementation. Self-adjusting trees are continuously rearranged as searches are performed; this imposes a significant overhead on any implementation of self-adjusting trees. Skip list algorithms seem to have very low inherent constant-factor overheads: the inner loop of the deletion algorithm for skip lists compiles to just six instructions on the 68020.

Second, if the algorithm is complex, programmers are deterred from implementing optimizations. For example, balanced tree algorithms are normally described using recursive insert and delete procedures, since that is the most simple and intuitive method of describing the algorithms. A recursive insert or delete procedure incurs a procedure call overhead. By using non-recursive insert and delete procedures, some of this overhead can be eliminated. However, the complexity of non-recursive algorithms for insertion and deletion in a balanced tree is intimidating and this complexity deters most programmers from eliminating recursion in these routines. Skip list al-

![](_page_4_Figure_14.jpeg)

FIGURE 8 - This graph shows a plot of an upper bound on the probability of a search taking substantially longer than expected. The vertical axis show the probability that the length of the search path for a search exceeds the average length by more than the ratio on the horizontal axis. For example, for p = 1/2 and n = 4096, the probability that the search path will be more than three times the expected length is less than one in 200 million. This graph was calculated using our probabilistic upper bound.

| Implementation          | Search Time | Insertion Time | Deletion Time |
|-------------------------|-------------|----------------|---------------|
| Skip lists              | 0.051 msec  | 0.065 msec     | 0.059 msec    |
|                         | (1.0)       | (1.0)          | (1.0)         |
| non-recursive AVL trees | 0.046 msec  | 0.10 msec      | 0.085 msec    |
|                         | (0.91)      | (1.55)         | (1.46)        |
| recursive 2–3 trees     | 0.054 msec  | 0.21 msec      | 0.21 msec     |
|                         | (1.05)      | (3.2)          | (3.65)        |
| Self–adjusting trees:   |             |                |               |
| top-down splaying       | 0.15 msec   | 0.16 msec      | 0.18 msec     |
|                         | (3.0)       | (2.5)          | (3.1)         |
| bottom-up splaying      | 0.49 msec   | 0.51 msec      | 0.53 msec     |
|                         | (9.6)       | (7.8)          | (9.0)         |

Table 2 - Timings of implementations of different algorithms

gorithms are already non-recursive and they are simple enough that programmers are not deterred from performing optimizations.

Table 2 compares the performance of implementations of skip lists and four other techniques. All implementations were optimized for efficiency. The AVL tree algorithms were written by James Macropol of Contel and based on those in [Wir76]. The 2–3 tree algorithms are based on those presented in [AHU83]. Several other existing balanced tree packages were timed and found to be much slower than the results presented below. The self-adjusting tree algorithms are based on those presented in [ST85]. The times in this table reflect the CPU time on a Sun-3/60 to perform an operation in a data structure containing 216 elements with integer keys. The values in parenthesis show the results relative to the skip list time The times for insertion and deletion do not include the time for memory management (e.g, in *C* programs, calls to *malloc* and *free*).

Note that skip lists perform more comparisons than other methods (the skip list algorithms presented here require an average of *L*(*n*)/*p* + 1/(1–*p*) + 1 comparisons). For tests using real numbers as keys, skip lists were slightly slower than the non-recursive AVL tree algorithms and search in a skip list was slightly slower than search in a 2–3 tree (insertion and deletion using the skip list algorithms was still faster than using the recursive 2–3 tree algorithms). If comparisons are very expensive, it is possible to change the algorithms so that we never compare the search key against the key of a node more than once during a search. For *p* = 1/2, this produces an upper bound on the expected number of comparisons of 7/2 + 3/2 log2 *n*. This modification is discussed in [Pug89b].

## **Type of performance bound**

These three classes of algorithm have different kinds of performance bounds. Balanced trees have worst-case time bounds, self-adjusting trees have amortized time bounds and skip lists have probabilistic time bounds. With self-adjusting trees, an individual operation can take *O*(*n*) time, but the time bound always holds over a long sequence of operations. For skip lists, any operation or sequence of operations can take longer than expected, although the probability of any operation taking significantly longer than expected is negligible.

In certain real-time applications, we must be assured that an operation will complete within a certain time bound. For such applications, self-adjusting trees may be undesirable, since they can take significantly longer on an individual operation than expected (e.g., an individual search can take *O*(*n*) time instead of *O*(log *n*) time). For real-time systems, skip lists may be usable if an adequate safety margin is provided: the chance that a search in a skip lists containing 1000 elements takes more than 5 times the expected time is about 1 in 1018.

## **Non-uniform query distribution**

Self-adjusting trees have the property that they adjust to nonuniform query distributions. Since skip lists are faster than self-adjusting trees by a significant constant factor when a uniform query distribution is encountered, self-adjusting trees are faster than skip lists only for highly skewed distributions. We could attempt to devise self-adjusting skip lists. However, there seems little practical motivation to tamper with the simplicity and fast performance of skip lists; in an application where highly skewed distributions are expected, either selfadjusting trees or a skip list augmented by a cache may be preferable [Pug90].

## **ADDITIONAL WORK ON SKIP LISTS**

 I have described a set of algorithms that allow multiple processors to concurrently update a skip list in shared memory [Pug89a]. This algorithms are much simpler than concurrent balanced tree algorithms. They allow an unlimited number of readers and *n* busy writers in a skip list of *n* elements with very little lock contention.

Using skip lists, it is easy to do most (all?) the sorts of operations you might wish to do with a balanced tree such as use search fingers, merge skip lists and allow ranking operations (e.g., determine the *k*th element of a skip list) [Pug89b].

Tom Papadakis, Ian Munro and Patricio Poblette [PMP90] have done an exact analysis of the expected search time in a skip list. The upper bound described in this paper is close to their exact bound; the techniques they needed to use to derive an exact analysis are very complicated and sophisticated. Their exact analysis shows that for *p* = 1/2 and *p* = 1/4, the upper bound given in this paper on the expected cost of a search is not more than 2 comparisons more than the exact expected cost.

I have adapted idea of probabilistic balancing to some other problems arising both in data structures and in incremental computation [PT88]. We can generate the level of a node based on the result of applying a hash function to the element (as opposed to using a random number generator). This results in a scheme where for any set *S*, there is a unique data structure that represents *S* and with high probability the data structure is approximately balanced. If we combine this idea with an *applicative* (i.e., persistent) probabilistically balanced data structure and a scheme such as hashed-consing [All78] which allows constant-time structural equality tests of applicative data structures, we get a number of interesting properties, such as constant-time equality tests for the representations of sequences. This scheme also has a number of applications for incremental computation. Since skip lists are

somewhat awkward to make applicative, a probabilistically balanced *tree* scheme is used.

## **RELATED WORK**

James Discroll pointed out that R. Sprugnoli suggested a method of randomly balancing search trees in 1981 [Spr81]. With Sprugnoli's approach, the state of the data structure is *not* independent of the sequence of operations which built it. This makes it much harder or impossible to formally analyze his algorithms. Sprugnoli gives empirical evidence that his algorithm has good expected performance, but no theoretical results.

A randomized data structure for ordered sets is described in [BLLSS86]. However, a search using that data structure requires *O*(*n*1/2) expected time.

Cecilia Aragon and Raimund Seidel describe a probabilistically balanced search trees scheme [AC89]. They discuss how to adapt their data structure to non-uniform query distributions.

## **SOURCE CODE AVAILABILITY**

Skip list source code libraries for both C and Pascal are available for anonymous ftp from mimsy.umd.edu.

## **CONCLUSIONS**

From a theoretical point of view, there is no need for skip lists. Balanced trees can do everything that can be done with skip lists and have good worst-case time bounds (unlike skip lists). However, implementing balanced trees is an exacting task and as a result balanced tree algorithms are rarely implemented except as part of a programming assignment in a data structures class.

Skip lists are a simple data structure that can be used in place of balanced trees for most applications. Skip lists algorithms are very easy to implement, extend and modify. Skip lists are about as fast as highly optimized balanced tree algorithms and are substantially faster than casually implemented balanced tree algorithms.

## **ACKNOWLEDGEMENTS**

Thanks to the referees for their helpful comments. Special thanks to all those people who supplied enthusiasm and encouragement during the years in which I struggled to get this work published, especially Alan Demers, Tim Teitelbaum and Doug McIlroy. This work was partially supported by an AT&T Bell Labs Fellowship and by NSF grant CCR– 8908900.

## **REFERENCES**

- [AC89] Aragon, Cecilia and Raimund Seidel, Randomized Search Trees, *Proceedings of the 30th Ann. IEEE Symp on Foundations of Computer Science*, pp 540–545, October 1989.
- [AHU83] Aho, A., Hopcroft, J. and Ullman, J. *Data Structures and Algorithms,* Addison-Wesley Publishing Company, 1983.
- [All78] John Allen. *Anatomy of LISP,* McGraw Hill Book Company, NY, 1978.

- [BLLSS86] Bentley, J., F. T. Leighton, M.F. Lepley, D. Stanat and J. M. Steele, *A Randomized Data Structure For Ordered Sets,* MIT/LCS Technical Memo 297, May 1986.
- [Knu73] Knuth, D. "Sorting and Searching," *The Art of Computer Programming,* Vol. 3, Addison-Wesley Publishing Company, 1973.
- [PMP90] Papadakis, Thomas, Ian Munro and Patricio Poblette, *Exact Analysis of Expected Search Cost in Skip Lists,* Tech Report # ????, Dept. of Computer Science, Univ. of Waterloo, January 1990.
- [PT89] Pugh, W. and T. Teitelbaum, "Incremental Computation via Function Caching," *Proc. of the Sixteenth conference on the Principles of Programming Languages*, 1989.
- [Pug89a] Pugh, W., *Concurrent Maintenance of Skip Lists*, Tech Report TR-CS-2222, Dept. of Computer Science, University of Maryland, College Park, 1989.
- [Pug89b] Pugh, W., *Whatever you might want to do using Balanced Trees, you can do it faster and more simply using Skip Lists,* Tech Report CS–TR–2286, Dept. of Computer Science, University of Maryland, College Park, July 1989.
- [Pug90] Pugh, W. Slow Optimally Balanced Search Strategies vs. Cached Fast Uniformly Balanced Search Strategies, to appear in *Information Processing Letters*.
- [Spr81] Sprugnoli, R. Randomly Balanced Binary Trees, *Calcolo*, V17 (1981), pp 99-117.
- [ST85] Sleator, D. and R. Tarjan "Self-Adjusting Binary Search Trees," *Journal of the ACM,* Vol 32, No. 3, July 1985, pp. 652-666.
- [Wir76] Wirth, N. *Algorithms + Data Structures = Programs,* Prentice-Hall, 1976.

#### PROBABILISTIC ANALYSIS

In addition to analyzing the expected performance of skip lists, we can also analyze the probabilistic performance of skip lists. This will allow us to calculate the probability that an operation takes longer than a specified time. This analysis is based on the same ideas as our analysis of the expected cost, so that analysis should be understood first.

A *random variable* has a fixed but unpredictable value and a predictable probability distribution and average. If X is a random variable, Prob{ X = t } denotes the probability that X equals t and Prob{ X > t } denotes the probability that X is greater than t. For example, if X is the number obtained by throwing a unbiased die, Prob{ X > 3 } = 1/2.

It is often preferable to find simple upper bounds on values whose exact value is difficult to calculate. To discuss upper bounds on random variables, we need to define a partial ordering and equality on the probability distributions of nonnegative random variables.

**Definitions** (= $_{prob}$  and  $\leq_{prob}$ ). Let X and Y be non-negative independent random variables (typically, X and Y would denote the time to execute algorithms  $A_X$  and  $A_Y$ ). We define  $X \leq_{prob} Y$  to be true if and only if for any value t, the probability that X exceeds t is less than the probability that Y exceeds t. More formally:

$$X =_{prob} Y \text{ iff } \forall t, \text{Prob}\{X > t\} = \text{Prob}\{Y > t\} \text{ and } X \leq_{prob} Y \text{ iff } \forall t, \text{Prob}\{X > t\} \leq \text{Prob}\{Y > t\}. \square$$

For example, the graph in Figure 7shows the probability distribution of three random variables X, Y and Z. Since the probability distribution curve for X is completely under the curves for Y and Z,  $X \leq_{prob} Y$  and  $X \leq_{prob} Z$ . Since the probability curves for Y and Z intersect, neither  $Y \leq_{prob} Z$  nor  $Z \leq_{prob} Y$ . Since the expected value of a random variable X is simply the area under the curve Prob{ X > t }, if  $X \leq_{prob} Y$  then the average of X is less than or equal to the average of Y.

We make use of two probability distributions:

**Definition** (binomial distributions — B(t, p)). Let t be a non-negative integer and p be a probability. The term B(t, p) denotes a random variable equal to the number of successes seen in a series of t independent random trials where the probability of a success in a trial is p. The average and variance of B(t, p) are tp and tp(1-p) respectively.  $\square$  **Definition** (negative binomial distributions — NB(s, p)). Let s

be a non-negative integer and p be a probability. The term NB(s, p) denotes a random variable equal to the number of failures seen before the  $s^{th}$  success in a series of random independent trials where the probability of a success in a trial is p. The average and variance of NB(s, p) are s(1-p)/p and  $s(1-p)/p^2$  respectively.  $\square$ 

![](_page_7_Figure_10.jpeg)

FIGURE 7 – Plots of three probability distributions

#### Probabilistic analysis of search cost

The number of leftward movements we need to make before we move up a level (in an infinite list) has a negative binomial distribution: it is the number of failures (situations b's) we see before we see the first success (situation c) in a series of independent random trials, where the probability of success is p. Using the probabilistic notation introduced above:

Cost to climb one level in an infinite list 
$$=_{prob} 1 + NB(1, p)$$
.

We can sum the costs of climbing each level to get the total cost to climb up to level L(n):

Cost to climb to level 
$$L(n)$$
 in an infinite list  $=_{prob} (L(n) - 1) + NB(L(n) - 1, p)$ .

Our assumption that the list is infinite is a pessimistic assumption:

Cost to climb to level 
$$L(n)$$
 in a list of  $n$  elements  $\leq_{prob} (L(n) - 1) + NB(L(n) - 1, p)$ .

Once we have climbed to level L(n), the number of leftward movements is bounded by the number of elements of level L(n) or greater in a list of n elements. The number of elements of level L(n) or greater in a list of n elements is a random variable of the form B(n, 1/np).

Let M be a random variable corresponding to the maximum level in a list of n elements. The probability that the level of a node is greater than k is  $p^k$ , so Prob{ M > k } = 1–  $(1-p^k)^n < np^k$ . Since  $np^k = p^{k-L(n)}$  and Prob{ NB(1, 1-p) + 1 > i } =  $p^i$ , we get an probabilistic upper bound of  $M \le_{prob} L(n) + NB(1, 1-p) + 1$ . Note that the average of L(n) + NB(1, 1-p) + 1 is L(n) + 1/(1-p).

This gives a probabilistic upper bound on the cost once we have reached level L(n) of B(n, 1/np) + (L(n) + NB(1, 1-p) + 1) - L(n). Combining our results to get a probabilistic upper bound on the total length of the search path (i.e., cost of the entire search):

total cost to climb out of a list of 
$$n$$
 elements  $\leq_{prob} (L(n) - 1) + NB(L(n) - 1, p) + B(n, 1/np) + NB(1, 1-p) + 1$ 

The expected value of our upper bound is equal to

$$(L(n) - 1) + (L(n) - 1)(1 - p)/p + 1/p + p/(1-p) + 1$$
  
=  $L(n)/p + 1/(1-p)$ ,

which is the same as our previously calculated upper bound on the expected cost of a search. The variance of our upper bound is

$$(L(n) - 1)(1-p)/p^2 + (1 - 1/np)/p + p/(1-p)^2$$
  
<  $(1-p)L(n)/p^2 + p/(1-p)^2 + (2p-1)/p^2$ .

Figure 8 show a plot of an upper bound on the probability of an actual search taking substantially longer than average, based on our probabilistic upper bound.

</details>

</golden_source>