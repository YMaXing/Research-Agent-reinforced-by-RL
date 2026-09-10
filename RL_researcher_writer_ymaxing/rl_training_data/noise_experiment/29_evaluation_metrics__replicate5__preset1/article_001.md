# The North Star of AI Engineering: A Framework for Evaluation-Driven Development

In our previous lessons, we instrumented our agents with observability tools like Opik and constructed offline datasets to test them. Now, we move to the core theoretical framework for designing the metrics themselves. In classical machine learning, we rely on rigorous evaluation standards like accuracy, precision, recall, and F1 scores to measure performance. We demand statistical significance before declaring victory. Yet, in AI engineering, many teams fall back on "vibe checks," approving changes because an output "feels more coherent."

Investing in a proper evaluation layer is hard to prioritize. It delivers no immediate user-visible feature and requires upfront effort to design datasets and metrics, all while the pressure to ship new features mounts. However, this same investment greatly accelerates long-term iteration. It provides an objective signal on every change and catches regressions instantly. Evals are the north star of AI engineering: the single source of truth that tells you exactly which modifications improve your system and which degrade it.

In this lesson, we will establish the foundation for evaluation-driven development. We will cover:

*   How to operationalize evals using the **optimization flywheel**, a systematic process for evidence-based iteration and regression testing.
*   The trade-offs between **metric families** for unstructured outputs, from lexical overlap scores to semantic similarity and LLM judges.
*   Why you must define **custom business metrics** instead of relying on misleading public benchmarks or generic, out-of-the-box scores.
*   How **binary pass/fail judgments** deliver a clearer, more actionable signal than subjective Likert scales.

With the problem and its importance clear, we now examine how to operationalize evals inside a repeatable optimization flywheel that replaces intuition with evidence.

## Using Evals Through the Optimization Flywheel

To build intuition, let's examine how we can effectively use and integrate AI evaluations into our application development lifecycle. There are three core scenarios where evaluations provide value.

First, evals **quantify the quality of your system**. They provide a snapshot of its current performance on a fixed dataset against metrics that matter to your business. This initial measurement establishes a baseline, a critical reference point against which all future changes are judged. Without a baseline, you are flying blind. You cannot know if your system is production-ready, nor can you objectively determine if your modifications are actually making it better.

Second, metrics serve as **guidance when optimizing your system**. They provide the empirical evidence needed to steer development, transforming the process from one based on intuition to one based on data. Every proposed change, a new prompt, a different model, a tweaked retrieval strategy, becomes a testable hypothesis. The evaluation results are the experiment's outcome, telling you whether to adopt, discard, or rethink the change.

Third, evals act as **regression tests** that protect shared components from unintended degradation. In complex AI systems, a single prompt or tool can be used by multiple workflows. A change designed to improve one feature can easily break another. Here, the goal is not improvement but stability. By running a comprehensive evaluation suite before merging changes, you can catch these regressions automatically, ensuring that new features don't come at the cost of existing functionality.

### The Optimization Process

How does this look in a real-world scenario? The optimization flywheel is a step-by-step plan of attack.

1.  **Gather your dataset:** Assemble the offline evaluation dataset. This is your ground truth, containing a diverse set of inputs that represent real-world use cases and known edge cases.
2.  **Build your metrics:** Define business-aligned metrics to measure performance. As we will see, these should be custom, binary checks that reflect what success means for your product.
3.  **Establish a baseline:** Run evals on the current system to compute baseline scores. This number is your stake in the ground, the score you need to beat.
4.  **Start the optimization:** Make one isolated change you believe will improve performance. This could be a prompt tweak, a model swap, or a change in your RAG strategy.
5.  **Compute the new score:** Re-evaluate the entire dataset by re-running the evals on the modified system.
6.  **Compare:** Compare the new scores to the baseline, considering statistical significance. Is the improvement real or just noise?
7.  **Decide:** If the score is better, you keep the change. If it is the same, you might still keep it if it reduces cost or latency. If it is worse, you revert it.
8.  **Repeat:** Repeat the cycle, continuously iterating until the scores meet your quality bar for production.

This iterative process turns optimization from a guessing game into a systematic, evidence-driven engineering discipline.![Diagram of the AI optimization flywheel](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-4d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down)
Image 1: The iterative optimization flywheel for AI applications using evaluations. (Source: https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-4d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down)

It is critical to keep all components fixed except for one variable per cycle. Confounding multiple modifications makes it impossible to attribute score movements to a specific change, turning the process back into guesswork. If you change the prompt, the model, and the retrieval strategy all at once, you will have no idea which change was responsible for the final outcome.

This disciplined, single-variable approach is a practical application of causal inference, the discipline of identifying what interventions actually cause a change in outcomes. While predictive models tell you what is likely to happen, causal inference tells you what to do about it. By isolating one change, you are attempting to create a controlled experiment that allows you to attribute the change in score directly to your modification, avoiding confounding variables that would otherwise make the results impossible to interpret [[59]](https://telnyx.com/learn-ai/casual-inference-explained).

Furthermore, you must distinguish between statistical significance and **practical significance**, which is anchored to actual business impact [[71]](https://arxiv.org/html/2605.02050v1). This idea draws from decision theory in fields like clinical trials, where the goal is not just to find a statistical effect but to determine if a model leads to better decisions [[70]](https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation). The key is to define a "net benefit" threshold that is relevant to your use case.

For a high-volume support bot processing millions of queries, a tiny 0.5% reduction in checkout errors could translate to thousands of fewer failed transactions and substantial savings in lost revenue and support costs [[46]](https://www.nngroup.com/articles/practical-significance). In this context, the small improvement has a massive net benefit and is worth prioritizing. Conversely, for a low-volume creative writing tool used by a few hundred people, a small bump in a "helpfulness" score may have no discernible impact on user satisfaction or business outcomes. The improvement is statistically present but practically irrelevant. This threshold reflects your tolerance for misclassification costs—the harm of a false positive versus the benefit of a true positive [[70]](https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation).

### Regression Testing

The optimization flywheel can be adapted for regression testing. This process is analogous to implementing **quality gates**, a concept from manufacturing and software engineering where automated pass/fail checkpoints enforce predefined standards [[65]](https://www.softwareseni.com/building-quality-gates-for-ai-generated-code-with-practical-implementation-strategies). By running the full evaluation suite before merging any new feature that touches shared components, you ensure that new features do not degrade the quality of existing ones, stopping a problematic change early before it reaches production [[66]](https://www.codecentric.de/en/knowledge-hub/blog/evaluating-machine-learning-models-quality-gates).

The strategy involves five steps:

1.  **Implement a new feature:** You write the code and verify it works locally for the new use case, ensuring it meets the immediate requirements.
2.  **Run the AI evaluations:** You run the full suite of assessments, covering all previous use cases captured in your dataset, not just the new one.
3.  **Compare Scores:** You compare the new scores against the established baseline from before your changes were introduced.
4.  **Metrics similar to baseline:** If the scores are identical or within an acceptable, predefined range of the baseline, your feature is considered safe and can be merged.
5.  **Metrics lower than the baseline:** If the scores are worse, you have introduced a regression. You must fix your code and repeat the process from step 2.![Diagram of AI evaluations in a CI pipeline](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down)
Image 2: Integrating AI evaluations into CI pipelines for regression testing. (Source: https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down)

This treats evals like integration tests, where you compare scores against a moving baseline instead of enforcing a strict pass/fail threshold. As your product evolves, the dataset must continuously expand. You should add new samples that cover edge cases for new features, production trace failures captured via observability tools like Opik, and hard debugging examples that expose current failure modes.

Instead of writing new tests in code, you broaden the tests by adding new data to the dataset. For instance, if you discover a real-world regression from production data, you can add that specific interaction to your evaluation dataset to ensure the same failure never happens again [[28]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets). This living dataset becomes a comprehensive record of your system's expected behavior and known failure points.

With the flywheel mechanics clear, we can now examine the different families of metrics we might plug into it when dealing with unstructured outputs.

## Exploring Possible Metric Types

The core difficulty in evaluating AI systems is that we are often dealing with unstructured text, reasoning traces, and sometimes image outputs. Unlike classical ML with structured labels, standard accuracy-style metrics are often unavailable.

There are three core families of metrics to consider.

### 1. BLEU and ROUGE

N-gram overlap metrics like Bilingual Evaluation Understudy (BLEU) and Recall-Oriented Understudy for Gisting Evaluation (ROUGE) are lexical metrics that work by counting overlapping words and phrases between a generated text and a reference text [[30]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ). Their pros are that they are fast to compute, widely understood, and deterministic. However, their cons are notable: they are blind to semantic equivalence, cannot handle paraphrasing, and do not care about factual accuracy. A response can be perfectly correct but receive a low score if it uses different wording than the reference [[33]](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb). For example, "The test was successful" would score near zero against the reference "The experiment succeeded," despite meaning the same thing.

### 2. BERTScore

Embedding similarity metrics like BERTScore address the semantic limitations of n-gram methods. They work by embedding the generated and reference texts into a high-dimensional vector space and measuring their closeness using cosine similarity. This approach uses contextual embeddings, meaning it understands that "bank" in "river bank" is different from "bank" in "financial bank" [[BERTScore explained: A modern metric for evaluating text generation](https://spotintelligence.com/2024/08/20/bertscore/)]. This captures semantic meaning far better than pure lexical methods. However, they are still fundamentally comparison metrics and are unable to verify complex business rules or logic. A fluently written piece of nonsense can still achieve a high BERTScore if it is semantically close to the reference text.

### 3. LLM Judges

The LLM-as-a-judge approach involves prompting a capable evaluator model with the input, the output, a set of detailed criteria, few-shot examples, and chain-of-thought instructions. The judge then produces a structured judgment, which can incorporate domain-specific guidelines and multi-faceted requirements [[38]](https://www.braintrust.dev/articles/what-is-llm-as-a-judge). This method is highly flexible and customizable, allowing you to evaluate subjective aspects like tone or brand voice and provide detailed, human-like critiques [[50]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge). The main drawback is that their performance depends heavily on the quality of the prompt and the evaluator model. They can also be slower and more expensive than automated metrics and may inherit the LLM’s biases if not properly developed and tested [[52]](https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw).

| Metric Family | Speed | Cost | Semantic Awareness | Business Alignment | Explainability |
| --- | --- | --- | --- | --- | --- |
| **BLEU/ROUGE** | Very Fast | Very Low | Low | Very Low | High |
| **BERTScore** | Fast | Low | High | Low | Medium |
| **LLM Judges** | Slow | High | Very High | Very High | High |

Table 1: A trade-off summary of different metric families.

For the kinds of guideline adherence, structure fidelity, and research grounding needed for complex workflows like our capstone projects, LLM judges are the most practical choice.

Now, you have heard from us repeatedly: "business metrics here, business metrics there." Let's understand why defining your own business metrics is such an essential and underrated step in building your AI evals strategy.

## Why Business Metrics Over Benchmarks

Benchmarks are the most deceiving type of metric. Looking at popular leaderboards or open benchmarks to find the best LLM and make product decisions is often a mistake.

There are two core reasons for this. First, benchmarks often function as marketing artifacts. Once a test set becomes public, teams can overfit to it, "train on the test set," and hill-climb on leaderboard scores [[15]](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053). This is exacerbated by data contamination, where public test data unintentionally leaks into training datasets, compromising evaluation integrity [[11]](https://www.evidentlyai.com/llm-guide/llm-benchmarks). The benchmark loses its validity because the set no longer represents unseen data. There have been instances where models were fine-tuned on test sets to inflate their final scores, producing too-good-to-be-true results [[Benchmark Overfitting in Large Language Models](https://openreview.net/forum?id=XbVMiW0jTM)].

Second, there is a fundamental mismatch between typical benchmark tasks, such as solving math problems or answering generic questions, and real business workloads like long-form creative writing, nuanced legal analysis, or personalized customer support [[12]](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches). A model's ability to score well on MMLU has little bearing on its ability to draft a brand-aligned marketing email. The proper role for benchmarks is narrow: advancing research, helping with initial model selection during early exploration, but never as a proxy for product-level decisions or optimization targets.

If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous. We must instead build metrics that are deeply tied to our specific application.

## Why Custom Business Metrics Over Generic Metrics

Generic metrics like toxicity, helpfulness, or RAGAS-style faithfulness act as a mirage. They optimize the wrong signal and create false confidence because they lack context about your product, user expectations, and brand voice [[16]](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP). An AI application can score brilliantly on "helpfulness" but fail catastrophically on your specific constraints.

This problem is not unique to AI engineering. In healthcare AI evaluation, researchers have found that many common classification metrics, like the F1 score, are "improper" because they can be gamed. A model can improve its score by changing its predictions in a way that actually makes clinical decisions worse. Such metrics conflate statistical performance with clinical utility without properly accounting for what matters in the real world [[70]](https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation).

Consider the dashboard below. It looks impressive, with scores for "Truthfulness" and "Personalization." But what does a 3.7 in Personalization actually mean?![Dashboard with generic AI metrics labeled 'Don't Do This!'](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down)
Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!" (Source: https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down)

Let's assume we want to check if an article written by our Brown agent contains hallucinations. A generic `hallucination` score might return "positive," but what does that tell us? Did it add information not present in the research? Did it deviate from the article guidelines? Or did it simply include a personal story that was not in the source text but is factually correct and relevant?

A generic detector might flag an engaging personal anecdote as a fabrication because it doesn't appear in the source documents. Yet, that same anecdote may be exactly what your brand voice requires for this specific article type. The generic metric, lacking this context, cannot distinguish between an undesirable invention (a hallucinated fact) and a desirable creative elaboration (a brand-aligned story).

Prefab scores are fundamentally limited. They lack any notion of your domain-specific constraints; a generic "helpfulness" score cannot know that your legal AI must never cite overruled case law. They are unable to localize failure; a low "faithfulness" score on a long article doesn't tell you which of the 50 claims was the problem. Finally, they introduce additional statistical noise into your decision-making, creating the illusion of precision with numbers that are disconnected from your actual product goals.

There is, however, a narrow and valid role for generic metrics during exploratory data analysis. They can be used as a flashlight to surface interesting examples for human review, but never as the primary optimization target [[The Mirage of Generic AI Metrics](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics)]. Here are a few useful examples:

1.  **Verbosity:** Sort your outputs by length to reveal if your most verbose answers are rambling and unhelpful. This helps you spot failure modes in long-form generation.
2.  **Similarity Score:** Use this to evaluate your RAG retriever specifically. If the similarity between the user query and the retrieved chunks is low, your retriever is likely failing to find relevant information. This is a valid component-level check.
3.  **BERTScore:** Use this to check the quality of your golden references. If you find a cluster of outputs with a low BERTScore against a reference you expected to be similar, you might realize the LLM found a more creative or even better way to solve the problem than your reference answer.

In all these cases, the generic metric is the starting point of an investigation, not the final verdict. Every production metric must be deeply application-centric, derived from concrete product requirements, user success criteria, and explicit constraints.

Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments from our LLM judge. Here, binary pass/fail criteria outperform every alternative.

## Choosing Binary Metrics Over Anything Else

When designing these custom metrics, you will face a choice: should you use a Likert scale (e.g., 1-5 stars) or a binary pass/fail? We strongly recommend **binary metrics**.

Likert scales are a seductive trap. They introduce several problems that sabotage your evaluation process [[4]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals):

1.  **Inconsistent Labeling:** There is high subjectivity in deciding whether an output is a 3 or a 4. One person's "4" is another's "3," making it difficult to achieve high inter-annotator agreement.
2.  **Statistical Noise:** Detecting a meaningful improvement becomes much harder. A shift from an average score of 3.2 to 3.4 is often statistically indistinguishable from random variance. From an information theory perspective, scalar ratings introduce noise that inflates entropy, or uncertainty, without adding meaningful structural information. A binary metric reduces this noise, leading to a clearer signal [[60]](https://arxiv.org/html/2602.07168).
3.  **Lazy Decision-Making:** Evaluators, both human and LLM, often default to middle values to avoid making a difficult judgment call. This "satisficing" behavior hides uncertainty rather than resolving it [[6]](https://www.scribbr.com/methodology/likert-scale).

Binary evaluations work because they **force decisions**. An output either met a specific criterion or it did not. This simple constraint is incredibly powerful. The benefits are immediate:

1.  **Clearer Thinking:** They force precise, unambiguous definitions of quality. You cannot hide in ambiguity.
2.  **Consistency:** They yield higher inter-annotator and inter-judge consistency because the decision is simpler.
3.  **Actionability:** They deliver an immediate, actionable failure signal. An engineer seeing a spike in the "Constraint Violation" failure rate knows exactly where to start debugging.

<aside>
💡
**Note:** The 3 points above translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate the inherent randomness of LLMs. LLMs are much more stable when asked to make a binary decision than when asked to assign a scalar value. A binary metric translates to a more robust and repeatable evaluation pipeline.

</aside>

### Capturing Nuance

The standard objection is, "But I'm losing nuance! A 1-5 scale captures shades of gray." This is a valid concern, but a Likert scale is the wrong solution. The right way to capture nuance is not by making your scale fuzzier, but by making your criteria more **granular**. You should decompose overall quality into multiple, specific, binary checks [[The 5-Star Lie: You’re Doing AI Evaluations Wrong](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals)].

For our writing agent, instead of rating an article 1-5 for "Quality," we can create multiple binary evaluations that capture specific dimensions of quality:

1.  **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
2.  **Flow of Ideas Adherence:** Does the generated article present ideas in the same order as the expected article? (Yes/No)
3.  **Article Guideline Adherence:** Does the generated article follow the flow of ideas from the article guideline input? (Yes/No)
4.  **Research Anchoring:** Is every claim in the article supported by the provided research? (Yes/No)

By aggregating these binary signals—perhaps with a simple average or a weighted sum that prioritizes critical criteria—you can construct a highly nuanced view of overall performance. A single dashboard can now show you, "Our system passes Content Adherence 95% of the time and Flow Adherence 92% of the time, but it fails Research Anchoring 40% of the time." This is a precise, actionable signal. You know exactly where your system is strong and where it is failing, allowing you to focus your optimization efforts where they will have the most impact. You have captured all the desired nuance without sacrificing clarity, and you can track progress on each dimension independently. This approach is simple, intuitive, scalable, and robust in production systems.

With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in the next lesson.

## Conclusion

The path to a truly robust AI product requires a shift away from vibe checks, leaderboards, and generic scores. It demands a commitment to rigorous, evaluation-driven development built on custom, binary, business-aligned metrics. Granular pass/fail criteria deliver the clearest optimization signal, avoiding the statistical noise and subjectivity inherent in scalar ratings. This systematic, measurement-driven approach is the core engine of product improvement. In our next lesson, we will translate this theory into practice by implementing custom LLM judges from scratch to evaluate our Brown writing workflow.

## References

- [1] Husain, H. (n.d.). Using LLM-as-a-Judge For Evaluation: A Complete Guide. *Hamel’s Blog*. https://hamel.dev/blog/posts/llm-judge/
- [2] Yan, E. (n.d.). Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge). *eugeneyan.com*. https://eugeneyan.com/writing/llm-evaluators/
- [3] PROBE: BENCHMARKING REASONING PARADIGM OVERFITTING IN LARGE LANGUAGE MODELS. (n.d.). *OpenReview*. https://openreview.net/forum?id=XbVMiW0jTM
- [4] Iusztin, P. (2025, October 21). The 5-Star Lie: You’re Doing AI Evaluations Wrong. *Decoding AI*. https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals
- [5] Husain, H. (2025, October 9). The Mirage of Generic AI Metrics. *Decoding AI*. https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics
- [6] Streefkerk, R. (2023, June 22). Likert Scale | Definition, Examples, and Analysis. *Scribbr*. https://www.scribbr.com/methodology/likert-scale
- [7] Bowne-Anderson, H., & Krawczyk, S. (2025, October 16). Escaping POC Purgatory: Evaluation-Driven Development for AI Systems. *Decoding AI*. https://www.decodingai.com/p/escaping-poc-purgatory-evaluation
- [8] Bowne-Anderson, H. (2025, October 30). Stop Launching AI Apps Without This Framework. *Decoding AI*. https://www.decodingai.com/p/stop-launching-ai-apps-without-this
- [9] Mansuy, R. (2023, September 20). Evaluating NLP Models: A Comprehensive Guide to ROUGE, BLEU, METEOR, and BERTScore Metrics. *PlainEnglish.io*. https://plainenglish.io/blog/evaluating-nlp-models-a-comprehensive-guide-to-rouge-bleu-meteor-and-bertscore-metrics-d0f1b1
- [10] Datumo. (n.d.). Key NLP Evaluation Metrics. https://datumo.com/en/blog/insight/key-nlp-evaluation-metrics/
- [11] Evidently AI. (n.d.). LLM benchmarks: 30+ benchmarks and how they work. https://www.evidentlyai.com/llm-guide/llm-benchmarks
- [12] Raschka, S. (2024, May 26). A Guide to LLM Evaluation: 4 Approaches. *Ahead of AI*. https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches
- [13] Van Otten, N. (2024, August 20). BERTScore explained: A modern metric for evaluating text generation. *Spot Intelligence*. https://spotintelligence.com/2024/08/20/bertscore/
- [14] EllaMind. (n.d.). Binary vs. Likert Scales in AI Evaluation. https://www.ellamind.com/blog/binary-vs-likert-scales
- [15] Hari, B. (2026, April 26). AI — Benchmark scores are becoming marketing; dynamic eval is the only antidote. *HEY World*. https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053
- [16] Aggarwal, S. (2025, October 29). AI evaluation is broken when we hide behind generic metrics. *LinkedIn*. https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP
- [28] Comet. (n.d.). Manage Datasets. *Opik Docs*. https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets
- [30] Ferrer, J. (2025, December 9). LLM evaluation benchmarking: Beyond BLEU and ROUGE. *Weights & Biases*. https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ
- [33] Sthanikam, S. (2023, April 20). Understanding BLEU and ROUGE score for NLP Evaluation. *Medium*. https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb
- [38] Braintrust. (n.d.). What is LLM-as-a-judge? https://www.braintrust.dev/articles/what-is-llm-as-a-judge
- [46] Budiu, R. (2022, November 20). Practical Significance in UX Research. *Nielsen Norman Group*. https://www.nngroup.com/articles/practical-significance
- [48] Sturdivant, R. (2007, June 18). Effective uses of effect size statistics to demonstrate business value. *Quirks*. https://www.quirks.com/articles/effective-uses-of-effect-size-statistics-to-demonstrate-business-value
- [50] Evidently AI. (2026, May 19). LLM-as-a-judge: a complete guide to using LLMs for evaluations. https://www.evidentlyai.com/llm-guide/llm-as-a-judge
- [52] Abdella, A. (2025, July 11). LLM as a Judge is scalable, cost-effective, good at understanding open-ended AI-generated content. *LinkedIn*. https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw
- [59] Causal Inference Explained. (n.d.). *Telnyx*. https://telnyx.com/learn-ai/casual-inference-explained
- [60] Information Theory in Image Processing. (2026, February 13). *arXiv*. https://arxiv.org/html/2602.07168
- [65] Building Quality Gates for AI-Generated Code with Practical Implementation Strategies. (n.d.). *SoftwareSeni*. https://www.softwareseni.com/building-quality-gates-for-ai-generated-code-with-practical-implementation-strategies
- [66] Evaluating Machine Learning Models with Quality Gates. (n.d.). *codecentric*. https://www.codecentric.de/en/knowledge-hub/blog/evaluating-machine-learning-models-quality-gates
- [70] Gebauer, S. (n.d.). Three Metrics for Healthcare AI Evaluation You Need to Know. *Substack*. https://sarahgebauermd.substack.com/p/three-metrics-for-healthcare-ai-evaluation
- [71] Statistical analysis and inference for AI evaluation RCTs. (2026, May 4). *arXiv*. https://arxiv.org/html/2605.02050v1