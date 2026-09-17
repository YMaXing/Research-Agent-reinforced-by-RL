# Lesson 29: The North Star of AI Engineering: A Theoretical Framework for Evals

In our previous lessons, we instrumented our agents with observability tools like Opik and learned how to build offline evaluation datasets from production traces and synthetic data. With our data foundation in place, we now move to the core theoretical framework of designing the metrics themselves. In classical Machine Learning, we rely on rigorous evaluation standards like accuracy, precision, recall, and F1-score to measure performance. In AI engineering, however, it is all too common to see teams rely on "vibe checks." This is a subjective feeling that "this output feels more coherent." Other times, teams skip evaluation altogether.

This tendency is understandable. Investing in a proper evaluation layer can feel difficult to prioritize. It delivers no immediate user-visible feature, requires upfront effort to design datasets and metrics, and competes with the constant pressure to ship new functionality. This is especially true in the fast-paced world of generative AI, where the non-deterministic nature of LLMs can make regressions silent and difficult to catch without a formal process. However, this same investment greatly accelerates long-term iteration. It provides an objective signal on every change, catches regressions instantly, and focuses your efforts on what truly matters.

Evals are the north star of AI engineering. They are the single source of truth that tells you exactly which modifications improve your system and which degrade it. In a field defined by rapid change and probabilistic outputs, a robust evaluation framework provides the stable direction needed to build reliable products.

In this lesson, we will cover the theoretical foundations that will empower you to build a robust evaluation strategy. We will explore:

*   The optimization flywheel and its three core use cases.
*   The trade-offs between different metric types for unstructured outputs.
*   Why custom business metrics are superior to public benchmarks and generic scores.
*   Why binary pass/fail judgments are more effective than Likert scales.

With the problem and its importance clear, we will now examine how to operationalize evals inside a repeatable optimization flywheel that replaces intuition with evidence.

## Using Evals Through the Optimization Flywheel

To build intuition, let's examine how you can effectively use and integrate AI evaluations into your application development lifecycle. Evaluations provide value in three core scenarios: quantifying system quality, guiding optimization, and preventing regressions.

First, evals **quantify the quality of your system** on a given set of metrics, snapshotting a baseline of its current performance. Without this baseline, you cannot know if your system is ready for production or if your changes are actually improving it. Second, these metrics serve as **guidance when optimizing your system**, providing evidence for experiments and shifting development from being intuition-based to evidence-based. Finally, they act as **regression tests** that protect shared components. The goal here is stability rather than improvement, which is essential in AI engineering as components are often interconnected [[7]](https://galileo.ai/blog/nvidia-data-flywheel-for-de-risking-agentic-ai), [[8]](https://www.nvidia.com/en-us/glossary/data-flywheel).

### The Optimization Process

How does this look in a real-world scenario? Let's look at a step-by-step plan for the optimization flywheel.

1.  **Gather your dataset:** You start by assembling an offline evaluation dataset, combining real production traces with targeted synthetic data to ensure broad coverage, as we did in Lesson 28. This dataset becomes the ground truth against which all changes are measured.
2.  **Build your metrics:** You define a set of business-aligned metrics to measure performance. This involves identifying the key behaviors that define success for your application, a topic we will explore later in this lesson. These metrics translate abstract goals into quantifiable signals.
3.  **Establish a baseline:** You run your evals on the current system to compute baseline scores. This snapshot represents your starting point and is the reference against which all future changes are measured. It is your system's initial "report card."
4.  **Start the optimization:** You make one isolated change that you believe will improve performance. This could be a prompt modification, a change in the retrieval strategy, swapping out the underlying LLM, or adjusting a hyperparameter like temperature.
5.  **Compute the new score:** You re-evaluate the entire dataset by re-running the evals. This ensures you are measuring the impact of your change across all known scenarios, not just a few cherry-picked examples. This comprehensive re-evaluation is what makes the process rigorous.
6.  **Compare:** You compare the new scores to the baseline, considering statistical significance. This step quantifies the impact of your change, telling you if it resulted in a meaningful improvement, a degradation, or no real change.
7.  **Decide:** Based on whether the score is better, the same, or worse, you decide to keep the change, consider its complexity, or revert it. This decision should also factor in operational costs like latency and token usage. A 2% accuracy gain might not be worth a 50% increase in cost.
8.  **Repeat:** You repeat this cycle, continuously iterating and refining your system until the scores meet your target for production readiness. This iterative process is the engine of systematic improvement.![The iterative optimization flywheel for AI applications using evaluations.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-4d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down)
Image 1: The iterative optimization flywheel for AI applications using evaluations. (Source [Escaping POC Purgatory: Evaluation-Driven Development for AI Systems](https://www.decodingai.com/p/escaping-poc-purgatory-evaluation))

It is essential to keep all components fixed except for one variable per cycle. If you change the prompt and the retrieval model simultaneously, you cannot know which change caused the score to move. This disciplined, one-variable-at-a-time approach is a practical application of principles from causal inference. To understand causality, you must isolate the cause by controlling for confounding variables [[1]](https://www.statsig.com/perspectives/causal-inference-in-product-experimentation), [[20]](http://www.jmlr.org/papers/volume7/MLOPT-intro06a/MLOPT-intro06a.pdf).

Your definition of "better" must also be anchored to actual **business impact**, not just arbitrary p-values. This concept is known as **practical significance**, which asks whether a statistically significant result is large enough to matter in the real world. The field of healthcare AI evaluation makes a similar distinction between statistical performance and clinical utility. This refers to whether a model leads to better patient outcomes [[2]](https://arxiv.org/html/2605.02050v1), [[3]](https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation).

For a high-volume support bot processing millions of checkouts per year, a small improvement of 0.5% in error reduction could translate to 10,000 fewer failed transactions and save $150,000 annually. In this context, even a tiny numerical improvement has a massive real-world gain. Conversely, for a low-volume creative writing tool used internally by a small team, a similar small improvement is likely negligible, and larger performance gains would be required before declaring victory [[39]](https://www.nngroup.com/articles/practical-significance), [[41]](https://www.quirks.com/articles/effective-uses-of-effect-size-statistics-to-demonstrate-business-value).

### Regression Testing

A valuable variation of this flywheel is using evals for regression testing. Before merging any new feature that touches shared prompts, tool descriptions, or orchestration logic, you run the full eval suite to guard against breaking existing behavior. This practice mirrors the concept of "quality gates" in traditional software engineering, where automated checkpoints enforce predefined standards and prevent regressions before code is merged [[4]](https://www.softwareseni.com/building-quality-gates-for-ai-generated-code-with-practical-implementation-strategies).

This process can be broken down into five steps:

1.  **Implement a new feature:** You write the code and verify it works locally for the new use case, ensuring it meets the immediate requirements.
2.  **Run the AI evaluations:** You run the full suite of assessments, which covers all previous use cases, not just the new one. This is the key step to ensure backward compatibility.
3.  **Compare Scores:** You compare the new scores against the baseline for all use cases to identify any performance changes.
4.  **Metrics similar to baseline:** If the scores are identical or better, your feature is safe to merge as it has not negatively impacted existing functionality.
5.  **Metrics lower than the baseline:** If any score is worse, you have introduced a regression. You must debug and fix your code, then repeat the process from step 2.![Integrating AI evaluations into CI pipelines for regression testing.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down)
Image 2: Integrating AI evaluations into CI pipelines for regression testing. (Source [Escaping POC Purgatory: Evaluation-Driven Development for AI Systems](https://www.decodingai.com/p/escaping-poc-purgatory-evaluation))

Unlike traditional software unit tests that have a fixed pass/fail condition, AI evals often compare scores against a moving baseline. This allows you to track performance drift and make informed decisions about whether a change represents a true improvement or an acceptable trade-off.

Your evaluation dataset must also be a living artifact. It should continuously expand with new edge cases from feature development, real-world failures captured from production traces via observability tools like Opik, and hard examples that expose current failure modes. For instance, if you discover a regression in production where your agent fails on a specific type of user input, you should add that trace to your evaluation dataset. This ensures that your test suite grows to cover real-world scenarios and prevents the same regression from happening again [[21]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets), [[22]](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals).

With the flywheel mechanics clear, we can now examine the different families of metrics we might plug into it when dealing with unstructured outputs.

## Exploring Possible Metric Types

The core difficulty in evaluating AI systems is that you are often working with unstructured outputs like text or images. Unlike classical ML where you can compare predictions to structured labels, here you need different families of metrics to assess quality.

### BLEU and ROUGE

N-gram overlap metrics like BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Oriented Understudy for Gisting Evaluation) are the oldest and simplest. They work by counting the number of overlapping words or sequences of words (n-grams) between the generated output and a reference text. Their main advantages are that they are fast, deterministic, and require no additional models [[26]](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb).

However, this is also their biggest weakness: they are blind to semantic meaning. They cannot recognize paraphrasing and will penalize a perfectly correct answer simply because it uses different words than the reference. For example, if the reference is "The experiment succeeded" and the model outputs "The test was successful," the BLEU score would be near zero despite the identical meaning. These metrics also do not care about factual accuracy or logical consistency. Furthermore, they can be misleading if they fail to account for the costs of different error types. For example, the popular F1 score, often used in classification, is known to be an improper metric for clinical AI evaluation because it completely ignores true negatives. In medicine, correctly identifying that a patient *doesn't* need surgery is a vital outcome, not an irrelevant one [[3]](https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation), [[23]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ).

### BERTScore

Embedding similarity metrics like BERTScore address the semantic blindness of n-gram methods. They use a pre-trained language model like BERT to convert both the generated and reference texts into high-dimensional vectors, or embeddings. By calculating the cosine similarity between these embeddings, they can measure how close the two texts are in meaning. This allows them to correctly identify paraphrases as high-quality outputs. Their main limitation is that they are still comparison-based and cannot verify complex business logic or factual accuracy outside the provided reference [[5]](https://spotintelligence.com/2024/08/20/bertscore/).

### LLM Judges

The LLM-as-a-judge approach uses a powerful LLM to evaluate an output based on a detailed set of criteria. You provide the judge model with the input, the generated output, a rubric, few-shot examples, and chain-of-thought instructions to produce a structured judgment. This method is highly flexible and can be customized to evaluate subjective qualities like tone, adherence to brand voice, or complex, domain-specific rules. For example, you could create a judge to verify if a generated legal summary correctly identifies all relevant clauses and avoids making unsubstantiated claims [[28]](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method), [[32]](https://arize.com/llm-as-a-judge).

The main pros are that they can evaluate subjective aspects and provide detailed, human-like critiques. The main cons are that their performance depends heavily on the prompt and the evaluator model. They can also be slower, more expensive, and inherit the biases of the LLM they are built on, such as a preference for longer answers (verbosity bias) or answers generated by the same model family (self-enhancement bias) [[43]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge), [[46]](https://cameronrwolfe.substack.com/p/llm-as-a-judge).

| Dimension | BLEU/ROUGE | BERTScore | LLM Judge |
| :--- | :--- | :--- | :--- |
| **Speed** | Very Fast | Fast | Slow |
| **Cost** | Very Low | Low | High |
| **Semantic Awareness** | None | High | Very High |
| **Business Alignment** | Low | Medium | High |
| **Explainability** | High | Low | High (with CoT) |

Table 1: A comparison of trade-offs between different metric families.

For the complex requirements of our capstone writing agent, such as guideline adherence and research grounding, LLM judges are the most practical choice. You have probably heard us say "business metrics here, business metrics there." Thus, let's understand why defining your own business metrics is such an essential step in building your AI evals strategy.

## Why Business Metrics Over Benchmarks

It is a common mistake to look at popular leaderboards or open benchmarks to select an LLM for a product. Benchmarks are often the most deceiving type of metric, and relying on them for product decisions is a path to failure. There are two core reasons for this.

First, public benchmarks often become marketing artifacts. Once a test set is public, teams can inadvertently or deliberately overfit to it, "teaching to the test" to climb leaderboard scores. There have been instances where models were found to have been trained on benchmark test sets, a form of data contamination that inflates their scores and renders the benchmark useless for measuring true generalization. This erodes the benchmark's validity, as it no longer represents performance on unseen data [[6]](https://openreview.net/forum?id=XbVMiW0jTM), [[13]](https://launchdarkly.com/blog/llm-evaluation), [[15]](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053).

Second, there is a fundamental mismatch between the tasks in most benchmarks and the needs of real business applications. A model that excels at solving math problems from GSM8k or answering trivia questions may be completely unsuited for long-form creative writing, nuanced legal analysis, or personalized customer support. The proper role for benchmarks is narrow. They are useful for advancing research and for initial model filtering during early exploration, but they should never be the primary target for product-level optimization [[12]](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches).

If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous. You must instead build metrics that are deeply tied to your specific application.

## Why Custom Business Metrics Over Generic Metrics

Generic, off-the-shelf metrics for qualities like "toxicity," "helpfulness," or "hallucination" create a mirage. They seem objective, but they lack the context of your product, your users, and your brand voice. Optimizing for them often means optimizing for the wrong signal, creating a false sense of confidence. A model can score brilliantly on a generic "helpfulness" metric but fail catastrophically on your specific business constraints [[16]](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP), [[48]](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics).

Consider the dashboard below. It looks impressive, with scores for "Truthfulness" and "Personalization." But what does a 3.7 in "Personalization" actually mean? Without a clear, business-grounded definition, such numbers are vanity metrics that do not drive meaningful action.![A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down)
Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!" (Source [The 5-Star Lie: You’re Doing AI Evaluations Wrong](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals))

Let's take our Brown writing agent as an example. Suppose we want to check if a generated article contains hallucinations. A generic `hallucination` score might return "positive." But what does that tell us? Did the agent invent information not present in the research? Did it deviate from the article guidelines? Or did it simply include a personal story that, while not in the source text, is factually correct and aligns with the desired authorial voice? A generic detector cannot distinguish between undesirable invention and desirable creative elaboration. For example, a generic detector might flag an engaging personal anecdote as a fabrication, yet that same anecdote may be exactly what your brand voice requires.

Prefab scores are limited because they lack domain-specific constraints, cannot localize which part of an output failed, and introduce additional statistical noise. Their only valid role is during exploratory data analysis, where they can act as a "flashlight" to surface interesting examples for manual review, not as a report card for grading quality.

Here are a few useful examples of using generic metrics for exploration:

1.  **Verbosity:** Sorting your outputs by length can reveal if your most verbose answers are rambling and unhelpful, or if your shortest answers are curt and missing information. This helps you spot failure modes in long-form generation. For example, you might discover that your longest responses are often the result of the model getting stuck in a repetitive loop.
2.  **Similarity Score:** In a RAG system, you can use a similarity score to evaluate the retriever component. If the similarity between the user query and the retrieved document chunks is low, your retriever is likely failing. This is a valid component-level check that helps isolate problems in your pipeline.
3.  **BERTScore:** If a cluster of generated outputs has a low BERTScore against your "golden" reference, a manual review might reveal that the LLM found a more creative or even better solution than the one you provided. This challenges your assumptions about what a "good" answer is and can lead to improvements in your reference dataset.

In all these cases, the generic metric is the start of an investigation, not the final verdict. Every production metric must be deeply application-centric, derived from your product requirements and user success criteria [[48]](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics).

Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments. Here, binary pass/fail criteria outperform every alternative.

## Choosing Binary Metrics Over Anything Else

When designing custom metrics, you face a choice: should you use a Likert scale, like a 1-to-5 star rating, or a simple binary pass/fail? We strongly recommend **binary metrics**.

Likert scales are a seductive trap. They promise nuance but deliver noise. They suffer from three fundamental problems [[49]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).

1.  **Inconsistent Labeling:** The difference between a '3' and a '4' is subjective. One person's '4' is another's '3', leading to low inter-annotator agreement and a fuzzy rubric [[9]](https://www.ellamind.com/blog/binary-vs-likert-scales).
2.  **Statistical Noise:** Detecting a meaningful improvement from an average score of 3.2 to 3.4 requires a much larger sample size than detecting a shift in a binary pass rate from 75% to 80%. You can waste weeks on changes without knowing if you are making real progress [[9]](https://www.ellamind.com/blog/binary-vs-likert-scales).
3.  **Lazy Decision-Making:** Annotators, both human and LLM, often default to the middle value ('3') to avoid a difficult judgment. This "satisficing" behavior hides uncertainty, and a dashboard full of '3's tells you nothing about what to fix [[10]](https://www.scribbr.com/methodology/likert-scale), [[49]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).

Think of it this way: a 1-5 scale adds noise and uncertainty to your evaluation. A clear yes/no decision cuts through that noise, giving you a much cleaner signal about your system's performance. Binary evaluations solve these problems by **forcing decisions**. An output either met the criterion or it did not. This simple constraint brings immediate benefits:

1.  **Clearer Thinking:** You cannot hide in ambiguity. This forces you to create precise, unambiguous definitions of quality.
2.  **Consistency:** Binary decisions are faster and more consistent for both human annotators and LLM judges, increasing throughput and reliability.
3.  **Actionability:** The output is a clear signal tied to a specific problem. A spike in the "Constraint Violation" failure rate tells an engineer exactly where to start debugging.

<aside>
💡
**Note:** These points translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate the inherent randomness of LLMs. LLMs are much more stable when asked to make a binary decision than when asked to assign a scalar value. A binary metric translates to a more robust and repeatable evaluation pipeline.

</aside>

### Capturing Nuance

The standard objection to binary evals is the perceived loss of nuance: "What if a response is partially correct? A 'Fail' seems too harsh."

This is a valid concern, but the solution is not a fuzzier scale. The right way to capture nuance is by making your criteria more **granular**. Instead of a single, subjective rating for a complex quality, you decompose it into multiple, specific, binary checks. This approach not only provides a more accurate picture but also creates a direct link between a specific metric and a specific part of the system that can be improved, making the optimization loop much tighter.

For our writing agent, instead of rating an article 1-5 for "Quality," we can create multiple binary evaluations that capture specific dimensions:

1.  **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
2.  **Flow of Ideas Adherence:** Does the generated article present ideas in the same order as the expected article? (Yes/No)
3.  **Article Guideline Adherence:** Does the generated article follow the flow of ideas from the article guideline input? (Yes/No)
4.  **Research Anchoring:** Is every claim in the article supported by the provided research? (Yes/No)

By aggregating these binary signals, you gain a far more precise and actionable view of performance. You can now say, "Our system is passing Content Adherence 95% of the time, but failing Research Anchoring 40% of the time." This is a signal you can act on. You have captured nuance without sacrificing clarity.

With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in our next lesson.

## Conclusion

This lesson has laid out the case for a fundamental shift in how we approach AI engineering: moving away from vibe checks, leaderboards, and generic scores toward a rigorous, evaluation-driven development cycle. This cycle is built on a foundation of custom, business-aligned metrics that prioritize clarity and actionability.

We have argued that granular, pass/fail criteria deliver the clearest optimization signal while avoiding the statistical noise and subjectivity inherent in scalar ratings. This disciplined approach is what separates prototypes from production-ready AI systems. In the next lesson, we will translate this theory into practice by implementing custom LLM judges from scratch to evaluate our Brown writing workflow.

## References

- [1] Causal inference in product experimentation. (https://www.statsig.com/perspectives/causal-inference-in-product-experimentation)
- [2] Evidentiary standards for clinical evaluation of AI. (https://arxiv.org/html/2605.02050v1)
- [3] Three Metrics for Healthcare AI Evaluation You Need to Know. (https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation)
- [4] Building Quality Gates for AI-Generated Code. (https://www.softwareseni.com/building-quality-gates-for-ai-generated-code-with-practical-implementation-strategies)
- [5] BERTScore explained: A modern metric for evaluating text generation. (https://spotintelligence.com/2024/08/20/bertscore/)
- [6] Benchmark Overfitting in Large Language Models. (https://openreview.net/forum?id=XbVMiW0jTM)
- [7] A Powerful Data Flywheel for De-Risking Agentic AI. (https://galileo.ai/blog/nvidia-data-flywheel-for-de-risking-agentic-ai)
- [8] What is a Data Flywheel?. (https://www.nvidia.com/en-us/glossary/data-flywheel)
- [9] Binary vs. Likert Scales in AI Evals. (https://www.ellamind.com/blog/binary-vs-likert-scales)
- [10] How to Use a Likert Scale. (https://www.scribbr.com/methodology/likert-scale)
- [11] What Is a Likert Scale?. (https://inmoment.com/blog/likert-scale)
- [12] 4 Approaches to Evaluating LLMs. (https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches)
- [13] The challenges of LLM evaluation. (https://launchdarkly.com/blog/llm-evaluation)
- [14] Benchmarking LLM Agents for Government. (https://arxiv.org/html/2601.20617v1)
- [15] AI — Benchmark scores are becoming marketing; dynamic eval is the only antidote. (https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053)
- [16] Shivanshu Aggarwal on LinkedIn. (https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP)
- [17] A Meta-Evaluation of Evaluation Metrics for General-Purpose Text-to-Text Generation. (https://arxiv.org/html/2508.13816v1)
- [18] Human Evaluation Metrics in AI. (https://galileo.ai/blog/human-evaluation-metrics-ai)
- [19] LLM Evaluation from Classic Metrics to Modern Methods. (https://toloka.ai/blog/llm-evaluation-from-classic-metrics-to-modern-methods)
- [20] Introduction to Optimization Methods. (http://www.jmlr.org/papers/volume7/MLOPT-intro06a/MLOPT-intro06a.pdf)
- [21] Manage Datasets. (https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets)
- [22] Generate Synthetic Datasets for AI Evals. (https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals)
- [23] LLM evaluation benchmarking: Beyond BLEU and ROUGE. (https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ)
- [24] Demystifying the BLEU Metric. (https://www.traceloop.com/blog/demystifying-the-bleu-metric)
- [25] BLEU and ROUGE. (https://docs.galileo.ai/concepts/metrics/expression-and-readability/bleu-and-rouge)
- [26] Understanding BLEU and ROUGE Score for NLP Evaluation. (https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb)
- [27] Evaluating RAG: A practical guide to metrics. (https://www.elastic.co/search-labs/blog/evaluating-rag-metrics)
- [28] Why LLM-as-a-Judge is the Best LLM Evaluation Method. (https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method)
- [29] LLM-as-a-Judge: When to Use Reasoning (CoT) and Explanations. (https://medium.com/data-science-collective/llm-as-a-judge-when-to-use-reasoning-cot-and-explanations-964ad82ebc3d)
- [30] Evidence-Based Prompting Strategies for LLM-as-a-Judge: Explanations and Chain of Thought. (https://arize.com/blog/evidence-based-prompting-strategies-for-llm-as-a-judge-explanations-and-chain-of-thought)
- [31] What is LLM-as-a-Judge?. (https://www.braintrust.dev/articles/what-is-llm-as-a-judge)
- [32] LLM-as-a-Judge. (https://arize.com/llm-as-a-judge)
- [33] Vibe Checks are All You Need. (https://olshansky.substack.com/p/vibe-checks-are-all-you-need)
- [34] VibeCheck: A Self-Correcting Challenge Set for Vibe-Based Evaluation of LLMs. (https://arxiv.org/html/2410.12851v1)
- [35] AI Evals vs. A/B Testing: Why You Need Both to Ship GenAI. (https://www.growthbook.io/blog/ai-evals-vs-a-b-testing-why-you-need-both-to-ship-genai)
- [36] From Vibe Checks to Continuous Evaluation. (https://cloud.google.com/blog/topics/developers-practitioners/from-vibe-checks-to-continuous-evaluation-engineering-reliable-ai-agents)
- [37] Stop Evaluating LLMs with Vibe Checks. (https://towardsdatascience.com/stop-evaluating-llms-with-vibe-checks)
- [38] What Is Statistical Significance?. (https://corporatefinanceinstitute.com/resources/data-science/statistical-significance)
- [39] Practical Significance. (https://www.nngroup.com/articles/practical-significance)
- [40] Understanding Statistical Significance. (https://www.statsig.com/perspectives/understanding-statistical-significance)
- [41] Effective uses of effect size statistics to demonstrate business value. (https://www.quirks.com/articles/effective-uses-of-effect-size-statistics-to-demonstrate-business-value)
- [42] What is Statistical Significance?. (https://www.cloudresearch.com/resources/guides/statistical-significance/what-is-statistical-significance)
- [43] LLM-as-a-judge: a complete guide to using LLMs for evaluations. (https://www.evidentlyai.com/llm-guide/llm-as-a-judge)
- [44] LLM-as-a-Judge vs. Human Evaluation. (https://galileo.ai/blog/llm-as-a-judge-vs-human-evaluation)
- [45] Alla Abdella on LinkedIn. (https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw)
- [46] LLM as a Judge. (https://cameronrwolfe.substack.com/p/llm-as-a-judge)
- [47] Why LLM-as-a-Judge is the Best LLM Evaluation Method. (https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method)
- [48] The Mirage of Generic AI Metrics. (https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics)
- [49] The 5-Star Lie: You’re Doing AI Evaluations Wrong. (https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals)
- [50] An Information-Theoretic Approach to Artefact and Noise Removal in Tomographic Reconstructions. (https://arxiv.org/html/2602.07168)
- [51] Using LLM-as-a-Judge For Evaluation: A Complete Guide. (https://hamel.dev/blog/posts/llm-judge/)
- [52] Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge). (https://eugeneyan.com/writing/llm-evaluators/)
- [53] Stop Launching AI Apps Without This Framework. (https://www.decodingai.com/p/stop-launching-ai-apps-without-this)
- [54] Escaping POC Purgatory: Evaluation-Driven Development for AI Systems. (https://www.decodingai.com/p/escaping-poc-purgatory-evaluation)
- [55] Evaluating NLP Models: A Comprehensive Guide to ROUGE, BLEU, METEOR, and BERTScore Metrics. (https://plainenglish.io/blog/evaluating-nlp-models-a-comprehensive-guide-to-rouge-bleu-meteor-and-bertscore-metrics-d0f1b1)
- [56] Key NLP Evaluation Metrics. (https://datumo.com/en/blog/insight/key-nlp-evaluation-metrics/)
- [57] Causal Inference Explained. (https://telnyx.com/learn-ai/casual-inference-explained)
</article>