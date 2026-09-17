## Global Context of the Lesson

### What We Are Planning to Share

We will write a lesson that establishes the theoretical foundation for evaluation-driven development (EDD) as the north star for AI engineering. We begin by contrasting traditional rigorous ML evaluation standards with the common reliance on vibe checks in AI work. We then detail the optimization flywheel and its three core use cases, the disciplined single-variable iteration process anchored to business impact, and the mechanics of continuously expanding datasets. Next we compare families of metrics suitable for unstructured outputs before making the case for custom business metrics over public benchmarks or generic prefab scores. Finally we argue for binary pass/fail judgments over Likert scales, showing how multiple granular binary criteria capture nuance without introducing subjectivity or statistical noise, and we close by connecting everything to the shift away from intuition-driven development.

### Why We Think It's Valuable

AI engineers routinely ship prompt or architecture changes based on intuition, leading to silent regressions and slow progress. Rigorous, business-aligned evals replace vibe checks with an evidence-based flywheel that quantifies impact, prevents breakage, and focuses effort on changes that actually move product metrics. Mastering when to use which metric family, why benchmarks mislead, why generic scores create false confidence, and why binary judgments reduce noise gives you a repeatable system for confident iteration at production scale.

### Expected Length of the Lesson

**3,400 words** (without the titles and references), where we assume that 200-250 words ≈ 1 minute of reading time.

### Theory / Practice Ratio

100% theory - 0% practice

## Anchoring the Lesson in the Course

### Details About the Course

This piece is part of a broader course on Agentic AI Engineering. The course consists of multiple modules with lessons progressing from foundational concepts to advanced implementation and production practices. 

Thus, it's essential to always anchor this piece into the broader course, understanding where the reader is in its journey. You will be careful to consider the following:
- The points of view.
- To not reintroduce concepts already taught in the previous lessons.
- To be careful when talking about concepts introduced only in future lessons.
- To always reference previous and future lessons when discussing topics outside the piece's scope.

### Lesson Scope

Lesson 29 sits after observability/tracing (Lesson 27) and offline dataset construction (Lesson 28); it supplies the conceptual framework for designing metrics before Lesson 30 implements LLM judges hands-on for the capstone writing agent.

### Point of View

The course is created by a team writing for a single reader, also known as the student. Thus, for voice consistency across the course, we will always use 'we,' 'our,' and 'us' to refer to the team who creates the course, and 'you' or 'your' to address the reader. Avoid singular first person and don't use 'we' to refer to the student.

Examples of correct point of view:

- Instead of "Before we can choose between workflows and agents, we need a clear understanding of what they are." word it as "To choose between workflows and agents, you need a clear understanding of what they are."

### Who Is the Intended Audience

AI engineers who have built agents, instrumented them with tracing tools such as Opik, and assembled evaluation datasets and who are now ready to replace subjective assessment with systematic, business-grounded metrics.

### Concepts Introduced in Previous Lessons

In previous lessons of the course, we introduced the following concepts:
**Part 1:**

- **Lesson 1 - AI Engineering & Agent Landscape**: Understanding the role, the stack, and why agents matter now
- **Lesson 2 - Workflows vs. Agents**: Grasping the crucial difference between predefined logic and LLM-driven autonomy
- **Lesson 3 - Context Engineering**: The art of managing information flow to LLMs
- **Lesson 4 - Structured Outputs**: Ensuring reliable data extraction from LLM responses
- **Lesson 5 - Basic Workflow Ingredients**: Implementing chaining, routing, parallel and the orchestrator-worker patterns
- **Lesson 6 - Agent Tools & Function Calling**: Giving your LLM the ability to take action
- **Lesson 7 - Planning & Reasoning**: Understanding patterns like ReAct (Reason + Act)
- **Lesson 8 - Implementing ReAct**: Building a reasoning agent from scratch
- **Lesson 9 - Agent Memory & Knowledge**: Short-term vs. long-term memory (procedural, episodic, semantic)
- **Lesson 10 - RAG Deep Dive**: Advanced retrieval techniques for knowledge-augmented agents
- **Lesson 11 - Multimodal Data**: Foundations and Implementations of Multimodal LLMs

**Part 2:**

- **Lesson 12 - Central Project: Scope & Design**: Introducing the scope and design of the central project
- **Lesson 13 - Agent Frameworks Overview & Comparison**: Dimensions of choosing suitable a agent framework, justifying the choices made for our central project
- **Lesson 14 - LLM Agent System Design Considerations and Framework**: Decision framework of system design, inference-time scaling and the cost/latency calculus
- **Lesson 15 - Nova End-to-End Project Walkthrough**: The end-to-end architecture of Nova: The research workflow
- **Lesson 16 - Foundations of Agentic Systems with FastMCP**: The primitives and transports of MCP and how MCP servers and clients are organized
- **Lesson 17 - Initial Data Ingestion and Tooling**: Tools to parallelize data processing in the ingestion layer 
- **Lesson 18 - The Research Loop: Query Generation, Perplexity, and Human Feedback**: The research loop - generating queries, integrating external web searches, and adding human feedbacks.
- **Lesson 19 - Final Outputs and Agent Completion**: Filter and scrape search results, create the final output of the research workflow
- **Lesson 20 - Brown End-to-End Project Walkthrough**: The end-to-end architecture of Brown: The writing workflow
- **Lesson 21 - Behind the Scenes of Iterating AI Architectures with the Brown Writing Agent**: The technical details about the architecture of Brown: The writing workflow
- **Lesson 22 - Implementing the Foundations of the Writing Workflow**: Context loading including writing profiles, media generation using the orchestrator-worker pattern and article generation using context enginnering
- **Lesson 23 - Reviewing and Editing Through the Evaluator-Optimizer Pattern**: Transforming linear writing workflow into a reliable, self-correcting system by implementing the Evaluator-Optimizer pattern
- **Lesson 24 - Human-in-the-Loop Through MCP Servers**: Adding human-in-the-loop MCP tools to enable editing the whole article or selected text workflow 
- **Lesson 25 - Orchestrate and Integrate Our Capstone Agents**: Introducing two architecture of the Central LLM orchestration pattern - Multi-Server Client & Composed Server - to integrate the two agents
- **Lesson 26 - End-to-End Demo: Generating a Course Lesson**: The end-to-end demo of Brown: The writing workflow

**Part 3:**

- **Lesson 27 - Agent Observability with Opik**: Introducing Opik as the main instrument to observe the activities of the two agents
- **Lesson 28 - Creating Datasets for AI Evals**: Building the dataset for evaluating the writing workflow

As this is the third lesson in Part 3 - Evaluation, Observability, Optimizations, and Deployment, after we introduced the concept of agent observability using Opik and started building our offline evaluation dataset in lesson 27 and 28, we move to the core theoretical framework of designing the metrics themselves. With a well-defined evaluation layer, we know exactly what to optimize, and when developing new features, we can easily catch regressions.


### Concepts That Will Be Introduced in Future Lessons

In future lessons of the course, we will introduce the following concepts:

- Implementing the evaluation pipeline including custom LLM judges from scratch
- Caliberating the custom judges and running the End-to-End Evaluation
- Continuous Integration workflows including pre-commit hooks, unit-tests, automated enforcement
- Stateless architecture, authentication with Descope, containerization with Docker
- Database and File Download/Upload, moving all states to a PostgreSQL database
- Continuous Deployment: set up the gcloud infrastructure, create a production-ready deployment pipeline 

If you must mention these, keep it high-level and note we will cover them in their respective lessons.

### Anchoring the Reader in the Educational Journey

Within the course we are teaching the reader multiple topics and concepts. Thus, understanding where the reader is in its educational journey it's critical for this piece. You have to use only previous introduced concepts, while being reluctant about using concepts that haven't been introduced yet.

When discussing the **concepts introduced in previous lessons** listed in the `Concepts Introduced in Previous Lessons` section, avoid reintroducing them to the reader. Especially don't reintroduce the acronyms. Use them as if the reader already knows what they are. 

Avoid using all the **concepts that haven't been introduced in previous lessons** listed in the `Concepts That Will Be Introduced in Future Lessons` subsection. Whenever another concept requires references to these banned concepts, instead of directly using it, use other intuitive and grounded explanations as you would explain them to a 7-year-old. For example:
- If the "tools" concept wasn't introduced yet and you have to talk about agents, refer them to as "actions".
- If the "routing" concept wasn't introduced yet and you have to talk about it, refer it to as "guiding the workflow between multiple decisions".
You can use the concepts that haven't been introduced in previous lessons listed in the `Concepts That Will Be Introduced in Future Lessons` subsection, only if we explicitly specify them. Still, even in that case, as the reader doesn't know how that concept works, you are just allowed to use the term, while keeping the explanation extremely high-level and intuitive, as if you were explaining it to a 7-year-old.
Whenever you use a concept from the `Concepts That Will Be Introduced in Future Lessons` subsection explicitly specify that it will be explained in more detail in future lessons.

In all use cases avoid using acronyms that aren't explicitly stated in the guidelines. Rather use other more accessible synonyms or descriptions that are easier to understand by non-experts.

## Narrative Flow of the Lesson

Follow the next narrative flow when writing the end-to-end lesson:

- What problem are we solving? Why is it essential to solve it?
	- Start with a personal story where we encountered the problem
- Why other solutions are not working and what's wrong with them.
- At a theoretical level, explain our solution or transformation. Highlight:
    - The theoretical foundations.
    - Why is it better than other solutions?
    - What tools or algorithms can we use?
- Provide some hands-on examples.
- Go deeper into the advanced theory.
- Provide a more complex example supporting the advanced theory.
- Connect our solution to the bigger picture and next steps.

## Lesson Outline

1. Introduction
2. Using Evals Through the Optimization Flywheel
3. Exploring Possible Metric Types
4. Why Business Metrics Over Benchmarks
5. Why Custom Business Metrics Over Generic Metrics
6. Choosing Binary Metrics Over Anything Else
7. Conclusion

## Section 1 - Introduction

- Start the section with a review on the previous lessons, specifically lesson 27 and 28, about agent observability using Opik and building offline evaluation dataset. 
- Now, we move to the core theoretical framework of designing the metrics themselves. Contrast the rigorous evaluation standards we expect in classical ML (accuracy, precision, recall, F1, statistical significance) with the pervasive reliance on vibe checks or simply skipping evaluation altogether in current AI engineering ("this output feels more coherent").
- Explain why investing in the eval layer feels hard to prioritize: it delivers no immediate user-visible feature, requires upfront dataset and metric design effort, and competes with the pressure to ship.
- Show how that same investment dramatically accelerates long-term iteration by giving an objective signal on every change and catching regressions instantly.
- Position evals as the north star of AI engineering: the single source of truth that tells you exactly which modifications improve the system and which degrade it.
- Provide a high-level roadmap of the lesson in the form of 4 bullet points: the optimization flywheel and its three core use cases, metric-type trade-offs for unstructured outputs, why business metrics beat benchmarks and generic scores, and why binary judgments beat Likert scales.
- Transition to Section 2: With the problem and importance clear, we now examine how to operationalize evals inside a repeatable optimization flywheel that replaces intuition with evidence.
-  **Section length:** 300 words

## Section 2 - Using Evals Through the Optimization Flywheel

To build intuition, let's examine how we can effectively use and integrate AI evaluations into our application development lifecycle. There are three core scenarios where evaluations provide value.

- Introduce the three core use cases for evals: (1) the evals **quantify the quality of your system** on a set of given metrics, snapshotting a baseline of current system quality. Without the baseline, one can't know if the system is ready or improving.
(2) metrics serve as **guidance when optimizing your system**, providing evidence for optimization experiments, shifting developement from intuition-based to evidence-based (3) acting as regression tests that protect shared components. Similar but unlike optimization, the goal is stability rather than improvement. Explain why it is critical in AI engineering as components are ofter shared and connected.

### **The Optimization Process**

- How does this look in a real-world scenario? Let's look at a step-by-step plan of attack for the optimization flywheel. Detail the eight-step flywheel in the form of eight numbered bullet points, where each step is carefuly explained in a single sentence following its name: (1) **Gather your dataset:** - assemble offline dataset, (2) **Build your metrics:** - define business-aligned metrics, (3) **Establish a baseline:** - run evals on the current system and compute baseline scores, (4) **Start the optimization:** - make one isolated change one believes to improve performance, (5) **Compute the new score:** - re-evaluate the entire dataset by re-running the evals, (6) **Compare:** - compare new scores to baseline with statistical significance, (7) **Decide:** - decide to keep, consider the complexity or revert the change based on the score is better, the same, or worse(8) **Repeat:** - repeat the cycle until the scores are good enough.

- Include the image in the link <https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/3fe225f6-9114-4d87-943c-d5bbe3fbbdfc/ai_evals/w=1920,quality=90,fit=scale-down>, the caption should be verbatim - "Image 1: The iterative optimization flywheel for AI applications using evaluations."

- Explain why it is critical to keep all the components fixed except one variable per cycle: confounding multiple modifications makes it impossible to attribute score movements and turns the process into guesswork.

- Anchor statistical significance to actual **business impact** rather than arbitrary p-value thresholds, using contrasting examples of a high-volume support bot (small movements matter) versus a low-volume creative writing tool (larger movements are required before declaring victory). To show "better" is always relative to the specific business use case, add an example where tiny numerical improvements translate to a massive real-world gain; then, add a contrasting example where small improvements are likely negligible.

### **Regression Testing**

-  Describe the regression-test variant: before merging any new feature that touches shared prompts, tool descriptions, orchestration logic, or memory retrieval, run the full eval suite against the offline dataset to guard against breakage in existing behavior. Explain why running AI evaluations as regression tests is an extremely powerful technique to ensure that your new features don't break existing features. One can modify the strategy from the above optimization flywheel to five steps:  

1. **Implement a new feature:** You write the code and verify it works locally for the new use case.
2. **Run the AI evaluations:** You run the full suite of assessments, covering all previous use cases, not just the new one.
3. **Compare Scores:** The baseline vs. the AI evals scores on your new feature
4. **Metrics similar to baseline:** If the scores are identical to the baseline, your feature is OK, as it didn't affect any old feature. You can merge the feature into your production codebase.
5. **Metrics lower than the baseline:** If the score is worse, you have introduced a regression. You should fix your code. Then repeat steps 2 and 3.

- Include the image in the link <https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/81fa7407-fdcd-4427-8468-669a31e2ca3f/ai_evals_-1/w=1920,quality=90,fit=scale-down>, the caption should be verbatim - "Image 2: Integrating AI evaluations into CI pipelines for regression testing."

- Contrast treating evals like unit or integration tests (where we compare scores against a moving baseline instead of enforcing a strict pass/fail threshold).

- Discuss how the dataset must continuously expand with new feature edge cases, production trace failures captured via observability and tracing with Opik, and hard debugging examples that expose current failure modes. Stress that instead of writing new tests in code, one broadens the tests by adding new sampels to the dataset. Also, add an example of expanding AI evals dataset when debugging code, say an example of expanding the dataset with production data the acaptures real-world regressions.

- Transition to Section 3: With the flywheel mechanics clear, we can now examine the different families of metrics we might plug into it when dealing with unstructured text and image outputs.

- **Section length:** 1200 words

## Section 3 - Exploring Possible Metric Types

- Frame the core difficulty: unlike classical ML with structured labels, we are evaluating unstructured text, reasoning traces, and sometimes image outputs, so standard accuracy-style metrics are unavailable.

There are three core families of metrics:

### **1\. BLEU and ROUGE**

- Present n-gram overlap metrics (BLEU, ROUGE): describe their lexical overlap calculation, pros (fast to compute, widely understood, deterministic, no additional model required), and cons (blind to semantic equivalence, paraphrasing, or correct reasoning that uses different words, nor care about factual accuracy).

### **2\. BERTScore**

- Present embedding similarity metrics (BERTScore, cosine similarity on embeddings): explain how they embed the generated and the reference texts in a high-dimensional vector space and capture semantic closeness, their advantage over pure lexical methods in terms of capturing semantic meaning, and their remaining limitation (still a comparison metric and unable to encode and verify complex business rules or logic).

### **3\. LLM Judges**

- Present the LLM-as-judge approach: prompt a capable evaluator LLM model with the input, the output, a set of detailed criteria, few-shot examples, and chain-of-thought instructions to produce judgments that can incorporate domain-specific, guideline-level, and multi-faceted requirements. Stress that this method is highly flexible and customizable, which enables evaluation against complex criteria, add an example here. 
- Talk about the pros and cons of LLM judges. Pros: evaluate subjective aspects and provide detailed, human-like critiques. They can be tuned to specific business contexts; Cons: Performance depends heavily on the quality of the prompt and the evaluator model. They can be slower and more expensive than automated metrics. Also, if not properly developed and tested, they inherit the LLM’s bias.
- Provide a trade-off summary table (speed, cost, semantic awareness, business alignment, explainability) that positions LLM judges as the most practical choice for the kinds of guideline adherence, structure fidelity, and research grounding needed for the writing workflow in capstone projects.
- Transition to Section 4: Now, you kept hearing from us:  _"business metrics here, business metrics there"_. Thus, let's understand why defining your own business metrics is such an essential and underrated step in building your AI evals strategy.

- **Section length:** 450 words

## Section 4 - Why Business Metrics Over Benchmarks

- State explicitly htat benchmarks are the most deceiving type of metrics, and looking at popular leaderboards or open benchmarks to find the best LLM and make product decisions is often a mistake.

There are two core reasons for this.

- Reason No.1 - Characterize benchmarks as marketing artifacts: once a test set becomes public, teams overfit to it, hill-climb on leaderboard scores, and lose validity because the set no longer represents unseen data. Add an example here of too-good-to-be-true models where there have been instances where models were fine-tuned on the test sets to inflate the final score.

- Reason No.2 - Highlight the fundamental mismatch between typical benchmark tasks (e.g., GSM8k-style math problems or generic QA) and real business workloads such as long-form creative writing, nuanced legal analysis, or personalized customer support.

- Define the proper, narrow role of benchmarks: advancing research frontiers, initial model selection or filtering during early exploration, and never as a proxy for product-level decisions or optimization targets.

- Transition to Section 5: If benchmarks are misleading, generic prefab metrics that claim to measure universal qualities are even more dangerous; we must instead build metrics that are deeply tied to our specific application.

- **Section length:** 250 words

## Section 5 - Why Custom Business Metrics Over Generic Metrics

- Show how generic metrics (toxicity, helpfulness, hallucination, RAGAS-style faithfulness, pre-built metrics in Opik) act as a mirage: they optimize the wrong signal and create false confidence because they lack context about your product, user expectations, and brand voice. Also, add an example to exemplify the case where the metric doesn't align with what users need,  leading to wrongful optimization.
- We need application-centric evaluations. A model can score brilliantly on "helpfulness," but fail catastrophically on your specific constraints. Consider the dashboard below. It looks impressive, with scores for "Truthfulness" and "Personalization." But what does a 3.7 in Personalization actually mean? Insert an image from the URL - <https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/585bb9f6-0bf3-427f-a9d3-994dd5849a1a/322c2e07-ee9a-4139-b51d-8f0c4787d880_1600x822/w=1920,quality=90,fit=scale-down> with the caption - "Image 3: A dashboard showing generic metrics like Helpfulness and Truthfulness, labeled "Don't Do This!" verbatim.
- For example, let's assume we want to check if the article written by our Brown agent contains hallucinations. If we use a generic `hallucination` score and it returns "positive," what does that tell us? Did it add information not present in the research? Did it deviate from the article guidelines? Or did it simply include a personal story that wasn't in the source text but is factually correct and relevant?
- Use a concrete hallucination example: a generic detector flags an engaging personal anecdote as fabrication, yet that same anecdote may be exactly what your brand voice requires; the generic metric cannot distinguish undesirable invention from desirable creative elaboration.
- Detail the limitations of prefab scores: absence of domain-specific constraints, inability to localize which part of the output failed, and introduction of additional statistical noise into decision making.
- Carve out a narrow, valid role for generic metrics strictly during exploratory data analysis (sorting examples by verbosity, retriever similarity, or reference quality) but never as the primary optimization target.
- List useful examples of using generic metrics:
  1. **Verbosity:** Sort your outputs by length to reveal if your most verbose answers are rambling and unhelpful. This helps you spot failure modes in long-form generation.
  2. **Similarity Score:** Use this to evaluate your RAG retriever specifically. If the similarity between the user query and the retrieved chunks is low, your retriever is likely failing to retrieve relevant information. This is a valid component-level check.
  3. **BERTScore:** Use this to check the quality of your golden references. If you find a cluster of outputs with low BERTScore against the reference that you expected to be similar, you might realize the LLM found a more creative, or even better, way to solve the problem than your reference answer.
- Insist that every production metric must be deeply application-centric, derived from concrete product requirements, user success criteria, and explicit constraints.
- Transition to Section 6: Once we have rejected both benchmarks and generic metrics, the remaining design choice is how to elicit judgments from our LLM judge; here binary pass/fail criteria outperform every alternative.

-  **Section length:** 600 words

## Section 6 - Choosing Binary Metrics Over Anything Else

When designing these custom metrics, you will face a choice: should you use a Likert scale (e.g., 1-5 stars) or a binary pass/fail?

We strongly recommend **binary metrics**.

- Expose the problems with Likert scales (1–5) in numbered bullet points: **Inconsistent Labeling** - high subjectivity in deciding whether an output is a 3 or a 4, **Statistical Noise** - statistical noise in small movements that are indistinguishable from random variance, and **Lazy Decision-Making** - lazy satisficing where evaluators or LLM judges default to middle values, leading to flatten signals and hidden failure modes.

Binary evaluations work because they **force decisions**.

- Present the advantages of binary pass/fail judgments in numbered bullet points: **Clearer Thinking** - they force precise, unambiguous definitions of quality, **Consistency** - yield higher inter-annotator (and inter-judge) consistency, **Actionability** - and deliver immediate actionable failure signals instead of vague score deltas.

- Explain how binary decisions materially reduce LLM judge variance compared with scalar ratings, producing more repeatable and trustworthy signals across runs with the following call-out box:

</aside>
💡
**Note:** The 3 points above translate exceptionally well to LLM Judges. Using binary scoring is a key design choice to mitigate the inherent randomness of LLMs. LLMs are much more stable when asked to make a binary decision than when asked to assign a scalar value. A binary metric translates to a more robust and repeatable evaluation pipeline.

</aside>

### **Capturing Nuance**

The standard objection is, "But I'm losing nuance! A 1-5 scale captures shades of gray."

- Demonstrate how to capture nuance without reintroducing subjectivity: instead of a fuzzier scale (1-5), making criteria **granular** - decompose overall quality into many multiple, specific, binary binary checks:

For our writing agent, instead of rating an article 1-5 for "Quality," we create multiple binary evaluations that capture specific dimensions of quality:

  1. **Content Adherence:** Does the generated article contain the same core concepts as the expected article? (Yes/No)
  2. **Flow of Ideas Adherence:** Does the generated article contain the ideas in the same order as the expected article? (Yes/No)
  3. **Article Guideline Adherence:** Does the generated article follow the flow of ideas from the article guideline input? (Yes/No)
  4. **Research Anchoring:** Is every claim in the article supported by the provided research? (Yes/No)

- Show how aggregating many binary signals (simple average or weighted sum) yields a nuanced performance view while eliminating scale noise and middle-value bias. This approach is simple, intuitive, scalable, and robust in production systems.

- Transition to Section 7: With the full theoretical picture in place, we can now summarize the mindset shift required and preview the hands-on implementation that follows in the next lesson.

- **Section length:** 500 words

## Section 7 - Conclusion

- Summarize the core shift from vibe checks, leaderboards, and generic scores to rigorous evaluation-driven development built on custom, binary, business-aligned metrics.
- Reiterate that granular pass/fail criteria deliver the clearest optimization signal while avoiding the statistical noise and subjectivity inherent in scalar scales.
- Connect back to the broader course by noting that the next lesson translates this theory into practice by implementing custom LLM judges from scratch to evaluate our Brown writing workflow.

- **Section length:** 100 words

## Golden Sources

- [Using LLM-as-a-Judge For Evaluation: A Complete Guide](https://hamel.dev/blog/posts/llm-judge/)
- [Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)](https://eugeneyan.com/writing/llm-evaluators/)
- [Benchmark Overfitting in Large Language Models](https://openreview.net/forum?id=XbVMiW0jTM)
- [The Mirage of Generic AI Metrics](https://www.decodingai.com/p/the-mirage-of-generic-ai-metrics)
- [The 5-Star Lie: You’re Doing AI Evaluations Wrong](https://www.decodingai.com/p/the-5-star-lie-you-are-doing-ai-evals)
- [Escaping POC Purgatory: Evaluation-Driven Development for AI Systems](https://www.decodingai.com/p/escaping-poc-purgatory-evaluation)
- [Stop Launching AI Apps Without This Framework](https://www.decodingai.com/p/stop-launching-ai-apps-without-this)

## Other Sources

- [Evaluating NLP Models: A Comprehensive Guide to ROUGE, BLEU, METEOR, and BERTScore Metrics](https://plainenglish.io/blog/evaluating-nlp-models-a-comprehensive-guide-to-rouge-bleu-meteor-and-bertscore-metrics-d0f1b1)
- [Key NLP Evaluation Metrics](https://datumo.com/en/blog/insight/key-nlp-evaluation-metrics/)
- [BERTScore explained: A modern metric for evaluating text generation](https://spotintelligence.com/2024/08/20/bertscore/)

