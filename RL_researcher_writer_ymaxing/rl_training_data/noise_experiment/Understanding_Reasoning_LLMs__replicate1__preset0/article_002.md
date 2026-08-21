# Methods and Strategies for Building and Refining Reasoning Models

AI applications are evolving. In 2023, Retrieval-Augmented Generation (RAG) was the dominant trend. For 2024, it was AI agents. For 2025, we are seeing the rise of reasoning models. This new specialization goes beyond injecting domain knowledge through RAG or fine-tuning. It focuses on developing robust, multi-step logical capabilities, allowing models to tackle complex problems in mathematics, logic, and coding.![Image 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.](https://substackcdn.com/image/fetch/$s_!QwUc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png)

Image 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

This specialization is crucial for the next wave of agentic AI, which must decompose complex goals and self-correct. However, reasoning models are not meant to replace general-purpose LLMs for tasks like summarization or simple Q&A. Instead, they are specialized tools for problems that require decomposition and self-correction. This power comes with trade-offs. Reasoning models often have higher latency and cost due to longer, more detailed outputs. They can also "overthink" simple problems, introducing unnecessary complexity and sometimes degrading performance where a general-purpose model would succeed. Understanding these nuances is key for any AI engineer.

In this article, we will explore the world of reasoning models. We will:

1.  Explain the meaning of "reasoning model"
2.  Discuss the advantages and disadvantages of reasoning models
3.  Outline the methodology behind DeepSeek R1
4.  Describe the four main approaches to building and improving reasoning models
5.  Share thoughts on the LLM landscape following the DeepSeek V3 and R1 releases
6.  Provide tips for developing reasoning models on a tight budget

Having set the context and roadmap, we now establish a working definition of "reasoning model" that you can use to evaluate future systems and research.

## How do we define "reasoning model"?

A reasoning model is an LLM designed to solve multi-step problems by generating intermediate steps, or a "thought process." Unlike a standard LLM that might provide a direct answer, a reasoning model breaks down its approach, making it more reliable for complex tasks like puzzles, coding challenges, and mathematical problems. For example, asking "How far does a train go at 60 mph for 3 hours?" requires a simple calculation, whereas a math olympiad problem demands a structured, step-by-step approach.![Image 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process.](https://substackcdn.com/image/fetch/$s_!8oZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png)

Image 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

All modern LLMs can perform some level of reasoning, especially when guided by Chain-of-Thought (CoT) prompting [[1]](https://arxiv.org/abs/2205.11916). This technique, often triggered by a simple phrase like "Let's think step by step," encourages the model to externalize its reasoning process, which often improves accuracy on complex problems. However, specialized reasoning models are explicitly trained to excel at these tasks, achieving a level of performance that prompting alone cannot match on the hardest benchmarks, such as formal proofs or novel puzzles.

These specialized models generate intermediate steps in one of two ways:

1.  **Visible thought traces:** The model outputs its step-by-step reasoning process as part of the response. This allows the user to read and verify the logic, which is a key feature of models like DeepSeek-R1. The generated text serves as both the reasoning process and a component of the final answer.
2.  **Invisible internal iterations:** The model allocates extra computation time to "think" internally before producing a final answer. This is often called "test-time scaling" and is rumored to be a core mechanism behind models like OpenAI's o1, which take longer to respond but deliver more accurate results on difficult problems. This internal deliberation is not exposed to the user but is crucial for the model's problem-solving ability.

It is important to distinguish between the reasoning process and the final output. A model can reason internally without showing its work, or it can be prompted to explain its steps as part of the answer. Specialized reasoning models are optimized for the former, which often leads to better performance on complex tasks. The ability to generate a visible thought trace is often a byproduct of this optimization, but the core capability lies in the multi-step processing itself.![Image 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user.](https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png)

Image 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.

## When should we use reasoning models?

Before diving into technical details, it is important to consider when reasoning models are needed. They deliver the highest returns on puzzles, advanced mathematics, and competitive coding. These are problems that require decomposition and self-correction. For tasks like summarization, simple Q&A, or creative writing, a general-purpose model is often more efficient and cost-effective.

The power of reasoning models comes with practical downsides. The verbose intermediate steps lead to higher latency and token costs. This can frustrate users in conversational settings who expect quick answers. There is also the risk of "overthinking," where a model invents unnecessary complications for a straightforward problem. For instance, a reasoning model might break down `2+2` into a multi-step philosophical inquiry, increasing latency and the chance of error, whereas a standard LLM would correctly answer "4" instantly. Choosing the right tool for the job is key.![Image 4: The key strengths and weaknesses of reasoning models.](https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png)

Image 4: The key strengths and weaknesses of reasoning models. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

Understanding when to deploy reasoning models leads naturally to studying a concrete, open pipeline that demonstrates how such capabilities are created at scale.

## A brief look at the DeepSeek training pipeline

The DeepSeek-R1 series provides a transparent look into how reasoning models are built [[2]](https://arxiv.org/abs/2501.12948). The pipeline involves three key models, all built on top of the DeepSeek-V3-Base architecture, a 671B parameter Mixture-of-Experts (MoE) model.

1.  **DeepSeek-R1-Zero:** This model is trained using pure Reinforcement Learning (RL) directly from the base model, skipping the usual Supervised Fine-Tuning (SFT) stage. This "cold-start" approach allows the model to develop its own reasoning patterns without being constrained by human-annotated examples. The training relies on verifiable rewards, such as whether a math problem's final answer is correct or if code passes unit tests. This method proved that complex reasoning can emerge without direct supervision.
2.  **DeepSeek-R1:** This is the flagship reasoning model. It starts with an R1-Zero checkpoint and refines its capabilities through additional SFT and RL stages. The initial SFT uses a small "cold-start" dataset of human-readable reasoning traces to improve coherence. Subsequent RL stages introduce a language consistency reward to prevent the model from mixing languages, making the output more user-friendly. This hybrid approach results in a model that is both a powerful reasoner and a clear communicator.
3.  **DeepSeek-R1-Distill:** To make powerful reasoning more accessible, DeepSeek created smaller, distilled models. This is not traditional, logit-based distillation. Instead, it involves fine-tuning smaller open-source models (like Qwen and Llama) on a large dataset of 800,000 high-quality reasoning traces generated by the full-sized R1 model. This SFT-based approach effectively transfers the reasoning capabilities of the large model to smaller, more efficient ones.![Image 5: Development process of DeepSeek's three different reasoning models that are discussed in the DeepSeek R1 technical report.](https://substackcdn.com/image/fetch/$s_!z-dr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png)

Image 5: Development process of DeepSeek's three different reasoning models that are discussed in the DeepSeek R1 technical report. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

This multi-stage process highlights a key theme in modern AI engineering: building powerful, specialized models is an iterative process. It starts with a strong foundation, introduces new capabilities through techniques like RL, and then refines and democratizes those capabilities through distillation.

The DeepSeek pipeline incorporates all four main techniques we will now examine in depth, allowing direct comparison of their mechanisms, emergent phenomena, and empirical outcomes.

## The 4 main ways to build and improve reasoning models

Several key techniques have emerged to enhance LLM reasoning and build specialized models. While the exact workings of proprietary models like OpenAI's o1 and o3 remain under wraps, they are rumored to combine both training and inference-time methods. Here, we will break down the four main approaches.

### 1) Inference-time scaling

Inference-time scaling is the practice of dedicating more computational resources during inference to improve a model's performance. This is analogous to giving a human extra time to think through a problem and is also known as test-time compute scaling. It is a powerful way to boost reasoning without altering the model's weights. The core idea is that performance can be improved by increasing compute not just during training, but also at the moment of prediction.

Common methods include:

-   **Chain-of-Thought (CoT) Prompting:** This is the simplest form of inference-time scaling. By adding a phrase like "Let's think step by step" to the prompt, we encourage the model to generate more tokens in the form of intermediate reasoning steps. This increased output length requires more compute but often leads to more accurate answers on complex problems [[1]](https://arxiv.org/abs/2205.11916).![Image 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper](https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png)

Image 6: An example of classic CoT prompting from the 2022 *Large Language Models are Zero-Shot Reasoners* paper [[1]](https://arxiv.org/abs/2205.11916).

-   **Search Strategies:** More advanced techniques involve exploring multiple potential solutions and selecting the best one. This can be done through simple **majority voting** (generating multiple answers and picking the most common one) or more sophisticated search algorithms like **beam search** and **Monte Carlo Tree Search (MCTS)**. These methods often rely on a **Process Reward Model (PRM)**, which is a separate model trained to evaluate the quality of each intermediate step in a reasoning chain. The PRM acts as a guide, helping the search algorithm navigate the vast space of possible solutions and focus on the most promising paths [[3]](https://arxiv.org/abs/2408.03314). A PRM provides real-time feedback to guide the reasoning process, allowing smaller models to sometimes outperform larger ones through this compute-optimal scaling.![Image 7: Different search-based methods rely on a process-reward-based model to select the best answer.](https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png)

Image 7: Different search-based methods rely on a process-reward-based model to select the best answer. (Source: Annotated figure from the *LLM Test-Time Compute* paper [[3]](https://arxiv.org/abs/2408.03314))

Interestingly, the DeepSeek R1 paper categorizes some of these methods, including PRM-based search and MCTS, under "unsuccessful attempts" during their training process [[2]](https://arxiv.org/abs/2501.12948). This suggests that while these techniques can be effective, they may introduce too much complexity or computational overhead in a large-scale RL pipeline. However, this does not mean DeepSeek avoids inference-time scaling altogether. It is likely applied at the application layer, allowing for flexibility without complicating the core model training.

This reliance on heavy inference-time compute could also explain the higher cost of models like OpenAI's o1. Compared to GPT-4o, o1 models are significantly more expensive. For example, o1's API pricing can be up to 6 times higher for input tokens and 6 times higher for output tokens [[4]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison). This price difference may be due to the additional computational resources required for the model to "think" longer and explore multiple reasoning paths before generating a final response. For a basic reasoning task, GPT-4o might take less than a second, while o1 could take minutes to generate a more detailed, self-verified answer [[5]](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o).

### 2) Pure reinforcement learning (RL)

The DeepSeek-R1-Zero model is a prime example of using pure RL to develop reasoning capabilities [[2]](https://arxiv.org/abs/2501.12948). Unlike typical RLHF pipelines that start with a model already fine-tuned on human demonstrations (SFT), R1-Zero applies RL directly to the base model. This "cold-start" approach is driven by two main types of rule-based rewards, which provide clear, automated feedback without human intervention:

1.  **Accuracy rewards:** The model receives a positive reward if its final answer is correct. This is straightforward for tasks with verifiable solutions, like math problems where the answer can be checked, or coding challenges where the code can be run against test cases. The reward is binary: 1 for correct, 0 otherwise.
2.  **Format rewards:** The model is incentivized to follow a specific output structure, such as wrapping its thought process in `<think>` and `</think>` tags. This ensures the output is well-structured and interpretable, making it easier to analyze the model's reasoning process.

To optimize for these rewards, DeepSeek used an algorithm called Group Relative Policy Optimization (GRPO). Unlike the more common Proximal Policy Optimization (PPO), GRPO does not require a separate, large value model to estimate rewards. Instead, it generates a group of responses for each prompt, calculates the average reward for the group, and then updates the policy by reinforcing answers that scored above the average and penalizing those that scored below. This makes the training process more memory-efficient and scalable.![Image 8: The development process of DeepSeek-R1-Zero model.](https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png)

Image 8: The development process of DeepSeek-R1-Zero model. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

One of the most notable outcomes of this process was the emergence of an "Aha moment." As training progressed, the model spontaneously began to generate long, complex reasoning traces. These traces included self-correction patterns, where the model would pause, re-evaluate its approach, and correct its own mistakes, often using phrases like "Wait, wait. Wait. That's an aha moment I can flag here." This was accompanied by a steady increase in the average length of the model's responses, indicating that it was learning to allocate more "thinking time" to problems. This emergent behavior, which also included strange quirks like mixing languages in its reasoning, was a direct result of the RL process optimizing for final answer accuracy, without any explicit instruction on how to reason.![Image 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment.](https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png)

Image 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment. (Source: [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948))

The success of R1-Zero was a milestone. It was the first clear demonstration that it is possible to develop a reasoning model with pure RL, opening up new possibilities for training AI systems that can learn to solve complex problems on their own without being limited by human-provided examples.

### 3) Supervised finetuning and reinforcement learning (SFT + RL)

While pure RL can unlock emergent reasoning, it can also lead to outputs that are difficult for humans to follow, sometimes mixing languages or producing chaotic thought processes. The DeepSeek-R1 model addresses this by using a hybrid approach that combines SFT with RL for a more stable and refined outcome [[2]](https://arxiv.org/abs/2501.12948). This multi-stage pipeline is designed to build on the strengths of each method.

The process involves several key stages:

1.  **Cold-Start SFT:** The process begins by fine-tuning the base model on a small, curated set of "cold-start" data. This dataset consists of a few thousand high-quality reasoning traces, some of which are generated by the R1-Zero model and then refined by human annotators to be more conversational and follow a consistent, human-like thought process. This initial SFT stage "warms up" the model, teaching it the basic structure of a coherent reasoning chain and avoiding the "chaotic start" problem where a base model doesn't even know basic reasoning templates.
2.  **Reasoning-Oriented RL:** The model then undergoes RL training similar to R1-Zero, but with an added **language consistency reward**. This reward, calculated as the proportion of target language words in the CoT, penalizes the model for mixing languages (e.g., English and Chinese) in its response. While this can slightly decrease performance on some benchmarks, it significantly improves the readability and usability of the model's output.
3.  **Rejection Sampling and General SFT:** After the first RL stage, the model is used to generate a large synthetic dataset of over 600,000 correct reasoning solutions through rejection sampling. This dataset is then combined with general-purpose, non-reasoning data (e.g., factual QA, general writing) and used for another round of SFT. This stage broadens the model's capabilities, ensuring it maintains its proficiency in tasks like writing and general Q&A while specializing in reasoning.
4.  **Final RL Polish:** The pipeline concludes with a final RL stage that uses a mix of verifiable rewards for reasoning tasks and preference-based rewards (from a reward model) for general tasks. This polishes the model, further aligning it with human preferences for helpfulness and harmlessness.![Image 10: The development process of DeepSeek-R1 model.](https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-d148e0a61be_1548x1154.png)

Image 10: The development process of DeepSeek-R1 model. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

This multi-stage approach allows DeepSeek-R1 to inherit the powerful, emergent reasoning of R1-Zero while being more aligned with human preferences for clarity and consistency. The result is a model that rivals top-tier proprietary models like OpenAI's o1 on reasoning benchmarks, showcasing the power of a carefully orchestrated SFT + RL pipeline.![Image 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models.](https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png)

Image 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. (Source: Annotated figure from the [DeepSeek-R1 technical report](https://arxiv.org/abs/2501.12948))

### 4) Pure supervised finetuning (SFT) and distillation

Inference-time scaling offers flexibility without retraining, pure RL unlocks emergent behaviors, and a hybrid SFT+RL approach provides a balanced path to production. The fourth major method, pure SFT and distillation, offers the most accessible and cost-effective way to create specialized reasoning models.

In the context of reasoning models, distillation is not the classic, logit-based method where a student model tries to mimic the full probability distribution of a teacher. Instead, it is a simpler form of SFT. A large, powerful "teacher" model (like DeepSeek-R1) is used to generate a massive dataset of high-quality reasoning traces. A smaller "student" model is then fine-tuned on this synthetic dataset [[6]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond). DeepSeek used this approach to create its R1-Distill models, fine-tuning smaller open-source models like Qwen and Llama on 800,000 reasoning samples from the full-sized R1 model.![Image 12: The development process of DeepSeek-R1-Distill models.](https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png)

Image 12: The development process of DeepSeek-R1-Distill models. (Source: [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

DeepSeek developed these distilled models for two main reasons: to make advanced reasoning accessible to those with limited computational resources, and to create more efficient models for production environments where cost and latency are critical.

The results are impressive. Even the smallest 1.5B distilled model outperforms powerful non-reasoning models on some math benchmarks [[2]](https://arxiv.org/abs/2501.12948). This demonstrates that the complex reasoning patterns discovered through large-scale RL can be effectively transferred to smaller models through a simple SFT process.![Image 13: Benchmark comparison of distilled versus non-distilled models.](https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png)

Image 13: Benchmark comparison of distilled versus non-distilled models. (Source: Annotated figure from the [DeepSeek-R1 technical report](https://arxiv.org/abs/2501.12948))

The DeepSeek report also offers a crucial insight: for smaller models, distillation is more effective than pure RL. They trained a 32B model with the same pure RL process as R1-Zero and found that it performed on par with other open-source models but was significantly outperformed by the 32B model distilled from R1.![Image 14: Benchmark comparison distillation and RL on a smaller 32B model.](https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png)

Image 14: Benchmark comparison distillation and RL on a smaller 32B model. (Source: Annotated figure from the [DeepSeek-R1 technical report](https://arxiv.org/abs/2501.12948))

This suggests that emergent reasoning behaviors are a property of scale. Smaller models may not have the capacity to discover these patterns on their own through RL, but they can learn to replicate them when given high-quality examples. While the table provides a good comparison, it would have been even more useful to see how these models stack up against a 32B model trained with a hybrid SFT+RL approach, or how they compare to a distilled model that also underwent a final RL stage.

After dissecting the four techniques and seeing them embodied in DeepSeek-R1, we can step back to evaluate the release's broader significance and limitations.

## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 models was a significant moment for the open-source AI community. The combination of an open MIT license and a detailed technical report provided a rare look into the engineering behind a state-of-the-art reasoning model [[7]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners). The demonstration that pure, cold-start RL could lead to emergent reasoning was a particularly valuable insight, showing that models could learn to "think" without being explicitly taught how.

When comparing DeepSeek-R1 to OpenAI's o1, we see two different philosophies at play. On benchmarks, the models are comparable in many reasoning tasks, but R1 appears to be more efficient at inference [[2]](https://arxiv.org/abs/2501.12948). This suggests that DeepSeek invested heavily in training-time optimization, creating a model that is inherently a strong reasoner. In contrast, o1 may rely more on inference-time scaling, using more compute at runtime to achieve its performance. This is a classic trade-off between training cost and inference cost.

However, a direct comparison is difficult. We do not know the size or architecture of the o1 model, the exact mix of techniques used in its training, or the strength of its base model. Without this information, it is impossible to definitively attribute performance differences to any single factor. A direct comparison would be unwarranted until OpenAI discloses more details about its methodology.

There is also the question of training cost. The widely cited $6 million figure for DeepSeek-V3 likely refers to the pre-training of the base model. The true incremental cost of the specialized RL and SFT stages for R1 remains undisclosed [[6]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond). The final cost for the R1 fine-tuning process was reported as $294,000, but this figure excludes prior expenses, most notably the development of the V3 base model itself [[8]](https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18). This highlights that even "cheaper" fine-tuning efforts stand on the shoulders of extremely expensive foundational models.

Despite these open questions, DeepSeek-R1 stands as a milestone. It proved that high-level reasoning is not the exclusive domain of closed-source labs and has accelerated open research into all four of the techniques we have discussed.

## Developing reasoning models on a limited budget

Developing a reasoning model from scratch is a massive undertaking, but recent projects have shown that it is possible to achieve impressive results on a limited budget. These efforts typically focus on distillation and smaller-scale RL, making advanced reasoning more accessible to the broader community.

The Sky-T1 project is a great example of budget-friendly distillation [[9]](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450). Developed by researchers at UC Berkeley, Sky-T1 is a 32B parameter model trained for less than $450. It was created by fine-tuning an existing open-source model on a curated dataset of just 17,000 samples generated by a more powerful reasoning model (Alibaba's Qwen QwQ). The data was then refactored using GPT-4o-mini. This highly targeted approach allowed them to achieve performance that approaches early versions of OpenAI's o1 on several reasoning benchmarks, including outperforming it on MATH500 and LiveCodeBench. This demonstrates how effective a focused distillation strategy can be.![Image 15: Figure from the "Sky-T1: Train your own O1 preview model within $450" article](https://substackcdn.com/image/fetch/$s_!Y8HI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8865a313-2326-4f07-a6dc-72cc94cb2ebe_1364x570.png)

Image 15: Figure from the "Sky-T1: Train your own O1 preview model within $450" article (Source: [novasky-ai.github.io](https://novasky-ai.github.io/posts/sky-t1/))

On the pure RL front, the TinyZero project shows what is possible at an even smaller scale [[10]](https://github.com/Jiayi-Pan/TinyZero). This project reproduced the cold-start RL approach of DeepSeek-R1-Zero on a 3B parameter Qwen2.5 model for under $30. While trained on simpler tasks like multiplication and the Countdown game, TinyZero exhibited the same emergent self-verification and reasoning behaviors seen in its larger counterpart. This reinforces the idea that the principles of pure RL can be applied even without massive computational resources, as long as the task has a clear, verifiable reward signal. The ability to reproduce the "Aha moment" so cheaply is a significant step for democratizing research into this phenomenon.![Image 16: A figure from the TinyZero repository showing that the model is capable of self-verification.](https://substackcdn.com/image/fetch/$s_!Ykdn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6111f4b4-cfb9-494c-8390-ec251702914b_1600x955.png)

Image 16: A figure from the TinyZero repository showing that the model is capable of self-verification. (Source: [github.com/Jiayi-Pan/TinyZero](https://github.com/Jiayi-Pan/TinyZero))

A third, and perhaps most innovative, budget-conscious approach is "journey learning." This paradigm shifts the focus of SFT from "shortcut learning"—training only on correct solution paths—to training on the entire problem-solving journey, including incorrect attempts, reflections, and self-corrections [[11]](https://arxiv.org/abs/2410.18982).![Image 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solutions paths in the SFT data.](https://substackcdn.com/image/fetch/$s_!TxCO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0bfcd0-6d93-4c91-a0d6-28178839b7cf_1492x724.png)

Image 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solutions paths in the SFT data. (Source: Annotated figure from the *O1 Replication Journey: A Strategic Progress Report – Part 1* [[11]](https://arxiv.org/abs/2410.18982))

By exposing the model to the messy reality of how problems are actually solved, journey learning helps it develop more robust self-correction mechanisms. A model trained only on "golden paths" can be brittle when it encounters a novel error. In contrast, a model trained on a journey of trial and error is better equipped to recognize and recover from its own mistakes. The initial results are promising: with just 327 training samples, journey learning improved performance on the MATH dataset by over 8% compared to traditional SFT [[11]](https://arxiv.org/abs/2410.18982). This suggests that the quality and nature of the training data can be just as important as the quantity.

Looking ahead, the most effective budget-friendly pipelines will likely be hybrids. A combination of the targeted distillation of Sky-T1, the emergent RL principles of TinyZero, and the robust self-correction of journey learning could balance cost, performance, and reliability, making advanced reasoning accessible to a much wider range of developers and researchers.

## Conclusion

We have explored the four primary ways to build and improve reasoning models. Each offers a different set of trade-offs, providing a toolkit for AI engineers to choose from based on their specific needs and constraints.

-   **Inference-time scaling** is a powerful but costly approach that boosts performance without any training. This makes it ideal for leveraging existing models when you can tolerate higher latency and cost per query. It offers maximum flexibility at the cost of serving efficiency.
-   **Pure RL** is a research-forward technique that can unlock emergent behaviors and novel reasoning patterns, as seen with DeepSeek-R1-Zero. It is best suited for tasks with clear, verifiable rewards and requires significant computational investment, but it holds the key to discovering non-human-like problem-solving strategies.
-   **SFT + RL** is a production-ready blueprint that combines the stability of supervised learning with the exploratory power of reinforcement learning. It offers a balanced path to high performance and is likely the approach used by many state-of-the-art models, providing both strong capabilities and user-friendly outputs.
-   **Distillation** is an efficient method for transferring capabilities from large models to smaller ones. Its ultimate performance is capped by the teacher model, but it is the most accessible way to create specialized models on a budget, democratizing access to advanced reasoning.

The future of reasoning models is likely a hybrid one. The most capable systems will probably combine a robust SFT+RL training pipeline with sophisticated inference-time scaling. This is the pattern we suspect is already at play in models like o1 and will likely define the next generation of o3-class models. This hybrid approach allows models to be both inherently capable (from training) and dynamically adaptable (at inference), delivering the best of both worlds.

As AI engineers, the key is not to chase the largest or most expensive model, but to match the right technique to the constraints of the problem at hand. Your choice will depend on your budget, performance targets, and deployment requirements. Do you need the absolute best performance, or is cost-efficiency more important? Is low latency critical, or can your users wait for a more thoughtful answer? By understanding the trade-offs between these four approaches, you can make informed decisions and build AI systems that are not just powerful, but also practical and effective for your specific use case.

## References

- [1] [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)
- [2] [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- [3] [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314)
- [4] [GPT-o1 vs GPT-4o: Comparison of the Newest OpenAI Models](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison)
- [5] [OpenAI GPT-o1 API & Pricing: A Comprehensive Guide](https://francpetracci.medium.com/openai-gpt-o1-api-pricing-a-comprehensive-guide-b93fdaed217c)
- [6] [The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)
- [7] [DeepSeek-R1 for Beginners](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners)
- [8] [China's DeepSeek says its hit AI model cost just $294,000 to train](https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18)
- [9] [Researchers open source Sky-T1, a ‘reasoning’ AI model that can be trained for less than $450](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450)
- [10] [TinyZero GitHub Repository](https://github.com/Jiayi-Pan/TinyZero)
- [11] [O1 Replication Journey: A Strategic Progress Report – Part 1](https://arxiv.org/abs/2410.18982)
- [12] [Analysis of OpenAI o1 vs GPT-4o](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o)
</article>