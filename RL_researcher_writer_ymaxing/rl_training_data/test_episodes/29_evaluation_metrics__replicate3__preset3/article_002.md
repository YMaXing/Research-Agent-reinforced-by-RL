# Lesson 29: The Theoretical Foundations of AI Evals

In our previous lessons, we instrumented our agents with observability tools like Opik and assembled our first offline evaluation datasets. We now have the raw materials for evaluation: traces and test cases. But how do we move from a folder of examples to a rigorous, repeatable system for measuring quality? With a well-defined evaluation layer, we know exactly what to optimize, and when developing new features, we can easily catch regressions.

This lesson moves to the core theoretical framework of designing the metrics themselves. In classical machine learning, we would never ship a model without a deep understanding of its accuracy, precision, recall, and F1 score, all validated with statistical significance. Yet in AI engineering, it has become common to rely on "vibe checks"—running a few queries and deciding a change "feels more coherent" [[31]](https://olshansky.substack.com/p/vibe-checks-are-all-you-need). This is not a new problem, but generative AI has turned all software engineers into ML engineers, making it easier to fall into this trap. This intuition-driven approach is a primary reason so many AI projects get stuck in proof-of-concept purgatory, leading to silent regressions and wasted engineering cycles [[32]](https://www.growthbook.io/blog/ai-evals-vs-a-b-testing-why-you-need-both-to-ship-genai).

Investing in a proper evaluation layer can feel difficult to prioritize. It delivers no immediate user-visible feature, requires upfront effort to design datasets and metrics, and competes with the constant pressure to ship new functionality. However, this investment is what unlocks long-term velocity. It replaces subjective guesswork with an objective signal that quantifies the impact of every change, catches regressions instantly, and focuses your team on what actually improves the system. Evals are the north star of AI engineering: the single source of truth that guides you toward a better product.

In this lesson, we will establish the theoretical foundation for evaluation-driven development. We will cover:
- How to operationalize evals inside a repeatable optimization flywheel.
- The trade-offs between different metric types for unstructured outputs.
- Why custom, business-aligned metrics are superior to public benchmarks and generic scores.
- Why binary pass/fail judgments provide a clearer signal than 1-5 star ratings.

With the problem and its importance clear, we will now examine how to operationalize evals inside a repeatable optimization flywheel that replaces intuition with evidence.

## Using Evals Through the Optimization Flywheel

To build intuition, let's examine how we can effectively use and integrate AI evaluations into our application development lifecycle. There are three core use cases where evaluations provide value.

First, evals **quantify the quality of your system** on a given set of metrics, creating a baseline snapshot of its current performance. This baseline is your single source of truth. It provides a clear, objective score that tells you how well your system is performing against your business goals. Without it, you cannot know if your system is production-ready or if your changes are making it better or worse. This single number is also invaluable for communicating progress to stakeholders and leadership, providing a shared language for what "good" looks like.

Second, these metrics serve as **guidance when optimizing your system**. They provide objective evidence for experiments, shifting development from being intuition-based to evidence-based. Instead of making a prompt change because it "feels better," you make a change, run your evals, and see a quantifiable impact on your metrics. This disciplined process, often called a data flywheel, creates a virtuous cycle of continuous improvement, where each iteration is guided by data, not guesswork. This systematic process involves curating data, customizing models, and running comprehensive evaluations to continuously refine the system based on real-world performance [[33]](https://galileo.ai/blog/nvidia-data-flywheel-for-de-risking-agentic-ai), [[34]](https://www.nvidia.com/en-us/glossary/data-flywheel).

Finally, evals act as **regression tests** that protect shared components from unintended degradation. This is critical in AI engineering, where prompts, tools, and retrieval strategies are often interconnected. A small change in one area can have unforeseen consequences elsewhere. For example, modifying a shared system prompt to make an agent more polite might accidentally break its ability to output valid JSON in a completely different workflow [[32]](https://www.growthbook.io/blog/ai-evals-vs-a-b-testing-why-you-need-both-to-ship-genai). In traditional software, a unit test like `assert 2 + 2 == 4` will never statistically drift. But in AI, a prompt that works 99% of the time today might work 92% tomorrow due to a minor model update. An automated evaluation suite catches these regressions before they reach production.

### The Optimization Process

How does this look in a real-world scenario? The optimization flywheel provides a step-by-step plan of attack.

1.  **Gather your dataset:** Assemble an offline dataset of representative examples, as we discussed in Lesson 28. This dataset is the foundation of your evaluation process and should cover a diverse range of scenarios your application will encounter, from common use cases to known edge cases.
2.  **Build your metrics:** Define a set of metrics that are deeply aligned with your business goals. These metrics will be your yardstick for success, so they must measure what truly matters for your product, such as task completion rate, factual accuracy, or adherence to brand voice.
3.  **Establish a baseline:** Run your evaluation suite on the current version of your system to compute baseline scores. This initial measurement is the stake in the ground against which all future changes will be compared. It is your objective starting point.
4.  **Start the optimization:** Make one, and only one, isolated change that you believe will improve performance. This could be a prompt tweak, a different model, or a new retrieval strategy. The discipline of changing only one variable is crucial for clear attribution.
5.  **Compute the new score:** Re-run the entire evaluation suite on the modified system. This ensures you are measuring the full impact of your change across all test cases, not just the ones you were focused on.
6.  **Compare:** Compare the new scores to your baseline, checking for statistical significance. This step tells you whether the change you made had a real, measurable effect or if the difference is just noise.
7.  **Decide:** Based on whether the score is better, the same, or worse, decide to keep the change, revert it, or reconsider its complexity. A better score is a win, but you must also weigh the added complexity, latency, or cost of the change.
8.  **Repeat:** Continue this cycle until your scores meet the desired quality bar for production. This iterative process is the engine of continuous improvement for your AI system.

```mermaid
flowchart LR
  A["1. Gather your dataset<br/>(Assemble offline dataset)"] --> B["2. Build your metrics<br/>(Define business-aligned metrics)"]
  B --> C["3. Establish a baseline<br/>(Run evaluations & compute scores)"]
  C --> D["4. Start the optimization<br/>(Make one isolated change)"]
  D --> E["5. Compute the new score<br/>(Re-evaluate entire dataset)"]
  E --> F["6. Compare<br/>(New scores to baseline with statistical significance)"]
  F --> G{"7. Decide<br/>(Keep, consider complexity, or revert change)"}
  G -->|"Score Better"| H["8. Repeat<br/>(Cycle until scores are good enough)"]
  G -->|"Score Same/Worse"| D
  H --> D
```
Image 1: The iterative optimization flywheel for AI applications using evaluations.

It is critical to keep all components fixed except for one variable per cycle. If you change the prompt, the model, and the retrieval strategy all at once, it becomes impossible to attribute any score movement to a specific cause. This turns a disciplined engineering process back into guesswork.

Furthermore, you must anchor the concept of a "better" score to actual business impact, not arbitrary p-values. A result being statistically significant says nothing about how valuable it is to users or the business [[3]](https://www.nngroup.com/articles/practical-significance). The practical significance depends entirely on your use case [[30]](https://www.cloudresearch.com/resources/guides/statistical-significance/what-is-statistical-significance). For a high-volume customer support bot processing millions of requests, a 0.5% reduction in checkout errors could translate to hundreds of thousands of dollars in saved revenue and support costs. In this context, even a small, statistically significant improvement has a massive business impact. In contrast, for a low-volume internal creative writing tool, a similar percentage improvement might be negligible, and you would require a much larger effect size before declaring a change successful [[29]](https://www.quirks.com/articles/effective-uses-of-effect-size-statistics-to-demonstrate-business-value). "Better" is always relative to the business problem you are trying to solve.

### Regression Testing

A powerful variant of this flywheel is using evaluations for regression testing. Before merging any new feature that touches shared components, you run the full evaluation suite. These components can include prompts, tool definitions, orchestration logic, or memory retrieval. This guards against breaking existing functionality.

This is because AI systems fail in ways that traditional software testing never anticipated. A unit test cannot catch a plausible-sounding but completely fabricated answer, and an integration test will not sound an alarm when performance degrades gradually as user behavior shifts. This is why structured evaluation frameworks are not just best practices; they are the core infrastructure that separates organizations that deploy AI responsibly from those that operate without a clear measure of quality [[6]](https://agility-at-scale.com/ai/architecture/evaluation-and-testing-frameworks).

Running AI evaluations as regression tests is a powerful technique to ensure new features do not break old ones. The process can be adapted from the optimization flywheel into five steps:

1.  **Implement a new feature:** You write the code and verify it works locally for the new use case. This is standard development practice.
2.  **Run the AI evaluations:** As part of your continuous integration (CI) pipeline, you automatically run the full suite of assessments against your changes, covering all previous use cases, not just the new one.
3.  **Compare Scores:** The CI system compares the new scores from your feature branch against the baseline scores from the main branch.
4.  **Metrics similar to baseline:** If the scores are statistically identical to the baseline, your feature has not introduced a regression. The change is safe to merge into your production codebase.
5.  **Metrics lower than the baseline:** If the scores are worse, you have introduced a regression. The merge is blocked, and you must fix your code, then repeat the evaluation cycle.

```mermaid
flowchart LR
  A["Implement New Feature"] --> B["Run AI Evaluations"]
  B --> C["Compare Scores"]
  C --> D{"Scores Similar to Baseline?"}
  D -- "Yes" --> E["Merge to Production"]
  D -- "No" --> F["Fix Code"]
  F --> B
```
Image 2: Integrating AI evaluations into CI pipelines for regression testing.

This treats your evaluation suite like unit or integration tests, but with a crucial difference: instead of asserting a strict pass or fail, you compare performance against a moving baseline. This is necessary because of the probabilistic nature of AI systems.

Your evaluation dataset must be a living artifact. It should continuously expand with edge cases from new features, real-world failures captured from production traces via observability tools like Opik, and difficult examples that expose current failure modes [[4]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets), [[5]](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals). For example, when debugging a regression found in production, you should add the specific trace that caused the failure to your evaluation dataset. This ensures that once you fix the issue, the same regression will be caught automatically in the future. In AI engineering, you broaden your test coverage not just by writing new test code, but by adding new, challenging samples to your dataset.

With the flywheel mechanics clear, we can now examine the different families of metrics we might plug into it when dealing with unstructured text and image outputs.

## Exploring Possible Metric Types

The core difficulty in evaluating LLM applications is that we are often dealing with unstructured outputs like text, reasoning traces, or images. Unlike classical ML with its clean, structured labels, we cannot use standard accuracy metrics directly. This has led to the development of several families of metrics, each with its own trade-offs.

### BLEU and ROUGE

Metrics like BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Oriented Understudy for Gisting Evaluation) are based on lexical overlap. They work by counting the overlap of n-grams (sequences of words) between the generated text and a reference text [[7]](https://plainenglish.io/blog/evaluating-nlp-models-a-comprehensive-guide-to-rouge-bleu-meteor-and-bertscore-metrics-d0f1b1). They are fast and deterministic but are blind to semantic meaning, penalizing correct paraphrasing and ignoring factual accuracy or logic [[8]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ), [[9]](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb).

### BERTScore

Embedding similarity metrics, like BERTScore, represent an improvement over lexical methods. They use a pre-trained language model like BERT to embed both the generated text and the reference text into a high-dimensional vector space. The similarity between these embeddings is used as the evaluation score [[10]](https://spotintelligence.com/2024/08/20/bertscore/). This captures semantic closeness better than lexical overlap but remains a comparison metric, unable to verify complex business rules or logical reasoning [[11]](https://www.elastic.co/search-labs/blog/evaluating-rag-metrics).

### LLM Judges

The LLM-as-a-judge approach uses a powerful LLM to evaluate the output of another model. You provide the judge model with the original input, the generated output, a detailed set of evaluation criteria, and often a few-shot examples and chain-of-thought instructions [[12]](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method), [[13]](https://arize.com/llm-as-a-judge). The approach gained popularity with the release of GPT-4, as it was one of the first models powerful enough to reliably evaluate the nuances of text generated by other models [[14]](https://cameronrwolfe.substack.com/p/llm-as-a-judge). This method is highly flexible and can be customized to evaluate against complex, domain-specific requirements that other metrics cannot capture. For example, you can ask an LLM judge to verify if a generated legal summary correctly identifies all relevant precedents while maintaining a formal tone.

The main advantage of LLM judges is their ability to evaluate subjective qualities and provide detailed, human-like critiques [[15]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge). However, their performance is highly dependent on the quality of the prompt and the capability of the evaluator model. They can also be slower and more expensive than automated metrics and may inherit the biases of the underlying LLM if not carefully designed and tested [[16]](https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw). These weaknesses can be mitigated through calibration, such as using multi-judge consensus or aligning the judge with human-scored golden datasets to correct for bias [[17]](https://galileo.ai/blog/llm-as-a-judge-vs-human-evaluation), [[18]](https://deepchecks.com/llm-judge-calibration-automated-issues).

Table 1: A comparison of trade-offs between different metric families for AI evaluations.

| Metric Family | Speed | Cost | Semantic Awareness | Business Alignment | Explainability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BLEU/ROUGE** | High | Low | Low | Low | Medium |
| **BERTScore** | Medium | Medium | High | Low | Low |
| **LLM Judges** | Low | High | Very High | Very High | High |

For complex tasks like our capstone writing workflow, which requires adherence to specific guidelines, structural fidelity, and grounding in research, LLM judges are the most practical choice. They are the only method that can flexibly encode and evaluate against such nuanced, multi-faceted criteria.

Now, you keep hearing from us: *"business metrics here, business metrics there"*. Thus, let's understand why defining your own business metrics is such an essential and underrated step in building your AI evals strategy.

## Why Business Metrics Over Benchmarks

It is a common mistake to look at popular leaderboards or open benchmarks to select a model or make product decisions. Benchmarks are often the most deceiving type of metric, and relying on them is a path to failure [[19]](https://launchdarkly.com/blog/llm-evaluation).

There are two core reasons for this. First, public benchmarks often function as marketing artifacts. Once a test set becomes public, models can be trained on the test data, intentionally or not, leading to data contamination and inflated scores [[20]](https://www.evidentlyai.com/llm-guide/llm-benchmarks), [[21]](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053). This "training to the test" means the benchmark no longer represents unseen data, and high scores become a misleading indicator of a model's true reasoning ability [[22]](https://openreview.net/forum?id=XbVMiW0jTM). There have even been instances where models were deliberately fine-tuned on test sets just to climb the leaderboards. Once a model achieves a top score, the benchmark can also become outdated, losing its effectiveness as a measure of progress and requiring the creation of more difficult tasks [[20]](https://www.evidentlyai.com/llm-guide/llm-benchmarks).

Second, there is a fundamental mismatch between the tasks found in most benchmarks and the workloads of real business applications. A model's ability to solve grade-school math problems (like in GSM8K) or answer multiple-choice questions (like in MMLU) has little bearing on its performance in tasks like long-form creative writing, nuanced legal analysis, or personalized customer support [[23]](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches). Many benchmarks also lack ecological validity, using synthetic or toy tasks that do not reflect the messiness of real-world workflows [[24]](https://arxiv.org/html/2601.20617v1).

The proper role for benchmarks is narrow: they are useful for advancing research frontiers and for initial model filtering during the early exploration phase of a project. They should never be used as a proxy for product-level decisions or as the primary target for optimization.

If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous. We must instead build metrics that are deeply tied to our specific application.

## Why Custom Business Metrics Over Generic Metrics

Generic, off-the-shelf metrics for qualities like "toxicity," "helpfulness," or "hallucination" create a mirage of progress. They optimize for the wrong signal and generate false confidence because they lack essential context about your product, your users, and your brand voice [[25]](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP), [[26]](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics). A model can score brilliantly on a generic "helpfulness" metric but fail catastrophically on your specific constraints.

Consider the dashboard below. It looks impressive, with scores for "Truthfulness" and "Personalization." But what does a 3.7 in "Personalization" actually mean? And what should the team do to improve it? These vague scores are often un-actionable vanity metrics [[1]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).![A dashboard showing generic, un-actionable AI metrics.](https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/w=1920,quality=90,fit=scale-down)
Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"

Let's assume we want to check if the article written by our Brown agent contains hallucinations. A generic `hallucination` score might return "positive," but what does that tell us? Did the model invent information not present in the research? Did it deviate from the article guidelines? Or did it simply include a personal story that, while not in the source text, is factually correct and relevant to the narrative? A generic detector might flag an engaging personal anecdote as a fabrication, but that same anecdote might be exactly what your brand voice requires. The generic metric cannot distinguish between undesirable invention and desirable creative elaboration.

Prefab scores suffer from several limitations: they cannot account for domain-specific constraints, they cannot localize which part of an output failed, and they introduce additional statistical noise into your decision-making process.

This does not mean generic metrics are useless. They have a narrow but valid role during exploratory data analysis. You can use them as a "flashlight" to surface interesting examples for manual review, not as a final "report card" for quality. Here are some examples:
1.  **Verbosity:** Sort your outputs by length. This can help you quickly find responses that are either too brief and unhelpful or too long and rambling. By inspecting the extremes, you might discover that your agent is consistently failing to provide enough detail on complex queries or, conversely, is overwhelming users with unnecessary information on simple ones. This simple check can reveal systemic issues in your generation logic.
2.  **Similarity Score:** In a RAG system, you can use a similarity score to evaluate the retriever component specifically. A low similarity between the user's query and the retrieved document chunks is a strong signal that your retriever is failing. This is a valid component-level check that helps isolate problems upstream from the final generation step, allowing you to debug your embedding model or chunking strategy independently.
3.  **BERTScore:** Use this to challenge your own assumptions about what a "good" answer is. If you have a set of "golden" reference answers and find a cluster of generated outputs with low BERTScore, a manual review might reveal that the LLM found a more creative or even more correct solution than the one you provided. This turns the evaluation process into a feedback loop for improving your ground truth.

In all these cases, the generic metric is the start of an investigation, not the final verdict. Every production metric must be deeply application-centric, derived from concrete product requirements, user success criteria, and explicit constraints.

Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments from our LLM judge. Here, binary pass/fail criteria outperform every alternative.

## Choosing Binary Metrics Over Anything Else

When designing these custom metrics, you will face a choice: should you use a Likert scale (e.g., 1-5 stars) or a binary pass/fail? We strongly recommend **binary metrics**.

Likert scales are a seductive trap. They promise nuance but often deliver noise. They suffer from several core problems [[1]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals), [[2]](https://www.ellamind.com/blog/binary-vs-likert-scales):
1.  **Inconsistent Labeling:** The difference between a '3' and a '4' is subjective. One person's '4' is another's '3', leading to low inter-annotator agreement and a fuzzy rubric.
2.  **Statistical Noise:** Detecting a meaningful improvement from an average score of 3.2 to 3.4 is difficult to distinguish from random variance and requires a much larger sample size than detecting a shift in a binary pass rate. For one common scenario, moving from a 60% to 70% pass rate requires less than half the samples to reach statistical significance compared to an equivalent shift on a 5-point scale.
3.  **Lazy Decision-Making:** Annotators—both human and LLM—often default to the middle value ('3') to avoid making a difficult judgment. This creates a "mushy middle" where most ratings cluster, hiding uncertainty rather than resolving it and leaving you with a sea of '3's that tells you your system is vaguely "okay" but not what to fix.

Binary evaluations solve these problems by forcing clarity. The benefits are immediate:
1.  **Clearer Thinking:** You cannot hide in ambiguity. An output either met a specific criterion or it did not. This forces you to create precise, unambiguous definitions of quality.
2.  **Consistency:** Binary decisions are faster and more consistent for both humans and LLMs, leading to higher agreement and a more reliable signal.
3.  **Actionability:** The output is not a fuzzy number but a clear signal tied to a specific failure mode. A spike in the "Constraint Violation" failure rate tells an engineer exactly where to start debugging.

The real value is often in the reasoning, not the score. A binary "Fail" paired with an explanation provides a specific diagnosis of what to fix, whereas a numeric '3' is ambiguous. This is why pairing binary judgments with explanations is so powerful for debugging.

<aside>
💡
**Note:** The 3 points above translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate the inherent randomness of LLMs. LLMs are much more stable when asked to make a binary decision than when asked to assign a scalar value. A binary metric translates to a more robust and repeatable evaluation pipeline.
</aside>

### Capturing Nuance

The standard objection is, "But I'm losing nuance! A 1-5 scale captures shades of gray." This is a valid concern, but a Likert scale is the wrong solution. The right way to capture nuance is not by making your scale fuzzier, but by making your criteria more **granular** [[2]](https://www.ellamind.com/blog/binary-vs-likert-scales).

Instead of a single, subjective rating, you decompose overall quality into multiple, specific, binary checks. For our Brown writing agent, instead of rating an article 1-5 for "Quality," we can create multiple binary evaluations that capture specific dimensions:
1.  **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
2.  **Flow of Ideas Adherence:** Does the generated article present ideas in the same order as the expected article? (Yes/No)
3.  **Article Guideline Adherence:** Does the generated article follow the structural flow from the article guideline input? (Yes/No)
4.  **Research Anchoring:** Is every claim in the article supported by the provided research? (Yes/No)

By aggregating these binary signals (using a simple average or a weighted sum), you get a nuanced, multi-dimensional view of performance. You can now say, "Our system has a 95% pass rate on Content Adherence but only a 60% pass rate on Research Anchoring." That is a clear, actionable signal. You have captured the nuance without sacrificing clarity, all while eliminating the statistical noise and middle-value bias inherent in Likert scales. This approach is simple, intuitive, and robust enough for production systems.

With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in the next lesson.

## Conclusion

The path to building reliable AI products requires a fundamental shift in mindset: away from vibe checks, leaderboards, and generic scores, and toward a rigorous practice of evaluation-driven development. This means building custom, business-aligned metrics that measure what actually matters to your users.

We have seen that granular, binary pass/fail criteria deliver the clearest and most actionable signal for optimization, avoiding the statistical noise and subjectivity inherent in scalar scales. This disciplined approach is the engine of product improvement. In our next lesson, we will translate this theory into practice by implementing custom LLM judges from scratch to evaluate our Brown writing workflow and put these principles into action.

## References

- [1] [The 5-Star Lie: You’re Doing AI Evaluations Wrong](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals)
- [2] [Why We Use Binary Yes/No Evaluations (And You Should Too)](https://www.ellamind.com/blog/binary-vs-likert-scales)
- [3] [Practical vs. Statistical Significance](https://www.nngroup.com/articles/practical-significance)
- [4] [Adding traces to a dataset](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets)
- [5] [Generate Synthetic Datasets for AI Evals](https://www.decodingai.com/p/generate-synthetic-datasets-for-ai-evals)
- [6] [Evaluation and Testing Frameworks for AI Systems](https://agility-at-scale.com/ai/architecture/evaluation-and-testing-frameworks)
- [7] [Evaluating NLP Models: A Comprehensive Guide to ROUGE, BLEU, METEOR, and BERTScore Metrics](https://plainenglish.io/blog/evaluating-nlp-models-a-comprehensive-guide-to-rouge-bleu-meteor-and-bertscore-metrics-d0f1b1)
- [8] [LLM evaluation & benchmarking: Beyond BLEU and ROUGE](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ)
- [9] [Understanding BLEU and ROUGE score for NLP evaluation](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb)
- [10] [BERTScore explained: A modern metric for evaluating text generation](https://spotintelligence.com/2024/08/20/bertscore/)
- [11] [Evaluating RAG: A practical guide to evaluation metrics](https://www.elastic.co/search-labs/blog/evaluating-rag-metrics)
- [12] [Why LLM-as-a-Judge is the Best LLM Evaluation Method](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method)
- [13] [How to use LLM-as-a-Judge](https://arize.com/llm-as-a-judge)
- [14] [LLM-as-a-Judge](https://cameronrwolfe.substack.com/p/llm-as-a-judge)
- [15] [LLM-as-a-Judge: The Go-To LLM Evaluation Method](https://www.evidentlyai.com/llm-guide/llm-as-a-judge)
- [16] [Post on LLM as a Judge by Alla Abdella](https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw)
- [17] [LLM-as-a-Judge vs. Human Evaluation: A Comparative Analysis](https://galileo.ai/blog/llm-as-a-judge-vs-human-evaluation)
- [18] [Calibrating LLM Judges for Automated Issue Detection](https://deepchecks.com/llm-judge-calibration-automated-issues)
- [19] [How to evaluate large language models (LLMs)](https://launchdarkly.com/blog/llm-evaluation)
- [20] [30 LLM evaluation benchmarks and how they work](https://www.evidentlyai.com/llm-guide/llm-benchmarks)
- [21] [AI — Benchmark scores are becoming marketing; dynamic eval is the only antidote](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053)
- [22] [PROBE: BENCHMARKING REASONING PARADIGM OVERFITTING IN LARGE LANGUAGE MODELS](https://openreview.net/forum?id=XbVMiW0jTM)
- [23] [4 Approaches for LLM Evaluation](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches)
- [24] [Benchmarks for Generative AI in the Public Sector](https://arxiv.org/html/2601.20617v1)
- [25] [Post on Generic AI Metrics by Shivanshu Aggarwal](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP)
- [26] [The Mirage of Generic AI Metrics](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics)
- [27] [What is Statistical Significance?](https://corporatefinanceinstitute.com/resources/data-science/statistical-significance)
- [28] [Understanding Statistical Significance](https://www.statsig.com/perspectives/understanding-statistical-significance)
- [29] [Effective uses of effect size statistics to demonstrate business value](https://www.quirks.com/articles/effective-uses-of-effect-size-statistics-to-demonstrate-business-value)
- [30] [What Is Statistical Significance?](https://www.cloudresearch.com/resources/guides/statistical-significance/what-is-statistical-significance)
- [31] [Vibe Checks Are All You Need](https://olshansky.substack.com/p/vibe-checks-are-all-you-need)
- [32] [AI Evals vs. A/B Testing: Why You Need Both to Ship GenAI](https://www.growthbook.io/blog/ai-evals-vs-a-b-testing-why-you-need-both-to-ship-genai)
- [33] [A Powerful Data Flywheel for De-Risking Agentic AI](https://galileo.ai/blog/nvidia-data-flywheel-for-de-risking-agentic-ai)
- [34] [What Is the Data Flywheel?](https://www.nvidia.com/en-us/glossary/data-flywheel)