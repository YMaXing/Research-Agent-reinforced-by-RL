# The North Star of AI Engineering: A Guide to Evaluation-Driven Development

In our last lessons, we instrumented our AI agents with observability tools like Opik and learned how to build offline datasets from production traces. Now, we move to the core theoretical framework of designing the metrics themselves. In classical machine learning, we rely on rigorous evaluation standards like accuracy, precision, and F1-scores. In AI engineering, however, it is common to see teams rely on "vibe checks" or skip evaluation altogether, approving changes because an output "feels more coherent."

Investing in a proper evaluation layer can feel hard to prioritize. It delivers no immediate user-visible feature and requires upfront effort to design datasets and metrics, all while competing with the pressure to ship. But this same investment dramatically accelerates long-term iteration. It provides an objective signal on every change and catches regressions instantly.

Evals are the north star of AI engineering: the single source of truth that tells you exactly which modifications improve the system and which degrade it. This lesson will establish the theoretical foundation for evaluation-driven development (EDD) by covering:

*   The optimization flywheel and its three core use cases.
*   Metric trade-offs for unstructured outputs.
*   Why business metrics beat benchmarks and generic scores.
*   Why binary judgments are superior to Likert scales.

With the problem and its importance clear, we will now examine how to operationalize evals inside a repeatable optimization flywheel that replaces intuition with evidence.

## Using Evals Through the Optimization Flywheel

To build intuition, let's examine how we can effectively use and integrate AI evaluations into our application development lifecycle. There are three core scenarios where evaluations provide value. First, evals **quantify the quality of your system** on a set of given metrics, snapshotting a baseline of its current state. Without this baseline, you cannot know if the system is ready for production or if it is improving. Second, metrics serve as **guidance when optimizing your system**, shifting development from intuition-based to evidence-based. Finally, they act as **regression tests** that protect shared components, ensuring stability rather than just improvement. This is critical in AI engineering, as components are often interconnected.

### The Optimization Process

How does this look in a real-world scenario? The optimization flywheel is an eight-step process for systematically improving your AI application.

1.  **Gather your dataset:** Assemble an offline dataset that represents the real-world scenarios your application will face.
2.  **Build your metrics:** Define a set of business-aligned metrics that capture what "good" looks like for your product.
3.  **Establish a baseline:** Run your evaluation suite on the current system to compute baseline scores for each metric.
4.  **Start the optimization:** Make one isolated change you believe will improve performance, such as tweaking a prompt or swapping a model.
5.  **Compute the new score:** Re-evaluate the entire dataset by re-running the evals on the modified system.
6.  **Compare:** Analyze the new scores against the baseline, considering statistical significance.
7.  **Decide:** Based on whether the score is better, the same, or worse, decide to keep the change, revert it, or conduct further analysis.
8.  **Repeat:** Continue the cycle until your scores meet the desired quality threshold.

This iterative process turns subjective guesswork into a systematic, evidence-driven workflow.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-4d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down
Image 1: The iterative optimization flywheel for AI applications using evaluations.

It is critical to keep all components fixed except for one variable per cycle. Confounding multiple modifications makes it impossible to attribute score movements and turns the process back into guesswork. This principle is grounded in the field of causal inference, which aims to distinguish correlation from causation. When multiple variables change simultaneously, their effects are confounded, making it impossible to know which change drove the outcome [[55]](https://www.statsig.com/perspectives/causal-inference-in-product-experimentation). By changing only one thing at a time—a prompt, a model parameter, or a retrieval strategy—you can confidently attribute any performance change to that specific modification [[27]](http://www.jmlr.org/papers/volume7/MLOPT-intro06a/MLOPT-intro06a.pdf).

Furthermore, you must anchor statistical significance to actual **business impact** [[46]](https://www.nngroup.com/articles/practical-significance), [[47]](https://www.statsig.com/perspectives/understanding-statistical-significance). Decision theory from high-stakes fields like medicine provides a useful framework here called "net benefit analysis," which connects a decision threshold to the explicit costs of misclassification [[56]](https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation). For a high-volume support bot, a 0.5% reduction in checkout errors may be worth thousands of dollars, justifying a change. In contrast, for a low-volume creative writing tool, a similar small improvement might be negligible to users, requiring a much larger movement before you declare victory [[48]](https://www.quirks.com/articles/effective-uses-of-effect-size-statistics-to-demonstrate-business-value).

### Regression Testing

The optimization flywheel can be adapted for regression testing, an approach analogous to the "quality gates" used in modern software development and Six Sigma manufacturing. These are automated pass/fail checkpoints that enforce predefined standards [[57]](https://www.softwareseni.com/building-quality-gates-for-ai-generated-code-with-practical-implementation-strategies). Before merging any new feature that touches shared components, you run the full eval suite to guard against breaking existing behavior. This transforms AI evaluations into a powerful regression testing framework that ensures new features do not degrade existing ones.

This five-step process integrates directly into your development workflow:

1.  **Implement a new feature:** You write the code and verify it works locally for the new use case.
2.  **Run the AI evaluations:** You run the full suite of assessments, covering all previous use cases, not just the new one.
3.  **Compare Scores:** Compare the new scores against the baseline from your main production branch.
4.  **Metrics similar to baseline:** If the scores are nearly identical to the baseline, your feature has not introduced a regression. You can merge it.
5.  **Metrics lower than the baseline:** If any score is significantly worse, you have introduced a regression. You should fix your code and repeat the process.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down
Image 2: Integrating AI evaluations into CI pipelines for regression testing.

Unlike traditional unit tests with fixed pass/fail thresholds, AI evals compare scores against a moving baseline. This is more like an integration test for your AI system's probabilistic components.

Your evaluation dataset must continuously expand. As new features are added, you must include their edge cases. When observability tools like Opik capture production failures, those traces should be converted into new evaluation samples [[28]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets). Hard debugging examples that expose current failure modes also become permanent additions. Instead of writing new tests in code, you broaden the test coverage by adding new, challenging samples to your dataset [[29]](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals).

With the flywheel mechanics clear, we can now examine the different families of metrics we might plug into it when dealing with unstructured outputs.

## Exploring Possible Metric Types

The core difficulty in evaluating AI systems is that we are often dealing with unstructured text, reasoning traces, or even images, where standard accuracy metrics do not apply. There are three main families of metrics designed to handle these outputs.

### 1. BLEU and ROUGE

N-gram overlap metrics like BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Oriented Understudy for Gisting Evaluation) are the oldest and simplest. They work by counting the number of overlapping words or sequences of words (n-grams) between the generated text and a reference text [[33]](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb). Their main advantages are that they are fast, deterministic, easy to understand, and require no additional models [[31]](https://www.traceloop.com/blog/demystifying-the-bleu-metric). However, they are blind to semantic meaning. They penalize valid paraphrasing and cannot assess if the reasoning is correct, only if the words match [[30]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ), [[34]](https://www.elastic.co/search-labs/blog/evaluating-rag-metrics).

### 2. BERTScore

Embedding similarity metrics like BERTScore address the semantic blindness of n-gram methods. They use a pre-trained language model like BERT to convert both the generated and reference texts into high-dimensional vector embeddings. By calculating the cosine similarity between these embeddings, BERTScore can measure how semantically close the two pieces of text are. This allows it to recognize paraphrases and different phrasings that carry the same meaning [[30]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ). While this is a significant improvement, it is still a comparison metric and cannot verify complex business logic or factual accuracy on its own.

### 3. LLM Judges

The LLM-as-a-judge approach uses a capable LLM to evaluate an output based on a detailed set of criteria [[38]](https://www.braintrust.dev/articles/what-is-llm-as-a-judge). You provide the judge model with the input, the generated output, a rubric, few-shot examples, and chain-of-thought instructions. This method is highly flexible and can be customized to evaluate subjective qualities like tone, brand voice, or adherence to complex guidelines [[50]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge). The main drawback is that performance depends heavily on the prompt and the evaluator model. LLM judges can also be slower, more expensive, and may inherit the biases of the underlying model if not carefully designed and validated [[52]](https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw), [[53]](https://cameronrwolfe.substack.com/p/llm-as-a-judge).

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

First, public benchmarks often function as marketing artifacts. Once a test set is public, teams can inadvertently or intentionally overfit to it, "teaching to the test" to climb leaderboards. This inflates scores and erodes the benchmark's validity, as it no longer represents unseen data. There have been instances where models were found to have been trained on test sets, leading to misleadingly high performance [[11]](https://www.evidentlyai.com/llm-guide/llm-benchmarks), [[15]](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053).

Second, there is a fundamental mismatch between typical benchmark tasks—like solving math problems (GSM8K) or answering trivia—and the complex, nuanced workloads of a real business application [[12]](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches), [[14]](https://arxiv.org/html/2601.20617v1). A model that excels at multiple-choice questions may fail completely at generating long-form creative content or providing empathetic customer support.

The proper role for benchmarks is narrow: they are useful for advancing research frontiers and for initial model filtering during early exploration. They should never be used as a proxy for product-level decisions or become the primary optimization target [[13]](https://launchdarkly.com/blog/llm-evaluation).

If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous. We must instead build metrics that are deeply tied to our specific application.

## Why Custom Business Metrics Over Generic Metrics

Generic, off-the-shelf metrics like "toxicity," "helpfulness," or RAGAS-style "faithfulness" create a mirage. They optimize for the wrong signal and create false confidence because they lack context about your product, user expectations, and brand voice [[16]](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP). An AI application can score brilliantly on a generic "helpfulness" metric but fail catastrophically on your specific business constraints.

A classic example is the F1 score, widely used for imbalanced datasets. While it seems objective, it is considered an "improper" metric for many real-world decisions because a model can improve its F1 score in ways that make business outcomes worse. In medicine, F1 ignores true negatives, yet correctly identifying that a patient *doesn't* need surgery is a critical outcome [[56]](https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation).

Consider the dashboard below. It looks impressive, with scores for "Truthfulness" and "Personalization." But what does a 3.7 in "Personalization" actually mean?

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down
Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"

For example, let's assume we want to check if an article written by our Brown agent contains hallucinations. A generic `hallucination` score might return "positive," but what does that tell us? Did it add information not present in the research? Did it deviate from the article guidelines? Or did it simply include a personal story that, while not in the source text, is factually correct and aligns with the desired brand voice? A generic detector might flag an engaging personal anecdote as a fabrication, yet that same anecdote may be exactly what your brand requires. The generic metric cannot distinguish between undesirable invention and desirable creative elaboration.

Prefab scores are limited because they lack domain-specific constraints, cannot localize which part of an output failed, and introduce statistical noise into decision-making [[18]](https://arxiv.org/html/2508.13816v1), [[20]](https://toloka.ai/blog/llm-evaluation-from-classic-metrics-to-modern-methods).

Generic metrics do have a narrow, valid role, but only during exploratory data analysis. You can use them as a "flashlight" to surface interesting traces for manual review, not as a "report card" for grading overall quality. Here are some useful examples:

1.  **Verbosity:** Sort your outputs by length. This can reveal if your most verbose answers are rambling and unhelpful or if your shortest answers are curt and missing information.
2.  **Similarity Score:** Use this to evaluate your RAG retriever specifically. If the similarity between the user query and the retrieved chunks is low, your retriever is likely failing. This is a valid component-level check.
3.  **BERTScore:** Use this to check the quality of your "golden" reference answers. If you find a cluster of outputs with a low BERTScore against a reference you expected to be similar, it might be that the LLM found a more creative or even better solution than your reference.

In all these cases, the generic metric is the start of an investigation, not the final verdict. Every production metric must be deeply application-centric, derived from concrete product requirements, user success criteria, and explicit constraints.

Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments from our LLM judge. Here, binary pass/fail criteria outperform every alternative.

## Choosing Binary Metrics Over Anything Else

When designing these custom metrics, you will face a choice: should you use a Likert scale (e.g., 1-5 stars) or a binary pass/fail? We strongly recommend **binary metrics**.

Likert scales are a seductive trap. They promise nuance but introduce ambiguity and noise. There are three main problems with them [[4]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals):

1.  **Inconsistent Labeling:** The difference between a '3' and a '4' is subjective and varies between annotators, leading to low inter-annotator agreement.
2.  **Statistical Noise:** Detecting a meaningful improvement from an average score of 3.2 to 3.4 requires a much larger sample size than detecting a shift in a binary pass rate from 75% to 80% [[5]](https://www.ellamind.com/blog/binary-vs-likert-scales).
3.  **Lazy Decision-Making:** Annotators—and LLM judges—often default to the middle value ('3') to avoid a difficult judgment, hiding uncertainty instead of resolving it.

Binary evaluations work because they **force decisions**. An output either met a specific criterion or it did not. This simple constraint is incredibly powerful and offers several advantages:

1.  **Clearer Thinking:** Binary evaluations force you to create precise, unambiguous definitions of quality. You cannot simply label something as "Fail" without knowing *why* it failed.
2.  **Consistency:** Binary decisions are faster and more consistent for both human annotators and LLM judges, reducing fatigue and increasing throughput.
3.  **Actionability:** The result is not a fuzzy number but a clear signal tied to a specific problem. A spike in the "Constraint Violation" failure rate tells an engineer exactly where to start debugging.

This noise reduction can be quantified using principles from information theory. Scalar ratings introduce random fluctuations that inflate entropy—a measure of uncertainty—without adding meaningful information. Binary decisions, by contrast, reduce this entropy by forcing a clear judgment, thereby increasing the mutual information between the evaluation signal and the system's true quality [[58]](https://arxiv.org/html/2602.07168).

<aside>
💡
**Note:** The three points above translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate the inherent randomness of LLMs. LLMs are much more stable when asked to make a binary decision than when asked to assign a scalar value. A binary metric translates to a more robust and repeatable evaluation pipeline.
</aside>

### Capturing Nuance

The standard objection is, "But I'm losing nuance! A 1-5 scale captures shades of gray." This is a valid concern, but the solution is not a fuzzier scale. The right way to capture nuance is by making your criteria more **granular** [[9]](https://www.ellamind.com/blog/binary-vs-likert-scales).

Instead of a single, subjective rating for "Quality," you break it down into multiple, specific, binary checks. For our writing agent, instead of rating an article 1-5, we could create binary evaluations for distinct dimensions of quality:

1.  **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
2.  **Flow of Ideas Adherence:** Does the generated article present ideas in the same order as the expected article? (Yes/No)
3.  **Article Guideline Adherence:** Does the generated article follow the flow of ideas from the article guideline input? (Yes/No)
4.  **Research Anchoring:** Is every claim in the article supported by the provided research? (Yes/No)

By aggregating these binary signals—using a simple average or a weighted sum—you get a nuanced, multi-dimensional view of performance. This approach eliminates scale noise and middle-value bias, resulting in a system that is simple, intuitive, scalable, and robust.

With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in the next lesson.

## Conclusion

This lesson argued for a fundamental shift away from vibe checks, leaderboards, and generic scores toward a rigorous, evaluation-driven development process. This process is built on custom, binary, business-aligned metrics that provide a clear and actionable signal for improvement. We have established that granular pass/fail criteria deliver the strongest optimization signal while avoiding the statistical noise and subjectivity inherent in scalar ratings.

This theoretical foundation is the key to building reliable AI products. In the next lesson, we will translate this theory into practice by implementing custom LLM judges from scratch to evaluate our Brown writing workflow.

## References

- [1] Husain, H. (n.d.). Using LLM-as-a-Judge For Evaluation: A Complete Guide. Hamel’s Blog. https://hamel.dev/blog/posts/llm-judge/
- [2] Yan, E. (n.d.). Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-a-Judge). https://eugeneyan.com/writing/llm-evaluators/
- [3] PROBE: BENCHMARKING REASONING PARADIGM OVERFITTING IN LARGE LANGUAGE MODELS. (n.d.). OpenReview. https://openreview.net/forum?id=XbVMiW0jTM
- [4] Husain, H. (n.d.). The 5-Star Lie: You’re Doing AI Evaluations Wrong. Decoding AI. https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals
- [5] Binary vs. Likert scales in AI evaluation. (n.d.). Ellamind. https://www.ellamind.com/blog/binary-vs-likert-scales
- [6] Husain, H. (n.d.). The Mirage of Generic AI Metrics. Decoding AI. https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics
- [7] Bowne-Anderson, H. (2025, October 30). Stop Launching AI Apps Without This Framework. Decoding AI. https://www.decodingai.com/p/stop-launching-ai-apps-without-this
- [8] Bowne-Anderson, H., & Krawczyk, S. (2025, October 16). Escaping POC Purgatory: Evaluation-Driven Development for AI Systems. Decoding AI. https://www.decodingai.com/p/escaping-poc-purgatory-evaluation
- [9] Granular binary criteria for nuance. (n.d.). Ellamind. https://www.ellamind.com/blog/binary-vs-likert-scales
- [10] Rubric-based evals. (n.d.). Medium. https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80
- [11] LLM Benchmarks. (n.d.). Evidently AI. https://www.evidentlyai.com/llm-guide/llm-benchmarks
- [12] Raschka, S. (n.d.). LLM Evaluation Approaches. Sebastian Raschka's Magazine. https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches
- [13] LLM Evaluation. (n.d.). LaunchDarkly. https://launchdarkly.com/blog/llm-evaluation
- [14] Agent Benchmarks. (2026, January 20). ArXiv. https://arxiv.org/html/2601.20617v1
- [15] Hari, B. (2026, April 26). AI Benchmark Scores Are Becoming Marketing. https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053
- [16] Aggarwal, S. (n.d.). Generic Metrics Mirage. LinkedIn. https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP
- [17] NVIDIA Data Flywheel. (n.d.). Galileo. https://galileo.ai/blog/nvidia-data-flywheel-for-de-risking-agentic-ai
- [18] Metric Validity Concerns. (2025, August 13). ArXiv. https://arxiv.org/html/2508.13816v1
- [19] Human Evaluation Metrics. (n.d.). Galileo. https://galileo.ai/blog/human-evaluation-metrics-ai
- [20] LLM Evaluation Methods. (n.d.). Toloka. https://toloka.ai/blog/llm-evaluation-from-classic-metrics-to-modern-methods
- [21] Data Flywheel. (n.d.). NVIDIA. https://www.nvidia.com/en-us/glossary/data-flywheel
- [22] Vibe Checks vs. Rigorous Metrics. (n.d.). Substack. https://olshansky.substack.com/p/vibe-checks-are-all-you-need
- [23] VibeCheck Metric. (2024, October 12). ArXiv. https://arxiv.org/html/2410.12851v1
- [24] AI Evals vs. A/B Testing. (n.d.). GrowthBook. https://www.growthbook.io/blog/ai-evals-vs-a-b-testing-why-you-need-both-to-ship-genai
- [25] From Vibe Checks to Continuous Evaluation. (n.d.). Google Cloud Blog. https://cloud.google.com/blog/topics/developers-practitioners/from-vibe-checks-to-continuous-evaluation-engineering-reliable-ai-agents
- [26] Stop Evaluating LLMs with Vibe Checks. (n.d.). Towards Data Science. https://towardsdatascience.com/stop-evaluating-llms-with-vibe-checks
- [27] Sequential Minimal Optimization. (2006). JMLR. http://www.jmlr.org/papers/volume7/MLOPT-intro06a/MLOPT-intro06a.pdf
- [28] Expanding Datasets with Opik. (n.d.). Comet. https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets
- [29] Generate Synthetic Datasets. (n.d.). Decoding AI. https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals
- [30] Beyond BLEU and ROUGE. (2025, December 9). Weights & Biases. https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ
- [31] Demystifying BLEU. (n.d.). Traceloop. https://www.traceloop.com/blog/demystifying-the-bleu-metric
- [32] BLEU and ROUGE. (n.d.). Galileo Docs. https://docs.galileo.ai/concepts/metrics/expression-and-readability/bleu-and-rouge
- [33] Understanding BLEU and ROUGE. (n.d.). Medium. https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb
- [34] Evaluating RAG Metrics. (n.d.). Elastic. https://www.elastic.co/search-labs/blog/evaluating-rag-metrics
- [35] LLM-as-a-Judge Guide. (n.d.). Confident AI. https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method
- [36] LLM-as-a-Judge with CoT. (n.d.). Medium. https://medium.com/data-science-collective/llm-as-a-judge-when-to-use-reasoning-cot-and-explanations-964ad82ebc3d
- [37] Prompting Strategies for LLM-as-a-Judge. (n.d.). Arize. https://arize.com/blog/evidence-based-prompting-strategies-for-llm-as-a-judge-explanations-and-chain-of-thought
- [38] What is LLM-as-a-Judge. (n.d.). Braintrust. https://www.braintrust.dev/articles/what-is-llm-as-a-judge
- [39] LLM-as-a-Judge. (n.d.). Arize. https://arize.com/llm-as-a-judge
- [40] Mansuy, R. (2023, September 20). Evaluating NLP Models: A Comprehensive Guide to ROUGE, BLEU, METEOR, and BERTScore Metrics. PlainEnglish.io. https://plainenglish.io/blog/evaluating-nlp-models-a-comprehensive-guide-to-rouge-bleu-meteor-and-bertscore-metrics-d0f1b1
- [41] Key NLP Evaluation Metrics. (n.d.). Datumo. https://datumo.com/en/blog/insight/key-nlp-evaluation-metrics/
- [42] Van Otten, N. (2024, August 20). BERTScore explained: A modern metric for evaluating text generation. Spot Intelligence. https://spotintelligence.com/2024/08/20/bertscore/
- [43] LLM-as-a-Judge Guide. (n.d.). Evidently AI. https://www.evidentlyai.com/llm-guide/llm-as-a-judge
- [44] Likert Scale Issues. (n.d.). Scribbr. https://www.scribbr.com/methodology/likert-scale
- [45] Likert Scale Limitations. (n.d.). InMoment. https://inmoment.com/blog/likert-scale
- [46] Practical Significance. (n.d.). Nielsen Norman Group. https://www.nngroup.com/articles/practical-significance
- [47] Understanding Statistical Significance. (n.d.). Statsig. https://www.statsig.com/perspectives/understanding-statistical-significance
- [48] Effective Uses of Effect Size Statistics. (n.d.). Quirks. https://www.quirks.com/articles/effective-uses-of-effect-size-statistics-to-demonstrate-business-value
- [49] What is Statistical Significance? (n.d.). CloudResearch. https://www.cloudresearch.com/resources/guides/statistical-significance/what-is-statistical-significance
- [50] LLM-as-a-Judge Pros and Cons. (n.d.). Evidently AI. https://www.evidentlyai.com/llm-guide/llm-as-a-judge
- [51] LLM-as-a-Judge vs Human Evaluation. (n.d.). Galileo. https://galileo.ai/blog/llm-as-a-judge-vs-human-evaluation
- [52] LLM as a Judge Trade-offs. (n.d.). LinkedIn. https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw
- [53] LLM-as-a-Judge Biases. (n.d.). Substack. https://cameronrwolfe.substack.com/p/llm-as-a-judge
- [54] Why LLM-as-a-Judge is the Best Method. (n.d.). Confident AI. https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method
- [55] Causal inference in product experimentation. (n.d.). Statsig. https://www.statsig.com/perspectives/causal-inference-in-product-experimentation
- [56] Three Metrics for Healthcare AI Evaluation You Need to Know. (n.d.). Substack. https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation
- [57] Building Quality Gates for AI-Generated Code. (n.d.). SoftwareSeni. https://www.softwareseni.com/building-quality-gates-for-ai-generated-code-with-practical-implementation-strategies
- [58] Information Theory for Noise Reduction. (2026, February 7). ArXiv. https://arxiv.org/html/2602.07168