# The 2025 AI Engineer’s Guide to LLM Reasoning

In 2025, building agentic systems that can solve complex, multi-step problems is a top priority. Direct-answer models often fail at tasks requiring deep reasoning, sparking a research surge to make LLMs “think” more effectively. Since the release of models like DeepSeek-R1, we have seen an explosion of techniques blending inference-time scaling, reinforcement learning (RL), and supervised fine-tuning (SFT). This article focuses on one critical branch: inference-time compute scaling, which enhances an LLM's reasoning at the moment of inference without altering its weights. We will survey 14 recent papers showcasing diverse methods for scaling this test-time computation, from simple token controls to dynamic, latent-space strategies. To understand how these techniques fit into the broader landscape, we will first examine the four main categories of reasoning model development.![The four main categories of implementing reasoning models I explained in Understanding Reasoning LLMs. This article focuses on inference-time-scaling methods.](https://substackcdn.com/image/fetch/$s_!IOSP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf9e2677-652a-4af1-9f57-dc0c253d2198_1448x1260.png)

Image 1: The four main categories of implementing reasoning models. This article focuses on inference-time-scaling methods. (Source [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

## Implementing and improving reasoning in LLMs: The four main categories

Reasoning models are LLMs designed to generate an explicit or internal thought process before producing a final answer [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms). This contrasts with direct-answer models, which map an input directly to an output in a single forward pass. The intermediate steps, whether visible to the user or not, allow the model to break down complex problems, verify its logic, and correct mistakes along the way.![Side-by-side comparison of a basic LLM's one-line answer and a reasoning LLM's explanatory response.](https://substackcdn.com/image/fetch/$s_!ZsN9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8abbfe39-f656-4845-b376-18c1e563210a_1326x564.png)

Image 2: A regular LLM may only provide a short answer, whereas reasoning models typically include intermediate steps that reveal the thought process. (Source [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

There are two primary ways to enhance an LLM's reasoning capabilities: increasing training compute or increasing inference compute. Training compute involves modifying the model's weights through methods like RL or SFT. This is like studying for an exam; you are permanently encoding knowledge into the model.

Inference compute, on the other hand, involves allocating extra FLOPs at test time without changing the model's weights. The simplest example is chain-of-thought (CoT) prompting, where you ask the model to "think step by step." This encourages it to generate a longer, more detailed response, effectively using more computation to arrive at the answer. This is like taking extra time to solve a problem during the exam itself.![Accuracy improvements can be achieved through increased training or test-time compute, where test-time compute is synonymous with inference-time compute and inference-time scaling.](https://substackcdn.com/image/fetch/$s_!pgyl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddde6f39-3b88-4962-9d02-2cf767dc82e9_1484x994.png)

Image 3: Accuracy improvements can be achieved through increased training or test-time compute. Test-time compute is synonymous with inference-time compute and scaling. (Source [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382) [[65]](https://arxiv.org/abs/2502.14382))

In practice, most state-of-the-art systems combine both. Heavy train-time preparation equips the model with strong foundational reasoning skills, while test-time thinking allows it to apply those skills to specific, complex problems. Relying on training alone can lead to issues like reward hacking, where the model learns to exploit the reward function without genuinely improving its reasoning. Conversely, pure inference scaling on a weak base model often yields limited gains.

The development of reasoning models generally falls into four main categories, as outlined by Sebastian Raschka [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).![Four categories of reasoning models development](https://substackcdn.com/image/fetch/$s_!_2dU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5e5fdf9-e72c-497b-9cf4-b4e3c24f33f1_1600x591.png)

Image 4: The four main categories for developing reasoning models. (Source [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms) [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

### Inference-time compute scaling

This category focuses on improving reasoning capabilities without modifying the underlying model. The core idea is to increase computational resources during inference to enhance output quality. While models like OpenAI's o1 are suspected to use this technique, the DeepSeek R1 technical report noted that their explicit attempts at inference-time methods like Process Reward Model-based search and MCTS were largely unsuccessful. However, their model does exhibit an implicit form of inference scaling by generating longer, more detailed responses, which naturally increases inference costs and can be seen as a form of inference-time scaling [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms). This approach is a no-brainer for improving already strong models but becomes expensive at scale as user volume grows.

### Pure reinforcement learning

This approach demonstrates that reasoning can emerge as a learned behavior without the need for supervised fine-tuning. The DeepSeek-R1-Zero model, for example, was trained exclusively with RL on top of a pre-trained base model. This "cold start" approach, which skipped the SFT stage, was sufficient for the model to develop basic reasoning skills, including generating intermediate "thinking" steps and even exhibiting an "Aha!" moment where it began to self-verify its answers. While interesting for research, pure RL is generally less effective in practice than combining it with SFT, as it can be challenging to implement and may not be as effective for smaller models [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

### Reinforcement learning and supervised fine-tuning

This hybrid approach is used to build high-performance reasoning models like DeepSeek-R1 and likely OpenAI's o1. It combines an SFT stage, which provides the model with high-quality reasoning examples, with an RL stage that further refines its problem-solving abilities. The SFT data often includes CoT examples, and the RL stage may use a combination of verifiable rewards (for math and coding) and human preference-based rewards. This combination is currently the key approach for building state-of-the-art reasoning models, as it leverages the strengths of both supervised learning and reinforcement learning to produce robust and capable systems [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

### Supervised fine-tuning and model distillation

This is an effective strategy for creating smaller, more efficient reasoning models. In this context, distillation refers to instruction fine-tuning a smaller LLM on an SFT dataset generated by a larger, more powerful model. For example, the DeepSeek team fine-tuned smaller Qwen and Llama models on outputs from their 671B DeepSeek-R1 model. While this approach does not drive innovation in the same way as developing a new state-of-the-art model, it is a cost-effective way to transfer reasoning capabilities to smaller models, making them more accessible for research and practical applications [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

With these four categories mapped out, we can now zoom in on the inference-time compute scaling branch, which forms the core of this article.

## Inference-time compute scaling methods

The central idea behind inference-time compute scaling is that allowing an LLM to "think longer" can lead to better answers, much like how humans benefit from spending more time on difficult problems. This is achieved by allocating additional computational resources at the moment of inference to improve the quality of the output [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

This idea has historical parallels in game AI like AlphaGo, which used extensive search at inference time to evaluate possible moves—a step critical to its superhuman performance [[72]](https://ve3.global/blog/inference-time-scaling-the-next-frontier-in-ai-performance). The concept also echoes ensemble methods in classic machine learning, which trade more compute for better results by combining multiple models [[73]](https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling).

The most classic approach is through prompt engineering. CoT prompting, which encourages the model to generate intermediate reasoning steps, is a form of inference-time scaling because it increases the number of output tokens, leading to higher latency and cost [[32]](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more), [[33]](https://aclanthology.org/2025.emnlp-main.165.pdf), [[34]](https://www.aussieai.com/research/cot-optimization), [[35]](https://arxiv.org/html/2406.09136v1), [[36]](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought). While this can improve accuracy on complex problems, it is often inefficient for simpler tasks.![An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper](https://substackcdn.com/image/fetch/$s_!Knds!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d37faa4-3261-492c-85a4-766926b8c17c_1600x419.png)

Image 5: An example of classic CoT prompting. (Source [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916) [[71]](https://arxiv.org/abs/2205.11916))

More advanced techniques involve search and voting strategies. Majority voting, for instance, generates multiple answers and selects the one that appears most frequently. Beam search and other algorithms explore different reasoning paths and use a Process Reward Model (PRM) to select the most promising one. PRMs evaluate each step of the reasoning process, providing more granular feedback than models that only score the final outcome [[37]](https://openreview.net/forum?id=l19DmXbwPK), [[38]](https://icml.cc/virtual/2025/oral/47195), [[39]](https://arxiv.org/html/2512.15146v1), [[40]](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf), [[41]](https://cameronrwolfe.substack.com/p/reward-models).![Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper](https://substackcdn.com/image/fetch/$s_!O9a-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ad9742b-993f-4ecd-8f80-2fa41d43164b_1334x798.png)

Image 6: Different search-based methods use a process-reward-based model to select the best answer. (Source [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314) [[69]](https://arxiv.org/abs/2408.03314))

These methods represent a shift from static prompting to dynamic, compute-intensive strategies that actively guide the model's reasoning process. The *s1* paper, which we will examine next, provides a concrete example of these ideas, combining curated reasoning traces with explicit length-control tokens to regulate test-time compute.

## s1: Simple test-time scaling

The paper "[s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393)" (January 31, 2025) introduces a hybrid approach that combines a small, carefully curated 1k-example SFT dataset with an inference-time length control mechanism [[1]](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8), [[2]](https://huggingface.co/papers/2501.19393). This distinguishes it from pure distillation methods, as it actively manages the model's "thinking" process at runtime.![Illustration of "wait" token insertion to control the length of the output. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/$s_!qk_K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e7f4d94-9f8f-4353-87ad-78f3cba7b9cd_1154x854.png)

Image 7: Illustration of "wait" token insertion to control the length of the output. (Source [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382) [[65]](https://arxiv.org/abs/2502.14382))

The core mechanism is "budget forcing," a sequential scaling technique that controls the length of the model's reasoning trace. If the model tries to stop thinking too early, the system suppresses the end-of-thinking signal and appends a "Wait" token. This simple intervention encourages the model to continue its analysis, often leading to self-correction and improved accuracy [[1]](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8). This is in contrast to parallel methods like majority voting, which generate multiple independent responses. Budget forcing directly manipulates the length and depth of a single reasoning path.

The paper reports a clear correlation between the length of the generated response and the accuracy of the final answer on reasoning benchmarks. As the model is forced to "think" longer, its performance tends to improve, up to a certain point. This aligns with the "Aha moment" observed in the DeepSeek-R1 training, where the model spontaneously began to use words like "wait" during self-reflection [[68]](https://arxiv.org/abs/2501.12948).![Correlation between response accuracy and length. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7f0c49b-a644-4142-bed0-7d114ecd39c2_798x456.png)

Image 8: Correlation between response accuracy and length. (Source [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393) [[67]](https://arxiv.org/abs/2501.19393))

Interestingly, the choice of token matters. An empirical comparison showed that appending "Wait" led to better accuracy than a more neutral phrase like "Hmm," suggesting that the "Wait" token specifically triggers a process of doubt and re-evaluation rather than just extending the generation time [[2]](https://huggingface.co/papers/2501.19393).!["Wait" vs "Hmm" tokens. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bdfe7db-8c97-4240-8be0-11efa7abdf7c_758x510.png)

Image 9: "Wait" vs "Hmm" tokens. (Source [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382) [[65]](https://arxiv.org/abs/2502.14382))

However, the paper also acknowledges its limitations. The authors call for future work to compare budget forcing against other sequential methods like beam search, lookahead search, and compute-optimal search, as well as to establish a stronger baseline against standard CoT prompting [[67]](https://arxiv.org/abs/2501.19393). This highlights that while simple, budget forcing is just one of many potential strategies for controlling test-time compute, and its relative effectiveness is still an open question. The paper also notes that suppressing the end-of-thinking token too often can trap the model in repetitive loops, indicating a clear upper bound to the benefits of this specific technique.

## Other noteworthy research papers on inference-time compute scaling

The high volume of recent papers on this topic makes it impractical to cover each one in exhaustive detail. Instead, we will provide brief summaries of several noteworthy contributions, allowing you to see the breadth of the research landscape without getting bogged down in repetitive explanations.

A common pattern you will notice is that many of these papers blend some form of training with explicit control of inference-time compute. This is different from pure distillation or SFT approaches that simply train a model to produce longer outputs. The methods we will discuss involve active regulation of the model's compute budget or reasoning process during inference. This regulated approach allows for more dynamic and context-aware allocation of computational resources, moving beyond the static nature of traditional SFT.

## Test-Time Preference Optimization

"[Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://arxiv.org/abs/2501.12895)" introduces an iterative alignment process that occurs entirely at inference time, avoiding any changes to the underlying model weights [[3]](https://icml.cc/virtual/2025/poster/46149), [[4]](https://proceedings.mlr.press/v267/li25ac.html). This positions it as a pure inference-time method.

The framework operates in a four-step loop. First, it generates multiple responses to a given query. Second, a reward model scores these responses, selecting the best ("chosen") and worst ("rejected") ones. Third, the system generates textual critiques and suggestions based on this comparison. Finally, these critiques are used to guide the model in refining its output in the next iteration. This process repeats, progressively improving the quality of the generated responses on a per-query basis [[3]](https://icml.cc/virtual/2025/poster/46149).![Test-Time Preference Optimization process. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!dmJN!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2a1bd16-7cf7-4898-8dce-a2d8352f76a8_1600x819.png)

Image 10: The Test-Time Preference Optimization process. (Source [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://arxiv.org/abs/2501.12895) [[70]](https://arxiv.org/abs/2501.12895))

## Thoughts Are All Over the Place

The paper "[Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://arxiv.org/abs/2501.18585)" identifies a phenomenon called "underthinking" in o1-like models, where frequent switching between reasoning paths can actually reduce the accuracy of the final answer [[5]](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme), [[6]](https://tldr.takara.ai/p/2501.18585).

To address this, the authors propose the Thought Switching Penalty (TIP) method. This technique modifies the model's logits at inference time to discourage premature transitions between different lines of thought, all without any fine-tuning. By penalizing tokens associated with thought switching, TIP encourages the model to explore each promising reasoning path more deeply. The paper reports that this no-fine-tuning approach improves accuracy on challenging benchmarks by forcing the model to engage in more thorough and focused reasoning [[5]](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme).![Thought Switching Penalty method visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!vvCX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7111ccaa-c4c1-4c7c-84f9-74d38df3c663_1528x894.png)

Image 11: Visualization of the Thought Switching Penalty method. (Source [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382) [[65]](https://arxiv.org/abs/2502.14382))

## Trading Inference-Time Compute for Adversarial Robustness

The paper "[Trading Inference-Time Compute for Adversarial Robustness](https://arxiv.org/abs/2501.18841)" explores the relationship between inference-time compute and model safety. It finds that increasing computation at inference time generally reduces the success rate of adversarial attacks, even without specific adversarial training [[7]](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf), [[8]](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness), [[9]](https://huggingface.co/papers/2501.18841). The paper's empirical trade-off curves show a clear trend: as the model "thinks" longer, it becomes more resilient.

However, the authors highlight exceptions where gains are limited, especially in scenarios involving policy ambiguity or loophole exploitation [[8]](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness). The paper also introduces new attack strategies, such as "Think Less" and "Nerd Sniping," designed to counteract these robustness gains. The conclusion is that while inference scaling is a valuable tool for improving LLM safety, it is not a complete solution on its own [[7]](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf). This assumes the model's reasoning steps are hidden; if exposed, an "inverse scaling law" can emerge where more compute *decreases* robustness by expanding the attack surface [[74]](https://arxiv.org/html/2507.15974v1).![Trading Inference-Time Compute for Adversarial Robustness analysis. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!Gt2_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F704acd82-10a8-4879-9bd3-26bb67c3155f_1600x1173.png)

Image 12: Analysis of trading inference-time compute for adversarial robustness. (Source [TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS.](https://arxiv.org/abs/2501.18841) [[61]](https://arxiv.org/abs/2501.18841))

## Chain-of-Associated-Thoughts

The paper "[CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning](https://arxiv.org/abs/2502.02390)" proposes a framework that combines Monte Carlo Tree Search (MCTS) with an "associative memory" that functions as a dynamic knowledge base during inference [[21]](https://arxiv.org/html/2502.02390v3).

This associative memory allows the model to recall earlier reasoning paths and incorporate newly generated information without losing context. The MCTS component, in turn, provides a structured way to explore different reasoning pathways. The synergy between these two elements enables a more systematic and context-aware exploration of the solution space at test time, leading to more accurate and comprehensive outputs [[21]](https://arxiv.org/html/2502.02390v3).![CoAT: Chain-of-Associated-Thoughts Framework visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!AtpC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d0635fb-c0b4-45df-b8d3-b54254ab92b5_1600x777.png)

Image 13: CoAT: Chain-of-Associated-Thoughts Framework visualization. (Source [CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning](https://arxiv.org/abs/2502.02390) [[21]](https://arxiv.org/html/2502.02390v3))

## Step Back to Leap Forward

"[Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://arxiv.org/abs/2502.04404)" introduces a self-backtracking mechanism that teaches models to recognize and correct their own suboptimal reasoning paths [[22]](https://arxiv.org/html/2502.04404v1), [[23]](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947).

The key innovation is the use of a special "backtrack" token. During the training phase, the model learns to generate this token when it identifies a point in its reasoning where it has gone astray. At inference time, the model leverages this learned ability to perform a tree-based search. When the backtrack token is generated, the model revisits its previous steps and explores alternative paths.

A significant advantage of this approach is that it does not require an external reward model, unlike standard process-reward-guided search methods. The model learns to evaluate its own reasoning paths and decide when to backtrack, making it a more self-contained and efficient system. This allows the model to dynamically adjust its search depth and breadth, leading to more robust and flexible reasoning [[22]](https://arxiv.org/html/2502.04404v1).![Step Back to Leap Forward: Self-Backtracking mechanism. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!e6x3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1df5fbf3-97f2-4976-b46f-2d5196b6bdc4_1594x888.png)

Image 14: Step Back to Leap Forward: Self-Backtracking mechanism. (Source [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://arxiv.org/abs/2502.04404) [[22]](https://arxiv.org/html/2502.04404v1))

## Scaling up Test-Time Compute with Latent Reasoning

The paper "[Scaling Test-Time Compute: How Recurrent Depth Transforms AI Reasoning](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db)" explores a different approach to scaling test-time compute: iterating in latent space rather than generating more output tokens [[24]](https://huggingface.co/papers/2502.05171), [[25]](https://openreview.net/forum?id=S3GhJooWIC), [[26]](https://neurips.cc/virtual/2025/poster/117966), [[27]](https://icml.cc/virtual/2025/51856), [[28]](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db).

This technique, known as recurrent depth, allows the model to perform multiple rounds of internal computation on the same input, refining its understanding before producing an output. This is similar to the behavior of Recurrent Neural Networks (RNNs), where the hidden state is updated iteratively. The process converges when the hidden state reaches a stable fixed point, often controlled at inference time by a KL-divergence threshold [[75]](https://www.lesswrong.com/posts/pLnLSgWphqDbdorgi/on-recent-results-in-llm-latent-reasoning), [[76]](https://arxiv.org/html/2605.26733v1). The main advantage is that the model can "think" for as long as needed without increasing the length of the visible output. However, this comes with a major drawback: the absence of explicit reasoning steps makes it difficult for humans to interpret or debug the model's thought process [[24]](https://huggingface.co/papers/2502.05171).![Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!kVPW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb82da925-5736-44ba-bed1-ea3207b06382_1516x602.png)

Image 15: Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach visualization. (Source [Scaling by Thinking in Continuous Space](https://arxiv.org/abs/2502.05171) [[62]](https://arxiv.org/abs/2502.05171))

## Can a 1B LLM Surpass a 405B LLM?

The paper "[Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling](https://arxiv.org/abs/2502.06703)" conducts a systematic study of the interactions between inference-time scaling, PRMs, and problem difficulty. The authors propose a "compute-optimal" scaling strategy that adapts the inference budget based on the choice of PRM, the size of the policy model, and the complexity of the task at hand.

The most striking finding is that a 1B model, when paired with the right scaling strategy, can outperform an unscaled 405B Llama 3 model on the same benchmarks. This provides strong evidence that a well-allocated inference budget can allow smaller, more efficient models to surpass much larger ones. This has direct implications for AI engineers, as it highlights the importance of making informed trade-off decisions between model size, cost, and performance. The paper underscores that the right inference budget is a powerful lever for performance, enabling smaller models to punch far above their weight class [[63]](https://arxiv.org/abs/2502.06703).![Can 1B LLM Surpass 405B LLM? Compute-optimal scaling comparison. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!DiM2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c471e7f-36e7-41a8-a7e0-80bebf3c0f36_1600x1046.png)

Image 16: Compute-optimal scaling comparison. (Source [Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling](https://arxiv.org/abs/2502.06703) [[63]](https://arxiv.org/abs/2502.06703))

## Inference-Time Computations for LLM Reasoning and Planning

The paper "[Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521)" introduces Sys2Bench, a comprehensive benchmark for evaluating inference-time techniques across eleven diverse tasks [[29]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM), [[30]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM), [[31]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM). The benchmark covers arithmetic, logical, commonsense, and algorithmic reasoning, as well as planning domains.

The authors evaluate a range of techniques, including CoT, Tree-of-Thought, and Reasoning as Planning. The key insight from their extensive experiments is that no single inference-time technique dominates across all task types. This forces engineers to match the right method to the specific domain they are working in. The paper also provides a valuable analysis of the trade-offs between computational cost and performance, helping practitioners make more informed decisions when choosing an inference-time strategy [[64]](https://www.arxiv.org/abs/2502.12521).![Inference-Time Computations for LLM Reasoning and Planning benchmark results. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!Vm7j!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42115dab-1086-4035-9a64-65a83631377e_1600x1023.png)

Image 17: Benchmark results for inference-time computations. (Source [Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521) [[64]](https://www.arxiv.org/abs/2502.12521))

## Learning to Reason from Feedback at Test-Time

The method presented in "[Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521)" is challenging to classify as either a pure inference-time or training-time technique because it updates the model's weights during inference.

The paper introduces the OpTune optimizer, which adjusts the model's weights based on previous mistakes without storing the failed attempts in the prompt context. This is in contrast to sequential revision methods, which grow the context with each attempt, and parallel sampling approaches, which generate multiple independent responses.

The main benefit of this approach is that the model can "remember" its errors through lightweight weight updates, rather than relying on an ever-expanding context window. This makes it a more scalable solution for long, iterative reasoning tasks. However, the need to perform weight updates at inference time adds a layer of complexity that is not present in pure inference-time methods.![Learning to Reason from Feedback at Test-Time: OpTune optimizer visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!nJMD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1925302-7fc2-4c7b-91e9-1c0fc4f0609e_1426x652.png)

Image 18: Visualization of the OpTune optimizer. (Source [Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521) [[64]](https://www.arxiv.org/abs/2502.12521))

## Inner Thinking Transformer

The "[Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://arxiv.org/abs/2502.13842)" introduces the concept of dynamic depth scaling, which avoids using a fixed number of transformer layers for every token [[12]](https://aclanthology.org/2025.acl-long.1369.pdf), [[13]](https://arxiv.org/pdf/2502.13842), [[14]](https://arxiv.org/html/2502.13842v1), [[15]](https://www.emergentmind.com/topics/inner-thinking-transformer-itt).

The core mechanism is Adaptive Token Routing (ATR), which identifies "difficult" tokens and sends them through the same layer multiple times. This selectively increases the inference compute budget for the tokens that need it most. The main advantage is that the model can allocate extra "thinking" effort exactly where it is required, without lengthening the overall output sequence. This allows for a more efficient and targeted use of computational resources [[12]](https://aclanthology.org/2025.acl-long.1369.pdf).

This efficiency translates to measurable performance gains. For example, a 162M parameter ITT model with four thinking steps outperformed a standard Transformer of the same size, achieving a 1.7% accuracy improvement where a comparable "Loop" variant only gained 0.3% [[77]](https://liner.com/review/inner-thinking-transformer-leveraging-dynamic-depth-scaling-to-foster-adaptive).![Inner Thinking Transformer: Adaptive Token Routing mechanism. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!-oC7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a6eb47e-fcbe-4c71-8d45-e7d82ae14ba1_1414x1090.png)

Image 19: Inner Thinking Transformer: Adaptive Token Routing mechanism. (Source [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://arxiv.org/abs/2502.13842) [[14]](https://arxiv.org/html/2502.13842v1))

## Test Time Scaling for Code Generation

The paper "[S\*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382)" proposes the S\* method, a technique specialized for code generation that combines parallel generation of candidate solutions with sequential iterative debugging [[65]](https://arxiv.org/abs/2502.14382).![S*: Test Time Scaling for Code Generation overview. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!quMS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94a88f17-b4b1-4642-aeb1-6db29071ef91_972x752.png)

Image 20: S*: Test Time Scaling for Code Generation overview. (Source [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382) [[65]](https://arxiv.org/abs/2502.14382))

The framework operates in a two-stage process. The first stage, generation, involves using execution feedback from public test cases to guide the model. The model generates N initial samples in parallel and then refines each one through up to R rounds of sequential revision. This iterative debugging process continues until a sample passes all public tests or the maximum number of attempts is reached.

The second stage focuses on the adaptive selection and repair of the generated candidates. A key technique in this stage is "adaptive input synthesis," where the model creates discriminating test cases specifically designed to distinguish between solutions that pass the initial public tests. For each pair of passing solutions, an LLM generates a new test input. By executing both solutions on this new input and comparing the outputs, the system can more reliably identify the correct one. By leveraging execution results and error messages, S\* can iteratively repair and refine its solutions, leading to more robust and accurate code generation. This approach connects back to earlier Google research on optimal test-time compute scaling, applying similar principles to the domain of code [[65]](https://arxiv.org/abs/2502.14382).

## Chain of Draft

The paper "[Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/abs/2502.18600)" makes a simple but powerful observation: humans often use concise drafts or shorthand notes rather than verbose, step-by-step explanations when solving problems internally [[42]](https://www.helicone.ai/blog/chain-of-draft), [[43]](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft), [[44]](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169), [[45]](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock), [[46]](https://arxiv.org/html/2502.18600v1).

Based on this insight, the authors propose Chain of Draft (CoD) prompting. This technique encourages the model to generate minimal yet informative intermediate steps, such as equations or key terms, instead of full natural-language reasoning. The results are impressive: CoD drastically reduces the token count, leading to significant efficiency gains in terms of both cost and latency, while maintaining an accuracy comparable to that of full CoT on various reasoning benchmarks.![Chain of Draft: Thinking Faster by Writing Less comparison. Annotated figures from the paper](https://substackcdn.com/image/fetch/$s_!Gaj6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869a967-9498-435f-85f2-a38557db14e3_1460x982.png)

Image 21: Comparison of Chain of Draft with other methods. (Source [Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/abs/2502.18600) [[46]](https://arxiv.org/html/2502.18600v1))

This approach does come with a trade-off. The loss of human-readable reasoning traces can make it more difficult to debug or interpret the model's thought process. However, for applications where efficiency is paramount and full interpretability is not a strict requirement, CoD offers a compelling alternative to traditional CoT prompting [[46]](https://arxiv.org/html/2502.18600v1).

## Better Feedback and Edit Models

Applying inference scaling to open-ended tasks like creative writing or high-level planning is challenging because there are no easily verifiable answers. The paper "[Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/abs/2503.04378)" addresses this by proposing a specialized architecture that decouples the generation, feedback, and editing processes [[47]](https://arxiv.org/html/2503.04378v1), [[48]](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended).

The system consists of three distinct models: a generator, a feedback model, and an edit model. Each is optimized for its specific role. The feedback and edit models are trained on large, human-annotated datasets of responses, critiques, and revisions. This allows them to produce higher-quality signals than a single, all-purpose model could generate through a generic self-critique loop. During inference, these dedicated models enable an iterative refinement process that has been shown to surpass the performance of standard self-correction methods on open-ended tasks [[47]](https://arxiv.org/html/2503.04378v1).![Dedicated Feedback and Edit Models for Inference-Time Scaling system architecture](https://substackcdn.com/image/fetch/$s_!zA8v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73568387-83fb-4744-bd3d-f5cbcfe53f1d_1136x716.png)

Image 22: Dedicated Feedback and Edit Models for Inference-Time Scaling system architecture. (Source [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/abs/2503.04378) [[47]](https://arxiv.org/html/2503.04378v1))

## Conclusion

Inference-time compute scaling has firmly established itself as a major research direction in 2025, primarily because it offers a way to enhance the reasoning capabilities of existing models without the need for permanent weight modifications. As we have seen, the techniques for achieving this are incredibly diverse, ranging from simple "Wait" tokens and budget forcing to sophisticated search algorithms, dynamic routing, and even latent-space iteration. This flexibility allows AI engineers to apply these methods to a wide range of models, from open-source to proprietary, without the high costs and complexities of retraining.

A recurring theme across these papers is the remarkable finding that smaller models, when equipped with proper inference-time scaling, can often rival or even exceed the performance of much larger models that lack such scaling. This has profound implications for AI engineers, as it directly impacts the trade-offs between model size, training costs, latency, and accuracy. For example, the ability to achieve state-of-the-art performance with a smaller, more efficient model can be a game-changer for production systems where cost and speed are critical. This shift in perspective encourages a move away from a "bigger is always better" mentality towards a more nuanced understanding of how to best allocate computational resources.

However, it is important to acknowledge the caveats. Increased inference-time compute almost always comes at the cost of higher latency, which can negatively impact the user experience. Furthermore, as the Sys2Bench paper demonstrated, there is no universally best technique that works across all tasks. The optimal approach often depends on the specific domain, the complexity of the problem, and the capabilities of the base model. More critically, the safety benefits of increased compute may rely on the assumption that the model's internal reasoning is hidden. Recent research shows that if these reasoning steps are exposed, an "inverse scaling law" can emerge where more thinking actually *decreases* robustness by creating a larger attack surface [[74]](https://arxiv.org/html/2507.15974v1).

To mitigate the performance costs, the hardware ecosystem is rapidly evolving. Specialized accelerators are being designed to handle these compute-intensive inference strategies more efficiently. These range from next-generation GPUs and optimized CPUs to experimental architectures like Processing-in-Memory (PIM) [[78]](https://gradientflow.substack.com/p/llm-inference-hardware-emerging-from), [[79]](https://community.juniper.net/blogs/sharada-yeluri/2024/02/20/llm-inference-hw-sw-optimizations). This trend toward LLM-hardware co-design will be critical for making advanced reasoning practical at scale.

Looking ahead, we are seeing an emerging industry trend toward "thinking-on-demand" toggles. These features allow developers or even end-users to dial the amount of inference compute up or down depending on the difficulty of the task. This dynamic allocation of resources represents a more intelligent and efficient way to leverage the power of reasoning models.![Feedback and Edit Models enable effective Inference-Time scaling across various dimensions.](https://substackcdn.com/image/fetch/$s_!nhEn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1f749e4-4167-4013-b1c9-651c83bf8d3b_1504x756.png)

Image 23: Feedback and Edit Models enable effective Inference-Time scaling across various dimensions. (Source [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/html/2503.04378v1) [[47]](https://arxiv.org/html/2503.04378v1))

As we move forward, it is becoming clear that explicit reasoning will likely become the default mode of operation for future agentic systems, rather than an optional feature. The ability to "think" before acting is fundamental to building robust, reliable, and truly intelligent AI.

In our next article, we will shift our focus to train-time compute scaling methods, exploring advanced reinforcement learning techniques, hybrid RL-SFT approaches, and distillation strategies in depth.

## References

- [1] [Paper review of s1: Simple test-time scaling](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8)
- [2] [s1: Simple test-time scaling](https://huggingface.co/papers/2501.19393)
- [3] [Test-Time Preference Optimization](https://icml.cc/virtual/2025/poster/46149)
- [4] [Test-Time Preference Optimization](https://proceedings.mlr.press/v267/li25ac.html)
- [5] [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme)
- [6] [Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs](https://tldr.takara.ai/p/2501.18585)
- [7] [Trading Inference-Time Compute for Adversarial Robustness](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf)
- [8] [Trading inference-time compute for adversarial robustness](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness)
- [9] [Trading Inference-Time Compute for Adversarial Robustness](https://huggingface.co/papers/2501.18841)
- [12] [Inner Thinking Transformer](https://aclanthology.org/2025.acl-long.1369.pdf)
- [13] [Inner Thinking Transformer](https://arxiv.org/pdf/2502.13842)
- [14] [Inner Thinking Transformer](https://arxiv.org/html/2502.13842v1)
- [15] [Inner Thinking Transformer (ITT)](https://www.emergentmind.com/topics/inner-thinking-transformer-itt)
- [16] [Understanding Reasoning LLMs](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)
- [21] [CoAT: Chain-of-Associated-Thoughts Framework for Enhancing Large Language Models Reasoning](https://arxiv.org/html/2502.02390v3)
- [22] [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://arxiv.org/html/2502.04404v1)
- [23] [Step Back to Leap Forward: Self-Backtracking for Boosting Reasoning of Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947)
- [24] [Scaling test-time computation by implicitly reasoning in latent space](https://huggingface.co/papers/2502.05171)
- [25] [Scaling test-time computation by implicitly reasoning in latent space](https://openreview.net/forum?id=S3GhJooWIC)
- [26] [Scaling test-time computation by implicitly reasoning in latent space](https://neurips.cc/virtual/2025/poster/117966)
- [27] [Scaling test-time computation by implicitly reasoning in latent space](https://icml.cc/virtual/2025/51856)
- [28] [Scaling Test-Time Compute: How Recurrent Depth Transforms AI Reasoning](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db)
- [29] [Sys2Bench benchmark repository](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [30] [Sys2Bench benchmark repository](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [31] [Sys2Bench benchmark repository](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [32] [Token Economics & Chain of Thought: When "Thinking" Costs More Than It's Worth](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more)
- [33] [Impact of Chain-of-Thought on token count and latency](https://aclanthology.org/2025.emnlp-main.165.pdf)
- [34] [CoT Optimization](https://www.aussieai.com/research/cot-optimization)
- [35] [Impact of Chain-of-Thought on token count and latency](https://arxiv.org/html/2406.09136v1)
- [36] [Tech Report: Chain of Thought](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought)
- [37] [Weighted Majority Voting with Process Reward Models](https://openreview.net/forum?id=l19DmXbwPK)
- [38] [VersaPRM for multi-domain reasoning](https://icml.cc/virtual/2025/oral/47195)
- [39] [SCOPE framework for test-time reinforcement learning](https://arxiv.org/html/2512.15146v1)
- [40] [Improving Mathematical Reasoning with Process Supervision](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf)
- [41] [Reward Models](https://cameronrwolfe.substack.com/p/reward-models)
- [42] [Chain of Draft](https://www.helicone.ai/blog/chain-of-draft)
- [43] [Chain of Draft](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft)
- [44] [What is Chain of Drafts?](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169)
- [45] [Move beyond Chain-of-Thought with Chain-of-Draft on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock)
- [46] [Chain of Draft: Thinking Faster by Writing Less](https://arxiv.org/html/2502.18600v1)
- [47] [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://arxiv.org/html/2503.04378v1)
- [48] [Dedicated Feedback and Edit Models Empower Inference-Time Scaling for Open-Ended General-Domain Tasks](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended)
- [61] [TRADING INFERENCE-TIME COMPUTE FOR ADVERSARIAL ROBUSTNESS.](https://arxiv.org/abs/2501.18841)
- [62] [Scaling by Thinking in Continuous Space](https://arxiv.org/abs/2502.05171)
- [63] [Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling](https://arxiv.org/abs/2502.06703)
- [64] [Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights](https://www.arxiv.org/abs/2502.12521)
- [65] [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382)
- [67] [s1: Simple test-time scaling](https://arxiv.org/abs/2501.19393)
- [68] [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- [69] [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314)
- [70] [Test-Time Preference Optimization: On-the-Fly Alignment via Iterative Textual Feedback](https://arxiv.org/abs/2501.12895)
- [71] [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)
- [72] [Inference-Time Scaling: The Next Frontier in AI Performance](https://ve3.global/blog/inference-time-scaling-the-next-frontier-in-ai-performance)
- [73] [Categories of Inference-Time Scaling Methods](https://magazine.sebastianraschka.com/p/categories-of-inference-time-scaling)
- [74] [Does More Inference-Time Compute Really Help Robustness?](https://arxiv.org/html/2507.15974v1)
- [75] [On Recent Results in LLM Latent Reasoning](https://www.lesswrong.com/posts/pLnLSgWphqDbdorgi/on-recent-results-in-llm-latent-reasoning)
- [76] [Looped Language Models: Learning to Reason with Stable Fixed-Points](https://arxiv.org/html/2605.26733v1)
- [77] [Inner Thinking Transformer: Leveraging Dynamic Depth Scaling to Foster Adaptive Internal Thinking](https://liner.com/review/inner-thinking-transformer-leveraging-dynamic-depth-scaling-to-foster-adaptive)
- [78] [LLM Inference Hardware is Emerging from the Shadows](https://gradientflow.substack.com/p/llm-inference-hardware-emerging-from)
- [79] [LLM Inference - HW/SW optimizations](https://community.juniper.net/blogs/sharada-yeluri/2024/02/20/llm-inference-hw-sw-optimizations)
</article>