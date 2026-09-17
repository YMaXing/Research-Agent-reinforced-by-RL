# Evaluation-Driven Development: Your North Star for AI Engineering

In our previous lessons, we instrumented our AI agents with observability tools like Opik and constructed offline datasets for evaluation. We now have the raw materials: the traces and the test cases. With this foundation in place, we can now move to the core theoretical framework of designing the metrics themselves.

In classical Machine Learning, we operate with a high degree of rigor. We rely on well-defined metrics like accuracy, precision, recall, and F1 scores, and we anchor our findings in statistical significance. Yet, in AI engineering, it has become common to rely on "vibe checks" or to skip evaluation entirely. We often hear things like, "this output *feels* more coherent," without any data to back it up.

Investing in a proper evaluation layer can feel difficult to prioritize. It does not deliver an immediate, user-visible feature. It requires upfront effort to design datasets and metrics, and it competes with the pressure to ship new functionality. However, this investment is what separates prototypes from production-grade systems. It substantially accelerates long-term iteration by providing an objective signal on every change and catching regressions instantly.

Evals are the north star of AI engineering: the single source of truth that tells you exactly which modifications improve your system and which degrade it. In this lesson, we will cover the complete theoretical framework for building this evaluation layer. We will explore:

*   The optimization flywheel and its three core use cases.
*   The trade-offs between different metric types for unstructured outputs.
*   Why custom business metrics are superior to public benchmarks and generic scores.
*   Why binary pass/fail judgments are more effective than Likert scales.

With the problem and its importance now clear, we will examine how to operationalize evaluations inside a repeatable optimization flywheel that replaces intuition with evidence.

## Using Evals Through the Optimization Flywheel

To build intuition, let's examine how we can effectively use and integrate AI evaluations into our application development lifecycle. There are three core scenarios where evaluations provide value.

First, evals **quantify the quality of your system** on a given set of metrics, creating a baseline snapshot of its current performance. Without this baseline, you cannot know if your system is ready for production or if subsequent changes are making it better or worse. Second, these metrics serve as **guidance when optimizing your system**. They provide objective evidence for experiments, shifting development from being intuition-based to evidence-based. Finally, they act as **regression tests** that protect shared components. Unlike optimization, the goal here is stability. This is critical in AI engineering, as components are often interconnected, and a small change in one area can have unintended consequences elsewhere.

### The Optimization Process

How does this look in a real-world scenario? Let's look at a step-by-step plan of attack for the optimization flywheel.

1.  **Gather your dataset:** You start by assembling an offline dataset that represents the real-world scenarios your application will face, as we did in Lesson 28. This dataset should be diverse enough to cover common use cases, edge cases, and known failure modes.
2.  **Build your metrics:** You define a set of metrics that are aligned with your business goals. These metrics should be specific, measurable, and relevant to the user's success. We will cover how to do this later in this lesson.
3.  **Establish a baseline:** You run your evaluation suite on the current version of the system to compute baseline scores for each metric. This baseline is your single source of truth for current performance.
4.  **Start the optimization:** You make a single, isolated change that you believe will improve performance. This could be a prompt tweak, a change in the retrieval strategy, swapping out the LLM, or modifying a tool's logic.
5.  **Compute the new score:** You re-evaluate the entire dataset by re-running the evaluation suite on the modified system. It is essential to run it on the full dataset to ensure the change did not introduce regressions in other areas.
6.  **Compare:** You compare the new scores to the baseline, checking for statistical significance. This step quantifies the impact of your change, telling you if the observed improvement is real or just noise.
7.  **Decide:** Based on whether the score is better, the same, or worse, you decide whether to keep the change, revert it, or conduct further analysis. This decision should also factor in the complexity and cost of the change.
8.  **Repeat:** You repeat this cycle, continuously iterating and improving the system until the scores meet your target for production readiness.

This iterative process turns what is often a chaotic, intuition-driven guessing game into a disciplined, evidence-based engineering practice.![Image 1: The iterative optimization flywheel for AI applications using evaluations.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-4d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down)
Image 1: The iterative optimization flywheel for AI applications using evaluations.

It is critical to keep all components fixed except for one variable per cycle. If you change the prompt, the model, and the chunking strategy all at once, it becomes impossible to attribute any score movements to a specific cause. This confounding of variables turns the process back into guesswork and undermines the entire point of a systematic evaluation framework. By isolating changes, you can confidently attribute improvements or regressions to specific modifications, making your optimization efforts more effective.

When comparing scores, it is important to anchor statistical significance to actual **business impact** rather than arbitrary p-value thresholds. "Better" is always relative to the specific business use case. A result has practical significance if the size of the difference is large enough to meaningfully affect real-world outcomes, regardless of the p-value.

For example, for a high-volume customer support bot that handles millions of interactions, a tiny improvement of 0.5% in reducing checkout errors could translate to thousands of fewer failed transactions and significant cost savings. In this context, even a small, statistically significant improvement has a massive real-world gain. In contrast, for a low-volume creative writing tool, a similar small improvement is likely negligible. A much larger movement would be required before declaring a victory [[1]](https://www.nngroup.com/articles/practical-significance).

### Regression Testing

The flywheel can also be adapted for regression testing. Before merging any new feature that touches shared prompts, tool descriptions, orchestration logic, or memory retrieval, you run the full evaluation suite against the offline dataset to guard against breaking existing behavior. Running AI evaluations as regression tests is an extremely powerful technique to ensure that your new features do not break existing ones.

The strategy can be adapted from the optimization flywheel to five steps:

1.  **Implement a new feature:** You write the code and verify it works locally for the new use case.
2.  **Run the AI evaluations:** You run the full suite of assessments, covering all previous use cases, not just the new one.
3.  **Compare Scores:** You compare the new evaluation scores against the established baseline for your production codebase.
4.  **Metrics similar to baseline:** If the scores are identical or within an acceptable range of the baseline, your feature has not introduced any regressions. You can merge it.
5.  **Metrics lower than the baseline:** If the scores are worse, you have introduced a regression. You should fix your code and repeat the process until the scores return to the baseline.![Image 2: Integrating AI evaluations into CI pipelines for regression testing.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down)
Image 2: Integrating AI evaluations into CI pipelines for regression testing.

This approach treats evaluations similarly to unit or integration tests, but with a key difference: instead of enforcing a strict pass/fail threshold, we often compare scores against a moving baseline. This allows for managed evolution while preventing unintended degradation.

For this process to work, the dataset must continuously expand. As new features are added, you must include their specific edge cases. As failures are captured in production via observability and tracing tools like Opik, these real-world examples should be converted into new dataset items. Hard-to-debug examples that expose current failure modes should also be added [[4]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets).

Instead of writing new tests in code, you broaden the test coverage by adding new samples to the dataset. For example, if you discover a production regression where the agent fails to handle a specific query format, you can add that exact production trace to your dataset. This ensures the fix is validated and the regression never reoccurs, making your evaluation suite a living, evolving representation of your product's required behavior [[5]](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals).

With the mechanics of the flywheel now clear, we can examine the different families of metrics we might plug into it when dealing with unstructured text and image outputs.

## Exploring Possible Metric Types

The core difficulty in evaluating AI systems is that we are often dealing with unstructured outputs like text, reasoning traces, or images. Unlike classical ML with its structured labels, standard accuracy-style metrics are often unavailable. This has led to the development of several families of metrics, each with its own trade-offs.

### 1. BLEU and ROUGE

Metrics like BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Oriented Understudy for Gisting Evaluation) are based on lexical overlap. They work by counting the number of overlapping n-grams (sequences of words) between the generated text and a reference text. Their pros include being fast to compute, widely understood, and deterministic. However, they are blind to semantic meaning. They cannot recognize paraphrasing and will penalize a perfectly correct response simply because it uses different words than the reference. They also cannot assess the validity of reasoning or factual accuracy [[6]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ), [[7]](https://www.traceloop.com/blog/demystifying-the-bleu-metric), [[8]](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb).

### 2. BERTScore

Embedding similarity metrics, such as BERTScore, address the semantic limitations of n-gram metrics. They use a language model like BERT to embed both the generated and reference texts into a high-dimensional vector space. The similarity between these embeddings, often measured by cosine similarity, serves as the evaluation score. This approach is better at capturing semantic closeness and is more robust to paraphrasing. However, it is still a comparison-based metric and cannot verify complex business rules or logical correctness on its own. Furthermore, it is more computationally expensive and less interpretable than lexical methods.

### 3. LLM Judges

The LLM-as-a-judge approach uses a powerful LLM to evaluate the output of another model. You provide the judge model with the input, the generated output, a set of detailed criteria, few-shot examples, and chain-of-thought instructions. The judge then produces a score or a verdict. This method is highly flexible and can be customized to evaluate against complex, domain-specific requirements. It can assess subjective qualities like tone and provide detailed, human-like critiques. However, its performance depends heavily on the quality of the prompt and the evaluator model. LLM judges can be slower, more expensive, and may inherit the biases of the underlying LLM if not carefully developed and tested [[9]](https://www.braintrust.dev/articles/what-is-llm-as-a-judge), [[10]](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method), [[11]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge), [[12]](https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw).

| Metric Family | Speed | Cost | Semantic Awareness | Business Alignment | Explainability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BLEU/ROUGE** | High | Low | Low | Low | Low |
| **BERTScore** | Medium | Low | Medium | Medium | Low |
| **LLM Judges** | Low | High | High | High | High |

Table 1: A trade-off summary of different metric families.

For the complex requirements of our capstone projects, such as guideline adherence, structure fidelity, and research grounding in the writing workflow, LLM judges are the most practical choice. They offer the necessary flexibility to encode our specific business logic.

Now, you have probably heard from us multiple times: *"business metrics here, business metrics there"*. Thus, let's understand why defining your own business metrics is such an essential and underrated step in building your AI evaluation strategy.

## Why Business Metrics Over Benchmarks

It is a common mistake to look at popular leaderboards or open benchmarks to select an LLM and make product decisions. Benchmarks are often the most deceiving type of metric, and relying on them can lead you astray for two core reasons.

First, benchmarks often function as marketing artifacts. Once a test set becomes public, teams can inadvertently or deliberately overfit to it. Models can be fine-tuned on test sets to inflate their scores, a practice that undermines the validity of the benchmark. For instance, research on reasoning benchmarks has shown that models can learn to memorize solution *paradigms* for specific problem types, rather than developing generalizable reasoning skills. This form of overfitting means a high score may not reflect true capability on novel problems [[18]](https://openreview.net/forum?id=XbVMiW0jTM). As models "conquer" a benchmark, it loses its ability to measure true progress, as the scores no longer represent performance on unseen data [[13]](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053), [[14]](https://launchdarkly.com/blog/llm-evaluation), [[15]](https://www.evidentlyai.com/llm-guide/llm-benchmarks).

Second, there is a fundamental mismatch between the tasks in most public benchmarks and the demands of real business workloads. A model's ability to solve grade-school math problems (like those in GSM8K) or answer multiple-choice questions (like in MMLU) tells you very little about its capacity for long-form creative writing, nuanced legal analysis, or personalized customer support [[16]](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches).

Benchmarks do have a proper, narrow role. They are useful for advancing research frontiers and for initial model filtering during the early exploration phase of a project. However, they should never be used as a proxy for product-level decisions or as the primary target for optimization.

If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous; we must instead build metrics that are deeply tied to our specific application.

## Why Custom Business Metrics Over Generic Metrics

Generic, off-the-shelf metrics for qualities like "toxicity," "helpfulness," or "hallucination" create a mirage. They can lead you to optimize for the wrong signal and build false confidence because they lack context about your product, your users, and your brand voice. A model can score brilliantly on a generic "helpfulness" metric but fail catastrophically on your specific constraints.

Consider the dashboard below. It looks impressive, with scores for "Truthfulness" and "Personalization." But what does a 3.7 in "Personalization" actually mean? These abstract scores are often impossible to act on. They create the illusion of progress while masking the failures that actually matter to users [[17]](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP).![Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down)
Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"

For example, a real estate assistant designed to schedule property viewings might receive a high "helpfulness" score for proposing viewing times, but if those times are when the agent is unavailable, it has failed at its core task. The generic metric completely misses this critical functional error.

Let's assume we want to check if an article written by our Brown agent contains hallucinations. If we use a generic `hallucination` score and it returns "positive," what does that tell us? Did it add information not present in the research? Did it deviate from the article guidelines? Or did it simply include a personal story that was not in the source text but is factually correct and relevant? A generic detector might flag an engaging personal anecdote as a fabrication, but that same anecdote may be exactly what your brand voice requires. The generic metric cannot distinguish between undesirable invention and desirable creative elaboration.

These prefab scores lack domain-specific constraints, cannot localize which part of an output failed, and introduce statistical noise into your decision-making.

Generic metrics do have a narrow, valid role during exploratory data analysis. You can use them as a "flashlight" to surface interesting examples for manual review, but never as the primary optimization target. Here are a few useful examples:

1.  **Verbosity:** Sort your outputs by length. This might reveal that your most verbose answers are rambling and unhelpful, while your least verbose ones are curt and missing information. This helps you spot failure modes in long-form generation.
2.  **Similarity Score:** Use this to evaluate your RAG retriever specifically. If the similarity between the user query and the retrieved chunks is low, your retriever is likely failing to retrieve relevant information. This is a valid component-level check.
3.  **BERTScore:** Use this to check the quality of your golden reference answers. If you find a cluster of outputs with a low BERTScore against a reference you expected to be similar, you might realize the LLM found a more creative, or even better, way to solve the problem than your reference answer.

Every production metric must be deeply application-centric, derived from concrete product requirements, user success criteria, and explicit constraints.

Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments from our LLM judge. Here, binary pass/fail criteria outperform every alternative.

## Choosing Binary Metrics Over Anything Else

When designing these custom metrics, you will face a choice: should you use a Likert scale (e.g., 1-5 stars) or a binary pass/fail?

We strongly recommend **binary metrics**.

Likert scales are a seductive trap. They seem to offer more nuance, but in practice, they introduce ambiguity and noise right where you need clarity. There are three main problems with them:

1.  **Inconsistent Labeling:** The difference between a '3' and a '4' is subjective. One person's '4' is another's '3', leading to low inter-annotator agreement. You spend more time debating the rubric than evaluating the system. This ambiguity makes it incredibly difficult to achieve a high Cohen's Kappa score, a common measure of agreement [[2]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).
2.  **Statistical Noise:** Detecting a real improvement is harder. An average score moving from 3.2 to 3.4 might just be random variance. Proving it is a statistically significant improvement requires a much larger sample size than detecting a binary pass rate shift from 70% to 75% [[3]](https://www.ellamind.com/blog/binary-vs-likert-scales).
3.  **Lazy Decision-Making:** Evaluators—both human and LLM—often default to the middle value ('3') to avoid a difficult judgment. This behavior, known as "satisficing" in survey research, hides uncertainty rather than resolving it. A dashboard full of '3's tells you your system is vaguely "okay," but gives you no signal on what to fix [[2]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).

Binary evaluations work because they **force decisions**. An output either met the criterion or it did not. This simple constraint brings several benefits:

1.  **Clearer Thinking:** You cannot hide in ambiguity. A pass/fail decision forces you to create precise, unambiguous definitions of quality.
2.  **Consistency:** Binary choices are faster and more consistent for both human annotators and LLM judges, leading to higher agreement.
3.  **Actionability:** The result is a clear failure signal tied to a specific problem, not a fuzzy score change. When the "Constraint Violation" failure rate spikes, engineers know exactly where to look.

<aside>
💡
**Note:** The 3 points above translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate the inherent randomness of LLMs. LLMs are much more stable when asked to make a binary decision than when asked to assign a scalar value. A binary metric translates to a more robust and repeatable evaluation pipeline.

</aside>

### Capturing Nuance

The standard objection to binary evaluations is the perceived loss of nuance. "What if a response is partially correct? A 'Fail' seems too harsh."

This is a valid concern, but a Likert scale is the wrong solution. The right way to capture nuance is not by making your scale fuzzier, but by making your criteria more **granular**. Instead of a single, subjective rating for a complex quality, you break it down into multiple, specific, binary checks. This decomposition gives you more actionable detail than a single numeric score ever could [[3]](https://www.ellamind.com/blog/binary-vs-likert-scales).

For our writing agent, instead of rating an article 1-5 for "Quality," we create multiple binary evaluations that capture specific dimensions of quality:

1.  **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
2.  **Flow of Ideas Adherence:** Does the generated article contain the ideas in the same order as the expected article? (Yes/No)
3.  **Article Guideline Adherence:** Does the generated article follow the flow of ideas from the article guideline input? (Yes/No)
4.  **Research Anchoring:** Is every claim in the article supported by the provided research? (Yes/No)

By aggregating these binary signals, you get a nuanced view of performance without the noise and bias of a scalar rating. You can now say, "Our system passes Content Adherence 95% of the time but fails Research Anchoring 30% of the time." That is a signal you can act on. You have captured the nuance without sacrificing clarity, and you can track progress on each dimension independently. This approach is simple, intuitive, scalable, and robust in production systems.

With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in the next lesson.

## Conclusion

The path to building reliable AI products requires a fundamental shift in mindset. We must move away from vibe checks, leaderboard chasing, and generic scores, and toward a rigorous practice of evaluation-driven development. This means building custom, business-aligned metrics that measure what truly matters for your application.

Granular, binary pass/fail criteria provide the clearest and most actionable signal for optimization. They eliminate the statistical noise and subjectivity inherent in scalar ratings, forcing clarity and consistency. This is how you turn evaluation from a vague art into a disciplined engineering practice.

In our next lesson, we will translate this theory into practice by implementing custom LLM judges from scratch to evaluate our Brown writing workflow.

## References

- [1] https://www.nngroup.com/articles/practical-significance
- [2] https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals
- [3] https://www.ellamind.com/blog/binary-vs-likert-scales
- [4] https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets
- [5] https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals
- [6] https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ
- [7] https://www.traceloop.com/blog/demystifying-the-bleu-metric
- [8] https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb
- [9] https://www.braintrust.dev/articles/what-is-llm-as-a-judge
- [10] https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method
- [11] https://www.evidentlyai.com/llm-guide/llm-as-a-judge
- [12] https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw
- [13] https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053
- [14] https://launchdarkly.com/blog/llm-evaluation
- [15] https://www.evidentlyai.com/llm-guide/llm-benchmarks
- [16] https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches
- [17] https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP
- [18] https://openreview.net/forum?id=XbVMiW0jTM

</article>