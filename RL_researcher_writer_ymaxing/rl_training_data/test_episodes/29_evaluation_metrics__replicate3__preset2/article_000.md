# Evaluation-Driven Development: The North Star of AI Engineering

In our previous lessons, we instrumented our agents with observability tools like Opik and constructed offline datasets to capture their behavior. Now, we move to the core theoretical framework for designing the metrics themselves. In classical machine learning, we rely on rigorous standards like accuracy, precision, recall, and F1 scores to measure performance. Yet, in AI engineering, many teams fall back on "vibe checks," approving changes because an output "feels more coherent."

Prioritizing a robust evaluation layer is difficult. It delivers no immediate, user-visible features and requires significant upfront effort to design datasets and metrics. This investment competes with the constant pressure to ship new functionality. However, that same investment dramatically accelerates long-term iteration. It provides an objective signal on every change, catches regressions instantly, and transforms development from a speculative art into an engineering discipline.

Evals are the north star of AI engineering. They are the single source of truth that tells you exactly which modifications improve your system and which degrade it.

In this lesson, we will explore this evaluation-driven framework. We will cover:

*   The optimization flywheel and its three core use cases.
*   Trade-offs between different metric types for unstructured outputs.
*   Why business-aligned metrics beat public benchmarks and generic scores.
*   Why binary pass/fail judgments are superior to Likert scales.

With the problem and its importance clear, we will now examine how to operationalize evaluations inside a repeatable optimization flywheel that replaces intuition with evidence.

## Using Evals Through the Optimization Flywheel

To build intuition, let's examine how we can effectively use and integrate AI evaluations into our application development lifecycle. There are three core scenarios where evaluations provide value. First, evals **quantify the quality of your system** on a given set of metrics, creating a baseline snapshot of its current performance. Without a baseline, you cannot know if your system is ready for production or if it is improving.

Second, these metrics serve as **guidance when optimizing your system**. They provide objective evidence for experiments, shifting development from being intuition-based to evidence-based. Finally, evals act as **regression tests** that protect shared components. Unlike optimization, the goal here is stability. This is critical in AI engineering, as components are often interconnected; a small change in a prompt can have unintended consequences elsewhere.

### The Optimization Process

How does this look in a real-world scenario? The optimization flywheel provides a step-by-step plan of attack. It is an iterative process for systematically improving your AI application.

![Image 1: The iterative optimization flywheel for AI applications using evaluations.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-4d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down)

Image 1: The iterative optimization flywheel for AI applications using evaluations.

The process consists of eight steps:

1.  **Gather your dataset:** Assemble an offline dataset that covers diverse use cases, edge cases, and failure modes.
2.  **Build your metrics:** Define a suite of business-aligned metrics that measure what truly matters for your application's success.
3.  **Establish a baseline:** Run your evaluation suite on the current system to compute baseline scores for each metric.
4.  **Start the optimization:** Make one isolated change that you believe will improve performance, such as modifying a prompt or swapping a model.
5.  **Compute the new score:** Re-evaluate the entire dataset by re-running the full evaluation suite on the modified system.
6.  **Compare:** Compare the new scores to the baseline, assessing statistical significance to ensure the change is not just noise.
7.  **Decide:** Based on whether the scores are better, the same, or worse, decide to keep the change, revert it, or conduct further analysis.
8.  **Repeat:** Continue this cycle, making one change at a time, until the scores meet your target for production readiness.

It is critical to keep all components fixed except for one variable per cycle. Modifying multiple things at once makes it impossible to attribute score changes to a specific cause, turning a disciplined process back into guesswork. This principle of single-variable isolation is borrowed from classical control theory, which optimizes complex systems by analyzing single-input, single-output feedback loops. By changing only one variable at a time, you ensure that any observed performance change can be confidently attributed to that specific modification, maintaining the stability of the optimization process [[1]](https://en.wikipedia.org/wiki/Control_theory).

Furthermore, statistical significance must be anchored to actual **business impact**, not arbitrary p-values. A tiny numerical improvement might be negligible for a low-volume creative writing tool, where large movements are needed to declare victory. However, for a high-volume support bot, even a small improvement can have a massive real-world gain. For example, a 0.5% reduction in checkout errors may sound small, but for a product processing two million checkouts annually, it translates to 10,000 fewer failed transactions. If each failure costs the business $15, that small improvement is worth $150,000 per year [[2]](https://www.nngroup.com/articles/practical-significance). "Better" is always relative to the business use case.

It is helpful to think of your evaluation metrics as proxies for the real-world outcomes you care about. The score itself is not the goal; the user experience is. This proxy is only valid as long as it tracks the actual outcome. Therefore, your evaluation process must include periodic validation against online business metrics to ensure your offline scores genuinely predict production performance and haven't drifted away from what users actually value [[3]](https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork).

### Regression Testing

A variation of this flywheel serves as a powerful regression testing framework. Before merging any feature that touches shared components—prompts, tool descriptions, or memory retrieval—you run the full evaluation suite. This guards against breaking existing functionality. This is an extremely powerful technique to ensure new features do not degrade performance elsewhere.![Image 2: Integrating AI evaluations into CI pipelines for regression testing.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down)

Image 2: Integrating AI evaluations into CI pipelines for regression testing.

This process can be simplified into five steps:

1.  **Implement a new feature:** You write the code and verify it works locally for the new use case.
2.  **Run the AI evaluations:** You run the full suite of assessments, covering all previous use cases, not just the new one.
3.  **Compare Scores:** You compare the new evaluation scores against the established baseline.
4.  **Metrics similar to baseline:** If the scores are identical or better, the feature has not introduced a regression and can be merged.
5.  **Metrics lower than the baseline:** If any score is worse, you have introduced a regression. You must fix the code and repeat the process.

This treats evals like integration tests, but with a crucial difference: instead of a strict pass/fail threshold, you often compare scores against a moving baseline. The goal is to prevent degradation, not to demand perfection on every run. This approach parallels the shift from traditional Test-Driven Development (TDD) to Evaluation-Driven Development (EDD). While TDD asks a binary question—"Does it work?" (Yes/No)—EDD asks a qualitative one: "How well does it work?" This reframes testing from a simple check for correctness to a continuous process of quantifying performance against a spectrum of quality [[4]](https://medium.com/@nimrodbusany_9074/from-tdd-to-edd-why-evaluation-driven-development-is-the-future-of-ai-engineering-a5e5796b2af4).

Your evaluation dataset must continuously expand. New edge cases discovered for features, production failures captured via observability tools like Opik, and hard examples found during debugging should all be added to the dataset [[5]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets). Instead of writing new tests in code, you broaden your test coverage by adding new, challenging samples. For instance, if a production trace reveals a regression, you can convert that trace into a new dataset item to ensure the same failure is caught automatically in the future [[6]](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals).

With the mechanics of the flywheel clear, we can now examine the different families of metrics we might plug into it when dealing with unstructured outputs.

## Exploring Possible Metric Types

The core difficulty in evaluating AI systems is that we are often working with unstructured text, reasoning traces, or even images. Standard metrics like accuracy are unavailable, forcing us to explore other families of metrics.

### BLEU and ROUGE

N-gram overlap metrics like BLEU and ROUGE are fast, deterministic, and widely understood. They work by calculating the lexical overlap between the generated output and a reference text [[7]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ), [[8]](https://www.traceloop.com/blog/demystifying-the-bleu-metric). However, they are blind to semantic meaning. They penalize correct answers that use different phrasing or paraphrasing and do not check for factual accuracy, making them brittle for modern LLM applications [[7]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ), [[9]](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb).

### BERTScore

Embedding similarity metrics like BERTScore address the semantic blindness of n-gram methods. They embed both the generated and reference texts into a high-dimensional vector space and measure their cosine similarity [[7]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ). This captures semantic closeness, making it better at recognizing paraphrases. However, it remains a comparison-based metric and cannot verify complex business rules or logic on its own.

### LLM Judges

The LLM-as-a-judge approach uses a capable model to evaluate an output based on detailed criteria. You provide the judge with the input, the output, a rubric, few-shot examples, and chain-of-thought instructions [[10]](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method), [[11]](https://arize.com/llm-as-a-judge). This method is highly flexible and can be customized to evaluate subjective qualities and complex, domain-specific requirements [[12]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge). For example, a judge can check if a response adheres to a specific brand voice or legal constraint.

The main downside is that LLM judges can be slower, more expensive, and their performance depends heavily on the prompt and the evaluator model [[12]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge), [[13]](https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw). Without proper validation, they can also inherit biases from the underlying LLM [[14]](https://cameronrwolfe.substack.com/p/llm-as-a-judge). To mitigate these issues, LLM judges require a systematic calibration process before being used in production. This involves an iterative loop: run the judge on a representative set of labeled data, review disagreements between the judge and human labels, and then refine the evaluation criteria or few-shot examples accordingly. This helps you understand how the judge fails before you trust its outputs [[15]](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production). Other techniques, like combining multiple judgments weighted by token probabilities, can also help smooth out biases and increase consistency [[16]](https://www.reddit.com/r/LLMDevs/comments/1j3gbil/5_techniques_to_improve_llmjudges).

| Metric Family | Speed | Cost | Semantic Awareness | Business Alignment | Explainability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BLEU/ROUGE** | High | Low | Low | Low | Medium |
| **BERTScore** | Medium | Low | High | Medium | Low |
| **LLM Judges** | Low | High | High | High | High |

Table 1: A comparison of trade-offs between different evaluation metric families.

For the complex requirements of our capstone writing workflow, such as guideline adherence and research grounding, LLM judges are the most practical choice.

You have heard us repeatedly mention "business metrics." Let's now understand why defining your own business metrics is such an essential and underrated step in building your AI evaluation strategy.

## Why Business Metrics Over Benchmarks

Using popular leaderboards or public benchmarks to choose a model or make product decisions is often a mistake. Benchmarks are the most deceiving type of metric for two core reasons.

First, public benchmarks often function as marketing artifacts. Once a test set is public, models can be fine-tuned on it to inflate scores, and teams "teach to the test" [[17]](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053). The benchmark loses its validity as a measure of performance on unseen data. This can lead to inflated scores that misrepresent a model's true reasoning ability [[18]](https://openreview.net/forum?id=XbVMiW0jTM). This issue, known as data contamination, invalidates the benchmark's ability to measure generalization [[19]](https://medium.com/@yujiisobe/navigating-the-maze-of-llm-evaluation-a-guide-to-benchmarks-rag-and-agent-assessment-fb7aef299e66). Worse, even without direct fine-tuning, the common practice of iterative prompt engineering against a benchmark is a form of implicit training on the evaluation data, repeating early mistakes from machine learning history where the line between training and test sets became blurred [[20]](https://openreview.net/forum?id=maMnVCHl8J).

Second, there is a fundamental mismatch between typical benchmark tasks (like math problems or generic question-answering) and real-world business workloads (like long-form creative writing or nuanced legal analysis) [[21]](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches), [[22]](https://arxiv.org/html/2601.20617v1). A model that excels at a standardized test may still fail at your specific application [[23]](https://www.evidentlyai.com/llm-guide/llm-benchmarks).

The proper role for benchmarks is narrow: they are useful for advancing research, and for initial model filtering during early exploration. They should never be the primary target for product-level optimization [[24]](https://launchdarkly.com/blog/llm-evaluation).

If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous. We must instead build metrics that are deeply tied to our specific application.

## Why Custom Business Metrics Over Generic Metrics

Generic metrics for qualities like "toxicity," "helpfulness," or "hallucination" create a mirage. They optimize for the wrong signal and build false confidence because they lack context about your product, users, and brand voice [[25]](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP). A model can score brilliantly on a generic "helpfulness" metric but fail catastrophically on your specific constraints.

Consider the dashboard below. It looks impressive, with scores for "Truthfulness" and "Personalization." But what does a 3.7 in "Personalization" actually mean?![Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down)

Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"

For example, let's assume we want to check if an article written by our Brown agent contains hallucinations. If we use a generic `hallucination` score and it returns "positive," what does that tell us? Did it add information not present in the research? Did it deviate from the article guidelines? Or did it simply include a personal story that was not in the source text but is factually correct and relevant?

A generic detector might flag an engaging personal anecdote as a fabrication, yet that same anecdote may be exactly what your brand voice requires. The generic metric cannot distinguish between undesirable invention and desirable creative elaboration.

These prefab scores lack domain-specific constraints, cannot localize which part of an output failed, and introduce statistical noise into your decision-making [[26]](https://arxiv.org/html/2508.13816v1), [[27]](https://toloka.ai/blog/llm-evaluation-from-classic-metrics-to-modern-methods).

Generic metrics do have a narrow, valid role during exploratory data analysis. You can use them as a "flashlight, not a report card," to surface interesting examples for manual review. Here are some examples:

1.  **Verbosity:** Sorting outputs by length can reveal if your most verbose answers are rambling and unhelpful, helping you spot failure modes in long-form generation.
2.  **Similarity Score:** You can use this to evaluate your RAG retriever. If the similarity between the user query and retrieved chunks is low, your retriever is likely failing. This is a valid component-level check.
3.  **BERTScore:** This can help check the quality of your golden references. If a cluster of outputs has a low BERTScore against a reference you expected to be similar, the LLM might have found a better way to solve the problem.

Ultimately, every production metric must be application-centric, derived from concrete product requirements, user success criteria, and explicit constraints.

Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments from our LLM judge. Here, binary pass/fail criteria outperform every alternative.

## Choosing Binary Metrics Over Anything Else

When designing custom metrics, you face a choice: should you use a Likert scale (e.g., 1-5 stars) or a binary pass/fail judgment? We strongly recommend **binary metrics**.

Likert scales are plagued with problems:

1.  **Inconsistent Labeling:** The difference between a '3' and a '4' is subjective and varies between annotators, making it difficult to achieve high inter-annotator agreement [[28]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals). One person's '4' is another's '3'.
2.  **Statistical Noise:** Detecting a real improvement, like an average score moving from 3.2 to 3.5, requires a much larger sample size than detecting a shift in a binary pass rate from 60% to 70% [[29]](https://www.ellamind.com/blog/binary-vs-likert-scales). You end up uncertain if you are making progress or seeing random fluctuations.
3.  **Lazy Decision-Making:** Raters often default to the middle value ('3') to avoid a difficult judgment. This "satisficing" behavior hides uncertainty rather than resolving it, leaving you with a vague signal that your system is just "okay" [[28]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).

Binary evaluations work because they **force decisions**. The benefits are immediate:

1.  **Clearer Thinking:** You cannot hide in ambiguity. An output either met a specific criterion or it did not. This sharpens your definitions of quality.
2.  **Consistency:** Binary decisions are faster and more consistent for both human and AI evaluators, leading to more reliable data.
3.  **Actionability:** The output is a clear signal tied to a specific problem. A spike in the failure rate for "Constraint Violation" tells an engineer exactly where to start debugging.

<aside>
💡
**Note:** The three points above translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate their inherent randomness. An LLM is far more stable making a binary decision than assigning a scalar value, and the results can be analyzed with simple, interpretable classification metrics [[30]](https://cameronrwolfe.substack.com/p/finetuned-judge). In fact, breaking a complex evaluation into a series of fine-grained binary questions is a recognized technique for improving judge reliability [[16]](https://www.reddit.com/r/LLMDevs/comments/1j3gbil/5_techniques_to_improve_llmjudges).

</aside>

### Capturing Nuance

The standard objection is, "But I'm losing nuance! A 1-5 scale captures shades of gray."

You can capture nuance without reintroducing subjectivity. Instead of using a fuzzier scale, you make your criteria more **granular**. You decompose a complex quality into multiple, specific, binary checks [[29]](https://www.ellamind.com/blog/binary-vs-likert-scales).

For our writing agent, instead of rating an article 1-5 for "Quality," we can create multiple binary evaluations:

1.  **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
2.  **Flow of Ideas Adherence:** Does the generated article present ideas in the same order as the expected article? (Yes/No)
3.  **Article Guideline Adherence:** Does the generated article follow the flow of ideas from the article guideline input? (Yes/No)
4.  **Research Anchoring:** Is every claim in the article supported by the provided research? (Yes/No)

Aggregating these binary signals provides a nuanced view. A score of 4/4 is a strong quality signal, while 2/4 tells you not only that the article failed but also precisely which dimensions it failed on. This approach yields granular, actionable insights while eliminating the noise and bias of scalar ratings.

However, for highly creative tasks, even granular binary checks can have blind spots. They may struggle to detect high-level failures like an incomplete narrative or a lack of coherence, as these qualities are hard to distill into simple Yes/No criteria without a ground truth reference [[31]](https://www.linkedin.com/posts/pauliusztin_i-created-an-ai-agent-to-write-a-substack-activity-7420095430807691266-fQ1U), [[32]](https://www.mdpi.com/2076-3417/15/6/2971). Calibrating your metrics to be aware of what they might miss remains essential.

With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in the next lesson.

## Conclusion

The path to robust AI products requires a shift away from vibe checks, leaderboards, and generic scores. The alternative is a rigorous, evaluation-driven development process built on custom, binary, and business-aligned metrics. Granular pass/fail criteria provide the clearest optimization signal, avoiding the statistical noise and subjectivity inherent in scalar ratings.

This framework is the engine of product improvement. In our next lesson, we will translate this theory into practice by implementing custom LLM judges from scratch to evaluate our Brown writing workflow.

## References

- [1]  https://en.wikipedia.org/wiki/Control_theory
- [2]  https://www.nngroup.com/articles/practical-significance
- [3]  https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork
- [4]  https://medium.com/@nimrodbusany_9074/from-tdd-to-edd-why-evaluation-driven-development-is-the-future-of-ai-engineering-a5e5796b2af4
- [5]  https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets
- [6]  https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals
- [7]  https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ
- [8]  https://www.traceloop.com/blog/demystifying-the-bleu-metric
- [9]  https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb
- [10]  https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method
- [11]  https://arize.com/llm-as-a-judge
- [12]  https://www.evidentlyai.com/llm-guide/llm-as-a-judge
- [13]  https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw
- [14]  https://cameronrwolfe.substack.com/p/llm-as-a-judge
- [15]  https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production
- [16]  https://www.reddit.com/r/LLMDevs/comments/1j3gbil/5_techniques_to_improve_llmjudges
- [17]  https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053
- [18]  https://openreview.net/forum?id=XbVMiW0jTM
- [19]  https://medium.com/@yujiisobe/navigating-the-maze-of-llm-evaluation-a-guide-to-benchmarks-rag-and-agent-assessment-fb7aef299e66
- [20]  https://openreview.net/forum?id=maMnVCHl8J
- [21]  https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches
- [22]  https://arxiv.org/html/2601.20617v1
- [23]  https://www.evidentlyai.com/llm-guide/llm-benchmarks
- [24]  https://launchdarkly.com/blog/llm-evaluation
- [25]  https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP
- [26]  https://arxiv.org/html/2508.13816v1
- [27]  https://toloka.ai/blog/llm-evaluation-from-classic-metrics-to-modern-methods
- [28]  https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals
- [29]  https://www.ellamind.com/blog/binary-vs-likert-scales
- [30]  https://cameronrwolfe.substack.com/p/finetuned-judge
- [31]  https://www.linkedin.com/posts/pauliusztin_i-created-an-ai-agent-to-write-a-substack-activity-7420095430807691266-fQ1U
- [32]  https://www.mdpi.com/2076-3417/15/6/2971
- [Using LLM-as-a-Judge For Evaluation: A Complete Guide](https://hamel.dev/blog/posts/llm-judge/)
- [Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)](https://eugeneyan.com/writing/llm-evaluators/)
- [Benchmark Overfitting in Large Language Models](https://openreview.net/forum?id=XbVMiW0jTM)
- [The Mirage of Generic AI Metrics](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics)
- [The 5-Star Lie: You’re Doing AI Evaluations Wrong](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals)
- [Escaping POC Purgatory: Evaluation-Driven Development for AI Systems](https://www.decodingai.com/p/escaping-poc-purgatory-evaluation)
- [Stop Launching AI Apps Without This Framework](https://www.decodingai.com/p/stop-launching-ai-apps-without-this)
- [Evaluating NLP Models: A Comprehensive Guide to ROUGE, BLEU, METEOR, and BERTScore Metrics](https://plainenglish.io/blog/evaluating-nlp-models-a-comprehensive-guide-to-rouge-bleu-meteor-and-bertscore-metrics-d0f1b1)
- [Key NLP Evaluation Metrics](https://datumo.com/en/blog/insight/key-nlp-evaluation-metrics/)
- [BERTScore explained: A modern metric for evaluating text generation](https://spotintelligence.com/2024/08/20/bertscore/)