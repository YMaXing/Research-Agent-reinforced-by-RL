# Research

<research_source type="tavily_results" phase="exploration">
## Research Results

<details>
<summary>What causal inference techniques isolate effects in confounded AI optimization experiments?</summary>

Phase: [EXPLORATION]

### Source [55]: https://link.springer.com/chapter/10.1007/978-981-95-6465-1_8

Query: What causal inference techniques isolate effects in confounded AI optimization experiments?

Answer: inference include regression analysis, propensity score matching (PSM), instrumental variables (IVs), regression discontinuity, and difference-in-differences (DID) (Angrist and Pischke 2014; Chen et al. 2021; Chen 2022). Regression analysis adjusts for observable confounding variables using statistical control strategies, whereas PSM creates a quasi-experimental design by balancing covariate distributions between treatment and control groups. IVs leverage exogenous tools to isolate variation in explanatory variables, whereas regression discontinuity uses institutional thresholds to establish quasi-randomization conditions. Finally, DID eliminates time-invariant confounders by comparing changes over time. Collectively, these methods reconstruct counterfactual inference frameworks using [...] Reliance on Strong Assumptions: Most causal inference methods depend on assumptions that are difficult to verify or satisfy, such as assumptions regarding relevance and exogeneity of IVs, local randomization in regression discontinuity, parallel trends in DID, and conditional independence assumption in PSM. These assumptions limit the applicability of these methods.

Covariate Limitations: Traditional causal inference methods rely on precise control of covariates to accurately isolate causal effects. Missing key covariates can introduce confounding bias, negatively affecting the identification of causal effects. By contrast, including too many covariates can lead to the “curse of dimensionality,” increasing model complexity and resulting in unstable parameter estimates. [...] mitigating confounding effects (note that DML principles will be introduced in Chapter 9). When observable confounders are not satisfied, machine learning can complement causal estimation methods by fitting data before and after the cutoff for regression discontinuity or by improving two-stage estimation for IVs through deep learning.

-----

Phase: [EXPLORATION]

### Source [56]: https://pmc.ncbi.nlm.nih.gov/articles/PMC11658928

Query: What causal inference techniques isolate effects in confounded AI optimization experiments?

Answer: Fourth, in a sequential randomised experiment, standard methods such as regression adjustment, statistical structural equation models and multi-level models will often fail to yield unbiased estimands (Bulbulia, 2024a; Richardson & Robins, 2013; Young et al., 2014). Special estimators such as ‘g-methods’ (Hernán & Robins, 2024) or targeted learning (Van Der Laan & Rose, 2018) may be necessary to recover per-protocol effects in sequential designs. The requirements for estimating per-protocol effects in experiments cannot be stated in isolation from the details of each study (Hernán & Robins, 2024; Robins, 1986). [...] sequential treatments, collect data for adherence (where possible).For sequential treatments, at each measurement interval, ensure covariate data collection for any variable that might affect adherence or that might be proxies for such variables, particularly if these variables, or proxies for these variables, might affect outcomes at the end of the study.Do not infer per-protocol effects from the portion of the sample that followed experimental protocols. Such selection can lead to differences between the study population at the start and end, compromising external validity.Where possible, report both the per-protocol effect and the intention-to-treat effect.Describing the specialised methods for estimating per-protocol effects with multiple sequential treatments is beyond the scope of [...] an intention-to-treat or per-protocol effect. They should do this in addition to stating a causal contrast, effect measure and target population (Hernán, 2004; Tripepi et al., 2007) and to evaluating sources of measurement error bias (Bulbulia, 2024b).

-----

Phase: [EXPLORATION]

### Source [58]: https://www.statsig.com/perspectives/causal-inference-in-product-experimentation

Query: What causal inference techniques isolate effects in confounded AI optimization experiments?

Answer: So what do we do when RCTs aren't feasible? Alternative methods like quasi-experiments and instrumental variables can come to the rescue. Quasi-experiments compare naturally occurring groups using techniques like difference-in-differences and regression discontinuity. Instrumental variables, on the other hand, involve a third variable that affects the treatment but not the outcome directly. This allows us to estimate causal effects even when we can't measure all confounders.

Observational studies also have their place in inferring causality. Using statistical adjustments, methods like propensity score matching and inverse probability weighting help control for confounding variables in observational data. These techniques aim to mimic the balance we'd get through randomization. [...] Applying these techniques isn't without challenges, of course. We need to carefully consider things like selection bias, confounding variables, and external validity. Strategies like matching, stratification, and statistical adjustments help us tackle these hurdles, ensuring our conclusions are reliable. At Statsig, we emphasize rigorous experiment design, appropriate methods, and thoughtful interpretation to make the most of causal inference.

## Closing thoughts [...] ## Practical applications and best practices

Designing effective experiments with causal inference starts with defining clear research questions, selecting the right metrics, ensuring our groups are comparable, collecting enough data, and accounting for confounders. When randomization isn't possible, quasi-experimental designs can step in, comparing naturally occurring groups with different exposures. Similarly, instrumental variables help estimate causal effects in scenarios like pricing strategies.

-----

Phase: [EXPLORATION]

### Source [59]: https://telnyx.com/learn-ai/casual-inference-explained

Query: What causal inference techniques isolate effects in confounded AI optimization experiments?

Answer: ## Causal inference in machine learning

Standard supervised learning optimizes for predictive accuracy. Causal machine learning optimizes for accurate counterfactuals: what would have happened under a different treatment.

This shift has practical consequences. A predictive model in healthcare might identify which patients are likely to be readmitted. A causal model identifies which interventions actually reduce readmission. The first ranks patients. The second changes outcomes.

Methods such as causal forests, double machine learning, and meta-learners are now standard tools for estimating treatment effects in high-dimensional data. They are increasingly built into inference pipelines for production AI systems.

## Why causal inference matters for AI agents [...] When randomization is not possible, researchers turn to observational methods such as propensity score matching, instrumental variables, and difference-in-differences.

Across all three designs, researchers use directed acyclic graphs (DAGs) to make their causal assumptions explicit.

A DAG is not a study design itself, but a representational tool for showing which variables affect which, and therefore which variables must be controlled for to avoid bias.

Several assumptions underpin most causal inference work:

Violating these assumptions produces biased estimates, regardless of how sophisticated the statistical method.

This is why methodology often matters more than model complexity, a point worth remembering as LLMs are increasingly applied to decision-making tasks. [...] ## Why causal inference matters for AI agents

AI agents that take actions in the real world face causal questions constantly. An agent deciding whether to escalate a request, a system choosing between scripts, a model selecting contact times, all of these are causal decisions.

Predictive models tell the agent what is likely to happen. Causal inference tells the agent what to do about it.

That shift, from AI as advisor to AI as decision-maker, is what raises the stakes for causal reasoning. Modern causal inference rests on two dominant frameworks: Donald Rubin's potential outcomes approach and Judea Pearl's structural causal models.

-----

</details>

<details>
<summary>How does information theory quantify noise reduction in granular binary AI metrics?</summary>

Phase: [EXPLORATION]

### Source [60]: https://arxiv.org/html/2602.07168

Query: How does information theory quantify noise reduction in granular binary AI metrics?

Answer: Information theory quantifies noise reduction using mutual information, which measures the statistical dependence between input and output data, minimizing noise preserves mutual information. Entropy assesses the spread of data, with lower entropy indicating less noise. Noise reduction enhances mutual information and reduces entropy. Overall, post-processing should aim to minimise noise and artefacts while preserving or enhancing mutual information between the reconstruction and the original structure. Entropy analysis provides a consistent framework to assess the quality and cost of each enhancement step, supporting decisions about which processing methods offer the greatest information return. Noise directly modulates the information metrics introduced in Section 2. Entropy is inflated by random fluctuations that increase the spread of grey-level distributions, raising entropy values even when no additional structural information is present [3, 1]. Structured artefacts further distort entropy by embedding false patterns that mimic structural variability. From the perspective of mutual information, noise reduces the statistical dependence between acquired and reference data. Poisson and Gaussian components act to randomise pixel values, lowering the overlap in joint probability distributions between input and reconstructed datasets [1, 17]. Structured artefacts are particularly detrimental, as they can decrease mutual information even while raising entropy, indicating that

-----

Phase: [EXPLORATION]

### Source [62]: https://vinvashishta.substack.com/p/an-information-theory-approach-to

Query: How does information theory quantify noise reduction in granular binary AI metrics?

Answer: There’s noise, entropy, or uncertainty in the communications between a person and an LLM. My personal writing style is one region where the LLM has learned some information, proven by the LLM’s reasoning log, but not enough information to simulate my writing style. In my level 1 experiment, there remained too much uncertainty to fully meet my intent and deliver my outcome. AI evaluations must focus on assessing how well a model or agent can: 1. Detect an intent from an unstructured input 2. Determine the appropriate outcome 3. Create a path to that outcome 4. Implement it to deliver the outcome. My approach has deep roots in information theory. When information structures and AI don’t address uncertainty, we can’t trust the output.

-----

</details>

<details>
<summary>How do Six Sigma quality gates inform binary criteria design for AI evaluations?</summary>

Phase: [EXPLORATION]

### Source [65]: https://www.softwareseni.com/building-quality-gates-for-ai-generated-code-with-practical-implementation-strategies

Query: How do Six Sigma quality gates inform binary criteria design for AI evaluations?

Answer: Quality gates are automated checkpoints in the development lifecycle that enforce predefined standards for code quality, security, and performance. They operate as pass/fail criteria applied consistently across every pull request and deployment. For AI-generated code, quality gates address issues like high complexity or security vulnerabilities that AI might introduce despite functional outputs. They can be implemented via pre-commit hooks, pull request checks including linting and security scans, and CI/CD pipelines. This systematic approach prevents technical debt by enforcing standards automatically rather than relying on manual reviews.

-----

Phase: [EXPLORATION]

### Source [66]: https://www.codecentric.de/en/knowledge-hub/blog/evaluating-machine-learning-models-quality-gates

Query: How do Six Sigma quality gates inform binary criteria design for AI evaluations?

Answer: Quality gates can be integrated at various points in a pipeline with predefined success criteria checked automatically. They help stop machine learning pipelines early if criteria are not met to save resources. Data quality gates ensure training on meaningful data by checking raw data against assumptions. For model predictions, numerical metrics on test sets are used as automatically evaluable criteria to evaluate quality.

-----

Phase: [EXPLORATION]

### Source [67]: https://www.qualitymag.com/articles/98430-beyond-dmaic-leveraging-ai-and-quality-40-for-manufacturing-innovation-in-the-fourth-industrial-revolution

Query: How do Six Sigma quality gates inform binary criteria design for AI evaluations?

Answer: Binary classification of quality in manufacturing involves labeling data samples as 'good' or 'defective' based on predefined criteria from sensors and devices. This uses features like temperature or images for classification. AI enhances this beyond traditional Six Sigma DMAIC by handling real-time data and continuous adaptation in complex environments.

-----

</details>

<details>
<summary>What decision theory principles from clinical trials apply to AI eval thresholds?</summary>

Phase: [EXPLORATION]

### Source [68]: https://www.gov.il/BlobFolder/generalpage/principles-evaluation-ai-interventional-clinical-trials/he/files_publications_drugs_Principles-Evaluation-AI-Based-Interventional-Clinical-Trials-en.pdf

Query: What decision theory principles from clinical trials apply to AI eval thresholds?

Answer: Decision theory principles for AI evaluation in clinical trials include setting clinically relevant decision thresholds, using net benefit analysis, and ensuring external validation in target environments. These principles help ensure AI algorithms perform effectively and safely in real-world clinical settings.

-----

Phase: [EXPLORATION]

### Source [69]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7909857

Query: What decision theory principles from clinical trials apply to AI eval thresholds?

Answer: A threshold is then applied to convert it into a binary result. The sensitivity and specificity of the AI algorithm vary depending on how the threshold is set. If the threshold is set high, sensitivity decreases and specificity increases. If the threshold is set low, the sensitivity increases and the specificity decreases. A receiver operating characteristic (ROC) curve is a graph drawn by plotting the sensitivity on the y-axis and 1 - specificity on the x-axis, while varying the threshold value (Fig. 3) . The value of the area under the curve (AUC) or area under the ROC (AUROC) curve is the mean sensitivity or specificity for all possible threshold values. Its maximum value is 1. In theory, the higher the value, the higher the diagnostic accuracy. Interpretations should be made [...] First, when evaluating AI algorithm performance, it is important to perform external validation using external data, as discussed further later . Given that an AI algorithm's performance in a clinical envirionment may differ from when it was developed, it is best to conduct external validation directly in the target clinical environment. Nevertheless, insufficient external validation of AI algorithms frequently poses problem . Second, instead of blindly accepting the result presented by an AI algorithm, medical professionals should make final decisions after due consideration to the clinical situation and other relevant information. The threshold value described above should also be properly tuned to the clinical situation. For these reasons, while high-performance AI might replace [...] way, data with the natural spectrum and prevalence can be collected, and the performance and the threshold value determined in the validation study can be more directly applied to the clinical setting defined by the eligibility criteria. Whereas a diagnostic case-control study evaluates performance in a somewhat artificial experimental setting, a diagnostic cohort study evaluates performance in a more realistic clinical environment. It is essential to clearly understand the actual clinical setting for which the AI algorithm is intended when determining the concrete eligibility criteria to reflect the clinical setting adequately.

-----

Phase: [EXPLORATION]

### Source [70]: https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation

Query: What decision theory principles from clinical trials apply to AI eval thresholds?

Answer: Net benefit is calculated at a specific decision threshold, and that threshold should be clinically relevant. It represents the point where you’d change your decision, like choosing between referring for surgery versus observing conservatively.

The decision threshold connects to misclassification costs through decision theory. A threshold of 0.1 or 10% means you’re willing to intervene in 10 patients per true positive, which implies the benefit of a true positive is 9 times greater than the harm of a false positive.

Decision curves plot net benefit across a range of reasonable thresholds. This lets you see whether the model has better utility than default strategies like treating everyone or treating no one.

## What to Remember When Evaluating AI [...] Is it Statistical or Clinical?

A measure should either evaluate statistical performance (discrimination, calibration) or decision-analytical performance (does using this model lead to better clinical decisions). Measures that try to do both without following proper decision theory usually end up doing neither well.

## The Incomplete Metrics Healthcare Uses

Classification Metrics at Clinical Thresholds

The big problem is that most every summary classification metric is improper at clinically relevant decision thresholds.

The list includes classification accuracy, balanced accuracy, Youden index, F1 score, Matthews correlation coefficient, diagnostic odds ratio, and Cohen’s kappa. All of them are improper when you’re using a threshold that actually matters clinically. [...] Ask for these specifics (whether you’re reviewing vendors, reading papers, or building models):

 AUROC on an independent validation set that represents the target population
 Calibration assessment (at minimum the calibration slope, ideally a smoothed calibration plot)
 Net benefit analysis at clinically relevant decision thresholds, or a clear explanation of what thresholds are recommended and why
 Transparent discussion of what was tested and what wasn’t

Next in this series: We’ll explore evaluation suites and why testing AI once isn’t enough.

-----

Phase: [EXPLORATION]

### Source [71]: https://arxiv.org/html/2605.02050v1

Query: What decision theory principles from clinical trials apply to AI eval thresholds?

Answer: | 1 | Use an evidentiary continuum to interpret statistical significance | Interpret pp-values as continuous evidence, not binary pass/fail. For novel AI causal claims, use p<0.005p<0.005 as threshold. Report exact pp-values with effect sizes and CIs. Label strength as “suggestive/strong/very strong” rather than “significant/non-significant.” Less stringent thresholds may apply for direct replications or very large pre-registered samples (n>1000n>1000/group). | Early AI evaluations studies can set field precedents. Moving to p<0.005p<0.005 reduces false positives from 5% to 0.5%, critical in a nascent field with many researcher degrees of freedom and high-stakes deployment implications. | Analysis; Reporting | SCV; TRV | [...] In AI evaluation RCTs, this encompasses evidentiary thresholds for novel claims, power and precision (especially for heterogeneity and interaction effects), appropriate treatment of multiple outcomes and analyses, and a shift from dichotomous significance testing toward estimation and graded evidence. We set α=0.005\alpha=0.005 for novel causal claims, emphasize effect size estimation with confidence intervals, and require sensitivity analyses. Threats include underpowered designs, noisy or low-reliability measures, extensive researcher degrees of freedom without pre-specification, and over-interpretation of fragile or marginal results.

### 3.5 Transparency, Repeatability, and Verification [...] | 3 | Distinguish statistical significance, practical significance, and scientific importance | Explicitly discuss all three types of significance. Contextualize effect sizes relative to: domain baseline, implementation costs, scale of application, task criticality, and time horizon. Pre-specify practical significance thresholds before analysis. Avoid applying Cohen’s conventions without domain justification. | The same numerical effect has vastly different implications across domains. Decision-makers need magnitude and cost-effectiveness information, not just detectability. | Design; Analysis; Reporting | SCV; TRV |

-----

</details>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="causal-inference-in-product-experimentation.md">
<details>
<summary>Causal inference in product experimentation</summary>

Phase: [EXPLORATION]

**Source URL:** <https://www.statsig.com/perspectives/causal-inference-in-product-experimentation>

# Causal inference in product experimentation

Fri Nov 15 2024

https://images.ctfassets.net/083zfbgkrzxz/69Ykeiv522qAAezxMPi0ya/db6f8535decfb4aa59aceab283ffdc5b/image.png

Ever wondered why some product changes delight users while others fall flat? Understanding the "why" behind user behavior is the holy grail for product teams. That's where causal inference comes in—it helps us see beyond surface-level correlations to uncover the actual drivers of user actions.

In this blog, we'll explore how causal inference can revolutionize product experimentation. We'll dive into methods for establishing causality, tackle common challenges, and share practical best practices. Let's get started!

## Understanding causal inference in product experimentation

[Causal inference](https://rudrendupaul.medium.com/using-causal-inference-to-understand-product-experiments-e785c4493878) helps us uncover the **real drivers behind user behavior**, moving past mere correlations. It lets us figure out how changes in one variable directly cause changes in another, so we can make smarter product decisions.

Now, you might be thinking: isn't that what A/B testing does? Well, traditional A/B testing tells us if a change had an effect, but it doesn't always explain the "why" behind it. **That's where causal inference steps in**, diving deeper to understand the underlying mechanisms at play.

Applying causal inference isn't just about running any experiment—it requires rigorous design, controlling for those pesky confounding variables, and using the right statistical tools. This thorough approach is crucial for making sure our findings hold up and can predict future outcomes.

By embracing **causal inference** in product experimentation, we can seriously level up our decision-making. It uncovers true causal relationships, helps optimize user experiences, and drives business growth. That's why applying causal inference techniques is so crucial for making informed product decisions.

## Methods for establishing causality

When it comes to nailing down causality, [randomized controlled trials (RCTs)](https://rudrendupaul.medium.com/using-causal-inference-to-understand-product-experiments-e785c4493878) are the gold standard. By **randomly assigning** participants to treatment and control groups, they help minimize confounding factors. But let's face it—RCTs can have ethical concerns, and sometimes they don't quite capture real-world conditions.

So what do we do when RCTs aren't feasible? Alternative methods like **quasi-experiments** and **instrumental variables** can come to the rescue. Quasi-experiments compare naturally occurring groups using techniques like difference-in-differences and regression discontinuity. Instrumental variables, on the other hand, involve a third variable that affects the treatment but not the outcome directly. This allows us to estimate causal effects even when we can't measure all confounders.

**Observational studies** also have their place in inferring causality. Using statistical adjustments, methods like propensity score matching and inverse probability weighting help control for confounding variables in observational data. These techniques aim to mimic the balance we'd get through randomization.

No matter which method we choose, **rigorous experiment design is key**. That means defining clear research questions, picking the right metrics, making sure our groups are comparable, and gathering enough data. At Statsig, we've seen how applying these methods can unlock deeper insights that drive product success. [Practical applications](https://www.statsig.com/blog/the-causal-roundup) abound—for instance, using quasi-experiments for feature assessments or instrumental variables for pricing strategies.

## Overcoming challenges in causal inference

[Causal inference](https://rudrendupaul.medium.com/using-causal-inference-to-understand-product-experiments-e785c4493878) is powerful, but it's not without its hurdles. Challenges like **selection bias** and **confounding variables** can throw a wrench in our results. Selection bias happens when our treatment and control groups aren't comparable, leading us down the wrong path. And confounding variables? They're those third factors that mess with both the treatment and outcome, potentially skewing the true causal relationship.

So how do we tackle these issues? Researchers use strategies like **matching** and **stratification**. Matching pairs similar individuals from the treatment and control groups based on key characteristics. Stratification divides our sample into subgroups based on potential confounders, allowing for more precise effect estimates within each group.

Another big consideration is **external validity**—basically, can we generalize our findings beyond the study? Making sure our sample represents the target population and that our experimental conditions mimic the real world is essential for drawing conclusions that actually matter.

By addressing selection bias, controlling for confounding variables, and keeping an eye on external validity, we can boost the reliability and applicability of our causal inferences. These strategies help us uncover the true drivers of user behavior and make data-driven decisions in product experimentation.

## Practical applications and best practices

Designing effective experiments with causal inference starts with defining clear research questions, selecting the right metrics, ensuring our groups are comparable, collecting enough data, and accounting for confounders. When randomization isn't possible, **quasi-experimental designs** can step in, comparing naturally occurring groups with different exposures. Similarly, [instrumental variables](https://www.reddit.com/r/CausalInference/comments/1ddnu0v/will_automated_causal_inference_analyses_become_a/) help estimate causal effects in scenarios like pricing strategies.

Real-world case studies show how powerful causal inference can be for product decisions. For example, Roblox used instrumental variables to measure the impact of their Avatar Shop on engagement—uncovering valuable insights from past experiments. And LinkedIn? They employed surrogate metrics like Predicted Confirmed Hires to deal with the long lag times in their main metric, enabling timely decision-making.

By leveraging causal inference, we can make truly **data-driven decisions**. It allows us to optimize user interfaces, pricing, and features based on solid evidence—not just correlations. Uncovering causal relationships empowers product teams to make choices that drive long-term growth and keep users happy.

Applying these techniques isn't without challenges, of course. We need to carefully consider things like selection bias, confounding variables, and external validity. Strategies like matching, stratification, and statistical adjustments help us tackle these hurdles, ensuring our conclusions are reliable. At Statsig, we emphasize rigorous experiment design, appropriate methods, and thoughtful interpretation to make the most of causal inference.

## Closing thoughts

Causal inference is a game-changer in product experimentation. By digging beyond surface-level correlations, we can uncover the **real reasons behind user behavior** and make smarter decisions. Whether we're using RCTs, quasi-experiments, or observational studies, the key is to design rigorous experiments and be mindful of potential pitfalls like bias and confounding variables.

If you're keen to dive deeper into causal inference, there are plenty of resources out there. At Statsig, we're passionate about helping teams harness the power of data to drive growth. Feel free to explore our [blog](https://www.statsig.com/blog) for more insights.

Hope you found this useful!

Permalink: [https://www.statsig.com/perspectives/causal-inference-in-product-experimentation](https://www.statsig.com/perspectives/causal-inference-in-product-experimentation)

</details>

</research_source>

</research_source>

<research_source type="scraped_from_research" phase="exploration" file="three-metrics-for-healthcare-ai-evaluation-you-need-to-know.md">
<details>
<summary>Three Metrics for Healthcare AI Evaluation You Need to Know</summary>

Phase: [EXPLORATION]

**Source URL:** <https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation>

# Three Metrics for Healthcare AI Evaluation You Need to Know

### F1 is not just a Brad Pitt movie

# **Article 3: The Metrics That Matter (And The Ones That Don’t)**

[Researchers](https://www.thelancet.com/journals/landig/article/PIIS2589-7500(25)00098-6/fulltext) recently evaluated 32 different performance measures used to validate AI models for healthcare, and concluded that most of them are fundamentally misleading or incomplete, meaning that these measures can make a wrong model look better than the right one.

They call this problem “improperness,” (which sounds like something from Downton Abbey) and they found it to be fairly common. Of the 32 measures they evaluated, 13 were improper and another 3 mixed statistical performance with clinical utility in ways that violate basic decision theory. Only one measure violated both criteria: the F1 score, which is widely used in machine learning for “imbalanced” datasets.

If you’re evaluating healthcare AI, whether you’re on a governance committee, doing vendor diligence, or building models, you need to understand what makes a metric trustworthy versus misleading.

## **The Two Characteristics That Matter**

The Lancet paper argues that a performance measure should have two key characteristics: properness and clear focus.

**Properness: Can It Be Gamed?**

**A measure is “proper” if its expected value is optimal when using the correct model, meaning the model that gives true probabilities.** Here’s what that means in practice. Imagine you validate a model multiple times on different samples from the same population. A proper measure, on average across those validations, will give the best score to the model that’s actually calculating probabilities correctly. **An improper measure can be gamed**, where an incorrect model can score better than the correct one.

**Is it Statistical or Clinical?**

A measure should either evaluate statistical performance (discrimination, calibration) or decision-analytical performance (does using this model lead to better clinical decisions). Measures that try to do both without following proper decision theory usually end up doing neither well.

## **The Incomplete Metrics Healthcare Uses**

**Classification Metrics at Clinical Thresholds**

The big problem is that most every summary classification metric is improper at clinically relevant decision thresholds.

The list includes classification accuracy, balanced accuracy, Youden index, F1 score, Matthews correlation coefficient, diagnostic odds ratio, and Cohen’s kappa. All of them are improper when you’re using a threshold that actually matters clinically.

Some become semi-proper at specific thresholds like 0.5 for classification accuracy, or when the threshold equals true prevalence for F1, but these are rarely the clinically relevant thresholds.

These measures treat a threshold of 10% the same as any other number between 0 and 1. A 10% threshold might mean “we accept operating on 9 patients with benign tumors to catch 1 malignancy,” but the measures don’t incorporate why that threshold matters or what trade-offs it represents. **A model can improve its F1 score by changing predicted probabilities in ways that actually make clinical decisions worse.**

**The F1 Problem**

F1 is the only measure that’s both improper and lacks clear focus. F1 was designed to address class imbalance, so when events are rare, classification accuracy can be inflated by just classifying everything as “no event.” F1 fixes this by ignoring true negatives.

**But in medicine, true negatives matter. If you’re deciding whether to do surgery, correctly identifying that someone doesn’t need surgery is not irrelevant. It’s the whole point of some of your decisions.**

F1 also has no intuitive interpretation, and its absolute value changes if you switch the outcome labels (make 0s into 1s and 1s into 0s). This reveals it’s not measuring something fundamental about model performance.

The Lancet paper says that F1 conflates statistical and decision-analytical performance without properly accounting for misclassification costs and it shouldn’t be used it for clinical AI evaluation.

## **What Actually Works**

The paper recommends focusing on three performance domains that each measure something specific and meaningful.

https://substackcdn.com/image/fetch/$s_!GcOM!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F118836b1-1dff-4564-bd0b-95a9be10df2d_2048x1143.png

**1\. Discrimination**

_What it measures:_ Whether the model can separate people with the event from people without.

_Recommended metric:_ AUROC (area under the ROC curve, also called the C-statistic).

AUROC is semi-proper because it’s based on ranks, so it’s invariant to certain transformations of probabilities. It has a clear focus on statistical performance.

The paper pushes back against common criticisms of AUROC. People say it’s “misleading when prevalence is low” or “doesn’t account for class imbalance.” The authors argue this criticism confuses class imbalance (an epidemiological feature of your population) with misclassification costs (a clinical judgment about decision-making).

AUROC isn’t supposed to reflect misclassification costs. That’s what clinical utility measures are for. Class imbalance is not the same as misclassification costs. If 5% of patients have cancer, that’s the prevalence, but it doesn’t tell you whether missing a cancer case is 10 times worse or 1000 times worse than a false positive. Those are clinical judgments about the intervention, not features of the dataset.

**2\. Calibration**

_What it measures:_ Whether the predicted probabilities match observed event rates.

_Recommended approach:_ Calibration plots with confidence intervals, using smoothing rather than grouping.

The paper recommends smoothed calibration plots because they reveal whether predictions are systematically too high or too low across the full range of probabilities. This matters especially for external validation, when you’re testing the model in different contexts and populations.

**3\. Clinical Utility**

_What it measures:_ Whether using this model leads to better decisions than not using it.

_Recommended metrics:_ Net benefit with decision curve analysis.

This is the only measure that properly incorporates misclassification costs.

Net benefit is calculated at a specific decision threshold, and that threshold should be clinically relevant. It represents the point where you’d change your decision, like choosing between referring for surgery versus observing conservatively.

The decision threshold connects to misclassification costs through decision theory. A threshold of 0.1 or 10% means you’re willing to intervene in 10 patients per true positive, which implies the benefit of a true positive is 9 times greater than the harm of a false positive.

Decision curves plot net benefit across a range of reasonable thresholds. This lets you see whether the model has better utility than default strategies like treating everyone or treating no one.

## **What to Remember When Evaluating AI**

The Lancet paper distilled decades of medical statistics into a clear framework. The three-domain approach gives you what you need: discrimination measured by AUROC to show whether the model can separate high-risk from low-risk patients, calibration measured by calibration plots to show whether the predicted probabilities are accurate, and clinical utility measured by net benefit to show whether using this model leads to better decisions than not using it.

**Watch for these red flags:**

- Vendors who only report F1 score or classification accuracy

- Papers with no calibration assessment

- Models validated only on training data

- Claims of “98% accuracy” without specifying the population or task

- No discussion of decision thresholds or clinical utility

**Ask for these specifics** (whether you’re reviewing vendors, reading papers, or building models):

- AUROC on an independent validation set that represents the target population

- Calibration assessment (at minimum the calibration slope, ideally a smoothed calibration plot)

- Net benefit analysis at clinically relevant decision thresholds, or a clear explanation of what thresholds are recommended and why

- Transparent discussion of what was tested and what wasn’t

**Next in this series**: We’ll explore evaluation suites and why testing AI once isn’t enough.

</details>

</research_source>

