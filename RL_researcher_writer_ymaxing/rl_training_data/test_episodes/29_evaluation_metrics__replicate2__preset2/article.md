# The North Star of AI Engineering: A Framework for Evaluation-Driven Development

In the last lessons, you instrumented your agents with observability tools like Opik and assembled your first offline evaluation datasets. You now have the raw materials for a robust testing process. But raw data is not enough. We need a principled way to measure performance, a framework that tells us whether our changes are making the system better or worse. This is where we design the metrics themselves.

In classical Machine Learning (ML), evaluation is a non-negotiable discipline. We live by metrics like accuracy, precision, recall, and F1-score, all validated with statistical significance. Yet, in AI engineering, many teams revert to "vibe checks." We run a few prompts, eyeball the output, and if it "feels more coherent," we ship it [[3]](https://olshansky.substack.com/p/vibe-checks-are-all-you-need). This intuition-driven approach is a primary reason so many AI projects get stuck in proof-of-concept purgatory [[1]](https://www.decodingai.com/p/escaping-poc-purgatory-evaluation). This shift can be framed as an evolution from Test-Driven Development (TDD) to Evaluation-Driven Development (EDD). TDD asks a binary question: "Does it work?" EDD asks a probabilistic one: "How well does it work, and with what level of confidence?" [[2]](https://medium.com/@nimrodbusany_9074/from-tdd-to-edd-why-evaluation-driven-development-is-the-future-of-ai-engineering-a5e5796b2af4)

Prioritizing a rigorous evaluation layer is difficult. It delivers no immediate, user-visible feature and requires upfront effort to design datasets and metrics, all while the pressure to ship new functionality mounts. In many organizations, the team that builds the "cool demo" gets the praise, while the team that suggests slowing down to build a testing harness is seen as a blocker. This short-term thinking, however, leads to long-term technical debt and fragile systems that are impossible to iterate on safely. This investment in evaluation is what unlocks long-term velocity. It replaces subjective guesswork with an objective signal, catching regressions instantly and focusing your team on changes that produce measurable improvements. Evals are the north star of AI engineering: the single source of truth that guides you toward a better product.

In this lesson, we will establish the theoretical foundation for evaluation-driven development. We will cover:

*   The optimization flywheel and its three core use cases.
*   The trade-offs between different metric types for unstructured outputs.
*   Why custom, business-aligned metrics are superior to public benchmarks and generic scores.
*   Why binary pass/fail judgments provide a clearer signal than 1-5 Likert scales.

With the problem and its importance clear, we will now examine how to operationalize evals inside a repeatable optimization flywheel that replaces intuition with evidence.

## Using Evals Through the Optimization Flywheel

To build intuition, let's examine how we can effectively use and integrate AI evaluations into our application development lifecycle. There are three core scenarios where evaluations provide value.

First, evals **quantify the quality of your system**. They take a snapshot of your system's current performance against a set of given metrics, establishing a baseline. This baseline is your ground truth. Without it, you cannot know if your system is production-ready, where its weaknesses lie, or if your changes are leading to genuine improvements. It transforms the vague question "Is it good enough?" into a measurable state, giving you a clear starting point for any optimization effort.

Second, these metrics serve as **guidance when optimizing your system**. By providing quantitative evidence for every experiment, they shift development from being intuition-based to evidence-based. You no longer have to guess if a prompt change worked; you can measure its impact directly across hundreds of test cases. This disciplined approach allows you to systematically hill-climb toward better performance, confident that each accepted change is a step in the right direction. It turns product development into a scientific process of hypothesis, experiment, and validation.

Finally, evals act as **regression tests that protect shared components**. This is critical in AI engineering, where prompts, tools, and retrieval strategies are often shared and interconnected. The goal here is stability. A change intended to improve one feature might inadvertently break another, and a comprehensive evaluation suite is your only defense against such silent regressions. It ensures that as you add new capabilities, you do not degrade the performance of existing ones.

### The Optimization Process

How does this look in a real-world scenario? The optimization flywheel is a step-by-step plan of attack for systematically improving your AI application.

1.  **Gather your dataset:** Assemble an offline dataset that covers diverse use cases, edge cases, and known failure modes, as we discussed in Lesson 28. This dataset is the foundation of your entire evaluation process and must be representative of the problems your system will face in production.
2.  **Build your metrics:** Define a suite of business-aligned metrics that measure what "quality" means for your specific application. This involves moving beyond generic scores to custom, often binary, checks that reflect your product's unique constraints and goals, a topic we will cover in detail later in this lesson.
3.  **Establish a baseline:** Run your full evaluation suite on the current system to compute baseline scores for each metric. This is your stake in the ground, the quantitative snapshot of your system's performance before any changes are made.
4.  **Start the optimization:** Make one, isolated change that you hypothesize will improve performance. This could be a prompt tweak, a model swap, a change to your RAG chunking strategy, or adjusting the temperature parameter.
5.  **Compute the new score:** Re-run the entire evaluation suite on the modified system to generate a new set of scores. This must be done on the same dataset to ensure a fair, apples-to-apples comparison.
6.  **Compare:** Compare the new scores to your baseline, assessing for statistical significance to ensure the observed difference is not due to random chance. This step is crucial for making data-driven decisions.
7.  **Decide:** Based on whether the scores improved, stayed the same, or worsened, decide whether to keep the change, revert it, or reconsider its complexity trade-offs. An improvement in one metric might come at the cost of another, requiring a careful decision.
8.  **Repeat:** Continue this cycle, making one change at a time, until your scores reach the desired quality bar for production. This iterative process is the engine of continuous improvement.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-4d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down
Image 1: The iterative optimization flywheel for AI applications using evaluations.

It is critical to change only one variable per cycle. This principle mirrors classical control theory, which focuses on single-input, single-output (SISO) systems to ensure stability and allow for clear analysis of how a single change affects the system's output [[4]](https://en.wikipedia.org/wiki/Control_theory). If you change the prompt, the model, and the retrieval strategy all at once, it becomes impossible to attribute any score movement to a specific cause. This turns a disciplined engineering process back into guesswork.

Your interpretation of "better" must also be anchored to business impact, not just an arbitrary p-value [[5]](https://www.nngroup.com/articles/practical-significance). For a high-volume customer support bot processing millions of requests, a 0.5% reduction in checkout errors might achieve statistical significance and translate to hundreds of thousands of dollars in saved revenue and support time [[5]](https://www.nngroup.com/articles/practical-significance). That small movement matters. In contrast, for a low-volume creative writing tool, a similar percentage improvement might be imperceptible to users and have no meaningful business impact. In that context, you would require a much larger improvement before declaring victory. Statistical significance tells you if a result is reliable; practical significance tells you if it's worth acting on [[5]](https://www.nngroup.com/articles/practical-significance).

### Regression Testing

AI evaluations are also an extremely powerful technique for regression testing. Before merging any new feature that touches shared prompts, tool descriptions, or orchestration logic, you run the full eval suite to guard against breaking existing behavior. The strategy is a modification of the optimization flywheel.

1.  **Implement a new feature:** You write the code and verify it works locally for the new use case. This is standard development practice.
2.  **Run the AI evaluations:** You run the full suite of assessments, covering all previous use cases, not just the new one. This is the crucial step that protects against unintended side effects.
3.  **Compare Scores:** You compare the new scores against the established baseline for all existing metrics. The goal is to ensure that performance on old tasks has not degraded.
4.  **Metrics similar to baseline:** If the scores are identical or better across all metrics, your feature has not introduced a regression. You can merge it into your production codebase with confidence.
5.  **Metrics lower than the baseline:** If any score is worse, you have introduced a regression. You must fix your code and repeat the evaluation cycle until all scores are back at or above the baseline. This prevents the slow, silent degradation of your product over time.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down
Image 2: Integrating AI evaluations into CI pipelines for regression testing.

This treats evals like integration tests, but instead of enforcing a strict pass/fail threshold, you compare scores against a moving baseline. This is a more flexible approach suitable for the probabilistic nature of AI systems. By integrating this process into your Continuous Integration (CI) pipeline, you can automate regression testing and ensure that no code is merged without being validated against your full suite of quality checks.

Of course, this process is only as strong as your dataset. Your dataset must be a living asset, continuously expanding with new edge cases from feature development, real-world failures captured from production traces via observability tools like Opik, and hard examples discovered during debugging [[6]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets), [[7]](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals). For example, if your observability platform flags a real-world regression where the agent fails to handle a specific user query format, you should immediately add that trace to your evaluation dataset [[6]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets). This failed production trace can also serve as a seed to generate dozens of synthetic variations, stress-testing your fix and ensuring the system never fails the same way twice [[7]](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals). Instead of writing a new test in code, you broaden your test coverage by adding new, challenging samples to the dataset.

With the flywheel mechanics clear, we can now examine the different families of metrics we might plug into it when dealing with unstructured text and image outputs.

## Exploring Possible Metric Types

The core difficulty in evaluating modern AI systems is that their outputs lack the structured labels of classical ML. We are often dealing with unstructured text, reasoning traces, and sometimes images. We cannot simply calculate accuracy. Instead, we must rely on metrics designed for this ambiguity. There are three main families.

### 1. BLEU and ROUGE

N-gram overlap metrics like BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Oriented Understudy for Gisting Evaluation) are the oldest and simplest. They work by counting the number of overlapping words or sequences of words (n-grams) between the generated output and a reference text [[9]](https://www.traceloop.com/blog/demystifying-the-bleu-metric), [[10]](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb). Their main advantages are that they are fast, deterministic, cheap to compute, and widely understood [[11]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ), [[9]](https://www.traceloop.com/blog/demystifying-the-bleu-metric). However, their limitations are severe. They are blind to semantic meaning, penalizing correct answers that use different phrasing (paraphrases) and rewarding outputs that stuff keywords without logical coherence. For example, a model saying "The capital of France is Paris" and a reference of "Paris is the capital of France" would receive a mediocre score despite being semantically identical [[11]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ). They also cannot assess factual accuracy or reasoning.

### 2. BERTScore

Embedding similarity metrics, such as BERTScore, represent an improvement. They use a neural network like BERT to convert both the generated output and the reference text into high-dimensional vectors (embeddings). They then measure the cosine similarity between these embeddings to gauge semantic closeness [[11]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ). This approach is better at recognizing paraphrases and capturing meaning than lexical methods, and studies show it correlates more closely with human judgments of quality [[11]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ). However, it is still fundamentally a comparison metric. It cannot verify complex business logic or ensure adherence to specific guidelines that are not present in the reference text.

### 3. LLM Judges

The LLM-as-a-judge approach uses a powerful "evaluator" LLM to assess an output based on a detailed prompt. This prompt typically includes the original input, the generated output, a set of evaluation criteria, few-shot examples of good and bad responses, and chain-of-thought instructions to guide the judge's reasoning [[12]](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method), [[13]](https://arize.com/llm-as-a-judge). This method is highly flexible and customizable, allowing you to evaluate subjective qualities like tone, style, and adherence to complex, domain-specific rules [[14]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge). For example, a judge can check if a legal summary correctly identifies all relevant precedents, a task impossible for lexical or semantic metrics.

Their performance, however, depends heavily on prompt quality and the judge model's capability. They can be slower, more expensive, and may inherit biases from the underlying LLM, such as a preference for longer answers (verbosity bias) or for outputs generated by the same model family (self-enhancement bias) [[14]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge), [[15]](https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw). Their reliability can be improved with techniques like including few-shot examples in the prompt, using chain-of-thought reasoning, or even fine-tuning a smaller judge model on domain-specific evaluation data [[16]](https://www.reddit.com/r/LLMDevs/comments/1j3gbil/5_techniques_to_improve_llmjudges).

| Metric Family | Speed | Cost | Semantic Awareness | Business Alignment | Explainability |
| --- | --- | --- | --- | --- | --- |
| **BLEU/ROUGE** | Very Fast | Very Low | None | Low | High (n-gram overlap) |
| **BERTScore** | Moderate | Low | High | Moderate | Low (embedding space) |
| **LLM Judges** | Slow | High | Very High | Very High | High (reasoning trace) |

Table 1: A trade-off summary of the three main metric families.

For the complex requirements of our capstone writing agent—such as guideline adherence, structural fidelity, and grounding in research—LLM judges are the most practical choice.

Now, you kept hearing from us: *"business metrics here, business metrics there"*. Thus, let's understand why defining your own business metrics is such an essential and underrated step in building your AI evals strategy.

## Why Business Metrics Over Benchmarks

Using popular leaderboards or public benchmarks to choose an LLM for your product is often a mistake. Benchmarks are the most deceiving type of metric. There are two core reasons for this.

First, benchmarks often function as marketing artifacts. Once a test set is public, models can be trained or fine-tuned on the test data, intentionally or not, which inflates scores and compromises the benchmark's integrity [[17]](https://www.evidentlyai.com/llm-guide/llm-benchmarks), [[18]](https://launchdarkly.com/blog/llm-evaluation). This problem of data contamination is a repeat of early mistakes in ML history, where iterative development on a static benchmark implicitly "trains" on the evaluation data, invalidating claims of generalization [[19]](https://medium.com/@yujiisobe/navigating-the-maze-of-llm-evaluation-a-guide-to-benchmarks-rag-and-agent-assessment-fb7aef299e66), [[20]](https://openreview.net/forum?id=maMnVCHl8J). This can lead to models that have simply memorized the answers to benchmark questions rather than learning to reason, a phenomenon known as "reasoning paradigm overfitting" [[20]](https://openreview.net/forum?id=maMnVCHl8J). There have even been instances where models were explicitly fine-tuned on test sets just to climb a leaderboard.

Second, there is a fundamental mismatch between typical benchmark tasks (like solving math problems or answering trivia) and the nuanced demands of real business workloads [[21]](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches). A model that excels at MMLU may fail completely at generating long-form creative content, performing nuanced legal analysis, or providing empathetic customer support. Your product has specific constraints that generic benchmarks cannot capture.

The proper role for benchmarks is narrow: they are useful for advancing research, for initial model filtering during early exploration, but never as a proxy for product-level decisions or as a primary optimization target. Ultimately, all offline evaluations are proxies for the real-world outcomes you care about, and their validity must be confirmed by online A/B testing [[22]](https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork).

If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous. We must instead build metrics that are deeply tied to our specific application.

## Why Custom Business Metrics Over Generic Metrics

Generic, off-the-shelf metrics for qualities like "toxicity," "helpfulness," or "hallucination" create a mirage. They feel objective, they produce a score, but they optimize for the wrong signal and create false confidence because they lack context about your product, your users, and your brand voice [[23]](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP).

An AI application can score brilliantly on "helpfulness" yet fail catastrophically on your specific constraints. Consider a dashboard filled with these scores. It looks impressive, but what does a "3.7" in "Personalization" actually mean? And what should a developer do to improve it?

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down
Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"

For our Brown writing agent, a generic `hallucination` score is useless. If it returns "positive," what does that tell us? Did the agent invent information not present in the research? Did it deviate from the article guidelines? Or did it simply include a personal story that, while not in the source text, is factually correct and aligns perfectly with the desired brand voice? A generic detector might flag an engaging anecdote as a fabrication, even when that creative elaboration is exactly what the task requires. The metric cannot distinguish between undesirable invention and desirable creativity.

Prefabricated scores suffer from three main limitations: they lack domain-specific constraints, they cannot localize which part of an output failed, and they introduce statistical noise that obscures real signals.

This does not mean generic metrics have no place. Their valid role is strictly during exploratory data analysis, where they can act as a "flashlight" to surface interesting traces for manual review. For example:

1.  **Verbosity:** Sorting your outputs by length can reveal if your longest responses are rambling and unhelpful or if your shortest ones are curt and missing information. An engineer can then inspect these clusters to identify and label a new failure mode related to output length. This is a simple heuristic that can quickly surface problems in long-form generation tasks.
2.  **Similarity Score:** In a RAG system, you can use a similarity score to evaluate the retriever component specifically. You measure the semantic similarity between the user's query and the retrieved document chunks. If this score is consistently low, it’s a strong signal that your retriever is failing to find relevant information, pointing to a problem with your embedding model, chunking strategy, or search algorithm. This is a valid component-level check that helps isolate problems in your pipeline.
3.  **BERTScore:** You can use BERTScore to audit the quality of your "golden" reference answers. If a cluster of generated outputs scores poorly against a reference, a manual review might reveal that the LLM found a more creative or even more correct solution than the one you provided. This helps you improve your ground truth and challenge your own assumptions about what a "good" answer looks like.

In all these cases, the generic metric is the start of an investigation, not the final verdict. Every metric you use to make production decisions must be application-centric, derived from your product requirements, user success criteria, and explicit constraints.

Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments from our LLM judge. Here, binary pass/fail criteria outperform every alternative.

## Choosing Binary Metrics Over Anything Else

When designing custom metrics, you will face a choice: should you use a Likert scale (e.g., 1-5 stars) or a binary pass/fail judgment? We strongly recommend **binary metrics**.

Likert scales are a seductive trap. They promise nuance but deliver noise. They suffer from three fundamental problems:

1.  **Inconsistent Labeling:** The difference between a '3' and a '4' is subjective. One person's '4' is another's '3', leading to low inter-annotator agreement and endless debates over the rubric [[24]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals), [[25]](https://www.ellamind.com/blog/binary-vs-likert-scales).
2.  **Statistical Noise:** Detecting a real improvement from an average score of 3.2 to 3.4 requires a much larger sample size than detecting a shift in a binary pass rate from 75% to 80%. You waste time on changes without knowing if you're making progress or just seeing random fluctuations [[24]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals), [[25]](https://www.ellamind.com/blog/binary-vs-likert-scales).
3.  **Lazy Decision-Making:** Raters, both human and LLM, often default to the middle value ('3') to avoid a difficult judgment. This "satisficing" behavior hides uncertainty, creating a sea of '3's that tells you nothing about what to fix [[24]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).

Binary evaluations solve these problems by **forcing decisions**. An output either met the criterion or it did not. This simple constraint is incredibly powerful. It delivers:

1.  **Clearer Thinking:** You cannot hide in ambiguity. Binary judgments force you to create precise, unambiguous definitions of quality.
2.  **Consistency:** Binary decisions are faster and yield higher agreement among both human and LLM evaluators.
3.  **Actionability:** A spike in the "Constraint Violation" failure rate is a clear, actionable signal for an engineer, whereas a dip in the "Helpfulness" score from 3.7 to 3.5 is not.

<aside>
💡 **Note:** The 3 points above translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate the inherent randomness of LLMs. Because the output is binary, you can use standard, easy-to-interpret classification metrics to evaluate the judge itself [[26]](https://cameronrwolfe.substack.com/p/finetuned-judge). This translates to a more robust and repeatable evaluation pipeline.
</aside>

Before deploying a judge, you must calibrate it to understand how it fails. A common practice is an iterative loop: label a representative dataset, run the judge, review disagreements, update the evaluation criteria or examples, and repeat until judge agreement with humans is high [[27]](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production). This process ensures the judge is reliable enough to gate a release or monitor production quality.

### Capturing Nuance

The standard objection is that a binary scale loses the "shades of gray" a 1-5 scale can capture. This is a valid concern, but a Likert scale is the wrong solution. The right way to capture nuance is not by making your scale fuzzier, but by making your criteria more **granular**.

Instead of a single, subjective rating for a complex quality, you break it down into multiple, specific, binary checks. For our writing agent, instead of rating an article 1-5 for "Quality," we create multiple binary evaluations that capture specific dimensions:

1.  **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
2.  **Flow of Ideas Adherence:** Does the generated article present ideas in the same order as the expected article? (Yes/No)
3.  **Article Guideline Adherence:** Does the generated article follow the flow of ideas from the article guideline input? (Yes/No)
4.  **Research Anchoring:** Is every claim in the article supported by the provided research? (Yes/No)

By aggregating these binary signals, you get a far more precise and actionable view of performance. You can now say, "Our system passes content and flow checks 95% of the time, but it fails the research anchoring check 40% of the time." That is a signal you can act on. You have captured nuance without sacrificing clarity. For highly open-ended creative tasks, this approach can still miss subtle failures in narrative flow or stylistic coherence, but it provides a robust and debuggable starting point [[28]](https://www.linkedin.com/posts/pauliusztin_i-created-an-ai-agent-to-write-a-substack-activity-7420095430807691266-fQ1U), [[29]](https://www.mdpi.com/2076-3417/15/6/2971).

With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in the next lesson.

## Conclusion

The path to building robust AI products requires a fundamental shift in mindset. It is a move away from vibe checks, leaderboards, and generic scores, and toward a rigorous practice of evaluation-driven development. This means building custom, business-aligned metrics that measure what truly matters for your application.

Granular, binary pass/fail criteria deliver the clearest optimization signal while avoiding the statistical noise and subjectivity inherent in scalar scales. Your evaluation framework is your product's moat. These principles are becoming so central that major agent frameworks from Microsoft, AWS, and others are now building continuous evaluation capabilities directly into their platforms [[30]](https://learn.microsoft.com/en-us/agents/architecture/evaluation-frameworks), [[31]](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents), [[32]](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon). In our next lesson, we will translate this theory into practice by implementing custom LLM judges from scratch to evaluate our Brown writing workflow.

## References

- [1] Bowne-Anderson, H., & Krawczyk, S. (2025, October 16). _Escaping POC Purgatory: Evaluation-Driven Development for AI Systems_. Decoding AI. [https://www.decodingai.com/p/escaping-poc-purgatory-evaluation](https://www.decodingai.com/p/escaping-poc-purgatory-evaluation)
- [2] Busany, N. (n.d.). _From TDD to EDD: Why Evaluation-Driven Development is the Future of AI Engineering_. Medium. [https://medium.com/@nimrodbusany_9074/from-tdd-to-edd-why-evaluation-driven-development-is-the-future-of-ai-engineering-a5e5796b2af4](https://medium.com/@nimrodbusany_9074/from-tdd-to-edd-why-evaluation-driven-development-is-the-future-of-ai-engineering-a5e5796b2af4)
- [3] Olshansky, V. (n.d.). _Vibe checks are all you need_. [https://olshansky.substack.com/p/vibe-checks-are-all-you-need](https://olshansky.substack.com/p/vibe-checks-are-all-you-need)
- [4] Wikipedia. (n.d.). _Control theory_. [https://en.wikipedia.org/wiki/Control_theory](https://en.wikipedia.org/wiki/Control_theory)
- [5] Banawa, R. (2026, March 6). _Statistical Significance Isn’t the Same as Practical Significance_. Nielsen Norman Group. [https://www.nngroup.com/articles/practical-significance](https://www.nngroup.com/articles/practical-significance)
- [6] Comet. (n.d.). _Manage Datasets - Opik Documentation_. [https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets)
- [7] Iusztin, P. (2024, October 15). _Generate Synthetic Datasets for AI Evals_. Decoding AI. [https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals)
- [8] Bowne-Anderson, H. (2025, October 30). _Stop Launching AI Apps Without This Framework_. Decoding AI. [https://www.decodingai.com/p/stop-launching-ai-apps-without-this](https://www.decodingai.com/p/stop-launching-ai-apps-without-this)
- [9] Traceloop. (n.d.). _Demystifying the BLEU Metric_. [https://www.traceloop.com/blog/demystifying-the-bleu-metric](https://www.traceloop.com/blog/demystifying-the-bleu-metric)
- [10] S, S. (2023, April 20). _Understanding BLEU and ROUGE score for NLP evaluation_. Medium. [https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb)
- [11] Ferrer, J. (2025, December 9). _LLM evaluation benchmarking: Beyond BLEU and ROUGE_. Weights & Biases. [https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ)
- [12] Confident AI. (n.d.). _Why LLM-as-a-Judge is the best LLM evaluation method_. [https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method)
- [13] Arize. (n.d.). _LLM-as-a-Judge_. [https://arize.com/llm-as-a-judge](https://arize.com/llm-as-a-judge)
- [14] Evidently AI. (n.d.). _LLM-as-a-judge: a complete guide to using LLMs for evaluations_. [https://www.evidentlyai.com/llm-guide/llm-as-a-judge](https://www.evidentlyai.com/llm-guide/llm-as-a-judge)
- [15] Abdella, A. (n.d.). _LLM as a Judge_. LinkedIn. [https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw](https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw)
- [16] Reddit. (n.d.). _5 techniques to improve LLM-judges_. [https://www.reddit.com/r/LLMDevs/comments/1j3gbil/5_techniques_to_improve_llmjudges](https://www.reddit.com/r/LLMDevs/comments/1j3gbil/5_techniques_to_improve_llmjudges)
- [17] Evidently AI. (n.d.). _LLM benchmarks_. [https://www.evidentlyai.com/llm-guide/llm-benchmarks](https://www.evidentlyai.com/llm-guide/llm-benchmarks)
- [18] LaunchDarkly. (n.d.). _Effective LLM evaluation beyond basic benchmarks_. [https://launchdarkly.com/blog/llm-evaluation](https://launchdarkly.com/blog/llm-evaluation)
- [19] Isobe, Y. (n.d.). _Navigating the Maze of LLM Evaluation: A Guide to Benchmarks, RAG, and Agent Assessment_. Medium. [https://medium.com/@yujiisobe/navigating-the-maze-of-llm-evaluation-a-guide-to-benchmarks-rag-and-agent-assessment-fb7aef299e66](https://medium.com/@yujiisobe/navigating-the-maze-of-llm-evaluation-a-guide-to-benchmarks-rag-and-agent-assessment-fb7aef299e66)
- [20] Anonymous. (n.d.). _On the Imitation Games of LLM-based prompt engineering and evaluation_. OpenReview. [https://openreview.net/forum?id=maMnVCHl8J](https://openreview.net/forum?id=maMnVCHl8J)
- [21] Raschka, S. (n.d.). _4 Ways to Evaluate LLMs_. magazine.sebastianraschka.com. [https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches)
- [22] Spotify Engineering. (2026, May). _Better Experiments with LLM Evals: A Funnel, Not a Fork_. [https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork](https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork)
- [23] Aggarwal, S. (n.d.). _AI evaluation is broken when we hide behind generic metrics._ LinkedIn. [https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP)
- [24] Iusztin, P. (n.d.). _The 5-Star Lie: You’re Doing AI Evaluations Wrong_. Decoding AI. [https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals)
- [25] ellamind. (n.d.). _Why We Use Binary Yes/No Evaluations (And You Should Too)_. ellamind Blog. [https://www.ellamind.com/blog/binary-vs-likert-scales](https://www.ellamind.com/blog/binary-vs-likert-scales)
- [26] Wolfe, C. (n.d.). _Finetuned Judge_. [https://cameronrwolfe.substack.com/p/finetuned-judge](https://cameronrwolfe.substack.com/p/finetuned-judge)
- [27] Arize. (n.d.). _How to Build LLM-as-a-Judge Evaluators That Hold Up in Production_. [https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production)
- [28] Iusztin, P. (n.d.). _I created an AI Agent to write a Substack article for me_. LinkedIn. [https://www.linkedin.com/posts/pauliusztin_i-created-an-ai-agent-to-write-a-substack-activity-7420095430807691266-fQ1U](https://www.linkedin.com/posts/pauliusztin_i-created-an-ai-agent-to-write-a-substack-activity-7420095430807691266-fQ1U)
- [29] MDPI. (n.d.). _Automatic Story Evaluation with Large Language Models: A Comprehensive Analysis_. [https://www.mdpi.com/2076-3417/15/6/2971](https://www.mdpi.com/2076-3417/15/6/2971)
- [30] Microsoft. (n.d.). _Agent evaluation frameworks_. [https://learn.microsoft.com/en-us/agents/architecture/evaluation-frameworks](https://learn.microsoft.com/en-us/agents/architecture/evaluation-frameworks)
- [31] Microsoft. (2026). _Build 2026: The open trust stack for AI agents_. [https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents](https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents)
- [32] AWS. (n.d.). _Evaluating AI agents: Real-world lessons from building agentic systems at Amazon_. [https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon)