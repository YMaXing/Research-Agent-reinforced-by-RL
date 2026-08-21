# The AI Evals Playbook: From Vibe Checks to Production-Ready Metrics

In our last lessons, we instrumented our agents with observability tools like Opik and assembled our first offline evaluation datasets. We now have the raw materials for a robust evaluation pipeline. With a well-defined evaluation layer, we know exactly what to optimize, and when developing new features, we can easily catch regressions.

Now, we move to the core theoretical framework of designing the metrics themselves. In classical machine learning, we operate with rigorous evaluation standards. Metrics like accuracy, precision, recall, and F1-score are non-negotiable, and we anchor our findings in statistical significance. In AI engineering, however, it is common to rely on "vibe checks." We tweak a prompt, run a few examples, and if the output "feels more coherent," we ship it.

Investing in a proper evaluation layer can feel hard to prioritize. It delivers no immediate user-visible feature, requires upfront effort in dataset and metric design, and competes with the constant pressure to ship. However, this investment dramatically accelerates long-term iteration by providing an objective signal on every change and catching regressions instantly. Evals are the north star of AI engineering: the single source of truth that tells you exactly which modifications improve the system and which degrade it.

In this lesson, we will cover the complete theoretical foundation for evaluation-driven development. We will explore:
- The optimization flywheel and its three core use cases.
- The trade-offs between different metric types for unstructured outputs.
- Why custom business metrics are superior to public benchmarks and generic scores.
- Why binary pass/fail judgments consistently outperform Likert scales.

With the problem and its importance clear, we will now examine how to operationalize evaluations inside a repeatable optimization flywheel that replaces intuition with evidence.

## Using Evals Through the Optimization Flywheel

To build intuition, let's examine how we can effectively use and integrate AI evaluations into our application development lifecycle. There are three core scenarios where evaluations provide value.

First, evaluations **quantify the quality of your system** on a set of given metrics, snapshotting a baseline of its current performance. Without a baseline, you cannot know if your system is production-ready or if your changes are leading to genuine improvements. Second, these metrics serve as **guidance when optimizing your system**. They provide objective evidence for experiments, shifting development from being intuition-based to evidence-based. Finally, they act as **regression tests** that protect shared components. Unlike optimization, the goal here is to ensure stability. This is critical in AI engineering, where prompts, tools, and retrieval strategies are often shared and interconnected across different features.

### The Optimization Process

How does this look in a real-world scenario? The optimization flywheel is an eight-step, iterative process for systematically improving your AI application.

1.  **Gather your dataset:** Assemble the offline dataset that represents the key scenarios and edge cases for your application.
2.  **Build your metrics:** Define the business-aligned metrics that measure what success looks like for your product.
3.  **Establish a baseline:** Run your evaluation suite on the current system to compute baseline scores for each metric.
4.  **Start the optimization:** Make one isolated change that you hypothesize will improve performance, such as modifying a prompt or swapping a model.
5.  **Compute the new score:** Re-evaluate the entire dataset by re-running the evaluation suite on the modified system.
6.  **Compare:** Compare the new scores to the baseline, considering statistical significance in the context of your business goals.
7.  **Decide:** Based on whether the scores improved, stayed the same, or worsened, decide to keep the change, revert it, or conduct further analysis, considering any new complexity introduced.
8.  **Repeat:** Continue this cycle, making one change at a time, until the scores meet your target for production readiness.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-4d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down> 
Image 1: The iterative optimization flywheel for AI applications using evaluations.

It is critical to keep all components fixed except for one variable per cycle. Confounding multiple modifications makes it impossible to attribute score movements to a specific cause, turning the process back into guesswork [[1]](https://www.decodingai.com/p/escaping-poc-purgatory-evaluation).

A "better" score is always relative to the specific business use case. You must anchor statistical significance to actual business impact rather than arbitrary p-value thresholds [[2]](https://www.nngroup.com/articles/practical-significance). For example, a 0.5% improvement in a high-volume customer support bot that handles millions of interactions could translate to thousands of dollars in savings from reduced support tickets. That small numerical improvement has massive real-world gain. In contrast, for a low-volume creative writing tool, a 5% improvement might be the minimum required to be noticeable or valuable to the user; any smaller improvement is likely negligible [[2]](https://www.nngroup.com/articles/practical-significance).

### Regression Testing

The optimization flywheel can be adapted for regression testing. Before merging any new feature that touches shared prompts, tool descriptions, orchestration logic, or memory retrieval, you run the full evaluation suite to guard against breaking existing behavior. Running AI evaluations as regression tests is a powerful technique to ensure new features do not degrade system performance.

This process can be simplified into five steps:

1.  **Implement a new feature:** You write the code and verify it works locally for the new use case.
2.  **Run the AI evaluations:** You run the full suite of assessments, which covers all previous use cases, not just the new one.
3.  **Compare Scores:** Compare the new scores against the established baseline for your production system.
4.  **Metrics similar to baseline:** If the scores for existing use cases are identical or within an acceptable range of the baseline, your new feature has not introduced a regression. You can merge the feature into your production codebase.
5.  **Metrics lower than the baseline:** If any score is significantly worse, you have introduced a regression. You should fix your code and then repeat the process from step 2.

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down> 
Image 2: Integrating AI evaluations into CI pipelines for regression testing.

This treats evaluations like integration tests, where you compare scores against a moving baseline instead of enforcing a strict pass/fail threshold. The dataset itself must also evolve. It should continuously expand with new edge cases from feature development, production trace failures captured via observability tools like Opik, and difficult examples that expose current failure modes [[3]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets). Instead of writing new tests in code, you broaden the test coverage by adding new samples to the dataset. For instance, if you discover a production regression where the agent fails on a specific type of user query, you can add that query and its expected outcome to your evaluation dataset, ensuring that future changes are tested against this known failure mode [[3]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets).

With the flywheel mechanics clear, we can now examine the different families of metrics we might plug into it when dealing with unstructured outputs.

## Exploring Possible Metric Types

The core difficulty in evaluating AI systems is that we are often working with unstructured outputs like text or images. Unlike classical ML with structured labels, standard metrics like accuracy are unavailable. This has led to the development of several families of metrics, each with its own trade-offs.

### 1. BLEU and ROUGE

N-gram overlap metrics like BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Oriented Understudy for Gisting Evaluation) are the most traditional. They work by counting the number of overlapping word sequences (n-grams) between the generated text and a reference text [[4]](https://datumo.com/en/blog/insight/key-nlp-evaluation-metrics/), [[5]](https://www.traceloop.com/blog/demystifying-the-bleu-metric). Their main advantages are that they are fast to compute, deterministic, widely understood, and do not require an additional model. However, they are also blind to semantic equivalence. They cannot tell if a paraphrase is correct, and they do not care about factual accuracy. If the generated text uses different words to express the same correct idea, it will be penalized [[6]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ).

### 2. BERTScore

Embedding similarity metrics, such as BERTScore, address the semantic limitations of n-gram overlap [[7]](https://spotintelligence.com/2024/08/20/bertscore/). They work by embedding both the generated and reference texts into a high-dimensional vector space using a model like BERT. The cosine similarity between these embeddings is then used to measure how close they are in meaning. This approach is better at capturing semantic meaning and is more robust to paraphrasing [[7]](https://spotintelligence.com/2024/08/20/bertscore/). However, it remains a comparison-based metric. It can tell you if two pieces of text are similar, but it cannot verify complex business rules or multi-step logic on its own.

### 3. LLM Judges

The LLM-as-a-judge approach uses a powerful LLM to evaluate the output of another model [[8]](https://hamel.dev/blog/posts/llm-judge/). You provide the judge model with the input, the generated output, a set of detailed criteria, few-shot examples, and chain-of-thought instructions. The judge then produces a structured judgment, such as a score or a pass/fail decision [[9]](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method). This method is highly flexible and can be customized to evaluate against complex, domain-specific requirements that other metrics cannot handle. For example, you can ask an LLM judge to verify if a generated summary adheres to a specific tone of voice while also being factually consistent with a source document.

The main advantage of LLM judges is their ability to evaluate subjective qualities and provide detailed, human-like critiques. However, their performance depends heavily on the quality of the prompt and the power of the evaluator model. They can be slower and more expensive than other metrics and may inherit the biases of the underlying LLM if not carefully designed and validated [[10]](https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw).

| Metric Family | Speed | Cost | Semantic Awareness | Business Alignment | Explainability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BLEU/ROUGE** | Very Fast | Very Low | None | Low | Low |
| **BERTScore** | Fast | Low | High | Medium | Low |
| **LLM Judges** | Slow | High | Very High | Very High | High |
Table 1: A trade-off summary of different metric families.

For the kinds of nuanced evaluation needed for our capstone writing agent—such as guideline adherence, structural fidelity, and research grounding—LLM judges are the most practical choice. They offer the customizability required to enforce our specific business rules.

Now, you have probably heard us say: *"business metrics here, business metrics there"*. Thus, let's understand why defining your own business metrics is such an essential and underrated step in building your AI evaluation strategy.

## Why Business Metrics Over Benchmarks

It is a common mistake to use popular leaderboards or open benchmarks to select an LLM or make product decisions. We believe this is often a mistake, as benchmarks are one of the most deceiving types of metrics.

First, benchmarks often function as marketing artifacts [[11]](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053). Once a test set becomes public, models can be trained on the test data, a phenomenon known as data contamination [[12]](https://www.evidentlyai.com/llm-guide/llm-benchmarks). This leads to inflated scores that no longer reflect performance on unseen data. Some research has shown that even powerful models can suffer from "reasoning paradigm overfitting," where they memorize solution patterns specific to a benchmark rather than developing generalizable reasoning skills [[13]](https://openreview.net/forum?id=XbVMiW0jTM).

Second, there is a fundamental mismatch between the tasks found in most benchmarks and the needs of real business applications [[12]](https://www.evidentlyai.com/llm-guide/llm-benchmarks). A model that excels at solving grade-school math problems from the GSM8k benchmark may not be suitable for generating nuanced legal analysis or providing personalized customer support. The skills are not transferable.

Benchmarks have a narrow but important role in advancing research and for initial model filtering during early exploration. However, they should never be used as a proxy for product-level decisions or as the primary target for optimization.

If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous. We must instead build metrics that are deeply tied to our specific application.

## Why Custom Business Metrics Over Generic Metrics

Generic, off-the-shelf metrics for qualities like "toxicity," "helpfulness," or "hallucination" create a mirage of progress. They optimize for the wrong signal and build false confidence because they lack context about your product, your users, and your brand voice [[14]](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics). A model can score brilliantly on a generic "helpfulness" metric but fail catastrophically on your specific constraints.

Consider the dashboard below. It looks impressive, with scores for "Truthfulness" and "Personalization." But what does a 3.7 in "Personalization" actually mean? These abstract scores are not actionable [[15]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).

<https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down> 
Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"

For example, let's assume we want to check if an article written by our Brown agent contains hallucinations. A generic `hallucination` score might return "positive," but what does that tell us? Did the agent invent information not present in the research? Did it deviate from the article guidelines? Or did it simply include a personal story that, while not in the source text, is factually correct and aligns with the desired brand voice? A generic detector might flag an engaging personal anecdote as a fabrication, but that same anecdote may be exactly what your product requires. The generic metric cannot distinguish between undesirable invention and desirable creative elaboration [[14]](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics).

These prefab scores lack domain-specific constraints, cannot localize which part of an output failed, and introduce additional statistical noise into your decision-making. Their only valid role is during exploratory data analysis, where they can act as a "flashlight" to surface interesting examples for manual review, but never as a "report card" for grading your system [[14]](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics).

Here are a few examples of using generic metrics for exploration:
1.  **Verbosity:** Sort your outputs by length. This can help you find rambling, unhelpful responses or curt, incomplete ones, pointing you toward failure modes in long-form generation.
2.  **Similarity Score:** In a RAG system, you can use a similarity score to evaluate the retriever specifically. If the similarity between the user's query and the retrieved chunks is consistently low, it is a strong signal that your retriever is failing.
3.  **BERTScore:** You can use BERTScore to check the quality of your "golden" reference answers. If you find a cluster of generated outputs with a low score against a reference you expected to be similar, it might be that the LLM found a more creative or even better solution than your reference.

Every production metric must be deeply application-centric, derived from concrete product requirements, user success criteria, and explicit constraints.

Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments from our LLM judge. Here, binary pass/fail criteria outperform every alternative.

## Choosing Binary Metrics Over Anything Else

When designing these custom metrics, you will face a choice: should you use a Likert scale (e.g., 1-5 stars) or a binary pass/fail? We strongly recommend **binary metrics**.

Likert scales are plagued with problems that make them unsuitable for rigorous AI evaluation [[15]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals), [[16]](https://www.ellamind.com/blog/binary-vs-likert-scales).

1.  **Inconsistent Labeling:** The difference between a '3' and a '4' is subjective. One person's '4' is another's '3', leading to low inter-annotator agreement and noisy data.
2.  **Statistical Noise:** Detecting a meaningful improvement from an average score of 3.2 to 3.4 requires a much larger sample size than detecting a shift in a binary pass rate from 75% to 80%. Small movements are often indistinguishable from random variance.
3.  **Lazy Decision-Making:** Evaluators, both human and LLM, tend to default to the middle value ('3') to avoid making a difficult judgment. This "satisficing" behavior flattens the signal and hides real failure modes in a "mushy middle" [[16]](https://www.ellamind.com/blog/binary-vs-likert-scales).

Binary evaluations work because they **force decisions**. They offer several advantages:

1.  **Clearer Thinking:** A pass/fail decision forces you to create precise, unambiguous definitions of quality. You cannot fail an output without knowing *why* it failed.
2.  **Consistency:** Binary judgments yield higher consistency across both human annotators and LLM judges, as the task is simpler and less subjective.
3.  **Actionability:** A pass rate of 75% is a clear, actionable signal. An average score of 3.4 is not. Binary metrics provide immediate failure signals tied to specific problems.

<aside>
💡
**Note:** The three points above translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate the inherent randomness of LLMs. LLMs are much more stable when asked to make a binary decision than when asked to assign a scalar value. A binary metric translates to a more robust and repeatable evaluation pipeline [[16]](https://www.ellamind.com/blog/binary-vs-likert-scales).
</aside>

### Capturing Nuance

The standard objection is, "But I'm losing nuance! A 1-5 scale captures shades of gray." This is a misconception. The right way to capture nuance is not by making your scale fuzzier, but by making your criteria more **granular** [[15]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).

Instead of a single, subjective rating for "Quality," you should decompose it into multiple, specific, binary checks. For our writing agent, this might look like:

1.  **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
2.  **Flow of Ideas Adherence:** Does the generated article present ideas in the same logical order as the expected article? (Yes/No)
3.  **Article Guideline Adherence:** Does the generated article follow all constraints from the article guideline input? (Yes/No)
4.  **Research Anchoring:** Is every factual claim in the article directly supported by the provided research? (Yes/No)

By aggregating these binary signals, you get a nuanced, multi-dimensional view of performance without the noise and ambiguity of a Likert scale. This approach is simple, scalable, and robust, making it ideal for production systems.

With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in the next lesson.

## Conclusion

This lesson has laid out the case for a fundamental shift in how we approach AI evaluation. We must move away from vibe checks, leaderboards, and generic scores toward a rigorous practice of evaluation-driven development. This practice is built on a foundation of custom, business-aligned metrics that are evaluated with binary judgments. Granular pass/fail criteria deliver the clearest optimization signal while avoiding the statistical noise and subjectivity inherent in scalar ratings.

This theoretical framework provides the "why" behind a robust evaluation strategy. In our next lesson, we will translate this theory into practice by implementing custom LLM judges from scratch to evaluate our Brown writing workflow.

## References

- [1] [Escaping POC Purgatory: Evaluation-Driven Development for AI Systems](https://www.decodingai.com/p/escaping-poc-purgatory-evaluation)
- [2] [Statistical Significance Isn’t the Same as Practical Significance](https://www.nngroup.com/articles/practical-significance)
- [3] [manage-datasets-opik-documentation-opik-documentation](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets)
- [4] [Key NLP Evaluation Metrics](https://datumo.com/en/blog/insight/key-nlp-evaluation-metrics/)
- [5] [Demystifying the BLEU Metric: A Comprehensive Guide to Machine Translation Evaluation](https://www.traceloop.com/blog/demystifying-the-bleu-metric)
- [6] [LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ)
- [7] [BERTScore explained: A modern metric for evaluating text generation](https://spotintelligence.com/2024/08/20/bertscore/)
- [8] [Using LLM-as-a-Judge For Evaluation: A Complete Guide](https://hamel.dev/blog/posts/llm-judge/)
- [9] [LLM-as-a-Judge Simply Explained: The Complete Guide to Run LLM Evals at Scale](https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method)
- [10] [LLM as a Judge: when to use reasoning (CoT) and explanations](https://www.linkedin.com/posts/allaabdella_llm-aijudge-genai-activity-7353053642590932994-s3sw)
- [11] [AI — Benchmark scores are becoming marketing; dynamic eval is the only antidote](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053)
- [12] [30 LLM evaluation benchmarks and how they work](https://www.evidentlyai.com/llm-guide/llm-benchmarks)
- [13] [PROBE: BENCHMARKING REASONING PARADIGM OVERFITTING IN LARGE LANGUAGE MODELS](https://openreview.net/forum?id=XbVMiW0jTM)
- [14] [The Mirage of Generic AI Metrics](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics)
- [15] [The 5-Star Lie: You’re Doing AI Evaluations Wrong](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals)
- [16] [Why We Use Binary Yes/No Evaluations (And You Should Too)](https://www.ellamind.com/blog/binary-vs-likert-scales)
- [17] [Evaluating NLP Models: A Comprehensive Guide to ROUGE, BLEU, METEOR, and BERTScore Metrics](https://plainenglish.io/blog/evaluating-nlp-models-a-comprehensive-guide-to-rouge-bleu-meteor-and-bertscore-metrics-d0f1b1)
- [18] [Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)](https://eugeneyan.com/writing/llm-evaluators/)
- [19] [Stop Launching AI Apps Without This Framework](https://www.decodingai.com/p/stop-launching-ai-apps-without-this)