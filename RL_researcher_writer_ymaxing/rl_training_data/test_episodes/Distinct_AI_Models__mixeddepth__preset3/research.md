# Research

<research_source type="tavily_results" phase="exploitation">
## Research Results

<details>
<summary>What quote did Ilia Sucholutsky give about measuring similarities of similarities in model representations?</summary>

Phase: [EXPLOITATION]

### Source [1]: https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107

Query: What quote did Ilia Sucholutsky give about measuring similarities of similarities in model representations?

Answer: “It can kind of be described as measuring the similarity of similarities,” said Ilia Sucholutsky, an AI researcher at New York University.

-----

</details>

<details>
<summary>What did Minyoung Huh say about his existential life crisis in relation to AI model scaling?</summary>

Phase: [EXPLOITATION]

### Source [2]: https://www.youtube.com/watch?v=oBAQLsDkZwc

Query: What did Minyoung Huh say about his existential life crisis in relation to AI model scaling?

Answer: Minyoung Huh suggests AI scaling may address existential questions but risks creating uncontrollable systems. He advocates for a sage model over a sorcerer's approach. AI's potential to manipulate and spread misinformation is a significant concern.

-----

</details>

<details>
<summary>What critique did Christopher Wolfram make on generalizability of representational similarity results from one dataset?</summary>

Phase: [EXPLOITATION]

### Source [7]: https://openreview.net/pdf/8f5b35d2ddc2eb1879dfc35e29053095d81d7d69.pdf

Query: What critique did Christopher Wolfram make on generalizability of representational similarity results from one dataset?

Answer: The pattern persists across probe datasets, implying its generalizability. Moreover, we find no difference in effect size across datasets (please refer to Figure 2). This contrasts with a previous finding Ciernik et al. (2024), which showed that the correspondence between representational similarity and task behavior depends on the dataset. The same trend holds across other CKA variants as well (see Appendix E.1).

-----

Phase: [EXPLOITATION]

### Source [9]: https://kriegeskortelab.zuckermaninstitute.columbia.edu/sites/default/files/content/NiliKriegeskorte_2014_PLoSComputBiol.pdf

Query: What critique did Christopher Wolfram make on generalizability of representational similarity results from one dataset?

Answer: t value from dataset 1 would be positively biased and could not be used to test whether the response patterns contain information discriminating stimuli i and j. Applying the same weights to the dataset 2 (the test data) and calculating the resulting t statistic gives us the linear-discriminant t (LD-t) value. The LD-t is the t value for dataset 2 computed after projection onto the linear discriminant estimated with data set 1. It is a valid t value (t distributed under the null hypothesis of equal response pattern distributions for stimuli i and j) and can be used to test discriminability of i and j. The LD-t value is a crossvalidated measure of the discriminability of the two stimuli. Low discriminability could be due to similar responses to the two stimuli or high levels of noise. One [...] Figure 4 shows the results of statistical inference for our simulated data set. In this example, the reference RDM is a (simulated) brain RDM (to be explained) and the candidate RDMs are model RDMs (serving to explain). Note that we refer to the reference RDM as a single representation, even though the analysis is based on one reference-RDM estimate per subject. The relatedness of a candidate RDM to the reference RDM is measured as the average across subjects of the correlations between the candidate RDM and the single-subject reference-RDM estimates. [...] for estimating . Alternatively, for time-course data (e.g. fMRI), a linear-model fit to each response channel’s time series could provide the errors matrix (number of time points by number of response channels). Given the errors matrix, we could use the sample covariance 16 or a shrinkage estimator (Ledoit and Wolf, 2003) of the covariance. The latter choice promises a more stable covariance estimate that is guaranteed to be invertible. The weights defining the linear discriminant are estimated for dataset 1 (the training data). These weights maximize the t statistic (computed after weighted averaging) for contrasting stimuli i and j in dataset 1. However, because the weights are necessarily somewhat overfitted to dataset 1, the t value from dataset 1 would be positively biased and could

-----

Phase: [EXPLOITATION]

### Source [10]: https://www.emergentmind.com/topics/representational-similarity-analysis-rsa

Query: What critique did Christopher Wolfram make on generalizability of representational similarity results from one dataset?

Answer: 2000 character limit reached

# Representational Similarity Analysis (RSA)

Updated 29 September 2025

 Representational Similarity Analysis (RSA) is a statistical method that transforms high-dimensional neural or model activity into representational dissimilarity matrices (RDMs) for cross-system comparison.
 It leverages varied metrics such as Euclidean distance and Pearson’s correlation along with techniques like GLM, gradient descent, and deep learning to robustly compare complex data.
 RSA is widely applied in neuroscience, AI, and behavioral research to enhance model interpretability, align human and machine representations, and support innovative cross-modal analyses. [...] Representational Similarity Analysis (RSA) is a statistical and computational framework for quantifying and comparing the internal representational geometries of neural, behavioral, and artificial systems. By abstracting complex, high-dimensional activity patterns into similarity structures—commonly represented as representational dissimilarity matrices (RDMs)—RSA enables rigorous comparisons across measurement modalities, subjects, species, computational models, and stimuli. It is heavily utilized in cognitive neuroscience, systems neuroscience, and increasingly in artificial intelligence and computational linguistics for model comparison, interpretability, and alignment assessment.

## 1. Theoretical Principles and Core Definitions [...] Deconfounded similarity. In network comparison contexts, confounding from input population structure is removed by regressing out baseline input similarity from the representational similarity matrices before final correlation (the “deconfounded RSA”) (Cui et al., 2022).

Topological extensions. Recent proposals generalize the RDM using nonlinear, monotonic (piecewise linear) transforms, emphasizing discrete topological structure (e.g., neighborhood relations) rather than fine-grained metric geometry. This yields geo-topological matrices and “topological RSA” (tRSA), which can be “tuned” from pure geometry to pure topology via threshold parameters (Lin et al., 2023, Lin, 2024).

## 3. Application Domains

-----

Phase: [EXPLOITATION]

### Source [11]: https://proceedings.iclr.cc/paper_files/paper/2025/file/3f9bbf77fbd858e5b6e39d39fe84ed2e-Paper-Conference.pdf

Query: What critique did Christopher Wolfram make on generalizability of representational similarity results from one dataset?

Answer: Such results suggest that the generalization capability is related to the similarity among subjects. [...] The above experimental results show that when the subjects are similar, the models achieve better generalization performance, and vice versa. On the other hand, when a mix of similar and dissimilar subjects are used for training, generalization remains stable, with performance approaching to the models trained on similar subjects. This suggests that generalization capability depends on learning inherent commonalities among human brains, with substantial tolerance for dissimilarities. It also explains why increasing the number of subjects enhances generalization — a larger dataset is more likely to include subjects with higher similarities.

-----

</details>

<details>
<summary>What was Efros's specific observation and remark regarding Huh's Platonic representation results?</summary>

Phase: [EXPLOITATION]

### Source [12]: https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107

Query: What was Efros's specific observation and remark regarding Huh's Platonic representation results?

Answer: Efros disagreed with Huh's Platonic representation results, arguing that real-world data lacks the translation simplicity seen in Huh's dataset. Efros emphasized the complexity of real-world data compared to the controlled Wikipedia dataset used in Huh's experiment. Efros noted that in the Wikipedia dataset that Huh used, the images and text contained very similar information by design. But most data we encounter in the world has features that resist translation. “There is a reason why you go to an art museum instead of just reading the catalog,” he said. Efros said of the MIT team: “They’re all good friends and they’re all very, very smart people. I think they’re wrong, but that’s what science is about.”

-----

</details>

<details>
<summary>What quotes has Jeff Clune made about Platonic explanations versus complexity of large AI models?</summary>

Phase: [EXPLOITATION]

### Source [13]: https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107

Query: What quotes has Jeff Clune made about Platonic explanations versus complexity of large AI models?

Answer: “You can’t reduce a trillion-parameter system to simple explanations,” said Jeff Clune, an AI researcher at the University of British Columbia. “The answers are going to be complicated.”

-----

</details>

<details>
<summary>What quote did Phillip Isola give about not being bothered by responses to the Platonic representation hypothesis?</summary>

Phase: [EXPLOITATION]

### Source [14]: https://phillipi.github.io/prh

Query: What quote did Phillip Isola give about not being bothered by responses to the Platonic representation hypothesis?

Answer: Phillip Isola stated he is not bothered by responses to the Platonic Representation Hypothesis. He focuses on the hypothesis's core ideas. His work emphasizes representation convergence in AI models.

-----

Phase: [EXPLOITATION]

### Source [15]: https://www.youtube.com/watch?v=V7AyriUcXZQ

Query: What quote did Phillip Isola give about not being bothered by responses to the Platonic representation hypothesis?

Answer: Phillip Isola stated he is not bothered by responses to the Platonic Representation Hypothesis. He focuses on the hypothesis's core ideas. His work emphasizes representation convergence in AI models.

-----

Phase: [EXPLOITATION]

### Source [16]: https://proceedings.mlr.press/v235/huh24a.html

Query: What quote did Phillip Isola give about not being bothered by responses to the Platonic representation hypothesis?

Answer: Phillip Isola stated he is not bothered by responses to the Platonic Representation Hypothesis. He focuses on the hypothesis's core ideas. His work emphasizes representation convergence in AI models.

-----

Phase: [EXPLOITATION]

### Source [17]: https://new-savanna.blogspot.com/2024/05/the-platonic-representation-hypothesis.html

Query: What quote did Phillip Isola give about not being bothered by responses to the Platonic representation hypothesis?

Answer: Phillip Isola stated he is not bothered by responses to the Platonic Representation Hypothesis. He focuses on the hypothesis's core ideas. His work emphasizes representation convergence in AI models.

-----

Phase: [EXPLOITATION]

### Source [18]: https://sidn.baulab.info/universality

Query: What quote did Phillip Isola give about not being bothered by responses to the Platonic representation hypothesis?

Answer: Phillip Isola stated he is not bothered by responses to the Platonic Representation Hypothesis. He focuses on the hypothesis's core ideas. His work emphasizes representation convergence in AI models.

-----

</details>

</research_source>

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What mathematical underpinnings support similarity-of-similarities for cross-model representation comparison?</summary>

Phase: [EXPLORATION]

### Source [19]: https://orbilu.uni.lu/bitstream/10993/67222/1/Cross_M_Semantics.pdf

Query: What mathematical underpinnings support similarity-of-similarities for cross-model representation comparison?

Answer: Centered Kernel Alignment (CKA) is a widely used metric for comparing representations across neural networks. Given two sets of activation vectors X ∈Rn×d1 and Y ∈Rn×d2, the (linear) CKA similarity is defined as: CKA(X, Y ) = ∥Y ⊤X∥^{2} F / (∥X⊤X∥F · ∥Y ⊤Y ∥F), where ∥·∥F denotes the Frobenius norm. A value of 1 indicates perfect alignment up to rotation and scaling, while 0 indicates orthogonality. The degree of alignment can be quantified using metrics such as Centered Kernel Alignment (CKA) between representation matrices, Subspace Overlap via principal angle statistics, and Inter-model Transfer Accuracy using frozen representations. These metrics reveal not only how similar two representations are, but also how effectively one model’s internal representations can substitute for another’s in downstream inference. Moschella et al. show that relative representations enable robust zero-shot communication. Recent work emphasizes geometric and topological properties underlying representation similarity. Xu examines metrics for cross-modal alignment and highlights architectural limitations in retrieval tasks. Funero introduces latent functional maps to align models via geometric correspondences.

-----

Phase: [EXPLORATION]

### Source [20]: https://www.emergentmind.com/topics/representational-similarity-metrics

Query: What mathematical underpinnings support similarity-of-similarities for cross-model representation comparison?

Answer: RSA and Soft Matching, which preserve global geometry or detailed unit tuning, yield stronger discrimination between brain regions, model families, or training paradigms. Metrics based on flexible linear mappings (e.g., linear predictivity, unconstrained linear regression) capture the globally shared, linearly accessible information across representations. These principles have analogues in the neuroscience and neural network literature, where an ideal metric must also be robust to measurement noise, invariant to irrelevant coordinate choices (such as orthogonal transformations or scaling), and accommodate the specific invariances and structure of the representations under comparison (Diedrichsen et al., 2020, Williams et al., 2021). Contemporary research classifies representational similarity metrics along several dimensions. Through continued advances in principles, analytical methodology, and compositional integration, representational similarity metrics are poised to remain at the core of comparative research in both artificial and biological learning systems. References include AMR Similarity Metrics from Principles (2020), Comparing representational geometries using whitened unbiased-distance-matrix similarity (2020), Generalized Shape Metrics on Neural Representations (2021), Duality of Bures and Shape Distances with Implications for Comparing Neural Representations (2023).

-----

Phase: [EXPLORATION]

### Source [21]: https://arxiv.org/html/2505.13899v1

Query: What mathematical underpinnings support similarity-of-similarities for cross-model representation comparison?

Answer: ⋅⋅⟨·,·⟩ is the inner product. Representation similarity between two models is often evaluated via kernel matrix comparison through a technique known as Centered Kernel Alignment (CKA). Other common metrics include nearest-neighbor scores, mutual KNN, and SVCCA. We use implementations of these from the codebase of, and report CKA in our main results due to its widespread in both vision and language models. Additional metrics are evaluated in the Appendix. One interesting, well-studied phenomenon is representational similarity across AI models. A large body of work has considered ways in which AI model representations (e.g. their mathematical depictions of real-world inputs) align. Although much of this work has focused on neural networks, recent work has applied similar methods to generative models like large language models (LLMs) and found some evidence of “feature universality” across these models. Given an input z∈D and model backbones f	heta^1 and f	heta^2, we can measure the similarity in the latent representations of.

-----

</details>

<details>
<summary>What limitations arise when applying nearest-neighbor metrics to measure representational alignment across modalities?</summary>

Phase: [EXPLORATION]

### Source [24]: https://arxiv.org/html/2506.08774v2

Query: What limitations arise when applying nearest-neighbor metrics to measure representational alignment across modalities?

Answer: Nearest-neighbor metrics struggle with high dimensionality and scalability, often failing to capture true representational alignment across modalities. They also break down in many-to-many mappings, where one-to-one assumptions no longer hold. Computational complexity limits their use in large datasets. Overall, we can conclude that (1) the alignment among different modalities cannot be fully characterized by either spatial distances (e.g., Euclidean distance) nor by distribution differences (e.g., Wasserstein distance); and (2) well-aligned representations of CLIP and BLIP and unaligned representations of other models do not show substantially distinctive geometry for the same dataset. To measure the similarity between two representations, we can apply multiple metrics to obtain d(𝒙^i,𝒚^i), where d(⋅,⋅) is a (dis)similarity function. We first use 4 standard metrics (Euclidean, Manhattan, and Chi-Square distance, and cosine similarity; see Table 1) that can measure how close or different two representations 𝒙^i∈ℝn and 𝒚^i∈ℝn are, motivated by previous work [66, 1, 43, 14]. We should note that cosine similarity is in the range of [−1,1], while the dissimilarity metrics are unbounded. We then find the corresponding representations between modalities. In addition, computational scalability presents another significant constraint: Cross-modal similarity computation scales quadratically, O(N^{2}) with dataset cardinality N under one-to-one modality mapping assumptions. This complexity imposes practical limitations on large-scale retrieval systems.

-----

Phase: [EXPLORATION]

### Source [25]: https://arxiv.org/html/2602.19367v1

Query: What limitations arise when applying nearest-neighbor metrics to measure representational alignment across modalities?

Answer: Nearest-neighbor metrics struggle with high dimensionality and scalability, often failing to capture true representational alignment across modalities. They also break down in many-to-many mappings, where one-to-one assumptions no longer hold. Computational complexity limits their use in large datasets. This metric captures local neighborhood agreement across modalities. Higher values indicate stronger preservation of neighborhood structure. We use k=5 in all computations as want to preserve the results on local structure and increasing it more would turn it into a global geometry metric. Figure 5 reports alignment quality across modality pairs as a function of total model size. Overall alignment improves with scale, but gains are highly uneven across modality pairs. TS–TXT alignment remains the weakest in absolute terms across all model sizes, reflecting the difficulty of directly aligning numeric signals with language, yet it also exhibits the strongest positive relationship with scale. In contrast, TS–IMG alignment achieves substantially higher absolute performance even at smaller scales, but shows weaker scaling trends, suggesting earlier saturation driven by stronger shared visual grounding with temporal data. Notably, global alignment across modalities is consistently strong, as reflected by cosine similarity and geometric metrics, while local neighborhood structure. We further show that semantic explicitness constrains how much shared structure can be recovered across modalities. Increasing information density improves alignment at low to moderate levels, but saturates beyond a latent threshold, indicating that alignment limits arise from representational mismatch rather than insufficient supervision or scale alone. Although scaling and improved optimization selectively help weaker modality pairs, architectural coupling and pretraining objectives also play a stronger role, as evidenced by the effectiveness of jointly pretrained VL models.

-----

Phase: [EXPLORATION]

### Source [26]: https://akoepke.github.io/cave_umwelten

Query: What limitations arise when applying nearest-neighbor metrics to measure representational alignment across modalities?

Answer: Nearest-neighbor metrics struggle with high dimensionality and scalability, often failing to capture true representational alignment across modalities. They also break down in many-to-many mappings, where one-to-one assumptions no longer hold. Computational complexity limits their use in large datasets. The core metric used by Huh et al. to measure cross-modal alignment is mutual k-nearest neighbors (mutual k-NN). Given paired image-text data, find the (k) nearest neighbors for each sample in both the vision and the language embedding space. Use the slider below to grow the dataset size. As it gets denser, both models find closer neighbors, but they stop agreeing on which one: Dataset size: 1,024 sparse dense. Measured Alignment Doesn't Hold Up for Real Data The original experiments used one-to-one image-text pairings. But real data is many-to-many: a single image can be described in countless ways, and a single caption can match many different images. When we progressively add more captions per image or more images per caption, mutual k-NN alignment drops consistently. Alignment when adding more images per caption Adding more images per caption using CycleReward data. Mutual k-NN alignment decreases consistently for both k=1 and k=10. Alignment when adding more captions per image Adding more captions per image gives the same pattern. Alignment drops as the one-to-one setting is relaxed. Coarse Agreement, Not Fine-Grained Convergence Dataset size: 1,024 sparse dense Interactive illustration of the mutual nearest neighbor metric (k=1). Each dot represents an image-text pair in the dataset, shown in image embedding space (left, DINOv2) and text embedding space (right, OpenLlama3b). The blue dot is the query, the other colored dots are the nearest neighbors in each space. On a small dataset (1,024 samples), both models agree on the same NN (green). As the dataset grows denser, each model finds a closer match in its own space, but they are not consistent. Hover over dots to see their image and caption. Alignment Degrades at Scale

-----

</details>

<details>
<summary>What 2025 studies extend Platonic Representation Hypothesis with new cross-architecture benchmarks?</summary>

Phase: [EXPLORATION]

### Source [29]: https://www.emergentmind.com/topics/platonic-representation-hypothesis

Query: What 2025 studies extend Platonic Representation Hypothesis with new cross-architecture benchmarks?

Answer: In astronomy, model scaling experiments reveal that foundation models trained on different astronomical modalities (imaging, spectroscopy) increasingly converge in their internal representations, as quantified by mutual k-nearest-neighbour scores. This convergence supports model interoperability and transfer across diverse data sources (UniverseTBD et al., 23 Sep 2025). Open questions persist regarding the uniqueness and generality of Platonic representations: the prevalence and quantification of “geometrically distinct” paths in combinatorial constructions; the full space of solution alignments in large nonlinear models; the extension of these ideas to semantic or agent-induced novelty in socio-economic data (O'Rourke, 2010, Murugaboopathy et al., 1 Aug 2025).

-----

Phase: [EXPLORATION]

### Source [31]: https://natecombs.substack.com/p/the-strong-platonic-representation

Query: What 2025 studies extend Platonic Representation Hypothesis with new cross-architecture benchmarks?

Answer: R. Jha, C. Zhang, V. Shmatikov, and J. X. Morris, “Harnessing the Universal Geometry of Embeddings,” arXiv preprint arXiv:2505.12540, May 2025. Our conjecture is as follows: neural networks trained with the same objective and modality, but with different data and model architectures, converge to a universal latent space such that a translation between their respective representations can learned without any pairwise correspondence. The Platonic Representation Hypothesis conjectures that the representation spaces of modern neural networks are converging. We assert the Strong Platonic Representation Hypothesis: the latent universal representation can be learned and harnessed to translate between representation spaces without any encoders or paired data.

-----

</details>

<details>
<summary>What open questions remain on convergence in scaling multimodal AI systems?</summary>

Phase: [EXPLORATION]

### Source [33]: https://arxiv.org/html/2502.01677v1

Query: What open questions remain on convergence in scaling multimodal AI systems?

Answer: However, as Scaling Up progresses, the field faces a critical bottleneck: data (Shumailov et al., 2024). The success of scaling has been largely contingent on the availability of massive, high-quality datasets. Foundational datasets like Common Crawl111 and large-scale multimodal Corpus have been extensively mined, leaving diminishing returns from further expansion. While multimodal data sources remain an underexplored frontier, their integration presents unique challenges, including alignment across modalities and domain-specific constraints. Moreover, the cost of processing this data at scale, in terms of both computational energy and infrastructure demands, compounds the difficulty of sustaining the current paradigm. These challenges underscore a pivotal question: can Scaling Up alone [...] Content creation platforms like TikTok, YouTube, and Instagram showcase how AI scaling transforms creativity and engagement. Scaling Up integrates vast multimodal datasets, enabling foundation models to analyze trends, predict preferences, and optimize recommendations on a global scale. These models, trained on billions of interactions, continuously evolve to match audience demands. Scaling Down brings AI closer to users, with lightweight models enabling real-time video, music, and AR generation on personal devices. On-device AI also enhances content moderation, ensuring platform safety without heavy computational costs. Scaling Out redefines these platforms as AI-driven ecosystems where specialized AI agents actively participate alongside human users. These AI contributors focus on [...] Effectively scaling AI requires quantitative models to predict performance and resource trade-offs. Developing scaling metrics for Scaling Down and Scaling Out can help assess efficiency, such as measuring performance gains relative to changes in model size, data, or compute (Kaplan et al., 2020). Formalized metrics also address industry concerns by providing predictable cost-benefit analyses. Scaling laws can estimate energy savings from replacing large models with smaller, task-specific AI, encouraging broader adoption of Scaling Down. Additionally, open benchmarks for Scaling Out should evaluate how distributed models communicate, adapt, and collaborate in real-world tasks, ensuring AI ecosystems remain robust and efficient (Dou et al., 2023).

-----

</details>

<details>
<summary>How does biological convergent evolution parallel representational convergence across AI architectures?</summary>

Phase: [EXPLORATION]

### Source [38]: https://arxiv.org/html/2507.01966v1

Query: How does biological convergent evolution parallel representational convergence across AI architectures?

Answer: The consistent brain-performance correlation across vastly different model architectures, training objectives, and modalities provides compelling evidence for a form of convergent evolution, whereby optimization for task performance naturally leads AI systems toward more brain-like representations without explicit neurobiological constraints. The substantially stronger correlations observed in language models compared to vision models likely reflects that language processing involves more abstract and complex cognitive operations, such as semantic integration, contextual reasoning, and compositional understanding, which may naturally drive both biological and artificial systems toward similar computational solutions. This modality gap in correlation strength is maintained across different model families. Our findings provide compelling evidence for convergent evolution between artificial and biological intelligence systems. Despite fundamentally different origins, architectures, and learning mechanisms, AI models spontaneously develop representations that progressively align with human brain activity patterns as they optimize for task performance. This emergent alignment occurs without explicit neurobiological constraints, suggesting that certain computational solutions may be universal for intelligent information processing, transcending specific physical implementations.

-----

Phase: [EXPLORATION]

### Source [39]: https://www.pnas.org/doi/10.1073/pnas.2319709121

Query: How does biological convergent evolution parallel representational convergence across AI architectures?

Answer: Our rationale is an extension of the well-known concept of convergent evolution, long established in evolutionary biology. In convergent evolution, finding parallel functions in remote species is taken to signify their crucial functionality which forced these remote systems to converge on finding parallel solutions despite their otherwise major discrepancies. We would like to propose here that this notion of convergence evolution can be extended to such unexpected “coincidental” parallels found between biological and artificial systems. The specific manifestation of the convergent evolution—in this case, its appearance specifically in intermediate levels of the artificial network hierarchy—is informative about the function of the biological face-areas’ relational geometry. The fact that the correlation is found in intermediate layers rather than the uppermost, fully connected layers, which reflects the labeling of personal identity bears significance. It supports the hypothesis that human face-selective cortical regions located in the fusiform gyrus likely function as a pictorial rather than identity representation, namely, representing how faces look like rather than whose face is presented in the images. Convergent evolution between Entorhinal grid cells and cosine basis functions. Examples of three Entorhinal grid neurons reflecting the typical hexagonal grid-like arrangement, and the different scales of grid distances along the entorhinal dorso-ventral axis. These grid cell images were DCT transformed and the most prominent basis function (the one with the largest coefficient of this transformation), marked by a red arrow, is depicted in the Upper-Right panels (CSB). Note the remarkable correspondence between the biological grid neurons and the CSBs, suggesting a parallel evolution between these two very different modes of representation.

-----

Phase: [EXPLORATION]

### Source [40]: https://arxiv.org/html/2505.23774v1

Query: How does biological convergent evolution parallel representational convergence across AI architectures?

Answer: To achieve effective internal decoupling in AI architectures, learning must prioritize the acquisition and encapsulation of fundamental processes—such as perceptual representations and behavioral patterns—mirroring how biological systems encapsulate core processes to enhance reuse and minimize interference. These processes can serve as building blocks for more complex functions and be interconnected through weak linkages. Biological organisms consistently showcase fundamental structural properties like modularity, hierarchy, repetition and correlated changes. These traits stem from the architecture of the regulatory networks previously discussed, such as reuse of regulatory mechanisms across various processes (repetition/correlation), distinct gene sets regulating different parts of the organism (modularity), or higher-level regulatory genes controlling the

-----

Phase: [EXPLORATION]

### Source [41]: https://3dvar.com/Huh2024The.pdf

Query: How does biological convergent evolution parallel representational convergence across AI architectures?

Answer: The second finding agrees with extensive research that oriented Gabor-like filters are common in both artificial and biological vision systems. This suggests a convergence to a similar initial layer of representation across various neural network architectures. Bansal et al. (2021) expanded on the idea of model stitching, uncovering that models trained using self-supervised objectives align closely with their supervised counterparts. We conjecture that representation learning algorithms will converge on a shared representation of Z, and scaling model size, as well as data and task diversity, drives this convergence. This paper explores one aspect of this trend: representational convergence. We argue that there is a growing similarity in how datapoints are represented in different neural network models. This similarity spans across different model architectures, training objectives, and even data modalities. One indication of representational convergence is the rising number of systems built on top of pre-trained foundation models. These models are becoming standard backbones across a growing spectrum of tasks. Their versatility across numerous applications implies a level of universality in the way they represent data.

-----

Phase: [EXPLORATION]

### Source [42]: https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107

Query: How does biological convergent evolution parallel representational convergence across AI architectures?

Answer: The story of the Platonic representation hypothesis paper began in early 2023, a turbulent time for AI researchers. ChatGPT had been released a few months before, and it was increasingly clear that simply scaling up AI models — training larger neural networks on more data — made them better at many different tasks. But it was unclear why. That paper, like much of the early work on representational similarity, focused only on computer vision, which was then the most popular branch of AI research. The advent of powerful language models was about to change that. For Isola, it was also an opportunity to see just how far representational similarity could go. Convergent Evolution

-----

</details>

<details>
<summary>What philosophical shifts from Plato to 20th-century cognitive science shaped ideas of shared universal representations?</summary>

Phase: [EXPLORATION]

### Source [45]: https://mechanism.ucsd.edu/bill/research/philcogsci.pdf

Query: What philosophical shifts from Plato to 20th-century cognitive science shaped ideas of shared universal representations?

Answer: mind trades in representations has roots in the history of philosophy. An innovation of the cognitive revolution was its treatment of the brain, a physical system, as a representational system. One inspiration for the crucial idea that the mind uses representation is that human culture has developed a number of systems used to represent phenomena. The one initially most influential in cognitive science was natural language: we use spoken and written words to communicate with each other because words and the sentences composed from them represent things. But humans operate with a variety of non‐linguistic representational systems as well: maps, diagrams, pictures, and so on. Using such external representational systems as models, cognitive scientists posited that states in our heads could [...] cognitive scientists posited that states in our heads could similarly be understood as representing things outside the head. It is important to note, however, that these culturally created external representational systems do not function independently of human beings—if a sandstorm left a tracing in sand on the Martian surface with the shape “Stay out,” that would not be a representation as it was neither constructed by human beings nor processed by them. When “Stay out” is printed on a fence here on Earth, it was the fact that it is created and interpreted by human beings that makes it a representation. When cognitive science proposes to incorporate representations in the head as part of the explanation of how we perform cognitive tasks, including the task of interpreting external [...] behavior with events in the outside world. The states in the head are construed as re‐presentations of the phenomena outside the head. Consider how you are able to cook a meal from a memorized recipe (or, a bit more challenging, how good cooks can modify memorized recipes to create new dishes). The prototypical cognitive approach treats your knowledge of the recipe as a set of representations in your head and explains your behavior by positing causal processes operating on these representations. The challenge for cognitive science is to characterize these representations more precisely and identify the operations performed on them. There are differing views in cognitive science as to how to meet this challenge. The idea that the mind trades in representations has roots in the history of

-----

Phase: [EXPLORATION]

### Source [47]: https://plato.stanford.edu/archives/win2023/entries/cognitive-science

Query: What philosophical shifts from Plato to 20th-century cognitive science shaped ideas of shared universal representations?

Answer: Attempts to understand the mind and its operation go back at least to the Ancient Greeks, when philosophers such as Plato and Aristotle tried to explain the nature of human knowledge. The study of mind remained the province of philosophy until the nineteenth century, when experimental psychology developed. Wilhelm Wundt and his students initiated laboratory methods for studying mental operations more systematically. Within a few decades, however, experimental psychology became dominated by behaviorism, a view that virtually denied the existence of mind. According to behaviorists such as J. B. Watson, psychology should restrict itself to examining the relation between observable stimuli and observable behavioral responses. Talk of consciousness and mental representations [...] Some philosophy, in particular naturalistic philosophy of mind, is part of cognitive science. But the interdisciplinary field of cognitive science is relevant to philosophy in several ways. First, the psychological, computational, and other results of cognitive science investigations have important potential applications to traditional philosophical problems in epistemology, metaphysics, and ethics. Second, cognitive science can serve as an object of philosophical critique, particularly concerning the central assumption that thinking is representational and computational. Third and more constructively, cognitive science can be taken as an object of investigation in the philosophy of science, generating reflections on the methodology and presuppositions of the enterprise. [...] Most work in cognitive science assumes that the mind has mental representations analogous to computer data structures, and computational procedures similar to computational algorithms. Cognitive theorists have proposed that the mind contains such mental representations as logical propositions, rules, concepts, images, and analogies, and that it uses mental procedures such as deduction, search, matching, rotating, and retrieval. The dominant mind-computer analogy in cognitive science has taken on a novel twist from the use of another analog, the brain.

-----

</details>

<details>
<summary>How do foundation models act as enabling technologies for cross-modal representation translation in robotics?</summary>

Phase: [EXPLORATION]

### Source [48]: https://arxiv.org/html/2507.10087v1

Query: How do foundation models act as enabling technologies for cross-modal representation translation in robotics?

Answer: Foundation models enable cross-modal representation translation in robotics by integrating diverse sensor data into unified representations, facilitating perception, planning, and control. They enhance sim-to-real transfer and support complex reasoning tasks. Foundation models provide robust, generalizable knowledge for robot autonomy. The rapid emergence of foundation models, particularly Large Language Models (LLMs) and Vision-Language Models (VLMs), has introduced a transformative paradigm in robotics. These models offer powerful capabilities in semantic understanding, high-level reasoning, and cross-modal generalization, enabling significant advances in perception, planning, control, and human-robot interaction. Foundation models offer promising solutions by facilitating reliable transfer through improved domain-invariant representations and improved policy generalization. Emerging methods leverage LLMs not as direct task controllers, but rather to refine simulations or training processes, resulting in robust real-world performance. Such approaches exploit the extensive prior knowledge and abstraction capabilities inherent in foundation models, enabling efficient transfer across robotic platforms. Yu et al. introduced Octopi, a tactile language model that combines an LLM with a touch sensor to infer object properties. They validate the model in cases where tactile features such as softness relate to abstract concepts such as ripeness through language-based reasoning. This enables sensory input to be interpreted with human-centric semantics, supporting generalization to novel tasks. Foundation models shape robotic perception by enabling open-ended visual recognition, semantic alignment across modalities, and elementary physical reasoning from sensory signals.

-----

Phase: [EXPLORATION]

### Source [49]: https://www.ashpress.org/index.php/jcts/article/download/248/199

Query: How do foundation models act as enabling technologies for cross-modal representation translation in robotics?

Answer: The survey further examines key training strategies such as contrastive learning, multimodal pretraining, and instruction-based alignment methods that enable effective cross-modal representation learning. Finally, we discuss emerging applications of multimodal foundation models in domains such as healthcare, robotics, and intelligent interactive systems. Another important line of research explores embodied multimodal models that integrate perception with physical interaction capabilities. Models such as PaLM-E combine multimodal perception with robotic control systems, enabling robots to interpret visual observations and natural language instructions while performing physical actions in real-world environments. This research highlights the potential of multimodal models to support intelligent agents capable of interacting with both digital and physical environments. Overall, the rapid development of multimodal foundation models demonstrates the growing importance of cross-modal representation learning. In addition to healthcare, multimodal models are increasingly used in robotics and autonomous systems. Robots operating in real-world environments must interpret complex sensory inputs that include visual perception, audio signals, spatial information, and human language instructions. Multimodal foundation models provide a unified framework for integrating these diverse data sources, enabling robots to perform tasks that require both perception and reasoning.

-----

Phase: [EXPLORATION]

### Source [50]: https://www.emergentmind.com/topics/robot-foundation-model

Query: How do foundation models act as enabling technologies for cross-modal representation translation in robotics?

Answer: Key characteristics distinguishing RFMs include: Zero-shot and few-shot generalization to unseen downstream tasks and environments. Unified representation space enabling cross-modal transfer of knowledge between vision, language, and action. Plug-and-play modularity within the robot autonomy stack, supporting perception, planning, or control without core retraining. A robot foundation model is a large, pre-trained, parameterized neural function Fθ:Xv×Xl×Xp→Z mapping high-dimensional, multi-modal robotic observations—including vision (Xv), language (Xl), and proprioceptive states (Xp)—to a latent embedding Z that encodes generalizable world knowledge and affordances. Pre-trained on expansive, heterogeneous datasets, these models are adapted via prompting or fine-tuning for a broad spectrum of downstream embodied tasks, from high-level planning to low-level control, serving as the core algorithmic substrate for enabling generalist, scalable, and robust robot behavior. Robot foundation models are large, pre-trained, multimodal networks that encode generalizable world knowledge from vision, language, and proprioceptive data. They integrate high-level planning with low-level control using architectures like transformers, cross-attention, and modular fusion techniques.

-----

Phase: [EXPLORATION]

### Source [51]: https://ashpress.org/index.php/jcts/article/view/248

Query: How do foundation models act as enabling technologies for cross-modal representation translation in robotics?

Answer: This paper presents a comprehensive survey of multimodal foundation models, focusing on architectural design principles, training paradigms, and emerging application domains. We review representative multimodal architectures, including transformer-based cross-modal fusion frameworks and vision-language models that integrate perception with language reasoning capabilities. The survey further examines key training strategies such as contrastive learning, multimodal pretraining, and instruction-based alignment methods that enable effective cross-modal representation learning. Finally, we discuss emerging applications of multimodal foundation models in domains such as healthcare, robotics, and intelligent interactive systems. Multimodal foundation models have emerged as a transformative paradigm in artificial intelligence by enabling unified learning across heterogeneous data modalities such as images, text, audio, and sensor signals. Unlike traditional unimodal learning systems, multimodal models are capable of integrating diverse information sources to perform complex perception and reasoning tasks that more closely resemble human cognitive processes. Recent advances in large-scale pretraining, transformer architectures, and cross-modal representation learning have significantly accelerated the development of multimodal models capable of performing a wide range of tasks including visual question answering, image captioning, multimodal dialogue, and embodied reasoning.

-----

Phase: [EXPLORATION]

### Source [52]: https://aclanthology.org/2025.emnlp-main.843.pdf

Query: How do foundation models act as enabling technologies for cross-modal representation translation in robotics?

Answer: In this survey, we investigate the representation potentials of foundation models, defined as the latent capacity of their learned representations to capture task-specific information within a single modality while also providing a transferable basis for alignment and unification across modalities. We begin by reviewing representative foundation models and the key metrics that make alignment measurable. We then synthesize empirical evidence of representation potentials from studies in vision, language, speech, multimodality, and neuroscience. The evidence suggests that foundation models often exhibit structural regularities and semantic consistencies in their representation spaces, positioning them as strong candidates for cross-modal transfer and alignment. We further analyze the key factors contributing to these potentials. These results resonate with the Platonic Representation Hypothesis, which argues that foundation models are converging toward a common statistical model of reality embedded within their representation spaces. All these findings suggest that cross-modal convergence may reflect a deeper tendency of foundation models to discover modality-agnostic abstractions. This emerging evidence points to the possibility that foundation models, even when trained separately, may inhabit overlapping representational manifolds that facilitate alignment, transfer, and integration across modalities. A growing body of research has shown that the representations learned by foundation models are not only powerful in isolation but also exhibit strong similarity across architectures, training objectives, and even modalities. We refer to this capacity as the representation potential of foundation models.

-----

</details>

<details>
<summary>What emerging trends in neuro-symbolic AI leverage convergent representations for hybrid reasoning systems?</summary>

Phase: [EXPLORATION]

### Source [54]: https://www.sciencedirect.com/science/article/pii/S2667305325000675

Query: What emerging trends in neuro-symbolic AI leverage convergent representations for hybrid reasoning systems?

Answer: Neuro-symbolic AI represents the convergence of two principal paradigms in artificial intelligence: neural networks, which are efficient in data-driven learning, and symbolic reasoning, which offers explainability and logical inference. This hybrid methodology combines the adaptability of neural networks with symbolic AI's interpretability and formal reasoning abilities, which provide a practical framework for advanced cognitive systems. This paper analyzes the present condition of neuro-symbolic AI, emphasizing essential techniques that combine reasoning and learning. We explore models such as Logic Tensor Networks, Differentiable Logic Programs, and Neural Theorem Provers. The study analyzes their impact on the advancement of cognitive systems in natural language processing, robotics,

-----

Phase: [EXPLORATION]

### Source [56]: https://arxiv.org/html/2511.17644v1

Query: What emerging trends in neuro-symbolic AI leverage convergent representations for hybrid reasoning systems?

Answer: Looking forward, the field’s trajectory points to hybrid architectures that are adaptive, multimodal, and self-healing. These systems will evolve under the dual pressures of technical innovation and regulatory oversight, requiring balance between autonomy and accountability. By placing ethics at the core of design and leveraging both neural and symbolic reasoning, hybrid AI can become a trusted collaborator in high-stakes environments, advancing not only performance but also societal trust in artificial intelligence. [...] Recent work in trustworthy AI emphasizes fairness, accountability, transparency, and human oversight. Neuro-symbolic hybrids offer practical tools to operationalize these principles by binding statistical inference to symbolic guardrails. This convergence aligns closely with emerging regulatory frameworks, ensuring that AI systems can be both high-performing and ethically compliant. [...] Hybrid neuro-symbolic models are also emerging in critical infrastructure such as energy grids, transportation systems, and defense operations. These environments require robust anomaly detection and fault diagnosis under tight ethical and safety guardrails. A neural model may detect unusual sensor activity in a power grid, while symbolic reasoning ensures that mitigation strategies comply with operational safety standards. Explanations include root-cause analysis paired with the logical rules applied, allowing human operators to validate or override system recommendations [isaca2023bias].

-----

Phase: [EXPLORATION]

### Source [57]: https://en.wikipedia.org/wiki/Neuro-symbolic_AI

Query: What emerging trends in neuro-symbolic AI leverage convergent representations for hybrid reasoning systems?

Answer: Since 2020, interest in neuro-symbolic AI has surged much further with the rise of foundation models such as LLMs highlighting the limitations of pure neural networks, such as hallucinations, lack of understanding of the mechanisms behind sudden variations in performance, and lack of sound reasoning or poor systematic generalization beyond training data distributions. As a response, hybrid LLMs with symbolic tools started to appear, which combine LLMs with theorem provers, logic verifiers or proof assistants, functional programming, databases and logic programs. This is one of the first times that neuro-symbolic AI has seen a significant industry adoption in companies such as Amazon (Vulcan and Rufus AI), Google (AlphaGeometry) and Anthropic [...] Neuro-symbolic AI is a subfield of artificial intelligence that combines neural networks and symbolic AI approaches, such as knowledge representation and automated reasoning, to create more robust, more reliable, and more trustworthy AI. This combination allows statistical patterns to be combined with explicitly defined rules and knowledge to give AI systems the ability to better represent, reason and generalize. Thus, neuro-symbolic AI provides a reasoning infrastructure to state-of-the-art machine learning for solving a wider range of problems more effectively. [...] Symbolic Neuro symbolic is the current approach of many neural models in natural language processing, where words or subword tokens are the ultimate input and output of large language models. Examples include BERT and GPT-3. Symbolic[Neuro] is a hybrid architecture where symbolic techniques are used to invoke neural techniques. It is exemplified by AlphaGo, where the symbolic approach is Monte Carlo tree search and the neural techniques learn how to evaluate game positions. Neural | Symbolic uses a neural architecture to interpret perceptual data as symbols and relationships that are further reasoned about symbolically; Neural-Concept Learner is one example of such a system and Google DeepMind's AlphaProof Nexus is another.

-----

</details>

<details>
<summary>How does dog concept example motivate Platonic representation hypothesis?</summary>

Phase: [EXPLORATION]

### Source [58]: https://3dvar.com/Huh2024The.pdf

Query: How does dog concept example motivate Platonic representation hypothesis?

Answer: The Platonic Representation Hypothesis suggests AI models develop a shared understanding of reality, regardless of their specific training, akin to Plato's ideal forms. Evidence shows neural networks converge in representing objects like dogs, indicating a common underlying structure. This shared representation is termed the "platonic representation." In the paper, the dog example illustrates convergence: different neural networks, even when trained on distinct tasks like scene recognition or colorization, develop similar internal representations, such as dog face detectors. This convergence across models and modalities supports the idea that representations are aligning toward a shared statistical model of reality, driven by simplicity bias and other selective pressures, rather than diverging into overly complex or distinct forms.

-----

Phase: [EXPLORATION]

### Source [62]: https://proceedings.mlr.press/v235/huh24a.html

Query: How does dog concept example motivate Platonic representation hypothesis?

Answer: The paper argues representations in deep networks are converging toward a shared statistical model of reality. The dog example from related literature shows convergence in object detection across tasks, motivating the hypothesis by demonstrating alignment in how models represent data points like dogs, regardless of training differences.

-----

</details>

<details>
<summary>What nuances distinguish rank-order neighbors from CKA in representation comparison?</summary>

Phase: [EXPLORATION]

### Source [63]: https://proceedings.mlr.press/v162/barannikov22a/barannikov22a.pdf

Query: What nuances distinguish rank-order neighbors from CKA in representation comparison?

Answer: Rank-order neighbors (RTD) considers persistence across scales, while CKA focuses on pairwise distances without rank order. RTD captures architecture's block structure better, while CKA can be chaotic. RTD is more robust to hyperparameters than CKA. RTD reveals a nice monotonic pattern w.r.t. a number of neighbors, while values of CKA are quite chaotic. Visual inspection reveals apparent incoherences of CKA. According to CKA, U(10) is closer to U(200) than to U(20); also U(200) is closer to U(10) than to U(100). We observe that RTD catches architecture’s block structure better than CKA, SVCCA. The ResNet-50 architecture has sequence of blocks in form [3, 4, 6, 3] and it can be seen that RTD highlights it with sub-squares of corresponding sizes.

-----

Phase: [EXPLORATION]

### Source [64]: https://arxiv.org/html/2510.22953v1

Query: What nuances distinguish rank-order neighbors from CKA in representation comparison?

Answer: CKA is globally density-weighted: a single high-density region of large distances can dominate the score. kCKA mitigates this by restricting interactions to local k-NN neighborhoods, making it less susceptible to interactions from large distances. MKA goes further by ordering neighbors within each neighborhood and assigning weights that depend on rank and local density. In essence, vanilla CKA ignores ranks and depends solely on pairwise distances, while kCKA merely dichotomizes pairs into “within-k” vs “outside-k” and treats the k nearest neighbors essentially uniformly. RTD, a topological approach, sometimes tracks true topology and other times behaves like CKA. Our hypothesis is scale: RTD relies on persistence across scales (barcodes), whereas kCKA and MKA are single-scale (k-NN). CKA with σ=M fails to align the manifold of Swiss-roll and S-curve (r=0.5), giving a lower value. However, for cases where the 1-D manifold structure is absent (e.g., r<0.4 and r>0.6), CKA provides a higher value. On the contrary, CKA with δ=0.2, kCKA, and MKA properly capture the alignment of the two shapes. kCKA is more sensitive to the number of nearest neighbors k, while MKA is very robust to the parameter.

-----

</details>

<details>
<summary>What alignment scores show cross-modal convergence in scaled AI models?</summary>

Phase: [EXPLORATION]

### Source [65]: https://akoepke.github.io/cave_umwelten

Query: What alignment scores show cross-modal convergence in scaled AI models?

Answer: Cross-modal alignment scores drop significantly when scaling AI models from 1,024 to 15 million samples, from 13.5% to 0.81%. The core metric used is mutual k-nearest neighbors (mutual k-NN). Alignment degrades as dataset size increases. Huh et al. themselves ask whether the obtained mutual kNN score is “indicative of strong alignment with the remaining gap being ‘noise’ or does it signify poor alignment with major differences left to explain?” When scaling from 1,024 to 15 million samples, the alignment score drops from 13.5% to just 0.81%, leaving very little room for a convergence narrative. Alignment scores on WIT across dataset sizes. Scaling the dataset to 1M (WIT) shows a large drop in mutual k-NN alignment for both k=1 and k=10. Alignment scores on LAION-15M across dataset sizes. We see a similar alignment degradation on LAION-15M when scaling to 15M samples. The core metric used by Huh et al. to measure cross-modal alignment is mutual k-nearest neighbors (mutual k-NN). Given paired image-text data, find the (k) nearest neighbors for each sample in both the vision and the language embedding space. As the dataset gets denser, each modality can find neighbors that are closer in its own space, and the overlap vanishes. 13.5% Alignment on WIT-1024 (k=10). 0.8% Alignment on LAION-15M (k=10). 16× Drop in alignment when scaling up.

-----

Phase: [EXPLORATION]

### Source [66]: https://arxiv.org/html/2507.01966v1

Query: What alignment scores show cross-modal convergence in scaled AI models?

Answer: Layer-wise and multi-scale alignment analyses revealed systematic gradients of representational organization. Vision models show a gradual increase in brain alignment with depth, paralleling the hierarchical progression from low-level to high-level visual processing in the brain. Language models exhibit stronger and more distributed alignment, corresponding to association areas involved in abstract semantic processing. Importantly, deeper vision model layers begin to resemble language models, suggesting cross-modal convergence at higher abstraction levels. Multi-scale analysis further revealed a posterior-to-anterior shift in alignment across brain regions, consistent with a transition from localized, feature-specific representations to distributed, integrative. Language models exhibit strongest alignment with limbic and integrative regions, while vision models show progressive alignment with visual cortices; and as representational scale increases, alignment systematically shifts from primary sensory to higher-order. Importantly, these alignment patterns were highly consistent across different subjects, as demonstrated by the strong inter-subject correlations in both vision and language modalities. Our comprehensive consistency analysis verified this robustness, with inter-subject correlations ranging from 0.997 to 1.000 for language models and 0.970 to 0.999 for vision models.

-----

Phase: [EXPLORATION]

### Source [67]: https://openaccess.thecvf.com/content/ICCV2025/papers/Huang_Deciphering_Cross-Modal_Alignment_in_Large_Vision-Language_Models_via_Modality_Integration_ICCV_2025_paper.pdf

Query: What alignment scores show cross-modal convergence in scaled AI models?

Answer: This convergence also reflects the alignment between vision and text tokens throughout the language model layers, indicating the cross-modal alignment’s gradually stabilizing during pre-training. Additionally, MIR’s ability to track convergence provides practical value. By using MIR as a pre-training monitor, we can identify when the model has reached sufficient cross-modal alignment, allowing for early stopping and reducing unnecessary training costs. MIR Model Performance. MoCa achieves lower MIR and +1.5% average benchmark scores on LLaVA-v1.5, as well as +0.9% on Mini-Gemini. We report the reproduced results of Mini-Gemini since the data links provided by the official are partially unavailable. with post-SFT performance, making it a strong indicator of effective pre-training.

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="Harnessing the Universal Geometry of Embeddings.md">
<details>
<summary>Harnessing the Universal Geometry of Embeddings</summary>

Phase: [EXPLORATION]

**Source URL:** <https://natecombs.substack.com/p/the-strong-platonic-representation>

# Harnessing the Universal Geometry of Embeddings

Rishi Jha Collin Zhang Vitaly Shmatikov John X. Morris Department of Computer Science Cornell University

### 1 Introduction

Text embeddings are the backbone of modern NLP, powering tasks like retrieval, RAG, classification, and clustering. There are many embedding models trained on different datasets, data shufflings, and initializations. An embedding of a text encodes its semantics: a good model maps texts with similar semantics to vectors close to each other in the embedding space. Since semantics is a property of text, different embeddings of the same text should encode the same semantics. In practice, however, different models encode texts into completely different and incompatible vector spaces.

The Platonic Representation Hypothesis Huh et al. [\[18\]](#page-10-0) conjectures that all vision models of sufficient size converge to the same latent representation. We propose a stronger, constructive version of this hypothesis for text models: the universal latent structure of text representations can be learned and, furthermore, harnessed to translate representations from one space to another without any paired data or encoders.

<span id="page-1-2"></span>![](_page_1_Figure_0.jpeg)

Figure 2: Given only a vector database from an unknown model, vec2vec translates the database into the space of a known model using latent structure alone. Converted embeddings reveal sensitive information about the original documents, such as the topic of an email (pictured, real example).

In this work, we show that the Strong Platonic Representation Hypothesis holds in practice. Given unpaired examples of embeddings from two models with different architectures and training data, our method learns a latent representation in which the embeddings are almost identical (Figure 1).

We draw inspiration from research on aligning word embeddings across languages [62, 10, 15, 9] and unsupervised image translation [36, 70]. Our vec2vec method uses adversarial losses and cycle consistency to learn to encode embeddings into a shared latent space and decode with minimal loss. This makes unsupervised translation possible. We use a basic adversarial approach with vector space preservation [46] to learn a mapping from an unknown embedding distribution to a known one.

vec2vec is the first method to successfully translate embeddings from the space of one model to another without paired data. vec2vec translations achieve cosine similarity as high as 0.96 to the ground-truth vectors in their target embedding spaces and perfect matching on over 8000 shuffled embeddings (without access to the set of possible matches in advance).

To show that our translations preserve not only the relative geometry of embeddings but also the semantics of underlying inputs, we extract information from them using zero-shot attribute inference and inversion, without any knowledge of the model that produced the original embeddings.<sup>2</sup>

#### 2 Problem formulation: unsupervised embedding translation

Consider a collection of embedding vectors  $\{u_1, \ldots u_n\}$ , for example, a dump of a compromised vector database, where each  $u_i = M_1(d_i)$  is generated by an unknown encoder  $M_1 : \mathbb{V}^s \to \mathbb{R}^{d_{M_1}}$  from an unknown document  $d_i$ . We cannot make queries to  $M_1$  and do not know its training data, nor architectural details. Our goal is to extract any information about the documents  $d_i$ .

We do assume access to a different encoder  $M_2$  that we can query at will to generate new embeddings in some other space. We also assume high-level distributional knowledge about the hidden documents: their modality (text) and language (e.g., English). To extract information, we may translate  $\{u_1, \ldots u_n\}$  into the output space of  $M_2$  and apply techniques like inversion that require the encoder.

**Limitations of correspondence methods.** There is significant prior research on the problem of *matching* or *correspondence* between sets of embedding vectors [1, 49, 8, 54]. These methods typically assume that the two (or more) sets of embeddings are generated by different encoders on the *same or highly-overlapping inputs*. In other words, for each unknown vector, there must already exist a set of candidate vectors in a different embedding. In practice, it is unrealistic to expect that such a database be available, so these methods are not directly applicable. Some matching methods,

<span id="page-1-0"></span><sup>&</sup>lt;sup>1</sup>Prior work has successfully translated *word* embeddings between languages, typically relying on overlapping vocabularies across languages. In contrast, we translate embeddings of entire sequences between model spaces.

<span id="page-1-1"></span><sup>&</sup>lt;sup>2</sup>Our code is available on GitHub.

![](_page_2_Figure_0.jpeg)

Figure 3: Unsupervised embedding translation. With access to only  $u_i = M_1(d_i)$ , vec2vec seeks to generate a translation  $F(u_i)$  that is close in  $M_2$ 's embedding space to the ideal embedding  $v_i = M_2(d_i)$  without access to  $d_i$ ,  $v_i$ , or  $M_1$ .

however, support translation between embedding spaces without overlapping inputs. Our experiments demonstrate that these methods struggle significantly, even when correspondence exists.

Our task is inherently more challenging than matching, because we do not assume access to encoder  $M_1$ , nor do we have additional representations of documents  $d_1, \ldots, d_n$  beyond their embeddings  $u_i = M_1(d_i)$ . Therefore, we rely solely on unsupervised *translation* from  $M_1$  to  $M_2$ . The effectiveness of such unsupervised translation approaches thus critically depends on identifying and leveraging shared geometric structures within the embedding spaces produced by  $M_1$  and  $M_2$ .

The Strong Platonic Representation Hypothesis. Our hope that unsupervised embedding translation is possible at all rests on the stronger version of the Platonic Representation Hypothesis [18]. Our conjecture is as follows: neural networks trained with the same objective and modality, but with different data and model architectures, converge to a universal latent space such that a translation between their respective representations can be learned without any pairwise correspondence.

**Translation enables information extraction.** Solving unsupervised translation will allow us to use information extraction tools designed to operate on vectors produced by known encoders. For example, we could apply inversion models [43, 67] to recover unknown documents  $\{d_i\}$ .

#### <span id="page-2-0"></span>3 Our method: vec2vec

Unsupervised translation has been successful in computer vision, using a combination of cycle consistency and adversarial regularization [36, 70]. Our design of vec2vec is inspired in part by these methods. We aim to learn embedding-space translations that are cycle-consistent (mapping to and from an embedding space should end in the same place) and indistinguishable (embeddings for the same text from either space should have identical latents).

#### 3.1 Architecture

We propose a modular architecture, where embeddings are encoded and decoded using space-specific adapter modules and passed through a shared backbone network. Figure 2 shows these components. Input adapters  $A_1:\mathbb{R}^d\to\mathbb{R}^Z$  and  $A_2:\mathbb{R}^d\to\mathbb{R}^Z$  transform embeddings from each encoder-specific space into a universal latent representation of dimension Z. The shared backbone  $T:\mathbb{R}^Z\to\mathbb{R}^Z$  extracts a common latent embedding from adapted inputs. Output adapters  $B_1:\mathbb{R}^Z\to\mathbb{R}^d$  and  $B_2:\mathbb{R}^Z\to\mathbb{R}^d$  translate these common latent embeddings back into the encoder-specific spaces. Thus, translation functions  $F_1,F_2$  and additional reconstruction mappings  $R_1,R_2$  are defined as:

$$F_1 = B_2 \circ T \circ A_1, \quad F_2 = B_1 \circ T \circ A_2 \quad R_1 = B_1 \circ T \circ A_1 \quad R_2 = B_2 \circ T \circ A_2$$

Parameters of all components are collectively denoted  $\theta = \{A_1, A_2, T, B_1, B_2\}$ .

Unlike images, embeddings do not have any spatial bias. Instead of CNNs, we use multilayer perceptrons (MLP) with residual connections, layer normalization, and SiLU nonlinearities. Discriminators mirror this structure but omit residual connections to simplify adversarial learning.

#### 3.2 Optimization

In addition to the 'generator' networks F and R, we introduce discriminators operating on both the latent representations of  $F(D_1^{\ell}, D_2^{\ell})$  and the output embeddings  $(D_1, D_2)$ .

Our goal is to train the parameters of  $\theta$  by solving:

$$\theta^* = \arg\min_{\theta} \max_{D_1, D_2, D_1^{\ell}, D_2^{\ell}} \mathcal{L}_{adv}(F_1, F_2, D_1, D_2, D_1^{\ell}, D_2^{\ell}) + \lambda_{gen} \mathcal{L}_{gen}(\theta), \tag{1}$$

where  $\mathcal{L}_{adv}$  and  $\mathcal{L}_{gen}$  represent adversarial and generator-specific constraints respectively and hyper-parameter  $\lambda_{gen}$  controls their tradeoff.

**Adversarial.** The adversarial loss encourages generated embeddings to match the empirical distributions of original embeddings both at the embedding and latent levels. Specifically, applying the standard GAN loss formulation [13] to both levels yields:

$$\begin{split} \mathcal{L}_{\text{adv}}(F_{1}, F_{2}, D_{1}, D_{2}, D_{1}^{\ell}, D_{2}^{\ell}) &= \mathcal{L}_{\text{GAN}}(D_{1}, F_{1}) + \mathcal{L}_{\text{GAN}}(D_{2}, F_{2}) \\ &+ \mathcal{L}_{\text{GAN}}(D_{1}^{\ell}, T \circ A_{1}) + \mathcal{L}_{\text{GAN}}(D_{2}^{\ell}, T \circ A_{2}). \end{split}$$

**Generator.** Because adversarial losses alone do not guarantee that translated embeddings preserve semantics [70], we introduce three additional constraints to help the generator learn a useful mapping:

*Reconstruction* enforces that an embedding, when mapped into the latent space and back into its original embedding space, closely matches its initial representation:

$$\mathcal{L}_{\text{rec}}(R_1, R_2) = \mathbb{E}_{x \sim p} \|R_1(x) - x\|_2^2 + \mathbb{E}_{y \sim q} \|R_2(y) - y\|_2^2.$$

where p and q are distributions of embeddings sampled from  $M_1$  and  $M_2$ , respectively.

Cycle-consistency acts as an unsupervised proxy for supervised pair alignment, ensuring that F and G can translate an embedding to the other embedding space and back again with minimal corruption:

$$\mathcal{L}_{CC}(F_1, F_2) = \mathbb{E}_{x \sim p} \|F_2(F_1(x)) - x\|_2^2 + \mathbb{E}_{y \sim q} \|F_1(F_2(y)) - y\|_2^2.$$

Vector space preservation (VSP) ensures that pairwise relationships between translated embeddings are consistent with the target space [46, 65]. Given a batch of B embeddings  $x_1, ..., x_B$  and  $y_1, ..., y_B$ , we sum their average pairwise distances after translation by both  $F_1$  and  $F_2$ :

$$\mathcal{L}_{\text{VSP}}(F_1, F_2) = \frac{1}{B^2} \sum_{i=1}^{B} \sum_{j=1}^{B} \left[ \|M_1(x_i) \cdot M_1(x_j) - F_2(M_2(y_i)) \cdot F_2(M_2(y_j))\|_2^2 + \|M_2(y_i) \cdot M_2(y_j) - F_1(M_1(x_i)) \cdot F_1(M_1(x_j))\|_2^2 \right]$$

Combining these losses yields:  $\mathcal{L}_{\text{gen}}(\theta) = \lambda_{\text{rec}} \mathcal{L}_{\text{rec}}(R_1, R_2) + \lambda_{\text{CC}} \mathcal{L}_{\text{CC}}(F_1, F_2) + \lambda_{\text{VSP}} \mathcal{L}_{\text{VSP}}(F_1, F_2)$ , where hyperparameters  $\lambda_{\text{CC}}$ ,  $\lambda_{\text{rec}}$ , and  $\lambda_{\text{VSP}}$  control relative importance.

#### 4 Experimental setup

#### 4.1 Preliminaries

**Datasets.** We use the *Natural Questions* (*NQ*) [25] dataset of user queries and Wikipedia-sourced answers for training (a 2-million subset) and evaluation (a 65536 subset). To evaluate information extraction, we use *TweetTopic* [2], a dataset of tweets multi-labeled by 19 topics; a random 8192-record subset of *Pseudo Re-identified MIMIC-III* (*MIMIC*) [28], a pseudo re-identified version of the MIMIC dataset [19] of patient records multi-labeled by 2673 MedCAT [24] disease descriptions; and a random 50-email subset of the *Enron Email Corpus* (*Enron*) [21], an unlabeled, public dataset of internal emails from a defunct energy company. In Appendix D, we ablate a model on *MS COCO* [34], a captioned image dataset, to evaluate performance on multimodal retrieval.

**Models.** Table 1 lists the embedding models representing four size categories, five transformer backbones, and two output dimensionalities. Granite is multilingual; CLIP is multimodal. Since Qwen is very compute-intensive, we only evaluate it for a single model pair in Appendix C.

<span id="page-4-0"></span>

| Model                   | Params (M) | Backbone     | Year         | Dims       | Max Seq.   |
|-------------------------|------------|--------------|--------------|------------|------------|
| [47] gtr                | 110        | T5           | 2021         | 768        | 512        |
| [50] clip<br>[58] e5    | 151<br>109 | CLIP<br>BERT | 2021<br>2022 | 512<br>768 | 77<br>512  |
| [32] gte<br>[68] stella | 109<br>109 | BERT<br>BERT | 2023<br>2023 | 768<br>768 | 512<br>512 |
| [14] granite            | 278        | RoBERTa      | 2023         | 768        | 512        |
| [69] qwen               | 4000       | Qwen3        | 2025         | 2560       | 32K        |

Table 1: Embedding models used in our experiments.

**Training.** Unless otherwise specified, each vec2vec is trained on two sets of embeddings generated from disjoint sets of 1 million 64-token sequences sampled from NQ (see Section 7 for experiments with fewer embeddings). Due to GAN instability [53], we select the best of multiple initializations (see Appendix E) and leave more robust training to future work. See Appendix A for compute details.

#### 4.2 Evaluating translation

Let  $u_i = M_1(d_i)$  and  $v_i = M_2(d_i)$  denote the source and target embeddings of the same input  $d_i$ . The goal of translation is to generate a vector that is as close to  $v_i$  as possible. We say that  $(u_i, v_j)$  are "aligned" by the translator F if  $v_j$  is the closest embedding to  $F(u_i)$ :  $j = \arg\min_k \cos(F(u_i), v_k)$ . A perfect translator  $F^*$  satisfies  $i = \arg\min_k \cos(F^*(u_i), v_k)$  for all i.

Given (unknown) embeddings  $\{M_2(d_j)\}_{j=0}^n$  ordered by decreasing cosine similarity to  $F(u_i)$ , let  $r_i$  be the rank of the correct embedding  $v_i=M_2(d_i)$ . To measure quality of F, we use three metrics. **Mean Cosine Similarity** measures how close translations are, on average, to their targets. **Top-1 Accuracy** is the fraction of translations whose target is closer than any other embedding. **Mean Rank** is the average rank of targets with respect to translations. The ideal translator  $F^*$  achieves mean similarity of 1.0, top-1 accuracy of 1.0, and mean rank of 1.0. Recall that a random alignment corresponds to a mean rank of  $\frac{n}{2}$ . Formally,

$$\cos(u_i, v_i) = \frac{1}{n} \sum_{i=1}^n \left[ 1 - \cos \left( F(u_i), v_i \right) \right] \quad \text{Top-1}(r) = \frac{1}{n} \sum_{i=1}^n \mathbf{1} \{ r_i = 1 \} \quad \text{Rank}(\mathbf{r}) = \frac{1}{n} \sum_{i=1}^n r_i$$

vec2vec is the first unsupervised embedding translator, thus there is no direct baseline. As our Naïve baseline, we simply use F(x)=x to measure geometric similarity between embedding spaces. The second (pseudo)baseline is Oracle-aided optimal transport. It assumes that candidate targets are known and is thus strictly easier vec2vec and the Naïve baseline. We solve optimal assignment,  $\pi^* = \arg\min_{\pi} \sum_{i=1}^n \cos(u_i, v_{\pi(i)})$ , via either the Hungarian, Earth Mover's Distance, Sinkhorn, or (Entropic) Gromov-Wasserstein algorithms, choosing the solver with the lowest rank for each experiment. See Appendix B for more details.

#### <span id="page-4-1"></span>4.3 Evaluating information extraction

We measure whether translation preserves semantics via attribute inference: for each translated embedding  $F(M_1(d_i))$ , our goal is to infer attributes  $c_i \subseteq \mathcal{C}$  of  $d_i$ .

The first method we use is **zero-shot embedding attribute inference**: calculate pairwise cosine similarities between  $F(M_1(d_i))$  and the embeddings of all attributes in  $\mathcal{C}$ , identify top k closest attributes, and measure whether they are correct via *top-k accuracy*:  $\frac{1}{n} \sum_{i=0}^{n} \mathbf{1} \{|c_i^k \cap c_i| \geq 1\}$ .

The second method is **embedding inversion** that recovers text inputs from embeddings. Since [43] requires a pre-trained inversion model for each embedding space, we use [67] instead to generate an approximation  $d_i'$  of  $d_i$  from  $F(M_1(d_i))$  in a zero-shot manner. We measure the extracted information using *LLM judge accuracy*: the fraction of translated embeddings for which GPT-40 determines that d' reveals information in d. See Appendix H for our prompt.

In addition to the Naïve baseline, we also consider an **Oracle attribute inference**: zero-shot classification with the correct embedding  $M_2(d)$  and class labels  $M_2(\mathcal{C})$ .

<span id="page-5-0"></span>![](_page_5_Figure_0.jpeg)

Figure 4: Pairwise cosine similarities of input embeddings (left) and their vec2vec latents (middle) across different embedding pairs. The absolute difference between the heatmaps plots is on the right. All numbers are computed on the same batch of 1024 NQ texts.

#### <span id="page-5-2"></span>5 vec2vec learns to translate embeddings without any paired data

We first show that vec2vec learns a universal latent space, then demonstrate that this space preserves the geometry of all embeddings. Therefore, we can use it like a **universal language of text encoders** to translate their representations without any paired data.

vec2vec learns a universal latent space. vec2vec projects embeddings  $M_{1,2,\ldots}$  into a shared latent space via compositions of input adapters  $(A_{1,2,\ldots})$  and a shared translator T. Figure 4 shows that even when the embeddings  $u_i=M_1(d_i)$  and  $v_i=M_2(d_i)$  are far apart (i.e., have low cosine similarity), their representations in vec2vec's latent space are incredibly close:  $T(A_1(u_i)) \approx T(A_2(v_i))$ . Figure 1 visualizes this (via two-dimensional projections) for vec2vec trained on GTE and GTR embeddings: the embeddings are far apart, but their latents are nearly overlapping.

<span id="page-6-0"></span>

|       |       |                       | TweetTopic |             |                       | MIMI  | С              |
|-------|-------|-----------------------|------------|-------------|-----------------------|-------|----------------|
| $M_1$ | $M_2$ | $\cos(\cdot)\uparrow$ | T-1 ↑      | Rank ↓      | $\cos(\cdot)\uparrow$ | T-1 ↑ | Rank ↓         |
| gran. | gtr   | 0.74 (0.0)            | 0.99       | 1.09 (0.1)  | 0.74 (0.0)            | 0.60  | 23.38 (1.6)    |
|       | gte   | 0.85 (0.0)            | 0.95       | 1.26 (0.1)  | 0.85 (0.0)            | 0.08  | 346.21 (7.8)   |
|       | stel. | 0.77 (0.0)            | 0.96       | 1.11 (0.0)  | 0.72 (0.0)            | 0.13  | 242.23 (6.1)   |
|       | e5    | 0.83 (0.0)            | 0.87       | 3.10 (0.7)  | 0.84 (0.0)            | 0.12  | 361.06 (8.7)   |
| gtr   | gran. | 0.79 (0.0)            | 0.98       | 2.41 (0.6)  | 0.78 (0.0)            | 0.51  | 35.27 (1.9)    |
|       | gte   | 0.85 (0.0)            | 0.96       | 1.29 (0.2)  | 0.84 (0.0)            | 0.12  | 279.56 (6.9)   |
|       | stel. | 0.77 (0.0)            | 0.96       | 1.10 (0.0)  | 0.72 (0.0)            | 0.27  | 127.92 (4.4)   |
|       | e5    | 0.80 (0.0)            | 0.53       | 13.38 (1.2) | 0.82 (0.0)            | 0.01  | 1413.80 (18.3) |
| gte   | gran. | 0.73 (0.0)            | 0.94       | 1.33 (0.1)  | 0.73 (0.0)            | 0.09  | 342.15 (7.8)   |
|       | gtr   | 0.71 (0.0)            | 0.95       | 1.29 (0.1)  | 0.69 (0.0)            | 0.12  | 256.63 (6.4)   |
|       | stel. | 0.86 (0.0)            | 1.00       | 1.00 (0.0)  | 0.85 (0.0)            | 1.00  | 1.00 (0.0)     |
|       | e5    | 0.83 (0.0)            | 0.91       | 1.57 (0.2)  | 0.86 (0.0)            | 0.54  | 17.71 (0.9)    |
| stel. | gran. | 0.79 (0.0)            | 0.99       | 1.09 (0.1)  | 0.77 (0.0)            | 0.14  | 221.95 (5.9)   |
|       | gtr   | 0.77 (0.0)            | 1.00       | 1.00 (0.0)  | 0.75 (0.0)            | 0.56  | 17.70 (1.0)    |
|       | gte   | 0.90 (0.0)            | 1.00       | 1.00 (0.0)  | 0.91 (0.0)            | 1.00  | 1.00 (0.0)     |
|       | e5    | 0.85 (0.0)            | 0.98       | 1.05 (0.0)  | 0.85 (0.0)            | 0.51  | 26.33 (1.2)    |
| e5    | gran. | 0.79 (0.0)            | 0.98       | 1.08 (0.0)  | 0.78 (0.0)            | 0.21  | 151.09 (4.6)   |
|       | gtr   | 0.67 (0.0)            | 0.80       | 3.10 (0.6)  | 0.66 (0.0)            | 0.01  | 1029.64 (14.9) |
|       | gte   | 0.87 (0.0)            | 0.99       | 1.02 (0.0)  | 0.87 (0.0)            | 0.60  | 32.59 (2.6)    |
|       | stel. | 0.75 (0.0)            | 0.98       | 1.06 (0.0)  | 0.75 (0.0)            | 0.46  | 32.12 (1.4)    |

Table 3: Out-of-distribution translations: vec2vecs trained on NQ and evaluated on the entire TweetTopic test set (800 tweets) and an 8192-record subset of MIMIC. The rank metric varies from 1 to 800 (for TweetTopic) and 8192 (for MIMIC), thus 400 and, respectively, 4096 correspond to a random ordering. Standard errors are shown in parentheses.

vec2vec translations mirror target geometry. Table 2 shows that vec2vec generates embeddings with near-optimal assignment across model pairs, achieving cosine similarity scores up to 0.92, top-1 accuracies up to 100%, and ranks as low as 1. In same-backbone pairings (e.g., (gte, e5)), vec2vec's top-1 accuracy and rank are comparable to both the naïve baseline and (surprisingly) the oracle-aided optimal transport. Although the embeddings generated by vec2vec are significantly closer to the ground truth than the naïve baseline, in same-backbone pairings the embeddings are close enough to be compatible. In cross-backbone pairings, vec2vec is far superior on all metrics, while baseline methods perform similarly to random guessing.

Table 3 shows that this performance extends to out-of-distribution data. Our vec2vec translators were trained on NQ (drawn from Wikipedia), yet exhibit high cosine similarity, high accuracy, and low rank when evaluated on tweets (which are far more colloquial and use emojis) and medical records (which contain domain-specific jargon unlikely to appear in NQ). In Appendix F, we show that baseline methods fail on cross-backbone embedding pairs.

<span id="page-6-1"></span>

|                            |                   |                                                      | vec2vec                      |                                                               |                                                                        | OT Baseline                  |                                                                                                                      |  |  |
|----------------------------|-------------------|------------------------------------------------------|------------------------------|---------------------------------------------------------------|------------------------------------------------------------------------|------------------------------|----------------------------------------------------------------------------------------------------------------------|--|--|
| $M_1$                      | $M_2$             | $\cos(\cdot)\uparrow$                                | T-1 ↑                        | Rank ↓                                                        | $\cos(\cdot) \uparrow$                                                 | T-1 ↑                        | Rank ↓                                                                                                               |  |  |
| gra.<br>gtr<br>gte<br>ste. | clip              | 0.78 (0.0)<br>0.73 (0.0)<br>0.62 (0.0)<br>0.77 (0.0) | 0.35<br>0.13<br>0.00<br>0.31 | 226.62 (3.2)<br>711.23 (5.9)<br>3233.41 (9.8)<br>286.69 (3.6) | 0.76 (0.0)<br>0.59 (0.0)<br><b>0.76 (0.0)</b><br>0.76 (0.0)            | 0.00<br>0.00<br>0.00<br>0.00 | 4073.58 (9.4) <sup>‡</sup><br>4096.78 (9.2) <sup>‡</sup><br>4026.96 (9.4) <sup>‡</sup><br>3955.71 (8.9) <sup>‡</sup> |  |  |
| e5                         | gra.<br>gtr       | 0.64 (0.0)<br>0.74 (0.0)<br>0.67 (0.0)               | 0.01<br>0.72<br>0.27         | 2568.21 (9.4)<br>4.46 (0.1)<br>155.11 (2.1)                   | 0.69 (0.0)<br>0.49 (0.0)                                               | 0.00<br>0.00<br>0.00         | $3771.52 (9.1)^{\ddagger}$ $4053.11 (9.4)^{\ddagger}$ $4096.35 (9.2)^{\ddagger}$                                     |  |  |
| clip                       | gte<br>ste.<br>e5 | 0.75 (0.0)<br><b>0.72 (0.0)</b><br>0.73 (0.0)        | 0.00<br>0.61<br>0.01         | 2678.90 (8.9)<br>22.50 (0.5)<br>1692.28 (8.2)                 | <b>0.85</b> ( <b>0.0</b> )<br>0.67 (0.0)<br><b>0.83</b> ( <b>0.0</b> ) | 0.00<br>0.00<br>0.00         | 4025.81 (9.3) <sup>‡</sup><br>3951.73 (8.9) <sup>‡</sup><br>3771.38 (9.0) <sup>‡</sup>                               |  |  |

Table 4: Translations between unimodal and multimodal (CLIP) embeddings: vec2vecs trained on NQ and evaluated on a 65536 text subset of NQ (chunked in batches of size 8192). Rank varies from 1 to 8192, thus 4096 corresponds to a random ordering. Since the embedding dimensionalities are different, only the Gromov-Wasserstein<sup>‡</sup> OT baseline is run and the naive baseline does not apply. Bold denotes best value.

<span id="page-7-0"></span>

|       |       | Tw      | eetTopic ( | k = 1) |       | M       | IMIC (k = | = 10) |       |
|-------|-------|---------|------------|--------|-------|---------|-----------|-------|-------|
| $M_1$ | $M_2$ | vec2vec | Naïve      | $M_1$  | $M_2$ | vec2vec | Naïve     | $M_1$ | $M_2$ |
|       | gtr   | 0.25    | 0.10       | 0.30   | 0.24  | 0.19    | 0.11      | 0.76  | 0.88  |
| oron  | gte   | 0.32    | 0.09       | 0.30   | 0.34  | 0.36    | 0.13      | 0.76  | 1.00  |
| gran. | stel. | 0.24    | 0.10       | 0.30   | 0.28  | 0.27    | 0.04      | 0.76  | 0.96  |
|       | e5    | 0.31    | 0.18       | 0.30   | 0.31  | 0.19    | 0.20      | 0.76  | 0.97  |
|       | gran. | 0.34    | 0.08       | 0.24   | 0.30  | 0.16    | 0.12      | 0.88  | 0.76  |
| o-t-u | gte   | 0.33    | 0.13       | 0.24   | 0.34  | 0.28    | 0.05      | 0.88  | 1.00  |
| gtr   | stel. | 0.30    | 0.10       | 0.24   | 0.28  | 0.25    | 0.07      | 0.88  | 0.96  |
|       | e5    | 0.30    | 0.04       | 0.24   | 0.31  | 0.09    | 0.09      | 0.88  | 0.97  |
|       | gran. | 0.37    | 0.04       | 0.34   | 0.30  | 0.18    | 0.11      | 1.00  | 0.76  |
| at a  | gtr   | 0.24    | 0.13       | 0.34   | 0.24  | 0.10    | 0.03      | 1.00  | 0.88  |
| gte   | stel. | 0.31    | 0.20       | 0.34   | 0.28  | 0.68    | 0.83      | 1.00  | 0.96  |
|       | e5    | 0.37    | 0.30       | 0.34   | 0.31  | 0.37    | 0.63      | 1.00  | 0.97  |
|       | gran. | 0.35    | 0.07       | 0.28   | 0.30  | 0.23    | 0.09      | 0.96  | 0.76  |
| -4-1  | gtr   | 0.26    | 0.13       | 0.28   | 0.24  | 0.22    | 0.09      | 0.96  | 0.88  |
| stel. | gte   | 0.38    | 0.36       | 0.28   | 0.34  | 0.90    | 0.98      | 0.96  | 1.00  |
|       | e5    | 0.35    | 0.34       | 0.28   | 0.31  | 0.38    | 0.46      | 0.96  | 0.97  |
|       | gran. | 0.33    | 0.15       | 0.31   | 0.30  | 0.14    | 0.07      | 0.97  | 0.76  |
| - 5   | gtr   | 0.26    | 0.22       | 0.31   | 0.24  | 0.11    | 0.04      | 0.97  | 0.88  |
| e5    | gte   | 0.34    | 0.28       | 0.31   | 0.34  | 0.47    | 0.66      | 0.97  | 1.00  |
|       | stel. | 0.26    | 0.16       | 0.31   | 0.28  | 0.36    | 0.40      | 0.97  | 0.96  |

Table 5: Information leakage via top-k zero-shot attribute inference: vec2vecs trained on NQ and evaluated on the TweetTopic test set (800 tweets) and an 8192-record subset of MIMIC.  $M_1$  and  $M_2$  represent *ideal* zero-shot inference: attributes and embeddings are encoded using the same model.

Finally, Table 4 shows that vec2vec can even translate to and from the space of CLIP, a multimodal embedding model which was trained in part on *image* data. While the translations are not as strong as in Table 2, vec2vec consistently outperforms the optimal transport baseline. These results show the promise of our method at adapting to new modalities: in particular, the embedding space of CLIP has been successfully connected to other modalities such as heatmaps, audio, and depth charts [12].

#### <span id="page-7-2"></span>**6** Using vec2vec translations to extract information

In this section, we show that vec2vec translations not only preserve the geometric structure of embeddings but also retain sufficient semantics to enable attribute inference.

**Zero-shot attribute inference.** Table 5 shows that attribute inference on vec2vec translations consistently outperforms the naïve baseline and often does better than the ideal zero-shot baseline which performs inference on ground-truth document and attribute embeddings in the same space (this baseline is imaginary since these embeddings are not available in our setting).

vec2vec translations even work for embeddings of medical records, which are much further from the training distribution than tweets. The attributes in this case are MedCAT disease descriptions, very few of which occur in the training data. Attribute inference on translated embeddings is comparable to the naïve baseline in samebackbone pairings and outperforms it (often greatly) in cross-backbone pairings. The fact that vec2vec preserves the semantics of concepts like "alveolar periostitis" (which never appears in its training data) is evidence that its latent space is indeed a universal representation.

<span id="page-7-1"></span>![](_page_7_Figure_7.jpeg)

Figure 5: Leakage of information via inversion. Trained on NQ and evaluated on a 50-email subset of the Enron Email Corpus. Cells denote judge accuracy.

**Zero-shot inversion.** Inversion, i.e., reconstruction of text inputs, is more ambitious than attribute inference. vec2vec translations retain enough semantic information that off-the-shelf, zero-shot inversion methods like [67], developed for embeddings computed by standard encoders, extract

```
Ground Truth: "Subject: Enron Bashing on Frontline \n Body:..."
Generation: "Some emails discussing NROn Employee/s Complaint To thePublic ..."
Ground Truth: "Subject: Trades for 3/1/02 \n Body: \n John , \n The following trades..."
Generation: "... future transactions may await John G..."
Ground Truth: " The following expense report is ready for approval..."
Generation: " The upcoming expense statement from YYYY MM Dec..."
```

Figure 6: Examples of Enron Email Corpus inversions that infer entities and content .

information for as many as 80% of emails and 67% of tweets given *only* their translated embeddings, for some model pairs (Figure [5](#page-7-1) and Appendix [G\)](#page-17-1). These inversions are imperfect and we leave development of specialized inverters for translated embeddings to future work. Nevertheless, as exemplified in Figure [6,](#page-8-1) they still extract potentially sensitive information such as individual and company names, dates, promotions, financial information, outages, and even lunch orders. In Appendix [H,](#page-17-0) we show the prompt we use to measure extraction.

### <span id="page-8-2"></span><span id="page-8-0"></span>7 Ablations

| Method               | cos(·) ↑   | T-1 ↑ | Rank ↓        |
|----------------------|------------|-------|---------------|
| vec2vec              | 0.75 (0.0) | 0.91  | 2.64 (0.1)    |
| Naïve Baseline       | 0.04 (0.0) | 0.00  | 4084.15 (9.2) |
| OT Baseline          | 0.70 (0.0) | 0.00  | 3064.16 (8.9) |
| – VSP loss           | 0.58 (0.0) | 0.00  | 4196.64 (9.2) |
| – CC loss            | 0.50 (0.0) | 0.00  | 3941.36 (9.3) |
| – latent GAN         | 0.49 (0.0) | 0.00  | 3897.09 (9.5) |
| – VSP and CC loss    | 0.47 (0.0) | 0.00  | 3365.24 (9.3) |
| – hyperparam. tuning | 0.50 (0.0) | 0.00  | 4011.73 (9.3) |

Table 6: gte → gtr translators trained without individual components of our method on NQ and evaluated on a 65536-text subset of NQ (chunked in batches of 8192). The rank metric varies from 1 to 8192, thus 4096 corresponds to a random ordering. Standard errors are shown in parentheses.

<span id="page-8-3"></span>Each component of our method is important. We ablate our method subtractively, measuring the key metrics after removing individual components of our algorithm (described in Section [3\)](#page-2-0). Table [6](#page-8-2) shows that each component appears to be *critical* to building good translations. While vec2vec's cos(·) is higher than the naïve baseline, it performs worse across the board than the OT baseline and does not preserve the geometry of the vector space.

| N                                  | cos(·) ↑                                             | T-1 ↑                        | Rank ↓                                                  |
|------------------------------------|------------------------------------------------------|------------------------------|---------------------------------------------------------|
| 1000000                            | 0.75 (0.0)                                           | 0.92                         | 2.73 (0.2)                                              |
| 10000<br>50000<br>100000<br>500000 | 0.57 (0.0)<br>0.74 (0.0)<br>0.74 (0.0)<br>0.75 (0.0) | 0.01<br>0.81<br>0.85<br>0.92 | 1462.21 (20.)<br>3.91 (0.6)<br>4.52 (0.4)<br>2.73 (0.2) |

Table 7: gte → gtr translators trained with different amounts of GTE data: vec2vec models trained on NQ and evaluated an 8192-record subset of NQ. The rank metric varies from 1 to 8192, thus 4096 corresponds to a random ordering. Standard errors are shown in parentheses.

vec2vecs can be trained with significantly less data. In Sections [5](#page-5-2) and [6,](#page-7-2) we use 1M-point subsets of NQ to train our vec2vec models. Now, we train the gte → gtr vec2vec with 1M GTR embeddings but fewer GTE embeddings. Table [7](#page-8-3) shows that with as few as 10K embeddings, the translators still learn something (i.e. are better than random). Translations trained on 50K embeddings are almost as good as those trained on 1M. Translations generally improve with more training data.

### 8 Related work

Representation alignment. Similarities between representations of different neural networks are investigated in [\[26,](#page-11-7) [31,](#page-11-8) [59,](#page-13-7) [5,](#page-10-10) [18,](#page-10-0) [61,](#page-13-8) [30\]](#page-11-9). Methods based on CCA [\[42\]](#page-12-8), SVCCA, [\[51\]](#page-12-9), CKA [\[23,](#page-11-10) [38\]](#page-12-10), ICA [\[63\]](#page-13-9), time-series [\[39\]](#page-12-11), and GUIs [\[16\]](#page-10-11) have been used to compare embeddings from different subspaces. [\[37,](#page-12-12) [45,](#page-12-13) [40,](#page-12-14) [57,](#page-13-10) [48\]](#page-12-15) harness representation similarity for zero-shot stitching, substitution, domain transfer, and multimodal adaptation. All rely on some amount of paired data, which is difficult to reduce [\[6\]](#page-10-12). Our method does not just measure similarity, we learn how to *translate* representations across spaces without any paired data.

Optimal transport. The problem of unsupervised optimal transport has been studied for image style transfer [\[17,](#page-10-13) [36,](#page-12-1) [70\]](#page-13-1), word translation [\[62,](#page-13-0) [10,](#page-10-1) [15,](#page-10-2) [9,](#page-10-3) [20\]](#page-11-11), and natural language sequence translation [\[52,](#page-12-16) [27,](#page-11-12) [1,](#page-10-4) [4,](#page-10-14) [64,](#page-13-11) [3\]](#page-10-15). Our method builds on these works, which often employ a combination of cycle-consistency and adversarial loss. Importantly, unlike prior word and sequence translation methods, multiple representations of the same input (e.g., heavily overlapping word vocabularies) are unavailable in our setting. [\[54\]](#page-12-4) proposes a solver for matching small sets of embeddings between different vision-language models. Our method goes well beyond matching by taking unknown embeddings and *generating* matching embeddings in the space of another model.

Embedding inversion. An emerging line of research investigates decoding text from language model embeddings [\[55,](#page-12-17) [29,](#page-11-13) [43\]](#page-12-5) and outputs [\[44,](#page-12-18) [7,](#page-10-16) [66\]](#page-13-12). vec2vec helps apply these to unknown embeddings, without an encoder or paired data, by translating them to the space of a known model.

Bridging modality gaps. Previous work has noted an inherent "gap" between image- and text-based models [\[33\]](#page-11-14) and proposed various ways to unify the modalities [\[56\]](#page-13-13). Some approaches feed image embeddings directly into language models [\[22,](#page-11-15) [60,](#page-13-14) [11,](#page-10-17) [35\]](#page-11-16), while others generate captions from image embeddings [\[41\]](#page-12-19) or even from text embeddings themselves [\[43\]](#page-12-5). [\[12\]](#page-10-9) introduces a shared embedding space that integrates inputs from multiple modalities, including text, audio, and vision. In contrast, our post-hoc approach directly translates between representations and complements these systems by enabling inputs from a wide variety of embedding models.

# 9 Discussion and Future Work

The Platonic Representation Hypothesis conjectures that the representation spaces of modern neural networks are converging. We assert the Strong Platonic Representation Hypothesis: the latent universal representation can be learned and harnessed to translate between representation spaces without any encoders or paired data.

In Section [5,](#page-5-2) we demonstrated that our vec2vec method successfully translates embeddings generated from unseen documents by unseen encoders, and the translator is robust to (sometimes very) outof-distribution inputs. This suggests that vec2vec learns domain-agnostic translations based on the universal geometric relationships which encode the same semantics in multiple embedding spaces.

In Section [6,](#page-7-2) we showed that vec2vec translations preserve sufficient input semantics to enable attribute inference. We extracted sensitive disease information from patient records and partial content from corporate emails, with access only to document embeddings and no access to the encoder that produced them. Better translation methods will enable higher-fidelity extraction, confirming once again that embeddings reveal (almost) as much as their inputs.

Our findings provide compelling evidence for the Strong Platonic Representation Hypothesis for textbased models. Our preliminary results on CLIP suggest that the universal geometry can be harnessed in other modalities, too. The results in this paper are but a *lower bound* on inter-representation translation. Better and more stable learning algorithms, architectures, and other methodological improvements will support scaling to more data, more model families, and more modalities.

# Acknowledgments and Disclosure of Funding

This research is supported in part by the Google Cyber NYC Institutional Research Program. RJ is supported by the Digital Life Initiative Fellowship and JM by the National Science Foundation.

## <span id="page-14-0"></span>A Compute

Our training and evaluation were conducted using diverse compute environments, including both local and cloud GPU clusters. Experiments were done on NVIDIA 2080Ti, L4, A40, and A100 GPUs, listed in order of increasing computational capacity.

For our final results, we trained 25 vec2vec models fully and 30 models partially (see Appendix [E\)](#page-15-2). The full models' training durations usually ranged from 1 to 7 days, depending on the specific GPU and model pair (which affected convergence rates). Partial convergence was stopped after 2 days. Due to the size of Qwen, our (qwen, gte) ablation was trained for 20 days on an A100. Taking a conservative estimate of the average training time, this amounted to approximately 176 GPU days (24 models × 4 days / model + 30 models × 2 days / model + 1 (qwen, gte) × 20 days / model).

Evaluation procedures varied by model type:

- The 10 main vec2vec models required ∼1 hour each for NQ, TweetTopic, and MIMIC evaluation (across GPU types), plus 30 minutes for attribute extraction on TweetTopic and MIMIC, and 1.5 hours for inversion and downstream LLM evaluation on Enron and TweetTopic. Naive baselines required ∼30 minutes each across all datasets.
- The 15 additional fully-trained models required 30 minutes each for NQ evaluation, with an extra 30 minutes for MS COCO evaluation of (clip, granite).
- Optimal transport baselines ran on CPU only, requiring ∼1 hour per dataset (three datasets for main models, one for others).

In total, our experiments consumed almost 176 GPU days for training and an additional 42 GPU hours for evaluation and analysis. An additional 45 CPU hours were required for optimal transport.

### <span id="page-14-1"></span>B Oracle-aided optimal transport baseline

Let u<sup>i</sup> = M1(di) and v<sup>i</sup> = M2(di) denote embeddings of the same document d<sup>i</sup> from two different embedding models. In Section [5,](#page-5-2) we solve the optimal assignment problem:

$$\pi^* = \arg\min_{\pi} \sum_{i=1}^n \cos(u_i, v_{\pi(i)}),$$

using four algorithms: Hungarian (linear sum assignment), Earth Mover's Distance (EMD), Sinkhorn, Gromov-Wasserstein. For the Gromov-Wasserstein algorithm, we try both the entropic and nonentropic variants with multiple hyperparameter configurations and select the best figure. Note that the optimal transport (OT) baseline computes matchings and transports between embeddings derived from the *same underlying texts*, strongly favoring OT methods. Nevertheless, OT still struggles when embeddings originate from different model backbones.

Since the Hungarian algorithm produces a discrete matching, it is evaluated only using Top-1 Accuracy, while the other algorithms are evaluated across all metrics. For each experiment, the lowest-rank solver is reported in Table [2](#page-5-1) and Table [4](#page-6-1) (denoted by symbols in the final column). Evaluation metrics are defined as follows:

- 1. Top-1 Accuracy: Fraction of embeddings correctly identified as closest pairs, calculated by either selecting the maximum transported mass per embedding or applying the Hungarian algorithm directly to the transport plan P. We report the higher accuracy between the two.
- 2. Mean Rank: Average rank position of the correct embedding match v<sup>i</sup> when sorted by descending transported mass Pij from u<sup>i</sup> :

$$rank(v_i) = position of v_i among sorted P_{ij}$$
.

3. Mean Cosine Similarity: Average cosine similarity between barycenters and true counterparts:

$$v_i' = \frac{\sum_{j=1}^n P_{ij} v_j}{\sum_{j=1}^n P_{ij}}, \quad \text{Similarity} = \frac{1}{n} \sum_{i=1}^n \cos(v_i', v_i).$$

# <span id="page-15-3"></span><span id="page-15-1"></span>C Translating to and from Qwen

| vec2vec     |             |                          |              |                          | OT Baseline              |              |                                |  |  |
|-------------|-------------|--------------------------|--------------|--------------------------|--------------------------|--------------|--------------------------------|--|--|
| M1          | M2          | cos(·) ↑                 | T-1 ↑        | Rank ↓                   | cos(·) ↑                 | T-1 ↑        | Rank ↓                         |  |  |
| gte<br>qwen | qwen<br>gte | 0.50 (0.0)<br>0.84 (0.0) | 0.92<br>0.88 | 2.28 (0.2)<br>2.49 (0.3) | 0.38 (0.0)<br>0.85 (0.0) | 0.00<br>0.00 | 425.28 (1.1)‡<br>425.07 (1.2)‡ |  |  |

Table 8: Translations between GTE and Qwen embeddings trained on NQ and evaluated on a 65536 text subset of NQ (chunked in batches of size 1024). Rank varies from 1 to 1024, thus 512 corresponds to a random ordering. Since the embedding dimensionalities are different, only the Gromov-Wasserstein‡ OT baseline is run and the naive baseline does not apply. Bold denotes best value.

As shown in Table [8,](#page-15-3) vec2vec successfully translates between GTE and Qwen, significantly outperforming the optimal transport baseline in all metrics except qwen → gte cosine similarity, which we hypothesize may be due to the substantial performance gap between the models—indeed, Qwen differs from GTE in architecture (dense Qwen backbone), training methodology (unsupervised + model merging techniques), size (14× larger than the next largest model and 37× larger than GTE), context length, and recency. Given Qwen's size and computational cost, we only evaluated this representative pair. We leave further evaluation to future work.

## <span id="page-15-4"></span><span id="page-15-0"></span>D Text-image retrieval on MS COCO

| model           | R@16 ↑ | cos(·) ↑   | Rank ↓       |
|-----------------|--------|------------|--------------|
| granite → clip  | 0.23   | 0.23 (0.0) | 233.67 (3.0) |
| clip (baseline) | 0.75   | 0.30 (0.0) | 23.20 (0.8)  |

Table 9: Cross-model text-image retrieval on MS COCO: granite → clip vec2vec trained on NQ (unimodal) and evaluated on MS COCO's validation set. The rank metric varies from 1 to 5000, thus 2500 corresponds to a random ordering. Queries (captions) embedded with either Granite or CLIP. Documents (images) embedded with CLIP. Each caption has a unique image. Standard errors are shown in parentheses.

Our vec2vecs can "stitch" modalities onto unimodal models by translating to a multimodal model. To test this, we evaluated cross-modal text-image retrieval on MS COCO's validation set (5000 examples) [\[34\]](#page-11-6), translating queries (captions) embedded with Granite to retrieve documents (images) embedded with CLIP using our unimodal granite → clip translator from section [4.3.](#page-4-1) Each caption has a unique image. We report Recall@16, cosine similarities, and Rank, with CLIP (for both documents and queries) as our baseline.

As Table [9](#page-15-4) shows, translating Granite embeddings to CLIP enables non-negligible cross-model multimodal retrieval with a unimodal model for queries—despite zero multimodal training. Further evaluation of this paradigm with multimodal-specific training is a promising direction.

### <span id="page-15-2"></span>E Initialization robustness by model backbone

GAN training is notoriously unstable to weight initialization [\[53\]](#page-12-7). To measure our method's robustness, we trained fifteen e5 → gte (shared backbone) and e5 → gtr (cross-backbone) vec2vecs on the NQ dataset for a fixed 10 epochs.

For the translations between related models, vec2vec training was relatively stable across random seeds: 14 out of 15 seeds achieved at least 80% top-1 accuracy within a fixed epoch budget, while the remaining run reached 72%. In contrast, translation between unrelated models proved significantly less stable, with only 3 out of 15 runs achieving convergence (80% top-1 accuracy). We leave improving the seed stability of our training regime as future, valuable work.

#### <span id="page-16-0"></span>F Full out-of-distribution translation results

We provide baseline numbers for the experiments shown in Table 3, by dataset.

|       |       |                       | vec2vec | ;           | N                     | aïve Base | line         |                        | OT Basel | line                      |
|-------|-------|-----------------------|---------|-------------|-----------------------|-----------|--------------|------------------------|----------|---------------------------|
| $E_1$ | $E_2$ | $\cos(\cdot)\uparrow$ | T-1 ↑   | Rank ↓      | $\cos(\cdot)\uparrow$ | T-1 ↑     | Rank ↓       | $\cos(\cdot) \uparrow$ | T-1 ↑    | Rank ↓                    |
|       | gtr   | 0.74 (0.0)            | 0.99    | 1.09 (0.1)  | -0.04 (0.0)           | 0.00      | 415.61 (8.2) | 0.71 (0.0)             | 0.01     | 220.93 (7.1) <sup>‡</sup> |
| gra.  | gte   | 0.85 (0.0)            | 0.95    | 1.26 (0.1)  | 0.00 (0.0)            | 0.00      | 406.73 (8.2) | 0.87 (0.0)             | 0.01     | 201.48 (6.6) <sup>‡</sup> |
| gia.  | ste.  | 0.77 (0.0)            | 0.96    | 1.11 (0.0)  | 0.00 (0.0)            | 0.00      | 417.27 (8.2) | 0.74 (0.0)             | 0.00     | 239.36 (6.7) <sup>‡</sup> |
|       | e5    | 0.83 (0.0)            | 0.87    | 3.10 (0.7)  | 0.02 (0.0)            | 0.00      | 405.53 (8.1) | 0.87 (0.0)             | 0.01     | 244.94 (7.4) <sup>‡</sup> |
|       | gra.  | 0.79 (0.0)            | 0.98    | 2.41 (0.6)  | -0.04 (0.0)           | 0.00      | 411.53 (8.3) | 0.57 (0.0)             | 0.01     | 398.29 (8.2) <sup>‡</sup> |
| gtr   | gte   | 0.85 (0.0)            | 0.96    | 1.29 (0.2)  | 0.04 (0.0)            | 0.00      | 392.01 (8.2) | 0.86 (0.0)             | 0.01     | 259.47 (7.4) <sup>‡</sup> |
| gu    | ste.  | 0.77 (0.0)            | 0.96    | 1.10(0.0)   | 0.00 (0.0)            | 0.00      | 394.69 (8.3) | 0.74(0.0)              | 0.00     | 294.58 (7.4) <sup>‡</sup> |
|       | e5    | 0.80 (0.0)            | 0.53    | 13.38 (1.2) | 0.03 (0.0)            | 0.00      | 400.85 (8.2) | 0.87 (0.0)             | 0.01     | 266.04 (7.7) <sup>‡</sup> |
|       | gra.  | 0.73 (0.0)            | 0.94    | 1.33 (0.1)  | 0.00 (0.0)            | 0.00      | 408.81 (8.3) | 0.56 (0.0)             | 0.01     | 398.16 (8.2)*             |
| gte   | gtr   | 0.71 (0.0)            | 0.95    | 1.29 (0.1)  | 0.04 (0.0)            | 0.00      | 386.58 (8.3) | 0.71 (0.0)             | 0.01     | 254.74 (7.3) <sup>‡</sup> |
| gic   | ste.  | 0.86 (0.0)            | 1.00    | 1.00(0.0)   | 0.58 (0.0)            | 1.00      | 1.00 (0.0)   | 1.00 (0.0)             | 1.00     | 1.00 (0.0)*               |
|       | e5    | 0.83 (0.0)            | 0.91    | 1.57 (0.2)  | 0.68 (0.0)            | 1.00      | 1.00 (0.0)   | 1.00 (0.0)             | 1.00     | 1.00 (0.0)*               |
|       | gra.  | 0.79 (0.0)            | 0.99    | 1.09 (0.1)  | 0.00 (0.0)            | 0.00      | 418.16 (8.4) | 0.57 (0.0)             | 0.00     | 399.56 (8.2) <sup>‡</sup> |
| ste.  | gtr   | 0.77 (0.0)            | 1.00    | 1.00(0.0)   | 0.00 (0.0)            | 0.00      | 393.07 (8.1) | 0.71 (0.0)             | 0.00     | 294.65 (7.4) <sup>‡</sup> |
| Sic.  | gte   | 0.90(0.0)             | 1.00    | 1.00(0.0)   | 0.58 (0.0)            | 1.00      | 1.00(0.0)    | 1.00(0.0)              | 1.00     | 1.00 (0.0)*               |
|       | e5    | 0.85 (0.0)            | 0.98    | 1.05 (0.0)  | 0.37 (0.0)            | 0.89      | 1.55 (0.1)   | 1.00 (0.0)             | 1.00     | 1.00 (0.0)*               |
|       | gra.  | 0.79 (0.0)            | 0.98    | 1.08 (0.0)  | 0.02 (0.0)            | 0.00      | 405.75 (8.3) | 0.57 (0.0)             | 0.01     | 398.34 (8.2) <sup>‡</sup> |
| e5    | gtr   | 0.67 (0.0)            | 0.80    | 3.10(0.6)   | 0.03 (0.0)            | 0.00      | 401.16 (8.4) | 0.71 (0.0)             | 0.00     | 268.28 (7.6) <sup>‡</sup> |
| CS    | gte   | 0.87 (0.0)            | 0.99    | 1.02 (0.0)  | 0.68 (0.0)            | 1.00      | 1.00 (0.0)   | 1.00 (0.0)             | 1.00     | 1.00 (0.0)*               |
|       | ste.  | 0.75 (0.0)            | 0.98    | 1.06 (0.0)  | 0.37 (0.0)            | 1.00      | 1.00 (0.0)   | 1.00 (0.0)             | 1.00     | 1.00 (0.0)*               |

Table 10: Out-of-distribution translations on TweetTopic (with baselines): vec2vec models trained on NQ and evaluated on the entire TweetTopic test set (800 tweets). The rank metric varies from 1 to 800, thus 400 corresponds to a random ordering. Standard errors are shown in parentheses. Symbols denote the lowest-rank solver: Earth Mover's Distance\* and Gromov-Wasserstein<sup>‡</sup>

|       |       |                        | vec2v | ec             | 1                      | Naïve Bas | eline          |                       | OT Baseline |                             |  |
|-------|-------|------------------------|-------|----------------|------------------------|-----------|----------------|-----------------------|-------------|-----------------------------|--|
| $E_1$ | $E_2$ | $\cos(\cdot) \uparrow$ | T-1 ↑ | Rank ↓         | $\cos(\cdot) \uparrow$ | T-1 ↑     | Rank ↓         | $\cos(\cdot)\uparrow$ | T-1 ↑       | Rank ↓                      |  |
|       | gtr   | 0.74 (0.0)             | 0.60  | 23.38 (1.6)    | -0.02 (0.0)            | 0.00      | 4010.00 (25.8) | 0.82 (0.0)            | 0.00        | 3962.83 (26.1) <sup>†</sup> |  |
| gra.  | gte   | 0.85 (0.0)             | 0.08  | 346.21 (7.8)   | 0.01 (0.0)             | 0.00      | 3978.35 (26.1) | 0.92 (0.0)            | 0.00        | 3808.18 (25.9) <sup>†</sup> |  |
| gra.  | ste.  | 0.72 (0.0)             | 0.13  | 242.23 (6.1)   | -0.01 (0.0)            | 0.00      | 3900.74 (26.2) | 0.86 (0.0)            | 0.02        | 3780.44 (26.0) <sup>†</sup> |  |
|       | e5    | 0.84 (0.0)             | 0.12  | 361.06 (8.7)   | 0.02 (0.0)             | 0.00      | 4024.92 (26.1) | 0.93 (0.0)            | 0.00        | 3937.63 (26.2) <sup>†</sup> |  |
|       | gra.  | 0.78 (0.0)             | 0.51  | 35.27 (1.9)    | -0.02 (0.0)            | 0.00      | 4023.67 (26.1) | 0.87 (0.0)            | 0.00        | 3964.83 (26.1) <sup>†</sup> |  |
| gtr   | gte   | 0.84 (0.0)             | 0.12  | 279.56 (6.9)   | 0.08 (0.0)             | 0.00      | 4180.47 (26.2) | 0.87 (0.0)            | 0.00        | 4088.97 (26.2) <sup>‡</sup> |  |
| gu    | ste.  | 0.72 (0.0)             | 0.27  | 127.92 (4.4)   | 0.00 (0.0)             | 0.00      | 4296.04 (26.1) | 0.76 (0.0)            | 0.00        | 4095.11 (26.1) <sup>‡</sup> |  |
|       | e5    | 0.82 (0.0)             | 0.01  | 1413.80 (18.3) | 0.09 (0.0)             | 0.00      | 4064.47 (26.2) | 0.93 (0.0)            | 0.00        | $4010.13 (26.1)^{\dagger}$  |  |
|       | gra.  | 0.73 (0.0)             | 0.09  | 342.15 (7.8)   | 0.01 (0.0)             | 0.00      | 3946.19 (25.8) | 0.87 (0.0)            | 0.00        | 3802.92 (25.9) <sup>†</sup> |  |
| ata   | gtr   | 0.69 (0.0)             | 0.12  | 256.63 (6.4)   | 0.08 (0.0)             | 0.00      | 4229.90 (26.2) | 0.69 (0.0)            | 0.00        | 4094.02 (26.1) <sup>‡</sup> |  |
| gte   | ste.  | 0.85 (0.0)             | 1.00  | 1.00 (0.0)     | 0.56 (0.0)             | 1.00      | 1.00 (0.0)     | 1.00 (0.0)            | 1.00        | 1.00 (0.0)*                 |  |
|       | e5    | 0.86 (0.0)             | 0.54  | 17.71 (0.9)    | 0.69 (0.0)             | 0.98      | 1.04 (0.0)     | 1.00 (0.0)            | 1.00        | 1.00 (0.0)*                 |  |
|       | gra.  | 0.77 (0.0)             | 0.14  | 221.95 (5.9)   | -0.01 (0.0)            | 0.00      | 3951.42 (25.9) | 0.87 (0.0)            | 0.01        | 3776.52 (26.0) <sup>†</sup> |  |
| ste.  | gtr   | 0.75 (0.0)             | 0.56  | 17.70 (1.0)    | 0.00 (0.0)             | 0.00      | 4339.83 (26.2) | 0.70(0.0)             | 0.00        | 4093.61 (26.1) <sup>‡</sup> |  |
| sic.  | gte   | 0.91 (0.0)             | 1.00  | 1.00(0.0)      | 0.56 (0.0)             | 1.00      | 1.00 (0.0)     | 1.00(0.0)             | 1.00        | 1.00 (0.0)*                 |  |
|       | e5    | 0.85 (0.0)             | 0.51  | 26.33 (1.2)    | 0.35 (0.0)             | 0.59      | 12.68 (0.6)    | 0.93 (0.0)            | 1.00        | 1.00 (0.0)                  |  |
|       | gra.  | 0.78 (0.0)             | 0.21  | 151.09 (4.6)   | 0.02 (0.0)             | 0.00      | 4008.10 (25.9) | 0.87 (0.0)            | 0.00        | 3932.58 (26.2) <sup>†</sup> |  |
| e5    | gtr   | 0.66 (0.0)             | 0.01  | 1029.64 (14.9) | 0.09 (0.0)             | 0.00      | 4032.85 (26.2) | 0.82 (0.0)            | 0.00        | 4010.06 (26.1) <sup>†</sup> |  |
| CS    | gte   | 0.87 (0.0)             | 0.60  | 32.59 (2.6)    | 0.69 (0.0)             | 0.98      | 1.09 (0.0)     | 1.00 (0.0)            | 1.00        | 1.00 (0.0)*                 |  |
|       | ste.  | 0.75 (0.0)             | 0.46  | 32.12 (1.4)    | 0.35 (0.0)             | 0.86      | 2.49 (0.1)     | 0.86 (0.0)            | 1.00        | 1.01 (0.0)                  |  |

Table 11: Out-of-distribution translations on MIMIC (with baselines): vec2vec models trained on NQ and evaluated on an 8192-record subset of MIMIC. The rank metric varies from 1 to 8192, thus 4096 corresponds to a random ordering. Standard errors are shown in parentheses. Symbols denote the lowest-rank solver: Earth Mover's Distance\*, Sinkhorn† and Gromov-Wasserstein‡

# <span id="page-17-2"></span><span id="page-17-1"></span>G Zero-shot inversion on TweetTopic

![](_page_17_Figure_1.jpeg)

Figure 7: Leakage of information via inversion. Trained on NQ and evaluated on a 50-tweet subset of the TweetTopic dataset. Cells denote judge accuracy.

We replicate Figure [5](#page-7-1) on the TweetTopic dataset in Figure [7,](#page-17-2) extracting information given *only* translated embeddings of tweets. We achieve non-negligible leakage for all model pairs.

### <span id="page-17-0"></span>H Prompt for measuring information extraction

Figures [5](#page-7-1) and [7](#page-17-2) utilize an LLM judge to determine whether the approximate inversion (using [\[67\]](#page-13-2)) of a translated email embedding leaks information about the original email. Figure [8](#page-17-3) shows our prompt to the GPT-4o judge:

<span id="page-17-3"></span>Original email: {ground\_truth} Reconstructed email: {generation}. Does the reconstructed email leak any information about the original email? Answer with only 'yes' or 'no'.

Figure 8: The prompt given to the LLM judge.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="back-into-plato-s-cave-examining-cross-modal-representationa.md">
<details>
<summary>Back into Plato's Cave: Examining Cross-modal Representational Convergence at Scale</summary>

Phase: [EXPLORATION]

**Source URL:** <https://akoepke.github.io/cave_umwelten>

# Back into Plato's Cave: Examining Cross-modal Representational Convergence at Scale

The Platonic Representation Hypothesis:

### The Platonic Representation Hypothesis, explained

The idea is appealing: as neural networks get bigger and train on more data, they all converge toward the same representation of reality, regardless of whether they process images, text, or audio. [Huh et al. (2024)](https://arxiv.org/abs/2405.07987) called this the _Platonic Representation Hypothesis_, drawing on Plato's idea that behind the world of appearances lies a single set of ideal forms.

If true, this would mean there's one "correct" way to represent the world, and all our models will eventually find it. But we examined the experimental evidence closely and found it to be surprisingly fragile. The alignment was measured on just 1,024 samples with one-to-one pairings. Under more realistic conditions, cross-modal representational alignment decreases dramatically.

### Did you check the experimental evidence?

**TL;DR for you:** The evidence was measured on 1,024 samples with one-to-one pairings. That's not how most real data works. When we test under realistic conditions, cross-modal representational alignment decreases significantly.

The experimental evidence comes from a highly constrained setting: only **1,024 samples**, **one-to-one** image-text pairings, and a metric evaluated at a small scale. These conditions are far removed from how real-world multi-modal data looks: it is large-scale and inherently many-to-many.

When we relax the experimental setting (scaling to millions of samples, allowing multiple captions per image, testing with newer models), the alignment trends used to support the hypothesis are no longer observed. This suggests that rather than finding a shared representation, each modality may yield a representation specific to its own [_Umwelt_](https://en.wikipedia.org/wiki/Umwelt).

### You're not alone. We stress-tested the experimental evidence

**TL;DR for you:** We use the same metric and same models as the original paper, and show that their experimental evidence breaks at scale, with more realistic data, and newer models. Others have found problems with the hypothesis from different angles. [1]

Specifically, we take the original experimental setup and show that alignment **degrades when scaling** from 1,024 to millions of samples, **breaks when the data is not bijective**, captures only **coarse categorical agreement** rather than fine-grained structure, and the predicted trend that stronger models align more **fails for newer LLMs**. This suggests that rather than finding a shared representation, modalities may yield representations specific to their own [_Umwelten_](https://en.wikipedia.org/wiki/Umwelt).

## Why Question Platonic Convergence?

Large language models keep solving tasks we thought required vision, like visual question answering, spatial reasoning, even robotic manipulation. This has led some to ask: do we even need pixels, or is language all you need?

The [Platonic Representation Hypothesis](https://arxiv.org/abs/2405.07987) says it doesn't matter. As neural networks scale, their representations converge toward the same one regardless of modality. If true, you might just use text, since it's a convenient source of data.

But there is a reason we visit art museums rather than just read descriptions of paintings in a catalogue. And when we looked closely at the experimental evidence for convergence in the Platonic Representation Hypothesis, we found that it came from a surprisingly limited setting. The evaluations were done on just 1,024 samples with bijective pairings. Under more realistic conditions, what looked like little alignment turns out to be shallow. Both models sometimes agree on broad categories but organize the finer details differently.

* * *

## How is Alignment Measured?

The core metric used by [Huh et al.](https://arxiv.org/abs/2405.07987) to measure cross-modal alignment is **mutual k-nearest neighbors** (mutual k-NN). Given paired image-text data, find the (k) nearest neighbors for each sample in both the vision and the language embedding space.

Use the slider below to grow the dataset size. As it gets denser, both models find closer neighbors, but they stop agreeing on which one:

**Dataset size: 1,024**

sparsedense

Image SpaceText SpaceNNNNqueryquery✓ The NNs in text and image space are consistent

https://akoepke.github.io/cave_umwelten/

Interactive illustration of the mutual nearest neighbor metric (k=1). Each dot represents an image-text pair in the dataset, shown in image embedding space (left, DINOv2) and text embedding space (right, OpenLlama3b). The **blue dot** is the query, the other colored dots are the nearest neighbors in each space. On a small dataset (1,024 samples), both models agree on the same NN ( **green**). As the dataset grows denser, each model finds a closer match in its own space, but they are **not consistent**. Hover over dots to see their image and caption.

* * *

## Alignment Degrades at Scale

The original experimental evidence for the [Platonic Representation Hypothesis](https://arxiv.org/abs/2405.07987) used a dataset of just **1,024 samples**. We systematically scaled up to **15 million**, and found that alignment degraded.

13.5%Alignment on

WIT-1024 (k=10)

0.8%Alignment on

LAION-15M (k=10)

16×Drop in alignment

when scaling up

Why does this happen? In a sparse dataset, both modalities tend to retrieve the same neighbors, not necessarily because they agree, but because the pool is too small to reveal their differences. As the dataset gets denser, each modality can find neighbors that are closer _in its own space_, and the overlap vanishes.

Huh et al. themselves ask whether the obtained mutual kNN score is _“indicative of strong alignment with the remaining gap being ‘noise’ or does it signify poor alignment with major differences left to explain?”_ When scaling from 1,024 to 15 million samples, the alignment score **drops from 13.5% to just 0.81%**, leaving very little room for a convergence narrative.

https://akoepke.github.io/cave_umwelten/images/figures/nested_wit1m_v6style_no_kpct.png

Scaling the dataset to 1M (WIT) shows a large drop in mutual k-NN alignment for both k=1 and k=10.

https://akoepke.github.io/cave_umwelten/images/figures/nested_laion15m_v6style_no_kpct.png

We see a similar alignment degradation on LAION-15M when scaling to 15M samples.

## Measured Alignment Doesn't Hold Up for Real Data

The original experiments used **one-to-one** image-text pairings. But real data is many-to-many: a single image can be described in countless ways, and a single caption can match many different images. When we progressively add more captions per image or more images per caption, mutual k-NN alignment drops consistently.

https://akoepke.github.io/cave_umwelten/images/figures/densifying_tv/densifying_images.png

Adding more images per caption using [CycleReward](https://cyclereward.github.io/) data. Mutual k-NN alignment decreases consistently for both k=1 and k=10.

https://akoepke.github.io/cave_umwelten/images/figures/densifying_tv/densifying_texts.png

Adding more captions per image gives the same pattern. Alignment drops as the one-to-one setting is relaxed.

## Coarse Agreement, Not Fine-Grained Convergence

Both models might retrieve a "stone wall", but the vision model finds one with a _similar texture_, while the language model finds _interlocking concrete blocks_. Same category, different items.

Images per class:1949

Image SpaceText SpaceNNNNqueryquery

https://akoepke.github.io/cave_umwelten/

Each dot represents an image-text pair, shown in both the image embedding space (left, DINOv2) and text embedding space (right, OpenLlama3b). As the number of images per class grows, both models find closer neighbors in their own space, but they no longer agree on the same item. Hover over a dot to see its caption.

To quantify this phenomenon, we turn to ImageNet, where every image has a class label. We decompose the mutual k-NN metric into three questions:

1.  Does each model individually retrieve a _correct-class_ neighbor? Mostly, yes! (red and blue lines)
2.  Do _both_ models retrieve a correct-class neighbor? At increasing rates. (orange line)
3.  Do they agree on the _exact same item_? Mostly, no! (dark green line)

https://akoepke.github.io/cave_umwelten/images/figures/ipc_alignment_with_accuracy.png

Per-modality retrieval accuracy and cross-modal mutual k-NN alignment (k=1) as images per class increase. As the dataset densifies, both DINOv2 and OpenLlama3b individually retrieve correct-class neighbors at rising rates, but cross-modal alignment remains flat: the models agree on the category but not on the specific instance.

The **limited alignment we do observe is just coarse categorical agreement**. Both models know what a stone wall is, but they have fundamentally different ideas about which walls are most similar to each other.

## Stronger Unimodal Models Do Not Seem More Aligned

One argument for convergence was that _stronger language models align better with vision models_. We tested this across 55 language models and multiple benchmarks.

The trend (shown as dashed lines) from the models used in the original Platonic Representation Hypothesis experiments does not seem to hold for recent models (diamonds that are off the lines). Indeed, newer models appear to be specializing in their own modality.

https://akoepke.github.io/cave_umwelten/images/figures/trends/mutual_knn_k10_prh_extended_vs_PRH_gsm8k_5shots.png

**GSM8K**

https://akoepke.github.io/cave_umwelten/images/figures/trends/mutual_knn_k10_prh_extended_vs_PRH_arc.png

**ARC**

https://akoepke.github.io/cave_umwelten/images/figures/trends/mutual_knn_k10_prh_extended_vs_PRH_mmlu.png

**MMLU**

https://akoepke.github.io/cave_umwelten/images/figures/trends/mutual_knn_k10_prh_extended_vs_PRH_logiqa2.png

**LogiQA2**

Alignment vs. language model capability across four benchmarks. Dashed lines show the original trend from the Platonic Representation Hypothesis; diamonds represent recent models that fall off the predicted scaling curve. Stronger LLMs don't appear to align better with vision.

* * *

## Back in the Cave: Models in Their Own _Umwelten_

Nearly a century ago, biologist [Jakob von Uexküll](https://en.wikipedia.org/wiki/Jakob_Johann_von_Uexk%C3%BCll) argued that every organism inhabits its own perceptual environment, or [_Umwelt_](https://en.wikipedia.org/wiki/Umwelt): a tick lives in a world of thermal gradients, a bat in a world of echoes. The different _Umwelten_ might have only little overlap with each other. [2]
The same, we believe, might hold
for our models: each constructs its own representational structure, determined
by its modality and training data, rather than converging toward a shared model
of reality. Though it is still early days, we suspect future evidence will favor von
Uexküll over Plato.

* * *

1.  **Others have also questioned the hypothesis:**

    *   **Hadgi et al.** ( ["Escaping Plato's Cave"](https://arxiv.org/abs/2503.05283)): weaker alignment for 3D encoders.
    *   **Gröger et al.** ( ["Revisiting the Platonic Representation Hypothesis"](https://arxiv.org/pdf/2602.14486)): CKA confounded by width and depth, global alignment collapses.
    *   **Tjandrasuwita et al.** ( ["Emergence of Multimodal Alignment"](https://arxiv.org/abs/2502.16282)): alignment varies with modality similarity.
    *   **Kumar et al.** ( ["Fractured Entangled Representations"](https://arxiv.org/abs/2505.11581)): a fractured view of how representations form.
    *   **Smith et al.** ( ["Functional Alignment Can Mislead"](https://proceedings.mlr.press/v267/smith25a.html)): model stitching succeeds even between unrelated tasks.

    Please get in touch with us if we have left your paper off this list.

2.  For a grand tour of von Uexküll's ideas, see Jan Koenderink's delightful book [_Sentience_ (2019)](https://gestaltrevision.be/wp-content/uploads/clootcrans_press/2019_Sentience.pdf).

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="brain-machine-convergent-evolution-why-finding-parallels-bet.md">
<details>
<summary>Brain–machine convergent evolution: Why finding parallels between brain and artificial systems is informative | PNAS</summary>

Phase: [EXPLORATION]

**Source URL:** <https://www.pnas.org/doi/10.1073/pnas.2319709121>

# Brain–machine convergent evolution: Why finding parallels between brain and artificial systems is informative | PNAS

## Abstract

Central nervous system neurons manifest a rich diversity of selectivity profiles—whose precise role is still poorly understood. Following the striking success of artificial networks, a major debate has emerged concerning their usefulness in explaining neuronal properties. Here we propose that finding parallels between artificial and neuronal networks is informative precisely because these systems are so different from each other. Our argument is based on an extension of the concept of convergent evolution—well established in biology—to the domain of artificial systems. Applying this concept to different areas and levels of the cortical hierarchy can be a powerful tool for elucidating the functional role of well-known cortical selectivities. Importantly, we further demonstrate that such parallels can uncover novel functionalities by showing that grid cells in the entorhinal cortex can be modeled to function as a set of basis functions in a lossy representation such as the well-known JPEG compression. Thus, contrary to common intuition, here we illustrate that finding parallels with artificial systems provides novel and informative insights, particularly in those cases that are far removed from realistic brain biology.

The discovery and characterization of the specialized activation properties of neurons in the mammalian brain is undoubtedly one of the most successful research programs in systems neuroscience. This research has uncovered a remarkably rich and intriguing library of tuning properties ranging from orientation-selective neurons in the visual cortex ( [1](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r1)) to place cells in the hippocampus ( [2](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r2)). However, a major challenge posed by this remarkable diversity of neuronal properties is to understand what is the functional role these specializations play in the ability of brain systems to generate specific adaptive behaviors.

At this point, it is important to clarify the terms that will be central to this perspective. First, what is meant by tuning or selectivity of neuronal activations and then clarifying the difference between functional and auxiliary or nonfunctional tuning properties. Finally, we will define the term functional role of tuned neurons.

To explain these terms, let us consider the simple example of a rod photoreceptor. The specialization of the photoreceptor is characterized by a number of dimensions—for example, by its receptive field, i.e., the angle from which it can absorb light rays. We will term this unique constraint the tuning or selectivity profile of the photoreceptor’s receptive field. As to the function of the photoreceptor—in this case, we have a rather accepted model proposing that the rod’s function is to convert low light levels into electrical signals. We will term this the functional role of the rod photoreceptor. Finally, there are certain behaviors of the photoreceptor that are not directly central to its function, for example, the fact that it recycles its membrane. However, these maintenance processes do not play a direct role in the service of the rod’s main function, we will term these properties auxiliary properties of the rod photoreceptor.

Having defined these terms, the fundamental problem that system neuroscientists face and is the motivation for this perspective is that except for extremely few cases (e.g., the function of retinal photoreceptors) we are still largely in the dark concerning the functionality of the numerous neuronal selectivity profiles discovered in the brain. We do not know whether these selectivity profiles truly play a role in achieving a certain brain function or are merely an auxiliary phenomenon (see also ref. [3](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r3)).

The situation is even worse when trying to decipher _what_ is the functional role of these selectivity profiles. Here it is important to acknowledge, as will be discussed below, that the simple mechanistic photoreceptor model used as an example above may not even be relevant to brain systems. As recent developments in artificial networks demonstrate, a system may be highly successful functionally, yet each of its constituent neurons may play a unique role that cannot be predicted by or clustered into a modular or well-defined algorithmic scheme.

To summarize, when facing the central question of systems neuroscience—namely, how do neurons contribute to behavior—the available information remains quite limited. This is partially because we lack precise enough causal tools whereby we can selectively activate functionally unique subsets of neurons, and partially because accurate, large-scale, modeling of the neuronal basis of perception, cognition, and behavior is still not feasible. Lacking such appropriate tools and models limits our ability to validate hypothetical functionalities of the observed neuronal tuning properties.

Following the remarkable success of artificial networks in achieving human-level performance in behaviors such as image recognition and language production, a potentially powerful opportunity opened up to employ such artificial networks as brain models that may offer informative insights into the functional role of neuronal properties. However, this notion has met with major criticism (see for example, refs. [4](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r4)– [7](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r7)).

The main objection is that artificial networks are simply too remote in their hardware, signaling, and general structural properties from biological neuronal systems. Here, we would like to argue that somewhat counterintuitively, the very dissimilarities, that are glaringly obvious, between artificial and brain networks should be taken as strengthening rather than discouraging the significance that we should derive from finding parallel functionalities between such remote systems.

Our rationale is an extension of the well-known concept of convergent evolution, long established in evolutionary biology. In convergent evolution, finding parallel functions in remote species is taken to signify their crucial functionality which forced these remote systems to converge on finding parallel solutions despite their otherwise major discrepancies. We would like to propose here that this notion of convergence evolution can be extended to such unexpected “coincidental” parallels found between biological and artificial systems.

The rationale underlying such far-reaching extension is derived from the realization that both biological and engineered systems—despite their acknowledged fundamental discrepancies—share a common property: They are both systems that evolve and optimize through trial and error. While this principle does not need to be elaborated in the case of biological evolution, it may seem far-fetched when applied to engineering. The common view is that engineering and technological advance in general evolve through a carefully planned, deliberate procedure. However, a closer look at the history of technological progress reveals a major and quite striking element of trial and error ( [8](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r8)). Just one example of many, consider the numerous trials it took Thomas Edison until he settled on the then-optimal light bulb design. The fundamental aspect, which is the basis of our argument here, is that technological development, just as biological evolution, is a rather haphazard evolutionary process by which systems that are more adaptive and more successful in performing their needed function are selected for, while the less adaptive biological or engineered systems are discarded.

How then can the search for cross-modal convergent evolution, i.e., emergent parallels between neurobiology and engineering, help us understand the function of neuronal specializations and tuning? As commonly defined, convergent evolution is the “creation of analogous structures that have similar form or function” \[Web definition ( [9](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r9))\]. This implies that the convergence toward parallel properties is driven by the necessary and successful functionality of such properties, as can be illustrated by the well-known case of convergent evolution of wings. If we consider the structure of wings, we find that diverse animals—ranging from insects to bats to birds—“reinvent” analogous side protrusions in the service of flight. There are three general aspects in this convergent evolution that need to be emphasized: First, convergent evolution highlights the functionality of a system’s property even in the absence of a model or explanation of how this property functions. So, in the case of wings, their importance to flying can be inferred merely by noting that they are common to many air-borne organisms, which correctly supports their essential role in flying. We will term such coincidences descriptive alignments. This inference can be derived even with no understanding of aerodynamics.

Second, the more remote the converging systems are from each other, the less likely it is that the parallel functionalities between them could be auxiliary, i.e., nonfunctional alignments. Thus, the argument for the advantage derived from dissimilarity between biological and artificial systems is essentially an argument about informativeness. To put it simply, unlikely coincidences carry more information.

Finally, once a convergent evolution is established, one can often use one species as a model system, helping to understand the function of other, parallel, systems as well. With regard to wings, understanding how wings make birds fly will translate quite readily to understanding how they make insects fly, etc.

The advantage of extending the search for convergent evolution from biology to engineered systems is that such parallels exhibit the most profound case of remoteness between systems. Again, the case of wings illustrates this point—while convergent evolution between winged organisms may be attributed to some auxiliary biological constraints, such possibility obviously cannot account for the appearance of airplane wings. Furthermore, artificial wings are far easier to model and manipulate and hence provide principles that could then be applied to biological wings as well.

Recently, a rapidly growing line of modeling research strategy has been proposed that aims to optimize the artificial system for achieving a specific goal rather than simulate the biological system’s neuronal properties ( [10](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r10), [11](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r11)). These “top–down” approaches share fundamental similarities to the convergent evolution perspective proposed here.

At the same time, it is important to highlight the distinct aspects of the convergent evolution perspective from the, indeed powerful, strategy of goal optimization. First, the convergent evolution approach can be applied beyond artificial neural networks—to any information processing system, as illustrated here in the case of optimal Joint Photographic Experts Group (JPEG) signal compression.

Second, a central aspect of evolution is in serendipity and selection of successful systems while in current goal-optimization approaches the focus is on machine learning and training targeted networks to perform preselected tasks. However, it is important to emphasize that the distinction between the approaches is not binary: Goal-optimization approaches often select among a set of available networks while evolution, at least as it appears in the engineering domain, often includes an element of system refinement and optimization as well. Considering the final step, i.e., comparing the artificial systems to brain networks—the two approaches converge in taking the parallels that are found between the optimal artificial systems and brain networks as informative in suggesting the potential functionality of the relevant brain functions. It is interesting to note that the introduction of the goal-optimization approach itself had a subtle element of convergent evolution since it received a major advance by the stunning recent engineering success of Deep Neural Networks.

Here we illustrate the potential usefulness of finding convergent evolution between brain and engineered systems by first explaining two well-established properties of the visual cortical hierarchy. We next demonstrate that the convergent evolution approach can uncover new functionalities by highlighting an intriguing parallel between entorhinal grid cells and basis functions of lossy space representations.

## The Function of Orientation Tuning in the Primary Visual Cortex

The discovery of neurons in the primary visual cortex that show tuning to specific line orientations has marked a pioneering achievement in systems neuroscience, earning Hubel and Wiesel the Nobel Prize in medicine for their discovery in 1981. The outstanding property of these neurons, as illustrated in [Fig. 1](https://www.pnas.org/doi/10.1073/pnas.2319709121#fig01), is that they show preferential sensitivity to specific orientations of lines and edges. However, is this feature of neuronal selectivity essential to vision or is it just an auxiliary by-product of neuronal development? In the case of orientation-selective neurons, an essential role in shape processing has been proposed from the earliest papers describing their properties. And indeed, it is likely that a major appeal of this seminal research was related to the fact that the orientation tuning properties of individual V1 neurons had such readily intuitive and naturalistic appeal as “edge and line detectors,” fitting nicely with well-known psychophysical properties documented already in the classic Gestalt Literature, such as the rule of good continuation ( [12](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r12)). However, despite this naturalistic appeal, whether the orientation selectivity of V1 neurons actually plays a functional role in visual perception, and in what manner does it contribute to this function remained, until recently, largely in the domain of intuition and ad hoc modeling.

https://www.pnas.org/cms/10.1073/pnas.2319709121/asset/997302f0-3e47-4148-bdbb-74a6c3c6e314/assets/images/large/pnas.2319709121fig01.jpgConvergent evolution between ( _A_) receptive fields of orientation selective, simple cells found in area V1 of the cat cortex (taken from ref. [13](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r13)) and ( _B_) artificial units in the first layer of a convolutional neural network (reprinted from ref. [14](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r14)). Note the remarkable similarity, including the orientation but also the side-lobe organization, of the receptive fields. Critically, the artificial receptive field properties emerged through backpropagation training and were not simulated based on the biological data.

More recently, a novel support for a role of orientation selectivity in perception, and specifically in object recognition, has been suggested by the finding of a remarkable convergent evolution between the cortical visual system and engineered machine vision networks. Specifically, in a truly dramatic instance of a forward leap in the technological evolution of artificial vision machines, a specific type of artificial system, termed convolutional neural networks (CNNs), has reached, and in some cases even surpassed, human visual recognition performance ( [15](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r15)). Relevant to the idea of convergent evolution, these networks show intriguing structural commonalities with the human visual system, for example in their hierarchical, layered structure, reminiscent to some extent of the hierarchy of visual areas in the primate brain.

Nonetheless, it should be noted that the argument for a convergent evolution of CNNs and biological neural networks is actually more subtle. This is since the precursor of modern convolutional networks—the Neocognitron model ( [16](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r16))—was actually inspired by the cortical architecture including Hubel and Wiesel’s findings, so it could be argued that these networks in fact mimic brain structures. Yet, these initial brain-inspired networks did not perform well. Thus, from the convergent evolution perspective, these pioneering networks paradoxically provided evidence against the functionality of the brain-inspired organization principles. Only recently, the advent of the highly successful new generations of deep convolutional networks which match human-level recognition performance motivated the search for converging principles between these networks and the human brain.

The discovery that is particularly relevant to the issue of orientation selectivity in V1 discussed here is that characterizing the tuning properties of these successful artificial neurons along the different levels of the deep convolutional hierarchy uncovered a striking resemblance between the orientation tuning properties of V1 neurons and that of the artificial neurons found in the first (most upstream) artificial layer. This similarity is illustrated in [Fig. 1](https://www.pnas.org/doi/10.1073/pnas.2319709121#fig01).

It is important to emphasize that these analogous tuning functions were not engineered into the artificial network by design, i.e., copied from the observed properties of V1 neurons. Rather—precisely as required for a true case of convergent evolution—the functionalities of artificial neurons which paralleled these of the cortical ones naturally emerged as the artificial network was trained to optimally perform its visual recognition task.

In line with the convergent evolution approach proposed here, the appearance of similar functional tuning between artificial and biological neurons, as in the case of orientation tuning, strongly argues that these properties play a functional role rather than being just an auxiliary epiphenomenon. However, it does not, on its own, provide a ready explanation of what is the exact role that such neuronal tuning plays in the ability of the organism or artificial system to recognize and categorize visual images. In fact, it is still far from clear, in the case of CNNs, what, if any, role do specific functional categories of artificial neurons play in the overall performance of the network (see ref. [17](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r17)). Nonetheless, the fact that we now have an artificial network that mimics visual performance opens the way for examining such potential roles of these neurons, for example by eliminating them, or modifying their tuning properties. Such work is feasible and will certainly shed important light on this issue, which may be relevant to our understanding of the biological system as well.

It is also important to note that the convergent evolution of orientation tuning has emerged in a number of diverse artificial networks with different objective functions (e.g., refs. [18](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r18), and [19](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r19)). This actually fits nicely with the fact that orientation selectivity is positioned upstream in the processing hierarchy and may feed into diverse down-stream functionalities. However, this diversity calls for caution when trying to interpret effects of e.g., artificial “lesions” performed in one type of model and argues for a more comprehensive and detailed work.

## The Function of Relational Coding in Human High-Order Face-Selective Areas

The discovery of orientation tuning of V1 neurons discussed above provides a seminal example of encoding expressed through the tuning properties of individual neurons. However, a growing interest has emerged in recent years focusing on a higher-order type of encoding that is not directly derived from the tuning of single or populations of neurons. Instead, this high-order code is proposed to be derived from the set of (dis)similarities (typically measured as the inverse correlation distances, or as the Euclidean distance between the population vectors) that are found between the activation patterns to different relevant stimuli. Such distance code is likely implemented in the unique interneuronal synaptic connectivity structure of each cortical area ( [20](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r20)). Operationally, this synaptic structure can be uncovered by activating the relevant neuronal populations by a set of appropriate stimuli or tasks and then examining the pairwise similarities (e.g., correlations, Euclidean distances) between these activation patterns. We will refer here to this kind of structure-derived coding by the term _relational_ code, since it derives its information from the similarity that appears between different neuronal patterns ( [21](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r21)– [25](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r25)).

At the conceptual level, relational coding, being an intrinsic, structural property of cortical areas, offers a plausible mechanism that can account for the observed diversity of functional properties found across different cortical areas ( [20](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r20), [22](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r22), [25](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r25)). A growing body of research has highlighted the usefulness and power of uncovering relational coding in characterizing the functional properties of different cortical areas and networks ( [26](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r26)– [30](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r30)).

Grossman et al. ( [31](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r31)) examined high-frequency amplitude responses of face-selective neuronal groups to different face exemplars using iEEG recordings (intracranial electrocorticography) obtained directly from the high-order human visual cortex in patients. These recordings are conducted strictly for clinical purposes in the course of diagnosis for intractable epilepsy. As we and others have shown, these direct recordings provide exceptionally high spatial and temporal resolutions of neuronal signals in the human brain ( [32](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r32)– [34](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r34)), and therefore provide a unique opportunity to look at relational geometries within a category-selective neuronal population.

Examining the activation patterns (population vectors) of the iEEG face-selective contacts to different face exemplars highlighted that beyond these activation patterns, a second-order coding was revealed in which, rather than the population vectors themselves, the matrix of similarities and dissimilarities between these vectors constituted a consistent relational geometry ( [20](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r20)) in which pairs of different face images expressed a varying degree of crossactivation-pattern similarity between their corresponding population vectors. However, it remains unclear, as pointed out in the introduction to this paper, what could be the functional role, if any, of such relational geometries. For example, considering the case of the face-related relational geometry, it could be argued that the consistent similarities and dissimilarities we find among patterns of activations to different faces are just auxiliary nonfunctional relationships with no direct role in the overall goal of the visual system, or in this case in perceiving and recognizing faces.

Here is where convergent evolution may be of help. Considering the fact that artificial, deep convolutional networks, trained for face and object recognition now, remarkably, perform equally well or even surpass human performance ( [35](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r35), [36](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r36)), one can experimentally test the convergent evolution conjecture. Thus, if relational geometry is of fundamental functional importance for face recognition, then it should have likely developed in parallel in both the face-selective human cortical areas and in the artificial convolutional network trained for face recognition. As in the case of orientation tuning in V1 neurons, it should be emphasized that, finding such “coincidence” will be more informative if the networks that are compared are very different in their make-up, development, and signaling.

Following this logic, Grossman et al. embarked upon comparing the relational geometry of human high-order face-selective cortical sites—as revealed in iEEG recordings with the different layers of a deep convolutional network trained for face recognition (VGG-Face). Significantly, this analysis revealed a high level of similarity between the relational geometries of the biological and artificial systems, which was specifically expressed in medium-high levels of the artificial network hierarchy ( [Fig. 2](https://www.pnas.org/doi/10.1073/pnas.2319709121#fig02)).

https://www.pnas.org/cms/10.1073/pnas.2319709121/asset/f7382efd-3fc1-46c4-8564-602c4fe028e2/assets/images/large/pnas.2319709121fig02.jpgConvergent evolution between the relational geometry of face-selective neural populations in humans and an artificial DCNN trained to recognize faces (VGG-face). ( _A_) The distribution of Human-to-DCNN correlations in relational geometries across the full hierarchy of the artificial network layers. Note that the correlation was highest in intermediate layers, pointing to a perceptual rather than identity role of the human face-selective geometry. ( _B_) Scatter plot depicting, on the _y_-axis, the pair-wise Euclidean distances between the activation patterns of human face-selective groups of neurons (estimated by the high-frequency amplitude signal recorded intracranially in iEEG face-selective contacts) and, on the _x_-axis, the patterns of artificial neurons in an intermediate-high layer of a deep convolutional network trained on face recognitions objective function (VGG-face). The significant correlation indicates similar relational geometries between the human and artificial systems. Figure reprinted from ref. [31](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r31). Copyright 2019. Licensed under CC BY, (link to [https://creativecommons.org/licenses/by/4.0/deed.en](https://creativecommons.org/licenses/by/4.0/deed.en)).

This example of convergent evolution helps to shed light on three important issues. First, it provides an indirect support to the hypothesis that relational geometries in the visual system, and especially in high-order visual areas, are not auxiliary phenomena but are essential to accomplishing the perceptual function of the visual system ( [37](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r37)). Second, they demonstrate that functional relational geometries can be established in feed-forward connectional patterns, a feat that conventional modeling approaches have failed to accomplish.

Finally, the specific manifestation of the convergent evolution—in this case, its appearance specifically in intermediate levels of the artificial network hierarchy—is informative about the function of the biological face-areas’ relational geometry. The fact that the correlation is found in intermediate layers rather than the uppermost, fully connected layers, which reflects the labeling of personal identity bears significance. It supports the hypothesis that human face-selective cortical regions located in the fusiform gyrus likely function as a pictorial rather than identity representation, namely, representing how faces look like rather than whose face is presented in the images (see refs. [20](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r20), and [31](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r31)).

However, it is important to emphasize that establishing a firm correspondence between such details as the layer profile may necessitate more detailed exploration across a number of network implementations. One productive approach may be to carefully analyze the details of the relational structures in each such layer and the tuning properties of their artificial neurons (see ref. [31](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r31)).

## The Function of Entorhinal Grid Cells

As has been extensively documented, the mammalian visual neocortex can be viewed as a large-scale hierarchy of cortical areas ( [38](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r38)). It has been demonstrated across a number of species that situated at the top of this cortical hierarchy is the entorhinal cortex—a medial-temporal region, which is the last station of neocortical information processing and serves as a major gateway to the paleocortical hippocampus. It is thus of great interest to consider whether convergent evolution principles of the kind discussed here could be applied to this top-level region as well.

While entorhinal neurons exhibit a diversity of functional properties whose detailed discussion is beyond the scope of this review, undoubtedly their most striking and intriguing tuning property, discovered and extensively explored by the Moser group, are the so-called “grid” cells ( [39](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r39)). This unique category of neurons, discovered first in rodents, but later found in other mammalian species ( [40](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r40)), including humans ( [41](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r41)), exhibit an intriguing firing pattern that is clearly related to an animal’s location in space. However, unlike hippocampal “place” cells ( [2](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r2)), these neurons are not tuned to a specific location. Instead, grid cells are active when the animal is located at multiple topographic locations organized, for 2D arenas, in hexagonal patterns ( [Fig. 3](https://www.pnas.org/doi/10.1073/pnas.2319709121#fig03)). Comparing the grid patterns across neighboring neurons reveals that they can phase-shift, while maintaining their grid distances, thus essentially tiling the entire surface of the arena ( [42](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r42)). Finally, and importantly, moving along the dorso-ventral axis of the rodent entorhinal cortex reveals that the grid spacing changes—shifting in modular jumps from large grid distances dorsally to small grid distances ventrally ( [42](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r42)). [Fig. 3](https://www.pnas.org/doi/10.1073/pnas.2319709121#fig03) depicts three examples of such grid patterns obtained from three different scale-modules.

https://www.pnas.org/cms/10.1073/pnas.2319709121/asset/c802f3df-3efd-4845-ab44-1c03b8d5a797/assets/images/large/pnas.2319709121fig03.jpgConvergent evolution between Entorhinal grid cells and cosine basis functions. ( _A_– _C_) Examples of three Entorhinal grid neurons ( _Top_, taken from ref. [43](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r43)) reflecting the typical hexagonal grid-like arrangement, and the different scales of grid distances along the entorhinal dorso-ventral axis. These grid cell images ( _Upper-Left_) were DCT transformed and the most prominent basis function (the one with the largest coefficient of this transformation), marked by a red arrow, is depicted in the _Upper-Right_ panels (CSB). Note the remarkable correspondence between the biological grid neurons and the CSBs, suggesting a parallel evolution between these two very different modes of representation.

This grid-like category of tuning properties is clearly of great interest and indeed a number of studies have made great progress in modeling the mechanisms that form the grids, with recent papers arguing for an intrinsic mechanism analogous to a continuous attractor organization ( [28](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r28)). However, while grid cells are clearly related to the animal’s estimate of its location in space—their functional role, i.e., what do they contribute to this function and specifically, why do they develop the unique grid structure—remains unknown. For example, it could be argued that the grid structure per se is not mandatory for coding an animal’s sense of location, and that its specific tuning properties may have emerged due to developmental or other constraints that are not directly relevant to performing the function of topographical localization. Here is where convergent evolution may help to shed light on this issue.

The critical question from the convergent evolution perspective is whether we can find a similar grid-like tuning in successful artificially engineered systems and if so—could it provide insight into entorhinal grid-cell functionality. Searching for such convergent evolution reveals a surprising correspondence in an engineering domain that seems, at first glance, highly unrelated to topography or navigation. This is the domain of image compression. Among the massive and diverse set of image compression tools that have been developed over the years, one specific compression algorithm—the JPEG format—has emerged as one of the most popular and widely used worldwide. JPEG compression has been applied, so far, to several billions of images ( [44](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r44)). Considering the domain of image compression algorithms, JPEG is certainly one of the top compression algorithms as evaluated by its evolutionary success from an engineering perspective.

Of particular relevance to grid neurons is the fact that at the heart of the JPEG compression algorithm is the decomposition of the image into a superposition of discrete cosine basis functions (CSBs). Critically, these CSBs manifest a remarkable functional tuning similarity to entorhinal grid cells. This surprising similarity between grid-cells receptive fields and JPEG CSBs is illustrated in [Fig. 3](https://www.pnas.org/doi/10.1073/pnas.2319709121#fig03). To obtain the estimated similarity between the biological and JPEG CSBs, we conducted the following analysis. Three example images of grid response fields were each transformed using 2-dimensional discrete cosine transform (2d-DCT), yielding the spectrum of DCT coefficients. By preserving only the highest DCT coefficient and nulling all others, we present the CSB function that best matches the original grid cell image (by calculating the inverse 2d-DCT of the single highest coefficient; [Fig. 3](https://www.pnas.org/doi/10.1073/pnas.2319709121#fig03), _Upper Right_-side panels).

What insights can we gain from this surprising similarity that appears between JPEG CSBs and entorhinal grid cells? First, it suggests that, similar to JPEG compression, the overall function of grid cells is to serve as a set of basis functions. In the case of grid cells, these functions provide an optimal compression of the topographical map of the animal location in space. Thus, each grid neuron functions, according to this suggested scheme, as a unique basis function in a global spatial map where the animal location is coded by the joint activity of all grid cells. A prediction derived from this analogy to JPEG CSBs is that individual grid cells and even same scale modules of grid cells do not function as isolated entities, but rather integrate their information across the many grid scales in order to form a unique compressed representation of the animal’s spatial location. Indeed, it has been previously demonstrated that by using such global population coding derived from multiple entorhinal grid neurons, of different scales, the animal’s position can be accurately decoded ( [45](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r45)).

Second, the convergent evolution perspective may also suggest what specific adaptive advantages the grid-like tuning properties of entorhinal neurons may endow the system over alternative possible coding schemes. Such hints may be derived by considering the advantages of the JPEG CSBs decomposition scheme over other coding alternatives that led to the evolutionary choice of JPEG CSBs as the most popular compression algorithm in use today. Indeed, JPEG is a lossy compression technique, which smartly discards some of the picture information (mainly high-frequency colors) with little perceptible loss in image quality. The main advantage of JPEG over other compression techniques (e.g., BMP or PNG) is the ability to store images in small-size files. This enables fast real-time loading of pictures over the internet, and also to store efficiently high-resolution pictures from cameras. It is interesting to consider which of these advantages led to the appearance of a similar mechanism manifested in the grid structure of entorhinal neurons’ receptive fields.

Finally, as we proposed above, the engineering parallel of biological systems can also provide a convenient model by which we can examine additional potential properties of the neuronal coding. Here, we examined whether the Cosine-basis functions were structured so as to generate an informative relational coding of space. As was explained above, in a _relational_ coding the information is coded by the similarities and differences between the different activation patterns elicited by different stimuli.

For a useful spatial representation, such a relational coding will necessitate, at a first approximation, that topographical distances between locations in the animal’s arena will be linearly related to the similarity distances between the collective grid-cells’ activation patterns. Specifically, one could ask whether the population vectors of the JPEG basis function amplitudes indeed show similarities that are linearly related to the similarity distance between pairs of images to be compressed (see also ref. [46](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r46)). For example, if we represent an animal’s estimated location by an image of a single-peaked 2-d exponential sphere function, will two images having nearby peak locations generate two vector patterns of JPEG basis functions that are more similar to each other compared to two remote spheres? Examining this issue illustrates that indeed CSBs decomposition captures image similarity in its relational coding. This is illustrated in [Fig. 4](https://www.pnas.org/doi/10.1073/pnas.2319709121#fig04), which depicts the observed relationship between these two measures—showing a clear linear correlation between them. Thus, if indeed grid cells operate in a similar fashion to JPEG basis functions, this leads not only to a unique coding for each location of the animal in the arena but also generates a relational code in which the distance between patterns actually represents their topographical interlocation distances.

https://www.pnas.org/cms/10.1073/pnas.2319709121/asset/2c05c90c-bb06-47d9-8abe-401a97ceb85a/assets/images/large/pnas.2319709121fig04.jpgRelational coding as represented by distances between perceived locations in space. ( _A_) Simulation of random locations in space, as represented by 2-d exponential sphere functions, with random mean and equal exponential decay. ( _B_) The dissimilarity (Euclidean) distance between pairs of 2d-DCT representations (vectors) of spheres as a function of Euclidean distance in real space of the same spheres. Note the high correlation (r = 0.94) between the distances in real space between all perceived locations, and the dissimilarity distance in DCT space of the same locations (the distance between the DCT coefficients of each location).

It is important to emphasize that the convergent evolution perspective is not aimed at replacing important contributions and insights obtained through a-priory hypothesis-driven approaches. Rather, it is aimed to augment and complement these insights by providing an additional perspective. The parallels we find between JPEG and entorhinal basis functions provide a case in point. A number of previous modeling works indeed came to a similar conclusion by taking a goal optimization approach ( [47](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r47), [48](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r48)). The convergent-evolution results should be viewed as confirming and extending these earlier insights.

Finally, it should be noted that the JPEG compression scheme has been successfully applied to other modalities, for example, to sound compression. It is thus tempting to consider the possibility that in analogous fashion there may be cortical grid representations of other cognitive categories. Indeed, a hint of such “conceptual” grid organization in the human cortex has been proposed ( [49](https://www.pnas.org/doi/10.1073/pnas.2319709121#core-collateral-r49)).

To conclude, we propose here that searching for unexpected parallels, i.e., convergent evolution, that emerge between neuronal properties and human-engineered systems could provide new insights into the role and adaptive advantage inherent in the observed neuronal tuning properties of cortical systems. We illustrate such insights using three examples derived from well-known visual and spatial representations: the case of orientation-selective neurons in the early visual cortex, the relational geometry of face responses in the high-order visual cortex, and entorhinal grid cells.

Importantly, we demonstrate the feasibility of employing engineering parallels in proposing novel hypothesis concerning neuronal properties in the case of grid-cells of the entorhinal cortex. Here, our perspective highlights a surprising parallel between entorhinal grid-cell receptive fields and basis function of lossy representations which have been successfully implemented in popular compression tools such as JPEG. In all these cases, the convergent evolution perspective offers fresh insights into the functional role of neuronal tuning properties as well as suggesting insights into how these unique tunings contribute to the overall adaptive function of the brain.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="distinct-ai-models-seem-to-converge-on-how-they-encode-reali.md">
<details>
<summary>Distinct AI Models Seem To Converge On How They Encode Reality</summary>

Phase: [EXPLORATION]

**Source URL:** <https://www.quantamagazine.org/distinct-ai-models-seem-to-converge-on-how-they-encode-reality-20260107>

# Distinct AI Models Seem To Converge On How They Encode Reality
_By_ [Ben Brubaker](https://www.quantamagazine.org/authors/brubaker_ben/)

_January 7, 2026_

Is the inside of a vision model at all like a language model? Researchers argue that as the models grow more powerful, they may be converging toward a singular “Platonic” way to represent the world.

https://www.quantamagazine.org/wp-content/uploads/2026/01/Platonic-Representations-cr-Mark-Belan-Lede.webp

Do all AI models represent “cat” in the same way?

Mark Belan/ _Quanta Magazine_

## Introduction

Read a story about dogs, and you may remember it the next time you see one bounding through a park. That’s only possible because you have a unified concept of “dog” that isn’t tied to words or images alone. Bulldog or border collie, barking or getting its belly rubbed, a dog can be many things while still remaining a dog.

Artificial intelligence systems aren’t always so lucky. These systems learn by ingesting [vast troves of data](https://www.quantamagazine.org/how-can-ai-id-a-cat-an-illustrated-guide-20250430/) in a process called training. Often, that data is all of the same type — text for language models, images for computer vision systems, and more exotic kinds of data for systems designed to predict the [odor of molecules](https://www.quantamagazine.org/ai-model-links-smell-molecules-with-metabolic-processes-20221010/) or the [structure of proteins](https://www.quantamagazine.org/how-ai-revolutionized-protein-science-but-didnt-end-it-20240626/). So to what extent do language models and vision models have a shared understanding of dogs?

Researchers investigate such questions by peering inside AI systems and studying how they represent scenes and sentences. A [growing body of research (opens a new tab)](http://arxiv.org/abs/2310.13018) has found that different AI models can develop similar representations, even if they’re trained using different datasets or entirely different data types. What’s more, a few studies have suggested that those representations are growing more similar as models grow more capable. In a [2024 paper (opens a new tab)](https://arxiv.org/abs/2405.07987), four AI researchers at the Massachusetts Institute of Technology argued that these hints of convergence are no fluke. Their idea, dubbed the Platonic representation hypothesis, has inspired a lively debate among researchers and a [slew (opens a new tab)](http://arxiv.org/abs/2502.16282) [of (opens a new tab)](https://arxiv.org/abs/2503.05283) [follow-up (opens a new tab)](https://arxiv.org/abs/2512.03750) [work (opens a new tab)](http://arxiv.org/abs/2511.02767).

The team’s hypothesis gets its name from a 2,400-year-old allegory by the Greek philosopher Plato. In it, prisoners trapped inside a cave perceive the world only through shadows cast by outside objects. Plato maintained that we’re all like those unfortunate prisoners. The objects we encounter in everyday life, in his view, are pale shadows of ideal “forms” that reside in some transcendent realm beyond the reach of the senses.

The Platonic representation hypothesis is less abstract. In this version of the metaphor, what’s outside the cave is the real world, and it casts machine-readable shadows in the form of streams of data. AI models are the prisoners. The MIT team’s claim is that very different models, exposed only to the data streams, are beginning to converge on a shared “Platonic representation” of the world behind the data.

“Why do the language model and the vision model align? Because they’re both shadows of the same world,” said [Phillip Isola (opens a new tab)](https://web.mit.edu/phillipi/), the senior author of the paper.

Not everyone is convinced. One of the main points of contention involves which representations to focus on. You can’t inspect a language model’s internal representation of every conceivable sentence, or a vision model’s representation of every image. So how do you decide which ones are, well, representative? Where do you look for the representations, and how do you compare them across very different models? It’s unlikely that researchers will reach a consensus on the Platonic representation hypothesis anytime soon, but that doesn’t bother Isola.

“Half the community says this is obvious, and the other half says this is obviously wrong,” he said. “We were happy with that response.”

## **The Company Being Kept**

If AI researchers don’t agree on Plato, they might find more common ground with his predecessor Pythagoras, whose philosophy supposedly started from the premise “All is number.” That’s an apt description of the neural networks that power AI models. Their representations of words or pictures are just long lists of numbers, each indicating the degree of activation of a specific artificial neuron.

To simplify the math, researchers typically focus on a single layer of a neural network in isolation, which is akin to taking a snapshot of brain activity in a specific region at a specific moment in time. They write down the neuron activations in this layer as a geometric object called a vector — an arrow that points in a particular direction in an abstract space. Modern AI models have many thousands of neurons in each layer, so their representations are high-dimensional vectors that are impossible to visualize directly. But vectors make it easy to compare a network’s representations: Two representations are similar if the corresponding vectors point in similar directions.

Within a single AI model, similar inputs tend to have similar representations. In a language model, for instance, the vector representing the word “dog” will be relatively close to vectors representing “pet,” “bark,” and “furry,” and farther from “Platonic” and “molasses.” It’s a [precise mathematical realization](https://www.quantamagazine.org/how-embeddings-encode-what-words-mean-sort-of-20240918/) of an idea memorably expressed more than 60 years ago by the British linguist John Rupert Firth: “You shall know a word by the company it keeps.”

What about representations in different models? It doesn’t make sense to directly compare activation vectors from separate networks, but researchers have devised indirect ways to assess representational similarity. One popular approach is to embrace the lesson of Firth’s pithy quote and measure whether two models’ representations of an input keep the same company.

Imagine that you want to compare how two language models represent words for animals. First, you’ll compile a list of words — dog, cat, wolf, jellyfish, and so on. You’ll then feed these words into both networks and record their representations of each word. In each network, the representations will form a cluster of vectors. You can then ask: How similar are the overall shapes of the two clusters?

“It can kind of be described as measuring the similarity of similarities,” said [Ilia Sucholutsky (opens a new tab)](https://ilia10000.github.io/), an AI researcher at New York University.

Mark Belan/ _Quanta Magazine_

In this simple example, you’d expect some similarity between the two models — the “cat” vector would probably be close to the “dog” vector in both networks, for instance, and the “jellyfish” vector would point in a different direction. But the two clusters probably won’t look exactly the same. Is “dog” more like “cat” than “wolf,” or vice versa? If your models were trained on different datasets, or built on different network architectures, they might not agree.

Researchers [began to explore (opens a new tab)](https://arxiv.org/abs/1511.07543) representational similarity among AI models with this approach in the mid-2010s and found that different models’ representations of the same concepts were often similar, though far from identical. Intriguingly, a few studies found that more powerful models seemed to have more similarities in their representations than weaker ones. One 2021 paper dubbed this the “ [Anna Karenina scenario (opens a new tab)](https://arxiv.org/abs/2106.07682),” a nod to the opening line of the [classic Tolstoy novel (opens a new tab)](https://www.gutenberg.org/files/1399/1399-h/1399-h.htm). Perhaps successful AI models are all alike, and every unsuccessful model is unsuccessful in its own way.

That paper, like much of the early work on representational similarity, focused only on computer vision, which was then the most popular branch of AI research. The advent of powerful language models was about to change that. For Isola, it was also an opportunity to see just how far representational similarity could go.

## **Convergent Evolution**

The story of the Platonic representation hypothesis paper began in early 2023, a turbulent time for AI researchers. ChatGPT had been released a few months before, and it was increasingly clear that simply scaling up AI models — training larger neural networks on more data — made them better at many different tasks. But it was unclear why.

“Everyone in AI research was going through an existential life crisis,” said [Minyoung Huh (opens a new tab)](https://minyoungg.github.io/me/), an OpenAI researcher who was a graduate student in Isola’s lab at the time. He began meeting regularly with Isola and their colleagues [Brian Cheung (opens a new tab)](https://briancheung.github.io/) and [Tongzhou Wang (opens a new tab)](https://www.tongzhouwang.info/) to discuss how scaling might affect internal representations.

https://www.quantamagazine.org/wp-content/uploads/2026/01/Phillip-Isola-Mosaic.webp

Clockwise from top right: Minyoung Huh, Brian Cheung, Tongzhou Wang, and Phillip Isola proposed that different AI models are converging toward a shared “Platonic representation” of the world behind their training data.

From top right: Anna Decker; @by.h\_official; Jiaxi Chen; Kris Brewer

Imagine a case where multiple models are trained on the same data, and the stronger models learn more similar representations. This isn’t necessarily because these models are creating a more accurate likeness of the world. They could just be better at grasping quirks of the training dataset.

Now consider models trained on different datasets. If their representations also converge, that would be more compelling evidence that models are getting better at grasping shared features of the world behind the data. Convergence between models that learned from entirely different data types, such as language and vision models, would provide even stronger evidence.

A year after their initial conversations, Isola and his colleagues decided to write a paper reviewing the evidence for convergent representations and presenting an argument for the Platonic representation hypothesis.

By then, other researchers had [started (opens a new tab)](https://arxiv.org/abs/2209.15162) [studying (opens a new tab)](https://arxiv.org/abs/2302.06555) [similarities (opens a new tab)](https://arxiv.org/abs/2401.05224) between vision and language model representations. Huh conducted his own experiment, in which he tested a set of five vision models and 11 language models of varying sizes on a dataset of captioned pictures from Wikipedia. He would feed the pictures into the vision models and the captions into the language models, and then compare clusters of vectors in the two types. He observed a steady increase in representational similarity as models became more powerful. It was exactly what the Platonic representation hypothesis predicted.

## **Find the Universals**

Of course, it’s never so simple. Measurements of representational similarity invariably involve a host of experimental choices that can affect the outcome. Which layers do you look at in each network? Once you have a cluster of vectors from each model, which of the [many (opens a new tab)](https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/neuro.06.004.2008/full) [mathematical (opens a new tab)](https://arxiv.org/abs/1905.00414) [methods (opens a new tab)](https://arxiv.org/abs/2305.06329) do you use to compare them? And which representations do you measure in the first place?

“If you only test one dataset, you don’t necessarily know how \[the result\] generalizes,” said Christopher Wolfram, a researcher at the University of Chicago who has studied [representational similarity in language models (opens a new tab)](https://arxiv.org/abs/2504.08775). “Who knows what would happen if you did some weirder dataset?”

Isola acknowledged that the issue is far from settled. It’s not a question that any one paper can resolve: In principle, you can measure models’ representations of any picture or any sentence. To him, cases where models do exhibit convergence are more compelling than cases where they may not.

https://www.quantamagazine.org/wp-content/uploads/2026/01/Alexei-Efros-cr.PeterDaSilve.webp

Alexei Efros argues that the differences between AI models reveal more than the similarities.

Peter DaSilva for _Quanta Magazine_

“The endeavor of science is to find the universals,” Isola said. “We could study the ways in which models are different or disagree, but that somehow has less explanatory power than identifying the commonalities.”

Other researchers argue that it’s more productive to focus on where models’ representations differ. Among them is [Alexei Efros](https://www.quantamagazine.org/the-computing-pioneer-helping-ai-see-20231024/), a researcher at the University of California, Berkeley, who has been an adviser to three of the four members of the MIT team.

“They’re all good friends and they’re all very, very smart people,” Efros said. “I think they’re wrong, but that’s what science is about.”

Efros noted that in the Wikipedia dataset that Huh used, the images and text contained very similar information by design. But most data we encounter in the world has features that resist translation. “There is a reason why you go to an art museum instead of just reading the catalog,” he said.

Any intrinsic sameness across models doesn’t have to be perfect to be useful. Last summer, researchers [devised a method (opens a new tab)](http://arxiv.org/abs/2505.12540) to translate internal representations of sentences from one language model to another. And if language and vision model representations are to some extent interchangeable, that could lead to new ways to train models that learn from both data types. Isola and others explored [one such training scheme (opens a new tab)](https://arxiv.org/abs/2510.08492) in a recent paper.

Despite these promising developments, other researchers think it’s unlikely that any single theory will fully capture the behavior of modern AI models.

“You can’t reduce a trillion-parameter system to simple explanations,” said [Jeff Clune (opens a new tab)](http://jeffclune.com/), an AI researcher at the University of British Columbia. “The answers are going to be complicated.”

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="representation-topology-divergence-a-method-for-comparing-ne.md">
<details>
<summary>Representation Topology Divergence: a Method for Comparing Neural Network Representations</summary>

Phase: [EXPLORATION]

**Source URL:** <https://proceedings.mlr.press/v162/barannikov22a/barannikov22a.pdf>

# Representation Topology Divergence: a Method for Comparing Neural Network Representations 

Serguei Barannikov 1 2 Ilya Trofimov 1 Nikita Balabin 1 Evgeny Burnaev 1 3 

# Abstract 

Comparison of data representations is a complex multi-aspect problem that has no complete solu-tion yet. We propose a method for comparing two data representations. We introduce the Rep-resentation Topology Divergence (RTD) which measures the dissimilarity in multi-scale topology between two point clouds of equal size with a one-to-one correspondence between points. The data point clouds are allowed to lie in different ambient spaces. The RTD is one of the few practical meth-ods based on Topological Data Analysis (TDA) applicable to real machine learning datasets. Ex-periments show the proposed RTD agrees with the intuitive assessment of data representation simi-larity and is sensitive to its topological structure. We apply RTD to gain insights into neural net-work representations in computer vision and NLP domains for various problems: training dynamics analysis, data distribution shift, transfer learning, ensemble learning. 

# 1. Introduction 

Representations of objects are the essential component learnt by deep neural networks. In opposite to the distance in the original space, the similarity of representations is proved to be semantically meaningful. Despite the significant prac-tical success of deep neural networks, many aspects of their behavior are poorly understood. Only a few methods study neural representations without relying on their quality on a specific downstream task. In this work, we focus on the comparison of representations from neural networks. Comparison of representations is an ill-posed problem with-out a “ground truth” answer. Early studies were based on variants of Canonical Correlation Analysis (CCA): SVCCA,         

> 1Skolkovo Institute of Science and Technology, Moscow, Rus-sia 2CNRS, Universit ´e Paris Cit ´e, France 3Artificial Intelligence Research Institute (AIRI), Moscow, Russia Correspondence to: Serguei Barannikov <S.Barannikov@skoltech.ru >.
> Proceedings of the 39 th International Conference on Machine Learning , Baltimore, Maryland, USA, PMLR 162, 2022. Copy-right 2022 by the author(s).

(Raghu et al., 2017), PWCCA (Morcos et al., 2018). How-ever, CCA-like measures define similarity too loosely since they are invariant under any invertible linear transformation. The Centered Kernel Alignment (CKA), (Kornblith et al., 2019) is the statistical test to measure the independence of two sets of variables. (Kornblith et al., 2019) proved CKA to be more consistent with the intuitive similarity of representations. Particularly, neural networks learn similar representations from different seeds as evaluated by CKA. Another line of work is concerned with the alignment be-tween groups of neurons (Li et al., 2015), (Wang et al., 2018). The similarity of representations is also a topic of study in neuroscience (Edelman, 1998; Kriegeskorte et al., 2008; Connolly et al., 2012). Representational similarity metrics like CKA and CCA were used to gain insights on representations obtained in meta-learning (Raghu et al., 2020), to compare representations from different layers of language models (Voita et al., 2019), and to study the effect of fine-tuning (Wu et al., 2020). Finally, (Nguyen et al., 2021) used CKA to study the phe-nomenon of a “block structure” emerging in wide and deep networks in computer vision and compare their representa-tions. In this paper, we take a topological perspective on the comparison of neural network representations. We pro-pose the Representation Topology Divergence (RTD) score, which measures dissimilarity between two point clouds of equal size with a one-to-one correspondence between points. Point clouds are allowed to lie in different ambient spaces. Existing geometrical and topological methods are dedicated to other problems: they are either too general and do not incorporate the one-to-one correspondence re-quirement (Khrulkov & Oseledets, 2018), (Tsitsulin et al., 2020), or they restrict point clouds to lie in the same ambi-ent space (Kynk ¨a ¨anniemi et al., 2019), (Barannikov et al., 2021). Most of these methods are applied to the evaluation of GANs. Recently, (Moor et al., 2020) proposed a loss term to compare the topology of data in original and latent spaces and applied the term as a part of the Topological Autoencoder. In this work, we make the following contributions: Representation Topology Divergence: a Method for Comparing Neural Network Representations 

Figure 1: Comparison of representations after the ith epoch and the final one done by RTD, 1−CKA, and disagreement of predictions. All the measures are normalized by division to their maximal values. Strikingly, RTD highly correlates with the disagreement of models’ predictions. 1. We propose a topologically-inspired approach for com-parison of neural network representations; 2. We introduce the R-Cross-Barcode (P, ˜P ), a tool based on Topological Data Analysis (TDA), which measures the differences in the multi-scale topology of two point clouds P, ˜P with a one-to-one correspondence between points; 3. Based on the R-Cross-Barcode (P, ˜P ), we define the 

Representation Topology Divergence (RTD) , the quan-tity measuring the multi-scale topological dissimilarity between two representations; 4. Our computational experiments show that RTD agrees with an intuitive notion of neural network representa-tions similarity. In contrast to most existing approaches, RTD is sensitive to differences in topological structures (clusters, voids, cavities, tunnels, etc.) of the represen-tations and enjoys a very good correlation with dis-agreement of models predictions. We apply RTD to compare representations in computer vision and NLP domains and various problems: training dynamics anal-ysis, data distribution shift, transfer learning, ensemble learning, and disentanglement. Experiments show that RTD outperforms CKA, IMD, and SVCCA. The source code is publicly available: 

https://github.com/IlyaTrofimov/RTD .

# 2. Comparing Neural Network Representations 

Our starting point is the geometric perspective on represen-tation learning through the lens of the manifold hypothesis (Goodfellow et al., 2016), according to which real-world data presented in a high-dimensional space are expected to concentrate in the vicinity of a manifold of much lower dimension. The low-dimensional manifold MP underlying the given data representation P can be accessed in general only through discrete sets of samples. The standard ap-proach to recover the manifold MP is to take a sample P

and to approximate MP by a set of simplexes with vertices from P . Commonly, to select the simplexes approximat-ing MP one has to fix a threshold α > 0 and consider the simplexes with edge lengths not exceeding α (Niyogi et al., 2008; Belkin & Niyogi, 2001). It is difficult to guess the cor-rect value of the threshold, and hence a reasonable approach is to study all thresholds at once. Given two representations, we consider two corresponding graphs with distance-like weights and compare the differ-ence in the multiscale topology of the two graphs. Let P, ˜P be two representations giving two embeddings of the same data V. The two embeddings P, ˜P belong in general to different ambient spaces and have the natural one-to-one correspondence between points in P and ˜P. Given a sample of data V ⊆ V , the two representations P = P(V ),

˜P = ˜P(V ) define two weighted graphs Gw, G ˜w with the same vertex set V . The weights wAB , ˜wAB of an edge 

AB are given by the distances wAB = dist( P (A), P (B)) ,

˜wAB = dist( ˜P (A), ˜P (B)) .The simplicial approximation to the manifold MP at thresh-old α consists of simplexes whose edges in Gw have weights not exceeding α. Let Gw≤α denote the graph with the vertex set V and the edges with weights not exceeding α. To com-pare the simplicial approximations to the manifolds MP and 

M ˜P described by the graphs Gw≤α and G ˜w≤α, we compare each of the two simplicial approximations with the union of simplices formed by edges present in at least one of the two graphs. The graph Gmin( w, ˜w)≤α contains an edge between vertices A and B iff the distance between the points A and 

B is smaller than α in at least one of the representations P ,

˜P . The set of edges of the graph Gmin( w, ˜w)≤α is the union of sets of edges of Gw≤α and G ˜w≤α. The similarity of manifolds MP and M ˜P can be measured by the degrees of Representation Topology Divergence: a Method for Comparing Neural Network Representations 

similarities of the graph Gmin( w, ˜w)≤α with the graph Gw≤α

and the graph G ˜w≤α.

Figure 2: Graphs Gw≤α, G ˜w≤α and Gmin( w, ˜w)≤α with edges not in Gw≤α colored in green. 

2.1. Topological features for a pair of weighted graphs 

One way to measure the discrepancy between the graphs 

Gw≤α and Gmin( w, ˜w)≤α is to count the graph Gw≤α

connected components merged together in the graph 

Gmin( w, ˜w)≤α. We show an example of this situation in Fig-ure 2 right, see also Figure 10, where three graphs Gw≤α,

G ˜w≤α and Gmin( w, ˜w)≤α are shown, with edges of the graph 

Gmin( w, ˜w)≤α not in Gw≤α colored in green. Each merging is represented by a class of green paths in Gmin( w, ˜w)≤α join-ing two blue clusters. The significance of the discrepancy constituted by the green path is measured by the differ-ence αd − αb in the smallest thresholds αb, α d at which the two clusters are merged in Gmin( w, ˜w)≤αb and Gw≤αd .Homology is the tool that permits counting such topological features, because of the space limit we gather the defini-tions and necessary properties of homology in Appendix A, see also (Hatcher, 2005). The number of these simplest topological features is the dimension of the kernel of linear map H0(Gw≤α) → H0(Gmin( w, ˜w)≤α), as basis elements of the vector space H0 correspond to the graph connected components. It may also happen that a non-trivial merg-ing happens between two distant parts of the same Gw≤α

cluster or between two Gw≤α clusters already connected via a chain of merging, as on Figure 9. The number of these features is the dimension of the cokernel of the map 

H1(Gw≤α) → H1(Gmin( w, ˜w)≤α). Hence the number of non-trivial mergings is the sum of the two numbers. We are interested in these numbers for all possible thresholds α.When the threshold α is increased then more green and blue edges appear, and also certain green edges become blue. Using an auxiliary graph and the barcodes algorithm, we calculate the numbers of such topological features for all values of α at once. 

2.2. R-Cross-Barcode 

Recall that the Vietoris-Rips complex of a graph G

equipped with edge weights’ matrix m is the collection of k−simplexes, k ≥ 0, which are (k + 1) −element subsets of the set of vertices of G, with the filtration threshold of a simplex defined by the maximal weight on the edges: 

Rα(Gm) = {{Ai0 , . . . , A ik }, A i ∈ Vert( G)|mAiAj ≤ α}

Our simplicial approximation to the manifold MP at thresh-old α is the union of all simplexes from the simplicial com-plex Rα(Gw), and similarly the approximation to M ˜P is the union of all simplexes from Rα(G ˜w).The dissimilarity between the filtered simplicial complexes 

Rα(Gw) and Rα(G ˜w) can be quantified using the homo-logical methods. The relevant tools here are homology, barcodes and homology exact sequences. We describe our construction below and, because of space limitations, we sketch further explanation of the construction in Appendix, Section A.2. Concretely, to compare the multi-scale topology of the two weighted graphs Gw and G ˜w we introduce the weighted graph ˆGw, ˜w with doubled set of vertices and with the edge weights defined as follows. For convenience, fix a number-ing of vertices Vert (G) = {A1, . . . , A N }. For each vertex 

A ∈ Vert (G) we add the extra vertex A′ together with A

to ˆG, plus the unique additional vertex O, and define the distance-like edge weights in ˆGw, ˜w as: 

dA′ 

> iA′
> j

= min( wAiAj , ˜wAiAj ), d AiA′ 

> j

= dAiAj = wAiAj ,dAiA′ 

> i

= dOA i = 0 , d Aj A′ 

> i

= dOA ′ 

> i

= + ∞ (1) where i < j and O ∈ Vert ( ˆGw, ˜w) is the additional vertex. In practice, for the calculation of RTD described below, the distance matrix can be taken in a slightly simpler form 

m =

( 0 (w+)ᵀ

w+ min( w, ˜w)

)

, where w and ˜w are the edge weight matrices of Gw and G ˜w, and w+, respectively (w+)ᵀ,is the matrix w with upper-(respectively, lower-)triangular part replaced by +∞.Next, we construct the Vietoris-Rips filtered simplicial complex of the graph ˆGw, ˜w and take its barcode. The doubling of vertices in ˆGw, ˜w creates triangles OA iAj ,

AiAj A′ 

> j

, AiA′

> i

A′ 

> j

at the threshold α = wAiAj . These triangles ”kill” the edge A′

> i

A′ 

> j

becoming blue at this thresh-old. Intuitively, the i−th barcode of Rα( ˆGw, ˜w) records the i-dimensional topological features that are born in 

Gmin( w, ˜w)≤α but are not yet born near the same place in 

Gw≤α and the (i − 1) −dimensional topological features that are dead in Gmin( w, ˜w)≤α but are not yet dead at the same place in Gw≤α, see Theorem 2.1 below. 

Definition . The R-Cross-Barcode i(P, ˜P ) is the set of inter-vals recording the “births” and “deaths” of i-dimensional Representation Topology Divergence: a Method for Comparing Neural Network Representations 

Algorithm 1 R-Cross-Barcode i(P, ˜P )

Input: w, ˜w : matrices of pairwise distances within point clouds P , ˜P

Require: vr (m): function computing filtered complex from pairwise distances matrix m

Require: B(C, i ): function computing persistence intervals of filtered complex C in dimension iw, ˜w ← w, ˜w divided by their 0.9 quantiles 

m ←



w (w+)ᵀ 0

w+ min( w, ˜w) +∞

0 +∞ 0



R-Cross-Barcode i ← B(vr (m), i )

Return: intervals list R-Cross-Barcode i(P, ˜P ) represent-ing ”births” and ”deaths” of topological discrepancies between P and ˜P .

Algorithm 2 RTD (P, ˜P), see section 2.4 for details, sug-gested default values: b = 500 , n = 10 

Input: P ∈ R|V|× D , ˜P ∈ R|V|× ˜D : data representations 

for j = 1 to n do 

Vj ← random choice ( V, b )

Pj , ˜Pj ← P (Vj ), ˜P(Vj )

Bj ← R-Cross-Barcode 1(Pj , ˜Pj ) intervals’ list calcu-lated by Algorithm 1 

rtd j ← sum of lengths of all intervals in Bj

end for 

RTD 1(P, ˜P) ← mean (rtd )

Return: number RTD 1(P, ˜P) representing discrepancy be-tween the representations P, ˜P

topological features in the filtered simplicial complex 

Rα( ˆGw, ˜w).The R-Cross-Barcode ∗(P, ˜P ) (for Representations’ Cross-Barcode ) records the differences in the multiscale topology of the two embeddings. The topological features with longer lifespans indicate in general the essential features. 

Theorem 2.1. Basic properties of R-Cross-Barcode ∗(P, ˜P ):

• if P (A) = ˜P (A) for any object A ∈ V , then R-Cross-Barcode ∗(P, ˜P ) = ∅;

• if all distances within ˜P (V ) are zero i.e. all objects are represented by the same point in ˜P , then for all k ≥ 0: R-Cross-Barcode k+1 (P, ˜P ) = Barcode k(P ) the standard barcode of the point cloud P ;

• for any value of threshold α, the following sequence of natural linear maps of homology groups 

> r3i+3

−−−→ Hi(Rα(Gw)) r3i+2 

−−−→ Hi(Rα(Gmin( w, ˜w))) r3i+1 

−−−→

> r3i+1

−−−→ Hi(Rα( ˆGw, ˜w)) r3i

−−→ Hi−1(Rα(Gw)) r3i−1

−−−→

> r3i−1

−−−→ . . . r1

−→ H0(Rα(Gmin( w, ˜w))) r0

−→ 0 (2) 

is exact, i.e. for any j the kernel of the map rj is the image of the map rj+1 .

The proof of the first two properties is immediate and the third property follows from the properties of distinguished triangles of complexes, see Appendix A for more details. The exactness of the sequence (2) for j = 1 , 2, 3 implies that the calculation of the topological features from Section 2.1 for all α is reduced to the calculation of H1(Rα( ˆGw, ˜w)) 

for all α, i.e. to the calculation of R-Cross-Barcode 1(P, ˜P ).

2.3. Representation Topology Divergence. 

The R-Cross-Barcode ∗(P, ˜P ) is by itself, to our opinion, a precise and intuitive tool for understanding discrepancies between two representations. There are several numerical characteristics measuring the non-emptyness of R-Cross-Barcode . Based on experiments and on relation of sum of bars’ lengths with Earth Moving Distance (Barannikov et al., 2021), we define the sum of lengths of the bars in R-Cross-Barcode i(P, ˜P ), denoted RT D i(P, ˜P ), as the scalar char-acterizing the degree of topological discrepancy between the representations P, ˜P . We use most often the average of RT D 1(P, ˜P ) and RT D 1( ˜P , P ), denoted RTD score, in our computations below. 

Proposition 2.2. If RT D i(P, ˜P ) = RT D i( ˜P , P ) = 0 for all i ≥ 1, then the barcodes of the weighted graphs Gw

and G ˜w are the same in any degree. Moreover, in this case the topological features are located in the same places: the inclusions Rα(Gw) ⊆ Rα(Gmin( w, ˜w)), Rα(G ˜w) ⊆

Rα(Gmin( w, ˜w)) induce homology isomorphisms for any threshold α.

2.4. Algorithm 

First we compute the R-Cross-Barcode 1(P, ˜P ) on two rep-resentations P, ˜P of a sample V . For this we calculate the matrices of pairwise distances w, ˜w within the point clouds 

P , ˜P . We assume that the metrics in the ambient spaces of representations are normalized so that the two point clouds are of comparable size, namely their 0.9 quantile of pair-wise distances coincide. This ensures that our score has scaling invariance, the reasonable property of a good repre-sentation similarity measure, as argued in e.g. (Kornblith et al., 2019). Next, the algorithm builds the Vietoris-Rips complex from the matrix m defined in Equation 1. Then the 

1−dimensional barcode, see (Barannikov, 2021; Chazal & Michel, 2017), of the built filtered simplicial complex is cal-culated. The last two steps can be done using scripts that are optimized for GPU acceleration (Zhang et al., 2020). Then we sum the lengths of bars in R-Cross-Barcode 1(P, ˜P ). To get the symmetric measure we usually take the half-sum Representation Topology Divergence: a Method for Comparing Neural Network Representations        

> (a) Point clouds used in “clusters” experiment.
> (b) Representations’ comparison measures. Ideally, the measure should change monotonically with the increase of topological discrepancy.
> (c) R-Cross-Barcode (P, ˜P)for the “clusters” experiments. ˜P- is the point cloud having one cluster, P- 2, 3, 4, 5, 6, 10, 12 clusters.

Figure 3: RTD perfectly detects cluster structures, while rival measures fail. One cluster is compared with 2-12 clusters. with the similar sum of bars in R-Cross-Barcode 1( ˜P , P ).The computation is repeated a sufficient number of times to obtain the mean of the chosen characteristics. We have observed experimentally that about 10 times is usually suffi-cient for common datasets. The main steps of the computa-tion are summarized in Algorithms 1 and 2. 

Complexity. Algorithm 1 starts with computation of the two matrices of pairwise distances w, ˜w for a pair of repre-sentations of a sample V : P ∈ Rb×D , ˜P ∈ Rb× ˜D involving 

O(|V |2(D + ˜D)) operations. Next, persistent intervals of the filtered complex must be computed. Given the distance matrix m, the complexity of their computation does not depend on the dimensions D, ˜D of the data representations. Generally, the barcode computation is at worst cubic in the number of simplexes involved. In practice, the computation is quite fast since the boundary matrix is typically sparse for real datasets. For R-Cross-Barcodes’ calculation, we used GPU-optimized software. Thus, the computation of R-Cross-Barcode takes a similar time as in the previous step even on datasets of high dimensionality. Since only the dissimilarities in representation topology are calculated, the results are quite robust and a rather low number of iterations is needed to obtain accurate results. 

# 3. Experiments 

In the experimental section, we study the ability of the proposed R-Cross-Barcodes and RTD to detect changes in topological structures with the use of synthetic point clouds; we demonstrate the superiority of RTD over CKA, SVCCA, IMD (Section 3.1). RTD meaningfully compares represen-tations from UMAP with different parameters (Section 3.2). By comparing representations from various architectures (Section 3.3), layers, epochs, ensembles and after data distri-bution shift (Section 3.4) we show that RTD is in line with natural notion of representational similarity. A high corre-lation between RTD and disagreement of neural network predictions is an interesting empirical finding. 

3.1. Experiments with synthetic point clouds 

We start with small-scale experiments with synthetic point clouds: “clusters” and “rings”. For the “clusters” exper-iment (Figure 3, top), the initial point cloud consists of 300 points randomly sampled from the 2-dimensional nor-mal distribution having mean (0 , 0) . Next, we split it into 2,3. . . 12 parts (clusters) and move them to the circle of ra-dius 10. Then, we compare the initial point cloud (having one cluster) with the split ones. We compared these point clouds by calculating: RTD, CKA (Kornblith et al., 2019), IMD (Tsitsulin et al., 2020) and SVCCA (Raghu et al., 2017). We calculated linear CKA since (Kornblith et al., 2019) concluded that it provides the same performance as the RBF kernel, but does not re-quire selecting a kernel width. For SVCCA, we calculated average correlation ¯ρ for the truncation threshold 0.99, as recommended in (Raghu et al., 2017). The IMD score (Tsit-sulin et al., 2020) was very noisy and we averaged it over 100 runs. Representation Topology Divergence: a Method for Comparing Neural Network Representations   

> (a) 2D representations of MNIST with n neighbors = 10, 50, 200 (b) 1-CKA (c) RTD

Figure 4: Comparing representations of MNIST by UMAP with varying n neighbors. Figure 3b presents the results: RTD perfectly tracks the change of the topological complexity while the alternative measures mostly fail. The Kendall-tau rank correlations of the measures with a number of clusters are: RTD: 1.0, CKA: 0.23, IMD: 0.43, SVCCA: 0.14. We also note that RTD does not have any tunable parameters as SVCCA and does not require averaging over as many runs as IMD. Fig-ure 3c shows the H1 R-Cross-Barcodes calculated while comparing clusters. In accordance with the definition of RTD, H0 barcodes are absent. The sum of the lengths of the segments increases with increasing differences in topology. Running times and all of the R-Cross-Barcodes are shown in Appendix C. Additional representation similarity measures were evaluated in Appendix I. In the “rings” experiment , we compared synthetic point clouds consisting of a variable number of rings, see Figure 12a in Appendix D. Initially, there are 500 points uniformly distributed over the unit circle. Then, the points are moved onto circles with radii varying from 0.5 to 1.5. Finally, we compare the point cloud having 5 rings with other ones. Figure 12b in Appendix D present the results. RTD almost ideally reflects the change of the topological complexity while the alternative measures mostly fail. The Kendall-tau rank correlations of the measures with a number of rings are: RTD: 0.8, CKA: -0.2, IMD: 0.8, SVCCA: -0.2. In the next sections, we compare RTD only with CKA, since it is the most popular method for comparing neural representations (Kornblith et al., 2019; Nguyen et al., 2021). 

3.2. Comparing representations from UMAP 

UMAP (McInnes et al., 2018) is the state-of-the-art method for visualizing high-dimensional datasets by obtaining their 2D/3D representations. We apply UMAP to the MNIST dataset to get 2D representations. We vary the number of neighbors in UMAP in the range (10 , 20 , 50 , 100 , 200) ,see Figure 4a (all of the figures are in Appendix H). This parameter affects the cluster structure: for low values, the algorithm focuses on the local structure and clusters are crisp; for high values, the algorithm pays more attention to the global structure, and clusters were found to often overlap. Then, we perform the pairwise comparison of all the variants of 2D representations by RTD and CKA, see Figure 4. RTD reveals a nice monotonic pattern w.r.t. a number of neighbors, while values of CKA are quite chaotic. 

3.3. Experiments with NAS-Bench-NLP 

Figure 5: Multi-dimensional scaling of 90 architectures selected randomly from NAS-Bench-NLP. Color depicts log. perplexity. Recently, neural architecture search has attracted a lot of attention in the machine learning community (Liu et al., 2019; Dong & Yang, 2019; Chen et al., 2021). NAS-Bench-NLP (Klyuchnikov et al., 2020) is a benchmark for neural architecture search which is a collection of 14,322 recurrent architectures; all of the architectures were trained on the PTB dataset. We took 90 randomly selected architectures and compared word embeddings by RTD: each architec-ture contains 400-dimensional embeddings of 10,000 words. Then, we evaluated all the pairwise similarities between embeddings 1 from the architectures and visualized them via multi-dimensional scaling, see Fig. 5, where color depicts a log. perplexity. According to common sense, architectures having similar embeddings have a similar log. perplexity. Also, we checked that RTD is approximately a metric for this particular case since it satisfies the triangle inequality for 97% of triplets of architectures from NAS-Bench-NLP.  

> 1to speedup computation, we averaged the metrics for 10 ran-dom batches of 100 word embeddings. The average relative std. dev. of RTD was 8% .Representation Topology Divergence: a Method for Comparing Neural Network Representations

Table 1: The correlation of metrics with Disagreement in the training dynamics experiment RTD 1−CKA VGG-11 0.976 ± 0.003 0.818 ± 0.010 ResNet-20 0.971 ± 0.001 0.924 ± 0.008 

3.4. Experiments with convolutional neural networks 

To demonstrate the abilities of RTD to work with image representations, we train ResNet-20 (He et al., 2016) and VGG-11 (Simonyan & Zisserman, 2014) networks on CI-FAR (Krizhevsky et al., 2009) datasets. In experiments, we compare RTD with CKA and disagreement of predic-tions. For a more intuitive comparison, we consider 1−CKA instead of CKA. As a measure of the difference in predic-tions, we use Disagreement (Kuncheva & Whitaker, 2003; Wen et al., 2020), the fraction of mismatched predictions calculated as 1

> N

∑Nn=1 [fθ1 (xn) 6 = fθ2 (xn)] , where fθ (x)

denotes the class label predicted by the network for input x.As discussed in (Fort et al., 2019), the lower the accuracy of predictions, the higher its potential mismatch due to the possibility of the wrong answers being random, and then we normalize the Disagreement by (1 − a), where a is the mean accuracy of the predictions. To calculate the final metrics, we averaged the values for five random batches of 500 representations from the test dataset. 3.4.1. T RAINING DYNAMICS 

In the first experiment, we analyze the training dynamics of neural networks. On each epoch, we collect the outputs of the convolutional part that extract the representations. To compare dynamics properly, we scaled the metrics by their maximum value. Fig. 1 shows the dynamics of the differ-ences with the final representations. The results coincide with the intuition: the representations on each epoch become more similar to the final one. Moreover, RTD demonstrates the same behavior as disagreement of predictions. RTD better correlates with the Disagreement, see Table 1. 3.4.2. L AYERS 

In the next experiment, we compare the outputs of layer blocks within the trained network. For VGG-11, the block has the form Conv →BN →Activation →(Pooling), and for ResNet-20, we take the output of the first Conv →BN →Activation block, and then the outputs of each residual block. In Figure 6, we see that both RTD and 

1−CKA show similar results, including the slight difference between adjacent layers. We see that both metrics reveal the significant changes in the outputs of the ResNet-20 last block. In Figure 18, we performed similar experiment with ResNet-50 and ConvNeXt-tiny (Liu et al., 2022) architec-tures pre-trained on ImageNet-1k dataset (Deng et al., 2009). 

Figure 6: The representation differences between the layer blocks within trained networks. The columns correspond to the architecture, and the rows, to the metric. Table 2: Analysis of ResNet-20 representations under differ-ent data distribution shifts. The correlation of metrics with Disagreement. RTD 1−CKA Noise 0.966 ± 0.001 0.927 ± 0.006 Gaussian blur 0.982 ± 0.004 0.913 ± 0.011 Grayscale 0.990 ± 0.004 0.928 ± 0.040 Hue 0.978 ± 0.008 0.927 ± 0.017 3.4.3. D ATA DISTRIBUTION SHIFT 

Here, we apply the data distribution shift to test the RTD. As a shift, we consider different image transformations: nois-ing, blurring, grayscaling, and hue changing. For each trans-formation, we analyze the metric dynamics as the strength of a transformation increases. Figure 7 confirms our san-ity check of the monotony of RTD and other metrics with respect to data distribution shift. Moreover, Table 2 shows that RTD has a higher correlation with disagreement of predictions. 3.4.4. E NSEMBLES 

It is known that an ensemble of neural networks performs better than a single network and can estimate the uncertainty of the predictions. It is shown in (Lee et al., 2015; Opitz et al., 1996) that the diverse ensembles work better. Thus, measuring ensembles’ diversity is important. The disagree-ment is a good example of such a measure. To show that RTD can measure the diversity as well as disagreement, we learn two types of ensembles: the classical ensemble, when we learn the networks from different random initializations, and the Fast Geometric Ensemble (FGE) (Garipov et al., 2018), which is known to have lower diversity. We learn four models for each type of ensemble and average the met-rics among all pairs. The results in Table 3 confirm that RTD is capable of measuring the diversity on the same scale as the disagreement of predictions. Representation Topology Divergence: a Method for Comparing Neural Network Representations    

> (a) Noise (b) Gaussian blur (c) Grayscale (d) Hue

Figure 7: Analysis of ResNet-20 representations under different data distribution shifts. The dynamics of scaled metrics with the monotonic transformations of images. Table 3: The averaged metric among all pairs of ensemble members with a ResNet-20 architecture, and the relative difference between the types of ensemble. Class. Ensemble FGE Diff. % RTD 15.27 ± 0.12 10.45 ± 0.32 31.6 

1−CKA 0.094 ± 0.02 0.033 ± 0.003 64.9 Disagreement 0.915 ± 0.05 0.607 ± 0.03 33.6 

Table 4: The correlation of metrics with Disagreement in the transfer learning experiment RTD 1−CKA CIFAR-100 0.98 ± 0.01 0.93 ± 0.02 CIFAR-10 0.91 ± 0.01 0.89 ± 0.02 3.4.5. T RANSFER LEARNING 

Another possible application is the measure of changes in representations after transferring the pre-trained model to a new task. In this experiment, we conduct the transfer learning from CIFAR-100 to the CIFAR-10 dataset. We make full fine-tuning with the small learning rate for the convolutional part. In Fig. 8, we demonstrate the dynamics for both dataset representations. The results again coincide with the intuition about the difference during the learning steps, and here RTD has also a high correlation with Dis-agreement, see Table 4. Also, we note that RTD can be applied to the continual learning task, where catastrophic forgetting appears, and thus it is crucial to track the changes in network representations. 

3.5. Additional experiments 

We describe how RTD can be used to evaluate a disentan-glement of generative models in Appendix G. Comparisons of BigGAN’s internal representations by RTD agree with those of images by FID, see Appendix E. 

# 4. Conclusions 

In this paper, we have proposed a topologically-inspired approach to compare neural network representations. The most widely used methods for this problem are statistical: Canonical Correlation Analysis (CCA) and Centered Kernel Alignment (CKA). But the problem itself is a geometric one: the comparison of two neural representations of the same objects is de-facto the comparison of two points clouds from different spaces. The natural way is to compare their geo-metrical and topological features with due account of their localization — that is exactly what was done by the R-Cross-Barcode and RTD. We demonstrated that RTD coincides with the natural assessment of representations similarity. We used the RTD to gain insights into neural network repre-sentations in computer vision and NLP domains for various problems: training dynamics analysis, data distribution shift, transfer learning, ensemble learning, and disentanglement assessment. RTD correlates strikingly well with the disagreement of models’ predictions; this is an intriguing topic for further research. Finally, R-Cross-Barcode and RTD are general tools that are not limited only to the comparison of represen-tations. They could be applied to other problems involving comparison of two point clouds with one-to-one correspon-dence, for example, in 3D computer vision. 

Acknowledgements . The work was supported by the An-alytical center under the RF Government (subsidy agree-ment 000000D730321P5Q0002, Grant No. 70-2021-00145 02.11.2021). 

# References 

Barannikov, S. Framed Morse complexes and its invariants. 

Adv. Soviet Math. , 22:93–115, 1994. Barannikov, S. Canonical Forms = Persistence Diagrams. Tutorial. In European Workshop on Computational Ge-ometry (EuroCG 2021) , 2021. Barannikov, S., Trofimov, I., Sotnikov, G., Trimbach, E., Korotin, A., Filippov, A., and Burnaev, E. Manifold Representation Topology Divergence: a Method for Comparing Neural Network Representations 

Figure 8: Scaled metrics demonstrating the difference between representations of CIFAR-100 and CIFAR-10 datasets during fine-tune process. Topology Divergence: a framework for comparing data manifolds. In Proceedings of the 35th International Conference on Neural Information Processing Systems, NeurIPS’21, arXiv:2106.04024 , 2021. Belkin, M. and Niyogi, P. Laplacian eigenmaps and spectral techniques for embedding and clustering. In Proceedings of the 14th International Conference on Neural Infor-mation Processing Systems: Natural and Synthetic , pp. 585–591, 2001. Brock, A., Donahue, J., and Simonyan, K. Large scale gan training for high fidelity natural image synthesis. arXiv preprint arXiv:1809.11096 , 2018. Chazal, F. and Michel, B. An introduction to topological data analysis: fundamental and practical aspects for data scientists. arXiv:1710.04019 , 2017. Chen, W., Gong, X., and Wang, Z. Neural architecture search on imagenet in four gpu hours: A theoretically in-spired perspective. International Conference on Learning Representations , 2021. Connolly, A. C., Guntupalli, J. S., Gors, J., Hanke, M., Halchenko, Y. O., Wu, Y.-C., Abdi, H., and Haxby, J. V. The representation of biological classes in the human brain. Journal of Neuroscience , 32(8):2608–2618, 2012. Deng, J., Dong, W., Socher, R., Li, L.-J., Li, K., and Fei-Fei, L. Imagenet: A large-scale hierarchical image database. In 2009 IEEE conference on computer vision and pattern recognition , pp. 248–255. Ieee, 2009. Dong, X. and Yang, Y. Searching for a robust neural architecture in four gpu hours. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pp. 1761–1770, 2019. Edelman, S. Representation is representation of similarities. 

Behavioral and brain sciences , 21(4):449–467, 1998. Fort, S., Hu, H., and Lakshminarayanan, B. Deep en-sembles: A loss landscape perspective. arXiv preprint arXiv:1912.02757 , 2019. Garipov, T., Izmailov, P., Podoprikhin, D., Vetrov, D., and Wilson, A. G. Loss surfaces, mode connectivity, and fast ensembling of dnns. In Proceedings of the 32nd Inter-national Conference on Neural Information Processing Systems , pp. 8803–8812, 2018. Gelfand, S. I. and Manin, Y. I. Methods of homological algebra . Springer Science & Business Media, 2002. Goodfellow, I., Bengio, Y., Courville, A., and Bengio, Y. 

Deep learning , volume 1. MIT press Cambridge, 2016. Gretton, A., Bousquet, O., Smola, A., and Sch ¨olkopf, B. Measuring statistical dependence with hilbert-schmidt norms. In International conference on algorithmic learn-ing theory , pp. 63–77. Springer, 2005. Hatcher, A. Algebraic topology . 2005. He, K., Zhang, X., Ren, S., and Sun, J. Deep residual learn-ing for image recognition. In Proceedings of the IEEE conference on computer vision and pattern recognition ,pp. 770–778, 2016. Heusel, M., Ramsauer, H., Unterthiner, T., Nessler, B., and Hochreiter, S. Gans trained by a two time-scale update rule converge to a local Nash equilibrium. Advances in neural information processing systems , 30, 2017. Khrulkov, V. and Oseledets, I. Geometry score: A method for comparing generative adversarial networks. In In-ternational Conference on Machine Learning , pp. 2621– 2629. PMLR, 2018. Klyuchnikov, N., Trofimov, I., Artemova, E., Salnikov, M., Fedorov, M., and Burnaev, E. Nas-bench-nlp: neural architecture search benchmark for natural language pro-cessing. arXiv preprint arXiv:2006.07116 , 2020. Representation Topology Divergence: a Method for Comparing Neural Network Representations 

Kornblith, S., Norouzi, M., Lee, H., and Hinton, G. Similar-ity of neural network representations revisited. In Interna-tional Conference on Machine Learning , pp. 3519–3529. PMLR, 2019. Kriegeskorte, N., Mur, M., and Bandettini, P. A. Repre-sentational similarity analysis-connecting the branches of systems neuroscience. Frontiers in systems neuroscience ,2:4, 2008. Krizhevsky, A., Hinton, G., et al. Learning multiple layers of features from tiny images. 2009. Kuncheva, L. I. and Whitaker, C. J. Measures of diversity in classifier ensembles and their relationship with the ensemble accuracy. Machine learning , 51(2):181–207, 2003. Kynk ¨a ¨anniemi, T., Karras, T., Laine, S., Lehtinen, J., and Aila, T. Improved precision and recall metric for assess-ing generative models. In 33rd Conference on Neural Information Processing Systems (NeurIPS 2019) , 2019. Le Peutrec, D., Nier, F., and Viterbo, C. Precise Arrhe-nius law for p-forms: The Witten Laplacian and Morse– Barannikov complex. Annales Henri Poincar ´e, 14(3): 567–610, Apr 2013. ISSN 1424-0661. doi: 10.1007/ s00023-012-0193-9. Lee, S., Purushwalkam, S., Cogswell, M., Crandall, D., and Batra, D. Why m heads are better than one: Training a diverse ensemble of deep networks. arXiv preprint arXiv:1511.06314 , 2015. Li, Y., Yosinski, J., Clune, J., Lipson, H., Hopcroft, J. E., et al. Convergent learning: Do different neural networks learn the same representations? In FE@ NIPS , pp. 196– 212, 2015. Liu, H., Simonyan, K., and Yang, Y. Darts: Differentiable ar-chitecture search. International Conference on Learning Representations , 2019. Liu, Z., Mao, H., Wu, C.-Y., Feichtenhofer, C., Darrell, T., and Xie, S. A convnet for the 2020s. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition , pp. 11976–11986, 2022. McInnes, L., Healy, J., and Melville, J. Umap: Uniform manifold approximation and projection for dimension reduction. arXiv preprint arXiv:1802.03426 , 2018. Moor, M., Horn, M., Rieck, B., and Borgwardt, K. Topo-logical autoencoders. In International Conference on Machine Learning , pp. 7045–7054. PMLR, 2020. Morcos, A. S., Raghu, M., and Bengio, S. Insights on repre-sentational similarity in neural networks with canonical correlation. arXiv preprint arXiv:1806.05759 , 2018. Nguyen, T., Raghu, M., and Kornblith, S. Do wide and deep networks learn the same things? uncovering how neural network representations vary with width and depth. 

International Conference on Learning Representations ,2021. Niyogi, P., Smale, S., and Weinberger, S. Finding the homol-ogy of submanifolds with high confidence from random samples. Discrete & Computational Geometry , 39(1-3): 419–441, 2008. Opitz, D. W., Shavlik, J. W., et al. Generating accurate and diverse members of a neural-network ensemble. Ad-vances in neural information processing systems , pp. 535– 541, 1996. Raghu, A., Raghu, M., Bengio, S., and Vinyals, O. Rapid learning or feature reuse? towards understanding the ef-fectiveness of maml. International Conference on Learn-ing Representations , 2020. Raghu, M., Gilmer, J., Yosinski, J., and Sohl-Dickstein, J. Svcca: Singular vector canonical correlation analysis for deep learning dynamics and interpretability. arXiv preprint arXiv:1706.05806 , 2017. Simonyan, K. and Zisserman, A. Very deep convolu-tional networks for large-scale image recognition. arXiv preprint arXiv:1409.1556 , 2014. Tsitsulin, A., Munkhoeva, M., Mottin, D., Karras, P., Bron-stein, A., Oseledets, I., and Mueller, E. The shape of data: Intrinsic distance for data distributions. In International Conference on Learning Representations , 2020. Voita, E., Sennrich, R., and Titov, I. The bottom-up evolu-tion of representations in the transformer: A study with machine translation and language modeling objectives. 

EMNLP , 2019. Wang, L., Hu, L., Gu, J., Wu, Y., Hu, Z., He, K., and Hopcroft, J. Towards understanding learning representa-tions: To what extent do different neural networks learn the same representation. 32nd Conference on Neural Information Processing Systems (NeurIPS) , 2018. Wen, Y., Tran, D., and Ba, J. Batchensemble: An alterna-tive approach to efficient ensemble and lifelong learning. 

ArXiv , abs/2002.06715, 2020. Whitehead, G. W. Elements of homotopy theory , volume 61. Springer Science & Business Media, 1968. Wu, J. M., Belinkov, Y., Sajjad, H., Durrani, N., Dalvi, F., and Glass, J. Similarity analysis of contextual word representation models. Proceedings of ACL , 2020. Representation Topology Divergence: a Method for Comparing Neural Network Representations 

Zhang, S., Xiao, M., and Wang, H. Gpu-accelerated com-putation of Vietoris-Rips persistence barcodes. In 36th International Symposium on Computational Geometry (SoCG 2020) . Schloss Dagstuhl-Leibniz-Zentrum f¨ ur In-formatik, 2020. Zhou, S., Zelikman, E., Lu, F., Ng, A. Y., Carlsson, G., and Ermon, S. Evaluating the disentanglement of deep generative models through manifold topology. preprint arXiv:2006.03680 , 2020. Zomorodian, A. J. Computing and comprehending topology: Persistence and hierarchical Morse com-plexes (Ph.D.Thesis) . University of Illinois at Urbana-Champaign, 2001. Representation Topology Divergence: a Method for Comparing Neural Network Representations 

# A. Background on Simplicial Complexes. Barcodes 

The simplicial complex is a combinatorial object that can be thought of as a higher-dimensional generalization of a graph. A simplex is defined via the set of its vertices. Given a finite set V , a k−simplex is a finite (k + 1) −element subset in 

V . Simplicial complex S is a collection of k−simplexes, k ≥ 0, which satisfies the natural condition that for each σ ∈ S,

σ′ ⊂ σ implies σ′ ∈ S. A simplicial complex consisting only of 0− and 1−simplexes is a graph. Denote via Ck(S) the vector space over the field Z/2Z = {0, 1} whose basis elements are k−simplexes from S. The boundary linear operator ∂k : Ck(S) → Ck−1(S) is defined on σ = {A0, . . . , A k} as 

∂kσ =

> k

∑

> j=0

{A0, . . . , A j−1, A j+1 , . . . , A k}.

The kth homology group Hk(S) is the factor vector space ker ∂k/ im ∂k+1 . The elements c ∈ ker ∂k are called cycles. The elements of Hk(S) represent various k−dimensional topological features in S. A basis in Hk(S) corresponds to a set of basic topological features. For example, the vector space H0 has the basis whose elements are in one-to-one correspondence with equivalence classes of vertices, connected by paths of 1−simplices (edges), i.e. with connected components of S. The basis elements of the vector space H1 correspond to basic equivalence classes of nontrivial closed paths of 1−simplices. Two closed paths, also named 1−cycles, are equivalent if they are connected by a chain of modifications by boundaries of triangles ( 2−simplices). A map S1 → S2, e.g. Gw≤α → G min( w, ˜w)≤α see section 2.1, defines the maps Hk(S1) → Hk(S2). The kernel of the linear map H0(S1) → H0(S2) is spanned by the pairs of S1 clusters merged together in S2. The cokernel of the linear map 

H1(S1) → H1(S2) consists of 1−cycles in S2 which are not from S1, i.e. it consists of equivalence classes of closed paths in S2, which cannot be modified by boundaries of triangles into images of 1−cycles from S1.In applications, the simplicial complexes are often built via consequential adding of simplexes one after another in increasing order of some numerical characteristics. Mathematically this corresponds to a filtration on the simplicial complex. It is defined as a family of simplicial complexes Sα, indexed by a finite set of real numbers, with nested collections of simplexes: for α1 < α 2 all simplexes of Sα1 are also in Sα2 . An example of a filtered simplicial complex is the Vietoris-Rips simplicial complex from Section 2.2. The inclusions Sα ⊆ Sβ induce the maps on homology Hk(Sα) → Hk(Sβ ). The evolution of cycles across the nested family of simplicial complexes Sαi is described by the principal persistent homology theorem (Barannikov, 1994; Zomorodian, 2001; Le Peutrec et al., 2013), according to which for each dimension there exists a choice of a set of basic topological features across all nested simplicial complexes Sα so that each basic feature c appears in Hk(Sα) at specific time α = bc

and disappears at specific time α = dc. The barcode of the filtered complex is the record of the appearance, or “birth” time, and the disappearance, or “death” time, of all these basic topological features. 

A.1. Exact sequence and topological features 

A sequence of vector spaces and linear maps 

A5

> r4

−→ A4

> r3

−→ A3

> r2

−→ A2

> r1

−→ A1 (3) is exact at Aj if the kernel of the linear map rj−1 coincides with the image of the previous map rj .

Proposition A.1. If the sequence (3) is exact at A2, A 3, A 4 then A3 ' Ker( r1) ⊕ Coker( r4).Proof. Since A/ Ker( r) ' Image( r) for any linear map r : A → A′, therefore A3 ' Image( r2)⊕Ker( r2). If the sequence is exact at A2, then Image( r2) ' Ker( r1). Exactness at A3, A4 gives Ker( r2) ' Image( r3), Ker( r3) ' Image( r4). Then 

Image( r3) ' A4/ Ker( r3) imply that Ker( r2) ' A4/ Image( r4), which equals Coker( r4), the cokernel of the linear map 

r4. Hence A3 ' Ker( r1) ⊕ Coker( r4).Therefore the exact sequence from Theorem 2.1 implies that the calculation of the topological features from Section 2.1 for all α is reduced to the calculation of H1(Rα( ˆGw, ˜w)) for all α, i.e. to the calculation of R-Cross-Barcode 1(P, ˜P ).Representation Topology Divergence: a Method for Comparing Neural Network Representations 

A.2. Construction of R-Cross-Barcode 

Here we gather some intuition behind the construction of the graph ˆGw, ˜w and the R-Cross-Barcode .The Vietoris-Rips complex Rα(Gmin( w, ˜w)) is the union of simplexes whose edges connect data points with distance less than α in at least one of representations P, ˜P. An inclusion of simple simplicial complexes S ⊂ R is an equivalence in homotopy category, if and only if the induced map on homology is an isomorphism (Whitehead, 1968). The maps on homology induced by the inclusions of filtered simplicial complexes 

Rα(Gw) ⊆ Rα(Gmin( w, ˜w)), R α(G ˜w) ⊆ Rα(Gmin( w, ˜w)) (4) should therefore be as close as possible to isomorphisms, in order that the approximations at threshold α to the manifolds 

MP and M ˜P have essentially the same geometric features located at the same places. It follows from the exact sequence from Theorem 2.1 that the R-Cross-Barcode ∗(P, ˜P ) is exactly the list of topological features describing the failure of the maps induced on homology by inclusions (4) to be isomorphisms. Introduce the weighted graph ˆGw with doubled set of vertices and with the edge weights defined as follows. We fix the numbering of vertices Vert (G) = {A1, . . . , A N }. Let us add the extra vertex A′ together with A to ˆGw for each vertex 

A ∈ Vert (G), plus the two additional vertexes O, O ′, and define the distance-like edge weights in ˆGw as: 

dAiAj = dAiA′ 

> j

= wAiAj ,dA′ 

> iA′
> j

= dAiA′ 

> i

= dO′A′ 

> i

= dOA i = 0 , d A′  

> jAi

= dO′Ai = dOA ′ 

> i

= dOO ′ = + ∞ (5) where i < j and O, O ′ ∈ Vert ( ˆGw) are the two additional vertexes. The suspension C[−1] of chain complex C denotes the same chain complex with degree shifted by 1, C[−1] n = Cn−1,so that the the nth chains of Rα(Gw)[ −1] are linear combinations of (n − 1) −dimensional simplexes from Rα(Gw). We denote via Ai1 . . . A in [−1] the element from Cn(Rα(Gw)[ −1]) corresponding to the simplex Ai1 . . . A in .A chain map f between two chain complexes (C, d C ) and (B, d B ) is a sequence of linear maps fn : Cn → Bn that commutes with the boundary operators: dB,n ◦ fn = fn−1 ◦ dC,n . The cone of a chain map f is the chain complex 

Cone( f ) = C[−1] ⊕ B with differential dCone( f ) =

(dC[−1] 0

f [−1] dB

)

. A homotopy equivalence is a pair of chain maps 

f : C → B, g : B → C, and a pair of maps hC,n : Cn → Cn+1 , hB,n : Bn → Bn+1 , such that g ◦ f = Id +[ hC , d C ] and 

f ◦ g = Id +[ hB , d B ]. We assume that the Vietoris-Rips complexes are augmented with C−1 = Z/2Z and ∂0{Ai} = 1 .The proof of the exact homology sequence from Theorem 2.1 follows from the following two propositions. 

Proposition A.2. There are homotopy equivalences of chain complexes: 

Rα(Gw)[ −1] ∼ Rα( ˆGw) (6) 

Cone 

(

Rα(Gw) → Rα(Gmin( w, ˜w))

)

∼ Rα( ˆGw, ˜w). (7) 

Proof. The simplexes of the chain complex Rα( ˆGw) are of four types: Ai1 . . . A ik A′ 

> ik

. . . A ′ 

> in

, Ai1 . . . A ik A′ 

> ik+1

. . . A ′ 

> in

,

OA i1 . . . A in and O′A′ 

> i1

. . . A ′ 

> in

where Aik ∈ Vert (G), i0 < . . . < i k < i k+1 < . . . < i n, with edge weights satisfying 

wAir Ais < α for r ≤ k. Define the map φ : Rα(Gw)[ −1] → Rα( ˆGw)

φ : Ai1 . . . A in [−1] 7 → OA i1 . . . A in + O′A′ 

> i1

. . . A ′ 

> in

+

> n

∑

> k=1

Ai1 . . . A ik A′ 

> ik

. . . A ′ 

> in

(8) The map φ together with the map ˜φ : Rα( ˆGw) → Rα(Gw)[ −1] ˜φ : OA i1 . . . A in 7 → Ai1 . . . A in [−1] , ˜φ(∆) = 0 for any other simplex ∆, (9) gives a homotopy equivalence, ˜φ ◦ φ = Id , φ ◦ ˜φ = Id +[ h, ∂ ], where the homotopy h is given by 

h : Ai1 . . . A ik A′ 

> ik+1

. . . A ′ 

> in

7 →

> k

∑

> l=1

Ai1 . . . A il A′ 

> il

. . . A ′ 

> in

+ O′A′ 

> i1

. . . A ′ 

> in

(10) 

h : A′ 

> i1

. . . A ′ 

> in

7 → O′A′ 

> i1

. . . A ′ 

> in

, h (∆) = 0 for any other simplex ∆.Representation Topology Divergence: a Method for Comparing Neural Network Representations 

Simplexes of the chain complex Rα( ˆGw, ˜w) are of three types. The first type: Ai1 . . . A ik A′ 

> ik

. . . A ′ 

> in

with edge weights satisfying wAir Ais < α for r ≤ k and min( wAir Ais , ˜wAir Ais ) < α for r, s > k; the second type: 

Ai1 . . . A ik−1 A′ 

> ik

. . . A ′ 

> in

with edge weights satisfying wAir Ais < α for r < k , and min( wAir Ais , ˜wAir Ais ) < α for 

r, s ≥ k; and the third type: OA i1 . . . A in with edge weights satisfying wAir Ais < α for all r, s . Define the map 

ψ : Cone (Rα(Gw) → Rα(Gmin( w, ˜w))) → Rα( ˆGw, ˜w)

ψ : Ai1 . . . A in [−1] 7 → OA i1 . . . A in +

> n

∑

> k=1

Ai1 . . . A ik A′ 

> ik

. . . A ′ 

> in

(11) for Ai1 . . . A in [−1] ∈ Rα(Gw)[ −1] ,

ψ : Ai1 . . . A in 7 → A′ 

> i1

. . . A ′ 

> in

(12) for Ai1 . . . A in ∈ Rα(Gmin( w, ˜w)). The map ψ together with the map ˜ψ : Rα( ˆGw, ˜w) → Cone (Rα(Gw) → Rα(Gmin( w, ˜w)))

˜ψ : OA i1 . . . A in 7 → Ai1 . . . A in [−1] , A i1 . . . A in [−1] ∈ Rα(Gw)[ −1] ,A′ 

> i1

. . . A ′ 

> in

7 → Ai1 . . . A in , A i1 . . . A in ∈ Rα(Gmin( w, ˜w)), (13) 

˜ψ(∆) = 0 for any other simplex ∆,

gives a homotopy equivalence, ˜ψ ◦ ψ = Id , ψ ◦ ˜ψ = Id +[ H, ∂ ], where the homotopy H is given by 

H : Ai1 . . . A ik A′ 

> ik+1

. . . A ′ 

> in

7 →

> k

∑

> l=1

Ai1 . . . A il A′ 

> il

. . . A ′ 

> in

, 1 ≤ k ≤ n (14) 

H(∆) = 0 for any other simplex ∆.

The long exact sequences such as (2) arise from distinguished triangles in the homotopy category of chain complexes. A distinguished triangle is a diagram isomorphic in this category to a diagram A f

−→B → Cone( f ) → A[−1] .

Proposition A.3. The embeddings of graphs Gw≤α ⊆ G min( w, ˜w)≤α ⊂ ˆGw, ˜w≤α give distinguished triangles, see (Gelfand & Manin, 2002), in the homotopy category of chain complexes: 

Rα(Gw) → Rα(Gmin( w, ˜w)) → Rα( ˆGw, ˜w) → Rα(Gw)[ −1] . (15) 

Proof. Taken together the homotopy equivalences (8)-(14) define an isomorphism of (15) with the distinguished triangle 

Rα(Gw) → Rα(Gmin( w, ˜w)) → Cone 

(

Rα(Gw) → Rα(Gmin( w, ˜w))

)

→ Rα(Gw)[ −1] . (16) 

Comparison with Cross-Barcode and Geometry Score. The Cross-Barcode from (Barannikov et al., 2021) compares two data manifolds lying in the same ambient space. It does not use the information that can be provided by a one-to-one correspondence between points of the two data clouds. To compare the locations of topological features the Cross-Barcode from loc.cit. uses instead the proximity information inferred from the pairwise distances between points from different clouds lying in the same ambient space. Geometry score from (Khrulkov & Oseledets, 2018) is based on a comparison of standard barcodes for each cloud and is insensitive to the location of topological features, for example, it does not detect any difference when similar topological features are located geometrically in distant places of the two clouds. Representation Topology Divergence: a Method for Comparing Neural Network Representations 

Figure 9: Merging between clusters already connected via a chain of mergings. 

Figure 10: Merging of three clusters into two clusters. Graphs Gw≤α, G ˜w≤α and Gmin( w, ˜w)≤α are shown. Edges of 

Gmin( w, ˜w)≤α not in Gw≤α are colored in green. In this example there are exactly four different weights (13) , (14) , (23) , (24) 

in the graphs Gw≤α and Gmin( w, ˜w)≤α. The unique topological feature in R-Cross-Barcode 1(P, ˜P ) in this case is born at the threshold ˜w24 when the difference in the cluster structures of the two graphs arises, as the points 2 and 4 are in the same cluster at this threshold in Gmin( w, ˜w) and not in Gw. This feature dies at the threshold w23 since the clusters containing 2

and 4 are merged at this threshold in Gw.

# B. Discussion of CKA 

Given two series of equal size xi ∈ Rnx , yi ∈ Rny , i = 1 . . . n the CKA (Kornblith et al., 2019) is defined as CKA (K, L ) = HSIC (K, L )

√HSIC (K, K )HSIC (L, L )

where HSIC (K, L ) is a Hilbert-Schmidt Independence Criterion (Gretton et al., 2005), Ki,j = k(xi, x j ), Li,j = l(yi, y j ),

L = E − n−1 where k(·, ·), l(·, ·) are kernels. HSIC itself an empirical estimate of the Hilbert-Schmidt norm of the cross-covariance operator. HSIC is equivalent to maximum mean discrepancy between the joint distribution P (X, Y ) and the product of the marginal distributions P (X)P (Y ); HSIC = 0 implies independence of X and Y if the associated kernel is universal. However, CKA is sometimes applied to measure similarity between representations from different layers of a neural network. In this case Y = f (X). X and Y are tightly dependent and the joint distribution can always be factorized as Representation Topology Divergence: a Method for Comparing Neural Network Representations 

P (X, Y ) = P (Y |X)P (X). Thus, the application of CKA to the comparison of representation from different layers is questionable. 

# C. Details on experiments with synthetic point clouds 

Figure 11: R-Cross-Barcodes for the “clusters” experiments. Top: R-Cross-Barcode ( ˜P , P ), Bottom: R-Cross-Barcode (P, ˜P ); ˜P is the point cloud having one cluster; P - 2, 3, 4, 5, 6, 10, 12 clusters. 

Runtime comparison . Here we present the total wall time of the experiments with synthetic point clouds: “Clusters experiment”: RTD: 19.7 s, CKA: 0.07 s, IMD: 83 s, SVCCA: 0.03 s. “Rings experiment”: RTD: 144 s, CKA: 0.7 s, IMD: 91 s, SVCCA: 0.6 s. 

# D. Details on the “rings” experiment 

> (a) Point clouds used in “rings” experiment.
> (b) Representations’ comparison measures. Ideally, the measure should change monotonically with the increase of topological discrepancy.

Figure 12: RTD perfectly detects changes in topology, while rival measures fail. Five rings are compared with 5,4,3,2,1 rings. 

# E. Experiment with BigGAN 

In this experiment, we applied RTD and CKA for comparison of internal representations in BigGAN (Brock et al., 2018) 2.Initially, we generated a set of k = 100 random latent codes Z0 = {z0,j }kj=1 and derived sets Z1, . . . , Z n by adding to Z0 aGaussian noise of increasing strength zi,j = z0,j + i,j , where i,j ∼ N (0 , σ i). The noise standard deviation σi grows from 

0.001 to 0.25 by a logarithmic scale and the difference between Z0 and Zi tends to increase when i increases. 

> 2we used the pretrained model from
> https://github.com/lukemelas/pytorch-pretrained-gans Representation Topology Divergence: a Method for Comparing Neural Network Representations

Figure 13: R-Cross-Barcodes for the “rings” experiments. Top: R-Cross-Barcode (P, ˜P ), Bottom: R-Cross-Barcode ( ˜P , P ).

P - is the point cloud having 5 rings, ˜P - 4, 3, 2, 1 rings. 

Figure 14: Comparison of normalized RTD, CKA (computed for sets of internal representations) vs. FID (computed for sets of images). Then, we pass sets of latent codes Z0, . . . , Z n together with vector encoding of the “husky” class through the BigGAN and save internal representations Ri for one of the top layers (results were quite similar for other layers). Also, we get sets of images I0, . . . , I k. To compare these sets we used the state-of-the-art measure FID (Heusel et al., 2017) which is often applied for GAN evaluation. It is natural to assume that the difference between sets of internal representations R0 and Ri should have a good correlation with the difference between sets of images I0 and Ii. To check this hypothesis, we calculated RTD( R0, Ri), CKA( R0, Ri)and compared them with FID( I0, Ii), for i = 1 , . . . , n . Figure 14 shows the results. We conclude that RTD enjoys higher correlation with FID: 0.97, while the correlation of CKA and FID is lower: 0.79. 

# F. Details on experiments with convolutional networks 

Metrics to correlate Noise Gaussian Blur Grayscale Hue Disagreement RTD 0.966 ± 0.001 0.982 ± 0.004 0.990 ± 0.004 0.978 ± 0.008 

1−CKA 0.927 ± 0.006 0.913 ± 0.011 0.928 ± 0.040 0.927 ± 0.017 Error rate RTD 0.982 ± 0.002 0.963 ± 0.007 0.856 ± 0.052 0.935 ± 0.030 

1−CKA 0.966 ± 0.007 0.999 ± 0.001 0.958 ± 0.018 0.944 ± 0.033 

Table 5: Analysis of ResNet-20 representations under different data distribution shifts. The correlation of RTD and 1−CKA with Disagreement and Error rate. Representation Topology Divergence: a Method for Comparing Neural Network Representations    

> (a) Zoom (b) Contrast (c) Brightness (d) Rotation

Figure 15: Analysis of ResNet-20 representations under different data distribution shifts. The dynamics of scaled metrics with the monotonic application of various types of image transformations. Metrics to correlate Zoom Brightness Contrast Rotation Disagreement RTD 0.950 ± 0.006 0.975 ± 0.002 0.936 ± 0.010 0.955 ± 0.015 

1−CKA 0.886 ± 0.010 0.854 ± 0.024 0.851 ± 0.021 0.857 ± 0.020 Error rate RTD 0.946 ± 0.006 0.921 ± 0.011 0.937 ± 0.005 0.940 ± 0.009 

1−CKA 0.994 ± 0.002 0.997 ± 0.001 0.998 ± 0.001 0.981 ± 0.005 

Table 6: Analysis of ResNet-20 representations under different data distribution shifts. The correlation of RTD and 1−CKA with Disagreement and Error rate. 

# G. Experiments with disentanglement 

Learning disentangled representations is a fundamental problem for improving the generalization, robustness, and inter-pretability of generative models. (Zhou et al., 2020) proposed to evaluate the disentanglement of generative models by comparing the topology of data manifold slices. Let Z be a latent space, X - a space of objects, g : Z → X - a generator. (Zhou et al., 2020) compares slices Xv = g(Z |zi=v ) for different values of v. If the direction zi corresponds to an interpretable factor, then Xv must be topologically similar for different v.We use the following experimental design. Zv,n = {z ∈ Z | (z, n ) = v} - a slice in a latent space orthogonal to a unit vector n. We take a finite random sample Z1 ⊂ Zv,n and a shifted sample Z2 = {zi + δn }|Z1| 

> i=1

for small δ. By definition, 

Z1 and Z2 have natural point-wise mapping and we can estimate homological similarity of g(Z1) and g(Z2) by RTD. In this experiment, we use dSprites 3 for the evaluation of disentanglement. dSprites is a dataset of procedurally generated 2D shapes from 5 ground truth independent latent factors: shape, scale, rotation, x-position, and y-position of a sprite. Thus, the latent space is disentangled and fully factorized. Particularly, we compare the slices orthogonal to axis-aligned vectors and orthogonal to random vectors, see Table 10. Except for the first axis, the topological dissimilarity estimated by RTD is significantly less than for a random direction. The first axis corresponds to a categorical factor - shape for which the aforementioned approach is arguably not applicable. The dSprites dataset is quite simple and RTD was calculated for point clouds in the pixel space. However, the same technique can be straightforwardly applied to evaluate the disentanglement of image representations for more complex datasets. RTD 1−CKA Disagreement 0.98 ± 0.01 0.93 ± 0.02 Error rate 0.9 ± 0.03 0.99 ± 0.01 

> (a) CIFAR-100

RTD 1−CKA Disagreement 0.91 ± 0.01 0.89 ± 0.02 Error rate 0.60 ± 0.02 0.73 ± 0.01 

> (b) CIFAR-10

Table 7: The correlation of metric dynamics when transferring the ResNet-20 network from CIFAR-100 to CIFAR-10 dataset. Representation Topology Divergence: a Method for Comparing Neural Network Representations 

VGG-11 ResNet-20 Number of epochs 100 Optimizer SGD, momentum=0.9 Learning rate (initial) 0.1 Scheduler 

<50%: 0.1 50-90%: 0.1-0.001 (linear) 

>90%: 0.001 Batch size 128 Table 8: Details on learning the neural networks from random initialization on CIFAR datasets. Encoder part Classifier part Number of epochs 50 Optimizer SGD, momentum=0.9 Learning rate (initial) 0.001 0.1 Scheduler None 

<50%: 0.1 50-90%: 0.1-0.001 (linear) 

>90%: 0.001 Batch size 128 Table 9: Details on fine-tuning the ResNet-20 from CIFAR-100 to CIFAR-10 dataset. 

# H. Details on dimensionality reduction of MNIST with UMAP 

Visual inspection of Figure 17 reveals apparent incoherences of CKA. Denote by U (n) representations obtained by UMAP with the number of neighbors n. According to CKA (Figure 4b), U (10) is closer to U (200) than to U (20) ; also U (200) is closer to U (10) than to U (100) .

# I. Additional experiments 

For the “clusters” experiments, we did additional comparisons of point clouds with alternative similarity measures. Firstly, we calculated CKA with the RBF kernel for 3 bandwidths equal to 0.2, 0.4, 0.8 of median pairwise distances (as proposed in (Kornblith et al., 2019)). The performance as measured by Kendall-tau correlation with the true ordering was 0.23, 0.04, 0.14 - not better than for CKA with the linear kernel. Secondly, we applied the topological loss term from (Moor et al., 2020). The performance as measured by Kendall-tau correlation with the true ordering was poor: -0.52. 

# J. Internal similarity of Neural Network layers 

Here we compare the outputs of layer blocks within the trained network. We consider ResNet-50 and ConvNeXt-tiny (Liu et al., 2022) architectures pre-trained on ImageNet-1k dataset (Deng et al., 2009). We calculate RTD, CKA and SVCCA within outputs after each Bottleneck Residual Block or ConvNeXt’s block respectively. In Fig. 18, we plot similarity 

> 3https://github.com/deepmind/dsprites-dataset

Table 10: Evaluation of the disentanglement for various directions in the latent space of dSprites .

axis RTD 

axis 1 148.1 axis 2 71.3 axis 3 53.4 axis 4 41.2 axis 5 40.5 random 162 .8 ± 18 .6Representation Topology Divergence: a Method for Comparing Neural Network Representations 

Figure 16: dSprites generated across directions in the latent space, top: random direction, bottom: axis-aligned direction, corresponds to an interpretable factor of variation. 

Figure 17: 2D representations of MNIST produced by UMAP, n neighbors ∈ (10 , 20 , 50 , 100 , 200) 

between layers within each architecture. We observe that RTD catches architecture’s block structure better than CKA, SVCCA. The ResNet-50 architecture has sequence of blocks in form [3, 4, 6, 3] and it can be seen that RTD highlights it with sub-squares of corresponding sizes. 

Figure 18: The representation differences between the layer blocks within trained networks, ImageNet-1k dataset. The columns correspond to the metrics, and the rows – to the architectures.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="the-platonic-representation-hypothesis.md">
<details>
<summary>How to measure if representations are converging?</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://phillipi.github.io/prh>

https://phillipi.github.io/prh/images/platonic_rep_less_space_v2.jpg

The world (Z) can be viewed in many different ways: in images (X), in text (Y), etc. We conjecture that representations learned on each
modality on its own will converge to similar representations of Z.

Conventionally, different AI systems represent the world in different ways. A vision system might represent shapes and colors,
a language model might focus on syntax and semantics. However, in recent years, the architectures and objectives
for modeling images and text, and many other signals, are becoming remarkably alike. **Are the internal representations in these**
**systems also converging?**

We argue that they are, and put forth the following hypothesis:

Neural networks, trained with different objectives on different data and modalities,
are converging to a shared statistical model of reality in their representation spaces.

The intuition behind our hypothesis is that all the data we consume -- images, text, sounds, etc -- are projections of
some underlying reality. A concept like

"apple"
     🍎

can be viewed in many
different ways but the meaning, what is represented, is roughly\* the same. Representation learning algorithms might recover
this shared meaning.

\* Not _exactly_ the same. The text "apple" does not tell whether the fruit is red or green, but an image can.
Sufficiently descriptive text is necessary. See the limitations section of our paper for discussion of this point.

# How to measure if representations are converging?

We characterize representations in terms of their _kernels_, i.e. how they measure distance/similarity between inputs.
Two representations are considered the same if their kernels are the same for corresponding inputs. We then say the
representations are _aligned_.
For example, if a text encoder
ftext
is aligned with an image encoder fimg,
then we would have relationships like:

sim(ftext("apple"), ftext("orange"))   ≈   sim(fimg(🍎), fimg(🍊))

\[
\text{sim}(f_{\text{text}}(\text{“apple"}), f_{\text{text}}(\text{“orange"})) \quad\approx\quad \text{sim}(f_{\text{img}}(\text{🍎}), f_{\text{img}}(\text{🍊}))
\]

Kernel _alignment metrics_ quantify the degree to which statements like the above are true, and we use these metrics to analyze if representations in different models are converging.
Check out our [code](https://github.com/minyoungg/platonic-rep) for implementations of such metrics, including several new ones we introduce.

# Evidence of convergence

We survey many examples of convergence in the literature: over time and across multiple domains, the ways by which different neural networks represent data are becoming more aligned.
Then, we demonstrate convergence across data modalities: as vision models and language models get larger, they measure distance between datapoints in a more and more alike way:

Scatterplot with Voronoi

0.000.100.200.300.400.500.100.110.120.130.140.150.160.170.18LANGUAGE modeling score (1 - bits-per-byte)Alignment to VISION (kernel alignment to DINOv2)

Model family

BloomOpenLlamaLlamaOLMoGemmaMistralLlama3Parameters7 B30 B70 B

As LLMs get better at language modeling, they learn representations that are more and more aligned with vision models (and conversely, bigger vision models are also better aligned with LLM embeddings).
Plotted using [voronoi](https://www.visualcinnamon.com/2015/07/voronoi/).

# What is driving convergence?

We argue that task and data pressures, combined with increasing model capacity, can lead to convergence. One such pressure is visualized below:
As we train models on more tasks, there are fewer representations that can satisfy our demands. As models become more
general-purpose, they become more alike:

The more tasks we must solve, the fewer functions satisfy them all. [Cao & Yamins](https://arxiv.org/abs/2104.01489) term this the "Contravariance principle."

# What representation are we converging to?

In a particular idealized world, we show that a certain family of learners will converge to a representation whose kernel is equal to the pointwise mutual information (PMI) function
over the underlying events (Z) that cause our observations, regardless of modality. For example, in a world of colors, where events
zred and zorange
generate visual and textual observations, we would have:

sim(f(

"red"

🟥

), f(

"orange"

🟧

))   =   PMI(zred, zorange) + const

\[
\text{sim}(f_{\text{text}}(\text{red"}), f_{\text{text}}(\text{“orange"})) \quad=\quad \text{PMI}(z_{\text{red}}, z_{\text{orange}}) + \text{const}
\]
\[
\text{sim}(f(\color{red}{\blacksquare}\color{black}), f(\color{orange}{\blacksquare}\color{black})) \quad=\quad \text{PMI}(z_{\text{red}}, z_{\text{orange}}) + \text{const}
\]

This analysis makes various assumptions and should be read as a starting point for a fuller theory. Nonetheless, empirically, we do find that
PMI over pixel colors recovers a similar kernel to human perception of colors, and this is also similar to the kernel that LLMs recover:

This analysis suggests that certain representation learning algorithms may boil down to a simple rule: _find an embedding in which similarity equals pointwise mutual information._

https://phillipi.github.io/prh/images/color-study.png

Kernels visualized with multidimensional scaling (i.e. a visualization where nearby points are similar according to the kernel, and far apart points are dissimilar).
The language experiment here is a replication of [Abdou et al. 2021](https://arxiv.org/abs/2109.06129).

# Implications and limitations

The final sections of our paper discuss implications and limitations of the hypothesis. Perhaps the primary implication is this: if there is indeed a platonic representation,
then finding it, and fully characterizing it, is a research program worth pursuing.

However, like any good hypothesis, there are also numerous counterarguments one can make:
what about the knowledge that is _unique_ to each model and modality? What about specialist systems, that don't require general-purpose world representations?
We hope this work sparks vigorous debate.

Other works that have made similar arguments:

\[1\] [Allegory of the Cave](https://en.wikipedia.org/wiki/Allegory_of_the_cave), Plato, c. 375 BC

\[2\] [Three Kinds of Scientific Realism](https://www.jstor.org/stable/2219323), Putnam, The Philosophical Quarterly, 1982

\[3\] [Contrastive Learning Inverts the Data Generating Process](https://arxiv.org/abs/2102.08850), Zimmermann, Sharma, Schneider, Bethge, Brendel, ICML 2021

\[4\] [Revisiting Model Stitching to Compare Neural Representations](https://arxiv.org/abs/2106.07682), Yamini Bansal, Preetum Nakkiran, Boaz Barak, NeurIPS 2021

\[5\] [Can Language Models Encode Perceptual Structure Without Grounding? A Case Study in Color](https://arxiv.org/abs/2109.06129), Abdou, Kulmizev, Hershcovich, Frank, Pavlik, Søgaard, CoNLL 2021

\[6\] [Explanatory models in neuroscience: Part 2 -- Constraint-based intelligibility](https://arxiv.org/abs/2104.01489), Cao, Yamins, Cognitive Systems Research, 2024

\[7\] [Robust agents learn causal world models](https://arxiv.org/abs/2402.10877), Jonathan Richens, Tom Everitt, ICLR 2024

Plato imagined an "ideal" reality of which our observations are mere shadows. Putnam and others developed the idea of "convergent realism": scientists,
via observation, converge on truth; our position is that deep nets work similarly. Zimmermann et al., Richens and Everitt, and many others have argued
that certain representation learners recover statistical models of the latent causes of our observations.
Bansal et al. hypothesized an "Anna Karenina scenario," in which all well-performing neural nets are alike. Abdou et al. showed that LLMs learn
visual similarities from text alone (an experiment we have replicated). Cao and Yamins argue for a "Contravariance Principle," by which
models and minds become aligned when tasked to solve hard problems. This is a curated list of close work. Please see our paper for more.

</details>

</research_source>

<golden_source type="guideline_code">
## Code Sources (from Article Guidelines)

_No guideline code sources found._

</golden_source>

<golden_source type="guideline_youtube">
## YouTube Video Transcripts (from Article Guidelines)

_No guideline YouTube video transcripts found._

</golden_source>

<golden_source type="guideline_urls">
## Additional Sources Scraped (from Article Guidelines)

_No additional guideline sources scraped._

</golden_source>

<research_source type="guideline_exploitation" phase="exploitation">
## Exploitation Sources (from Article Guidelines — Other Sources)

_No exploitation guideline sources found._

</research_source>

<golden_source type="local_files">
## Local File Sources (from Article Guidelines)

<details>
<summary><span id="page-0-1"></span>The Platonic Representation Hypothesis</summary>

# <span id="page-0-1"></span>The Platonic Representation Hypothesis

Minyoung Huh \* 1 Brian Cheung \* 1 Tongzhou Wang \* 1 Phillip Isola \* 1

# Abstract

We argue that representations in AI models, particularly deep networks, are converging. First, we survey many examples of convergence in the literature: over time and across multiple domains, the ways by which different neural networks represent data are becoming more aligned. Next, we demonstrate convergence across data modalities: as vision models and language models get larger, they measure distance between datapoints in a more and more alike way. We hypothesize that this convergence is driving toward a shared statistical model of reality, akin to Plato's concept of an ideal reality. We term such a representation the *platonic representation* and discuss several possible selective pressures toward it. Finally, we discuss the implications of these trends, their limitations, and counterexamples to our analysis.

Project Page: [phillipi.github.io/prh](https://phillipi.github.io/prh/) Code: [github.com/minyoungg/platonic-rep](https://github.com/minyoungg/platonic-rep/)

# 1. Introduction

AI systems are rapidly evolving into highly multifunctional entities. For example, whereas in the past we had specialpurpose solutions for different language processing tasks (*e.g.*, sentiment analysis, parsing, dialogue), modern large language models (LLMs) are competent at all these tasks using a single set of weights [\(Srivastava et al.,](#page-14-0) [2022\)](#page-14-0). Unified systems are also being built across data modalities: instead of using a different architecture for processing images versus text, recent models, such as GPT4-V [\(Ope](#page-13-0)[nAI,](#page-13-0) [2023\)](#page-13-0), Gemini [\(Google,](#page-11-0) [2023\)](#page-11-0), and LLaVA [\(Liu et al.,](#page-13-1) [2023\)](#page-13-1), handle both modalities with a combined architecture. More and more systems are built off of general-purpose pretrained backbones, sometimes called foundation models [\(Bommasani et al.,](#page-10-0) [2021\)](#page-10-0), that support a large range of tasks, including robotics [\(Driess et al.,](#page-11-1) [2023;](#page-11-1) [Brohan](#page-10-1)

*Proceedings of the* 41 st *[International Conference on Machine](#page-10-1) Learning*[, Vienna, Austria. PMLR 235, 2024. Copyright 2024 by](#page-10-1) [the author\(s\).](#page-10-1)

## The Platonic Representation Hypothesis

Neural networks, trained with different objectives on different data and modalities, are converging to a shared statistical model of reality in their representation spaces.

![](_page_0_Figure_12.jpeg)

<span id="page-0-0"></span>Figure 1. The Platonic Representation Hypothesis: Images (X) and text (Y ) are projections of a common underlying reality (Z). We conjecture that representation learning algorithms will converge on a shared representation of Z, and scaling model size, as well as data and task diversity, drives this convergence.

[et al.,](#page-10-1) [2023\)](#page-10-1), bioinformatics [\(Ma et al.,](#page-13-2) [2024\)](#page-13-2), and healthcare [\(Steinberg et al.,](#page-14-1) [2021\)](#page-14-1). In short, AI systems are becoming increasingly homogeneous in both their architectures and their capabilities.

This paper explores one aspect of this trend: representational convergence. We argue that there is a growing similarity in how datapoints are represented in different neural network models. This similarity spans across different model architectures, training objectives, and even data modalities.

What has led to this convergence? Will it continue? And ultimately, where does it end?

Our central hypothesis, stated above in Figure [1,](#page-0-0) is that there is indeed an endpoint to this convergence and a principle that drives it: different models are all trying to arrive at a

<sup>\*</sup>Equal contribution <sup>1</sup>[MIT. Correspondence to: Minyoung Huh](#page-10-1) <[minhuh@mit.edu](#page-10-1)>.

*representation of reality*, meaning a representation of the joint distribution over events in the world that generate the data we observe. Figure [1](#page-0-0) conveys this hypothesis: there exists a real world (labeled Z), which we measure with various sensors, such as the camera shown to the left (X). Other *projections* of these measurements, such as the textual description shown, can be produced from the first set of measurements or mediated by some other set of measurements, *e.g.*, touch or other camera views (dotted arrow from X to Y ) [1](#page-0-1) . Representation learning algorithms find vector embeddings that statistically model the various measurements and projections. The resulting vector embeddings are all derived from the underlying reality in Z and thereby become aligned. As models are trained on more data and for more tasks, they require representations that capture more and more information about Z, and hence alignment toward Z increases toward a convergent point as a function of scale.

We call this converged hypothetical representation the "platonic representation" in reference to Plato's Allegory of the Cave [\(Plato,](#page-14-2) [c. 375 BC\)](#page-14-2), and his idea of an ideal reality that underlies our sensations. The training data for our algorithms are shadows on the cave wall, yet, we hypothesize, models are recovering ever better representations of the actual world outside the cave. This idea is not unique to Plato; our hypothesis is also related to the notion of "convergent realism" [\(Newton-Smith,](#page-13-3) [1981;](#page-13-3) [Putnam,](#page-14-3) [1982;](#page-14-3) [Doppelt,](#page-11-2) [2007;](#page-11-2) [Hardin & Rosenberg,](#page-11-3) [1982\)](#page-11-3) in the philosophy of science (*i.e.*, that science is converging on truth), and to many arguments that have been put forth in the representation learning literature (*e.g.*, [Tian et al.](#page-15-0) [\(2020a\)](#page-15-0); [Zimmermann et al.](#page-16-0) [\(2021\)](#page-16-0); [Richens & Everitt](#page-14-4) [\(2024\)](#page-14-4); [Cao & Yamins](#page-10-2) [\(2024\)](#page-10-2)).

Also closely related to our hypothesis is the "Anna Karenina scenario" described by [Bansal et al.](#page-10-3) [\(2021\)](#page-10-3), referring to the possibility that all well-performing neural nets represent the world in the same way. We discuss the evidence they give for this possibility in Section [2](#page-1-0) . The platonic representation hypothesis refers to the situation where we are in an Anna Karenina scenario *and* the "happy representation" that is converged upon is one that reflects a statistical model of the underlying reality. We discuss the potential nature of this statistical model in more detail in Section [4.](#page-6-0)

# <span id="page-1-0"></span>2. Representations are converging

Preliminaries We restrict our attention to representations that are *vector embeddings*. We characterize such a repre-

sentation by the similarity structure it induces, referred to as its kernel. Kernels are commonly used to assess representations [\(Kornblith et al.,](#page-12-0) [2019;](#page-12-0) [Klabunde et al.,](#page-12-1) [2023\)](#page-12-1); this can be justified by the fact that they capture the relative structures among data samples, which are also the learning signal for many machine learning algorithms [\(Aronszajn,](#page-10-4) [1950;](#page-10-4) [Smola & Scholkopf](#page-14-5) ¨ , [1998\)](#page-14-5). Following prior literature, we define *representational alignment* as a measure of the similarity of the similarity structures induced by two representations, *i.e.*, a similarity metric over kernels. We give the mathematical definition of these concepts below:

- A representation is a function f : X → **R** <sup>n</sup> that assigns a feature vector to each input in some data domain X .
- A kernel, K : X × X → **R**, characterizes how a representation measures distance/similarity between datapoints. K(x<sup>i</sup> , x<sup>j</sup> ) = ⟨f(xi), f(x<sup>j</sup> )⟩, where ⟨ · , · ⟩ denotes inner product, x<sup>i</sup> , x<sup>j</sup> ∈ X and K ∈ K.
- A kernel-alignment metric, m: K × K → **R**, measures the similarity between two kernels, *i.e.*, how similar is the distance measure induced by one representation to the distance measure induced by another. Examples include Centered Kernel Distance (CKA) [\(Kornblith et al.,](#page-12-0) [2019\)](#page-12-0), SVCCA [\(Raghu et al.,](#page-14-6) [2017\)](#page-14-6), and nearest-neighbor metrics [\(Klabunde et al.,](#page-12-1) [2023\)](#page-12-1).

In our experiments, we use a *mutual nearest-neighbor metric* that measures the mean intersection of the k-nearest neighbor sets induced by two kernels, K<sup>1</sup> and K2, normalized by k. This metric is a variant of those proposed in [Park](#page-14-7) [et al.](#page-14-7) [\(2024\)](#page-14-7), [Klabunde et al.](#page-12-1) [\(2023\)](#page-12-1) and [Oron et al.](#page-14-8) [\(2017\)](#page-14-8). See Appendix [A](#page-17-0) for the exact definition and Appendix [B](#page-19-0) for comparisons with alternative alignment metrics.

Next, we explore several ways in which representations are converging. First, we argue that different neural networks are converging to aligned representations. Then, we show that this continues to hold across modalities, where image embeddings in vision models align with text embeddings in language models.

## 2.1. Different models, with different architectures and objectives, can have aligned representations

One indication of representational convergence is the rising number of systems built on top of pre-trained foundation models. These models are becoming standard backbones across a growing spectrum of tasks. Their versatility across numerous applications implies a level of universality in the way they represent data.

While this trend implies convergence toward a relatively small set of foundation models, it does not imply that *different* foundation models will arrive at the same representation. Yet that is what has been observed by several recent papers.

[Lenc & Vedaldi](#page-12-2) [\(2015\)](#page-12-2) conducted one such study, in which

<sup>1</sup>Touch could convey the shapes in this example but not the colors. This is an important limitation to our hypothesis that we discuss at several points in the paper: different sensors and views might capture different information, which may limit their potential to converge to identical representations.

<sup>2</sup>Borrowed from [Tolstoy](#page-15-1) [\(1877\)](#page-15-1), similar analogies have been made in other domains, such as the "Anna Karenina principle" popularized by [Diamond](#page-11-4) [\(1998\)](#page-11-4) to explain animal domestication.

![](_page_2_Figure_1.jpeg)

<span id="page-2-0"></span>Figure 2. VISION models converge as COM-PETENCE increases: We measure alignment among 78 models using mutual nearest-neighbors on Places-365 (Zhou et al., 2017), and evaluate their performance on downstream tasks from the Visual Task Adaptation Benchmark (VTAB; Zhai et al. (2019)). LEFT: Models that solve more VTAB tasks tend to be more aligned with each other. Error bars show standard error. RIGHT: We use UMAP to embed models into a 2D space, based on distance ≜ − log(alignment). More competent and general models (blue) have more similar representations.

they measured representational similarity through a technique called *model stitching*. Given two models, f and g, each composed of multiple layers ( $f = f_1 \circ \cdots \circ f_n$ ,  $g = g_1 \circ \cdots \circ g_m$ ), an intermediate representation from f is integrated into g via a learned affine stitching layer h, resulting in a new stitched model  $F = f_1 \circ \cdots \circ f_k \circ h \circ g_{k+1} \circ \cdots \circ g_m$ . If F has good performance, it indicates that f and g have compatible representations at layer k, up to the transform h.

In their study, Lenc & Vedaldi (2015) made two notable findings: (1) A vision model trained on ImageNet (Russakovsky et al., 2015) can be aligned with a model trained on Places-365 (Zhou et al., 2017) while maintaining good performance; (2) The early layers of these convolutional networks are more interchangeable than later layers. The first finding illustrates a level of data independence where distinct image datasets lead to similar representations. The second finding agrees with extensive research that oriented Gabor-like filters are common in both artificial and biological vision systems. This suggests a convergence to a similar initial layer of representation across various neural network architectures (Olshausen & Field, 1996; Krizhevsky et al., 2017). Bansal et al. (2021) expanded on the idea of model stitching, showing that models trained using self-supervised objectives align closely with their supervised counterparts.

Moschella et al. (2022) further demonstrated the feasibility of "zero-shot" model stitching without learning a stitching layer. Despite the fact that different text models were trained on different modalities, they found that the models often embed data in remarkably similar ways. In particular, they considered the kernel K defined by learned representations and showed that K serves as a bridge between models, allowing an encoder trained in one language, like English, to work effectively with a decoder in another, like French.

Dravid et al. (2023) extended this idea to individual neurons, and found "Rosetta Neurons" that are activated by the same pattern across a range of vision models. Such neurons form a common dictionary independently discovered by all models.

#### 2.2. Alignment increases with scale and performance

Kornblith et al. (2019) and Roeder et al. (2021) observed model alignment not only exists but also increases with model scale and dataset size. On CIFAR-10 classification, Krizhevsky et al. (2009) found that larger models exhibit greater alignment with each other compared to smaller ones. Theoretically, Balestriero & Baraniuk (2018) showed that models with similar outputs (*e.g.*, as a result of having high performance) also have similar internal activations. With the continuing trend of models scaling up, this suggests model alignment will increase over time – we might expect that the next generation of bigger, better models will be even more aligned with each other.

We expand upon this observation by evaluating the transfer performance of 78 vision models. These models were trained with varying architectures, training objectives, and datasets (detailed in Appendix C.1). In Figure 2 (left), we bin these models based on their average transfer performance on the VTAB dataset (Zhai et al., 2019), and then measure the average kernel alignment of the models within each bin. The results indicate that models with high transfer performance form a tightly clustered set of representations, while models with weak performance have more variable representations. We further visualize this structure with UMAP (McInnes et al., 2018) over models representation in Figure 2 (right). This suggests that models that are competent all represent data in a similar way. Echoing Bansal et al. (2021) and Tolstoy (1877), we might say: all strong models are alike, each weak model is weak in its own way.

The discussion so far indicates that various models are aligning toward a unified representation. But does the convergence extend to model weights? While models with different architectures might not have compatible weight spaces, there exists ample evidence that models with the same architecture will often converge to the same basin of weights (Nagarajan & Kolter, 2019; Garipov et al., 2018; Lubana et al., 2023). This holds even for models with different initializations, up to permutations over weight space (Ainsworth

![](_page_3_Figure_1.jpeg)

Figure 3. LANGUAGE and VISION models align: We measure alignment using mutual nearest-neighbor on the Wikipedia caption dataset (WIT) (Srinivasan et al., 2021). The x-axis is the language model performance measured over 4M tokens from the OpenWebText dataset (Gokaslan & Cohen, 2019) (see Appendix B for plots with model names). We measure performance using 1 — bits-per-byte, where bits-per-byte normalizes the cross-entropy by the total bytes in the input text string. The results show a linear relationship between language-vision alignment and language modeling score, where a general trend is that more capable language models align better with more capable vision models. We find that CLIP models, which are trained with explicit language supervision, exhibit a higher level of alignment. However, this alignment decreases after being fine-tuned on ImageNet classification (labeled CLIP (I12K ft)).

et al., 2022). Because of this, it is possible to merge separately trained models of the same architecture, and achieve some of the capabilities of all models in the mixture (Stoica et al., 2023; Jordan et al., 2022; Wortsman et al., 2022).

## 2.3. Representations are converging across modalities

Do models trained on different data modalities also converge? Several works indicate that the answer is *yes*.

Merullo et al. (2022) extended model stitching to the crossmodal setting, finding that a single linear projection is sufficient to stitch a vision model to an LLM and achieve good performance on visual question answering and image captioning. Koh et al. (2023) showed that linear stitching can also work in the opposite direction, aligning text inputs to visual outputs. In fact, many recent language-vision models stitch pre-trained language and vision models together. For example, LLaVA (Liu et al., 2023) demonstrated state-ofthe-art results by projecting visual features into a language model with a 2-layer MLP.

Other works show further kinds of evidence of cross-modal synergy. OpenAI (2023) found that jointly training a language model with a vision model improves performance on language tasks, compared to training the language model on its own. Sorscher et al. (2022) show a setting in which word embeddings of visual concept names can be isometrically mapped to image embeddings for those same concepts. In work concurrent to ours, Maniparambil et al. (2024) show well-trained vision encoders on large datasets exhibit high semantic similarity with language encoders regardless

<span id="page-3-0"></span>of the training paradigm (supervised, self-supervised, or language-supervised). Sharma et al. (2024) probed the visual knowledge of LLMs trained only on language data, by converting images into code that an LLM can process. They found that LLMs have rich knowledge of visual structures, to the extent that decent visual representations can be trained on images generated solely by querying an LLM to produce code and rendering the response. In visual generation, LLMs show abilities to augment captions with visual structures (e.g., bounding boxes) and improve generation quality (Betker et al., 2023; Lian et al., 2023a;b; Wu et al., 2023). Over other modalities, Ngo & Kim (2024) showed auditory models are also roughly aligned with LLMs up to a linear transformation, and Ng et al. (2023) demonstrated the effectiveness of using pre-trained LLMs for facial motion prediction.

We set out to address these claims in a broader scope to determine whether models are indeed learning an increasingly modality-agnostic representation of the world. We sampled a variety of models trained either solely on vision or solely on language, and compared their representations as they became larger and more competent over many tasks.

In Figure 3, we assess alignment between a suite of language models and vision models. So far we have only defined alignment for two kernels defined over the same input space. To measure cross-modal alignment, we use paired datasets to bridge the two modalities. For vision and text, we use the Wikipedia captions dataset  $\{(x_i, y_i)\}_i$  (Srinivasan et al., 2021), composed of images from Wikipedia  $(x_i)$  and their

![](_page_4_Figure_1.jpeg)

![](_page_4_Figure_2.jpeg)

<span id="page-4-0"></span>Figure 4. Alignment predicts downstream performance: We visualize correlation between LLM alignment score to DINOv2 (Oquab et al., 2023) and downstream task performance on Hellaswag (common-sense) (Zellers et al., 2019) and GSM8K (math) (Cobbe et al., 2021). LLMs are plotted with radii proportional to the size of the model, and color-coded by their rank order in language modeling scores (1 – bits-per-byte). We observe that models aligned more closely with vision also show better performance on downstream language tasks. For Hellaswag, there is a linear relationship with alignment score, while GSM8K exhibits an "emergence"-esque trend.

corresponding captions  $(y_i)$ . We then measure alignment between a language model  $f_{\text{text}}$  and a vision model  $f_{\text{img}}$  as the alignment of the two following kernels:

$$K_{\rm img}(i,j) = \langle f_{\rm img}(x_i), f_{\rm img}(x_j) \rangle \tag{1}$$

$$K_{\text{text}}(i,j) = \langle f_{\text{text}}(y_i), f_{\text{text}}(y_i) \rangle.$$
 (2)

Using this analysis, we find that the better an LLM is at language modeling, the more it tends to aligns with vision models, as shown in Figure 3. The converse effect also holds: the better a vision models is, the more it tends to align with LLMs. See Appendix C.2 for more details.

#### 2.4. Models are increasingly aligning to brains

Neural networks also show substantial alignment with biological representations in the brain (Yamins et al., 2014). This commonality may be due to similarities in the task and data constraints both systems are confronted with. Even though the mediums may differ - silicon transistors versus biological neurons – the fundamental problem faced by brains and machines is the same: efficiently extracting and understanding the underlying structure in images, text, sounds, etc. (Barlow et al., 1961; Olshausen & Field, 1997). Sorscher et al. (2022) developed a theoretical framework for how the efficient extraction of novel concepts occurs for both the human visual system and deep networks. The tasks that the human visual system has been honed to perform through evolution - like segmentation, detection, and whole-image classification – are also the ones that we train our neural nets to perform. Yamins et al. (2014) went as far as to title their work in the spirit that performance over such tasks implies brain alignment. Antonello & Huth (2024) posited that it is less the particular task and more the generality of the representations that explain their alignment with biological representations. Further, Conwell et al. (2022) showed that training data plays a large role in alignment. Psychophysical studies have also shown agreement between how humans perceive visual similarity and how models do, even when the models are trained on tasks, such as self-supervised prediction, that are seemingly unrelated to mimicking human perception (Zhang et al., 2018).

## 2.5. Does alignment predict downstream performance?

If models are converging towards a more accurate representation of reality, we expect that alignment should correspond to improved performance on downstream tasks. Figure 4 supports this hypothesis by demonstrating improved performance on commonsense reasoning (Hellaswag; Zellers et al. (2019)) and mathematical problem solving (GSM8K; Cobbe et al. (2021)) as alignment improves.

## 3. Why are representations converging?

Modern machine learning models are generally trained to minimize the empirical risk with possible implicit and/or explicit regularization:

$$f^* = \underset{\text{function class}}{\operatorname{arg\,min}} f \in \underset{\text{function class}}{\operatorname{\mathbb{F}}} \mathbb{E}_{x \sim \text{ dataset}} \left[ \underbrace{\mathcal{L}(f,x)} \right] + \underset{\text{regularization}}{\operatorname{\mathbb{F}}} (f)$$

In the following sections, we lay out how each colored component in this optimization process potentially plays a role in facilitating representational convergence.

### 3.1. Convergence via Task Generality

Each training datapoint and objective (task) places an additional constraint on the model. As data and tasks scale, the volume of representations that satisfy these constraints must proportionately grow smaller, as visualized in Figure 6 and stated below:

![](_page_5_Picture_1.jpeg)

Figure 5. The Capacity Hypothesis: If an optimal representation exists in function space, larger hypothesis spaces are more likely to cover it. **LEFT:** Two small models might not cover the optimum and thus find *different* solutions (marked by outlined  $\bigstar$ ). **RIGHT:** As the models become larger, they cover the optimum and converge to the same solution (marked by filled  $\bigstar$ ).

<span id="page-5-1"></span>![](_page_5_Picture_3.jpeg)

Figure 6. The Multitask Scaling Hypothesis: Models trained with an increasing number of tasks are subjected to pressure to learn a representation that can solve all the tasks.

#### <span id="page-5-0"></span>The Multitask Scaling Hypothesis

There are fewer representations that are competent for N tasks than there are for M < N tasks. As we train more general models that solve more tasks at once, we should expect fewer possible solutions.

This has been previously termed as the Contravariance principle by Cao & Yamins (2024), which states that the set of solutions to an easy goal is large, while the set of solutions to a challenging goal is comparatively smaller. Moreover, we argue that this narrower solution set also generalizes better. As data scales, models that optimize the empirical risk  $\mathbb{E}_{x \sim \text{dataset}} [\mathcal{L}(f,x)]$  also improve on the population risk  $\mathbb{E}_{x \sim \text{reality}} [\mathcal{L}(f,x)]$ , and become better at capturing statistical structures of the true data generating process (reality).

Recent work has demonstrated a power law relationship between data scale and model performance (Hestness et al., 2017). This implies that with enough data (*e.g.*, consisting of the entire internet and all offline scientific measurements) one ought to converge to a very small solution set with irreducible error – the inherent epistemic uncertainty of the world. As more models are trained on internet-scale data, the set of solutions that satisfies all data constraints must become relatively small.

In addition to data-scaling, many modern representation learning objectives  $\mathcal{L}(f,x)$  directly optimize for multitask solving. Contrastive learning finds a distance structure over data samples that optimizes many classification tasks (Arora et al., 2019b; Wang & Isola, 2020; Tian et al., 2020b). Masked Autoencoders (He et al., 2021) optimize randomly sampled reconstruction tasks. In fact, autoregressive language modeling can also be seen as optimizing a diverse set of tasks (Radford et al., 2019). Such multi-task objectives may be more effective than single-task ones (e.g., ImageNet classification) due to the fact that they impose more task constraints on the representation, leading to a smaller and higher-quality solution space (Chen et al., 2020; He et al., 2020; Radford et al., 2017; 2019).

#### 3.2. Convergence via Model Capacity

Suppose there is a globally optimal representation for standard learning objectives. Then, under sufficient data, *scaling* a model (*i.e.*, using larger function classes  $\mathcal{F}$ ), as well as improved optimization, should be more effective at finding better approximations to this optimum, as illustrated in Figure 5. With the same training objective, larger models, even of different architectures, will thus tend to converge toward this optimum. When different training objectives share similar minimizers, larger models are better at finding these minimizers, and will train to similar solutions over the training tasks. We summarize this hypothesis as follows:

![](_page_6_Picture_1.jpeg)

Figure 7. The Simplicity Bias Hypothesis: Larger models have larger coverage of all possible ways to fit the same data. However, the implicit simplicity biases of deep networks encourage larger models to find the simplest of these solutions.

## <span id="page-6-1"></span>The Capacity Hypothesis

Bigger models are more likely to converge to a shared representation than smaller models.

## 3.3. Convergence via Simplicity Bias

Arriving at the same mapping on the *training data* does not prohibit the models from developing distinct internal representations. It is not unreasonable to posit that the representations used to detect a dog in a 1M parameter model could be quite different than that used by a 1B parameter model. What would stop a billion-parameter (and counting) model from learning an overly complicated and distinct representation? One key factor might be simplicity bias:

### The Simplicity Bias Hypothesis

Deep networks are biased toward finding simple fits to the data, and the bigger the model, the stronger the bias. Therefore, as models get bigger, we should expect convergence to a smaller solution space.

Such simplicity bias could be coming from explicit regularization R(f) commonly used in deep learning (*e.g.*, weight decay and dropout). However, even in the absence of external influences, deep networks naturally adhere to Occam's razor, implicitly favoring simple solutions that fit the data [\(Solomonoff,](#page-14-17) [1964;](#page-14-17) [Gunasekar et al.,](#page-11-11) [2018;](#page-11-11) [Arora](#page-10-11) [et al.,](#page-10-11) [2019a;](#page-10-11) [Valle-Perez et al.,](#page-15-10) [2019;](#page-15-10) [Huh et al.,](#page-12-11) [2023;](#page-12-11) [Din](#page-11-12)[gle et al.,](#page-11-12) [2018;](#page-11-12) [Goldblum et al.,](#page-11-13) [2023\)](#page-11-13). Figure [7](#page-6-1) visualizes how simplicity bias can drive convergence.

# <span id="page-6-0"></span>4. What representation are we converging to?

By now, we hope to have convinced the reader that task and data pressures, combined with increasing model capacity, can lead to convergence. We next turn our attention to *what* exactly is the endpoint of all this convergence.

Our central hypothesis, stated in Figure [1,](#page-0-0) is that the representation we are converging toward is a statistical model of the underlying reality that generates our observations. Consistent with the multitask scaling hypothesis, such a representation would naturally be useful toward many tasks (or at least toward any task grounded in reality). Additionally, this representation might be relatively simple, assuming that scientists are correct in suggesting that the fundamental laws of nature are indeed simple functions [\(Gell-Mann,](#page-11-14) [1995\)](#page-11-14), in line with the simplicity bias hypothesis.

But what exactly do we mean by "a statistical model of the underlying reality." In this section, we formalize one definition with concrete mathematical statements. *Importantly*, this section should be read as just one concrete candidate for the form of the platonic representation; other candidates could be arrived at from other modeling assumptions.

#### 4.1. An idealized world

We consider a world that works as follows, consistent with the cartoon in Figure [1.](#page-0-0) The world consists of a sequence of T discrete events, denoted as Z ≜ [z1, . . . , z<sup>T</sup> ], sampled from some unknown distribution **P**(Z). Each event can be observed in various ways. An observation is a bijective, deterministic function obs : Z → · that maps events to an arbitrary measurement space, such as pixels, sounds, mass, force, torque, words, etc. Later, in Section [6,](#page-8-0) we discuss limitations and potential extensions to continuous and unbounded worlds, and stochastic observations, that could yield a model that better reflects real learning scenarios.

One can think of an event as corresponding to the state of the world at some point in time[3](#page-0-1) , but it is also fine to simply consider an event as any variable that indexes observations, with no further physical meaning[4](#page-0-1) .

In this idealized world, knowing **P**(Z) would be useful for many kinds of predictions; this would constitute a world model over the events that cause our observations [\(Werbos,](#page-15-11) [1987;](#page-15-11) [Ha & Schmidhuber,](#page-11-15) [2018;](#page-11-15) [Richens & Everitt,](#page-14-4) [2024\)](#page-14-4). We will next show that a particular representation of **P**(Z) is recovered by certain contrastive learners.

<sup>3</sup>Here we only analyze temporal sequences, but note that the same could be done with respect to events laid out in space instead.

<sup>4</sup>This latter interpretation may be more consistent with Plato's intent. Scholars have argued that his allegory of the cave rejects any notion of a true world state [\(Nettleship,](#page-13-16) [1897\)](#page-13-16). Instead, we could say that the joint distribution of observation indices is *itself* the platonic reality.

![](_page_7_Figure_1.jpeg)

<span id="page-7-1"></span>Figure 8. Color cooccurrence in VISION and LANGUAGE yields perceptual organization: Similar representations of color are obtained via, from LEFT to RIGHT, the perceptual layout from CIELAB color space, cooccurrence in CIFAR-10 images, and language cooccurrence modeling [\(Gao et al.](#page-11-16) [\(2021\)](#page-11-16); [Liu et al.](#page-13-17) [\(2019\)](#page-13-17); computed roughly following [Abdou et al.](#page-10-12) [\(2021\)](#page-10-12)). Details in Appendix [D.](#page-24-0)

## <span id="page-7-2"></span>4.2. A family of contrastive learners converge to a representation of **P**(Z)

Consider a contrastive learner that models observations that *cooccur* together. For simplicity, we ground our discussion with the following definition of the *cooccurrence probability*, Pcoor, of two observations x<sup>a</sup> and x<sup>b</sup> both occurring within some window Twindow:

$$P_{\text{coor}}(x_a, x_b) \propto \sum_{(t, t'): |t - t'| \le T_{\text{window}}} \mathbb{P}(X_t = x_a, X_{t'} = x_b).$$

Analogously, we can define Pcoor for Z and other observation modalities. Note that Pcoor is symmetric.

Consider *positive pairs* as two observations nearby in time (sampled from Pcoor) and *negative pairs* as observations drawn from any point in time (sampled independently from the marginal). Our contrastive learner tries to classify if a pair is positive or negative by learning a representation f<sup>X</sup> : X → **R** d such that the dot-product kernel approximates the log odds ratio up to some offset:

$$\langle f_X(x_a), f_X(x_b) \rangle \approx \log \frac{\mathbb{P}(\text{pos} \mid x_a, x_b)}{\mathbb{P}(\text{neg} \mid x_a, x_b)} + \tilde{c}_X(x_a) \quad (3)$$

$$= \log \frac{P_{\text{coor}}(x_a \mid x_b)}{P_{\text{coor}}(x_a)} + c_X(x_a) \quad (4)$$

= KPMI(xa, xb) + cX(xa), (5)

where KPMI is the pointwise mutual information (PMI) kernel, and cX(xa) is constant in xb. We note that this is a common setting for self-supervised contrastive learners with NCE objectives [\(Gutmann & Hyvarinen](#page-11-17) ¨ , [2010;](#page-11-17) [Oord](#page-13-18) [et al.,](#page-13-18) [2018\)](#page-13-18), including SimCLR [\(Chen et al.,](#page-11-10) [2020\)](#page-11-10) and SimCSE [\(Gao et al.,](#page-11-16) [2021\)](#page-11-16). (See [Oord et al.](#page-13-18) [\(2018\)](#page-13-18) and Appendix [F.1](#page-25-0) for detailed derivations.)

Under mild conditions that the world is smooth enough (see Appendix [F.2\)](#page-26-0), a choice of f<sup>X</sup> can exactly represent KPMI:

$$\langle f_X(x_a), f_X(x_b) \rangle = K_{\mathsf{PMI}}(x_a, x_b) + c_X, \tag{6}$$

where we observed that cX(xa) from Equation [\(5\)](#page-7-0) must be a constant since both sides are symmetric.

Therefore, the contrastive learners we consider are minimized by a representation f<sup>X</sup> whose kernel is KPMI (up to a constant offset). With sufficient data and optimization, we will observe convergence to this point.

Thus we have convergence to a representation of the statistics of X, but what about Z? Recall that our idealized world consists of *bijective* observation functions, which, over discrete random variables, preserve probabilities. So we have:

$$\begin{split} P_{\mathsf{coor}}(x_a, x_b) &= P_{\mathsf{coor}}(z_a, z_b) \\ K_{\mathsf{PMI}}(x_a, x_b) &= K_{\mathsf{PMI}}(z_a, z_b), \end{split}$$

where we use Pcoor and KPMI in a modality-agnostic way to emphasize that different modalities share the same these quantities.

All these arguments hold not just for X but also for Y (or any other bijective, discrete modality), implying:

$$K_{\mathsf{PMI}}(z_a, z_b) = \langle f_X(x_a), f_X(x_b) \rangle - c_X \tag{7}$$

$$= \langle f_Y(y_a), f_Y(y_b) \rangle - c_Y. \tag{8}$$

<span id="page-7-0"></span>Therefore, for any modality in our idealized world, we observe representational convergence to the same kernel, which represents certain pairwise statistics of **P**(Z).

This analysis suggests that certain representation learning algorithms may boil down to a simple rule: *find an embedding in which similarity equals PMI*. We note that this idea is consistent with prior works that have used PMI as a similarity measure for clustering in vision and language (*e.g.*, [Isola et al.](#page-12-12) [\(2014\)](#page-12-12); [Isola](#page-12-13) [\(2015\)](#page-12-13); [Isola et al.](#page-12-14) [\(2016\)](#page-12-14); [Chambers & Jurafsky](#page-11-18) [\(2008\)](#page-11-18)).

A study in color We conduct a case study to verify that convergence does happen on real data. [Abdou et al.](#page-10-12) [\(2021\)](#page-10-12) discovered that color distances in learned language representations, when trained to predict cooccurrences in *text* [\(Devlin et al.,](#page-11-19) [2018\)](#page-11-19), closely mirror human perception of these distances, which we reproduce in Figure [8](#page-7-1) with both contrastive and predictive models. Interestingly, they noted an increasing similarity as models scale larger and become better at modeling *text* cooccurrences. In Figure [8,](#page-7-1) we also learn representations of color based on KPMI from cooccurrences in *images*. Indeed, learning cooccurrence statistics in either domain recovers roughly the *same* perceptual representation. Details of this experiment are described in Appendix [D.](#page-24-0)

We believe that our simple model encapsulates essential aspects of complex real-world systems, and offers a path toward understanding the representation that models are converging to—a unified model that is proficient across various domains and modalities, grounded in the statistical properties of the underlying world. Section [6](#page-8-0) further elaborates some limitations.

# 5. What are the implications of convergence?

Scaling is sufficient, but not necessarily efficient Our arguments are roughly in line with the claim that "scale is all you need" to reach high levels of intelligence. We have argued that as resources are scaled (# parameters, # datapoints, # flops), representations are converging, regardless of other modeling choices and even data modality. Does this mean that scale is all that matters? Not quite: different methods can scale with different levels of *efficiency* [\(Hestness et al.,](#page-12-8) [2017;](#page-12-8) [Kaplan et al.,](#page-12-15) [2020\)](#page-12-15), and successful methods must still satisfy some general requirements (*e.g.*, be a consistent estimator, model pairwise statistics of **P**(Z)).

Training data can be shared across modalities Suppose you have access to N images and M sentences, and want to learn the best representation. If there is indeed a modality-agnostic platonic representation, then *both* image and language data should help find it. The implication is that if you want to train the best vision model, you should train not just on N images but also on M sentences. This is already becoming common practice [\(OpenAI,](#page-13-0) [2023;](#page-13-0) [Rad](#page-14-18)[ford et al.,](#page-14-18) [2021\)](#page-14-18). Many vision models are finetuned from pre-trained LLMs. The other direction is less common, but also is implied by our hypothesis: if you want to build the best LLM, *you should also train on image data*. Indeed, [OpenAI](#page-13-0) [\(2023\)](#page-13-0) showed that training on images improved performance on text. In theory, there should be some conversion ratio: a pixel is worth a words for training LLMs, and a word is worth b pixels for training vision models.

Ease of translation and adaptation across modalities When two representations are aligned, transitioning from

one to the other should be a simple function that's easily obtained. Our hypothesis could explain the phenomenon that conditional generation is easier than unconditional [\(Mirza &](#page-13-19) [Osindero,](#page-13-19) [2014;](#page-13-19) [Liu et al.,](#page-13-20) [2020;](#page-13-20) [Sauer et al.,](#page-14-19) [2022\)](#page-14-19), as the data we condition on may have the same platonic structure as the data we are generating. In line with this, recent work has found that representation-conditioning is even easier [\(Li](#page-12-16) [et al.,](#page-12-16) [2023\)](#page-12-16). Similarly, representational convergence could act as a bridge that lets us find mappings between domains even without paired data; this may underlie the success of unpaired translation in vision [\(Zhu et al.,](#page-16-2) [2017;](#page-16-2) [Shi et al.,](#page-14-20) [2024;](#page-14-20) [Xie et al.,](#page-15-12) [2022\)](#page-15-12) and language [\(Tran et al.,](#page-15-13) [2017;](#page-15-13) [Lam](#page-12-17)[ple et al.,](#page-12-17) [2018\)](#page-12-17). We emphasize that this doesn't mean that models trained on a single modality (*e.g.*, language) can immediately process raw data from another (*e.g.*, vision). What makes them adaptable to the new modalities is that they share a common modality-agnostic representation, and can readily process *representations* of new modalities. Furthermore, this implies that language models would achieve some notion of grounding in the visual domain even in the absence of cross-modal data[5](#page-0-1) . The primary advantage of cross-modal data could then simply be sample efficiency.

Scaling may reduce hallucination and bias A prominent shortcoming of current LLMs is their propensity to hallucinate, or output false statements. If models are indeed converging toward an accurate model of reality, and scale powers this convergence, then we may expect hallucinations to decrease with scale. Of course, our hypothesis is conditioned on the training data for future models constituting a sufficiently lossless and diverse set of measurements. This may not come to pass, but it is an implication of our hypothesis worth pointing out. A similar argument can be made about certain kinds of bias. It has been shown that large models can exacerbate existing biases present in their training data [\(Hall et al.,](#page-11-20) [2022\)](#page-11-20). Our hypothesis implies that, while this may be true, we should expect *larger* models to amplify bias *less*. This does not mean bias will be removed, rather that the model's biases will more accurately reflect the data's biases, rather than exacerbating them.

# <span id="page-8-0"></span>6. Counterexamples and limitations

Different modalities may contain different information One immediate objection to our hypothesis is: what about the information that is unique to a given modality? Can language really describe the ineffable experience of watching

<sup>5</sup> In 1688, William Molyneux asked if a person born blind, upon gaining sight, could distinguish shapes by vision alone [\(Locke,](#page-13-21) [1690\)](#page-13-21). Our arguments suggest they could not do so immediately, but after some visual experience, they could easily map shapes to their prior touch-based representations. Empirical data supports this, showing that congenitally blind children given sight can quickly learn these abilities [\(Held et al.,](#page-12-18) [2011\)](#page-12-18).

![](_page_9_Figure_1.jpeg)

Figure 9. Increasing caption density improves alignment: We vary caption length using the Densely-Captioned-Images (DCI) dataset (Urbanek et al., 2023). Starting from a dense caption, we used LLaMA3-8B-Instruct (Meta, 2024) to summarize and generate coarse-grained captions. We compute the average alignment score across all vision and language models with standard deviation measured over the language models we evaluated. With denser captions, the mapping may become more bijective, leading to improved language-vision alignment scores.

a total solar eclipse? Or, how could an image convey the a concept like "I believe in the freedom of speech," which is easy to write in English? Two different models cannot converge to the same representation if they have access to fundamentally different information.

More precisely, our mathematical argument in Section 4 only strictly holds for bijective projections of **Z**, so that the information in all the projections is equivalent to the information in the underlying world. This will not hold true for either lossy or stochastic observation functions. Nonetheless, similar arguments have been made theoretically and empirically that cooccurrence relations are learned by practical contrastive (Wang & Isola, 2020; Zimmermann et al., 2021) and predictive learners (Papyan et al., 2020; Roeder et al., 2021). Lu et al. (2021) and Mirchandani et al. (2023) also showed that models trained to autoregressively generate text also capture statistical relations in many other modalities, including symbolic reasoning, vision, protein folding, and robotics.

A more nuanced version of our hypothesis will need to be developed to handle the case of non-bijective observations and abstract concepts. A starting point could be: different models will converge to the same representation when the input signals are sufficiently high information and the models are sufficiently high capacity; when they are not, the lower-information representation will only align with the higher-information one up to a level capped by the mutual information between the input signals and by the capacity of each model. This cap might or might not be practically important. Popular representations like CLIP are explicitly

optimized to only capture the shared information between vision and language, yet are highly successful on many pure vision tasks. We perform a preliminary test of the effect of information level in Figure 9 (detailed in Appendix E), and find that the more descriptive (higher information) a caption is, the better its LLM representation aligns with the visual representation of the corresponding image.

<span id="page-9-0"></span>Not all representations are presently converging Our argument has mainly focused on two modalities: vision and language. While we do expect other modalities will follow similar trends, we have yet to see the same level of convergence across all domains. For example, in robotics there is not yet a standardized approach to representing world states in the same way as there is for representing images and text. One limitation lies in the hardware used in robotics, which is often expensive and slow. This creates a bottleneck in the quantity and diversity of training data.

Sociological bias in producing AI models Researcher bias and collective preferences within the AI community have shaped the trajectory of model development. There is often an explicit or implicit goal of designing AI systems that mimic human reasoning and performance, and this could lead to convergence toward human-like representations even if other kinds of intelligence are in fact possible. Additionally, the "hardware lottery" (Hooker, 2021) suggests that the success of AI models can also depend on the compatibility of their design with available computational architectures, further contributing to convergent trends.

Special-purpose intelligences might not converge Different intelligent systems can be designed to accomplish different tasks. For instance: A bioinformatics systems might predict protein structure; an autonomous vehicle might follow lanes on highways. It's possible that not much is shared between these two narrow tasks. Our argument only holds for intelligences that are optimized to perform well on *many* tasks. We have argued that a representation of *reality* is a structure that is useful across many tasks, but for any special purpose there may be shortcuts, or even effective representations detached from reality. Such shortcuts may be more efficient and necessary for continued improvements in specific domains. This will become more relevant if continued scaling comes up against boundary conditions around resources like energy and compute.

How do we measure alignment? We focused on one particular alignment measure, mutual nearest-neighbor, in our experiments, and cited experiments using several others. However, there is active debate on the merits and deficiencies of all these ways of measuring alignment (Bansal et al., 2021; Sucholutsky et al., 2023). We discuss our choice and show results for other alignment metrics in Appendix A.

Lots left to explain We have shown results where different models arrive at *similar* but not the *same* representations. For example, in Figure [3,](#page-3-0) alignment clearly increases but only reaches a score of 0.16, according to our mutual nearest-neighbor metric. The maximum theoretical value for this metric is 1. Is a score of 0.16 indicative of strong alignment with the remaining gap being "noise" or does it signify poor alignment with major differences left to explain? We leave this as an open question.

## <span id="page-17-0"></span>A. Mutual k-Nearest Neighbor Alignment Metric

For two models with representations f, g the mutual k-nearest neighbor metric measures the average overlap of their respective nearest neighbor sets. In this section, we refer to this metric as  $m_{NN}$ , which we will formally define below.

For cross-modal domains, define  $(x_i,y_i) \in \mathcal{X}$  as a sample from the data distribution  $\mathcal{X}$  (e.g. image-caption dataset). For the single domain alignment measurements, the samples are equivalent  $x_i = y_i$  (e.g., images for vision, and text for language). Let  $\{x_i,y_i\}_{i=1}^b$  be the corresponding mini-batch sampled from this data distribution. Then given two model representations f and g the corresponding features are:  $\phi_i = f(x_i)$  and  $\psi_i = g(y_i)$ , where the collection of these features are denoted as  $\Phi = \{\phi_1,\ldots,\phi_b\}$  and  $\Psi = \{\psi_1,\ldots,\psi_b\}$ . Then for each feature pair  $(\phi_i,\psi_i)$ , we compute the respective nearest neighbor sets  $\mathcal{S}(\phi_i)$  and  $\mathcal{S}(\psi_i)$ .

$$d_{\mathsf{knn}}(\phi_i, \Phi \setminus \phi_i) = \mathcal{S}(\phi_i) \tag{9}$$

$$d_{\mathsf{knn}}(\psi_i, \Psi \setminus \psi_i) = \mathcal{S}(\psi_i) \tag{10}$$

where  $d_{knn}$  returns the set of indices of its k-nearest neighbors. Then we measure its average intersection via

$$m_{\text{NN}}(\phi_i, \psi_i) = \frac{1}{k} |\mathcal{S}(\phi_i) \cap \mathcal{S}(\psi_i)| \tag{11}$$

where  $|\cdot|$  is the size of the intersection.

The choice to use mutual nearest-neighbors Our initial efforts to measure alignment with CKA revealed a very weak trend of alignment between models, even when comparing models within their own modality. This has also been observed by (Bansal et al., 2021), which had relied on alternative metrics such as model-stitching as it "reveals aspects of representations that measures such as centered kernel alignment (CKA) cannot" (Bansal et al., 2021).

We chose to use nearest-neighbor as a metric, as methods like CKA has a very strict definition of alignment, which may not fit our current needs. For instance, understanding the precise similarity between unrelated items, such as an orange and Bill Gates, may not be critical.

**Relationship between CKA and Mutual Nearest-Neighbors** Let  $\phi_i \in \mathbb{R}^n$  and  $\psi_i \in \mathbb{R}^m$  be vectorized features of two models (e.g. language and vision models). Let  $\mathbf{K}_{ij} = \kappa(\phi_i, \phi_j)$  and  $\mathbf{L}_{ij} = \kappa(\psi_i, \psi_j)$  be the kernel matrices computed from a dataset using some kernel-function  $\kappa$ . Using an inner-product kernel, the ij-th entry of the centered counterpart of these Kernel matrices is:

$$\bar{\mathbf{K}}_{ij} = \langle \phi_i, \phi_j \rangle - \mathbb{E}_l[\langle \phi_i, \phi_l \rangle] \qquad \bar{\mathbf{L}}_{ij} = \langle \psi_i, \psi_j \rangle - \mathbb{E}_l[\langle \psi_i, \psi_l \rangle]$$
 (12)

Then, the cross-covariance of K and L is given by:

$$\mathsf{HSIC}(\mathbf{K}, \mathbf{L}) = \frac{1}{(n-1)^2} \mathsf{Trace}(\bar{\mathbf{K}}\bar{\mathbf{L}}) \tag{13}$$

which serves as an empirical estimator of the Hilbert-Schmidt Independence Criterion (Gretton et al., 2005). The Centered Kernel Alignment (CKA) (Kornblith et al., 2019) is then its normalized counterpart:

$$\mathsf{CKA}(\mathbf{K}, \mathbf{L}) = \frac{\mathsf{HSIC}(\mathbf{K}, \mathbf{L})}{\sqrt{\mathsf{HSIC}(\mathbf{K}, \mathbf{K})\mathsf{HSIC}(\mathbf{L}, \mathbf{L})}} \tag{14}$$

CKA measures the congruence between two random variables, with a maximum alignment of 1 and a minimum of 0. It is invariant to isotropic scaling and offers a strict notion of alignment, measuring alignment across all samples. Hence, the CKA score reflects the global similarities of the models. This can be illustrated by expanding the trace term in HSIC:

$$\mathsf{Trace}(\bar{\mathbf{K}}\bar{\mathbf{L}}) = \sum_{i} \sum_{j} \left( \langle \phi_{i}, \phi_{j} \rangle - \mathbb{E}_{l}[\langle \phi_{i}, \phi_{l} \rangle] \right) \left( \langle \psi_{i}, \psi_{j} \rangle - \mathbb{E}_{l}[\langle \psi_{i}, \psi_{l} \rangle] \right) \tag{15}$$

One can modify the definition of alignment to restrict the cross-covariance measurement to samples considered to be nearest neighbors of the current sample i. This emphasizes similarity over dissimilarity, biasing the measure toward local alignment:

$$\mathsf{Align}_{\mathsf{knn}}(\mathbf{K}, \mathbf{L}) = \sum_{i} \sum_{j} \alpha(i, j) \cdot (\langle \phi_i, \phi_j \rangle - \mathbb{E}_l[\langle \phi_i, \phi_l \rangle]) \left(\langle \psi_i, \psi_j \rangle - \mathbb{E}_l[\langle \psi_i, \psi_l \rangle]\right) \tag{16}$$

where 
$$\alpha(i,j) = \mathbb{1}[\phi_i \in \mathsf{knn}(\phi_i) \land \psi_j \in \mathsf{knn}(\psi_i) \land i \neq j]$$
 (17)

Alignment trend using CKNNA metric

#### 0.4 ImageNet21K CLIP (112K ft) 0.2 0.0 0.0 -0.2 -0.4 -0.4 100.78 10<sup>1.48</sup>10<sup>1.30</sup> 100.78 101.48101.30 10<sup>1</sup> 101.48101.30 101.48101.30 LANGUAGE model perplexity (log-scale) K=1000 -- K=500 -- K=200 -- K=100

<span id="page-18-1"></span>Figure 10. Cross-modal alignment increases locally: Alignment trend when varying the top-k nearest neighbors in the CKNNA metrics (Eqn. 18). We center alignment score to the smallest language model and divide the total trend by the standard deviation. When k=1024, we recover the original CKA metric, and when  $k<|\mathcal{X}|$  it closely resembles the mutual nearest-neighbor metric  $m_{\texttt{NN}}$ . Each line represents the average of all LLM models for a specific k. As we decrease k, the alignment becomes more pronounced.

K=800

Where  $\alpha(i,j)$  is a scalar weighting that assigns 1 if j is a mutual nearest neighbors to both  $\phi_i$  and  $\psi_i$ , and 0 otherwise. We refer to this metric as the Centered Kernel Nearest-Neighbor Alignment (CKNNA) metric. As the number of nearest neighbors  $k \to \dim(\mathbf{K})$ , we recover the original CKA metric.

$$\mathsf{CKNNA}(\mathbf{K}, \mathbf{L}) = \frac{\mathsf{Align}_{\mathsf{knn}}(\mathbf{K}, \mathbf{L})}{\sqrt{\mathsf{Align}_{\mathsf{knn}}(\mathbf{K}, \mathbf{K}), \mathsf{Align}_{\mathsf{knn}}(\mathbf{L}, \mathbf{L})}} \tag{18}$$

We can further relax the metric to treat the cross-covariance term identically across all nearest-neighbor samples. This is equivalent to the assumption that all nearby samples have the same distance. This simplification leads us back to the mutual nearest neighbor metric:

<span id="page-18-0"></span>
$$\sum_{i} \sum_{j} \alpha(i, j) \cdot 1 = n \cdot k \cdot m_{NN}(\phi_i, \psi_i)$$
(19)

By equating these metrics, we analyze the changes in alignment between language and vision models as we vary the number of neighbors k in Eqn. 18. In Figure 10, we compute the average alignment score across all LLM models. For each k, we center the scores to the smallest vision model and divide by the standard deviation of the scores. We find that high values of k show less conclusive alignment across tasks while decreasing k shows a coherent trend across both models and tasks.

# <span id="page-19-0"></span>B. Consistency across various metrics

We describe the metrics in Table [11](#page-19-1) and their corresponding properties. The *symmetric* property implies that the metric is symmetric with respect to the data points d(x, y) = d(y, x). The *global* property means all samples are used to compute the distance with respect to every sample. The *ordinal* property is when the ordering of the distance is taken into consideration. For example, mutual nearest neighbor is not ordinal since the nearest neighbors {a, b, c} and {c, a, b} are treated equally. The *batchable* property is a computational property that makes it feasible to compute in a reasonable time frame.

Vision-vision comparison In Figure [12,](#page-20-0) we evaluate Spearman's rank correlation among different metrics and hyperparameters over 78 vision models (details in Appendix [C.1\)](#page-23-0). We find most metrics highly correlated with each other.

Cross-modal comparison We measure vision-language alignment using a range of alternative metrics. We visualize the corresponding alignment results in Figure [13](#page-21-0) and Figure [14.](#page-22-0) Our findings indicate that alignment sensitivity not only depends on the metric used to compute it but also varies according to the specific tasks on which the vision models are trained.

| Metric       | Property  |        |         |           | Description                                                                                                                                                                                    |
|--------------|-----------|--------|---------|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|              | symmetric | global | ordinal | batchable |                                                                                                                                                                                                |
| CKA          | ✓         | ✓      | ✓       | ✓         | Centered Kernel Alignment (CKA; Kornblith et al. (2019))<br>measures the similarity of neural networks by comparing<br>the alignment of their kernel induced by their feature spaces.          |
| Unbiased CKA | ✓         | ✓      | ✓       | ✓         | Unbiased estimator of CKA that corrects for sample bias in<br>HSIC (Song et al., 2012).                                                                                                        |
| SVCCA        | ✓         | ✓      | ✓       | ✓         | Singular Value Canonical Correlation Analysis (SVCCA;<br>Raghu et al. (2017)) compares neural networks by decom<br>posing their activities into singular vectors and measuring<br>correlation. |
| Mutual k-NN  | ✓         |        |         | ✓         | Measures the intersection over union (IoU) of nearest neigh<br>bors between two models.                                                                                                        |
| CKNNA        | ✓         | ✓∗     | ✓       | ✓         | Modified CKA measure that computes the kernel alignment<br>only for its nearest neighbors. See Appendix A.                                                                                     |
| Cycle k-NN   |           |        |         | ✓         | Measures whether the nearest neighbor in one domain also<br>considers the original sample as its nearest neighbor in the<br>other domain.                                                      |
| Edit k-NN    | ✓         | ✓∗     | ✓       |           | Computes the edit distance required to match the nearest<br>neighbors between two datasets. The score is normalized<br>by the maximum edit distance.                                           |
| LCS k-NN     | ✓         | ✓∗     | ✓       |           | Calculates the longest common subsequence of nearest<br>neighbors and is normalized by the sequence length.                                                                                    |

<span id="page-19-1"></span>Figure 11. Comparative analysis of neural network similarity metrics. ✓∗ indicates the metric is global and still meaningful when the nearest neighbor k is set to maximum batch-size k = |X |.

![](_page_20_Figure_1.jpeg)

<span id="page-20-0"></span>Figure 12. Vision-vision alignment measured with various metrics. Spearman's rank correlation among different metrics and batch sizes (bsz) when used to measure alignment among 78 vision models (see Appendix C.1 for details of these models). All p-values are below  $2.24 \times 10^{-105}$ . Our vision-vision analysis in Figure 2 is based on the first metric (Mutual k-NN with k = 10 and bsz = 1000).

![](_page_21_Figure_1.jpeg)

<span id="page-21-0"></span>Figure 13. Cross-modal alignment for various metrics

![](_page_22_Figure_1.jpeg)

<span id="page-22-0"></span>Figure 14. Cross-modal alignment measured with various metrics

# C. Experiments on Evaluating Alignment and Convergence

To demonstrate representational convergence, we take off-the-shelf models at multiple scales and multiple modalities and measure their representational alignment.

#### <span id="page-23-0"></span>C.1. Vision-Vision Alignment and Representation Quality

We consider 78 vision models in total:

- 17 ViT models ranging from ViT-tiny to ViT-giant, trained on tasks including ImageNet-21k [\(Dosovitskiy et al.,](#page-11-22) [2020\)](#page-11-22) classification, Masked Autoencoders [\(He et al.,](#page-12-9) [2021\)](#page-12-9), DINO [\(Caron et al.,](#page-10-13) [2021\)](#page-10-13), and CLIP [\(Radford et al.,](#page-14-18) [2021\)](#page-14-18), including some finetuned on ImageNet-12k.
- 1 randomly initialized ResNet-50.
- 11 ResNet-50 models trained with contrastive learning on ImageNet-1k, Places-365 [\(Zhou et al.,](#page-16-1) [2017;](#page-16-1) [Lopez-Cifuentes](#page-13-26) ´ [et al.,](#page-13-26) [2020\)](#page-13-26), and 9 synthetic image datasets used in [Baradad et al.](#page-10-14) [\(2022\)](#page-10-14).
- 49 ResNet-18 models trained with Alignment and Uniformity contrastive loss [\(Wang & Isola,](#page-15-8) [2020\)](#page-15-8) on ImageNet-100, Places-365, and 47 realistic and synthetic image datasets from [Baradad et al.](#page-10-15) [\(2021\)](#page-10-15).

To test representation quality, we evaluate linear probing performance on all 19 VTAB classification tasks [\(Zhai et al.,](#page-15-2) [2019\)](#page-15-2), which is a standard multi-task transfer learning benchmark containing structured, specialized, and natural datasets covering diverse domains. To reduce compute requirements, we subsample training and validation datasets to have at most 10,000 samples. We consider a representation solves a task if its performance is ≥ 80% of the best performance on that task across all 78 models.

To compute the alignment metric, we use k = 10 nearest neighbors over 1000 image representations computed on Places-365's validation dataset [\(Zhou et al.,](#page-16-1) [2017\)](#page-16-1). This dataset is disjoint from VTAB datasets, although both contain natural images.

## <span id="page-23-1"></span>C.2. Cross-Modal Alignment

We compare the representation of an image in a vision model to the representation of a caption describing that image in a language model. The language model families we consider are BLOOM [\(BigScience et al.,](#page-10-16) [2022\)](#page-10-16), OpenLLaMA [\(Geng & Liu,](#page-11-23) [2023\)](#page-11-23), and LLaMA [\(Touvron et al.,](#page-15-15) [2023\)](#page-15-15). For Figure [4,](#page-4-0) we included more recent model families such as OLMo [\(Groeneveld](#page-11-24) [et al.,](#page-11-24) [2024\)](#page-11-24), LLaMA3 [\(Meta,](#page-13-22) [2024\)](#page-13-22), Gemma [\(Team et al.,](#page-15-16) [2024\)](#page-15-16), and Mistral/Mixtral [\(Jiang et al.,](#page-12-20) [2023;](#page-12-20) [2024\)](#page-12-21). These models were downloaded from Huggingface [\(Wolf et al.,](#page-15-17) [2019\)](#page-15-17).

For vision models, we consider ViT models [\(Dosovitskiy et al.,](#page-11-22) [2020\)](#page-11-22) of various sizes trained on various data and objectives. We mainly consider the popular vision models: classification on ImageNet-21K [\(Russakovsky et al.,](#page-14-9) [2015\)](#page-14-9), MAE [\(He](#page-12-9) [et al.,](#page-12-9) [2021\)](#page-12-9), DINOv2 [\(Oquab et al.,](#page-13-14) [2023\)](#page-13-14), CLIP [\(Radford et al.,](#page-14-18) [2021\)](#page-14-18), and CLIP finetuned on ImageNet-12K. These models were downloaded from PyTorch Image Models (TIMM; [Wightman](#page-15-18) [\(2021\)](#page-15-18)). This is a subset of the models used in vision-vision comparison.

To compute the alignment metric, we use k = 10 nearest neighbors over 1024 samples from WIT (Wikipedia-based Image Text; [Srinivasan et al.](#page-14-11) [\(2021\)](#page-14-11)). For the vision model, we use class token of each layer, and for the language model, we average pool each layer to a single token. Since it is not trivial to determine where the alignment might occur, we draw inspiration from BrainScore[\(Schrimpf et al.,](#page-14-24) [2018\)](#page-14-24) and compute pairwise alignment scores, then take the maximum. One of these pairwise comparisons also includes concatenated features. We apply l<sup>2</sup> normalization to the features before measuring the distance. As transformer architectures have "emergent outliers" [\(Dettmers et al.,](#page-11-25) [2022\)](#page-11-25), we truncate the elements in the features that are above the 95-th percentile.

Simply taking the last token did not show any strong alignment signal. We also experimented with prompting the language model and taking the last token representation. The prompt we used was

An image with the caption '<caption>'. This is an image of a <fill>

Using prompting showed similar trends to average pooling but had slightly lower alignment scores.

# <span id="page-24-0"></span>D. Color Cooccurrence Experiment

Here we describe the details of how we created the four color representations visualized in Figure [8,](#page-7-1) from left to right.

Perceptual representation from CIELAB color space We embed pixels taken from the CIFAR-10 image dataset [\(Krizhevsky et al.,](#page-12-4) [2009;](#page-12-4) [Torralba et al.,](#page-15-19) [2008\)](#page-15-19) based on the CIELAB color space, which is designed as a *perceptually uniform* space that changes numerical values correspond to similar perceived changes in color.

Three representations from cooccurrence in VISION and LANGUAGE For these three representations, we first obtain a dissimilarity matrix over colors (in different ways detailed below), then use multidimensional scaling [\(Shepard,](#page-14-25) [1980\)](#page-14-25) to find a 3-dimensional embedding in which Euclidean distance between the embeddings for A and B, z<sup>A</sup> and zB, best matches this dissimilarity matrix. We use 1,000 fits and take the best match. Afterward, we visually align it with the CIELAB space by finding the best rotation, translation, scaling, and flipping, by running the Kabsch-Umeyama algorithm [\(Kabsch,](#page-12-22) [1976;](#page-12-22) [1978;](#page-12-23) [Umeyama,](#page-15-20) [1991\)](#page-15-20) twice, once on z and once on −z, to account for flipping. The dissimilarity matrix we used in each case is described as following:

- VISION: Pixel cooccurrence. We collect color cooccurrence statistics from the CIFAR-10 dataset, and estimate a joint distribution p(A, B) over 300,000 randomly sampled pixel colors A and B that occur within a radius of at most 4 pixels of one another. Colors are quantized on a grid in RGB space and represented as discrete variables, and p(A, B) is modeled as a table of normalized counts, from which we compute the empirical pointwise mutual information matrix KPMI(A, B). Quantization ensures that there is no bias from how color distances are represented in RGB space. Dissimilarity matrix is defined as −KPMI(A, B) + c, where c = maxA,B KPMI(A, B) is an offset to ensure non-negativity (similar to the constant in Section [4.2](#page-7-2) and Proposition [F.1](#page-26-1) that ensures neural networks can express KPMI).
- LANGUAGE. We used an approach similar to [Abdou et al.](#page-10-12) [\(2021\)](#page-10-12).
  - We take 20 pairs of (color, word) appeared in the dataset collected by [Lindsey & Brown](#page-13-25) [\(2014\)](#page-13-25), where 51 participants were asked to free name each of the 330 colors from the Munsell Color Chart. We filtered words that appeared less than 100 times, and computed each word's associate color by taking the centroid in CIELAB space. Our filtering process followed [Abdou et al.](#page-10-12) [\(2021\)](#page-10-12) exactly, but resulted in 20 colors, a slightly different set than the 18 colors they claimed.
  - For each of the 20 color words <col>, we construct three sentences:

```
The color <col>.
This color is <col>.
The color of this thing is <col>.
```

and obtain the average sentence embedding from the language encoder, as the embedding for <col> (details below). We find this approach more effective than [Abdou et al.](#page-10-12) [\(2021\)](#page-10-12), which uses object names that potentially have color biases, even though the objects may appear in multiple colors.

- Unlike [Abdou et al.](#page-10-12) [\(2021\)](#page-10-12), we did not perform linear regression from language embedding to CIELAB space, which distorts distances and easily overfits with only 20 samples. Instead, we used multidimensional scaling to best preserve distances, as described above.
- Masked language contrastive learning (SimCSE) embedding: We used sentence embedding from the unsupervised SimCSE RoBERTa-L [\(Gao et al.,](#page-11-16) [2021\)](#page-11-16) to encode the above sentences into 1024-dimensional embeddings, and used the pairwise Euclidean distances among <col> embeddings as the dissimilarity matrix.
- Masked language predictive learning (RoBERTa) embedding: We concatenated hidden states of the last four layers of RoBERTa-L [\(Liu et al.,](#page-13-17) [2019\)](#page-13-17), following [\(Devlin et al.,](#page-11-19) [2018\)](#page-11-19). We averaged across token dimensions, and obtained a 4096-dimensional embedding for each of the above sentences, and used the pairwise Euclidean distances among <col> embeddings as the dissimilarity matrix.

# <span id="page-25-1"></span>E. Caption Density Experiments

We use LLaMA3-8B-Instruct [\(Meta,](#page-13-22) [2024\)](#page-13-22) to generate summary captions at various densities for images in the Densely Captioned Images dataset [\(Urbanek et al.,](#page-15-14) [2023\)](#page-15-14) from the train split. Following [Urbanek et al.](#page-15-14) [\(2023\)](#page-15-14), we prompt the language model with the following instructions to generate captions at differing granularity:

system: You are given a full-text description of an image. You should summarize it into about <num\_words> words, being sure to include as much salient visual information as possible given the <num\_words> word constraint, especially information from the start of the original description. The new description should apply for the original image. Respond with only the summary, in one line.

user: <original\_caption>

We measure the alignment with this generated caption to test our hypothesis that denser captations would result in higher alignment scores. In Figure [9,](#page-9-0) we find that the alignment score also improves as caption length increases.

# F. Analysis of Contrastive Learners

#### <span id="page-25-0"></span>F.1. Contrastive objectives learn pointwise mutual information

There are two widely used forms of contrastive objectives. We now discuss each form in detail and show how they both are minimized by the pointwise mutual information (PMI) as stated in Equation [\(5\)](#page-7-0). To simplify notation, we consider learning the bivariate model g(xa, xb) ∈ **R**. In Section [4,](#page-6-0) such g is optimized within the family of {g = ⟨fX, fX⟩: f<sup>X</sup> ∈ FX}.

Recall that our positive pairs are sampled from (x, x+) ∼ Pcoor, and that the negative pairs are sampled independently from its marginals which we denote as (x, x−) i.i.d. ∼ P where P(x) = P x<sup>+</sup> Pcoor(x, x+).

1. The binary NCE loss [\(Gutmann & Hyvarinen](#page-11-17) ¨ , [2010\)](#page-11-17) is defined with a certain prior over sampling positive vs. negative pairs. Let ppos be the probability of sampling a positive pair. Then the loss is given by

$$\mathcal{L}_{\mathsf{binary-NCE}}(g) \triangleq p_{\mathsf{pos}} \cdot \mathbb{E}_{(x,x_+) \sim P_{\mathsf{coor}}} \left[ -\log \sigma(g(x,x_+)) \right] + (1 - p_{\mathsf{pos}}) \cdot \mathbb{E}_{(x,x_-) \overset{\text{i.i.d.}}{\sim} P} \left[ -\log \sigma(-g(x,x_-)) \right]. \tag{20}$$

The Bayes optimal solution is given by

$$g(x_a, x_b) = \log \frac{P(\mathsf{pos} \mid x_a, x_b)}{1 - P(\mathsf{pos} \mid x_a, x_b)}$$
 (21)

$$= \log \frac{P(\mathsf{pos}, x_a, x_b)}{P(\mathsf{neg}, x_a, x_b)} \tag{22}$$

$$= \log \frac{p_{\mathsf{pos}} \cdot P_{\mathsf{coor}}(x_a, x_b)}{(1 - p_{\mathsf{pos}})P(x_a)P(x_b)} \tag{23}$$

$$= \log \frac{P_{\mathsf{coor}}(x_a, x_b)}{P(x_a)P(x_b)} + \log \frac{p_{\mathsf{pos}}}{1 - p_{\mathsf{pos}}}$$
(24)

$$= K_{\mathsf{PMI}}(x_a, x_b) + c_X. \tag{25}$$

2. The InfoNCE loss [\(Oord et al.,](#page-13-18) [2018\)](#page-13-18) is defined with randomly sampling one positive pair along with K negative ones. With some hyperparameter τ > 0, the loss is given by

$$\mathcal{L}_{\mathsf{InfoNCE}}(g) \triangleq \mathbb{E}_{\substack{(x, x_{+}) \sim P_{\mathsf{coor}} \\ (x_{-}^{(1)}, x_{-}^{(2)}, \dots, x_{-}^{(K)}) \overset{\mathsf{i.i.d.}}{\sim} P}} \left[ -\log \frac{e^{g(x, x_{+})/\tau}}{e^{g(x, x_{+})/\tau} + \sum_{i=1}^{K} e^{g(x, x_{-}^{(i)})/\tau}} \right]. \tag{26}$$

The Bayes optimal solution is given by

$$\frac{e^{g(x,x_{+})/\tau}}{e^{g(x,x_{+})/\tau} + \sum_{i=1}^{K} e^{g(x,x_{-}^{(i)})/\tau}} = \frac{P_{\mathsf{coor}}(x_{+} \mid x) \prod_{j} P(x_{-}^{(j)})}{P_{\mathsf{coor}}(x_{+} \mid x) \prod_{j} P(x_{-}^{(j)}) + \sum_{i} P_{\mathsf{coor}}(x_{-}^{(i)} \mid x) P(x_{+}) \prod_{j \neq i} P(x_{-}^{(j)})}$$
(27)

$$= \frac{P_{\mathsf{coor}}(x_{+} \mid x)/P(x_{+})}{P_{\mathsf{coor}}(x_{+} \mid x)/P(x_{+}) + \sum_{i} P_{\mathsf{coor}}(x_{-}^{(i)} \mid x)/P(x_{-}^{(i)})}.$$
 (28)

For τ = 1, this optima corresponds to g choices where

$$g(x_a, x_b) = \log \frac{P_{\mathsf{coor}}(x_b \mid x_a)}{P(x_b)} + c_X(x_a)$$
 (29)

$$= K_{\mathsf{PMI}}(x_a, x_b) + c_X(x_a). \tag{30}$$

For the general τ ̸= 1 case, we have g (and corresponding fX) recovers KPMI up to an offset and a scale. Our main argument in Section [4](#page-6-0) that f<sup>X</sup> recovers KPMI still holds.

## <span id="page-26-0"></span>F.2. Contrastive learners can represent KPMI exactly under smoothness conditions

We want to express KPMI + C using some representation function f<sup>X</sup> : X → **R** <sup>n</sup> so that

$$\langle f_X(x_a), f_X(x_b) \rangle = K_{\text{PMI}}(x_a, x_b) + C, \quad \text{for some } C.$$
 (31)

For such an f<sup>X</sup> to exist, an equivalent criterion is that KPMI + C is positive semi-definite (PSD), as can be seen from eigendecomposition.

<span id="page-26-1"></span>Proposition F.1. *Suppose that the off-diagonal elements of* KPMI *are bounded within* [log ρmin, log ρmin + δ] ∈ (−∞, 0]*. We have* KPMI + C *is positive semi-definite (PSD) for some* C *if the joint distribution is sufficiently smooth:*

$$\frac{P_{\mathsf{coor}}(z_i \mid z_i)}{P_{\mathsf{coor}}(z_i)} \ge e^{N\delta} \rho_{\mathsf{min}}, \qquad \forall i. \tag{32}$$

*Proof.* Note that KPMI + C still only has non-positive off-diagonal elements if

<span id="page-26-3"></span>
$$-C \ge \log \rho_{\min} + \delta. \tag{33}$$

For such C, it is diagonally dominant (and thus PSD) if,

$$\forall i, \qquad K_{\mathsf{PMI}}(z_i, z_i) + C \ge \sum_{j \ne i} |K_{\mathsf{PMI}}(z_i, z_j) + C| = -(N - 1)C - \sum_{j \ne i} K_{\mathsf{PMI}}(z_i, z_j), \tag{34}$$

or equivalently,

<span id="page-26-2"></span>
$$\forall i, \qquad NC + \sum_{j} K_{\mathsf{PMI}}(z_i, z_j) \ge 0. \tag{35}$$

The following choice of C readily satisfies the above Equation [\(35\)](#page-26-2):

$$C \triangleq -\min_{i} \frac{1}{N} \sum_{j} K_{\mathsf{PMI}}(z_{i}, z_{j}). \tag{36}$$

Therefore, it remains to show that Equation [\(33\)](#page-26-3) is true. Note that

$$-C \triangleq \min_{i} \frac{1}{N} \sum_{j} K_{\mathsf{PMI}}(z_i, z_j) \ge \frac{N-1}{N} \log \rho_{\mathsf{min}} + \frac{1}{N} (\min_{i} K_{\mathsf{PMI}}(z_i, z_i)). \tag{37}$$

Therefore, it suffices to have

$$\log \rho_{\min} + \delta \le \frac{N-1}{N} \log \rho_{\min} + \frac{1}{N} (\min_{i} K_{\mathsf{PMI}}(z_{i}, z_{i})). \tag{38}$$

Rearranging terms gives the desired condition

$$\frac{P_{\mathsf{coor}}(z_i \mid z_i)}{P_{\mathsf{coor}}(z_i)} \ge e^{N\delta} \rho_{\mathsf{min}}, \qquad \forall i. \tag{39}$$

*Remark* F.2*.* Proposition [F.1](#page-26-1) is one example that a sufficiently smooth world or a sufficiently high sampling rate allows the PMI kernel KPMI to be *exactly* represented as inner products of a learned feature space (up to a scale). The condition here can be satisfied, for example, if the off-diagonal terms decay linearly with respect to N and stay sufficiently close to each other. While the condition is somewhat strict, it captures the essence that smoothness and continuity allow easier learning. Nonetheless, we note that exact representation is not necessary for convergence, and thus this requirement can likely be relaxed. Please see Section [6](#page-8-0) for discussions on practical settings.

</details>

</golden_source>