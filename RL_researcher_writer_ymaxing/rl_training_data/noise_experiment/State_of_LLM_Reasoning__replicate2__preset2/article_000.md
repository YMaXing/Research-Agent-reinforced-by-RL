# The 2025 State of Inference-Time Compute Scaling

In 2025, building agentic systems that can reliably solve complex, multi-step problems is a top priority for AI engineers. The direct-answer models that dominated the past are no longer enough; we need LLMs that can reason. This has sparked a surge in research since the release of models like DeepSeek-R1, blending techniques from inference-time scaling, reinforcement learning, and supervised fine-tuning. This article provides a comprehensive survey of the latest advancements in inference-time compute scaling, a set of methods that enhance LLM reasoning without altering the model's weights. We will focus on the key papers published in this rapidly evolving field.![The four main categories of implementing reasoning models I explained in Understanding Reasoning LLMs. This article focuses on inference-time-scaling methods.](https://substackcdn.com/image/fetch/$s_!IOSP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faf9e2677-652a-4af1-9f57-dc0c253d2198_1448x1260.png)

Image 1: The four main categories of implementing reasoning models. This article focuses on inference-time-scaling methods. (Source [magazine.sebastianraschka.com [16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

We will explore how these techniques allow smaller, more efficient models to rival the performance of much larger ones, a critical trade-off for production systems. To understand how inference-time scaling fits into the broader landscape, we will first examine the four main categories of reasoning model development.

## Implementing and improving reasoning in LLMs: The four main categories

Reasoning models are a specialized class of LLMs designed to tackle complex problems by generating intermediate steps, either explicitly in their output or internally, before arriving at a final answer [[16]](httpshttps://magazine.sebastianraschka.com/p/understanding-reasoning-llms). This contrasts with standard LLMs, which typically map an input directly to an output in a single forward pass. This ability to "think" allows them to handle tasks like advanced math, puzzles, and coding challenges that are beyond the reach of direct-answer models.![Side-by-side comparison of a basic LLM's one-line answer and a reasoning LLM's explanatory response.](https://substackcdn.com/image/fetch/$s_!ZsN9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8abbfe39-f656-4845-b376-18c1e563210a_1326x564.png)

Image 2: A regular LLM may provide a short answer, whereas reasoning models typically include intermediate steps. (Source [magazine.sebastianraschka.com [16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

There are two primary ways to enhance an LLM's reasoning capabilities: increasing training compute or increasing inference compute. Training compute involves modifying the model's weights through methods like Supervised Fine-Tuning (SFT) or Reinforcement Learning (RL). This is a one-time, upfront investment. Inference compute, on the other hand, refers to the additional computational resources used at test time to improve output quality without changing the model's weights. The simplest example of this is chain-of-thought (CoT) prompting, which encourages the model to generate more tokens to "think through" a problem [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).![Accuracy improvements can be achieved through increased training or test-time compute, where test-time compute is synonymous with inference-time compute and inference-time scaling.](https://substackcdn.com/image/fetch/$s_!pgyl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fddde6f39-3b88-4962-9d02-2cf767dc82e9_1484x994.png)

Image 3: Accuracy improvements can be achieved through increased training or test-time compute. (Source [arxiv.org [49]](https://arxiv.org/abs/2502.14382))

In practice, the most effective systems often blend both approaches. Relying solely on training can lead to issues like reward hacking, where the model learns to exploit the reward function without genuinely improving its reasoning. Conversely, pure inference scaling on a weak base model yields limited gains. A well-trained model provides a strong foundation, while inference-time techniques unlock its full potential for complex tasks. This hybrid approach has given rise to four main categories for developing reasoning models [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).![Four categories of reasoning models development](https://substackcdn.com/image/fetch/$s_!_2dU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb5e5fdf9-e72c-497b-9cf4-b4e3c24f33f1_1600x591.png)

Image 4: The four main categories for developing reasoning models. (Source [magazine.sebastianraschka.com [16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

### Inference-time compute scaling

This approach focuses on improving an LLM's performance by allocating more computational resources during inference, without altering the model's parameters. It is analogous to giving a person more time to think through a difficult problem. Techniques range from simple prompt engineering, like CoT, to more complex search and voting strategies. Models like OpenAI's o1 are believed to heavily leverage inference-time scaling, which would explain their higher cost per token compared to models like DeepSeek-R1. While the DeepSeek R1 technical report noted that many explicit inference-time methods they tried were "unsuccessful," the model itself was trained to produce longer, more detailed responses. This serves as an implicit form of inference-time scaling, as generating more tokens naturally increases inference costs and time [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

### Pure reinforcement learning (RL)

This method trains a model to develop reasoning abilities from scratch using only RL, without an initial SFT stage. The DeepSeek-R1-Zero model is a prime example of this approach. It was trained using RL with rule-based rewards for accuracy and format, and surprisingly, it began to generate reasoning traces on its own—a phenomenon the researchers called an "Aha! moment." This demonstrated that reasoning can emerge as a learned behavior. However, this approach faces challenges, as it can be difficult to define reliable reward signals for all types of tasks, and it often requires significant computational resources to explore the vast solution space [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

### Reinforcement learning and supervised fine-tuning (SFT + RL)

This is the most common approach for building high-performance reasoning models and is the blueprint behind DeepSeek-R1. It combines the strengths of both SFT and RL. The process typically starts with SFT on a dataset of high-quality reasoning examples, which provides the model with a strong initial foundation. This is followed by one or more stages of RL to further refine its reasoning capabilities, often using a mix of rule-based and preference-based rewards. This hybrid approach allows the model to learn from both explicit demonstrations and its own exploration, leading to more robust and generalizable reasoning skills [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

### Supervised fine-tuning and model distillation

This category focuses on transferring the reasoning capabilities of a large, powerful model to a smaller, more efficient one. In the context of LLMs, this "distillation" typically involves instruction fine-tuning a smaller model on an SFT dataset generated by a larger teacher model. The DeepSeek-R1-Distill models were created this way, using data from the 671B DeepSeek-R1 model to train smaller Llama and Qwen models. While these distilled models are not as powerful as their teacher, they are surprisingly strong for their size and offer a cost-effective way to achieve advanced reasoning. However, this approach is limited by the capabilities of the teacher model; it can replicate existing knowledge but cannot innovate beyond it [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms).

With these four categories mapped out, we can now zoom in on the inference-time compute scaling branch, which forms the core of this article.

## Inference-time compute scaling methods

The core idea behind inference-time compute scaling is straightforward: giving a model more time to "think" can lead to better answers, much like how humans benefit from spending more time on difficult problems [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms). This concept has deep roots in AI, with historical parallels in game-playing systems like AlphaGo, which used extensive search at inference time to achieve superhuman performance [[67]](https://ve3.global/blog/inference-time-scaling-the-next-frontier-in-ai-performance). This is typically achieved by prompting the model to generate intermediate reasoning steps, which increases the number of tokens produced and, consequently, the latency and cost of each API call.![An example of classic CoT prompting from the 2022 Large Language Models are Zero-Shot Reasoners paper](https://substackcdn.com/image/fetch/$s_!Knds!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d37faa4-3261-492c-85a4-766926b8c17c_1600x419.png)

Image 5: An example of classic CoT prompting from the 2022 *Large Language Models are Zero-Shot Reasoners* paper. (Source [arxiv.org [50]](https://arxiv.org/abs/2205.11916))

Beyond simple CoT prompting, advanced techniques involve search and voting [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms). Parallel methods like majority voting generate multiple answers and choose the most frequent one to improve robustness. Sequential methods explore paths step-by-step. For instance, a Process Reward Model (PRM) can guide a beam search by scoring intermediate steps, allowing the system to prioritize promising paths while pruning others, making the search more efficient [[16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms), [[37]](https://openreview.net/forum?id=l19DmXbwPK).![Different search-based methods rely on a process-reward-based model to select the best answer. Annotated figure from the LLM Test-Time Compute paper](https://substackcdn.com/image/fetch/$s_!O9a-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5ad9742b-993f-4ecd-8f80-2fa41d43164b_1334x798.png)

Image 6: Different search-based methods rely on a process-reward-based model to select the best answer. (Source [magazine.sebastianraschka.com [16]](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms))

These methods represent different ways to allocate extra compute at inference time. We will now examine a concrete recent instantiation of these ideas in the s1 paper, which combines curated reasoning traces with explicit length-control tokens.

## s1: Simple test-time scaling

The paper *s1: Simple test-time scaling* (31 Jan, 2025) introduces a hybrid approach that combines a small, carefully curated SFT dataset with an inference-time length control mechanism [[1]](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8), [[2]](https://huggingface.co/papers/2501.19393). This distinguishes it from pure distillation methods by actively managing the model's "thinking" process at runtime. The core of the technique lies in what the authors call "budget forcing," a sequential scaling method that directly controls the length of the model's reasoning trace.

If the model attempts to conclude its reasoning prematurely, the system suppresses the end-of-thinking signal and appends a "Wait" token to the prompt. This simple intervention encourages the model to continue its analysis, often leading to self-verification and self-correction. For example, a model might initially arrive at an incorrect answer, but after being prompted to "Wait," it re-evaluates its steps and corrects the mistake. This is contrasted with simply using an end-of-thinking delimiter to cut the process short if it exceeds a certain token budget [[1]](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8).![Illustration of "wait" token insertion to control the length of the output. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/$s_!qk_K!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e7f4d94-9f8f-4353-87ad-78f3cba7b9cd_1154x854.png)

Image 7: The "s1" paper's budget forcing technique uses "Wait" tokens to encourage longer reasoning and self-correction. (Source [arxiv.org [51]](https://arxiv.org/abs/2501.19393))

The paper provides empirical evidence showing a correlation between the length of the generated response and its accuracy on reasoning benchmarks. By forcing the model to generate longer reasoning traces, the s1 method was able to improve performance on tasks like AIME24 from 50% to 57% [[2]](https://huggingface.co/papers/2501.19393). This scaling behavior, however, is not limitless; the authors note that the benefits eventually plateau as the model can get stuck in repetitive loops.![Correlation between response accuracy and length. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/$s_!kYWF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7f0c49b-a644-4142-bed0-7d114ecd39c2_798x456.png)

Image 8: The s1 paper found a correlation where longer reasoning traces often lead to higher accuracy. (Source [arxiv.org [51]](https://arxiv.org/abs/2501.19393))

Interestingly, the choice of token matters. The paper compares the effectiveness of "Wait" to a more neutral token like "Hmm" and finds that "Wait" leads to a greater improvement in accuracy (53.3% vs. 50.0% on AIME24). This suggests that the token doesn't just extend time but actively induces doubt and reconsideration, similar to the "Aha! moment" observed in DeepSeek-R1's training. The s1 paper calls for future work to compare its simple approach against more complex methods like beam search and compute-optimal search [[2]](https://huggingface.co/papers/2501.19393).!["Wait" vs "Hmm" tokens. Annotated figure from s1 paper](https://substackcdn.com/image/fetch/$s_!Qd4X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6bdfe7db-8c97-4240-8be0-11efa7abdf7c_758x510.png)

Image 9: The paper found that the "Wait" token was more effective at improving accuracy than a neutral token like "Hmm". (Source [arxiv.org [51]](https://arxiv.org/abs/2501.19393))

## Other noteworthy research papers on inference-time compute scaling

The field of inference-time compute scaling is vast and growing rapidly. While it's impractical to cover every recent publication in exhaustive detail, this section provides a high-level survey of several other noteworthy papers. Our goal is to give you a broad overview of the diverse techniques being explored, allowing you to see the breadth of the field without getting lost in repetitive details.

A common pattern you will notice is that many of these approaches are not purely prompt-based. They often blend some form of training or fine-tuning with explicit mechanisms to control inference-time compute. This is a key distinction from simple SFT or distillation methods that might incidentally produce longer outputs but lack active regulation or budgeting of compute during inference. Each of the following papers introduces a unique mechanism for managing this trade-off, offering different strategies to enhance reasoning at test time.

## Test-Time Preference Optimization

*Test-Time Preference Optimization (TPO)*, introduced in a paper from January 2025, presents a pure inference-time alignment process that avoids any changes to the underlying model weights [[3]](https://icml.cc/virtual/2025/poster/46149), [[4]](https://proceedings.mlr.press/v267/li25ac.html). It operates on a per-query basis, iteratively refining the model's output to better align with human preferences. The process follows a four-step loop: generation, scoring, critique, and refinement.

First, the model generates multiple candidate answers. A reward model scores them, selecting the best ("chosen") and worst ("rejected") options. The LLM is then prompted to generate textual critiques analyzing the chosen response's strengths and the rejected one's weaknesses. These critiques and suggestions guide the model in generating a new, refined set of responses. This loop repeats, progressively improving the output with each iteration [[3]](https://icml.cc/virtual/2025/poster/46149). However, the method's effectiveness can be limited by ambiguity in the preference data; if the "chosen" and "rejected" responses contain significant semantic overlap, the reward signal becomes noisy, which can degrade alignment performance [[68]](https://aclanthology.org/2025.emnlp-main.460.pdf).

```mermaid
flowchart LR
  Generation["Generation<br/>(multiple answers)"] --> Scoring["Scoring<br/>(reward model, chosen/rejected)"]
  Scoring --> Critique["Critique<br/>(textual critiques & suggestions)"]
  Critique --> Refinement["Refinement<br/>(update new responses)"]
  Refinement --> Generation
```

Image 10: A flowchart illustrating the four-step loop of Test-Time Preference Optimization (TPO).

## Thoughts Are All Over the Place

The paper *Thoughts Are All Over the Place* (January 2025) identifies a phenomenon in o1-like models it calls "underthinking," where frequent switching between different reasoning paths leads to a decrease in final accuracy [[5]](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme), [[6]](https://tldr.takara.ai/p/2501.18585). To address this, the authors propose a decoding strategy called Thought Switching Penalty (TIP). This method applies a penalty to the logits of tokens associated with thought transitions (e.g., "alternatively"), making it less likely for the model to prematurely abandon a promising line of reasoning.

The key advantage of TIP is that it is a pure inference-time intervention that requires no additional fine-tuning. By simply modifying the decoding process, it encourages the model to explore each reasoning path more deeply, leading to improved accuracy on challenging benchmarks [[5]](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme).![Thought Switching Penalty method visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!vvCX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7111ccaa-c4c1-4c7c-84f9-74d38df3c663_1528x894.png)

Image 11: The TIP method discourages premature thought transitions by penalizing specific tokens at inference time. (Source [arxiv.org [52]](https://arxiv.org/abs/2501.18585))

## Trading Inference-Time Compute for Adversarial Robustness

Research from OpenAI in January 2025 explores the relationship between inference compute and model safety [[7]](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf), [[8]](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness), [[9]](https://huggingface.co/papers/2501.18841). The study finds that more "thinking" time generally improves robustness against adversarial attacks, even without specific adversarial training. However, this scaling does not help when an attack exploits policy loopholes. The paper also introduces new attacks like "Think Less" and "Nerd Sniping" that target reasoning models. This research concludes that scaling inference-time compute is valuable for safety, but not a complete solution [[7]](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf).

More recent work critically examines the assumption that reasoning steps are hidden. If these steps are exposed, an "inverse scaling law" can emerge: more compute *reduces* robustness by increasing the attack surface for leaking secrets or generating malicious intermediate content [[69]](https://arxiv.org/html/2507.15974v1).![Trading Inference-Time Compute for Adversarial Robustness analysis. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!Gt2_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F704acd82-10a8-4879-9bd3-26bb67c3155f_1600x1173.png)

Image 12: Increased inference compute generally improves robustness, but new attack vectors like "Think Less" can counteract these gains. (Source [arxiv.org [53]](https://arxiv.org/abs/2501.18841))

## Chain-of-Associated-Thoughts

The *Chain-of-Associated-Thoughts (CoAT)* framework, proposed in February 2025, enhances LLM reasoning by combining Monte Carlo Tree Search (MCTS) with what the authors call an "associative memory" [[21]](https://arxiv.org/html/2502.02390v3). This memory acts as a dynamic knowledge base during inference, allowing the model to recall earlier reasoning steps and incorporate newly generated information in real-time.

By integrating the structured exploration of MCTS with this adaptive memory, the CoAT framework expands the search space and enables the model to explore diverse reasoning pathways without losing context. This synergy helps the model revisit and refine its inferences, leading to more accurate and comprehensive final outputs. The overall system is designed to provide a more systematic exploration of reasoning paths at test time [[21]](https://arxiv.org/html/2502.02390v3).![CoAT: Chain-of-Associated-Thoughts Framework visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!AtpC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5d0635fb-c0b4-45df-b8d3-b54254ab92b5_1600x777.png)

Image 13: The CoAT framework combines MCTS with an associative memory to enhance reasoning. (Source [arxiv.org [21]](https://arxiv.org/abs/2502.02390))

## Step Back to Leap Forward

The paper *Step Back to Leap Forward*, from February 2025, introduces a "self-backtracking" mechanism that teaches LLMs to recognize and correct their own suboptimal reasoning paths [[22]](https://arxiv.org/html/2502.04404v1), [[23]](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947). This is achieved by training the model to generate a special `<backtrack>` token when it identifies a flawed step in its reasoning.

During training, the model learns to associate this token with suboptimal states. Then, at inference time, it can use this learned ability to trigger a backtracking process. This allows the model to dynamically conduct a tree-based search, revisiting earlier decisions and exploring alternative reasoning trajectories. A key advantage of this approach is that it does not require an external reward model to guide the search, as the backtracking signal is internalized within the model itself. This self-correction capability allows the model to dynamically adjust its search depth and breadth, leading to more robust and flexible problem-solving [[22]](https://arxiv.org/html/2502.04404v1).![Step Back to Leap Forward: Self-Backtracking mechanism. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!e6x3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1df5fbf3-97f2-4976-b46f-2d5196b6bdc4_1594x888.png)

Image 14: The self-backtracking mechanism trains a model to recognize and correct its own errors using a special token. (Source [arxiv.org [54]](https://arxiv.org/abs/2502.04404))

## Scaling up Test-Time Compute with Latent Reasoning

A February 2025 approach scales compute by iterating in the model's latent space, not by generating more tokens [[24]](https://huggingface.co/papers/2502.05171), [[25]](https://openreview.net/forum?id=S3GhJooWIC), [[26]](https://neurips.cc/virtual/2025/poster/117966), [[27]](https://icml.cc/virtual/2025/51856), [[28]](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db). This "recurrent depth" uses a recurrent block to update its hidden state, allowing the model to "think" longer without increasing output length. This can improve performance but has a major drawback: the lack of explicit, human-readable reasoning steps makes debugging difficult, creating a trade-off between performance and transparency [[24]](https://huggingface.co/papers/2502.05171). The process continues until the latent state reaches a stable fixed point. At inference, convergence can be controlled by a KL-divergence threshold between successive states, stopping the loop when the internal representation stabilizes [[70]](https://arxiv.org/html/2605.26733v1), [[71]](https://www.lesswrong.com/posts/pLnLSgWphqDbdorgi/on-recent-results-in-llm-latent-reasoning).![Scaling up Test-Time Compute with Latent Reasoning: A Recurrent Depth Approach visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!kVPW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb82da925-5736-44ba-bed1-ea3207b06382_1516x602.png)

Image 15: Recurrent depth allows a model to "think" in its latent space without generating additional tokens. (Source [arxiv.org [55]](https://arxiv.org/abs/2502.05171))

## Can a 1B LLM Surpass a 405B LLM?

A February 2025 paper with this provocative title systematically studies the interactions between inference-time scaling, Process Reward Models (PRMs), and problem difficulty. The authors propose a "compute-optimal" scaling strategy that adapts the inference budget based on the specific PRM being used, the size of the policy model, and the complexity of the task at hand.

The key finding is that with this tailored approach, a much smaller model can achieve performance comparable to or even better than a much larger one. The paper provides compelling evidence that a 1B parameter model, when properly scaled at inference time, can outperform an unscaled 405B Llama 3 model on the same benchmarks. This has significant implications for AI engineers, as it demonstrates that the right inference strategy can allow smaller, more efficient models to rival the capabilities of their much larger counterparts, directly informing the trade-off between model size, cost, and performance [[56]](https://arxiv.org/abs/2502.06703).![Can 1B LLM Surpass a 405B LLM? Compute-optimal scaling comparison. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!DiM2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3c471e7f-36e7-41a8-a7e0-80bebf3c0f36_1600x1046.png)

Image 16: Compute-optimal scaling allows a 3B model to outperform a 405B model, and a 7B model to surpass o1 and DeepSeek-R1. (Source [arxiv.org [56]](https://arxiv.org/abs/2502.06703))

## Learning to Reason from Feedback at Test-Time

The method described in *Learning to Reason from Feedback at Test-Time* (February 2025) is challenging to classify as either a pure inference-time or training-time technique because it actually updates the model's weights during inference. The paper introduces the OpTune optimizer, which adjusts the model's weights based on its previous mistakes on a given problem.

This approach contrasts with sequential revision methods, which add failed attempts to the prompt context, and parallel sampling methods, which generate multiple independent solutions. Instead of growing the context window indefinitely, OpTune allows the model to "remember" its errors through lightweight weight updates. This enables the model to learn from its mistakes on the fly without the overhead of an ever-expanding prompt. While technically a form of test-time training, it operates at a much smaller scale than traditional fine-tuning, offering a hybrid approach that blends the adaptability of inference-time methods with the permanence of weight modification [[57]](https://www.arxiv.org/abs/2502.12521).![Learning to Reason from Feedback at Test-Time: OpTune optimizer visualization. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!nJMD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1925302-7fc2-4c7b-91e9-1c0fc4f0609e_1426x652.png)

Image 17: The OpTune optimizer updates model weights at inference time based on recent mistakes. (Source [www.arxiv.org [57]](https://www.arxiv.org/abs/2502.12521))

## Inference-Time Computations for LLM Reasoning and Planning

A February 2025 paper introduces Sys2Bench, a comprehensive benchmark for evaluating various inference-time techniques across a wide range of tasks [[29]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM), [[30]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM), [[31]](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM). The benchmark covers eleven different datasets across five categories: arithmetic, logical, commonsense, and algorithmic reasoning, as well as planning domains. The paper evaluates several popular techniques, including CoT, Tree-of-Thought, and Reasoning as Planning.

The key insight from this broad evaluation is that no single inference-time technique consistently performs best across all task types. For example, methods that excel at arithmetic reasoning may struggle with planning tasks. This finding forces engineers to move away from a one-size-fits-all approach and instead match the right inference-time method to the specific domain and problem they are trying to solve. The paper also provides a detailed analysis of the trade-offs between computational cost and performance for each technique, offering valuable guidance for practical applications [[57]](https://www.arxiv.org/abs/2502.12521).![Inference-Time Computations for LLM Reasoning and Planning benchmark results. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!Vm7j!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42115dab-1086-4035-9a64-65a83631377e_1600x1023.png)

Image 18: The Sys2Bench benchmark shows that no single inference-time technique is universally best across all reasoning tasks. (Source [www.arxiv.org [57]](https://www.arxiv.org/abs/2502.12521))

## Inner Thinking Transformer

The *Inner Thinking Transformer (ITT)*, proposed in February 2025, introduces a dynamic depth scaling mechanism that avoids using a fixed number of transformer layers for every token [[12]](https://aclanthology.org/2025.acl-long.1369.pdf), [[13]](https://arxiv.org/pdf/2502.13842), [[14]](https://arxiv.org/html/2502.13842v1), [[15]](https://www.emergentmind.com/topics/inner-thinking-transformer-itt). Its Adaptive Token Routing technique sends "difficult" tokens through the same layer multiple times, selectively increasing the inference compute budget where it is most needed. This deepens reasoning internally without lengthening the output sequence, balancing efficiency and depth [[12]](https://aclanthology.org/2025.acl-long.1369.pdf). This dynamic routing can reduce latency by focusing compute on critical tokens. For instance, a 162M parameter ITT model achieved a 1.7% performance improvement over its baseline without increasing model size [[72]](https://liner.com/review/inner-thinking-transformer-leveraging-dynamic-depth-scaling-to-foster-adaptive).![Inner Thinking Transformer: Adaptive Token Routing mechanism. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!-oC7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4a6eb47e-fcbe-4c71-8d45-e7d82ae14ba1_1414x1090.png)

Image 19: The Inner Thinking Transformer uses Adaptive Token Routing to apply more computation to difficult tokens. (Source [arxiv.org [58]](https://arxiv.org/abs/2502.13842))

## Test Time Scaling for Code Generation

The S\* method, detailed in a February 2025 paper, is a hybrid test-time scaling framework specifically designed for code generation [[49]](https://arxiv.org/abs/2502.14382). It combines the strengths of both parallel and sequential scaling to improve the quality and correctness of generated code. The framework operates in two main stages: generation and selection.![S*: Test Time Scaling for Code Generation overview. Annotated figure from the paper](https://substackcdn.com/image/fetch/$s_!quMS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F94a88f17-b4b1-4642-aeb1-6db29071ef91_972x752.png)

Image 20: The S\* framework combines parallel sampling with sequential iterative debugging for code generation. (Source [arxiv.org [49]](https://arxiv.org/abs/2502.14382))

In the generation stage, S\* starts by generating multiple candidate solutions in parallel. Each of these candidates is then refined through a sequential process of iterative debugging. The system executes the code against public test cases, and the resulting outputs and error messages are fed back to the model to guide the repair process. This loop continues until a solution passes all public tests or a maximum number of revisions is reached.

The selection stage then uses a novel technique called "adaptive input synthesis." Instead of relying on a static set of tests, the system prompts an LLM to generate new, discriminating test cases that are specifically designed to tell the difference between two candidate solutions that both pass the public tests. By executing the code against these adaptive inputs, the system can make a more robust and accurate selection. This approach, which is connected to earlier Google research on optimal test-time compute scaling, leverages execution-grounded feedback to iteratively repair and select the best possible code solution [[49]](https://arxiv.org/abs/2502.14382).

## Chain of Draft

The *Chain of Draft (CoD)* prompting technique, introduced in February 2025, is inspired by the observation that humans often rely on concise notes or drafts rather than verbose, step-by-step explanations when solving problems internally [[42]](https://www.helicone.ai/blog/chain-of-draft), [[43]](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft), [[44]](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169), [[45]](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock), [[46]](https://arxiv.org/html/2502.18600v1). Instead of prompting the model for a full natural-language reasoning trace, CoD encourages it to generate minimal yet informative intermediate steps, often in the form of equations or shorthand notation.![Chain of Draft: Thinking Faster by Writing Less comparison. Annotated figures from the paper](https://substackcdn.com/image/fetch/$s_!Gaj6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb869a967-9498-435f-85f2-a38557db14e3_1460x982.png)

Image 21: Chain of Draft produces more concise reasoning steps, reducing token usage while maintaining accuracy. (Source [arxiv.org [59]](https://arxiv.org/abs/2502.18600))

This approach offers significant efficiency gains, drastically reducing the number of tokens generated (by 68-92% in some cases) while maintaining accuracy comparable to full CoT on various reasoning benchmarks. However, this efficiency comes at a trade-off: the loss of human-readable reasoning traces. This makes it harder to debug or understand the model's thought process, forcing engineers to decide when this loss of interpretability is an acceptable price to pay for faster generation and lower costs [[42]](https://www.helicone.ai/blog/chain-of-draft).

## Better Feedback and Edit Models

Applying inference-time scaling to open-ended tasks like creative writing or high-level strategic planning is challenging because there are no easily verifiable "correct" answers. A paper from March 2025 addresses this by proposing a specialized architecture that decouples the generation, feedback, and editing processes into three distinct models [[47]](https://arxiv.org/html/2503.04378v1), [[48]](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended).

In this system, a generator model produces an initial response. A separate feedback model, trained on a large dataset of human-annotated critiques, then provides detailed, natural language feedback on the response. Finally, a dedicated edit model, also trained on human revisions, takes the original response and the feedback as input and produces an improved version. This modular approach allows each model to be highly optimized for its specific role, leading to higher-quality feedback and more effective revisions than a single model performing a generic self-critique loop could achieve. This enables iterative refinement during inference for tasks that lack a clear, objective correctness metric [[47]](https://arxiv.org/html/2503.04378v1).![Dedicated Feedback and Edit Models for Inference-Time Scaling system architecture](https://substackcdn.com/image/fetch/$s_!zA8v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73568387-83fb-4744-bd3d-f5cbcfe53f1d_1136x716.png)

Image 22: This system uses separate models for generating, providing feedback, and editing responses to improve performance on open-ended tasks. (Source [arxiv.org [60]](https://arxiv.org/abs/2503.04378))

## Conclusion

Inference-time compute scaling is shaping up to be a major research direction in 2025, primarily because it offers a way to enhance the capabilities of existing models without the need for costly and time-consuming retraining. The techniques we have surveyed—from simple "wait" tokens and budget forcing to sophisticated search algorithms, dynamic routing, and latent-space iteration—all share a common goal: to make LLMs "think" longer and more effectively.

A recurring and powerful finding across this body of research is that smaller models, when equipped with the right inference-time scaling strategy, can often rival or even exceed the performance of much larger models that lack such scaling. This has profound implications for AI engineering, as it directly impacts the trade-offs between model size, training cost, inference latency, and accuracy. For example, a project might choose a smaller, faster base model and invest the saved computational budget into a more sophisticated inference-time search strategy, achieving comparable or better results at a lower operational cost.

However, it is important to acknowledge the caveats. Increased inference-time compute directly translates to higher costs and latency, which can negatively impact the user experience in real-time applications. Furthermore, as the Sys2Bench benchmark demonstrated, there is no universally best technique; the optimal approach often depends on the specific task, model, and performance requirements. This is why we are beginning to see an industry trend toward "thinking-on-demand" toggles, which allow developers or even end-users to dynamically adjust the amount of inference compute based on the difficulty of the task at hand.![Feedback and Edit Models enable effective Inference-Time scaling across various dimensions.](https://substackcdn.com/image/fetch/$s_!nhEn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc1f749e4-4167-4013-b1c9-651c83bf8d3b_1504x756.png)

Image 23: Scaling different axes of the feedback-edit system can lead to significant performance gains on challenging benchmarks like Arena Hard. (Source [arxiv.org [60]](https://arxiv.org/abs/2503.04378))

Looking ahead, we can predict that explicit reasoning will become the default mode of operation for advanced agentic systems, rather than an optional feature. The ability to dynamically allocate computational resources to "think" more deeply about complex problems will be a defining characteristic of next-generation AI. Applications are already emerging in specialized fields; in healthcare, for instance, these techniques could be used to analyze disease progression or predict complications from new drug treatments based on their molecular structure [[73]](https://blogs.nvidia.com/blog/ai-scaling-laws).

While this article has focused on inference-time methods, the other side of the coin is, of course, train-time compute scaling. In an upcoming article, we will delve into the complementary set of techniques, including advanced reinforcement learning, hybrid RL plus SFT approaches, and distillation methods, to provide a complete picture of how reasoning models are built and refined.

## References

- [1] [https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8](https://medium.com/@jdegange85/paper-review-of-s1-simple-test-time-scaling-6094eff9c1e8)
- [2] [https://huggingface.co/papers/2501.19393](https://huggingface.co/papers/2501.19393)
- [3] [https://icml.cc/virtual/2025/poster/46149](https://icml.cc/virtual/2025/poster/46149)
- [4] [https://proceedings.mlr.press/v267/li25ac.html](https://proceedings.mlr.press/v267/li25ac.html)
- [5] [https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme](https://www.linkedin.com/pulse/thoughts-all-over-place-underthinking-o1-like-llms-vlad-bogolin-rhnme)
- [6] [https://tldr.takara.ai/p/2501.18585](https://tldr.takara.ai/p/2501.18585)
- [7] [https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf](https://cdn.openai.com/papers/trading-inference-time-compute-for-adversarial-robustness-20250121_1.pdf)
- [8] [https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness](https://openai.com/index/trading-inference-time-compute-for-adversarial-robustness)
- [9] [https://huggingface.co/papers/2501.18841](https://huggingface.co/papers/2501.18841)
- [12] [https://aclanthology.org/2025.acl-long.1369.pdf](https://aclanthology.org/2025.acl-long.1369.pdf)
- [13] [https://arxiv.org/pdf/2502.13842](https://arxiv.org/pdf/2502.13842)
- [14] [https://arxiv.org/html/2502.13842v1](https://arxiv.org/html/2502.13842v1)
- [15] [https://www.emergentmind.com/topics/inner-thinking-transformer-itt](https://www.emergentmind.com/topics/inner-thinking-transformer-itt)
- [16] [https://magazine.sebastianraschka.com/p/understanding-reasoning-llms](https://magazine.sebastianraschka.com/p/understanding-reasoning-llms)
- [21] [https://arxiv.org/html/2502.02390v3](https://arxiv.org/html/2502.02390v3)
- [22] [https://arxiv.org/html/2502.04404v1](https://arxiv.org/html/2502.04404v1)
- [23] [https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947](https://ojs.aaai.org/index.php/AAAI/article/view/39986/43947)
- [24] [https://huggingface.co/papers/2502.05171](https://huggingface.co/papers/2502.05171)
- [25] [https://openreview.net/forum?id=S3GhJooWIC](https://openreview.net/forum?id=S3GhJooWIC)
- [26] [https://neurips.cc/virtual/2025/poster/117966](https://neurips.cc/virtual/2025/poster/117966)
- [27] [https://icml.cc/virtual/2025/51856](https://icml.cc/virtual/2025/51856)
- [28] [https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db](https://medium.com/@sahin.samia/scaling-test-time-compute-how-recurrent-depth-transforms-ai-reasoning-fa866fa968db)
- [29] [https://github.com/usail-hkust/benchmark_inference_time_computation_LLM](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [30] [https://github.com/usail-hkust/benchmark_inference_time_computation_LLM](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [31] [https://github.com/usail-hkust/benchmark_inference_time_computation_LLM](https://github.com/usail-hkust/benchmark_inference_time_computation_LLM)
- [32] [https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more](https://tianpan.co/blog/2026-04-10-token-economics-chain-of-thought-when-thinking-costs-more)
- [33] [https://aclanthology.org/2025.emnlp-main.165.pdf](https://aclanthology.org/2025.emnlp-main.165.pdf)
- [34] [https://www.aussieai.com/research/cot-optimization](https://www.aussieai.com/research/cot-optimization)
- [35] [https://arxiv.org/html/2406.09136v1](https://arxiv.org/html/2406.09136v1)
- [36] [https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought](https://gail.wharton.upenn.edu/research-and-insights/tech-report-chain-of-thought)
- [37] [https://openreview.net/forum?id=l19DmXbwPK](https://openreview.net/forum?id=l19DmXbwPK)
- [38] [https://icml.cc/virtual/2025/oral/47195](https://icml.cc/virtual/2025/oral/47195)
- [39] [https://arxiv.org/html/2512.15146v1](https://arxiv.org/html/2512.15146v1)
- [40] [https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf)
- [41] [https://cameronrwolfe.substack.com/p/reward-models](https://cameronrwolfe.substack.com/p/reward-models)
- [42] [https://www.helicone.ai/blog/chain-of-draft](https://www.helicone.ai/blog/chain-of-draft)
- [43] [https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft](https://www.analyticsvidhya.com/blog/2025/03/chain-of-draft)
- [44] [https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169](https://medium.com/data-science-in-your-pocket/what-is-chain-of-drafts-bye-bye-chain-of-thoughts-76658d913169)
- [45] [https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock](https://aws.amazon.com/blogs/machine-learning/move-beyond-chain-of-thought-with-chain-of-draft-on-amazon-bedrock)
- [46] [https://arxiv.org/html/2502.18600v1](https://arxiv.org/html/2502.18600v1)
- [47] [https://arxiv.org/html/2503.04378v1](https://arxiv.org/html/2503.04378v1)
- [48] [https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended](https://liner.com/ko/review/dedicated-feedback-and-edit-models-empower-inferencetime-scaling-for-openended)
- [49] [https://arxiv.org/abs/2502.14382](https://arxiv.org/abs/2502.14382)
- [50] [https://arxiv.org/abs/2205.11916](https://arxiv.org/abs/2205.11916)
- [51] [https://arxiv.org/abs/2501.19393](https://arxiv.org/abs/2501.19393)
- [52] [https://arxiv.org/abs/2501.18585](https://arxiv.org/abs/2501.18585)
- [53] [https://arxiv.org/abs/2501.18841](https://arxiv.org/abs/2501.18841)
- [54] [https://arxiv.org/abs/2502.04404](https://arxiv.org/abs/2502.04404)
- [55] [https://arxiv.org/abs/2502.05171](https://arxiv.org/abs/2502.05171)
- [56] [https://arxiv.org/abs/2502.06703](https://arxiv.org/abs/2502.06703)
- [57] [https://www.arxiv.org/abs/2502.12521](https://www.arxiv.org/abs/2502.12521)
- [58] [https://arxiv.org/abs/2502.13842](https://arxiv.org/abs/2502.13842)
- [59] [https://arxiv.org/abs/2502.18600](https://arxiv.org/abs/2502.18600)
- [60] [https://arxiv.org/abs/2503.04378](https://arxiv.org/abs/2503.04378)
- [61] [https://arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948)
- [62] [https://arxiv.org/abs/2408.03314](https://arxiv.org/abs/2408.03314)
- [63] [https://arxiv.org/abs/2501.12895](https://arxiv.org/abs/2501.12895)
- [64] [https://arxiv.org/abs/2502.02390](https://arxiv.org/abs/2502.02390)
- [65] [https://arxiv.org/abs/2502.07191](https://arxiv.org/abs/2502.07191)
- [66] [https://www.arxiv.org/abs/2502.12521](https://www.arxiv.org/abs/2502.12521)
- [67] [https://ve3.global/blog/inference-time-scaling-the-next-frontier-in-ai-performance](https://ve3.global/blog/inference-time-scaling-the-next-frontier-in-ai-performance)
- [68] [https://aclanthology.org/2025.emnlp-main.460.pdf](https://aclanthology.org/2025.emnlp-main.460.pdf)
- [69] [https://arxiv.org/html/2507.15974v1](https://arxiv.org/html/2507.15974v1)
- [70] [https://arxiv.org/html/2605.26733v1](https://arxiv.org/html/2605.26733v1)
- [71] [https://www.lesswrong.com/posts/pLnLSgWphqDbdorgi/on-recent-results-in-llm-latent-reasoning](https://www.lesswrong.com/posts/pLnLSgWphqDbdorgi/on-recent-results-in-llm-latent-reasoning)
- [72] [https://liner.com/review/inner-thinking-transformer-leveraging-dynamic-depth-scaling-to-foster-adaptive](https://liner.com/review/inner-thinking-transformer-leveraging-dynamic-depth-scaling-to-foster-adaptive)
- [73] [https://blogs.nvidia.com/blog/ai-scaling-laws](https://blogs.nvidia.com/blog/ai-scaling-laws)