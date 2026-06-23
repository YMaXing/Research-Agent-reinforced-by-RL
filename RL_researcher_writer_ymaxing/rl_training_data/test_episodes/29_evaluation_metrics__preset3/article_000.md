# Evaluation-Driven Development: The North Star of AI Engineering

In our last lessons, we instrumented our AI agents with observability tools like Opik and built our first offline evaluation datasets. We now have the raw materials for assessment: traces and test cases. But how do we move from a pile of data to a clear, objective measure of quality? How do we know if a change *actually* improved our system?

This lesson introduces the theoretical framework for designing the metrics themselves. In classical machine learning, evaluation is a non-negotiable, rigorous discipline. We rely on metrics like accuracy, precision, recall, and F1 scores to quantify performance, and we use statistical significance to validate our results. Yet, in the world of AI engineering, many teams fall back on "vibe checks." We run a few prompts, eyeball the outputs, and declare victory if it "feels more coherent."

Prioritizing a robust evaluation layer is difficult. It delivers no immediate, user-visible feature. It requires upfront effort to design datasets and metrics, all while the pressure to ship new features mounts. However, this investment dramatically accelerates long-term development. It provides an objective signal on every change, catches regressions instantly, and turns a chaotic, intuition-driven process into a disciplined engineering practice.

Evals are the north star of AI engineering. They are the single source of truth that tells you which modifications improve the system and which degrade it. In this lesson, we will explore:

-   The optimization flywheel and its three core use cases.
-   The trade-offs between different metric types for unstructured outputs.
-   Why custom business metrics are superior to public benchmarks and generic scores.
-   Why binary pass/fail judgments provide a clearer signal than Likert scales.

With the problem and its importance clear, we will now examine how to operationalize evals inside a repeatable optimization flywheel that replaces intuition with evidence.

## Using Evals Through the Optimization Flywheel

To build intuition, let's examine how we can effectively use and integrate AI evaluations into our application development lifecycle. There are three core scenarios where evaluations provide value.

First, evals **quantify the quality of your system** on a given set of metrics, creating a baseline snapshot of its current performance. Without this baseline, you cannot know if your system is production-ready or whether your changes are making it better or worse. Second, these metrics serve as **guidance when optimizing your system**. By providing evidence for experiments, they shift development from being intuition-based to evidence-based. Finally, evals act as **regression tests that protect shared components**. Unlike optimization, the goal here is stability. This is critical in AI engineering, where components like prompts, tools, and memory systems are often interconnected and a small change in one can cause unexpected failures in another [[1]](https://www.decodingai.com/p/escaping-poc-purgatory-evaluation).

This challenge is magnified because AI agents are probabilistic systems. Unlike traditional deterministic software where the same input always produces the same output, an agent might take different paths or produce slightly different results on identical inputs. This inherent unpredictability is why rigorous, data-driven evaluation is not optional; it is the only way to build reliable systems [[2]](https://www.datarobot.com/blog/agentic-ai-enterprise-design).

### The Optimization Process

How does this look in a real-world scenario? Let's look at a step-by-step plan for the optimization flywheel.

1.  **Gather your dataset:** Assemble an offline dataset that represents the key scenarios and edge cases for your application.
2.  **Build your metrics:** Define a suite of business-aligned metrics that measure what truly matters for your product's success.
3.  **Establish a baseline:** Run the evaluation suite on your current system to compute baseline scores for each metric.
4.  **Start the optimization:** Make one isolated change that you believe will improve performance, such as tweaking a prompt or changing a model parameter.
5.  **Compute the new score:** Re-evaluate the entire dataset by re-running the evals on the modified system.
6.  **Compare:** Compare the new scores to the baseline, checking for statistical significance.
7.  **Decide:** If the score is better, keep the change. If it is the same, consider its complexity before deciding. If it is worse, revert the change.
8.  **Repeat:** Repeat this cycle until the scores meet your target for production readiness.![The iterative optimization flywheel for AI applications using evaluations.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-4d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down)
Image 1: The iterative optimization flywheel for AI applications using evaluations.

It is critical to keep all components fixed except for one variable per cycle. Confounding multiple modifications makes it impossible to attribute score movements to a specific cause, turning the process back into guesswork.

While isolating a single variable is the scientific ideal, it can be difficult in complex, interconnected agentic systems. A change in one agent's prompt can cause unpredictable emergent behaviors or cascading failures in downstream agents, a problem known as inter-agent misalignment [[3]](https://arxiv.org/html/2505.10468v1). Your evaluations must be designed to capture these system-level effects, not just the performance of a single component.

The concept of "better" is always relative to the business use case. You must anchor statistical significance to actual business impact rather than arbitrary p-value thresholds [[4]](https://corporatefinanceinstitute.com/resources/data-science/statistical-significance). For a high-volume customer support bot, a tiny improvement can have a massive real-world gain. For instance, a change that reduces checkout errors by just 0.5% might sound small. But if your product processes 2 million checkouts a year, that is 10,000 fewer failed transactions. If each failure costs $15 in lost revenue or support time, that small improvement translates to $150,000 per year [[5]](https://www.nngroup.com/articles/practical-significance). In contrast, for a low-volume creative writing tool, a similar small improvement is likely negligible; larger movements are required before declaring victory.

### Regression Testing

A powerful variant of this flywheel is using evals for regression testing. Before merging any new feature that touches shared prompts, tool descriptions, or orchestration logic, you run the full eval suite to guard against breaking existing behavior. This is an extremely powerful technique for ensuring that new features do not break old ones. The strategy involves five steps:

1.  **Implement a new feature:** You write the code and verify it works locally for the new use case.
2.  **Run the AI evaluations:** You run the full suite of assessments, covering all previous use cases, not just the new one.
3.  **Compare Scores:** You compare the new scores against the baseline.
4.  **Metrics similar to baseline:** If the scores are identical to the baseline, you can merge the feature, confident that it has not affected existing functionality.
5.  **Metrics lower than the baseline:** If a score is worse, you have introduced a regression. You must fix your code and repeat the process.![Integrating AI evaluations into CI pipelines for regression testing.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down)
Image 2: Integrating AI evaluations into CI pipelines for regression testing.

This treats evals like integration tests, but because of the probabilistic nature of AI systems, we often compare scores against a moving baseline instead of enforcing a strict pass/fail threshold. This practice, drawn from modern software testing, extends beyond just checking the final output. For agents, a robust evaluation suite also measures the quality of the reasoning trace, the accuracy of tool selection, and the agent's ability to recover from errors [[6]](https://agility-at-scale.com/ai/architecture/evaluation-and-testing-frameworks).

Your dataset must also continuously evolve. It should expand with edge cases from new features, production failures captured via observability tools like Opik, and hard debugging examples that expose current failure modes [[7]](https://www.growthbook.io/blog/ai-evals-vs-a-b-testing-why-you-need-both-to-ship-genai). Instead of writing new tests in code, you broaden your test coverage by adding new samples to the dataset. For example, if you observe a regression in production where your agent fails to handle a specific user query, you can add that trace from Opik directly to your evaluation dataset. This ensures that the same regression will be caught automatically in the future [[8]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets), [[9]](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals).

This offline process is often extended with **continuous evaluation** in production. By monitoring the performance of the live agent against the same metrics, you can detect performance degradation or concept drift as real-world data distributions change over time. This closes the loop between offline testing and live performance, ensuring your agent remains reliable long after deployment [[10]](https://datagrid.com/blog/4-frameworks-test-non-deterministic-ai-agents).

With the flywheel mechanics clear, we can now examine the different families of metrics we might plug into it when dealing with unstructured outputs.

## Exploring Possible Metric Types

The core difficulty in evaluating AI systems is that we are often dealing with unstructured text, reasoning traces, or even images. Standard accuracy metrics from classical ML do not apply. Instead, we have three main families of metrics to choose from.

### BLEU and ROUGE

N-gram overlap metrics like Bilingual Evaluation Understudy (BLEU) and Recall-Oriented Understudy for Gisting Evaluation (ROUGE) are the oldest and simplest. They work by counting the number of overlapping words or sequences of words (n-grams) between the generated output and a reference text [[11]](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb). Their main advantages are that they are fast, deterministic, and require no additional models. However, they are also blind to semantic meaning. They cannot tell if "The test was successful" means the same thing as "The experiment succeeded," and they do not care about factual accuracy [[12]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ).

### BERTScore

Embedding similarity metrics like BERTScore represent a step up. They embed both the generated and reference texts into a high-dimensional vector space using a model like BERT. Then, they compute the cosine similarity between these embeddings to measure how close they are in meaning. This approach captures semantic equivalence far better than lexical overlap [[13]](https://www.elastic.co/search-labs/blog/evaluating-rag-metrics). However, they are still fundamentally comparison metrics and cannot verify complex business rules or logic.

### LLM Judges

The most flexible and powerful approach is the LLM-as-a-judge. This involves prompting a capable evaluator LLM with the input, the generated output, a set of detailed criteria, and few-shot examples. By providing chain-of-thought instructions, the judge can produce nuanced evaluations that incorporate domain-specific rules and multi-faceted requirements [[14]](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method). For example, a judge can check if a generated legal summary not only captures the key facts but also adheres to a specific citation format.

The main advantage of LLM judges is their ability to evaluate subjective aspects and provide detailed, human-like critiques. However, their performance depends on prompt and model quality. They are slower, more expensive, and can inherit the LLM's biases if not properly calibrated [[15]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge), [[16]](https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw). These weaknesses can be mitigated through careful **calibration**, where the judge's outputs are compared against a "gold standard" dataset scored by human experts. The insights from this comparison are then used to build few-shot examples and refine the judge's instructions, aligning it more closely with human criteria and correcting for known biases, such as a preference for more verbose answers [[17]](https://www.langchain.com/resources/llm-as-a-judge), [[18]](https://deepchecks.com/llm-judge-calibration-automated-issues).

Table 1: A comparison of trade-offs for different metric families.

| Metric Family | Speed | Cost | Semantic Awareness | Business Alignment | Explainability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Lexical Overlap (BLEU, ROUGE) | Very Fast | Very Low | None | Very Low | High |
| Embedding Similarity (BERTScore) | Fast | Low | Medium | Low | Medium |
| LLM-as-a-Judge | Slow | High | High | High | High (with CoT) |

For the kinds of complex, guideline-driven tasks in our capstone writing project, LLM judges are the most practical choice. They are the only method that can reliably check for adherence to research, structural guidelines, and brand voice.

Now, you kept hearing from us: *"business metrics here, business metrics there"*. Thus, let's understand why defining your own business metrics is such an essential and underrated step in building your AI evals strategy.

## Why Business Metrics Over Benchmarks

Public benchmarks are the most deceiving type of metric. Looking at popular leaderboards to choose a model for your product is often a mistake. There are two core reasons for this.

First, benchmarks often function as marketing artifacts. Once a test set becomes public, teams can intentionally or unintentionally overfit to it, "teaching to the test" to climb the leaderboard [[19]](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053). This is exacerbated by data contamination, where benchmark data leaks into the model's training set, invalidating the results [[20]](https://www.evidentlyai.com/llm-guide/llm-benchmarks). There have been instances where models achieved too-good-to-be-true scores because they were effectively fine-tuned on the test set, memorizing answers rather than learning to reason [[21]](https://openreview.net/forum?id=XbVMiW0jTM).

Second, there is a fundamental mismatch between typical benchmark tasks and real business workloads. A model that excels at solving grade-school math problems (like on GSM8K) may be useless for long-form creative writing, nuanced legal analysis, or personalized customer support [[22]](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches). The skills tested are often irrelevant to the skills your product requires.

This defines the proper, narrow role of benchmarks: they are useful for advancing research frontiers and for initial model filtering during early exploration. They should never be used as a proxy for product-level decisions or as the primary target for optimization.

If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous. We must instead build metrics that are deeply tied to our specific application.

## Why Custom Business Metrics Over Generic Metrics

Generic, off-the-shelf metrics for "toxicity," "helpfulness," or "hallucination" are a mirage. They create a false sense of confidence by optimizing for the wrong signal, because they lack context about your product, your users, and your brand voice. A model can score brilliantly on a generic "helpfulness" metric but fail catastrophically on your specific constraints [[23]](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP).

Consider the dashboard below. It looks impressive, with scores for "Truthfulness" and "Personalization." But what does a 3.7 in "Personalization" actually mean? These vague scores are not actionable.![A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down)
Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!" (Source [https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals))

For our Brown writing agent, a generic `hallucination` score is useless. If it returns "positive," what does that tell us? Did the model invent a fact not present in the research? Did it deviate from the article guideline? Or did it simply add a personal story that, while not in the source text, is factually correct and aligns with the desired tone? A generic detector cannot distinguish between undesirable invention and desirable creative elaboration. It might flag an engaging personal anecdote as a fabrication, even though that anecdote is exactly what your brand voice requires.

Prefab scores are limited by their inability to incorporate domain-specific constraints, their failure to localize which part of an output failed, and the statistical noise they introduce into decision-making [[24]](https://arxiv.org/html/2508.13816v1).

This carves out a narrow, valid role for generic metrics: strictly during exploratory data analysis. You can use them as a "flashlight, not a report card," to surface interesting examples for manual review [[25]](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics).

1.  **Verbosity:** Sort your outputs by length. This can reveal if your most verbose answers are rambling and unhelpful or if your shortest answers are curt and missing information.
2.  **Similarity Score:** Use this to evaluate your RAG retriever specifically. If the similarity between a user query and the retrieved chunks is low, your retriever is likely failing.
3.  **BERTScore:** Use this to challenge your golden reference answers. If you find a cluster of outputs with a low BERTScore against a reference you expected to be similar, it might be because the LLM found a more creative or even better solution.

In all these cases, the generic metric is the start of an investigation, not the final verdict. Every production metric must be deeply application-centric, derived from concrete product requirements, user success criteria, and explicit constraints.

Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments from our LLM judge. Here, binary pass/fail criteria outperform every alternative.

## Choosing Binary Metrics Over Anything Else

When designing these custom metrics, you will face a choice: should you use a Likert scale (e.g., 1-5 stars) or a binary pass/fail? We strongly recommend **binary metrics**.

Likert scales are a seductive trap. They seem to offer more nuance, but in practice, they introduce ambiguity and noise. Their problems are threefold:

1.  **Inconsistent Labeling:** The difference between a '3' and a '4' is subjective. One person's '4' is another's '3', leading to low inter-annotator agreement and endless debates over the rubric [[26]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).
2.  **Statistical Noise:** Small movements in an average score are often statistically indistinguishable from random noise. To confidently detect a real improvement from an average of 3.2 to 3.5 might require around 350 test cases, whereas confirming a pass rate shift from 60% to 70% needs only about 150. Binary metrics give you a clearer signal with less data [[27]](https://www.ellamind.com/blog/binary-vs-likert-scales).
3.  **Lazy Decision-Making:** Both human and LLM evaluators tend to gravitate toward the middle of the scale, creating a "mushy middle" where '3's pile up. This value becomes a place to hide uncertainty rather than make a difficult decision. This satisficing behavior drowns the signal in your data, leaving you with a dashboard full of '3's that tells you nothing [[26]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals), [[28]](https://www.scribbr.com/methodology/likert-scale).

Binary evaluations work because they **force decisions**. They solve these problems by demanding clarity.

1.  **Clearer Thinking:** An output either met the criterion or it did not. You cannot hide in ambiguity. This forces you to create precise, unambiguous definitions of quality.
2.  **Consistency:** Binary decisions are faster and more consistent for both humans and LLMs, leading to higher agreement and more reliable data.
3.  **Actionability:** The result is not a fuzzy number but a clear signal tied to a specific failure mode. A spike in the "Constraint Violation" failure rate tells an engineer exactly where to start debugging.

<aside>
💡
**Note:** These points translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate the inherent randomness of LLMs. An LLM is much more stable when asked to make a binary choice ("Is this statement supported by the context? Yes or No.") than when asked to assign a scalar value ("Rate the faithfulness of this statement from 1 to 5."). A binary metric translates to a more robust and repeatable evaluation pipeline.
</aside>

### Capturing Nuance

The standard objection is, "But I'm losing nuance! A 1-5 scale captures shades of gray." This is a valid concern, but a Likert scale is the wrong solution. The right way to capture nuance is not by making your scale fuzzier, but by making your criteria more **granular** [[27]](https://www.ellamind.com/blog/binary-vs-likert-scales).

Instead of a single, subjective rating for "Quality," you decompose it into multiple, specific, binary checks. This approach gives you *more* nuance than a single Likert rating, not less, because you can pinpoint exactly which dimension of quality is failing. For our writing agent, instead of rating an article 1-5, we create separate binary evaluations:

1.  **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
2.  **Flow of Ideas Adherence:** Does the generated article present ideas in the same order as the expected article? (Yes/No)
3.  **Article Guideline Adherence:** Does the generated article follow the flow of ideas from the article guideline input? (Yes/No)
4.  **Research Anchoring:** Is every claim in the article supported by the provided research? (Yes/No)

By aggregating these binary signals—perhaps as a simple average or a weighted sum—you get a nuanced, multi-dimensional view of performance. You can now say, "We are passing Content Adherence 95% of the time, but failing Research Anchoring 30% of the time." This is a signal you can act on. You have captured nuance without sacrificing clarity, all while eliminating the noise and bias of subjective scales.

With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in the next lesson.

## Conclusion

This lesson has laid out the core theoretical shift required for modern AI engineering: moving from vibe checks, leaderboards, and generic scores to a rigorous, evaluation-driven development process. This process is built on a foundation of custom, binary, business-aligned metrics that provide a clear and actionable signal for improvement.

We have argued that granular pass/fail criteria deliver the most reliable optimization signal, avoiding the statistical noise and subjectivity inherent in scalar ratings. This disciplined approach is the only way to build confidence in complex, probabilistic systems. In our next lesson, we will translate this theory into practice by implementing custom LLM judges from scratch to evaluate our Brown writing workflow.

## References

- [1] Krawczyk, S., & Bowne-Anderson, H. (2025, October 16). Escaping POC Purgatory: Evaluation-Driven Development for AI Systems. Decoding AI. https://www.decodingai.com/p/escaping-poc-purgatory-evaluation
- [2] Agentic AI: A new paradigm for enterprise automation. (n.d.). Datarobot. https://www.datarobot.com/blog/agentic-ai-enterprise-design
- [3] Pan, A., et al. (2025). A Survey of Agent-Based AI for Programming. arXiv. https://arxiv.org/html/2505.10468v1
- [4] Statistical Significance. (n.d.). Corporate Finance Institute. https://corporatefinanceinstitute.com/resources/data-science/statistical-significance
- [5] Lahey, M. (2022, October 23). Practical vs. Statistical Significance. Nielsen Norman Group. https://www.nngroup.com/articles/practical-significance
- [6] Evaluation and Testing Frameworks for AI Systems. (n.d.). Agility at Scale. https://agility-at-scale.com/ai/architecture/evaluation-and-testing-frameworks
- [7] AI Evals vs. A/B Testing: Why You Need Both to Ship GenAI. (n.d.). GrowthBook. https://www.growthbook.io/blog/ai-evals-vs-a-b-testing-why-you-need-both-to-ship-genai
- [8] Manage Datasets. (n.d.). Opik Documentation. https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets
- [9] Iusztin, P. (2025, November 25). Generate Synthetic Datasets for AI Evals. Decoding AI. https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals
- [10] 4 Frameworks to Test Non-Deterministic AI Agents. (n.d.). DataGrid. https://datagrid.com/blog/4-frameworks-test-non-deterministic-ai-agents
- [11] Sthanikam, S. (2023, April 27). Understanding BLEU and ROUGE score for NLP evaluation. Medium. https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb
- [12] LLM evaluation benchmarking: Beyond BLEU and ROUGE. (n.d.). Weights & Biases. https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ
- [13] Evaluating RAG using RAGAs and other metrics with Elasticsearch. (n.d.). Elastic. https://www.elastic.co/search-labs/blog/evaluating-rag-metrics
- [14] What is LLM-as-a-Judge and Why is it The Best LLM Evaluation Method? (n.d.). Confident AI. https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method
- [15] LLM-as-a-judge: using LLMs for evaluation. (n.d.). Evidently AI. https://www.evidentlyai.com/llm-guide/llm-as-a-judge
- [16] Abdella, A. (2026, May 22). LLM as a Judge is scalable, cost-effective, good at understanding open-ended AI-generated content. LinkedIn. https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw
- [17] LLM As A Judge. (n.d.). LangChain. https://www.langchain.com/resources/llm-as-a-judge
- [18] Calibrating your LLM Judge: A Guide to Automated Issue Detection. (n.d.). Deepchecks. https://deepchecks.com/llm-judge-calibration-automated-issues
- [19] Hari, B. (2026, April 26). AI — Benchmark scores are becoming marketing; dynamic eval is the only antidote. https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053
- [20] 30 LLM evaluation benchmarks and how they work. (2026, May 19). Evidently AI. https://www.evidentlyai.com/llm-guide/llm-benchmarks
- [21] Flood, R., Engelen, G., Aspinall, D., & Desmet, L. (2024). Bad design smells in benchmark nids datasets. In _2024 IEEE 9th European Symposium on Security and Privacy (EuroS&P)_ (pp. 658–675). IEEE. https://openreview.net/forum?id=XbVMiW0jTM
- [22] Raschka, S. (2024, February 1). 4 Ways to Evaluate LLMs in Production. Ahead of AI. https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches
- [23] Aggarwal, S. (2026, October 15). AI evaluation is broken when we hide behind generic metrics. LinkedIn. https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP
- [24] Meta-evaluation of text-generation metrics. (2025). arXiv. https://arxiv.org/html/2508.13816v1
- [25] Husain, H. (2025, November 13). The Mirage of Generic AI Metrics. Decoding AI. https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics
- [26] Husain, H. (2025, December 4). The 5-Star Lie: You’re Doing AI Evaluations Wrong. Decoding AI. https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals
- [27] Binary vs. Likert Scales: Which is Better for AI Evals? (n.d.). Ellamind. https://www.ellamind.com/blog/binary-vs-likert-scales
- [28] Streefkerk, R. (2022, June 22). Likert Scale | Definition, Examples & Analysis. Scribbr. https://www.scribbr.com/methodology/likert-scale