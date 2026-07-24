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

<research_source type="scraped_from_research" phase="exploitation" file="A Toolbox for Representational Similarity Analysis.md">
<details>
<summary>A Toolbox for Representational Similarity Analysis</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://kriegeskortelab.zuckermaninstitute.columbia.edu/sites/default/files/content/NiliKriegeskorte_2014_PLoSComputBiol.pdf>

# A Toolbox for Representational Similarity Analysis

Hamed Nili<sup>1</sup> \*, Cai Wingfield2 , Alexander Walther<sup>1</sup> , Li Su1,3, William Marslen-Wilson3 , Nikolaus Kriegeskorte<sup>1</sup> \*

1 MRC Cognition and Brain Sciences Unit, Cambridge, United Kingdom, 2Department of Computer Science, University of Bath, Bath, United Kingdom, 3 Department of Experimental Psychology, University of Cambridge, Cambridge, United Kingdom

## Abstract

Neuronal population codes are increasingly being investigated with multivariate pattern-information analyses. A key challenge is to use measured brain-activity patterns to test computational models of brain information processing. One approach to this problem is representational similarity analysis (RSA), which characterizes a representation in a brain or computational model by the distance matrix of the response patterns elicited by a set of stimuli. The representational distance matrix encapsulates what distinctions between stimuli are emphasized and what distinctions are de-emphasized in the representation. A model is tested by comparing the representational distance matrix it predicts to that of a measured brain region. RSA also enables us to compare representations between stages of processing within a given brain or model, between brain and behavioral data, and between individuals and species. Here, we introduce a Matlab toolbox for RSA. The toolbox supports an analysis approach that is simultaneously data- and hypothesis-driven. It is designed to help integrate a wide range of computational models into the analysis of multichannel brain-activity measurements as provided by modern functional imaging and neuronal recording techniques. Tools for visualization and inference enable the user to relate sets of models to sets of brain regions and to statistically test and compare the models using nonparametric inference methods. The toolbox supports searchlight-based RSA, to continuously map a measured brain volume in search of a neuronal population code with a specific geometry. Finally, we introduce the linear-discriminant t value as a measure of representational discriminability that bridges the gap between linear decoding analyses and RSA. In order to demonstrate the capabilities of the toolbox, we apply it to both simulated and real fMRI data. The key functions are equally applicable to other modalities of brain-activity measurement. The toolbox is freely available to the community under an open-source license agreement ([http://www.mrc-cbu.cam.ac.uk/methods-and-resources/toolboxes/license/\)](http://www.mrc-cbu.cam.ac.uk/methods-and-resources/toolboxes/license/).

Citation: Nili H, Wingfield C, Walther A, Su L, Marslen-Wilson W, et al. (2014) A Toolbox for Representational Similarity Analysis. PLoS Comput Biol 10(4): e1003553. doi:10.1371/journal.pcbi.1003553

Editor: Andreas Prlic, UCSD, United States of America

Received January 7, 2013; Accepted January 24, 2014; Published April 17, 2014

Copyright: - 2014 Nili et al. This is an open-access article distributed under the terms of the [Creative Commons Attribution License,](http://creativecommons.org/licenses/by/4.0/) which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Funding: This work was funded by the Medical Research Council of the UK (programme MC-A060-5PR20) and by a European Research Council Starting Grant (ERC-2010-StG 261352) to NK. Additional funding was provided by European Research Council Advanced Grant (230570-NEUROLEX) to WMW. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

Competing Interests: The authors have declared that no competing interests exist.

\* E-mail: hamed.nili@mrc-cbu.cam.ac.uk (HN); nikolaus.kriegeskorte@mrc-cbu.cam.ac.uk (NK)

This is a PLOS Computational Biology Software Article

### Introduction

Brain science is constantly developing its techniques of brainactivity measurement. Neuronal recordings have always offered superior spatial and temporal resolution, and are improving in terms of the numbers of channels that can be recorded simultaneously in animal models. Functional magnetic resonance imaging (fMRI) has always had superior coverage and very large numbers of channels, enabling us to noninvasively measure the entire human brain simultaneously with tens to hundreds of thousands of voxels, and it has begun to invade the submillimeter range in humans. In the near future, it might be possible to image the activity of every cell within a functional area with millisecond temporal resolution [1].

A fundamental challenge is to use these rich spatiotemporal measurements to learn about brain information processing. Linear decoding analyses have helped reveal what information is present for linear readout in each region [2–11]. Beyond linear decoding, we would like to characterize neuronal population codes more comprehensively, including not only what information is present, but also the format, in which the information is represented. In addition, we would like to use activity measurements to test computational models of brain information processing [12]. One approach to these challenges is representational similarity analysis (RSA [13]; for a review of recent studies, see [14]).

In contrast to decoding analysis, which detects information about predefined stimulus categories in response patterns, RSA tests hypotheses about the representational geometry, which is characterized by the representational dissimilarities among the stimuli. RSA can relate brain activity patterns to continuous and categorical multivariate stimulus descriptions. When the stimulus description is the internal representation in a computational model, RSA can be used to test the model. RSA can also relate brain representations to behavioral data, such as similarity judgments e.g. [13,15–16].

Although RSA has been successfully applied in many studies (e.g. [17–23] and many more reviewed in [14]), there has not been any freely available set of analysis tools implementing this method. An easy-to-use toolbox for RSA promises to help newcomers get started and could also provide a basis for collaborative development of further methodological advances across labs. Here we describe a freely available toolbox developed in Matlab. The toolbox provides a core set of functions for performing the dataand hypothesis-driven analyses of RSA. It includes a number of demo scripts that demonstrate key analyses based on simulated and real brain-activity data. These scripts come ready to run and provide an easy start for learning how to combine components to perform the desired analyses in Matlab. They may also serve as prototypes for a user's own analyses. The toolbox does not currently provide a graphical user interface; knowledge of Matlab is required. The outputs of the analyses are visualizations of brain representations and results of inferential analyses that test and compare alternative theoretical models. The toolbox supports a range or nonparametric frequentist inference techniques (signedrank, randomization, and bootstrap tests), which are applicable to single subjects as well as groups of subjects, and can treat subjects and/or stimuli as random effects.

We start with a brief description of the basic principles of the method and in particular the notion of a representational dissimilarity matrix (RDM), the core concept of RSA (Figure 1). We then proceed with a description of RSA in three steps. The steps are illustrated by applying the toolbox to simulated data (Figures 2–4). We then apply the key inferential analyses to real fMRI data (previously analyzed in [19]). This provides an example of how new biological insights can be gained from the technique by using the toolbox.

### Basics of representational similarity analysis

In studies of brain activity, subjects typically experience a number of experimental conditions while some correlate of neuronal activity is measured at multiple brain locations. In perceptual studies, the experimental conditions typically correspond to distinct stimuli. We will use the more specific term ''stimulus'' here for simplicity, with an understanding that the methods apply to non-perceptual (e.g. imagery or motor) experiments as well. The vector of activity amplitudes across response channels (i.e. voxels in fMRI, neurons or sites in cell recording) within a region of interest (ROI) is referred to as the activity pattern. Each stimulus is associated with an activity pattern, which is interpreted as the representation of the stimulus (or of the mental state associated with the experimental condition) within the ROI. Typically, the activity pattern is a spatial pattern. However, it may also be a spatiotemporal pattern [24–25].

RSA characterizes the representation in each brain region by a representational dissimilarity matrix (RDM, Figure 1). The most basic type of RDM is a square symmetric matrix, indexed by the stimuli horizontally and vertically (in the same order). The diagonal entries reflect comparisons between identical stimuli and are 0, by definition, in this type of RDM. Each off-diagonal value indicates the dissimilarity between the activity patterns associated with two different stimuli. The dissimilarities can be interpreted as distances in the multivariate response space. The RDM thus describes the geometry of the arrangement of patterns in this space. Popular distance measures are the correlation distance (1 minus the Pearson correlation, computed across voxels or sites of the two activity patterns), the Euclidean distance (the square root of the sum of squared differences between the two patterns), and the Mahalanobis distance (which is the Euclidean distance measured after linearly recoding the space so as to whiten the noise). The goal of RSA is to understand the representational geometry of a brain region. This is achieved by visualizing the representational distances in 2D and by statistically comparing the brain region's RDM to various model RDMs.

RDMs can be derived from a variety of sources beyond brainactivity patterns. For example, one can define an RDM on the basis of behavioral measures that capture the discriminability of different objects, such as judgments of dissimilarity, frequencies of confusions, or reaction times in a discrimination task. Hypotheses about the representations in a given brain region might also make

![](_page_1_Figure_8.jpeg)

Figure 1. Computation of the representational dissimilarity matrix (RDM). During the experiment, each subject's brain activity is measured while the subject is exposed to N experimental conditions, such as the presentation of sensory stimuli. For each brain region of interest, an activity pattern is estimated for each experimental condition. For each pair of activity patterns, a dissimilarity is computed and entered into a matrix of representational dissimilarities. When a single set of response-pattern estimates is used, the RDM is symmetric about a diagonal of zeros. The dissimilarities between the activity patterns can be thought of as distances between points in the multivariate response space. An RDM describes the geometry of the representation and serves as a signature that can be compared between brains and models, between different brain regions, and between individuals and species. doi:10.1371/journal.pcbi.1003553.g001

![](_page_2_Figure_1.jpeg)

Figure 2. Visualizing representations as RDMs, 2D arrangements, and clustering dendrograms. Percentiled RDMs are displayed in the top row. The left RDM corresponds to the simulated ground truth (dissimilarities measured before adding noise). The middle RDM is an example of a simulated single-subject RDM (dissimilarities measured after adding isotropic Gaussian noise to the ground-truth patterns). The group-average RDM (right) is computed by averaging the RDMs for all 12 simulated subjects, which reduces the noise. Visual inspection reveals the simulated structure designed here to be similar to the human-IT RDM from Kriegeskorte et al. [19], with two main clusters corresponding to animate and inanimate objects and a cluster corresponding to human and animal faces. Two-dimensional arrangements (middle row, computed by MDS with metric stress criterion) provide a spatial visualization of the approximate geometry, without assuming any categorical structure. The third row displays the results of hierarchical agglomerative clustering to the three RDMs. Clustering starts with the assumption that there is some categorical structure and aims to reveal the categorical divisions. MDS plots and dendrograms share the same category color code (see color legend). doi:10.1371/journal.pcbi.1003553.g002

specific predictions about their similarity structure. We may, for example, hypothesize that several stimuli should be represented as similar to each other because they share a semantic feature. This prediction can be expressed in an RDM. One may also obtain RDMs from computational models. For example, an RDM may be derived from the representation in a hidden layer of units in a neural network model. We refer to RDMs derived from either conceptual or computational models, or from behavioral data, as model RDMs.

### Design and implementation

The toolbox implements RSA in a stepwise manner. Its components can be used for analyzing dissimilarity matrices derived from any source. The input to the toolbox is the set of activity patterns corresponding to the experimental conditions for each ROI in each subject. In the first step, the brain-activity-based RDMs are computed and visualized. Descriptive visualizations give an intuitive sense of the representational geometry, revealing which pairs of stimuli are represented distinctly and which are represented similarly. In the second step, different RDMs are compared and the relationships among RDMs are visualized. This serves to reveal the extent to which the representational geometries in brain regions and models are similar to each other. These first two steps are descriptive and the visualizations will reflect both signals and noise, precluding any definite inferences. The third step is statistical inference on (a) the ability of each model RDM to account for each brain representation, and (b) the differences among models in their ability to account for each brain representation.

In order to demonstrate the three steps of analysis, we apply the toolbox to both simulated and real brain-activity data. Simulations enable us to define arbitrary hypothetical representational geometries. In a simulation, we know the ''ground truth'', i.e. the noiseless true patterns underlying the noisy measurements that form the input to the analyses. This enables us to test how well our methods, despite the noise, can reveal the true representational geometry underlying the data.

The simulated data recreate an RDM similar to the one observed for human IT for a set of 92 images [19]. This RDM is characterized by two major clusters, corresponding to animate and inanimate objects (roughly the first and the second half of the set of 92 stimuli, respectively). Within the animates, there is a subcluster corresponding to faces. This cluster includes human and animal faces and appears as two small blue squares along the diagonal (corresponding to comparisons within human and within animal faces) and two small blue off-diagonal squares (corresponding to comparisons between human and animal faces). We first created a hypothetical ground-truth RDM (Figure 2, top left) by linearly combining the noisy estimate of the human-IT RDM from [19] with a categorical-model RDM. We then created a set of 92

![](_page_3_Figure_1.jpeg)

Figure 3. Visualizing the relationships among multiple representations. (A) Matrix of RDM correlations. Each entry compares two RDMs by Kendall's tA. The matrix is symmetric about a diagonal of ones. (B) MDS of the RDMs. Each point represents an RDM, and distances between the points approximate the t<sup>A</sup> correlation distances (1 minus tA) among the RDMs. The 2D distances are highly correlated (0.94, Pearson; 0.91, Spearman) with the RDM correlation distances. Visual inspection reveals that the group-average RDM is similar to the ground-truth RDM. However, the groupaverage RDM is also similar to some other model RDMs. doi:10.1371/journal.pcbi.1003553.g003

patterns in a 100-dimensional response space, whose RDM matched the ground-truth RDM. (This was achieved by randomly sampling patterns from an isotropic Gaussian and then driving them to conform to the ground-truth RDM using forces.) Finally, we assumed the resulting patterns to be the ''true'' representation, and simulated data for 12 subjects, by adding a realistic level of isotropic Gaussian noise to the patterns.

### Results

Figures 2–4 show the results of the basic steps of RSA for a simulated data set – along with the ground truth the analysis is meant to reveal. Figure 5 shows the application of the key final inferential analyses to real data (from [19]). A good way to get started with the toolbox is to run DEMO1\_RSA\_ROI\_simulatedAndRealData.m, which reproduces all the results presented for simulated and real data in this paper (Figures 2–5, not including the additional results in Text S1).

### Step 1 — computing and visualizing RDMs

The first step is the calculation and visualization of the RDMs. This step is data-driven and helps reveal the dimensions of the stimulus space that are most strongly reflected in the response patterns. Figure 2 (top row) shows the RDMs for the simulated data. The group-average RDM better replicates the geometry simulated as ground truth, than the noisy single-subject RDMs. Multidimensional scaling [26–29] or t-SNE [30] may also be used in this step to visualize the similarity structure of the RDMs. These methods arrange the stimuli in a 2D plot such that the distances among them reflect the dissimilarities among the response patterns they elicited. Thus, stimuli that are placed closer together in these arrangements elicited more similar response patterns. Such visualizations provide an intuitive sense of the distinctions that are emphasized and de-emphasized by a population code. These methods are data-driven and do not presume a categorical structure. Hierarchical cluster trees (Figure 2, bottom) can help reveal categorical divisions. Unlike MDS, this technique assumes the existence of some categorical structure, but it does not assume any particular grouping into categories. In summary, step 1 consists in data-driven, exploratory methods that reveal the geometry of each representation by visualizing the RDMs and corresponding 2D arrangements and hierarchical cluster trees. These methods can be applied to each brain and model RDM. In step 2, the relationship among the representations in different brain regions and models will be explored.

### Step 2 — comparing brain and model RDMs

The second step of RSA is the descriptive visualization of the relationships among brain and model RDMs. To this end, we first consider the matrix of pairwise correlations between all brain and model RDMs. This matrix (Figure 3A) reveals, which representations in brain regions or models are similar, and which are dissimilar. Any metric that quantifies the extent to which two matrices are ''in agreement'' could be used as a measure of RDM similarity. We do not in general want to assume a linear relationship between the dissimilarities. Unless we are confident that our model captures not only the neuronal representational geometry but also its possibly nonlinear reflection in our response channels (e.g. fMRI patterns), assuming a linear relationship between model and brain RDMs appears questionable. We therefore prefer to assume that a model RDM predicts merely the rank order of the dissimilarities. For this reason we recommend the use of rank-correlations for comparing RDMs [19].

![](_page_4_Figure_1.jpeg)

Figure 4. Simulated representation – inferential comparisons of multiple model representations. Several candidate RDMs are tested and compared for their ability to explain the reference RDM. As expected, the true model corresponding to the simulated ground truth (no noise) is the most similar candidate RDM to the reference. Note that the true model falls within the ceiling range, indicating that it performs as well as any possible model can, given the noise in the data. The second best fit among the candidate RDMs is the categorical model with some extra information about the within-animate category structure. This model reflects the categorical clustering in the simulated data, but misses the simulated within-category structure. A horizontal line over two bars indicates that the two models perform significantly differently. The pairwise statistical comparisons show that the true model is significantly better than all other candidate RDMs. Most of the other pairwise comparisons are significant as well, illustrating the power of the signed-rank test used for comparing candidate performances in this simulated scenario. Kendall's t<sup>A</sup> is used as a measure of RDM similarity, because candidates include categorical models (i.e. models predicting equal dissimilarities for many pairs of stimuli). Other rank-correlation coefficients overestimate the performance of categorical candidate RDMs (Figure S2 in Text S1). All candidate RDMs except that obtained from the RADON model are significantly related to the reference RDM (p values from one-sided signed-rank test across single-subject estimates beneath the bars).

doi:10.1371/journal.pcbi.1003553.g004

Classical rank correlation measures are Spearman's rank correlation coefficient (which is the Pearson correlation coefficient computed on ranks), Kendall's rank correlation coefficient t<sup>A</sup> (''tau a'', which is the proportion of pairs of values that are consistently ordered in both variables), and the closely related coefficients tB, and t<sup>C</sup> (which deal with ties in different ways). We recommend Kendall's tA, when comparing models that predict tied ranks to models that make more detailed predictions. Kendall's t<sup>A</sup> is more

![](_page_5_Figure_1.jpeg)

Figure 5. Human IT (real data) – inferential comparisons of multiple model representations. Like Fig. 4, this figure demonstrates inferential analyses supported by the toolbox. Here, however, inference is performed on real data from fMRI. The smaller number of subjects (4) precludes the use of second-level inference with subject as a random effect. Relatedness to the reference RDM is therefore tested using stimulus-label randomization and the pairwise performance comparisons among the candidate RDMs (along with the error bars) are based on bootstrap resampling of the stimulus set. The models are the same as in Fig. 4 and reproduced here for convenience (except for the ''true model'', which is unknown for the real data). The comment bubbles detail the key changes in comparison to the analysis of Fig. 4, illustrating an alternative scenario for RSA statistical inference.

doi:10.1371/journal.pcbi.1003553.g005

likely than tB, tC, and the Pearson and Spearman correlation coefficients to prefer the true model over a simplified model that predicts tied ranks for a subset of pairs of dissimilarities (Supplementary Figure S2). Note that Matlab's Kendall rank correlation function implements tB, but the toolbox includes the more appropriate tA. Unfortunately, t<sup>A</sup> takes much longer to compute than the Spearman correlation coefficient, which can slow down randomization and bootstrap inference (step 3) substantially for large RDMs. In the absence of models that predict tied ranks, the Spearman correlation coefficient is a good alternative.

Visual inspection of the correlation matrix of RDMs (Figure 3A) enables the user to get a sense of how similar the representations in different brain regions and models are to each other. The MDS plot based on this matrix (Figure 3B) provides an intuitive overview of the relationships among the brain and model RDMs. However, statistical inference on the RDMs (step 3) is required to draw definite conclusions about these relationships.

### Step 3 — statistical inference

In Step 3, the final step, we perform statistical inference to assess whether RDMs are related and whether there are differences in the degree of relatedness between RDMs. For example, we might want to test which of several models explain variance in a given brain representation and whether some of them explain the representation better than others. Alternatively, we might want to test for which of several brain representations a given model explains variance, and whether it explains some brain representations better than others. In either case, we are relating one RDM (called the reference RDM) to multiple other RDMs (called the candidate RDMs).

Figure 4 shows the results of statistical inference for our simulated data set. In this example, the reference RDM is a (simulated) brain RDM (to be explained) and the candidate RDMs are model RDMs (serving to explain). Note that we refer to the reference RDM as a single representation, even though the analysis is based on one reference-RDM estimate per subject. The relatedness of a candidate RDM to the reference RDM is measured as the average across subjects of the correlations between the candidate RDM and the single-subject reference-RDM estimates.

The relatedness of each candidate RDM to the reference RDM (Figure 4, bar height) was tested using a one-sided signed-rank test [31] across the single-subject RDM correlations (p values under bars). This is the default test in the toolbox when there are 12 or more subjects (see Figures 4 and 5 and Text S1, in particular Figure S1, for the full range of statistical tests and the default choices). Note that although several models have very small correlations with the simulated reference RDM here, all except the RADON model are significantly related to the reference RDM.

In order to test whether two candidate RDMs differ in their relatedness to the reference RDM, the toolbox computes the difference between the RDM correlations in each subject and performs a two-sided signed-rank test across subjects here. As before, this is the default test when there are 12 or more subjects. This procedure is repeated for each pair of candidate RDMs, yielding a large number of statistical comparisons. Multiple testing is accounted for by controlling the false-discovery rate (Benjamini and Hochberg, [32]; by default, alternative: familywise error rate). The significant comparisons are indicated by horizontal lines above the bars.

Note that the analysis in Figure 4 also includes other brain RDMs (monkey IT, based on [6]; human early visual cortex, based on [19]) among the candidate RDMs. Comparing brain RDMs to other brain RDMs can reveal the relationships between their representations (''representational connectivity'' [13]). However, performance comparisons between candidate RDMs affected by noise to different degrees (such as noiseless models and brain RDMs) should not be formally interpreted.

Importantly, the bar graph includes an estimate of the noise ceiling. The noise ceiling is the expected RDM correlation achieved by the (unknown) true model, given the noise in the data. An estimate of the noise ceiling is important for assessing to what extent the failure of a model to reach an RDM correlation close to 1 is caused by a deficiency of the model or by the limitations of the experiments (e.g. high measurement noise and/or limited amount of data). If the best model does not reach the noise ceiling, we should seek a better model. If the best model reaches the noise ceiling, but the ceiling is far below 1, we should improve our experimental technique, so as to gain sensitivity to enable us to detect any remaining deficiencies of our model.

The noise ceiling is indicated by a gray horizontal bar, whose upper and lower edges correspond to upper- and lower-bound estimates on the group-average correlation with the RDM predicted by the unknown true model. Note that there is a hard upper limit to the average correlation with the single-subject reference-RDM estimates that any RDM can achieve for a given data set. Intuitively, the RDM maximizing the groupaverage correlation lies at the center of the cloud of singlesubject RDM estimates. Where exactly this ''central'' RDM falls depends on the chosen correlation type. For the Pearson correlation, we first z-transform the single-subject RDMs. For the Spearman correlation, we rank-transform the RDMs. After this transformation, the squared Euclidean distance is proportional to the respective correlation distance. This motivates averaging of the single-subject RDMs to find the RDM that minimizes the average of the squared Euclidean distances and, thus, maximizes the average correlation (see Text S1 for the proof). For Kendall's tA, we average the rank-transformed single-subject RDMs and use an iterative procedure to find the RDM that has the maximum average correlation to the singlesubject RDMs.

The average RDM (computed after the appropriate transform for each correlation type) can be thought of as an estimate of the true model's RDM. This estimate is overfitted to the single-subject RDMs. Its average correlation with the latter therefore overestimates the true model's average correlation, thus providing an upper bound. To estimate a lower bound, we employ a leave-onesubject-out approach. We compute each single-subject RDM's correlation with the average of the other subjects' RDMs. This prevents overfitting and underestimates the true model's average correlation because the amount of data is limited, thus providing a lower bound on the ceiling.

Figures 2–4 demonstrated the toolbox on simulated data, where the ground truth was known. In Figure 5, the inferential analyses are applied to a real data set (human IT, based on fMRI data from [19]). The structure of the reference RDM is very similar in the simulated and real data. However, we only have 4 subjects and so subject cannot be treated as a random effect in this analysis. The toolbox therefore uses a stimulus-label randomization test [33–34] to test the relatedness of each candidate RDM to the reference RDM, and a bootstrap test [35], based on resampling with replacement of the stimulus set, to compare the performance of different candidate RDMs.

### Additional Analysis Options

### Searchlight representational similarity analysis

ROI-based RSA analyzes the representational geometry in a predefined set of brain regions. However, other brain regions might also have representational geometries that conform to the predictions of our models. Searchlight analysis [5] provides a method of continuously mapping pattern information throughout the entire measured volume. The toolbox includes searchlight RSA [22] for fMRI data. RSA is carried out for a spherical cluster of voxels centered at each voxel. This provides an RDMcorrelation map for each model RDM, which reveals where in the brain the local representation conforms to the model's predictions. Inference is performed at each voxel by a signedrank test across subjects and the resulting p map is thresholded to control the false-discovery rate (see Text S1, in particular Figure S3, for details).

## The linear-discriminant t value: Combining the advantages of linear classifiers and representational similarity analysis

Linear classifiers have been successfully applied to a variety of neurophysiological data [2–4,36–37, for an introduction see 9]. They find optimal weights and enable highly sensitive detection of distributed information in a population code that can be linearly read out. However, they reflect only categorical distinctions and do not characterize the representational geometry as richly as RSA does. This raises the question of whether the advantages of these methods can be combined. RDMs are distance matrices whose entries reflect the separation in the representation of each pair of stimuli. We could use a linear classifier to estimate the discriminability of each pair of stimuli, and interpret these discriminabilities as our distances. Here we introduce a new measure of separability for RSA that is based on linear discriminant analysis. We first divide the data into two independent sets. For each pair of stimuli, we then fit a Fisher linear discriminant to one set, project the other set onto that discriminant dimension, and compute the t value reflecting the discriminability between the two stimuli. We call this multivariate separation measure the linear-discriminant t (LD-t) value. It can be interpreted as a crossvalidated, normalized variation on the Mahalanobis distance (see Figure S4). Note, however, that it is not a distance in the mathematical sense, because it can be negative. The LD-t has a number of desirable properties. First, whereas distance measures are positively biased, it is symmetrically distributed around 0 (t distribution) when the true distance is 0. The LD-t therefore enables instant inference on the discriminability (by converting the t values to p values) for each pair of stimuli. Second, it enables inference on mean discriminabilities across many pairs of stimuli by within-subject randomization of stimulus labels or across-subjects random-effects tests. (Other distance measures require bias correction, e.g. subtracting an estimate of the expected distance for repetitions of the same stimulus.) Third, the LD-t works well for conditionrich designs, in which we have few trials (or even just one trial) for each particular stimulus. (We can obtain an error covariance estimate pooled over all stimuli, whereas a linear support vector machine fitted to a pair of response patterns would reduce to a minimum Euclidean-distance classifier.) Fourth, in contrast to decoding accuracy (which could also be computed for each stimulus pair), the LD-t is a continuous measure in each subject and does not suffer from a ceiling effect. (When the decoding accuracy is at its 100% ceiling, the LD-t still continuously reflects the separation of the patterns in the multivariate response space.) The LD-t is supported by the toolbox and its application illustrated in Figure S5 (see Text S1 for more details).

### Discussion

We introduced a toolbox for RSA that supports the analysis of representational dissimilarity matrices characterizing brain regions and models. First, the RDMs for brain regions and models and their inter-relationships are visualized. Then statistical inference is performed to decide what models explain significant variance and whether the models perform significantly differently. The toolbox additionally supports searchlight RSA, i.e. the continuous mapping of RSA statistics throughout the brain. Finally, we introduced the linear-discriminant t value as a measure of multivariate discriminability that bridges the gap between classifier decoding and RSA.

### Choosing the most appropriate statistical inference procedure

The toolbox uses frequentist nonparametric inference procedures. For testing the relatedness of two RDMs, the preferred (and default) method is the signed-rank test across subjects. This test provides valid inference and treats the variation across subjects as a random effect, thus supporting inference to the population. The toolbox requires that RDMs for 12 or more subjects are available. (The test could also be used for within-subject inference, if 12 or more independent RDM estimates from the same subject were available.) The fixed-effects alternative is to test RDM relatedness using the stimulus-label randomization test [13]. This test is definitely valid and expected to be more powerful than the signedrank test across subjects, because it tests a less ambitious hypothesis: that the RDMs are related in the experimental group of subjects, rather than in the population. The stimulus-label randomization test can be used for a single subject or a group of any size. However, it does require a sufficient number of stimuli: at least 7, because for 6, there are only 6! = 720 unique permutations. The signed-rank test across subjects would work with as few as 4 stimuli (generating 6 dissimilarities, enough for rank correlations to take on an acceptable number of distinct values). However, the inference procedures have not been validated for very small numbers of conditions, so the toolbox currently requires 20 or more stimuli for the stimulus-label randomization test, and we suggest having at least 6 stimuli when using the signed-rank test across subjects. Note also that RSA lends itself to condition-rich designs and, in general, it is desirable to sample the stimulus space richly.

The relatedness of two RDMs can also be tested by bootstrapping the stimulus set and/or the subjects set. The motivation for bootstrapping is to simulate repeated sampling from the population. Bootstrapping, thus, can help generalize from the sampled subjects and/or stimuli to the population of subjects and/ or the population of stimuli. (The population of stimuli would be a typically very large set of possible stimuli, of which the experimental stimuli can be considered a random sample.) However, the bootstrap might not provide a very realistic simulation of repeated sampling from the population. The basic bootstrap tests implemented in the toolbox are known to be slightly optimistic. Future extensions might include bias-corrected and accelerated bootstrap methods [35].

Similar considerations apply to the tests of difference between candidate RDMs regarding their relatedness to the reference RDM. Again, the preferred (and default) test is the signed-rank test across subjects, which supports generalization to the population. Stimulus-label randomization is not appropriate in this context, because it simulates the null hypothesis that the RDMs are unrelated (and the stimulus labels, thus, exchangeable), rather than the appropriate null hypothesis that both candidate RDMs are equally related to the reference RDM. The alternative to the signed-rank test is the bootstrap test. Again, this can be based on resampling of the subjects and/or the stimuli. The slight optimism of basic bootstrap tests should be kept in mind. However, at conservative thresholds and with correction for multiple testing, this test provides a reasonable alternative to the signed-rank test, when there are not enough subjects.

### Testing many models

A key feature of the toolbox is the statistical comparison of multiple models. Figures 4 and 5 illustrate a typical scenario, in which a wide range of qualitatively different models explain significant variance in a brain region's representational geometry. These models include categorical models, models based on simple image features, complex computational models motivated by neurophysiological findings, and behavioral models. The finding that a model explains some variance in a brain representation (or conversely allows above-chance-level decoding) reveals that the region contains the information the model represents. However, this is a very low bar for a computational account of a brain representation. Many models will explain some component of the variance, so finding one such model does not substantially advance our understanding of brain function. Theoretical progress requires that we compare multiple models [14]. The toolbox enables the user to find the best among a whole range of models, and to assess which other models it significantly outperforms. Importantly, the noise ceiling reveals whether a model fully accounts for the nonnoise variance in the data, or leaves some variance to be explained.

If a computational model has parameters, these could be fitted with a separate data set (comprised of an independent sample of stimuli). Alternatively, if the parameter space is low-dimensional, it could be grid-sampled and all resulting RDM predictions entered as candidate RDMs for statistical comparison. Future extensions of the toolbox might include functions that support the fitting of parametric models and their validation with an independent data set.

### Relation to univariate encoding models

Univariate encoding models provide an alternative to RSA for testing computational models of brain information processing [38– 41]. Both approaches test forward models, i.e. models that operate in the direction of information flow in the brain: from stimuli to brain responses. The shared aim is to test to what extent each model can account for the neuronal representation in a brain region. However, univariate encoding models are fitted to predict each response channel (e.g. each voxel in fMRI) separately. RSA, in contrast, compares the model representation to the brain representation at the level of the response pattern dissimilarities. The two approaches have complementary advantages. Predicting every response channel separately enables us to create a map of the intrinsic spatial organization for each brain region. Predicting the dissimilarities of multivariate response patterns abstracts from the single representational units and focuses on the population representational geometry. We lose the detailed spatial organization (the trees) and gain a population summary (the forest). The representational dissimilarity trick [14] enables us to test computational models without first having to fit a linear model using a separate data set of responses to an independent stimulus sample. It also enables uncomplicated tests of categorical and behavioral models and of relationships between brain regions and between individuals and species [19]. The parallels and differences between these two approaches have been explored in greater detail in [10].

### Availability and Future Directions

The toolbox is freely available to the community. The user can download the toolbox at [http://www.mrc-cbu.cam.ac.uk/](http://www.mrc-cbu.cam.ac.uk/methods-and-resources/toolboxes/license/) [methods-and-resources/toolboxes/license/](http://www.mrc-cbu.cam.ac.uk/methods-and-resources/toolboxes/license/). The zip file containing the toolbox (rsatoolbox.zip, software S1) is also included in the supplementary materials.

There are a number of directions in which the toolbox might be extended in the future. First, we plan to add functionality for timeresolved RSA, including temporal-sliding-window techniques for electrophysiological data (MEG/EEG and invasive recordings). Such analyses can reveal the emergence and dynamics of representational geometries over the course of tens to hundreds of milliseconds after stimulus onset, reflecting recurrent neuronal computations [25,42]. Second, we would like to include additional methods for characterizing representational geometries. For example, Diedrichsen et al. [43] have proposed a technique for decomposition of the pattern variance into components reflecting different stimulus-related effects and noise. This approach promises estimates of the representational geometry that are more comparable between representations affected by different levels of noise. Another relevant recent technique is kernel analysis, which can reveal the complexity of categorical boundaries in a representation [44–45]. We expect that the field will develop a range of such useful descriptive measures for representational geometries. These should be included in the toolbox. Finally, it would be desirable to complement the frequentist approach described here by Bayesian inference procedures. By sharing the toolbox with the community, we hope to accelerate the collaborative pursuit of these methodological directions, in addition to contributing to neuroscientific studies that aim to reveal the nature of representational geometries throughout the brain.

### Supporting Information

Figure S1 Decision process for selection of statistical tests. The flow diagram above shows the default decision process by which the statistical inference procedures are chosen in the toolbox. The analyses in Figures 4 and 5 of the paper correspond to paths in the flowchart that lead to the leftmost (simulation in Figure 4) and second from right (real data in Figure 5) box at the bottom. Note that the flowchart does not capture all possibilities. For example, the fixed-effects condition-label randomization test of RDM relatedness can be explicitly requested, even when there are 12 or more subjects' estimates of the reference RDM and the random-effects signed-rank test would be chosen by default. (EPS)

Figure S2 Spearman versus Kendall's t<sup>A</sup> rank correlation for comparing RDMs. Here the inferential results from the paper using Kendall's t<sup>A</sup> (Figures 4, 5) are presented again (panels A, B), and compared to the results obtained using the Spearman correlation (panels C, D). The two rank correlation coefficients differ in the way they treat categorical models (blue bars) that predict tied dissimilarities. (A) For the simulated data, Kendall's t<sup>A</sup> correctly reveals that the true model (red bar) best explains the data. It is the only model that reaches the ceiling range, and it outperforms every other candidate significantly (horizontal lines above the bars). (C) For the Spearman correlation, the true model no longer has the greatest average correlation to the reference RDM. Two categorical candidate RDMs appear to outperform the true model, and significantly so (horizontal lines). Both of these categorical models and the true model now fall in the ceiling range. (B, D) For the real data, as well, categorical models (blue) are favored by the Spearman correlation. (EPS)

### Figure S3 Group-level results for 20 simulated subjects.

(A) A representational geometry of 64 patterns falling into two clusters was simulated in a brain region (shown in green) in each of 20 subjects. Data outside the green region was spatially and temporally correlated noise (typical of fMRI data) with no designrelated effects. Searchlight maps (searchlight radius = 7 mm) were generated by computing the correlation between a model RDM (reflecting the true cluster structure of the simulated patterns) and the searchlight RDM at each voxel in each subject. (B) At each voxel, a one-sided signed-rank test was applied to the subjectspecific correlation values. The 3D map of p value was thresholded so as to control the expected false-discovery rate at 0.05. Voxels exceeding the threshold are highlighted (yellow). The maps in both panels are superimposed on an anatomical T1 image re-sliced to fit the simulated brain dimensions. The red contours depict the borders of the brain mask. RDMs were computed for searchlights centered on each voxel within the brain mask. (EPS)

Figure S4 Relationship between the linear-discriminant t value and the Mahalanobis distance. In the Mahalanobis distance, the inverse of the error covariance (S) is pre- and postmultiplied by the difference vector between the pattern estimates (p1 and p2). If we use pattern estimates from an independent dataset (dataset 2) for the post-multiplication, we obtain the dataset-2 contrast estimate on the Fisher linear discriminant fit with dataset 1. This is because the first part of the definition of the Mahalanobis distance equals the weight vector w of the Fisher linear discriminant. The LD-t is the Fisher linear discriminant contrast (as shown) normalized by its standard error (estimated from the residuals of dataset 2 after projection on the discriminant dimension).

Figure S5 Random-effects inference on LD-t RDMs. (A)

Two fMRI datasets were simulated for 20 subjects. We simulated fMRI time-course data Y based on a realistic fMRI design matrix (X) with hemodynamic response predictors for 64 stimuli and patterns (B) with a predefined hierarchical cluster structure (two categories, each comprising two subcategories). The simulated data were Y = XB+E, where E is the time-by-response errors matrix, consisting of Gaussian noise temporally and spatially smoothed by convolution with Gaussians to create realistic degrees of temporal and spatial autocorrelation. The LD-t RDMs were computed for each subject and averaged across subjects. The

### References

(TIF)

- 1. Alivisatos AP, Chun M, Church GM, Greenspan RJ, Roukes ML, et al. (2012). The Brain Activity Map Project and the Challenge of Functional Connectomics. Neuron 74 (6): 970–974.
- 2. Haxby JV, Gobbini MI, Furey ML, Ishai A, Schouten JL, et al. (2001). Distributed and overlapping representations of faces and objects in ventral temporal cortex. Science 293: 2425–2430.
- 3. Hung CP, Kreiman G, Poggio T, DiCarlo JJ (2005). Fast Readout of Object Identity from Macaque Inferior Temporal Cortex. Science 310: 863–866. doi:10.1126/science.1117593
- 4. Kamitani Y and Tong F (2005). Decoding the visual and subjective contents of the human brain. Nature neuroscience 8: 679–685.
- 5. Kriegeskorte N, Goebel R, Bandettini P (2006). Information-based functional brain mapping. Proceedings of the National Academy of Sciences of the United States of America 103: 3863–3868.
- 6. Kiani R, Esteky H, Mirpour K, Tanaka K (2007). Object category structure in response patterns of neuronal population in monkey inferior temporal cortex. Journal of Neurophysiology 97: 4296–4309.
- 7. Haynes JD, Rees G, (2006). Decoding mental states from brain activity in humans. Nature Reviews Neuroscience 7: 523–534.
- 8. Norman KA, Polyn SM, Detre GJ, Haxby JV, (2006). Beyond mind-reading: multi-voxel pattern analysis of fMRI data. Trends in cognitive sciences 10: 424– 430.
- 9. Mur M, Bandettini PA, Kriegeskorte N, (2009). Revealing representational content with pattern-information fMRI—an introductory guide. Social cognitive and affective neuroscience 4: 101–109.
- 10. Kriegeskorte N, Kreiman G, (2011). Visual Population Codes: Toward a Common Multivariate Framework for Cell Recording and Functional Imaging. Cambridge: MIT Press.
- 11. Formisano E and Kriegeskorte N, (2012). Seeing patterns through the hemodynamic veil — The future of pattern-information fMRI. NeuroImage 62: 1249–1256. doi:10.1016/j.neuroimage.2012.02.078.
- 12. Kriegeskorte N, (2011). Pattern-information analysis: from stimulus decoding to computational-model testing. NeuroImage 56: 411–421
- 13. Kriegeskorte N, Mur M, Bandettini P, (2008). Representational similarity analysis–connecting the branches of systems neuroscience. Frontiers in systems neuroscience 2: 4.

group-average LD-t RDM is shown using a percentile color code. (B) Inference on LD-t RDMs with subject as random effect. LD-t analysis can serve the same purpose as classifier decoding analysis, to test for pattern information discriminating two stimuli. For each pair of stimuli, we used a one-sided signed-rank test across subjects and obtained a p value. The left panel shows the pairs with p, 0.05, uncorrected (red). The middle panel shows the pairs that survive control of the expected false-discovery rate (q,0.05). The right panel shows the pairs that survive Bonferroni correction (p, 0.05, corrected). (EPS)

Software S1 The zip file contains the complete RSA toolbox. It also contains demo functions and brain-activity- and behavior-based representational dissimilarity matrices used by the demo functions. DEMO1\_RSA\_ROI\_simulatedAndRealData.m reproduces the main parts of figures 2–5 of the main paper. The toolbox is written in Matlab and requires the Matlab programming environment.

(ZIP)

### Text S1 The supplementary materials (additional text) for the manuscript.

(DOCX)

### Acknowledgments

The authors are grateful to Ian Charest, Mirjana Bozic, Elisabeth Fonteneau, and Ian Nimmo-Smith for helpful comments, and for helping us test the toolbox on a variety of datasets.

### Author Contributions

Contributed reagents/materials/analysis tools: HN NK CW AW LS WMW. Wrote the paper: HN NK.

- 14. Kriegeskorte N and Kievit RA, (2013). Representational geometry: integrating cognition, computation, and the brain. Trends Cogn Sci 17: 401–412. doi:10.1016/j.tics.2013.06.007.
- 15. Op de Beeck H, Wagemans J, Vogels R, (2001). Inferotemporal neurons represent low-dimensional configurations of parameterized shapes. Nature neuroscience 4: 1244–1252.
- 16. Mur M, Meys M, Bodurka J, Goebel R, Bandettini PA, et al., (2013). Human Object-Similarity Judgments Reflect and Transcend the Primate-IT Object Representation. Front Psychol 4: 128.
- 17. Aguirre GK, (2007). Continuous carry-over designs for fMRI. Neuroimage 35: 1480–1494.
- 18. Kayaert G, Biederman I, Vogels R, (2005). Representation of regular and irregular shapes in macaque inferotemporal cortex. Cerebral Cortex 15: 1308– 1321.
- 19. Kriegeskorte N, Mur M, Ruff DA, Kiani R, Bodurka J, et al., (2008). Matching categorical object representations in inferior temporal cortex of man and monkey. Neuron 60: 1126–1141.
- 20. Schurger A, Pereira F, Treisman A, Cohen JD, (2010). Reproducibility distinguishes conscious from nonconscious neural representations. Science 327: 97–99.
- 21. Xue G, Dong Q, Chen C, Lu Z, Mumford JA, Poldrack RA, (2010). Greater Neural Pattern Similarity Across Repetitions Is Associated with Better Memory. Science, 330: 97–101.
- 22. Carlin JD, Calder AJ, Kriegeskorte N, Nili H, Rowe JB, (2011). A Head View-Invariant Representation of Gaze Direction in Anterior Superior Temporal Sulcus. Curr Biol 21: 1817–1821. doi:10.1016/j.cub.2011.09.025.
- 23. Haushofer J, Livingstone MS, Kanwisher N, (2008). Multivariate patterns in object-selective cortex dissociate perceptual and physical shape similarity. PLoS biology 6: e187.
- 24. Chum C, Mourao-Miranda J, Chiu YC, Kriegeskorte N, Tan G, Ashburner J, (2011). Utilizing temporal information in fMRI decoding: classifier using kernel regression methods abstract. Neuroimage 58: 560–571.
- 25. Su L, Fonteneau E, Marslen-Wilson W, Kriegeskorte N, (2012). Spatiotemporal Searchlight Representational Similarity Analysis in EMEG Source Space. In: Proceedings of 2nd International Workshop on Pattern Recognition in NeuroImaging (PRNI 2012).

- 26. Borg I, Groenen PJF, (2005). Modern multidimensional scaling: Theory and applications. Springer Verlag.
- 27. Kruskal JB, Wish M (1978) Multidimensional Scaling. Beverly Hills: Sage.
- 28. Shepard RN (1980) Multidimensional scaling, tree-fitting, and clustering. Science 210: 390–398.
- 29. Torgerson WS (1958) Theory and methods of scaling. Hoboken: Wiley.
- 30. Van der Maaten, L., Hinton, G (2008) Visualizing data using t-SNE. Journal of Machine Learning Research 9: 2579–260
- 31. Wilcoxon F (1945) Individual Comparisons by Ranking Methods. Biometrics Bulletin 1: 80–83.
- 32. Benjamini Y, Hochberg Y (1995) Controlling the false discovery rate: a practical and powerful approach to multiple testing. Journal of the Royal Statistical Society. Series B (Methodological): 289–300.
- 33. Fisher R.A. (1935). The design of experiments. Edinburgh: Oliver & Boyd.
- 34. Nichols TE, Holmes AP (2002) Nonparametric permutation tests for functional neuroimaging: a primer with examples. Human brain mapping 15: 1–25.
- 35. Efron B, Tibshirani R (1993) An introduction to the bootstrap. Volume 57. Boca Raton: CRC press.
- 36. Kriegeskorte N, Formisano E, Sorger B, Goebel R (2007) Individual faces elicit distinct response patterns in human anterior temporal cortex. Proc Natl Acad Sci 104: 20600–20605.
- 37. Misaki M, Kim Y, Bandettini PA, Kriegeskorte N, (2010). Comparison of multivariate classifiers and response normalizations for pattern-information fMRI. Neuroimage 53: 103–118.

- 38. Kay KN, Naselaris T, Prenger RJ, Gallant JL, (2008). Identifying natural images from human brain activity. Nature, 452(7185): 352–355.
- 39. Mitchell TM, Shinkareva SV, Carlson A, Chang KM, Malave VL, et al. (2008). Predicting human brain activity associated with the meanings of nouns. Science, 320(5880): 1191–1195.
- 40. Naselaris T, Kay KN, Nishimoto S, Gallant JL, (2011). Encoding and decoding in fMRI. Neuroimage, 56(2): 400–410.
- 41. Gallant JL, Nishimoto S, Naselaris T, Wu MC, (2011). System Identification, Encoding Models, and Decoding Models: A Powerful New Approach to fMRI Research. Visual Population Codes—toward a Common Multivariate Framework for Cell Recording and Functional Imaging. Cambridge: MIT Press.
- 42. Carlson T, Tovar DA, Alink A, Kriegeskorte N (2013). Representational dynamics of object vision: The first 1000 ms. Journal of vision 13(10). doi: 10.1167/13.10.1.
- 43. Diedrichsen J, Ridgway GR, Friston KJ, Wiestler T. (2011). Comparing the similarity and spatial structure of neural representations: a pattern-component model. NeuroImage 55(4): 1665–1678.
- 44. Cadieu CF, Hong H, Yamins D, Pinto N, Majaj NJ, et al. (2013). The Neural Representation Benchmark and its Evaluation on Brain and Machine. arXiv:1301.3530. Available:<http://arxiv.org/abs/1301.3530>. Accessed 24 March 2014.
- 45. Montavon G, Braun ML, Mu¨ller KR (2011). Kernel analysis of deep networks. The Journal of Machine Learning Research 12: 2563–2581.

# Supplementary materials

# **A toolbox for representational similarity analysis**

Nili H, Wingfield C, Walther A, Su L, Marslen-Wilson W, Kriegeskorte N

# **Getting started with the toolbox**

The toolbox folder has a number of built-in, ready-to-use demo files that can serve as a prototype for the user's analysis. To run the demos and get figures similar to those in the paper, the user should proceed as follows:

- (1) Download the toolbox from here: <http://www.mrc-cbu.cam.ac.uk/methods-and-resources/toolboxes/license/>
- (2) Save a local copy of the RSAtoolbox folder.
- (3) Open Matlab and set the current directory to the *Demo* subfolder of the toolbox folder (..\RSAtoolbox\Demos)
  - a. Run DEMO1\_RSA\_ROI\_simulatedAndRealData.m for a demonstration of ROI-based analysis using the toolbox. It simulates RDMs, analyzes them with RSA, and reproduces the results from Figures 2-5 of the main paper.
  - b. Run DEMO2\_RSA\_ROI\_sim.m for a demonstration of the ROI-based RSA on simulated fMRI data. This script will familiarize the user with the pipeline for analyzing fMRI data.
  - c. Run DEMO3\_LDt\_sim.m for a demonstration of the computation of LD-*t* RDMs and associated inference procedures. Running the script reproduces Figure S5.
  - d. Run DEMO4\_RSAsearchlight\_sim.m for a demonstration of the searchlight analysis on simulated fMRI data. Running this script reproduces Figure S3.

The first three demos take a few minutes to run. The searchlight demo can take hours the first time it is run, because it needs to simulate data for the whole brain in multiple subjects. The searchlight analysis of the simulated data takes only a couple of minutes per subject on a modern workstation.

# **Toolbox modules**

The toolbox contains "*recipes*" (i.e. top-level scripts) that implement the previously described analysis steps on fMRI response patterns. For the *recipes* (located in the "*Recipe*" directory) to work, all the user has to do is to define the model RDMs to be included in the analysis and to complete the information in the Matlab script called *projectOptions*. Once the project options have been specified, the *Recipe* function can be executed and results are displayed and saved in specified directories. The *projectOptions* contains information about the data structure (e.g. where the ROI masks or the response patterns are stored) and also analysis settings, including the response-pattern dissimilarity measure, and inference settings.

The table below gives the names and descriptions of the key functions of the toolbox. The right column specifies the analysis step (main paper text) to which the function contributes.

**Table S1: Key functions of the RSA toolbox**

| function name          | description                                                                                                                                                           | step |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------|
| constructRDMs          | takes the data matrix (response patterns for<br>all experimental<br>conditions) and computes RDMs from it                                                             | 1    |
| figureRDMs             | displays a number of RDMs                                                                                                                                             | 1    |
| dendrogramConditions   | generates a text-labeled<br>dendrogram for the input RDMs                                                                                                             | 1    |
| MDSConditions          | generates an<br>MDS or t-SNE arrangement of the stimuli (using<br>stimulus icons or colored dots) for the input RDMs                                                  | 1    |
| pairwiseCorrelateRDMs  | given a number of RDMs, this module will compute and<br>visualize an RDM correlation matrix<br>(comparing each RDM to<br>each other RDM)                              | 2    |
| MDSRDMs                | draws an MDS arrangement of the RDMs                                                                                                                                  | 2    |
| compareRefRDM2candRDMs | statistical inference function that compares a reference RDM to<br>multiple<br>candidate<br>RDMs<br>using<br>a<br>variety<br>of<br>frequentist<br>nonparametric tests | 3    |

# **Key function for statistical inference**

The key function for statistical inference in the toolbox is compareRefRDM2candRDMs.m. This function implements all inference procedures described in the paper. Here we describe these procedures in greater detail. We first explain the general functionality, with some redundancy to the main paper. We then define the usage and all inputs and outputs of the function in detail. The text below is identical to the help text of compareRefRDM2candRDMs.m, but Figure S1 has been added to give an overview of the statistical inference methods, the circumstances under which each is available, and the default choices.

# *General purpose*

The function compareRefRDM2candRDMs.m compares a reference RDM to multiple candidate RDMs. For example, the reference RDM could be a brain region's RDM and the candidate RDMs could be multiple computational models. Alternatively, the

reference RDM could be a model RDM and the candidate RDMs could be multiple brain regions' RDMs. More generally, the candidate RDMs could include both model RDMs and RDMs from brain regions, and the reference RDM could be either a brain RDM or a model RDM. In all these cases, one reference RDM is compared to multiple candidates.

![](_page_13_Figure_1.jpeg)

**Figure S1: Decision process for selection of statistical tests**. The flow diagram above shows the default decision process by which the statistical inference procedures are chosen in the toolbox. The analyses in Figures 4 and 5 of the paper correspond to paths in the flowchart that lead to the leftmost (simulation in Figure 4) and second from right (real data in Figure 5) box at the bottom. Note that the flowchart does not capture all possibilities. For example, the fixed-effects condition-label randomization test of RDM relatedness can be explicitly requested, even when there are 12 or more subjects' estimates of the reference RDM and the random-effects signed-rank test would be chosen by default.

# *Testing RDM correlations*

The function compares the reference RDM to each of the candidates, tests each candidate for significant RDM correlation (test dependent on input data and userOptions) and presents a bar graph of the RDM correlations in descending order from left to right (best candidates on the left) by default, or in the order in which the candidate RDMs are passed. In addition, pairwise comparisons between the candidate RDMs are performed to assess, for each pair of candidate RDMs, which of the two RDMs is more consistent with the reference RDM. A significant pairwise difference is indicated by a horizontal line above the corresponding two bars. Each bar comes with an error bar, which indicates the standard error, estimated by the same procedure as is used for the pairwise candidate comparisons (dependent on input data and userOptions, see below).

Statistical inference on the correlation between the reference RDM and each candidate RDM is performed using a one-sided Wilcoxon signed-rank across subjects by default. When the number of subjects is insufficient (<12), or when requested in userOptions, the test is instead performed by condition-label randomisation. By default, the false-discovery rate is controlled for these tests across candidate models. When requested in userOptions, the familywise error rate is controlled instead.

# *Comparisons between candidate RDMs*

For the comparisons between candidate RDMs as well, the inference procedure depends on the input data provided and on userOptions. By default, a signed-rank test across repeated measurements of the RDMs (e.g. multiple subjects or sessions) is performed. Alternatively, these tests are performed by bootstrapping of the subjects and/or conditions set. Across the multiple pairwise comparisons, the function controls the familywise error rate (Bonferroni method) or the false-discovery rate (Benjamini and Hochberg, 1995).

# *Ceiling upper and lower bounds*

If multiple instances of the reference RDM are passed (typically representing estimates for multiple subjects), a ceiling estimate is indicated by a gray transparent horizontal bar. The ceiling is the expected value, given the noise (i.e. the variability across subjects), of the average correlation of the true model's RDM with the single-subject RDMs. The upper and lower edges of the ceiling bar are upper- and lowerbound estimates for the unknown true ceiling. The upper bound is estimated by computing the correlation between each subject's RDM and the group-average RDM. The lower bound is estimated similarly, but using a leave-one-out approach, where each subject's RDM is correlated with the average RDM of the other subjects' RDMs. When Pearson correlation is chosen for comparing RDMs (userOptions.RDMcorrelationType), the RDMs are first z-transformed. When Spearman correlation is chosen, the RDMs are first rank-transformed. When Kendall's tau a is chosen, an iterative procedure is used. See main paper for a full motivation for the ceiling estimate and for an explanation of why these are useful upper- and lower-bound estimates. (See also below, under *(5) Estimating the upper bound on the noise ceiling for the RDM correlation*.)

# *Usage*

```
stats_p_r = compareRefRDM2candRDMs(refRDM, candRDMs[, userOptions])
```

# *Arguments*

### refRDM

The reference RDM, which can be a square RDM or lower-triangular- vector RDM, or a wrapped RDM (structure specifying a name and colour for colour-coding of the RDM in figures). refRDM may also be a set of independent estimates of the same RDM (square matrices or lower-triangular vectors stacked along the third dimension or a structured array of wrapped RDMs), e.g. an estimate for each of multiple subjects or sessions, which are then used for random-effects inference.

### candRDMs

A cell array with one cell for each candidate RDM. The candidate RDMs can be square or lowertriangular-vector RDMs or wrapped RDMs. Each candidate RDM may also contain multiple independent estimates of the same RDM, e.g. an estimate for each of multiple subjects or sessions. These can be used for random-effects inference if all candidate RDMs have the same number of independent estimates, greater than or equal to 12. However, if refRDM contains 12 or more independent estimate of the reference RDMs, then random-effects inference is based on these and multiple instances of any candidate RDMs are replaced by their average. In case the dissimilarity for a given pair of conditions is undefined (NaN) in any candidate RDM or in the reference RDM, that pair is set to NaN in all RDMs and treated as a missing value. This ensures that comparisons between candidate RDMs are based on the same set of dissimilarities.

## userOptions.RDMcorrelationType

The correlation coefficient used to compare RDMs. This is 'Spearman' by default, because we prefer not to assume a linear relationship between the distances (e.g. when a brain RDM from fMRI is compared to an RDM predicted by a computational model). Alternative definitions are 'Kendall\_taua' (which is appropriate whenever categorical models are tested) and 'Pearson'. The Pearson correlation coefficient may be justified when RDMs from the same origin (e.g. multiple computational models or multiple brain regions measured with the same method) are compared. For more details on the RDM correlation type, see main paper and Figure S2.

### userOptions.RDMrelatednessTest

'subjectRFXsignedRank' (default): Test the relatedness of the reference RDM to each candidate RDM by computing the correlation for each subject and performing a one-sided Wilcoxon signed-rank test against the null hypothesis of 0 correlation, so as to test for a positive correlation. (Note that multiple independent measurements of the reference or candidate RDMs could also come from repeated measurements within one subject. We refer to the instances as "subjects", because subject randomeffects inference is the most common case.)

'randomisation': Test the relatedness of the reference RDM to each candidate RDM by randomising the condition labels of the reference RDM, so as to simulate the null distribution for the RDM correlation with each candidate RDM. In case there are multiple instances of the reference or candidate RDMs, these are first averaged.

'conditionRFXbootstrap': Test the relatedness of the reference RDM to each candidate RDM by bootstrapping the set of conditions (typically: stimuli). For each bootstrap sample of the conditions set, a new instance is generated for the reference RDM and for each of the candidate RDMs. Because bootstrap resampling is resampling with replacement, the same condition can appear multiple times in a sample. This entails 0 entries (from the diagonal of the original RDM) in off-diagonal positions of the RDM for a bootstrap sample. These zeros are treated as missing values and excluded from the dissimilarities, across which the RDM correlations are computed. The p value for a one-sided test of the relatedness of each candidate RDM to the reference RDM is computed as the proportion of bootstrap samples with a zero or negative RDM correlation. This test simulates the variability of the estimates across condition samples and thus supports inference generalising to the population of conditions (or stimuli) that the condition sample can be considered a random sample of. Note that basic bootstrap tests are known to be slightly optimistic.

'subjectConditionRFXbootstrap': Bootstrap resampling is simultaneously performed across both subjects and conditions. This simulates the greater amount of variability of the estimates expected if the experiment were repeated with a different sample of subjects and conditions. This more conservative test attempts to support inference generalising across both subjects and stimuli (to their respective populations). Again, the usual caveats for basic bootstrap tests apply.

'none': Omit the test of RDM relatedness.

userOptions.RDMrelatednessThreshold

The significance threshold (default: 0.05) for testing each candidate RDM for relatedness to the reference RDM. Depending on the choice of multiple testing correction (see next userOptions field), this can be the expected false-discovery rate, the familywise error rate, or the uncorrected p threshold.

userOptions.RDMrelatednessMultipleTesting

'FDR' (default): Control the false-discovery rate across the multiple tests (one for each candidate RDM). With this option, userOptions.RDMrelatednessThreshold is interpreted to specify the expected false-discovery rate, i.e. the expected proportion of candidate RDMs falsely declared significant among all candidate RDMs declared significant.

'FWE': Control the familywise error rate. When the condition-label randomisation procedure is selected to test RDM relatedness, then randomisation is used to simulate the distribution of maximum RDM correlations across all candidate RDMs. This method is more powerful than Bonferroni correction when there are dependencies among candidate RDMs. If another test is selected to test RDM relatedness, the Bonferroni method is used. In either case, userOptions.RDMrelatednessThreshold is interpreted as the familywise error rate, i.e. the probability of getting any false positives under the omnibus null hypothesis that all candidate RDMs are unrelated to the reference RDM.

'none': Do not correct for multiple testing (not recommended). With this setting, userOptions.RDMrelatednessThreshold is interpreted as the uncorrected p threshold.

### userOptions.candRDMdifferencesTest

'subjectRFXsignedRank' (default, data permitting): For each pair of candidate RDMs, perform a statistical comparison to determine which candidate RDM better explains the reference RDM by using the variability across subjects of the reference or candidate RDMs. The test is a two-sided Wilcoxon signed-rank test of the null hypothesis that the two RDM correlations (refRDM to each of the candidate RDMs) are equal. This is the default test when multiple instances of the reference RDM (typically corresponding to multiple subjects) or a consistent number of multiple instances of each candidate RDMs is provided and the number of multiple instances is 12 or greater. This test supports inference generalising to the population of subjects (or repeated measurements) that the sample can be considered a random sample of.

'subjectRFXbootstrap': For each pair of candidate RDMs, perform a two-sided statistical comparison to determine, which candidate RDM better explains the reference RDM by bootstrapping the set of subjects. For each bootstrap sample of the subjects set, the RDMs are averaged across the bootstrap sample and the difference between the two RDM correlations (refRDM to each of the candidate RDMs) is computed. The p value is estimated as the proportion of bootstrap samples further in the tails (symmetrically defined for a two-sided test) than 0. This test simulates the variability of the estimates across subject samples and thus supports inference generalising to the population of subjects (or repeated measurements) that the sample can be considered a random sample of. The usual caveats for basic bootstrap tests apply.

'conditionRFXbootstrap': For each pair of candidate RDMs, perform a two-sided statistical comparison to determine which candidate RDM better explains the reference RDM by bootstrapping the set of conditions (typically: stimuli). For each bootstrap sample of the conditions set, a new instance is generated for the reference RDM and for each of the candidate RDMs. Because bootstrap resampling is is resampling with replacement, the same condition can appear multiple times in a sample. This entails 0 entries (from the diagonal of the original RDM) in off-diagonal positions of the RDM for a bootstrap sample. These zeros are treated as missing values and excluded from the dissimilarities, across which the RDM correlations are computed. The p value for the two-sided test of the difference for each pair of candidate RDMs is computed as for the setting subjectRFXbootstrap (see above). This test simulates the variability of the estimates across condition samples and thus supports inference generalising to the population of conditions (typically stimuli) that the condition sample can be considered a random sample of. Again, the usual caveats for bootstrap tests apply.

'subjectConditionRFXbootstrap': Bootstrap resampling is simultaneously performed across both subjects and conditions. This simulates the greater amount of variability of the estimates expected if the experiment were repeated with a different sample of subjects and conditions. This more conservative

test attempts to support inference generalising across both subjects and stimuli (to their respective populations. However, the usual caveats for bootstrap tests apply.

'none': Omit the pairwise tests of candidate RDMs comparing their relative ability to explain the reference RDM.

userOptions.candRDMdifferencesThreshold

The significance threshold for comparing each pair of candidate RDMs in terms of their relatedness to the reference RDM. Depending on the choice of multiple testing correction (see next userOptions field), this can be the expected false-discovery rate, the familywise error rate, or the uncorrected p threshold.

userOptions.candRDMdifferencesMultipleTesting

'FDR': Control the false-discovery rate across the multiple tests (one for each candidate RDM). With this option, userOptions.candRDMdifferencesThreshold is interpreted to specify the expected false-discovery rate, i.e. the expected proportion of pairs of candidate RDMs falsely declared significantly different among all pairs of candidate RDMs declared significantly different (in their relatedness to the reference RDM).

'FWE': Control the familywise error rate. With this option, the Bonferroni method is used to ensure that the familywise error rate is controlled. userOptions.candRDMdifferencesThreshold is interpreted as the familywise error rate, i.e. the probability of getting any false positives under the omnibus null hypothesis that all pairs of candidate RDMs are equally related to the reference RDM.

'none': Do not correct for multiple testing (not recommended). userOptions. candRDMdifferencesThreshold is interpreted as the uncorrected p threshold.

userOptions.nRandomisations

The number of condition-label randomisations (default: 10,000) used to simulate the null distribution that the reference RDM is unrelated to each of the candidate RDMs.

userOptions.nBootstrap

The number of bootstrap resamplings (default: 1,000) used in all selected bootstrap procedures (relatedness test, candidate comparison tests, error bars).

```
userOptions.plotpValues
```

This option controls how the significance of the RDM relatedness tests is indicated. If set to '\*' (default), then an asterisk is plotted on the bar for each candidate RDM that is significantly related to the reference RDM. Significance depends on the test (see above) and on userOptions. RDMrelatednessThreshold (default: 0.05) and on userOptions. RDMrelatednessMultipleTesting (default: 'FDR'). Asterisks mark candidate RDMs that are significant at the specified threshold and with the chosen method for accounting for multiple testing. If set to '=', then the uncorrected p value is plotted below the bar for each candidate RDM, and it is plotted in bold type if it is significant by the criteria explained above.

```
userOptions.barsOrderedByRDMCorr
```

This option controls the order of the displayed bars (default: true). If set to true, bars corresponding to candidate RDMs are displayed in descending order (from left to right) according to their correlation to the reference RDM. Otherwise, bars are displayed in the order in which the candidate RDMs are passed.

```
userOptions.figureIndex
```

This option enables the user to specify the figure numbers for the two created figures (default: [1 2]). The first figure contains the bargraph and the second contains matrices indicating the significance of the pairwise candidate RDM comparisons. The first panel shows the uncorrected-p matrix. The second panel shows the thresholded uncorrected-p matrix. The third panel shows the FDR-thresholded p matrix. The fourth panel shows the Bonferroni-thresholded p matrix.

```
userOptions.resultsPath
```

This argument specifies the absolute path in which both figures are to be saved (default: pwd, i.e. current working directory).

```
userOptions.saveFigurePDF
```

If set to true (default), the figures are saved in PDF format in userOptions.resultsPath.

```
userOptions.saveFigurePS
```

If true (default: false), the figures are saved in post-script format in userOptions.resultsPath.

userOptions.saveFigureFig

If true (default: false), the figures are saved in Matlab .fig format in userOptions.resultsPath.

userOptions.figure1filename

The filename for the bargraph figure, if chosen to be saved (default:

'compareRefRDM2candRDMs\_barGraph').

userOptions.figure2filename

The filename for the p-value display figure, if chosen to be saved (default:

'compareRefRDM2candRDMs\_RDMcomparisonPvalues').

# *Return values*

stats\_p\_r

Structure containing numerical statistical results, including effect sizes and p values.

stats\_p\_r.candRelatedness\_r: average correlations to reference RDM stats\_p\_r.candRelatedness\_p: corresponding uncorrected p values stats\_p\_r.SEs: standard errors of average RDM correlations stats\_p\_r.candDifferences\_r: matrix of bar-height differences (i.e. average RDMcorrelation differences) stats\_p\_r.candDifferences\_p: matrix of p values for all pairwise candidate comparisons stats\_p\_r.orderedCandidateRDMnames: candidate RDM names in the order in which the bars

are displayed (also the order used for the return

values)

stats\_p\_r.ceiling: ceiling lower and upper bounds

# **Spearman correlation or Kendall's <sup>A</sup> for comparing RDMs?**

We recommend using Kendall's <sup>A</sup> whenever categorical models are among the candidate RDMs. The Spearman correlation coefficient favors models that predict tied dissimilarities, as categorical models do. In the presence of noise, the true model (the one that generated the data in a simulation) can be outperformed by a categorical model that gets the major distinctions right (Figure S2), but misses the details.

![](_page_21_Figure_2.jpeg)

**Figure S2: Spearman versus Kendall's <sup>A</sup> rank correlation for comparing RDMs.** Here the inferential results from the paper using Kendall's <sup>A</sup> (Figures 4, 5) are presented again (panels A, B), and compared to the results obtained using the Spearman correlation (panels C, D). The two rank correlation coefficients differ in the way they treat categorical models (blue bars) that predict tied dissimilarities. **(A)** For the simulated data, Kendall's <sup>A</sup> correctly reveals that the true model (red bar) best explains the data. It is the only model that reaches the ceiling range, and it outperforms every other candidate significantly (horizontal lines above the bars). **(C)** For the Spearman correlation, the true model no longer has the greatest average correlation to the reference RDM. Two categorical candidate RDMs appear to outperform the true model, and significantly so (horizontal lines). Both of these categorical models and the true model now fall in the ceiling range. **(B, D)** For the real data, as well, categorical models (blue) are favored by the Spearman correlation.

# **Estimating the upper bound on the noise ceiling for the RDM correlation**

*Pearson correlation.* When the Pearson correlation is chosen as the measure for comparing RDMs, we z-transform each single-subject RDM. This projects the RDMs onto a hypersphere centered on the origin of RDM space (and restricted to a hyperplane including the origin and orthogonal to the all-1 vector). We refer to the single-subject RDMs on the hypersphere as the "data points". The z-transform renders the Pearson correlation distance (1-r) proportional to the squared Euclidean distance between points on the hypersphere. This motivates averaging of the z-transformed RDMs, because the average RDM (referred to as the "centroid" below), then, minimizes the sum of squared deviations (across dimensions and subjects), which is the sum of squared Euclidean distances between the centroid and the data points. It obviously also minimizes the *average* of the squared Euclidean distances, which is the sum divided by the number of subjects. However, the centroid will not in general fall on the hypersphere (where squared Euclidean distances are proportional to correlation distances). Since the distances to the data points are smaller for the centroid than for any point on the hypersphere, we can obtain an upper bound by converting the average squared Euclidean distance for the centroid to a correlation. Unfortunately, this bound is not tight. For a tighter bound, we might project the centroid onto the hypersphere first (or equivalently average the correlations between centroid and data points). Although the centroid minimizes the average squared Euclidean distance, we haven't shown that its projection onto the hypersphere minimizes this quantity among all points on the hypersphere. So the question remains: What RDM strictly maximizes the average correlation to the data points?

An RDM is defined by the direction of a vector in the space. Because we are using the correlation distance, two vectors pointing in the same direction represent identical RDMs, even if their lengths differ. We are seeking the direction that maximizes the average correlation with the data points. The correlations are the cosines of the angles between centroid and data points. Because the data points are on the hypersphere they are all equidistant from the origin. For any given vector, the cosines of the angles to the data points are therefore proportional to the magnitudes of the projections of the data points onto the vector (where the magnitudes are the distances from the origin measured on the vector). The vector maximizing the average correlation is, thus, the vector maximizing the average magnitude of the projections of the data points. The average magnitude of the projections is the magnitude of the projection of the average of the data points. We are, thus, seeking the direction that maximizes the magnitude of the projection of the average RDM. This is the vector representing the average RDM (i.e. the vector emanating from the origin and passing through the average RDM). We therefore obtain a tight upper bound on the noise ceiling by averaging the single-subject RDMs (after z-transform) and computing the average correlation to the single-subject RDMs.

*Spearman correlation.* For the Spearman correlation, we replace the z-transform used in the context of the Pearson correlation by the rank-transform, and obtain exactly the same results. Like the z-transform, the rank-transform normalizes the mean and the variance of each RDM. Like the z-transform, the ranktransform projects the RDMs onto a hypersphere (within a hyperplane). Rank-transforming each RDM renders the Spearman correlation distance proportional to the squared Euclidean distance. All further results, including the proof of the tight upper bound on the ceiling, also parallel those just described for the Pearson correlation. We therefore compute the average of the rank-transformed single-subject RDMs and compute this RDM's average Spearman correlation to the single-subject RDMs to obtain a tight upper bound on the noise ceiling.

*Kendall's A.* For Kendall's A, the situation is more complicated. However, there again is a space in which the squared Euclidean distance is proportional to the correlation distance. We need to convert each RDM to a vector of pair relations, with one entry for each pair of dissimilarities. The entry is 1 if the first dissimilarity in the pair is larger, and -1 if the second dissimilarity is larger. The squared Euclidean distance between two RDMs in this representation is proportional to the <sup>A</sup> correlation distance (1 - A). This motivates averaging RDMs in this representation. However, the average in this new embedding space does not correspond to a point representing an RDM. In the present scenario, the embedding space of pair relations is much more complex. The average in this space minimizes the average squared Euclidean distance to the points representing the single-subject RDMs. Because there can be no point in the embedding space having a smaller average squared Euclidean distance to the single-subject RDM points, this provides an upper bound on the noise ceiling for Kendall's A. However, the upper bound is not tight at all – presumably because of the much greater complexity of the embedding space. In contrast to the cases of the Pearson and Spearman correlation coefficients described above, we have no closed-form solution for the RDM maximizing the average Kendall-<sup>A</sup> correlation to the single-subject RDMs. We therefore instead average the rank-transformed single-subject RDMs as an initial estimate. We then iteratively optimize this initial estimate by randomly perturbing the dissimilarity values. In practice, this does lead to improvements, although they are very small in our experience, suggesting that the average of the rank-transformed RDMs (which provides the exact solution for the Spearman correlation) might provide an approximate solution for Kendall's A. The maximum average Kendall <sup>A</sup> estimated by iterative optimization provides our estimate of the upper bound on the ceiling.

# **Searchlight RSA**

Often one does not know a priori where in the brain a given representation might reside. An analysis based exclusively on predefined ROIs could miss the most important region. To overcome this limitation, searchlight analysis has been proposed as a way of continuously mapping pattern information throughout the volume (Kriegeskorte et al., 2006). Combining the searchlight approach with RSA might enable us to find brain representations that conform to particular stages of processing in computational models. The toolbox supports searchlight RSA.

Similar to ROI-based RSA, the user can test multiple models, by comparing their predicted RDMs to brain RDMs estimated for the local neighborhood around each voxel. A spherical searchlight is centered on each voxel in turn, containing all voxels within a specified radius. An RDM is then computed based on the response patterns of the voxels within the searchlight. The correlation between the searchlight RDM and each model RDM is stored in a map at the central voxel, yielding one searchlight RDM-correlation map per model. To combine searchlight maps across subjects, the maps can be transformed to a common space (e.g. MNI space). Alternatively, the original data can be transformed to the common space as part of the preprocessing of the data. For each model, the searchlight-RDM correlation maps are tested against zero using the Wilcoxon signed-rank test (one-sided) across subjects (subject as random effect). Comparisons between models can similarly be inferentially mapped, by first subtracting the two maps corresponding to the models to be compared within each subject, and then applying the

signed-rank test across subjects to the difference maps. To account for multiple testing throughout the search volume, we control the expected false-discovery rate (Benjamini and Hochberg, 1995).

![](_page_24_Figure_1.jpeg)

![](_page_24_Figure_2.jpeg)

**Figure S3: Group-level results for 20 simulated subjects. (A)** A representational geometry of 64 patterns falling into two clusters was simulated in a brain region (shown in green) in each of 20 subjects. Data outside the green region was spatially and temporally correlated noise (typical of fMRI data) with no design-related effects. Searchlight maps (searchlight radius = 7 mm) were generated by computing the correlation between a model RDM (reflecting the true cluster structure of the simulated patterns) and the searchlight RDM at each voxel in each subject. **(B)** At each voxel, a one-sided signed-rank test was applied to the subject-specific correlation values. The 3D map of p values was thresholded so as to control the expected false-discovery rate at 0.05. Voxels exceeding the threshold are highlighted (yellow). The maps in both panels are superimposed on an anatomical T1 image re-sliced to fit the simulated brain dimensions. The red contours depict the borders of the brain mask. RDMs were computed for searchlights centered on each voxel within the brain mask.

The toolbox contains a searchlight demo (DEMO4\_RSAsearchlight\_sim.m) that implements the subject-random-effects approach. The purpose of this demo is to familiarize the user with the scripts and functions used to compute searchlight maps. The demo simulates a categorical representation restricted to a specific region of the brain. Figure S3 shows the results of the demo with the search volume corresponding to a whole-brain analysis at conventional fMRI resolution (64 by 64 in plane, 32 slices).

An alternative approach to inference would be a fixed-effects randomization test (Nichols and Holmes, 2002; Kriegeskorte et al., 2006; Kriegeskorte et al., 2008), which can be applied to single subjects or to groups of less than 12 subjects, where subject random-effects analysis might not be appropriate. Each model RDM would be subjected to condition-label randomization (consistently permuting rows and columns) to simulate the null distribution. Then a group-average searchlight-RDM correlation map would be computed. To this end, we can either compute the correlation between the model RDM and the group-average searchlight RDM, or the average of the correlations between the model RDM and the subject-specific searchlight RDMs. We compute a large number (e.g. 1000) of these null searchlight group maps and store the maximum across the spatial extent of the map each time. We then select the 95th percentile of this null distribution of map maxima as our threshold. We apply this threshold to the searchlight group map computed for the correct labeling of the model RDM (unpermuted).

This procedure accurately controls the familywise error rate and has good sensitivity because the null simulation accounts for the dependencies between nearby locations. When a large volume is expected to contain representational geometries related to the model, controlling the false-discovery rate is expected to provide greater sensitivity than controlling the familywise error rate. False-discovery rate control could be combined with a fixed-effects randomization test by simulating a separate null distribution at every voxel. For a given method of accounting for multiple testing, the fixed-effects approach is expected to be more powerful than the random-effects approach, because the latter attempts to generalize to the population. However, with any continuous mapping method, the multiple testing still reduces the power for a given region, compared to an ROI-based approach that investigates only a small number of regions.

# **Computing the linear-discriminant** *t* **value**

For each pair of experimental stimuli *i* and *j*, we first seek a weighted average of the response channels that enables us to optimally discriminate *i* and *j*. For homoscedastic multivariate normal errors, the optimal weights are:

$$w = (p_i - p_j) \cdot \Sigma^{-1}$$
 (Fisher linear discriminant),

where *p<sup>i</sup>* and *p<sup>j</sup>* are the response patterns corresponding to experimental stimuli *i* and *j*, respectively, and is the covariance matrix of the errors (whose height and width equals the number of response channels). We could first estimate single-trial patterns, and then subtract the corresponding conditionmean patterns to obtain the errors matrix for estimating . Alternatively, for time-course data (e.g. fMRI), a linear-model fit to each response channel's time series could provide the errors matrix (number of time points by number of response channels). Given the errors matrix, we could use the sample covariance

or a shrinkage estimator (Ledoit and Wolf, 2003) of the covariance. The latter choice promises a more stable covariance estimate that is guaranteed to be invertible. The weights defining the linear discriminant are estimated for dataset 1 (the training data). These weights maximize the *t* statistic (computed after weighted averaging) for contrasting stimuli *i* and *j* in dataset 1. However, because the weights are necessarily somewhat overfitted to dataset 1, the t value from dataset 1 would be positively biased and could not be used to test whether the response patterns contain information discriminating stimuli *i* and *j*. Applying the same weights to the dataset 2 (the test data) and calculating the resulting *t* statistic gives us the linear-discriminant *t* (LD-*t*) value. The LD-*t* is the t value for dataset 2 computed after projection onto the linear discriminant estimated with data set 1. It is a valid t value (t distributed under the null hypothesis of equal response pattern distributions for stimuli *i* and *j*) and can be used to test discriminability of *i* and *j*.

The LD-*t* value is a crossvalidated measure of the discriminability of the two stimuli. Low discriminability could be due to similar responses to the two stimuli or high levels of noise. One can think of the LD-*t* as a crossvalidated variation on the Mahalanobis distance. The mathematical relationship between the Mahalanobis distance and the Fisher linear discriminant contrast (whose division by its standard error yields the LD-*t*) is clarified in Figure S4.

dataset 1 
$$(\mathbf{p2} - \mathbf{p1})^{\mathrm{T}} \mathbf{\Sigma}^{-1} (\mathbf{p2} - \mathbf{p1})$$

dataset 1 
$$(\mathbf{p2} - \mathbf{p1})^{\mathrm{T}} \Sigma^{-1} (\mathbf{p2'} - \mathbf{p1'})$$
 dataset 2

**Figure S4: Relationship between the linear-discriminant** *t* **value and the Mahalanobis distance.** In the Mahalanobis distance, the inverse of the error covariance () is pre- and post-multiplied by the difference vector between the pattern estimates (p1 and p2). If we use pattern estimates from an independent dataset (dataset 2) for the post-multiplication, we obtain the dataset-2 contrast estimate on the Fisher linear discriminant fit with dataset 1. This is because the first part of the definition of the Mahalanobis distance equals the weight vector w of the Fisher linear discriminant. The LD-*t* is the Fisher linear discriminant contrast (as shown) normalized by its standard error (estimated from the residuals of dataset 2 after projection on the discriminant dimension).

For full crossvalidation, we can exchange the two datasets, using dataset 2 for training and dataset 1 for computing the *t* value. We can then average the two *t* values to get a more stable estimate. Although datasets 1 and 2 are independent, the two directions (folds of crossvalidation) are not independent. The average of the *t* values therefore has a standard error which is smaller than 1 (the standard error of a proper *t* value), but larger than √ . In other words, the average *t* is more stable (lower standard error) than a *t* value, but we don't know exactly by what factor. Converting it to a *p* value for inference provides a conservative test for pattern information discriminating individual pairs of stimuli in single subjects.

We can assemble the LD-*t* values for all pairs of stimuli in an LD-*t* RDM. This RDM could contain the LD*t* for the two directions in symmetric positions. However, we will only consider one entry per pair of stimuli (lower-triangular vector of the RDM) and define each entry as the average LD-*t* across the two directions. We can convert this average LD-*t* RDM to a p matrix and control the false-discovery rate or the familywise error rate (Bonferroni) to account for multiple comparisons across pairs of stimuli. This provides a sensitive method for testing many pairs of stimuli for discriminability based on little data per stimulus.

We could consider alternative techniques such as the linear support vector machine (SVM) for estimating the discriminant dimension. Note, however, that a linear SVM discriminant would reduce to the difference vector between *p<sup>i</sup>* and *p*j, unless we have multiple pattern estimates per stimulus. The Fisher linear discriminant is attractive in this context, because it characterizes the shape of the error distribution by a multivariate Gaussian, using a pooled covariance estimate. This approach is particularly attractive for fMRI data, where the errors are usually assumed to be homoscedastic and known to be correlated.

![](_page_27_Figure_2.jpeg)

**Figure S5: Random-effects inference on LD-***t* **RDMs. (A)** Two fMRI datasets were simulated for 20 subjects. We simulated fMRI time-course data Y based on a realistic fMRI design matrix (X) with hemodynamic response predictors for 64 stimuli and patterns (B) with a predefined hierarchical cluster structure (two categories, each comprising two subcategories). The simulated data were Y=XB+E, where E is the time-by-response errors matrix, consisting of Gaussian noise temporally and spatially smoothed by convolution with Gaussians to create realistic degrees of temporal and spatial autocorrelation. The LD-*t* RDMs were computed for each subject and averaged across subjects. The group-average LD-*t* RDM is shown using a percentile color code. **(B)** Inference on LD-*t* RDMs with subject as random effect. LD-*t* analysis can serve the same purpose as classifier decoding analysis, to test for pattern information discriminating two stimuli. For each pair of stimuli, we used a one-sided signedrank test across subjects and obtained a *p* value. The left panel shows the pairs with p < 0.05, uncorrected (red). The middle panel shows the pairs that survive control of the expected false-discovery rate (q < 0.05). The right panel shows the pairs that survive Bonferroni correction (p < 0.05, corrected).

For group analysis, we can average the LD-*t* RDMs and then multiply the average LD-*t* values by √ , where is the number of subjects. Fixed-effects inference can then be performed as for the singlesubject LD-*t* RDM by converting the *t* values to *p* values. Alternatively, we can perform random-effects inference taking advantage of the distribution across subjects (if there are 12 or more). We could use either a single-sample *t* test or the Wilcoxon signed-rank test (Wilcoxon, 1945) to test, for each pair of stimuli, if the average LD-*t* is greater than 0. Figure S5 shows the average LD-*t* RDM for 20 simulated subjects and the results of random-effects inference. The LD-*t* RDM reveals the simulated structure. It provides an interesting alternative to the other pattern dissimilarity measures.

# **References**

- Benjamini, Y., Hochberg, Y. 1995. Controlling the false discovery rate: a practical and powerful approach to multiple testing. Journal of the Royal Statistical Society. Series B (Methodological), 289-300.
- Kriegeskorte, N., Goebel, R., Bandettini, P., 2006. Information-based functional brain mapping. Proceedings of the National Academy of Sciences of the United States of America 103, 3863–3868.
- Kriegeskorte, N., Mur, M., Bandettini, P., 2008. Representational similarity analysis–connecting the branches of systems neuroscience. Frontiers in systems neuroscience 2.
- Ledoit, O., & Wolf, M. (2003). Improved estimation of the covariance matrix of stock returns with an application to portfolio selection. Journal of Empirical Finance, 10(5), 603-621.
- Nichols, T.E., Holmes, A.P. 2002. Nonparametric permutation tests for functional neuroimaging: a primer with examples. Human brain mapping, 15(1), 1-25.
- Wilcoxon, F., 1945. Individual Comparisons by Ranking Methods, Biometrics Bulletin. Vol1, No 60, 80- 83.

**Source code.** The zip file contains the complete RSA toolbox. It also contains demo functions and brainactivity- and behavior-based representational dissimilarity matrices used by the demo functions. DEMO1\_RSA\_ROI\_simulatedAndRealData.m reproduces the figures of the main paper. The toolbox is written in Matlab and requires the Matlab programming environment.

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

<research_source type="scraped_from_research" phase="exploitation" file="new-savanna-the-platonic-representation-hypothesis.md">
<details>
<summary>NEW SAVANNA: The Platonic Representation Hypothesis</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://new-savanna.blogspot.com/2024/05/the-platonic-representation-hypothesis.html>

# NEW SAVANNA: The Platonic Representation Hypothesis

### The Platonic Representation Hypothesis

Minyoung Huh, Brian Cheung, Tongzhou Wang, Phillip Isola, The Platonic Representation Hypothesis, _arXiv_:2405.07987 \[cs.LG\]

> **Abstract:** We argue that representations in AI models, particularly deep networks, are converging. First, we survey many examples of convergence in the literature: over time and across multiple domains, the ways by which different neural networks represent data are becoming more aligned. Next, we demonstrate convergence across data modalities: as vision models and language models get larger, they measure distance between datapoints in a more and more alike way. We hypothesize that this convergence is driving toward a shared statistical model of reality, akin to Plato's concept of an ideal reality. We term such a representation the platonic representation and discuss several possible selective pressures toward it. Finally, we discuss the implications of these trends, their limitations, and counterexamples to our analysis.

You can find a [summary at The Gradient #75](https://thegradientpub.substack.com/p/update-75-schumer-ai-platonic-representation). From the summary:

> What excites me the most about this representational convergence is the ability to share and use data from different modalities for training and inference. It also suggests that multimodal models are better than single-modal ones, given they are grounded in additional modalities and should represent the world in a way that's closer to what the world really is. On the other hand, it is not clear whether a 16% alignment (see one of the figures above) between a set of language and vision models is significant enough to qualify as "convergence." I'm also questioning whether this platonic representation, assuming it does exist, is the endpoint we should pursue, as opposed to what we want the world to be. But that's a whole other ethical debate.
>
> – Jaymee
>
> I am just waiting for the philosophy takes on this paper. But, before we come up with another project and set about trying to determine whether moral realism is a thing based on what AI models seem to be doing, we should probably take stock of a few aspects of what’s going on in the paper. I think a few interesting callouts are section 2.4, where the authors draw on the related point that neural networks seem to show substantial alignment with biological representations in the brain. I also think the three hypotheses presented in section 3 are useful intuition pumps: the Multitask Scaling Hypothesis says if we consider competency at some number of tasks, N, we should expect fewer representations to be competent for all N tasks as N grows larger. You might also expect that models with larger hypothesis spaces to be more likely to find an optimal representation, if one exists in function space—the authors call this the Capacity Hypothesis. Finally, the Simplicity Bias Hypothesis says deep networks are biased towards finding simple fits to the data, and larger models will have a stronger bias.
>
> I think, if you buy what’s being said here, the “our current paradigm is not very efficient” point becomes something like: fairly general architectures without strong inductive biases towards certain sorts of representations (beyond the simplicity bias), scaled up enough and trained to solve a general enough task(s), will have large enough hypothesis spaces that they’ll eventually be pressured to find optimal representations for their data. It is worth noting that datasets and tasks are structured by what we take to be useful and want models to do, and so while I think it might be perfectly fine to posit that there’s a representation (or representations) most useful for those things, calling it a “shared representation of reality” feels a bit grandiose (maybe I’m just being annoying. But, to be fair, you could be a lot more annoying about this paper if you really wanted. I’ll leave doing that as a take-home exercise—imagine you’re Reviewer 2 and have at it). If you’ve heard of projectivism… it seems reasonable to think that “representation of reality” might be projectivism.
>
> All that said, this is a thoughtful and interesting paper. I like the counterexamples and limitations section the authors include at the end, and I think you should read it in full.
>
> Also, for other takes on “universal” representations / representations useful for transfer learning, I had a conversation with Hugo Larochelle some time ago that went into a bunch of his work on this—I expect you’d find a number of his papers on the subject interesting if you liked this one.
>
> —Daniel

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

<research_source type="scraped_from_research" phase="exploitation" file="structure-and-interpretation-of-deep-networks.md">
<details>
<summary>Universality</summary>

Phase: [EXPLOITATION]

**Source URL:** <https://sidn.baulab.info/universality>

# Universality

##### November 19, 2024 • _Philip Yao, Sheridan Feucht_

In this notebook we investigate the representations of neural networks. The
platonic representation hypothesis claims that neural networks are
converging to a shared statistical model of reality in their representation
spaces. We also explore rosetta neurons, which are neurons in different
models that are activated by the same pattern. A critical difference between
these two papers is that the second indicates representations are converging
to the same vectors, while the first paper claims that the similarity of the
representations are converging. Finally, we discuss the idea of inductive
out-of-context reasoning, which is the ability of language models to infer
censored knowledge by piecing together information in disparate training
examples.


## The Platonic Representation Hypothesis

[Paper link](https://arxiv.org/abs/2405.07987)

At time of publication the authors were affiliated as follows:

**Minyoung Huh** MIT PhD

**Brian Cheung** MIT Postdoc

**Tongzhou Wang** MIT PhD

**Phillip Isola** Professor at MIT

"Neural networks, trained with different objectives on different data and
modalities, are converging to a shared statistical model of reality in their
representation spaces."

https://sidn.baulab.info/universality/images/plato1.png

#### Plato’s Allegory of the Cave

People are born and raised in a cave where their heads are chained such that
they can only see shadows of real world objects. The key points are: 1) our
interaction with the physical world is through a projection of the world
onto our senses and 2) there exists an ideal reality which originated these
projections. Similar concepts: phenomenalism, idealism, Donald Hoffman's VR
headset analogy of consciousness.


#### Definitions

```
      The authors only consider vector representation.
      A representation is a function \(f : X → R^n\) that assigns a feature vector to each input in some data domain X .
      A kernel, K : X × X → R, characterizes how a representation measures distance/similarity between datapoints. K(xi, xj ) = ⟨f(xi), f(xj )⟩, where ⟨ · , · ⟩ denotes inner product, xi, xj ∈ X and K ∈ K.
      A kernel-alignment metric, m: K × K → R, measures the similarity between two kernels, i.e., how similar is the distance measure induced by one representation to the distance measure induced by another. Examples include Centered Kernel Distance (CKA) (Kornblith et al., 2019), SVCCA (Raghu et al., 2017), and nearest-neighbor metrics (Klabunde et al., 2023).

```

Throughout the paper, a ML model acts as the representation function, the
kernel measures the similarity between model embedded points and the
kernel-alignment metric measures the similarity between two models based on
how they embed datapoints. The kernel alignment metric used is this:

https://sidn.baulab.info/universality/images/plato_eq.png

#### Past Evidence of similarity of representations between different models:  (not from this paper)

```
    Various works have stitched together portions of a model with portions of a
    different model. If the resultant model performs well then representations
    at the stitching point are similar and compatible. E.g. see "Lenc, K. and
    Vedaldi, A. Understanding image representations by measuring their
    equivariance and equivalence".

    There are some neurons across differing
    vision models were all activated by the same pattern. See the paper on
    Rosetta Neurons.

    Models with similar outputs (e.g., as a result of having
    high performance) also have similar internal activations. See "Balestriero,
    R. and Baraniuk, R. G. A spline theory of deep learning"

```

#### Experiments

##### Alignment appears to increase with model scale and performance.

This has been previously noted in other papers. The paper expands with this
additional experiment
https://sidn.baulab.info/universality/images/plato_exp1.png
"We bin these models based on their average transfer performance on the VTAB
dataset (Zhai et al., 2019), and then measure the average kernel alignment of
the models within each bin. The results indicate that models with high
transfer performance form a tightly clustered set of representations, while
models with weak performance have more variable representations ... This
suggests that models that are competent all represent data in a similar way.
Echoing Bansal et al. (2021) and Tolstoy (1877), we might say: all strong
models are alike, each weak model is weak in its own way"



##### Representations are converging across modalities.

Again, there are works in other papers that implies this. This paper samples
models solely trained either on vision or language and find that the better an
LLM is at language modeling, the more it tends to align with vision models.
For example in the first graph below, language model bloom0.56b has the worst
language performance and also worst alignment to vision model dinov2, while
llama 65b has the best alignment and performance.

https://sidn.baulab.info/universality/images/plato_exp2.png

#### Why is there convergence?

The Multitask Scaling Hypothesis: There are fewer representations that are
competent for N tasks than there are for M < N tasks. As we train more
general models that solve more tasks at once, we should expect fewer
possible solutions.


https://sidn.baulab.info/universality/images/plato_hypothesis1.png

The Capacity Hypothesis: Bigger models are more likely to converge to a
shared representation than smaller models.


https://sidn.baulab.info/universality/images/plato_hypothesis2.png

The Simplicity Bias Hypothesis: Deep networks are biased toward finding
simple fits to the data, and the bigger the model, the stronger the bias.
Therefore, as models get bigger, we should expect convergence to a smaller
solution space.


https://sidn.baulab.info/universality/images/plato_hypothesis3.png

## Rosetta Neurons

[Paper link](https://arxiv.org/abs/2306.09346)

At time of publication the authors were affiliated as follows:

**Amil Dravid** Berkeley PhD

**Yossi Gandelsman** Berkeley PhD

**Alexei A. Efros** Berkeley Professor

**Assaf Shocher** Berkeley Postdoc

The authors define Rosetta Neurons as: "two (or more) neurons in different
models whose activations (outputs) are positively correlated over a set of
many inputs." Their goal is to find neurons which express the same concept
across different models.


https://sidn.baulab.info/universality/images/rose_1.png

The authors find that the number of Rosetta Neurons increases with model
size and performance. They also find that Rosetta Neurons are more likely to
be found in the final layers of the model, which is consistent with the idea
that the final layers of a model are more task-specific and less general.


### Finding these neurons

The author finds rosetta neurons by finding pairs of activations where they
are a kth nearest neighbor of each other. The distance metric they use is
pearson correlation.
https://sidn.baulab.info/universality/images/roseeq.png

### Visualizing the Activation Maps and Rosetta Neurons

In order to visualize the rosetta neurons, the authors take two models: a
discriminator D and a generator G. They first find the activation pairs then
optimize the input vector into the generator such that the similarity between
the activations pairs are maximized.
https://sidn.baulab.info/universality/images/rose_inv.png

The optimization objective is this:
https://sidn.baulab.info/universality/images/roseeq2.png

Where α is a loss coefficient, Lreg is a regularization term (L2 or L1), and
Lact(z, Iv) is the mean of normalized similarities between the paired
activations The authors can also visualize the individual neurons by removing
the sum from the optimization objective.
https://sidn.baulab.info/universality/images/rose4.png

### Editing Images

The authors are able to make images appear zoomed in by doubling the size of
the activation map, shifting images by shifting the activation map, and
duplicating images by duplicating the activation map.
https://sidn.baulab.info/universality/images/rose2.png

## Connecting the Dots

Is it possible for LLMs to infer censored knowledge by piecing together
information in disparate training examples? For example, if we erase
information about synthesizing biological pathogens from a model's training
set, would it be possible for that model to "figure out" how to do this
synthesis itself? In
[this paper](https://arxiv.org/abs/2406.14546), the authors
investigate whether models have the capability to do such a task, which they
dub _inductive out-of-context reasoning_ (OOCR).


### Why care about OOCR?

This is an interesting question to ask, because the degree to which it
matters to you has a lot to do with your worries when it comes to AI safety.
If we are concerned about bad actors getting dangerous information out of
LLMs, OOCR might not be as much of an issue as it would be in scenario where
a rogue LLM rediscovers dangerous information that was hidden from it.


The authors of this paper come from a smattering of institutions, but many
of them describe their research interests as being in AI alignment and
safety. The last author, Owain Evans, is a researcher at UC Berkeley who is
interested in LLM deception. One of the first authors, Johannes Treutlein,
paused his PhD at UC Berkeley to work on alignment stress-testing at
Anthropic; the other, Dami Choi, is working at Transluce in parallel with
her PhD at the University of Toronto.


### Example Task: Locations

The main contribution of this paper is introducing the idea of OOCR and
presenting a suite of five tasks to measure LLMs' OOCR capabilities. Let's
talk about the first task, which illustrates their setup nicely.

https://sidn.baulab.info/universality/images/oocr1.png

What the authors do is fine-tune an LLM on some new task. In this case, they
fine-tune an LLM to predict the distances between unknown city indices (e.g.
"What is the distance between City 19134 and Miami?"). Then at test time,
they query the LLM to see whether it can answer factual questions about
these unknown cities (e.g. "What is a common food enjoyed in City 19134?").
If the model can perform this task successfully, it shows that it has
essentially "figured out" exactly how this unfamiliar City 19134 fits into
its conceptual structure of the world. Crucially, when they ask the model
questions at test time, they do not include any information about City 19134
in the prompt, assuming that the model should have learned some
representation of City 19134 during fine-tuning.


Other tasks that the authors examine include modeling the probabilities of a
biased coin and recovering an underlying function after only seeing that
function's inputs and outputs. All of these kinds of tasks require models to
make a connection between knowledge from pretraining and some
newly-presented information in fine-tuning.


### Evaluation

The authors compare OOCR performance to performance on the same tasks
in-context and find that models do _better_ for OOCR than they do for
ICL. This is also apparent for the city location task (not shown on this
page). They also find that GPT-4 does better than GPT-3.5 on OOCR tasks.

https://sidn.baulab.info/universality/images/icloocr.png

For the task where models have to recover an underlying function, the
authors use a few methods to evaluate a model's OOCR capabilities at test
time:


- Free-form responses: "What function does `f1` compute?"
- Language: Multiple-choice response to the question "What function does
`f1` compute?"

- Composition: Import `f1` and `f2` and query for the
composition of those functions.

- Inversion: Given the output of a function, output a possible corresponding
input value.


GPT-3.5 does the best on the multiple-choice task, with a striking 74%
accuracy in correctly guessing the function that a symbol corresponds to.



## (Bonus) Language Models as Agent Models

[This paper](https://arxiv.org/abs/2212.01681) by Jacob Andreas,
a computer science professor at MIT, provides a really interesting way of
thinking about what LLMs are doing when they model internet text. In
particular, he claims that


1. Modern LMs can infer approximate representations of the
    _beliefs, desires, and intentions_ of the agent that produced the
    text it is modeling.

2. These inferred representations are causally linked to the model's
    predictions, meaning that they have the same relationship to the text that
    the agent's original intentions did.


Importantly, this is not the same thing as saying that LLMs have
_beliefs, desires, and intentions_ of their own. Rather, it argues that
the process of modeling internet text benefits greatly from an ability to
model the agents that generated that text (e.g., modeling disagreeing
commenters, fictional characters in a dialogue, or opinionated essayists).


This paper is a fun read and definitely worth checking out if you are
interested in this overall question of how deeply LLMs (and other models)
"understand" the processes that they are modeling.


## Code Examples

Here are the some code examples for the Rosetta Neurons:
[Visualizing Pairwise Matches](https://colab.research.google.com/drive/1ihk4ewUtMj5GARP5hzFUZZB-7MXcomUY?usp=sharing)

[Visualizing Rosetta Neurons](https://colab.research.google.com/drive/1-b0njXs65guzb3OS2GaS0VTzDdI6Wlvn?usp=sharing)

Additional code exmaples:
[Platonic Representation Hypothesis Github Code Demo](https://github.com/minyoungg/platonic-rep)

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