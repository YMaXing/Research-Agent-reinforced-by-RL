# Methods and Strategies for Building and Refining Reasoning Models

Reasoning models are the key LLM specialization trend for 2025. This evolution extends beyond patterns we already know, such as Retrieval-Augmented Generation (RAG) and domain-specific fine-tuning. Instead of just injecting knowledge, reasoning specialization targets the emergence of robust, multi-step logical capabilities, allowing models to *think* rather than just *know*. This focus on the process of deduction enables them to tackle complex tasks like mathematical proofs, logical puzzles, and competitive programming that were previously out of reach.![Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.](https://substackcdn.com/image/fetch/$s_!QwUc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png)

Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

This specialization does not replace general-purpose LLMs for everyday generation, summarization, or simple question-answering. However, these powerful reasoning abilities come with drawbacks. The gains are often accompanied by increased inference latency and cost due to longer, more detailed outputs. There is also a risk of "overthinking" on trivial tasks, where a model might introduce unnecessary complications. Specialization is not free; improving capability in one area can sometimes degrade fluency or efficiency in others.

In this article, we will:

1.  Explain the meaning of "reasoning model"
2.  Discuss the advantages and disadvantages of reasoning models
3.  Outline the methodology behind DeepSeek R1
4.  Describe the four main approaches to building and improving reasoning models
5.  Share thoughts on the LLM landscape following the DeepSeek V3 and R1 releases
6.  Provide tips for developing reasoning models on a tight budget

Having set the context and roadmap, we will now establish a working definition of "reasoning model" that you can use to evaluate future systems and research.

## How do we define "reasoning model"?

A reasoning model is an LLM designed to solve multi-step problems by generating intermediate thoughts. This process can be explicit, appearing as a visible chain of thought, or it can happen internally as hidden iterations. This contrasts with standard LLMs that often rely on direct factual recall or single-pass pattern matching for simpler prompts. For example, a basic question like "How far does a train go at 60 mph for 3 hours?" can be answered directly, while a more complex problem benefits from breaking it down into smaller, logical steps.![Figure 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.)](https://substackcdn.com/image/fetch/$s_!8oZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png)

Figure 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.) (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

The spectrum of reasoning is broad. All modern LLMs exhibit some basic reasoning, which can be improved with techniques like Chain-of-Thought (CoT) prompting [[25]](https://arxiv.org/abs/2205.11916). This step-by-step approach is not entirely new; it has roots in classic symbolic AI, which relied on structured, rule-based systems for logical deduction. Modern CoT prompting can be seen as an evolution of these ideas, where the LLM acts as a flexible symbolic reasoner, generating intermediate steps that mimic a logical proof or calculation [[101]](https://www.mdpi.com/2227-7390/13/11/1707), [[102]](https://www.youtube.com/watch?v=yo8HtAbUynA). However, specialized reasoning models are engineered for excellence on difficult benchmarks, such as math olympiad problems, formal proofs, or novel puzzles.

The intermediate steps in these models manifest in two primary ways. The first is through **visible thought traces**, where the model outputs a step-by-step reasoning process that the user can read and follow. This enhances transparency and allows for easier debugging. The second is through **invisible internal iterations**, like those rumored to be used in OpenAI's o1 model. In this approach, the model allocates more computation time at inference to "think" internally without necessarily exposing every step to the user. This can improve performance on complex tasks while presenting a clean, final answer, though it sacrifices the interpretability of a visible thought process.![Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user.](https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png)

Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.

## When should we use reasoning models?

Before diving into the technical details, it is important to know when to use a reasoning model. They deliver the highest returns on tasks that require decomposition, self-correction, or complex logic, such as puzzles, advanced mathematics, and competitive coding. For tasks like summarization, simple factual question-answering, or creative writing, a general-purpose model is often sufficient and more efficient.

The power of reasoning models comes with practical downsides. Their verbose, intermediate steps lead to higher latency and token costs. This can frustrate users in conversational settings who expect quick answers. There is also the risk of overthinking, where the model might invent unnecessary complications for a straightforward problem that a base model would have solved correctly in a single pass [[31]](https://arxiv.org/abs/2501.18585). This trade-off between capability and efficiency is a central challenge in applying these models effectively.![Figure 4: The key strengths and weaknesses of reasoning models.](https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png)

Figure 4: The key strengths and weaknesses of reasoning models.

Understanding when to deploy these specialized models is key. This leads us to a concrete, open pipeline that demonstrates how such capabilities are created at scale: the DeepSeek-R1 series.

## A brief look at the DeepSeek training pipeline

The DeepSeek-R1 paper introduces three model variants that illustrate different approaches to building reasoning capabilities [[23]](https://www.nature.com/articles/s41586-025-09422-z). Understanding their relationships provides a clear map of the current landscape.![Figure 5: Development process of DeepSeeks three different reasoning models that are discussed in the DeepSeek R1 technical report.](https://substackcdn.com/image/fetch/$s_!z-dr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png)

Figure 5: Development process of DeepSeeks three different reasoning models that are discussed in the DeepSeek R1 technical report. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

First is **DeepSeek-R1-Zero**, a model created using a "cold-start" pure Reinforcement Learning (RL) process directly from the DeepSeek-V3 base model. This approach skips the conventional Supervised Fine-Tuning (SFT) stage that typically precedes RL. The idea is that by not pre-exposing the model to human-annotated reasoning paths, it can discover more novel and potentially more effective problem-solving strategies on its own. This requires strong, verifiable reward signals, such as checking the final answer in a math problem, to guide the model's learning [[4]](https://thelmbook.com/articles#!./DeepSeek-R1.md).

Next is **DeepSeek-R1**, the flagship reasoning model. It builds upon the insights from R1-Zero but follows a more refined, multi-stage training process. This pipeline starts with a small amount of "cold-start" SFT data to give the model a better initial grasp of generating readable, human-aligned thought processes. This is followed by large-scale RL and further SFT stages to enhance both reasoning and general abilities, making it more stable and user-friendly than the raw R1-Zero [[2]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

Finally, we have the **DeepSeek-R1-Distill** models. These are smaller, more efficient models that inherit the reasoning capabilities of the large R1 model. This process is not classical knowledge distillation, where a student model mimics the teacher's output probabilities (logits). Instead, it is a form of SFT where smaller open-source models (like Llama and Qwen) are fine-tuned on a large dataset of 800,000 high-quality reasoning traces generated by DeepSeek-R1 [[11]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d), [[14]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond).

The DeepSeek pipeline incorporates all four main techniques for building reasoning models. We will now examine each of these in depth to compare their mechanisms and outcomes.

## The 4 main ways to build and improve reasoning models

There are four key techniques currently used to build and enhance reasoning in LLMs. While the exact workings of advanced models like OpenAI's o1 and o3 remain undisclosed, they are rumored to combine several of these training and inference-time methods.

### Inference-time scaling

Inference-time scaling refers to dedicating more computational resources during inference to improve a model's output. The analogy is simple: just as a human can produce a better answer when given more time to think, an LLM can improve its performance on complex tasks with additional "thinking time." This is also known as test-time compute scaling [[30]](https://arxiv.org/abs/2408.03314).

One of the most common methods is **Chain-of-Thought (CoT) prompting**. By simply adding a phrase like "Let's think step by step" to the prompt, the model is encouraged to break down a problem into intermediate steps, which often leads to a more accurate final answer [[25]](https://arxiv.org/abs/2205.11916).![Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper.](https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png)

Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper [[25]](https://arxiv.org/abs/2205.11916).

More advanced techniques involve search strategies. **Best-of-N** or **majority voting** involves generating multiple responses and selecting the best one, either with a verifier model or by picking the most common answer. Other methods like **beam search** and **Monte Carlo Tree Search (MCTS)** explore a tree of possible reasoning steps, using a **Process Reward Model (PRM)** to score each intermediate step and guide the search toward the most promising path [[26]](https://arxiv.org/abs/2410.18982). A key distinction exists between Process Reward Models (PRMs) and the more common Outcome Reward Models (ORMs). While ORMs evaluate only the final answer, providing a single, coarse-grained signal, PRMs assess each intermediate step in the reasoning chain. This step-level feedback allows for finer credit assignment and can guide search more effectively, though it requires more complex and expensive data collection [[103]](https://arxiv.org/html/2510.08049v3).![Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer.](https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png)

Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

Interestingly, the DeepSeek-R1 paper categorizes PRMs and MCTS under "unsuccessful attempts," stating that the computational overhead they introduce during large-scale RL outweighs their benefits in their experiments [[23]](https://www.nature.com/articles/s41586-025-09422-z). This does not mean these methods are useless. It suggests that for their specific training setup, the trade-off was not favorable. DeepSeek may still use these techniques at the application layer, even if they were not part of the core training loop.

This brings us to the high cost of some reasoning models. OpenAI's o1 models, for instance, are more expensive than GPT-4o [[38]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison). The o1 model costs $60 per million output tokens, compared to $10 for GPT-4o. This price difference is likely due to the heavy inference-time compute o1 uses to "think" longer, a strategy that can lead to "overthinking." This involves expending excessive computation on simple problems [[41]](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o), [[30]](https://arxiv.org/abs/2408.03314).

### Pure reinforcement learning (RL)

The second approach is pure RL, best exemplified by DeepSeek-R1-Zero. Unlike typical RL pipelines that start with a model already fine-tuned on human examples (SFT), pure RL is applied directly to the base model. This "cold-start" approach is designed to let the model discover reasoning paths on its own, without being biased by human-provided demonstrations [[4]](https://thelmbook.com/articles#!./DeepSeek-R1.md).![Figure 8: The development process of DeepSeek-R1-Zero model.](https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png)

Figure 8: The development process of DeepSeek-R1-Zero model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

This process relies on a reward system that does not require a separate reward model trained on human preferences. Instead, it uses rule-based rewards. The DeepSeek-R1 paper details two main types [[23]](https://www.nature.com/articles/s41586-025-09422-z):

1.  **Accuracy rewards:** These are given if the model's final answer is correct. For math problems, this can be checked by comparing the final number. For code, it can be verified by running unit tests.
2.  **Format rewards:** These incentivize the model to follow a specific structure, such as enclosing its reasoning process within `<think>` and `</think>` tags. This makes the output more interpretable and stable.

One of the most interesting outcomes of this pure RL training was the emergence of an **"Aha moment."** The DeepSeek paper describes a point in training where the model spontaneously started generating long, reflective reasoning traces. It began using phrases like "Wait, wait. Wait. That's an aha moment" before re-evaluating its approach. This demonstrated that complex behaviors like self-correction can emerge from a simple, outcome-based reward signal without being explicitly taught [[23]](https://www.nature.com/articles/s41586-025-09422-z).![Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment.](https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png)

Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment [[23]](https://www.nature.com/articles/s41586-025-09422-z).

However, a growing body of research suggests this "Aha moment" is not created by RL but is instead an amplification of a latent capability. Studies show that self-reflection and self-correction behaviors emerge during pre-training, likely from exposure to extensive chain-of-thought data [[104]](https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training). One analysis found that while a fine-tuned model exhibited self-reflection nearly 100% of the time, its pretrained base model already did so spontaneously, just far less frequently [[105]](https://arxiv.org/html/2506.12217v1). The pre-training data mixture is therefore a critical, though undisclosed, factor in the stability of cold-start RL [[106]](https://www.youtube.com/watch?v=SD5raqvYG-0). Regardless, R1-Zero was the first open model to show that it is possible to develop strong reasoning capabilities through pure RL.

### Supervised finetuning and reinforcement learning (SFT + RL)

The third method is a hybrid approach that combines SFT with RL, as seen in the main DeepSeek-R1 model. This multi-stage process is designed to create a model that is not only a strong reasoner but also more stable, readable, and aligned with human preferences than a pure RL model like R1-Zero.![Figure 10: The development process of DeepSeek-R1 model.](https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png)

Figure 10: The development process of DeepSeek-R1 model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

The pipeline begins with a "cold-start" SFT stage, where the base model is fine-tuned on a few thousand examples of human-aligned reasoning traces. This initial step improves the readability of the model's output and prepares it for the more intensive RL phase [[2]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

Next, the model undergoes large-scale RL training, similar to R1-Zero, using verifiable rewards. The use of verifiable rewards is where PRMs become powerful in an RL context. Instead of relying on a sparse, final-outcome signal, a PRM provides dense, step-by-step rewards. This fine-grained feedback helps stabilize RL training, offers more precise credit assignment for long chains of thought, and allows the policy to learn more efficiently [[103]](https://arxiv.org/html/2510.08049v3). An additional reward is introduced: a **language consistency reward**. This was added to address the issue of "language mixing," where R1-Zero would sometimes switch between English and Chinese mid-thought. This reward penalizes outputs that do not match the language of the input query, improving user experience even at the cost of a slight dip in raw task performance [[27]](https://www.nature.com/articles/s41586-025-09422-z).

The process then iterates through more SFT and RL stages. Rejection sampling is used to generate a large dataset of high-quality completions for both reasoning and general chat problems, which are then used for SFT. A final RL stage mixes verifiable rewards for reasoning tasks with preference-based rewards (from a trained reward model) for general helpfulness and harmlessness. This staged refinement results in a powerful, well-rounded model that excels on reasoning benchmarks while being a capable general-purpose assistant [[23]](https://www.nature.com/articles/s41586-025-09422-z).

On benchmarks, DeepSeek-R1 is highly competitive with OpenAI's o1 models, often matching or exceeding their performance in math and code, demonstrating the success of this hybrid approach.![Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models.](https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png)

Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

### Pure supervised finetuning (SFT) and distillation

To recap, inference-time scaling improves reasoning without changing the model, pure RL allows the model to discover reasoning on its own, and the SFT+RL hybrid refines this emergent behavior for production. The final approach, pure SFT and distillation, focuses on efficiently transferring these hard-won reasoning capabilities to smaller, more accessible models.

As we discussed, DeepSeek's distillation process is a form of SFT. Instead of traditional distillation that matches logits, they fine-tune smaller open-source models (like Qwen and Llama) on a large dataset of 800,000 high-quality reasoning traces generated by the powerful DeepSeek-R1 model. This process does not include an additional RL stage [[14]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond).![Figure 12: The development process of DeepSeek-R1-Distill models.](https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png)

Figure 12: The development process of DeepSeek-R1-Distill models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

DeepSeek created these distilled models for two main reasons. First, the 671B parameter R1 model is massive and requires considerable computational resources to run, making it inaccessible for many users and applications. Distillation makes its powerful reasoning accessible on consumer-grade hardware. Second, it provides a valuable resource for the research community to study the mechanisms of long-CoT reasoning models without needing access to the large model itself [[11]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d).

The results are impressive. The distilled models outperform their original instruction-tuned counterparts and even strong closed-source models like GPT-4o on reasoning benchmarks. For example, the 1.5B distilled Qwen model surpasses non-reasoning baselines on mathematical tasks, a remarkable achievement for a model of its size [[23]](https://www.nature.com/articles/s41586-025-09422-z).![Figure 13: Benchmark comparison of distilled versus non-distilled models.](https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png)

Figure 13: Benchmark comparison of distilled versus non-distilled models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

This raises a key question: is distillation more effective than pure RL for smaller models? The DeepSeek-R1 paper provides an answer by comparing a 32B distilled model to a 32B model trained with pure RL (Qwen2.5-32B-Zero). The distilled model outperformed the pure RL model across all benchmarks [[23]](https://www.nature.com/articles/s41586-025-09422-z).![Figure 14: Benchmark comparison distillation and RL on a smaller 32B model.](https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png)

Figure 14: Benchmark comparison distillation and RL on a smaller 32B model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

This suggests two insights. First, for smaller models, distillation is a more economical and effective way to impart reasoning abilities than large-scale RL from scratch. Second, pushing the frontiers of AI intelligence likely still requires the massive scale of models like R1 to discover novel reasoning patterns, which can then be transferred to smaller models. The table above would have been more insightful if it also included a comparison to a non-reasoning base model and a model trained with SFT on human-generated data, to better isolate the impact of distillation.

After dissecting these four techniques and seeing them embodied in DeepSeek-R1, we can step back to evaluate the release's broader significance.

## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 series is a major moment for AI engineering. We appreciate not only the models themselves but also the open MIT license and the unusually detailed technical report that accompanied them. This level of transparency is rare and provides an invaluable blueprint for the community. The paper's demonstration that pure RL from a cold start can produce emergent reasoning and self-correction is a powerful proof of concept.

When comparing DeepSeek-R1 head-to-head with OpenAI's o1, the benchmarks show comparable quality on math and coding tasks. However, R1 appears to have superior inference efficiency, with API prices around 30 times lower than o1's [[2]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1). This suggests different philosophical bets: DeepSeek invested heavily in a more efficient, training-intensive architecture, while o1 seems to lean more on expensive inference-time scaling to achieve its results.

However, any direct comparison is limited because OpenAI has disclosed very little about o1. We do not know its size, whether it uses a Mixture-of-Experts (MoE) architecture like DeepSeek, or the exact mix of training techniques. Without this information, attributing performance gaps is difficult, and a direct comparison is not entirely warranted.

There is also ambiguity around the training cost. The widely cited $6M figure for DeepSeek likely refers to the pre-training of the V3 base model, not the full R1 reasoning specialization [[43]](https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1). The DeepSeek team has never disclosed the exact total GPU hours or full development cost for R1. While their paper provides some figures for specific training phases, these numbers exclude the extensive experimentation, data curation, and human annotation required, leaving the true incremental cost of reasoning specialization undisclosed [[23]](https://www.nature.com/articles/s41586-025-09422-z).

Despite these questions, DeepSeek-R1 stands as a milestone. It proves that high-level reasoning capabilities need not be the exclusive domain of closed labs. By providing both powerful models and a detailed recipe, DeepSeek has accelerated open research into all four of the core reasoning techniques we have discussed.

## Developing reasoning models on a limited budget

The development costs for frontier reasoning models are substantial, even when starting from an open-weight base model. This can be discouraging for researchers and engineers with limited budgets. Fortunately, recent projects have demonstrated effective, budget-conscious methods for developing reasoning capabilities.

One practical approach is **distillation**, as shown by the **Sky-T1** project from UC Berkeley’s Sky Computing Lab. The team created Sky-T1-32B-Preview, a reasoning model competitive with early versions of o1, by fine-tuning on just 17,000 carefully curated samples. The entire training process cost under $450 [[17]](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450). This illustrates how the distillation concept we covered earlier can be scaled down effectively.

Table 1: Benchmark results for the Sky-T1 model compared to an early version of OpenAI's o1.

| Model | AIME | MATH500 | LiveCodeBench |
| :--- | :--- | :--- | :--- |
| o1-preview | 50.0 | 93.0 | 57.6 |
| Sky-T1-32B-Preview | 50.0 | 92.2 | 59.6 |

Another method is **pure RL at a smaller scale**. The **TinyZero** project successfully reproduced DeepSeek-R1-Zero's emergent behaviors on a 3B parameter model for under $30. The model was trained on countdown and multiplication tasks and learned self-verification and search abilities on its own [[20]](https://github.com/Jiayi-Pan/TinyZero). This reinforces the finding that cold-start RL can produce useful reasoning behaviors even without massive compute.

Table 2: Key details of the TinyZero project, demonstrating budget-friendly pure RL.

| Aspect | Detail |
| :--- | :--- |
| Model Size | 3B parameters |
| Training Cost | < $30 |
| Key Capability | Emergent self-verification and search |
| Example Task | Countdown number game |

A third, and perhaps most innovative, budget-friendly technique is **journey learning**. This concept, introduced in the "O1 Replication Journey" paper, contrasts with traditional "shortcut learning," where models are only trained on correct, optimal solutions. In journey learning, the training data includes the entire problem-solving process: incorrect paths, self-corrections, and reflections, culminating in the final success [[26]](https://arxiv.org/abs/2410.18982).

Table 3: Performance comparison of Journey Learning vs. Shortcut Learning on the MATH500 test set.

| Base Model | SFT-phase1 (Shortcut) | SFT-phase2 (Shortcut) | SFT-phase2 (Journey) |
| :--- | :--- | :--- | :--- |
| deepseek-sft-abel | 0.372 | 0.386 | 0.470 |
| deepseek-sft-prm800k | 0.290 | 0.348 | 0.428 |

By exposing the model to mistakes during SFT, we reinforce the self-correction mechanisms that are crucial for robust reasoning. A model trained only on "golden paths" can be brittle; when it encounters a novel error, it does not know how to recover. In contrast, a model trained on journey-style data has learned to recognize and navigate failures. The "O1 Replication Journey" paper showed that with only 327 training samples, journey learning outperformed shortcut learning by over 8% on the MATH dataset, demonstrating its powerful potential [[26]](https://arxiv.org/abs/2410.18982).

While powerful, journey learning is not without its failure modes. If the training data is dominated by incorrect paths, the model can learn to persistently generate wrong answers or get stuck in unstable convergence loops. A key challenge is balancing the ratio of error paths to "golden paths" to teach self-correction without reinforcing bad habits [[107]](https://arxiv.org/html/2510.01624v1), [[108]](https://arxiv.org/html/2604.10079v2).

Looking ahead, the most effective budget-conscious pipelines will likely be hybrids. We can combine insights from these projects: using distillation like Sky-T1 for efficient knowledge transfer, applying small-scale pure RL like TinyZero to encourage emergent behaviors, and incorporating journey learning to build robust self-correction capabilities. This allows for a balance between cost, performance, and reliability.

## Conclusion

We have explored the four primary approaches to building reasoning models. **Inference-time scaling** offers improved performance with no training cost but comes at a high serving cost, making it a flexible but expensive tool. **Pure RL** is a powerful research method that can unlock emergent behaviors like self-correction from a cold start, revealing the latent potential within base models. The **SFT+RL hybrid** provides a production-ready blueprint, refining these emergent abilities with supervised data and verifiable rewards to achieve stability and peak performance. Finally, **distillation** offers an efficient way to transfer these hard-won capabilities to smaller, more accessible models, though the resulting models are ultimately derivative of their larger teacher.

We forecast a hybrid future where the most capable systems will combine these techniques. The production pipeline will likely involve a robust SFT+RL process to build a strong base model, which is then further enhanced with adaptive inference-time scaling at deployment. This is the pattern we suspect underlies OpenAI's o1 and will likely define future o3-class models. This combination allows for a powerful, efficient, and adaptable system that can handle a wide range of tasks.

For AI engineers, the key is to move beyond the default of using the largest proprietary model for every task. The choice of technique should be a strategic one, matched to concrete constraints like budget, performance targets, and latency. By using the decision heuristic and task-complexity framework we introduced, you can make informed choices. This strategic thinking is already being applied in domains like finance, where reasoning models act as algorithmic trading agents [[109]](https://arxiv.org/html/2504.10789v1), and in robotics, where techniques like Embodied Chain-of-Thought (ECoT) guide autonomous systems in complex, real-world tasks [[110]](https://www.mdpi.com/2673-2688/6/7/158), [[111]](https://venturebeat.com/business/researchers-develop-technique-to-give-robots-embodied-reasoning-abilities). By understanding these trade-offs, you can architect systems that are not only powerful but also practical and efficient.

## References

- [1] https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners
- [2] https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1
- [3] https://www.vellum.ai/blog/the-training-of-deepseek-r1-and-ways-to-use-it
- [4] https://thelmbook.com/articles#!./DeepSeek-R1.md
- [5] https://huggingface.co/blog/open-r1/mini-r1-contdown-game
- [6] https://www.philschmid.de/mini-deepseek-r1
- [7] https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners
- [8] https://arxiv.org/html/2503.20783v1
- [9] https://github.com/sail-sg/oat-zero
- [10] https://arxiv.org/abs/2402.03300
- [11] https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d
- [12] https://medium.com/@tahirbalarabe2/deepseek-r1-explained-chain-of-thought-reinforcement-learning-and-model-distillation-0eb165d928c9
- [13] https://redwerk.com/blog/what-is-model-distillation
- [14] https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond
- [15] https://www.linkedin.com/posts/muhammad-ali-masood-phd_researchers-open-source-sky-t1-a-reasoning-activity-7285536292493299712-M8b5
- [16] https://ivan.vlaevski.com/ai-models-go-cheaper-novasky-t1-sets-a-new-standard
- [17] https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450
- [18] https://www.technology.org/2025/01/14/sky-t1-open-source-ai-model-for-advanced-reasoning-you-can-train-for-less-than-450
- [19] https://campustechnology.com/articles/2025/01/15/uc-berkeley-announces-sky-t1-32b-open-source-ai-model.aspx?s=ct_in_070225
- [20] https://github.com/Jiayi-Pan/TinyZero
- [21] https://www.dailycal.org/news/campus/research-and-ideas/campus-researchers-replicate-disruptive-chinese-ai-for-30/article_a1cc5cd0-dee4-11ef-b8ca-171526dfb895.html
- [22] https://thelmbook.com/articles#!./DeepSeek-R1.md
- [23] https://www.nature.com/articles/s41586-025-09422-z
- [24] https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1
- [25] https://arxiv.org/abs/2205.11916
- [26] https://arxiv.org/abs/2410.18982
- [27] https://artgor.medium.com/paper-review-deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement-learning-edf4343dcf3a
- [28] https://transitions.substack.com/p/the-laymans-introduction-to-deepseek
- [29] https://www.nature.com/articles/s41586-025-09422-z
- [30] https://arxiv.org/abs/2408.03314
- [31] https://arxiv.org/abs/2501.18585
- [32] https://ojs.aaai.org/index.php/AAAI/article/view/40797/44758
- [33] https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling
- [34] https://medium.com/@techsachin/breaking-the-llm-bottleneck-genprms-approach-to-scale-test-time-compute-via-generative-reasoning-0e90e3ffa734
- [35] https://huggingface.co/papers?q=Process+Reward+Models+%28PRMs%29
- [36] https://github.com/RyanLiu112/GenPRM
- [37] https://www.uctoday.com/unified-communications/chatgpt-4o-vs-o1-which-openai-model-is-best
- [38] https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison
- [39] https://openai.com/api/pricing/
- [40] https://francpetracci.medium.com/openai-gpt-o1-api-pricing-a-comprehensive-guide-b93fdaed217c
- [41] https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o
- [42] https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18
- [43] https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1
- [44] https://www.yahoo.com/news/research-exposes-deepseek-ai-training-165025904.html
- [45] https://openai.com/index/learning-to-reason-with-llms/
- [46] https://prompt.16x.engineer/blog/deepseek-r1-cost-pricing-speed
- [47] https://www.interconnects.ai/t/open-source
- [48] https://www.interconnects.ai/p/tulu-3
- [49] https://www.interconnects.ai/p/understanding-reasoning-llms
- [50] https://github.com/MoonshotAI/Kimi-k1.5/blob/main/Kimi_k1.5.pdf
- [51] https://arxiv.org/abs/2501.19393
- [52] https://arxiv.org/abs/2501.12895
- [53] https://arxiv.org/abs/2501.18841
- [54] https://arxiv.org/abs/2502.02390
- [55] https://arxiv.org/abs/2502.0440
- [56] https://arxiv.org/abs/2502.05171
- [57] https://arxiv.org/abs/2502.06703
- [58] https://www.arxiv.org/abs/2502.15771
- [59] https://www.arxiv.org/abs/2502.12521
- [60] https://arxiv.org/abs/2502.13842
- [61] https://arxiv.org/abs/2502.14382
- [62] https://arxiv.org/abs/2502.18600
- [63] https://arxiv.org/abs/2503.04378
- [64] https://www.anthropic.com/news/claude-3-7-sonnet
- [65] https://x.ai/blog/grok-3
- [66] https://www.ibm.com/new/announcements/ibm-granite-3-2-open-source-reasoning-and-vision
- [67] https://gair-nlp.github.io/walnut-plan
- [68] https://openai.com/index/learning-to-reason-with-llms/
- [69] https://github.com/GAIR-NLP/O1-Journey
- [70] https://streamlit.io/
- [71] https://www.interconnects.ai/i/154176259/deepseeks-learning-efficiency
- [72] https://github.com/allenai/open-instruct
- [73] https://x.com/rosstaylor90/status/1881372810485899716
- [74] https://x.com/srush_nlp/status/1881383080528924868
- [75] https://rlhfbook.com/c/10-rejection-sampling.html
- [76] https://www.interconnects.ai/p/openais-reinforcement-finetuning
- [77] https://rlhfbook.com/c/11-policy-gradients.html#group-relative-policy-optimization
- [78] https://arxiv.org/abs/2411.15124
- [79] https://x.com/sea_snell/status/1881453551974805684
- [80] https://huggingface.co/datasets/allenai/dolmino-mix-1124
- [81] https://apps.apple.com/us/app/deepseek-ai-assistant/id6737597349
- [82] https://chat.deepseek.com/
- [83] https://github.com/deepseek-ai/DeepSeek-R1/blob/main/DeepSeek_R1.pdf
- [84] https://huggingface.co/deepseek-ai/DeepSeek-R1-Zero
- [85] https://huggingface.co/deepseek-ai/DeepSeek-R1
- [86] https://x.com/TheXeophon/status/1881443117787984265
- [87] https://www.latent.space/i/140396949/mixtral-sparks-a-gpuinference-race-to-the-bottom
- [88] https://api-docs.deepseek.com/quick_start/pricing
- [89] https://www.interconnects.ai/p/openais-o1-using-search-was-a-psyop
- [90] https://x.com/TheDavidSJ/status/1885075972057108508
- [91] https://arxiv.org/abs/2405.04434
- [92] https://huggingface.co/deepseek-ai/DeepSeek-R1/blob/main/config.json
- [93] https://epoch.ai/gradient-updates/moe-vs-dense-models-inference
- [94] https://epoch.ai/gradient-updates/how-has-deepseek-improved-the-transformer-architecture
- [95] https://github.com/huggingface/Math-Verify
- [96] https://github.com/sail-sg/understand-r1-zero?tab=readme-ov-file#training
- [97] https://github.com/sail-sg/oat
- [98] https://oatllm.notion.site/oat-zero
- [99] https://huggingface.co/HuggingFaceTB/FineMath-Llama-3B
- [100] https://github.com/Open-Reasoner-Zero/Open-Reasoner-Zero
- [101] https://www.mdpi.com/2227-7390/13/11/1707
- [102] https://www.youtube.com/watch?v=yo8HtAbUynA
- [103] https://arxiv.org/html/2510.08049v3
- [104] https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training
- [105] https://arxiv.org/html/2506.12217v1
- [106] https://www.youtube.com/watch?v=SD5raqvYG-0
- [107] https://arxiv.org/html/2510.01624v1
- [108] https://arxiv.org/html/2604.10079v2
- [109] https://arxiv.org/html/2504.10789v1
- [110] https://www.mdpi.com/2673-2688/6/7/158
- [111] https://venturebeat.com/business/researchers-develop-technique-to-give-robots-embodied-reasoning-abilities