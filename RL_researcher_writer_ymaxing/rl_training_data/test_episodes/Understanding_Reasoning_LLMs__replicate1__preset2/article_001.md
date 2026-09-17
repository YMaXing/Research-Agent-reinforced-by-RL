## Methods and Strategies for Building and Refining Reasoning Models

Reasoning models are set to be the key LLM specialization trend for 2025. This evolution extends beyond the patterns we already know, such as Retrieval-Augmented Generation (RAG) and domain-specific fine-tuning. Instead of just injecting knowledge, reasoning models aim to develop robust, multi-step logical capabilities.![Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.](https://substackcdn.com/image/fetch/$s_!QwUc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png)

Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.

This specialization targets complex tasks like mathematical proofs, logical puzzles, and competitive programming. It does not replace general-purpose LLMs for everyday generation, summarization, or simple question-answering. However, these advanced reasoning capabilities come with trade-offs. The gains are often accompanied by increased inference latency and cost due to longer outputs, a risk of overthinking simple tasks, and the reality that improving one capability can degrade performance in others.

This article will serve as a guide to this new frontier. We will:

1.  Explain the meaning of "reasoning model"
2.  Discuss the advantages and disadvantages of reasoning models
3.  Outline the methodology behind DeepSeek R1
4.  Describe the four main approaches to building and improving reasoning models
5.  Share thoughts on the LLM landscape following the DeepSeek V3 and R1 releases
6.  Provide tips for developing reasoning models on a tight budget

Having set the context and roadmap, we now establish a working definition of "reasoning model" that you can use to evaluate future systems and research.

## How do we define "reasoning model"?

A reasoning model is one that generates multi-step intermediate thinking to solve complex queries. This process can involve explicit token traces that we can read or hidden internal iterations that happen before an answer is produced. This stands in contrast to the direct factual recall or single-pass pattern matching that is sufficient for simpler prompts. For example, asking "What is the capital of France?" requires simple recall. But a question like "If a train leaves Paris at 8 AM traveling at 60 mph and another leaves Lyon at 9 AM traveling at 70 mph, when and where will they meet?" requires breaking the problem down into multiple logical steps.![Figure 2: A regular LLM may provide a short answer, whereas reasoning models typically include intermediate steps that reveal the thought process.](https://substackcdn.com/image/fetch/$s_!8oZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png)

Figure 2: A regular LLM may provide a short answer, whereas reasoning models typically include intermediate steps that reveal the thought process.

All modern LLMs exhibit some level of reasoning, which can be enhanced with techniques like Chain-of-Thought (CoT) prompting. However, the term "reasoning model" typically refers to specialized systems designed for excellence on difficult benchmarks, such as math olympiad problems, formal proofs, or novel puzzle-solving.

The intermediate steps these models take can manifest in two primary ways. The first is through visible thought traces, which are step-by-step outputs the user can read. The second is through invisible internal iterations, where the model allocates more computation time at inference to "think" without exposing every token of its process. This latter approach is rumored to be part of how models like OpenAI's o1 operate.![Figure 3: "Reasoning" can refer to the internal process of generating an answer or the explicit reasoning steps shown in the output.](https://substackcdn.com/image/fetch/$s_!DyRP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png)

Figure 3: "Reasoning" can refer to the internal process of generating an answer or the explicit reasoning steps shown in the output.

This shift from visible to hidden reasoning represents a key evolution from earlier techniques. The concept began with CoT prompting, where models were explicitly guided to output their intermediate steps. As this proved effective, the process became more automated in what are now called test-time scaling models. These systems self-direct their reasoning process, generating 'hidden' thinking tokens internally before producing a final answer. This effectively turns a prompting strategy into a core model behavior [[18]](https://www.nvidia.com/en-us/glossary/cot-prompting). This automation is a breakthrough, allowing AI to handle complex reasoning tasks with greater autonomy.

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.

## When should we use reasoning models?

Before diving into the technical details, it is important to know when reasoning models are truly needed. They deliver the highest returns on tasks that require decomposition, multi-step logic, or self-correction, such as puzzles, advanced mathematics, and competitive coding. For tasks like summarization, simple factual question-answering, or creative writing, where direct generation is sufficient, they are often overkill.

Deploying a reasoning model also comes with practical downsides. The verbose intermediate steps lead to higher latency and token costs, and can frustrate users in conversational settings. Furthermore, there is the risk of "overthinking." Research has shown that accuracy can follow an inverted U-shaped curve relative to reasoning length, where a model second-guesses a correct initial answer and performance drops [[19]](https://arxiv.org/html/2604.10739v1).![Figure 4: The key strengths and weaknesses of reasoning models.](https://substackcdn.com/image/fetch/$s_!lnf2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png)

Figure 4: The key strengths and weaknesses of reasoning models.

Understanding when to deploy these specialized models is the first step. The next is understanding how they are built. This leads us to a concrete, open pipeline that demonstrates how these capabilities are created at scale.

## A brief look at the DeepSeek training pipeline

The release of DeepSeek-R1 provided the first detailed, open-source look into how a state-of-the-art reasoning model is built. The project introduced three related models, each representing a different stage or approach in the development process.![Figure 5: Development process of DeepSeek's three different reasoning models that are discussed in the DeepSeek R1 technical report.](https://substackcdn.com/image/fetch/$s_!z-dr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png)

Figure 5: The development process for DeepSeek's three reasoning models.

First is **DeepSeek-R1-Zero**, a model trained using a "cold-start" pure reinforcement learning (RL) approach. It was developed directly from the DeepSeek-V3 base model, skipping the conventional Supervised Fine-Tuning (SFT) stage that typically precedes RL. This method relies on verifiable reward signals, such as whether a math problem's final answer is correct or if a piece of code passes its unit tests [[1]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners).

Next is **DeepSeek-R1**, the flagship reasoning model. It builds on R1-Zero by incorporating additional SFT stages and further RL training. This multi-stage refinement process is designed to improve the readability of the reasoning traces and enhance overall performance, making it more aligned with human preferences [[2]](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1).

Finally, there are the **DeepSeek-R1-Distill** models. These are smaller, more efficient models created by training on the high-quality, step-by-step reasoning outputs generated by the full-scale R1 model. This is not classical, logit-based knowledge distillation. Instead, it is a form of SFT where smaller models learn to mimic the reasoning patterns of a more powerful "teacher" model [[3]](https://redwerk.com/blog/what-is-model-distillation).

The DeepSeek pipeline incorporates all four main techniques for building reasoning models. This allows for a direct comparison of their mechanisms, emergent phenomena, and empirical outcomes, which we will now examine in depth.

## The 4 main ways to build and improve reasoning models

There are currently four key techniques used to build specialized reasoning models and enhance the reasoning abilities of LLMs. While the exact workings of proprietary models like OpenAI's o1 and o3 remain unknown, they are rumored to combine multiple training and inference-time strategies.

### 1) Inference-time scaling

Inference-time scaling refers to allocating more computational resources during inference to improve a model's output. It is analogous to giving a human extra time to think through a problem. This approach connects to the concept of test-time compute scaling laws, which suggest that performance can improve by dedicating more computation at the moment a query is made, not just during training [[4]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).

Common methods include Chain-of-Thought (CoT) prompting, where a model is explicitly asked to "think step by step" [[5]](https://arxiv.org/abs/2205.11916).![Figure 6: An example of classic CoT prompting from the "Large Language Models are Zero-Shot Reasoners" paper. (Source: Kojima et al. [[5]](https://arxiv.org/abs/2205.11916))](https://substackcdn.com/image/fetch/$s_!VFAa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png)

Figure 6: An example of classic CoT prompting from the "Large Language Models are Zero-Shot Reasoners" paper. (Source: Kojima et al. [[5]](https://arxiv.org/abs/2205.11916))

More advanced techniques involve generating multiple potential solutions and using a selection mechanism. This can be as simple as **majority voting** or as complex as **beam search** and **Monte Carlo Tree Search (MCTS)**. These search algorithms often rely on a **Process Reward Model (PRM)**, which evaluates the correctness of each intermediate reasoning step, to guide the search toward the most promising solution path [[6]](https://arxiv.org/abs/2408.03314).![Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. (Source: Annotated from Snell et al. [[6]](https://arxiv.org/abs/2408.03314))](https://substackcdn.com/image/fetch/$s_!YGJO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png)

Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. (Source: Annotated from Snell et al. [[6]](https://arxiv.org/abs/2408.03314))

Interestingly, the DeepSeek-R1 technical report categorizes both PRMs and MCTS under "unsuccessful attempts," stating that their benefits were limited compared to the computational overhead they introduced during large-scale RL [[7]](https://arxiv.org/abs/2501.12948). This does not necessarily mean these techniques are useless. It is possible DeepSeek still applies them at the application layer, separate from the core model training, or that their specific implementation was not optimal.

This finding aligns with a growing body of research challenging the assumption that more thinking always leads to better answers. Studies have applied the economic law of diminishing marginal returns to test-time compute, revealing that beyond a certain point, additional reasoning provides little benefit and can even be harmful. This "overthinking" can cause a model to abandon a correct initial answer, an event termed a "negative flip." The optimal thinking length varies by task difficulty, with simpler problems suffering from overthinking much earlier than complex ones [[19]](https://arxiv.org/html/2604.10739v1).

The high cost of models like OpenAI's o1 and o3 compared to general-purpose models like GPT-4o is likely due to this heavy use of inference-time computation. Generating and evaluating multiple reasoning paths is far more resource-intensive than producing a single, direct answer [[8]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison).

### 2) Pure reinforcement learning (RL)

The second approach, exemplified by DeepSeek-R1-Zero, is pure reinforcement learning. Unlike typical RLHF pipelines, which start with a model already fine-tuned on human-written examples (SFT), pure RL is applied directly to the base model. This "cold-start" process relies on automated, verifiable reward signals instead of a reward model trained on human preferences.![Figure 8: The development process of the DeepSeek-R1-Zero model.](https://substackcdn.com/image/fetch/$s_!_9Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png)

Figure 8: The development process of the DeepSeek-R1-Zero model.

In the R1 paper, the reward function has two main components. **Accuracy rewards** provide a binary signal (correct or incorrect) based on whether the final answer to a math or coding problem matches the ground truth. **Format rewards** incentivize the model to structure its output correctly, such as by enclosing its reasoning within `<think>` tags [[7]](https://arxiv.org/abs/2501.12948), [[9]](https://www.nature.com/articles/s41586-025-09422-z).

A key phenomenon observed during this process is the "Aha moment." This is a point in training where the model spontaneously begins to generate long, complex reasoning traces and exhibit self-correction patterns, even for simple questions [[1]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners). It starts using phrases like "Wait, let me reevaluate" without being explicitly taught to do so.![Figure 9: An example from the DeepSeek R1 technical report showing the emergence of the "Aha moment." (Source: Guo et al. [[7]](https://arxiv.org/abs/2501.12948))](https://substackcdn.com/image/fetch/$s_!Prn2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png)

Figure 9: An example from the DeepSeek R1 technical report showing the emergence of the "Aha moment." (Source: Guo et al. [[7]](https://arxiv.org/abs/2501.12948))

The RL algorithm used by DeepSeek, Group Relative Policy Optimization (GRPO), is key to this cold-start process. Unlike other RL methods like PPO, GRPO is a simpler, critic-less algorithm. For a given prompt, it generates multiple responses, calculates the average reward for the group, and then normalizes each response's reward against this group mean and standard deviation. This process creates a clean, learnable signal of how much better or worse a given reasoning trace was compared to its siblings, without the need to train a separate value network, saving memory and compute [[20]](http://scalable-ai.eecs.berkeley.edu/assets/lecture_slides/lecture_15.pdf), [[21]](https://ghost.oxen.ai/why-grpo-is-important-and-how-it-works).

However, some research offers a more critical perspective. A study examining R1-Zero-like training suggests this "Aha moment" may not be entirely emergent [[10]](https://arxiv.org/html/2503.20783v1). The analysis found that base models, including DeepSeek-V3-Base, already generate self-reflection keywords before any RL is applied. The paper also identifies a potential bias in Group Relative Policy Optimization (GRPO), the RL algorithm used by DeepSeek, which may artificially encourage longer responses.

Despite this debate, DeepSeek-R1-Zero remains a landmark, as it was the first open demonstration that a model could develop sophisticated reasoning capabilities through pure RL, without being pre-loaded with human-written reasoning examples.

### 3) Supervised finetuning and reinforcement learning (SFT + RL)

The third method is a hybrid approach that combines Supervised Fine-Tuning with Reinforcement Learning. This is the pipeline used to create the flagship DeepSeek-R1 model, and it is designed to produce more stable and higher-performing results than pure RL alone.![Figure 10: The development process of the DeepSeek-R1 model.](https://substackcdn.com/image/fetch/$s_!19pK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdf7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png)

Figure 10: The development process of the DeepSeek-R1 model.

The process has multiple stages [[7]](https://arxiv.org/abs/2501.12948):
1.  **Cold-Start SFT:** The process begins by fine-tuning the base model on a small, "cold-start" dataset of a few thousand high-quality reasoning examples. This initial SFT phase helps stabilize the subsequent RL training by providing the model with a basic template for coherent, step-by-step thinking.
2.  **Reasoning-Oriented RL:** The model then undergoes large-scale RL training, similar to the R1-Zero process. However, in addition to accuracy and format rewards, a **language consistency reward** is introduced. This penalizes the model for mixing languages (e.g., English and Chinese) in its responses, improving readability even if it causes a slight dip in raw accuracy on some tasks.
3.  **Rejection Sampling and General SFT:** Next, the RL-tuned model is used to generate a large synthetic dataset of hundreds of thousands of correct reasoning traces. This data is combined with general-purpose instruction-following data and used for another round of SFT. This step broadens the model's capabilities beyond pure reasoning.
4.  **Final RL Polish:** The final stage involves another round of RL, this time mixing verifiable reasoning tasks with general preference-tuning using a standard reward model. This polishes the model for helpfulness and harmlessness, resulting in the final, user-friendly DeepSeek-R1.

This iterative, multi-stage pipeline allows the final model to inherit the powerful reasoning abilities discovered through RL while ensuring its outputs are readable, consistent, and aligned with human preferences. The result is a model that achieves state-of-the-art performance on reasoning benchmarks, rivaling closed-source competitors like OpenAI's o1.![Figure 11: Benchmark comparison of OpenAI o1 and DeepSeek R1 models. (Source: Annotated from Guo et al. [[7]](https://arxiv.org/abs/2501.12948))](https://substackcdn.com/image/fetch/$s_!22Cm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png)

Figure 11: Benchmark comparison of OpenAI o1 and DeepSeek R1 models. (Source: Annotated from Guo et al. [[7]](https://arxiv.org/abs/2501.12948))

### 4) Pure supervised finetuning (SFT) and distillation

To recap, we have covered three primary methods for building reasoning models: inference-time scaling, which uses more compute at runtime; pure RL, which teaches reasoning from scratch using verifiable outcomes; and the SFT+RL hybrid, which refines RL-discovered abilities for production use. The fourth and final approach is pure supervised finetuning, most notably used in the form of distillation.

DeepSeek used this method to create its R1-Distill models. This process involves taking the powerful DeepSeek-R1 model and using it to generate a large dataset of around 800,000 high-quality, step-by-step reasoning solutions. Smaller, open-source base models like Qwen and Llama are then fine-tuned on this synthetic dataset [[11]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d).![Figure 12: The development process of DeepSeek-R1-Distill models.](https://substackcdn.com/image/fetch/$s_!xUjE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png)

Figure 12: The development process of DeepSeek-R1-Distill models.

This is different from traditional distillation, which often involves matching the output probabilities (logits) of the teacher model. Here, the student model simply learns to replicate the reasoning text generated by the teacher. DeepSeek developed these distilled models to make advanced reasoning capabilities more accessible, as the massive 671B-parameter R1 model is impractical for most users to run [[12]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond).![Figure 13: Benchmark comparison of distilled versus non-distilled models. (Source: Annotated from Guo et al. [[7]](https://arxiv.org/abs/2501.12948))](https://substackcdn.com/image/fetch/$s_!XwZe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png)

Figure 13: Benchmark comparison of distilled versus non-distilled models. (Source: Annotated from Guo et al. [[7]](https://arxiv.org/abs/2501.12948))

So, how effective is this approach? The DeepSeek report shows that while distillation is less powerful than the full-scale R1 model, it significantly outperforms pure RL when applied to smaller models. For example, they ran a large-scale RL experiment on a 32B model (Qwen2.5-32B-Zero) and found it performed worse than the distilled version of the same size (DeepSeek-R1-Distill-Qwen-32B) across all benchmarks [[7]](https://arxiv.org/abs/2501.12948).![Figure 14: Benchmark comparison of distillation and RL on a smaller 32B model. (Source: Annotated from Guo et al. [[7]](https://arxiv.org/abs/2501.12948))](https://substackcdn.com/image/fetch/$s_!5_5L!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png)

Figure 14: Benchmark comparison of distillation and RL on a smaller 32B model. (Source: Annotated from Guo et al. [[7]](https://arxiv.org/abs/2501.12948))

This suggests that certain advanced reasoning behaviors may be emergent properties of very large models and are difficult for smaller models to discover on their own through RL. It is more efficient to "teach" them these patterns through distillation.

This highlights a fundamental challenge in distilling reasoning: it is not just about transferring knowledge, but about transferring an emergent capability. Chain-of-thought is often considered an emergent property of models exceeding 100B parameters. Smaller models lack the capacity to replicate this behavior organically, and simply showing them examples can lead to a shallow mimicry rather than a deep transfer of the underlying skill. This can result in a loss of nuanced reasoning and brittle performance on out-of-distribution problems [[22]](https://ojs.aaai.org/index.php/AAAI/article/view/29821/31426).

The table above could have been more useful with two additional comparisons: the performance of the base Qwen2.5-32B model and the full DeepSeek-R1 model. This would have provided a complete picture, from the baseline to the teacher model, showing the full spectrum of performance.

After dissecting these four techniques and seeing them embodied in the DeepSeek-R1 family, we can step back to evaluate the broader significance and limitations of this important release.

## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 models was a significant moment for the AI community. The combination of an open MIT license, a detailed technical report, and a clear demonstration of emergent reasoning from a pure RL cold start is a major contribution. It proved that high-level reasoning capabilities need not remain the exclusive domain of closed-door labs.

When comparing DeepSeek-R1 to OpenAI's o1, we see a notable contrast. On benchmarks for math, coding, and reasoning, their performance is often comparable. However, DeepSeek-R1 appears to be more inference-efficient, suggesting a different architectural philosophy. DeepSeek seems to have placed a training-heavy bet, investing immense computational resources into the RL process to bake reasoning capabilities into the model's weights. In contrast, o1 is rumored to lean more heavily on inference-time scaling, using more compute at runtime to achieve its results [[8]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison).

However, any direct comparison is limited by the lack of transparency from OpenAI. We do not know the size of the o1 model, its architecture, or the exact mix of techniques used in its training. Without these details, it is impossible to definitively attribute performance gaps to specific methods.

There is also the reality of training costs. The publicized $6M figure most likely refers to the V3 base model rather than the full R1 RL process, leaving the true incremental cost of reasoning specialization undisclosed. The DeepSeek team has never disclosed the exact GPU hours or total development cost for R1, making a full cost-benefit analysis difficult.

Ultimately, DeepSeek-R1 stands as a milestone for open-weight reasoning models. It provides a blueprint and a powerful set of tools that accelerate research into all four of the techniques we have discussed, democratizing the development of next-generation AI. But while this release democratizes knowledge, the cost of replication remains high. This raises a critical question for the broader community: how can we develop powerful reasoning models on a limited budget?

## Developing reasoning models on a limited budget

The cost of developing a reasoning model, even starting from an open-weight base, can be discouraging for researchers and engineers with limited budgets. Fortunately, several recent projects have demonstrated that it is possible to achieve impressive results without massive computational resources.

### Distillation on a Budget: The Sky-T1 Project

The Sky-T1 project from UC Berkeley's Sky Computing Lab exemplifies budget-conscious distillation. By fine-tuning an open-source model on a curated dataset of just 17,000 samples, the team trained their model for under $450 [[14]](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450). The resulting model approaches o1-preview performance on several reasoning benchmarks, showing how effective small-scale distillation can be.![Figure 15: Benchmark results for the Sky-T1 model. (Source: "Sky-T1: Train your own O1 preview model within $450" [[15]](https://novasky-ai.github.io/posts/sky-t1/))](https://substackcdn.com/image/fetch/$s_!Y8HI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8865a313-2326-4f07-a6dc-72cc94cb2ebe_1364x570.png)

Figure 15: Benchmark results for the Sky-T1 model. (Source: "Sky-T1: Train your own O1 preview model within $450" [[15]](https://novasky-ai.github.io/posts/sky-t1/))

### Pure RL at Small Scale: The TinyZero Project

The TinyZero project demonstrates that pure RL can yield results even at a much smaller scale. By training a 3B parameter model on specific tasks like the Countdown numbers game, the researchers were able to elicit emergent self-verification and reasoning traces for under $30 [[16]](https://github.com/Jiayi-Pan/TinyZero). This reinforces the finding from DeepSeek-R1-Zero: a cold-start RL process can produce useful reasoning behaviors even without massive compute, provided the task has a clear, verifiable reward signal.![Figure 16: An example from the TinyZero repository showing the model's self-verification capabilities. (Source: Pan et al. [[16]](https://github.com/Jiayi-Pan/TinyZero))](https://substackcdn.com/image/fetch/$s_!Ykdn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6111f4b4-cfb9-494c-8390-ec251702914b_1600x955.png)

Figure 16: An example from the TinyZero repository showing the model's self-verification capabilities. (Source: Pan et al. [[16]](https://github.com/Jiayi-Pan/TinyZero))

The emergence of such capabilities in small models is not random but can be predicted by scaling laws. Research shows that these abilities follow power-law scaling with compute, and that a model's pre-training loss is a better predictor of emergence than parameter count alone. A lower loss seems to be a prerequisite for these downstream skills to unlock during RL [[23]](https://www.emergentmind.com/topics/emergent-self-verification), [[24]](https://gregrobison.medium.com/emergent-properties-in-large-language-models-a-deep-research-analysis-d6886c37061b).

### Journey Learning: Training on the Entire Process

A third powerful, budget-friendly technique is "journey learning." This concept, explored in the O1 Replication Journey report, shifts the focus of supervised fine-tuning [[17]](https://arxiv.org/abs/2410.18982). Instead of training a model only on "shortcut" or "golden path" solutions, journey learning involves training on the entire problem-solving trajectory, including incorrect paths, self-corrections, and reflections.![Figure 17: Journey learning includes incorrect solution paths in the training data, unlike traditional shortcut learning. (Source: Annotated from Qin et al. [[17]](https://arxiv.org/abs/2410.18982))](https://substackcdn.com/image/fetch/$s_!TxCO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0bfcd0-6d93-4c91-a0d6-28178839b7cf_1492x724.png)

Figure 17: Journey learning includes incorrect solution paths in the training data, unlike traditional shortcut learning. (Source: Annotated from Qin et al. [[17]](https://arxiv.org/abs/2410.18982))

By exposing the model to mistakes and how to recover from them, journey learning reinforces self-correction mechanisms. This contrasts with shortcut-only datasets, which can lead to brittle behavior when the model encounters a novel error. The O1 Replication Journey report showed that with only 327 training samples, journey learning outperformed conventional SFT by over 8% on the MATH dataset, demonstrating its powerful potential [[17]](https://arxiv.org/abs/2410.18982).

Looking ahead, the most effective budget-conscious pipelines will likely be hybrids. One could imagine combining insights from all these projects: using journey learning to create a high-quality, error-inclusive dataset, distilling it into a smaller model like Sky-T1, and then running a final, targeted RL polish similar to TinyZero. This would balance cost, emergent behavior, and reliability. These budget-conscious approaches provide a path forward for the entire community, complementing the large-scale industrial efforts and enriching our understanding of the core techniques.

## Conclusion

We have explored the four primary approaches to building and improving reasoning models. **Inference-time scaling** offers a way to boost performance without retraining but comes at a high serving cost. **Pure RL** provides a valuable research insight, unlocking emergent behaviors from a cold start. The **SFT+RL hybrid** offers a production-ready blueprint that balances performance with readability. Finally, **distillation** provides an efficient method for transferring capabilities to smaller models, though its performance is ultimately derivative of the teacher.

The future of the most capable AI systems is likely to be a hybrid one. We suspect that frontier models like o1, and likely future o3-class models, already combine robust SFT+RL training pipelines with sophisticated inference-time scaling. This allows them to benefit from both the deep, baked-in reasoning abilities developed during training and the dynamic, on-the-fly computational depth available at inference. This combination addresses the core trade-off: training-time methods build a strong foundation, while inference-time methods provide the flexibility to tackle novel or exceptionally difficult problems.

For AI engineers, the key takeaway is strategic. The choice of which technique to use should be matched to concrete constraints. Budget, performance targets, innovation needs, and deployment latency all play a role. There is no one-size-fits-all answer. Instead of defaulting to the largest proprietary model available, a clear understanding of these trade-offs allows you to build more efficient, targeted, and cost-effective AI systems. This means evaluating whether the high cost of an o1-class model is justified for your use case, or if a smaller, distilled model could achieve 90% of the performance for a fraction of the cost. It is about making an informed engineering decision rather than chasing the state-of-the-art.

## References

- [1] [DeepSeek-R1 for Beginners](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners)
- [2] [DeepSeek R1's recipe to replicate o1 and the future of reasoning LMs](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1)
- [3] [What Is Model Distillation? How Teams Are Cloning GPT-Class AI Into Models 10x Cheaper](https://redwerk.com/blog/what-is-model-distillation)
- [4] [State of LLM Reasoning and Inference Scaling](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling)
- [5] [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)
- [6] [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314)
- [7] [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- [8] [GPT-o1 vs GPT-4o Comparison](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison)
- [9] [DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning](https://www.nature.com/articles/s41586-025-09422-z)
- [10] [Understanding R1-Zero-Like Training: A Critical Perspective](https://arxiv.org/html/2503.20783v1)
- [11] [What are DeepSeek-R1 distilled models?](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d)
- [12] [The Complete Guide to DeepSeek Models: From V3 to R1 and Beyond](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)
- [13] [China's DeepSeek says its hit AI model cost just $294,000 to train](https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18)
- [14] [Researchers open source Sky-T1, a ‘reasoning’ AI model that can be trained for less than $450](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450)
- [15] [Sky-T1: Train your own O1 preview model within $450](https://novasky-ai.github.io/posts/sky-t1/)
- [16] [TinyZero GitHub Repository](https://github.com/Jiayi-Pan/TinyZero)
- [17] [O1 Replication Journey: A Strategic Progress Report – Part 1](https://arxiv.org/abs/2410.18982)
- [18] [Chain of Thought (CoT) Prompting](https://www.nvidia.com/en-us/glossary/cot-prompting)
- [19] [When More Thinking Hurts: Overthinking in LLM Test-Time Compute Scaling](https://arxiv.org/html/2604.10739v1)
- [20] [GRPO Lecture Slides](http://scalable-ai.eecs.berkeley.edu/assets/lecture_slides/lecture_15.pdf)
- [21] [Why GRPO is Important and How it Works](https://ghost.oxen.ai/why-grpo-is-important-and-how-it-works)
- [22] [Distilling Step-by-Step! Outperforming Larger Language Models with Less Training Data and Smaller Model Sizes](https://ojs.aaai.org/index.php/AAAI/article/view/29821/31426)
- [23] [Emergent Self-Verification](https://www.emergentmind.com/topics/emergent-self-verification)
- [24] [Emergent Properties in Large Language Models: A Deep Research Analysis](https://gregrobison.medium.com/emergent-properties-in-large-language-models-a-deep-research-analysis-d6886c37061b)
- [25] [Multi-Agent Reasoning Frameworks](https://www.emergentmind.com/topics/multi-agent-reasoning-frameworks)
- [26] [What is Multi-Agent Reasoning in AI?](https://milvus.io/ai-quick-reference/what-is-multiagent-reasoning-in-ai)
- [27] [OmniScience: A Large Reasoning Model for General Science](https://arxiv.org/html/2503.17604v1)
- [28] [A Survey on LLMs in Scientific Discovery](https://www.linkedin.com/posts/omarsar_new-paper-a-survey-on-llms-in-scientific-activity-7330614738780844032-fToW)
</article>