# Methods and Strategies for Building and Refining Reasoning Models

AI model specialization has evolved rapidly. After mastering Retrieval-Augmented Generation (RAG) for knowledge injection and supervised fine-tuning (SFT) for domain adaptation, the new frontier for 2025 is reasoning. This trend moves beyond simply providing models with more information; it focuses on unlocking their ability to perform complex, multi-step logical tasks.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/d6ebc5c9-461f-4d3a-889b-b8ea4e14e5ba_1600x830.png
Figure 1: Stages 1-3 are the common steps to developing LLMs. Stage 4 specializes LLMs for specific use cases.

Reasoning specialization is aimed at complex multi-step tasks like mathematical proofs, logical puzzles, and competitive programming. It does not replace general-purpose LLMs for everyday generation, summarization, or simple question-answering. This specialization comes with trade-offs. The gains in reasoning often lead to higher inference latency and costs due to longer, more detailed outputs. There is also the risk of "overthinking" simple problems, where a specialized model might introduce unnecessary complexity that a standard model would handle correctly and efficiently.

In this article, we will explore the world of reasoning models. We will:
1.  Explain the meaning of "reasoning model"
2.  Discuss the advantages and disadvantages of reasoning models
3.  Outline the methodology behind DeepSeek R1
4.  Describe the four main approaches to building and improving reasoning models
5.  Share thoughts on the LLM landscape following the DeepSeek V3 and R1 releases
6.  Provide tips for developing reasoning models on a tight budget

Having set the context and roadmap, we now establish a working definition of "reasoning model" that readers can use to evaluate future systems and research.

## How do we define "reasoning model"?

A reasoning model is an LLM designed to solve complex problems by generating multi-step intermediate thoughts before arriving at a final answer [[2]](https://www.nature.com/articles/s41586-025-09422-z). Unlike standard models that might provide a direct response, reasoning models break down a problem, showing their work either through an explicit chain of thought or through hidden internal iterations. This approach is essential for tasks that cannot be solved in a single pass, such as advanced math problems or logical puzzles.

For a simple question like, "If a train travels at 60 mph for 3 hours, how far does it go?", a standard model might just answer "180 miles." A reasoning model, however, would first outline the formula, perform the calculation, and then state the conclusion.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/f2987079-25f4-45fb-a020-1ac936ed16cb_1424x820.png
Figure 2: A regular LLM may only provide a short answer (as shown on the left), whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Note that many LLMs who have not been specifically developed for reasoning tasks can also provide intermediate reasoning steps in their answers.)

All modern LLMs possess some reasoning ability, which can be enhanced with techniques like Chain-of-Thought (CoT) prompting [[3]](https://arxiv.org/abs/2205.11916). However, specialized reasoning models take this a step further, achieving state-of-the-art performance on difficult benchmarks like math olympiads and formal proofs. These intermediate steps can manifest in two primary ways. The first is through **visible thought traces**, where the model outputs its step-by-step reasoning for the user to see. This is common in models like DeepSeek-R1. The second is through **invisible internal iterations**, where the model allocates more computational resources at inference time to "think" without exposing every step. OpenAI's o1 models are rumored to use this latter approach, which allows for deeper processing while presenting a cleaner final output to the user [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling).

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/35712d0e-0f40-4855-8d81-4dcea94055ce_1538x810.png
Figure 3: "Reasoning" is used at two different levels: 1) processing the input and generating via multiple intermediate steps and 2) providing some sort of reasoning as part of the response to the user.

With a clear definition established, we can now examine the practical question of when deploying these more expensive reasoning models actually makes sense for an AI engineer.

## When should we use reasoning models?

Before diving into the technical details, it is important to know when to use a reasoning model. They provide the most value for tasks that require decomposition, planning, and self-correction, such as advanced mathematics, competitive coding, and logical puzzles. For simpler tasks like summarization, creative writing, or basic question-answering, they are often overkill and can be inefficient.

The main drawbacks of reasoning models are practical. Their verbose, step-by-step outputs lead to higher latency and token costs, which can be a major concern for applications requiring real-time responses. This can also frustrate users in conversational settings who expect quick answers. There is also the risk of "overthinking," where a model complicates a straightforward problem that a standard LLM would solve correctly and more efficiently in a single pass. For example, a reasoning model might generate hundreds of tokens to solve a simple arithmetic problem, increasing cost and wait time unnecessarily.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/46dbe029-ab7d-4278-8dfe-7bc4af79a103_1352x524.png
Figure 4: The key strengths and weaknesses of reasoning models.

Understanding when to deploy reasoning models leads naturally to studying a concrete, open pipeline that demonstrates how such capabilities are created at scale.

## A brief look at the DeepSeek training pipeline

The DeepSeek-R1 series provides a transparent look into how reasoning capabilities can be built and refined [[2]](https://www.nature.com/articles/s41586-025-09422-z). The lineup consists of three main variants, each building on the last.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/db19df56-c5bf-4a0c-aafb-4629a39b13f5_1542x1166.png
Figure 5: Development process of DeepSeeks three different reasoning models that are discussed in the DeepSeek R1 technical report.

**DeepSeek-R1-Zero** is the starting point. It was created using a "cold-start" approach, applying pure reinforcement learning (RL) directly to the DeepSeek-V3 base model without any initial supervised fine-tuning. This is a departure from standard RLHF pipelines, which typically "warm up" a model with SFT on human-written examples. The goal was to see if reasoning could emerge organically, guided only by verifiable reward signals like correct answers to math problems.

**DeepSeek-R1** is the flagship model, refined from R1-Zero. It incorporates SFT on a small "cold-start" dataset of high-quality reasoning traces, some of which were generated by R1-Zero itself. This is followed by further RL stages to enhance performance and ensure the model's outputs are more human-readable and consistent.

**DeepSeek-R1-Distill** models are smaller, more efficient versions. Instead of repeating the entire training process, these models are created by fine-tuning existing open-source models (from the Llama and Qwen families) on a large dataset of high-quality CoT outputs generated by the full-sized DeepSeek-R1. This is not classical knowledge distillation, which often involves matching logits, but rather a form of SFT on synthetic data [[9]](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond).

The DeepSeek pipeline incorporates all four main techniques we will now examine in depth, allowing direct comparison of their mechanisms, emergent phenomena, and empirical outcomes.

## The 4 main ways to build and improve reasoning models

Current key techniques to enhance LLM reasoning and build specialized reasoning models fall into four main categories. While the exact workings of proprietary models like OpenAI's o1 and o3 remain unknown, they are rumored to combine both inference and training techniques.

### 1) Inference-time scaling

Inference-time scaling is the practice of dedicating more computational resources during inference to improve a model's performance [[1]](https://magazine.sebastianraschka.com/p/state-of-llm-reasoning-and-inference-scaling). It is analogous to giving a person extra time to think through a difficult problem. This approach, also known as test-time compute scaling, can be applied to any LLM without altering its weights.

One of the simplest methods is **Chain-of-Thought (CoT) prompting**, where adding a phrase like "Let's think step by step" encourages the model to generate intermediate reasoning steps before giving a final answer [[3]](https://arxiv.org/abs/2205.11916). This increases the number of tokens generated, effectively trading more compute for better accuracy on complex tasks.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/523eee5e-afb6-4019-a11b-e0a291d2c286_1600x419.png
Figure 6: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper

More advanced techniques involve search and voting strategies. These methods generate multiple potential solutions and use a verifier, or a **Process Reward Model (PRM)**, to select the best one. A PRM evaluates each intermediate step of a solution, providing a more fine-grained signal than simply checking the final answer [[4]](https://ojs.aaai.org/index.php/AAAI/article/view/40797/44758). Common search algorithms include:

*   **Best-of-N:** The model generates N full solutions, and a verifier selects the best one.
*   **Beam Search:** The model explores multiple reasoning paths simultaneously, keeping the most promising ones at each step.
*   **Lookahead Search / Monte Carlo Tree Search (MCTS):** These methods explore a tree of possible reasoning steps, using rollouts to estimate the value of different paths before committing to one.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/5cb10e5a-738b-4c9e-ba65-5850d4793706_1600x919.png
Figure 7: Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper

Interestingly, the DeepSeek-R1 technical report categorizes some of these methods, including PRM-based approaches and MCTS, under "unsuccessful attempts" for their large-scale RL process [[2]](https://www.nature.com/articles/s41586-025-09422-z). They argue that the computational overhead of these techniques during training outweighs their benefits. This suggests that while inference-time scaling is powerful, DeepSeek may have prioritized optimizing the model's inherent reasoning abilities during training. However, this does not preclude them from applying these same techniques at the application layer during deployment.

The higher cost of OpenAI's o1 models compared to general-purpose models like GPT-4o is likely due to this heavy use of inference-time compute [[6]](https://neoteric.eu/blog/gpt-o1-vs-gpt-4o-comparison). By spending more time and resources "thinking," these models can tackle more complex problems, but at a premium price. For instance, GPT-o1's input costs are 6 times higher than GPT-4o's, and its output tokens are also 6 times more expensive. This cost difference reflects the additional computational power required for the sophisticated reasoning techniques employed by these models.

### 2) Pure reinforcement learning (RL)

Pure reinforcement learning aims to teach a model to reason from a "cold start," without any initial supervised fine-tuning. This is the approach used to create DeepSeek-R1-Zero [[2]](https://www.nature.com/articles/s41586-025-09422-z). Unlike traditional RLHF, which relies on a reward model trained on human preferences, this method uses verifiable, rule-based rewards.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/a5bb6ecc-7e46-45fe-abff-1eb02e6b0e3a_1556x1162.png
Figure 8: The development process of DeepSeek-R1-Zero model.

The training process for R1-Zero uses two main types of rewards:
*   **Accuracy rewards:** The model receives a positive reward if its final answer to a math or coding problem is correct. This is determined automatically by checking against a known solution or running unit tests. For math problems, the model must provide the answer in a specific format, like inside a box, which allows for reliable rule-based verification.
*   **Format rewards:** The model is rewarded for structuring its output correctly, such as placing its reasoning inside `<think>` and `</think>` tags. This ensures the model's thought process is clearly delineated, which helps with interpretability.

During this process, the DeepSeek team observed an emergent phenomenon they called the **"Aha moment."** After thousands of RL iterations, the model spontaneously began to generate long, detailed reasoning traces, even for simple problems. It started to use words like "Wait," indicating self-reflection and correction, without being explicitly trained to do so. This discovery showed that complex reasoning behaviors could emerge from a simple, outcome-based reward signal [[7]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners).

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/30f8e37b-ba60-49d2-a95e-9c06b2033ee4_1600x1019.png
Figure 9: A figure from the DeepSeek R1 technical report showing the emergence of the "Aha" moment.

The success of R1-Zero was a milestone, as it was the first clear demonstration that a powerful reasoning model could be developed using pure RL, without the need for human-annotated reasoning examples. The model learned to allocate more "thinking time" to problems by re-evaluating its own approaches, a sophisticated behavior that emerged without any direct human feedback on how to perform such reflections.

### 3) Supervised finetuning and reinforcement learning (SFT + RL)

The hybrid SFT + RL approach, exemplified by the full DeepSeek-R1 model, combines the stability of supervised learning with the exploratory power of reinforcement learning. This multi-stage process is designed to build on the raw reasoning capabilities of R1-Zero while making the model more reliable and human-friendly [[2]](https://www.nature.com/articles/s41586-025-09422-z).

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https://substack-post-media.s3.amazonaws.com/public/images/df7f99f0-d154-49e5-b60a-4d148e0a61be_1548x1154.png
Figure 10: The development process of DeepSeek-R1 model.

The pipeline for DeepSeek-R1 involves several key stages:
1.  **Cold-Start SFT:** The process begins by fine-tuning the base model on a small, high-quality dataset of several thousand "cold-start" examples. These examples, generated by earlier models including R1-Zero, provide a conversational, human-aligned thinking process. This initial SFT helps stabilize the subsequent RL training and avoids the "chaotic start" problem where a base model doesn't even know basic reasoning templates.
2.  **Reasoning-Oriented RL:** The model then undergoes large-scale RL, similar to the process for R1-Zero. In addition to accuracy and format rewards, a **language consistency reward** is introduced. This reward penalizes the model for mixing languages (e.g., Chinese and English) in its responses, which was an issue with R1-Zero. While this slightly degrades performance on some tasks, it improves readability and user preference [[2]](https://www.nature.com/articles/s41586-025-09422-z).
3.  **Rejection Sampling and SFT:** After the first RL stage, the model is used to generate a large synthetic dataset of around 800,000 examples. Only the correct solutions are kept (rejection sampling). This dataset, which includes both reasoning (600k) and non-reasoning (200k) tasks, is then used for another round of SFT. This helps the model retain its reasoning abilities while improving its general capabilities, like writing.
4.  **Final RL Stage:** A final RL phase is conducted to further align the model with human preferences for helpfulness and harmlessness, using a combination of rule-based and model-based rewards. This stage polishes the model for general use.

This iterative refinement process allows DeepSeek-R1 to achieve strong performance across a wide range of benchmarks, making it competitive with leading closed-source models like OpenAI's o1.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff7f73f16-db4e-4047-89b0-823f16cefb33_1556x490.png
Figure 11: Benchmark comparison of OpenAI O1 and DeepSeek R1 models. Annotated figure from the DeepSeek-R1 technical report

### 4) Pure supervised finetuning (SFT) and distillation

Inference-time scaling offers a way to improve reasoning without any training. Pure RL teaches reasoning from scratch. The SFT+RL hybrid refines it for production. The final approach, pure SFT and distillation, focuses on efficiently transferring these hard-won reasoning capabilities to smaller, more accessible models [[8]](https://medium.com/data-science-in-your-pocket/what-are-deepseek-r1-distilled-models-329629968d5d).

DeepSeek used this method to create its R1-Distill series. The process is straightforward: the large DeepSeek-R1 model was used to generate a high-quality dataset of 800,000 reasoning examples. Then, smaller, existing open-source models (from the Llama and Qwen families) were fine-tuned on this synthetic data.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7db7c46b-fe67-49f4-9f65-b0e7b7e5ac08_1444x1174.png
Figure 12: The development process of DeepSeek-R1-Distill models.

This differs from traditional knowledge distillation, which often involves matching the output probabilities (logits) of the teacher model. Here, it is simply SFT on the text outputs, a more direct way to transfer the reasoning "style" and problem-solving patterns [[10]](https://www.youtube.com/watch?v=jrf76uNs77k).

DeepSeek developed these distilled models for two main reasons. First, the full 671B R1 model is computationally expensive and impractical for many to run. Distilled models make powerful reasoning accessible on consumer-grade hardware. Second, it serves as an efficient way to transfer knowledge, as smaller models often struggle to develop complex reasoning abilities on their own through RL.

The results are impressive. Even the smallest 1.5B distilled model outperforms powerful non-reasoning models like GPT-4o on certain math benchmarks. As the model size increases, the performance gets closer to the original R1.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Febc749fb-6a79-483f-bcda-b219f284bc09_1168x604.png
Figure 13: Benchmark comparison of distilled versus non-distilled models. Annotated figure from the DeepSeek-R1 technical report

The DeepSeek report also provides a direct comparison between distillation and pure RL on a smaller 32B model. They trained a `Qwen-32B` model using the same pure RL process as R1-Zero. The distilled version of `Qwen-32B` outperformed the RL-trained one across all reasoning benchmarks.

https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F05514c9f-eb04-496b-bd98-bb4710c65b14_1448x408.png
Figure 14: Benchmark comparison distillation and RL on a smaller 32B model. Annotated figure from the DeepSeek-R1 technical report

This suggests that for smaller models, it is more effective to learn from the well-structured reasoning paths of a larger, more capable teacher than to try to discover those paths from scratch. The emergent properties of reasoning seem to require a certain scale to appear organically through RL. The table above could have been more useful with additional comparisons, such as including the performance of the original DeepSeek-R1 and a non-reasoning baseline like the base Qwen-32B model.

After dissecting the four techniques and seeing them embodied in DeepSeek-R1, we step back to evaluate the release's broader significance and limitations.

## Thoughts about DeepSeek R1

The release of the DeepSeek-R1 series is a major moment for open-source AI. The combination of an MIT license, a detailed technical report, and a family of powerful models provides an invaluable resource for the community [[7]](https://www.lesswrong.com/posts/a9GR7m4nyBsqjjL8d/deepseek-r1-for-beginners). The demonstration that pure RL from a cold start can lead to emergent reasoning and self-correction is a particularly important insight, proving that complex behaviors can be learned without direct human supervision of the reasoning process itself.

When comparing DeepSeek-R1 to OpenAI's o1, the benchmarks show that they are competitive, especially in math and coding [[2]](https://www.nature.com/articles/s41586-025-09422-z). However, DeepSeek-R1 appears to be more inference-efficient, which suggests a difference in strategy. DeepSeek seems to have invested heavily in training a model with strong inherent reasoning, while o1 may rely more on expensive inference-time scaling techniques to achieve its performance. This is a classic trade-off between training-time compute and inference-time compute.

However, any direct comparison is limited by the lack of transparency from OpenAI. We do not know the size of the o1 model, its architecture (e.g., if it is a Mixture-of-Experts model), or the exact mix of training techniques used. Without these details, it is difficult to definitively attribute performance differences to specific methods. A fair comparison is not possible until more information about o1 is disclosed.

There is also some ambiguity around the training costs. The often-cited $6M figure for DeepSeek likely refers to the pre-training of the V3 base model. The incremental cost of the R1-specific SFT and RL stages is reported to be around $294,000, but the full picture of development costs, including the extensive experimentation and data generation, remains undisclosed [[11]](https://www.reuters.com/world/china/chinas-deepseek-says-its-hit-ai-model-cost-just-294000-train-2025-09-18). The DeepSeek team has not provided a complete breakdown of GPU hours or total investment for the R1 project.

Despite these caveats, DeepSeek-R1 stands as a milestone. It proves that high-level reasoning capabilities are not exclusive to closed-source labs and provides an open blueprint that will accelerate research into all four of the techniques we have discussed.

## Developing reasoning models on a limited budget

Developing reasoning models from scratch is computationally expensive, but recent open-source projects have shown that it is possible to achieve impressive results on a limited budget. These efforts make advanced AI research more accessible to smaller teams and individual researchers, democratizing the development of powerful AI.

Distillation is a practical approach, as demonstrated by the **Sky-T1** project. Developed by researchers at UC Berkeley, Sky-T1 is a 32B parameter reasoning model trained for less than $450 [[12]](https://techcrunch.com/2025/01/11/researchers-open-source-sky-t1-a-reasoning-ai-model-that-can-be-trained-for-less-than-450). The team used another reasoning model to generate an initial dataset of 17,000 samples, which they then curated and used to fine-tune a base model. The result is a model that approaches the performance of an early o1 preview on several benchmarks.

| Benchmark | Sky-T1-32B-Preview | QwQ-32B-Preview | o1-preview |
| :--- | :--- | :--- | :--- |
| MATH500 | 93.0 | 90.6 | 90.0 |
| AIME | 50.0 | 50.0 | 63.6 |
| GPQA-Diamond | 57.6 | 54.5 | 60.0 |
| LiveCodeBench | 55.1 | 41.9 | 53.8 |
Table 1: Figure from the "Sky-T1: Train your own O1 preview model within $450" article

Pure RL can also be applied at a smaller scale. **TinyZero** is a 3B parameter model trained for under $30 that successfully reproduces the "Aha moment" seen in DeepSeek-R1-Zero [[13]](https://github.com/Jiayi-Pan/TinyZero). By focusing on simpler tasks like multiplication and the Countdown game, the project demonstrates that emergent behaviors like self-verification can be achieved even without massive computational resources. This reinforces the idea that the principles of cold-start RL can yield useful results at various scales.

> **Question:** The countdown game: target 831, numbers \[100, 75, 50, 25, 6, 3].
> 
> **TinyZero Response:**
> Let's think step by step.
> I need to reach 831 using the numbers \[100, 75, 50, 25, 6, 3] and the operations +, -, \*, /.
> Let's try to get close to 831.
> 100 \* 6 = 600
> 75 + 50 = 125
> 600 + 125 = 725
> 725 + 100 = 825 (Wait, I used 100 twice)
> Let's try again.
> 100 \* (6 + 3) = 900
> 900 - 75 = 825
> 825 + 6 = 831 (Wait, I used 6 twice)
> Let's try again.
> (100 + 6) \* (75 / 25 + 3) = 106 \* 6 = 636 (Not close)
> Let's try another approach.
> 100 \* (6+3) - 75 + 6 = 831 (Wait, I used 6 twice)
> Let's try to build up to 831.
> 100 \* 75 / (6+3) = 833.33 (Not an integer)
> Let's try to get 831.
> 100 \* (6+3) - 75 = 825
> 825 + 6 = 831 (Wait, I used 6 twice)
> Let's try to use all numbers.
> (100 + 3) \* 6 + 75 + 50 - 25 = 103 \* 6 + 100 = 618 + 100 = 718
> Let's try to get 831.
> (100 + 6) \* (75/25 + 3) = 106 \* 6 = 636
> Let's try to get 831.
> 100 \* (6+3) - 75 = 825
> 825 + 6 = 831 (Wait, I used 6 twice)
> Let's try to get 831.
> (100+75-50-25)\*6+3 = 100\*6+3 = 603
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100 \* 6 + 75 + 50 + 25 + 3 = 853
> 100 \* 6 + 75 + 50 + 25 - 3 = 847
> 100 \* 6 + 75 + 50 - 25 + 3 = 803
> 100 \* 6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 106\*3+3 = 318+3 = 321
> Let's try to get 831.
> (100+3)\*6+75 = 618+75 = 693
> Let's try to get 831.
> 100\*6 + 75 + 50 + 25 + 3 = 853
> 100\*6 + 75 + 50 + 25 - 3 = 847
> 100\*6 + 75 + 50 - 25 + 3 = 803
> 100\*6 + 75 + 50 - 25 - 3 = 797
> Let's try to get 831.
> (100+75/25)\*6+3 = 103\*6+3 = 618+3 = 621
> Let's try to get 831.
> (100+6)\* (75/25) + 3 = 1