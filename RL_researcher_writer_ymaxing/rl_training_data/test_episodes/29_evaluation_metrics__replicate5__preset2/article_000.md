# Evaluation-Driven Development: The North Star of AI Engineering

In our previous lessons, we instrumented our agents with observability tools like Opik and constructed offline datasets to capture their behavior. We have the data. Now we need to make sense of it. This lesson introduces the core theoretical framework for designing the metrics that will guide our development process. In classical machine learning, we rely on rigorous standards like accuracy, precision, recall, and F1 scores to measure success. Yet in AI engineering, many teams fall back on "vibe checks," making decisions based on whether an output "feels more coherent."

This is a regression from the discipline found in traditional software engineering, where practices like Test-Driven Development (TDD) provide a clear, binary answer to the question: "Does it work?" Evaluation-Driven Development is the necessary evolution for AI, shifting the question to "How well does it work?" [[19]](https://medium.com/@nimrodbusany_9074/from-tdd-to-edd-why-evaluation-driven-development-is-the-future-of-ai-engineering-a5e5796b2af4).

Investing in a proper evaluation layer can feel like a detour. It does not deliver an immediate, user-visible feature. It requires upfront effort to design datasets and metrics, all while the pressure to ship new functionality mounts. However, this investment dramatically accelerates long-term iteration. It provides an objective signal on every change, catches regressions instantly, and transforms development from a series of hopeful guesses into a systematic process of improvement.

Evals are the north star of AI engineering. They are the single source of truth that tells you exactly which modifications improve your system and which degrade it.

In this lesson, we will cover the foundational principles of Evaluation-Driven Development (EDD). You will learn about:

*   The optimization flywheel and its three core use cases.
*   The trade-offs between different metric types for unstructured outputs.
*   Why custom business metrics are superior to public benchmarks and generic scores.
*   Why binary pass/fail judgments provide a clearer signal than Likert scales.

With the problem and its importance clear, we will now examine how to operationalize evals inside a repeatable optimization flywheel that replaces intuition with evidence.

## Using Evals Through the Optimization Flywheel

To build intuition, let's examine how we can effectively use and integrate AI evaluations into our application development lifecycle. There are three core scenarios where evaluations provide indispensable value.

First, evals **quantify the quality of your system**. They snapshot a baseline of your system's current performance on a set of given metrics. Without a baseline, you cannot know if your system is ready for production or if your changes are actually making it better [[1]](https://www.decodingai.com/p/escaping-poc-purgatory-evaluation).

Second, these metrics serve as **guidance when optimizing your system**. They provide objective evidence for your experiments, shifting development from being intuition-based to evidence-based. Instead of saying, "this prompt feels better," you can say, "this prompt improved our 'Research Anchoring' score by 7%."

Finally, evals act as **regression tests** that protect shared components. In complex AI systems, prompts, tool definitions, and orchestration logic are often interconnected. A small change intended to improve one feature can silently break another. Evals catch these unintended consequences, ensuring stability as the system evolves.

### The Optimization Process

How does this look in a real-world scenario? The optimization flywheel is an eight-step iterative process for systematically improving your AI application.

1.  **Gather your dataset:** Assemble the offline dataset that represents the inputs your system will handle.
2.  **Build your metrics:** Define the business-aligned metrics you will use to measure quality.
3.  **Establish a baseline:** Run your evals on the current system to compute your baseline scores.
4.  **Start the optimization:** Make one, isolated change that you believe will improve performance.
5.  **Compute the new score:** Re-evaluate the entire dataset by re-running the evals on the modified system.
6.  **Compare:** Compare the new scores to the baseline, considering statistical significance.
7.  **Decide:** Based on whether the score is better, the same, or worse, decide to keep the change, revert it, or analyze its complexity trade-offs.
8.  **Repeat:** Continue the cycle until your scores meet the desired quality bar.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-4d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down 
Image 1: The iterative optimization flywheel for AI applications using evaluations.

During this cycle, it is critical to change only one variable at a time. If you modify the prompt, the model, and the retrieval strategy all at once, you create confounding variables. It becomes impossible to attribute any score changes to a specific modification, turning your evidence-based process back into guesswork. This principle of isolating variables is not new; it is a cornerstone of classical control theory, which designs stable feedback loops by analyzing single-input, single-output (SISO) systems to ensure predictable behavior [[20]](https://en.wikipedia.org/wiki/Control_theory).

Furthermore, "better" is always relative to your business use case. Statistical significance must be anchored to actual business impact, not arbitrary p-value thresholds [[2]](https://www.nngroup.com/articles/practical-significance). For a high-volume customer support bot, a small improvement can have a massive effect. A 0.5% reduction in checkout errors on a site processing two million transactions a year translates to 10,000 fewer failed transactions. If each failure costs $15 in lost revenue or support time, that small improvement is worth $150,000 annually [[2]](https://www.nngroup.com/articles/practical-significance). In contrast, for a low-volume creative writing tool, a similar percentage improvement might be negligible. The impact of the change, not just its statistical reliability, should guide your decision.

### Regression Testing

A powerful variation of this flywheel is using evals for regression testing. Before merging any new feature that touches shared components—prompts, tool descriptions, orchestration logic, or memory retrieval—you run the full eval suite to guard against breaking existing behavior. This is a critical practice for maintaining stability in production AI systems [[3]](https://olshansky.substack.com/p/vibe-checks-are-all-you-need).

The process is a streamlined version of the optimization flywheel:

1.  **Implement a new feature:** You write the code and verify it works locally for the new use case.
2.  **Run the AI evaluations:** You run the full suite of assessments, covering all previous use cases, not just the new one.
3.  **Compare Scores:** You compare the new scores against the established baseline for existing features.
4.  **Metrics similar to baseline:** If the scores for existing features are identical or within an acceptable tolerance of the baseline, your new feature has not introduced a regression. You can merge it into your production codebase.
5.  **Metrics lower than the baseline:** If any score has dropped, you have introduced a regression. You must fix your code and repeat the process until all scores are back at the baseline.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down 
Image 2: Integrating AI evaluations into CI pipelines for regression testing.

This treats your evals like integration tests, but with a key difference: instead of a strict pass/fail threshold, you compare scores against a moving baseline. The goal is to ensure that quality does not degrade over time.

This framework also demands that your dataset continuously expands. As you add new features, you must add examples that cover their specific edge cases. When your observability and tracing tools, like Opik, capture production failures, those traces should be converted into new evaluation items [[4]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets). Hard examples you encounter during debugging should also be added. In AI engineering, you do not just write new tests in code; you broaden your test coverage by adding new, challenging samples to your dataset [[5]](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals).

With the flywheel mechanics clear, we can now examine the different families of metrics we might plug into it when dealing with unstructured text and image outputs.

## Exploring Possible Metric Types

The core difficulty in evaluating modern AI systems is that their outputs are often unstructured. Unlike classical ML with structured labels, we are evaluating free-form text, complex reasoning traces, and sometimes even images. Standard metrics like accuracy are unavailable, so we must turn to other families of evaluation.

### BLEU and ROUGE

N-gram overlap metrics like BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Oriented Understudy for Gisting Evaluation) were some of the earliest methods for evaluating text. They work by calculating the lexical overlap between a generated text and a reference text, counting matching words and phrases (n-grams) [[6]](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb). Their main advantages are that they are fast, deterministic, and require no additional models to run [[7]](https://www.traceloop.com/blog/demystifying-the-bleu-metric). However, their significant drawback is their blindness to semantics. They cannot recognize paraphrasing, penalizing a correct answer simply because it uses different words than the reference. They also cannot assess factual accuracy or the validity of a reasoning process [[8]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ).

### BERTScore

Embedding similarity metrics like BERTScore improve on this by using embeddings to measure semantic closeness instead of just lexical overlap [[8]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ). This captures paraphrasing well but remains a comparison metric, unable to verify complex business rules or factual accuracy without a perfect reference.

### LLM Judges

The LLM-as-a-judge approach uses a capable LLM to evaluate the output of another model. You provide the judge model with the input, the generated output, a detailed set of criteria, and often a few examples (few-shot learning) and chain-of-thought instructions. The judge then produces a structured judgment, such as a score or a pass/fail label, along with its reasoning [[9]](https://www.braintrust.dev/articles/what-is-llm-as-a-judge). This method is highly flexible and customizable, allowing you to evaluate against complex, domain-specific guidelines that are impossible to capture with lexical or embedding-based metrics [[10]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge). For example, you can ask a judge to verify if a response adheres to a specific brand voice or legal constraint.

The main downside is that their performance depends heavily on the quality of the prompt and the capability of the evaluator model. They can also be slower and more expensive than other automated metrics and may inherit biases from the underlying LLM if not carefully developed and tested [[11]](https://cameronrwolfe.substack.com/p/llm-as-a-judge). These weaknesses can be mitigated through **calibration**, an iterative loop of running the judge, reviewing disagreements with human labels, and refining the criteria [[21]](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production). Even a calibrated judge is a proxy for user outcomes and must be validated against online business metrics to ensure it tracks real-world value, not just surface-level patterns [[22]](https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork).

| Dimension | Statistical (BLEU/ROUGE) | Embedding-Based (BERTScore) | LLM-as-a-Judge |
| :--- | :--- | :--- | :--- |
| **Speed** | Instant | Seconds per example | Seconds to minutes per example |
| **Cost** | Free | GPU time | API calls or GPU time |
| **Semantic Awareness** | None | High | Very High |
| **Business Alignment** | Low | Moderate | High (Customizable) |
| **Explainability** | High (n-gram matches) | Low (embedding space) | High (reasoning provided) |

*Table 1: A trade-off summary of the three main metric families for evaluating unstructured text.*

For the kind of nuanced evaluation needed for our capstone writing agent—adherence to guidelines, structural fidelity, and grounding in research—LLM judges are the most practical choice.

You have heard from us repeatedly: "business metrics here, business metrics there." Now, let's understand why defining your own business metrics is such an essential and underrated step in building your AI evals strategy.

## Why Business Metrics Over Benchmarks

It is often a mistake to look at popular leaderboards or public benchmarks to choose an LLM for a product. Benchmarks are the most deceiving type of metric, and there are two core reasons for this.

First, public benchmarks are prone to overfitting. Once a test set is known, models inevitably begin to hill-climb on it, whether through intentional fine-tuning on the test data or simply via data contamination in large training sets [[12]](https://www.evidentlyai.com/llm-guide/llm-benchmarks), [[13]](https://openreview.net/forum?id=XbVMiW0jTM). The very process of iterative prompt engineering against a benchmark is a form of "training on the test set," mirroring historical validation failures in machine learning and invalidating the results [[23]](https://openreview.net/forum?id=maMnVCHl8J).

Second, there is a fundamental mismatch between the tasks in most benchmarks and the workloads of real business applications. A model's ability to solve math problems from the GSM8k benchmark or answer trivia questions says little about its capacity for long-form creative writing, nuanced legal analysis, or personalized customer support [[14]](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches).

Benchmarks have a proper, narrow role: advancing research, providing a quick sanity check, or serving as a filter during the initial exploration of models. They should never be used as a proxy for product-level decisions or as the primary target for optimization.

If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous. We must instead build metrics that are deeply tied to our specific application.

## Why Custom Business Metrics Over Generic Metrics

Generic, off-the-shelf metrics like "toxicity," "helpfulness," or RAGAS-style "faithfulness" create a mirage. They give the illusion of progress by optimizing for the wrong signal and generate false confidence because they lack context about your product, users, and brand voice [[15]](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP). A model can score brilliantly on a generic "helpfulness" benchmark and still fail catastrophically on your specific constraints.

Consider the dashboard below. It looks impressive, with scores for "Truthfulness" and "Personalization." But what does a 3.7 in "Personalization" actually mean? These vague scores are not actionable.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down 
Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"

Let's take our Brown writing agent as an example. Suppose we use a generic `hallucination` score, and it returns "positive." What does that tell us? Did the agent invent facts not present in the research? Did it deviate from the article guidelines? Or did it simply include a personal story that, while not in the source text, is factually correct and aligns with our desired brand voice? The generic metric cannot distinguish between undesirable invention and desirable creative elaboration.

These prefab scores have severe limitations. They lack domain-specific constraints, they cannot localize which part of an output failed, and they introduce statistical noise into your decision-making. Their only valid role is during exploratory data analysis, where they can act as a "flashlight" to surface interesting examples for manual review, not as a "report card" for grading quality [[16]](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics).

Here are a few useful examples of using generic metrics for exploration:

1.  **Verbosity:** Sorting your outputs by length can reveal if your most verbose answers are rambling and unhelpful or if your shortest answers are curt and incomplete. This helps you spot failure modes in long-form generation.
2.  **Similarity Score:** In a RAG system, you can use a similarity score to evaluate the retriever component specifically. If the similarity between the user query and the retrieved document chunks is low, your retriever is likely failing. This is a valid component-level check.
3.  **BERTScore:** You can use this to check the quality of your "golden" reference answers. If you find a cluster of generated outputs with a low BERTScore against a reference, a manual review might reveal that the LLM found a more creative or even better way to solve the problem than your reference answer.

In all these cases, the generic metric is the start of an investigation, not the final verdict. Every production metric must be deeply application-centric, derived from concrete product requirements and user success criteria.

Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments from our LLM judge. Here, binary pass/fail criteria outperform every alternative.

## Choosing Binary Metrics Over Anything Else

When designing custom metrics, choose a binary pass/fail over a Likert scale (e.g., 1-5 stars). We strongly recommend **binary metrics**.

Likert scales are seductive because they seem to offer more nuance, but in practice, they introduce several problems that undermine the evaluation process [[17]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals):

1.  **Inconsistent Labeling:** The difference between a '3' and a '4' is subjective. One person's '4' is another's '3', leading to low inter-annotator agreement. You spend more time debating the rubric than evaluating the system [[17]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).
2.  **Statistical Noise:** Detecting a real improvement from an average score of 3.2 to 3.5 requires a much larger sample size than detecting a shift in a binary pass rate from 60% to 70% [[18]](https://www.ellamind.com/blog/binary-vs-likert-scales). Small movements are often indistinguishable from random variance.
3.  **Lazy Decision-Making:** Evaluators—both human and LLM—often default to the middle value ('3') to avoid a difficult judgment. This "satisficing" behavior flattens the signal and hides the very failures you need to find [[17]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).

Binary evaluations work because they **force decisions**. An output either met a specific criterion or it did not. This constraint has immediate benefits:

1.  **Clearer Thinking:** You cannot hide in ambiguity. This forces you to create precise, unambiguous definitions of quality.
2.  **Consistency:** Binary decisions are faster and yield higher agreement among both human raters and LLM judges.
3.  **Actionability:** The result is not a fuzzy number but a clear failure signal tied to a specific problem. A spike in the "Research Anchoring" failure rate tells an engineer exactly where to start debugging.

<aside>
💡 **Note:** The points above translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate the inherent randomness of LLMs. LLMs are much more stable when asked to make a binary decision than when asked to assign a scalar value. A binary metric translates to a more robust and repeatable evaluation pipeline. This reliability is further enhanced by treating the evaluation as a classification task, allowing you to use standard metrics to calibrate the judge's performance against human-labeled examples [[18]](https://www.ellamind.com/blog/binary-vs-likert-scales), [[24]](https://cameronrwolfe.substack.com/p/finetuned-judge).
</aside>

### Capturing Nuance

The common objection is that binary metrics lose nuance. This is a misconception. You capture nuance not with a fuzzier scale, but with more **granular** criteria.

Instead of one vague "Quality" rating, you decompose it into multiple, specific, binary checks. For our Brown writing agent, we would not rate an article 1-5 for "Quality." Instead, we would create multiple binary evaluations:

1.  **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
2.  **Flow of Ideas Adherence:** Does the generated article present ideas in the same order as the expected article? (Yes/No)
3.  **Article Guideline Adherence:** Does the generated article follow the flow of ideas from the article guideline input? (Yes/No)
4.  **Research Anchoring:** Is every claim in the article supported by the provided research? (Yes/No)

It is important to acknowledge, however, that even granular binary checks can fall short for highly subjective or creative tasks. They may fail to capture subtle issues in narrative flow or unfairly penalize a creative output that is good but incomplete, a common failure mode for LLM evaluators [[25]](https://www.linkedin.com/posts/pauliusztin_i-created-an-ai-agent-to-write-a-substack-activity-7420095430807691266-fQ1U), [[26]](https://www.mdpi.com/2076-3417/15/6/2971).

Aggregating these binary signals gives you a far more nuanced and actionable view of performance. You can track progress on each dimension independently, and a simple average or weighted sum provides an overall quality score without the noise and bias of a Likert scale. This approach is simple, intuitive, scalable, and robust for production systems [[18]](https://www.ellamind.com/blog/binary-vs-likert-scales).

With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in the next lesson.

## Conclusion

This lesson laid the foundation for Evaluation-Driven Development: a shift from vibe checks to a rigorous practice built on custom, binary, business-aligned metrics. Decomposing quality into granular pass/fail criteria creates a clear signal, free from the noise of scalar ratings. In our next lesson, we will translate this theory into practice by implementing custom LLM judges for our Brown writing workflow. This is a core skill for building modern AI systems, which increasingly rely on continuous evaluation frameworks to maintain quality in production [[27]](https://learn.microsoft.com/en-us/agents/architecture/evaluation-frameworks).

## References

- [1] Krawczyk, S., & Bowne-Anderson, H. (2025, October 16). Escaping POC Purgatory: Evaluation-Driven Development for AI Systems. Decoding AI. https://www.decodingai.com/p/escaping-poc-purgatory-evaluation
- [2] Banawa, R. (2026, March 6). Statistical Significance Isn’t the Same as Practical Significance. Nielsen Norman Group. https://www.nngroup.com/articles/practical-significance
- [3] Olshansky, D. (2025, April 29). "Vibe Checks" Are All You Need. Technically. https://olshansky.substack.com/p/vibe-checks-are-all-you-need
- [4] Comet. (n.d.). Manage datasets. Opik Documentation. https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets
- [5] Iusztin, P. (2025, September 10). Generate Synthetic Datasets for AI Evals. Decoding AI. https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals
- [6] Kam-Santhosh, S. (2023, April 20). Understanding BLEU and ROUGE score for NLP Evaluation. Medium. https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb
- [7] Demystifying the BLEU Metric. (2024, May 21). Traceloop. https://www.traceloop.com/blog/demystifying-the-bleu-metric
- [8] Ferrer, J. (2025, December 9). LLM evaluation benchmarking: Beyond BLEU and ROUGE. Weights & Biases. https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ
- [9] Braintrust. (n.d.). What is LLM-as-a-judge? Braintrust. https://www.braintrust.dev/articles/what-is-llm-as-a-judge
- [10] Evidently AI. (2026, May 19). LLM-as-a-judge: a complete guide to using LLMs for evaluations. Evidently AI. https://www.evidentlyai.com/llm-guide/llm-as-a-judge
- [11] Wolfe, C. (2024, May 2). LLM as a Judge. Cameron R. Wolfe. https://cameronrwolfe.substack.com/p/llm-as-a-judge
- [12] Evidently AI. (n.d.). LLM benchmarks: everything you need to know. Evidently AI. https://www.evidentlyai.com/llm-guide/llm-benchmarks
- [13] Li, Z., et al. (2025). PROBE: BENCHMARKING REASONING PARADIGM OVERFITTING IN LARGE LANGUAGE MODELS. OpenReview. https://openreview.net/forum?id=XbVMiW0jTM
- [14] Raschka, S. (2024, May 15). 4 Approaches for LLM Evaluation. Ahead of AI. https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches
- [15] Aggarwal, S. (2025, September 24). AI evaluation is broken when we hide behind generic metrics. LinkedIn. https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP
- [16] Husain, H. (2025, October 2). The Mirage of Generic AI Metrics. Decoding AI. https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics
- [17] Iusztin, P. (2025, September 24). The 5-Star Lie: You’re Doing AI Evaluations Wrong. Decoding AI. https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals
- [18] ellamind. (n.d.). Why We Use Binary Yes/No Evaluations (And You Should Too). ellamind Blog. https://www.ellamind.com/blog/binary-vs-likert-scales
- [19] Busany, N. (2024, May 16). From TDD to EDD: Why Evaluation-Driven Development is the Future of AI Engineering. Medium. https://medium.com/@nimrodbusany_9074/from-tdd-to-edd-why-evaluation-driven-development-is-the-future-of-ai-engineering-a5e5796b2af4
- [20] Control theory. (n.d.). Wikipedia. https://en.wikipedia.org/wiki/Control_theory
- [21] Arize AI. (2024, February 21). How to Build LLM-as-a-Judge Evaluators That Hold Up In Production. Arize AI Blog. https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production
- [22] Gimeno, P., & Pardal, J. (2026, May 5). Better Experiments with LLM Evals: A Funnel, Not a Fork. Spotify Engineering. https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork
- [23] Zhou, Y., et al. (2024). Don't Trust Your Vibe: A Critical Look at LLM Evaluation by LLMs. OpenReview. https://openreview.net/forum?id=maMnVCHl8J
- [24] Wolfe, C. (2024, June 6). Finetuning an LLM to be a Better Judge. Cameron R. Wolfe. https://cameronrwolfe.substack.com/p/finetuned-judge
- [25] Iusztin, P. (2025, July 1). I created an AI Agent to write a Substack post for me. LinkedIn. https://www.linkedin.com/posts/pauliusztin_i-created-an-ai-agent-to-write-a-substack-activity-7420095430807691266-fQ1U
- [26] Zhang, R., et al. (2025). Creative Writing with an AI-Powered Writing Assistant: Perceptions and Challenges. Applied Sciences. https://www.mdpi.com/2076-3417/15/6/2971
- [27] Microsoft. (n.d.). Agent evaluation frameworks. Microsoft Learn. https://learn.microsoft.com/en-us/agents/architecture/evaluation-frameworks