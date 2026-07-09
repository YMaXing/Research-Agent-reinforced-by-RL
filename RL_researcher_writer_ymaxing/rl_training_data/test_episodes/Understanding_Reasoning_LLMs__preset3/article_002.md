# Methods and Strategies for Building and Refining Reasoning Models

Reasoning models are the key LLM specialization trend for 2025. This evolution extends beyond patterns we already know, such as Retrieval-Augmented Generation (RAG) and domain-specific fine-tuning. Instead of just injecting knowledge, reasoning specialization targets the emergence of robust, multi-step logical capabilities, allowing models to *think* rather than just *know*. This focus on the process of deduction enables them to tackle complex tasks like mathematical proofs, logical puzzles, and competitive programming that were previously out of reach.![Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.](https://substackcdn.com/image/fetch/$s_!QwUc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png)

Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

This specialization does not replace general-purpose LLMs for everyday generation, summarization, or simple question-answering. However, these powerful reasoning abilities come with drawbacks. The gains are often accompanied by increased inference latency and cost due to longer, more detailed outputs. There is also a risk of "overthinking" on trivial tasks, where a model might introduce unnecessary complications that a base model would solve correctly in one pass. Specialization is not free; improving capability in one area can sometimes degrade fluency or efficiency in others. This trade-off means that while a reasoning model might excel at a complex calculus problem, it could be slower and more expensive for a simple summarization task, making the choice of model critical for production systems.

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

The spectrum of reasoning is broad. All modern LLMs exhibit some basic reasoning, which can be improved with techniques like Chain-of-Thought (CoT) prompting [[1]](https://arxiv.org/abs/2205.11916). This step-by-step approach is not entirely new; it has roots in classic symbolic AI, which relied on structured, rule-based systems for logical deduction. Modern CoT prompting can be seen as an evolution of these ideas, where the LLM acts as a flexible symbolic reasoner, generating intermediate steps that mimic a logical proof or calculation [[2]](https://www.mdpi.com/2227-7390/13/11/1707), [[3]](https://www.youtube.com/watch?v=yo8HtAbUynA). However, specialized reasoning models are engineered for excellence on difficult benchmarks, such as math olympiad problems, formal proofs, or novel puzzles.

The intermediate steps in these models manifest in two primary ways. The first is through **visible thought traces**, where the model outputs a step-by-step reasoning process that the user can read and follow. This enhances transparency and allows for easier debugging. The second is through **invisible internal iterations**, like those rumored to be used in OpenAI's o1 model. In this approach, the model allocates more computation time at inference to "think" internally without necessarily exposing every step to the user. This can improve performance on complex tasks while presenting a clean, final answer, though it sacrifices the interpretability of a visible thought process.![Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user.](https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png)

Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.

## When should we use reasoning models?

Before diving into the technical details, it is important to know when to use a reasoning model. They deliver the highest returns on tasks that require decomposition, self-correction, or complex logic, such as puzzles, advanced mathematics, and competitive coding. For tasks like summarization, simple factual question-answering, or creative writing, a general-purpose model is often sufficient and more efficient.

The power of reasoning models comes with practical downsides. Their verbose, intermediate steps lead to higher latency and token costs. This can frustrate users in conversational settings who expect quick answers. There is also the risk of overthinking, where the model might invent unnecessary complications for a straightforward problem that a base model would have solved correctly in a single pass [[4]](https://arxiv.org/abs/2501.18585). This trade-off between capability and efficiency is a central challenge in applying these models effectively.![Figure 4: The key strengths and weaknesses of reasoning models.](https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png)

Figure 4: The key strengths and weaknesses of reasoning models.

Understanding when to deploy these specialized models is key. This leads us to a concrete, open pipeline that demonstrates how such capabilities are created at scale: the DeepSeek-R1 series.

## A brief look at the DeepSeek training pipeline

The DeepSeek-R1 paper introduces three model variants that illustrate different approaches to building reasoning capabilities [[5]](https://www.nature.com/articles/s41586-025-09422-z). Understanding their relationships provides a clear map of the current landscape.![Figure 5: Development process of DeepSeeks three different reasoning models that are discussed in the DeepSeek R1 technical report.](https://substackcdn.com/image/fetch/$s_!z-dr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png)

Figure 5: Development process of DeepSeeks three different reasoning models that are discussed in the DeepSeek R1 technical report. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

First is **DeepSeek-R1-Zero**, a model created using a "cold-start" pure Reinforcement Learning (RL) process directly from the DeepSeek-V3 base model. This approach skips the conventional Supervised Fine-Tuning (SFT) stage that typically precedes RL. The idea is that by not pre-exposing the model to human-annotated reasoning paths, it can discover more novel and potentially more effective problem-solving strategies on its own. This requires strong, verifiable reward signals, such as checking the final answer in a math problem, to guide the model's learning [[6]](https://thelmbook.com/articles#!./DeepSeek-R1.md).

Next is **DeepSeek-R1**, the flagship reasoning model. It builds upon the insights from R1-Zero but follows a more refined, multi-stage training process. This pipeline starts with a small amount of "cold-start" SFT data to give the model a better initial grasp of generating readable, human-aligned thought processes. This is followed by large-scale RL and further SFT stages to enhance both reasoning and general abilities, making it more stable and user-friendly than the raw R1-Zero [[7]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

Finally, we have the **DeepSeek-R1-Distill** models. These are smaller, more efficient models that inherit the reasoning capabilities of the large R1 model. This process is not classical knowledge distillation, where a student model mimics the teacher's output probabilities (logits). Instead, it is a form of SFT where smaller open-source models (like Llama and Qwen) are fine-tuned on a large dataset of 800,000 high-quality reasoning traces generated by DeepSeek-R1 [[8]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d), [[9]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond).

The DeepSeek pipeline incorporates all four main techniques for building reasoning models. We will now examine each of these in depth to compare their mechanisms and outcomes.

## The 4 main ways to build and improve reasoning models

There are four key techniques currently used to build and enhance reasoning in LLMs. While the exact workings of advanced models like OpenAI's o1 and o3 remain undisclosed, they are rumored to combine several of these training and inference-time methods.

### Inference-time scaling

Inference-time scaling refers to dedicating more computational resources during inference to improve a model's output. The analogy is simple: just as a human can produce a better answer when given more time to think, an LLM can improve its performance on complex tasks with additional "thinking time." This is also known as test-time compute scaling [[10]](https://arxiv.org/abs/2408.03314).

One of the most common methods is CoT prompting. By simply adding a phrase like "Let's think step by step" to the prompt, the model is encouraged to break down a problem into intermediate steps, which often leads to a more accurate final answer [[1]](https://arxiv.org/abs/2205.11916).![Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper.](https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png)

Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper [[1]](https://arxiv.org/abs/2205.11916).

More advanced techniques involve search strategies. **Best-of-N** or **majority voting** involves generating multiple responses and selecting the best one, either with a verifier model or by picking the most common answer. Other methods like **beam search** and **Monte Carlo Tree Search (MCTS)** explore a tree of possible reasoning steps, using a **Process Reward Model (PRM)** to score each intermediate step and guide the search toward the most promising path [[11]](https://arxiv.org/abs/2410.18982). A key distinction exists between PRMs and the more common Outcome Reward Models (ORMs). While ORMs evaluate only the final answer, providing a single, coarse-grained signal, PRMs assess each intermediate step in the reasoning chain. This step-level feedback allows for finer credit assignment and can guide search more effectively, though it requires more complex and expensive data collection [[12]](https://arxiv.org/html/2510.08049v3).![Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer.](https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png)

Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. (Source [LLM Test-Time Compute paper](https://arxiv.org/abs/2408.03314))

Interestingly, the DeepSeek-R1 paper categorizes PRMs and MCTS under "unsuccessful attempts," stating that the computational overhead they introduce during large-scale RL outweighs their benefits in their experiments [[5]](https://www.nature.com/articles/s41586-025-09422-z). This does not mean these methods are useless. It suggests that for their specific training setup, the trade-off was not favorable. DeepSeek may still use these techniques at the application layer, even if they were not part of the core training loop.

This brings us to the high cost of some reasoning models. OpenAI's o1 models, for instance, are more expensive than GPT-4o [[13]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison). The o1 model costs $60 per million output tokens, compared to $10 for GPT-4o. This price difference is likely due to the heavy inference-time compute o1 uses to "think" longer, a strategy that can lead to "overthinking." This involves expending excessive computation on simple problems [[14]](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o), [[10]](https://arxiv.org/abs/2408.03314).

### Pure reinforcement learning (RL)

The second approach is pure RL, best exemplified by DeepSeek-R1-Zero. Unlike typical RL pipelines that start with a model already fine-tuned on human examples (SFT), pure RL is applied directly to the base model. This "cold-start" approach is designed to let the model discover reasoning paths on its own, without being biased by human-provided demonstrations [[6]](https://thelmbook.com/articles#!./DeepSeek-R1.md).![Figure 8: The development process of DeepSeek-R1-Zero model.](https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png)

Figure 8: The development process of DeepSeek-R1-Zero model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

This process relies on a reward system that does not require a separate reward model trained on human preferences. Instead, it uses rule-based rewards. The DeepSeek-R1 paper details two main types [[5]](https://www.nature.com/articles/s41586-025-09422-z):

1.  **Accuracy rewards:** These are given if the model's final answer is correct. For math problems, this can be checked by comparing the final number. For code, it can be verified by running unit tests.
2.  **Format rewards:** These incentivize the model to follow a specific structure, such as enclosing its reasoning process within `<think>` and `</think>` tags. This makes the output more interpretable and stable.

One of the most interesting outcomes of this pure RL training was the emergence of an **"Aha moment."** The DeepSeek paper describes a point in training where the model spontaneously started generating long, reflective reasoning traces. It began using phrases like "Wait, wait. Wait. That's an aha moment" before re-evaluating its approach. This demonstrated that complex behaviors like self-correction can emerge from a simple, outcome-based reward signal without being explicitly taught [[5]](https://www.nature.com/articles/s41586-025-09422-z).![Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment.](https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png)

Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment [[5]](https://www.nature.com/articles/s41586-025-09422-z).

However, a growing body of research suggests this "Aha moment" is not created by RL but is instead an amplification of a latent capability. Studies show that self-reflection and self-correction behaviors emerge during pre-training, likely from exposure to extensive chain-of-thought data [[15]](https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training). One analysis found that while a fine-tuned model exhibited self-reflection nearly 100% of the time, its pretrained base model already did so spontaneously, just far less frequently [[16]](https://arxiv.org/html/2506.12217v1). The pre-training data mixture is therefore a critical, though undisclosed, factor in the stability of cold-start RL [[17]](https://www.youtube.com/watch?v=SD5raqvYG-0). Regardless, R1-Zero was the first open model to show that it is possible to develop strong reasoning capabilities through pure RL.

### Supervised finetuning and reinforcement learning (SFT + RL)

The third method is a hybrid approach that combines SFT with RL, as seen in the main DeepSeek-R1 model. This multi-stage process is designed to create a model that is not only a strong reasoner but also more stable, readable, and aligned with human preferences than a pure RL model like R1-Zero.![Figure 10: The development process of DeepSeek-R1 model.](https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png)

Figure 10: The development process of DeepSeek-R1 model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

The pipeline begins with a "cold-start" SFT stage, where the base model is fine-tuned on a few thousand examples of human-aligned reasoning traces. This initial step improves the readability of the model's output and prepares it for the more intensive RL phase [[7]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

Next, the model undergoes large-scale RL training, similar to R1-Zero, using verifiable rewards. The use of verifiable rewards is where PRMs become powerful in an RL context. Instead of relying on a sparse, final-outcome signal, a PRM provides dense, step-by-step rewards. This fine-grained feedback helps stabilize RL training, offers more precise credit assignment for long chains of thought, and allows the policy to learn more efficiently [[12]](https://arxiv.org/html/2510.08049v3). An additional reward is introduced: a **language consistency reward**. This was added to address the issue of "language mixing," where R1-Zero would sometimes switch between English and Chinese mid-thought. This reward penalizes outputs that do not match the language of the input query, improving user experience even at the cost of a slight dip in raw task performance [[5]](https://www.nature.com/articles/s41586-025-09422-z).

The process then iterates through more SFT and RL stages. Rejection sampling is used to generate a large dataset of high-quality completions for both reasoning and general chat problems, which are then used for SFT. A final RL stage mixes verifiable rewards for reasoning tasks with preference-based rewards (from a trained reward model) for general helpfulness and harmlessness. This staged refinement results in a powerful, well-rounded model that excels on reasoning benchmarks while being a capable general-purpose assistant [[5]](https://www.nature.com/articles/s41586-025-09422-z).

On benchmarks, DeepSeek-R1 is highly competitive with OpenAI's o1 models, often matching or exceeding their performance in math and code, demonstrating the success of this hybrid approach.![Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models.](https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png)

Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

### Pure supervised finetuning (SFT) and distillation

To recap, inference-time scaling improves reasoning without changing the model, pure RL allows the model to discover reasoning on its own, and the SFT+RL hybrid refines this emergent behavior for production. The final approach, pure SFT and distillation, focuses on efficiently transferring these hard-won reasoning capabilities to smaller, more accessible models.

As we discussed, DeepSeek's distillation process is a form of SFT. Instead of traditional distillation that matches logits, they fine-tune smaller open-source models (like Qwen and Llama) on a large dataset of 800,000 high-quality reasoning traces generated by the powerful DeepSeek-R1 model. This process does not include an additional RL stage [[9]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond).![Figure 12: The development process of DeepSeek-R1-Distill models.](https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png)

Figure 12: The development process of DeepSeek-R1-Distill models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

DeepSeek created these distilled models for two main reasons. First, the 671B parameter R1 model is massive and requires considerable computational resources to run, making it inaccessible for many users and applications. Distillation makes its powerful reasoning accessible on consumer-grade hardware. Second, it provides a valuable resource for the research community to study the mechanisms of long-CoT reasoning models without needing access to the large model itself [[8]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d).

The results are impressive. The distilled models outperform their original instruction-tuned counterparts and even strong closed-source models like GPT-4o on reasoning benchmarks. For example, the 1.5B distilled Qwen model surpasses non-reasoning baselines on mathematical tasks, a remarkable achievement for a model of its size [[5]](https://www.nature.com/articles/s41586-025-09422-z).![Figure 13: Benchmark comparison of distilled versus non-distilled models.](https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png)

Figure 13: Benchmark comparison of distilled versus non-distilled models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

This raises a key question: is distillation more effective than pure RL for smaller models? The DeepSeek-R1 paper provides an answer by comparing a 32B distilled model to a 32B model trained with pure RL (Qwen2.5-32B-Zero). The distilled model outperformed the pure RL model across all benchmarks [[5]](https://www.nature.com/articles/s41586-025-09422-z).![Figure 14: Benchmark comparison distillation and RL on a smaller 32B model.](https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png)

Figure 14: Benchmark comparison distillation and RL on a smaller 32B model. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

This suggests two insights. First, for smaller models, distillation is a more economical and effective way to impart reasoning abilities than large-scale RL from scratch. Second, pushing the frontiers of AI intelligence likely still requires the massive scale of models like R1 to discover novel reasoning patterns, which can then be transferred to smaller models. The table above would have been more insightful if it also included a comparison to a non-reasoning base model and a model trained with SFT on human-generated data, to better isolate the impact of distillation.

After dissecting these four techniques and seeing them embodied in DeepSeek-R1, we can step back to evaluate the release's broader significance.

## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 series is a major moment for AI engineering. We appreciate not only the models themselves but also the open MIT license and the unusually detailed technical report that accompanied them. This level of transparency is rare and provides an invaluable blueprint for the community. The paper's demonstration that pure RL from a cold start can produce emergent reasoning and self-correction is a powerful proof of concept.

When comparing DeepSeek-R1 head-to-head with OpenAI's o1, the benchmarks show comparable quality on math and coding tasks. However, R1 appears to have superior inference efficiency, with API prices around 30 times lower than o1's [[7]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1). This suggests different philosophical bets: DeepSeek invested heavily in a more efficient, training-intensive architecture, while o1 seems to lean more on expensive inference-time scaling to achieve its results.

However, any direct comparison is limited because OpenAI has disclosed very little about o1. We do not know its size, whether it uses a Mixture-of-Experts (MoE) architecture like DeepSeek, or the exact mix of training techniques. Without this information, attributing performance gaps is difficult, and a direct comparison is not entirely warranted.

There is also ambiguity around the training cost. The widely cited $6M figure for DeepSeek likely refers to the pre-training of the V3 base model, not the full R1 reasoning specialization [[18]](https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1). The DeepSeek team has never disclosed the exact total GPU hours or full development cost for R1. While their paper provides some figures for specific training phases, these numbers exclude the extensive experimentation, data curation, and human annotation required, leaving the true incremental cost of reasoning specialization undisclosed [[5]](https://www.nature.com/articles/s41586-025-09422-z).

Despite these questions, DeepSeek-R1 stands as a milestone. It proves that high-level reasoning capabilities need not be the exclusive domain of closed labs. By providing both powerful models and a detailed recipe, DeepSeek has accelerated open research into all four of the core reasoning techniques we have discussed.

## Developing reasoning models on a limited budget

The development costs for frontier reasoning models are substantial, even when starting from an open-weight base model. This can be discouraging for researchers and engineers with limited budgets. Fortunately, recent projects have demonstrated effective, budget-conscious methods for developing reasoning capabilities.

One practical approach is **distillation**, as shown by the **Sky-T1** project from UC Berkeley’s Sky Computing Lab. The team created Sky-T1-32B-Preview, a reasoning model competitive with early versions of o1, by fine-tuning on just 17,000 carefully curated samples. The entire training process cost under $450 [[19]](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450). This illustrates how the distillation concept we covered earlier can be scaled down effectively.![Figure 15: Figure from the "Sky-T1: Train your own O1 preview model within $450" article.](https://substackcdn.com/image/fetch/$s_!Y8HI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8865a313-2326-4f07-a6dc-72cc94cb2ebe_1364x570.png)

Figure 15: Figure from the "Sky-T1: Train your own O1 preview model within $450" article.

Another method is **pure RL at a smaller scale**. The **TinyZero** project successfully reproduced DeepSeek-R1-Zero's emergent behaviors on a 3B parameter model for under $30. The model was trained on countdown and multiplication tasks and learned self-verification and search abilities on its own [[20]](https://github.com/Jiayi-Pan/TinyZero). This reinforces the finding that cold-start RL can produce useful reasoning behaviors even without massive compute.![Figure 16: A figure from the TinyZero repository showing that the model is capable of self-verification.](https://substackcdn.com/image/fetch/$s_!Ykdn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6111f4b4-cfb9-494c-8390-ec251702914b_1600x955.png)

Figure 16: A figure from the TinyZero repository showing that the model is capable of self-verification.

A third, and perhaps most innovative, budget-friendly technique is **journey learning**. This concept, introduced in the "O1 Replication Journey" paper, contrasts with traditional "shortcut learning," where models are only trained on correct, optimal solutions. In journey learning, the training data includes the entire problem-solving process: incorrect paths, self-corrections, and reflections, culminating in the final success [[11]](https://arxiv.org/abs/2410.18982).![Figure 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solutions paths in the SFT data.](https://substackcdn.com/image/fetch/$s_!TxCO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0bfcd0-6d93-4c91-a0d6-28178839b7cf_1492x724.png)

Figure 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solutions paths in the SFT data. (Source [O1 Replication Journey: A Strategic Progress Report – Part 1](https://arxiv.org/abs/2410.18982))

By exposing the model to mistakes during SFT, we reinforce the self-correction mechanisms that are crucial for robust reasoning. A model trained only on "golden paths" can be brittle; when it encounters a novel error, it does not know how to recover. In contrast, a model trained on journey-style data has learned to recognize and navigate failures. The "O1 Replication Journey" paper showed that with only 327 training samples, journey learning outperformed shortcut learning by over 8% on the MATH dataset, demonstrating its powerful potential [[11]](https://arxiv.org/abs/2410.18982).

While powerful, journey learning is not without its failure modes. If the training data is dominated by incorrect paths, the model can learn to persistently generate wrong answers or get stuck in unstable convergence loops. A key challenge is balancing the ratio of error paths to "golden paths" to teach self-correction without reinforcing bad habits [[21]](https://arxiv.org/html/2510.01624v1), [[22]](https://arxiv.org/html/2604.10079v2).

Looking ahead, the most effective budget-conscious pipelines will likely be hybrids. We can combine insights from these projects: using distillation like Sky-T1 for efficient knowledge transfer, applying small-scale pure RL like TinyZero to encourage emergent behaviors, and incorporating journey learning to build robust self-correction capabilities. This allows for a balance between cost, performance, and reliability.

## Conclusion

We have explored the four primary approaches to building reasoning models, each with distinct trade-offs. **Inference-time scaling** offers a training-free way to boost performance but at a high serving cost, making it a flexible but expensive tool. **Pure RL** provides a powerful research pathway, unlocking emergent behaviors like self-correction from a cold start and revealing the latent potential within base models. The **SFT+RL hybrid** offers a production-ready blueprint, refining these emergent abilities with supervised data and verifiable rewards to achieve stability and peak performance. Finally, **distillation** presents an efficient method for transferring these hard-won capabilities to smaller, more accessible models, though the resulting models are ultimately derivative of their larger teacher.

We forecast a hybrid future where the most capable systems will combine these techniques. The production pipeline will likely involve a robust SFT+RL process to build a strong base model, which is then further enhanced with adaptive inference-time scaling at deployment. This is the pattern we suspect underlies OpenAI's o1 and will likely define future o3-class models. This combination allows for a powerful, efficient, and adaptable system that can handle a wide range of tasks. Looking further ahead, emerging research into quantum-classical hybrid architectures could reshape LLM reasoning. These approaches aim to use quantum circuits as targeted accelerators for computational bottlenecks in classical models, such as attention mechanisms or feature mapping, rather than replacing the entire architecture [[23]](https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.177004376.69666864), [[24]](https://arxiv.org/html/2504.08732v1). While still in early stages, this line of work points toward a future where specialized hardware could unlock new levels of efficiency and capability in reasoning systems.

For AI engineers, the key is to move beyond the default of using the largest proprietary model for every task. The choice of technique should be a strategic one, matched to concrete constraints like budget, performance targets, and latency. This strategic thinking is already being applied in domains like finance, where reasoning models act as algorithmic trading agents [[25]](https://arxiv.org/html/2504.10789v1), and in robotics, where techniques like Embodied Chain-of-Thought (ECoT) guide autonomous systems in complex, real-world tasks [[26]](https://www.mdpi.com/2673-2688/6/7/158), [[27]](https://venturebeat.com/business/researchers-develop-technique-to-give-robots-embodied-reasoning-abilities). By understanding these trade-offs, you can architect systems that are not only powerful but also practical and efficient.

## References

- [1] [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)
- [2] [LLM-Guided Neural-Symbolic Reasoning for Large-Scale Models](https://www.mdpi.com/2227-7390/13/11/1707)
- [3] [Symbolic Reasoning in Modern AI](https://www.youtube.com/watch?v=yo8HtAbUynA)
- [4] [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://arxiv.org/abs/2501.18585)
- [5] [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://www.nature.com/articles/s41586-025-09422-z)
- [6] [DeepSeek-R1 for Beginners](https://thelmbook.com/articles#!./DeepSeek-R1.md)
- [7] [DeepSeek R1's recipe to replicate o1 and the future of reasoning LMs](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1)
- [8] [What are DeepSeek-R1 distilled models?](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d)
- [9] [The Complete Guide to DeepSeek Models: From V3 to R1 and Beyond](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)
- [10] [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314)
- [11] [O1 Replication Journey: A Strategic Progress Report – Part 1](https://arxiv.org/abs/2410.18982)
- [12] [A Survey of Process Reward Models](https://arxiv.org/html/2510.08049v3)
- [13] [GPT-o1 vs GPT-4o: Comparison of the two models](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison)
- [14] [Analysis of OpenAI o1 vs GPT-4o](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o)
- [15] [The State of LLM Reasoning Model Training](https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training)
- [16] [From Emergence to Control: Probing and Modulating Self-Reflection in Language Models](https://arxiv.org/html/2506.12217v1)
- [17] [Undisclosed Pre-training Data's Impact on RL Fine-Tuning](https://www.youtube.com/watch?v=SD5raqvYG-0)
- [18] [What went into training DeepSeek-R1?](https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1)
- [19] [Researchers open-source Sky-T1, a reasoning AI model that can be trained for less than $450](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450)
- [20] [TinyZero GitHub Repository](https://github.com/Jiayi-Pan/TinyZero)
- [21] [Failure modes in journey learning when error paths dominate SFT data distribution](https://arxiv.org/html/2510.01624v1)
- [22] [Incomplete Learning Phenomenon in Supervised Fine-Tuning](https://arxiv.org/html/2604.10079v2)
- [23] [Quantum-Classical Hybrid LLM Pipeline](https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.177004376.69666864)
- [24] [Hybrid Quantum-Classical Architecture for Language Model Fine-Tuning](https://arxiv.org/html/2504.08732v1)
- [25] [Reasoning LLMs in Financial Modeling and Algorithmic Trading](https://arxiv.org/html/2504.10789v1)
- [26] [Adapting LLM Reasoning for Robotic Control and Autonomous Systems](https://www.mdpi.com/2673-2688/6/7/158)
- [27] [Researchers develop technique to give robots embodied reasoning abilities](https://venturebeat.com/business/researchers-develop-technique-to-give-robots-embodied-reasoning-abilities)
</article>