# The North Star of AI Engineering: A Guide to Evaluation-Driven Development

In our last lessons, we instrumented our AI agents with observability tools like Opik and learned how to build offline datasets from production traces. Now, we move to the core theoretical framework of designing the metrics themselves. In classical machine learning, we rely on rigorous evaluation standards like accuracy, precision, recall, and F1-scores to measure performance. These metrics provide a clear, quantitative signal that guides model development and ensures statistical validity.

In AI engineering, however, it is common to see teams rely on "vibe checks" or skip evaluation altogether, approving changes because an output "feels more coherent" [[1]](https://olshansky.substack.com/p/vibe-checks-are-all-you-need). This informal process of manually inspecting a few outputs is useful for early exploration, but it is unscalable and statistically flawed for production systems. It fails to account for edge cases, regressions, or large-scale user preferences [[2]](https://www.growthbook.io/blog/ai-evals-vs-a-b-testing-why-you-need-both-to-ship-genai). This is not a new problem; I have seen it across various domains for over a decade, from spam filtering at Twitter to autonomous vehicle interactions at Waymo [[1]](https://olshansky.substack.com/p/vibe-checks-are-all-you-need).

Investing in a proper evaluation layer can feel hard to prioritize. It delivers no immediate user-visible feature and requires upfront effort to design datasets and metrics, all while competing with the pressure to ship. But this same investment substantially accelerates long-term iteration. It provides an objective signal on every change and catches regressions instantly, turning a chaotic process into a disciplined engineering practice.

Evals are the north star of AI engineering: the single source of truth that tells you exactly which modifications improve the system and which degrade it. This lesson will establish the theoretical foundation for evaluation-driven development (EDD) by covering:

*   The optimization flywheel and its three core use cases.
*   Metric trade-offs for unstructured outputs.
*   Why business metrics beat benchmarks and generic scores.
*   Why binary judgments are superior to Likert scales.

With the problem and its importance clear, we will now examine how to operationalize evals inside a repeatable optimization flywheel that replaces intuition with evidence.

## Using Evals Through the Optimization Flywheel

To build intuition, let's examine how we can effectively use and integrate AI evaluations into our application development lifecycle. There are three core scenarios where evaluations provide value. First, evals **quantify the quality of your system** on a set of given metrics, snapshotting a baseline of its current state. Without this baseline, you cannot know if the system is ready for production or if it is improving. Second, metrics serve as **guidance when optimizing your system**, shifting development from intuition-based to evidence-based [[3]](https://galileo.ai/blog/nvidia-data-flywheel-for-de-risking-agentic-ai). Finally, they act as **regression tests** that protect shared components, ensuring stability rather than just improvement. This is critical in AI engineering, as components are often interconnected [[4]](https://www.nvidia.com/en-us/glossary/data-flywheel).

### The Optimization Process

How does this look in a real-world scenario? The optimization flywheel is an eight-step process for systematically improving your AI application. This virtuous cycle of continuous improvement is a cornerstone of modern AI development, allowing teams to iteratively refine models based on real-world data and feedback [[3]](https://galileo.ai/blog/nvidia-data-flywheel-for-de-risking-agentic-ai).

1.  **Gather your dataset:** Assemble an offline dataset that represents the real-world scenarios your application will face. This dataset, which can be built from production traces or synthetic data, becomes the foundation for all subsequent improvements.
2.  **Build your metrics:** Define a set of business-aligned metrics that capture what "good" looks like for your product. These metrics, which we will explore later in this lesson, will be your guideposts for success.
3.  **Establish a baseline:** Run your evaluation suite on the current system to compute baseline scores for each metric. This snapshot represents your starting point and the performance you aim to beat.
4.  **Start the optimization:** Make one isolated change you believe will improve performance, such as tweaking a prompt, swapping a model, or adjusting a retrieval parameter.
5.  **Compute the new score:** Re-evaluate the entire dataset by re-running the evals on the modified system. This generates a new set of scores to compare against your baseline.
6.  **Compare:** Analyze the new scores against the baseline, considering statistical significance to determine if the change resulted in a meaningful improvement, degradation, or no real difference.
7.  **Decide:** Based on whether the score is better, the same, or worse, decide to keep the change, revert it, or conduct further analysis. This decision should also factor in the complexity and cost of the change.
8.  **Repeat:** Continue the cycle, making one change at a time, until your scores meet the desired quality threshold for production deployment.

This iterative process turns subjective guesswork into a systematic, evidence-driven workflow.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-4d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down
Image 1: The iterative optimization flywheel for AI applications using evaluations.

It is critical to keep all components fixed except for one variable per cycle. This principle is grounded in the field of causal inference, which aims to distinguish correlation from causation. When multiple variables change simultaneously, their effects are confounded, making it impossible to know which change drove the outcome [[5]](https://www.statsig.com/perspectives/causal-inference-in-product-experimentation). By changing only one thing at a time, such as a prompt, a model parameter, or a retrieval strategy, you can confidently attribute any performance change to that specific modification [[6]](http://www.jmlr.org/papers/volume7/MLOPT-intro06a/MLOPT-intro06a.pdf).

Furthermore, you must anchor statistical significance to actual **business impact** [[7]](https://www.nngroup.com/articles/practical-significance), [[8]](https://www.statsig.com/perspectives/understanding-statistical-significance). Decision theory from high-stakes fields like medicine provides a useful framework here called "net benefit analysis," which connects a decision threshold to the explicit costs of misclassification [[9]](https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation). For a high-volume support bot processing millions of transactions, a tiny 0.5% reduction in checkout errors could translate to hundreds of thousands of dollars in saved revenue, making the change practically significant [[7]](https://www.nngroup.com/articles/practical-significance). In contrast, for a low-volume creative writing tool used by a few hundred people, a similar small improvement might be negligible to users and not justify the engineering effort [[10]](https://www.quirks.com/articles/effective-uses-of-effect-size-statistics-to-demonstrate-business-value).

### Regression Testing

The optimization flywheel can be adapted for regression testing, an approach analogous to the "quality gates" used in modern software development and Six Sigma manufacturing. These are automated pass/fail checkpoints that enforce predefined standards [[35]](https://www.softwareseni.com/building-quality-gates-for-ai-generated-code-with-practical-implementation-strategies). Before merging any new feature that touches shared components, you run the full eval suite to guard against breaking existing behavior. This transforms AI evaluations into a powerful regression testing framework that ensures new features do not degrade existing ones.

This five-step process integrates directly into your development workflow:

1.  **Implement a new feature:** You write the code and verify it works locally for the new use case.
2.  **Run the AI evaluations:** You run the full suite of assessments, covering all previous use cases, not just the new one.
3.  **Compare Scores:** The baseline vs. the AI evals scores on your new feature.
4.  **Metrics similar to baseline:** If the scores are identical to the baseline, your feature is OK, as it didn't affect any old feature. You can merge the feature into your production codebase.
5.  **Metrics lower than the baseline:** If the score is worse, you have introduced a regression. You should fix your code. Then repeat steps 2 and 3.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down
Image 2: Integrating AI evaluations into CI pipelines for regression testing.

Unlike traditional unit tests with fixed pass/fail thresholds, AI evals compare scores against a moving baseline. This is more like an integration test for your AI system's probabilistic components.

Your evaluation dataset must continuously expand. As new features are added, you must include their edge cases. When observability tools like Opik capture production failures, those traces should be converted into new evaluation samples [[11]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets). For example, if you notice in your production logs that a specific user query about "billing disputes" consistently causes your agent to select the wrong tool, you can add that exact trace to your evaluation dataset. This ensures that any future changes are tested against this known failure mode, preventing the same regression from happening again [[12]](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals). Hard debugging examples that expose current failure modes also become permanent additions. Instead of writing new tests in code, you broaden the test coverage by adding new, challenging samples to your dataset.

With the flywheel mechanics clear, we can now examine the different families of metrics we might plug into it when dealing with unstructured outputs.

## Exploring Possible Metric Types

The core difficulty in evaluating AI systems is that we are often dealing with unstructured text, reasoning traces, or even images, where standard accuracy metrics do not apply. There are three main families of metrics designed to handle these outputs.

### BLEU and ROUGE

N-gram overlap metrics like BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Oriented Understudy for Gisting Evaluation) are the oldest and simplest. They work by counting the number of overlapping words or sequences of words (n-grams) between the generated text and a reference text [[13]](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb). Their main advantages are that they are fast, deterministic, easy to understand, and require no additional models [[14]](https://www.traceloop.com/blog/demystifying-the-bleu-metric). However, they are blind to semantic meaning. They penalize valid paraphrasing and cannot assess if the reasoning is correct, only if the words match [[15]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ), [[16]](https://www.elastic.co/search-labs/blog/evaluating-rag-metrics). For example, if a reference is "The test was successful" and the model outputs "The experiment succeeded," the n-gram overlap is zero, resulting in a poor score despite the identical meaning [[15]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ).

### BERTScore

Embedding similarity metrics like BERTScore address the semantic blindness of n-gram methods. They use a pre-trained language model like BERT to convert both the generated and reference texts into high-dimensional vector embeddings. By calculating the cosine similarity between these embeddings, BERTScore can measure how semantically close the two pieces of text are. This allows it to recognize paraphrases and different phrasings that carry the same meaning [[15]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ). While this is a significant improvement, it is still a comparison metric and cannot verify complex business logic or factual accuracy on its own.

### LLM Judges

The LLM-as-a-judge approach uses a capable LLM to evaluate an output based on a detailed set of criteria [[17]](https://www.braintrust.dev/articles/what-is-llm-as-a-judge). You provide the judge model with the input, the generated output, a rubric, few-shot examples, and chain-of-thought instructions. This method is highly flexible and can be customized to evaluate subjective qualities like tone, brand voice, or adherence to complex guidelines [[18]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge). For example, an LLM judge can assess whether a customer support response is not only factually correct but also empathetic and aligned with the company's brand voice, a nuance that lexical and semantic metrics would miss. The main drawback is that performance depends heavily on the prompt and the evaluator model. LLM judges can also be slower, more expensive, and may inherit the biases of the underlying model if not carefully designed and validated [[19]](https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw), [[20]](https://cameronrwolfe.substack.com/p/llm-as-a-judge).

| Metric Family | Speed | Cost | Semantic Awareness | Business Alignment | Explainability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BLEU/ROUGE** | High | Low | Low | Low | Medium |
| **BERTScore** | Medium | Medium | High | Low | Low |
| **LLM Judges** | Low | High | High | High | High |

Table 1: A comparison of trade-offs between different metric families for evaluating unstructured outputs.

For the complex requirements of our capstone writing agent, such as guideline adherence and research grounding, LLM judges are the most practical choice due to their high degree of customizability and alignment with business logic.

Now, you have heard from us repeatedly: *"business metrics here, business metrics there."* Thus, let's understand why defining your own business metrics is such an essential step in building your AI evals strategy.

## Why Business Metrics Over Benchmarks

Using popular leaderboards or open benchmarks to select an LLM for your product is often a mistake. Benchmarks are the most deceiving type of metric for two core reasons.

First, public benchmarks often function as marketing artifacts. Once a test set is public, teams can inadvertently or intentionally overfit to it, "teaching to the test" to climb leaderboards. This inflates scores and erodes the benchmark's validity, as it no longer represents unseen data. There have been instances where models were found to have been trained on test sets, leading to misleadingly high performance [[21]](https://www.evidentlyai.com/llm-guide/llm-benchmarks), [[22]](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053). This phenomenon, known as "benchmark overfitting," means that a high score may reflect memorization of the test set's patterns rather than genuine reasoning ability. Research has shown that even powerful models can fail on simple variations of benchmark problems, revealing they have memorized a solution "paradigm" rather than learning to reason flexibly [[23]](https://openreview.net/forum?id=XbVMiW0jTM).

Second, there is a fundamental mismatch between typical benchmark tasks—like solving math problems (GSM8K) or answering trivia (MMLU)—and the complex, nuanced workloads of a real business application [[24]](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches), [[25]](https://arxiv.org/html/2601.20617v1). A model that excels at multiple-choice questions may fail completely at generating long-form creative content, providing empathetic customer support, or performing domain-specific analysis.

The proper role for benchmarks is narrow: they are useful for advancing research frontiers and for initial model filtering during early exploration. They should never be used as a proxy for product-level decisions or become the primary optimization target [[26]](https://launchdarkly.com/blog/llm-evaluation).

If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous. We must instead build metrics that are deeply tied to our specific application.

## Why Custom Business Metrics Over Generic Metrics

Generic, off-the-shelf metrics like "toxicity," "helpfulness," or RAGAS-style "faithfulness" create a mirage. They optimize for the wrong signal and create false confidence because they lack context about your product, user expectations, and brand voice [[27]](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP). An AI application can score brilliantly on a generic "helpfulness" metric but fail catastrophically on your specific business constraints.

A classic example is the F1 score, widely used for imbalanced datasets. While it seems objective, it is considered an "improper" metric for many real-world decisions because a model can improve its F1 score in ways that make business outcomes worse. In medicine, F1 ignores true negatives, yet correctly identifying that a patient *doesn't* need surgery is a critical outcome [[9]](https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation). Similarly, optimizing for perplexity can lead to bland, generic answers that are statistically likely but not useful [[29]](https://toloka.ai/blog/llm-evaluation-from-classic-metrics-to-modern-methods).

Consider the dashboard below. It looks impressive, with scores for "Truthfulness" and "Personalization." But what does a 3.7 in "Personalization" actually mean?

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down
Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"

For example, let's assume we want to check if an article written by our Brown agent contains hallucinations. A generic `hallucination` score might return "positive," but what does that tell us? Did it add information not present in the research? Did it deviate from the article guidelines? Or did it simply include a personal story that, while not in the source text, is factually correct and aligns with the desired brand voice? A generic detector might flag an engaging personal anecdote as a fabrication, yet that same anecdote may be exactly what your brand requires. The generic metric cannot distinguish between undesirable invention and desirable creative elaboration.

Prefab scores are limited because they lack domain-specific constraints, cannot localize which part of an output failed, and introduce statistical noise into decision-making [[28]](https://arxiv.org/html/2508.13816v1), [[29]](https://toloka.ai/blog/llm-evaluation-from-classic-metrics-to-modern-methods).

Generic metrics do have a narrow, valid role, but only during exploratory data analysis. You can use them as a "flashlight" to surface interesting traces for manual review, not as a "report card" for grading overall quality. Here are some useful examples:

1.  **Verbosity:** Sort your outputs by length. This can reveal if your most verbose answers are rambling and unhelpful or if your shortest answers are curt and missing information. This helps you spot failure modes in long-form generation.
2.  **Similarity Score:** Use this to evaluate your RAG retriever specifically. If the similarity between the user query and the retrieved chunks is low, your retriever is likely failing to retrieve relevant information. This is a valid component-level check.
3.  **BERTScore:** Use this to check the quality of your "golden" reference answers. If you find a cluster of outputs with a low BERTScore against a reference you expected to be similar, you might realize the LLM found a more creative, or even better, way to solve the problem than your reference answer.

In all these cases, the generic metric is the start of an investigation, not the final verdict. Every production metric must be deeply application-centric, derived from concrete product requirements, user success criteria, and explicit constraints.

Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments from our LLM judge. Here, binary pass/fail criteria outperform every alternative.

## Choosing Binary Metrics Over Anything Else

When designing these custom metrics, you will face a choice: should you use a Likert scale (e.g., 1-5 stars) or a binary pass/fail? We strongly recommend **binary metrics**.

Likert scales are a seductive trap. They promise nuance but introduce ambiguity and noise. There are three main problems with them [[30]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals):

1.  **Inconsistent Labeling:** The difference between a '3' and a '4' is subjective and varies between annotators, leading to low inter-annotator agreement [[31]](https://www.scribbr.com/methodology/likert-scale). One person's '4' is another's '3', making it difficult to achieve a high Cohen's Kappa score, a measure of rater agreement.
2.  **Statistical Noise:** Detecting a meaningful improvement from an average score of 3.2 to 3.4 requires a much larger sample size than detecting a shift in a binary pass rate from 75% to 80% [[32]](https://www.ellamind.com/blog/binary-vs-likert-scales). You can spend weeks making changes without knowing if you are making progress or just seeing random fluctuations.
3.  **Lazy Decision-Making:** Annotators—and LLM judges—often default to the middle value ('3') to avoid a difficult judgment, hiding uncertainty instead of resolving it [[30]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals). This "satisficing" behavior flattens the signal and masks important failure modes.

Binary evaluations work because they **force decisions**. An output either met a specific criterion or it did not. This simple constraint is incredibly powerful and offers several advantages:

1.  **Clearer Thinking:** Binary evaluations force you to create precise, unambiguous definitions of quality. You cannot simply label something as "Fail" without knowing *why* it failed.
2.  **Consistency:** Binary decisions are faster and more consistent for both human annotators and LLM judges, reducing fatigue and increasing throughput.
3.  **Actionability:** The result is not a fuzzy number but a clear signal tied to a specific problem. A spike in the "Constraint Violation" failure rate tells an engineer exactly where to start debugging.

This noise reduction can be quantified using principles from information theory. Scalar ratings introduce random fluctuations that inflate entropy—a measure of uncertainty—without adding meaningful information. Binary decisions, by contrast, reduce this entropy by forcing a clear judgment, thereby increasing the mutual information between the evaluation signal and the system's true quality [[33]](https://arxiv.org/html/2602.07168).

<aside>
💡
**Note:** The 3 points above translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate the inherent randomness of LLMs. LLMs are much more stable when asked to make a binary decision than when asked to assign a scalar value. A binary metric translates to a more robust and repeatable evaluation pipeline.
</aside>

### Capturing Nuance

The standard objection is, "But I'm losing nuance! A 1-5 scale captures shades of gray." This is a valid concern, but the solution is not a fuzzier scale. The right way to capture nuance is by making your criteria more **granular** [[34]](https://www.ellamind.com/blog/binary-vs-likert-scales).

Instead of a single, subjective rating for "Quality," you break it down into multiple, specific, binary checks. For our writing agent, instead of rating an article 1-5 for "Quality," we create multiple binary evaluations that capture specific dimensions of quality:

1.  **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
2.  **Flow of Ideas Adherence:** Does the generated article present ideas in the same order as the expected article? (Yes/No)
3.  **Article Guideline Adherence:** Does the generated article follow the flow of ideas from the article guideline input? (Yes/No)
4.  **Research Anchoring:** Is every claim in the article supported by the provided research? (Yes/No)

By aggregating these binary signals—using a simple average or a weighted sum—you get a nuanced, multi-dimensional view of performance. This approach eliminates scale noise and middle-value bias, resulting in a system that is simple, intuitive, scalable, and robust.

With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in the next lesson.

## Conclusion

This lesson argued for a fundamental shift away from vibe checks, leaderboards, and generic scores toward a rigorous, evaluation-driven development process. This process is built on custom, binary, business-aligned metrics that provide a clear and actionable signal for improvement. We have established that granular pass/fail criteria deliver the strongest optimization signal while avoiding the statistical noise and subjectivity inherent in scalar ratings. This theoretical foundation is the key to building reliable AI products.

This theoretical foundation is the key to building reliable AI products. In the next lesson, we will translate this theory into practice by implementing custom LLM judges from scratch to evaluate our Brown writing workflow.

## References

- [1] [Vibe Checks Are All You Need](https://olshansky.substack.com/p/vibe-checks-are-all-you-need)
- [2] [AI Evals vs A/B Testing: Why You Need Both to Ship GenAI](https://www.growthbook.io/blog/ai-evals-vs-a-b-testing-why-you-need-both-to-ship-genai)
- [3] [A Powerful Data Flywheel for De-Risking Agentic AI](https://galileo.ai/blog/nvidia-data-flywheel-for-de-risking-agentic-ai)
- [4] [What Is a Data Flywheel?](https://www.nvidia.com/en-us/glossary/data-flywheel)
- [5] [Causal inference in product experimentation](https://www.statsig.com/perspectives/causal-inference-in-product-experimentation)
- [6] [Sequential Minimal Optimization for SVM](http://www.jmlr.org/papers/volume7/MLOPT-intro06a/MLOPT-intro06a.pdf)
- [7] [Practical Significance: What It Is and How to Report It](https://www.nngroup.com/articles/practical-significance)
- [8] [Understanding Statistical Significance and How to Use It](https://www.statsig.com/perspectives/understanding-statistical-significance)
- [9] [Three Metrics for Healthcare AI Evaluation You Need to Know](https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation)
- [10] [Effective uses of effect size statistics to demonstrate business value](https://www.quirks.com/articles/effective-uses-of-effect-size-statistics-to-demonstrate-business-value)
- [11] [Manage Evaluation Datasets in Opik](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets)
- [12] [Generate Synthetic Datasets for AI Evals](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals)
- [13] [Understanding BLEU and ROUGE score for NLP evaluation](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb)
- [14] [Demystifying the BLEU Metric](https://www.traceloop.com/blog/demystifying-the-bleu-metric)
- [15] [LLM evaluation benchmarking: Beyond BLEU and ROUGE](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ)
- [16] [Evaluating RAG: A Practical Guide to Evaluation Metrics](https://www.elastic.co/search-labs/blog/evaluating-rag-metrics)
- [17] [What is LLM-as-a-Judge?](https://www.braintrust.dev/articles/what-is-llm-as-a-judge)
- [18] [LLM-as-a-judge: a complete guide to using LLMs for evaluations](https://www.evidentlyai.com/llm-guide/llm-as-a-judge)
- [19] [LinkedIn post by Alla Abdella on LLM as a Judge](https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw)
- [20] [LLM As A Judge](https://cameronrwolfe.substack.com/p/llm-as-a-judge)
- [21] [LLM Benchmarks: 30+ LLM Evaluation Benchmarks and How They Work](https://www.evidentlyai.com/llm-guide/llm-benchmarks)
- [22] [AI — Benchmark scores are becoming marketing; dynamic eval is the only antidote](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053)
- [23] [PROBE: BENCHMARKING REASONING PARADIGM OVERFITTING IN LARGE LANGUAGE MODELS](https://openreview.net/forum?id=XbVMiW0jTM)
- [24] [LLM Evaluation: 4 Approaches to Large Language Model Evaluation](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches)
- [25] [Benchmarks for Agentic AI in the Public Sector](https://arxiv.org/html/2601.20617v1)
- [26] [LLM Evaluation: How to Evaluate LLM Applications](https://launchdarkly.com/blog/llm-evaluation)
- [27] [LinkedIn post by Shivanshu Aggarwal on generic metrics](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP)
- [28] [A Meta-Evaluation of Evaluation Metrics for Text Generation](https://arxiv.org/html/2508.13816v1)
- [29] [LLM Evaluation: From Classic Metrics to Modern Methods](https://toloka.ai/blog/llm-evaluation-from-classic-metrics-to-modern-methods)
- [30] [The 5-Star Lie: You’re Doing AI Evaluations Wrong](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals)
- [31] [Likert Scale: Examples and how to use it](https://www.scribbr.com/methodology/likert-scale)
- [32] [Binary vs. Likert Scales in AI Evaluation](https://www.ellamind.com/blog/binary-vs-likert-scales)
- [33] [Information Theory Quantifies Noise Reduction](https://arxiv.org/html/2602.07168)
- [34] [How granular binary criteria capture nuance for writing agents](https://www.ellamind.com/blog/binary-vs-likert-scales)
- [35] [Building Quality Gates for AI-Generated Code with Practical Implementation Strategies](https://www.softwareseni.com/building-quality-gates-for-ai-generated-code-with-practical-implementation-strategies)