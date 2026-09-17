# Beyond Vibe Checks: The Engineering Guide to AI Evals

In our previous lessons, we instrumented our agents with Opik for observability and constructed an offline dataset from production traces. We now have the raw materials for evaluation. The next step is to move from simply collecting data to designing the metrics that will guide our development. In classical Machine Learning, we have rigorous standards like accuracy, precision, recall, and F1-scores. In AI engineering, however, it is common to rely on "vibe checks." These are subjective assessments like “this output feels more coherent.” Others skip evaluation entirely [[40]](https://olshansky.substack.com/p/vibe-checks-are-all-you-need).

Prioritizing a robust evaluation layer can feel difficult. It delivers no immediate, user-visible features and requires an upfront investment in designing datasets and metrics, all while the pressure to ship new functionality mounts. However, this investment significantly speeds up long-term iteration. It provides an objective signal on every change, catches regressions instantly, and replaces intuition with evidence. This approach parallels the shift from manual testing to Test-Driven Development (TDD) in traditional software, but with a key difference. TDD asks, "Does it work?" with a binary answer. Evaluation-Driven Development (EDD) asks, "How well does it work?" answered on a spectrum [[54]](https://medium.com/@nimrodbusany_9074/from-tdd-to-edd-why-evaluation-driven-development-is-the-future-of-ai-engineering-a5e5796b2af4). Evals are the north star of AI engineering: the single source of truth that tells you which modifications improve the system and which degrade it.

This lesson will establish the theoretical foundation for building that source of truth. We will cover:

*   The optimization flywheel and its three core use cases.
*   Trade-offs between metric types for unstructured outputs.
*   Why custom business metrics beat benchmarks and generic scores.
*   Why binary pass/fail judgments are superior to Likert scales.

With the problem and its importance clear, we will now examine how to operationalize evals inside a repeatable optimization flywheel.

## Using Evals Through the Optimization Flywheel

To build intuition, let's examine how we can effectively use and integrate AI evaluations into our application development lifecycle. Evals are not just for a final grade; they are an active part of the engineering process. There are three core scenarios where evaluations provide value.

First, evals **quantify the quality of your system**. They take a snapshot of your system's current performance against a set of business-aligned metrics, establishing a baseline. This baseline is your anchor point. Without it, you cannot know if your system is production-ready or whether your changes are leading to genuine improvements. It is the objective starting line from which all progress is measured. This initial quantification turns a subjective "vibe" into a concrete number, which is the first step toward engineering rigor [[42]](https://www.growthbook.io/blog/ai-evals-vs-a-b-testing-why-you-need-both-to-ship-genai).

Second, these metrics serve as **guidance when optimizing your system**. They provide objective evidence for experiments, transforming development from an intuition-based art to an evidence-based science. Instead of guessing if a new prompt is "better," you can measure its impact directly across hundreds of test cases. This data-driven approach allows you to focus your efforts on changes that demonstrably move the needle on the metrics that matter. This is the core of Evaluation-Driven Development, where the evaluation harness becomes the engine for iteration, not an afterthought [[65]](https://www.decodingai.com/p/escaping-poc-purgatory-evaluation).

Third, evals act as **regression tests that protect shared components**. This is critical in AI engineering, where components like prompts, tool definitions, and retrieval logic are often interconnected. A small change in one area can have unintended and negative consequences elsewhere. The non-deterministic nature of LLMs makes these side effects hard to predict. Unlike optimization, the goal here is stability, ensuring that new features do not silently break existing functionality [[44]](https://towardsdatascience.com/stop-evaluating-llms-with-vibe-checks).

### The Optimization Process

How does this look in a real-world scenario? The optimization flywheel is a systematic, repeatable process for improving your AI application.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down
Image 1: The iterative optimization flywheel for AI applications using evaluations.

This flywheel follows a clear, eight-step plan of attack:

1.  **Gather your dataset:** Assemble the offline dataset of inputs and expected outputs that represents your target use cases. This "golden dataset" is the foundation of your entire testing strategy and must include not just happy paths but also edge cases and adversarial prompts [[44]](https://towardsdatascience.com/stop-evaluating-llms-with-vibe-checks).
2.  **Build your metrics:** Define the business-aligned metrics that measure what success looks like for your application. As we will see later, these should be custom, granular, and often binary.
3.  **Establish a baseline:** Run your evaluation suite on the current system to compute baseline scores for each metric. This gives you a quantitative snapshot of your system's current state.
4.  **Start the optimization:** Make one, and only one, isolated change that you believe will improve performance, such as modifying a prompt, swapping a model, or adjusting a retrieval parameter.
5.  **Compute the new score:** Re-evaluate the entire dataset by re-running the evals on the modified system. This ensures you are comparing apples to apples.
6.  **Compare:** Compare the new scores to the baseline, assessing for statistical significance where appropriate. This step quantifies the impact of your change.
7.  **Decide:** If the score is better, keep the change. If it is the same, you must weigh the performance against any added complexity or cost. If the score is worse, you revert the change.
8.  **Repeat:** Continue the cycle, making one change at a time, until the scores meet your quality bar. This iterative process drives continuous improvement.

It is critical to keep all components fixed except for one variable per cycle. If you change the prompt and the retrieval chunking strategy at the same time, it becomes impossible to attribute any score movement to a specific cause. This principle echoes classical control theory, which focuses on systems with a single input and single output (SISO) to ensure stability and predictable optimization through a feedback loop [[55]](https://en.wikipedia.org/wiki/Control_theory). Confounding multiple changes turns a disciplined process back into guesswork.

Furthermore, statistical significance must be anchored to actual **business impact**, not arbitrary p-value thresholds. A "better" score is always relative to the specific business context. For example, a change that reduces checkout errors by just 0.5% might sound small. But if your product processes 2 million checkouts per year, that’s 10,000 fewer failed transactions. If each failed checkout costs the business $15 in lost revenue or support time, that small improvement translates to $150,000 per year. In this high-volume scenario, the small movement matters [[46]](https://www.nngroup.com/articles/practical-significance).

In contrast, for a low-volume creative writing tool used by a handful of authors, a similar percentage change in a "creativity" score might be statistically significant but practically meaningless to the user experience. The improvement would need to be much larger before it justifies the engineering effort. The key is to connect the metric to a tangible outcome, whether it is saving money, reducing errors, or improving a key performance indicator like conversion or retention [[45]](https://corporatefinanceinstitute.com/resources/data-science/statistical-significance), [[47]](https://www.statsig.com/perspectives/understanding-statistical-significance).

### Regression Testing

The optimization flywheel can be adapted to serve as a powerful regression testing framework. Before merging any new feature that touches shared components like prompts, tool descriptions, orchestration logic, or memory retrieval, you run the full eval suite to guard against breaking existing behavior. This is an extremely effective technique for ensuring stability.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down
Image 2: Integrating AI evaluations into CI pipelines for regression testing.

The process simplifies to five steps:

1.  **Implement a new feature:** You write the code and verify it works locally for the new use case.
2.  **Run the AI evaluations:** You run the full suite of assessments, covering all existing use cases, not just the new one.
3.  **Compare Scores:** You compare the new scores against the baseline.
4.  **Metrics similar to baseline:** If scores are identical or within an acceptable tolerance, the feature has not introduced a regression and can be merged.
5.  **Metrics lower than the baseline:** If scores are worse, you have introduced a regression. You must fix your code and repeat the process.

This treats evals like integration tests, but instead of enforcing a strict pass/fail threshold, you compare scores against a moving baseline. This is necessary because the system's behavior is probabilistic. This practice is becoming foundational to the AI ecosystem, with major agent frameworks evolving to include built-in continuous evaluation capabilities. These frameworks are designed to monitor for performance degradation and ensure operational quality long after initial deployment, as models, tools, and data distributions change over time [[56]](https://learn.microsoft.com/en-us/agents/architecture/evaluation-frameworks), [[57]](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon).

Your evaluation dataset must also be a living artifact. It should continuously expand with edge cases from new features, real-world failures captured from production traces via observability tools like Opik, and difficult debugging examples that expose current failure modes. Instead of writing new tests in code, you broaden your test coverage by adding new, challenging samples to the dataset. For instance, if you discover a regression in production where the agent fails on a specific user query, you should add that query and its expected outcome to your evaluation set to prevent the same error from happening again [[28]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets), [[29]](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals).

With the mechanics of the flywheel clear, we can now examine the different families of metrics we might plug into it when dealing with unstructured outputs.

## Exploring Possible Metric Types

The core difficulty in evaluating AI systems is that we are often dealing with unstructured outputs like text or images, not the structured labels of classical ML. This means standard metrics like accuracy are often unavailable. We can group the alternatives into three main families.

### 1. BLEU and ROUGE

Metrics like BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Oriented Understudy for Gisting Evaluation) measure the overlap of n-grams (sequences of words) between a generated text and a reference text. Their primary advantages are that they are fast to compute, deterministic, and require no additional models. However, they are blind to semantic meaning. An answer that is a valid paraphrase of the reference but uses different words will receive a low score, and they cannot assess factual correctness or the validity of a reasoning process. They reward keyword stuffing and penalize valid paraphrases, making them a poor fit for modern, creative LLMs [[30]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ), [[33]](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb).

### 2. BERTScore

Embedding similarity metrics, such as BERTScore, address the semantic blindness of n-gram overlap. They embed both the generated and reference texts into a high-dimensional vector space using a model like BERT and then calculate their cosine similarity. This captures semantic closeness, meaning paraphrased but correct answers score well. This approach aligns better with human judgments than lexical methods. The main limitation is that they are still comparison-based and cannot verify complex, multi-step business logic or adherence to specific guidelines that are not present in the reference text. They also inherit the computational cost and potential biases of the underlying embedding model [[30]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ), [[66]](https://spotintelligence.com/2024/08/20/bertscore/).

### 3. LLM Judges

The LLM-as-a-judge approach uses a capable LLM to evaluate an output based on a detailed set of criteria. You provide the judge model with the original input, the generated output, a rubric defining quality, few-shot examples of good and bad outputs, and chain-of-thought instructions to guide its reasoning. This method is highly flexible and can be customized to evaluate subjective qualities like tone, brand voice, or adherence to complex, domain-specific rules. For example, you can create a judge to check if a response is polite, factually aligned with a source document, or follows a specific JSON schema. The primary downsides are that performance depends heavily on the prompt and the judge model, they can be slower and more expensive, and they can inherit the biases of the evaluator LLM if not carefully designed and validated [[38]](https://www.braintrust.dev/articles/what-is-llm-as-a-judge), [[35]](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method), [[53]](https://cameronrwolfe.substack.com/p/llm-as-a-judge).

Before being used to gate a release, a judge must be calibrated. This involves an iterative loop: label a representative dataset, run the judge, review disagreements, and update the criteria or examples until the judge's scores track the real-world outcomes you care about. Advanced techniques can further enhance reliability, such as using statistical methods to correct for measurement error, weighting scores by token probabilities, or fine-tuning smaller, specialized judge models on preference data [[58]](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production), [[59]](https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork), [[60]](https://arxiv.org/html/2601.05420v1), [[61]](https://www.reddit.com/r/LLMDevs/comments/1j3gbil/5_techniques_to_improve_llmjudges), [[62]](https://cameronrwolfe.substack.com/p/finetuned-judge).

| Metric Family | Speed | Cost | Semantic Awareness | Business Alignment | Explainability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BLEU/ROUGE** | High | Low | Low | Low | Moderate |
| **BERTScore** | Moderate | Low | High | Moderate | Low |
| **LLM Judges** | Low | High | High | High | High |

Table 1: A trade-off summary of different metric families.

For the kinds of complex, guideline-driven tasks we encounter in agentic systems, such as the writing workflow in our capstone project, LLM judges are often the most practical choice.

Now, you have heard from us repeatedly: "business metrics here, business metrics there." Let's understand why defining your own business metrics is such an essential and underrated step in building your AI evals strategy.

## Why Business Metrics Over Benchmarks

Using popular leaderboards or public benchmarks to select an LLM for your product is often a mistake. Benchmarks are one of the most deceiving types of metrics for two core reasons.

First, public benchmarks often function as marketing artifacts. Once a test set becomes public, models can be trained on it, and teams begin to overfit their systems to the specific questions in the benchmark. This "teaching to the test" inflates scores and erodes the benchmark's validity as a measure of generalized performance on unseen data. This pattern repeats historical issues in ML, where benchmarks like GLUE were eventually replaced by harder versions like SuperGLUE to combat overfitting. There have been instances where models achieved suspiciously high scores, suggesting they may have been fine-tuned on the test sets themselves, a phenomenon known as data contamination [[11]](https://www.evidentlyai.com/llm-guide/llm-benchmarks), [[13]](https://launchdarkly.com/blog/llm-evaluation), [[15]](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053), [[63]](https://medium.com/@yujiisobe/navigating-the-maze-of-llm-evaluation-a-guide-to-benchmarks-rag-and-agent-assessment-fb7aef299e66).

Second, there is a fundamental mismatch between the tasks in most benchmarks and the demands of real-world business applications. A model's ability to solve math problems from a dataset like GSM8K says little about its capacity for long-form creative writing, nuanced legal analysis, or personalized customer support. The tasks are often synthetic or lack ecological validity, meaning they do not reflect the messy, complex workflows of a real production environment. The proper role for benchmarks is narrow. They are useful for advancing research and for initial model filtering during early exploration, but they should never be the primary driver of product-level decisions or optimization [[12]](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches), [[14]](https://arxiv.org/html/2601.20617v1).

If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous. We must instead build metrics that are deeply tied to our specific application.

## Why Custom Business Metrics Over Generic Metrics

Generic, off-the-shelf metrics for qualities like "toxicity," "helpfulness," or "hallucination" create a mirage. They generate a score, creating the illusion of progress while optimizing for a signal that is disconnected from your product, users, and brand voice. A model can score brilliantly on a generic "helpfulness" benchmark and still fail catastrophically on your specific constraints [[16]](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP), [[18]](https://arxiv.org/html/2508.13816v1).

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down
Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"

Consider the dashboard in Image 3. It looks impressive, with scores for "Truthfulness" and "Personalization." But what does a "3.7" in "Personalization" actually mean? Without context, the number is unactionable. This lack of alignment with user needs can lead to optimizing for the wrong thing.

For example, let's assume we want to check if the article written by our Brown agent contains hallucinations. If we use a generic `hallucination` score and it returns "positive," what does that tell us? Did it add information not present in the research? Did it deviate from the article guidelines? Or did it simply include a personal story that was not in the source text but is factually correct and relevant to the topic? A generic detector might flag an engaging personal anecdote as a fabrication, but that same anecdote may be exactly what your brand voice requires. The generic metric cannot distinguish between undesirable invention and desirable creative elaboration.

These prefab scores lack domain-specific constraints, cannot localize which part of an output failed, and introduce statistical noise into your decision-making. Their only valid role is during exploratory data analysis, where they can act as a "flashlight" to surface interesting examples for manual review, not as a "report card" for grading overall quality.

Here are some useful ways to use generic metrics for exploration:

1.  **Verbosity:** Sort your outputs by length. This can help reveal if your most verbose answers are rambling and unhelpful, or if your shortest answers are curt and missing information. This is a simple way to spot failure modes in long-form generation.
2.  **Similarity Score:** Use a similarity metric to evaluate your RAG retriever specifically. If the similarity between the user query and the retrieved chunks is consistently low, your retriever is likely failing. This is a valid component-level check.
3.  **BERTScore:** Use this to challenge the quality of your golden reference answers. If you find a cluster of generated outputs with a low BERTScore against a reference you expected to be similar, a manual review might reveal that the LLM found a more creative or even better way to solve the problem.

In all these cases, the generic metric is the start of an investigation, not the final verdict. Every production metric must be deeply application-centric, derived from concrete product requirements, user success criteria, and explicit constraints.

Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments from our LLM judge. Here, binary pass/fail criteria outperform every alternative.

## Choosing Binary Metrics Over Anything Else

When designing these custom metrics, you will face a choice: should you use a Likert scale (e.g., 1-5 stars) or a binary pass/fail? We strongly recommend **binary metrics**.

Likert scales are seductive because they seem to offer more nuance, but they introduce several problems that undermine the reliability of your evaluations:

1.  **Inconsistent Labeling:** The difference between a '3' and a '4' is subjective. One person's '4' is another's '3', leading to low inter-annotator agreement and noisy data. This ambiguity makes it difficult to achieve a high Cohen's Kappa score, a common measure of rater agreement [[4]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).
2.  **Statistical Noise:** Detecting a real improvement from an average score of 3.2 to 3.4 requires a much larger sample size than detecting a shift in a binary pass rate from 60% to 70%. Small movements are often indistinguishable from random variance, making it hard to know if your changes are having a real effect [[5]](https://www.ellamind.com/blog/binary-vs-likert-scales).
3.  **Lazy Decision-Making:** Both human evaluators and LLM judges often default to the middle value ('3') to avoid a difficult judgment. This "satisficing" behavior flattens the signal and hides the very failures you need to find. A dashboard full of '3's tells you your system is vaguely "okay," but not what to fix [[4]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).

Binary evaluations work because they **force decisions**. An output either met the specific criterion or it did not. This constraint leads to several benefits:

1.  **Clearer Thinking:** It forces you to create precise, unambiguous definitions of quality. You cannot hide in the ambiguity of a '3'.
2.  **Consistency:** Binary decisions are faster and more consistent for both humans and LLMs, yielding higher agreement.
3.  **Actionability:** The result is a clear failure signal tied to a specific problem, not a vague score change.

<aside>
💡

**Note:** The 3 points above translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate the inherent randomness of LLMs. LLMs are much more stable when asked to make a binary decision than when asked to assign a scalar value. A binary metric translates to a more robust and repeatable evaluation pipeline.

</aside>

### Capturing Nuance

The standard objection to binary metrics is the perceived loss of nuance. "A 'Fail' seems too harsh for a response that is partially correct."

The solution is not to use a fuzzier scale, but to make your criteria more **granular**. Instead of a single, subjective 1-5 rating for "Quality," you decompose it into multiple, specific, binary checks. However, for highly open-ended creative tasks, even granular checks can miss fundamental failures in narrative flow or coherence. For these genuinely indeterminate cases, a pragmatic escape hatch is to add a third `needs_review` label to flag examples for manual inspection instead of forcing a noisy binary judgment [[9]](https://www.ellamind.com/blog/binary-vs-likert-scales), [[58]](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production), [[64]](https://www.linkedin.com/posts/pauliusztin_i-created-an-ai-agent-to-write-a-substack-activity-7420095430807691266-fQ1U).

For our writing agent, instead of a single 1-5 score for "Article Quality," we could create several binary evaluations:

1.  **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
2.  **Flow of Ideas Adherence:** Does the generated article present ideas in the same order as the expected article? (Yes/No)
3.  **Article Guideline Adherence:** Does the generated article follow the flow of ideas from the article guideline input? (Yes/No)
4.  **Research Anchoring:** Is every claim in the article supported by the provided research? (Yes/No)

By aggregating these binary signals, you get a far more nuanced and actionable view of performance. A dashboard showing a 95% pass rate on "Content Adherence" but a 60% pass rate on "Research Anchoring" tells you exactly where to focus your optimization efforts. This approach provides granularity where it matters, without the statistical noise and subjectivity of Likert scales [[9]](https://www.ellamind.com/blog/binary-vs-likert-scales).

With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in the next lesson.

## Conclusion

The path to building robust AI products requires a fundamental shift away from vibe checks, leaderboards, and generic scores. It demands a commitment to rigorous, evaluation-driven development built on a foundation of custom, binary, and business-aligned metrics. Granular pass/fail criteria provide the clearest and most actionable signal for optimization, avoiding the statistical noise and subjectivity inherent in scalar ratings.

This theoretical framework is your blueprint for creating a reliable evaluation system. In the next lesson, we will translate this theory into practice by implementing custom LLM judges from scratch to evaluate our Brown writing workflow.

## References

- [4] The 5-Star Lie: You’re Doing AI Evaluations Wrong. (https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals)
- [5] Why We Use Binary Yes/No Evaluations (And You Should Too). (https://www.ellamind.com/blog/binary-vs-likert-scales)
- [9] Why We Use Binary Yes/No Evaluations (And You Should Too). (https://www.ellamind.com/blog/binary-vs-likert-scales)
- [11] LLM Benchmarks. (https://www.evidentlyai.com/llm-guide/llm-benchmarks)
- [12] 4 Approaches for LLM Evaluation. (https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches)
- [13] Effective LLM evaluation beyond basic benchmarks. (https://launchdarkly.com/blog/llm-evaluation)
- [14] Benchmarks for tool-using language agents in the public sector. (https://arxiv.org/html/2601.20617v1)
- [15] AI — Benchmark scores are becoming marketing; dynamic eval is the only antidote. (https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053)
- [16] Post by Shivanshu Aggarwal on LinkedIn. (https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP)
- [18] A Meta-Evaluation of Evaluation Metrics for General-Purpose Chatbots. (https://arxiv.org/html/2508.13816v1)
- [28] Manage Datasets. (https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets)
- [29] Generate Synthetic Datasets for AI Evals. (https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals)
- [30] LLM evaluation benchmarking: Beyond BLEU and ROUGE. (https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ)
- [33] Understanding BLEU and ROUGE score for NLP evaluation. (https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb)
- [35] Why LLM-as-a-Judge is The Best LLM Evaluation Method. (https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method)
- [38] What is LLM-as-a-judge? (https://www.braintrust.dev/articles/what-is-llm-as-a-judge)
- [40] Vibe Checks Are All You Need. (https://olshansky.substack.com/p/vibe-checks-are-all-you-need)
- [42] AI Evals vs. A/B Testing: Why You Need Both to Ship GenAI. (https://www.growthbook.io/blog/ai-evals-vs-a-b-testing-why-you-need-both-to-ship-genai)
- [44] Stop Evaluating LLMs with “Vibe Checks”. (https://towardsdatascience.com/stop-evaluating-llms-with-vibe-checks)
- [45] Statistical Significance. (https://corporatefinanceinstitute.com/resources/data-science/statistical-significance)
- [46] Statistical Significance Isn’t the Same as Practical Significance. (https://www.nngroup.com/articles/practical-significance)
- [47] Understanding Statistical Significance. (https://www.statsig.com/perspectives/understanding-statistical-significance)
- [53] LLM as a Judge. (https://cameronrwolfe.substack.com/p/llm-as-a-judge)
- [54] From TDD to EDD: Why Evaluation-Driven Development is the Future of AI Engineering. (https://medium.com/@nimrodbusany_9074/from-tdd-to-edd-why-evaluation-driven-development-is-the-future-of-ai-engineering-a5e5796b2af4)
- [55] Control theory. (https://en.wikipedia.org/wiki/Control_theory)
- [56] Evaluation frameworks for agents. (https://learn.microsoft.com/en-us/agents/architecture/evaluation-frameworks)
- [57] Evaluating AI agents: Real-world lessons from building agentic systems at Amazon. (https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon)
- [58] How To Build LLM-as-a-Judge Evaluators That Hold Up in Production. (https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production)
- [59] Better Experiments with LLM Evals: A Funnel, Not a Fork. (https://engineering.atspotify.com/2026/5/better-experiments-with-llm-evals-a-funnel-not-a-fork)
- [60] Calibrating LLM-as-a-Judge: A Unified Lens via Efficient Influence Functions. (https://arxiv.org/html/2601.05420v1)
- [61] 5 Techniques to Improve LLM-Judges. (https://www.reddit.com/r/LLMDevs/comments/1j3gbil/5_techniques_to_improve_llmjudges)
- [62] Fine-Tuned Judge. (https://cameronrwolfe.substack.com/p/finetuned-judge)
- [63] Navigating the Maze of LLM Evaluation. (https://medium.com/@yujiisobe/navigating-the-maze-of-llm-evaluation-a-guide-to-benchmarks-rag-and-agent-assessment-fb7aef299e66)
- [64] Post by Paul Iusztin on LinkedIn. (https://www.linkedin.com/posts/pauliusztin_i-created-an-ai-agent-to-write-a-substack-activity-7420095430807691266-fQ1U)
- [65] Escaping POC Purgatory: Evaluation-Driven Development for AI Systems. (https://www.decodingai.com/p/escaping-poc-purgatory-evaluation)
- [66] BERTScore explained: A modern metric for evaluating text generation. (https://spotintelligence.com/2024/08/20/bertscore/)