# Methods and Strategies for Building and Refining Reasoning Models

Reasoning models are set to be the key LLM specialization trend of 2025. This evolution moves beyond familiar patterns like Retrieval-Augmented Generation (RAG) or domain-specific fine-tuning. Instead of injecting knowledge, reasoning specialization targets the emergence of robust, multi-step logical capabilities. This allows models to tackle complex problems that require more than simple information retrieval.![Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png)
Image 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.

This specialization is aimed at tasks like mathematical proofs, logical puzzles, and competitive programming. It does not replace general-purpose LLMs, which remain effective for everyday generation, summarization, or simple question-answering. However, these advanced reasoning capabilities come with trade-offs. The gains in logic are often accompanied by increased inference latency and cost due to longer, more detailed outputs. There is also a risk of "overthinking" on trivial tasks, where a specialized model might introduce unnecessary complexity that a standard model would handle correctly and efficiently. Recent research has begun to systematically study this "overthinking," finding that answer quality can follow an inverted U-shaped curve where too much reasoning hurts performance, especially on easier problems [[16]](https://arxiv.org/html/2604.10739v1).

In this article, we will explore the world of reasoning models. We will cover the following topics:

1.  Explain the meaning of "reasoning model"
2.  Discuss the advantages and disadvantages of reasoning models
3.  Outline the methodology behind DeepSeek R1
4.  Describe the four main approaches to building and improving reasoning models
5.  Share thoughts on the LLM landscape following the DeepSeek V3 and R1 releases
6.  Provide tips for developing reasoning models on a tight budget

Having set the context and roadmap, we will now establish a working definition of "reasoning model" that you can use to evaluate future systems and research.

## How do we define "reasoning model"?

A reasoning model is one that generates multi-step intermediate thinking to solve complex queries. This process can involve explicit token traces that we can read or hidden internal iterations that happen within the model. This stands in contrast to the direct factual recall or single-pass pattern matching that is sufficient for simpler prompts. For example, asking "What is the capital of France?" requires a simple fact retrieval. Asking "If a train leaves Paris at 8 AM traveling at 100 km/h and a second train leaves Lyon 30 minutes later traveling at 120 km/h, where will they meet?" requires a series of calculations and logical steps.![Figure 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png)
Image 2: A regular LLM may provide a short answer, whereas a reasoning model typically includes intermediate steps that reveal its thought process.

All modern LLMs exhibit some level of reasoning, which can be improved with techniques like Chain-of-Thought (CoT) prompting. However, specialized reasoning models are designed to achieve exceptional performance on difficult benchmarks that involve tasks like math olympiad problems, formal proofs, or novel puzzle-solving [[1]](https://arxiv.org/abs/2501.12948).

The intermediate steps in these models manifest in two primary ways. The first is through visible thought traces, where the model outputs its step-by-step reasoning process for the user to see. This is common in models that use CoT. The second is through invisible internal iterations, a characteristic of models like OpenAI's o1, which allocate additional computation time at inference without exposing every intermediate token to the user [[2]](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o). This shift from explicit to hidden reasoning represents a key evolution, where the structured thought process of CoT is automated and internalized by the model itself, allowing it to self-direct its reasoning without explicit prompting [[17]](https://www.nvidia.com/en-us/glossary/cot-prompting). This allows the model to "think" more deeply about a problem before providing a final answer.![Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png)
Image 3: Reasoning can refer to the internal multi-step generation process or the explicit reasoning shown to the user.

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.

## When should we use reasoning models?

Before diving into the technical details, it is important to consider when reasoning models are truly necessary. These models deliver the highest returns on tasks that require decomposition or self-correction, such as puzzles, advanced mathematics, and competitive coding. However, they are often overkill for tasks like summarization, simple factual question-answering, or creative writing, where direct generation is sufficient and more efficient.

Deploying a reasoning model comes with practical downsides. The verbose intermediate steps lead to significantly higher latency and token costs. This increased verbosity can also frustrate users in conversational settings, who may prefer a direct answer over a lengthy explanation. Furthermore, there is a risk of overthinking, where the model invents unnecessary complications for straightforward problems that a base model would solve correctly in a single pass [[3]](https://arxiv.org/html/2503.20783v1). This can even cause the model to abandon a correct initial answer, a phenomenon documented in recent studies [[16]](https://arxiv.org/html/2604.10739v1).![Figure 4: The key strengths and weaknesses of reasoning models.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png)
Image 4: A summary of the primary strengths and weaknesses of reasoning models.

Understanding when to deploy reasoning models leads naturally to studying a concrete, open pipeline that demonstrates how such capabilities are created at scale.

## A brief look at the DeepSeek training pipeline

The DeepSeek-R1 series provides a transparent case study of how reasoning capabilities can be cultivated. The series includes three main variants, each built upon the last: R1-Zero, R1, and the distilled models [[1]](https://arxiv.org/abs/2501.12948).![Figure 5: Development process of DeepSeeks three different reasoning models that are discussed in the DeepSeek R1 technical report.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png)
Image 5: The development process for DeepSeek's three reasoning models as detailed in their technical report.

**DeepSeek-R1-Zero** is the foundational model, created using a "cold-start" pure Reinforcement Learning (RL) process directly from the DeepSeek-V3 base model. This approach skips the conventional Supervised Fine-Tuning (SFT) stage that typically precedes RL. The model learns to reason by being rewarded for correct final answers on verifiable tasks, allowing reasoning patterns to emerge without being constrained by human-written examples [[4]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners). This was achieved using Group-wise Reward Policy Optimization (GRPO), an algorithm that avoids the need for a separate critic model, reducing computational cost and memory usage during the RL phase [[18]](http://scalable-ai.eecs.berkeley.edu/assets/lecture_slides/lecture_15.pdf).

**DeepSeek-R1** is the flagship reasoning model, which refines the capabilities of R1-Zero. It undergoes additional training stages, including SFT and further RL, to improve the readability of its reasoning and its overall performance. This multi-stage process helps align the model's outputs with human preferences while retaining the strong reasoning abilities developed in the R1-Zero phase [[1]](https://arxiv.org/abs/2501.12948).

**DeepSeek-R1-Distill** models are smaller, more efficient versions created by transferring the capabilities of the large R1 model. This is not classical logit-based knowledge distillation. Instead, it involves using the high-quality, step-by-step reasoning outputs generated by R1 as a dataset for SFT on smaller, open-source models like Qwen and Llama. This allows the smaller models to inherit advanced reasoning patterns without undergoing the full, computationally expensive RL training process [[5]](https://redwerk.com/blog/what-is-model-distillation).

The DeepSeek pipeline incorporates all four main techniques we will now examine in depth, allowing a direct comparison of their mechanisms, emergent phenomena, and empirical outcomes.

## The 4 main ways to build and improve reasoning models

Current techniques for enhancing LLM reasoning and building specialized models can be grouped into four main categories. While the exact workings of OpenAI's o1 and o3 models remain undisclosed, they are rumored to combine multiple training and inference strategies to achieve their performance.

### 1) Inference-time scaling

Inference-time scaling refers to allocating more computational resources at the moment a query is made, which is analogous to giving a human extra time to think about a difficult problem. This approach improves performance without altering the model's weights. It is governed by "test-time compute scaling laws," which suggest that for some models, performance continues to improve as they are allowed to "think" for longer [[6]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).

Common methods for inference-time scaling include:
*   **Chain-of-Thought (CoT) prompting:** Encouraging the model to generate a step-by-step reasoning process before giving a final answer. This can be done with zero-shot prompts like "Let's think step by step" [[7]](https://arxiv.org/abs/2205.11916). While originally a prompting technique, this concept was later automated in test-time scaling models, which learn to self-direct their own multi-step reasoning without needing a specific user prompt to trigger it [[17]](https://www.nvidia.com/en-us/glossary/cot-prompting).![Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png)
Image 6: An example of classic CoT prompting from the 2022 "Large Language Models are Zero-Shot Reasoners" paper.

*   **Majority Voting (Self-Consistency):** Generating multiple reasoning paths and selecting the most common final answer.
*   **Search Algorithms:** More complex methods like beam search or Monte Carlo Tree Search (MCTS) explore a tree of possible reasoning steps to find the optimal path. These often rely on a Process Reward Model (PRM) to evaluate the correctness of each intermediate step [[8]](https://arxiv.org/abs/2408.03314).![Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png)
Image 7: Different search-based methods rely on a process-reward model to select the best answer, as shown in the "Scaling LLM Test-Time Compute" paper.

However, the core assumption that more thinking always leads to better answers is flawed. Research on "overthinking" has shown that for many problems, especially simpler ones, performance follows an inverted U-shaped curve. After a certain point, additional computation leads to diminishing or even negative returns, as the model may second-guess a correct answer and "flip" it to an incorrect one [[16]](https://arxiv.org/html/2604.10739v1).

Interestingly, the DeepSeek R1 technical report categorizes both PRM and MCTS under "Unsuccessful Attempts," stating that the computational overhead they introduce outweighs their benefits during large-scale RL training [[1]](https://arxiv.org/abs/2501.12948). This suggests that while these methods can improve performance during inference, they may not be efficient enough for the training loop. However, it is possible that DeepSeek still applies these techniques at the application layer for specific use cases.

The higher cost of OpenAI's o1 models compared to models like GPT-4o may be due to this increased inference-time computation. O1 is designed to spend more time reasoning through complex tasks, which naturally requires more resources and leads to higher latency and cost [[9]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison).

### 2) Pure reinforcement learning (RL)

The pure RL approach, exemplified by DeepSeek-R1-Zero, bypasses the standard SFT stage and applies RL directly to a base model. Instead of relying on a reward model trained on human preferences, this method uses verifiable outcomes to guide the model's learning. The reward system is typically rule-based, consisting of two main components [[1]](https://arxiv.org/abs/2501.12948):

1.  **Accuracy Rewards:** The model receives a positive reward if its final answer is correct and zero otherwise. This is used for tasks with deterministic solutions, like math problems or coding challenges where outputs can be verified by unit tests.
2.  **Format Rewards:** The model is incentivized to follow specific formatting rules, such as enclosing its reasoning process within `<think>` and `</think>` tags. This ensures the output is structured and interpretable.![Figure 8: The development process of DeepSeek-R1-Zero model.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png)
Image 8: The development process of the DeepSeek-R1-Zero model.

The algorithm behind this process is typically Group-wise Reward Policy Optimization (GRPO). Unlike other RL algorithms like PPO, GRPO does not require training a separate value network or critic. Instead, it normalizes rewards across a group of responses to the same prompt. This makes it computationally efficient and a natural fit for verifiable tasks where multiple solutions can be generated and automatically checked for correctness [[18]](http://scalable-ai.eecs.berkeley.edu/assets/lecture_slides/lecture_15.pdf).

A key phenomenon observed during this process is the "Aha moment," where the model spontaneously begins to generate long, detailed reasoning traces and self-correction patterns. For example, the model might generate phrases like "Wait, let me reevaluate" before correcting a mistake in its reasoning. This emergent behavior is a direct result of the RL process optimizing for correct final answers [[1]](https://arxiv.org/abs/2501.12948), [[10]](https://www.philschmid.de/mini-deepseek-r1).![Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png)
Image 9: The emergence of the "Aha moment" as shown in the DeepSeek R1 technical report.

The success of R1-Zero is significant because it was the first demonstration that a model could develop advanced reasoning capabilities through pure RL, without being explicitly taught how to reason through supervised examples.

### 3) Supervised finetuning and reinforcement learning (SFT + RL)

The SFT+RL hybrid approach, used to create the final DeepSeek-R1 model, builds upon the foundation of pure RL to create a more stable and user-friendly model. This multi-stage process is designed to refine the raw reasoning capabilities of R1-Zero while aligning its outputs with human preferences [[1]](https://arxiv.org/abs/2501.12948).![Figure 10: The development process of DeepSeek-R1 model.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png)
Image 10: The development process of the DeepSeek-R1 model.

The pipeline generally consists of these phases:

1.  **Cold-Start SFT:** The process begins with a small SFT stage using a few thousand high-quality reasoning examples. This "cold-start" data, often generated and filtered from earlier models like R1-Zero, teaches the base model the basic structure of a reasoning trace, making the subsequent RL phase more stable [[4]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners).
2.  **Reasoning-Oriented RL:** The model then undergoes large-scale RL training similar to R1-Zero, using verifiable rewards. During this phase, a **language consistency reward** is introduced to penalize outputs that mix languages (e.g., English and Chinese), improving readability even if it slightly degrades raw accuracy on some tasks [[1]](https://arxiv.org/abs/2501.12948).
3.  **Rejection Sampling and SFT:** After the RL stage, a large synthetic dataset is generated. The model produces multiple solutions for each problem, and only the correct ones are kept. This filtered dataset, often mixed with general-purpose instruction data, is used for another round of SFT. This step helps the model absorb the best reasoning strategies discovered during RL while maintaining its general capabilities.
4.  **Final RL Alignment:** A final RL stage is performed on a mix of reasoning and general-purpose tasks. For open-ended prompts, a preference model is used to reward helpfulness and harmlessness, similar to standard RLHF.

This iterative refinement process allows DeepSeek-R1 to achieve state-of-the-art performance on reasoning benchmarks, rivaling closed-source models like OpenAI's o1 [[1]](https://arxiv.org/abs/2501.12948).![Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png)
Image 11: A benchmark comparison of OpenAI o1 and DeepSeek-R1 models from the DeepSeek-R1 technical report.

### 4) Pure supervised finetuning (SFT) and distillation

Inference-time scaling offers a way to improve performance without training, pure RL allows for the emergence of novel reasoning, and a hybrid SFT+RL approach provides a stable path to production-ready models. The fourth approach, pure SFT or distillation, offers an efficient way to transfer these hard-won capabilities to smaller, more accessible models.

DeepSeek's approach to distillation is a form of SFT. Instead of traditional methods that involve matching the output probabilities (logits) of a smaller "student" model to a larger "teacher" model, DeepSeek uses the high-quality, step-by-step reasoning outputs generated by the powerful R1 model as a training dataset. Smaller open-source models, like Qwen and Llama, are then fine-tuned on this data [[1]](https://arxiv.org/abs/2501.12948), [[11]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d).![Figure 12: The development process of DeepSeek-R1-Distill models.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png)
Image 12: The development process of DeepSeek-R1-Distill models.

DeepSeek developed these distilled models for two main reasons. First, it makes powerful reasoning accessible to a wider audience, as smaller models are cheaper to run and can be deployed on consumer-grade hardware. Second, it provides a more efficient path to strong reasoning capabilities for smaller models, which often struggle to develop these skills through pure RL alone [[1]](https://arxiv.org/abs/2501.12948).

The results show that this distillation technique is highly effective. Even the 1.5B parameter distilled Qwen model surpasses strong non-reasoning baselines on mathematical benchmarks. As the size of the student model increases, its performance gets progressively closer to that of the original R1 teacher [[1]](https://arxiv.org/abs/2501.12948).![Figure 13: Benchmark comparison of distilled versus non-distilled models. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png)
Image 13: A benchmark comparison of distilled versus non-distilled models from the DeepSeek-R1 technical report.

However, the DeepSeek report also provides a crucial insight when comparing these approaches. While distillation is effective, it is ultimately derivative; the student model is unlikely to surpass the teacher. This limitation stems from several open challenges in distilling reasoning to smaller models. These include a loss of nuanced, multi-step logic that smaller models struggle to represent, architectural mismatches between teacher and student, and the student's tendency to hallucinate when it lacks the vast factual knowledge of the teacher [[19]](https://medium.com/@graison/knowledge-distillation-in-the-era-of-large-language-models-llms-7b0bead7d822). For a 32B model, distillation significantly outperformed a model of the same size trained with pure RL. This suggests that for smaller models, it is more economical and effective to learn from a powerful teacher than to discover reasoning abilities from scratch [[1]](https://arxiv.org/abs/2501.12948).![Figure 14: Benchmark comparison distillation and RL on a smaller 32B model. Annotated figure from the DeepSeek-R1 technical report](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png)
Image 14: A benchmark comparison of distillation and RL on a smaller 32B model from the DeepSeek-R1 technical report.

This finding highlights a key trade-off. Distillation is a practical and efficient strategy, but true breakthroughs in intelligence may still require the more computationally intensive path of large-scale RL on powerful base models. The table above would have been even more insightful if it included a comparison with a model trained using the full SFT+RL hybrid approach on the same 32B architecture, as well as a baseline showing the performance of the original, non-distilled 32B model.

After dissecting the four techniques and seeing them embodied in DeepSeek-R1, we can step back to evaluate the release's broader significance and limitations.

## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 series is a significant event for the AI community. The open MIT license, combined with an unusually detailed technical report, provides a level of transparency that is rare for a frontier model. It offers a concrete demonstration that pure RL from a cold start can lead to the emergence of advanced reasoning and self-correction, without the need for supervised warm-up data [[1]](https://arxiv.org/abs/2501.12948).

When compared to OpenAI's o1, DeepSeek-R1 shows comparable performance on key math, coding, and reasoning benchmarks. However, R1 appears to be more inference-efficient, suggesting different philosophical bets by the two labs. DeepSeek seems to have invested heavily in a complex, multi-stage training pipeline, while o1 may lean more on expensive inference-time scaling to achieve its results [[4]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners), [[12]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

However, any direct comparison is limited by the secrecy surrounding o1. We do not know its model size, whether it uses a Mixture-of-Experts (MoE) architecture, or the exact mix of training techniques employed. The strength of the respective base models also differs, making it difficult to attribute performance gaps to any single factor. A truly fair comparison is not possible without more transparency from OpenAI.

There is also the reality of training costs. The DeepSeek R1 paper mentions that training R1-Zero took approximately 101,000 H800 GPU hours, and the full R1 pipeline (including data creation and multiple training stages) totaled 147,000 H800 GPU hours, costing an estimated $294,000 [[1]](https://arxiv.org/abs/2501.12948). It is unclear if this figure includes the initial pre-training of the V3 base model, leaving the true incremental cost of the reasoning specialization somewhat ambiguous.

Despite these caveats, DeepSeek-R1 stands as a milestone for open-weight reasoning models. It proves that high-level reasoning capabilities are not the exclusive domain of closed labs. By providing both the models and a detailed recipe, DeepSeek has accelerated open research into all four of the primary techniques for building reasoning models.

## Developing reasoning models on a limited budget

The high cost of developing reasoning models can be discouraging for researchers and engineers with limited resources. However, several recent projects have demonstrated that it is possible to achieve impressive results on a tight budget.

One practical approach is distillation, as shown by the Sky-T1 project. A team from UC Berkeley's Sky Computing Lab used just 17,000 carefully curated samples generated by a larger reasoning model to train a 32B parameter model for less than $450. This distilled model approached the performance of an early version of o1 on several reasoning benchmarks, illustrating how effectively the capabilities of a large model can be transferred [[13]](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450).![Figure 15: Figure from the "Sky-T1: Train your own O1 preview model within $450" article](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8865a313-2326-4f07-a6dc-72cc94cb2ebe_1364x570.png)
Image 15: The performance of Sky-T1, a reasoning model trained for under $450.

Even pure RL can be applied at a smaller scale. The TinyZero project demonstrated this by training a 3B parameter model for under $30 on specific tasks like the countdown numbers game. Despite the low cost, the model exhibited emergent self-verification and reasoning traces, reinforcing the idea that cold-start RL can produce useful behaviors without massive compute [[14]](https://github.com/Jiayi-Pan/TinyZero). This emergence in smaller models is not random; it follows predictable scaling laws. Research suggests that pre-training loss, more so than just parameter count, is a key predictor for when these abilities will appear, often following a sharp transition once a critical loss threshold is passed [[20]](https://gregrobison.medium.com/emergent-properties-in-large-language-models-a-deep-research-analysis-d6886c37061b).![Figure 16: A figure from the TinyZero repository showing that the model is capable of self-verification.](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6111f4b4-cfb9-494c-8390-ec251702914b_1600x955.png)
Image 16: An example from the TinyZero repository demonstrating the model's self-verification capabilities.

Another powerful, budget-conscious technique is **journey learning**. This paradigm shifts the focus of SFT from "shortcut learning," where models are only trained on "golden" solution paths, to training on the entire problem-solving journey. This includes incorrect paths, dead ends, self-corrections, and reflections [[15]](https://arxiv.org/abs/2410.18982).![Figure 17: Journey learning, as opposed to traditional shortcut learning, includes wrong solutions paths in the SFT data. Annotated figure from the O1 Replication Journey: A Strategic Progress Report – Part 1](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0bfcd0-6d93-4c91-a0d6-28178839b7cf_1492x724.png)
Image 17: Journey learning includes incorrect solution paths in the training data, in contrast to traditional shortcut learning.

By exposing the model to the full, messy process of human (or AI) thought, journey learning reinforces self-correction mechanisms. Models trained only on perfect solutions can be brittle and struggle when they encounter novel errors. In contrast, models trained on journey-style data learn how to recognize and recover from mistakes, leading to more robust and reliable reasoning. This approach has shown significant potential, with one study reporting an 8% performance boost on the MATH dataset using only 327 journey learning examples compared to shortcut learning [[15]](https://arxiv.org/abs/2410.18982).

Looking ahead, the most effective budget-friendly approaches will likely involve hybrid pipelines. By combining insights from these projects—using distillation for efficient knowledge transfer (Sky-T1), pure RL for emergent behaviors (TinyZero), and journey learning for robustness—it is possible to create powerful reasoning models that balance cost, performance, and reliability.

## Conclusion

We have explored the four primary approaches to building and refining reasoning models. Inference-time scaling offers performance gains with no training cost but can be expensive to serve. Pure RL is a powerful research tool that can unlock emergent, non-human-like reasoning. The SFT+RL hybrid provides a production-ready blueprint for creating stable, high-performing models. Finally, distillation offers an efficient way to transfer these capabilities to smaller models, though the results are ultimately derivative of the teacher.

The future of the most capable systems will likely be a hybrid one. We suspect that frontier models like o1, and its successors, already combine complex SFT+RL training pipelines with significant inference-time scaling. This allows them to benefit from both the robust, emergent behaviors discovered during training and the "extra thinking time" at inference.

For AI engineers, the key takeaway is strategic. There is no single best approach. The right choice depends on your specific constraints: budget, performance targets, latency requirements, and the need for novel problem-solving versus reliable execution. Instead of defaulting to the largest or most hyped proprietary model, you should match the technique to the task. By understanding the trade-offs between these four methods, you can build or select the right reasoning model for your application.

## References

- [1] [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- [2] [Analysis of OpenAI o1 vs GPT-4o](https://www.vellum.ai/blog/analysis-openai-o1-vs-gpt-4o)
- [3] [Understanding R1-Zero-Like Training: A Critical Perspective](https://arxiv.org/html/2503.20783v1)
- [4] [DeepSeek-R1 for Beginners](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners)
- [5] [What Is Model Distillation?](https://redwerk.com/blog/what-is-model-distillation)
- [6] [The State of LLM Reasoning and Inference Scaling](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling)
- [7] [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)
- [8] [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314)
- [9] [OpenAI GPT-o1 vs GPT-4o: Comparison](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison)
- [10] [Mini DeepSeek-R1: Recreating the "Aha" Moment with a 1.5B Model](https://www.philschmid.de/mini-deepseek-r1)
- [11] [What are DeepSeek-R1 Distilled Models?](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d)
- [12] [DeepSeek R1's recipe to replicate o1 and the future of reasoning LMs](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1)
- [13] [Researchers open source Sky-T1, a ‘reasoning’ AI model that can be trained for less than $450](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450)
- [14] [TinyZero GitHub Repository](https://github.com/Jiayi-Pan/TinyZero)
- [15] [O1 Replication Journey: A Strategic Progress Report – Part 1](https://arxiv.org/abs/2410.18982)
- [16] [When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling](https://arxiv.org/html/2604.10739v1)
- [17] [CoT Prompting](https://www.nvidia.com/en-us/glossary/cot-prompting)
- [18] [CS 285: Deep Reinforcement Learning, Lecture 15](http://scalable-ai.eecs.berkeley.edu/assets/lecture_slides/lecture_15.pdf)
- [19] [Knowledge Distillation in the Era of Large Language Models (LLMs)](https://medium.com/@graison/knowledge-distillation-in-the-era-of-large-language-models-llms-7b0bead7d822)
- [20] [Emergent Properties in Large Language Models: A Deep Research Analysis](https://gregrobison.medium.com/emergent-properties-in-large-language-models-a-deep-research-analysis-d6886c37061b)