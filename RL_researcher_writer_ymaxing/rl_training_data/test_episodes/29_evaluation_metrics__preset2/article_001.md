# Beyond the Vibe Check: A Framework for AI Evals That Actually Work

In our previous lessons, we instrumented our AI agents with observability tools like Opik and built our first offline evaluation datasets. We now have the raw materials for assessing our system. The next step is to move from simply collecting data to designing the metrics that will guide our development.

In classical machine learning, evaluation is a rigorous discipline. We rely on well-defined metrics like accuracy, precision, recall, and F1 scores to measure performance. We demand statistical significance before declaring a new model superior. Yet, in AI engineering, many teams have fallen back on "vibe checks." An engineer runs a few prompts, looks at the output, and declares, "this feels more coherent." This intuition-driven approach is a primary reason so many AI projects get stuck in proof-of-concept purgatory.

This shift can be understood by drawing a parallel to traditional software engineering's move from manual testing to Test-Driven Development (TDD). TDD asks, "Does it work?" with a binary yes/no. Evaluation-Driven Development (EDD) for AI asks, "How well does it work?" and expects a nuanced, statistical answer. EDD is a fundamental rethinking of how we build reliable AI systems [[1]](https://medium.com/@nimrodbusany_9074/from-tdd-to-edd-why-evaluation-driven-development-is-the-future-of-ai-engineering-a5e5796b2af4).

Investing in a proper evaluation layer can feel like a detour. It does not deliver an immediate, user-visible feature. It requires upfront effort to design datasets and metrics, all while the pressure to ship new features mounts. However, this investment is what unlocks long-term, sustainable progress. It replaces guesswork with an evidence-based system that quantifies the impact of every change, catches regressions instantly, and focuses your team on what matters.

AI evaluations are the north star of AI engineering. They are the source of truth that tells you which modifications improve your system and which degrade it. In this lesson, we will build the theoretical foundation for evaluation-driven development, covering:

*   The optimization flywheel and its three core use cases.
*   The trade-offs between different metric types for unstructured outputs.
*   Why custom business metrics are superior to public benchmarks and generic scores.
*   Why binary pass/fail judgments provide a clearer signal than Likert scales.

With this framework clear, we can then examine how to operationalize evaluations inside a repeatable optimization flywheel that replaces intuition with evidence.

## Using Evals Through the Optimization Flywheel

To build intuition, let's examine how we can effectively use and integrate AI evaluations into our application development lifecycle. There are three core scenarios where evaluations provide value.

First, evals **quantify the quality of your system**. They provide a snapshot of your system's current performance against a set of business-aligned metrics, establishing a baseline. This baseline is the foundational source of truth for all future comparisons. It answers the question, "How good is our system right now?" Without this objective starting point, you cannot know if your system is ready for production or if subsequent changes are actually improvements. It transforms an abstract sense of quality into a concrete, measurable state.

Second, these metrics serve as **guidance when optimizing your system**. They provide objective evidence for your experiments, shifting development from being intuition-based to evidence-based. When a team refactors a prompt chain, they no longer have to rely on subjective feelings that "it feels much better." Instead, they can run the new version against the evaluation dataset and point to a quantifiable improvement in the scores. This data-driven approach allows you to prioritize changes that deliver the biggest impact and avoid wasting time on modifications that offer no real benefit.

Finally, evals act as **regression tests** that protect shared components. In AI engineering, components like prompts, tool descriptions, and retrieval logic are often interconnected. A small change in one area can have unintended consequences elsewhere. Evals ensure that new features do not break existing functionality, making them critical for maintaining stability as the system evolves.

### The Optimization Process

How does this look in a real-world scenario? Let's look at a step-by-step plan for the optimization flywheel.

1.  **Gather your dataset:** Assemble an offline dataset of representative inputs. As we covered in Lesson 28, this should be a mix of real production traces and targeted synthetic data designed to cover key features, personas, and edge cases.
2.  **Build your metrics:** Define a set of business-aligned metrics to measure performance. These should be custom-tailored to what "success" means for your specific application, a topic we will explore in depth later in this lesson.
3.  **Establish a baseline:** Run your evaluation suite on the current version of your system to compute baseline scores. This initial run creates the "source of truth" against which all future changes will be measured.
4.  **Start the optimization:** Make one isolated change that you hypothesize will improve performance. This could be a prompt tweak, swapping in a new model, or adjusting a RAG chunking strategy.
5.  **Compute the new score:** Re-evaluate the entire dataset with the modified system. An automated evaluation harness is essential here to make this step fast and repeatable.
6.  **Compare:** Compare the new scores to the baseline. This is not just about seeing if the number went up; it is about assessing if the change is statistically and practically significant.
7.  **Decide:** Based on whether the score is better, the same, or worse, you make a decision. If the score improves, you keep the change. If it is worse, you revert it. If it is the same, you might still revert it to avoid adding unnecessary complexity for no gain.
8.  **Repeat:** This cycle is the core of iterative development. You repeat it, one change at a time, until your scores meet the target you have set for production readiness.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-4d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down
Image 1: The iterative optimization flywheel for AI applications using evaluations.

It is critical to change only one variable per cycle. If you modify the prompt, the retrieval strategy, and the model all at once, it becomes impossible to attribute any score change to a specific modification. This turns your disciplined process back into guesswork. This principle mirrors practices from classical control theory, which often focuses on single-input, single-output (SISO) systems to create stable and predictable feedback loops for optimization [[2]](https://en.wikipedia.org/wiki/Control_theory).

When comparing scores, you must anchor statistical significance to actual **business impact**, not just arbitrary p-values [[3]](https://www.nngroup.com/articles/practical-significance). A result is statistically significant if it is unlikely to have occurred by chance, but it is practically significant only if the size of the effect matters in the real world.

For a high-volume customer support bot that handles millions of interactions, a tiny 0.5% reduction in checkout errors could translate to thousands of fewer failed transactions and save the business hundreds of thousands of dollars per year [[3]](https://www.nngroup.com/articles/practical-significance). In this context, a small but statistically significant improvement has massive practical significance. Conversely, for a low-volume creative writing tool, a small improvement in a helpfulness score might be statistically significant but practically meaningless if users do not perceive a difference. "Better" is always relative to the business use case, and you must define what magnitude of change is worth acting on.

### Regression Testing

The optimization flywheel can be adapted for regression testing. Before merging any new feature that touches shared prompts, tool descriptions, or orchestration logic, you run the full evaluation suite to guard against breaking existing behavior. Running AI evaluations as regression tests is an extremely powerful technique to ensure your new features do not break old ones.

The process is a simplified version of the optimization flywheel:

1.  **Implement a new feature:** You write the code and verify it works locally for the new use case.
2.  **Run the AI evaluations:** You run the full suite of assessments, covering all previous use cases, not just the new one.
3.  **Compare Scores:** You compare the new scores against the established baseline.
4.  **Metrics similar to baseline:** If the scores are identical or better than the baseline, your feature has not introduced a regression. You can merge it into your production codebase.
5.  **Metrics lower than the baseline:** If any score is worse, you have introduced a regression. You should fix your code and repeat the process until all scores are at or above the baseline.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down
Image 2: Integrating AI evaluations into CI pipelines for regression testing.

Unlike traditional software unit tests that have a fixed pass/fail threshold, AI evaluations often compare against a moving baseline. The goal is to ensure that performance does not degrade, while allowing for improvements to raise the baseline over time. This practice of continuous evaluation is becoming a standard feature in major agent development frameworks, which are evolving to include built-in monitoring to detect performance degradation before it impacts users [[4]](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon).

Your evaluation dataset must be a living asset. It must continuously expand with new edge cases, production failures captured via observability tools like Opik, and difficult examples that expose current failure modes [[5]](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets). For instance, after debugging a production issue where the agent failed on a specific user query, you should add that query and its expected outcome to your dataset. Instead of writing new tests in code, you broaden your test coverage by adding new samples to the dataset.

With the flywheel mechanics clear, we can now examine the different families of metrics we might plug into it when dealing with unstructured text and image outputs.

## Exploring Possible Metric Types

The core difficulty in evaluating modern AI systems is that we are often working with unstructured outputs like text, reasoning traces, or images. Unlike classical ML, where we have structured labels, standard accuracy metrics are often unavailable. This has led to the development of several families of metrics designed for these new modalities.

### 1. BLEU and ROUGE

Metrics like BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Oriented Understudy for Gisting Evaluation) measure the lexical overlap of n-grams between a generated text and a reference text [[6]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ), [[7]](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb). They are fast to compute, deterministic, and widely understood. However, they are blind to semantic meaning. A response can be a perfect paraphrase of the reference and receive a near-zero score because it uses different words [[6]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ). They also do not care about factual accuracy or the logical soundness of an argument. For example, if a reference is "The experiment succeeded," an output of "The test was successful" would get a BLEU score near zero despite meaning the same thing [[6]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ).

### 2. BERTScore

Embedding similarity metrics, such as BERTScore, address the semantic blindness of n-gram metrics [[8]](https://plainenglish.io/blog/evaluating-nlp-models-a-comprehensive-guide-to-rouge-bleu-meteor-and-bertscore-metrics-d0f1b1). They work by embedding both the generated and reference texts into a high-dimensional vector space using a model like BERT. The cosine similarity between these embeddings is then used to measure how close they are in meaning [[9]](https://spotintelligence.com/2024/08/20/bertscore/). This approach is much better at capturing semantic equivalence and recognizing paraphrases. However, it is still a comparison-based metric and cannot verify complex business rules or multi-step logic on its own. Furthermore, it is slower, more computationally expensive, and can inherit biases from the underlying embedding model [[6]](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ).

### 3. LLM Judges

The "LLM-as-a-judge" approach uses a powerful LLM to evaluate an output based on a detailed set of criteria [[10]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge). You provide the judge model with the input, the output, your evaluation rubric, few-shot examples, and chain-of-thought instructions. This method is highly flexible and can be customized to evaluate subjective qualities like tone, adherence to brand voice, or complex, domain-specific logic [[11]](https://www.braintrust.dev/articles/what-is-llm-as-a-judge).

The main advantage of LLM judges is their ability to provide detailed, human-like critiques. However, their performance is heavily dependent on the quality of the prompt and the capability of the judge model. They are also slower and more expensive than other automated metrics and can inherit the biases of the underlying LLM if not carefully developed and validated [[12]](https://cameronrwolfe.substack.com/p/llm-as-a-judge). Known biases include a preference for longer answers (verbosity bias), favoring answers that appear first (position bias), and favoring answers generated by the same model family (self-enhancement bias) [[10]](https://www.evidentlyai.com/llm-guide/llm-as-a-judge). To be trusted in production, a judge must first be calibrated by running it on a representative set of labeled data, reviewing disagreements with human labels, and iteratively updating the evaluation criteria until its judgments are reliable [[13]](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production).

| Metric Family | Speed | Cost | Semantic Awareness | Business Alignment | Explainability |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **BLEU/ROUGE** | Fast | Low | None | Low | Low |
| **BERTScore** | Medium | Medium | High | Medium | Medium |
| **LLM Judge** | Slow | High | High | High | High |
Table 1: A trade-off summary of different evaluation metric families.

For the complex requirements of our capstone writing agent, such as guideline adherence and research grounding, LLM judges are the most practical choice.

Now, you kept hearing from us: *"business metrics here, business metrics there"*. Thus, let's understand why defining your own business metrics is such an essential and underrated step in building your AI evals strategy.

## Why Business Metrics Over Benchmarks

Public benchmarks are one of the most deceiving types of metrics. Looking at popular leaderboards or open benchmarks to choose an LLM for your product is often a mistake. There are two core reasons for this.

First, benchmarks often become marketing artifacts [[14]](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053). Once a test set is public, it is susceptible to data contamination, where parts of the test set leak into the model's training data [[15]](https://www.evidentlyai.com/llm-guide/llm-benchmarks). This leads to inflated scores that do not reflect true generalization ability. More subtly, iterative prompt engineering and benchmark-driven development can themselves act as a form of training on the evaluation data, leading to systems that overfit to the benchmark without improving on real-world tasks [[16]](https://openreview.net/forum?id=maMnVCHl8J). For example, a model might memorize the specific solution pattern for a classic puzzle in a benchmark, like the "burning ropes for timing" problem. When presented with a slight variation of the puzzle that invalidates the standard solution, the overfit model fails because it rigidly applies the memorized procedure instead of reasoning from first principles [[17]](https://openreview.net/forum?id=XbVMiW0jTM).

Second, there is a fundamental mismatch between the tasks in most benchmarks and the demands of real business workloads. A model that excels at solving math problems from the GSM8k benchmark may be terrible at generating long-form, creative articles or performing nuanced legal analysis. The skills tested are often irrelevant to your product's specific needs [[18]](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches).

The proper role for benchmarks is narrow: they are useful for advancing research frontiers and for initial model filtering during early exploration. They should never be used as a proxy for product-level decisions or as a primary optimization target.

If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous. We must instead build metrics that are deeply tied to our specific application.

## Why Custom Business Metrics Over Generic Metrics

Generic, off-the-shelf metrics like "toxicity," "helpfulness," or RAGAS-style "faithfulness" create a mirage of progress [[19]](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP). They optimize for the wrong signal and build false confidence because they lack context about your product, your users, and your brand voice. A model can score brilliantly on a generic "helpfulness" benchmark and still fail catastrophically on your specific constraints [[20]](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics). For example, a real estate assistant might get a high helpfulness score for proposing showing times, but if those times are when the agent is unavailable, it has failed at its core task. The generic metric completely misses this critical functional error.

https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down
Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!"

Consider the dashboard in Image 3. It looks impressive, with scores for "Truthfulness" and "Personalization." But what does a 3.7 in "Personalization" actually mean? These vague scores are not actionable [[20]](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics).

Let's assume we want to check if the article written by our Brown agent contains hallucinations. If we use a generic `hallucination` score and it returns "positive," what does that tell us? Did it add information not present in the research? Did it deviate from the article guidelines? Or did it simply include a personal story that was not in the source text but is factually correct and relevant to the narrative? A generic detector might flag an engaging personal anecdote as a fabrication, yet that same anecdote may be exactly what your brand voice requires. The generic metric cannot distinguish between undesirable invention and desirable creative elaboration.

Prefab scores lack domain-specific constraints, cannot localize which part of an output failed, and introduce statistical noise into your decision-making. Their only valid role is during exploratory data analysis, where they can act as a "flashlight" to surface interesting examples for manual review, but they should never be the primary optimization target [[20]](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics).

Here are some valid, exploratory uses for generic metrics:

1.  **Verbosity:** Sorting your outputs by length can quickly reveal if your longest answers are rambling and unhelpful or if your shortest answers are too curt. This helps you spot failure modes in long-form generation by clustering problematic traces at the extremes.
2.  **Similarity Score:** In a RAG system, you can use a similarity score to evaluate the retriever component specifically. If the similarity between the user query and the retrieved document chunks is consistently low, your retriever is likely failing to find relevant information. This is a valid component-level diagnostic check.
3.  **BERTScore:** You can use BERTScore to challenge the quality of your own "golden" reference answers. If you find a cluster of outputs with a low score against a reference you expected to be similar, a manual review might reveal that the LLM found a more creative or even better solution than your reference.

In all these cases, the generic metric is the start of an investigation, not the final verdict. Every production metric must be deeply application-centric, derived from concrete product requirements and user success criteria.

Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments from our LLM judge. Here, binary pass/fail criteria outperform every alternative.

## Choosing Binary Metrics Over Anything Else

When designing these custom metrics, you will face a choice: should you use a Likert scale (e.g., 1-5 stars) or a binary pass/fail? We strongly recommend **binary metrics**.

Likert scales introduce several problems that undermine the evaluation process [[21]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals):

1.  **Inconsistent Labeling:** The difference between a '3' and a '4' is subjective and varies between annotators, leading to low inter-annotator agreement. One person's '4' is another's '3' [[21]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).
2.  **Statistical Noise:** Detecting a meaningful improvement from an average score of 3.2 to 3.5 requires a much larger sample size than detecting a shift in a binary pass rate from 60% to 70%. This noise makes it difficult to know if your changes are having a real impact [[22]](https://www.ellamind.com/blog/binary-vs-likert-scales).
3.  **Lazy Decision-Making:** Annotators, both human and LLM, often default to the middle value ('3') to avoid making a difficult judgment. This "satisficing" behavior hides uncertainty and flattens the signal, leaving you with a sea of '3's that tell you nothing about what to fix [[21]](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals).

Binary evaluations solve these issues because they **force decisions**. An output either met the specific criterion or it did not. This simple constraint leads to several benefits:

1.  **Clearer Thinking:** You cannot hide in ambiguity. Binary evaluations force you to create precise, unambiguous definitions of quality for each failure mode.
2.  **Consistency:** Binary decisions are faster and more consistent for both human annotators and LLM judges, leading to higher agreement and more reliable data.
3.  **Actionability:** The output is a clear signal tied to a specific problem. A spike in the failure rate for a "Constraint Violation" metric tells an engineer exactly where to start debugging.

<aside>
💡 **Note:** The 3 points above translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate the inherent randomness of LLMs. LLMs are much more stable when asked to make a binary decision than when asked to assign a scalar value. A binary metric translates to a more robust and repeatable evaluation pipeline.

</aside>
### Capturing Nuance

The standard objection to binary metrics is the perceived loss of nuance. "What if a response is partially correct? A 'Fail' seems too harsh." This is a valid concern, but the solution is not to use a fuzzier scale. The right way to capture nuance is to make your criteria more **granular**.

However, for complex creative tasks, it is important to acknowledge that even a suite of granular binary checks can sometimes miss high-level failures. An agent's output might pass every specific check but still lack overall coherence or narrative flow, an edge case that requires careful dataset design to capture [[23]](https://www.linkedin.com/posts/pauliusztin_i-created-an-ai-agent-to-write-a-substack-activity-7420095430807691266-fQ1U). Instead of a single, subjective 1-5 rating for a complex quality, you decompose it into multiple, specific, binary checks [[22]](https://www.ellamind.com/blog/binary-vs-likert-scales).

For our writing agent, instead of rating an article 1-5 for "Quality," we can create multiple binary evaluations that capture specific dimensions of quality:

1.  **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
2.  **Flow of Ideas Adherence:** Does the generated article contain the ideas in the same order as the expected article? (Yes/No)
3.  **Article Guideline Adherence:** Does the generated article follow the flow of ideas from the article guideline input? (Yes/No)
4.  **Research Anchoring:** Is every claim in the article supported by the provided research? (Yes/No)

By aggregating the results of these binary checks, you get a nuanced, multi-dimensional view of performance. A dashboard might show a 95% pass rate on "Content Adherence" but only a 60% pass rate on "Research Anchoring." This is a far more actionable signal than an overall "Quality" score of 3.8. You have captured the nuance without sacrificing clarity, all while eliminating the statistical noise and middle-value bias of Likert scales.

With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in the next lesson.

## Conclusion

The path to building robust AI products requires a fundamental shift in mindset. We must move away from vibe checks, public leaderboards, and generic scores, and embrace a rigorous, evaluation-driven development process. This means building custom, business-aligned metrics that measure what truly matters for your application.

Granular, binary pass/fail criteria provide the clearest and most actionable signal for optimization. They eliminate the statistical noise and subjectivity inherent in scalar ratings, forcing clarity and driving meaningful improvement. In our next lesson, we will translate this theory into practice by implementing custom LLM judges from scratch to evaluate our Brown writing workflow.

## References

- [1] [From TDD to EDD: Why Evaluation-Driven Development is the Future of AI Engineering](https://medium.com/@nimrodbusany_9074/from-tdd-to-edd-why-evaluation-driven-development-is-the-future-of-ai-engineering-a5e5796b2af4)
- [2] [Control theory - Wikipedia](https://en.wikipedia.org/wiki/Control_theory)
- [3] [Statistical Significance Isn’t the Same as Practical Significance](https://www.nngroup.com/articles/practical-significance)
- [4] [Evaluating AI agents: Real-world lessons from building agentic systems at Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon)
- [5] [Manage Datasets - Opik Documentation](https://www.comet.com/docs/opik/evaluation/advanced/manage_datasets)
- [6] [LLM evaluation benchmarking: Beyond BLEU and ROUGE](https://wandb.ai/ai-team-articles/llm-evaluation/reports/LLM-evaluation-benchmarking-Beyond-BLEU-and-ROUGE--VmlldzoxNTIzMTY0NQ)
- [7] [Understanding BLEU and ROUGE Score for NLP Evaluation](https://medium.com/@sthanikamsanthosh1994/understanding-bleu-and-rouge-score-for-nlp-evaluation-1ab334ecadcb)
- [8] [Evaluating NLP Models: A Comprehensive Guide to ROUGE, BLEU, METEOR, and BERTScore Metrics](https://plainenglish.io/blog/evaluating-nlp-models-a-comprehensive-guide-to-rouge-bleu-meteor-and-bertscore-metrics-d0f1b1)
- [9] [BERTScore explained: A modern metric for evaluating text generation](https://spotintelligence.com/2024/08/20/bertscore/)
- [10] [LLM-as-a-judge: a complete guide to using LLMs for evaluations](https://www.evidentlyai.com/llm-guide/llm-as-a-judge)
- [11] [What is LLM-as-a-judge?](https://www.braintrust.dev/articles/what-is-llm-as-a-judge)
- [12] [LLM As A Judge](https://cameronrwolfe.substack.com/p/llm-as-a-judge)
- [13] [How to Build LLM-as-a-Judge Evaluators That Hold Up in Production](https://arize.com/blog/how-to-build-llm-as-a-judge-evaluators-that-hold-up-in-production)
- [14] [AI — Benchmark scores are becoming marketing; dynamic eval is the only antidote](https://world.hey.com/bhari/ai-benchmark-scores-are-becoming-marketing-dynamic-eval-is-the-only-antidote-dedd7053)
- [15] [LLM evaluation benchmarks and how they work](https://www.evidentlyai.com/llm-guide/llm-benchmarks)
- [16] [On the Dangers of Stochastic Parrots: Can Language Models Be Too Big?](https://openreview.net/forum?id=maMnVCHl8J)
- [17] [Benchmark Overfitting in Large Language Models](https://openreview.net/forum?id=XbVMiW0jTM)
- [18] [LLM Evaluation in 4 Approaches](https://magazine.sebastianraschka.com/p/llm-evaluation-4-approaches)
- [19] [Shivanshu Aggarwal on LinkedIn](https://www.linkedin.com/posts/shivanshu-aggarwal_evals-aievals-llm-activity-7375884554177449985-16kP)
- [20] [The Mirage of Generic AI Metrics](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics)
- [21] [The 5-Star Lie: You’re Doing AI Evaluations Wrong](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals)
- [22] [Why We Use Binary Yes/No Evaluations (And You Should Too)](https://www.ellamind.com/blog/binary-vs-likert-scales)
- [23] [Paul Iusztin on LinkedIn](https://www.linkedin.com/posts/pauliusztin_i-created-an-ai-agent-to-write-a-substack-activity-7420095430807691266-fQ1U)
- [24] [Using LLM-as-a-Judge For Evaluation: A Complete Guide](https://hamel.dev/blog/posts/llm-judge/)
- [25] [Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)](https://eugeneyan.com/writing/llm-evaluators/)
- [26] [Escaping POC Purgatory: Evaluation-Driven Development for AI Systems](https://www.decodingai.com/p/escaping-poc-purgatory-evaluation)
- [27] [Stop Launching AI Apps Without This Framework](https://www.decodingai.com/p/stop-launching-ai-apps-without-this)
- [28] [Key NLP Evaluation Metrics](https://datumo.com/en/blog/insight/key-nlp-evaluation-metrics/)