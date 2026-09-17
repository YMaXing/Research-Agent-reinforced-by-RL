# 2025’s LLM Reasoning Playbook: 14 Inference-Time Scaling Papers You Need to Know

In 2025, building agentic systems that can reliably solve complex, multi-step problems is no longer a niche research area; it is a core requirement for production AI. The direct-answer models that dominated the early years of LLMs routinely fail at these tasks, pushing the industry to find new ways to enhance reasoning capabilities. This has led to a surge in research that blends inference-time scaling, pure reinforcement learning (RL), hybrid RL and supervised fine-tuning (SFT) approaches, and SFT with distillation, especially since the release of DeepSeek-R1.

This article focuses on one of these areas: inference-time compute scaling. We will survey 14 recent papers that explore how to make LLMs "think longer" and more effectively at the moment of inference, without altering their underlying weights.![Image 1: The four main categories of implementing reasoning models. This article focuses on inference-time-scaling methods.](https://substackcdn.com/image/fetch/$s_!IOSP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf9e2677-652a-4af1-9f57-dc0c253d2198_1448x1260.png)

Image 1: The four main categories of implementing reasoning models. This article focuses on inference-time-scaling methods. (Source [understanding-reasoning-llms](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

We will now examine each of the four categories in detail so you can understand how inference-time scaling fits inside the broader landscape.

## Implementing and improving reasoning in LLMs: The four main categories

Reasoning models are a specialized class of LLMs designed to solve problems by generating intermediate steps, either internally or as part of their output, before arriving at a final answer [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms). This contrasts sharply with standard LLMs, which typically produce a direct response in a single forward pass. This ability to "think" allows them to tackle complex tasks like mathematical proofs, puzzles, and coding challenges that direct-answer models often fail to solve.![Image 2: Side-by-side comparison of a basic LLM's one-line answer and a reasoning LLM's explanatory response.](https://substackcdn.com/image/fetch/$s_!ZsN9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8abbfe39-f656-4845-b376-18c1e563210a_1326x564.png)

Image 2: Side-by-side comparison of a basic LLM's one-line answer and a reasoning LLM's explanatory response. (Source [understanding-reasoning-llms](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

Improving an LLM's reasoning involves two fundamental approaches: increasing training compute or increasing inference compute. Training compute modifies the model's weights through methods like SFT or RL. Inference compute, on the other hand, involves allocating extra computational resources (FLOPs) at test time to enhance output quality without altering the model's parameters. A classic example is chain-of-thought (CoT) prompting, where adding "Let's think step by step" encourages the model to generate a reasoning trace, thereby increasing the FLOPs used for a single query [[2]](https://arxiv.org/abs/2205.11916).

In practice, the most effective systems often combine both. Training alone can lead to issues like "reward hacking," where a model learns to exploit the reward function without genuinely improving its reasoning. Conversely, relying solely on inference-time scaling with a weak base model yields limited gains. A well-trained model provides a strong foundation, which can then be amplified through techniques that allow it to "think longer" at inference time.![Image 3: Accuracy improvements can be achieved through increased training or test-time compute. Test-time compute is synonymous with inference-time compute and inference-time scaling.](https://substackcdn.com/image/fetch/$s_!pgyl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddde6f39-3b88-4962-9d02-2cf767dc82e9_1484x994.png)

Image 3: Accuracy improvements can be achieved through increased training or test-time compute. Test-time compute is synonymous with inference-time compute and inference-time scaling. (Source [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382))

The development of reasoning models can be broken down into four main categories, as outlined by Sebastian Raschka [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms). These categories provide a framework for understanding the current landscape of reasoning-focused LLMs.

### Inference-Time Compute Scaling

This approach improves a model's reasoning capabilities without any additional training. By allocating more computational resources at inference time, techniques like CoT prompting, majority voting, or search algorithms allow the model to explore more reasoning paths or refine its answers. Models like OpenAI's o1 are suspected to heavily rely on this method, which explains their higher cost per token [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms). The DeepSeek R1 technical report noted that their explicit attempts at inference-time methods were largely unsuccessful. However, the model itself demonstrates an implicit form of inference scaling, as its training encourages it to generate longer, more detailed reasoning traces, which naturally increases inference costs [[4]](https://arxiv.org/abs/2501.12948).

### Pure Reinforcement Learning

This method trains a model to reason using only RL, without a preliminary SFT stage. The DeepSeek-R1-Zero model is a prime example. It was trained from a base model using RL with rule-based accuracy and format rewards [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms), [[4]](https://arxiv.org/abs/2501.12948). This "cold start" approach demonstrated that reasoning behaviors, like self-correction, can emerge without being explicitly taught through supervised examples. However, this method can be challenging to stabilize and may result in outputs that are not well-aligned with human readability or preferences.

### Reinforcement Learning and Supervised Fine-Tuning

This hybrid approach, which is common for building high-performance reasoning models, combines the strengths of both SFT and RL. An initial SFT stage aligns the model with desired reasoning formats (often using CoT examples), creating a strong baseline. Subsequent RL stages then refine these capabilities, optimizing for correctness and other objectives. DeepSeek's flagship model, DeepSeek-R1, was developed using this method. It started from the R1-Zero model, incorporated SFT stages with data generated by R1-Zero, and underwent further RL with additional rewards for consistency and human preference [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms), [[4]](https://arxiv.org/abs/2501.12948). This multi-stage process results in a model that is both a powerful reasoner and well-aligned with user expectations.

### Supervised Fine-Tuning and Model Distillation

The final category involves using SFT to transfer the reasoning capabilities of a large, powerful "teacher" model to a smaller "student" model. This is often called distillation, but in the context of LLMs, it typically means instruction fine-tuning a smaller model on the high-quality outputs of a larger one [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms). The DeepSeek team used this approach to create the R1-Distill series, where models like Llama and Qwen were fine-tuned on the SFT data generated during the development of DeepSeek-R1 [[4]](https://arxiv.org/abs/2501.12948). This strategy is attractive for creating smaller, more efficient models that retain strong reasoning abilities, though their performance is ultimately limited by the quality of the teacher model's outputs.![Image 4: The four categories of reasoning model development.](https://substackcdn.com/image/fetch/$s_!_2dU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5e5fdf9-e72c-497b-9cf4-b4e3c24f33f1_1600x591.png)

Image 4: The four categories of reasoning model development. (Source [understanding-reasoning-llms](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

With the four categories now mapped, we will zoom in on the inference-time compute scaling branch that forms the core of this article.

## Inference-time compute scaling methods

The core idea behind inference-time compute scaling is straightforward: allowing an LLM to "think longer" on a problem often leads to better answers, much like how humans benefit from spending more time on difficult tasks.

The most classic example of this is CoT prompting. By adding a simple phrase like "Let's think step by step," we encourage the model to generate intermediate reasoning steps instead of jumping to a final answer [[2]](https://arxiv.org/abs/2205.11916). This increases the number of tokens generated, which directly translates to higher latency and monetary cost, but often improves accuracy on complex problems.![Image 5: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper.](https://substackcdn.com/image/fetch/$s_!Knds!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d37faa4-3261-492c-85a4-766926b8c17c_1600x419.png)

Image 5: An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper [[2]](https://arxiv.org/abs/2205.11916).

Beyond simple prompting, more structured methods involve search and voting strategies. In majority voting, the LLM generates multiple answers, and the most frequent one is selected [[5]](https://openreview.net/forum?id=l19DmXbwPK). More advanced techniques use search algorithms like beam search, which explore multiple potential reasoning paths simultaneously. These search processes are often guided by a Process Reward Model (PRM), which scores each intermediate step, allowing the system to prioritize more promising paths [[1]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms). These methods allocate additional compute either in parallel (generating multiple full solutions) or sequentially (exploring paths step-by-step).![Image 6: Different search-based methods rely on a process-reward-based model to select the best answer.](https://substackcdn.com/image/fetch/$s_!O9a-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ad9742b-993f-4ecd-8f80-2fa41d43164b_1334x798.png)

Image 6: Different search-based methods rely on a process-reward-based model to select the best answer. (Source [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314))

We will now examine a concrete recent instantiation of these ideas in the s1 paper, which combines curated traces with explicit length-control tokens.

## s1: Simple test-time scaling

The paper "[s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393)" (31 Jan, 2025) introduces a hybrid approach that combines a small, curated SFT dataset of 1,000 reasoning traces with a simple yet effective inference-time control mechanism [[7]](https://arxiv.org/abs/2501.19393), [[8]](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8), [[9]](https://huggingface.co/papers/2501.19393). This distinguishes it from pure distillation, as it actively regulates compute at test time.

A key mechanism in s1 is the use of "wait" tokens. When the model attempts to conclude its reasoning prematurely, the system suppresses the end-of-thinking token and instead appends "Wait". This simple intervention encourages the model to re-evaluate its current reasoning path, often leading to self-correction and improved accuracy. This is in contrast to simply using an end-of-thinking delimiter to terminate the process.![Image 7: Illustration of "wait" token insertion to control the length of the output.](https://substackcdn.com/image/fetch/$s_!qk_K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e7f4d94-9f8f-4353-87ad-78f3cba7b9cd_1154x854.png)

Image 7: Illustration of "wait" token insertion to control the length of the output. (Source [s1: Simple Test-Time Scaling](https://arxiv.org/abs/2501.19393))

This technique is a form of sequential scaling called **budget forcing**. It gives developers direct control over the length of the reasoning trace by either forcing an early exit or extending the thinking process. This is different from parallel methods like majority voting, which generate multiple independent solutions. The paper finds a positive correlation between the length of the generated response and its accuracy on reasoning benchmarks, showing that "thinking longer" generally leads to better outcomes.![Image 8: Correlation between response accuracy and length.](https://substackcdn.com/image/fetch/$s_!kYWF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7f0c49b-a644-4142-bed0-7d114ecd39c2_798x456.png)

Image 8: Correlation between response accuracy and length. (Source [s1: Simple Test-Time Scaling](https://arxiv.org/abs/2501.19393))

This self-correction behavior is reminiscent of the "Aha moment" observed during the training of DeepSeek-R1, where the model spontaneously began to use words like "wait" to pause and rethink its approach [[4]](https://arxiv.org/abs/2501.12948). The s1 paper empirically validates this, showing that appending "Wait" improves accuracy more than neutral phrases like "Hmm," suggesting it specifically triggers a re-evaluation process rather than just extending time [[9]](https://huggingface.co/papers/2501.19393).![Image 9: "Wait" vs "Hmm" tokens.](https://substackcdn.com/image/fetch/$s_!Qd4X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bdfe7db-8c97-4240-8be0-11efa7abdf7c_758x510.png)

Image 9: "Wait" vs "Hmm" tokens. (Source [s1: Simple Test-Time Scaling](https://arxiv.org/abs/2501.19393))

However, the authors state that the method has its limitations and call for future work to compare its effectiveness against other scaling techniques like beam search, lookahead search, and compute-optimal search.

## Other noteworthy research papers on inference-time compute scaling

The field of inference-time compute scaling has seen a high volume of research recently. To provide a broad overview without getting lost in repetitive details, we will briefly summarize several other noteworthy papers.

A common pattern emerges from this body of work: many of the most effective techniques are not purely prompt-based. Instead, they often blend some form of training or fine-tuning with mechanisms for explicit control over inference-time compute. This hybrid approach allows models to be both pre-disposed to reason effectively and dynamically regulated at test time.

It is important to distinguish these regulated approaches from SFT or distillation methods that simply train a model to produce longer outputs. The key difference is the active management of the compute budget during inference, allowing for adaptive "thinking" based on the task's demands.

## Test-Time Preference Optimization

The paper "[Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://arxiv.org/abs/2501.12895)" introduces a pure inference-time method that aligns model outputs with human preferences without changing the underlying model weights [[10]](https://arxiv.org/abs/2501.12895), [[11]](https://icml.cc/virtual/2025/poster/46149), [[12]](https://proceedings.mlr.press/v267/li25ac.html). It works through an iterative loop that progressively refines the model's response on a per-query basis.

The process begins by generating multiple candidate responses, which are then scored by a reward model. The highest-scoring ("chosen") and lowest-scoring ("rejected") responses are used to generate textual critiques and suggestions. This textual feedback, which explains the strengths of the chosen response and weaknesses of the rejected one, guides the model in generating a new, improved set of responses. This four-step loop of generation, scoring, critique, and refinement repeats, allowing the model to "learn" on the fly and better align its output with the reward model's preferences.![Image 10: The Test-Time Preference Optimization process.](https://substackcdn.com/image/fetch/$s_!dmJN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2a1bd16-7cf7-4898-8dce-a2d8352f76a8_1600x819.png)

Image 10: The Test-Time Preference Optimization process. (Source [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://arxiv.org/abs/2501.12895))

## Thoughts Are All Over the Place

In "[Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://arxiv.org/abs/2501.18585)," researchers identify a phenomenon they call "underthinking" in o1-like models [[13]](https://arxiv.org/abs/2501.18585), [[14]](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme), [[15]](https://tldr.takara.ai/p/2501.18585). This occurs when a model frequently switches between different reasoning paths without sufficiently exploring any single one, which can lead to lower accuracy on complex problems.

To address this, the paper proposes the Thought Switching Penalty (TIP). TIP is a decoding strategy that modifies the model's logits at inference time, applying a penalty to tokens associated with thought transitions. This discourages the model from prematurely abandoning a promising line of reasoning. By forcing deeper exploration of each path, this no-fine-tuning approach was shown to improve accuracy on challenging benchmarks.![Image 11: A diagram illustrating the Thought Switching Penalty method.](https://substackcdn.com/image/fetch/$s_!vvCX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7111ccaa-c4c1-4c7c-84f9-74d38df3c663_1528x894.png)

Image 11: A diagram illustrating the Thought Switching Penalty method. (Source [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://arxiv.org/abs/2501.18585))

## Trading Inference-Time Compute for Adversarial Robustness

The paper "[Trading Inference-Time Compute for Adversarial Robustness](https://arxiv.org/abs/2501.18841)" explores the relationship between inference-time compute and model safety [[16]](https://arxiv.org/abs/2501.18841), [[17]](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf), [[18]](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness). It finds that increasing the amount of reasoning a model performs generally reduces the success rate of adversarial attacks, even without any specific adversarial training. The empirical trade-off curves in the paper show that for many unambiguous tasks, attack success approaches zero as compute grows.

However, the gains are limited in scenarios involving policy ambiguity or the exploitation of loopholes, where an attacker can frame a request in a way that is not a clear policy violation. The paper also introduces two novel attack strategies that can counteract these robustness gains: "Think Less," which tricks the model into reducing its reasoning time, and "Nerd Sniping," which traps the model in unproductive thinking loops. The authors conclude that while inference scaling is a valuable tool for improving safety, it is not a complete solution on its own.![Image 12: An analysis of trading inference-time compute for adversarial robustness.](https://substackcdn.com/image/fetch/$s_!Gt2_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F704acd82-10a8-4879-9bd3-26bb67c3155f_1600x1173.png)

Image 12: An analysis of trading inference-time compute for adversarial robustness. (Source [Trading Inference-Time Compute for Adversarial Robustness](https://arxiv.org/abs/2501.18841))

## Chain-of-Associated-Thoughts

"[CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning](https://arxiv.org/abs/2502.02390)" combines Monte Carlo Tree Search (MCTS) with an "associative memory" that acts as a dynamic knowledge base during inference [[19]](https://arxiv.org/abs/2502.02390). MCTS, a search method popularized by game AI like AlphaGo, helps systematically explore reasoning pathways by balancing the exploration of new ideas with the exploitation of promising ones [[20]](https://www.turingpost.com/p/testtimescaling2), [[21]](https://openreview.net/forum?id=h6CQPEYAVp). The associative memory complements this by allowing the model to recall earlier reasoning paths and incorporate newly generated information without losing context.![Image 13: A visualization of the CoAT: Chain-of-Associated-Thoughts Framework.](https://substackcdn.com/image/fetch/$s_!AtpC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d0635fb-c0b4-45df-b8d3-b54254ab92b5_1600x777.png)

Image 13: A visualization of the CoAT: Chain-of-Associated-Thoughts Framework. (Source [CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning](https://arxiv.org/abs/2502.02390))

## Step Back to Leap Forward

The paper "[Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://arxiv.org/abs/2502.0440)" introduces a self-backtracking mechanism that trains models to recognize and correct their own suboptimal reasoning paths [[22]](https://arxiv.org/abs/2502.0440), [[23]](https://arxiv.org/html/2502.04404v1), [[24]](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947). This is achieved by teaching the model to generate a special `<backtrack>` token when it identifies a mistake.

During the training phase, the model learns when and where to use this token. At inference time, this learned ability is leveraged in a tree-based search process. When the model generates the `<backtrack>` token, it rolls back to a previous state and explores an alternative reasoning trajectory. A key advantage of this approach is that it does not require an external reward model to guide the search, unlike standard process-reward-guided methods. The model can dynamically adjust its search depth and breadth based on its own internally learned backtracking skill, allowing it to transition from "slow thinking" (search) to "fast thinking" (direct generation) through self-improvement.![Image 14: A diagram of the Step Back to Leap Forward: Self-Backtracking mechanism.](https://substackcdn.com/image/fetch/$s_!e6x3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1df5fbf3-97f2-4976-b46f-2d5196b6bdc4_1594x888.png)

Image 14: A diagram of the Step Back to Leap Forward: Self-Backtracking mechanism. (Source [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://arxiv.org/abs/2502.04404v1))

## Scaling up Test-Time Compute with Latent Reasoning

The paper "[Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach](https://arxiv.org/abs/2502.05171)" proposes a "recurrent depth" approach that iterates in latent space rather than producing additional output tokens, aiming to overcome the "verbalization bottleneck" where complex thought is inefficient to express in text [[25]](https://arxiv.org/abs/2502.05171), [[26]](https://introl.com/blog/latent-reasoning-recurrent-depth-thinking-without-tokens-2026). This method behaves like an RNN, reusing layers to deepen the reasoning process without increasing the length of the visible output.

The major drawback is the absence of explicit reasoning steps that aid human interpretability and debugging. This opacity makes the model's internal process a black box, raising concerns about safety and "monitorability" [[27]](https://arxiv.org/html/2604.04902v1). It also reintroduces a classic RNN problem: reasoning is constrained by a fixed-size latent "scratchpad," which may struggle with problems requiring many intermediate steps [[28]](https://www.lesswrong.com/posts/pLnLSgWphqDbdorgi/on-recent-results-in-llm-latent-reasoning).![Image 15: A visualization of the recurrent depth approach for scaling up test-time compute with latent reasoning.](https://substackcdn.com/image/fetch/$s_!kVPW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb82da925-5736-44ba-bed1-ea3207b06382_1516x602.png)

Image 15: A visualization of the recurrent depth approach for scaling up test-time compute with latent reasoning. (Source [Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach](https://arxiv.org/abs/2502.05171))

## Can a 1B LLM Surpass a 405B LLM?

"[Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling](https://arxiv.org/abs/2502.06703)" presents a systematic study of the interactions between inference-time scaling, PRMs, and problem difficulty [[30]](https://arxiv.org/abs/2502.06703). The authors propose a "compute-optimal" scaling strategy that adapts the inference budget based on the specific PRM being used, the size of the policy model, and the complexity of the task at hand.

Through extensive experiments, the paper provides compelling evidence that a 1B parameter model, when paired with the right scaling strategy, can outperform a much larger 405B Llama 3 model on the same benchmarks. This finding has significant implications for AI engineers, as it demonstrates that intelligently allocating inference compute can be a more effective and efficient way to boost performance than simply scaling up model size. This directly informs the trade-off decisions between model size, cost, and accuracy in production systems.![Image 16: A comparison of compute-optimal scaling.](https://substackcdn.com/image/fetch/$s_!DiM2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c471e7f-36e7-41a8-a7e0-80bebf3c0f36_1600x1046.png)

Image 16: A comparison of compute-optimal scaling. (Source [Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling](https://arxiv.org/abs/2502.06703))

## Learning to Reason from Feedback at Test-Time

The method described in "[Learning to Reason from Feedback at Test-Time](https://www.arxiv.org/abs/2502.12521)" is challenging to classify as either a pure inference-time or training-time approach because it updates the model's weights during inference [[31]](https://www.arxiv.org/abs/2502.12521). The paper introduces an optimizer that adjusts model weights based on previous mistakes made on a given task, without storing the failed attempts in the prompt context.

This weight-update approach is distinct from both sequential revision, where previous attempts are added to the context, and parallel sampling, where multiple independent attempts are generated. Instead of growing the context length, this method allows the model to "remember" its errors through lightweight weight updates. This hybrid approach offers a way to learn from feedback at test-time without the computational overhead of full retraining or the context window limitations of sequential revision.![Image 17: A visualization of the OpTune optimizer.](https://substackcdn.com/image/fetch/$s_!nJMD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1925302-7fc2-4c7b-91e9-1c0fc4f0609e_1426x652.png)

Image 17: A visualization of the OpTune optimizer. (Source [Learning to Reason from Feedback at Test-Time](https://www.arxiv.org/abs/2502.12521))

## Inference-Time Computations for LLM Reasoning and Planning

The paper "[Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521)" introduces Sys2Bench, a comprehensive benchmark for evaluating various inference-time techniques [[31]](https://www.arxiv.org/abs/2502.12521), [[32]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM). It assesses methods like CoT, Tree-of-Thought, and Reasoning as Planning across eleven diverse tasks.

The benchmark covers five main categories: arithmetic, logical, commonsense, and algorithmic reasoning, as well as planning domains. A key insight from the paper is that no single inference-time technique consistently performs best across all task types. This finding forces engineers to move away from a one-size-fits-all approach and instead match specific scaling methods to the domains they are best suited for. The paper also provides a detailed analysis of the trade-offs between computational cost and performance for each technique.![Image 18: Benchmark results from Inference-Time Computations for LLM Reasoning and Planning.](https://substackcdn.com/image/fetch/$s_!Vm7j!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42115dab-1086-4035-9a64-65a83631377e_1600x1023.png)

Image 18: Benchmark results from Inference-Time Computations for LLM Reasoning and Planning. (Source [Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521))

## Inner Thinking Transformer

"[Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://arxiv.org/abs/2502.13842)" introduces a novel architecture that uses dynamic depth scaling, avoiding a fixed number of transformer layers for every token [[33]](https://arxiv.org/abs/2502.13842), [[34]](https://aclanthology.org/2025.acl-long.1369.pdf), [[35]](https://www.emergentmind.com/topics/inner-thinking-transformer-itt).

The core mechanism is Adaptive Token Routing (ATR), which identifies "difficult" tokens and processes them through the same layer multiple times. This selectively increases the inference compute budget for the parts of the input that require more complex reasoning. By doing so, the model can allocate extra "thinking" effort precisely where it is needed, without lengthening the overall output sequence. This allows for a more efficient use of computational resources, as simpler tokens are processed more quickly.![Image 19: The Adaptive Token Routing mechanism of the Inner Thinking Transformer.](https://substackcdn.com/image/fetch/$s_!-oC7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a6eb47e-fcbe-4c71-8d45-e7d82ae14ba1_1414x1090.png)

Image 19: The Adaptive Token Routing mechanism of the Inner Thinking Transformer. (Source [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://arxiv.org/abs/2502.13842))

## Test Time Scaling for Code Generation

The paper "[S\*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382)" proposes the S\* method, a hybrid test-time scaling framework specifically designed for code generation [[3]](https://arxiv.org/abs/2502.14382). This approach combines the parallel generation of multiple candidate solutions with sequential, iterative debugging to improve both the coverage and accuracy of the final selected code.![Image 20: An overview of the S*: Test Time Scaling for Code Generation framework.](https://substackcdn.com/image/fetch/$s_!quMS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94a88f17-b4b1-4642-aeb1-6db29071ef91_972x752.png)

Image 20: An overview of the S*: Test Time Scaling for Code Generation framework. (Source [S\*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382))

The framework operates in two stages. First, in the generation stage, it generates multiple initial samples in parallel. Each of these samples is then refined sequentially through iterative debugging, using feedback from execution on public test cases. This allows the model to correct errors and improve the quality of its initial attempts.

The second stage is selection. A key innovation here is **adaptive input synthesis**. Instead of relying on a static set of tests, the system prompts an LLM to generate new, discriminating test cases specifically designed to tell the difference between two candidate solutions that both pass the public tests. These new inputs are then executed, and the results are used to make a final, more robust selection. This adaptive, execution-grounded approach is a powerful way to identify the most correct solution among multiple plausible candidates, and it connects to earlier Google research on optimal test-time compute scaling.

## Chain of Draft

The paper "[Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/abs/2502.18600)" is inspired by the observation that humans often rely on concise drafts or shorthand notes when solving problems, rather than producing verbose, step-by-step explanations [[36]](https://arxiv.org/abs/2502.18600), [[37]](https://www.helicone.ai/blog/chain-of-draft), [[38]](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft), [[39]](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169), [[40]](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock). It proposes a prompting strategy called Chain of Draft (CoD), which encourages LLMs to generate minimal yet informative intermediate steps.![Image 21: A comparison of standard, Chain of Thought, and Chain of Draft prompting.](https://substackcdn.com/image/fetch/$s_!Gaj6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869a967-9498-435f-85f2-a38557db14e3_1460x982.png)

Image 21: A comparison of standard, Chain of Thought, and Chain of Draft prompting. (Source [Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/abs/2502.18600))

Instead of full natural-language reasoning, CoD produces concise outputs, often in the form of equations or shorthand notation. This significantly reduces the number of tokens generated, leading to faster response times and lower computational costs. The paper quantifies these efficiency gains, showing that CoD can achieve accuracy comparable to full CoT on reasoning benchmarks while using far fewer tokens. This presents an important trade-off for AI engineers: while the full, human-readable reasoning trace is lost, the gains in speed and cost can be substantial, making it a valuable technique when interpretability can be sacrificed for efficiency.

## Better Feedback and Edit Models

Applying inference-time scaling to open-ended tasks like creative writing or high-level planning is challenging because there are no easily verifiable "correct" answers. The paper "[Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/abs/2503.04378)" addresses this by proposing a specialized, multi-model architecture [[41]](https://arxiv.org/abs/2503.04378), [[42]](https://arxiv.org/html/2503.04378v1), [[43]](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended).

This system decouples the generation, feedback, and editing processes into three separate models, each optimized for its specific role. The feedback and edit models are trained on large, human-annotated datasets of responses, critiques, and revisions. This allows them to produce higher-quality signals than a single, general-purpose model attempting to self-critique. During inference, this setup enables an iterative refinement loop where the generator produces an initial response, the feedback model provides detailed critiques, and the edit model incorporates that feedback to create an improved version. This approach has been shown to surpass the performance of generic self-critique loops on open-ended tasks.![Image 22: The system architecture for dedicated feedback and edit models for inference-time scaling.](https://substackcdn.com/image/fetch/$s_!zA8v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73568387-83fb-4744-bd3d-f5cbcfe53f1d_1136x716.png)

Image 22: The system architecture for dedicated feedback and edit models for inference-time scaling. (Source [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/abs/2503.04378))

## Conclusion

Inference-time compute scaling has firmly established itself as a major research direction in 2025, and for good reason. These techniques offer a powerful way to enhance the reasoning capabilities of existing models without the need for permanent and costly weight modifications. As we have seen, the methods for achieving this are diverse, ranging from simple interventions like "wait" tokens and budget forcing to more sophisticated approaches involving search algorithms, dynamic routing, and even latent-space iteration.

A recurring and powerful finding across this body of research is that smaller models, when equipped with the right inference-time scaling strategy, can often rival or even exceed the performance of much larger models that lack such scaling. This has profound implications for AI engineering, as it directly impacts the trade-offs between model size, training costs, inference latency, and accuracy. For engineers building production systems, this means that the biggest model is not always the best choice. A smaller, more efficient model paired with an intelligent scaling strategy might deliver better performance at a fraction of the cost.

However, it is important to acknowledge the caveats. Increased inference compute is not free; it comes with higher costs and increased latency, which can negatively impact user experience. Furthermore, as the Sys2Bench benchmark demonstrated, there is no universally best technique that dominates across all tasks. The optimal approach often depends on the specific domain, the complexity of the problem, and the capabilities of the base model. This forces engineers to think critically and match the right method to the right problem.

We are already seeing an emerging industry trend toward "thinking-on-demand" features, where developers or even end-users can adjust the amount of inference compute a model uses, dialing it up for difficult tasks and down for simpler ones. This flexibility suggests a future where explicit reasoning is not an optional feature but the default mode of operation for advanced agentic systems. The ability to dynamically control and allocate computational "thought" will be a defining characteristic of next-generation AI.![Image 23: Inference-time scaling enables effective performance boosts across various dimensions.](https://substackcdn.com/image/fetch/$s_!nhEn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1f749e4-4167-4013-b1c9-651c83bf8d3b_1504x756.png)

Image 23: Inference-time scaling enables effective performance boosts across various dimensions. (Source [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/abs/2503.04378))

This article has focused on the diverse landscape of inference-time scaling. In an upcoming piece, we will shift our attention to the other side of the equation: train-time compute scaling. We will take a deep dive into advanced reinforcement learning techniques, hybrid RL plus SFT approaches, and distillation strategies that are shaping the next wave of powerful reasoning models.

## References

- [1] [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)
- [2] [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)
- [3] [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382)
- [4] [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- [5] [VersaPRM: A General-Purpose Process Reward Model for LLM Reasoning via Self-Supervision](https://openreview.net/forum?id=l19DmXbwPK)
- [6] [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314)
- [7] [s1: Simple Test-Time Scaling](https://arxiv.org/abs/2501.19393)
- [8] [Paper Review of s1: Simple test-time scaling](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8)
- [9] [s1: Simple test-time scaling](https://huggingface.co/papers/2501.19393)
- [10] [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://arxiv.org/abs/2501.12895)
- [11] [Test-Time Preference Optimization](https://icml.cc/virtual/2025/poster/46149)
- [12] [Test-time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://proceedings.mlr.press/v267/li25ac.html)
- [13] [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://arxiv.org/abs/2501.18585)
- [14] [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme)
- [15] [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://tldr.takara.ai/p/2501.18585)
- [16] [Trading Inference-Time Compute for Adversarial Robustness](https://arxiv.org/abs/2501.18841)
- [17] [TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS.](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf)
- [18] [Trading Inference-Time Compute for Adversarial Robustness](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness)
- [19] [CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning](https://arxiv.org/abs/2502.02390)
- [20] [Test-Time Scaling for LLMs (Part 2)](https://www.turingpost.com/p/testtimescaling2)
- [21] [A Survey of Test-Time Reasoning with Large Language Models](https://openreview.net/forum?id=h6CQPEYAVp)
- [22] [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://arxiv.org/abs/2502.0440)
- [23] [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://arxiv.org/html/2502.04404v1)
- [24] [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947)
- [25] [Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach](https://arxiv.org/abs/2502.05171)
- [26] [Latent Reasoning: Recurrent Depth and Thinking Without Tokens](https://introl.com/blog/latent-reasoning-recurrent-depth-thinking-without-tokens-2026)
- [27] [On the Interpretability of Latent Reasoning Models](https://arxiv.org/html/2604.04902v1)
- [28] [On recent results in LLM latent reasoning](https://www.lesswrong.com/posts/pLnLSgWphqDbdorgi/on-recent-results-in-llm-latent-reasoning)
- [29] [Can we interpret latent reasoning using current mechanistic interpretability techniques?](https://www.alignmentforum.org/posts/YGAimivLxycZcqRFR/can-we-interpret-latent-reasoning-using-current-mechanistic)
- [30] [Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling](https://arxiv.org/abs/2502.06703)
- [31] [Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521)
- [32] [Repository for "Bag of Tricks for Inference-time Computation of LLM Reasoning"](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [33] [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://arxiv.org/abs/2502.13842)
- [34] [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://aclanthology.org/2025.acl-long.1369.pdf)
- [35] [Inner Thinking Transformer (ITT)](https://www.emergentmind.com/topics/inner-thinking-transformer-itt)
- [36] [Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/abs/2502.18600)
- [37] [Chain of Draft](https://www.helicone.ai/blog/chain-of-draft)
- [38] [Chain of Draft](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft)
- [39] [What is Chain of Drafts? Bye Bye Chain of Thoughts](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169)
- [40] [Move beyond Chain-of-Thought with Chain-of-Draft on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock)
- [41] [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/abs/2503.04378)
- [42] [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/html/2503.04378v1)
- [43] [Dedicated Feedback and Edit Models Empower InferenceTime Scaling for OpenEnded General-Domain Tasks](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended)