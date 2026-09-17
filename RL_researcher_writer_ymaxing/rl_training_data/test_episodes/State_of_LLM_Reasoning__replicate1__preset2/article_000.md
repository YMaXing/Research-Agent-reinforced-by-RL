# The 2025 AI Engineer's Guide to Inference-Time Compute Scaling

In 2025, building complex agentic systems is no longer a niche research area; it is a core task for AI Engineers. These systems need to solve multi-step problems that go far beyond simple question-answering, but direct-answer models often fail at this. This reliability gap has made stronger LLM reasoning a top priority.

Since the release of models like DeepSeek-R1, the research landscape has exploded with new techniques that blend inference-time scaling, pure reinforcement learning (RL), supervised fine-tuning (SFT), and distillation. This article focuses on one of these areas: the rapid advancements in inference-time compute scaling. We will survey the key papers published in this domain, providing a comprehensive update for engineers who need to balance model size, cost, latency, and accuracy.![Image 1: The four main categories of implementing reasoning models. This article focuses on inference-time-scaling methods.](https://substackcdn.com/image/fetch/$s_!IOSP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf9e2677-652a-4af1-9f57-dc0c253d2198_1448x1260.png)

Image 1: The four main categories of implementing reasoning models. This article focuses on inference-time-scaling methods. (Source [magazine.sebastianraschka.com [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)])

To build a solid foundation, we will first examine the four main categories of reasoning models so you can understand how inference-time scaling fits into the broader landscape.

## Implementing and improving reasoning in LLMs: The four main categories

The development of reasoning models represents a specialization in the LLM field. We refine general-purpose LLMs to excel at complex tasks that are best solved with intermediate steps, such as advanced math and coding challenges. We define these "reasoning models" as those that generate an explicit or internal thought process before producing a final answer. This is a clear departure from direct-answer LLMs, which map an input directly to an output in a single forward pass [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).![Image 2: A regular LLM may only provide a short answer, whereas reasoning models typically include intermediate steps that reveal part of the thought process.](https://substackcdn.com/image/fetch/$s_!ZsN9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8abbfe39-f656-4845-b376-18c1e563210a_1326x564.png)

Image 2: A regular LLM may only provide a short answer, whereas reasoning models typically include intermediate steps that reveal part of the thought process. (Source [magazine.sebastianraschka.com [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)])

There are two primary ways to enhance a model's reasoning capabilities: increasing training compute or increasing inference compute. Training compute involves modifying the model's weights through methods like RL or SFT. Inference compute, on the other hand, involves allocating extra FLOPs at test time to improve output quality without changing the model's weights. A simple example of this is chain-of-thought (CoT) prompting, where adding "Let's think step by step" encourages the model to generate intermediate reasoning, thereby using more compute to arrive at an answer [[32]](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more), [[33]](https://aclanthology.org/2025.emnlp-main.165.pdf), [[34]](https://www.aussieai.com/research/cot-optimization), [[35]](https://arxiv.org/html/2406.09136v1), [[36]](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought).![Image 3: Accuracy improvements can be achieved through increased training or test-time compute, where test-time compute is synonymous with inference-time compute and inference-time scaling.](https://substackcdn.com/image/fetch/$s_!pgyl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddde6f39-3b88-4962-9d02-2cf767dc82e9_1484x994.png)

Image 3: Accuracy improvements can be achieved through increased training or test-time compute, where test-time compute is synonymous with inference-time compute and inference-time scaling. (Source [arxiv.org [[49]](https://arxiv.org/abs/2502.14382)])

In practice, most systems blend heavy train-time preparation with test-time thinking to achieve the best results. Relying solely on training can lead to issues like reward hacking, where the model learns to exploit the reward function without genuinely improving its reasoning. Conversely, pure inference scaling on a weak base model often yields limited gains. The development of reasoning models generally falls into four main categories, each with its own trade-offs [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).![Image 4: The four main approaches to building and improving reasoning models.](https://substackcdn.com/image/fetch/$s_!_2dU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5e5fdf9-e72c-497b-9cf4-b4e3c24f33f1_1600x591.png)

Image 4: The four main approaches to building and improving reasoning models. (Source [magazine.sebastianraschka.com [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)])

**1. Inference-time compute scaling** improves reasoning without altering the underlying model. This approach increases computational resources during inference to enhance output quality. While models like OpenAI's o1 are suspected to use this technique, the DeepSeek-R1 paper reported that their attempts with explicit inference-time methods were largely unsuccessful. However, their model does exhibit a form of implicit inference scaling by generating longer, more detailed responses, which naturally increases inference costs [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

**2. Pure reinforcement learning (RL)** has shown that reasoning can emerge as a learned behavior without supervised fine-tuning. DeepSeek-R1-Zero, for instance, was trained exclusively with RL and developed basic reasoning skills, including generating intermediate "thinking" steps. However, this approach faces challenges, as it can be difficult to define a reward function that consistently encourages effective reasoning without leading to reward hacking [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

**3. Reinforcement learning and supervised fine-tuning (SFT)** is a hybrid approach that combines the strengths of both methods. This is the strategy used to build high-performance reasoning models like DeepSeek-R1. The process typically starts with an SFT stage to establish a baseline, followed by RL to further refine the model's reasoning capabilities. This combination allows the model to learn from both explicit examples and reward-based feedback, leading to more robust and reliable performance [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

**4. Supervised fine-tuning and model distillation** offers a cost-effective way to create smaller, more efficient reasoning models. In this context, "distillation" refers to instruction fine-tuning a smaller model on an SFT dataset generated by a larger, more capable model. While this approach doesn't produce state-of-the-art models, it allows for the creation of surprisingly strong reasoners at a fraction of the size and cost. However, it's important to note that this method differs from traditional knowledge distillation, which typically involves training a student model on the logits of a teacher model [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

With these four categories mapped out, we can now zoom in on inference-time compute scaling, which forms the core of this article.

## Inference-time compute scaling methods

The core idea behind inference-time compute scaling is that allowing a model to "think longer" can lead to better answers, much like how humans benefit from spending more time on difficult problems. This principle has a strong precedent in game-playing AI like AlphaGo, which used Monte Carlo Tree Search at inference to evaluate possible moves—a critical factor in its superhuman performance [[60]](https://ve3.global/blog/inference-time-scaling-the-next-frontier-in-ai-performance). The most direct method is prompt engineering. Classic techniques like CoT, which encourages the model to generate step-by-step reasoning, directly increase the number of tokens generated, which in turn raises latency and cost [[32]](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more), [[33]](https://aclanthology.org/2025.emnlp-main.165.pdf), [[34]](https://www.aussieai.com/research/cot-optimization), [[35]](https://arxiv.org/html/2406.09136v1), [[36]](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought).![Image 5: An example of classic CoT prompting.](https://substackcdn.com/image/fetch/$s_!Knds!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d37faa4-3261-492c-85a4-766926b8c17c_1600x419.png)

Image 5: An example of classic CoT prompting. (Source [arxiv.org [[50]](https://arxiv.org/abs/2205.11916)])

Beyond simple prompting, more advanced methods involve search and voting strategies. These can be parallel, like majority voting, where multiple answers are generated and the most frequent one is selected, or sequential, like beam search, which explores multiple reasoning paths and prunes less promising ones. These approaches often rely on process reward models (PRMs) to guide the search by evaluating the quality of intermediate steps [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms), [[37]](https://openreview.net/forum?id=l19DmXbwPK), [[38]](https://icml.cc/virtual/2025/oral/47195), [[39]](https://arxiv.org/html/2512.15146v1), [[40]](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf), [[41]](https://cameronrwolfe.substack.com/p/reward-models).![Image 6: Different search-based methods often use a process-reward model to select the best answer.](https://substackcdn.com/image/fetch/$s_!O9a-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ad9742b-993f-4ecd-8f80-2fa41d43164b_1334x798.png)

Image 6: Different search-based methods often use a process-reward model to select the best answer. (Source [arxiv.org [[49]](https://arxiv.org/abs/2502.14382)])

Now, let's examine a concrete recent example of these ideas in the *s1* paper, which combines curated reasoning traces with explicit length-control tokens.

## s1: Simple test-time scaling

The paper *s1: Simple test-time scaling* introduces a hybrid approach that combines a small, curated SFT dataset of 1,000 reasoning traces with an inference-time length control mechanism [[61]](https://arxiv.org/abs/2501.19393). This distinguishes it from pure distillation methods, as it actively manages compute at test time.

A key mechanism in this paper is the use of "wait" tokens. When the model attempts to conclude its reasoning prematurely, the system suppresses the end-of-thinking token and instead appends "Wait." This simple intervention encourages the model to double-check its work, often leading to self-correction and improved accuracy. The paper's empirical results show that "Wait" is more effective than a neutral phrase like "Hmm," suggesting that inducing doubt is a crucial part of the self-correction process [[61]](https://arxiv.org/abs/2501.19393). This is reminiscent of the "Aha!" moment observed during the training of DeepSeek-R1, where the model spontaneously began to use reflective language.![Image 7: A visualization of how "wait" tokens are used to control the length of the model's output.](https://substackcdn.com/image/fetch/$s_!qk_K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e7f4d94-9f8f-4353-87ad-78f3cba7b9cd_1154x854.png)

Image 7: A visualization of how "wait" tokens are used to control the length of the model's output. (Source [arxiv.org [[61]](https://arxiv.org/abs/2501.19393)])

This technique is part of a broader strategy called **budget forcing**, a sequential scaling method that gives engineers precise control over the length of the model's output. It can either cut the reasoning process short by appending an end-of-thinking token or extend it with "wait" tokens. This contrasts with parallel methods like majority voting, which generate multiple independent responses. The paper reports a clear correlation between the length of the generated response and the accuracy on reasoning benchmarks, with performance scaling positively with increased compute.![Image 8: The correlation between response accuracy and the length of the reasoning trace.](https://substackcdn.com/image/fetch/$s_!kYWF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7f0c49b-a644-4142-bed0-7d114ecd39c2_798x456.png)

Image 8: The correlation between response accuracy and the length of the reasoning trace. (Source [arxiv.org [[61]](https://arxiv.org/abs/2501.19393)])

However, the authors acknowledge the limitations of their approach. The performance gains from budget forcing eventually plateau, and the technique is constrained by the model's context window. They also call for future work to compare their method against other scaling techniques like beam search, lookahead search, and compute-optimal search, which we will explore later in this article.![Image 9: A comparison of the effectiveness of "Wait" vs. "Hmm" tokens.](https://substackcdn.com/image/fetch/$s_!Qd4X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bdfe7db-8c97-4240-8be0-11efa7abdf7c_758x510.png)

Image 9: A comparison of the effectiveness of "Wait" vs. "Hmm" tokens. (Source [arxiv.org [[61]](https://arxiv.org/abs/2501.19393)])

## Other noteworthy research papers on inference-time compute scaling

The field of inference-time compute scaling is evolving rapidly, with a high volume of recent papers exploring new techniques. To provide a broad overview without getting lost in repetitive details, we will briefly summarize the key contributions of several noteworthy papers.

A common pattern among these studies is the blending of some form of training with explicit control of inference-time compute. This is a departure from purely prompt-based scaling, as it involves preparing the model to respond to these new control mechanisms. It's also important to differentiate these regulated approaches from SFT or distillation methods that simply train models to produce longer outputs. The key distinction is the active management of compute or output length during the inference phase.

## Test-Time Preference Optimization

The paper *Test-Time Preference Optimization* introduces a purely inference-time method that avoids any changes to the underlying model weights [[3]](https://icml.cc/virtual/2025/poster/46149), [[4]](https://proceedings.mlr.press/v267/li25ac.html). It uses an iterative, on-the-fly alignment process to progressively improve outputs for each query.

The method employs a four-step loop. First, it generates multiple responses and uses a reward model to select the best ("chosen") and worst ("rejected") ones. Next, the model generates textual critiques that analyze the strengths of the chosen response and the weaknesses of the rejected one. These critiques then guide the model to generate a refined set of responses for the next iteration. This cycle of generation, scoring, critique, and refinement continues, allowing the model to align its output with the reward model's preferences at test time.![Image 10: The four-step process of Test-Time Preference Optimization.](https://substackcdn.com/image/fetch/$s_!dmJN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2a1bd16-7cf7-4898-8dce-a2d8352f76a8_1600x819.png)

Image 10: The four-step process of Test-Time Preference Optimization. (Source [arxiv.org [[51]](https://arxiv.org/abs/2501.12895)])

## Thoughts Are All Over the Place

The paper *Thoughts Are All Over the Place* identifies a phenomenon in o1-like models called **underthinking**, where frequent switching between reasoning paths leads to a decrease in final accuracy [[5]](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme), [[6]](https://tldr.takara.ai/p/2501.18585). To address this, the authors propose a method called **Thought Switching Penalty (TIP)**.

TIP is a decoding strategy that modifies the model's logits at inference time to discourage premature transitions between reasoning paths. By applying a penalty to tokens associated with thought switching, the method encourages the model to explore each promising path more deeply before moving on to an alternative. This approach improves accuracy on challenging benchmarks without requiring any fine-tuning, making it a lightweight and effective way to enhance reasoning.![Image 11: A visualization of the Thought Switching Penalty (TIP) method.](https://substackcdn.com/image/fetch/$s_!vvCX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7111ccaa-c4c1-4c7c-84f9-74d38df3c663_1528x894.png)

Image 11: A visualization of the Thought Switching Penalty (TIP) method. (Source [arxiv.org [[52]](https://arxiv.org/abs/2501.18585)])

## Trading Inference-Time Compute for Adversarial Robustness

The paper *Trading Inference-Time Compute for Adversarial Robustness* shows that increasing inference-time compute can improve a model's resilience to adversarial attacks, even without any adversarial training [[7]](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf), [[8]](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness), [[9]](https://huggingface.co/papers/2501.18841). The authors present empirical trade-off curves demonstrating that as the model is allowed to "think" longer, the success rate of various attacks generally decreases.

However, the paper also highlights important exceptions where these gains are limited. In scenarios involving policy ambiguity or the exploitation of loopholes, increased compute does not always lead to better robustness. The authors also introduce two new attack strategies, **Think Less** and **Nerd Sniping**, which are designed to counteract the benefits of scaling. These findings suggest that while inference scaling is a valuable tool for improving LLM safety, it is not a complete solution on its own.

A critical perspective on these findings points out that they rely on the assumption that the model's intermediate reasoning steps are hidden. Subsequent research has shown that if these reasoning steps are exposed, an "inverse scaling law" emerges: more compute consistently *reduces* robustness, as longer reasoning chains provide a larger attack surface [[62]](https://arxiv.org/html/2507.15974v1). This vulnerability can persist even with hidden chains in scenarios involving tool-use or advanced reasoning extraction attacks.![Image 12: An analysis of how increased inference-time compute affects adversarial robustness.](https://substackcdn.com/image/fetch/$s_!Gt2_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F704acd82-10a8-4879-9bd3-26bb67c3155f_1600x1173.png)

Image 12: An analysis of how increased inference-time compute affects adversarial robustness. (Source [arxiv.org [[53]](https://arxiv.org/abs/2501.18841)])

## Chain-of-Associated-Thoughts

The paper *CoAT: Chain-of-Associated-Thoughts* introduces a framework that combines Monte Carlo Tree Search (MCTS) with an **associative memory** mechanism [[21]](https://arxiv.org/html/2502.02390v3). This memory acts as a dynamic knowledge base during inference, allowing the model to recall earlier reasoning paths and incorporate newly generated information without losing context.

The synergy between the structured exploration of MCTS and the adaptive learning of the associative memory helps the model systematically explore a wider range of reasoning pathways at test time. This approach enhances the model's ability to handle complex problems that require iterative refinement and the integration of evolving information.![Image 13: A visualization of the Chain-of-Associated-Thoughts (CoAT) framework.](https://substackcdn.com/image/fetch/$s_!AtpC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d0635fb-c0b4-45df-b8d3-b54254ab92b5_1600x777.png)

Image 13: A visualization of the Chain-of-Associated-Thoughts (CoAT) framework. (Source [arxiv.org [[21]](https://arxiv.org/html/2502.02390v3)])

## Step Back to Leap Forward

The paper *Step Back to Leap Forward* presents a **self-backtracking** mechanism that teaches models to recognize and correct suboptimal reasoning paths [[22]](https://arxiv.org/html/2502.04404v1), [[23]](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947). During training, the model learns to generate a special backtrack token when it identifies a flawed step. This learned ability is then leveraged during inference through a tree-based search that allows the model to dynamically adjust its search depth and breadth.

A key advantage of this approach is that it does not require an external reward model, which is typically used in process-reward-guided search methods. Instead, the model internalizes the ability to evaluate its own reasoning, making it more autonomous and efficient. The self-backtracking mechanism allows for a flexible search process where the model can systematically revisit and revise its decisions, leading to more robust and accurate solutions.![Image 14: The self-backtracking mechanism from "Step Back to Leap Forward."](https://substackcdn.com/image/fetch/$s_!e6x3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1df5fbf3-97f2-4976-b46f-2d5196b6bdc4_1594x888.png)

Image 14: The self-backtracking mechanism from "Step Back to Leap Forward." (Source [arxiv.org [[54]](https://arxiv.org/html/2502.04404v1)])

## Scaling up Test-Time Compute with Latent Reasoning

The paper *Scaling Test-Time Compute* introduces a **recurrent depth** approach that allows a model to "think" in its latent space rather than by generating additional output tokens [[24]](https://huggingface.co/papers/2502.05171), [[25]](https://openreview.net/forum?id=S3GhJooWIC), [[26]](https://neurips.cc/virtual/2025/poster/117966), [[27]](https://icml.cc/virtual/2025/51856), [[28]](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db). This method iterates a recurrent block to refine the model's understanding before generating output, similar to an RNN.

This iterative process continues until the hidden state converges, which can be determined by the KL-divergence between steps falling below a set threshold [[63]](https://www.lesswrong.com/posts/pLnLSgWphqDbdorgi/on-recent-results-in-llm-latent-reasoning). The goal is to reach a stable fixed point where the representation no longer changes [[64]](https://arxiv.org/html/2605.26733v1). This technique enables deeper reasoning without increasing the length of the visible output. However, it comes with a major drawback: the absence of explicit reasoning steps makes it difficult for humans to interpret and debug the model's thought process.![Image 15: A visualization of the recurrent depth approach for latent reasoning.](https://substackcdn.com/image/fetch/$s_!kVPW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb82da925-5736-44ba-bed1-ea3207b06382_1516x602.png)

Image 15: A visualization of the recurrent depth approach for latent reasoning. (Source [arxiv.org [[55]](https://arxiv.org/abs/2502.05171)])

## Can a 1B LLM Surpass a 405B LLM?

The paper *Can 1B LLM Surpass 405B LLM?* conducts a systematic study of the interactions between inference-time scaling, process reward models (PRMs), and problem difficulty [[56]](https://arxiv.org/abs/2502.06703). The authors propose a **compute-optimal scaling** strategy that adapts the inference budget based on the specific PRM, policy model size, and task complexity.

Through extensive experiments, the paper provides evidence that a 1B model, when properly scaled, can outperform an unscaled 405B Llama 3 model on the same benchmarks. This finding has significant implications for AI engineers, as it demonstrates that the right inference budget can allow smaller, more efficient models to surpass much larger ones. This directly informs the trade-off decisions between model size, cost, and performance in production systems.![Image 16: A comparison of compute-optimal scaling for a 1B vs. a 405B model.](https://substackcdn.com/image/fetch/$s_!DiM2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c471e7f-36e7-41a8-a7e0-80bebf3c0f36_1600x1046.png)

Image 16: A comparison of compute-optimal scaling for a 1B vs. a 405B model. (Source [arxiv.org [[56]](https://arxiv.org/abs/2502.06703)])

## Learning to Reason from Feedback at Test-Time

The method presented in *Learning to Reason from Feedback at Test-Time* is challenging to classify as either a pure inference-time or training-time technique because it updates the model's weights during inference [[57]](https://www.arxiv.org/abs/2502.12521). The paper introduces the **OpTune optimizer**, which adjusts model weights based on previous mistakes without storing the failed attempts in the prompt context.

This weight-update approach is a departure from both sequential revision, which grows the context by adding previous attempts to the prompt, and parallel sampling, which generates multiple independent responses. The key benefit of OpTune is its ability to "remember" errors through lightweight weight updates, avoiding the need to manage an indefinitely growing context length. This hybrid approach offers a novel way to combine the benefits of both training and inference-time methods.![Image 17: A visualization of the OpTune optimizer, which updates model weights at test time.](https://substackcdn.com/image/fetch/$s_!nJMD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1925302-7fc2-4c7b-91e9-1c0fc4f0609e_1426x652.png)

Image 17: A visualization of the OpTune optimizer, which updates model weights at test time. (Source [www.arxiv.org [[57]](https://www.arxiv.org/abs/2502.12521)])

## Inference-Time Computations for LLM Reasoning and Planning

The paper *Inference-Time Computations for LLM Reasoning and Planning* introduces **Sys2Bench**, a comprehensive benchmark that evaluates various inference-time techniques across eleven diverse tasks [[29]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM), [[30]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM), [[31]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM), [[57]](https://www.arxiv.org/abs/2502.12521). The benchmark covers a wide range of domains, including arithmetic, logical, commonsense, and algorithmic reasoning, as well as planning.

The key insight from this study is that no single inference-time technique consistently dominates across all task types. This finding underscores the importance of matching the right method to the specific domain, forcing engineers to think critically about which approach is best suited for their particular use case. The paper also provides a detailed analysis of the trade-offs between computational cost and performance, offering valuable guidance for making informed decisions in production environments.![Image 18: Results from the Sys2Bench benchmark, showing the performance of various inference-time techniques across different tasks.](https://substackcdn.com/image/fetch/$s_!Vm7j!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42115dab-1086-4035-9a64-65a83631377e_1600x1023.png)

Image 18: Results from the Sys2Bench benchmark, showing the performance of various inference-time techniques across different tasks. (Source [www.arxiv.org [[57]](https://www.arxiv.org/abs/2502.12521)])

## Inner Thinking Transformer

The *Inner Thinking Transformer* paper introduces a **dynamic depth scaling** mechanism that avoids using a fixed number of Transformer layers for every token [[12]](https://aclanthology.org/2025.acl-long.1369.pdf), [[13]](https://arxiv.org/pdf/2502.13842), [[14]](https://arxiv.org/html/2502.13842v1), [[15]](https://www.emergentmind.com/topics/inner-thinking-transformer-itt). It uses **Adaptive Token Routing**, sending difficult tokens through the same layer multiple times.

This selectively increases the inference compute budget for harder tokens, allowing the model to allocate extra "thinking" effort exactly where it is needed. By doing so, the model can perform deeper processing on critical tokens without lengthening the overall output sequence. This dynamic routing improves efficiency. For instance, a 162M parameter ITT model showed a 1.7% performance gain over a standard transformer on reasoning tasks, achieving better results without increasing model size [[65]](https://liner.com/review/inner-thinking-transformer-leveraging-dynamic-depth-scaling-to-foster-adaptive).![Image 19: The Adaptive Token Routing mechanism from the Inner Thinking Transformer.](https://substackcdn.com/image/fetch/$s_!-oC7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a6eb47e-fcbe-4c71-8d45-e7d82ae14ba1_1414x1090.png)

Image 19: The Adaptive Token Routing mechanism from the Inner Thinking Transformer. (Source [arxiv.org [[58]](https://arxiv.org/abs/2502.13842)])

## Test Time Scaling for Code Generation

The paper *S\*: Test Time Scaling for Code Generation* proposes a method specialized for code that combines parallel generation of candidate solutions with sequential iterative debugging [[49]](https://arxiv.org/abs/2502.14382). This hybrid approach is designed to improve both the coverage of potential solutions and the accuracy of the final selection.![Image 20: An overview of the S* method for test-time scaling in code generation.](https://substackcdn.com/image/fetch/$s_!quMS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94a88f17-b4b1-4642-aeb1-6db29071ef91_972x752.png)

Image 20: An overview of the S* method for test-time scaling in code generation. (Source [arxiv.org [[49]](https://arxiv.org/abs/2502.14382)])

The S\* framework operates in a two-stage process. The first stage involves generating multiple code samples and using execution feedback from public test cases to iteratively repair and refine them. The second stage focuses on selecting the best candidate. This is where the paper introduces a novel technique called **adaptive input synthesis**, which creates discriminating test cases designed to tell the difference between solutions that have already passed all public tests. This approach, which is connected to earlier Google research on optimal test-time compute scaling, uses a combination of execution results and error messages to guide the repair and selection process, leading to more robust and accurate code generation.

## Chain of Draft

The paper *Chain of Draft: Thinking Faster by Writing Less* makes the observation that humans often rely on concise drafts rather than verbose, step-by-step explanations when solving problems [[42]](https://www.helicone.ai/blog/chain-of-draft), [[43]](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft), [[44]](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169), [[45]](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock), [[46]](https://arxiv.org/html/2502.18600v1). Inspired by this, the authors propose **Chain of Draft (CoD) prompting**, a technique that encourages the model to generate minimal yet informative intermediate steps instead of full natural-language reasoning.![Image 21: A comparison of Chain of Draft with standard and Chain of Thought prompting.](https://substackcdn.com/image/fetch/$s_!Gaj6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869a967-9498-435f-85f2-a38557db14e3_1460x982.png)

Image 21: A comparison of Chain of Draft with standard and Chain of Thought prompting. (Source [arxiv.org [[46]](https://arxiv.org/html/2502.18600v1)])

This approach offers significant efficiency gains by drastically reducing the number of tokens generated, while maintaining an accuracy comparable to that of full CoT on reasoning benchmarks. However, this efficiency comes at a trade-off: the loss of human-readable reasoning traces. This forces engineers to decide when the benefits of faster generation and lower cost outweigh the need for interpretability.

## Better Feedback and Edit Models

Applying inference scaling to open-ended tasks like creative writing or high-level planning is challenging because these tasks often lack verifiable answers. The paper *Dedicated Feedback and Edit Models Empower Inference-Time Scaling* addresses this by proposing a specialized architecture that decouples the generator, feedback, and edit models [[47]](https://arxiv.org/html/2503.04378v1), [[48]](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended).

Each model in this system is optimized for its specific role. The feedback and edit models are trained on large, human-annotated datasets of responses, critiques, and revisions, allowing them to produce higher-quality signals than a single, general-purpose model could. This dedicated architecture enables an iterative refinement process during inference that surpasses the performance of generic self-critique loops, making it a powerful tool for improving the quality of open-ended generation.![Image 22: The system architecture of the dedicated feedback and edit models.](https://substackcdn.com/image/fetch/$s_!zA8v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73568387-83fb-4744-bd3d-f5cbcfe53f1d_1136x716.png)

Image 22: The system architecture of the dedicated feedback and edit models. (Source [arxiv.org [[59]](https://arxiv.org/abs/2503.04378)])

## Conclusion

Inference-time compute scaling is shaping up to be a major research direction in 2025, largely because it offers a way to enhance existing models without the need for permanent weight modifications. This article has surveyed a wide range of techniques, from simple "wait" tokens and budget forcing to sophisticated methods involving search, optimization loops, dynamic routing, and even latent-space iteration. A recurring theme across these studies is the remarkable finding that smaller models, when equipped with proper inference-time scaling, can rival or even exceed the performance of much larger models that lack such capabilities.

This has profound implications for AI engineers, as it directly impacts the trade-offs between model size, training costs, latency, and accuracy in production systems. Instead of defaulting to the largest available model, we can now consider using smaller, more efficient models and strategically allocating additional compute at inference time to achieve the desired performance. This is leading to an emerging industry trend of "thinking-on-demand" toggles, which allow developers or even end-users to dial inference compute up or down depending on the difficulty of the task.![Image 23: Inference-time scaling allows for a flexible trade-off between performance and compute.](https://substackcdn.com/image/fetch/$s_!nhEn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1f749e4-4167-4013-b1c9-651c83bf8d3b_1504x756.png)

Image 23: Inference-time scaling allows for a flexible trade-off between performance and compute. (Source [arxiv.org [[59]](https://arxiv.org/abs/2503.04378)])

However, it is important to acknowledge the caveats. Increased inference compute comes with higher costs and can negatively impact latency, which is a critical factor for user experience. Furthermore, as we have seen, there is no universally best technique that works across all tasks. The optimal approach often depends on the specific domain, the complexity of the problem, and the capabilities of the base model. This means that as AI engineers, we must be prepared to experiment and adapt our strategies to fit the needs of our applications.

Looking ahead, we can predict that explicit reasoning will become the default rather than an optional feature in future agentic systems. The ability to "think" longer and more deeply will be a fundamental requirement for building reliable and capable AI. In our next article, we will shift our focus to train-time compute scaling methods, exploring advanced reinforcement learning, hybrid RL plus SFT approaches, and distillation techniques in depth.

## References

- [1] medium.com. (n.d.). [https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8)
- [2] huggingface.co. (n.d.). [https://huggingface.co/papers/2501.19393](https://huggingface.co/papers/2501.19393)
- [3] icml.cc. (n.d.). [https://icml.cc/virtual/2025/poster/46149](https://icml.cc/virtual/2025/poster/46149)
- [4] proceedings.mlr.press. (n.d.). [https://proceedings.mlr.press/v267/li25ac.html](https://proceedings.mlr.press/v267/li25ac.html)
- [5] linkedin.com. (n.d.). [https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme)
- [6] tldr.takara.ai. (n.d.). [https://tldr.takara.ai/p/2501.18585](https://tldr.takara.ai/p/2501.18585)
- [7] cdn.openai.com. (n.d.). [https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf)
- [8] openai.com. (n.d.). [https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness)
- [9] huggingface.co. (n.d.). [https://huggingface.co/papers/2501.18841](https://huggingface.co/papers/2501.18841)
- [10] aclanthology.org. (n.d.). [https://aclanthology.org/2025.acl-long.1369.pdf](https://aclanthology.org/2025.acl-long.1369.pdf)
- [11] arxiv.org. (n.d.). [https://arxiv.org/pdf/2502.13842](https://arxiv.org/pdf/2502.13842)
- [12] aclanthology.org. (n.d.). [https://aclanthology.org/2025.acl-long.1369.pdf](https://aclanthology.org/2025.acl-long.1369.pdf)
- [13] arxiv.org. (n.d.). [https://arxiv.org/pdf/2502.13842](https://arxiv.org/pdf/2502.13842)
- [14] arxiv.org. (n.d.). [https://arxiv.org/html/2502.13842v1](https://arxiv.org/html/2502.13842v1)
- [15] emergentmind.com. (n.d.). [https://www.emergentmind.com/topics/inner-thinking-transformer-itt](https://www.emergentmind.com/topics/inner-thinking-transformer-itt)
- [16] magazine.sebastianraschka.com. (n.d.). [https://magazine.sebastianraschka.com/p/understanding-reasoning-llms](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)
- [17] arxiv.org. (n.d.). [https://arxiv.org/html/2502.02390v3](https://arxiv.org/html/2502.02390v3)
- [18] arxiv.org. (n.d.). [https://arxiv.org/html/2502.04404v1](https://arxiv.org/html/2502.04404v1)
- [19] ojs.aaai.org. (n.d.). [https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947)
- [20] huggingface.co. (n.d.). [https://huggingface.co/papers/2502.05171](https://huggingface.co/papers/2502.05171)
- [21] arxiv.org. (n.d.). [https://arxiv.org/html/2502.02390v3](https://arxiv.org/html/2502.02390v3)
- [22] arxiv.org. (n.d.). [https://arxiv.org/html/2502.04404v1](https://arxiv.org/html/2502.04404v1)
- [23] ojs.aaai.org. (n.d.). [https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947)
- [24] huggingface.co. (n.d.). [https://huggingface.co/papers/2502.05171](https://huggingface.co/papers/2502.05171)
- [25] openreview.net. (n.d.). [https://openreview.net/forum?id=S3GhJooWIC](https://openreview.net/forum?id=S3GhJooWIC)
- [26] neurips.cc. (n.d.). [https://neurips.cc/virtual/2025/poster/117966](https://neurips.cc/virtual/2025/poster/117966)
- [27] icml.cc. (n.d.). [https://icml.cc/virtual/2025/51856](https://icml.cc/virtual/2025/51856)
- [28] medium.com. (n.d.). [https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db)
- [29] github.com. (n.d.). [https://github.com/usail-hkust/benchmark_inference_time_computation_LLM](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [30] github.com. (n.d.). [https://github.com/usail-hkust/benchmark_inference_time_computation_LLM](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [31] github.com. (n.d.). [https://github.com/usail-hkust/benchmark_inference_time_computation_LLM](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [32] tianpan.co. (n.d.). [https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more)
- [33] aclanthology.org. (n.d.). [https://aclanthology.org/2025.emnlp-main.165.pdf](https://aclanthology.org/2025.emnlp-main.165.pdf)
- [34] aussieai.com. (n.d.). [https://www.aussieai.com/research/cot-optimization](https://www.aussieai.com/research/cot-optimization)
- [35] arxiv.org. (n.d.). [https://arxiv.org/html/2406.09136v1](https://arxiv.org/html/2406.09136v1)
- [36] gail.wharton.upenn.edu. (n.d.). [https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought)
- [37] openreview.net. (n.d.). [https://openreview.net/forum?id=l19DmXbwPK](https://openreview.net/forum?id=l19DmXbwPK)
- [38] icml.cc. (n.d.). [https://icml.cc/virtual/2025/oral/47195](https://icml.cc/virtual/2025/oral/47195)
- [39] arxiv.org. (n.d.). [https://arxiv.org/html/2512.15146v1](https://arxiv.org/html/2512.15146v1)
- [40] cdn.openai.com. (n.d.). [https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf)
- [41] cameronrwolfe.substack.com. (n.d.). [https://cameronrwolfe.substack.com/p/reward-models](https://cameronrwolfe.substack.com/p/reward-models)
- [42] helicone.ai. (n.d.). [https://www.helicone.ai/blog/chain-of-draft](https://www.helicone.ai/blog/chain-of-draft)
- [43] analyticsvidhya.com. (n.d.). [https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft)
- [44] medium.com. (n.d.). [https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169)
- [45] aws.amazon.com. (n.d.). [https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock)
- [46] arxiv.org. (n.d.). [https://arxiv.org/html/2502.18600v1](https://arxiv.org/html/2502.18600v1)
- [47] arxiv.org. (n.d.). [https://arxiv.org/html/2503.04378v1](https://arxiv.org/html/2503.04378v1)
- [48] liner.com. (n.d.). [https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended)
- [49] arxiv.org. (n.d.). [https://arxiv.org/abs/2502.14382](https://arxiv.org/abs/2502.14382)
- [50] arxiv.org. (n.d.). [https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)
- [51] arxiv.org. (n.d.). [https://arxiv.org/abs/2501.12895](https://arxiv.org/abs/2501.12895)
- [52] arxiv.org. (n.d.). [https://arxiv.org/abs/2501.18585](https://arxiv.org/abs/2501.18585)
- [53] arxiv.org. (n.d.). [https://arxiv.org/abs/2501.18841](https://arxiv.org/abs/2501.18841)
- [54] arxiv.org. (n.d.). [https://arxiv.org/html/2502.04404v1](https://arxiv.org/html/2502.04404v1)
- [55] arxiv.org. (n.d.). [https://arxiv.org/abs/2502.05171](https://arxiv.org/abs/2502.05171)
- [56] arxiv.org. (n.d.). [https://arxiv.org/abs/2502.06703](https://arxiv.org/abs/2502.06703)
- [57] www.arxiv.org. (n.d.). [https://www.arxiv.org/abs/2502.12521](https://www.arxiv.org/abs/2502.12521)
- [58] arxiv.org. (n.d.). [https://arxiv.org/abs/2502.13842](https://arxiv.org/abs/2502.13842)
- [59] arxiv.org. (n.d.). [https://arxiv.org/abs/2503.04378](https://arxiv.org/abs/2503.04378)
- [60] ve3.global. (n.d.). [https://ve3.global/blog/inference-time-scaling-the-next-frontier-in-ai-performance](https://ve3.global/blog/inference-time-scaling-the-next-frontier-in-ai-performance)
- [61] arxiv.org. (n.d.). [https://arxiv.org/abs/2501.19393](https://arxiv.org/abs/2501.19393)
- [62] arxiv.org. (n.d.). [https://arxiv.org/html/2507.15974v1](https://arxiv.org/html/2507.15974v1)
- [63] lesswrong.com. (n.d.). [https://www.lesswrong.com/posts/pLnLSgWphqDbdorgi/on-recent-results-in-llm-latent-reasoning](https://www.lesswrong.com/posts/pLnLSgWphqDbdorgi/on-recent-results-in-llm-latent-reasoning)
- [64] arxiv.org. (n.d.). [https://arxiv.org/html/2605.26733v1](https://arxiv.org/html/2605.26733v1)
- [65] liner.com. (n.d.). [https://liner.com/review/inner-thinking-transformer-leveraging-dynamic-depth-scaling-to-foster-adaptive](https://liner.com/review/inner-thinking-transformer-leveraging-dynamic-depth-scaling-to-foster-adaptive)