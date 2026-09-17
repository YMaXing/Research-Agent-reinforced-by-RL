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
<summary>What mathematical conditions allow PMI kernels to be exactly represented as inner products in contrastive models?</summary>

Phase: [EXPLORATION]

### Source [19]: https://arxiv.org/pdf/2309.02651

Query: What mathematical conditions allow PMI kernels to be exactly represented as inner products in contrastive models?

Answer: PMI kernels can be exactly represented as inner products if the dataset is smooth and the off-diagonal terms decay linearly. This exact representation holds under mild conditions of dataset smoothness. Mercer's theorem supports this for positive-definite kernels.

-----

Phase: [EXPLORATION]

### Source [20]: https://ojs.aaai.org/index.php/AAAI/article/view/29077/30039

Query: What mathematical conditions allow PMI kernels to be exactly represented as inner products in contrastive models?

Answer: PMI kernels can be exactly represented as inner products if the dataset is smooth and the off-diagonal terms decay linearly. This exact representation holds under mild conditions of dataset smoothness. Mercer's theorem supports this for positive-definite kernels.

-----

Phase: [EXPLORATION]

### Source [21]: https://proceedings.mlr.press/v202/dufumier23a/dufumier23a.pdf

Query: What mathematical conditions allow PMI kernels to be exactly represented as inner products in contrastive models?

Answer: PMI kernels can be exactly represented as inner products if the dataset is smooth and the off-diagonal terms decay linearly. This exact representation holds under mild conditions of dataset smoothness. Mercer's theorem supports this for positive-definite kernels.

-----

Phase: [EXPLORATION]

### Source [22]: https://mathworld.wolfram.com/InnerProduct.html

Query: What mathematical conditions allow PMI kernels to be exactly represented as inner products in contrastive models?

Answer: PMI kernels can be exactly represented as inner products if the dataset is smooth and the off-diagonal terms decay linearly. This exact representation holds under mild conditions of dataset smoothness. Mercer's theorem supports this for positive-definite kernels.

-----

</details>

<details>
<summary>What 2025-2026 benchmarks quantitatively test representational alignment across new model families and architectures?</summary>

Phase: [EXPLORATION]

### Source [23]: https://arxiv.org/html/2602.08336v2

Query: What 2025-2026 benchmarks quantitatively test representational alignment across new model families and architectures?

Answer: KRIS-Bench (Wu et al., 2025b) is a benchmark for Image Editing with 1,267 items across 7/22 categories. It evaluates unified multimodal models (UMMs) that integrate language and image processing in a single architecture for a unified representational interface. Other related benchmarks include RISEBench (Zhao et al., 2025) with 360 items, ROVER-IG (Liang et al., 2026) with 908 items, and UReason with 2,000 items for Text-to-Image. These test alignment between reasoning and visual generation quality in new multimodal architectures like those from Jiang et al. (2025), Deng et al. (2025), Jin et al. (2025), Qin et al. (2026), and Liang et al. (2026). UMMs bridge perception-oriented Vision-Language Models and specialized Visual Generation Models.

-----

Phase: [EXPLORATION]

### Source [24]: https://rewire.it/blog/genomic-foundation-models-in-2026

Query: What 2025-2026 benchmarks quantitatively test representational alignment across new model families and architectures?

Answer: GENEB is a 2026 diagnostic benchmark evaluating frozen representations from 40 genomic foundation models across 100 tasks in 13 functional categories under one unified probing protocol. It quantitatively tests representational alignment, showing that aggregate leaderboards are unstable, model rankings vary across task categories, scale provides modest gains, and architectural and pretraining alignment often outweigh parameter count. It covers tasks like variant effect prediction where models like Evo 2 and AlphaGenome set new states of the art on noncoding benchmarks without task-specific training.

-----

Phase: [EXPLORATION]

### Source [25]: https://www.emergentmind.com/topics/repa

Query: What 2025-2026 benchmarks quantitatively test representational alignment across new model families and architectures?

Answer: REPA is a framework for aligning internal representations with external pretrained features in generative diffusion models. It uses an auxiliary alignment loss with diffusion objectives for efficiency and semantic accuracy. Variants include U-REPA, REPA-E, and Video REPA for different architectures like U-Nets and video backbones. It addresses architecture sensitivity and computational overheads, with findings on encoder choice (DINOv2, SigLIP), alignment depth, and applications beyond image generation. Alignment is recommended at early-to-mid transformer layers.

-----

Phase: [EXPLORATION]

### Source [26]: https://iclr.cc/virtual/2026/workshop/10000807

Query: What 2025-2026 benchmarks quantitatively test representational alignment across new model families and architectures?

Answer: The Re-Align Workshop at ICLR 2026 focuses on representational alignment among artificial and biological neural systems. It notes 688 papers submitted to ICLR 2026 on these topics (up 51% yearly), facilitating discussion on applications like neural control via representational alignment. It builds on prior workshops addressing foundational questions of alignment across machine learning, neuroscience, and cognitive science.

-----

Phase: [EXPLORATION]

### Source [27]: https://www.preprints.org/manuscript/202601.1018

Query: What 2025-2026 benchmarks quantitatively test representational alignment across new model families and architectures?

Answer: Techniques for quantifying representational alignment include representational similarity analysis (correlations between response patterns), canonical correlation analysis, linear probing, and mutual predictability measures. These assess alignment across layers or models in large language models (Chen et al. 2025) and scientific foundation models (Edamadaka et al. 2025). The paper discusses challenges in comparing representations across architectures, datasets, and domains, noting the need for baselines accounting for dimensionality reduction and shared statistical structure.

-----

</details>

<details>
<summary>What open directions exist for applying convergent representations to improve multimodal reasoning in agentic AI?</summary>

Phase: [EXPLORATION]

### Source [28]: https://arxiv.org/html/2407.08516v5

Query: What open directions exist for applying convergent representations to improve multimodal reasoning in agentic AI?

Answer: Open directions include developing neuro-vector-symbolic architectures and program-proof-of-thoughts prompting to enhance multimodal reasoning in agentic AI. Future research focuses on integrating learned controllers and extending reasoning to multi-agent scenarios. Breakthroughs in cross-modal representation alignment and dynamic attention mechanisms are also essential.

-----

Phase: [EXPLORATION]

### Source [29]: https://www.emergentmind.com/topics/agentic-multimodal-reasoning

Query: What open directions exist for applying convergent representations to improve multimodal reasoning in agentic AI?

Answer: Open directions include developing neuro-vector-symbolic architectures and program-proof-of-thoughts prompting to enhance multimodal reasoning in agentic AI. Future research focuses on integrating learned controllers and extending reasoning to multi-agent scenarios. Breakthroughs in cross-modal representation alignment and dynamic attention mechanisms are also essential.

-----

Phase: [EXPLORATION]

### Source [30]: https://mmragi.github.io/mmragi

Query: What open directions exist for applying convergent representations to improve multimodal reasoning in agentic AI?

Answer: Open directions include developing neuro-vector-symbolic architectures and program-proof-of-thoughts prompting to enhance multimodal reasoning in agentic AI. Future research focuses on integrating learned controllers and extending reasoning to multi-agent scenarios. Breakthroughs in cross-modal representation alignment and dynamic attention mechanisms are also essential.

-----

Phase: [EXPLORATION]

### Source [31]: https://www.linkedin.com/posts/anthony-alcaraz-b80763155_agentic-ai-the-convergence-of-context-engineering-activity-7309530498840551425-tjJk

Query: What open directions exist for applying convergent representations to improve multimodal reasoning in agentic AI?

Answer: Open directions include developing neuro-vector-symbolic architectures and program-proof-of-thoughts prompting to enhance multimodal reasoning in agentic AI. Future research focuses on integrating learned controllers and extending reasoning to multi-agent scenarios. Breakthroughs in cross-modal representation alignment and dynamic attention mechanisms are also essential.

-----

Phase: [EXPLORATION]

### Source [32]: https://sra.samsung.com/wp-content/uploads/2026/03/2.1_START-CFP-Brief_Multimodal-Reasoning-Agents-for-Complex-Long-Horizon-Tasks.pdf

Query: What open directions exist for applying convergent representations to improve multimodal reasoning in agentic AI?

Answer: Open directions include developing neuro-vector-symbolic architectures and program-proof-of-thoughts prompting to enhance multimodal reasoning in agentic AI. Future research focuses on integrating learned controllers and extending reasoning to multi-agent scenarios. Breakthroughs in cross-modal representation alignment and dynamic attention mechanisms are also essential.

-----

</details>

<details>
<summary>How does biological convergent evolution parallel representational convergence across AI modalities?</summary>

Phase: [EXPLORATION]

### Source [33]: https://arxiv.org/html/2507.01966v1

Query: How does biological convergent evolution parallel representational convergence across AI modalities?

Answer: Biological convergent evolution parallels representational convergence across AI modalities by showing similar patterns of adaptation and problem-solving in unrelated systems, revealing shared strategies for complex tasks. This alignment-driven taxonomy offers a biologically grounded organizational view of the model landscape. It complements traditional task benchmarks by revealing deeper commonalities and distinctions in representational structure. These results reinforce the broader theme of our study: representational convergence between artificial and biological systems is structured and quantifiable, and emerges in systematic ways across model families, architectures, and modalities. Notably, deeper vision model layers positioned closer to the language model manifold, suggesting that as visual processing becomes more abstract, it begins to share representational properties with language processing. Brain regions followed a similar organizational pattern, with visual cortex regions (yellow stars) clustering near early and middle vision model layers, while association cortices and limbic regions (blue and purple stars) positioned closer to language model representations. This visualization provides striking evidence for a hierarchical organization of representational alignment spanning both biological and artificial systems, with deeper processing stages across modalities converging toward similar representational strategies for high-level information integration.

-----

Phase: [EXPLORATION]

### Source [34]: https://www.pnas.org/doi/10.1073/pnas.2319709121

Query: How does biological convergent evolution parallel representational convergence across AI modalities?

Answer: Biological convergent evolution parallels representational convergence across AI modalities by showing similar patterns of adaptation and problem-solving in unrelated systems, revealing shared strategies for complex tasks. Convergent evolution between Entorhinal grid cells and cosine basis functions. Examples of three Entorhinal grid neurons reflecting the typical hexagonal grid-like arrangement, and the different scales of grid distances along the entorhinal dorso-ventral axis. These grid cell images were DCT transformed and the most prominent basis function (the one with the largest coefficient of this transformation), marked by a red arrow, is depicted in the Upper-Right panels (CSB). Note the remarkable correspondence between the biological grid neurons and the CSBs, suggesting a parallel evolution between these two very different modes of representation. The specific manifestation of the convergent evolution—in this case, its appearance specifically in intermediate levels of the artificial network hierarchy—is informative about the function of the biological face-areas’ relational geometry. The fact that the correlation is found in intermediate layers rather than the uppermost, fully connected layers, which reflects the labeling of personal identity bears significance. It supports the hypothesis that human face-selective cortical regions located in the fusiform gyrus likely function as a pictorial rather than identity representation, namely, representing how faces look like rather than whose face is presented in the images.

-----

Phase: [EXPLORATION]

### Source [35]: https://hai.stanford.edu/news/intertwined-quest-understanding-biological-intelligence-and-creating-artificial-intelligence

Query: How does biological convergent evolution parallel representational convergence across AI modalities?

Answer: Biological convergent evolution parallels representational convergence across AI modalities by showing similar patterns of adaptation and problem-solving in unrelated systems, revealing shared strategies for complex tasks. Just as we have added spatial depth to our networks to achieve complex hierarchical representations, we may also need to add dynamical depth to our synapses to achieve complex temporal learning capabilities. Complex molecular states within single synapses can aid learning and memory. Taking cues from systems-level modular brain architecture. Often, current commercial AI systems involve training networks with relatively homogenous layered or recurrent architectures starting from a tabula rasa of random weights. However, this may be too hard of a problem to solve for more complex tasks. Indeed biological evolution has taken a very different path. The last common ancestor of all vertebrates lived. Seeking universal laws governing both biological and artificial intelligence. An oft-quoted trope to argue for ignoring biology in the design of AI systems involves the comparison of planes to birds. After all, if we wish to create artificial machines that propel humans into the air, it now seems ridiculous to mimic biological ingredients like feathers and flapping wings in order to invent flying machines. However, a closer inspection of this idea reveals much more nuance. The general problem of flight involves solving two fundamental problems: (1) the generation of thrust in order to move forward, and (2) the generation of lift so that we do not fall out of.

-----

Phase: [EXPLORATION]

### Source [36]: https://en.wikipedia.org/wiki/Convergent_evolution

Query: How does biological convergent evolution parallel representational convergence across AI modalities?

Answer: Biological convergent evolution parallels representational convergence across AI modalities by showing similar patterns of adaptation and problem-solving in unrelated systems, revealing shared strategies for complex tasks. Evolution at an amino acid position. In each case, the left-hand species changes from having alanine (A) at a specific position in a protein in a hypothetical ancestor, and now has serine (S) there. The right-hand species may undergo divergent, parallel, or convergent evolution at this amino acid position relative to the first species. When two species are similar in a particular character, evolution is defined as parallel if the ancestors were also similar, and convergent if they were not. Some scientists have argued that there is a continuum between parallel and convergent evolution, while others maintain that despite some overlap, there are still important distinctions between the two. The opposite of convergent evolution is divergent evolution, where related species evolve different traits. Convergent evolution is similar to parallel evolution, which occurs when two independent species evolve in the same direction and thus independently acquire similar characteristics; for instance, gliding frogs have evolved in parallel from multiple types of tree frog. Many instances of convergent evolution are known in plants, including the repeated development of C4 photosynthesis, seed dispersal by fleshy fruits adapted to be eaten by animals, and carnivory. Phylogenetic reconstruction and ancestral state reconstruction proceed by assuming that evolution has occurred without convergence. Convergent patterns may, however, appear at higher levels in a phylogenetic reconstruction, and are sometimes explicitly sought by investigators. The methods applied to infer convergent evolution depend on whether pattern-based or process-based convergence is expected. Pattern-based convergence is the broader term, for when two or more lineages independently evolve patterns of similar traits. Process-based convergence is when the convergence is due to similar forces of natural selection.

-----

Phase: [EXPLORATION]

### Source [37]: https://www.nhm.ac.uk/discover/convergent-evolution.html

Query: How does biological convergent evolution parallel representational convergence across AI modalities?

Answer: Biological convergent evolution parallels representational convergence across AI modalities by showing similar patterns of adaptation and problem-solving in unrelated systems, revealing shared strategies for complex tasks. Since DNA is the building block of life, convergent evolution starts at the level of DNA. Mutations in an individual’s DNA can result in a trait that makes them better suited to their environment. These individuals tend to survive more often than those without the beneficial trait and pass this trait on to their offspring. Over time, all individuals of a species evolve to have that trait or characteristic. This helps the species to be more successful in its habitat. It’s natural selection at work. In some examples of convergent evolution, species evolve the same solution to a problem but take a different genetic route to get there. In other cases, the convergence takes place at the molecular level and the same genetic changes occur in different species. We share the planet with a huge diversity of plants and creatures. But we can see similarities between organisms that live continents apart or are very different in other aspects. One reason for this is convergent evolution. In convergent evolution, two organisms look or behave in a very similar way, even though they’re only distantly related. This means they’ve independently evolved those similarities rather than inheriting them from a common ancestor. We observe this phenomenon all over the tree of life, from mammals and invertebrates to plants and microorganisms. Species face different challenges, called selection pressures, depending on their environment. These pressures could include which predators they encounter, what food is available or conditions such as extreme heat or cold.

-----

</details>

<details>
<summary>What historical debates in cognitive science preceded the Platonic representation hypothesis in AI?</summary>

Phase: [EXPLORATION]

### Source [38]: https://aiscientist.substack.com/p/musing-38-the-platonic-representation

Query: What historical debates in cognitive science preceded the Platonic representation hypothesis in AI?

Answer: In AI, we’ve always had a healthy debate, even tension, between such real-valued ‘continuous’ representations and symbolic representations. Cognitively, symbols play an important role in our own thinking and reasoning, and one could argue that without a symbolic component, DNNs

-----

Phase: [EXPLORATION]

### Source [39]: https://3dvar.com/Huh2024The.pdf

Query: What historical debates in cognitive science preceded the Platonic representation hypothesis in AI?

Answer: our hypothesis is also related to the notion of “convergent realism” (Newton-Smith, 1981; Putnam, 1982; Doppelt, 2007; Hardin & Rosenberg, 1982) in the philosophy of science (i.e., that science is converging on truth), and to many arguments that have been put forth in the representation learning literature (e.g., Tian et al. (2020a); Zimmermann et al.

-----

Phase: [EXPLORATION]

### Source [40]: https://www.emergentmind.com/topics/platonic-representation-hypothesis

Query: What historical debates in cognitive science preceded the Platonic representation hypothesis in AI?

Answer: Rooted in Platonic realism, this hypothesis has been developed across mathematics, geometry, cognitive science, machine learning, quantum information, and the physical sciences.

-----

Phase: [EXPLORATION]

### Source [41]: https://www.britannica.com/science/cognitive-science/Controversies

Query: What historical debates in cognitive science preceded the Platonic representation hypothesis in AI?

Answer: The history of science shows, however, that philosophical assumptions can be overthrown by powerful empirical theories. By the early 21st century, researchers in cognitive science had already generated many interesting ideas about how consciousness might be achieved through the interaction of multiple brain areas in the construction of representations of representations (see mind, philosophy of: consciousness reconsidered).

-----

Phase: [EXPLORATION]

### Source [42]: https://www.lehigh.edu/~mhb0/AIFull.pdf

Query: What historical debates in cognitive science preceded the Platonic representation hypothesis in AI?

Answer: Hermeneutics Historically, hermeneutics derives from the interpretation and understanding of historical texts; it emphasizes the intrinsic situatedness of all understanding, and the intrinsic linguistic and historical nature of all such situations of understanding (Bleicher, 1980; Gadamer, 1975, 1976; Howard, 1982; Warnke, 1987). Understanding is inextricably embedded in linguistic historical situations because understanding is always a matter of hermeneutic interpretation and reinterpretation — interpretation and reinterpretation, in turn, is always in terms of language, and is, therefore, intrinsically constituted within and from the social, cultural, and historical Current Criticisms of AI and Cognitive Science 45 sedimented ontology of that language. To try to eliminate that

-----

</details>

<details>
<summary>How are convergent representations applied in multimodal sensor fusion for robotics and neuroscience?</summary>

Phase: [EXPLORATION]

### Source [43]: https://www.emergentmind.com/topics/multimodal-sensor-fusion-strategy

Query: How are convergent representations applied in multimodal sensor fusion for robotics and neuroscience?

Answer: Multimodal sensor fusion strategy refers to the suite of theoretical frameworks, algorithmic techniques, and system architectures for integrating information streams from heterogeneous sensors—such as cameras, LiDAR, radar, inertial units, and wireless modalities—into unified, semantically coherent representations suitable for downstream tasks (e.g., detection, classification, state estimation, control). By leveraging the complementary strengths and compensating for the weaknesses of each modality, these strategies are essential to robust decision-making in fields such as autonomous driving, robotics, surveillance, intelligent manufacturing, and human activity recognition. Early CNN/RNN fusion as in "Gas Detection and Identification Using Multimodal Artificial Intelligence Based Sensor Fusion" (Narkhede et al., 2021), where concatenated feature representations from LSTM (gas time series) and CNN (thermal images) enable joint learning of cross-modal patterns.

-----

Phase: [EXPLORATION]

### Source [44]: https://www.emergentmind.com/topics/multi-modal-sensor-fusion

Query: How are convergent representations applied in multimodal sensor fusion for robotics and neuroscience?

Answer: Multi-modal sensor fusion refers to the principled integration of data from heterogeneous sensors—such as LiDAR, cameras, radar, audio, IMUs, and more—into unified representations that support robust perception, state estimation, or decision-making. By leveraging complementary sensing characteristics, sensor fusion overcomes the limitations of individual modalities, mitigates failure cases, and improves accuracy and robustness for tasks ranging from autonomous driving and robotics to human activity recognition and remote sensing. It employs multi-stage methodologies—data-level, feature-level, and decision-level fusion—using deep learning, attention mechanisms, and probabilistic models to enhance accuracy. Practical applications span autonomous driving, robotics, and remote sensing while addressing challenges like sensor misalignment, adverse conditions, and computational constraints.

-----

Phase: [EXPLORATION]

### Source [45]: https://www.linkedin.com/pulse/advancing-robotic-perception-through-multimodal-ai-anand-ramachandran-6dihe

Query: How are convergent representations applied in multimodal sensor fusion for robotics and neuroscience?

Answer: The limitations inherent to single-sensor modalities necessitate integrated approaches, leading to the emergence of multimodal sensor fusion as an essential component of modern robotic perception. Multimodal fusion systematically combines complementary sensor data to ensure reliable perception even under adverse environmental conditions. By capitalizing on sensor diversity, multimodal fusion significantly enhances robustness, accuracy, and reliability, creating richer, more comprehensive environmental representations. In autonomous vehicles, fusing radar, camera, and LiDAR data enables effective obstacle detection and navigation even under severe fog or rain. Underwater robots integrating visual, tactile, and acoustic sensors reliably execute complex manipulation tasks despite poor visibility. Advanced multimodal AI reasoning models—including OpenAI o3, Llama 3.3, Claude 3.7, and Gemini 2.0—represent powerful tools to overcome many limitations inherent to sensor fusion approaches. These sophisticated AI systems enhance robotic perception by providing contextually rich reasoning across multiple sensory inputs. For instance, Gemini 2.0 excels in dynamically interpreting ambiguous or incomplete sensor data, intelligently adapting sensor weighting to maintain accurate environmental representations even in challenging conditions such as sensor degradation or uncertainty.

-----

Phase: [EXPLORATION]

### Source [46]: https://link.springer.com/article/10.1007/s42235-026-00865-2

Query: How are convergent representations applied in multimodal sensor fusion for robotics and neuroscience?

Answer: This review argues that the path toward truly autonomous robots lies not in further refining isolated methods, but in a conscious return to neurobiological principles. We posit that the challenge of multimodal fusion is as much a fundamental scientific question inspired by biological neurology as it is an exercise in engineering pragmatism. By systematically integrating recent breakthroughs across neuroscience, computer science, and robotics, this article aims to foster cross-disciplinary convergence and chart a developmental roadmap for bio-inspired artificial intelligence. Multisensor fusion integrates information from multiple sources to enhance perception, estimation, and decision-making in intelligent systems. Traditionally, it is categorized into three hierarchical levels: data-level fusion, which combines raw sensor measurements to preserve full physical detail and support real-time state estimation (e.g., Kalman filters); feature-level fusion, which merges abstracted, often lower-dimensional representations to capture cross-modal semantic relationships; and decision-level fusion, which aggregates high-level outputs from individual classifiers or estimators for robust, modular inference (e.g., Dempster-Shafer theory). The choice among these strategies hinges on trade-offs between latency, heterogeneity, robustness, and computational cost. Despite notable progress, critical challenges in multimodal perception remain. Robotic systems must contend with heterogeneous data characteristics including varying noise levels, temporal misalignment, and dimensional mismatch. Furthermore, today’s robots fall far short of human capabilities in real-time integration of perception and action.

-----

Phase: [EXPLORATION]

### Source [47]: https://www.sciencedirect.com/topics/computer-science/multimodal-data-fusion

Query: How are convergent representations applied in multimodal sensor fusion for robotics and neuroscience?

Answer: Questions: (1) How convergent (or divergent) are approaches within single disciplines? (2) How similar are the challenges posed across different disciplines, i.e., might there be opportunity for successes in MMDF achieved in one field to inform progress in other areas as well? and (3) Where are the outstanding gaps in MMDF research, and what does this imply as targets for high impact research in the coming years? To begin to answer these questions, an apples-to-apples comparison of the literature of nine stakeholder-centric engineering domains (civil engineering, transportation, energy, environmental engineering, food engineering, critical care (healthcare), neuroscience, manufacturing/automation, and robotics) was created by quantifying the numbers and dimensionalities of modalities and

-----

</details>

<details>
<summary>What emerging trends in physics-informed AI intersect with universal representation convergence?</summary>

Phase: [EXPLORATION]

### Source [48]: https://arxiv.org/html/2506.13777v1

Query: What emerging trends in physics-informed AI intersect with universal representation convergence?

Answer: Emerging trends in physics-informed AI focus on universal representation convergence through adaptive learning and regularization techniques, enhancing generalization and predictive reliability. PINNs integrate physical laws into neural networks, improving convergence and scalability. Recent advancements aim at discovering governing equations from data. The integration of AI with physics-based modeling has emerged as a pivotal research direction for tackling complex system challenges. Traditional physics-based models, grounded in explicit mathematical formulations and fundamental laws, provide physically consistent predictions but often face computational inefficiencies and challenges in handling multi-scale dynamics. In contrast, AI-driven methods excel at capturing complex, nonlinear patterns from large-scale data but lack inherent physical constraints, limiting their reliability in data-scarce or extrapolation scenarios. Variants include conservative PINNs (CPINNs), variational hp-PINNs, and physics-constrained neural networks (PCNNs). Theoretical studies on the generalization, convergence, and error analysis of PINNs have gradually progressed, laying a preliminary mathematical foundation for their role as a tool in scientific machine learning.

-----

Phase: [EXPLORATION]

### Source [49]: https://www.mdpi.com/2673-2688/5/3/74

Query: What emerging trends in physics-informed AI intersect with universal representation convergence?

Answer: Algorithmic advancements in neural networks (NNs) are crucial for the evolution and enhancement of Physics-Informed Neural Networks (PINNs). Key breakthroughs include novel training algorithms tailored to NNs, improving efficiency, scalability, and efficacy. Adaptive learning rate schedules optimize stability and convergence, especially with non-uniform gradients or noisy data. Advanced regularization techniques, incorporating domain-specific knowledge, enhance generalization and robustness. Uncertainty quantification methods improve prediction reliability, particularly in data-scarce environments. Self-supervised and semi-supervised learning with unlabeled or partially labeled data boost performance and generalization. Model compression and pruning streamline NN complexity. Subsequent research has advanced PINNs’ capabilities, include developing adaptive activation functions and multi-fidelity approaches to address PDE stiffness and improve convergence rates. Methods incorporating physical equations into deep learning model loss functions enable training without labeled data, providing accurate predictions while respecting problem constraints and quantifying predictive uncertainty across diverse scenarios.

-----

Phase: [EXPLORATION]

### Source [50]: https://www.research.autodesk.com/projects/physics-informed-ai-seminars

Query: What emerging trends in physics-informed AI intersect with universal representation convergence?

Answer: Data-driven models have emerged as a promising approach for solving partial differential equations (PDEs) in science and engineering. Previous machine learning (ML) models typically cover only a narrow distribution of PDE problems; for example, a trained ML model for the Navier-Stokes equations usually works only for a fixed Reynolds number and domain size. To overcome these limitations, we propose a data augmentation scheme based on scale-consistency properties of PDEs and design a scale-informed neural operator that can model a wide range of scales. Our formulation leverages the fact that many PDEs possess a scale consistency under rescaling of the spatial domain, and is based on the discretization-convergent property of neural operators. Physics discovery aims to uncover governing equations from data, leveraging explainable AI techniques to identify the underlying physical laws governing a system. This approach ensures alignment with physics and provides interpretable, symbolic representations of the discovered equations, making it particularly useful in fields where the governing equations are not well known or need refinement.

-----

Phase: [EXPLORATION]

### Source [51]: https://proceedings.mlr.press/v202/podina23a.html

Query: What emerging trends in physics-informed AI intersect with universal representation convergence?

Answer: Universal Physics-Informed Neural Networks (UPINNs) enable symbolic differential operator discovery with sparse data. Hidden term neural networks can be converted into symbolic equations using symbolic regression techniques like AI Feynman. In order to achieve convergence of the neural networks, algorithms are provided with (noisy) measurements of both the initial condition as well as (synthetic) experimental data obtained at later times. Strong performance of UPINNs is demonstrated even when provided with very few measurements of noisy data in both the ODE and PDE regime. This intersects with universal representation convergence by achieving convergence of neural networks for symbolic discovery in physics-informed settings.

-----

Phase: [EXPLORATION]

### Source [52]: https://glasswing.vc/blog/rudinas-ai-atlas-1-physics-informed-neural-networks-pinns

Query: What emerging trends in physics-informed AI intersect with universal representation convergence?

Answer: Physics-informed AI can be used to “fill in the gaps” and create stronger representations in health sciences and medicine, where the human body is a mess of diverse interacting systems. In energy, Google’s DeepMind has demonstrated that such models be used in fusion science through learned plasma control to model the complexity of a reaction. In the environment and climate change, using PINNs to create digital twins allows for a more holistic understanding of the complex interactions that make up the environment.

-----

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

<research_source type="scraped_from_research" phase="exploitation" file="distinct-ai-models-seem-to-converge-on-how-they-encode-reali.md">
<details>
<summary>Distinct AI Models Seem To Converge On How They Encode Reality</summary>

Phase: [EXPLOITATION]

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

<research_source type="scraped_from_research" phase="exploration" file="from-reasoning-to-pixels-benchmarking-the-alignment-gap-in-u.md">
<details>
<summary>From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models</summary>

Phase: [EXPLORATION]

**Source URL:** <https://arxiv.org/html/2602.08336v2>

# From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models

Cheng Yang1,  Chufan Shi2,* Bo Shui3 Yaokang Wu4 Muzi Tao2 Huijuan Wang2

Ivan Yee Lee1  Yong Liu2  Xuezhe Ma2  Taylor Berg-Kirkpatrick1

1University of California San Diego  2University of Southern California

3University of Illinois Urbana-Champaign  4Carnegie Mellon University

chy085@ucsd.edu, chufansh@usc.edu

Equal Contribution. Project Page: [https://ureason.github.io](https://ureason.github.io/ "")

###### Abstract

Unified multimodal models (UMMs) aim to integrate multimodal understanding and generation within a unified architecture, yet it remains unclear to what extent their representations are truly aligned across modalities.
To investigate this question, we use reasoning-guided image generation as a diagnostic task, where models produce textual reasoning first and then generate images.
We introduce UReason, a benchmark for evaluating cross-modal alignment in this paradigm, consisting of 2,0002,000 manually curated instances spanning five reasoning-intensive tasks: Code, Arithmetic, Spatial, Attribute and Text.
To enable controlled analysis, we develop an evaluation framework that compares direct generation, reasoning-guided generation and de-contextualized generation, which conditions only on the refined prompt extracted from reasoning.
Across eight widely used UMMs, while we find that reasoning-guided generation yields improvements over direct generation, somewhat surprisingly, de-contextualized generation consistently outperforms reasoning-guided generation by a large margin.
Our results suggest that the intended visual semantics in textual reasoning are not reliably reflected in the generated images. This finding indicates that, despite unified design and training, current UMMs still do not robustly align representations across modalities. Overall, UReason serves as a practical litmus test for cross-modal alignment and provides a challenging benchmark for developing next-generation, more tightly aligned UMMs.

## 1 Introduction

The emergence of unified multimodal models has marked a significant milestone in artificial intelligence Team ( [2024](https://arxiv.org/html/2602.08336v2#bib.bib40 "")); Xie et al. ( [2024](https://arxiv.org/html/2602.08336v2#bib.bib48 "")); Zhou et al. ( [2024](https://arxiv.org/html/2602.08336v2#bib.bib52 "")); Deng et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib7 "")); Tong et al. ( [2026](https://arxiv.org/html/2602.08336v2#bib.bib43 "")).
These models integrate multimodal understanding and generation within a single architecture, aiming to learn a unified representational interface across different modalities.
In doing so, UMMs bridge the long-standing divide between perception-oriented Vision-Language Models Liu et al. ( [2023](https://arxiv.org/html/2602.08336v2#bib.bib26 "")); Team ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib41 "")); Guo et al. ( [2025b](https://arxiv.org/html/2602.08336v2#bib.bib14 "")); Huang et al. ( [2025b](https://arxiv.org/html/2602.08336v2#bib.bib17 "")) and specialized Visual Generation Models Sauer et al. ( [2023](https://arxiv.org/html/2602.08336v2#bib.bib33 "")); Betker et al. ( [2023](https://arxiv.org/html/2602.08336v2#bib.bib1 "")); Esser et al. ( [2024](https://arxiv.org/html/2602.08336v2#bib.bib8 "")); Wu et al. ( [2025a](https://arxiv.org/html/2602.08336v2#bib.bib46 "")).
However, despite operating under a unified design, it remains unclear to what extent textual and visual representations are truly aligned within these models.

To investigate this question, we propose to study _reasoning-guided image generation_ as a practical testbed for diagnosing
cross-modal alignment in UMMs.
Reasoning-guided image generation has been increasingly adopted in recent UMMs to elicit capabilities to address complex and implicit visual requirements Deng et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib7 "")); Jin et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib19 "")); Qin et al. ( [2026](https://arxiv.org/html/2602.08336v2#bib.bib31 "")); Liang et al. ( [2026](https://arxiv.org/html/2602.08336v2#bib.bib25 "")). In this paradigm, the model first produces an explicit textual reasoning, and then generates the image conditioned on that reasoning.
This paradigm provides a diagnostic setting to study the cross-modal alignment between textual and visual representations: if representations are well aligned, the target visual semantics in textual reasoning should be robustly preserved and reliably reflected in the generated images.

https://arxiv.org/html/2602.08336v2/figs/task_examples.pngFigure 1: Representative UReason instances covering Code, Arithmetic, Spatial, Attribute, and Text reasoning. Prompts specify implicit targets that must be derived via reasoning. Detailed tasks and subtasks descriptions are listed in Appx. [B](https://arxiv.org/html/2602.08336v2#A2 "Appendix B Data Annotation ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models").

To this end, we introduce UReason, a benchmark that utilizes reasoning-guided image generation as a testbed for diagnosing cross-modal alignment in UMMs (Sec. [2](https://arxiv.org/html/2602.08336v2#S2 "2 The UReason Benchmark ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")).
UReason focuses on reasoning-centric generation and contains 2,0002{,}000 manually annotated instances with verifiable evaluation criteria, spanning five task categories: Code, Arithmetic, Spatial, Attribute, and Text reasoning (Fig. [1](https://arxiv.org/html/2602.08336v2#S1.F1 "Figure 1 ‣ 1 Introduction ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")).
In each instance, models must infer an implicit visual target through multi-step reasoning and then synthesize the result visually.

To enable rigorous diagnosis, we develop the UReason Evaluation Toolkit (Sec. [3](https://arxiv.org/html/2602.08336v2#S3 "3 Evaluation Framework ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")).
Specifically, it compares three settings: _direct generation_ from the original prompt, _reasoning-guided generation_ with textual reasoning for image generation, and _de-contextualized generation_, which conditions only on the extracted refined prompt part of textual reasoning (Fig. [2](https://arxiv.org/html/2602.08336v2#S1.F2 "Figure 2 ‣ 1 Introduction ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")).
In principle, the latter two settings preserve the same visual semantics intended by the model.
This design provides a controlled framework to evaluate whether the intended visual semantics encoded in textual reasoning are faithfully reflected in visual generation.

We evaluate 88 widely used UMMs on UReason (Sec. [2](https://arxiv.org/html/2602.08336v2#S4.T2 "Table 2 ‣ 4 Experiments ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")).
Our results reveal that translating implicit targets into pixel-level outputs remains challenging: while reasoning-guided generation generally improves performance over direct generation (e.g., +11.2% for Bagel). Surprisingly, de-contextualized generation consistently outperforms reasoning-guided generation by a substantial margin (e.g., +44.8% for Bagel), suggesting that the intended visual semantics encoded in textual reasoning is not reliably reflected in generation process.

Our analyses demonstrate that textual reasoning is beneficial for high-level planning (Sec. [5](https://arxiv.org/html/2602.08336v2#S5 "5 Discussion ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")).
Specifically, UMMs can often generate reasoning that correctly specifies target visual requirements.
However, these intended visual semantics are not always faithfully reflected in the generated images, indicating that current UMMs do not fully integrate visual generation with textual reasoning despite their unified architecture and training paradigm.
Through error and attention analyses, we find that contextual interference may weaken the transfer from intended visual semantics to generated images, such as distracting tokens in intermediate results. This reflects limitations in maintaining robust cross-modal alignment.

Overall, we position UReason as a litmus test for assessing cross-modal alignment in UMMs, specifically whether generated images reflect the intended visual semantics in textual reasoning. Our results suggest that, despite unified design, current UMMs behave as though their modalities are only partially aligned, leaving substantial room for improvement.

https://arxiv.org/html/2602.08336v2/figs/case_figure.pngFigure 2: Overview of UReason evaluation framework. UReason compares 33 settings: 1 Direct Generation, 2 Reasoning-Guided Generation and 3 De-contextualized Generation.

## 2 The UReason Benchmark

Unlike traditional text-to-image benchmarks Saharia et al. ( [2022](https://arxiv.org/html/2602.08336v2#bib.bib32 "")); Lee et al. ( [2023](https://arxiv.org/html/2602.08336v2#bib.bib20 "")); Huang et al. ( [2025a](https://arxiv.org/html/2602.08336v2#bib.bib16 "")) that evaluate descriptive prompts with emphasis on aesthetic fidelity, UReason is curated to test whether implicit targets inferred via multi-step reasoning can be realized in the final visual output.
Our design is guided by two complementary considerations.
First, UReason shifts the paradigm from description to deduction: the target content is not stated verbatim and must be inferred from the input scenario, which requires multi-step reasoning such as state tracking and distractor suppression.
Second, we formulate 55 diagnostic tasks spanning Code, Arithmetic, Spatial, Attribute, and Text reasoning (Fig. [1](https://arxiv.org/html/2602.08336v2#S1.F1 "Figure 1 ‣ 1 Introduction ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")), with 3030 fine-grained subcategories (Fig. [4](https://arxiv.org/html/2602.08336v2#A2.F4 "Figure 4 ‣ Arithmetic Reasoning ‣ B.1 Task Taxonomy ‣ Appendix B Data Annotation ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")) and 2,0002{,}000 manually annotated instances, enabling identification of failure modes and supporting objective, automated evaluation with task-specific criteria.
As shown in Tab. [1](https://arxiv.org/html/2602.08336v2#S2.T1 "Table 1 ‣ 2.1 Task ‣ 2 The UReason Benchmark ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), UReason expands prior benchmarks with broader task coverage and instances, including the under-explored Code domain.

### 2.1 Task

We now introduce the 55 tasks of UReason with representative instances presented in Fig. [1](https://arxiv.org/html/2602.08336v2#S1.F1 "Figure 1 ‣ 1 Introduction ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models").

Code Reasoning.

The Code Reasoning task introduces a novel challenge to evaluate UMMs’ capacity to function as a neural visual interpreter that bridges the gap between abstract code and concrete visual rendering. Given code snippets ranging from static structural language (e.g, HTML) to executable scripts (e.g., Python), the model must transform them into their respective visual renderings through reasoning. The core challenge lies not only in syntactic recognition but also in the necessity for the model to simulate the execution process through reasoning to determine the final visual state.
Building on code knowledge gained during pre-training, UMMs are expected to first map abstract programming logic into a language description, which guides image generation.

Arithmetic Reasoning.

Arithmetic Reasoning evaluates the ability of UMMs to perform arithmetic operations within a sequential narrative.
Inputs describe scenarios where the quantity of an item changes through events such as addition or removal, and the model must generate a scene whose visible count matches the computed final state.
Specifically, this task challenges models to transcend superficial keyword matching, compelling them to act as quantitative reasoners that translate narrative fluctuations into an explicit calculation process, thereby ensuring the derived final quantity strictly constrains the visual generation.

Spatial Reasoning.

The Spatial Reasoning task assesses UMMs’ capacity to interpret complex instructions and translate them into structured visual arrangements. Unlike standard benchmarks where spatial relations are explicitly stated, our prompts contain implicit spatial cues, such as swap operations and logical constraints.
The key challenge is to resolve these high-level descriptions into a coherent coordinate-based layout before rendering the final image. This evaluates whether UMMs can reason about inter-object spatial relationships beyond surface prompt alignment.

Attribute Reasoning.

Attribute Reasoning evaluates whether UMMs can track and update object attributes under explicitly described state transitions and logical modifications (e.g., a hat being removed).
The model must generate a scene where objects strictly exhibit the final attributes implied by the prompt.
This task requires logical filtering: models must infer the terminal outcome rather than rendering intermediate states, suppressing the tendency to visualize irrelevant attributes.

Text Reasoning.

The Text Reasoning task focuses on the model’s ability to perform context-aware text rendering. In this setting, the model is provided with an input where the target text for rendering is not explicitly quoted but must be inferred from contextual rules, such as identifying the “second” and “fourth” letters of a word and get the text. The primary challenge lies in the model’s role as a symbolic reasoner: it must derive the correct answer while suppressing irrelevant information, ensuring only the final result is rendered.

| | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Benchmark | Problem | Size | Cat./ | Task Category | Evaluation | Metric Aspect |
| Setting | Sub. | Code | Arith. | Spatial | Attr. | Text | Setting | Perf. | Abl. |
| Commonsense-T2I (Fu et al., [2024](https://arxiv.org/html/2602.08336v2#bib.bib9 "")) | Text-to-Image | 150 | 5/5 | ✗ | ✗ | ✓ | ✓ | ✗ | 1 | ✓ | ✗ |
| WISE (Niu et al., [2025b](https://arxiv.org/html/2602.08336v2#bib.bib28 "")) | Text-to-Image | 1,000 | 3/25 | ✗ | ✗ | ✓ | ✓ | ✗ | 1 | ✓ | ✗ |
| R2I-Bench (Chen et al., [2025a](https://arxiv.org/html/2602.08336v2#bib.bib3 "")) | Text-to-Image | 3,068 | 7/32 | ✗ | ✓ | ✓ | ✓ | ✓ | 1 | ✓ | ✗ |
| OneIG-Bench (Chang et al., [2025](https://arxiv.org/html/2602.08336v2#bib.bib2 "")) | Text-to-Image | 2,440 | 6/26 | ✗ | ✓ | ✓ | ✓ | ✓ | 1† | ✓ | ✗ |
| T2I-ReasonBench (Sun et al., [2025](https://arxiv.org/html/2602.08336v2#bib.bib37 "")) | Text-to-Image | 800 | 4/35 | ✗ | ✗ | ✗ | ✓ | ✓ | 1† | ✓ | ✗ |
| KRIS-Bench (Wu et al., [2025b](https://arxiv.org/html/2602.08336v2#bib.bib47 "")) | Image Editing | 1,267 | 7/22 | ✗ | ✓ | ✓ | ✓ | ✓ | 1† | ✓ | ✗ |
| RISEBench (Zhao et al., [2025](https://arxiv.org/html/2602.08336v2#bib.bib51 "")) | Image Editing | 360 | 4/16 | ✗ | ✓ | ✓ | ✓ | ✗ | 1 | ✓ | ✗ |
| ROVER-IG (Liang et al., [2026](https://arxiv.org/html/2602.08336v2#bib.bib25 "")) | Image Editing | 908 | 4/17 | ✗ | ✓ | ✓ | ✓ | ✗ | 12 | ✓ | ✗ |
| UReason (Ours) | Text-to-Image | 2,000 | 5/30 | ✓ | ✓ | ✓ | ✓ | ✓ | 123 | ✓ | ✓ |

Table 1: Comparison of UReason with existing reasoning-driven image generation benchmarks.
“Cat./Sub.”: number of categories/subcategories.
Evaluation settings: 1 Direct, 2 Reasoning-Guided, 3 De-contextualized.
“Perf.”: performance evaluation; “Abl.”: ablation diagnosis.
“†” denotes benchmarks that run preliminary reasoning-chain experiments on specific models (e.g., Bagel) but primarily evaluate Direct Generation.

### 2.2 Data Curation

UReason adopts a two-stage curation pipeline to ensure that each instance requires multi-step reasoning to determine a specific visual output.
We begin with human-curated seed instances and then expand coverage through controlled LLM-assisted augmentation with human verification. Additional details about data annotation are provided in Appx. [B](https://arxiv.org/html/2602.08336v2#A2 "Appendix B Data Annotation ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models").

Human-Curated Seed Data Construction.
To guarantee the quality and diversity of UReason, human experts first establish a fine-grained taxonomy under the 55 primary tasks, resulting in 3030 subcategories in total. Specifically, detailed sub-categories are designed to cover distinct reasoning and visual perspectives. Based on this hierarchical schema, experts manually construct corresponding seed instances for each sub-category. Each instance comprises a reasoning-intensive prompt and an evaluation criterion that specifies the expected visual outcome. These seeds undergo strict validation to ensure correctness, resulting in a foundational dataset of 500500 high-quality seed instances that serve as the bedrock.

LLM-Assisted Data Augmentation.
After constructing the seed dataset, we scale UReason with a human-guided augmentation pipeline powered by Gemini-3-Pro DeepMind ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib6 "")).
Annotators systematically vary key factors of each seed instance, including the number of reasoning steps, target visual entities, and narrative context, to generate diverse yet logically consistent variants.
All candidates undergo multi-round human-LLM refinement and verification to ensure quality and correctness.
This process expands UReason to 2,0002{,}000 test instances, providing broad coverage of realistic and challenging reasoning scenarios.

Dataset Split.
We partition the 2,000 instances of UReason into two subsets: test and testmini.
The test set contains 1,500 instances, while testmini contains 500 instances and is intended for rapid validation during model development.
As reported in Appx. [D](https://arxiv.org/html/2602.08336v2#A4 "Appendix D Correlation Between Test Set and Testmini Set ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), comparative experiments show consistent trends across the two subsets.
Unless otherwise stated, we report results on testmini for efficiency in the following sections.

## 3 Evaluation Framework

### 3.1 Evaluation Settings

UMMs can understand and generate multimodal information, typically achieved through a unified architecture to enable end-to-end training and inference.
For image generation task, recent UMMs support reasoning-guided image generation, in which textual reasoning is produced before visual synthesis. As a result, image generation in UMMs differs from traditional text-to-image models in both architectural design and the training paradigm.

Previously, image generation in UMMs is commonly evaluated under two settings—direct generation and reasoning-guided generation (Sun et al., [2025](https://arxiv.org/html/2602.08336v2#bib.bib37 ""); Chang et al., [2025](https://arxiv.org/html/2602.08336v2#bib.bib2 "")). To more systematically diagnose cross-modal alignment in reasoning-guided image generation, we introduce an additional de-contextualized generation setting as a controlled comparison. As shown in Tab. [1](https://arxiv.org/html/2602.08336v2#S2.T1 "Table 1 ‣ 2.1 Task ‣ 2 The UReason Benchmark ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), we evaluate UMMs under the following three settings.

Setting 1: Direct Generation.

As illustrated in Fig. [2](https://arxiv.org/html/2602.08336v2#S1.F2 "Figure 2 ‣ 1 Introduction ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") (
1), this setting evaluates a model’s ability to generate an image directly from the original prompt without explicitly producing textual reasoning.
Given a prompt PP and a UMM MM, the generated image II is:

| | | | |
| --- | --- | --- | --- |
| | I=M​(P).I=M(P). | | (1) |

This setting serves as the baseline for reasoning-guided generation and quantifies performance without any additional textual reasoning.

Setting 2: Reasoning-Guided Generation.

As illustrated in Fig. [2](https://arxiv.org/html/2602.08336v2#S1.F2 "Figure 2 ‣ 1 Introduction ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") (
2), the model generates a reasoning trace RR followed by the output image II, conditioned on the prompt PP.
Crucially, both RR and II are produced within the same model and context window.
Formally:

| | | | |
| --- | --- | --- | --- |
| | \[R,I\]=M​(P).\[R,I\]=M(P). | | (2) |

This setting follows the standard chain-of-thought style adaptation for visual generation and measures the net effect of textual reasoning Deng et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib7 "")).
The reasoning trace is defined as R=\[Rt,Rp\]R=\[R\_{t},R\_{p}\], where RtR\_{t} denotes intermediate thoughts and RpR\_{p} denotes a refined prompt that explicitly summarizes the intended visual specification.

Setting 3: De-contextualized Generation.

As shown in Fig. [2](https://arxiv.org/html/2602.08336v2#S1.F2 "Figure 2 ‣ 1 Introduction ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") (
3), after producing the reasoning trace R=\[Rt,Rp\]R=\[R\_{t},R\_{p}\] in Setting 2, we discard the original prompt PP and the intermediate thoughts RtR\_{t}, and generate the image conditioned only on the refined prompt RpR\_{p}:

| | | | |
| --- | --- | --- | --- |
| | I=M​(Rp).I=M(R\_{p}). | | (3) |

As a result, this setting serves as a controlled comparison to reasoning-guided generation: since the refined prompt RpR\_{p} is extracted from RR in Setting 2, both settings encode the same intended visual semantics in the textual space. In principle, if textual reasoning and visual generation are well aligned, Setting 2 and Setting 3 should lead to comparable performance.

### 3.2 Evaluation Metric

Each test instance in UReason specifies an instance-specific, verifiable ground-truth criterion, enabling objective and scalable evaluation across all tasks.
We therefore report two complementary metrics.
_Visual Verification Accuracy_ measures whether a generated image satisfies the ground-truth criterion.
_Performance Gain_ measures accuracy differences between settings under our ablation protocol in practice.

Visual Verification Accuracy.
For each test instance, UReason provides a ground-truth criterion CC that specifies the expected visual outcome under correct reasoning.
The criterion is instance-specific and focuses on objectively verifiable attributes.
Given a generated image II, we define an indicator function 𝕀​(I,C)\\mathbb{I}(I,C) that returns 11 if II satisfies CC, and 0 otherwise.
The overall visual verification accuracy over a dataset of NN instances is then computed as:

| | | | |
| --- | --- | --- | --- |
| | Accuracy=1N​∑i=1N𝕀​(Ii,Ci).\\text{Accuracy}=\\frac{1}{N}\\sum\_{i=1}^{N}\\mathbb{I}(I\_{i},C\_{i}). | | (4) |

For example, in Arithmetic reasoning, CC specifies the exact object count (Fig. [1](https://arxiv.org/html/2602.08336v2#S1.F1 "Figure 1 ‣ 1 Introduction ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")). To implement 𝕀​(⋅,⋅)\\mathbb{I}(\\cdot,\\cdot) at scale, we employ Qwen3-VL-235B-A22B Team ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib41 "")) as our automated evaluator Zhao et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib51 "")); Niu et al. ( [2025b](https://arxiv.org/html/2602.08336v2#bib.bib28 "")); Chen et al. ( [2025a](https://arxiv.org/html/2602.08336v2#bib.bib3 "")); Wu et al. ( [2025b](https://arxiv.org/html/2602.08336v2#bib.bib47 "")).
We use prompting templates that ask the evaluator to perform focused verification against CC. The prompt template is provided in Appx. [K](https://arxiv.org/html/2602.08336v2#A11 "Appendix K Prompts ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models").

Performance Gain.
To further compare and analyze the contribution of different contextual information for the reasoning-driven image generation, we measure the performance improvement between consecutive settings. Let ii and jj denote two settings in our evaluation protocol with i<ji<j.
We define the performance gain from ii to jj as:

| | | | |
| --- | --- | --- | --- |
| | Δi→j=Accuracyj−Accuracyi\\Delta\_{i\\rightarrow j}=\\text{Accuracy}\_{j}-\\text{Accuracy}\_{i} | | (5) |

We focus on two key transitions: Δ1→2\\Delta\_{1\\rightarrow 2} quantifies the benefit of incorporating reasoning for image generation, while Δ2→3\\Delta\_{2\\rightarrow 3} measures the performance gap between Setting 2 and Setting 3 , which are designed to preserve the same final intended visual semantics.

## 4 Experiments

| | | | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | Setting | Code | Arithmetic | Spatial | Attribute | Text | Overall |
| Acc | Δ\\Delta | Acc | Δ\\Delta | Acc | Δ\\Delta | Acc | Δ\\Delta | Acc | Δ\\Delta | Acc | Δ\\Delta |
| Bagel | 1 | 10.0 | - | 5.0 | - | 3.0 | - | 6.0 | - | 9.0 | - | 6.6 | - |
| 2 | 30.0 | +20.0 | 14.0 | +9.0 | 15.0 | +12.0 | 19.0 | +13.0 | 11.0 | +2.0 | 17.8 | +11.2 |
| 3 | 58.0 | +28.0 | 51.0 | +37.0 | 58.0 | +43.0 | 60.0 | +41.0 | 86.0 | +75.0 | 62.6 | +44.8 |
| UniCoT-v2 | 1 | 9.0 | - | 2.0 | - | 2.0 | - | 5.0 | - | 3.0 | - | 4.2 | - |
| 2 | 27.0 | +18.0 | 19.0 | +17.0 | 29.0 | +27.0 | 21.0 | +16.0 | 21.0 | +18.0 | 23.4 | +19.2 |
| 3 | 65.0 | +38.0 | 45.0 | +26.0 | 46.0 | +17.0 | 67.0 | +46.0 | 87.0 | +66.0 | 62.0 | +38.6 |
| SRUM | 1 | 11.0 | - | 4.0 | - | 3.0 | - | 6.0 | - | 7.0 | - | 6.2 | - |
| 2 | 25.0 | +14.0 | 8.0 | +4.0 | 20.0 | +17.0 | 24.0 | +18.0 | 6.0 | -1.0 | 16.6 | +10.4 |
| 3 | 67.0 | +42.0 | 50.0 | +42.0 | 50.0 | +30.0 | 50.0 | +26.0 | 82.0 | +76.0 | 59.8 | +43.2 |
| Bagel-Zebra-CoT | 1 | 7.0 | - | 7.0 | - | 2.0 | - | 10.0 | - | 5.0 | - | 6.2 | - |
| 2 | 14.0 | +7.0 | 10.0 | +3.0 | 15.0 | +13.0 | 23.0 | +13.0 | 10.0 | +5.0 | 14.4 | +8.2 |
| 3 | 50.0 | +36.0 | 43.0 | +33.0 | 33.0 | +18.0 | 48.0 | +25.0 | 85.0 | +75.0 | 51.8 | +37.4 |
| ThinkMorph | 1 | 9.0 | - | 1.0 | - | 4.0 | - | 3.0 | - | 10.0 | - | 5.4 | - |
| 2 | 19.0 | +10.0 | 12.0 | +11.0 | 15.0 | +11.0 | 26.0 | +23.0 | 5.0 | -5.0 | 15.4 | +10.0 |
| 3 | 49.0 | +30.0 | 37.0 | +25.0 | 45.0 | +30.0 | 55.0 | +29.0 | 71.0 | +66.0 | 51.4 | +36.0 |
| UniCoT | 1 | 12.0 | - | 3.0 | - | 6.0 | - | 12.0 | - | 8.0 | - | 8.2 | - |
| 2 | 33.0 | +21.0 | 18.0 | +15.0 | 26.0 | +20.0 | 21.0 | +9.0 | 12.0 | +4.0 | 22.0 | +13.8 |
| 3 | 57.0 | +24.0 | 42.0 | +24.0 | 50.0 | +24.0 | 42.0 | +21.0 | 52.0 | +40.0 | 48.6 | +26.6 |
| T2I-R1 | 1 | 3.0 | - | 6.0 | - | 4.0 | - | 9.0 | - | 2.0 | - | 4.8 | - |
| 2 | 6.0 | +3.0 | 4.0 | -2.0 | 2.0 | -2.0 | 11.0 | +2.0 | 3.0 | +1.0 | 5.2 | +0.4 |
| 3 | 20.0 | +14.0 | 15.0 | +11.0 | 12.0 | +10.0 | 27.0 | +16.0 | 47.0 | +44.0 | 24.2 | +19.0 |
| UniMoE2 | 1 | 5.0 | - | 4.0 | - | 2.0 | - | 10.0 | - | 4.0 | - | 5.0 | - |
| 2 | 10.0 | +5.0 | 3.0 | -1.0 | 3.0 | +1.0 | 12.0 | +2.0 | 6.0 | +2.0 | 6.8 | +1.8 |
| 3 | 17.0 | +7.0 | 13.0 | +10.0 | 8.0 | +5.0 | 21.0 | +9.0 | 13.0 | +7.0 | 14.4 | +7.6 |

Table 2: Model performance across three evaluation settings on UReason. Acc and Δ\\Delta denote visual verification accuracy (%) and performance gain over the previous setting, respectively. 1, 2, and 3 represent Direct Generation, Reasoning-Guided Generation and De-contextualized Generation, respectively.

### 4.1 Models

We benchmark 88 widely utilized open-source UMMs trained to perform reasoning-guided image generation: Bagel Deng et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib7 "")), SRUM Jin et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib19 "")), UniCoT, UniCoT-v2 Qin et al. ( [2026](https://arxiv.org/html/2602.08336v2#bib.bib31 "")), ThinkMorph Gu et al. ( [2026](https://arxiv.org/html/2602.08336v2#bib.bib12 "")), Bagel-Zebra-CoT Li et al. ( [2026](https://arxiv.org/html/2602.08336v2#bib.bib21 "")), Uni-MoE2 Li et al. ( [2025a](https://arxiv.org/html/2602.08336v2#bib.bib22 "")) and T2I-R1 Jiang et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib18 "")). We do not evaluate closed-source model like Nano Banana Pro Google ( [2026](https://arxiv.org/html/2602.08336v2#bib.bib11 "")), since its reasoning traces are not accessible 111 [https://ai.google.dev/gemini-api/docs/thinking](https://ai.google.dev/gemini-api/docs/thinking ""), making it difficult to apply our trace-based diagnostic protocol as detailed in Appx. [H](https://arxiv.org/html/2602.08336v2#A8 "Appendix H Discussion on Closed-Source Systems ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models").

### 4.2 Main Results

Tab. [2](https://arxiv.org/html/2602.08336v2#S4.T2 "Table 2 ‣ 4 Experiments ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") reports the performance of all evaluated models under our 33 diagnostic settings.

Direct Prompting Performs Poorly on Implicit Targets.
Direct Generation yields uniformly low accuracy across models and tasks with overall performance around 5% to 8%.
This demonstrates that direct text-to-image mapping is fundamentally insufficient to solve UReason, as the target visual content is intentionally implicit and must be derived through multi-step reasoning before visual generation.

Chain-of-Thought Reasoning Enhances Generation Capabilities.
Comparing Direct Generation with Reasoning-Guided Generation, introducing explicit chain-of-thought reasoning consistently improves overall performance across most models, with gains ranging from +8.2% (Bagel-Zebra-CoT) to +19.2% (UniCoT-v2).
These results indicate that CoT can effectively elicit reasoning behaviors that benefit unified multimodal generation.
A concrete illustration of this benefit emerges in the Code task.
In Direct Generation, models frequently fail to map raw syntax, such as HTML tags, into coherent visual layouts.
In contrast, Reasoning-Guided Generation enables models to first translate the code into a description of the intended rendering, which provides a more interpretable conditioning signal for subsequent image synthesis.
For example, Bagel improves from 10.0% to 30.0% on Code, and UniCoT improves from 12.0% to 33.0%.

De-contextualized Generation Consistently Outperforms Reasoning-Guided Generation.
While Reasoning-Guided Generation improves performance over Direct Generation, De-contextualized Generation yields an even larger gain.
As shown in Tab. [2](https://arxiv.org/html/2602.08336v2#S4.T2 "Table 2 ‣ 4 Experiments ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), accuracy increases from Reasoning-Guided Generation to De-contextualized Generation for every model, reaching +44.8% for Bagel, +43.2% for SRUM and +26.6% for UniCoT.
This result is notable because the two settings are designed to preserve the same intended visual semantics.
In principle, if textual reasoning is reliably reflected in visual generation, these two settings should yield comparable performance.
Their consistent gap therefore suggests that, despite a unified architecture and training in reasoning-guided image generation, current UMMs still exhibit fragile cross-modal alignment between textual reasoning and visual generation.

## 5 Discussion

In this section, we further discuss the cross-modal alignment gap between textual reasoning and visual generation by analyzing reasoning chain correctness, internal prompt rewriting, the reliability of automated evaluation and attention analysis.

| | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Model | Code | Arith. | Spatial | Attr. | Text | Overall |
| Bagel | 93.0 | 94.0 | 88.0 | 96.0 | 96.0 | 93.4 |
| SRUM | 91.0 | 91.0 | 88.0 | 93.0 | 95.0 | 91.6 |
| UniCoT | 84.0 | 70.0 | 84.0 | 99.0 | 95.0 | 86.4 |
| ThinkMorph | 83.0 | 82.0 | 85.0 | 96.0 | 91.0 | 87.4 |
| Bagel-Zebra-CoT | 75.0 | 89.0 | 79.0 | 94.0 | 92.0 | 85.8 |

Table 3: Reasoning chain quality evaluation. We report the accuracy (%) of generated reasoning chains against ground-truth criteria across tasks.

Evaluating the Quality of Reasoning Chain.
To localize the performance bottleneck, we ask whether failures originate from incorrect reasoning in intended visual semantics.
We evaluate correctness of reasoning-chain RR against ground-truth criteria using Qwen3-235B-A22B as an LLM-as-judge (see Appx. [K](https://arxiv.org/html/2602.08336v2#A11 "Appendix K Prompts ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") for details).
As shown in Tab. [3](https://arxiv.org/html/2602.08336v2#S5.T3 "Table 3 ‣ 5 Discussion ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), models achieve consistently high reasoning accuracy, with Bagel reaching 93.4% overall.
This suggests that UMMs can often infer the ground-truth visual target and produce coherent specifications. Therefore, the dominant challenge lies in faithfully realizing these specifications in pixels.

https://arxiv.org/html/2602.08336v2/x1.pngFigure 3: Comparison of internal (Bagel) and external (Qwen) prompt models across 55 tasks.

UMMs as Intrinsic Prompt Models.
Modern online T2I systems employ an external “prompt model” to rewrite instructions before image synthesis (e.g., Qwen-Image 222 [https://qwen-image.ai](https://qwen-image.ai/ "")), highlighting prompt optimization as a practical component of T2I pipelines. A key advantage of UMMs is that they can perform this refinement end-to-end, without depending on an external LLM.
To quantify this capability, we compare Bagel’s self-generated refined prompts with external prompt models based on Qwen2.5-7B, Qwen3-8B, and Qwen3-235B-A22B.
As shown in Fig. [3](https://arxiv.org/html/2602.08336v2#S5.F3 "Figure 3 ‣ 5 Discussion ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), Bagel outperforms its LLM backbone Qwen2.5-7B and achieves performance comparable to stronger prompt models, including Qwen3-8B and Qwen3-235B-A22B.
These results suggest that UMMs are native self-prompt models, offering a promising end-to-end alternative to the two-stage prompt-rewrite-then-generate pipeline.

Ablating the Effect of Context Length.

| | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Model | Input | Code | Arith. | Spatial | Attr. | Text | Overall |
| Bagel | 1×Rp1\\times R\_{p} | 58.0 | 51.0 | 58.0 | 60.0 | 86.0 | 62.6 |
| 4×Rp4\\times R\_{p} | 63.0 | 49.0 | 52.0 | 53.0 | 85.0 | 60.4 |
| 8×Rp8\\times R\_{p} | 58.0 | 46.0 | 48.0 | 47.0 | 84.0 | 56.6 |
| ThinkMorph | 1×Rp1\\times R\_{p} | 49.0 | 37.0 | 45.0 | 55.0 | 71.0 | 51.4 |
| 4×Rp4\\times R\_{p} | 46.0 | 34.0 | 37.0 | 55.0 | 73.0 | 49.0 |
| 8×Rp8\\times R\_{p} | 44.0 | 33.0 | 34.0 | 51.0 | 73.0 | 47.0 |
| Bagel-Zebra-CoT | 1×Rp1\\times R\_{p} | 50.0 | 43.0 | 33.0 | 48.0 | 85.0 | 51.8 |
| 4×Rp4\\times R\_{p} | 53.0 | 38.0 | 30.0 | 42.0 | 77.0 | 48.0 |
| 8×Rp8\\times R\_{p} | 49.0 | 36.0 | 25.0 | 38.0 | 74.0 | 44.4 |

Table 4: Length-controlled ablation. 1×1\\times/4×4\\times/8×8\\timesRpR\_{p} denotes the refined prompt repeated once, four, or eight
times, where 4×Rp4\\times R\_{p} approximates the average token length
of a full reasoning trace in our evaluation.

To determine whether the observed performance drop is due to longer contextual sequences, we conduct a length-controlled ablation. In this setup, the refined prompt RpR\_{p} is repeated 4×4\\times or 8×8\\times without introducing any new semantic content.
As shown in Tab. [4](https://arxiv.org/html/2602.08336v2#S5.T4 "Table 4 ‣ 5 Discussion ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), artificially lengthening the context causes a relatively minor overall performance decline (at most −6.0%-6.0\\% for Bagel at 8×8\\times), which is drastically smaller than the −44.8%-44.8\\% gap observed between Reasoning-Guided Generation and De-contextualized Generation.
Moreover, the evaluated UMMs are explicitly trained for reasoning-guided image generation. We further examine the training length distributions of representative models (Appx. [E](https://arxiv.org/html/2602.08336v2#A5 "Appendix E Context Length Statistics for Training and Evaluation ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")) and verify that the UReason evaluation sequences fall well within their typical training ranges, indicating no out-of-distribution length pressure.

Correlation with Human Evaluation.
To validate the reliability of our automated evaluation, we conduct a correlation study against human judgments.
For images generated by UniCoT across all three settings, human experts assess whether each image satisfies the ground-truth criterion.
Comparing judgments from Qwen3-VL-235B-A22B against human assessments yields strong agreement with a consistency of 0.9240.924.
For reasoning chains under Setting 2 (Tab. [3](https://arxiv.org/html/2602.08336v2#S5.T3 "Table 3 ‣ 5 Discussion ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")), human experts judge whether each chain satisfies the ground-truth criterion, achieving a consistency of 0.9620.962 with Qwen3-235B-A22B.
These results demonstrate that our task design, which provides concrete and verifiable criteria such as exact object counts and specific text strings, enables reliable evaluation with state-of-the-art MLLM/LLM evaluators. Details on human evaluation is provided in Appx. [G.2](https://arxiv.org/html/2602.08336v2#A7.SS2 "G.2 Details on Human Evaluation ‣ Appendix G Discussion on Evaluation Metrics ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models").

| | | | |
| --- | --- | --- | --- |
| Layers | PP | RtR\_{t} | RpR\_{p} |
| 1–7 | 3.98 | 5.50 | 9.79 |
| 8–14 | 3.11 | 4.22 | 8.24 |
| 15–21 | 0.20 | 0.30 | 0.79 |
| 22–28 | 0.12 | 0.21 | 0.58 |
| 1–28 | 1.85 | 2.56 | 4.85 |

Table 5: Average attention weights across layers for Bagel during image generation, scaled by 10−410^{-4}.

Attention Analysis.

To better understand why the same intended visual semantics can lead to different generation outcomes, we conduct an attention analysis on Bagel.
Specifically, during image generation, we extract the average attention weights assigned to three token groups: PP, RtR\_{t}, and RpR\_{p}.
As shown in Table [5](https://arxiv.org/html/2602.08336v2#S5.T5 "Table 5 ‣ 5 Discussion ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), the model allocates a substantial portion of its attention to PP and RtR\_{t}, particularly in the early to middle layers.
Across layers, the attention paid to the intermediate reasoning trace RtR\_{t} remains more than half of that assigned to the refined prompt RpR\_{p}.
This pattern suggests that image generation remains highly sensitive to contextual interference, which may compete with the final visual specification for attention and weaken the transfer from intended visual semantics to pixels.
This pattern suggests that cross-modal alignment in UMMs is not yet robust to contextual interference, despite their unified architecture and training.
In Appx. [F](https://arxiv.org/html/2602.08336v2#A6 "Appendix F Details on Attention Analysis ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), we provide further details together with additional analyses. We hope these findings motivate future work on UMMs that better preserve the intended visual semantics during cross-modal transfer.

Error Analysis.

To understand failure modes, error cases from Bagel under Setting 2 are analyzed, identifying four error types: (1) Reasoning Errors (5.8%): incorrect reasoning chains, such as miscalculating object counts; (2) Instruction Misinterpretation. (10.6%): misinterpreting prompt intent, such as rendering text as words rather than objects; (3) Concept Hallucination (8.2%): generating unspecified objects; (4) Task-Specific Errors (75.4%): failing to realize task requirements despite correct reasoning. The dominance of task-specific errors highlights the cross-modal alignment gap: even when models derive the correct visual intent in textual reasoning, they often fail to faithfully realize it in the generated image. This result demonstrates UReason’s effectiveness as a diagnostic benchmark for fine-grained failure analysis. Representative error cases and detailed analysis are provided in Appx. [J](https://arxiv.org/html/2602.08336v2#A10 "Appendix J Case Study ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models").

## 6 Related Work

Unified Multimodal Models.
Unified multimodal models aim to support multimodal understanding and generation within a single model, typically by mapping text and images into a shared representational interface and enabling flexible multimodal interleavings.
Recent approaches span diffusion-based models Li et al. ( [2025c](https://arxiv.org/html/2602.08336v2#bib.bib24 "")); Swerdlow et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib38 "")); Shi et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib36 "")), autoregressive models Team ( [2024](https://arxiv.org/html/2602.08336v2#bib.bib40 "")); Wang et al. ( [2024](https://arxiv.org/html/2602.08336v2#bib.bib44 "")); Wu et al. ( [2025a](https://arxiv.org/html/2602.08336v2#bib.bib46 "")); Chen et al. ( [2025c](https://arxiv.org/html/2602.08336v2#bib.bib5 "")); Tong et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib42 "")), and hybrids that combine both mechanisms Zhou et al. ( [2024](https://arxiv.org/html/2602.08336v2#bib.bib52 "")); Xie et al. ( [2024](https://arxiv.org/html/2602.08336v2#bib.bib48 "")); Deng et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib7 "")).
Despite these advances, characterizing cross-modal interactions and the interplay between understanding and generation remains an active research area Yan et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib49 "")); Liang et al. ( [2026](https://arxiv.org/html/2602.08336v2#bib.bib25 "")); Niu et al. ( [2025a](https://arxiv.org/html/2602.08336v2#bib.bib27 "")); Zhang et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib50 "")).
UReason complements this line of work by providing a diagnostic evaluation of cross-modal alignment, specifically how textual reasoning influences visual generation.

Chain-of-Thought.
Chain-of-thought reasoning has emerged as a powerful technique to enhance the capabilities of LLMs Wei et al. ( [2022](https://arxiv.org/html/2602.08336v2#bib.bib45 "")); Chen et al. ( [2025b](https://arxiv.org/html/2602.08336v2#bib.bib4 "")) and MLLMs Li et al. ( [2025b](https://arxiv.org/html/2602.08336v2#bib.bib23 "")). Recent large reasoning models (OpenAI, [2024](https://arxiv.org/html/2602.08336v2#bib.bib29 ""); [2025](https://arxiv.org/html/2602.08336v2#bib.bib30 ""); Guo et al., [2025a](https://arxiv.org/html/2602.08336v2#bib.bib13 "")) further demonstrate that test-time scaling, achieved through iterative reasoning, enables more accurate outcomes.
UMMs integrate processing for language and image within a single architecture, which provides a natural foundation for reasoning-guided image generation. Consequently, recent works (Jiang et al., [2025](https://arxiv.org/html/2602.08336v2#bib.bib18 ""); Deng et al., [2025](https://arxiv.org/html/2602.08336v2#bib.bib7 ""); Jin et al., [2025](https://arxiv.org/html/2602.08336v2#bib.bib19 ""); Qin et al., [2026](https://arxiv.org/html/2602.08336v2#bib.bib31 ""); Liang et al., [2026](https://arxiv.org/html/2602.08336v2#bib.bib25 "")) have adopted explicit reasoning chains to plan via natural language before synthesizing images. Despite the appeal of this reasoning-guided paradigm, the actual alignment between reasoning and visual generation quality remains underexplored, motivating our systematic investigation in this area.

T2I Benchmarks.
T2I benchmarks have progressed from evaluating explicit prompt adherence to probing implicit reasoning capabilities.
Prior work focuses on generation quality via text-image alignment Saharia et al. ( [2022](https://arxiv.org/html/2602.08336v2#bib.bib32 "")); Ghosh et al. ( [2023](https://arxiv.org/html/2602.08336v2#bib.bib10 "")); Lee et al. ( [2023](https://arxiv.org/html/2602.08336v2#bib.bib20 "")), compositional generation Huang et al. ( [2023](https://arxiv.org/html/2602.08336v2#bib.bib15 "")), and safety constraints Schramowski et al. ( [2023](https://arxiv.org/html/2602.08336v2#bib.bib34 "")); Seshadri et al. ( [2024](https://arxiv.org/html/2602.08336v2#bib.bib35 "")).
More recent benchmarks target reasoning-driven scenarios that require commonsense and world knowledge Fu et al. ( [2024](https://arxiv.org/html/2602.08336v2#bib.bib9 "")); Niu et al. ( [2025b](https://arxiv.org/html/2602.08336v2#bib.bib28 "")); Chen et al. ( [2025a](https://arxiv.org/html/2602.08336v2#bib.bib3 "")); Sun et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib37 "")); Chang et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib2 "")).
UReason complements this line of work with probing cross-modality alignment between textual reasoning and visual generation in UMMs.

## 7 Conclusion

We introduce UReason, a diagnostic benchmark for reasoning-guided image generation in unified multimodal models, with 55 verifiable tasks and a controlled framework comparing direct, reasoning-guided, and de-contextualized generation.
Across 88 open-source models, we observe that reasoning improves over direct prompting, the intended visual semantics expressed in textual reasoning are not always faithfully reflected in the generated images, and conditioning only on the refined prompt often performs best.
These findings suggest that advancing UMMs requires not only stronger reasoning capabilities, but also more robust cross-modal alignment to ensure that inferred visual semantics can be reliably carried through the image generation process.

## Appendix A LLM Disclosure

We use Gemini-3-Pro to conduct LLM-Assisted Data Augmentation as detailed in
Section [B](https://arxiv.org/html/2602.08336v2#A2 "Appendix B Data Annotation ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"). LLMs are used to assist with drafting
and polishing paper text. No LLMs are used to originate research ideas.

## Appendix B Data Annotation

### B.1 Task Taxonomy

To guarantee the quality and diversity of UReason, human experts first establish a fine-grained taxonomy spanning 30 subcategories under the five primary tasks (Fig. [4](https://arxiv.org/html/2602.08336v2#A2.F4 "Figure 4 ‣ Arithmetic Reasoning ‣ B.1 Task Taxonomy ‣ Appendix B Data Annotation ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")). Each subcategory is designed to isolate a distinct reasoning capability or visual aspect, intentionally focusing on fundamental operations and visual characteristics. This granular design enables convenient and precise error localization and diagnostic analysis. Importantly, these subcategories are not mutually exclusive and can be combined to construct test cases when needed.

##### Code Reasoning

UReason defines eight subcategories for Code Reasoning based on programming languages, covering object-oriented languages (Python, C#, C++, Java), front-end technologies (HTML, CSS, JavaScript), SQL for data querying, and various programming paradigms. Models are required to understand language-specific syntax, control flow, data structures, and computational logic to simulate code execution and determine the final visual rendering. This comprehensive coverage ensures that models must possess broad code comprehension capabilities across different programming ecosystems. Notably, code snippets are designed such that their visual outputs involve arithmetic counts, spatial layouts, attribute constraints, and text rendering.

##### Arithmetic Reasoning

UReason defines seven subcategories for Arithmetic Reasoning covering different operational complexities and object configurations. Single-Type (St) and Multi-Type (Mt) subcategories distinguish scenarios based on object diversity, while Add (Add), Subtract (Sub), Multiply (Mul), Divide (Div), and Transfer (Trf) subcategories focus on specific arithmetic operations. Models are required to perform sequential numerical reasoning through narrative events, tracking quantity changes dynamically and ensuring that the final visual output strictly reflects the calculated object count. This demands models to transcend superficial keyword matching and function as quantitative reasoners.

https://arxiv.org/html/2602.08336v2/x2.pngFigure 4: Taxonomy of UReason tasks. The benchmark contains 55 task categories with 3030 fine-grained subcategories covering diverse reasoning and visual generation challenges.

##### Spatial Reasoning

UReason defines six subcategories for Spatial Reasoning covering different spatial arrangement paradigms: Horizontal (Hor), Vertical (Ver), Grid (Grd), Absolute (Abs), Relative (Rel), and Constraint (Cst). These subcategories assess models’ capacity to resolve high-level semantic descriptions into structured coordinate-based layouts. Unlike standard benchmarks where spatial relationships are explicitly stated, models must infer spatial configurations from implicit cues, logical constraints, and relational reasoning. The Constraint subcategory particularly challenges models to act as spatial reasoners that interpret and satisfy predefined placement rules and restrictions—such as “object A cannot be adjacent to object B” or “all red objects must be on the left side”—before determining the final spatial arrangement that complies with all specified constraints.

##### Attribute Reasoning

UReason defines five subcategories for Attribute Reasoning based on different object properties: Color (Clr), Shape (Shp), Texture (Tex), Presence (Prs) and Position (Pos). These subcategories evaluate models’ capability to track and update object attributes through state transitions and logical modifications described in the text. Models must perform logical filtering to derive the terminal outcome rather than rendering initial or intermediate states, effectively suppressing visual biases toward irrelevant attributes mentioned in the prompt. This requires maintaining attribute consistency throughout complex state evolution narratives.

##### Text Reasoning

UReason defines four subcategories for Text Reasoning based on the granularity of textual elements: Character (Chr), Word (Wrd), Number (Num), and Symbol (Sym). These subcategories assess models’ ability to perform context-aware text inference at different semantic levels. Models must derive the target text through contextual rules, linguistic transformations, mathematical operations, or symbolic reasoning, rather than directly rendering explicitly quoted strings. This requires models to act as symbolic reasoners that suppress irrelevant information and render only the logically derived final result.

### B.2 Annotation Pipeline

In this section, we provide comprehensive details about the data curation process of UReason, including the human-curated seed data construction, LLM-assisted augmentation pipeline, and data statistics.

#### B.2.1 Human-Curated Seed Data Construction

##### Annotator Background.

Our annotation team consists of 5 expert annotators with professional backgrounds in computer vision and natural language processing. All annotators possess at least a Master’s degree in computer science, with an average of 3 years of experience in AI research.

##### Taxonomy Design Process.

The design of our fine-grained taxonomy follows a systematic, multi-stage approach. We first identify five primary reasoning dimensions—Code, Arithmetic, Spatial, Attribute, and Text—based on a literature review of reasoning capabilities in language models and an analysis of real-world visual generation requirements. For each primary category, we conduct brainstorming sessions with human annotators to identify representative subcategories, with selection criteria emphasizing coverage of diverse reasoning patterns, distinctiveness in targeting specific skills, verifiability for objective evaluation and practical relevance to real-world use cases. We then conduct a pilot study with 10 instances per subcategory to verify feasibility. After iterative refinement, we establish the final taxonomy comprising 3030 subcategories across 55 main tasks, as illustrated in Fig. [4](https://arxiv.org/html/2602.08336v2#A2.F4 "Figure 4 ‣ Arithmetic Reasoning ‣ B.1 Task Taxonomy ‣ Appendix B Data Annotation ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models").

##### Seed Instance Construction Details.

Expert annotators manually construct seed instances following specific design principles:

As shown in Fig. [1](https://arxiv.org/html/2602.08336v2#S1.F1 "Figure 1 ‣ 1 Introduction ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), for prompt design, each prompt necessitates intermediate reasoning steps to derive the visual target. While the target remains implicit, the prompt provides sufficient information for a unique, deterministic solution. For evaluation criterion design, each criterion specifies a concrete, verifiable aspect of the generated image, such as exact object counts, specific text strings, or precise spatial relationships. We specify exact values rather than ranges for quantitative attributes and define clear verification rules for qualitative attributes. Different task categories employ tailored criterion formats: Arithmetic tasks specify exact object counts after all operations, Spatial tasks define precise positional relationships or arrangements, Attribute tasks indicate final resolved object attributes, Text tasks require exact text strings to be rendered, and Code tasks encompass all four of the above aspects.

Notably, our early pilot experiments reveal that excessively large quantities or lengthy text strings pose significant challenges for current UMMs, prompting us to adjust the difficulty levels accordingly in our annotation process.

#### B.2.2 LLM-Assisted Data Augmentation

We use Gemini-3-Pro DeepMind ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib6 "")) for data augmentation based on its strong performance in instruction following and creative generation. For each seed instance, we systematically vary three key dimensions to generate diverse yet logically consistent variants. First, we adjust reasoning complexity by adding or removing reasoning steps, introducing distractor information, while maintaining similar difficulty. Second, we vary target visual objects through type substitution with semantically related alternatives, quantity adjustments within reasonable ranges, and attribute modifications including colors, shapes, sizes or textures. Third, we modify narrative scenarios by changing contextual backgrounds, varying linguistic styles, common sense scenarios, scientific phenomena, or everyday situations. This multi-dimensional augmentation strategy ensures comprehensive coverage of reasoning patterns while maintaining the logical consistency and verifiability of each instance.

##### Human-LLM Interaction Workflow.

The augmentation process follows a structured multi-round interaction protocol. In the initial generation round, the LLM generates multiple candidate variants for each seed instance. Human annotators then review all candidates and categorize them as accepted, requiring revision, or rejected. For variants requiring revision, annotators provide specific feedback on issues. The LLM subsequently generates revised versions based on this feedback. All accepted and revised variants undergo final human verification and discussion among annotators to ensure their correctness, diversity, stylistic variation, and overall quality.

#### B.2.3 Data Statistics

| | | | | | | |
| --- | --- | --- | --- | --- | --- | --- |
| Category | Code | Arithmetic | Spatial | Attribute | Text | Overall |
| Count | 400 | 400 | 400 | 400 | 400 | 2000 |
| Subcategories | 8 | 7 | 6 | 5 | 4 | 30 |
| Prompt Length (AVG.) | 113.14 | 131.44 | 169.27 | 97.78 | 79.66 | 118.26 |
| Prompt Length (STD.) | 51.61 | 13.11 | 35.90 | 18.79 | 8.33 | 42.97 |

Table 6: Statistics of UReason across different tasks.

Tab. [6](https://arxiv.org/html/2602.08336v2#A2.T6 "Table 6 ‣ B.2.3 Data Statistics ‣ B.2 Annotation Pipeline ‣ Appendix B Data Annotation ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") presents the statistics of UReason. The benchmark comprises 2,0002,000 instances evenly distributed across five task categories (400400 each), spanning 3030 fine-grained subcategories. Subcategory counts reflect each domain’s scope: Code encompasses 88 programming languages, while Arithmetic, Spatial, Attribute, and Text contain 77, 66, 55, and 44 subcategories respectively. Prompt lengths are measured using the Qwen3-8B tokenizer.

## Appendix C Details on Evaluation Settings

Our evaluation settings are designed to diagnose whether visual generation in reasoning-guided image generation faithfully reflects the intended visual semantics expressed in textual reasoning, thereby providing a controlled lens on cross-modal alignment in UMMs.

UMMs typically support two generation modes: _Direct Generation_, which generates an image directly from the user instruction, and _Reasoning-Guided Generation_, which generates textual reasoning for image generation. We additionally introduce _De-contextualized Generation_, which conditions image generation only on the model’s intended visual specification333In this paper, we use _intended visual semantics_ to refer to the visual target in the abstract representational space, and _intended visual specification_ to refer to its expression in concrete textual form..

A key design choice is how to obtain this intended visual specification.
Rather than relying on an external model or human annotation to summarize the reasoning trace, we explicitly require the evaluated model to output a refined prompt, RpR\_{p}, at the end of the reasoning trace.
This refined prompt serves as the model’s own textual summary of the final visual target, i.e., the intended visual semantics that the model aims to realize in the image.

This design is important for fairness and comparability.
In principle, one could attempt to infer the intended visual semantics directly from the textual reasoning trace.
However, doing so would typically require an additional summarization step, often involving an external model, to convert reasoning trace into a concise visual specification.
Such a multi-stage pipeline would introduce additional model bias and cumulative error, making it harder to attribute performance differences to the evaluated UMM itself.
By instead requiring the model to explicitly produce RpR\_{p}, we ensure that the de-contextualized setting uses the model’s own final visual specification while avoiding confounding effects from external summarization.

This formulation also brings practical benefits.
Because RpR\_{p} is explicitly expressed in text, it provides an interpretable representation of the intended visual semantics for downstream analysis.
This supports not only a fair comparison between Reasoning-Guided Generation and De-contextualized Generation, but also subsequent analyses of reasoning chains and attention behavior discussed in the paper.

| | | | | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Model | Test Set | Setting | Code | Arithmetic | Spatial | Attribute | Text | Overall |
| Acc | Δ\\Delta | Acc | Δ\\Delta | Acc | Δ\\Delta | Acc | Δ\\Delta | Acc | Δ\\Delta | Acc | Δ\\Delta |
| Bagel | testmini | 1 | 10.0 | - | 5.0 | - | 3.0 | - | 6.0 | - | 9.0 | - | 6.6 | - |
| 2 | 30.0 | +20.0 | 14.0 | +9.0 | 15.0 | +12.0 | 19.0 | +13.0 | 11.0 | +2.0 | 17.8 | +11.2 |
| 3 | 58.0 | +28.0 | 51.0 | +37.0 | 58.0 | +43.0 | 60.0 | +41.0 | 86.0 | +75.0 | 62.6 | +44.8 |
| test | 1 | 12.0 | - | 8.0 | - | 6.0 | - | 5.0 | - | 10.0 | - | 8.2 | - |
| 2 | 33.0 | +21.0 | 18.0 | +10.0 | 16.0 | +10.0 | 21.0 | +16.0 | 13.0 | +3.0 | 20.2 | +12.0 |
| 3 | 60.0 | +27.0 | 54.0 | +36.0 | 59.0 | +43.0 | 63.0 | +42.0 | 87.0 | +74.0 | 64.6 | +44.4 |
| UniCoT | testmini | 1 | 12.0 | - | 3.0 | - | 6.0 | - | 12.0 | - | 8.0 | - | 8.2 | - |
| 2 | 33.0 | +21.0 | 18.0 | +15.0 | 26.0 | +20.0 | 21.0 | +9.0 | 12.0 | +4.0 | 22.0 | +13.8 |
| 3 | 57.0 | +24.0 | 42.0 | +24.0 | 50.0 | +24.0 | 42.0 | +21.0 | 52.0 | +40.0 | 48.6 | +26.6 |
| test | 1 | 13.0 | - | 5.0 | - | 9.0 | - | 13.0 | - | 9.0 | - | 9.8 | - |
| 2 | 37.0 | +24.0 | 18.0 | +13.0 | 31.0 | +22.0 | 24.0 | +11.0 | 15.0 | +6.0 | 25.0 | +15.2 |
| 3 | 57.0 | +20.0 | 46.0 | +28.0 | 54.0 | +23.0 | 42.0 | +18.0 | 57.0 | +42.0 | 51.2 | +26.2 |
| SRUM | testmini | 1 | 11.0 | - | 4.0 | - | 3.0 | - | 6.0 | - | 7.0 | - | 6.2 | - |
| 2 | 25.0 | +14.0 | 8.0 | +4.0 | 20.0 | +17.0 | 24.0 | +18.0 | 6.0 | -1.0 | 16.6 | +10.4 |
| 3 | 67.0 | +42.0 | 50.0 | +42.0 | 50.0 | +30.0 | 50.0 | +26.0 | 82.0 | +76.0 | 59.8 | +43.2 |
| test | 1 | 10.0 | - | 5.0 | - | 6.0 | - | 10.0 | - | 9.0 | - | 8.0 | - |
| 2 | 27.0 | +17.0 | 10.0 | +5.0 | 23.0 | +17.0 | 28.0 | +18.0 | 10.0 | +1.0 | 19.6 | +11.6 |
| 3 | 69.0 | +42.0 | 49.0 | +39.0 | 53.0 | +30.0 | 55.0 | +27.0 | 85.0 | +75.0 | 62.2 | +42.6 |
| ThinkMorph | testmini | 1 | 9.0 | - | 1.0 | - | 4.0 | - | 3.0 | - | 10.0 | - | 5.4 | - |
| 2 | 19.0 | +10.0 | 12.0 | +11.0 | 15.0 | +11.0 | 26.0 | +23.0 | 5.0 | -5.0 | 15.4 | +10.0 |
| 3 | 49.0 | +30.0 | 37.0 | +25.0 | 45.0 | +30.0 | 55.0 | +29.0 | 71.0 | +66.0 | 51.4 | +36.0 |
| test | 1 | 12.0 | - | 3.0 | - | 5.0 | - | 5.0 | - | 13.0 | - | 7.6 | - |
| 2 | 23.0 | +11.0 | 16.0 | +13.0 | 18.0 | +13.0 | 27.0 | +22.0 | 9.0 | -4.0 | 18.6 | +11.0 |
| 3 | 48.0 | +25.0 | 35.0 | +19.0 | 46.0 | +28.0 | 53.0 | +26.0 | 68.0 | +59.0 | 50.0 | +31.4 |

Table 7: Performance comparison on testmini and test sets across different models and settings. Acc and Δ\\Delta denote visual verification accuracy (%) and performance gain over the previous setting, respectively. 1, 2, and 3 represent Direct Generation, Reasoning-Guided Generation and De-contextualized Generation, respectively.

## Appendix D Correlation Between Test Set and Testmini Set

Tab. [7](https://arxiv.org/html/2602.08336v2#A3.T7 "Table 7 ‣ Appendix C Details on Evaluation Settings ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") reports the detailed performance of four unified multimodal models (Bagel, UniCoT, SRUM, and ThinkMorph) across all three evaluation settings on both test and testmini sets.
The results demonstrate strong consistency between the two subsets. The consistent trends and minimal performance gaps suggest that testmini effectively mirrors the full test set, serving as a reliable and efficient evaluation subset for model development, particularly for researchers with limited computational resources.

## Appendix E Context Length Statistics for Training and Evaluation

| | | |
| --- | --- | --- |
| Model | Training Length (# tokens) | UReason Eval Length (# tokens) |
| ThinkMorph | 490.8 (276.7) | 316.3 (154.8) |
| Bagel-Zebra-CoT | 476.4 (474.4) | 256.7 (123.4) |

Table 8: Token length comparison between model training data and UReason evaluation contexts. Mean (Std.) reported. Prompt lengths are measured using the Qwen3-8B tokenizer.

The UMMs evaluated in our experiments are all explicitly post-trained for reasoning-guided image generation, which helps avoid the concern that the reasoning-style context or their lengths are out of distribution for the models.
To further verify that the performance degradation observed in Reasoning-guided Generation is not attributable to context lengths, we compare the token lengths of open-source reasoning-guided image generation training data for ThinkMorph (Gu et al., [2026](https://arxiv.org/html/2602.08336v2#bib.bib12 "")) and Bagel-Zebra-CoT (Li et al., [2026](https://arxiv.org/html/2602.08336v2#bib.bib21 "")), both of which explicitly include reasoning-guided image generation data, against the average textual context length encountered during UReason evaluation. As shown in Tab. [8](https://arxiv.org/html/2602.08336v2#A5.T8 "Table 8 ‣ Appendix E Context Length Statistics for Training and Evaluation ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), UReason evaluation sequences are consistently shorter than the models’ training distribution across both models, confirming that the models are not exposed to unprecedented sequence lengths.

## Appendix F Details on Attention Analysis

### F.1 Attention Weight Computation

To explore the causal mechanisms, we conduct an attention analysis on Bagel Deng et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib7 "")) in Sec. [5](https://arxiv.org/html/2602.08336v2#S5.T5 "Table 5 ‣ 5 Discussion ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"). Here, we present more details on the attention analysis. To analyze attention during image generation, we consider three semantic groups in the input sequence: the original prompt PP, the intermediate reasoning trace RtR\_{t}, and the refined prompt RpR\_{p}. At each diffusion timestep, for each layer ℓ\\ell, the attention weight matrix 𝐀(ℓ)∈ℝH×Lq×Lk\\mathbf{A}^{(\\ell)}\\in\\mathbb{R}^{H\\times L\_{q}\\times L\_{k}} captures the normalized attention each query token assigns to every key token, where HH is the number of attention heads, and LqL\_{q}, LkL\_{k} denote the query and key sequence lengths, respectively. The query tokens correspond to the visual generation tokens produced during image synthesis, while the key tokens span the full input context including PP, RtR\_{t}, and RpR\_{p}. The attention received by each token group is obtained by averaging over the corresponding key positions and attention heads:

| | | | |
| --- | --- | --- | --- |
| | a¯𝒢(ℓ)=1H​∑h=1H1\|𝒢\|​∑j∈𝒢𝐀h,:,j(ℓ)\\bar{a}^{(\\ell)}\_{\\mathcal{G}}=\\frac{1}{H}\\sum\_{h=1}^{H}\\frac{1}{\|\\mathcal{G}\|}\\sum\_{j\\in\\mathcal{G}}\\mathbf{A}^{(\\ell)}\_{h,:,j} | | (6) |

where 𝒢∈{P,Rt,Rp}\\mathcal{G}\\in\\{P,\\,R\_{t},\\,R\_{p}\\} denotes the index set of tokens belonging to each group. The final reported values are averaged across all evaluated samples, all diffusion timesteps, and all query tokens within each of the four contiguous layer groups (layers 1–7, 8–14, 15–21, and 22–28).

### F.2 Qualitative Token Influence Analysis

To provide a more intuitive understanding of contextual interference, we further visualize token influence maps following DAAM Tang et al. ( [2023](https://arxiv.org/html/2602.08336v2#bib.bib39 "")). For each target noun token within RtR\_{t}, we isolate its attention weights from 𝐀(ℓ)\\mathbf{A}^{(\\ell)} and aggregate them across diffusion timesteps and layers, producing maps that highlight the pixel-level regions most strongly influenced by each token. As shown in Figure [5](https://arxiv.org/html/2602.08336v2#A6.F5 "Figure 5 ‣ F.2 Qualitative Token Influence Analysis ‣ Appendix F Details on Attention Analysis ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), even when the logical flow within RtR\_{t} correctly deduces that “cream” should be excluded, the image still contains cream. Moreover, the token “cream” is primarily associated with the cream region in the generated image through cross-attention. To further corroborate this, we manually select a local region in the generated image where cream appears, and compute the attention scores from the corresponding visual generation tokens to all textual tokens. As shown in Figure [8](https://arxiv.org/html/2602.08336v2#A6.F8 "Figure 8 ‣ F.2 Qualitative Token Influence Analysis ‣ Appendix F Details on Attention Analysis ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), “cream” ranks among the top-10 most attended textual tokens for that region, excluding special tokens (e.g., start/end of sentence token). Together, these findings suggest that visual synthesis can be influenced by the mere presence of a token in the conditioning context. More broadly, they indicate that, despite their unified architecture and training, current UMMs still exhibit fragile coupling between textual reasoning and visual generation, with even basic contextual interference remaining substantial.

Additional qualitative cases are provided in Figures [6](https://arxiv.org/html/2602.08336v2#A6.F6 "Figure 6 ‣ F.2 Qualitative Token Influence Analysis ‣ Appendix F Details on Attention Analysis ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") and [7](https://arxiv.org/html/2602.08336v2#A6.F7 "Figure 7 ‣ F.2 Qualitative Token Influence Analysis ‣ Appendix F Details on Attention Analysis ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), with their corresponding attention score analyses detailed in Figures [9](https://arxiv.org/html/2602.08336v2#A6.F9 "Figure 9 ‣ F.2 Qualitative Token Influence Analysis ‣ Appendix F Details on Attention Analysis ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") and [10](https://arxiv.org/html/2602.08336v2#A6.F10 "Figure 10 ‣ F.2 Qualitative Token Influence Analysis ‣ Appendix F Details on Attention Analysis ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models").

https://arxiv.org/html/2602.08336v2/figs/attention_analysis_1.pngFigure 5: Qualitative token influence maps following
DAAM Tang et al. ( [2023](https://arxiv.org/html/2602.08336v2#bib.bib39 "")). Although RtR\_{t} correctly deduces that sour cream should be
excluded, the token “cream” (highlighted in red) still induces strong localized
attention in the attention layers, correlating with the
region where sour cream is generated. This suggests that
token presence can influence visual synthesis independently
of the surrounding logical context, bypassing the constraints
of the refined prompt RpR\_{p}.https://arxiv.org/html/2602.08336v2/figs/attention_analysis_2.pngFigure 6: Qualitative token influence maps following DAAM Tang et al. ( [2023](https://arxiv.org/html/2602.08336v2#bib.bib39 "")). Although RtR\_{t} correctly deduces that the “Orange Carrot” in the top-left should be replaced by a radish, the mere presence of the “Orange” (highlighted in red) token still induces strong localized attention in the attention layers. This correlates directly with the top-left quadrant where an orange carrot is erroneously generated, suggesting that token presence can influence visual synthesis independently of the surrounding logical context, bypassing the constraints of the refined prompt RpR\_{p}.https://arxiv.org/html/2602.08336v2/figs/attention_analysis_3.pngFigure 7: Qualitative token influence maps following DAAM Tang et al. ( [2023](https://arxiv.org/html/2602.08336v2#bib.bib39 "")). Although RtR\_{t} correctly deduces from the C# code that sunglasses should be removed, the token “sunglasses”(highlighted in red) still induces strong localized attention in the attention layers, correlating with the region where sunglasses are erroneously generated. This suggests that token presence can influence visual synthesis independently of the surrounding logical context, bypassing the constraints of the refined prompt RpR\_{p}.https://arxiv.org/html/2602.08336v2/x3.pngFigure 8: Top-10 attended textual tokens for the cream region
in the generated image, measured by aggregating attention
scores from the corresponding visual generation tokens to all
textual tokens. The token “cream” appears three times in the
full context: once in PP, once in RtR\_{t} (highlighted in red
in Figure [5](https://arxiv.org/html/2602.08336v2#A6.F5 "Figure 5 ‣ F.2 Qualitative Token Influence Analysis ‣ Appendix F Details on Attention Analysis ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")), and once in RpR\_{p}.
We compute the attention scores for the highlighted occurrence
in RtR\_{t}, which ranks among the top-10 most attended textual
tokens for the cream region, excluding special tokens. The
other two occurrences of “cream” in PP and RpR\_{p} rank
16 and 48, respectively.https://arxiv.org/html/2602.08336v2/x4.pngFigure 9: Top-10 attended textual tokens for the erroneously generated carrot region
in the top-left quadrant of the image, measured by aggregating attention
scores from the corresponding visual generation tokens to all
textual tokens. We compute the attention scores for the occurrence
of the token “Orange” (from “Orange Carrot”) within RtR\_{t}
(highlighted in red in Figure [6](https://arxiv.org/html/2602.08336v2#A6.F6 "Figure 6 ‣ F.2 Qualitative Token Influence Analysis ‣ Appendix F Details on Attention Analysis ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")). This
specific instance ranks as the highest attended object-specific token for the
region.
The notably high attention score suggests that the mere presence of the “Orange”
token within the reasoning trace contributes strongly to the
erroneous visual manifestation of the carrot in the generated image,
overriding the intended spatial execution logic.https://arxiv.org/html/2602.08336v2/x5.pngFigure 10: Top-10 attended textual tokens for the sunglasses region
in the generated image, measured by aggregating attention
scores from the corresponding visual generation tokens to all
textual tokens. We compute the attention scores for the occurrence
of the token “sunglasses” within RtR\_{t}
(highlighted in red in Figure [7](https://arxiv.org/html/2602.08336v2#A6.F7 "Figure 7 ‣ F.2 Qualitative Token Influence Analysis ‣ Appendix F Details on Attention Analysis ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models")). This
specific instance ranks as the highest attended textual token for the
sunglasses region, excluding special tokens. The disproportionately
high attention score suggests that the mere presence of the “sunglasses”
token within the reasoning trace contributes most strongly to the
erroneous visual manifestation of sunglasses in the generated image,
overriding the intended execution logic.

### F.3 Attention Analysis on ThinkMorph and T2I-R1

| | | | |
| --- | --- | --- | --- |
| Layers | PP | RtR\_{t} | RpR\_{p} |
| 1–7 | 2.45 | 4.57 | 6.93 |
| 8–14 | 1.71 | 3.32 | 5.33 |
| 15–21 | 0.12 | 0.21 | 0.43 |
| 22–28 | 0.08 | 0.12 | 0.34 |
| 0–27 | 1.09 | 2.06 | 3.26 |

Table 9: Average attention weights across layers for ThinkMorph during image generation, scaled by 10−410^{-4}.

| | | | |
| --- | --- | --- | --- |
| Layers | PP | RtR\_{t} | RpR\_{p} |
| 1–10 | 2.57 | 3.56 | 4.01 |
| 11–20 | 1.17 | 2.19 | 2.73 |
| 21–30 | 1.08 | 1.83 | 4.21 |
| 1–30 | 1.61 | 2.53 | 3.65 |

Table 10: Average attention weights across layers for T2I-R1 during image generation, scaled by 10−410^{-4}.

To further validate our findings beyond a single model, we additionally conduct the same attention analysis on ThinkMorph Gu et al. ( [2026](https://arxiv.org/html/2602.08336v2#bib.bib12 "")) and T2I-R1 Jiang et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib18 "")), which generates images in an autoregressive manner. Specifically, we extract the average attention weights assigned to the three token groups PP, RtR\_{t}, and RpR\_{p} following the same procedure described above. The results are consistent with our observations on Bagel: for UMMs, visual generation remains highly sensitive to surrounding context, which may compete with the final visual specification for attention and weaken the transfer from intended visual semantics to pixels.

## Appendix G Discussion on Evaluation Metrics

### G.1 Details on MLLM-as-a-Judge

Unlike evaluations that test open-ended and subjective alignment, UReason evaluates strictly verifiable ground-truth criteria—such as exact object counts and specific text strings.
By relying on these deterministic criteria, we frame the evaluation as a binary Visual Question Answering (VQA) problem (i.e., Yes/No judgment) rather than an open-ended assessment of overall image quality.
This formulation minimizes evaluator bias and ensures strict objectivity, serving as a robust methodology widely adopted when evaluating images against deterministic targets Zhao et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib51 "")); Niu et al. ( [2025b](https://arxiv.org/html/2602.08336v2#bib.bib28 "")); Chen et al. ( [2025a](https://arxiv.org/html/2602.08336v2#bib.bib3 "")); Wu et al. ( [2025b](https://arxiv.org/html/2602.08336v2#bib.bib47 "")).

### G.2 Details on Human Evaluation

https://arxiv.org/html/2602.08336v2/figs/data_label_interface.pngFigure 11: Screenshot of the interface used for human evaluation.

To validate the reliability of the automated evaluation metric
described in Sec. [3.2](https://arxiv.org/html/2602.08336v2#S3.SS2 "3.2 Evaluation Metric ‣ 3 Evaluation Framework ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), we conduct a human evaluation study. Specifically, we evaluate
all 500500 instances in the testmini set using the UniCoT
model, with each instance assessed under all three diagnostic
settings: Direct Generation, Reasoning-Guided Generation and
De-contextualized Generation. This yields a total of 1,5001{,}500
generated images and 500500 generated reasoning traces to be
assessed.

##### Evaluators.

Our evaluation panel consists of three graduate students, all
holding Master’s degrees in Computer Science with research
experience in computer vision or natural language processing.

##### Annotation Task and Interface.

A screenshot of the annotation interface is provided in
Figure [11](https://arxiv.org/html/2602.08336v2#A7.F11 "Figure 11 ‣ G.2 Details on Human Evaluation ‣ Appendix G Discussion on Evaluation Metrics ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"). Each generated image and reasoning
trace is paired with its corresponding ground-truth criterion CC,
which specifies a concrete and verifiable target outcome. The
annotation task is framed as an objective binary judgment problem:
given a generated image or reasoning trace alongside the criterion,
the evaluator judges whether it satisfies CC, selecting either
Yes or No. This binary formulation minimizes subjectivity and
aligns directly with our automated metric. Each evaluator annotated all 1,5001{,}500 image–criterion pairs and
500500 reasoning-trace–criterion pairs, without access to the
judgments of others.

##### Disagreement Resolution.

In cases where all three evaluators agree, the consensus label is
directly adopted as the ground-truth annotation. In cases of
disagreement, the three evaluators convene in a discussion session
to jointly review the image or reasoning trace alongside the
criterion and reach a final unanimous decision. The resolved label
is recorded only after full consensus is achieved, ensuring that
every ground-truth annotation is unambiguous.

##### Correlation Computation.

We treat the final human-annotated labels after disagreement
resolution as ground-truth binary scores and compare them against
the binary scores produced by our automated evaluators,
Qwen3-VL-235B-A22B and Qwen3-235B-A22B. The correlation between
the two sets of judgments is measured as the proportion of instances on which the automated evaluator and the human panel reach the same label. As reported
in Sec. [5](https://arxiv.org/html/2602.08336v2#S5 "5 Discussion ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") and Appx. [G.2](https://arxiv.org/html/2602.08336v2#A7.SS2 "G.2 Details on Human Evaluation ‣ Appendix G Discussion on Evaluation Metrics ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), the automated evaluators achieve
label matching rates of 0.9240.924 and 0.9620.962 with human judgments
on the two sub-tasks, respectively, confirming the reliability of
our automated pipeline as a scalable proxy for human judgment on
UReason’s criterion-grounded binary evaluation tasks.

### G.3 Experiments on Alternative Evaluators

| | | | | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Evaluator | Setting | Code | Arithmetic | Spatial | Attribute | Text | Overall |
| Acc | Δ\\Delta | Acc | Δ\\Delta | Acc | Δ\\Delta | Acc | Δ\\Delta | Acc | Δ\\Delta | Acc | Δ\\Delta |
| Qwen3-VL-235B-A22B | 1 | 12.0 | - | 3.0 | - | 6.0 | - | 12.0 | - | 8.0 | - | 8.2 | - |
| 2 | 33.0 | +21.0 | 18.0 | +15.0 | 26.0 | +20.0 | 21.0 | +9.0 | 12.0 | +4.0 | 22.0 | +13.8 |
| 3 | 57.0 | +24.0 | 42.0 | +24.0 | 50.0 | +24.0 | 42.0 | +21.0 | 52.0 | +40.0 | 48.6 | +26.6 |
| Gemini-2.5-Pro | 1 | 10.0 | - | 4.0 | - | 7.0 | - | 10.0 | - | 9.0 | - | 8.0 | - |
| 2 | 30.0 | +20.0 | 18.0 | +14.0 | 23.0 | +16.0 | 17.0 | +7.0 | 9.0 | 0.0 | 19.4 | +11.4 |
| 3 | 53.0 | +23.0 | 40.0 | +22.0 | 47.0 | +24.0 | 43.0 | +26.0 | 48.0 | +39.0 | 46.2 | +26.8 |
| Gemini-3.1-Pro | 1 | 10.0 | - | 3.0 | - | 6.0 | - | 10.0 | - | 8.0 | - | 7.4 | - |
| 2 | 31.0 | +21.0 | 16.0 | +13.0 | 23.0 | +17.0 | 15.0 | +5.0 | 10.0 | +2.0 | 19.0 | +11.6 |
| 3 | 52.0 | +21.0 | 41.0 | +25.0 | 48.0 | +25.0 | 40.0 | +25.0 | 45.0 | +35.0 | 45.2 | +26.2 |

Table 11: Alternative evaluator results on the UniCoT model. Acc and Δ\\Delta denote visual verification accuracy (%) and performance gain over the previous setting, respectively. 1, 2, and 3represent Direct Generation, Reasoning-Guided Generation and De-contextualized Generation, respectively.

Unlike prompts that test open-ended and subjective alignment, UReason evaluates strictly verifiable criteria—such as exact object counts and specific text strings. By relying on these deterministic criteria, we frame the evaluation as a binary visual question answering (VQA) problem (i.e., Yes/No judgment) rather than an open-ended assessment of overall image quality. This formulation minimizes evaluator bias and ensures strict objectivity, a robust methodology widely adopted when evaluating images against deterministic targets Zhao et al. ( [2025](https://arxiv.org/html/2602.08336v2#bib.bib51 "")); Niu et al. ( [2025b](https://arxiv.org/html/2602.08336v2#bib.bib28 "")); Chen et al. ( [2025a](https://arxiv.org/html/2602.08336v2#bib.bib3 "")); Wu et al. ( [2025b](https://arxiv.org/html/2602.08336v2#bib.bib47 "")). We have demonstrated its high correlation with human evaluation in Sec. [5](https://arxiv.org/html/2602.08336v2#S5 "5 Discussion ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") and Appx. [G.2](https://arxiv.org/html/2602.08336v2#A7.SS2 "G.2 Details on Human Evaluation ‣ Appendix G Discussion on Evaluation Metrics ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models").

To further demonstrate that our evaluation results are robust, we employ two stronger, closed-source model, Gemini-2.5-Pro and Gemini-3.1-Pro as alternative automated evaluators. We utilize alternative evaluators to assess the UniCoT model under all three settings.

As shown in Table [11](https://arxiv.org/html/2602.08336v2#A7.T11 "Table 11 ‣ G.3 Experiments on Alternative Evaluators ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), while minor absolute differences exist—attributable to Gemini-2.5-Pro and Gemini-3.1-Pro’s differing baseline VQA capabilities (human correlation: 0.941, 0.950) compared to Qwen3-VL-235B-A22B (human correlation: 0.924)—the relative performance trends across all three settings remain highly consistent. Crucially, Gemini-2.5-Pro and Gemini-3.1-Pro replicates the experimental findings, demonstrating significant performance gains in De-contextualized Generation over Reasoning-Guided Generation. The consistent nature of this performance drop across different evaluators confirms that the insufficient cross-modal alignment is a robust bottleneck in UMMs, rather than an artifact of the evaluation metric.

## Appendix H Discussion on Closed-Source Systems

We acknowledge the emergence of proprietary reasoning-supported image generation systems, such as Nano Banana Pro 444 [https://ai.google.dev/gemini-api/docs/nanobanana](https://ai.google.dev/gemini-api/docs/nanobanana ""). According to its technical documentation 555 [https://ai.google.dev/gemini-api/docs/image-generation](https://ai.google.dev/gemini-api/docs/image-generation ""), this architecture by default employs an iterative inference paradigm: it executes an initial reasoning phase, synthesizes a preliminary visual draft, performs a reasoning-based refinement, and yields a final output. The current API implementation encapsulates these intermediate reasoning phases, denying access to the explicit reasoning chain. Consequently, we are unable to subject Nano Banana to our diagnostic ablation protocol to isolate the impact of reasoning traces.

However, the open-source models we evaluate represent the mainstream models adopting the reasoning-guided image generation paradigm. Our experimental conclusions reveal consistent bottlenecks in how these UMMs handle alignment between textual reasoning and visual generation. Therefore, we believe our benchmark and findings provide a contribution to the open-source community, offering guidance for future improvements.

## Appendix I Model Repositories

Tab. [12](https://arxiv.org/html/2602.08336v2#A9.T12 "Table 12 ‣ Appendix I Model Repositories ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") summarizes the models we use and their Hugging Face repositories.

| | |
| --- | --- |
| Model Name | Hugging Face Repository |
| Bagel | [https://huggingface.co/ByteDance-Seed/BAGEL-7B-MoT](https://huggingface.co/ByteDance-Seed/BAGEL-7B-MoT "") |
| UniCoT | [https://huggingface.co/Fr0zencr4nE/UniCoT-7B-MoT](https://huggingface.co/Fr0zencr4nE/UniCoT-7B-MoT "") |
| UniCoT-v2 | [https://huggingface.co/Fr0zencr4nE/UniCoT-7B-MoT-v0.2](https://huggingface.co/Fr0zencr4nE/UniCoT-7B-MoT-v0.2 "") |
| SRUM | [https://huggingface.co/Wayne-King/SRUM\_BAGEL\_7B\_MoT](https://huggingface.co/Wayne-King/SRUM_BAGEL_7B_MoT "") |
| Bagel-Zebra-CoT | [https://huggingface.co/multimodal-reasoning-lab/Bagel-Zebra-CoT](https://huggingface.co/multimodal-reasoning-lab/Bagel-Zebra-CoT "") |
| ThinkMorph | [https://huggingface.co/ThinkMorph/ThinkMorph-7B](https://huggingface.co/ThinkMorph/ThinkMorph-7B "") |
| T2I-R1 | [https://huggingface.co/CaraJ/T2I-R1](https://huggingface.co/CaraJ/T2I-R1 "") |
| UniMoE2 | [https://huggingface.co/HIT-TMG/Uni-MoE-2.0-Image](https://huggingface.co/HIT-TMG/Uni-MoE-2.0-Image "") |
| Qwen2.5-7B | [https://huggingface.co/Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct "") |
| Qwen3-8B | [https://huggingface.co/Qwen/Qwen3-8B](https://huggingface.co/Qwen/Qwen3-8B "") |
| Qwen3-235B-A22B | [https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507 "") |
| Qwen3-VL-235B-A22B | [https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct "") |

Table 12: List of models and their Hugging Face repositories.

## Appendix J Case Study

### J.1 Error Cases

In this section, we provide a detailed qualitative analysis of the four failure modes identified in Sec. [5](https://arxiv.org/html/2602.08336v2#S5.T5 "Table 5 ‣ 5 Discussion ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") for Bagel.

##### Reasoning Errors.

This category involves failures where the model’s intermediate reasoning process is incorrect. As illustrated in Fig. [12](https://arxiv.org/html/2602.08336v2#A10.F12 "Figure 12 ‣ Task-Specific Errors. ‣ J.1 Error Cases ‣ Appendix J Case Study ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), the model is tasked with tracking the location and number of oranges. The target picture requires exactly “2 oranges on the wooden lid and 2 oranges on the grass.” However, the model’s thought process explicitly erroneously concludes that the final count is 4 oranges on the lid.

##### Instruction Misinterpretation.

These errors occur when the model fails to grasp the fundamental modality or semantic intent of the prompt. A representative example is observed in illustrated in Fig. [13](https://arxiv.org/html/2602.08336v2#A10.F13 "Figure 13 ‣ Task-Specific Errors. ‣ J.1 Error Cases ‣ Appendix J Case Study ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"): when asked to “visualize a jewelry item based on the code”, the model occasionally renders the code text itself as an image rather than compiling the code into a visual object.

##### Concept Hallucination.

This error type refers to the generation of objects that appear nowhere in the input prompt. For instance, as illustrated in Fig. [14](https://arxiv.org/html/2602.08336v2#A10.F14 "Figure 14 ‣ Task-Specific Errors. ‣ J.1 Error Cases ‣ Appendix J Case Study ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") in a scene describing a simple garden, the model might spontaneously generate “yellow roses” despite them never being mentioned. This suggests an over-reliance on training priors rather than strict adherence to the prompt constraints.

##### Task-Specific Errors.

This category accounts for the majority of failures. In these instances, the model successfully avoids the pitfalls of incorrect reasoning, instruction misinterpretation and concept hallucination, yet still fails to produce a correct output. Crucially, these execution failures occur precisely in the dimensions UReason is designed to diagnose. Our fine-grained task design enables analysis of how reasoning impacts different visual aspects - arithmetic counts, spatial layouts, attribute consistency and text rendering -allowing researchers to identify specific failure modes in the reasoning-to-generate pipeline. We analyze representative examples across the five tasks below:

- •

Code: In Fig. [15](https://arxiv.org/html/2602.08336v2#A10.F15 "Figure 15 ‣ Task-Specific Errors. ‣ J.1 Error Cases ‣ Appendix J Case Study ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), the prompt defines a specific HTML table layout for four fashion items. While the model correctly infers the 2×\\times2 grid structure, it fails to map the specific items (Dress, Jeans, Jacket, Sneakers) to their designated table cells, resulting in misalignment despite the structural information being present in the refined prompt. This demonstrates a failure in binding semantic content to structural positions.

- •

Arithmetic: As shown in Fig. [16](https://arxiv.org/html/2602.08336v2#A10.F16 "Figure 16 ‣ Task-Specific Errors. ‣ J.1 Error Cases ‣ Appendix J Case Study ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), the refined prompt clearly specifies the final state: “two green apples placed on it and a white bowl containing one green apple.” The reasoning trace is concise and correct. Nevertheless, the generated image displays three apples on the table and one in the bowl, violating the count constraint. This highlights that even with a correct execution plan, current UMMs struggle to translate precise quantitative specifications into exact object counts, particularly when conditioned on verbose reasoning context.

- •

Spatial: In Fig. [17](https://arxiv.org/html/2602.08336v2#A10.F17 "Figure 17 ‣ Task-Specific Errors. ‣ J.1 Error Cases ‣ Appendix J Case Study ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), the prompt specifies four quadrants with distinct toppings. While the model generates a pizza, it fails to maintain strict boundary separation and correct topping distribution for each quadrant, instead blending the instructions into a generic pizza image. Examination of the reasoning trace reveals lengthy intermediate steps with detailed visual descriptions. This excessive context likely acts as noise, causing long-context interference that distracts the model from adhering to strict spatial layout constraints.

- •

Attribute: As shown in Fig. [18](https://arxiv.org/html/2602.08336v2#A10.F18 "Figure 18 ‣ Task-Specific Errors. ‣ J.1 Error Cases ‣ Appendix J Case Study ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), the refined prompt explicitly describes the cup as “empty except for the ice.” However, the generated image contains a brown, coffee-like liquid. This error could stem from contextual interference: the reasoning trace explicitly mentions “brown iced coffee” to describe the initial state, and this description likely acted as noise, causing the model to erroneously render the initial configuration instead of the final empty state specified in the refined prompt.

- •

Text: As seen in Fig. [19](https://arxiv.org/html/2602.08336v2#A10.F19 "Figure 19 ‣ Task-Specific Errors. ‣ J.1 Error Cases ‣ Appendix J Case Study ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models"), the prompt requests the text “FIRE,” but the model generates “EIME”. Despite the refined prompt containing the correct string, the visual generator fails to render the characters accurately. This likely reflects the difficulty of precisely controlling character-level generation when conditioned on verbose reasoning traces, where irrelevant token associations may interfere with accurate text rendering.

https://arxiv.org/html/2602.08336v2/figs/error_case_1.pngFigure 12: An Illustrative Example of Reasoning Error. This case shows where the model’s intermediate reasoning process is incorrect. The incorrect reasoning steps are highlighted in red.
https://arxiv.org/html/2602.08336v2/figs/error_case_2.pngFigure 13: An Illustrative Example of Instruction Misinterpretation. This case demonstrates a failure to grasp the semantic intent of the prompt. The model erroneously renders the code text itself rather than visualizing the target object described by the code.
https://arxiv.org/html/2602.08336v2/figs/error_case_3.pngFigure 14: An Illustrative Example of Concept Hallucination. This case illustrates the generation of unprompted objects. The model spontaneously renders “yellow roses” despite them being absent from the input.
https://arxiv.org/html/2602.08336v2/figs/error_case_4_2.pngFigure 15: An Illustrative Example of Task-Specific Error (Code). Although the model correctly identifies the 2x2 grid structure from the HTML prompt, it fails to map the specific items (Dress, Jeans, Jacket, Sneakers) to their corresponding cells, resulting in generation errors.
https://arxiv.org/html/2602.08336v2/figs/error_case_4_5.pngFigure 16: An Illustrative Example of Task-Specific Error (Arithmetic). The refined prompt specifies “two apples on the table and one apple in the bowl”. Although the reasoning trace is correct, the generated image displays three apples on the table, highlighting the challenge of translating precise quantitative tokens into exact object counts.
https://arxiv.org/html/2602.08336v2/figs/error_case_4_3.pngFigure 17: An Illustrative Example of Task-Specific Error (Spatial). While the prompt specifies four quadrants with distinct toppings, the model fails to maintain strict boundary separation. It blends the instructions into a generic pizza image rather than distributing the toppings correctly across the requested regions.
https://arxiv.org/html/2602.08336v2/figs/error_case_4_1.pngFigure 18: An Illustrative Example of Task-Specific Error (Attribute).Despite the prompt explicitly specifying the cup as “empty except for the ice”, the model generates a brown liquid. This error likely stems from contextual interference, where the model’s priors dilute the strict attribute constraint.
https://arxiv.org/html/2602.08336v2/figs/error_case_4_4.pngFigure 19: An Illustrative Example of Task-Specific Error (Text). The prompt requests the text “FIRE”, but the model generates “EIME”. Despite the correct string being present in the refined prompt, the UMM fails to render the characters accurately.

### J.2 More Qualitative Results

In addition to the failure modes analyzed above, we provide comprehensive qualitative comparisons across the five tasks defined in UReason: Code, Arithmetic, Spatial, Attribute, and Text reasoning. Fig. [20](https://arxiv.org/html/2602.08336v2#A10.F20 "Figure 20 ‣ J.2 More Qualitative Results ‣ Appendix J Case Study ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") to [24](https://arxiv.org/html/2602.08336v2#A10.F24 "Figure 24 ‣ J.2 More Qualitative Results ‣ Appendix J Case Study ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") showcase generated samples from representative UMMs across the three evaluation settings.

https://arxiv.org/html/2602.08336v2/figs/example_apx_code.pngFigure 20: Qualitative examples for Code.
https://arxiv.org/html/2602.08336v2/figs/example_apx_arithmetic.pngFigure 21: Qualitative examples for Arithmetichttps://arxiv.org/html/2602.08336v2/figs/example_apx_spatial.pngFigure 22:
Qualitative examples for Spatialhttps://arxiv.org/html/2602.08336v2/figs/example_apx_attribute.pngFigure 23:
Qualitative examples for Attribute.
https://arxiv.org/html/2602.08336v2/figs/example_apx_text.pngFigure 24:
Qualitative examples for Text.

## Appendix K Prompts

We present the evaluation prompts used in our automated evaluation. Fig. [25](https://arxiv.org/html/2602.08336v2#A11.F25 "Figure 25 ‣ Appendix K Prompts ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") shows the visual verification accuracy prompt, and Fig. [26](https://arxiv.org/html/2602.08336v2#A11.F26 "Figure 26 ‣ Appendix K Prompts ‣ From Reasoning to Pixels: Benchmarking the Alignment Gap in Unified Multimodal Models") shows the reasoning chain evaluation prompt.

Evaluation Prompt for Visual Verification AccuracyYou are an objective image evaluator. Your goal is to verify if the image content matches the provided text description.Target Description: "{description}"Please think step by step:1.Analyze the image content carefully.2.Compare the visual elements with the "Target Description".3.Determine if the image strictly meets the requirements.Finally, output your judgment in the following format:If it matches, output <answer>Yes</answer>.If it does not match, output <answer>No</answer>.Figure 25: Evaluation prompt for visual verification accuracy.Evaluation Prompt for the Quality of Reasoning ChainYou are an objective reading comprehension evaluator.I will provide you with a "User Prompt", a model’s "Thought Process" (which includes its intermediate thoughts and final refined prompt) and "Target Criteria".Your task is to judge whether the final state or conclusion described in the model’s thought process contains and satisfies a specific "Target Criteria".=== User Prompt ==={user\_prompt}

=== Model Thought Process ==={model\_thought}

=== Target Criteria ==={criteria}

=== Instruction ===Please think step by step:1.Analyze the "Target Criteria" to understand the specific visual or logical constraints required.2.Read the entire "Thought Process" carefully.3.Determine whether the "Target Criteria" is successfully met or clearly present in the outcome of the thought process.•Note: The text does not need to match the criteria word-for-word, but the specific semantic meaning and target state must be unambiguously present. Do not guess or assume unstated information.Finally, output your judgment in the following format:If the target criteria is clearly met or present in the text, output <answer>Yes</answer>.If the criteria is missed or contradicted, output <answer>No</answer>.Figure 26: Evaluation prompt for assessing the reasoning chain against target criteria.

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploitation" file="representational-similarity-analysis-rsa.md">
<details>
<summary>Representational Similarity Analysis (RSA)</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://www.emergentmind.com/topics/representational-similarity-analysis-rsa>

# Representational Similarity Analysis (RSA)

Updated 29 September 2025

- Representational Similarity Analysis (RSA) is a statistical method that transforms high-dimensional neural or model activity into representational dissimilarity matrices (RDMs) for cross-system comparison.
- It leverages varied metrics such as Euclidean distance and Pearson’s correlation along with techniques like GLM, gradient descent, and deep learning to robustly compare complex data.
- RSA is widely applied in neuroscience, AI, and behavioral research to enhance model interpretability, align human and machine representations, and support innovative cross-modal analyses.

Representational Similarity Analysis (RSA) is a statistical and computational framework for quantifying and comparing the internal representational geometries of neural, behavioral, and artificial systems. By abstracting complex, high-dimensional activity patterns into similarity structures—commonly represented as [representational dissimilarity matrices](https://www.emergentmind.com/topics/representational-dissimilarity-matrices-rdms "") (RDMs)—RSA enables rigorous comparisons across measurement modalities, subjects, species, computational models, and stimuli. It is heavily utilized in cognitive neuroscience, systems neuroscience, and increasingly in artificial intelligence and computational linguistics for model comparison, interpretability, and alignment assessment.

## 1\. Theoretical Principles and Core Definitions

At its foundation, RSA operates by transforming multivariate response patterns (e.g., fMRI voxel time series, neural network activations, behavioral similarity judgments) into a pairwise (dis)similarity matrix. For a set of N stimuli or experimental conditions, responses are collected as vectors rir\_iri​ for each stimulus iii. The [RDM](https://www.emergentmind.com/topics/relay-diffusion-model-rdm "") is then constructed via a dissimilarity function ddd:

RDMij=d(ri,rj)RDM\_{ij} = d(r\_i, r\_j)RDMij​=d(ri​,rj​)

The choice of metric (e.g., Euclidean distance, correlation distance, Mahalanobis distance) is dictated by data type and scientific question. Unlike raw activity patterns, the RDM is invariant to orthogonal transformations and provides an abstract “geometry” of representational space. When applied across systems (e.g., brain regions, neural network layers, behavioral modalities), RSA summarizes by correlating the upper-triangular entries of the respective RDMs:

RSA score=corr(vec(RDMA),vec(RDMB))\\text{RSA score} = \\mathrm{corr}(\\text{vec}(RDM\_A), \\text{vec}(RDM\_B))RSA score=corr(vec(RDMA​),vec(RDMB​))

This correlation (often Spearman’s ρ\\rhoρ or Pearson’s rrr) reflects the alignment of relational geometry, enabling direct comparison even when representational bases differ completely ( [Chrupała et al., 2019](https://www.emergentmind.com/papers/1905.06401 ""), [Abnar et al., 2019](https://www.emergentmind.com/papers/1906.01539 ""), [Bersch et al., 2022](https://www.emergentmind.com/papers/2208.09677 "")).

## 2\. Methodological Implementations and Extensions

**Classical workflow.** Standard RSA leverages a general linear model ( [GLM](https://www.emergentmind.com/topics/generalized-lagrange-multiplier-glm-approach "")) for neural data, estimating response coefficients BBB from the relation

Y=X⋅B+ϵY = X \\cdot B + \\epsilonY=X⋅B+ϵ

where YYY is the time series data, iii0 is the design matrix, and iii1 contains neural signatures per condition or category ( [Sheng et al., 2018](https://www.emergentmind.com/papers/1809.04429 "")). Dissimilarities are then computed between coefficient vectors iii2 for all stimulus pairs.

**Regularized and scalable algorithms.** Classical approaches depend on inversion of large covariance matrices, which is problematic for high-dimensional data. This computational bottleneck is addressed by Gradient-based RSA (GRSA) ( [Sheng et al., 2018](https://www.emergentmind.com/papers/1809.04429 "")), which:

- Reformulates the estimation as an optimization problem with L1 (LASSO) regularization:

iii3

- Solves via [mini-batch stochastic gradient descent](https://www.emergentmind.com/topics/mini-batch-stochastic-gradient-descent-sgd "") (SGD), sidestepping matrix inversion and enabling scalability to full-brain and multi-subject settings.

**Searchlight RSA.** For spatial mapping, the searchlight approach slides a small, local region (e.g., 3×3×3 voxels) across the brain. RSA is computed within each local cube, producing a detailed spatial map of representational similarity ( [Sheng et al., 2018](https://www.emergentmind.com/papers/1809.04429 ""), [Bersch et al., 2022](https://www.emergentmind.com/papers/2208.09677 "")).

**Deep extensions and nonlinearity.** [Deep Representational Similarity Learning](https://www.emergentmind.com/topics/deep-representational-similarity-learning-drsl "") (DRSL) replaces the linear transformation with subject-specific neural networks, enabling complex nonlinear mapping from raw fMRI signals to compact, information-rich signatures ( [Yousefnezhad et al., 2020](https://www.emergentmind.com/papers/2010.02012 "")).

**Partial correlation and whitening.** When the design matrix iii4 is not orthogonal, classical RSA can be confounded. Corrective frameworks include:

- Partialing out the bias by controlling for the covariance matrix in the GLM (i.e., (X′X)iii5), removing spurious correlations ( [Viviani, 2021](https://www.emergentmind.com/papers/2102.08931 "")).
- Whitened unbiased RDM cosine similarity (WUC) combines cross-validated (unbiased) estimators of dissimilarity with whitening by the full (co-)variance of estimates, enabling statistically robust model selection in the presence of correlated and heteroscedastic noise ( [Diedrichsen et al., 2020](https://www.emergentmind.com/papers/2007.02789 "")).

**Deconfounded similarity.** In network comparison contexts, confounding from input population structure is removed by regressing out baseline input similarity from the [representational similarity matrices](https://www.emergentmind.com/topics/representational-similarity-matrices "") before final correlation (the “deconfounded RSA”) ( [Cui et al., 2022](https://www.emergentmind.com/papers/2202.00095 "")).

**[Topological extensions](https://www.emergentmind.com/topics/topological-extensions-trsa "").** Recent proposals generalize the RDM using nonlinear, monotonic (piecewise linear) transforms, emphasizing discrete topological structure (e.g., neighborhood relations) rather than fine-grained metric geometry. This yields geo-topological matrices and “ [topological RSA](https://www.emergentmind.com/topics/topological-rsa-trsa "")” (tRSA), which can be “tuned” from pure geometry to pure topology via threshold parameters ( [Lin et al., 2023](https://www.emergentmind.com/papers/2309.11028 ""), [Lin, 2024](https://www.emergentmind.com/papers/2408.11948 "")).

## 3\. Application Domains

**Neuroscience and systems biology.** RSA bridges data from fMRI, EEG, single-unit recordings, or other modalities to compare representations across brain regions, species, or levels of analysis. For example:

- Searchlight and spatiotemporal GRSA enable tractable, robust comparison of cognitive task representations across the whole brain ( [Sheng et al., 2018](https://www.emergentmind.com/papers/1809.04429 "")).
- Single-trial RSA extends the approach to time-resolved EEG, revealing dynamic encoding of semantic features in emotion processing ( [Cheng, 2021](https://www.emergentmind.com/papers/2110.03529 "")).
- Topological RSA and allied methods are now used to identify computational signatures resistant to individual variability and measurement noise ( [Lin et al., 2023](https://www.emergentmind.com/papers/2309.11028 ""), [Lin, 2024](https://www.emergentmind.com/papers/2408.11948 "")).

**Artificial intelligence model comparison.** RSA is widely deployed to interpret, compare, and audit neural network representations:

- Linguistic models: RSA detects encoding of syntactic and semantic features in BERT, ELMo, and other encoders, including layerwise tracking of linguistic phenomena ( [Chrupała et al., 2019](https://www.emergentmind.com/papers/1905.06401 ""), [Abdou et al., 2019](https://www.emergentmind.com/papers/1909.00303 ""), [Lepori et al., 2020](https://www.emergentmind.com/papers/2011.12073 "")).
- [Foundation models](https://www.emergentmind.com/topics/foundation-models-lams "") for vision and computational pathology: RSA reveals how architectural family (e.g., CNN vs. Transformer), training paradigm (self-supervised vs. contrastive), and even [stain normalization](https://www.emergentmind.com/topics/stain-normalization "") affect internal [representation geometry](https://www.emergentmind.com/topics/representation-geometry "") ( [Wu et al., 4 Sep 2025](https://www.emergentmind.com/papers/2509.04622 ""), [Mishra et al., 18 Sep 2025](https://www.emergentmind.com/papers/2509.15482 "")).
- Cross-lingual speech: RSA using [Centered Kernel Alignment](https://www.emergentmind.com/topics/centered-kernel-alignment-cka "") (CKA) quantifies the preservation of phonological and acoustic structure across languages and encoder architectures ( [Abdullah et al., 2021](https://www.emergentmind.com/papers/2109.10179 "")).

**Human-model alignment.** Turing RSA uses group and individual pairwise similarity ratings to assess [semantic alignment](https://www.emergentmind.com/topics/semantic-alignment-sa "") between human representations and LLMs/VLMs, revealing model strengths and limitations in reproducing the structure and variability of human cognition across modalities ( [Ogg et al., 2024](https://www.emergentmind.com/papers/2412.00577 "")).

## 4\. Statistical, Computational, and Interpretational Considerations

**Discriminability and separability.** RSA is among the highest-performing methods (d′ ≈ 3.8, ROC-AUC > 0.91) for separating model families when compared to other similarity metrics such as linear predictivity, Procrustes alignment, or soft-matching, due to its strict preservation of relative geometric structure ( [Wu et al., 4 Sep 2025](https://www.emergentmind.com/papers/2509.04622 "")).

**Sampling constraints and denoising.** Limited neuron sampling systematically underestimates representational similarity due to eigenvector delocalization. Analytical correction using [random matrix theory](https://www.emergentmind.com/topics/random-matrix-theory-rmt "") and spectral denoising allows recovery of population-level similarity from under-sampled data ( [Kang et al., 27 Feb 2025](https://www.emergentmind.com/papers/2502.19648 "")).

**Bias and confounding.** Non-orthogonality in experimental design or stimulus dependencies can bias classical RSA scores. Approaches such as partial correlation correction (controlling for off-diagonal design matrix structure), cross-validated distance estimation, and whitening achieve near-unbiased inference ( [Viviani, 2021](https://www.emergentmind.com/papers/2102.08931 ""), [Diedrichsen et al., 2020](https://www.emergentmind.com/papers/2007.02789 ""), [Cui et al., 2022](https://www.emergentmind.com/papers/2202.00095 "")).

**Model flexibility and regularization.** Advanced implementations combine L1 (LASSO) and L2 (ridge) regularization in the regression model, and deep learning-based pipelines (e.g., DRSL) for nonparametric adaptability to complex, high-dimensional fMRI or multi-subject data ( [Sheng et al., 2018](https://www.emergentmind.com/papers/1809.04429 ""), [Yousefnezhad et al., 2020](https://www.emergentmind.com/papers/2010.02012 "")).

**Interpretability.** RSA uniquely enables higher-order and cross-modal comparison (e.g., model–neural–behavioral), direct model selection, and elucidation of when and where cognitive or computational models capture functionally relevant stimulus structure ( [Chrupała et al., 2019](https://www.emergentmind.com/papers/1905.06401 ""), [Abdou et al., 2019](https://www.emergentmind.com/papers/1909.00303 ""), [Ogg et al., 2024](https://www.emergentmind.com/papers/2412.00577 "")).

## 5\. Practical Guideline Table: RSA Implementation and Model Comparison

| RSA Variant | Matrix Input | Key Alignment Metric | Domain Suitability |
| --- | --- | --- | --- |
| Classical/GLM-based | GLM iii6 RDM | Pearson/Spearman correlation | fMRI; small/medium voxels |
| Gradient-based (GRSA) | Data, Mini-batches | SGD, L1/L2 loss | Whole-brain, large N |
| Deep (DRSL) | Neural net iii7 RDM | Deep learn. + regression | fMRI, multi-subject, nonlin. |
| Partialled RSA | BB', Bcov | Partial correlation | Searchlight, bias-prone |
| Whitened Unbiased (WUC) | Cross-validated RDM | Cosine/whitened similarity | All, correlated noise/data |
| Deconfounded | RSMs, input simil. | Residual RSA/CKA | Model/model, OOD, transfer |
| Topological (tRSA) | RGTM, RDM | Varying topology/geometry | Robust/variant-invariant |

_Key: RDM = Representational Dissimilarity Matrix, [RSM](https://www.emergentmind.com/topics/reduced-stiffness-method-rsm "") = Representational Similarity Matrix, RGTM = Geo-Topological Matrix, OOD = Out-of-distribution._

## 6\. Impact, Contemporary Directions, and Future Prospects

RSA is a central tool for interrogating how brains, models, or behavioral systems encode, transform, and structure information. Its flexibility (abstracting away from basis, scaling, or modality), coupled with evolving methodological extensions, underpins its capacity for neuroscientific, cognitive, and AI research. Recent advances emphasize several trends:

- Integration of topological methods (tRSA, geo-topological transforms, persistent homology) for robust, noise-resistant model/brain comparisons ( [Lin et al., 2023](https://www.emergentmind.com/papers/2309.11028 ""), [Lin, 2024](https://www.emergentmind.com/papers/2408.11948 "")).
- Scaling to high-dimensional, massive, or temporally-resolved data, using computationally efficient algorithms (mini-batch SGD, deep architectures, temporal persistence methods) ( [Yousefnezhad et al., 2020](https://www.emergentmind.com/papers/2010.02012 ""), [Lin et al., 2019](https://www.emergentmind.com/papers/1906.09264 "")).
- Bias reduction, statistical optimality, and model selection robustness via whitening, crossvalidation, and spectral techniques ( [Diedrichsen et al., 2020](https://www.emergentmind.com/papers/2007.02789 ""), [Kang et al., 27 Feb 2025](https://www.emergentmind.com/papers/2502.19648 "")).
- Application to human–machine alignment on both group and individual levels, revealing the transfer, gaps, and variability in semantic and perceptual geometry ( [Ogg et al., 2024](https://www.emergentmind.com/papers/2412.00577 "")).

Future directions include linking RSA-derived topological invariants to information-theoretic coding principles, designing new alignment metrics for richer or more complex data structures, and further extending RSA frameworks to unsupervised and time-resolved analyses across neuroscience and machine learning domains ( [Lin, 2024](https://www.emergentmind.com/papers/2408.11948 "")).

RSA continues to serve as a cornerstone in quantitative model–brain, brain–behavior, and model–model comparison, with its methodological flexibility and theoretical soundness ensuring continued impact in systems, cognitive neuroscience, and AI research.

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