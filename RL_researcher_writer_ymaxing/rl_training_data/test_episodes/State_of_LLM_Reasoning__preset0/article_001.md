# 2025’s Guide to Inference-Time Compute Scaling

In 2025, building complex agentic systems requires LLMs that can reliably perform multi-step problem-solving, a task where direct-answer models often fail. This has pushed the AI engineering community to prioritize stronger reasoning capabilities. The release of models like DeepSeek-R1 sparked a surge of research into making LLMs "think" more effectively, leading to a landscape of techniques blending inference-time scaling, pure reinforcement learning (RL), hybrid RL with supervised fine-tuning (SFT), and SFT with distillation.

This article provides a comprehensive survey of the latest research on inference-time compute scaling, focusing on the diverse methods published post-DeepSeek-R1 that regulate and scale test-time computation.![The four main categories of implementing reasoning models I explained in Understanding Reasoning LLMs. This article focuses on inference-time-scaling methods.](https://substackcdn.com/image/fetch/$s_!IOSP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf9e2677-652a-4af1-9f57-dc0c253d2198_1448x1260.png)
Image 1: The four main categories of implementing reasoning models I explained in Understanding Reasoning LLMs. This article focuses on inference-time-scaling methods.

We will begin by examining the four main categories of reasoning model development to understand how inference-time scaling fits into the broader landscape.

## Implementing and improving reasoning in LLMs: The four main categories

Reasoning models are a class of LLMs that generate an explicit or internal intermediate thought process before producing a final answer. This is a significant departure from direct-answer models, which perform a single forward pass to map an input directly to an output. This ability to "think" allows reasoning models to tackle more complex problems that require decomposition and multi-step logic.![Side-by-side comparison of a basic LLM's one-line answer and a reasoning LLM's explanatory response.](https://substackcdn.com/image/fetch/$s_!ZsN9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8abbfe39-f656-4845-b376-18c1e563210a_1326x564.png)
Image 2: Side-by-side comparison of a basic LLM's one-line answer and a reasoning LLM's explanatory response.

There are two primary ways to improve an LLM's performance: increasing training compute or increasing inference compute. **Training compute** involves modifying the model's weights, typically through reinforcement learning or supervised fine-tuning. This is a one-time, upfront cost. **Inference compute**, on the other hand, refers to the additional FLOPs used at test time to generate a response, without altering the model's weights. The simplest example of this is chain-of-thought (CoT) prompting, which guides the model to produce a longer, more detailed reasoning trace, thereby increasing the computational cost of generating a single answer.![Accuracy improvements can be achieved through increased training or test-time compute, where test-time compute is synonymous with inference-time compute and inference-time scaling.](https://substackcdn.com/image/fetch/$s_!pgyl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddde6f39-3b88-4962-9d02-2cf767dc82e9_1484x994.png)
Image 3: Accuracy improvements can be achieved through increased training or test-time compute, where test-time compute is synonymous with inference-time compute and inference-time scaling. (Source [https://openai.com/index/learning-to-reason-with-llms/](https://openai.com/index/learning-to-reason-with-llms/))

In practice, most state-of-the-art systems combine extensive train-time preparation with dynamic test-time thinking. Relying on training alone can lead to "reward hacking," where a model learns to exploit the reward function without genuinely improving its reasoning. Conversely, pure inference scaling on a weak base model yields limited gains because the model lacks the foundational knowledge to reason effectively. This has led to four main categories for developing reasoning models [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).![Four categories of reasoning models development.](https://substackcdn.com/image/fetch/$s_!_2dU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5e5fdf9-e72c-497b-9cf4-b4e3c24f33f1_1600x591.png)
Image 4: The four main categories for developing reasoning models.

**1. Inference-time compute scaling** is the core focus of this article. This approach uses additional computation at inference to improve performance without changing the model's weights. Techniques include generating multiple reasoning paths and selecting the best one (e.g., best-of-N sampling), or using search algorithms like beam search guided by a reward model. Models like OpenAI's o1 are known for this capability. The DeepSeek R1 paper reported that explicit inference-time methods were largely unsuccessful for their model, but it's important to note that their training process implicitly encourages inference scaling by producing longer, more detailed responses, which naturally increases inference costs [[11]](https://arxiv.org/abs/2501.12948).

**2. Pure reinforcement learning** aims to teach models to reason by rewarding them for correct final answers, without providing explicit examples of how to reason. This approach, used to train DeepSeek-R1-Zero, allows the model to discover novel reasoning strategies that may differ from human thought processes. However, it faces significant challenges. The search space is vast, and providing a reward only at the end of a long reasoning chain makes it difficult for the model to assign credit to the specific steps that led to the correct answer. This "sparse reward" problem can make training inefficient and unstable. DeepSeek-R1-Zero, for instance, developed advanced reasoning patterns like self-reflection and verification through pure RL, but also suffered from issues like poor readability and language mixing [[11]](https://arxiv.org/abs/2501.12948).

**3. Reinforcement learning and supervised fine-tuning** is a hybrid approach that combines the strengths of both methods. It starts with an SFT phase to teach the model basic reasoning patterns from human-annotated examples. This provides a strong starting point and helps stabilize the subsequent RL phase. The model is then further refined with RL, allowing it to explore and improve upon the initial strategies. This is the approach used to create the final DeepSeek-R1 from DeepSeek-R1-Zero. The initial SFT on "cold-start" data helped align the model's outputs to a more conversational, human-like style, which was then scaled and enhanced through multiple RL stages [[11]](https://arxiv.org/abs/2501.12948).

**4. Supervised fine-tuning and model distillation** involves training a smaller "student" model to replicate the outputs of a more powerful "teacher" model. This differs from traditional distillation, where the student mimics the teacher's internal states (logits). Here, the student is trained on the high-quality reasoning traces generated by the teacher. This allows smaller, more efficient models to achieve the reasoning capabilities of much larger models. The DeepSeek-R1-Distill series is a prime example of this approach, where smaller models like Qwen and Llama were fine-tuned on outputs from the larger DeepSeek-R1, achieving strong reasoning performance with a fraction of the parameters [[11]](https://arxiv.org/abs/2501.12948), [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

With these four categories mapped out, we will now focus on the first one: inference-time compute scaling.

## Inference-time compute scaling methods

The core idea behind inference-time compute scaling is that allowing a model to "think longer" on a problem can improve its performance, much like a human spending more time on a difficult puzzle. This extra "thinking" translates to additional computational cost at inference time.

The most classic example is chain-of-thought (CoT) prompting. By simply instructing a model to "think step by step," we encourage it to generate a detailed reasoning trace before giving a final answer [[36]](https://arxiv.org/abs/2205.11916). This increases the number of tokens generated, which in turn raises the monetary cost and latency of the API call [[18]](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more), [[19]](https://aclanthology.org/2025.emnlp-main.165.pdf), [[20]](https://www.aussieai.com/research/cot-optimization), [[32]](https://arxiv.org/html/2406.09136v1), [[33]](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought). While effective, this is a basic form of inference scaling.![An example of classic CoT prompting from the 2022 "Large Language Models are Zero-Shot Reasoners" paper.](https://substackcdn.com/image/fetch/$s_!Knds!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d37faa4-3261-492c-85a4-766926b8c17c_1600x419.png)
Image 5: An example of classic CoT prompting from the 2022 "Large Language Models are Zero-Shot Reasoners" paper [[36]](https://arxiv.org/abs/2205.11916).

More advanced techniques use search and voting strategies. **Majority voting**, used in methods like self-consistency, involves generating multiple reasoning paths in parallel and selecting the answer that appears most frequently [[37]](https://openreview.net/forum?id=l19DmXbwPK), [[38]](https://icml.cc/virtual/2025/oral/47195), [[39]](https://arxiv.org/html/2512.15146v1). **Beam search**, on the other hand, is a sequential process. It explores multiple reasoning paths at each step, pruning the less promising ones and expanding only the top candidates. This search is often guided by a Process Reward Model (PRM), which scores the correctness of each intermediate step [[40]](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf), [[41]](https://cameronrwolfe.substack.com/p/reward-models).![Different search-based methods rely on a process-reward-based model to select the best answer.](https://substackcdn.com/image/fetch/$s_!O9a-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ad9742b-993f-4ecd-8f80-2fa41d43164b_1334x798.png)
Image 6: Different search-based methods rely on a process-reward-based model to select the best answer. (Source [https://www.arxiv.org/abs/2502.12521](https://www.arxiv.org/abs/2502.12521) [[29]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM))

These methods represent different ways of allocating additional compute to improve reasoning. We will now examine how these ideas are implemented in recent research, starting with the `s1` paper.

## s1: Simple test-time scaling

The paper "[s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393)" (January 2025) presents a hybrid approach that combines a small, curated SFT dataset with a simple yet effective inference-time control mechanism [[1]](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8), [[2]](https://huggingface.co/papers/2501.19393). This distinguishes it from pure distillation methods, as it actively regulates the amount of thinking at inference time. The s1K dataset consists of 1,000 questions with reasoning traces selected based on three criteria: difficulty, diversity, and quality. This careful curation is crucial, as ablations showed that random selection or focusing on a single criterion led to significantly worse performance.

The core mechanism is **budget forcing**, a sequential scaling technique that controls the length of the model's reasoning trace. If the model tries to stop thinking too early, the end-of-thinking delimiter is suppressed, and a "Wait" token is appended to the generation. This encourages the model to continue its reasoning, often leading to self-correction and verification. Conversely, if the model's reasoning becomes too long, an end-of-thinking token can be injected to force an answer. This provides direct control over the computational budget, a contrast to parallel methods like majority voting, which generate a fixed number of independent samples.![An illustration of "wait" token insertion to control the length of the output.](https://substackcdn.com/image/fetch/$s_!qk_K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e7f4d94-9f8f-4353-87ad-78f3cba7b9cd_1154x854.png)
Image 7: An illustration of "wait" token insertion to control the length of the output. (Source [https://arxiv.org/abs/2501.19393](https://arxiv.org/abs/2501.19393) [[22]](https://arxiv.org/html/2502.04404v1))

This technique is reminiscent of the "aha moment" observed during the training of DeepSeek-R1, where the model spontaneously began using reflective language like "wait" to pause and reconsider its reasoning path [[11]](https://arxiv.org/abs/2501.12948). The `s1` paper formalizes this behavior as an explicit inference-time intervention. Empirical results show a strong correlation between the length of the generated response and accuracy on reasoning benchmarks [[2]](https://huggingface.co/papers/2501.19393).![The correlation between response accuracy and length.](https://substackcdn.com/image/fetch/$s_!kYWF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7f0c49b-a644-4142-bed0-7d114ecd39c2_798x456.png)
Image 8: The correlation between response accuracy and length. (Source [https://arxiv.org/abs/2501.19393](https://arxiv.org/abs/2501.19393) [[22]](https://arxiv.org/html/2502.04404v1))

The paper also demonstrates that the choice of token matters. Appending "Wait" consistently outperforms more neutral phrases like "Hmm," suggesting that the token induces a state of doubt and active reconsideration rather than just extending the generation time.![A comparison of "Wait" vs "Hmm" tokens.](https://substackcdn.com/image/fetch/$s_!Qd4X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bdfe7db-8c97-4240-8be0-11efa7abdf7c_758x510.png)
Image 9: A comparison of "Wait" vs "Hmm" tokens. (Source [https://arxiv.org/abs/2501.19393](https://arxiv.org/abs/2501.19393) [[22]](https://arxiv.org/html/2502.04404v1))

The paper acknowledges its limitations, noting that it does not compare budget forcing against other search methods like beam search or compute-optimal search. This leaves open questions about how this simple, effective technique stacks up against more complex, resource-intensive methods.

## Other noteworthy research papers on inference-time compute scaling

The volume of research on inference-time compute scaling has been substantial, making it impractical to cover every paper in exhaustive detail. Instead, we will provide concise summaries of several other noteworthy papers, highlighting their core mechanisms and contributions. This will give you a broad overview of the diverse strategies being explored.

A common pattern you will notice is that many of these approaches are not purely prompt-based. They often involve a blend of training-time preparation and explicit control of inference-time compute. This is an important distinction from SFT or distillation techniques that simply train a model to produce longer outputs. The methods we will discuss here actively regulate the computational budget or reasoning process at inference time.

## Test-Time Preference Optimization

"[Test-Time Preference Optimization](https://arxiv.org/abs/2501.12895)" (January 2025) introduces an iterative alignment process that operates entirely at inference time, avoiding any changes to the underlying model weights [[3]](https://icml.cc/virtual/2025/poster/46149), [[4]](https://proceedings.mlr.press/v267/li25ac.html). This positions it as a pure inference-time method. The approach uses a reward model to score multiple generated responses, selecting the best ("chosen") and worst ("rejected") ones.

The core of the method is a four-step loop:
1.  **Generation:** The model produces multiple candidate answers.
2.  **Scoring:** A reward model evaluates each candidate.
3.  **Critique:** The model generates textual critiques, analyzing the strengths of the chosen response and the weaknesses of the rejected one. These critiques serve as "textual rewards."
4.  **Refinement:** Based on these critiques, the model generates a new set of improved responses.

This loop repeats, progressively refining the output for a given query without any gradient updates.![The Test-Time Preference Optimization process.](https://substackcdn.com/image/fetch/$s_!dmJN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2a1bd16-7cf7-4898-8dce-a2d8352f76a8_1600x819.png)
Image 10: The Test-Time Preference Optimization process. (Source [https://arxiv.org/abs/2501.12895](https://arxiv.org/abs/2501.12895))

## Thoughts Are All Over the Place

"[Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://arxiv.org/abs/2501.18585)" (January 2025) identifies a phenomenon called "underthinking" in reasoning models [[5]](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme), [[6]](https://tldr.takara.ai/p/2501.18585). This occurs when a model frequently switches between different reasoning paths without sufficiently exploring any single one, leading to a decrease in final accuracy despite generating a long response.

To address this, the paper proposes the **Thought Switching Penalty (TIP)**. This is a decoding-time strategy that applies a penalty to the logits of tokens associated with thought transitions (e.g., "Alternatively"). This discourages the model from prematurely abandoning a promising line of reasoning. By forcing deeper exploration of each path, this no-fine-tuning approach improves accuracy on challenging benchmarks.![The Thought Switching Penalty method visualization.](https://substackcdn.com/image/fetch/$s_!vvCX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7111ccaa-c4c1-4c7c-84f9-74d38df3c663_1528x894.png)
Image 11: The Thought Switching Penalty method visualization. (Source [https://arxiv.org/abs/2501.18585](https://arxiv.org/abs/2501.18585))

## Trading Inference-Time Compute for Adversarial Robustness

"[Trading Inference-Time Compute for Adversarial Robustness](https://arxiv.org/abs/2501.18841)" (January 2025) investigates the relationship between inference compute and model safety [[7]](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf), [[8]](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness), [[9]](https://huggingface.co/papers/2501.18841). The paper shows that increasing inference-time compute generally improves a model's robustness to adversarial attacks, reducing the success rate of attacks even without specific adversarial training.

However, the authors highlight important exceptions. The benefits are limited in cases of policy ambiguity, where an attacker can find "loopholes" that are not clear violations. The paper also introduces two novel attack strategies that specifically target reasoning models:
*   **Think Less:** An attack that tries to reduce the amount of computation the model performs.
*   **Nerd Sniping:** An attack that traps the model in unproductive thinking loops, wasting its computational budget.

These findings suggest that while inference scaling is a valuable tool for improving safety, it is not a complete solution on its own and opens up new attack surfaces [[10]](https://www.youtube.com/watch?v=6Yxc6uh0RyE), [[17]](https://arxiv.org/html/2507.15974v1).![An analysis of trading inference-time compute for adversarial robustness.](https://substackcdn.com/image/fetch/$s_!Gt2_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F704acd82-10a8-4879-9bd3-26bb67c3155f_1600x1173.png)
Image 12: An analysis of trading inference-time compute for adversarial robustness. (Source [https://arxiv.org/abs/2501.18841](https://arxiv.org/abs/2501.18841))

## Chain-of-Associated-Thoughts

"[CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning](https://arxiv.org/abs/2502.02390)" (February 2025) proposes a framework that combines Monte Carlo Tree Search (MCTS) with an "associative memory" [[21]](https://arxiv.org/html/2502.02390v3). This memory acts as a dynamic knowledge base during inference, allowing the model to recall earlier reasoning steps and incorporate newly generated information without losing context.

This synergy between the structured exploration of MCTS and the adaptive learning of the associative memory helps the model systematically explore diverse reasoning pathways at test time, leading to more accurate and comprehensive final answers.![The CoAT: Chain-of-Associated-Thoughts Framework visualization.](https://substackcdn.com/image/fetch/$s_!AtpC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d0635fb-c0b4-45df-b8d3-b54254ab92b5_1600x777.png)
Image 13: The CoAT: Chain-of-Associated-Thoughts Framework visualization. (Source [https://arxiv.org/abs/2502.02390](https://arxiv.org/abs/2502.02390) [[21]](https://arxiv.org/html/2502.02390v3))

## Step Back to Leap Forward

"[Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://arxiv.org/abs/2502.0440)" (February 2025) introduces a self-backtracking mechanism that trains a model to recognize when its reasoning path is suboptimal and revise it [[22]](https://arxiv.org/html/2502.04404v1), [[23]](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947).

During training, the model learns to generate a special `<backtrack>` token when it identifies a mistake. This learned ability is then leveraged at inference time within a tree-based search algorithm. When the model generates the `<backtrack>` token, the search algorithm revisits an earlier state and explores an alternative path.

A key advantage of this approach is that it does not require an external reward model to guide the search, unlike standard process-reward-guided methods. The model itself learns to identify and correct its own errors. This allows for dynamic adjustment of both the depth and breadth of the search based on the model's self-assessed confidence.![The Step Back to Leap Forward: Self-Backtracking mechanism.](https://substackcdn.com/image/fetch/$s_!e6x3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1df5fbf3-97f2-4976-b46f-2d5196b6bdc4_1594x888.png)
Image 14: The Step Back to Leap Forward: Self-Backtracking mechanism. (Source [https://arxiv.org/abs/2502.0440](https://arxiv.org/abs/2502.0440) [[22]](https://arxiv.org/html/2502.04404v1))

## Scaling up Test-Time Compute with Latent Reasoning

"[Scaling Test-Time Computation by Implicitly Reasoning in Latent Space](https://arxiv.org/abs/2502.05171)" (February 2025) explores a different paradigm for inference scaling: recurrent depth [[24]](https://huggingface.co/papers/2502.05171), [[25]](https://openreview.net/forum?id=S3GhJooWIC), [[26]](https://neurips.cc/virtual/2025/poster/117966), [[27]](https://icml.cc/virtual/2025/51856), [[28]](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db). Instead of generating more output tokens, this approach iterates computations in the model's latent space.

This is similar to how a Recurrent Neural Network (RNN) processes information, where the model's hidden state is refined over multiple steps before producing an output. This allows the model to "think" for longer without increasing the length of the visible reasoning trace. The main drawback of this approach is the loss of interpretability. Since the reasoning happens in a high-dimensional vector space, it is not human-readable, making it difficult to debug or understand the model's thought process.![A visualization of scaling up test-time compute with latent reasoning through a recurrent depth approach.](https://substackcdn.com/image/fetch/$s_!kVPW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb82da925-5736-44ba-bed1-ea3207b06382_1516x602.png)
Image 15: A visualization of scaling up test-time compute with latent reasoning through a recurrent depth approach. (Source [https://arxiv.org/abs/2502.05171](https://arxiv.org/abs/2502.05171))

## Can a 1B LLM Surpass a 405B LLM?

"[Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling](https://arxiv.org/abs/2502.06703)" (February 2025) conducts a systematic study of the interactions between inference-time scaling, Process Reward Models (PRMs), and problem difficulty.

The paper introduces a **compute-optimal scaling strategy**, which adapts the inference budget based on the PRM being used, the size of the policy model, and the complexity of the task. The key finding is that there is no one-size-fits-all approach; the optimal strategy is highly context-dependent.

The most striking result is the evidence that a 1B parameter model, when paired with the right scaling strategy, can outperform an unscaled 405B Llama 3 model on the same benchmarks. This has significant implications for AI engineers, as it demonstrates that intelligently allocating inference compute can allow smaller, more efficient models to rival the performance of much larger ones, directly impacting trade-off decisions between cost, speed, and capability.![A comparison of compute-optimal scaling.](https://substackcdn.com/image/fetch/$s_!DiM2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c471e7f-36e7-41a8-a7e0-80bebf3c0f36_1600x1046.png)
Image 16: A comparison of compute-optimal scaling. (Source [https://arxiv.org/abs/2502.06703](https://arxiv.org/abs/2502.06703))

## Learning to Reason from Feedback at Test-Time

The method proposed in "[Learning to Reason from Feedback at Test-Time](https://www.arxiv.org/abs/2502.12521)" (February 2025) is a hybrid that blurs the line between pure inference-time and training-time techniques, as it involves updating the model's weights during inference.

The paper introduces the **OpTune optimizer**, which adjusts the model's weights based on mistakes made on previous, similar problems. Unlike sequential revision methods that add failed attempts to the prompt context, OpTune modifies the model itself. This allows the model to "remember" its errors through lightweight weight updates rather than by indefinitely growing the context length.

This approach contrasts with both parallel sampling, where each attempt is independent, and standard sequential revision, where the model's weights remain fixed. The benefit is a more persistent form of learning that does not rely on an ever-expanding prompt, making it more scalable for long-term interactions.![A visualization of the OpTune optimizer.](https://substackcdn.com/image/fetch/$s_!nJMD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1925302-7fc2-4c7b-91e9-1c0fc4f0609e_1426x652.png)
Image 17: A visualization of the OpTune optimizer. (Source [https://www.arxiv.org/abs/2502.12521](https://www.arxiv.org/abs/2502.12521) [[29]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM))

## Inference-Time Computations for LLM Reasoning and Planning

"[Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521)" (February 2025) introduces **Sys2Bench**, a comprehensive benchmark for evaluating inference-time techniques [[29]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM), [[30]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM), [[31]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM). It assesses methods like CoT, Tree-of-Thought, and Reasoning as Planning across eleven diverse tasks.

The benchmark covers five main categories:
*   Arithmetic Reasoning
*   Logical Reasoning
*   Commonsense Reasoning
*   Algorithmic Reasoning
*   Planning

The key insight from the paper is that no single inference-time technique consistently outperforms others across all task types. This forces engineers to move away from a one-size-fits-all mindset and instead match specific methods to the domains they are best suited for. The paper also provides a valuable analysis of the trade-offs between computational cost and performance for each technique.![Benchmark results for inference-time computations for LLM reasoning and planning.](https://substackcdn.com/image/fetch/$s_!Vm7j!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42115dab-1086-4035-9a64-65a83631377e_1600x1023.png)
Image 18: Benchmark results for inference-time computations for LLM reasoning and planning. (Source [https://www.arxiv.org/abs/2502.12521](https://www.arxiv.org/abs/2502.12521) [[29]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM))

## Inner Thinking Transformer

The "[Inner Thinking Transformer](https://arxiv.org/abs/2502.13842)" (February 2025) introduces a dynamic depth scaling architecture that avoids using a fixed number of transformer layers for every token [[12]](https://aclanthology.org/2025.acl-long.1369.pdf), [[13]](https://arxiv.org/pdf/2502.13842), [[14]](https://arxiv.org/html/2502.13842v1).

The core mechanism is **Adaptive Token Routing**, which identifies "difficult" tokens and sends them through the same layer multiple times. This selectively increases the inference compute budget for the parts of the input that require more complex reasoning.

This approach allows the model to allocate extra "thinking" effort precisely where it is needed, without lengthening the overall output sequence. It is a more granular way of managing compute, focusing resources on the most challenging tokens rather than uniformly increasing computation for the entire generation.![The Inner Thinking Transformer's Adaptive Token Routing mechanism.](https://substackcdn.com/image/fetch/$s_!-oC7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a6eb47e-fcbe-4c71-8d45-e7d82ae14ba1_1414x1090.png)
Image 19: The Inner Thinking Transformer's Adaptive Token Routing mechanism. (Source [https://arxiv.org/abs/2502.13842](https://arxiv.org/abs/2502.13842) [[15]](https://www.emergentmind.com/topics/inner-thinking-transformer-itt))

## Test Time Scaling for Code Generation

"[S\*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382)" (February 2025) introduces the S\* framework, a hybrid approach specialized for code generation. It combines parallel generation of candidate solutions with sequential, iterative debugging.![An overview of the S*: Test Time Scaling for Code Generation framework.](https://substackcdn.com/image/fetch/$s_!quMS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94a88f17-b4b1-4642-aeb1-6db29071ef91_972x752.png)
Image 20: An overview of the S*: Test Time Scaling for Code Generation framework. (Source [https://arxiv.org/abs/2502.14382](https://arxiv.org/abs/2502.14382))

The framework operates in two stages:
1.  **Generation:** The model generates multiple code samples in parallel. Each sample is then executed against public test cases, and the execution results (outputs and errors) are fed back to the model for iterative repair. This sequential scaling via iterative debugging improves the overall coverage, which is the fraction of problems solved by at least one generated sample.
2.  **Selection and Repair:** To select the best solution from the candidates that pass the public tests, S\* uses **adaptive input synthesis**. An LLM is prompted to generate new, "distinguishing" test cases that are specifically designed to cause different behaviors between two candidate solutions. By executing the candidates on these new inputs, the system can more robustly identify the correct one. This adaptive, execution-grounded approach ensures a more reliable selection process compared to relying on a model's internal judgment alone.

This approach is connected to earlier Google research on compute-optimal scaling and is particularly powerful for code because of the availability of a deterministic execution environment (the interpreter or compiler) to provide ground-truth feedback. The results are impressive: S\* enables smaller models to outperform larger ones and allows instruction-based models to surpass reasoning models on coding benchmarks.

## Chain of Draft

"[Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/abs/2502.18600)" (February 2025) is based on the observation that humans often rely on concise notes or drafts rather than verbose, step-by-step explanations when solving problems [[42]](https://www.helicone.ai/blog/chain-of-draft), [[43]](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft), [[44]](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169), [[45]](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock), [[46]](https://arxiv.org/html/2502.18600v1).

The **Chain of Draft (CoD)** prompting technique encourages the model to generate minimal yet informative intermediate steps, such as equations or key terms, instead of full natural-language sentences. This drastically reduces the number of generated tokens while maintaining accuracy comparable to full CoT on reasoning benchmarks. For example, on the GSM8K benchmark, CoD reduced output tokens by up to 92% while having a minimal impact on accuracy.

The main trade-off is the loss of human-readable reasoning traces. While the final answer is correct, the intermediate "drafts" may be too concise to be easily understood. This makes CoD a good choice for applications where efficiency and cost are paramount, and full interpretability of the reasoning process can be sacrificed.![A comparison of Chain of Draft vs. other prompting methods.](https://substackcdn.com/image/fetch/$s_!Gaj6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869a967-9498-435f-85f2-a38557db14e3_1460x982.png)
Image 21: A comparison of Chain of Draft vs. other prompting methods. (Source [https://arxiv.org/abs/2502.18600](https://arxiv.org/abs/2502.18600) [[46]](https://arxiv.org/html/2502.18600v1))

## Better Feedback and Edit Models

Most inference scaling techniques are designed for tasks with verifiable answers, like math or coding. "[Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/abs/2503.04378)" (March 2025) addresses the challenge of applying these techniques to open-ended domains like creative writing or high-level planning, where there is no single correct answer [[47]](https://arxiv.org/html/2503.04378v1), [[48]](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended).

The paper proposes a specialized architecture that decouples the generation process into three distinct models:
1.  A **Generator Model** that produces an initial response.
2.  A **Feedback Model** that provides textual critiques of the initial response.
3.  An **Edit Model** that refines the initial response based on the feedback.

These dedicated models are trained on large, human-annotated datasets of responses, critiques, and revisions. This allows them to produce higher-quality signals than a single model performing a generic self-critique loop could. The result is an iterative refinement process at inference time that is effective for subjective, open-ended tasks.![Dedicated Feedback and Edit Models for Inference-Time Scaling system architecture](https://substackcdn.com/image/fetch/$s_!zA8v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73568387-83fb-4744-bd3d-f5cbcfe53f1d_1136x716.png)
Image 22: Dedicated Feedback and Edit Models for Inference-Time Scaling system architecture. (Source [https://arxiv.org/abs/2503.04378](https://arxiv.org/abs/2503.04378) [[47]](https://arxiv.org/html/2503.04378v1))

## Conclusion

Inference-time compute scaling has firmly established itself as a major research direction in 2025. Its appeal lies in its ability to enhance the reasoning capabilities of existing models without requiring permanent and costly weight modifications. This survey has highlighted the breadth of techniques being explored, from simple interventions like "Wait" tokens and budget forcing to more sophisticated approaches involving search algorithms, optimization loops, dynamic routing, and even latent-space iteration.

A recurring and powerful finding across these papers is that smaller models, when combined with effective inference-time scaling, can often rival or even surpass the performance of much larger models that lack such scaling. This has profound implications for engineering practice, as it offers a path to achieving high-level reasoning capabilities without being solely dependent on the largest, most expensive models. It shifts the trade-off, allowing engineers to balance model size, training cost, latency, and accuracy in new ways.

However, it is also important to acknowledge the caveats. Increased inference-time compute directly translates to higher inference costs and increased latency, which can negatively impact user experience. Furthermore, as the Sys2Bench paper demonstrated, there is no universally best technique; the optimal approach is highly dependent on the specific task. This complexity is giving rise to an emerging industry trend: "thinking-on-demand" toggles. These features allow developers or even end-users to dynamically adjust the amount of inference compute allocated to a task, dialing it up for difficult problems and down for simpler ones.

Looking ahead, it is clear that explicit reasoning, enabled by these scaling techniques, is becoming the default for agentic systems rather than an optional feature. As we continue to push the boundaries of what AI can do, the ability to "think longer" and more deeply will be essential.![Feedback and Edit Models enable effective Inference-Time scaling across various dimensions.](https://substackcdn.com/image/fetch/$s_!nhEn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1f749e4-4167-4013-b1c9-651c83bf8d3b_1504x756.png)
Image 23: Feedback and Edit Models enable effective Inference-Time scaling across various dimensions. (Source [https://arxiv.org/abs/2503.04378](https://arxiv.org/abs/2503.04378) [[47]](https://arxiv.org/html/2503.04378v1))

This article has focused exclusively on inference-time methods. In our next piece, we will explore the other side of the equation: train-time compute scaling. We will delve into advanced reinforcement learning techniques, hybrid RL and SFT approaches, and distillation methods that are shaping the next generation of reasoning models.

## References

- [1] [Paper Review of s1: Simple Test-Time Scaling](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8)
- [2] [s1: Simple test-time scaling](https://huggingface.co/papers/2501.19393)
- [3] [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://icml.cc/virtual/2025/poster/46149)
- [4] [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://proceedings.mlr.press/v267/li25ac.html)
- [5] [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme)
- [6] [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://tldr.takara.ai/p/2501.18585)
- [7] [Trading Inference-Time Compute for Adversarial Robustness](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf)
- [8] [Trading Inference-Time Compute for Adversarial Robustness](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness)
- [9] [Trading Inference-Time Compute for Adversarial Robustness](https://huggingface.co/papers/2501.18841)
- [10] [Trading Inference-Time Compute for Adversarial Robustness](https://www.youtube.com/watch?v=6Yxc6uh0RyE)
- [11] [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- [12] [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://aclanthology.org/2025.acl-long.1369.pdf)
- [13] [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://arxiv.org/pdf/2502.13842)
- [14] [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://arxiv.org/html/2502.13842v1)
- [15] [Inner Thinking Transformer (ITT)](https://www.emergentmind.com/topics/inner-thinking-transformer-itt)
- [16] [Understanding Reasoning in Large Language Models](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)
- [17] [Inverse Scaling of Robustness in Language Models with Verifiable Reasoning](https://arxiv.org/html/2507.15974v1)
- [18] [Chain-of-Thought increases token count and latency significantly](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more)
- [19] [The Impact of Reasoning Step Length on Truthfulness in Chain-of-Thought](https://aclanthology.org/2025.emnlp-main.165.pdf)
- [20] [CoT Optimization](https://www.aussieai.com/research/cot-optimization)
- [21] [CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning](https://arxiv.org/html/2502.02390v3)
- [22] [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://arxiv.org/html/2502.04404v1)
- [23] [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947)
- [24] [Recurrent Depth Scaling for Language Models](https://huggingface.co/papers/2502.05171)
- [25] [Scaling Test-Time Computation by Implicitly Reasoning in Latent Space](https://openreview.net/forum?id=S3GhJooWIC)
- [26] [Scaling Test-Time Computation by Implicitly Reasoning in Latent Space](https://neurips.cc/virtual/2025/poster/117966)
- [27] [Scaling Test-Time Computation by Implicitly Reasoning in Latent Space](https://icml.cc/virtual/2025/51856)
- [28] [Scaling Test-Time Compute: How Recurrent Depth Transforms AI Reasoning](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db)
- [29] [Sys2Bench: A Benchmark for Inference-Time Computations in LLM Reasoning](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [30] [Standardized Benchmark for Inference-Time Computation](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [31] [Inference-Time Computation Methods for LLMs](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [32] [Chain-of-Thought increases token count and latency](https://arxiv.org/html/2406.09136v1)
- [33] [Chain-of-Thought: When Thinking Costs More Than It's Worth](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought)
- [34] [When Thinking Costs More Than It's Worth](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought)
- [35] [When Thinking Costs More Than It's Worth](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought)
- [36] [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)
- [37] [VersaPRM: A Versatile Process Reward Model for Large Language Models](https://openreview.net/forum?id=l19DmXbwPK)
- [38] [VersaPRM: A Versatile Process Reward Model for Large Language Models](https://icml.cc/virtual/2025/oral/47195)
- [39] [Test-Time Reinforcement Learning with SCOPE](https://arxiv.org/html/2512.15146v1)
- [40] [Improving Mathematical Reasoning with Process Supervision](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf)
- [41] [Reward Models: A Deep Dive](https://cameronrwolfe.substack.com/p/reward-models)
- [42] [Chain of Draft: A New Prompting Technique for Concise Reasoning](https://www.helicone.ai/blog/chain-of-draft)
- [43] [Chain of Draft (CoD) Prompting](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft)
- [44] [What is Chain of Drafts? Bye-Bye Chain of Thoughts!](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169)
- [45] [Move Beyond Chain-of-Thought with Chain-of-Draft on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock)
- [46] [Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/html/2502.18600v1)
- [47] [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/html/2503.04378v1)
- [48] [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended)