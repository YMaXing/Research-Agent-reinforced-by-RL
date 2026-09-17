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
<summary>What mathematical conditions allow PMI kernels to exactly represent platonic representations?</summary>

Phase: [EXPLORATION]

### Source [19]: https://3dvar.com/Huh2024The.pdf

Query: What mathematical conditions allow PMI kernels to exactly represent platonic representations?

Answer: Remark F.2. Proposition F.1 is one example that a sufficiently smooth world or a sufficiently high sampling rate allows the PMI kernel KPMI to be exactly represented as inner products of a learned feature space (up to a scale). The condition here can be satisfied, for example, if the off-diagonal terms decay linearly with respect to N and stay sufficiently close to each other. While the condition is somewhat strict, it captures the essence that smoothness and continuity allow easier learning. Nonetheless, we note that exact representation is not necessary for convergence, and thus this requirement can likely be relaxed. Under mild conditions that the world is smooth enough (see Appendix F.2), a choice of fX can exactly represent KPMI: ⟨fX(xa), fX(xb)⟩= KPMI(xa, xb) + cX, (6) where we observed that cX(xa) from Equation (5) must be a constant since both sides are symmetric. For the general τ ̸= 1 case, we have g (and corresponding fX) recovers KPMI up to an offset and a scale. We want to express KPMI + C using some representation function fX : X →Rn so that < fX(xa), fX(xb) > = KPMI(xa, xb) + C, for some C. For such f to exist, an equivalent criterion is that KPMI + C is positive semi-definite (PSD), as can be seen from eigendecomposition. Proposition F.1. Suppose that the off-diagonal elements of KPMI are bounded within [log ρmin, log ρmin + δ] ∈(−∞, 0]. We have KPMI + C is positive semi-definite (PSD) for some C if the joint distribution is sufficiently smooth: Pcoor(zi | zi) Pcoor(zi) ≥eNδρmin, ∀i.

-----

</details>

<details>
<summary>What are key failure modes of nearest-neighbor metrics when measuring cross-modal alignment at scale?</summary>

Phase: [EXPLORATION]

### Source [20]: https://akoepke.github.io/cave_umwelten

Query: What are key failure modes of nearest-neighbor metrics when measuring cross-modal alignment at scale?

Answer: Key failure modes of nearest-neighbor metrics include degradation of alignment as dataset size increases and mismatches due to many-to-many relationships. Mutual k-NN alignment drops as datasets become denser. Fine-grained consistency is often lost at scale. The original experiments used one-to-one image-text pairings. But real data is many-to-many: a single image can be described in countless ways, and a single caption can match many different images. When we progressively add more captions per image or more images per caption, mutual k-NN alignment drops consistently. Alignment when adding more images per caption. Adding more images per caption using CycleReward data. Mutual k-NN alignment decreases consistently for both k=1 and k=10. Alignment when adding more captions per image. Adding more captions per image gives the same pattern. Alignment drops as the one-to-one setting is relaxed. The core metric used by Huh et al. to measure cross-modal alignment is mutual k-nearest neighbors (mutual k-NN). Given paired image-text data, find the (k) nearest neighbors for each sample in both the vision and the language embedding space. Use the slider below to grow the dataset size. As it gets denser, both models find closer neighbors, but they stop agreeing on which one. Dataset size: 1,024. Alignment Degrades at Scale. The original experimental evidence for the Platonic Representation Hypothesis used a dataset of just 1,024 samples. We systematically scaled up to 15 million, and found that alignment degraded. 13.5% Alignment on WIT-1024 (k=10). 0.8% Alignment on LAION-15M (k=10). 16× Drop in alignment when scaling up. Why does this happen? In a sparse dataset, both modalities tend to retrieve the same neighbors, not necessarily because they agree, but because the pool is too small to reveal their differences. As the dataset gets denser, each modality can find neighbors that are closer in its own space, and the overlap vanishes.

-----

Phase: [EXPLORATION]

### Source [21]: https://arxiv.org/html/2604.18572v2

Query: What are key failure modes of nearest-neighbor metrics when measuring cross-modal alignment at scale?

Answer: In a small dataset, weakly related samples may become nearest neighbors simply because no better alternatives exist (Fig. 1a). Here, two models can agree despite organizing their representations differently. As the dataset grows (i.e. the gallery used for retrieving nearest neighbors gets denser), both models find closer neighbors and cross-modal consistency requires more fine-grained structural alignment (Fig. 1b). A vision model may retrieve an image of a car taken from a similar angle as the query, while the language model retrieves a caption describing the same car model as the query but in a different pose. Both are valid, but inconsistent between modalities, producing a mismatch that gets penalized under the mutual nearest-neighbor metric. Alignment is measured using mutual nearest neighbors on small datasets (≈1K samples) and degrades substantially as the dataset is scaled to millions of samples. The same behavior is observed beyond text-image, for text-audio and text-video alignment. The alignment that remains between model representations reflects coarse semantic overlap rather than consistent fine-grained structure. Moreover, the evaluations in Huh et al. are done in a one-to-one image-caption setting, a constraint that breaks down in realistic many-to-many settings and further reduces measured alignment. We also find that the reported trend of stronger language models increasingly aligning with vision does not appear to hold for newer models. We additionally test whether the alignment drop with increasing gallery size is merely an artifact of the mutual kNN metric being harder at scale. Specifically, we measure within-modality alignment for two pairs of models: two language models of different scale (OpenLlama-3b and OpenLlama-13b), and, separately, two vision models (DINOv2-base and DINOv2-giant). If mutual kNN alignment collapses for dense galleries regardless of the models being compared, the cross-modal drop observed would be uninformative. If within-modality alignment remains stable, the cross-modal drop is meaningful.

-----

</details>

<details>
<summary>How does the Platonic representation hypothesis connect to convergent evolution in biological sensory systems?</summary>

Phase: [EXPLORATION]

### Source [22]: https://3dvar.com/Huh2024The.pdf

Query: How does the Platonic representation hypothesis connect to convergent evolution in biological sensory systems?

Answer: The Platonic Representation Hypothesis suggests that different neural networks converge on similar representations of reality, akin to convergent evolution in biological sensory systems. This convergence is driven by shared underlying truths and principles. The hypothesis posits a shared statistical model of reality across diverse neural networks. We call this converged hypothetical representation the “platonic representation” in reference to Plato’s Allegory of the Cave (Plato, c. 375 BC), and his idea of an ideal reality that underlies our sensations. The training data for our algorithms are shadows on the cave wall, yet, we hypothesize, models are recovering ever better representations of the actual world outside the cave. This idea is not unique to Plato; our hypothesis is also related to the notion of “convergent realism” (Newton-Smith, 1981; Putnam, 1982; Doppelt, 2007; Hardin & Rosenberg, 1982) in the philosophy of science (i.e., that science is converging on truth), and to many arguments that have been put forth in the representation learning literature (e.g., Tian et al. (2020a); Zimmermann et al. [...] The second finding agrees with extensive research that oriented Gabor-like filters are common in both artificial and biological vision systems. This suggests a convergence to a similar initial layer of representation across various neural network architectures (Olshausen & Field, 1996; Krizhevsky et al., 2017). Bansal et al. (2021) expanded on the idea of model stitching, uncovering that models trained using self-supervised objectives align closely with their supervised counterparts. [...] What has led to this convergence? Will it continue? And ultimately, where does it end? Our central hypothesis, stated above in Figure 1, is that there is indeed an endpoint to this convergence and a principle that drives it: different models are all trying to arrive at a representation of reality, meaning a representation of the joint distribution over events in the world that generate the data we observe. Figure 1 conveys this hypothesis: there exists a real world (labeled Z), which we measure with various sensors, such as the camera shown to the left (X).

-----

Phase: [EXPLORATION]

### Source [23]: https://kyrylok.substack.com/p/a-case-for-platonic-biology

Query: How does the Platonic representation hypothesis connect to convergent evolution in biological sensory systems?

Answer: Neural networks trained on completely different data (images versus text) with completely different training objectives are learning increasingly similar representations of the world. The better the model is, the more their internal representations converge. You can think of the training data as the shadows on the cave wall, and the model recovering better representations of the actual world outside the cave. If the Platonic Representation Hypothesis is correct, we should see convergence in biological data too since they are both projecting the same functional state of the cell. Even with primitive models and limited samples. The next part of the article will concern how these concepts are relevant in the context of drug discovery. [...] Platonic forms operate at the level of ultimate causation. They do not replace molecular details (proximate causality) but provide a framework for understanding why those details organize themselves the way they do. As we will see, this becomes very relevant in things like drug discovery. If the concept of Platonic representations is correct, it should extend beyond just biology. Neural Networks also offer a glimpse into this. The Platonic Representation Hypothesis, proposed by Huh et al., states that neural networks trained with different objectives on different data and modalities are converging to a shared statistical model of reality in their representation spaces. [...] If the Platonic Representation Hypothesis holds for biology, we should expect: 1. Models trained on different modalities should agree on which drugs are similar 2. This agreement should increase with model scale and data diversity 3. Supervision should accelerate convergence (by providing shared constraints) 4. Even unsupervised models should show some alignment (because the underlying biology is shared) ## Experimental setup I compare four embedding spaces derived from different biological measurement modalities The supervised models predict mechanism of action (MOA) labels with embeddings are taken from the second to last layer. The unsupervised models are simple autoencoders with no label information.

-----

Phase: [EXPLORATION]

### Source [24]: https://www.youtube.com/watch?v=V7AyriUcXZQ

Query: How does the Platonic representation hypothesis connect to convergent evolution in biological sensory systems?

Answer: little adaptation. And I think that's consistent with this hypothesis. If I already have this kind of platonic representation of the world from touch, then to learn the mapping to that representation from a new modality, all I have to do is learn how to map to that representation. I don't have to learn the representation in the first place, so it should be a lot more data efficient. But the main implication is just that if there really is some kind of thing we're converging to, then we should understand it. We should characterize it. We should know what that is. It's an important object. So if the hypothesis is true, at least in part, then I think this is an important thing to study. OK. Oh. So I'll end there. I had a set of slides in case [...] these hypothesis spaces. Then they won't converge because this guy will learn that point and this guy will learn that point. But if I simply scale up the models, I have a greater chance of finding a solution, which I have a greater chance that the two models will overlap on the optimum in the ambient space. So if I scale up two hypothesis spaces, they're going to overlap more. And therefore, there will be the chance that they can actually arrive at the same solution. So I think that this is part of it too, that we are making bigger and bigger models. And that should have the effect that there is the possibility of convergence, if I also have other constraints that force me to find solutions in a small subspace. OK. And then another hypothesis is that, well, here's the set of functions [...] about it a little bit more. AUDIENCE: What happens when you try to do it with the Gaussian process? PHILIP ISOLA: So I'm not sure if we've tried that. But we have tried doing this with just randomly initialized networks, which will vary in their embedding dimensionality. And those don't align with any of these models. So if it were just about as dimensionality goes to infinity, you approach some limit which is convergent, then you would expect a random network would also have that property. And that doesn't happen. We can talk a little bit more in detail about it. I think it's something we should look at more systematically. But I don't think that's explaining the data. So here's just another way of looking at that same result. OK, I'll come back

-----

Phase: [EXPLORATION]

### Source [25]: https://phillipi.github.io/prh

Query: How does the Platonic representation hypothesis connect to convergent evolution in biological sensory systems?

Answer: |  | | The Platonic Representation Hypothesis | | Minyoung Huh\ | Brian Cheung\ | Tongzhou Wang\ | Phillip Isola\ | |  | | Position Paper in ICML 2024 | |  | |  | | Paper | Code | | Outline  |  |  | Our hypothesis  |  |  | How to measure convergence?  |  |  | Evidence of convergence  |  |  | What is driving convergence?  |  |  | What are we converging to? | | The world (Z) can be viewed in many different ways: in images (X), in text (Y), etc. We conjecture that representations learned on each modality on its own will converge to similar representations of Z. [...] # What representation are we converging to? | In a particular idealized world, we show that a certain family of learners will converge to a representation whose kernel is equal to the pointwise mutual information (PMI) function over the underlying events (Z) that cause our observations, regardless of modality. For example, in a world of colors, where events and generate visual and textual observations, we would have:   |  |  | \[ \text{sim}(f\_{\text{text}}(\text{red"}), f\_{\text{text}}(\text{“orange"})) \quad=\quad \text{PMI}(z\_{\text{red}}, z\_{\text{orange}}) + \text{const} \] \[ \text{sim}(f(\color{red}{\blacksquare}\color{black}), f(\color{orange}{\blacksquare}\color{black})) \quad=\quad \text{PMI}(z\_{\text{red}}, z\_{\text{orange}}) + \text{const} \] [...] Conventionally, different AI systems represent the world in different ways. A vision system might represent shapes and colors, a language model might focus on syntax and semantics. However, in recent years, the architectures and objectives for modeling images and text, and many other signals, are becoming remarkably alike. Are the internal representations in these systems also converging?   |  |  | We argue that they are, and put forth the following hypothesis:   |  |  | Neural networks, trained with different objectives on different data and modalities, are converging to a shared statistical model of reality in their representation spaces.

-----

</details>

<details>
<summary>What implications does Platonic representational convergence have for brain-computer interface design?</summary>

Phase: [EXPLORATION]

### Source [28]: https://3dvar.com/Huh2024The.pdf

Query: What implications does Platonic representational convergence have for brain-computer interface design?

Answer: Different models, with different architectures and objectives, can have aligned representations One indication of representational convergence is the rising number of systems built on top of pre-trained foundation models. These models are becoming standard backbones across a growing spectrum of tasks. Their versatility across numerous applications implies a level of universality in the way they represent data. While this trend implies convergence toward a relatively small set of foundation models, it does not imply that differ-ent foundation models will arrive at the same representation. Yet that is what has been observed by several recent papers. Scaling is sufficient, but not necessarily efficient Our arguments are roughly in line with the claim that “scale is all you need” to reach high levels of intelligence. We have ar-gued that as resources are scaled (# parameters, # datapoints, # flops), representations are converging, regardless of other modeling choices and even data modality. Does this mean that scale is all that matters? Not quite: different methods can scale with different levels of efficiency (Hestness et al., 2017; Kaplan et al., 2020), and successful methods must still satisfy some general requirements (e.g., be a consistent estimator, model pairwise statistics of P(Z)). The Platonic Representation Hypothesis Minyoung Huh 1 Brian Cheung 1 Tongzhou Wang 1 Phillip Isola 1 Abstract We argue that representations in AI models, par-ticularly deep networks, are converging. First, we survey many examples of convergence in the lit-erature: over time and across multiple domains, the ways by which different neural networks rep-resent data are becoming more aligned. Next, we demonstrate convergence across data modalities: as vision models and language models get larger, they measure distance between datapoints in a more and more alike way. We hypothesize that this convergence is driving toward a shared sta-tistical model of reality, akin to Plato’s concept of an ideal reality. We term such a representation the platonic representation and discuss several possible

-----

Phase: [EXPLORATION]

### Source [29]: https://ui.adsabs.harvard.edu/abs/2024arXiv240507987H/abstract

Query: What implications does Platonic representational convergence have for brain-computer interface design?

Answer: We argue that representations in AI models, particularly deep networks, are converging. First, we survey many examples of convergence in the literature: over time and across multiple domains, the ways by which different neural networks represent data are becoming more aligned. Next, we demonstrate convergence across data modalities: as vision models and language models get larger, they measure distance between datapoints in a more and more alike way. We hypothesize that this convergence is driving toward a shared statistical model of reality, akin to Plato's concept of an ideal reality. We term such a representation the platonic representation and discuss several possible selective pressures toward it. Finally, we discuss the implications of these trends, their limitations, and

-----

Phase: [EXPLORATION]

### Source [30]: https://www.youtube.com/watch?v=V7AyriUcXZQ

Query: What implications does Platonic representational convergence have for brain-computer interface design?

Answer: that in the implications. But you would think, well, OK,
if all good models are somehow converging, then just take
them all and ensemble them. It should work well. They should already be
kind
of aligned and ensemble-able. So I think that is
an interesting thing that you could try. But you will have to-- in order to ensemble,
you'll have to somehow-- there's a symmetry, which is
that you can get the same kernel with differently rotated data. Any isometric
transformation of the data will have the same kernel. So you have to get rid
of that symmetry somehow. So that's something that
I think is interesting. But a lot of you
might be saying, OK, that's kind of obvious. Like, two different
computer vision systems that perform well in [...] our transformers, they're incapable of
doing certain things. And so all these models are
incapable of the same things, so it looks like convergence,
but not to something good. And there also could be
sociotechnical reasons for this, because again, we
share all of our ideas and everybody wants to do well
on ImageNet classification. So we converge to a
visual representation, which is good at that,
but not at other things. OK. But there are a lot of
interesting implications. I think one was
pointed out before that if these models learn
similar representations, you should be able to share data
and knowledge between models. You should be able to ensemble
them, distill one to the other. So in particular, it should
help if you train your language models on images. And it should help if you train [...] these hypothesis spaces. Then they won't converge
because this guy will learn that point and this
guy will learn that point. But if I simply
scale up the models, I have a greater chance of
finding a solution, which I have a greater chance
that the two models will overlap on the optimum
in the ambient space. So if I scale up two
hypothesis spaces, they're going to overlap more. And therefore, there will be the
chance that they can actually arrive at the same solution. So I think that
this is part of it too, that we are making
bigger and bigger models. And that should have
the effect that there is the possibility
of convergence, if I also have other constraints
that force me to find solutions in a small subspace. OK. And then another hypothesis
is that, well, here's the set of functions

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="a-case-for-platonic-biology-by-kyrylo-kalashnikov.md">
<details>
<summary>A Case for Platonic Biology</summary>

Phase: [EXPLORATION]

**Source URL:** <https://kyrylok.substack.com/p/a-case-for-platonic-biology>

# A Case for Platonic Biology
### And implications of Platonism in drug discovery.

Around 375 BC Plato wrote his famous Allegory of the Cave. He describes prisoners chained in a cave, seeing only shadows cast on a wall by objects passing before fire. From birth, they see nothing but flickering shadows on the cave wall, and mistake these shadows for ultimate reality. It’s the only world they’ve ever known. They hear echoes, believing the sounds come from the shadows. They become good at predicting their patterns, but have no concept of the true objects or the world outside.

Using this analogy Plato postulated that our sensory experiences are simply poor projections of a deeper, ideal reality. He believed that reality is made of forms, which we can only approach through reason.

https://substackcdn.com/image/fetch/$s_!A0aL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a2bfb45-ef7e-4485-b0ac-a7bc87546db2_533x400.png

I remember vigorously debating platonism in my college philosophy class. I had a gut feeling that Platonic forms were real, but I could never quite put a finger on how to properly describe them. My classmate would always yell: “Show me the forms”. I would quietly nod and retreat, unsure what to reply. I thought that the implications of Platonism are not far reaching. Ethics, metaphysics… how are these things relevant anyways? I would not want to waste my time debating them.

But I was wrong. And in this article I want to show evidence that the forms are real. And I can show you where to look.

I will take you through the failure of genomic reductionism, the forgotten wisdom of Waddington’s epigenetic landscape, and recent work showing that neural networks trained on completely different data converge toward shared representations of reality. I will conclude with my own tests whether this convergence exists when we train AI models for drug discovery.

But first, we need to understand what is broken in how we currently think about biology. Let me start with a cautionary tale.

The genomic revolution promised everything from immediate cures for common disease to personalized cancer vaccines and solving aging. However, it turned out that single gene diseases are rare, while the hunt for aging genes was not successful beyond producing some correlatory findings.

The response is always the same. Cancer is still viewed as a matter of a few mutations, and papers regularly [try](https://pubmed.ncbi.nlm.nih.gov/41381541/) to identify genes that are associated with longevity. “WE NEED MORE DATA” is the common answer that you would hear among these people.

I believe the problem is not a lack of data, but a fundamental framework. We keep searching for the single gene, the single pathway, the single molecule. **When we find a correlation between a mutation and cancer, we call it causality. When we can’t reduce a phenomenon to a clear cause, we label it “emergent” and move on, as if naming it explains it.**

Reductionism is seductive. If we go deep enough, we will find the lever that controls everything. Haven’t found it in the genome? Go deeper to atomic self-assembly. The cure is always one level down.

But what if the patterns we observe are not reducible to individual components at all?

In the 1950s, Conrad Waddington introduced his “epigenetic landscape” to explain the concept of “emergence”, or how a single genome produces distinct, stable cell types. In his framework, a cell’s fate is like a ball rolling down a landscape of valleys and ridges where each valley is a stable cell type, each ridge a barrier between fates. **The landscape itself, not any single gene, is what determines which states are possible.**

https://substackcdn.com/image/fetch/$s_!cvb8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0288db05-caf4-4417-ac05-d4d0cc6df0b7_1370x1080.png

To this day, it is treated as a useful pedagogical metaphor to teach in the classroom. It’s forgotten when it comes to practical research and we return to discussing pathways and molecular cascades.

[In 2009, Huang, Ernberg, and Kauffman](https://pubmed.ncbi.nlm.nih.gov/19595782/) argued that Waddington’s landscape is more than a metaphor. They showed it can be formally derived from the dynamics of gene regulatory networks.

The key concept is the attractor, which is a stable state that the network naturally settles into. Think of a ball coming down to rest at the bottom of a valley (image above). Each attractor corresponds to a distinct, self-maintaining gene expression pattern (a.k.a cell type). The valleys in Waddington’s landscape are these attractors.

The reason for this line of inquiry was hiding in plain sight. Lung cancer (despite hundreds of random mutations scattered through the genome), has only 4 transcriptomic clusters that account for over 95% of pulmonary neoplasia. Why isn’t there a continuum of tumor types, given that they result from “random” mutational processes?

https://substackcdn.com/image/fetch/$s_!PwC7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fad5e39ef-0fc7-456a-8455-dd6150b3a62e_1826x1374.png

This observation led Huang et al. to a deeper question: “ **prevailing paradigm of somatic evolution and multi-step tumorigenesis, while useful in many instances, offers no logically coherent reason for why oncogenesis recapitulates ontogenesis.**“ Why do cancer cells so consistently exhibit atavistic (ancient) states? Random mutations and selection can not explain this specificity. They noticed that if the cancer cells are trapped in pre-existing abnormal attractors (Platonic valleys that normal development avoids), then the atavistic phenotypes come “for free” encoded in the landscape.

There are other “free lunch” properties that come with attractors. For example, memory. Once a cell enters an attractor, it stays there. You need significant energy (e.g molecular perturbation) to push it over the ridge into a different valley. For instance this explains why just a few transiently expressed factors can permanently transform a cell into a cancerous state.

https://substackcdn.com/image/fetch/$s_!IRZh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fff841b80-05b4-4005-b6cf-8fdf79012643_816x702.png

This phrase “for free” is crucial. It means the pattern does not need to be constructed from scratch by evolution or learned from data. It is already there, latent in the structure of the system, waiting to be tapped into. The cancer cells do not evolve toward an atavistic state through mutations, but because the Platonic valley already encodes the state.

This is a signature of a Platonic structure. Same patterns get reused across different contexts because they are attractors in the underlying latent space. Same atavistic network motifs are present in the reversal to [atavism during aging](https://onlinelibrary.wiley.com/doi/10.1111/acel.70305), or when you are growing [primary 2D cell cultures](https://pubmed.ncbi.nlm.nih.gov/41111196/). Evolution clearly hasn’t been “optimizing” for this. These patterns recur because they are pre-existing attractors in the landscape.

Now I can confidently answer my classmate that the forms are these attractors that exist as stable states in the dynamics of the system waiting to be occupied.

## But why should you care about abstract representations?

Understanding why this matters requires distinguishing two types of causality: proximate and ultimate.

Proximate causality asks “how” questions. What molecular pathway, what mutation, what signal. Ultimate causality asks a “why” question. Why does this particular stable state exist? Why does this pattern keep recurring across contexts?

Biologists typically think that there are two ultimate causes: genetics and environment. However, these are still proximate mechanisms since they do not answer why these specific states exist in the first place. **The structure of reality itself constrains which states are possible and reachable.** The attractor landscape is not encoded in any single gene, nor is it purely environmental. It comes from the dynamics of the entire regulatory network. Similarly, a Platonic representation is not learned from any single training example but comes from the statistical structure that all observations share.

Platonic forms operate at the level of ultimate causation. They do not replace molecular details (proximate causality) but provide a framework for understanding why those details organize themselves the way they do. As we will see, this becomes very relevant in things like drug discovery.

If the concept of Platonic representations is correct, it should extend beyond just biology.

Neural Networks also offer a glimpse into this. The Platonic Representation Hypothesis, proposed by [Huh et al.](https://arxiv.org/pdf/2405.07987), states that neural networks trained with different objectives on different data and modalities are converging to a shared statistical model of reality in their representation spaces.

https://substackcdn.com/image/fetch/$s_!VY3Q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F880bff83-3e45-478b-902b-bf56658d3a8b_856x890.png

Neural networks trained on completely different data (images versus text) with completely different training objectives are learning increasingly similar representations of the world. The better the model is, the more their internal representations converge. You can think of the training data as the shadows on the cave wall, and the model recovering better representations of the actual world outside the cave.

https://substackcdn.com/image/fetch/$s_!qCu3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fab12fa5a-029e-42de-8c13-e692b26bbedb_1600x548.png

If the Platonic Representation Hypothesis is correct, we should see convergence in biological data too since they are both projecting the same functional state of the cell. Even with primitive models and limited samples. The next part of the article will concern how these concepts are relevant in the context of drug discovery.

If the Platonic Representation Hypothesis holds for biology, we should expect:

1. Models trained on different modalities should agree on which drugs are similar

2. This agreement should increase with model scale and data diversity

3. Supervision should accelerate convergence (by providing shared constraints)

4. Even unsupervised models should show some alignment (because the underlying biology is shared)

## Experimental setup

I compare four embedding spaces derived from different biological measurement modalities

https://substackcdn.com/image/fetch/$s_!E3p9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F31d2a9a7-f650-4c83-923d-0ac2a5a68235_1254x550.png

The supervised models predict mechanism of action (MOA) labels with embeddings are taken from the second to last layer. The unsupervised models are simple autoencoders with no label information.

**I am not testing if the embeddings are directly compatible. Instead I test whether they agree on which drugs are similar to which other drugs. In other words, we are asking if the geometry of drug relationships in the latent space look the same regardless how you measure it.**

https://substackcdn.com/image/fetch/$s_!Ol5K!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d538f8b-1200-4d18-87d3-93853ddee6f2_1024x800.png

## Evaluating Mutual k-Nearest Neighbors

I adapt the mutual k-NN metric from Huh et al. to biology by defining “items” as drugs rather than individual samples. For each modality, I compute drug centroids by averaging embeddings across replicates.

We are asking if drug A’s nearest neighbors in Space 1 are {B, C, D}, and its nearest neighbors in Space 2 are {C, D, E}, how much overlap is there? An mNN enrichment of 1× means chance-level agreement and higher values indicate shared structure.

Example of comparing adenosine across Cell Painting and L1000:

1. CP neighbors: \[drug\_3, drug\_7, drug\_2, drug\_9, drug\_1\]

2. L1000 neighbors: \[drug\_2, drug\_5, drug\_1, drug\_8, drug\_6\]

3. Overlap: {drug\_2, drug\_1} → 2 out of 5 shared

## Results

CP and L1000 embeddings become increasingly aligned as training progresses with mNN enrichment rises across epochs, strongest at small k. Models learn local similarity structure first.

https://substackcdn.com/image/fetch/$s_!eeE7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5455b97a-bc16-44be-abbe-b567900426c6_1000x496.png

The local neighborhood structure agrees even though the raw embedding spaces are completely different. Importantly, the models weren’t trained to agree on neighborhoods, only on MOA classification.

### MOA-dependent convergence

When I stratify the mNN by MOA class we see that some MOAs have a clear convergence over training while others remain low. There is a clear shared structure across modalities, but obviously with each capturing unique information.

https://substackcdn.com/image/fetch/$s_!BUy7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93a86393-355a-4760-a819-3a5fe0ead0be_856x712.png

Topoisomerase inhibitors and DNA synthesis inhibitors show the highest cross-modal alignment (mNN = 0.31 and 0.30). GPCR modulators like dopamine, adrenergic, and acetylcholine receptor antagonists cluster at the bottom (mNN < 0.12). When a drug pushes cells into a coherent attractor state (like the DNA damage response), both modalities see the same thing from different angles. The state itself is consistent with changes to the chromatin, morphology, transcriptional programs.

But when a drug makes a localized perturbation that does not engage a coherent cellular program, two modalities seem to capture different fragments. Blocking a dopamine receptor in an osteosarcoma cell doesn’t push the cell into a well-defined attractor.

### Platonic space map

Now, we can scale this procedure to check alignment between various modalities and methods of training.

https://substackcdn.com/image/fetch/$s_!DU0q!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7e3466a-bbef-4539-bf45-b35612fc198a_1600x1456.png

We see that the shared neighborhood structure across different measurement modalities is induced under supervision.

The CP <> L1000 Supervised pair shows the highest alignment (mNN enrichment ~8x). This shows that models trained on the same label space (MOA) converge toward a shared relational structure despite being trained on entirely different measurement modalities (morphology vs. transcriptomics).

Unsupervised models show moderate but real alignment. The L1000 Unsup <> Tahoe Unsup pair achieves ~2.2x enrichment despite using simple autoencoders trained independently on different gene expression datasets. This suggests that even without labels, the underlying biological structure partially surfaces in learned representations.

The goal of this toy example was to test whether Platonic representations exist in the current biological data. Whether different measurement modalities, when learning to represent drugs, converge towards a shared structure even when trained independently.

The answer appears to be yes, with important caveats.

The strongest evidence comes from the supervised setting. Models trained on Cell Painting and L1000 transcriptomics, using the same MOA labels but no shared architecture or training, learn representations where similar drugs cluster together across modalities. This is exactly what the Platonic Representation Hypothesis predicts.

More surprising is that even simple unsupervised autoencoders show partial alignment. The L1000 <> Tahoe comparison demonstrates that two gene expression datasets (with no labels and no architectural sharing) learn overlapping drug neighborhoods. The alignment is modest (~2x) but consistent. Importantly, it emerges from models with only thousands of training samples, compared to the hundreds of millions used in Huh et al.’s original work on vision-language convergence.

This suggests that Platonic structure in biology may be detectable even with primitive models and limited data. The next step would be to extend this work to foundation models like scGPT, Geneformer. If the Platonic Representation Hypothesis holds, we should see mNN enrichment increase with model scale and data diversity.

In “ [Multi-Modal Representation learning for molecules](https://openreview.net/pdf?id=WT7BpLvL6D)” we see that pretraining a molecular encoder on Cell Painting morphology improves downstream ChEMBL tasks by ~6% in low-data settings. Adding transcriptomics on top gives more gains. This is consistent with a well known phenomenon when pre-training on video helps you increase fine tuning performance on text.

https://substackcdn.com/image/fetch/$s_!rFfR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0b63be6b-9049-4413-b0b5-216180a42759_1600x993.png

Hopefully you can now see how different biological “shadows” can guide towards the same reality.

What exactly do these embeddings encode? At minimum, they capture where drugs push cells in state space. But they also might encode the attractor basin cells occupy, or even properties of the dynamics that generate those attractors. This distinction matters. Snapshot level representations tell you which drugs have similar immediate effects, while attractor level representations tell you which drugs produce equivalent endpoints regardless of path. Landscape level representations could predict how drugs interact and how resistance emerges. My current experiments can not distinguish these levels. Doing so would require time series data and perturbation combination experiments. But these questions are definitely worth asking.

The implications of Platonism in biomedicine become more interesting when we consider scale.

In their analysis of vision and language models, Huh et al. observed a correlation that the larger the model and the more data it consumes, the more strongly it converges toward a shared representation. Models that aligned more closely with vision showed superior performance on downstream tasks like Hellaswag (common-sense reasoning) and GSM8K (math).

https://substackcdn.com/image/fetch/$s_!fy9I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5e79c71f-618a-4b39-a233-910450dd7e75_1600x627.png

Biology is still in the age of small, siloed data. But if the same scaling principles hold, it suggests at least two things:

**Simplified assays may be enough**. You just need to capture the relevant Platonic patterns of the system without fully replicating it. Cellarity [achieves](https://www.nature.com/articles/s41467-025-65690-3) 88% sensitivity and 100% specificity on liver toxicity using transcriptomics from sandwich cultures. Likewise, [Axiom is using](https://www.alexkesin.com/p/a-better-proxy-than-the-rat-and-dog) “flattened spheroid” with seemingly good performance. These are not perfect models of human liver, but they may be projecting enough of the underlying structure to be useful. Why might simplified assays be sufficient? If we were trying to measure exact cellular state, we would need a high resolution measurement in a physiologically relevant system. But if we are trying to identify the attractor basin a drug pushes into, the task is easier. Attractors are stable and self-maintaining states. A flattened spheroid can’t capture every transcriptional nuance, but it might reliably distinguish a healthy hepatocyte attractor from a stressed hepatocyte attractor from a fibrotic attractor. The platonic structure does the heavy lifting.

**Scale and multimodality should compound**. The more data you integrate across modalities, the more constraints you place on the learned representation which forces it to capture Platonic structure that works across all tasks. For example, [you can predict](https://www.nature.com/articles/s41591-025-03856-8) biological age on par/better compared to most advanced aging clocks using LLMs. Anecdotally, you can prompt LLM to get novel clinically relevant SMILES signatures of a chemical. Asking LLM with a pathway level outcome of a chemical perturbation sometimes gives you better performance compared to frontier perturbational models on a single cell level.

# Conclusion

I showed here a modest experiment where drug embeddings learned from morphology and transcriptomics agree on neighborhood structure, and that this agreement increases with training.

But the implications are not modest. For example, cancer becomes less about accumulating the right mutations and more about cells falling into latent attractors that were always present in the landscape. Aging becomes less about reversing molecular damage and more about understanding why cells drift from their proper valleys.

To skeptics who demand to “see the forms”, I can finally point to them. Moreover, these representations are measurable, and not just a philosophical metaphor. Neural networks, cells, mathematical abstraction all offer empirical windows into these representations.

The Platonic world is wide open for you to explore!

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="back-into-plato-s-cave-examining-cross-modal-representationa-1.md">
<details>
<summary>Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale</summary>

Phase: [EXPLORATION]

**Source URL:** <https://arxiv.org/html/2604.18572v2>

# Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale

A. Sophia Koepke1,2,3  Daniil Zverev2  Shiry Ginosar4  Alexei A. Efros1

1UC Berkeley  2Technical University Munich, MCML

3University of Tübingen, Tübingen AI Center  4Toyota Technical Institute at Chicago

###### Abstract

The Platonic Representation Hypothesis \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] suggests that neural networks trained on different modalities (e.g., text and images) align and eventually converge toward the same representation of reality. If true, this has significant implications for whether modality choice matters at all.
We show that the experimental evidence for this hypothesis is fragile and depends critically on the evaluation regime.
Alignment is measured using mutual nearest neighbors on small datasets (≈\\approx1K samples) and degrades substantially as the dataset is scaled to millions of samples. The same behavior is observed beyond text-image, for text-audio and text-video alignment. The alignment that remains between model representations reflects coarse semantic overlap rather than consistent fine-grained structure. Moreover, the evaluations in Huh et al. \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] are done in a one-to-one image-caption setting, a constraint that breaks down in realistic many-to-many settings and further reduces measured alignment.
We also find that the reported trend of stronger language models increasingly aligning with vision does not appear to hold for newer models.
Overall, our findings suggest that the current evidence for cross-modal representational convergence is considerably weaker than subsequent works have taken it to be. Models trained on different modalities may learn equally rich representations of the world, just not the same one.

Project page: [https://akoepke.github.io/cave\_umwelten](https://akoepke.github.io/cave_umwelten "")

## 1 Introduction

The success of Large Language Models (LLMs) is causing much hand-wringing in the computer vision community: do we even need pixels to build machines that understand our world, or is language “all you need”?

Several works have demonstrated that models trained only on text data successfully solve what were thought to be fundamentally visual problems, such as visual question answering (VQA) \[ [32](https://arxiv.org/html/2604.18572v2#bib.bib32 ""), [40](https://arxiv.org/html/2604.18572v2#bib.bib40 "")\], visual reasoning \[ [11](https://arxiv.org/html/2604.18572v2#bib.bib11 ""), [39](https://arxiv.org/html/2604.18572v2#bib.bib39 ""), [98](https://arxiv.org/html/2604.18572v2#bib.bib98 ""), [2](https://arxiv.org/html/2604.18572v2#bib.bib2 "")\], or embodied robotics applications \[ [1](https://arxiv.org/html/2604.18572v2#bib.bib1 ""), [57](https://arxiv.org/html/2604.18572v2#bib.bib57 "")\].
This resonates with the suggestion that text data may make other modalities redundant \[ [88](https://arxiv.org/html/2604.18572v2#bib.bib88 "")\], on the premise that the part of the world that is relevant to humans is manifest in language.
On the other hand, it is argued that linguistic data alone cannot yield genuine understanding \[ [9](https://arxiv.org/html/2604.18572v2#bib.bib9 "")\] or allow actual embodiment. After all, there is a reason we visit art museums rather than just read descriptions of paintings in a catalogue.
This raises a central question: how do models trained on different modalities represent reality?

The Platonic Representation Hypothesis \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] offers a compelling answer: as neural networks grow larger and consume more data, their learned representations will become more and more aligned, no matter which data modality (text, vision, audio, touch, etc.) was used for training.
Proponents of language-only learning have interpreted this as validation of their approach:
since the choice of modality does not matter as they all lead to the same shared representation, one might as well use language as the most convenient source of data.111But analogously, the same argument could be made for vision-only learning \[ [43](https://arxiv.org/html/2604.18572v2#bib.bib43 "")\]. However, the strength of a hypothesis depends on the strength of its evidence, and the experimental protocol underpinning the claim rests on specific methodological choices that have largely gone unexamined in subsequent work.

https://arxiv.org/html/2604.18572v2/x1.png

https://arxiv.org/html/2604.18572v2/x2.png

Figure 1: Illustration of the mutual nearest neighbor metric used by Huh et al. \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] to measure cross-modal alignment.
(a) Sparse regime: given a query image and caption (blue), nearest neighbors (NN) are retrieved independently in image and text embedding spaces. Mutual NN alignment measures whether the NNs are consistent across modalities. (b) Dense regime: as dataset size increases, NNs within each modality get better. The vision model retrieves a car in the same pose, and the language model retrieves a caption of the same car model regardless of pose. At scale, improved within-modality organization does not translate into cross-modal agreement.

In this paper, we take a closer look at the experimental evidence for the hypothesis and find it to be fragile and to depend critically on the evaluation regime. Huh et al. \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] conducted their analysis on small, sparse datasets with one-to-one correspondences between modalities. However, real-world multi-modal data is large, dense, and inherently many-to-many: one image has many valid descriptions, and a single caption can correspond to many plausible images. These differences fundamentally change what it means for two representations to “align”.

In a small dataset, weakly related samples may become nearest neighbors simply because no better alternatives exist (Fig. [1](https://arxiv.org/html/2604.18572v2#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") a). Here, two models can agree despite organizing their representations differently. As the dataset grows (i.e. the gallery used for retrieving nearest neighbors gets denser), both models find closer neighbors and cross-modal consistency requires more fine-grained structural alignment (Fig. [1](https://arxiv.org/html/2604.18572v2#S1.F1 "Figure 1 ‣ 1 Introduction ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") b).
A vision model may retrieve an image of a car taken from a similar angle as the query, while the language model retrieves a caption describing the same car model as the query but in a different pose. Both are valid, but inconsistent between modalities, producing a mismatch that gets penalized under the mutual nearest-neighbor metric.
This illustrates how mutual nearest-neighbor agreement becomes an increasingly strict measure for alignment in many-to-many regimes. Using a mutual kkNN metric with k>1k>1 is less strict, but does not fundamentally change the conclusion.

In this paper, we examine how cross-modal alignment changes in evaluation settings with large, dense, and non-bijective datasets, and observe the following:

Alignment degrades with scale: Increasing the gallery from 10241024 to millions of samples causes a sharp drop in cross-modal mutual nearest-neighbor agreement.Coarse agreement persists but fine-grained agreement does not: In controlled settings (e.g., ImageNet), vision and language models reliably retrieve correct-class neighbors but rarely agree on the same instance.Many-to-many correspondence reduces alignment: Allowing multiple valid correspondences per sample leads to drops in agreement, even when retrieved neighbors are semantically sensible.Previously reported trends may not hold for newer models: The claim that stronger language models align better with vision seems to weaken for more recent models.

These findings paint a more mixed picture than the small-gallery results from Huh et al. suggest. Models trained on different modalities can learn rich and semantically meaningful structure, yet still organize that structure differently. Low agreement does not imply poor representations, it reflects differences in how information is arranged. These patterns are not specific to text and images. We observe similar behavior at scale for text-audio and text-video alignment.
Nearly a century ago, von Uexküll \[ [95](https://arxiv.org/html/2604.18572v2#bib.bib95 "")\] argued that every organism inhabits its own perceptual world, or Umwelt, shaped by its senses rather than by an observer-independent reality. The same, we believe, might hold for our models: each constructs its own representational structure, determined by its modality and training data, rather than converging toward a shared model of reality. Though it is still early days, we suspect future evidence will favor von Uexküll over Plato.

## 2 Related Work

One Platonic Ideal vs many Umwelten.
In his “Theory of Forms”, Plato argued that every physical object we perceive is a flawed imitation (a shadow) of some eternal, abstract “ideal” form \[ [76](https://arxiv.org/html/2604.18572v2#bib.bib76 "")\], and only by escaping from the tyranny of our physical senses (leaving the cave of shadows), we can achieve true understanding. But in the 20th century, this argument for a single, unified Platonic Ideal representation has been repeatedly undercut by biologists, psychologists, and philosophers. Biologist von Uexküll argued that every organism inhabits its own perceptual environment, or Umwelt\[ [95](https://arxiv.org/html/2604.18572v2#bib.bib95 "")\]: a tick lives in a world of thermal gradients, a bat in a world of echoes. The different Umwelten might have only little overlap with each other222For a tour of von Uexküll’s ideas, see Koenderink’s delightful book \[ [48](https://arxiv.org/html/2604.18572v2#bib.bib48 "")\].. Gibson’s ecological psychology \[ [27](https://arxiv.org/html/2604.18572v2#bib.bib27 "")\] pushed this further, proposing that perception is shaped by what an organism can do in its environment, not by an observer-independent reality.
Philosopher Wittgenstein, thinking about language, arrived at a strikingly similar conclusion. He famously argued: “If a lion could speak, we could not understand him” \[ [102](https://arxiv.org/html/2604.18572v2#bib.bib102 "")\], meaning that the lion’s world (goals, instincts, perceived reality) is so utterly different from our own, that even if it spoke English, we would not comprehend the meaning333For a great treatment of Wittgenstein’s argument in popular culture, see the episode Darmok of the American TV series Star Trek: The Next Generation.. Building on Wittgenstein, psychologist Rosch developed her Prototype Theory of Categorization \[ [80](https://arxiv.org/html/2604.18572v2#bib.bib80 "")\], arguing against a single platonic ideal as a representation of object categories, proposing a data-driven clustering-based model instead.

Representational alignment. The question of representational similarity has been studied extensively in the neurosciences \[ [21](https://arxiv.org/html/2604.18572v2#bib.bib21 ""), [35](https://arxiv.org/html/2604.18572v2#bib.bib35 ""), [50](https://arxiv.org/html/2604.18572v2#bib.bib50 "")\]. In machine learning, the parallel question of whether independently trained networks learn similar internal structure has received growing attention.
Lenc and Vedaldi \[ [54](https://arxiv.org/html/2604.18572v2#bib.bib54 "")\] investigated the equivalence of representations from different trained models and found that early convolutional layers are more interchangeable than later ones. This task, also referred to as “model stitching”, was later revisited by Bansal et al. \[ [6](https://arxiv.org/html/2604.18572v2#bib.bib6 "")\]. Related to this, Li et al. \[ [56](https://arxiv.org/html/2604.18572v2#bib.bib56 "")\] proposed methods to align neurons across independently trained networks. More recently, Dravid et al. \[ [20](https://arxiv.org/html/2604.18572v2#bib.bib20 "")\] introduced “Rosetta Neurons,” showing that different vision models share common units corresponding to similar visual concepts across architectures, tasks, and training data.
Tasker et al. \[ [89](https://arxiv.org/html/2604.18572v2#bib.bib89 "")\] propose the Universal Normal Embedding hypothesis, where encoder and generative latents are interpreted as noisy views of an approximately Gaussian shared space.

Furthermore, alignment has been linked with shared model capabilities measured by task performances \[ [5](https://arxiv.org/html/2604.18572v2#bib.bib5 ""), [47](https://arxiv.org/html/2604.18572v2#bib.bib47 ""), [42](https://arxiv.org/html/2604.18572v2#bib.bib42 ""), [69](https://arxiv.org/html/2604.18572v2#bib.bib69 ""), [6](https://arxiv.org/html/2604.18572v2#bib.bib6 "")\]. To directly quantify representational similarities, several metrics have been used to measure correlations between features \[ [69](https://arxiv.org/html/2604.18572v2#bib.bib69 ""), [38](https://arxiv.org/html/2604.18572v2#bib.bib38 "")\]. Kornblith et al. \[ [49](https://arxiv.org/html/2604.18572v2#bib.bib49 "")\] introduced Central Kernel Alignment (CKA) as a robust measure invariant to orthogonal transformations and isotropic scaling. Huh et al. \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] found the CKA metric to reveal only a “very weak trend of alignment between models” and therefore proposed the use of the mutual kkNN metric that measures the overlap of two sets of neighborhoods of size kk.

Multi-modal alignment. Early efforts to connect images and text utilized human annotations \[ [96](https://arxiv.org/html/2604.18572v2#bib.bib96 "")\]. The curation of large-scale paired image-caption datasets, such as MS-COCO \[ [58](https://arxiv.org/html/2604.18572v2#bib.bib58 "")\] and Visual Genome \[ [51](https://arxiv.org/html/2604.18572v2#bib.bib51 "")\], facilitated the systematic study of cross-modal correspondence and models. The CLIP model \[ [78](https://arxiv.org/html/2604.18572v2#bib.bib78 "")\] by Radford et al. formed a turning point by demonstrating that contrastive learning on web-scale image-text pairs could produce shared embedding spaces.

Since, a growing body of work has investigated whether such alignment arises even without explicit joint training. Merullo et al. \[ [67](https://arxiv.org/html/2604.18572v2#bib.bib67 "")\] showed that a simple learned linear transformation could map between frozen vision encoders and LLMs. Moschella et al. \[ [70](https://arxiv.org/html/2604.18572v2#bib.bib70 "")\] use similarities to an anchor set.
Maniparambil et al. \[ [64](https://arxiv.org/html/2604.18572v2#bib.bib64 "")\] demonstrated that even unaligned unimodal encoders possess high semantic similarity. Li et al. \[ [55](https://arxiv.org/html/2604.18572v2#bib.bib55 "")\] study alignment at the level of shared categories. Complementary to that, Lu et al. \[ [63](https://arxiv.org/html/2604.18572v2#bib.bib63 "")\] define each sample by its angular distances to others, improving training-free alignment across vision, language, and audio.

Fully unsupervised approaches include blind vision-language matching \[ [82](https://arxiv.org/html/2604.18572v2#bib.bib82 "")\] and unpaired embedding translation via cycle-consistency \[ [44](https://arxiv.org/html/2604.18572v2#bib.bib44 ""), [107](https://arxiv.org/html/2604.18572v2#bib.bib107 "")\].
Finally, Gupta et al. \[ [33](https://arxiv.org/html/2604.18572v2#bib.bib33 "")\] show that an orthogonal map can map between independently trained multi-modal contrastive models. These results are often seen as evidence for representational convergence, also supported by Lu et al. \[ [62](https://arxiv.org/html/2604.18572v2#bib.bib62 "")\] in their survey of multimodal alignment.
However, those results are obtained in restricted settings (e.g. \[ [82](https://arxiv.org/html/2604.18572v2#bib.bib82 "")\] experiments on CIFAR-100 and ImageNet-100) and do not scale to real-world multi-modal data. Our work examines whether alignment survives beyond these constraints, showing that it decreases at scale and reflects coarse categorical agreement rather than shared fine-grained structure.

Limits and measurement of emergent cross-modal structure.
Several analyses show that alignment between independently trained unimodal encoders depends strongly on data, architecture, and evaluation protocol. Tjandrasuwita et al. \[ [92](https://arxiv.org/html/2604.18572v2#bib.bib92 "")\] find that alignment varies with modality similarity and the balance of shared versus unique information, while Hadgi et al. \[ [34](https://arxiv.org/html/2604.18572v2#bib.bib34 "")\] report weaker alignment for “pure” 3D encoders without careful subspace selection. Zhu et al. \[ [108](https://arxiv.org/html/2604.18572v2#bib.bib108 "")\] further show that video–text alignment depends on temporal richness and text availability.

Gröger et al. \[ [31](https://arxiv.org/html/2604.18572v2#bib.bib31 "")\] show that global similarity measures such as CKA are sensitive to network scale and can be altered via null calibration, largely removing evidence of global convergence while leaving local neighborhood similarity (e.g., mutual kkNN) more stable, though still evaluated under small-scale and bijective regimes.
Beyond similarity metrics, Smith et al. \[ [86](https://arxiv.org/html/2604.18572v2#bib.bib86 "")\] and Kumar et al. \[ [52](https://arxiv.org/html/2604.18572v2#bib.bib52 "")\] show that functional agreement and output behavior can persist even when internal representations are misaligned or entangled, suggesting that behavioral compatibility does not imply shared structure.
These caveats echo grounding arguments that text-only learning may be insufficient to recover perceptual structure \[ [7](https://arxiv.org/html/2604.18572v2#bib.bib7 ""), [53](https://arxiv.org/html/2604.18572v2#bib.bib53 "")\], and motivate multimodal foundation models that integrate perception and language at scale \[ [41](https://arxiv.org/html/2604.18572v2#bib.bib41 ""), [4](https://arxiv.org/html/2604.18572v2#bib.bib4 ""), [68](https://arxiv.org/html/2604.18572v2#bib.bib68 ""), [37](https://arxiv.org/html/2604.18572v2#bib.bib37 "")\].

## 3 Experimental setup

Mutual kkNN metric.
To measure alignment between representations from different models, we use the mutual kk-nearest-neighbor metric (illustrated in [Fig.˜1](https://arxiv.org/html/2604.18572v2#S1.F1 "In 1 Introduction ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale")), following Huh et al. \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\].
Given a shared gallery set of nn datapoints (referred to as mini-batch sampled from the data distribution in \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\]) encoded into feature vectors 𝐚𝐢∈ℝd1\\mathbf{a\_{i}}\\in\\mathbb{R}^{d\_{1}} and 𝐛𝐢∈ℝd2\\mathbf{b\_{i}}\\in\\mathbb{R}^{d\_{2}} by two models with i∈{1,⋯,n}i\\in\\{1,\\cdots,n\\}, we first L2-normalize each representation. We then retrieve the kk nearest neighbors of every query point independently for each model (e.g. image and text query for vision and language encoders):

|     |     |     |
| --- | --- | --- |
|  | 𝒩k𝐚​(i)=argtopkj≠i⁡𝐚i⊤​𝐚j,𝒩k𝐛​(i)=argtopkj≠i⁡𝐛i⊤​𝐛j.\\mathcal{N}^{\\mathbf{a}}\_{k}(i)=\\operatorname{argtopk}\_{j\\neq i}\\mathbf{a}\_{i}^{\\top}\\mathbf{a}\_{j},\\qquad\\mathcal{N}^{\\mathbf{b}}\_{k}(i)=\\operatorname{argtopk}\_{j\\neq i}\\mathbf{b}\_{i}^{\\top}\\mathbf{b}\_{j}. |  |

The per-sample score is the number of overlapping samples normalized by kk:

|     |     |     |
| --- | --- | --- |
|  | si=\|𝒩k𝐚​(i)∩𝒩k𝐛​(i)\|k,s\_{i}=\\frac{\|\\mathcal{N}^{\\mathbf{a}}\_{k}(i)\\cap\\mathcal{N}^{\\mathbf{b}}\_{k}(i)\|}{k}, |  |

and the overall mutual-kkNN score is the mean over all samples. A score of 1 means that every point’s kk nearest neighbors are identical in both spaces, and a score of 0 means that the kk nearest neighbors do not overlap. In the sparse gallery in [Fig.˜1](https://arxiv.org/html/2604.18572v2#S1.F1 "In 1 Introduction ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"), the query (blue) retrieves the same neighbor in both image and text spaces, giving a mutual kkNN score of 1 for k=1k{=}1.
A score of kn\\frac{k}{n} suggests chance-level expected overlap for independent random retrieval, which decreases for growing nn. Note that throughout we report raw mutual kkNN (as in \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\]).

https://arxiv.org/html/2604.18572v2/x3.pngFigure 2: Nearest-neighbor quality depends on data density.
We show 1010 within-modality nearest neighbors for image (DINOv2) and text (LLM) embeddings on a sparse WIT-1024 gallery (top) and a denser WIT-1M gallery (bottom). For text queries, retrieved captions and their corresponding reference images are shown. At smaller scale, nearest neighbors are less semantically precise. Nearest-neighbor structure becomes more semantically refined as gallery density increases.

Implementation details.
For most experiments, we use DINOv2-base \[ [74](https://arxiv.org/html/2604.18572v2#bib.bib74 "")\] as the vision encoder. We refer to this model as DINOv2 in the following. Our primary language model is OpenLlama3b \[ [93](https://arxiv.org/html/2604.18572v2#bib.bib93 ""), [26](https://arxiv.org/html/2604.18572v2#bib.bib26 "")\] (abbreviated as OpenLlama). Additional models are considered in the supplementary material ( [Section˜A.4](https://arxiv.org/html/2604.18572v2#A1.SS4 "A.4 Mutual cross-modal 𝑘NN alignment drops at scale across model pairs ‣ Appendix A Is the drop in mutual 𝑘NN alignment at scale caused by the metric, layer selection, caption quality, or by specific model choices? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale")). For each image and text sample, we extract the representations from all layers of their respective encoders and follow the experimental protocol from \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\]. Details about additional models used in [Section˜4](https://arxiv.org/html/2604.18572v2#S4 "4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") are provided in [Section˜E.3.2](https://arxiv.org/html/2604.18572v2#A5.SS3.SSS2 "E.3.2 Language models. ‣ E.3 Models and feature extraction pipeline ‣ Appendix E Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") in the supplementary material.
We use Faiss \[ [19](https://arxiv.org/html/2604.18572v2#bib.bib19 "")\] for nearest neighbor computation at scale. Specifically, we use their exact nearest neighbor implementation with IndexFlatL2, equivalent to using cosine similarity on normalized vectors.

https://arxiv.org/html/2604.18572v2/figures/alignment_vs_k_v6.png(a)Effect of neighborhood sizes kk in mutual kkNN (both axes log-scaled). Trivially, mutual kkNN converges to 1.0 as kk approaches the full gallery size. \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] utilized mutual kkNN for k=10k=10.

https://arxiv.org/html/2604.18572v2/figures/new_tum1m_dedup_alignment_v6.png(b)Alignment between DINOv2 and different LLMs, measured on WIT-1024 and WIT-1M. As observed in \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\], alignment (mutual kkNN) increases with language performance (measured as 1−bitsperbyte1-\\text{bitsperbyte} from \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\]) on the 1024-sample set, but this trend breaks with larger gallery size.

Figure 3: Mutual kkNN text-image feature alignment when scaling from WIT-1024 to WIT-1M. (a) shows the dependence on neighborhood size kk, while (b) examines alignment for different LLMs. The observation from \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\], that more capable language models align better with vision at fixed small kk largely vanishes at WIT-1M scale.

## 4 How much do representations align?

In this section, we take a close look at the experimental evidence underpinning the Platonic Representation Hypothesis \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\]. The experiments in \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] rest on two foundations that warrant scrutiny: the use of mutual kkNN alignment on a small evaluation set of only 1024 samples from the Wikipedia Image-Text (WIT) dataset \[ [87](https://arxiv.org/html/2604.18572v2#bib.bib87 "")\] (WIT-1024), and the use of data with
effectively bijective (one-to-one) image-text correspondences, an assumption implicit in the WIT-1024 setup rather than stated explicitly in \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\].
Typically, these choices are not acknowledged when the hypothesis is cited \[ [65](https://arxiv.org/html/2604.18572v2#bib.bib65 ""), [81](https://arxiv.org/html/2604.18572v2#bib.bib81 ""), [60](https://arxiv.org/html/2604.18572v2#bib.bib60 ""), [10](https://arxiv.org/html/2604.18572v2#bib.bib10 ""), [14](https://arxiv.org/html/2604.18572v2#bib.bib14 "")\]. The claim is usually invoked in its broad, appealing form rather than in the narrow terms under which experimental support was provided.

Here, we analyze how alignment behaves for a finer-grained metric (k=1k{=}1 instead of k=10k{=}10), and a denser gallery (million(s of) instead of 1024 samples). We then decompose what mutual kkNN alignment actually measures in a controlled setup on ImageNet. This reveals that models individually retrieve correct-class neighbors but rarely agree on which one, suggesting that information is organized differently in each unimodal model.
We then turn to the bijective assumption, and examine what happens when it is relaxed. We further test whether these patterns extend beyond text-image to the text-audio and text-video settings. Finally, we perform a trend check to ask whether the predictions from \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] have held up as models have improved.

Sensitivity to kk in mutual kkNN. Huh et al. \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] reported mutual kkNN alignment for k=10k{=}10. We additionally evaluate at k=1k{=}1, which requires the two representation spaces to agree on the single nearest neighbor. As shown in [Fig.˜3(a)](https://arxiv.org/html/2604.18572v2#S3.F3.sf1 "In Figure 3 ‣ 3 Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"), the metric trivially converges to 1 as kk approaches the full gallery size nn, since both neighbor sets then contain all samples. Even moderate values of kk can inflate scores by capturing broadly similar rather than precisely matching neighbors. In our analyses at larger gallery scales, we perform deduplication to prevent near-duplicate samples from trivially inflating neighborhood overlap (see [Section˜E.1](https://arxiv.org/html/2604.18572v2#A5.SS1 "E.1 WIT-1M and LAION-15M datasets ‣ Appendix E Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") in the supplementary material for details).

### 4.1 Alignment across dataset scales

Nearest neighbors in sparse gallery.
We now turn to the data, and ask whether the 1024-sample gallery used in \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] is too sparse to capture more than coarse structural agreement.

Table 1: Nearest-neighbor quality across gallery sizes. As the gallery grows, nearest neighbors get closer to the query set in both DINOv2 and OpenLlama embedding spaces, facilitating a more fine-grained analysis of cross-modal alignment.

| Gallery | Model | k=1k{=}1 | k=10k{=}10 |
| --- | --- | --- | --- |
| WIT-1024 | DINOv2 | 0.799 | 0.717 |
| WIT-1024 | OpenLlama | 0.502 | 0.400 |
| WIT-1M | DINOv2 | 0.906 | 0.888 |
| WIT-1M | OpenLlama | 0.757 | 0.701 |

As shown in [Table˜1](https://arxiv.org/html/2604.18572v2#S4.T1 "In 4.1 Alignment across dataset scales ‣ 4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"), the mean cosine similarity between queries and nearest neighbors in terms of both image (DINOv2) and text features (OpenLlama) is significantly lower for the WIT-1024 gallery compared to WIT-1M (e.g. 0.799 compared to 0.906 for DINOv2 at k=1k{=}1). Note that in both cases, we use WIT-1024 as the query set.

We visualize nearest neighbors for k=10k{=}10 for image and text features on WIT-1024 and WIT-1M in [Fig.˜2](https://arxiv.org/html/2604.18572v2#S3.F2 "In 3 Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale").
At low density, semantically unrelated samples may end up as nearest neighbors as there is nothing closer available, meaning that measured mutual kkNN agreement mainly can reflect the shared lack of alternatives. To get more meaningful insights, we scale the density of the retrieval gallery in the following section.

https://arxiv.org/html/2604.18572v2/figures/nested_wit1m_v6style.png

https://arxiv.org/html/2604.18572v2/figures/nested_laion15m_v6style.png

Figure 4: Scaling the gallery size to 1M (WIT) and 15M (LAION) shows a large drop in mutual kkNN alignment for k=1k{=}1 and k=10k{=}10 for DINOv2 and OpenLlama features.

Densification by scaling the gallery size. Having established that the WIT-1024 gallery captures mainly coarse structure, we densify the gallery and test whether alignment persists. We evaluate on up to 1M and 15M gallery samples from the English-text WIT \[ [87](https://arxiv.org/html/2604.18572v2#bib.bib87 "")\] and LAION400M \[ [83](https://arxiv.org/html/2604.18572v2#bib.bib83 "")\] respectively. The best layer pair was determined on the 1024-sample subset of WIT (see ablation in [Section˜A.2](https://arxiv.org/html/2604.18572v2#A1.SS2 "A.2 Sanity check: is the alignment drop an artifact of the layer pair selected at WIT-1024? ‣ Appendix A Is the drop in mutual 𝑘NN alignment at scale caused by the metric, layer selection, caption quality, or by specific model choices? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") in the supplementary material), following \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\].

As shown in [Fig.˜4](https://arxiv.org/html/2604.18572v2#S4.F4 "In 4.1 Alignment across dataset scales ‣ 4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"), alignment scores decrease as gallery size grows for fixed kk and query set (WIT-1024). The mutual kkNN alignment scores drop from 0.135 and 0.058 on the 1024-sample gallery to 0.008 and 0.001 on LAION-15M for k=10k=10 and k=1k=1 respectively. This confirms that the agreement observed at small scale declines with the transition to finer-grained evaluation at large scale. Nearest neighbors become closer and more semantically similar to the query, placing greater demand on the two representation spaces to agree on subtle distinctions.

Interestingly, alignment at k=n/100k{=}n/100 remains relatively stable across scales, suggesting that models share some degree of coarse structural agreement.
We hypothesize that this amounts to precisely the kind of broad categorical correspondence one would expect from models trained on overlapping internet data, and lacks signal about whether representations are organized in the same way.

We also analyze how mutual kkNN alignment for various LLMs and DINOv2 behaves at the WIT-1M scale. Reproducing the setting of \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\], [Fig.˜3(b)](https://arxiv.org/html/2604.18572v2#S3.F3.sf2 "In Figure 3 ‣ 3 Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") shows a clear trend on WIT-1024: stronger language models exhibit higher alignment with visual features. This is a central finding of \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] and one of their most compelling pieces of evidence. However, when we scale the gallery to 1M samples, this trend largely vanishes for fixed small kk. The gap between LLMs narrows considerably, and the relationship between model capability and alignment weakens. This suggests that the observation in \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] may be a result of the sparse evaluation setting.

Re-running this analysis
at k=n100k{=}\\frac{n}{100} on WIT-1M ( [Fig.˜14](https://arxiv.org/html/2604.18572v2#A1.F14 "In A.1 Sanity check: does mutual 𝑘NN inherently drop at scale even within modalities? ‣ Appendix A Is the drop in mutual 𝑘NN alignment at scale caused by the metric, layer selection, caption quality, or by specific model choices? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") in the
supplementary material), the alignment trend matches the k=10k{=}10 trend on WIT-1024. This is consistent with the stable broad categorical correspondence across scales that one expects from models trained on overlapping web data. It appears that the original mutual-kkNN evidence establishes coarse semantic-category overlap, not the fine-grained representational convergence the Platonic Representation Hypothesis is taken to claim. If modalities truly converged to the same representation, they would have to agree on fine-grained structure, not merely on category.

The nearest-neighbor examples in [Figs.˜5](https://arxiv.org/html/2604.18572v2#S4.F5 "In 4.1 Alignment across dataset scales ‣ 4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") and [6](https://arxiv.org/html/2604.18572v2#S4.F6 "Figure 6 ‣ 4.1 Alignment across dataset scales ‣ 4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") further illustrate this. Matches at small gallery sizes often break down as candidates are added, with each modality finding better but divergent neighbors. The matches at 1M and 15M scale are mostly near-duplicates our deduplication missed (e.g. a crop shifted by a few pixels). We show additional visualizations in [Figs.˜26](https://arxiv.org/html/2604.18572v2#A6.F26 "In Appendix F Additional qualitative results ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"), [27](https://arxiv.org/html/2604.18572v2#A6.F27 "Figure 27 ‣ Appendix F Additional qualitative results ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"), [28](https://arxiv.org/html/2604.18572v2#A6.F28 "Figure 28 ‣ Appendix F Additional qualitative results ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") and [29](https://arxiv.org/html/2604.18572v2#A6.F29 "Figure 29 ‣ Appendix F Additional qualitative results ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") in the supplementary material.

https://arxiv.org/html/2604.18572v2/x4.pngFigure 5: Nearest-neighbor (k=1k{=}1) examples with DINOv2 and OpenLlama across gallery scales on WIT-1M. Captions are shown with corresponding images. Mutual kkNN matches across modalities are framed green. While the bottom example shows a match at 1M scale, at larger scales each model finds closer but different matches (top two).https://arxiv.org/html/2604.18572v2/x5.pngFigure 6: Nearest-neighbor (k=1k{=}1) examples with DINOv2 and OpenLlama across gallery scales on LAION-15M. As the gallery densifies, each model finds closer but different matches (top example). The match at 15M (bottom right) is a near-duplicate that survived our deduplication pipeline.

We additionally test whether the alignment drop with increasing gallery size is merely an artifact of the mutual kkNN metric being harder at scale. Specifically, we measure within-modality alignment for two pairs of models: two language models of different scale (OpenLlama-3b and OpenLlama-13b), and, separately, two vision models (DINOv2-base and DINOv2-giant). If mutual kkNN alignment collapses for dense galleries regardless of the models being compared, the cross-modal drop observed would be uninformative. If within-modality alignment remains stable, the cross-modal drop is meaningful.

As shown in the supplementary material ( [Fig.˜13](https://arxiv.org/html/2604.18572v2#A1.F13 "In A.1 Sanity check: does mutual 𝑘NN inherently drop at scale even within modalities? ‣ Appendix A Is the drop in mutual 𝑘NN alignment at scale caused by the metric, layer selection, caption quality, or by specific model choices? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale")), unimodal alignment remains stable across gallery sizes. For the OpenLlama pair, mutual kkNN at k=1k{=}1 stays between \[0.59,0.62\]\[0.59,0.62\], and for the DINOv2 pair between \[0.35,0.45\]\[0.35,0.45\], across all gallery scales.
This confirms that mutual kkNN does not inherently collapse at scale.

Observation 1: Mutual kkNN alignment scores decrease for denser galleries for fixed small kk, suggesting that mutual kkNN is sensitive to gallery sparsity.
Furthermore, the reported trend that stronger language models align better with vision weakens substantially for fixed small kk at WIT-1M scale, with all models scoring near zero.

https://arxiv.org/html/2604.18572v2/x6.jpg(a)The query image (left) is matched with galleries of increasing density. As the gallery becomes more dense, DINOv2 and OpenLlama retrieve from the same class, but different instances, illustrating how within-class structure is organized differently across modalities.

https://arxiv.org/html/2604.18572v2/figures/ipc_alignment_with_accuracy.png(b)Per-modality retrieval accuracy and cross-modal mutual kkNN alignment (k=1k{=}1) as images / captions per class in gallery increase. Modalities individually improve with gallery density, but alignment does not.

Figure 7: Decomposing cross-modal alignment on ImageNet val. (a) shows a qualitative retrieval example where both models find plausible neighbors but disagree on the specific instance. (b) quantifies this: individual class-level retrieval accuracy improves with gallery density, yet strict alignment remains flat, illustrating that models organize within-class structure differently.

### 4.2 What is captured by cross-modal mutual kkNN alignment?

Low mutual kkNN alignment at fixed small kk could mean two things: the models individually retrieve poor neighbors, or they each retrieve good neighbors but different ones. The stability at k=n100k=\\frac{n}{100} hints at the models agreeing at a coarse level but diverging on fine-grained structure. To test this, we use the ImageNet \[ [16](https://arxiv.org/html/2604.18572v2#bib.bib16 "")\] validation set, where class labels let us evaluate each model’s retrieval independently.

We decompose each query into: (i) whether each model individually retrieves a correct-class neighbor, (ii) whether both do, and (iii) whether they agree on the exact same gallery item (mutual kkNN with k=1k{=}1). Our query set consists of one image per class (1000 images), and we vary the number of images per class (ipc) in the gallery from 1 to 49. We use detailed image captions (981 words on average) generated by gemini-3-flash-preview \[ [91](https://arxiv.org/html/2604.18572v2#bib.bib91 ""), [75](https://arxiv.org/html/2604.18572v2#bib.bib75 "")\], making this a favorable setting for alignment (details are provided in [Section˜E.2](https://arxiv.org/html/2604.18572v2#A5.SS2 "E.2 Captioning pipeline for the ImageNet validation set and WIT-1M-recap ‣ Appendix E Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") in the supplementary material).

[Fig.˜7](https://arxiv.org/html/2604.18572v2#S4.F7 "In 4.1 Alignment across dataset scales ‣ 4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") b reveals that as the gallery densifies, in line with Cover and Hart \[ [13](https://arxiv.org/html/2604.18572v2#bib.bib13 "")\], both models individually improve at retrieving correct-class neighbors.
This indicates some degree of shared coarse structure.
At larger scale, both models retrieve reasonable neighbors but different ones.
We see similar trends when looking at coarser evaluation with k=10k{=}10 (see [Section˜B.3](https://arxiv.org/html/2604.18572v2#A2.SS3 "B.3 ImageNet ablation shows a similar pattern for 𝑘=10 ‣ Appendix B Additional ImageNet experiments ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") in the supplementary material).
At 49 images per class in the gallery, DINOv2 succeeds 46.1% of the time and OpenLlama 58.0%.

Yet strict alignment on the exact same gallery item remains flat around 11%, even with detailed captions. For reference, alignment with captions that only consist of the class dropping from 0.42 to near zero as ipc increases.

https://arxiv.org/html/2604.18572v2/x7.jpgFigure 8: Shared mistake at ipc=1. The query image (bookstore) is matched by both DINOv2 and OpenLlama to a library image. The models agree, but on the wrong answer.

The models are individually capable but organize within-class structure differently ( [Fig.˜7(a)](https://arxiv.org/html/2604.18572v2#S4.F7.sf1 "In Figure 7 ‣ 4.1 Alignment across dataset scales ‣ 4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale")).
At ipc=1, strict alignment (23.1%) actually exceeds the rate at which both models retrieve a correct-class neighbor (11.7%), meaning the models often agree on semantically plausible but technically incorrect neighbors ( [Fig.˜8](https://arxiv.org/html/2604.18572v2#S4.F8 "In 4.2 What is captured by cross-modal mutual 𝑘NN alignment? ‣ 4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale")).

This reveals what mutual kkNN actually captures. It does not measure unimodal representation quality, but agreement on fine-grained structure. Our experiments provide direct evidence that low cross-modal alignment in terms of mutual kkNN is not due to poor representations but rather due to fundamentally different representational organization within modalities. Both models learn structured, high-quality representations. They simply do not structure them the same way.

Observation 2: As the data gets denser, both models retrieve correct-class neighbors at increasing rates, yet strict cross-modal mutual kkNN alignment is flat at 11%.
This is not a failure of unimodal representation quality, but of unaligned representational organization across modalities.

https://arxiv.org/html/2604.18572v2/figures/densifying_tv/densifying_images.png

https://arxiv.org/html/2604.18572v2/figures/densifying_tv/densifying_texts.png

Figure 9: Effect of relaxing the bijective assumption on text-image alignment, using the CycleReward dataset \[ [3](https://arxiv.org/html/2604.18572v2#bib.bib3 "")\]. We densify one modality by adding more images per caption (left) or more captions per image (right) while keeping the other fixed. Mutual kkNN alignment decreases consistently for both k=1k{=}1 and k=10k{=}10.

### 4.3 What happens when the data is not bijective?

https://arxiv.org/html/2604.18572v2/x8.pngFigure 10: Illustration of non-bijective (many-to-many) correspondence between image and captions. The nearest neighbor of a text caption for one image (blue) is a caption for a different image (red). However, the nearest image neighbor for a given image may be another image with the same caption.

In practice, the relationship between modalities, such as image and text, is inherently many-to-many: a single image can be described by countless text descriptions, and a single text caption can correspond to a large set of visually distinct images. More fundamentally, modalities often differ in information content.

Specifically, images encode spatial, textural, and perceptual structure that text captures only to a limited extent. On the other hand, text encodes abstraction, negation, and compositional semantics that images do not.
One could, in principle, bridge this gap trivially. For instance, one could encode pixel values as text or render captions as images and establish a bijection between those. Those preserve the information, but the inductive structure (the modality-specific properties that make each modality useful) of each modality is lost.

To test what happens when bijectivity is relaxed, we use the CycleReward dataset \[ [3](https://arxiv.org/html/2604.18572v2#bib.bib3 "")\] which pairs each real sample with multiple synthetic candidates. The I2T subset contains 11 generated captions per real image, and T2I consists of 12 synthetic images for each text prompt. This directly breaks the bijection, i.e. one-to-one matching, that our earlier analysis assumes.

We evaluate mutual kkNN by densifying one modality at a time: for T2I we keep the text fixed and increase the number of generated images per prompt, and for I2T we keep the image fixed and add generated captions.
For illustration, let us consider the T2I experiments where the closest neighbor in the densified modality is more likely to be a similar image that is associated with the same caption, while in the sparse text space the NN will be a caption for a different image. This creates a scenario where mutual kkNN fails (see [Fig.˜10](https://arxiv.org/html/2604.18572v2#S4.F10 "In 4.3 What happens when the data is not bijective? ‣ 4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale")).

We adapt the mutual kkNN metric so that a match is counted when the retrieved item corresponds to the same source sample, even if it is not the exact same caption or image. This is a generous relaxation within the mutual-kkNN framework.
In [Fig.˜9](https://arxiv.org/html/2604.18572v2#S4.F9 "In 4.2 What is captured by cross-modal mutual 𝑘NN alignment? ‣ 4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"), we see that the mutual kkNN scores still decrease as the one-to-one assumption is relaxed.
This drop may reflect genuinely weaker alignment, or simply that mutual kkNN cannot capture alignment well once a query has multiple valid correspondences. Distinguishing these would require a metric designed for many-to-many settings. Nevertheless, the convergence evidence in \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] rests on a bijective pairing that real-world multi-modal data rarely satisfies, and the standard metric does not extend cleanly beyond it.

Observation 3: A single image can be described in countless ways, and a single caption can match many visually distinct images. When we progressively relax the one-to-one assumption, mutual kkNN alignment drops consistently. However, the mutual kkNN metric cannot distinguish between genuine misalignment and many-to-many correspondence.

### 4.4 Text-audio and text-video alignment

To test whether our findings extend beyond the text-image setting, we evaluate alignment between LLMs and a video encoder (VideoMAE-v2 \[ [97](https://arxiv.org/html/2604.18572v2#bib.bib97 "")\]) on the PVD-100k dataset, a 100k subset of PVD \[ [8](https://arxiv.org/html/2604.18572v2#bib.bib8 ""), [100](https://arxiv.org/html/2604.18572v2#bib.bib100 "")\], and between LLMs and an audio encoder (Dasheng \[ [17](https://arxiv.org/html/2604.18572v2#bib.bib17 "")\]) on a 100k subset of LAION-Audio630k \[ [103](https://arxiv.org/html/2604.18572v2#bib.bib103 "")\].

[Fig.˜11](https://arxiv.org/html/2604.18572v2#S4.F11 "In 4.4 Text-audio and text-video alignment ‣ 4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") shows that the same patterns observed for text-image alignment hold across these modality pairs. Here, the LLM used is Gemma-2-9b \[ [24](https://arxiv.org/html/2604.18572v2#bib.bib24 "")\]. Alignment at fixed small kk drops with gallery size, while alignment at k=n/100k{=}n/100 remains stable across scales. The trend that stronger LLMs align better with the non-text modality ( [Fig.˜11(c)](https://arxiv.org/html/2604.18572v2#S4.F11.sf3 "In Figure 11 ‣ 4.4 Text-audio and text-video alignment ‣ 4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale")) is weak: a slight positive slope for text-video and essentially flat for text-audio.

Our findings again suggest that models independently trained on different modalities organize information differently. Across text-image, text-video, and text-audio pairs, cross-modal alignment is limited (at fine granularity), consistent with the broader picture of modality-specific organizational structure rather than convergence to a shared representation.

https://arxiv.org/html/2604.18572v2/x9.png(a)Text-video alignment.

https://arxiv.org/html/2604.18572v2/x10.png(b)Text-audio alignment.

https://arxiv.org/html/2604.18572v2/figures/1k_all_lines_perf_vs_alignment.png(c)Alignment vs. LLM performance.

Figure 11: Cross-modal alignment beyond text-image. (a, b) Mutual kkNN text-video (on PVD-100k \[ [8](https://arxiv.org/html/2604.18572v2#bib.bib8 ""), [100](https://arxiv.org/html/2604.18572v2#bib.bib100 "")\]) and text-audio alignment (on LAION-Audio-100k \[ [103](https://arxiv.org/html/2604.18572v2#bib.bib103 "")\]) scales similarly to the text-image setting. (c) Alignment vs. LLM performance at 1k: weak trend for video, flat for audio.

### 4.5 Trend check: Are the predictions from \[ [42](https://arxiv.org/html/2604.18572v2\#bib.bib42 "")\] holding up so far?

Huh et al. \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] predict that as LLMs become stronger, their representations align more with vision representations. This claim is evaluated using three proxies for language performance: HellaSwag \[ [106](https://arxiv.org/html/2604.18572v2#bib.bib106 "")\], GSM8K \[ [12](https://arxiv.org/html/2604.18572v2#bib.bib12 "")\], and (1−bitsperbyte)(1-\\text{bitsperbyte}).

In this section, we revisit this trend analysis for an extended set of models and benchmarks. We follow the original experimental setup from \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] to evaluate 55 LLMs, spanning from BLOOMZ \[ [71](https://arxiv.org/html/2604.18572v2#bib.bib71 "")\] to recently released models. We use the ARC Challenge \[ [11](https://arxiv.org/html/2604.18572v2#bib.bib11 "")\], MMLU \[ [36](https://arxiv.org/html/2604.18572v2#bib.bib36 "")\], and LogiQA2 \[ [61](https://arxiv.org/html/2604.18572v2#bib.bib61 "")\] benchmarks. These probe arithmetic reasoning, general knowledge, and logical reasoning. We present results for models that surpass Llama-3-70B \[ [29](https://arxiv.org/html/2604.18572v2#bib.bib29 "")\] (the strongest model in \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\]) on at least one benchmark, testing whether the alignment-performance trend continues. The complete results for all models and benchmarks are included in [Appendix˜D](https://arxiv.org/html/2604.18572v2#A4 "Appendix D Does the alignment vs performance trend predicted by Huh et al. [42] continue with recent LLMs? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") in the supplementary material.

https://arxiv.org/html/2604.18572v2/figures/trends/mutual_knn_k10_prh_extended_vs_PRH_gsm8k_5shots.png

https://arxiv.org/html/2604.18572v2/figures/trends/mutual_knn_k10_prh_extended_vs_PRH_arc.png

https://arxiv.org/html/2604.18572v2/figures/trends/mutual_knn_k10_prh_extended_vs_PRH_mmlu.png

https://arxiv.org/html/2604.18572v2/figures/trends/mutual_knn_k10_prh_extended_vs_PRH_logiqa2.png

Figure 12:
Testing whether the alignment-LLM performance trend from \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\], tested on WIT-1024, holds for recent LLMs on ARC, GSM8K, MMLU, and LogiQA2.
Dashed lines show the trend for models from \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] (circles). Recent LLMs (diamonds) do not follow the trend:
stronger language models do not seem to be more aligned with DINOv2.

Our observations depend on the benchmark used to measure language-model performance.
For benchmarks close to those used in \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\], such as HellaSwag and Wikitext, the trend partially extends to newer models, with positive Rnew2R^{2}\_{\\text{new}} of 0.300.30 and 0.490.49. Those benchmarks measure next-token prediction and commonsense language understanding, closely tied to the autoregressive pretraining objective. However, these benchmarks are increasingly saturated for recent LLMs. We therefore focus on broader reasoning and knowledge benchmarks, which provide a more stringent test.
On these benchmarks ( [Fig.˜12](https://arxiv.org/html/2604.18572v2#S4.F12 "In 4.5 Trend check: Are the predictions from [42] holding up so far? ‣ 4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale")), we observe that recent models do not continue the scaling lines extrapolated from the model set from \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\]. Instead, their points do not follow the predicted trend and hint at saturation with respect to DINOv2 features.
The R2R^{2} ranges from −1.41-1.41 to −0.58-0.58, confirming that the extrapolated trend is not continued by recent models.

## 5 Discussion and future work

The Platonic Representation Hypothesis suggests that models trained on different modalities converge toward a shared representation of reality as they scale. Our results indicate a more conditional interpretation of this claim. Mutual kkNN agreement is highly sensitive to the evaluation regime: it drops sharply when moving from small galleries to million-scale datasets and degrades further under many-to-many cross-modal correspondences. Moreover, the previously reported trend that stronger language models yield higher alignment does not consistently hold for recent models.

These findings do not rule out shared structure across modalities. Overall, our results indicate that small-scale mutual nearest-neighbor evaluations may overstate the degree of convergence by relying on restrictive gallery sizes and one-to-one pairing. Low mutual kkNN agreement should not be conflated with weak representations. As our analysis on ImageNet shows, it may instead reflect differences in how fine-grained structure is organized.
Rather than converging on a single Platonic representation of reality, modalities appear to inhabit their own Umwelten, a distinct but coherent representational “cave” where alignment between them is local and partial.

Future work: in search of bijection.
Prior work on the Platonic Representation Hypothesis \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] evaluates alignment under a one-to-one correspondence assumption between modalities. We have shown that mutual kkNN agreement is not reliable once this assumption is relaxed. Likewise, interpretations of the Platonic Representation Hypothesis as evidence that “language is all you need” \[ [99](https://arxiv.org/html/2604.18572v2#bib.bib99 "")\] often rely on evaluation regimes that effectively assume bijective structure between images and text.

However, real-world image–text data is fundamentally many-to-many, and the extent to which any approximate bijection exists at the level of representations remains unclear. A key direction for future work is to directly test this assumption, for example by studying whether language can serve as a lossless bottleneck for image reconstruction (i.e. an image-text-image autoencoder). If, as we suspect, this proves illusive for realistic settings (e.g. text bottlenecks of under a thousand words), it would be very interesting to identify and model the part of the joint text-image space forming a bijection (the intersection of the Venn diagram), and disentangle it from the parts that do not.

## Appendix A Is the drop in mutual kkNN alignment at scale caused by the metric, layer selection, caption quality, or by specific model choices?

In this section, we provide additional experiments to verify that the main findings in the paper are not due to a confounding variable.

### A.1 Sanity check: does mutual kkNN inherently drop at scale even within modalities?

We test whether the alignment drop with increasing gallery size ( [Fig.˜4](https://arxiv.org/html/2604.18572v2#S4.F4 "In 4.1 Alignment across dataset scales ‣ 4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale")) is merely an artifact of the mutual kkNN metric being harder at scale.

Specifically, we measure within-modality alignment for two pairs of models: two language models of different scale (OpenLlama-3b and OpenLlama-13b), and, separately, two vision models (DINOv2-base and DINOv2-giant). If mutual kkNN alignment collapses for dense galleries regardless of the models being compared, the cross-modal drop observed in the paper would be uninformative. If within-modality alignment remains stable, the cross-modal drop is meaningful.

https://arxiv.org/html/2604.18572v2/figures_supp/v6_nested_ollama3b_ollama13b_alignment.png(a)OpenLlama-3b and OpenLlama-13b

https://arxiv.org/html/2604.18572v2/figures_supp/v6_nested_base_giant_alignment.png(b)DINOv2-base and DINOv2-giant

Figure 13: Unimodal mutual kkNN alignment as a function of gallery size on WIT-1M. In contrast to cross-modal alignment ( [Fig.˜4](https://arxiv.org/html/2604.18572v2#S4.F4 "In 4.1 Alignment across dataset scales ‣ 4 How much do representations align? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale")), unimodal alignment remains significantly more stable across scales.

As shown in [Fig.˜13](https://arxiv.org/html/2604.18572v2#A1.F13 "In A.1 Sanity check: does mutual 𝑘NN inherently drop at scale even within modalities? ‣ Appendix A Is the drop in mutual 𝑘NN alignment at scale caused by the metric, layer selection, caption quality, or by specific model choices? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"), unimodal alignment remains much more stable across gallery sizes than the cross-modal alignment reported in the main paper. For the OpenLlama pair, mutual kkNN at k=1k{=}1 stays between \[0.59,0.62\]\[0.59,0.62\], and for the DINOv2 pair between \[0.35,0.45\]\[0.35,0.45\], across all gallery scales.
This confirms that mutual kkNN does not inherently collapse at scale, and that the degradation observed for cross-modal pairs reflects an actual property of the representation spaces.

We additionally verify that the alignment trend occurs at the
coarse k=n100k{=}\\frac{n}{100} level: [Fig.˜14](https://arxiv.org/html/2604.18572v2#A1.F14 "In A.1 Sanity check: does mutual 𝑘NN inherently drop at scale even within modalities? ‣ Appendix A Is the drop in mutual 𝑘NN alignment at scale caused by the metric, layer selection, caption quality, or by specific model choices? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") compares the
WIT-1024 trend at k=10k{=}10 with the WIT-1M trend at k=n100k{=}\\frac{n}{100}, and
the two largely match. This indicates that the original mutual-kkNN evidence
establishes coarse semantic-category overlap rather than fine-grained
representational convergence.

https://arxiv.org/html/2604.18572v2/figures/alignment_vs_language_1024k10_1mkpct.pngFigure 14: Alignment vs. LLM performance: the WIT-1024 trend at k=10k{=}10
compared to WIT-1M at k=n100k{=}\\frac{n}{100}. Unlike the fixed-kk case
( [Fig.˜3(b)](https://arxiv.org/html/2604.18572v2#S3.F3.sf2 "In Figure 3 ‣ 3 Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") in the main paper), the capability trend persists for
k=n/100k{=}n/100, consistent with stable coarse overlap rather
than fine-grained convergence.

### A.2 Sanity check: is the alignment drop an artifact of the layer pair selected at WIT-1024?

For our experiments, we select the best layer pair on the 1024-sample subset of WIT and reuse this pair across larger-scale evaluations. Since our central claim concerns how alignment behaves as the gallery densifies, we test whether the observed patterns persist when the layer pair is re-selected at each gallery scale.

Specifically, we re-run the layer search at each gallery size in {1024,10​K,50​K,100​K,500​K,1​M}\\{1024,10\\text{K},50\\text{K},100\\text{K},500\\text{K},1\\text{M}\\} and report the resulting mutual kkNN alignment. [Fig.˜15](https://arxiv.org/html/2604.18572v2#A1.F15 "In A.2 Sanity check: is the alignment drop an artifact of the layer pair selected at WIT-1024? ‣ Appendix A Is the drop in mutual 𝑘NN alignment at scale caused by the metric, layer selection, caption quality, or by specific model choices? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") shows the comparison: (a) re-selecting layers per scale and per kk (i.e., the optimal layer pair for k=1k{=}1, k=10k{=}10, and k=n100k{=}\\frac{n}{100} separately at each gallery size), and (b) re-selecting layers per scale at fixed k=10k{=}10 and applying the same layer pair to other kk values. Exhaustive layer-pair search inflates alignment scores by selection. We follow the null calibration proposed by Gröger et al. \[ [31](https://arxiv.org/html/2604.18572v2#bib.bib31 "")\], subtracting the expected alignment under permuted image-text pairings to correct for this bias (shown as dotted lines).

In both cases, the alignment trend with increasing gallery size is preserved. This indicates that the alignment drop for fixed small kk reported in the main paper does not suffer from an artifact of the layer pair being fixed at WIT-1024 scale.

https://arxiv.org/html/2604.18572v2/figures_supp/nested_best_self_calibrated.png(a)Per-scale layer re-selection performed independently for each kk. The alignment trends are preserved.

https://arxiv.org/html/2604.18572v2/figures_supp/nested_kpct_layers_calibrated.png(b)Per-scale layer re-selection performed at k=10k{=}10 and applied to all kk values. The same trend is observed.

Figure 15: Cross-modal mutual kkNN alignment on WIT-1M with the layer pair re-selected at each gallery scale, rather than fixed at WIT-1024. Dotted lines show calibrated scores following \[ [31](https://arxiv.org/html/2604.18572v2#bib.bib31 "")\]. The qualitative scaling trend is unchanged, indicating that the alignment drop is not driven by suboptimal layer choices.

### A.3 WIT-1M-recap: Is the alignment drop caused by poor captions?

One might hypothesize that the alignment drop at scale is driven by low quality of the WIT captions rather than by a fundamental cross-modal difference. To test this, we recaption WIT-1M using gemini-3-flash-preview as described in [Section˜E.2](https://arxiv.org/html/2604.18572v2#A5.SS2 "E.2 Captioning pipeline for the ImageNet validation set and WIT-1M-recap ‣ Appendix E Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"). The resulting WIT-1M-recap dataset contains visually detailed descriptions of around 500 words per image. As shown in [Fig.˜16](https://arxiv.org/html/2604.18572v2#A1.F16 "In A.3 WIT-1M-recap: Is the alignment drop caused by poor captions? ‣ Appendix A Is the drop in mutual 𝑘NN alignment at scale caused by the metric, layer selection, caption quality, or by specific model choices? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"), mutual kkNN alignment still drops with gallery size. More detailed captions give overall higher mutual kkNN scores, but do not prevent the decline in scores. This suggests that caption quality is not the primary driver of the mutual kkNN alignment drop.

https://arxiv.org/html/2604.18572v2/figures_supp/gemini_nested_base_ollama3b_alignment.pngFigure 16: Cross-modal mutual kkNN alignment on images recaptioned using gemini-3-flash-preview (WIT-1M-recap) as the gallery grows to 1M samples. Detailed captions result in overall higher mutual kkNN scores, but do not prevent the drop in scores.

### A.4 Mutual cross-modal kkNN alignment drops at scale across model pairs

The cross-modal alignment drop reported in Fig. 4 in the paper uses DINOv2-base and OpenLlama-3b. Here, we examine whether similar patterns hold for stronger models. In [Fig.˜17](https://arxiv.org/html/2604.18572v2#A1.F17 "In A.4 Mutual cross-modal 𝑘NN alignment drops at scale across model pairs ‣ Appendix A Is the drop in mutual 𝑘NN alignment at scale caused by the metric, layer selection, caption quality, or by specific model choices? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"), we repeat the scaling experiment for two additional model pairs: DINOv2-base with OpenLlama-13b, and DINOv2-giant with OpenLlama-13b.

Replacing DINOv2-base with the stronger DINOv2-giant and OpenLlama-3b with OpenLlama-13b does not change the pattern. We observe that mutual kkNN still drops at scale.
This is consistent with Fig. 3b in the paper, which shows low alignment scores across different LLMs at WIT-1M scale.

https://arxiv.org/html/2604.18572v2/figures_supp/v6_nested_base_ollama13b_alignment.png(a)DINOv2-base and OpenLlama-13b

https://arxiv.org/html/2604.18572v2/figures_supp/v6_nested_giant_ollama13b_alignment.png(b)DINOv2-giant and OpenLlama-13b

Figure 17: Cross-modal mutual kkNN alignment as gallery grows from WIT-1024 to WIT-1M for additional, stronger model pairs. Replacing DINOv2-base with the stronger DINOv2-giant and OpenLlama-3b (Fig. 4 in the paper) with OpenLlama-13b does not prevent the drop. This suggests that the degradation in mutual kkNN alignment was not a result of the limitation of any individual model.

https://arxiv.org/html/2604.18572v2/figures/nested_kpct_layers_dino-facebook_pixio-vitb16_llm-openlm-research_open_llama_3b.png(a)Pixio-ViT-B/16 ×\\times OpenLlama-3B

https://arxiv.org/html/2604.18572v2/figures/nested_kpct_layers_dino-vit_base_patch16_clip_224.laion2b_llm-openlm-research_open_llama_3b.png(b)CLIP-B/16 ×\\times OpenLlama-3B

Figure 18: Cross-modal mutual kkNN alignment as the WIT gallery grows from 1024 to 1M, for vision encoders trained with different objectives (Pixio-style SSL and CLIP contrastive image-text pretraining), paired with OpenLlama-3B. The same scaling pattern holds: alignment at fixed small kk drops with gallery size while k=n/100k{=}n/100 stays flat.

https://arxiv.org/html/2604.18572v2/figures/nested_kpct_layers_dino-vit_base_patch14_dinov2.lvd142m_llm-google_gemma-7b.png(a)DINOv2-B/14 ×\\times Gemma-7B

https://arxiv.org/html/2604.18572v2/figures/nested_kpct_layers_dino-vit_base_patch14_dinov2.lvd142m_llm-mistralai_Mistral-7B-v0.1.png(b)DINOv2-B/14 ×\\times Mistral-7B

Figure 19: Cross-modal mutual kkNN alignment as the WIT gallery grows from 1024 to 1M, with DINOv2-B/14 paired with LLMs from different families (Gemma and Mistral). The scaling pattern is consistent across LLM families: drop at fixed small kk, stability at k=n/100k{=}n/100.

This confirms that the degradation reported in the paper is not specific to that particular choice of models.

## Appendix B Additional ImageNet experiments

The controlled experimental setting on the ImageNet validation set in Sec. 4.2 of the paper provides one of our key findings: models individually retrieve correct-class neighbors at increasing rates as the gallery densifies, yet cross-modal agreement remains flat. Here, we verify that the ImageNet validation set serves as a suitable test bed. Furthermore, we confirm that our observations are not limited to our choice of models or metric settings.

### B.1 The ImageNet validation set is denser than WIT-1024

A natural question is how the gallery density in our ImageNet experiments compares to the WIT data. As shown in [Table˜2](https://arxiv.org/html/2604.18572v2#A2.T2 "In B.1 The ImageNet validation set is denser than WIT-1024 ‣ Appendix B Additional ImageNet experiments ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"), nearest-neighbor cosine similarities on the ImageNet validation set are substantially higher than on WIT-1024 and comparable to WIT-1M. Even for only one image per class in the gallery (ipc=1), the ImageNet validation set provides a denser retrieval setting than WIT-1024.

This confirms that the ImageNet experiments operate in a denser retrieval regime comparable to WIT-1M, making this a meaningful test bed.

Table 2: Nearest-neighbor distances across gallery sizes. ImageNet, even with only one image per class in the gallery (ipc=1), has neighbor distances comparable to WIT-1M, confirming that it operates in a similarly dense retrieval regime.

| Gallery | Model | Dim | k=1k{=}1 | k=10k{=}10 |
| --- | --- | --- | --- | --- |
| WIT-1024 | DINOv2-base | 768 | 0.799 | 0.717 |
| WIT-1024 | OpenLlama3b | 3200 | 0.502 | 0.400 |
| WIT-1M | DINOv2-base | 768 | 0.906 | 0.888 |
| WIT-1M | OpenLlama3b | 3200 | 0.757 | 0.701 |
| ImageNet ipc=1 | DINOv2-base | 768 | 0.823 | 0.763 |
| ImageNet ipc=1 | DINOv2-giant | 1536 | 0.609 | 0.496 |
| ImageNet ipc=1 | OpenLlama3b | 3200 | 0.928 | 0.904 |
| ImageNet ipc=1 | LLaMA-65B | 8192 | 0.890 | 0.858 |
| ImageNet ipc=49 | DINOv2-base | 768 | 0.887 | 0.861 |
| ImageNet ipc=49 | DINOv2-giant | 1536 | 0.749 | 0.690 |
| ImageNet ipc=49 | OpenLlama3b | 3200 | 0.954 | 0.944 |
| ImageNet ipc=49 | LLaMA-65B | 8192 | 0.926 | 0.912 |

### B.2 Stronger models do not close the gap for ImageNet

The ImageNet decomposition experiments in Sec. 4.2 in the main paper use DINOv2-base and OpenLlama-3b as its vision and language model respectively. Here, we probe whether stronger models would show better cross-modal agreement that closes the gap to unimodal retrieval accuracy.

In [Fig.˜20](https://arxiv.org/html/2604.18572v2#A2.F20 "In B.2 Stronger models do not close the gap for ImageNet ‣ Appendix B Additional ImageNet experiments ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"), we repeat the experiment with DINOv2-base paired with OpenLlama-65b, and DINOv2-giant paired with OpenLlama-65b. The pattern is unchanged: both models individually improve at retrieving correct-class neighbors as the gallery densifies, but strict cross-modal alignment remains flat. Using substantially stronger models on both sides does not close the gap between individual retrieval accuracy and cross-modal agreement.

https://arxiv.org/html/2604.18572v2/figures_supp/ipc_alignment_with_accuracy_llama65b.png(a)DINOv2-base and Llama-65b

https://arxiv.org/html/2604.18572v2/figures_supp/ipc_alignment_with_accuracy_llama65b_dino_giant.png(b)DINOv2-giant and Llama-65b

Figure 20: ImageNet per-modality retrieval accuracy and cross-modal mutual kkNN alignment (k=1k{=}1) as images / captions per class in gallery increase for different model pairs. Even with substantially stronger models (OpenLlama-65b, DINOv2-giant), individual retrieval improves with gallery density while cross-modal alignment remains flat.

### B.3 ImageNet ablation shows a similar pattern for k=10k=10

The main paper reports the ImageNet decomposition experiments with mutual kkNN scores for k=1k{=}1. Here, we verify that the finding is not an artifact of this strict setting.
We additionally present how mutual kkNN with k=10k{=}10 evolves when the gallery grows in [Fig.˜21](https://arxiv.org/html/2604.18572v2#A2.F21 "In B.3 ImageNet ablation shows a similar pattern for 𝑘=10 ‣ Appendix B Additional ImageNet experiments ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") for two different model pairs.

We again observe that individual retrieval accuracy improves with gallery density while cross-modal alignment, here in terms of mutual kkNN with k=10k{=}10, does not.

https://arxiv.org/html/2604.18572v2/figures_supp/ipc_alignment_with_accuracy_k10.png(a)DINOv2-base and OpenLlama-3b

https://arxiv.org/html/2604.18572v2/figures_supp/ipc_alignment_with_accuracy_llama65b_dino_giant_k10.png(b)DINOv2-giant and OpenLlama-65b

Figure 21: Per-modality retrieval accuracy and cross-modal mutual kkNN alignment (k=10k{=}10) as images / captions per class in gallery increase for two different model pairs. Again, modalities individually improve with gallery density, but mutual kkNN alignment, here with k=10k{=}10, does not.

## Appendix C What happens with non-synthetic data that is not bijective?

In the main paper (Sec. 4.3), we use the CycleReward dataset \[ [3](https://arxiv.org/html/2604.18572v2#bib.bib3 "")\] to test alignment when the bijective (one-to-one) assumption is relaxed with _synthetic_ multi-modal correspondences. Here, we complement this analysis using non-synthetic many-to-many correspondences from the WIT dataset \[ [87](https://arxiv.org/html/2604.18572v2#bib.bib87 "")\].

### C.1 Non-synthetic dataset with many-to-many correspondences

Natural duplicates in WIT.
The WIT dataset naturally contains many-to-many correspondences
between images and captions: the same caption can describe
many visually distinct images, and the same image is reused across Wikipedia articles with different corresponding text. Specifically, 7.1% of the captions are associated with more than one image, and 24.6% of the images have more than one caption before deduplication (see [Section˜E.1](https://arxiv.org/html/2604.18572v2#A5.SS1 "E.1 WIT-1M and LAION-15M datasets ‣ Appendix E Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale")).
These naturally occurring one-to-many and many-to-one
correspondences provide a complementary test bed for relaxing the
bijective (one-to-one) setting without relying on generated images or captions.

Table 3: Natural duplicates in the WIT dataset after within-group deduplication.

|  | T2I | I2T |
| Unique elements | 3.2 M | 2.5 M |
| Appearing >>1 time | 7.1% | 24.6% |
| Groups with ≥\\geq5 corresp. |
| Before dedup | 7,844 | 38,254 |
| After dedup | 4,975 | 24,853 |

Within-group deduplication.
Grouping by caption text (for T2I) or by image (for I2T) can include _within-group_ duplicates, i.e. a caption group may contain duplicate images, and an image group may contain repeated captions.
After within-group deduplication, the number of qualifying one-to-many samples decreases from 7,844 to 4,975 for T2I and from 38,254 to 24,853 for I2T ( [Table˜3](https://arxiv.org/html/2604.18572v2#A3.T3 "In C.1 Non-synthetic dataset with many-to-many correspondences ‣ Appendix C What happens with non-synthetic data that is not bijective? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale")).

We construct two complementary one-to-many datasets to mirror the experimental setup in Sec. 4.3 of the paper:

T2I (text-to-images): We select all 4,975 captions that are associated with at least 5 unique images. For each caption, we take 5 images, yielding a flat dataset of 24,875 image-text pairs.

I2T (image-to-texts): We identify 24,853 unique images that are paired with at least 5 distinct captions (by exact string matching). To match the T2I dataset size, we randomly subsample 4,975 images. For each image, we take 5 captions, again yielding 24,875 samples.

### C.2 Mutual kkNN also decreases on non-synthetic data when the bijective assumption is relaxed

We evaluate alignment between DINOv2-base \[ [74](https://arxiv.org/html/2604.18572v2#bib.bib74 "")\] and OpenLlama-3b \[ [26](https://arxiv.org/html/2604.18572v2#bib.bib26 "")\] on the WIT-based T2I and I2T datasets. [Fig.˜22](https://arxiv.org/html/2604.18572v2#A3.F22 "In C.2 Mutual 𝑘NN also decreases on non-synthetic data when the bijective assumption is relaxed ‣ Appendix C What happens with non-synthetic data that is not bijective? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") shows mutual kkNN alignment for k=1k{=}1 and k=10k{=}10 as the number of images per caption and vice versa increases from 1 to 5.

In both directions, alignment decreases as bijectivity is relaxed. This is consistent with the results on the CycleReward dataset in the main paper (Fig. 10) and reinforces the conclusion that mutual kkNN alignment is sensitive to the bijective assumption. When multiple valid correspondences exist for a query, the two modalities are less likely to agree on the same nearest neighbor, even if each individually retrieves a good match. This confirms that the observed drop in alignment for non-bijective setting is not an artifact of synthetic data.

https://arxiv.org/html/2604.18572v2/x11.png(a)T2I: increasing the number of unique images per caption from 1 (bijective) to 5.

https://arxiv.org/html/2604.18572v2/x12.png(b)I2T: increasing the number of unique captions per image from 1 (bijective) to 5.

Figure 22: Effect of relaxing the bijective assumption on mutual kkNN alignment using many-to-many correspondences in the WIT data (I2T and T2I subset). Mutual kkNN alignment on non-synthetic drops consistently as we increase the number of images per caption and vice versa. This confirms that the pattern observed on CycleReward is not an artifact of synthetic data.

## Appendix D Does the alignment vs performance trend predicted by Huh _et al_.\[ [42](https://arxiv.org/html/2604.18572v2\#bib.bib42 "")\] continue with recent LLMs?

To assess whether the alignment vs performance trend predicted by Huh _et al_.\[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] continues with recent language models, we evaluate 55 LLMs (see [Section˜E.3.2](https://arxiv.org/html/2604.18572v2#A5.SS3.SSS2 "E.3.2 Language models. ‣ E.3 Models and feature extraction pipeline ‣ Appendix E Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") for full list) on six standard benchmarks using the LM Evaluation Harness framework \[ [22](https://arxiv.org/html/2604.18572v2#bib.bib22 "")\]. \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] originally used three benchmarks to measure language capability: HellaSwag \[ [106](https://arxiv.org/html/2604.18572v2#bib.bib106 "")\], GSM8K \[ [12](https://arxiv.org/html/2604.18572v2#bib.bib12 "")\], and (1−bitsperbyte)(1-\\texttt{bitsperbyte}) on OpenWebText \[ [28](https://arxiv.org/html/2604.18572v2#bib.bib28 "")\]. We replace OpenWebText with Wikitext \[ [66](https://arxiv.org/html/2604.18572v2#bib.bib66 "")\] and extend this analysis to three additional benchmarks that probe different aspects of language understanding: ARC Challenge \[ [11](https://arxiv.org/html/2604.18572v2#bib.bib11 "")\], MMLU \[ [36](https://arxiv.org/html/2604.18572v2#bib.bib36 "")\], and LogiQA2 \[ [61](https://arxiv.org/html/2604.18572v2#bib.bib61 "")\].

#### D.0.1 Benchmarks and metrics.

[Table˜4](https://arxiv.org/html/2604.18572v2#A4.T4 "In D.0.1 Benchmarks and metrics. ‣ Appendix D Does the alignment vs performance trend predicted by Huh et al. [42] continue with recent LLMs? ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") summarizes the evaluation configuration for each benchmark used in Sec. 4.4 of the paper (we used the default configurations from \[ [22](https://arxiv.org/html/2604.18572v2#bib.bib22 "")\]).

Table 4: Overview of language model benchmarks used in Sec. 4.4 of the paper.

| Benchmark | Capability | Few-shot | Metric |
| --- | --- | --- | --- |
| HellaSwag \[ [106](https://arxiv.org/html/2604.18572v2#bib.bib106 "")\] | Commonsense reasoning | 0 | Accuracy |
| Wikitext \[ [66](https://arxiv.org/html/2604.18572v2#bib.bib66 "")\] | Language modeling | 0 | 1−bits per byte1-\\text{bits per byte} |
| ARC Challenge \[ [11](https://arxiv.org/html/2604.18572v2#bib.bib11 "")\] | Science QA | 4 | Accuracy |
| GSM8K \[ [12](https://arxiv.org/html/2604.18572v2#bib.bib12 "")\] | Math reasoning | 5 | Exact match |
| MMLU \[ [36](https://arxiv.org/html/2604.18572v2#bib.bib36 "")\] | General knowledge | 5 | Accuracy |
| LogiQA2 \[ [61](https://arxiv.org/html/2604.18572v2#bib.bib61 "")\] | Logical reasoning | 5 | Accuracy |

#### D.0.2 Does the alignment vs performance trend hold?

For each benchmark and each DINOv2 variant, we fit a linear regression on the base models used in \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\], predicting mutual kkNN alignment aa from benchmark performance pp. We then evaluate how well this trend describes two populations:

R2R^{2} (Huh _et al_.): The standard coefficient of determination on the data is used to fit the regression, i.e. R2​(Huh et al.)=r2R^{2}(\\text{Huh~\\emph{et al}.\\hbox{}})=r^{2}, where rr is the Pearson correlation between mutual kkNN alignment and language modelling benchmark score across the 19 base models from Huh _et al_.\[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\].

R2R^{2} (new models): We apply the line fitted on the base models to the 36 recent models and compute the generalized R2R^{2}:

|     |     |     |
| --- | --- | --- |
|  | R2​(new)=1−∑i∈ℳnew(ai−a^i)2∑i∈ℳnew(ai−a¯new)2,R^{2}(\\text{new})=1-\\frac{\\sum\_{i\\in\\mathcal{M}\_{\\text{new}}}(a\_{i}-\\hat{a}\_{i})^{2}}{\\sum\_{i\\in\\mathcal{M}\_{\\text{new}}}(a\_{i}-\\bar{a}\_{\\text{new}})^{2}}, |  |

where a^i\\hat{a}\_{i} are the linear regression alignment predictions based on language performance pip\_{i}, aia\_{i} is the alignment score for the ii-th model and a¯new\\bar{a}\_{\\text{new}} is the mean alignment of the new models. When R2​(new)>0R^{2}(\\text{new})>0, the relation between alignment and language performance predicted in Huh _et al_. extrapolates; when R2​(new)<0R^{2}(\\text{new})<0, the regression line is a worse predictor than simply predicting the average a¯new\\bar{a}\_{\\text{new}}. Ravg2R^{2}\_{\\text{avg}} values are reported in [Table˜5](https://arxiv.org/html/2604.18572v2#A4.T5 "In D.0.2 Does the alignment vs performance trend hold? ‣ Appendix D Does the alignment vs performance trend predicted by Huh et al. [42] continue with recent LLMs? ‣ Back into Plato’s Cave: Examining Cross-Modal Representational Convergence at Scale") and [Figs.˜23](https://arxiv.org/html/2604.18572v2#A4.F23 "In D.0.2 Does the alignment vs performance trend hold? ‣ Appendix D Does the alignment vs performance trend predicted by Huh et al. [42] continue with recent LLMs? ‣ Back into Plato’s Cave: Examining Cross-Modal Representational Convergence at Scale") and [24](https://arxiv.org/html/2604.18572v2#A4.F24 "Figure 24 ‣ D.0.2 Does the alignment vs performance trend hold? ‣ Appendix D Does the alignment vs performance trend predicted by Huh et al. [42] continue with recent LLMs? ‣ Back into Plato’s Cave: Examining Cross-Modal Representational Convergence at Scale").

Table 5: Average R2R^{2} of the linear regression (fitted on the 19 base models from Huh _et al_.\[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\]) evaluated on the base models themselves and on the 36 recent models, across all four DINOv2 variants. Positive Ravg2​(new)R^{2}\_{\\text{avg}}(\\text{new}) indicates that the trend from the base models is a good predictor for the new models. Negative values indicate that the regression line is a worse predictor than the mean.

| Benchmark | Ravg2R^{2}\_{\\text{avg}}(Huh _et al_.) | Ravg2R^{2}\_{\\text{avg}}(new) |
| HellaSwag | 0.752 | 0.297 |
| Wikitext | 0.729 | 0.489 |
| ARC | 0.702 | −-0.575 |
| GSM8K | 0.336 | −-1.753 |
| MMLU | 0.430 | −-0.662 |
| LogiQA2 | 0.431 | −-1.414 |

The results reveal a split across language modelling benchmarks. For HellaSwag and Wikitext, the relation between alignment and language performance observed by Huh _et al_. partially extends to recent models: the Ravg2R^{2}\_{\\text{avg}} on new models remains positive (0.297 and 0.489, respectively), indicating that stronger language models according to these benchmarks have higher mutual kkNN alignment with DINOv2. Both benchmarks primarily measure next-token prediction quality and commonsense language understanding, which are closely related to the pretraining objective of autoregressive LLMs.

In contrast, for the four benchmarks that probe more specialized reasoning abilities: ARC (science QA), GSM8K (arithmetic), MMLU (general knowledge), and LogiQA2 (logical reasoning), the relation between alignment and language performance predicted from the base models Huh _et al_. does not appear to hold for this set of recent models.

Specifically, the Ravg2R^{2}\_{\\text{avg}} on new models is consistently negative, ranging from −0.575-0.575 (ARC) to −1.753-1.753 (GSM8K). This means that the linear fit from the base models from Huh _et al_.\[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] is a worse predictor of alignment for recent models than simply predicting the mean. In [Figs.˜23](https://arxiv.org/html/2604.18572v2#A4.F23 "In D.0.2 Does the alignment vs performance trend hold? ‣ Appendix D Does the alignment vs performance trend predicted by Huh et al. [42] continue with recent LLMs? ‣ Back into Plato’s Cave: Examining Cross-Modal Representational Convergence at Scale") and [24](https://arxiv.org/html/2604.18572v2#A4.F24 "Figure 24 ‣ D.0.2 Does the alignment vs performance trend hold? ‣ Appendix D Does the alignment vs performance trend predicted by Huh et al. [42] continue with recent LLMs? ‣ Back into Plato’s Cave: Examining Cross-Modal Representational Convergence at Scale"), we observe that recent models that are stronger than the best base model (Meta-Llama-3-70B) do not show higher mutual kkNN alignment with DINOv2 features. Instead, their alignment scores seem to saturate or decrease.

We note that the 36 added (new) models are heterogeneous. They include new models trained on next-token prediction (pre-training), instruction-tuned models, and reasoning-distilled models (e.g. DeepSeek-R1-Distill). We treat them as a single population to test whether the trend extrapolates to recent LLMs.

The above results support and extend the finding from Sec. 4.4 of the main paper.
The relationship between alignment and language performance from \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] holds for core language modelling benchmarks, but does not seem to generalize to reasoning benchmarks.

https://arxiv.org/html/2604.18572v2/x13.png

https://arxiv.org/html/2604.18572v2/x14.png

https://arxiv.org/html/2604.18572v2/x15.png

Figure 23: Mutual kkNN alignment vs. language benchmark performance for 55 LLMs across four DINOv2 variants, on WikiText, HellaSwag, and GSM8K. Dashed lines show the linear trend fit to the 19 base models from \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\]. For WikiText and HellaSwag (top two plots), recent models roughly follow the trend. For GSM8K (bottom plot), the trend is not followed.

https://arxiv.org/html/2604.18572v2/x16.png

https://arxiv.org/html/2604.18572v2/x17.png

https://arxiv.org/html/2604.18572v2/x18.png

Figure 24: Mutual kkNN alignment vs. language benchmark performance for 55 LLMs across four DINOv2 variants, on ARC, LogiQA2, and MMLU. As with GSM8K, the alignment-performance trend from \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\] does not extrapolate to recent models on any of these reasoning benchmarks. Stronger models do not appear to show higher mutual kkNN alignment with DINOv2 features.

## Appendix E Experimental setup

In [Section˜E.1](https://arxiv.org/html/2604.18572v2#A5.SS1 "E.1 WIT-1M and LAION-15M datasets ‣ Appendix E Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"), we provide additional details about the deduplication pipeline for the WIT-1M and LAION-15M datasets. We then describe the captioning pipeline used for WIT-1M-recap and for the ImageNet validation set in [Section˜E.2](https://arxiv.org/html/2604.18572v2#A5.SS2 "E.2 Captioning pipeline for the ImageNet validation set and WIT-1M-recap ‣ Appendix E Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale").

### E.1 WIT-1M and LAION-15M datasets

#### E.1.1 Image deduplication.

We deduplicate the gallery pools from WIT \[ [87](https://arxiv.org/html/2604.18572v2#bib.bib87 "")\] and LAION400M \[ [83](https://arxiv.org/html/2604.18572v2#bib.bib83 "")\] at the image level using perceptual hashing \[ [105](https://arxiv.org/html/2604.18572v2#bib.bib105 "")\]. For each image, a 64-bit hash 𝐡i∈{0,1}64\\mathbf{h}\_{i}\\in\\{0,1\\}^{64} is computed. For this, we first convert the image to grayscale, resize it to 32×3232\\times 32, apply a 2D Discrete Cosine Transform, and threshold the top-left 8×88\\times 8 low-frequency coefficients against their median. This produces a binary fingerprint that is robust to minor changes, e.g. due to recompression. We consider images ii and jj duplicates if their Hamming distance satisfies

|     |     |     |
| --- | --- | --- |
|  | d​H​(𝐡i,𝐡j)≤2,d{\\text{H}}(\\mathbf{h}\_{i},\\mathbf{h}\_{j})\\leq 2, |  |

measuring the number of bit positions at which two hashes differ:

|     |     |     |
| --- | --- | --- |
|  | dH​(𝐡i,𝐡j)=∑b=164𝟏​\[hi,b≠hj,b\].d\_{\\text{H}}(\\mathbf{h}\_{i},\\mathbf{h}\_{j})=\\sum\_{b=1}^{64}\\mathbf{1}\[h\_{i,b}\\neq h\_{j,b}\]. |  |

We perform deduplication of the gallery against the WIT-1024 images, and within the gallery by keeping the first occurrence in the case of image duplicates.

#### E.1.2 Caption deduplication.

In addition to image deduplication, we do a text deduplication pass to remove gallery samples with captions identical to another gallery sample or to a WIT-1024 query caption. Duplicate captions are undesirable because they allow trivial text-based query-gallery matching, inflating retrieval scores regardless of visual representations.

We use exact string matching and remove any gallery samples that match WIT-1024 captions. Among the gallery samples, we discard duplicates and keep only the first occurrence of a duplicate caption-sample.

Table 6: Deduplication statistics for the WIT-1M and LAION-15M gallery pools.
Image duplicates are detected via perceptual hashing (pHash) with Hamming distance ≤2\\leq 2.
Caption duplicates are detected by exact string matching. WIT-1M and LAION-15M are 1M and 15M image-caption pairs randomly sampled from the remaining final pool.

|  | WIT-1M | LAION-15M |
| Raw pool | 3,582,610 | 20,000,000 |
| Image deduplication |
| Duplicates (with WIT-1024) | 2,847 | 53 |
| Duplicates (within gallery) | 2,164,343 | 3,371,128 |
| Pool after image deduplication | 2,486,852 | 17,941,016 |
| Caption deduplication |
| Duplicates (with WIT-1024) | 52 | 14 |
| Duplicates (within gallery) | 97,654 | 642,895 |
| Final pool size | 2,389,146 | 17,298,107 |

Table 7: Distribution of caption duplicates in the WIT and LAION galleries after image deduplication. Note that the “unique captions” include some captions that are removed as query matches for the final pool.

|  | WIT | LAION |
| Copies per caption | Unique captions | Total samples | Unique captions | Total samples |
| 1 | 2,357,353 | 2,357,353 | 16,897,221 | 16,897,221 |
| 2 | 22,799 | 45,598 | 316,109 | 632,218 |
| 3 | 3,807 | 11,421 | 48,864 | 146,592 |
| 4 | 1,529 | 6,116 | 15,422 | 61,688 |
| 5 | 787 | 3,935 | 6,932 | 34,660 |
| 6–10 | 1,520 | 11,431 | 9,596 | 69,614 |
| 11–100 | 1,283 | 29,765 | 3,838 | 76,200 |
| 101–1,000 | 118 | 27,164 | 103 | 12,376 |
| >>1,000 | 2 | 5,077 | 4 | 14,588 |
| Total | 2,389,198 | 2,486,852 | 17,298,111 | 17,941,016 |

#### E.1.3 WIT-1M.

We obtain a raw pool of 3,582,610 samples from the English-text WIT dataset \[ [87](https://arxiv.org/html/2604.18572v2#bib.bib87 "")\]. To construct the English-only subset of the dataset, we used a subset of \[ [85](https://arxiv.org/html/2604.18572v2#bib.bib85 ""), [84](https://arxiv.org/html/2604.18572v2#bib.bib84 "")\].
Since \[ [84](https://arxiv.org/html/2604.18572v2#bib.bib84 "")\] only contains the image URLs, we retrieved the corresponding images from \[ [87](https://arxiv.org/html/2604.18572v2#bib.bib87 "")\].
The raw pool undergoes our deduplication pipeline, resulting in 2,389,146 samples. We randomly sampled 1 million samples for the WIT-1M dataset. Deduplication statistics are provided in [Table˜6](https://arxiv.org/html/2604.18572v2#A5.T6 "In E.1.2 Caption deduplication. ‣ E.1 WIT-1M and LAION-15M datasets ‣ Appendix E Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") and [Table˜7](https://arxiv.org/html/2604.18572v2#A5.T7 "In E.1.2 Caption deduplication. ‣ E.1 WIT-1M and LAION-15M datasets ‣ Appendix E Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"). In WIT, 31,845 captions appear repeatedly,
accounting for 129,499 samples (5.21%);
the most frequent captions are coat of arms (2716×\\times)
and Town hall (2361×\\times).

#### E.1.4 LAION-15M.

We randomly sample 20M samples from the LAION-400M dataset \[ [83](https://arxiv.org/html/2604.18572v2#bib.bib83 "")\] which consists of English image-text pairs. We randomly sample 20M samples as our raw pool which undergoes our deduplication pipeline. Finally, we randomly sample 15M from the final pool after deduplication, resulting in our LAION-15M data pool. Deduplication statistics are provided in [Table˜6](https://arxiv.org/html/2604.18572v2#A5.T6 "In E.1.2 Caption deduplication. ‣ E.1 WIT-1M and LAION-15M datasets ‣ Appendix E Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale") and [Table˜7](https://arxiv.org/html/2604.18572v2#A5.T7 "In E.1.2 Caption deduplication. ‣ E.1 WIT-1M and LAION-15M datasets ‣ Appendix E Experimental setup ‣ Back into Plato’s Cave: Examining Cross-Modal Representational Convergence at Scale"). In LAION, 400,890 unique captions appear repeatedly, accounting for 1,043,795 samples (5.82%);
the most frequent captions are Patent Drawing (10027×\\times)
and Throw Pillow (3246×\\times).

### E.2 Captioning pipeline for the ImageNet validation set and WIT-1M-recap

We used gemini-3-flash-preview \[ [91](https://arxiv.org/html/2604.18572v2#bib.bib91 ""), [75](https://arxiv.org/html/2604.18572v2#bib.bib75 "")\] for captioning the images in the ImageNet validation \[ [16](https://arxiv.org/html/2604.18572v2#bib.bib16 "")\] set and in WIT-1M. Specifically, we used the following text prompt for each image.

[⬇](data:text/plain;base64,WW91IGFyZSBhIHByZWNpc2UgaW1hZ2UgZGVzY3JpcHRpb24gc3lzdGVtLiBEZXNjcmliZSB0aGUgaW1hZ2UgaW4gdGhlIGZvbGxvd2luZyBKU09OIGZvcm1hdC4KUmV0dXJuIE9OTFkgYSB2YWxpZCBKU09OIG9iamVjdCB3aXRoIGV4YWN0bHkgdGhlc2UgNyBrZXlzLiBObyB0ZXh0IGJlZm9yZSBvciBhZnRlciB0aGUgSlNPTi4KewogICJvbmVfc2VudGVuY2UiOiAiPGV4YWN0bHkgb25lIHNlbnRlbmNlLCBzdHJpY3RseSBmZXdlciB0aGFuIDE1IHdvcmRzPiIsCiAgInNob3J0IjogICAgICAgICI8Mi0zIHNlbnRlbmNlcywgMjAtNDAgd29yZHMgdG90YWw+IiwKICAiMTAwdyI6ICAgICAgICAgIjxhIHBhcmFncmFwaCwgYXBwcm94aW1hdGVseSAxMDAgd29yZHM+IiwKICAiMjUwdyI6ICAgICAgICAgIjxzZXZlcmFsIHBhcmFncmFwaHMsIGFwcHJveGltYXRlbHkgMjUwIHdvcmRzPiIsCiAgIjUwMHciOiAgICAgICAgICI8ZGV0YWlsZWQgZGVzY3JpcHRpb24sIGFwcHJveGltYXRlbHkgNTAwIHdvcmRzPiIsCiAgIjc1MHciOiAgICAgICAgICI8dGhvcm91Z2ggZGVzY3JpcHRpb24gY292ZXJpbmcgYWxsIHZpc3VhbCBkZXRhaWxzLCBhcHByb3hpbWF0ZWx5IDc1MCB3b3Jkcz4iLAogICJleHRyZW1lX2xvbmciOiAiPG1heGltYWxseSBkZXRhaWxlZCBkZXNjcmlwdGlvbiBjb3ZlcmluZyBldmVyeSB2aXNpYmxlIGVsZW1lbnQsIHRleHR1cmUsIGNvbG9yLCBzcGF0aWFsIHJlbGF0aW9uc2hpcCwgbGlnaHRpbmcsIGFuZCBjb250ZXh0LiBZT1UgTVVTVCBXUklURSBBVCBMRUFTVCAxMDAwIFdPUkRTLiBJZiB5b3VyIGRyYWZ0IGlzIHVuZGVyIDEwMDAgd29yZHMsIGtlZXAgYWRkaW5nIG1vcmUgZGV0YWlsIGFib3V0IHRleHR1cmVzLCBtYXRlcmlhbHMsIGxpZ2h0aW5nLCBzcGF0aWFsIGxheW91dCwgY29sb3JzLCBhbmQgYW55IG90aGVyIHZpc2libGUgZWxlbWVudHMgdW50aWwgeXJldSBvYWNoIGF0IGxlYXN0IDEwMDAgd29yZHMuCiAgVGFyZ2V0IDEwMDAtMTUwMCB3b3Jkcy4+Igp9CkJlIGZhY3R1YWwgYW5kIHZpc3VhbC4gRGVzY3JpYmUgd2hhdCB5b3UgYWN0dWFsbHkgc2VlOiBvYmplY3RzLCBwZW9wbGUsIGFuaW1hbHMsIGNvbG9ycywgdGV4dHVyZXMsIHNwYXRpYWwgcmVsYXRpb25zaGlwcywgYmFja2dyb3VuZCwgbGlnaHRpbmcsIGFuZCBtb29kLiBEbyBub3QgaW52ZW50IGluZm9ybWF0aW9uIG5vdCB2aXNpYmxlIGluIHRoZSBpbWFnZS4=)

Youareapreciseimagedescriptionsystem.DescribetheimageinthefollowingJSONformat.

ReturnONLYavalidJSONobjectwithexactlythese7keys.NotextbeforeoraftertheJSON.

{

"one\_sentence":"<exactlyonesentence,strictlyfewerthan15words>",

"short":"<2-3sentences,20-40wordstotal>",

"100w":"<aparagraph,approximately100words>",

"250w":"<severalparagraphs,approximately250words>",

"500w":"<detaileddescription,approximately500words>",

"750w":"<thoroughdescriptioncoveringallvisualdetails,approximately750words>",

"extreme\_long":"<maximallydetaileddescriptioncoveringeveryvisibleelement,texture,color,spatialrelationship,lighting,andcontext.YOUMUSTWRITEATLEAST1000WORDS.Ifyourdraftisunder1000words,keepaddingmoredetailabouttextures,materials,lighting,spatiallayout,colors,andanyothervisibleelementsuntilyoureachatleast1000words.

Target1000-1500words.>"

}

Befactualandvisual.Describewhatyouactuallysee:objects,people,animals,colors,textures,spatialrelationships,background,lighting,andmood.Donotinventinformationnotvisibleintheimage.

For the ImageNet validation set, we perform experiments with captions of the extreme\_long type. As shown in [Fig.˜25(a)](https://arxiv.org/html/2604.18572v2#A5.F25.sf1 "In Figure 25 ‣ E.2 Captioning pipeline for the ImageNet validation set and WIT-1M-recap ‣ Appendix E Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"), alignment scores increase with caption length. Captions of approximately 500 words achieve scores close to the maximum, while the longest captions yield the best mutual
kkNN alignment scores between DINOv2-base and OpenLlama-3b on the ImageNet validation set.
A distribution over the number of words for captions of the extreme\_long caption type is shown in [Fig.˜25(b)](https://arxiv.org/html/2604.18572v2#A5.F25.sf2 "In Figure 25 ‣ E.2 Captioning pipeline for the ImageNet validation set and WIT-1M-recap ‣ Appendix E Experimental setup ‣ Back into Plato’s Cave: Examining Cross-modal Representational Convergence at Scale"). Despite prompting the model to produce at least 1,000 words per caption, 63.1% of captions fall below this target. The average caption length is 981 words.

For WIT-1M-recap, we caption the 1 million images in the WIT-1M dataset using the 500w variant for computational efficiency. This resulted in captions for 999,971 (29 images did not get processed by gemini-3-flash-preview) images of on average 478 words. We provide those in [https://huggingface.co/datasets/askoepke/wit\_1m\_recaptioned](https://huggingface.co/datasets/askoepke/wit_1m_recaptioned "").

https://arxiv.org/html/2604.18572v2/figures_supp/v2_caption_levels_searchIPC1.png(a)Mutual kkNN alignment for DINOv2-base and OpenLlama-3b increases with longer captions on the ImageNet validation set.

https://arxiv.org/html/2604.18572v2/figures_supp/extreme_long_histogram_imagenet.png(b)Distribution of word counts for Gemini-generated extreme\_long captions across 49,984 ImageNet validation images.

Figure 25: Generated image captions for the ImageNet validation set. a) shows the mutual kkNN alignment using captions of different lengths between DINOv2-base and OpenLlama3b on the ImageNet validation set. As also shown in \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\], longer detailed captions yield higher alignment scores. b) shows the distribution over caption length (word count). We use captions of on average 981 words for our ImageNet experiments.

### E.3 Models and feature extraction pipeline

Our feature extraction pipeline is based on the experimental protocol from Huh _et al_.\[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\], which we extend to include additional LLMs.

#### E.3.1 Vision models.

On the vision side, we use four DINOv2 \[ [74](https://arxiv.org/html/2604.18572v2#bib.bib74 "")\] variants: ViT-S/14 (384-d), ViT-B/14 (768-d), ViT-L/14 (1024-d), and ViT-G/14 (1536-d) \[ [18](https://arxiv.org/html/2604.18572v2#bib.bib18 "")\], loaded via the timm\[ [101](https://arxiv.org/html/2604.18572v2#bib.bib101 "")\] library. For each image, we extract the CLS token representation from every transformer layer, yielding a per-sample feature tensor of shape L×dL\\times d, where LL is the number of layers and dd the feature dimensionality.

#### E.3.2 Language models.

We evaluate 55 large language models spanning 13 model families. The first group comprises the 19 base models used by Huh _et al_.\[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\]: BLOOMZ (560M–7.1B) \[ [71](https://arxiv.org/html/2604.18572v2#bib.bib71 "")\], OpenLlama (3B–13B) \[ [26](https://arxiv.org/html/2604.18572v2#bib.bib26 "")\], LLaMA (7B–65B) \[ [93](https://arxiv.org/html/2604.18572v2#bib.bib93 "")\], OLMo (1B, 7B) \[ [30](https://arxiv.org/html/2604.18572v2#bib.bib30 "")\], Gemma (2B, 7B) \[ [23](https://arxiv.org/html/2604.18572v2#bib.bib23 "")\], Mistral-7B \[ [45](https://arxiv.org/html/2604.18572v2#bib.bib45 "")\], Mixtral-8×\\times7B \[ [46](https://arxiv.org/html/2604.18572v2#bib.bib46 "")\], and Meta-Llama-3-70B \[ [29](https://arxiv.org/html/2604.18572v2#bib.bib29 "")\].

For the trend analysis in [Appendix˜D](https://arxiv.org/html/2604.18572v2#A4 "Appendix D Does the alignment vs performance trend predicted by Huh et al. [42] continue with recent LLMs? ‣ Back into Plato’s Cave: Examining Cross-Modal Representational Convergence at Scale"), we extend this set with 36 recent models: LLaMA-2 (7B–70B) \[ [94](https://arxiv.org/html/2604.18572v2#bib.bib94 "")\], Llama-3/3.1 \[ [29](https://arxiv.org/html/2604.18572v2#bib.bib29 "")\], OLMo-2/3  \[ [72](https://arxiv.org/html/2604.18572v2#bib.bib72 "")\], Ministral-3 (3B–14B) \[ [59](https://arxiv.org/html/2604.18572v2#bib.bib59 "")\], Gemma-2 (2B–27B)\[ [24](https://arxiv.org/html/2604.18572v2#bib.bib24 "")\], Gemma-3 (270M–27B) \[ [25](https://arxiv.org/html/2604.18572v2#bib.bib25 "")\], DeepSeek-R1-Distill (1.5B–70B) \[ [15](https://arxiv.org/html/2604.18572v2#bib.bib15 "")\], Qwen3 (1.7B–32B) \[ [77](https://arxiv.org/html/2604.18572v2#bib.bib77 "")\], Falcon3 (7B, 10B) \[ [90](https://arxiv.org/html/2604.18572v2#bib.bib90 "")\], 01.AI Yi-1.5 (34B) \[ [104](https://arxiv.org/html/2604.18572v2#bib.bib104 "")\], IBM Granite (8b)  \[ [79](https://arxiv.org/html/2604.18572v2#bib.bib79 "")\], and OpenAI GPT-OSS (20b) \[ [73](https://arxiv.org/html/2604.18572v2#bib.bib73 "")\].

For each model, we extract hidden-state representations from all layers. Following \[ [42](https://arxiv.org/html/2604.18572v2#bib.bib42 "")\], we apply average pooling over non-padding tokens to obtain a single vector per layer.

## Appendix F Additional qualitative results

We present additional qualitative results for nearest-neighbor retrieval at different gallery scales on WIT-1M and LAION-15M in [Figs.˜26](https://arxiv.org/html/2604.18572v2#A6.F26 "In Appendix F Additional qualitative results ‣ Back into Plato’s Cave: Examining Cross-Modal Representational Convergence at Scale") and [27](https://arxiv.org/html/2604.18572v2#A6.F27 "Figure 27 ‣ Appendix F Additional qualitative results ‣ Back into Plato’s Cave: Examining Cross-Modal Representational Convergence at Scale") and [Figs.˜28](https://arxiv.org/html/2604.18572v2#A6.F28 "In Appendix F Additional qualitative results ‣ Back into Plato’s Cave: Examining Cross-Modal Representational Convergence at Scale") and [29](https://arxiv.org/html/2604.18572v2#A6.F29 "Figure 29 ‣ Appendix F Additional qualitative results ‣ Back into Plato’s Cave: Examining Cross-Modal Representational Convergence at Scale") respectively. In addition to the near-duplicate matches in Figs. 5 and 6 of the main paper, we here show further examples for cross-modal agreement (green-bordered matches) at scale when the modalities happen to select the same neighbor. Others show agreement at WIT-1024 that breaks down as the gallery densifies. In those cases, each modality individually finds a better match at scale, but they no longer agree on the same one.

https://arxiv.org/html/2604.18572v2/x19.pngFigure 26: Additional nearest-neighbor examples with DINOv2 and OpenLlama-3b for k=1k{=}1 across gallery scales on the WIT-1M dataset. For OpenLlama-3b, we show the (partial) retrieved captions along with the corresponding reference image (LLM-ref) for visualisation. Green-bordered captions and images indicate a mutual kkNN match across modalities.https://arxiv.org/html/2604.18572v2/x20.pngFigure 27: Additional nearest-neighbor examples with DINOv2 and OpenLlama-3b for k=1k{=}1 across gallery scales on the WIT-1M dataset. Green-bordered captions and images indicate a mutual kkNN match across modalities.https://arxiv.org/html/2604.18572v2/x21.pngFigure 28: Additional nearest-neighbor examples with DINOv2 and OpenLlama-3b for k=1k{=}1 across gallery scales on the LAION-15M dataset. Green-bordered captions and images indicate a mutual kkNN match across modalities.https://arxiv.org/html/2604.18572v2/x22.pngFigure 29: Additional nearest-neighbor examples with DINOv2 and OpenLlama-3b for k=1k{=}1 across gallery scales on the LAION-15M dataset. Green-bordered captions and images indicate a mutual kkNN match across modalities.

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

<research_source type="scraped_from_research" phase="exploration" file="the-platonic-representation-hypothesis.md">
<details>
<summary>How to measure if representations are converging?</summary>

Phase: [EXPLORATION]

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