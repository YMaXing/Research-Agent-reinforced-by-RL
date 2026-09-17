# Methods and Strategies for Building and Refining Reasoning Models

AI model specialization has evolved rapidly. After mastering Retrieval-Augmented Generation (RAG) for knowledge injection and supervised fine-tuning (SFT) for domain adaptation, the new frontier for 2025 is reasoning. This trend moves beyond simply providing models with more information; it focuses on unlocking their ability to perform complex, multi-step logical tasks.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/d6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png
Image 1: Stages 1-3 are the common steps for developing LLMs, while Stage 4 specializes them for specific use cases. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

Reasoning models are not meant to replace general-purpose LLMs. Their strength lies in tackling problems that require decomposition and self-correction, such as mathematical proofs, logical puzzles, and competitive programming. This specialization comes with trade-offs. The gains in reasoning often lead to higher inference latency and costs due to longer, more detailed outputs. There's also the risk of "overthinking" simple problems, where a specialized model might introduce unnecessary complexity that a standard model would handle correctly and efficiently.

In this article, we will explore the world of reasoning models. We will:
1.  Explain the meaning of "reasoning model"
2.  Discuss the advantages and disadvantages of reasoning models
3.  Outline the methodology behind DeepSeek R1
4.  Describe the four main approaches to building and improving reasoning models
5.  Share thoughts on the LLM landscape following the DeepSeek V3 and R1 releases
6.  Provide tips for developing reasoning models on a tight budget

Having set the context and roadmap, we will now establish a working definition of "reasoning model" that you can use to evaluate future systems and research.

## How do we define "reasoning model"?

A reasoning model is an LLM designed to solve complex problems by generating multi-step intermediate thoughts before arriving at a final answer [[21]](https://www.nature.com/articles/s41586-025-09422-z). Unlike standard models that might provide a direct response, reasoning models break down a problem, showing their work either through an explicit chain of thought or through hidden internal iterations. This approach is essential for tasks that cannot be solved in a single pass, such as advanced math problems or logical puzzles.

For a simple question like, "If a train travels at 60 mph for 3 hours, how far does it go?", a standard model might just answer "180 miles." A reasoning model, however, would first outline the formula, perform the calculation, and then state the conclusion.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/f2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png
Image 2: A regular LLM may provide a short answer, whereas reasoning models often include intermediate steps. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

All modern LLMs possess some reasoning ability, which can be enhanced with techniques like Chain-of-Thought (CoT) prompting [[24]](https://arxiv.org/abs/2205.11916). However, specialized reasoning models take this a step further, achieving state-of-the-art performance on difficult benchmarks like math olympiads and formal proofs.

These intermediate steps can manifest in two ways. The first is through visible thought traces, where the model outputs its step-by-step reasoning for the user to see. The second is through invisible internal iterations, where the model allocates more computational resources at inference time to "think" without exposing every step. OpenAI's o1 models are rumored to use this latter approach [[33]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png
Image 3: Reasoning can refer to both the internal process of generating a response and the explicit inclusion of that process in the output. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.

## When should we use reasoning models?

Before diving into the technical details, it is important to know when to use a reasoning model. They provide the most value for tasks that require decomposition, planning, and self-correction, such as advanced mathematics, competitive coding, and logical puzzles. For simpler tasks like summarization, creative writing, or basic question-answering, they are often overkill.

The main drawbacks of reasoning models are practical. Their verbose, step-by-step outputs lead to significantly higher latency and token costs. This can frustrate users in conversational applications who expect quick answers. There is also the risk of "overthinking," where a model complicates a straightforward problem that a standard LLM would solve correctly in a single pass.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png
Image 4: The key strengths and weaknesses of reasoning models. (Source [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

Understanding when to deploy these specialized models is key. This leads us to a concrete, open-source pipeline that demonstrates how these capabilities are created at scale.

## A brief look at the DeepSeek training pipeline

The DeepSeek-R1 series provides a transparent look into how reasoning capabilities can be built and refined [[21]](https://www.nature.com/articles/s41586-025-09422-z). The lineup consists of three main variants, each building on the last.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/db19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png
Image 5: The development process of DeepSeek's three reasoning models, as described in their technical report. (Image by Sebastian Raschka from [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

**DeepSeek-R1-Zero** is the starting point. It was created using a "cold-start" approach, applying pure reinforcement learning (RL) directly to the DeepSeek-V3 base model without any initial supervised fine-tuning. This is a departure from standard RLHF pipelines, which typically "warm up" a model with SFT on human-written examples. The goal was to see if reasoning could emerge organically, guided only by verifiable reward signals like correct answers to math problems.

**DeepSeek-R1** is the flagship model, refined from R1-Zero. It incorporates SFT on a small "cold-start" dataset of high-quality reasoning traces, some of which were generated by R1-Zero itself. This is followed by further RL stages to enhance performance and ensure the model's outputs are more human-readable and consistent.

**DeepSeek-R1-Distill** models are smaller, more efficient versions. Instead of repeating the entire training process, these models are created by fine-tuning existing open-source models (from the Llama and Qwen families) on a large dataset of high-quality CoT outputs generated by the full-sized DeepSeek-R1. This is not classical knowledge distillation, which often involves matching logits, but rather a form of SFT on synthetic data [[14]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond).

The DeepSeek pipeline incorporates all four main techniques for building reasoning models. We will now examine each in depth, allowing for a direct comparison of their mechanisms and outcomes.

## The 4 main ways to build and improve reasoning models

Current techniques for enhancing LLM reasoning fall into four main categories. While the exact workings of proprietary models like OpenAI's o1 and o3 remain undisclosed, they are rumored to combine several of these training and inference strategies.

### 1) Inference-time scaling

Inference-time scaling is the practice of dedicating more computational resources during inference to improve a model's performance [[33]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling). It is analogous to giving a person extra time to think through a difficult problem. This approach, also known as test-time compute scaling, can be applied to any LLM without altering its weights.

One of the simplest methods is **Chain-of-Thought (CoT) prompting**, where adding a phrase like "Let's think step by step" encourages the model to generate intermediate reasoning steps before giving a final answer [[24]](https://arxiv.org/abs/2205.11916). This increases the number of tokens generated, effectively trading more compute for better accuracy on complex tasks.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png
Image 6: An example of classic CoT prompting from the 2022 paper "Large Language Models are Zero-Shot Reasoners". (Source [arxiv.org](https://arxiv.org/abs/2205.11916))

More advanced techniques involve search and voting strategies. These methods generate multiple potential solutions and use a verifier, or a **Process Reward Model (PRM)**, to select the best one. A PRM evaluates each intermediate step of a solution, providing a more fine-grained signal than simply checking the final answer [[32]](https://ojs.aaai.org/index.php/AAAI/article/view/40797/44758). Common search algorithms include:

*   **Best-of-N:** The model generates N full solutions, and a verifier selects the best one.
*   **Beam Search:** The model explores multiple reasoning paths simultaneously, keeping the most promising ones at each step.
*   **Lookahead Search / Monte Carlo Tree Search (MCTS):** These methods explore a tree of possible reasoning steps, using rollouts to estimate the value of different paths before committing to one.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png
Image 7: Search-based methods like Best-of-N, Beam Search, and Lookahead Search rely on a Process Reward Model to evaluate and select the best reasoning path. (Source [arxiv.org](https://arxiv.org/abs/2408.03314))

Interestingly, the DeepSeek-R1 technical report categorizes some of these methods, including PRM-based approaches and MCTS, under "unsuccessful attempts" for their large-scale RL process [[21]](https://www.nature.com/articles/s41586-025-09422-z). They argue that the computational overhead of these techniques during training outweighs their benefits. This suggests that while inference-time scaling is powerful, DeepSeek may have prioritized optimizing the model's inherent reasoning abilities during training. However, this does not preclude them from applying these same techniques at the application layer during deployment.

The higher cost of OpenAI's o1 models compared to general-purpose models like GPT-4o is likely due to this heavy use of inference-time compute [[38]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison). By spending more time and resources "thinking," these models can tackle more complex problems, but at a premium price.

### 2) Pure reinforcement learning (RL)

Pure reinforcement learning aims to teach a model to reason from a "cold start," without any initial supervised fine-tuning. This is the approach used to create DeepSeek-R1-Zero [[21]](https://www.nature.com/articles/s41586-025-09422-z). Unlike traditional RLHF, which relies on a reward model trained on human preferences, this method uses verifiable, rule-based rewards.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/a5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png
Image 8: The development process of the DeepSeek-R1-Zero model, which uses pure reinforcement learning on a base model. (Image by Sebastian Raschka from [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

The training process for R1-Zero uses two main types of rewards:
*   **Accuracy rewards:** The model receives a positive reward if its final answer to a math or coding problem is correct. This is determined automatically by checking against a known solution or running unit tests.
*   **Format rewards:** The model is rewarded for structuring its output correctly, such as placing its reasoning inside `<think>` and `</think>` tags.

During this process, the DeepSeek team observed an emergent phenomenon they called the **"Aha moment."** After thousands of RL iterations, the model spontaneously began to generate long, detailed reasoning traces, even for simple problems. It started to use words like "Wait," indicating self-reflection and correction, without being explicitly trained to do so. This discovery showed that complex reasoning behaviors could emerge from a simple, outcome-based reward signal [[7]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners).

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png
Image 9: The "Aha moment" observed during the training of DeepSeek-R1-Zero, where the model spontaneously begins to use reflective language like "Wait". (Source [www.nature.com](https://www.nature.com/articles/s41586-025-09422-z))

The success of R1-Zero was a milestone, as it was the first clear demonstration that a powerful reasoning model could be developed using pure RL, without the need for human-annotated reasoning examples.

### 3) Supervised finetuning and reinforcement learning (SFT + RL)

The hybrid SFT + RL approach, exemplified by the full DeepSeek-R1 model, combines the stability of supervised learning with the exploratory power of reinforcement learning. This multi-stage process is designed to build on the raw reasoning capabilities of R1-Zero while making the model more reliable and human-friendly [[21]](https://www.nature.com/articles/s41586-025-09422-z).

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/df7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png
Image 10: The multi-stage development process of the DeepSeek-R1 model, which combines SFT and RL. (Image by Sebastian Raschka from [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

The pipeline for DeepSeek-R1 involves several key stages:
1.  **Cold-Start SFT:** The process begins by fine-tuning the base model on a small, high-quality dataset of several thousand "cold-start" examples. These examples, generated by earlier models including R1-Zero, provide a conversational, human-aligned thinking process. This initial SFT helps stabilize the subsequent RL training.
2.  **Reasoning-Oriented RL:** The model then undergoes large-scale RL, similar to the process for R1-Zero. In addition to accuracy and format rewards, a **language consistency reward** is introduced. This reward penalizes the model for mixing languages (e.g., Chinese and English) in its responses, which was an issue with R1-Zero. While this slightly degrades performance on some tasks, it significantly improves readability and user preference [[27]](https://www.nature.com/articles/s41586-025-09422-z).
3.  **Rejection Sampling and SFT:** After the first RL stage, the model is used to generate a large synthetic dataset of around 800,000 examples. Only the correct solutions are kept (rejection sampling). This dataset, which includes both reasoning and non-reasoning tasks, is then used for another round of SFT. This helps the model retain its reasoning abilities while improving its general capabilities, like writing.
4.  **Final RL Stage:** A final RL phase is conducted to further align the model with human preferences for helpfulness and harmlessness, using a combination of rule-based and model-based rewards.

This iterative refinement process allows DeepSeek-R1 to achieve strong performance across a wide range of benchmarks, making it competitive with leading closed-source models like OpenAI's o1.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/f7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png
Image 11: A benchmark comparison of DeepSeek-R1 and OpenAI's o1 models, showing competitive performance on various reasoning tasks. (Source [www.nature.com](https://www.nature.com/articles/s41586-025-09422-z))

### 4) Pure supervised finetuning (SFT) and distillation

Inference-time scaling offers a way to improve reasoning without any training, pure RL teaches reasoning from scratch, and the SFT+RL hybrid refines it for production. The final approach, pure SFT and distillation, focuses on efficiently transferring these hard-won reasoning capabilities to smaller, more accessible models [[11]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d).

DeepSeek used this method to create its R1-Distill series. The process is straightforward: the large DeepSeek-R1 model was used to generate a high-quality dataset of 800,000 reasoning examples. Then, smaller, existing open-source models (from the Llama and Qwen families) were fine-tuned on this synthetic data.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png
Image 12: The development process for DeepSeek-R1-Distill models, which involves SFT on data generated by the larger R1 model. (Image by Sebastian Raschka from [magazine.sebastianraschka.com](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling))

This differs from traditional knowledge distillation, which often involves matching the output probabilities (logits) of the teacher model. Here, it is simply SFT on the text outputs, a more direct way to transfer the reasoning "style" and problem-solving patterns.

DeepSeek developed these distilled models for two main reasons. First, the full 671B R1 model is computationally expensive and impractical for many to run. Distilled models make powerful reasoning accessible on consumer-grade hardware. Second, it serves as an efficient way to transfer knowledge, as smaller models often struggle to develop complex reasoning abilities on their own through RL.

The results are impressive. Even the smallest 1.5B distilled model outperforms powerful non-reasoning models like GPT-4o on certain math benchmarks. As the model size increases, the performance gets closer to the original R1.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/ebc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png
Image 13: Benchmark comparison showing the performance of DeepSeek-R1-Distill models against other popular models. (Source [arxiv.org](https://arxiv.org/abs/2501.12948))

The DeepSeek report also provides a direct comparison between distillation and pure RL on a smaller 32B model. They trained a `Qwen-32B` model using the same pure RL process as R1-Zero. The distilled version of `Qwen-32B` significantly outperformed the RL-trained one across all reasoning benchmarks.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png
Image 14: A comparison of distillation and pure RL on a 32B model shows that distillation is more effective for transferring reasoning capabilities to smaller models. (Source [arxiv.org](https://arxiv.org/abs/2501.12948))

This suggests that for smaller models, it is more effective to learn from the well-structured reasoning paths of a larger, more capable teacher than to try to discover those paths from scratch. The emergent properties of reasoning seem to require a certain scale to appear organically through RL. The table above could have been more useful with additional comparisons, such as including the performance of the original DeepSeek-R1 and a non-reasoning baseline like the base Qwen-32B model.

After dissecting the four techniques and seeing them embodied in DeepSeek-R1, we can now step back to evaluate the release's broader significance and limitations.

## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 series is a significant moment for open-source AI. The combination of an MIT license, a detailed technical report, and a family of powerful models provides an invaluable resource for the community [[7]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners). The demonstration that pure RL from a cold start can lead to emergent reasoning and self-correction is a particularly important insight.

When comparing DeepSeek-R1 to OpenAI's o1, the benchmarks show that they are competitive, especially in math and coding [[21]](https://www.nature.com/articles/s41586-025-09422-z). However, DeepSeek-R1 appears to be more inference-efficient, which suggests a difference in strategy. DeepSeek seems to have invested heavily in training a model with strong inherent reasoning, while o1 may rely more on expensive inference-time scaling techniques to achieve its performance.

However, any direct comparison is limited by the lack of transparency from OpenAI. We do not know the size of the o1 model, its architecture (e.g., if it is a Mixture-of-Experts model), or the exact mix of training techniques used. Without these details, it is difficult to definitively attribute performance differences to specific methods.

There is also some ambiguity around the training costs. The often-cited $6M figure for DeepSeek likely refers to the pre-training of the V3 base model. The incremental cost of the R1-specific SFT and RL stages is reported to be around $294,000, but the full picture of development costs remains undisclosed [[42]](https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18).

Despite these caveats, DeepSeek-R1 stands as a milestone. It proves that high-level reasoning capabilities are not exclusive to closed-source labs and provides an open blueprint that will accelerate research into all four of the techniques we have discussed.

## Developing reasoning models on a limited budget

Developing reasoning models from scratch is computationally expensive, but recent open-source projects have shown that it is possible to achieve impressive results on a limited budget. These efforts make advanced AI research more accessible to smaller teams and individual researchers.

Distillation is a practical approach, as demonstrated by the **Sky-T1** project. Developed by researchers at UC Berkeley, Sky-T1 is a 32B parameter reasoning model trained for less than $450 [[17]](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450). The team used another reasoning model to generate an initial dataset of 17,000 samples, which they then curated and used to fine-tune a base model. The result is a model that approaches the performance of an early o1 preview on several benchmarks.![Figure 15: Benchmark results for the budget-friendly Sky-T1 model.](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8865a313-2326-4f07-a6dc-72cc94cb2ebe_1364x570.png)
Image 15: Benchmark results for the budget-friendly Sky-T1 model. (Source [novasky-ai.github.io](https://novasky-ai.github.io/posts/sky-t1/))

Pure RL can also be applied at a smaller scale. **TinyZero** is a 3B parameter model trained for under $30 that successfully reproduces the "Aha moment" seen in DeepSeek-R1-Zero [[20]](https://github.com/Jiayi-Pan/TinyZero). By focusing on simpler tasks like multiplication and the Countdown game, the project demonstrates that emergent behaviors like self-verification can be achieved even without massive computational resources.![Figure 16: An example from the TinyZero repository showing the model's ability to self-verify its reasoning.](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6111f4b4-cfb9-494c-8390-ec251702914b_1600x955.png)
Image 16: An example from the TinyZero repository showing the model's ability to self-verify its reasoning. (Source [github.com](https://github.com/Jiayi-Pan/TinyZero))

A third promising technique is **journey learning**. This paradigm, proposed by researchers on the O1 Replication Journey, contrasts with "shortcut learning," where models are only trained on correct solution paths. In journey learning, the model is also exposed to the entire exploration process, including incorrect paths, reflections, and self-corrections.

By training on full trajectories that include mistakes, the model learns not just *what* the correct answer is, but *how* to recover from errors and find it. This reinforces self-correction mechanisms and makes the model more robust when facing novel problems. In initial experiments with only 327 training samples, journey learning improved performance on the MATH dataset by over 8% compared to traditional SFT on "golden" solutions.![Figure 17: Journey learning includes incorrect solution paths in the training data, in contrast to traditional shortcut learning, which only uses correct paths.](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a0bfcd0-6d93-4c91-a0d6-28178839b7cf_1492x724.png)
Image 17: Journey learning, as opposed to traditional shortcut learning, includes incorrect solution paths in the SFT data. (Source [arxiv.org](https://arxiv.org/abs/2410.18982))

Looking ahead, the most effective budget-conscious approaches will likely be hybrids. By combining insights from these projects—distillation from Sky-T1, small-scale RL from TinyZero, and the robust training data from journey learning—it will be possible to create powerful reasoning models that balance cost, emergent capabilities, and reliability.

## Conclusion

We have explored the four primary approaches to building and improving reasoning models. Inference-time scaling offers a training-free way to boost performance but comes at a high serving cost. Pure RL, as demonstrated by DeepSeek-R1-Zero, is a powerful research tool for unlocking emergent behaviors like self-reflection. The SFT+RL hybrid used for DeepSeek-R1 provides a production-ready blueprint for creating stable, high-performing models. Finally, distillation is an efficient method for transferring these capabilities to smaller models, though their performance is ultimately derivative of the teacher.

The future of reasoning models is likely hybrid. The most capable systems will probably combine robust SFT+RL training pipelines with sophisticated inference-time scaling—a pattern we suspect is already at play in OpenAI's o1 and will likely define the next generation of frontier models.

For AI engineers, the key is to match the right technique to the specific constraints of a project. The choice between these approaches is a strategic one, balancing budget, performance targets, latency requirements, and the need for innovation. Instead of defaulting to the largest proprietary model, understanding these trade-offs allows you to build more efficient and effective AI systems.

## References

- [1] [https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners)
- [2] [https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1)
- [3] [https://www.vellum.ai/blog/the-training-of-deepseek-r1-and-ways-to-use-it](https://www.vellum.ai/blog/the-training-of-deepseek-r1-and-ways-to-use-it)
- [4] [https://thelmbook.com/articles#!./DeepSeek-R1.md](https://thelmbook.com/articles#!./DeepSeek-R1.md)
- [5] [https://huggingface.co/blog/open-r1/mini-r1-contdown-game](https://huggingface.co/blog/open-r1/mini-r1-contdown-game)
- [6] [https://www.philschmid.de/mini-deepseek-r1](https://www.philschmid.de/mini-deepseek-r1)
- [7] [https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners)
- [8] [https://arxiv.org/html/2503.20783v1](https://arxiv.org/html/2503.20783v1)
- [9] [https://github.com/sail-sg/oat-zero](https://github.com/sail-sg/oat-zero)
- [10] [https://www.youtube.com/watch?v=jrf76uNs77k](https://www.youtube.com/watch?v=jrf76uNs77k)
- [11] [https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d)
- [12] [https://medium.com/@tahirbalarabe2/deepseek-r1-explained-chain-of-thought-reinforcement-learning-and-model-distillation-0eb165d928c9](https://medium.com/@tahirbalarabe2/deepseek-r1-explained-chain-of-thought-reinforcement-learning-and-model-distillation-0eb165d928c9)
- [13] [https://redwerk.com/blog/what-is-model-distillation](https://redwerk.com/blog/what-is-model-distillation)
- [14] [https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)
- [15] [https://www.linkedin.com/posts/muhammad-ali-masood-phd_researchers-open-source-sky-t1-a-reasoning-activity-7285536292493299712-M8b5](https://www.linkedin.com/posts/muhammad-ali-masood-phd_researchers-open-source-sky-t1-a-reasoning-activity-7285536292493299712-M8b5)
- [16] [https://ivan.vlaevski.com/ai-models-go-cheaper-novasky-t1-sets-a-new-standard](https://ivan.vlaevski.com/ai-models-go-cheaper-novasky-t1-sets-a-new-standard)
- [17] [https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450)
- [18] [https://www.technology.org/2025/01/14/sky-t1-open-source-ai-model-for-advanced-reasoning-you-can-train-for-less-than-450](https://www.technology.org/2025/01/14/sky-t1-open-source-ai-model-for-advanced-reasoning-you-can-train-for-less-than-450)
- [19] [https://campustechnology.com/articles/2025/01/15/uc-berkeley-announces-sky-t1-32b-open-source-ai-model.aspx?s=ct_in_070225](https://campustechnology.com/articles/2025/01/15/uc-berkeley-announces-sky-t1-32b-open-source-ai-model.aspx?s=ct_in_070225)
- [20] [https://github.com/Jiayi-Pan/TinyZero](https://github.com/Jiayi-Pan/TinyZero)
- [21] [https://www.nature.com/articles/s41586-025-09422-z](https://www.nature.com/articles/s41586-025-09422-z)
- [22] [https://thelmbook.com/articles#!./DeepSeek-R1.md](https://thelmbook.com/articles#!./DeepSeek-R1.md)
- [23] [https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1](https://www.interconnects.ai/p/deepseek-r1-recipe-for-o1)
- [24] [https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)
- [25] [https://artgor.medium.com/paper-review-deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement-learning-edf4343dcf3a](https://artgor.medium.com/paper-review-deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement-learning-edf4343dcf3a)
- [26] [https://transitions.substack.com/p/the-laymans-introduction-to-deepseek](https://transitions.substack.com/p/the-laymans-introduction-to-deepseek)
- [27] [https://www.nature.com/articles/s41586-025-09422-z](https://www.nature.com/articles/s41586-025-09422-z)
- [32] [https://ojs.aaai.org/index.php/AAAI/article/view/40797/44758](https://ojs.aaai.org/index.php/AAAI/article/view/40797/44758)
- [33] [https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling)
- [37] [https://www.uctoday.com/unified-communications/chatgpt-4o-vs-o1-which-openai-model-is-best](https://www.uctoday.com/unified-communications/chatgpt-4o-vs-o1-which-openai-model-is-best)
- [38] [https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison)
- [42] [https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18](https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18)
- [43] [https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1](https://epoch.ai/gradient-updates/what-went-into-training-deepseek-r1)
- [44] [https://www.yahoo.com/news/research-exposes-deepseek-ai-training-165025904.html](https://www.yahoo.com/news/research-exposes-deepseek-ai-training-165025904.html)
- [45] [https://hardforum.com/threads/ai-markets-were-deceived-to-believe-in-deepseeks-low-training-costs-they-are-actually-400-times-higher-than-the-reported-figure.2039555](https://hardforum.com/threads/ai-markets-were-deceived-to-believe-in-deepseeks-low-training-costs-they-are-actually-400-times-higher-than-the-reported-figure.2039555)
- [46] [https://prompt.16x.engineer/blog/deepseek-r1-cost-pricing-speed](https://prompt.16x.engineer/blog/deepseek-r1-cost-pricing-speed)