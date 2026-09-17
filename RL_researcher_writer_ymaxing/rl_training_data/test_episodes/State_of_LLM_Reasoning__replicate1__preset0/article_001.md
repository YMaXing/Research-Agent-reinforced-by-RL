# 2025 State of Reasoning: 14 Inference-Time Compute Scaling Papers

Stronger LLM reasoning is a top priority in 2025. As we build more complex agentic systems, we need models that can perform reliable, multi-step problem-solving, a task where direct-answer models often fail. This need has fueled a surge in research since the release of models like DeepSeek-R1. New methods now blend inference-time scaling, pure reinforcement learning (RL), RL-SFT hybrids, and supervised fine-tuning (SFT) with distillation.

This article focuses on one of these areas: the latest advancements in inference-time compute scaling. These techniques improve a model’s performance by allocating additional computation at test time, without changing the model’s weights. We will survey 14 recent papers that showcase a variety of methods for regulating and scaling this test-time computation.![The four main categories of implementing reasoning models I explained in Understanding Reasoning LLMs. This article focuses on inference-time-scaling methods.](https://substackcdn.com/image/fetch/$s_!IOSP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf9e2677-652a-4af1-9f57-dc0c253d2198_1448x1260.png)

Image 1: The four main categories of implementing reasoning models I explained in Understanding Reasoning LLMs. This article focuses on inference-time-scaling methods.

To understand how these methods fit into the broader landscape, we will first examine the four main categories of reasoning model development in detail.

## Implementing and improving reasoning in LLMs: The four main categories

Reasoning models are a class of LLMs that generate an explicit or internal intermediate thought process before producing a final answer. This is a notable departure from direct-answer models, which map an input directly to an output in a single forward pass. This ability to "think" allows them to tackle more complex problems that require multi-step logic.![A side-by-side comparison of a basic LLM's one-line answer and a reasoning LLM's explanatory response.](https://substackcdn.com/image/fetch/$s_!ZsN9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8abbfe39-f656-4845-b376-18c1e563210a_1326x564.png)

Image 2: A side-by-side comparison of a basic LLM's one-line answer and a reasoning LLM's explanatory response.

There are two primary ways to improve an LLM’s reasoning capabilities: increasing training compute or increasing inference compute [[47]](https://openai.com/index/o1-report/). Training compute involves modifying the model's weights through methods like reinforcement learning or supervised fine-tuning. This is a one-time, upfront cost. Inference compute, on the other hand, refers to the extra computational effort (FLOPs) used at test time to generate a better answer, without altering the model's weights. The simplest example of this is chain-of-thought (CoT) prompting, where the model generates more tokens to explain its reasoning, thereby using more compute to arrive at a solution.![Accuracy improvements can be achieved through increased training or test-time compute, where test-time compute is synonymous with inference-time compute and inference-time scaling.](https://substackcdn.com/image/fetch/$s_!pgyl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddde6f39-3b88-4962-9d02-2cf767dc82e9_1484x994.png)

Image 3: Accuracy improvements can be achieved through increased training or test-time compute, where test-time compute is synonymous with inference-time compute and inference-time scaling. (Image by OpenAI from [o1 performance smoothly improves with both train-time and test-time compute [[47]](https://openai.com/index/o1-report/)])

In practice, most state-of-the-art systems combine both. Heavy train-time preparation is necessary because pure inference scaling on a weak base model yields limited gains. At the same time, relying on training alone can lead to problems like reward hacking, where the model learns to exploit the reward function without genuinely improving its reasoning. This hybrid approach allows models to achieve the best results.

The development of reasoning models generally falls into four main categories [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).![The four categories of reasoning model development.](https://substackcdn.com/image/fetch/$s_!_2dU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5e5fdf9-e72c-497b-9cf4-b4e3c24f33f1_1600x591.png)

Image 4: The four categories of reasoning model development.

**1. Inference-time compute scaling** is the focus of this article. This approach enhances a model's performance by allocating additional computation at inference time without changing the model's weights. Techniques like chain-of-thought, self-consistency, and various search methods fall into this category. Models like OpenAI's o1 are prime examples, demonstrating performance gains from increased test-time compute. The DeepSeek-R1 paper reported that their attempts with explicit inference-time methods were largely unsuccessful. However, the model itself demonstrates an implicit form of inference scaling: its training process encourages longer, more detailed responses, which naturally increases the compute used at inference time.

**2. Pure reinforcement learning** aims to teach models reasoning from scratch, using only a reward signal to guide them. This method avoids the need for human-annotated reasoning paths, allowing the model to discover its own problem-solving strategies. For example, DeepSeek-R1-Zero was trained using only RL, without any initial supervised fine-tuning. This approach allows the model to develop emergent behaviors like self-reflection and verification. While this can lead to novel reasoning patterns, it presents challenges. The search space is vast, and without good initial guidance, the model can struggle to find effective strategies, often resulting in an inefficient training process.

**3. Reinforcement learning and supervised fine-tuning** is a hybrid approach that combines the strengths of both methods. It starts with an SFT phase to provide the model with a strong foundation of human-like reasoning. This is followed by an RL phase to further refine and enhance its capabilities. The initial SFT helps to guide the RL process, making it more efficient and stable. DeepSeek-R1 is a prominent example of this category. Its training pipeline involves multiple stages of rejection sampling, RL, and SFT to balance powerful reasoning with alignment to human preferences.

**4. Supervised fine-tuning and model distillation** involves training a smaller "student" model to mimic the outputs of a larger, more capable "teacher" model. This is different from traditional distillation, where the student model is trained on the teacher's logits or internal representations. In the context of reasoning, the student model is fine-tuned on the high-quality reasoning traces generated by the teacher. This allows the smaller model to inherit the advanced reasoning abilities of the larger one. The DeepSeek-R1-Distill series, for instance, was created by fine-tuning smaller models like Qwen and Llama on the outputs of the larger DeepSeek-R1 model.

With these four categories mapped out, we can now zoom in on the branch that forms the core of this article: inference-time compute scaling.

## Inference-time compute scaling methods

The core idea behind inference-time compute scaling is that allowing a model to "think longer" on a problem can lead to better answers, much like how humans spend more time on difficult tasks [[29]](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more), [[30]](https://aclanthology.org/2025.emnlp-main.165.pdf), [[31]](https://www.aussieai.com/research/cot-optimization), [[32]](https://arxiv.org/html/2406.09136v1), [[33]](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought). One of the earliest and most classic examples of this is chain-of-thought (CoT) prompting. By simply instructing the model to "think step by step," it generates a more detailed reasoning process, which often leads to more accurate results. However, this comes at the cost of increased token count, latency, and monetary expense.![An example of classic CoT prompting.](https://substackcdn.com/image/fetch/$s_!Knds!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d37faa4-3261-492c-85a4-766926b8c17c_1600x419.png)

Image 5: An example of classic CoT prompting. (Image by Kojima et al. from [Large Language Models are Zero-Shot Reasoners [[46]](https://arxiv.org/abs/2205.11916)])

More advanced techniques involve search and voting strategies to explore the solution space more effectively. Majority voting, for instance, generates multiple responses and selects the most common answer [[34]](https://openreview.net/forum?id=l19DmXbwPK), [[35]](https://icml.cc/virtual/2025/oral/47195), [[36]](https://arxiv.org/html/2512.15146v1), [[37]](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf), [[38]](https://cameronrwolfe.substack.com/p/reward-models). Beam search, on the other hand, explores multiple reasoning paths in parallel, guided by a process reward model (PRM) that scores each intermediate step [[28]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM). These methods allocate additional compute to find the most promising solution.![Different search-based methods rely on a process-reward-based model to select the best answer.](https://substackcdn.com/image/fetch/$s_!O9a-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ad9742b-993f-4ecd-8f80-2fa41d43164b_1334x798.png)

Image 6: Different search-based methods rely on a process-reward-based model to select the best answer. (Image by Liu et al. from [Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights [[19]](https://www.arxiv.org/abs/2502.12521)])

Let's now examine a concrete recent instantiation of these ideas in the `s1` paper, which combines curated reasoning traces with explicit length-control tokens.

## s1: Simple test-time scaling

The paper *s1: Simple test-time scaling* [[1]](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8), [[2]](https://huggingface.co/papers/2501.19393) introduces a hybrid approach that combines a small, carefully curated SFT dataset of 1,000 reasoning traces with an inference-time length control mechanism. This distinguishes it from pure distillation methods, as it actively manages the compute budget during inference. The curation of the `s1K` dataset was guided by three principles: quality, difficulty, and diversity. The authors found that jointly incorporating these criteria was crucial, as relying on any single one in isolation led to worse performance.

A key mechanism in this paper is the use of special tokens to control the length of the model's reasoning process. When the model needs to "think" longer, a "Wait" token is appended to its generation. This simple trick encourages the model to double-check its work, often leading to self-correction and improved accuracy. Conversely, an end-of-thinking delimiter can be used to terminate the reasoning process early. This technique, which the authors call "budget forcing," is a form of sequential scaling that provides direct control over the output length. It stands in contrast to parallel methods like majority voting, where the computational cost is less predictable.![An illustration of "wait" token insertion to control the length of the output.](https://substackcdn.com/image/fetch/$s_!qk_K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e7f4d94-9f8f-4353-87ad-78f3cba7b9cd_1154x854.png)

Image 7: An illustration of "wait" token insertion to control the length of the output. (Image by Muennighoff et al. from [s1: Simple test-time scaling [[2]](https://huggingface.co/papers/2501.19393)])

Empirically, the paper shows a clear correlation between the length of the generated response and the model's accuracy on reasoning benchmarks. As the model is given more "thinking time" via budget forcing, its performance consistently improves, up to a certain point. The paper also highlights that the "Wait" token is more effective than a more neutral token like "Hmm," suggesting that inducing doubt is a key part of the self-correction process. This mechanism is reminiscent of the "Aha moment" observed in DeepSeek-R1, where the model spontaneously started using reflective language during its RL training.![A chart showing the correlation between response accuracy and length.](https://substackcdn.com/image/fetch/$s_!kYWF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7f0c49b-a644-4142-bed0-7d114ecd39c2_798x456.png)

Image 8: A chart showing the correlation between response accuracy and length. (Image by Muennighoff et al. from [s1: Simple test-time scaling [[2]](https://huggingface.co/papers/2501.19393)])

Despite its successes, the paper acknowledges some limitations. The authors call for future work to compare budget forcing against other sequential methods like beam search and lookahead search, as well as compute-optimal strategies.![A comparison of "Wait" vs "Hmm" tokens performance.](https://substackcdn.com/image/fetch/$s_!Qd4X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bdfe7db-8c97-4240-8be0-11efa7abdf7c_758x510.png)

Image 9: A comparison of "Wait" vs "Hmm" tokens performance. (Image by Muennighoff et al. from [s1: Simple test-time scaling [[2]](https://huggingface.co/papers/2501.19393)])

## Other noteworthy research papers on inference-time compute scaling

The field of inference-time compute scaling is evolving rapidly, with a high volume of recent papers exploring different facets of this paradigm. To provide a broad overview without getting lost in repetitive details, we will briefly summarize several other noteworthy contributions.

A common pattern that emerges from this body of research is the blending of some form of training with explicit control of inference-time compute. This is a departure from purely prompt-based approaches, as these methods often involve fine-tuning the model to better respond to inference-time interventions.

It is also important to distinguish these regulated approaches from SFT or distillation methods that simply produce longer outputs. The key difference is the active management of the compute budget during inference. The goal is not just to generate more tokens, but to do so in a controlled and effective manner.

## Test-Time Preference Optimization

*Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback* [[3]](https://icml.cc/virtual/2025/poster/46149), [[4]](https://proceedings.mlr.press/v267/li25ac.html) introduces an iterative alignment process that operates entirely at inference time, avoiding any changes to the underlying model weights. This positions it as a pure inference-time method.

The process works in a four-step loop. First, the model generates multiple candidate responses to a given prompt. A separate reward model then scores these responses, selecting the best ("chosen") and worst ("rejected") ones. In the third step, the LLM generates textual critiques, analyzing the strengths of the chosen response and the weaknesses of the rejected one. Finally, these critiques are used to generate suggestions for improvement, which guide the model in refining its output in the next iteration. This cycle repeats, progressively improving the quality of the responses on a per-query basis.![A diagram illustrating the Test-Time Preference Optimization process.](https://substackcdn.com/image/fetch/$s_!dmJN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2a1bd16-7cf7-4898-8dce-a2d8352f76a8_1600x819.png)

Image 10: A diagram illustrating the Test-Time Preference Optimization process. (Image by Li et al. from [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback [[4]](https://proceedings.mlr.press/v267/li25ac.html)])

## Thoughts Are All Over the Place

*Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs* [[5]](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme), [[6]](https://tldr.takara.ai/p/2501.18585) identifies a phenomenon called "underthinking" in o1-like models. This occurs when a model frequently switches between different reasoning paths without sufficiently exploring any single one, which can lead to a decrease in final accuracy.

To address this, the paper proposes the Thought Switching Penalty (TIP) method. This technique modifies the model's logits at inference time, applying a penalty to tokens associated with thought transitions. This discourages the model from prematurely abandoning a promising line of reasoning. By forcing deeper exploration of each path, this no-fine-tuning approach has been shown to improve accuracy on challenging benchmarks.![A visualization of the Thought Switching Penalty method.](https://substackcdn.com/image/fetch/$s_!vvCX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7111ccaa-c4c1-4c7c-84f9-74d38df3c663_1528x894.png)

Image 11: A visualization of the Thought Switching Penalty method. (Image by Wang et al. from [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs [[6]](https://tldr.takara.ai/p/2501.18585)])

## Trading Inference-Time Compute for Adversarial Robustness

The paper *Trading Inference-Time Compute for Adversarial Robustness* [[7]](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf), [[8]](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness), [[9]](https://huggingface.co/papers/2501.18841), [[10]](https://www.youtube.com/watch?v=6Yxc6uh0RyE), [[11]](https://arxiv.org/html/2507.15974v1) explores the relationship between inference compute and model safety. It finds that increasing inference time generally reduces the success rate of adversarial attacks, even without any specific adversarial training. The paper's empirical trade-off curves show that as a model is given more "thinking time," it becomes more resilient to attacks.

However, the authors highlight important exceptions where these gains are limited. In cases of policy ambiguity or when an attacker can exploit loopholes in the model's safety guidelines, increased compute does not always lead to better robustness. The paper also introduces new attack strategies, such as "Think Less" (which tricks the model into reducing its compute) and "Nerd Sniping" (which traps the model in unproductive thinking loops), that can counteract the robustness gains from scaling. The conclusion is that while inference scaling is a helpful tool for improving safety, it is not a complete solution on its own.![An analysis from the Trading Inference-Time Compute for Adversarial Robustness paper.](https://substackcdn.com/image/fetch/$s_!Gt2_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F704acd82-10a8-4879-9bd3-26bb67c3155f_1600x1173.png)

Image 12: An analysis from the Trading Inference-Time Compute for Adversarial Robustness paper. (Image by Zaremba et al. from [Trading Inference-Time Compute for Adversarial Robustness [[8]](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness)])

## Chain-of-Associated-Thoughts

*CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning* [[20]](https://arxiv.org/html/2502.02390v3) proposes a framework that combines Monte Carlo Tree Search (MCTS) with an "associative memory." This memory acts as a dynamic knowledge base during inference, allowing the model to recall earlier reasoning paths and incorporate newly generated information without losing context.

This synergy between the structured exploration of MCTS and the adaptive learning of the associative memory helps the model to systematically explore different reasoning pathways at test time. The result is a more comprehensive and coherent reasoning process, leading to improved accuracy on complex tasks.![A visualization of the CoAT: Chain-of-Associated-Thoughts Framework.](https://substackcdn.com/image/fetch/$s_!AtpC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d0635fb-c0b4-45df-b8d3-b54254ab92b5_1600x777.png)

Image 13: A visualization of the CoAT: Chain-of-Associated-Thoughts Framework. (Image by Yang et al. from [CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning [[20]](https://arxiv.org/html/2502.02390v3)])

## Step Back to Leap Forward

*Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models* [[21]](https://arxiv.org/html/2502.04404v1), [[22]](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947) introduces a self-backtracking mechanism that teaches models to recognize and revise their own suboptimal reasoning paths. This is achieved through a two-phase process.

During the training phase, the model learns to generate a special `<backtrack>` token when it identifies a point in its reasoning that needs correction. This teaches the model *when* and *where* to backtrack.

Then, at inference time, the model leverages this learned ability to perform a tree-based search. When the `<backtrack>` token is generated, the model revisits the previous step and explores an alternative path. A key advantage of this approach is that it does not require an external reward model, unlike standard process-reward-guided search methods. This allows the model to dynamically adjust its search depth and breadth using its own acquired backtracking skill.![A diagram of the Step Back to Leap Forward: Self-Backtracking mechanism.](https://substackcdn.com/image/fetch/$s_!e6x3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1df5fbf3-97f2-4976-b46f-2d5196b6bdc4_1594x888.png)

Image 14: A diagram of the Step Back to Leap Forward: Self-Backtracking mechanism. (Image by Tian et al. from [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models [[21]](https://arxiv.org/html/2502.04404v1)])

## Scaling up Test-Time Compute with Latent Reasoning

The paper *Scaling Test-Time Compute: How Recurrent Depth Transforms AI Reasoning* [[23]](https://huggingface.co/papers/2502.05171), [[24]](https://openreview.net/forum?id=S3GhJooWIC), [[25]](https://neurips.cc/virtual/2025/poster/117966), [[26]](https://icml.cc/virtual/2025/51856), [[27]](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db) proposes a novel architecture that uses recurrent depth to iterate in latent space, rather than producing additional output tokens. This approach is similar to how a Recurrent Neural Network (RNN) works, with the model refining its internal hidden state through multiple computation rounds before generating an output.

This allows the model to "think" more deeply about a problem without increasing the length of its visible output. While this can lead to performance improvements, it comes with a major drawback: the absence of explicit reasoning steps makes the model's thought process opaque, which can be a challenge for human interpretability and debugging.![A visualization of the Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach.](https://substackcdn.com/image/fetch/$s_!kVPW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb82da925-5736-44ba-bed1-ea3207b06382_1516x602.png)

Image 15: A visualization of the Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach. (Image by Geiping et al. from [Scaling by Thinking in Continuous Space [[23]](https://huggingface.co/papers/2502.05171)])

## Can a 1B LLM Surpass a 405B LLM?

*Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling* [[18]](https://arxiv.org/abs/2502.06703) presents a systematic study of the interactions between inference-time scaling, process reward models (PRMs), and problem difficulty. The authors propose a compute-optimal scaling strategy that adapts the inference budget based on the specific PRM being used, the size of the policy model, and the complexity of the task at hand.

The paper provides compelling evidence that a 1B parameter model, when paired with the right scaling strategy, can outperform an unscaled 405B Llama 3 model on the same benchmarks. This finding has broad implications for AI engineering, as it suggests that smaller, more efficient models can achieve state-of-the-art performance with the right inference-time techniques. This directly informs the trade-off decisions that engineers must make between model size, cost, and performance.![A comparison of compute-optimal scaling.](https://substackcdn.com/image/fetch/$s_!DiM2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c471e7f-36e7-41a8-a7e0-80bebf3c0f36_1600x1046.png)

Image 16: A comparison of compute-optimal scaling. (Image by Liu et al. from [Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling [[18]](https://arxiv.org/abs/2502.06703)])

## Learning to Reason from Feedback at Test-Time

The method proposed in *Learning to Reason from Feedback at Test-Time* [[19]](https://www.arxiv.org/abs/2502.12521) is challenging to classify as either a pure inference-time or training-time technique, as it updates the model's weights during inference.

The paper introduces the OpTune optimizer, which adjusts the model's weights based on previous mistakes without storing the failed attempts in the prompt context. This is in contrast to sequential revision methods, which grow the context length with each attempt, and parallel sampling methods, which generate multiple independent responses.

The key benefit of this approach is that it allows the model to "remember" its errors through lightweight weight updates, rather than relying on an ever-expanding context window. This makes it a more memory-efficient way to learn from feedback at test time.![A visualization of the OpTune optimizer from the Learning to Reason from Feedback at Test-Time paper.](https://substackcdn.com/image/fetch/$s_!nJMD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1925302-7fc2-4c7b-91e9-1c0fc4f0609e_1426x652.png)

Image 17: A visualization of the OpTune optimizer from the Learning to Reason from Feedback at Test-Time paper. (Image by Wu et al. from [Learning to Reason from Feedback at Test-Time [[19]](https://www.arxiv.org/abs/2502.12521)])

## Inference-Time Computations for LLM Reasoning and Planning

*Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights* [[19]](https://www.arxiv.org/abs/2502.12521), [[28]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM) introduces Sys2Bench, a comprehensive benchmark that evaluates various inference-time techniques across eleven diverse tasks. The benchmark covers a wide range of domains, including arithmetic, logical, and commonsense reasoning, as well as algorithmic reasoning and planning.

The key insight from this paper is that no single inference-time technique consistently performs well across all task types. This forces engineers to match the right method to the specific domain they are working in. The paper also provides a detailed analysis of the trade-offs between computational cost and performance for each technique, offering valuable guidance for practical applications.![Benchmark results from Inference-Time Computations for LLM Reasoning and Planning.](https://substackcdn.com/image/fetch/$s_!Vm7j!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42115dab-1086-4035-9a64-65a83631377e_1600x1023.png)

Image 18: Benchmark results from Inference-Time Computations for LLM Reasoning and Planning. (Image by Liu et al. from [Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights [[19]](https://www.arxiv.org/abs/2502.12521)])

## Inner Thinking Transformer

The *Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking* [[12]](https://aclanthology.org/2025.acl-long.1369.pdf), [[13]](https://arxiv.org/pdf/2502.13842), [[14]](https://arxiv.org/html/2502.13842v1), [[15]](https://www.emergentmind.com/topics/inner-thinking-transformer-itt) introduces a dynamic depth scaling mechanism that avoids using a fixed number of transformer layers for every token.

The core of this approach is Adaptive Token Routing, a technique that selectively sends more difficult tokens through the same layer multiple times. This allows the model to increase its inference compute budget specifically for the tokens that require more complex reasoning. By allocating extra "thinking" effort exactly where it is needed, this mechanism improves performance without lengthening the overall output sequence.![A diagram of the Adaptive Token Routing mechanism from the Inner Thinking Transformer paper.](https://substackcdn.com/image/fetch/$s_!-oC7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a6eb47e-fcbe-4c71-8d45-e7d82ae14ba1_1414x1090.png)

Image 19: A diagram of the Adaptive Token Routing mechanism from the Inner Thinking Transformer paper. (Image by Chen et al. from [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking [[13]](https://arxiv.org/pdf/2502.13842)])

## Test Time Scaling for Code Generation

The paper *S\*: Test Time Scaling for Code Generation* [[48]](https://arxiv.org/abs/2502.14382) introduces a method specialized for code that combines parallel generation of candidate solutions with sequential iterative debugging. This hybrid approach is designed to improve both the coverage of potential solutions and the accuracy of the final selection. It pushes the limits of existing parallel scaling by integrating sequential scaling through iterative debugging, while also introducing a novel adaptive selection mechanism grounded in code execution.![An overview of the S*: Test Time Scaling for Code Generation method.](https://substackcdn.com/image/fetch/$s_!quMS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94a88f17-b4b1-4642-aeb1-6db29071ef91_972x752.png)

Image 20: An overview of the S*: Test Time Scaling for Code Generation method. (Image by Li et al. from [S\*: Test Time Scaling for Code Generation [[48]](https://arxiv.org/abs/2502.14382)])

The process operates in two stages. First, in the generation stage, the model produces multiple code samples in parallel. Each sample is then refined through iterative debugging, using execution feedback from public test cases to identify and fix errors. This sequential refinement continues until a sample passes all public tests or a maximum number of revisions is reached.

In the second stage, the selection and repair process begins. The paper introduces a technique called "adaptive input synthesis," which creates discriminating test cases to distinguish between solutions that pass the initial public tests. For each pair of candidate solutions, an LLM generates specific test inputs that are likely to produce different outputs. These inputs are then executed, and the results are used to ground the LLM's final selection. By generating inputs that are likely to cause failure in incorrect solutions, the system can more reliably identify the best candidate. This approach connects back to earlier Google research on optimal test-time compute scaling, applying similar principles to the domain of code generation [[17]](https://arxiv.org/abs/2408.03314).

## Chain of Draft

The paper *Chain of Draft: Thinking Faster by Writing Less* [[39]](https://www.helicone.ai/blog/chain-of-draft), [[40]](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft), [[41]](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169), [[42]](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock), [[43]](https://arxiv.org/html/2502.18600v1) is based on the observation that humans often use concise drafts or shorthand notes when solving problems, rather than verbose, step-by-step explanations.

Inspired by this, the authors propose Chain of Draft (CoD) prompting, a technique that encourages the model to generate minimal yet informative intermediate steps. Instead of full natural-language reasoning, the model produces a series of short "drafts" that capture the essential logic of the solution.

This approach offers efficiency gains, drastically reducing the token count while maintaining an accuracy comparable to that of full chain-of-thought on reasoning benchmarks. The main trade-off is the loss of human-readable reasoning traces. This makes CoD a valuable tool for engineers who need to balance performance and cost, and can sacrifice some interpretability for speed.![A comparison of standard, CoT, and CoD prompting.](https://substackcdn.com/image/fetch/$s_!Gaj6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869a967-9498-435f-85f2-a38557db14e3_1460x982.png)

Image 21: A comparison of standard, CoT, and CoD prompting. (Image by Li et al. from [Chain of Draft: Thinking Faster by Writing Less [[43]](https://arxiv.org/html/2502.18600v1)])

## Better Feedback and Edit Models

A key challenge in applying inference scaling to open-ended tasks like creative writing or high-level planning is the lack of verifiable answers. Without a clear ground truth, it's difficult for a model to evaluate and refine its own outputs.

The paper *Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks* [[44]](https://arxiv.org/html/2503.04378v1), [[45]](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended) addresses this by proposing a specialized architecture that decouples the generation, feedback, and editing processes. It uses three separate models: a generator model to produce the initial response, a feedback model to provide critiques, and an edit model to make revisions.

These feedback and edit models are trained on large, human-annotated datasets of responses, critiques, and revisions, allowing them to produce higher-quality signals than a single model performing self-critique could. This dedicated system enables an iterative refinement loop during inference that has been shown to surpass the performance of generic self-critique methods on open-ended tasks.![The system architecture for Dedicated Feedback and Edit Models for Inference-Time Scaling.](https://substackcdn.com/image/fetch/$s_!zA8v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73568387-83fb-4744-bd3d-f5cbcfe53f1d_1136x716.png)

Image 22: The system architecture for Dedicated Feedback and Edit Models for Inference-Time Scaling. (Image by Wang et al. from [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks [[44]](https://arxiv.org/html/2503.04378v1)])

## Conclusion

Inference-time compute scaling has firmly established itself as a major research direction in 2025. Its appeal lies in its ability to enhance the performance of existing models without the need for permanent weight modifications, making it a flexible and powerful tool for AI engineers.

In this article, we have surveyed a wide range of techniques, from simple "wait" tokens and budget forcing to sophisticated search algorithms, optimization loops, dynamic routing, and even latent-space iteration. A recurring theme across these papers is the remarkable finding that smaller models, when equipped with proper inference-time scaling, can rival or even exceed the performance of much larger models that lack such capabilities. This has profound implications for how we approach model development and deployment, suggesting that a smaller, more agile model with the right inference strategy can be more effective than a monolithic giant.

However, this power comes with important caveats. Increased inference compute translates directly to higher costs and latency, which can impact user experience. Furthermore, as we have seen, there is no universally best technique; the optimal approach often depends on the specific task, model, and constraints of the application. This highlights the need for a nuanced, engineering-driven approach to selecting and implementing these methods.

We are already seeing an emerging industry trend toward "thinking-on-demand" toggles, which allow developers or even end-users to dial the inference compute up or down depending on the difficulty of the task. This flexibility is a key advantage of inference-time scaling, and we predict that explicit reasoning will become the default mode of operation for future agentic systems, rather than an optional feature. As these systems become more integrated into our daily lives, the ability to dynamically allocate computational resources will be essential for balancing performance, cost, and efficiency.

This article has focused on the inference-time side of the equation. In our upcoming article, we will shift our focus to train-time compute scaling methods, including advanced reinforcement learning, hybrid RL plus SFT approaches, and distillation techniques. Stay tuned as we continue to explore the cutting edge of AI reasoning.![A chart showing performance scaling across different dimensions.](https://substackcdn.com/image/fetch/$s_!nhEn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1f749e4-4167-4013-b1c9-651c83bf8d3b_1504x756.png)

Image 23: A chart showing performance scaling across different dimensions. (Image by Wang et al. from [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks [[44]](https://arxiv.org/html/2503.04378v1)])

## References

- [1] Gange, J. D. (2025). Paper Review of s1: Simple Test-Time Scaling. [https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8)
- [2] Muennighoff, N., et al. (2025). s1: Simple test-time scaling. [https://huggingface.co/papers/2501.19393](https://huggingface.co/papers/2501.19393)
- [3] Li, Y., et al. (2025). Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback. [https://icml.cc/virtual/2025/poster/46149](https://icml.cc/virtual/2025/poster/46149)
- [4] Li, Y., et al. (2025). Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback. [https://proceedings.mlr.press/v267/li25ac.html](https://proceedings.mlr.press/v267/li25ac.html)
- [5] Bogolin, V. (2025). Thoughts All Over the Place: On the Underthinking of o1-Like LLMs. [https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme)
- [6] Wang, Y., et al. (2025). Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs. [https://tldr.takara.ai/p/2501.18585](https://tldr.takara.ai/p/2501.18585)
- [7] Zaremba, W., et al. (2025). Trading Inference-Time Compute for Adversarial Robustness. [https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf)
- [8] Zaremba, W., et al. (2025). Trading inference-time compute for adversarial robustness. [https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness)
- [9] Zaremba, W., et al. (2025). Trading Inference-Time Compute for Adversarial Robustness. [https://huggingface.co/papers/2501.18841](https://huggingface.co/papers/2501.18841)
- [10] Zaremba, W., et al. (2025). Trading Inference-Time Compute for Adversarial Robustness. [https://www.youtube.com/watch?v=6Yxc6uh0RyE](https://www.youtube.com/watch?v=6Yxc6uh0RyE)
- [11] Barak, B., et al. (2025). On the (In)security of Test-Time Compute. [https://arxiv.org/html/2507.15974v1](https://arxiv.org/html/2507.15974v1)
- [12] Chen, Y., et al. (2025). Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking. [https://aclanthology.org/2025.acl-long.1369.pdf](https://aclanthology.org/2025.acl-long.1369.pdf)
- [13] Chen, Y., et al. (2025). Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking. [https://arxiv.org/pdf/2502.13842](https://arxiv.org/pdf/2502.13842)
- [14] Chen, Y., et al. (2025). Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking. [https://arxiv.org/html/2502.13842v1](https://arxiv.org/html/2502.13842v1)
- [15] Chen, Y., et al. (2025). Inner Thinking Transformer (ITT). [https://www.emergentmind.com/topics/inner-thinking-transformer-itt](https://www.emergentmind.com/topics/inner-thinking-transformer-itt)
- [16] Raschka, S. (2025). Understanding Reasoning LLMs. [https://magazine.sebastianraschka.com/p/understanding-reasoning-llms](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)
- [17] Snell, C., et al. (2024). Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters. [https://arxiv.org/abs/2408.03314](https://arxiv.org/abs/2408.03314)
- [18] Liu, F., et al. (2025). Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling. [https://arxiv.org/abs/2502.06703](https://arxiv.org/abs/2502.06703)
- [19] Wu, Y., et al. (2025). Learning to Reason from Feedback at Test-Time. [https://www.arxiv.org/abs/2502.12521](https://www.arxiv.org/abs/2502.12521)
- [20] Yang, H., et al. (2025). CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning. [https://arxiv.org/html/2502.02390v3](https://arxiv.org/html/2502.02390v3)
- [21] Tian, H., et al. (2025). Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models. [https://arxiv.org/html/2502.04404v1](https://arxiv.org/html/2502.04404v1)
- [22] Tian, H., et al. (2025). Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models. [https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947)
- [23] Geiping, J., et al. (2025). Scaling by Thinking in Continuous Space. [https://huggingface.co/papers/2502.05171](https://huggingface.co/papers/2502.05171)
- [24] Geiping, J., et al. (2025). Scaling by Thinking in Continuous Space. [https://openreview.net/forum?id=S3GhJooWIC](https://openreview.net/forum?id=S3GhJooWIC)
- [25] Geiping, J., et al. (2025). Scaling by Thinking in Continuous Space. [https://neurips.cc/virtual/2025/poster/117966](https://neurips.cc/virtual/2025/poster/117966)
- [26] Geiping, J., et al. (2025). Scaling by Thinking in Continuous Space. [https://icml.cc/virtual/2025/51856](https://icml.cc/virtual/2025/51856)
- [27] Sahin, S. (2025). Scaling Test-Time Compute: How Recurrent Depth Transforms AI Reasoning. [https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db)
- [28] Liu, F., et al. (2025). Bag of Tricks for Inference-time Computation of LLM Reasoning. [https://github.com/usail-hkust/benchmark_inference_time_computation_LLM](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [29] Tian, P. (2026). The Token Economics of Chain-of-Thought: When Thinking Costs More Than It's Worth. [https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more)
- [30] Zhang, Y., et al. (2025). The Cost of Thinking: A Survey on Efficiency in LLM Reasoning. [https://aclanthology.org/2025.emnlp-main.165.pdf](https://aclanthology.org/2025.emnlp-main.165.pdf)
- [31] Aussie AI. (2025). Chain-of-Thought Optimization for Production-Grade LLM Applications. [https://www.aussieai.com/research/cot-optimization](https://www.aussieai.com/research/cot-optimization)
- [32] Jones, M. (2024). Token Efficiency in Chain-of-Thought Reasoning. [https://arxiv.org/html/2406.09136v1](https://arxiv.org/html/2406.09136v1)
- [33] Mack, E. (2024). Tech Report: Chain of Thought. [https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought)
- [34] Li, S., et al. (2025). VersaPRM: A General-Purpose Process Reward Model for Large Language Models. [https://openreview.net/forum?id=l19DmXbwPK](https://openreview.net/forum?id=l19DmXbwPK)
- [35] Li, S., et al. (2025). VersaPRM: A General-Purpose Process Reward Model for Large Language Models. [https://icml.cc/virtual/2025/oral/47195](https://icml.cc/virtual/2025/oral/47195)
- [36] Wu, Y., et al. (2025). SCOPE: A Confidence-Guided Test-Time RL Framework for Language Model Reasoning. [https://arxiv.org/html/2512.15146v1](https://arxiv.org/html/2512.15146v1)
- [37] Lightman, H., et al. (2023). Let's Verify Step by Step. [https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf)
- [38] Wolfe, C. (2024). Reward Models. [https://cameronrwolfe.substack.com/p/reward-models](https://cameronrwolfe.substack.com/p/reward-models)
- [39] Li, S., et al. (2025). Chain of Draft: Thinking Faster by Writing Less. [https://www.helicone.ai/blog/chain-of-draft](https://www.helicone.ai/blog/chain-of-draft)
- [40] Gupta, P. (2025). Chain of Draft (CoD) Prompting: A Deep Dive. [https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft)
- [41] Data Science in Your Pocket. (2025). What is Chain of Drafts? Bye Bye Chain of Thoughts? [https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169)
- [42] Barr, D. (2025). Move beyond Chain-of-Thought with Chain-of-Draft on Amazon Bedrock. [https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock)
- [43] Li, S., et al. (2025). Chain of Draft: Thinking Faster by Writing Less. [https://arxiv.org/html/2502.18600v1](https://arxiv.org/html/2502.18600v1)
- [44] Wang, Z., et al. (2025). Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks. [https://arxiv.org/html/2503.04378v1](https://arxiv.org/html/2503.04378v1)
- [45] Wang, Z., et al. (2025). Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks. [https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended)
- [46] Kojima, T., et al. (2022). Large Language Models are Zero-Shot Reasoners. [https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)
- [47] OpenAI. (2024). o1 Report. [https://openai.com/index/o1-report/](https://openai.com/index/o1-report/)
- [48] Li, R., et al. (2025). S\*: Test Time Scaling for Code Generation. [https://arxiv.org/abs/2502.14382](https://arxiv.org/abs/2502.14382)
</article>