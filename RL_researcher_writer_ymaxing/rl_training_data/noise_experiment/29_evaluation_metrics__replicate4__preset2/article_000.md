# Lesson 29: Designing AI Evals

In our previous lessons, we instrumented our agents with Opik for observability and built our first offline evaluation dataset from production traces. We now have the raw materials for a robust evaluation pipeline. But before we can build it, we must answer a fundamental question: what exactly are we measuring?

In classical machine learning, this question has a clear answer. We rely on rigorous, quantitative metrics like accuracy, precision, recall, and F1-score to measure performance against a labeled dataset. We debate the merits of p-values and statistical significance. In the world of AI engineering, however, many teams have fallen back on a far less rigorous standard: the "vibe check." We run a new prompt, look at the output, and decide, "this feels more coherent." Sometimes, evaluation is skipped altogether.

Investing in a proper evaluation layer can feel like a secondary priority. It delivers no immediate user-visible feature. It requires upfront effort to design datasets and metrics, all while the pressure to ship new functionality mounts. However, this initial investment dramatically accelerates long-term development. It provides an objective signal on every change, catches regressions instantly, and turns a process driven by intuition into one driven by evidence.

This shift is analogous to the move from manual testing to Test-Driven Development (TDD) in classical software engineering. Evaluation-Driven Development (EDD) asks a different question: not just "Does it work?" but "How well does it work, and is it getting better?" It reframes evaluation from a final quality gate to the central engine of development [[1]](https://medium.com/@nimrodbusany_9074/from-tdd-to-edd-why-evaluation-driven-development-is-the-future-of-ai-engineering-a5e5796b2af4).

Evals are the north star of AI engineering. They are the single source of truth that tells you which modifications improve your system and which degrade it. In this lesson, we will establish the theoretical foundation for building an evaluation framework that works. We will cover:

-   The optimization flywheel and its three core use cases.
-   Metric-type trade-offs for unstructured outputs.
-   Why custom business metrics beat benchmarks and generic scores.
-   Why binary pass/fail judgments are superior to Likert scales.

With the problem and its importance clear, we will now examine how to operationalize evaluations inside a repeatable optimization flywheel that replaces intuition with evidence.

## Using Evals Through the Optimization Flywheel

To build intuition, let's examine how we can effectively use and integrate AI evaluations into our application development lifecycle. There are three core scenarios where evaluations provide value. First, evals **quantify the quality of your system** on a given set of metrics, creating a baseline snapshot of its current performance. Without a baseline, you cannot know if the system is ready for production or if your changes are making it better.

Second, these metrics serve as **guidance when optimizing your system**. They provide objective evidence for experiments, shifting development from being intuition-based to evidence-based. Finally, evals act as **regression tests** that protect shared components. Unlike optimization, the goal here is stability. This is critical in AI engineering, where components like prompts, tools, and memory are often interconnected and shared across different parts of an application.

### The Optimization Process

How does this look in a real-world scenario? Let's look at a step-by-step plan for the optimization flywheel.

1.  **Gather your dataset:** Assemble an offline dataset of inputs and expected outputs, as we did in Lesson 28.
2.  **Build your metrics:** Define a set of business-aligned metrics to measure performance.
3.  **Establish a baseline:** Run the evaluations on the current system to compute your baseline scores.
4.  **Start the optimization:** Make one isolated change that you believe will improve performance.
5.  **Compute the new score:** Re-evaluate the entire dataset by re-running the evals.
6.  **Compare:** Compare the new scores to the baseline, considering statistical significance.
7.  **Decide:** Based on whether the score is better, the same, or worse, decide to keep the change, revert it, or continue experimenting.
8.  **Repeat:** Repeat this cycle until the scores meet your target for production readiness.![The iterative optimization flywheel for AI applications using evaluations.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-4d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down)
Image 1: The iterative optimization flywheel for AI applications using evaluations.

It is critical to keep all components fixed except for one variable per cycle. Confounding multiple modifications makes it impossible to attribute score movements to a specific change, turning the process back into guesswork. This principle of isolating a single variable is a cornerstone of classical control theory, which designs feedback loops for single-input, single-output systems to ensure stability and optimize performance [[2]](https://en.wikipedia.org/wiki/Control_theory).

Your decision to accept a change should anchor statistical significance to actual **business impact**, not just arbitrary p-value thresholds. A "better" score is always relative to the business use case. For example, for a high-volume customer support bot, a tiny improvement of 0.5% in resolution rate could translate to thousands of fewer support tickets and significant cost savings. In this context, even a small, statistically significant improvement has massive business value. In contrast, for a low-volume creative writing tool, a 0.5% increase in a "creativity" score is likely negligible and not worth the engineering effort to implement [[3]](https://www.nngroup.com/articles/practical-significance).

### Regression Testing

A powerful variation of this flywheel is using it for regression testing. Before merging any new feature that touches shared prompts, tool descriptions, or orchestration logic, you run the full evaluation suite to guard against breaking existing behavior. This ensures that new features do not silently degrade the performance of old ones.

The process is a simplified version of the optimization flywheel:

1.  **Implement a new feature:** You write the code and verify it works locally for the new use case.
2.  **Run the AI evaluations:** You run the full suite of assessments, covering all previous use cases.
3.  **Compare Scores:** You compare the new scores against the baseline for all existing use cases.
4.  **Metrics similar to baseline:** If the scores for existing features are identical to the baseline, your new feature has not introduced any regressions. You can merge it.
5.  **Metrics lower than the baseline:** If any score is worse, you have introduced a regression. You should fix your code and repeat the process.![Integrating AI evaluations into CI pipelines for regression testing.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down)
Image 2: Integrating AI evaluations into CI pipelines for regression testing.

This treats evaluations like integration tests, but instead of enforcing a strict pass/fail threshold, we compare scores against a moving baseline. The dataset for these evaluations must continuously expand. New edge cases discovered for features, production failures captured via observability tools like Opik, and difficult debugging examples should all be added to the dataset [[4]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets). For instance, if a user interaction from production reveals a regression, that trace can be converted into a new dataset item to ensure the same failure is caught automatically in the future [[5]](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals). Instead of writing new tests in code, you broaden your test coverage by adding new samples to the dataset.

This practice is becoming increasingly formalized as agent frameworks evolve to include built-in continuous evaluation. The goal is to create a system that can monitor for performance degradation or "agent decay" in near real-time, ensuring that agents maintain their quality as underlying models, tools, or data change [[6]](https://learn.microsoft.com/en-us/agents/architecture/evaluation-frameworks), [[7]](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon).

With the flywheel mechanics clear, we can now examine the different families of metrics we might plug into it when dealing with unstructured outputs.

## Exploring Possible Metric Types

The core difficulty in evaluating AI systems is that we are often dealing with unstructured text, reasoning traces, or even image outputs. Unlike classical ML with its structured labels, standard accuracy metrics are often unavailable. There are three core families of metrics to consider.

### 1. BLEU and ROUGE

N-gram overlap metrics like BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Oriented Understudy for Gisting Evaluation) are statistical methods that work by counting overlapping words and phrases between the generated text and a reference text. Their primary advantages are that they are fast, deterministic, widely understood, and require no additional models to run [[8]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ), [[9]](https://www.traceloop.com/blog/demystifying-the-bleu-metric). However, they are blind to semantic meaning. They cannot recognize paraphrasing, penalizing perfectly correct answers that use different wording, and they do not care about factual accuracy [[8]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ), [[10]](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb).

### 2. BERTScore

Embedding similarity metrics, such as BERTScore, address the semantic blindness of n-gram methods. They work by embedding both the generated and reference texts into a high-dimensional vector space using a model like BERT. By calculating the cosine similarity between these embeddings, they can measure semantic closeness [[8]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ). This allows them to recognize paraphrases and capture meaning far better than purely lexical methods. However, they are still fundamentally comparison metrics and cannot verify complex business logic or rules on their own.

### 3. LLM Judges

The LLM-as-a-judge approach uses a capable LLM to evaluate an output. You provide the judge model with the input, the generated output, a set of detailed criteria, few-shot examples, and chain-of-thought instructions. This method is highly flexible and can be customized to evaluate against complex, domain-specific requirements, such as adherence to brand voice or legal constraints [[11]](https://www.braintrust.dev/articles/what-is-llm-as-a-judge). LLM judges can also provide detailed, human-like critiques explaining their reasoning [[12]](https://medium.com/data-science-collective/llm-as-a-judge-when-to-use-reasoning-cot-and-explanations-964ad82ebc3d). The main downsides are that their performance depends heavily on the prompt and the evaluator model, they can be slower and more expensive, and they can inherit the LLM’s biases if not properly developed and tested [[13]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge), [[14]](https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw).

To be reliable in production, LLM judges require a rigorous calibration process. This involves an iterative loop of labeling a representative dataset, running the judge, reviewing disagreements, and updating the evaluation criteria until the judge's agreement with human labels is high [[15]](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production). The goal is to validate that the judge's score tracks the real-world outcomes you care about, not just surface-level patterns [[16]](https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork). Furthermore, because binary judgments can be validated with standard classification metrics, they often provide a more stable foundation for this process than scalar scores [[17]](https://cameronrwolfe.substack.com/p/finetuned-judge).

| Metric Family | Speed | Cost | Semantic Awareness | Business Alignment | Explainability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BLEU/ROUGE** | High | Low | Low | Low | Low |
| **BERTScore** | Medium | Medium | High | Medium | Low |
| **LLM Judges** | Low | High | High | High | High |

Table 1: A trade-off summary of different evaluation metric families.

For the kinds of guideline adherence and research grounding needed for our capstone writing projects, LLM judges are the most practical choice.

Now, you kept hearing from us: *"business metrics here, business metrics there"*. Thus, let's understand why defining your own business metrics is such an essential and underrated step in building your AI evals strategy.

## Why Business Metrics Over Benchmarks

It is important to state that benchmarks are often the most deceiving type of metric. Looking at popular leaderboards or public benchmarks to choose an LLM for your product is often a mistake. There are two core reasons for this.

First, benchmarks often function as marketing artifacts. Once a test set becomes public, it is susceptible to data contamination, where parts of the test set inadvertently leak into training data, invalidating the results [[18]](https://medium.com/@yujiisobe/navigating-the-maze-of-llm-evaluation-a-guide-to-benchmarks-rag-and-agent-assessment-fb7aef299e66). Even without direct leaks, teams can overfit to the benchmark, chasing leaderboard scores that no longer reflect performance on unseen data [[19]](https://www.evidentlyai.com/llm-guide/llm-benchmarks), [[20]](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053). This "teaching to the test" is a well-documented problem from ML history, where even iterative prompt engineering on a benchmark can act as a form of implicit training on the evaluation data [[21]](https://openreview.net/forum?id=maMnVCHl8J).

Second, there is a fundamental mismatch between typical benchmark tasks, like solving math problems (GSM8k) or answering general knowledge questions (MMLU), and the reality of real business workloads [[22]](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches). A model that excels at standardized tests may fail completely at tasks requiring long-form creative writing, nuanced legal analysis, or personalized customer support, as these require domain-specific knowledge and adherence to complex guidelines that benchmarks do not measure [[23]](https://arxiv.org/html/2601.20617v1).

The proper role for benchmarks is narrow: they are useful for advancing research, and for initial model filtering during early exploration. They should never be used as a proxy for product-level decisions or as a primary optimization target.

If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous; we must instead build metrics that are deeply tied to our specific application.

## Why Custom Business Metrics Over Generic Metrics

Generic, off-the-shelf metrics for qualities like "toxicity," "helpfulness," or "hallucination" can act as a mirage. They create a false sense of confidence by optimizing for the wrong signal, because they lack context about your product, user expectations, and brand voice. A model can score brilliantly on a generic "helpfulness" metric but fail catastrophically on your specific constraints [[24]](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP).

Consider the dashboard below. It looks impressive, with scores for "Truthfulness" and "Personalization." But what does a 3.7 in "Personalization" actually mean? Without a clear, actionable definition tied to the product, such numbers are vanity metrics [[24]](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP).![A dashboard showing generic metrics like Helpfulness and Truthfulness.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down)
Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"

For example, let's assume we want to check if an article written by our Brown agent contains hallucinations. A generic `hallucination` score might return "positive," but what does that tell us? Did the model add information not present in the research? Did it deviate from the article guidelines? Or did it simply include a personal story that wasn't in the source text but is factually correct and relevant to the topic? A generic detector might flag an engaging personal anecdote as a fabrication, yet that same anecdote may be exactly what your brand voice requires. The generic metric cannot distinguish between undesirable invention and desirable creative elaboration.

Prefabricated scores suffer from several limitations. They lack domain-specific constraints, cannot localize which part of an output failed, and introduce additional statistical noise into your decision-making process.

However, generic metrics can be useful when treated as a flashlight for exploratory data analysis, rather than a report card for quality. Here are some examples:

1.  **Verbosity:** Sorting your outputs by length can reveal if your most verbose answers are rambling and unhelpful, or if your shortest answers are too curt. This helps you spot failure modes in long-form generation.
2.  **Similarity Score:** In a RAG system, you can use a similarity score to evaluate the retriever component specifically. If the similarity between a user's query and the retrieved document chunks is low, your retriever is likely failing. This is a valid component-level check.
3.  **BERTScore:** You can use this to check the quality of your "golden" reference answers. If a cluster of outputs receives a low BERTScore against a reference you expected to be similar, it might be that the LLM found a more creative or even better solution than your reference.

Every production metric must be deeply application-centric, derived from concrete product requirements, user success criteria, and explicit constraints.

Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments from our LLM judge. Here, binary pass/fail criteria outperform every alternative.

## Choosing Binary Metrics Over Anything Else

When designing these custom metrics, you will face a choice: should you use a Likert scale (e.g., 1-5 stars) or a binary pass/fail? We strongly recommend **binary metrics**.

Likert scales introduce several problems:

1.  **Inconsistent Labeling:** There is high subjectivity in deciding whether an output is a "3" or a "4." One person's "good" is another's "okay," leading to low inter-annotator agreement [[25]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).
2.  **Statistical Noise:** Small movements in an average score, like from 3.2 to 3.5, are often statistically indistinguishable from random variance, especially with small sample sizes. This makes it hard to know if a change truly improved the system [[26]](https://www.ellamind.com/blog/binary-vs-likert-scales).
3.  **Lazy Decision-Making:** Evaluators, both human and LLM, often default to middle values like "3" to avoid making a difficult judgment. This "satisficing" behavior flattens the signal and hides real failure modes [[25]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).

Binary evaluations work because they **force decisions**. They offer several advantages:

1.  **Clearer Thinking:** They force you to create precise, unambiguous definitions of quality. An output either meets the criterion or it does not.
2.  **Consistency:** They yield higher agreement among both human annotators and LLM judges.
3.  **Actionability:** They deliver a clear failure signal tied to a specific problem, rather than a vague score change.

<aside>
💡

**Note:** The 3 points above translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate the inherent randomness of LLMs. LLMs are much more stable when asked to make a binary decision than when asked to assign a scalar value. A binary metric translates to a more robust and repeatable evaluation pipeline.

</aside>

### Capturing Nuance

The standard objection to binary metrics is, "But I'm losing nuance! A 1-5 scale captures shades of gray."

The way to capture nuance is not by making your scale fuzzier, but by making your criteria more **granular**. Instead of a single, subjective rating for a complex quality, you should break it down into multiple, specific, binary checks [[26]](https://www.ellamind.com/blog/binary-vs-likert-scales).

However, it is important to acknowledge the limitations. For highly creative or open-ended tasks like long-form writing, even a suite of granular binary metrics can sometimes fail to capture fundamental issues like a lack of narrative coherence or fluency. An agent might pass all individual checks but produce an output that is stylistically flawed or incomplete, a failure mode that binary checks can miss [[27]](https://www.linkedin.com/posts/pauliusztin_i-created-an-ai-agent-to-write-a-substack-activity-7420095430807691266-fQ1U), [[28]](https://www.mdpi.com/2076-3417/15/6/2971).

For our writing agent, instead of rating an article 1-5 for "Quality," we can create multiple binary evaluations that capture specific dimensions of quality:

1.  **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
2.  **Flow of Ideas Adherence:** Does the generated article present ideas in the same order as the expected article? (Yes/No)
3.  **Article Guideline Adherence:** Does the generated article follow the flow of ideas from the article guideline input? (Yes/No)
4.  **Research Anchoring:** Is every claim in the article supported by the provided research? (Yes/No)

By aggregating these binary signals, you can achieve a nuanced view of performance. For example, you can calculate a simple average or a weighted sum to get an overall quality score. This approach gives you a detailed, actionable breakdown of what is working and what is not, all while eliminating the noise and bias of scalar ratings.

With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in the next lesson.

## Conclusion

The path to building robust AI products requires a fundamental shift in mindset: away from vibe checks, leaderboards, and generic scores, and toward a rigorous, evaluation-driven development process. This process is built on a foundation of custom, binary, business-aligned metrics that provide a clear and actionable signal for improvement.

Granular pass/fail criteria deliver the clearest optimization signal while avoiding the statistical noise and subjectivity inherent in scalar scales. By breaking down complex qualities into specific, verifiable checks, you gain a nuanced understanding of your system's performance without sacrificing clarity. In our next lesson, we will translate this theory into practice by implementing custom LLM judges from scratch to evaluate our Brown writing workflow.

## References

- [1] From TDD to EDD: Why Evaluation-Driven Development is the Future of AI Engineering. (https://medium.com/@nimrodbusany_9074/from-tdd-to-edd-why-evaluation-driven-development-is-the-future-of-ai-engineering-a5e5796b2af4)
- [2] Control theory. (https://en.wikipedia.org/wiki/Control_theory)
- [3] Statistical Significance Isn’t the Same as Practical Significance. (https://www.nngroup.com/articles/practical-significance)
- [4] Manage Datasets | Opik Documentation. (https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets)
- [5] Generate Synthetic Datasets for AI Evals. (https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals)
- [6] Evaluation frameworks for agents. (https://learn.microsoft.com/en-us/agents/architecture/evaluation-frameworks)
- [7] Evaluating AI agents: Real-world lessons from building agentic systems at Amazon. (https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon)
- [8] LLM evaluation benchmarking: Beyond BLEU and ROUGE. (https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ)
- [9] Demystifying the BLEU Metric. (https://www.traceloop.com/blog/demystifying-the-bleu-metric)
- [10] Understanding BLEU and ROUGE Score for NLP Evaluation. (https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb)
- [11] What is LLM-as-a-Judge?. (https://www.braintrust.dev/articles/what-is-llm-as-a-judge)
- [12] LLM-as-a-Judge: When to Use Reasoning, CoT, and Explanations. (https://medium.com/data-science-collective/llm-as-a-judge-when-to-use-reasoning-cot-and-explanations-964ad82ebc3d)
- [13] LLM-as-a-judge: a complete guide to using LLMs for evaluations. (https://www.evidentlyai.com/llm-guide/llm-as-a-judge)
- [14] Pros and Cons of LLM as a Judge. (https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw)
- [15] How to Build LLM-as-a-Judge Evaluators That Hold Up in Production. (https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production)
- [16] Better Experiments with LLM Evals: A Funnel, Not a Fork. (https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork)
- [17] Finetuned Judge. (https://cameronrwolfe.substack.com/p/finetuned-judge)
- [18] Navigating the Maze of LLM Evaluation: A Guide to Benchmarks, RAG, and Agent Assessment. (https://medium.com/@yujiisobe/navigating-the-maze-of-llm-evaluation-a-guide-to-benchmarks-rag-and-agent-assessment-fb7aef299e66)
- [19] LLM Benchmarks. (https://www.evidentlyai.com/llm-guide/llm-benchmarks)
- [20] AI Benchmark scores are becoming marketing; dynamic eval is the only antidote. (https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053)
- [21] On the Impossible Problem of Evaluating Language Models. (https://openreview.net/forum?id=maMnVCHl8J)
- [22] LLM Evaluation: 4 Approaches. (https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches)
- [23] Benchmarks for LLM Agents in the Public Sector. (https://arxiv.org/html/2601.20617v1)
- [24] The Mirage of Generic AI Metrics. (https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP)
- [25] The 5-Star Lie: You’re Doing AI Evaluations Wrong. (https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals)
- [26] Why We Use Binary Yes/No Evaluations (And You Should Too). (https://www.ellamind.com/blog/binary-vs-likert-scales)
- [27] I created an AI Agent to write a Substack article from scratch. (https://www.linkedin.com/posts/pauliusztin_i-created-an-ai-agent-to-write-a-substack-activity-7420095430807691266-fQ1U)
- [28] A Comprehensive Evaluation of Large Language Models in the Legal Domain. (https://www.mdpi.com/2076-3417/15/6/2971)