<digest_meta>
  <article_title>Distinct_AI_Models</article_title>
  <total_sources>5</total_sources>
  <total_artefacts>24</total_artefacts>
  <tavily_saturation>0.905</tavily_saturation>
  <n_orphan_anchors>30</n_orphan_anchors>
  <n_content_sections>4</n_content_sections>
  <external_evidence_policy>allowed</external_evidence_policy>
</digest_meta>

<artefact_registry>
| ID | Source | Type | Topic | Lines | Preview |
|----|----|----|----|----|----|
</artefact_registry>

<sources>
<s slug="Better Together _ Leveraging Unpaired Multimodal Data for Stronger Unimodal Models" type="exploitation">UML (Unpaired Multimodal Learner) is a modality-agnostic framework that improves unimodal representations by alternately processing unpaired samples from auxiliary modalities (text, audio, images) through shared network weights. The core assumption is that modalities are projections of a shared latent reality \(Z^*\); weight sharing accumulates gradients on common parameters without pairings, surrogate losses, or inferred alignments. Under linear data-generating assumptions, each modality decomposes as \(X_i = A_{c,i}\theta_c + A_{x,i}\theta_x + \epsilon\) and \(Y_j = B_{c,j}\theta_c + B_{y,j}\theta_y + \epsilon\). Theorems 1–3 prove that unpaired \(Y\) samples strictly increase Fisher information on shared factors \(\theta_c\) (Loewner ordering \((I_X + I_Y)_{\theta_c,\theta_c} \succ (I_X)_{\theta_c,\theta_c}\)) and can outperform equal numbers of additional \(X\) samples when ranges differ, yielding directional variance reduction and an effective exchange rate below one. Two training regimes are defined: UML-SSL uses modality-specific decoders with next-token/patch prediction loss on a shared autoregressive transformer; UML-Sup uses a shared classifier head on labeled unpaired data. At inference only the target-modality pathway remains. The method extends to three modalities by adding further heads. Empirical results use ViT-S/14 DINOv2, OpenLLaMA-3B, AudioCLIP (ES-ResNeXT), CLIP encoders, and BERT initialization for ViT. Datasets include MultiBench (CMU-MOSEI, CMU-MOSI, UR-FUNNY, MUSTARD, MIMIC-III), ImageNet, Stanford Cars, FGVC Aircraft, Oxford-Pets, UCF101, and ImageNet-ESC-19/27. Gains appear in full fine-tuning, \(k\)-shot linear probing (\(k=1,2,4,8,16\)), distribution-shift robustness (ImageNet-V2/Sketch/A/R), and audio classification; three-modality combinations compound improvements. Exchange rates are quantified as 1 image \(\approx\) 228 words (CLIP) versus 1034 words (DINOv2+OpenLLaMA) on Oxford-Pets isolines. Analyses reveal emergent multimodal neurons with high vision-text activation correlations despite no pairing. The source includes tables on dataset statistics, hyperparameter grids, linear-probing results, and further related work. Limitations: evaluations focus on classification; generation and text-target tasks remain untested.</s>
<s slug="GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT" type="exploitation">Representational alignment quantifies agreement between internal representations of information-processing systems (humans, animals, DNNs) across cognitive science, neuroscience, and machine learning. The source reviews literature showing duplicated efforts due to absent shared terminology, then proposes a unifying framework of five controllable components—data (static stimulus sets \(\mathcal{D}\)), systems (functions \(f_\theta, g_\phi\)), measurements (\(\mu_\alpha, \nu_\beta\)), embeddings (\(\varphi_\psi, \chi_\omega\)), and alignment function \(\delta\)—plus three objectives: measuring similarity, bridging spaces, and increasing alignment. Key techniques include Representational Similarity Analysis (RSA) with Representational Dissimilarity Matrices (RDMs) and rank correlations (Kendall’s \(\tau_a\), Spearman \(\rho_a\)); hyperalignment via Procrustes transforms; shared response modeling; linear encoding models; knowledge distillation (Hinton et al., 2015) matching soft labels, geometries, or pairwise similarities; contrastive objectives (CLIP); and INDSCAL/MDS on similarity judgments. Concrete studies cited are Kriegeskorte et al. (2008b) establishing human–macaque IT homology via RSA on object images; Muttenthaler et al. (2023a,b) showing linear transforms raise human–CNN alignment and few-shot performance; Sucholutsky & Griffiths (2023) reporting a U-shaped relationship between teacher–student alignment and transfer; Jacoby et al. (2021a) cross-cultural rhythm biases across 39 groups; and Yamins et al. (2014) hierarchical DNN–brain correspondence in vision. The framework supports claims that static paired data suffice for measurement while dynamic systems and unpaired data appear in bridging/increasing settings, and that descriptive (non-differentiable) versus differentiable \(\delta\) functions distinguish measurement from optimization. Includes Figure 2 visualizing the five-component pipeline and three objectives, plus Table 2 mapping diverse studies onto the formalism. Limitations noted are restriction to static stimuli (no environment interaction), omission of intrinsic objectives or output mappings, and absence of concrete implementation code or benchmarks for cross-disciplinary transfer.</s>
<s slug="Harnessing the Universal Geometry of Embeddings" type="exploitation">vec2vec learns unsupervised translations between text embedding spaces produced by distinct models (different architectures, training data, output dimensions) by mapping inputs into a shared latent space. The method rests on the Strong Platonic Representation Hypothesis: networks trained on the same modality and objective converge to a universal latent geometry that can be recovered without paired data or encoder access. The architecture uses input adapters \(A_1, A_2 : \mathbb{R}^d \to \mathbb{R}^Z\), a shared MLP backbone \(T\) with residual connections, layer normalization and SiLU activations, and output adapters \(B_1, B_2\). Translation functions are \(F_1 = B_2 \circ T \circ A_1\) and \(F_2 = B_1 \circ T \circ A_2\). Optimization combines adversarial GAN losses at both embedding and latent levels with three generator terms: \(\ell_2\) reconstruction, cycle-consistency, and vector-space preservation (VSP) that matches pairwise cosine distances after translation. Experiments train on disjoint 1 M 64-token sequences from Natural Questions and evaluate on 65 536 held-out NQ texts plus out-of-distribution sets (TweetTopic 800 tweets, MIMIC-III 8 192 records, Enron 50 emails). Models tested include GTE, GTR, E5, Granite, CLIP and Qwen. Translation quality reaches mean cosine similarity 0.92, top-1 accuracy 100 % and mean rank 1 on same-backbone pairs; cross-backbone pairs still exceed optimal-transport baselines by large margins. On OOD data the same translators retain high similarity and low rank. Zero-shot attribute inference on translated embeddings matches or exceeds an oracle baseline that uses ground-truth embeddings in the target space; zero-shot inversion via the method of [67] recovers usable content for up to 80 % of Enron emails and 67 % of tweets, revealing names, dates and medical conditions. Ablations confirm that removing any loss term collapses performance; training remains possible with as few as 10 k–50 k source embeddings. Separate runs demonstrate translation involving CLIP (multimodal) and Qwen (14× larger). The source includes Table 3 (OOD results on TweetTopic/MIMIC), Table 6 (loss-component ablation) and Table 7 (data-scale ablation). Limitations noted are GAN training instability requiring multiple seeds, reduced stability on cross-backbone pairs, and the fact that all reported numbers constitute a lower bound pending more robust optimization.</s>
<s slug="Layers at Similar Depths Generate Similar Activations" type="exploitation">The source examines structural similarities in latent spaces across independently trained LLMs by analyzing nearest neighbor relationships induced by activations at different layers. Main claims are that activations at different depths within one model induce distinct nearest neighbor sets (Claim 1), while layers at proportionally corresponding depths across models induce similar sets (Claim 2). These are formalized via embedding functions \(f_M^{(\ell)}\) extracting final-token activations from decoder modules, the mutual \(k\)-NN similarity measure \(\mathcal{M}_k^{(\mathcal{D})}(f,g)\) (with cosine distance and \(k=10\)), and \(n_1 \times n_2\) affinity matrices \(A_{i,j} = \mathcal{M}_{10}^{(\mathcal{D})}(f_{M_1}^{(i)}, f_{M_2}^{(j)})\). Diagonal structure in these matrices (quantified via a generalized diagonal region and tested with moving-block bootstrap of size \(5 \times 5\)) indicates a shared progression of activation geometries, stretched or compressed to fit differing layer counts. Experiments use 2048 texts sampled from OpenWebText, with concrete cases such as the prompt "Training For Ice and Mixed Climbing Series brought to you by Furnace Industries continues..." whose 10-NN sets agree on 7/10 elements between Llama-3.1-8B layer 10 and Gemma-2-9B layer 20, and on 6/10 elements between Llama-3.1-8B layer 30 and Gemma-2-9B layer 40. The study covers 24 open-weight models (1B–70B parameters) from Gemma Team, Meta, Mistral, Microsoft, and TII; includes a table listing 24 models with their layer counts and instruction tuning status. Additional datasets tested are IMDB, OPUS Books (English/German), IFEval, MMLU, Wikipedia lead paragraphs, and random alphanumeric strings. Code is released at https://github.com/chriswolfram/unireps. Statistical results include maximum naive \(t\)-test \(p\)-value \(8 \times 10^{-7}\) and block-bootstrap \(p\)-value \(4.84 \times 10^{-3}\) across all model pairs; absolute mutual \(k\)-NN scores exceed the derived hypergeometric null distribution (concentrated near 0.02 for \(|\mathcal{D}|=2048\)). Diagonal structure persists for web-text distributions and other \(k\) values but disappears for random strings; instruction tuning reduces late-layer similarity on IFEval inputs. Limitations include restriction to decoder-end activations, reliance on a single similarity measure (mutual \(k\)-NN), and sensitivity of observed structure to input distribution.</s>
<s slug="Revisiting Model Stitching to Compare Neural Representations" type="exploitation">Model stitching connects bottom layers of one frozen trained network to top layers of another via a low-capacity trainable stitching layer (e.g., 1×1 convolution plus BatchNorm for CNNs; token-wise linear for transformers) and measures the resulting stitching penalty as the increase in task loss (CIFAR-10 or ImageNet error) relative to the base top model. The source defines stitching formally as \(\mathcal{L}_\ell(r;A)=\inf_{s\in\mathcal{S}}\mathcal{L}(A_{>\ell}\circ s\circ r)\), shows it distinguishes task-relevant from spurious features, is asymmetric, supplies interpretable loss units, and admits controlled invariances, unlike symmetric similarity metrics. It contrasts stitching with CKA, SVCCA, and PWCCA, noting that CKA cannot detect “better” representations or ignore irrelevant coordinates. Key experiments use ResNet-18 (CIFAR-10) and ResNet-50 (ImageNet) trained with SGD, plus Myrtle-CNN, Vision Transformer (timm library on CIFAR-5m), SimCLR, SwAV, and DINO. Networks with different random seeds, disjoint data subsets, supervised vs. self-supervised objectives, coarse vs. noisy labels, varying widths {0.25×,1×,2×}, sample sizes {5K,10K,25K}, and epochs {40,80,160} are shown to be stitching-connected at every layer with near-zero penalty, supporting the “Anna Karenina” claim that successful models converge to compatible internal representations. “More is better” is quantified by negative stitching penalties when higher-data, wider, or longer-trained bottom representations replace weaker ones. Includes a 3-line table (ARTEFACT_A24) summarizing qualitative agreement and divergence between stitching and CKA across initialization, task, and scale axes. Stitching connectivity is positioned as complementary to mode connectivity; random-network controls and fine-tuning ablations confirm the stitching layer does not simply learn arbitrary mappings. Notable limitations include restriction to vision tasks, computational cost of training a stitcher versus CKA, and the need for architecture-matched stitching families when architectures differ.</s>
</sources>

<tavily_yield_per_section>
| section_id | helping_rounds | unique_facts | duplicate_facts |
|---|---|---|---|
| S1::section-1-introduction | 3 | 10 | 0 |
| S2::section-2-the-company-being-kept | 3 | 9 | 0 |
| S3::section-3-convergent-evolution | 1 | 8 | 0 |
| S4::section-4-find-the-universals | 2 | 7 | 0 |
tavily_saturation=0.905
</tavily_yield_per_section>

<section_coverage>
<section id="S1::section-1-introduction" self_contained="no" sources="Revisiting Model Stitching to Compare Neural Representations,Layers at Similar Depths Generate Similar Activations,GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT" artefacts="">
  <intent>Introduce the Platonic representation hypothesis via a colloquial multimodal example and its philosophical roots while summarizing early empirical findings on representational convergence.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT"/>
    <item name="theoretical_foundations" present="yes" evidence="GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT"/>
    <item name="technical_nuances" present="yes" evidence="Layers at Similar Depths Generate Similar Activations"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="Revisiting Model Stitching to Compare Neural Representations"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="3">
    <item name="adjacent_concepts" present="yes" evidence="GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT"/>
    <item name="cross_domain_analogies" present="yes" evidence="GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT"/>
    <item name="historical_context" present="yes" evidence="GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT"/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="5" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Start the section by raising a short colloquial example of abstract semantic representation of the word - "dog": One rea" bullet="motivation">Requires motivational framing example absent from sources.</orphan>
    <orphan route="depth" anchor="Following the above opening example, make a distinction that the AI systems are unlike humans who are naturally capable" bullet="motivation">Human vs model distinction needs expansion from source material.</orphan>
    <orphan route="depth" anchor="Researchers investigate such questions by peering inside AI systems and studying how they represent scenes and sentences" bullet="theoretical_foundations">Key findings statements require source-backed citations.</orphan>
    <orphan route="depth" anchor="Formally introduce the Platonic representation hypothesis by first briefly explaining the original allegory by Plato, th" bullet="theoretical_foundations">Philosophical adaptation requires explicit Plato reference.</orphan>
    <orphan route="depth" anchor="Enumerate the main points of contention surrounding the hypothesis involving the definition of representations and the m" bullet="limitations_failure_modes">Contention points match source-noted definitional and methodological issues.</orphan>
    <orphan route="depth" anchor="Transition to Section 2: Having framed the Platonic representation hypothesis and its philosophical roots, we transition" bullet="motivation">Transition sentence is structural gap addressable by depth elaboration.</orphan>
  </orphan_anchors>
</section>
<section id="S2::section-2-the-company-being-kept" self_contained="no" sources="Harnessing the Universal Geometry of Embeddings,Layers at Similar Depths Generate Similar Activations,GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT" artefacts="">
  <intent>Explain geometric comparison of representations via relational geometry and similarity-of-similarities, anchored in Firth’s principle and Anna Karenina pattern.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="Harnessing the Universal Geometry of Embeddings"/>
    <item name="theoretical_foundations" present="yes" evidence="GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT"/>
    <item name="technical_nuances" present="yes" evidence="Layers at Similar Depths Generate Similar Activations"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="Harnessing the Universal Geometry of Embeddings"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT"/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="5" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="By first referencing to "All is number." by Plato's predecessor Pythagoras, explain that neural network representations" bullet="theoretical_foundations">Pythagorean framing and high-dimensional vector explanation required.</orphan>
    <orphan route="depth" anchor="Introduce the geometric basis for comparison: when vectors for the same concept point in similar directions across two i" bullet="technical_nuances">Geometric alignment details need source elaboration.</orphan>
    <orphan route="depth" anchor="Apply Firth's linguistic principle (quoting him "you shall know a word by the company it keeps") directly to representat" bullet="theoretical_foundations">Firth quote application is coverage gap.</orphan>
    <orphan route="depth" anchor="Detail the technique of measuring similarity of similarities: instead of trying to rotate one model's embedding space in" bullet="technical_nuances">Similarity-of-similarities technique requires Sucholutsky quote and detail.</orphan>
    <orphan route="depth" anchor="Contrast the Anna Karenina scenario: all successful, high-performing models converge toward the same representational ge" bullet="case_studies_metrics">Anna Karenina pattern needs stitching paper citations.</orphan>
    <orphan route="depth" anchor="Note that the earliest representational similarity research focused on comparing different vision models (different CNN" bullet="historical_context">Early vision-model focus requires explicit historical note.</orphan>
    <orphan route="depth" anchor="Transition to Section 3: With these measurement tools in hand, we can now look at the hierarchy of experimental evidence" bullet="motivation">Transition sentence is structural depth gap.</orphan>
  </orphan_anchors>
</section>
<section id="S3::section-3-convergent-evolution" self_contained="no" sources="Better Together _ Leveraging Unpaired Multimodal Data for Stronger Unimodal Models,Revisiting Model Stitching to Compare Neural Representations,GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT" artefacts="">
  <intent>Present hierarchy of convergence evidence from identical-data to cross-modal settings and describe Huh’s cross-modal experimental design.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="Better Together _ Leveraging Unpaired Multimodal Data for Stronger Unimodal Models"/>
    <item name="theoretical_foundations" present="yes" evidence="GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT"/>
    <item name="technical_nuances" present="yes" evidence="Revisiting Model Stitching to Compare Neural Representations"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="Better Together _ Leveraging Unpaired Multimodal Data for Stronger Unimodal Models"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="Revisiting Model Stitching to Compare Neural Representations"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="GETTING ALIGNED ON REPRESENTATIONAL ALIGNMENT"/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="5" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Frame the existential question that dominated the LLM scaling era: starting with the backfdrop - early 2023 when ChatGPT" bullet="motivation">Scaling-era existential framing and Huh quote required.</orphan>
    <orphan route="depth" anchor="Present the hierarchy of potential convergence evidence in increasing order of strength that would be in favor of the re" bullet="theoretical_foundations">Hierarchy of evidence ordered by strength needs source backing.</orphan>
    <orphan route="depth" anchor="State that, a year after Isola and his colleagues' discussion, they decide to write a paper reviewing the evidence of an" bullet="historical_context">Paper-writing timeline is coverage gap.</orphan>
    <orphan route="depth" anchor="After citing various researches by then, describe the core experimental design by Huh used to test cross-modal convergen" bullet="case_studies_metrics">Huh experimental design description requires expansion.</orphan>
    <orphan route="depth" anchor="Transition to Section 4: After reviewing the evidence for convergence, we must examine a host of experimental choices wi" bullet="motivation">Transition sentence is structural depth gap.</orphan>
  </orphan_anchors>
</section>
<section id="S4::section-4-find-the-universals" self_contained="no" sources="Better Together _ Leveraging Unpaired Multimodal Data for Stronger Unimodal Models,Revisiting Model Stitching to Compare Neural Representations,Layers at Similar Depths Generate Similar Activations" artefacts="">
  <intent>Catalog experimental degrees of freedom, present contrasting scientific attitudes (Isola vs Efros), and surface practical payoffs alongside model-complexity tensions.</intent>
  <depth_checklist depth_score="5">
    <item name="motivation" present="yes" evidence="Better Together _ Leveraging Unpaired Multimodal Data for Stronger Unimodal Models"/>
    <item name="theoretical_foundations" present="yes" evidence="Layers at Similar Depths Generate Similar Activations"/>
    <item name="technical_nuances" present="yes" evidence="Revisiting Model Stitching to Compare Neural Representations"/>
    <item name="latest_advancements" present="no" evidence=""/>
    <item name="limitations_failure_modes" present="yes" evidence="Better Together _ Leveraging Unpaired Multimodal Data for Stronger Unimodal Models"/>
    <item name="implementation_tradeoffs" present="no" evidence=""/>
    <item name="case_studies_metrics" present="yes" evidence="Revisiting Model Stitching to Compare Neural Representations"/>
    <item name="artefact_available" present="no" evidence=""/>
  </depth_checklist>
  <breadth_checklist breadth_score="2">
    <item name="adjacent_concepts" present="yes" evidence="Layers at Similar Depths Generate Similar Activations"/>
    <item name="cross_domain_analogies" present="no" evidence=""/>
    <item name="historical_context" present="yes" evidence="Revisiting Model Stitching to Compare Neural Representations"/>
    <item name="enabling_technologies" present="no" evidence=""/>
    <item name="industry_applications" present="no" evidence=""/>
    <item name="adjacent_trends" present="no" evidence=""/>
  </breadth_checklist>
  <orphan_anchors n_depth="6" n_breadth="0" n_unreachable="0">
    <orphan route="depth" anchor="Catalog the experimental degrees of freedom that complicate strong claims of convergence: choice of which layer to compa" bullet="technical_nuances">Degrees-of-freedom catalog matches source-noted measurement choices.</orphan>
    <orphan route="depth" anchor="Present the critique by Christopher Wolfram on the generalizability of results test on one dataset." bullet="limitations_failure_modes">Wolfram critique on dataset generalizability is direct coverage need.</orphan>
    <orphan route="depth" anchor="Contrast two complementary scientific attitudes by citing quotes explicitly: one (associated with Isola) that actively s" bullet="theoretical_foundations">Isola vs Efros attitude contrast requires explicit quotes.</orphan>
    <orphan route="depth" anchor="Highlight the immediate practical payoffs that exist even with only partial alignment: the ability to translate represen" bullet="implementation_tradeoffs">Practical payoffs paragraph needs source-supported examples.</orphan>
    <orphan route="depth" anchor="Surface the tension between elegant Platonic explanations and the irreducible complexity of trillion-parameter systems (" bullet="limitations_failure_modes">Clune tension quote and complexity discussion required.</orphan>
    <orphan route="depth" anchor="Because this is the final section there is no transition paragraph." bullet="motivation">Final-section instruction is structural.</orphan>
  </orphan_anchors>
</section>
</section_coverage>

<gap_profile>
  <section id="S1::section-1-introduction" need_depth="18" need_breadth="3" target_words="550" mandatory_bullets="6" must_cover_depth="3" must_stay_brief="1"/>
  <section id="S2::section-2-the-company-being-kept" need_depth="18" need_breadth="4" target_words="650" mandatory_bullets="7" must_cover_depth="3" must_stay_brief="0"/>
  <section id="S3::section-3-convergent-evolution" need_depth="18" need_breadth="4" target_words="350" mandatory_bullets="5" must_cover_depth="3" must_stay_brief="1"/>
  <section id="S4::section-4-find-the-universals" need_depth="21" need_breadth="4" target_words="450" mandatory_bullets="5" must_cover_depth="4" must_stay_brief="0"/>
  <overall>
    <weakest_sections>S3::section-3-convergent-evolution, S4::section-4-find-the-universals</weakest_sections>
    <strongest_sections>S1::section-1-introduction, S2::section-2-the-company-being-kept</strongest_sections>
    <dominant_gap_type>depth</dominant_gap_type>
    <exploration_insight>[computed from deterministic gap profile]</exploration_insight>
  </overall>
</gap_profile>